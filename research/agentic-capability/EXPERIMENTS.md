---
schema_version: 1
id: human.agentic-capability.experiments
title: HUMAN-AI-001 Experiment Program
type: research-proposal
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
summary: Prospective and retrospective experiments for falsifying Human–Agent learning allocation, review, delegation, distillation, recovery, and synchronization policies using real Ordivon work.
evidence_status: not_applicable
readiness: READY
applies_to:
  - HUMAN-AI-001
related:
  - human.agentic-capability.current-report
  - human.agentic-capability.hypotheses
---
# HUMAN-AI-001 Experiment Program

## Research rule

Do not evaluate a Human–Agent learning policy using only the joint system output
that the policy itself optimizes. Every experiment declares the target outcome
and separates assisted performance from retained Human capability where that
distinction matters.

No experiment below has permission to infer a universal educational or
professional prescription from one person or one technical domain.

**Round 1 implementation:** [`experiments/R1-R6-ROUND-1.md`](experiments/R1-R6-ROUND-1.md)
freezes the first R1–R6 apparatus, exact case assignments, R5 retrospective
replay/prospective policies, and R6 calibration protocol. It explicitly separates
`apparatus complete` from unresolved Human or future-event endpoints.

## Shared measurement surface

Use only the dimensions required by the question, selected from:

| Measure | What it tests |
|---|---|
| assisted task quality | joint-system capability while support is available |
| time / Human attention | cost of the policy |
| unaided reconstruction | immediate retained representation |
| delayed unaided reconstruction | persistence of the representation |
| varied / novel transfer | ability to use the model outside the trained instance |
| seeded-error detection | verification capability |
| provider/tool removal recovery | intervention and recovery capability |
| confidence calibration | relation between stated belief and resolvable outcomes |
| false accept / false reject | judgment policy error profile |
| interruption count | Human attention consumed by synchronization |
| correction cost | consequence of a missed or delayed escalation |

A high score on one row does not substitute for another.

## R1 — Learning allocation and distillation

### Problem

Does invariant-focused distillation plus active reconstruction produce more
useful Human learning per unit attention than raw-history consumption or a normal
summary?

### Units

Select at least three materially different, already closed Ordivon research
results. Prefer software/system questions with bounded consequence. Freeze the
source packet before assigning a condition.

### Competing policies

- **P1 raw history:** inspect the bounded research/execution history;
- **P2 normal summary:** consume a concise result-oriented summary;
- **P3 active distillation:** consume mechanism, evidence, counterexample,
  boundary, and model delta, then reconstruct before seeing the final answer.

### Measures

Immediate unaided explanation, time, seeded-error detection, varied transfer,
and delayed reconstruction when a later checkpoint becomes available.

### Falsifier

If P3 does not materially improve transfer or verification relative to P2 at a
reasonable Human attention cost, no special promotion format is justified.

## R2 — Independent, situated, and joint capability surface

### Problem

Does a multi-condition capability surface reveal failures that assisted output
alone hides?

### Conditions

For selected technical tasks compare, where safe and feasible:

1. unaided Human attempt;
2. ordinary external references/tools;
3. Human + Agent collaboration;
4. Agent result with Human verification responsibility;
5. tool/provider removal or substitution;
6. novel variant after the original solution is hidden.

Do not treat condition 1 as the universal gold standard. It is one observation
used to locate dependence and retained substrate.

### Falsifier

Delete dimensions that fail to change any prediction, intervention, or recovery
decision across complete cases.

## R3 — Review-policy falsification

### Problem

How much of an Agent research process must Human inspect to retain reliable
control?

### Frozen packets

Use already resolved Ordivon questions whose final disposition can be hidden
from the reviewer. Each packet must preserve enough evidence to score a decision
without relying on hidden chain-of-thought.

### Policies

- **full bounded evidence review** — maximum available process/evidence;
- **selective audit** — claim, decisive evidence, rival, boundary, contradiction,
  and source independence;
