#!/usr/bin/env python3
"""Reproduce the descriptive 2025 China household baseline.

The input values are transcribed from the National Bureau of Statistics release:
https://www.stats.gov.cn/sj/zxfbhjd/202601/t20260119_1962321.html

The calculation intentionally uses only aggregate published values. It does not
estimate a household saving rate or any individual causal effect.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

SOURCE = {
    "publisher": "National Bureau of Statistics of China",
    "title": "2025年居民收入和消费支出情况",
    "published": "2026-01-19",
    "url": "https://www.stats.gov.cn/sj/zxfbhjd/202601/t20260119_1962321.html",
}

INPUTS: dict[str, Any] = {
    "currency": "CNY",
    "period": 2025,
    "income": {
        "national_mean": 43_377,
        "national_median": 36_231,
        "urban_mean": 56_502,
        "rural_mean": 24_456,
        "wages": 24_555,
        "business": 7_252,
        "property": 3_490,
        "transfers": 8_080,
    },
    "consumption": {
        "national_mean": 29_476,
        "urban_mean": 35_869,
        "rural_mean": 20_259,
        "food_tobacco_liquor": 8_631,
        "clothing": 1_554,
        "residence": 6_397,
        "household_facilities_services": 1_667,
        "transport_communication": 4_306,
        "education_culture_recreation": 3_489,
        "health_care": 2_573,
        "miscellaneous": 859,
    },
}


def ratio(numerator: float, denominator: float) -> float:
    if denominator == 0:
        raise ZeroDivisionError("denominator must be non-zero")
    return numerator / denominator


def calculate() -> dict[str, Any]:
    income = INPUTS["income"]
    consumption = INPUTS["consumption"]

    mean_gap = income["national_mean"] - consumption["national_mean"]
    urban_gap = income["urban_mean"] - consumption["urban_mean"]
    rural_gap = income["rural_mean"] - consumption["rural_mean"]

    derived = {
        "mean_income_minus_mean_consumption_cny": mean_gap,
        "mean_gap_share_of_mean_income": ratio(mean_gap, income["national_mean"]),
        "median_to_mean_income_ratio": ratio(
            income["national_median"], income["national_mean"]
        ),
        "urban_income_minus_consumption_cny": urban_gap,
        "urban_gap_share_of_income": ratio(urban_gap, income["urban_mean"]),
        "rural_income_minus_consumption_cny": rural_gap,
        "rural_gap_share_of_income": ratio(rural_gap, income["rural_mean"]),
        "urban_to_rural_income_ratio": ratio(
            income["urban_mean"], income["rural_mean"]
        ),
        "urban_to_rural_consumption_ratio": ratio(
            consumption["urban_mean"], consumption["rural_mean"]
        ),
        "wage_income_share": ratio(income["wages"], income["national_mean"]),
        "business_income_share": ratio(
            income["business"], income["national_mean"]
        ),
        "property_income_share": ratio(
            income["property"], income["national_mean"]
        ),
        "transfer_income_share": ratio(
            income["transfers"], income["national_mean"]
        ),
        "food_and_residence_consumption_share": ratio(
            consumption["food_tobacco_liquor"] + consumption["residence"],
            consumption["national_mean"],
        ),
        "transport_education_health_consumption_share": ratio(
            consumption["transport_communication"]
            + consumption["education_culture_recreation"]
            + consumption["health_care"],
            consumption["national_mean"],
        ),
    }

    return {
        "schemaVersion": 1,
        "source": SOURCE,
        "inputs": INPUTS,
        "derived": derived,
        "interpretationLimits": [
            "The difference between aggregate mean income and aggregate mean consumption is not a household saving rate.",
            "The release does not identify the joint household distribution of income, consumption, assets, liabilities, or liquidity.",
            "Consumption category names do not identify necessity, adjustability, life-quality value, or capability value.",
            "No causal or individual recommendation is inferred from these aggregate values.",
        ],
    }


def main() -> None:
    result = calculate()
    output = Path(__file__).with_name("evidence") / "china-2025-baseline.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(output)


if __name__ == "__main__":
    main()
