# Reproducing Ordivon Human Evidence

This is the executable entry for the current public research artifacts. It uses
only aggregate public inputs and synthetic data. No private human records are
required.

## Requirements

- Python 3.12 or a compatible Python 3 version;
- Git for checking whether generated evidence changed;
- optional shared Ordivon content tools for managed-document validation.

Run commands from the repository root.

## Aggregate China 2025 calibration

```bash
python3 research/economy/china_2025_baseline.py
git diff --exit-code -- research/economy/evidence/china-2025-baseline.json
```

Inputs are transcribed in the script from the official public release. The
result is an aggregate magnitude check. It is not a household saving rate,
individual forecast, or recommendation.

## Population-to-individual synthetic demonstration

```bash
python3 methods/m0/simulate_population_to_individual.py > /tmp/ordivon-human-population-to-individual.json
git diff --exit-code -- methods/m0/evidence/population-to-individual.json
```

The simulation demonstrates confounding, heterogeneous individual effects, and
what randomized repeated within-person observations can identify under declared
synthetic assumptions. It is not a clinical or behavioural model.

## Python integrity

```bash
python3 -m compileall -q research/economy methods/m0
```

## Managed-document validation

When the shared Ordivon Computing content tools are available:

```bash
PYTHONPATH=/path/to/ordivon-computing/packages/content-cli/src \
  python3 /path/to/ordivon-computing/scripts/ordivon_content.py \
  check --root . --mode strict
```

The Human repository intentionally does not copy the shared content tool. Its
local authority remains in the documents and evidence listed here.

## What is reproducible

- exact aggregate inputs and derived quantities;
- exact synthetic seed, data-generating process, and simulation output;
- Markdown navigation and relative links;
- current source and evidence boundaries.

## What is not established

Reproduction does not establish that the economic-autonomy framework is an
effective intervention, that composite cases are representative, or that a
specific person should take a specific action. Those claims require additional
observed evidence and appropriate local authority.