- **conclusion only** — result and confidence without supporting packet.

### Measures

False accepts, false rejects, missed contradictions, review time, request for
additional evidence, and whether escalation is correctly targeted.

### Falsifier

Selective audit is rejected if it saves attention but systematically misses
high-impact errors that the bounded full review catches.

## R4 — Delegation and recovery

### Problem

What Human substrate is actually needed when the Agent or provider is wrong,
unavailable, or changed?

### Failure injections

Use only bounded, reversible technical work. Candidate perturbations:

- remove the preferred Agent/provider;
- change a tool interface;
- inject one plausible but false assumption into a review packet;
- hide an external memory artifact after a supported learning phase;
- present a materially novel task variant.

### Candidate substrate measures

Domain primitives, state reconstruction, verification procedure, ability to
form a useful question, alternative-tool navigation, and recovery time.

### Falsifier

If a retained substrate does not improve intervention/recovery enough to justify
its maintenance cost, stop treating it as a Human-core requirement.

## R5 — Timescale coordination replay

### Problem

Should Human and Agent loops synchronize every turn, on a fixed cadence, or on
meaningful evidence/state changes?

### Retrospective phase

Take several completed Host Tasks with different consequence and uncertainty.
Reconstruct a bounded sequence of semantic checkpoints without changing the
historical outcome. Label, using the later outcome, which changes actually
required Human attention and which were ordinary Agent-local convergence.

Compare three policies:

- every checkpoint;
- fixed review cadence;
- frozen event-trigger policy.

Measure interruption count, important-change recall, delay, and estimated
correction cost. The retrospective phase is hypothesis generation because labels
benefit from hindsight.

### Prospective phase

Freeze the best two policies before new Tasks run. The policy cannot be edited
in response to the evaluated outcomes. Record missed escalations and unnecessary
interruptions.

### Falsifier

Do not promote state-change triggering unless it outperforms the simpler rival
on prospective evidence.

## R6 — Calibration without bureaucracy

### Problem

For which decisions does an ex-ante forecast record improve judgment enough to
justify its cost?

### Admission

Use only repeated, resolvable uncertainties where a probability or ordered
prediction has a clear outcome. Do not log trivial everyday choices.

### Minimal record

```text
claim or event
probability / ordered confidence
one decisive reason
one condition that would change the estimate
resolution rule and date/event
```

For consequential actions add exposure and recovery boundaries.

### Measures

Calibration/Brier-style accuracy where appropriate, update magnitude after new
evidence, hindsight rewriting, and record cost.

### Falsifier

Delete the protocol from domains where it changes neither calibration nor action
and only creates monitoring overhead.

## R7 — Harness admission test

A `Human Learning Harness` is **not** an experiment premise. It becomes a
candidate implementation only if R1–R6 repeatedly expose one or more failures
that cannot be solved by existing Host checkpoints, ordinary documents,
retrieval practice, or current Harness/Runtime surfaces.

Implementation admission requires:

1. a repeated named failure;
2. an affected Human decision or retained capability;
3. a mechanism explaining why the failure persists;
4. evidence that a lighter process is insufficient;
5. a bounded data/privacy surface;
6. a deletion path;
7. an expected benefit larger than maintenance and attention cost.

If these conditions do not appear, the correct result of HUMAN-AI-001 may be a
research model and a small set of practices rather than a new subsystem.


## Evidence transport note

See [`EVIDENCE-TRANSPORT.md`](EVIDENCE-TRANSPORT.md). General Human evidence is the default starting point; Ordivon-specific experiments should target unresolved transport or system-policy questions.


**Current priority override:** the Round-1 designs above are frozen fixtures, not an execution queue. Apply the disposition in [`CONTRACTION-20260814.md`](CONTRACTION-20260814.md): external evidence first; Ordivon-specific system questions next; residual experiments only when they can change a real decision. R5 remains active, while R1/R3 fixtures and the standing R6 wave are dormant by default.
