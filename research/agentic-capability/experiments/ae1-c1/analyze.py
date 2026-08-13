#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
EVIDENCE = HERE.parent / "evidence" / "ae1-c1-round1.json"


def load(name: str) -> dict:
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def gate(case: dict) -> bool:
    p = case["promotion"]
    return all(
        p[key]
        for key in (
            "support_maturity_established",
            "boundary_or_falsifier_explicit",
            "implementation_independent_representation",
        )
    )


def classify(case: dict) -> str:
    # Minimal AE1 rule after choosing the representation granularity first.
    if case["controlValue"] == "low":
        return "external_only"
    if case["durability"] == "low":
        return "locator"
    if case["durability"] == "high" and case["controlValue"] == "high" and gate(case):
        return "stable_core"
    return "mechanism"


def classify_without_durability(case: dict) -> str:
    if case["controlValue"] == "low":
        return "external_only"
    if case["controlValue"] == "high" and gate(case):
        return "stable_core"
    return "mechanism"


def classify_without_control(case: dict) -> str:
    if case["durability"] == "low":
        return "locator"
    if case["durability"] == "high" and gate(case):
        return "stable_core"
    return "mechanism"


def classify_without_gate(case: dict) -> str:
    if case["controlValue"] == "low":
        return "external_only"
    if case["durability"] == "low":
        return "locator"
    if case["durability"] == "high" and case["controlValue"] == "high":
        return "stable_core"
    return "mechanism"


def mismatches(cases: list[dict], fn) -> list[str]:
    return [c["id"] for c in cases if fn(c) != c["expectedAllocation"]]


def main() -> None:
    knowledge = load("knowledge-cases.json")
    interface = load("interface-cases.json")
    holdout = load("holdout-cases.json")
    placement = load("interface-placement.json")
    kcases = knowledge["cases"]
    icases = interface["cases"]
    hkcases = holdout["knowledgeCases"]
    hicases = holdout["interfaceCases"]

    ids = [c["id"] for c in kcases] + [c["id"] for c in icases]
    assert len(ids) == len(set(ids)), "duplicate case id"

    baseline_mismatches = mismatches(kcases, classify)
    assert not baseline_mismatches, baseline_mismatches
    holdout_mismatches = mismatches(hkcases, classify)
    assert not holdout_mismatches, holdout_mismatches

    ablations = {
        "withoutDurability": mismatches(kcases, classify_without_durability),
        "withoutControlValue": mismatches(kcases, classify_without_control),
        "withoutPromotionGate": mismatches(kcases, classify_without_gate),
    }
    for name, failed in ablations.items():
        assert failed, f"{name} produced no falsifier"

    by_task: dict[str, set[str]] = defaultdict(set)
    for case in kcases:
        by_task[case["source"]["taskId"]].add(case["expectedAllocation"])
    multi_class_tasks = {
        task: sorted(classes)
        for task, classes in by_task.items()
        if len(classes) > 1
    }
    assert multi_class_tasks, "task-level classification was not falsified"

    expected_roles = {"claim", "evidence", "challenge", "boundary"}
    role_witnesses: dict[str, list[str]] = {role: [] for role in sorted(expected_roles)}
    for case in icases:
        roles = set(case["requiredRoles"])
        assert roles <= expected_roles
        for role in roles:
            role_witnesses[role].append(case["id"])
    for role, witnesses in role_witnesses.items():
        assert witnesses, f"no deletion witness for {role}"
    for case in hicases:
        assert set(case["requiredRoles"]) == expected_roles, case["id"]

    placement_by_case = {item["caseId"]: item["provider"] for item in placement["placements"]}
    expected_case_ids = {case["id"] for case in icases + hicases}
    assert set(placement_by_case) == expected_case_ids, "boundary placement coverage must be exact"
    assert set(placement_by_case.values()) <= set(placement["allowedProviders"])
    assert placement["newLocalBoundaryFieldRequired"] is False

    mapping = interface["compressedRoles"]
    mapped_fields = list(itertools.chain.from_iterable(mapping.values()))
    assert sorted(mapped_fields) == sorted(interface["candidateFields"]), "candidate field mapping must be exact"
    assert set(mapping) == expected_roles

    conditional_prefixes = Counter()
    for case in icases:
        for attribute in case.get("conditionalAttributes", []):
            conditional_prefixes[attribute.split(".", 1)[0]] += 1

    # All historical discrepancy cases in this frozen suite need a boundary role.
    three_role_only_failures = [
        case["id"] for case in icases if "boundary" in case["requiredRoles"]
    ]
    assert three_role_only_failures

    result = {
        "schemaVersion": 1,
        "kind": "human-ai-ae1-c1-round1-analysis",
        "ae1": {
            "caseCount": len(kcases),
            "allocationCounts": dict(Counter(c["expectedAllocation"] for c in kcases)),
            "baselineMismatches": baseline_mismatches,
            "holdoutCaseCount": len(hkcases),
            "holdoutMismatches": holdout_mismatches,
            "ablationMismatches": ablations,
            "multiClassSourceTasks": multi_class_tasks,
            "minimalAllocationModel": {
                "step0": "choose representation granularity before classifying knowledge",
                "axes": ["durability", "future_control_value"],
                "separateGate": "promotion_evidence_gate",
                "notIndependentTopLevelAxes": [
                    "recurrence",
                    "transfer",
                    "verification_leverage",
                    "recovery_leverage",
                    "external_retrievability",
                    "learning_cost",
                ],
                "interpretation": "recurrence/transfer/verification/recovery are evidence for control value or promotion maturity; retrievability/currentness helps choose representation granularity; learning cost schedules attention but does not determine semantic destination",
            },
        },
        "c1": {
            "caseCount": len(icases),
            "candidateFieldCount": len(interface["candidateFields"]),
            "compressedRoleCount": len(mapping),
            "roles": sorted(mapping),
            "roleDeletionWitnesses": role_witnesses,
            "conditionalAttributeFamilies": dict(conditional_prefixes),
            "claimEvidenceChallengeWithoutBoundaryFailures": three_role_only_failures,
            "interpretation": "claim/evidence/challenge/boundary are semantic roles, not a mandate for four new top-level fields; roles may be satisfied by existing owner/Run contracts and exact references",
        },
        "sourceDigests": {
            "knowledge-cases.json": digest(HERE / "knowledge-cases.json"),
            "interface-cases.json": digest(HERE / "interface-cases.json"),
            "holdout-cases.json": digest(HERE / "holdout-cases.json"),
        },
    }

    EVIDENCE.parent.mkdir(parents=True, exist_ok=True)
    EVIDENCE.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
