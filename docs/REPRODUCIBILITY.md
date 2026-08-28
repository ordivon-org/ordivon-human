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

## Current combined gate

The default current gate is:

```bash
scripts/check-reproducibility
# or, including a source-copy cold start:
scripts/owner-environment cold-start
```

It replays the aggregate China calibration, the population-to-individual synthetic demonstration, the current HUMAN-AI-001 contraction projection, and the post-contraction AE1/C1 natural-evidence analysis. Each generated current receipt must remain byte-identical to the committed evidence.

The older `research/agentic-capability/experiments/validate_round.py` remains a reproducible **frozen Round-1 apparatus** but is deliberately excluded from the default current gate. Executability alone does not make a dormant experimental sequence a current Human obligation.

## Python integrity

The current executable artifacts are exercised directly by the combined gate; no separate package/runtime compilation layer is required.

## HUMAN-AI-001 contraction compatibility

The dated contraction receipt is immutable historical evidence. Current navigation
and experiment files are checked through a separate, explicitly mutable current
compatibility projection:

```bash
python3 research/agentic-capability/experiments/validate_contraction.py
git diff --exit-code -- \
  research/agentic-capability/experiments/evidence/contraction-20260814.json \
  research/agentic-capability/experiments/evidence/contraction-current.json
```

A clean diff means the current sources still contain the contracted research
markers and that the current projection is synchronized. It does not turn the
historical receipt into current evidence or establish intervention effectiveness.

## HUMAN-AI-001 AE1/C1 natural-evidence compatibility

The post-contraction structured natural-evidence analysis is current research instrumentation:

```bash
python3 research/agentic-capability/experiments/ae1-c1/analyze.py
git diff --exit-code -- \
  research/agentic-capability/experiments/evidence/ae1-c1-round1.json
```

The current receipt checks the frozen cases, two holdouts, deletion-sensitive allocation controls, and the `Claim | Evidence | Challenge | Boundary` role compression. It remains research evidence rather than a mandatory interface schema or new service/API requirement.

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
