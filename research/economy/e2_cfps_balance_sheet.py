#!/usr/bin/env python3
"""Aggregate-only CFPS E2 balance-sheet and liquidity analysis.

The script never writes respondent-level records. CSV input works with the Python
standard library. Stata and Parquet inputs are supported when pandas and the
relevant reader are available, for example:

    uv run --with pandas --with pyreadstat python e2_cfps_balance_sheet.py ...

CFPS source data remain subject to the provider's data agreement and must stay
outside Git. The classifications produced here are sensitivity proxies, not
individual financial advice or exact replications of every CHFS definition.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import statistics
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_SPEC = SCRIPT_DIR / "spec" / "e2-cfps-2020-2022.json"

STATUS_ORDER = (
    "non_constrained",
    "wealthy_constrained",
    "poor_constrained",
    "unknown",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Produce disclosure-bounded aggregate E2 CFPS liquidity results."
    )
    parser.add_argument("--wave-2020", required=True, type=Path)
    parser.add_argument("--wave-2022", required=True, type=Path)
    parser.add_argument("--spec", type=Path, default=DEFAULT_SPEC)
    parser.add_argument("--weight-2020", default=None)
    parser.add_argument("--weight-2022", default=None)
    parser.add_argument("--min-cell-size", type=int, default=5)
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_records(path: Path) -> list[dict[str, Any]]:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return [dict(row) for row in csv.DictReader(handle)]
    if suffix in {".json", ".jsonl", ".ndjson"}:
        text = path.read_text(encoding="utf-8")
        if suffix == ".json":
            data = json.loads(text)
            if not isinstance(data, list):
                raise ValueError(f"JSON input must be an array of records: {path}")
            return [dict(row) for row in data]
        return [json.loads(line) for line in text.splitlines() if line.strip()]
    if suffix in {".dta", ".parquet"}:
        try:
            import pandas as pd  # type: ignore
        except ModuleNotFoundError as exc:
            raise RuntimeError(
                "Stata/Parquet input requires pandas. Run with "
                "`uv run --with pandas --with pyreadstat ...` for .dta input."
            ) from exc
        frame = pd.read_stata(path, convert_categoricals=False) if suffix == ".dta" else pd.read_parquet(path)
        return frame.to_dict(orient="records")
    raise ValueError(f"Unsupported input format: {path}")


def clean_id(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    if not text or text.lower() in {"nan", "none", "null"}:
        return None
    if text.endswith(".0") and text[:-2].isdigit():
        text = text[:-2]
    return text


def number(value: Any, *, negative_is_missing: bool = True) -> float | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return float(value)
    try:
        result = float(str(value).strip().replace(",", ""))
    except (TypeError, ValueError):
        return None
    if not math.isfinite(result):
        return None
    if negative_is_missing and result < 0:
        return None
    return result


def safe_ratio(numerator: float | None, denominator: float | None) -> float | None:
    if numerator is None or denominator is None or denominator <= 0:
        return None
    return numerator / denominator


def quantile(values: Sequence[float], q: float) -> float | None:
    clean = sorted(v for v in values if math.isfinite(v))
    if not clean:
        return None
    if len(clean) == 1:
        return clean[0]
    position = (len(clean) - 1) * q
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return clean[lower]
    weight = position - lower
    return clean[lower] * (1 - weight) + clean[upper] * weight


def weighted_quantile(pairs: Sequence[tuple[float, float]], q: float) -> float | None:
    clean = sorted((v, w) for v, w in pairs if math.isfinite(v) and math.isfinite(w) and w > 0)
    if not clean:
        return None
    total = sum(w for _, w in clean)
    target = q * total
    cumulative = 0.0
    for value, weight in clean:
        cumulative += weight
        if cumulative >= target:
            return value
    return clean[-1][0]


def distribution(values: Sequence[float], weighted_values: Sequence[tuple[float, float]]) -> dict[str, Any]:
    return {
        "valid": len(values),
        "p10": quantile(values, 0.10),
        "p25": quantile(values, 0.25),
        "median": quantile(values, 0.50),
        "p75": quantile(values, 0.75),
        "p90": quantile(values, 0.90),
        "weightedMedian": weighted_quantile(weighted_values, 0.50),
    }


def status_from(constrained: bool | None, illiquid_net: float | None) -> str:
    if constrained is None or illiquid_net is None:
        return "unknown"
    if not constrained:
        return "non_constrained"
    return "wealthy_constrained" if illiquid_net > 0 else "poor_constrained"


def derive_record(
    raw: Mapping[str, Any],
    *,
    wave: str,
    spec: Mapping[str, Any],
    weight_column: str | None,
) -> dict[str, Any]:
    wave_spec = spec["waves"][wave]
    variables = spec["variables"]

    def money(key: str, *, allow_negative: bool = False) -> float | None:
        return number(raw.get(variables[key]), negative_is_missing=not allow_negative)

    income = money("income")
    consumption = money("consumption")
    cash = money("cashDeposits")
    financial_assets = money("financialAssets")
    nonhousing_debt = money("nonHousingDebt")
    housing_debt = money("housingDebt")
    total_assets = money("netFamilyAssets", allow_negative=True)

    monthly_income = income / 12 if income is not None and income >= 0 else None
    threshold = 0.5 * monthly_income if monthly_income is not None else None
    cash_constraint = cash <= threshold if cash is not None and threshold is not None else None

    broad_net_liquidity = (
        financial_assets - nonhousing_debt
        if financial_assets is not None and nonhousing_debt is not None
        else None
    )
    broad_constraint = (
        broad_net_liquidity <= threshold
        if broad_net_liquidity is not None and threshold is not None
        else None
    )
    illiquid_net_residual = (
        total_assets - broad_net_liquidity
        if total_assets is not None and broad_net_liquidity is not None
        else None
    )

    total_debt = (
        housing_debt + nonhousing_debt
        if housing_debt is not None and nonhousing_debt is not None
        else None
    )

    weight = number(raw.get(weight_column), negative_is_missing=True) if weight_column else 1.0
    if weight is None or weight <= 0:
        weight = 1.0

    family_size = number(raw.get(wave_spec["familySize"]), negative_is_missing=True)
    housing_exp = money("housingExpenditure")

    return {
        "household_id": clean_id(raw.get(wave_spec["householdId"])),
        "panel_link_id": clean_id(raw.get(wave_spec["panelLinkId"])),
        "weight": weight,
        "income": income,
        "total_expenditure": money("totalExpenditure"),
        "consumption": consumption,
        "cash": cash,
        "financial_assets": financial_assets,
        "nonhousing_debt": nonhousing_debt,
        "housing_debt": housing_debt,
        "total_debt": total_debt,
        "net_housing_assets": money("netHousingAssets", allow_negative=True),
        "gross_housing_assets": money("grossHousingAssets"),
        "total_assets": total_assets,
        "food": money("foodExpenditure"),
        "housing_expenditure": housing_exp,
        "medical": money("medicalExpenditure"),
        "education_entertainment": money("educationEntertainmentExpenditure"),
        "transport_communication": money("transportCommunicationExpenditure"),
        "family_size": family_size,
        "monthly_income": monthly_income,
        "constraint_threshold": threshold,
        "cash_constraint": cash_constraint,
        "broad_net_liquidity": broad_net_liquidity,
        "broad_constraint": broad_constraint,
        "illiquid_net_residual": illiquid_net_residual,
        "cash_status": status_from(cash_constraint, illiquid_net_residual),
        "broad_status": status_from(broad_constraint, illiquid_net_residual),
        "cash_runway_months": safe_ratio(cash, consumption / 12 if consumption is not None else None),
        "debt_to_income": safe_ratio(total_debt, income),
        "housing_debt_to_income": safe_ratio(housing_debt, income),
        "housing_expenditure_share": safe_ratio(housing_exp, income),
        "housing_net_to_total_net": safe_ratio(
            money("netHousingAssets", allow_negative=True), total_assets
        ),
    }


def weighted_share(records: Sequence[Mapping[str, Any]], predicate: Any) -> dict[str, Any]:
    valid = [row for row in records if predicate(row) is not None]
    selected = [row for row in valid if predicate(row)]
    total_weight = sum(float(row["weight"]) for row in valid)
    selected_weight = sum(float(row["weight"]) for row in selected)
    return {
        "numerator": len(selected),
        "denominator": len(valid),
        "unweightedShare": len(selected) / len(valid) if valid else None,
        "weightedShare": selected_weight / total_weight if total_weight > 0 else None,
    }


def status_distribution(records: Sequence[Mapping[str, Any]], field: str) -> dict[str, Any]:
    counts = Counter(str(row[field]) for row in records)
    weighted = defaultdict(float)
    for row in records:
        weighted[str(row[field])] += float(row["weight"])
    total_weight = sum(weighted.values())
    return {
        status: {
            "count": counts.get(status, 0),
            "share": counts.get(status, 0) / len(records) if records else None,
            "weightedShare": weighted.get(status, 0.0) / total_weight if total_weight > 0 else None,
        }
        for status in STATUS_ORDER
    }


def wave_summary(records: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    metrics = (
        "income",
        "cash",
        "financial_assets",
        "broad_net_liquidity",
        "illiquid_net_residual",
        "total_assets",
        "total_debt",
        "consumption",
        "cash_runway_months",
        "debt_to_income",
        "housing_expenditure_share",
    )
    distributions = {}
    for metric in metrics:
        values = [float(row[metric]) for row in records if row.get(metric) is not None]
        weighted_values = [
            (float(row[metric]), float(row["weight"]))
            for row in records
            if row.get(metric) is not None
        ]
        distributions[metric] = distribution(values, weighted_values)

    required_raw = (
        "income",
        "cash",
        "financial_assets",
        "nonhousing_debt",
        "housing_debt",
        "total_assets",
        "consumption",
        "family_size",
    )
    missingness = {
        field: {
            "missing": sum(row.get(field) is None for row in records),
            "share": sum(row.get(field) is None for row in records) / len(records) if records else None,
        }
        for field in required_raw
    }

    return {
        "rows": len(records),
        "uniqueHouseholdIds": len({row["household_id"] for row in records if row["household_id"]}),
        "cashConstraint": weighted_share(records, lambda row: row["cash_constraint"]),
        "broadConstraint": weighted_share(records, lambda row: row["broad_constraint"]),
        "cashStatus": status_distribution(records, "cash_status"),
        "broadStatus": status_distribution(records, "broad_status"),
        "distributions": distributions,
        "missingness": missingness,
    }


def unique_index(records: Sequence[Mapping[str, Any]], key: str, wave: str) -> dict[str, Mapping[str, Any]]:
    index: dict[str, Mapping[str, Any]] = {}
    duplicates: list[str] = []
    for row in records:
        value = row.get(key)
        if value is None:
            continue
        text = str(value)
        if text in index:
            duplicates.append(text)
        index[text] = row
    if duplicates:
        raise ValueError(f"Duplicate {key} values in wave {wave}: {duplicates[:10]}")
    return index


def suppress_count(count: int, minimum: int) -> dict[str, Any]:
    if count < minimum:
        return {"count": None, "display": f"<{minimum}"}
    return {"count": count, "display": str(count)}


def transition_table(
    pairs: Sequence[tuple[Mapping[str, Any], Mapping[str, Any]]],
    field: str,
    minimum: int,
) -> dict[str, Any]:
    counts: Counter[tuple[str, str]] = Counter()
    weighted: defaultdict[tuple[str, str], float] = defaultdict(float)
    for before, after in pairs:
        key = (str(before[field]), str(after[field]))
        counts[key] += 1
        weighted[key] += float(before["weight"])
    total_weight = sum(weighted.values())
    rows = []
    for source in STATUS_ORDER:
        for destination in STATUS_ORDER:
            count = counts[(source, destination)]
            if count == 0:
                continue
            row = {"from": source, "to": destination, **suppress_count(count, minimum)}
            row["baselineWeightedShare"] = weighted[(source, destination)] / total_weight if total_weight > 0 else None
            rows.append(row)
    return {"cells": rows, "rawTotal": len(pairs), "suppressionThreshold": minimum}


def change_distribution(
    pairs: Sequence[tuple[Mapping[str, Any], Mapping[str, Any]]], field: str
) -> dict[str, Any]:
    changes = []
    weighted_changes = []
    for before, after in pairs:
        left, right = before.get(field), after.get(field)
        if left is None or right is None:
            continue
        change = float(right) - float(left)
        changes.append(change)
        weighted_changes.append((change, float(before["weight"])))
    return distribution(changes, weighted_changes)


def panel_summary(
    wave_2020: Sequence[Mapping[str, Any]],
    wave_2022: Sequence[Mapping[str, Any]],
    minimum: int,
) -> dict[str, Any]:
    baseline = unique_index(wave_2020, "household_id", "2020")

    followup_groups: defaultdict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for row in wave_2022:
        link = row.get("panel_link_id")
        if link is not None:
            followup_groups[str(link)].append(row)

    one_to_one_followup = {
        link: rows[0] for link, rows in followup_groups.items() if len(rows) == 1
    }
    split_links = {link: rows for link, rows in followup_groups.items() if len(rows) > 1}

    matched_ids = sorted(set(baseline) & set(one_to_one_followup))
    pairs = [(baseline[key], one_to_one_followup[key]) for key in matched_ids]

    change_fields = (
        "income",
        "cash",
        "financial_assets",
        "broad_net_liquidity",
        "total_assets",
        "total_debt",
        "consumption",
        "food",
        "housing_expenditure",
        "medical",
        "education_entertainment",
        "family_size",
    )

    return {
        "baselineHouseholds": len(baseline),
        "followupLinkedHouseholds": len(followup_groups),
        "followupRowsWithPanelLink": sum(len(rows) for rows in followup_groups.values()),
        "oneToOneFollowupLinks": len(one_to_one_followup),
        "splitHouseholdLinks": len(split_links),
        "splitFollowupRows": sum(len(rows) for rows in split_links.values()),
        "matchedOneToOneHouseholds": len(pairs),
        "baselineNotMatchedOneToOne": len(set(baseline) - set(one_to_one_followup)),
        "followupLinksWithoutBaseline": len(set(one_to_one_followup) - set(baseline)),
        "panelRule": "Primary transitions include only one-to-one 2020-to-2022 household links. Split links are reported and excluded rather than silently selected.",
        "cashStatusTransitions": transition_table(pairs, "cash_status", minimum),
        "broadStatusTransitions": transition_table(pairs, "broad_status", minimum),
        "changes": {field: change_distribution(pairs, field) for field in change_fields},
    }


def input_metadata(path: Path, records: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    return {
        "fileName": path.name,
        "sha256": file_sha256(path),
        "rowsRead": len(records),
    }


def main() -> int:
    args = parse_args()
    if args.min_cell_size < 1:
        raise ValueError("--min-cell-size must be at least 1")

    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    raw_2020 = load_records(args.wave_2020)
    raw_2022 = load_records(args.wave_2022)
    wave_2020 = [
        derive_record(row, wave="2020", spec=spec, weight_column=args.weight_2020)
        for row in raw_2020
    ]
    wave_2022 = [
        derive_record(row, wave="2022", spec=spec, weight_column=args.weight_2022)
        for row in raw_2022
    ]

    output = {
        "schemaVersion": 1,
        "kind": "ordivon-human-e2-cfps-aggregate",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "study": spec.get("study"),
        "inputs": {
            "2020": input_metadata(args.wave_2020, raw_2020),
            "2022": input_metadata(args.wave_2022, raw_2022),
            "spec": {"fileName": args.spec.name, "sha256": file_sha256(args.spec)},
        },
        "weights": {
            "2020": args.weight_2020,
            "2022": args.weight_2022,
            "note": "No candidate CFPS weight is selected automatically. Validate official household and longitudinal weights before publication.",
        },
        "definitions": spec.get("definitions"),
        "waves": {
            "2020": wave_summary(wave_2020),
            "2022": wave_summary(wave_2022),
        },
        "panel2020to2022": panel_summary(wave_2020, wave_2022, args.min_cell_size),
        "warnings": spec.get("warnings", [])
        + [
            "The output contains aggregate diagnostics only and is not individualized financial advice.",
            "Synthetic-fixture results validate code paths but are not empirical estimates.",
            "Real microdata outputs require provider-compliant access, weighting, attrition analysis, and disclosure review.",
        ],
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
