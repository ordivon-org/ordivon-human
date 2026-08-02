# Methods M0 — Measurement and Inference Foundations

**Status: completed on 2026-08-02. Reclassified from the original H0 during P0 correction.**

M0 tested how Ordivon Human should distinguish state, context, action, observation, causal scope, population evidence, individual evidence, and human–AI capability claims. It is methodological support for Human research; it is not the Human System Map itself.

## Result

H0 selects the first exit outcome from Issue #1:

> Retain a smaller evidence-backed model.

The initial ten-level hierarchy is not retained. It mixed state domains, actions, context, time, measurement, and study-specific causal roles in one list. The retained model separates them instead.

## Evidence

- [`FRAMEWORK-COMPOSITION.md`](FRAMEWORK-COMPOSITION.md) — comparison against WHO ICF, NIMH RDoC, OECD well-being, All of Us, UK Biobank, life-course research, within-person methods, N-of-1 trials, and human–AI experiments;
- [`MODEL-DELETION.md`](MODEL-DELETION.md) — five case-based deletion tests and the smaller retained model;
- [`POPULATION-TO-INDIVIDUAL.md`](POPULATION-TO-INDIVIDUAL.md) — synthetic demonstration separating observational association, population average effect, and individual effects;
- [`HUMAN-AI-CAPABILITY-TRANSFER.md`](HUMAN-AI-CAPABILITY-TRANSFER.md) — minimum evidence contract for distinguishing output, joint-system performance, retained human capability, and agency;
- [`evidence/population-to-individual.json`](evidence/population-to-individual.json) — deterministic simulation result;
- [`simulate_population_to_individual.py`](simulate_population_to_individual.py) — standard-library reproduction script;
- [`SOURCES.md`](SOURCES.md) — primary and official sources used by H0;
- [`CLOSEOUT.md`](CLOSEOUT.md) — final judgment, deletions, limits, and next frontier.

## What H0 did not create

H0 created no collector, service, database, dashboard, universal schema, personal score, medical system, persistent profile, or public human dataset.

The only executable artifact is one synthetic causal simulation. It exists because a concrete population-to-individual inference failure is difficult to demonstrate precisely in prose alone.
