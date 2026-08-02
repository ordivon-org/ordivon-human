#!/usr/bin/env python3
"""Reproducible H0 simulation for population-to-individual inference.

This is a synthetic causal demonstration, not a model of any real person or
clinical intervention. It uses only the Python standard library.
"""

from __future__ import annotations

import json
import math
import random
import statistics
from pathlib import Path
from typing import Iterable

SEED = 20260802
POPULATION_SIZE = 5000
TRIAL_REPLICATES = 400
TRIAL_PERIODS = 96
OUTPUT = Path(__file__).parent / "evidence" / "population-to-individual.json"


def logistic(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-value))


def mean(values: Iterable[float]) -> float:
    return statistics.fmean(values)


def quantile(values: list[float], probability: float) -> float:
    ordered = sorted(values)
    index = probability * (len(ordered) - 1)
    lower = math.floor(index)
    upper = math.ceil(index)
    if lower == upper:
        return ordered[lower]
    weight = index - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def solve_linear_system(matrix: list[list[float]], vector: list[float]) -> list[float]:
    """Solve Ax=b with partial-pivot Gauss-Jordan elimination."""
    n = len(vector)
    augmented = [row[:] + [vector[i]] for i, row in enumerate(matrix)]
    for column in range(n):
        pivot = max(range(column, n), key=lambda row: abs(augmented[row][column]))
        if abs(augmented[pivot][column]) < 1e-12:
            raise ValueError("singular design matrix")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        divisor = augmented[column][column]
        augmented[column] = [value / divisor for value in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                current - factor * reference
                for current, reference in zip(augmented[row], augmented[column], strict=True)
            ]
    return [augmented[row][-1] for row in range(n)]


def ordinary_least_squares(design: list[list[float]], outcome: list[float]) -> list[float]:
    columns = len(design[0])
    xtx = [[0.0 for _ in range(columns)] for _ in range(columns)]
    xty = [0.0 for _ in range(columns)]
    for row, observed in zip(design, outcome, strict=True):
        for i in range(columns):
            xty[i] += row[i] * observed
            for j in range(columns):
                xtx[i][j] += row[i] * row[j]
    return solve_linear_system(xtx, xty)


def treatment_effect(baseline_capability: float, latent_stress: float) -> float:
    return 0.4 + 0.5 * baseline_capability - 0.3 * latent_stress


def simulate_population() -> dict[str, float | int]:
    rng = random.Random(SEED)
    records: list[tuple[int, float, float]] = []
    true_effects: list[float] = []
    for _ in range(POPULATION_SIZE):
        capability = rng.gauss(0.0, 1.0)
        stress = rng.gauss(0.0, 1.0)
        probability = logistic(-0.2 - capability + 0.6 * stress)
        treated = 1 if rng.random() < probability else 0
        effect = treatment_effect(capability, stress)
        outcome = capability + 0.7 * stress + treated * effect + rng.gauss(0.0, 0.8)
        records.append((treated, outcome, effect))
        true_effects.append(effect)

    treated_outcomes = [outcome for treated, outcome, _ in records if treated]
    untreated_outcomes = [outcome for treated, outcome, _ in records if not treated]
    return {
        "population_size": POPULATION_SIZE,
        "treated_fraction": mean(treated for treated, _, _ in records),
        "naive_observational_difference": mean(treated_outcomes) - mean(untreated_outcomes),
        "true_average_treatment_effect": mean(true_effects),
        "effect_standard_deviation": statistics.pstdev(true_effects),
        "negative_effect_fraction": mean(effect < 0.0 for effect in true_effects),
    }


def one_randomized_trial(seed: int, capability: float, stress: float) -> float:
    rng = random.Random(seed)
    effect = treatment_effect(capability, stress)
    prior_treatment = 0
    serial_error = 0.0
    design: list[list[float]] = []
    outcome: list[float] = []

    for period in range(TRIAL_PERIODS):
        treatment = 1 if rng.random() < 0.5 else 0
        external_event = 1 if 35 <= period < 50 else 0
        serial_error = 0.35 * serial_error + rng.gauss(0.0, 0.6)
        observed = (
            1.2
            + 0.004 * period
            + effect * treatment
            + 0.18 * prior_treatment
            - 0.3 * external_event
            + serial_error
        )
        design.append([1.0, float(treatment), float(prior_treatment), float(period), float(external_event)])
        outcome.append(observed)
        prior_treatment = treatment

    coefficients = ordinary_least_squares(design, outcome)
    return coefficients[1]


def simulate_target(name: str, capability: float, stress: float, seed_offset: int) -> dict[str, object]:
    true_effect = treatment_effect(capability, stress)
    estimates = [
        one_randomized_trial(SEED + seed_offset + replicate, capability, stress)
        for replicate in range(TRIAL_REPLICATES)
    ]
    estimate_mean = mean(estimates)
    return {
        "name": name,
        "baseline_capability": capability,
        "latent_stress": stress,
        "true_individual_effect": true_effect,
        "trial_periods": TRIAL_PERIODS,
        "replicates": TRIAL_REPLICATES,
        "mean_estimated_effect": estimate_mean,
        "estimate_bias": estimate_mean - true_effect,
        "estimate_standard_deviation": statistics.pstdev(estimates),
        "central_95_percent_simulation_interval": [
            quantile(estimates, 0.025),
            quantile(estimates, 0.975),
        ],
    }


def main() -> None:
    population = simulate_population()
    targets = [
        simulate_target("target-benefit", capability=1.0, stress=-0.5, seed_offset=10_000),
        simulate_target("target-harm", capability=-1.0, stress=0.7, seed_offset=20_000),
    ]

    assert population["naive_observational_difference"] < -0.2
    assert population["true_average_treatment_effect"] > 0.2
    assert targets[0]["true_individual_effect"] > 0.5
    assert targets[1]["true_individual_effect"] < 0.0
    assert abs(targets[0]["estimate_bias"]) < 0.05
    assert abs(targets[1]["estimate_bias"]) < 0.05

    result = {
        "schema_version": 1,
        "kind": "ordivon-human-h0-population-to-individual-simulation",
        "seed": SEED,
        "scope": "synthetic methodological demonstration; not a human or clinical model",
        "data_generating_process": {
            "observational_treatment_selection": "depends on baseline capability and latent stress",
            "individual_effect": "0.4 + 0.5 * baseline_capability - 0.3 * latent_stress",
            "n_of_1_assignment": "independent randomized treatment each period",
            "n_of_1_adjustment": ["linear time trend", "prior-period carryover", "external event window"],
        },
        "population": population,
        "targets": targets,
        "interpretation": [
            "The observational group difference has the opposite sign from the true population average effect because treatment selection is confounded.",
            "The positive population average does not determine either target: one benefits substantially and one is harmed.",
            "Repeated randomized within-person observations recover each target effect under the declared synthetic assumptions.",
            "Randomization and modeling assumptions, not personal data volume alone, create identification.",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
