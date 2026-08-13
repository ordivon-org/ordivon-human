---
schema_version: 1
id: human.agentic-capability.evidence-transport
title: HUMAN-AI-001 Evidence Transport Boundary
type: research-policy
profile: research
lifecycle: active
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - builder
  - agent
updated: 2026-08-14
summary: Population-level Human evidence is the default prior; Ordivon-specific experiments are reserved for transport gaps, system-policy questions, and unresolved effect heterogeneity that can change a decision.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-AI-001
---
# HUMAN-AI-001 Evidence Transport Boundary

## Default rule

Use the least specialized evidence that can resolve the question:

```text
external Human evidence
→ mechanism and moderator boundary
→ Ordivon structural transport analysis
→ natural Ordivon dogfood
→ bounded residual experiment only if still decision-relevant
```

A population result is not an exact law for every individual, but neither should a general Human mechanism be re-tested by default when the studied population, mechanism, and target outcome already transport reasonably.

## Residual-experiment admission

A new experiment is justified only when external evidence and system analysis leave competing policies that would change a real decision, and when there is a named reason that the unresolved effect may differ in the target context.

Useful reasons include a known moderator, a materially different task or support structure, repeated natural contradiction, or a consequence large enough that the remaining uncertainty matters.

Measurement availability alone is not an admission reason.

## Relationship to Methods M0

[`../../methods/m0/POPULATION-TO-INDIVIDUAL.md`](../../methods/m0/POPULATION-TO-INDIVIDUAL.md) demonstrates that population-average and individual effects can differ, while also showing that data volume alone does not create identification. The correct implication is selective transport analysis, not universal N-of-1 replication.

## Consequence for R1–R6

| Line | Post-contraction role |
|---|---|
| R1 | external learning science plus Ordivon knowledge-allocation policy; treatment comparison dormant unless a transport gap survives |
| R2 | capability accounting distinction, not a standing measurement program |
| R3 | evidence-interface and adversarial-system testing first; direct Human comparison only for unresolved interface questions |
| R4 | natural failure/recovery evidence first |
| R5 | remains active because synchronization triggers are Ordivon-specific |
| R6 | optional for selected consequential, resolvable decisions rather than a standing forecast series |

The research target is therefore `General Human science × Ordivon-specific system structure`, with residual experiments used only where they add information.
