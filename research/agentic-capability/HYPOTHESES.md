---
schema_version: 1
id: human.agentic-capability.hypotheses
title: HUMAN-AI-001 Competing Hypotheses
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
summary: Competing, falsifiable hypotheses for learning allocation, capability attribution, judgment, delegation, distillation, recovery, and Human–Agent timescale coordination.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-AI-001
related:
  - human.agentic-capability.current-report
  - human.agentic-capability.experiments
---
# HUMAN-AI-001 Competing Hypotheses

This document prevents an attractive Human–Agent architecture from becoming the
answer before it earns evidence. Each axis keeps at least one rival explanation.

## Status labels

- **retained distinction** — required to avoid an already demonstrated category error;
- **supported candidate** — consistent with current evidence but not yet validated in Human × Ordivon;
- **open rival** — plausible competing explanation or policy;
- **rejected universal** — evidence is already sufficient to reject the claim as a universal rule.

## A — Learning allocation

### A1 — Stable-core allocation by future control value

**Supported candidate.** Internal learning is most valuable when knowledge has
high transfer value, is repeatedly used to verify consequential work, changes
slowly enough to amortize learning cost, or is needed to recover when external
aids fail.

**Prediction:** compared with equal-time learning of low-transfer implementation
detail, this allocation produces better delayed transfer and error detection at
similar Human study cost.

**Falsifier:** a simpler policy such as project-immediate learning produces equal
or better transfer, verification, and recovery across materially different work.

### A2 — Pure just-in-time learning

**Open rival, currently weak.** Learn only what the current task demands and
externalize everything else.

**Risk:** the learner may not possess enough prior structure to notice missing
concepts or verify a wrong Agent decomposition.

### A3 — Full internal replication of Agent competence

**Rejected universal.** Human attention and learning bandwidth are finite, many
implementation details are rapidly changing, and joint-system capability is a
legitimate outcome. This may remain locally justified for selected domains.

## B — Capability attribution

### B1 — Multi-surface capability model

**Retained distinction.** Independent, situated, joint-system, verification,
transfer, and recovery performance are not interchangeable observations.

**Prediction:** measuring at least two materially different support conditions
explains failure and transfer behavior that one assisted-output score misses.

### B2 — Unaided performance is the only real capability

**Rejected universal.** Distributed and tool-mediated cognition can produce
reliable real-world capability that is not reducible to unaided performance.

### B3 — Joint output is sufficient evidence of Human capability

**Rejected universal.** Offloading and AI assistance can raise immediate output
without establishing retained unaided performance.

## C — Judgment and calibration

### C1 — Consequence-sensitive selective audit

**Supported candidate.** Human review should concentrate on high-leverage
assumptions, evidence independence, contradictions, boundary conditions, and
irreversible or high-consequence effects rather than reproducing every Agent
step.

**Prediction:** selective audit preserves most detectable important errors with
substantially lower Human review time than full-process review.

**Falsifier:** important errors are systematically located in low-salience local
steps that selective audit misses often enough to erase its throughput benefit.

### C2 — Full Human replay

**Open rival for high consequence, rejected as universal.** Reproduce the Agent
process whenever correctness matters.

### C3 — Multi-Agent agreement as sufficient validation

**Rejected universal.** Correlated models, prompts, training data, or sources can
share the same error; agreement is not independent evidence.

## D — Delegation, leverage, and deskilling

### D1 — Retain intervention-capable substrate

**Supported candidate.** For tasks with meaningful failure consequence or slow
replacement, Human capability should remain sufficient to detect failure,
understand the relevant state, intervene or switch tools, and recover. Full
manual expert proficiency is not presumed.

**Prediction:** a bounded substrate measure predicts better recovery from Agent
or provider failure than joint-output performance alone.

**Falsifier:** substrate retention adds substantial practice cost without
improving detection, intervention, switching, or recovery in representative
failures.

### D2 — Maximal delegation

**Open rival for low-consequence, easily verified, easily replaced work.** The
optimal policy may rationally allow independent skill to decay.

### D3 — Preserve all manual skills

**Rejected universal.** Maintenance cost can exceed resilience value, and some
dependence is rational in a tool-rich environment.

## E — Distillation and promotion

### E1 — Promotion requires active reconstruction and transfer

**Supported candidate.** A compressed Agent conclusion enters the Human stable
core only after the person can reconstruct the mechanism sufficiently for its
role, apply it to a varied or novel case, and detect at least one plausible
boundary or injected error.

**Prediction:** this gate produces better later transfer and contradiction
detection than reading a normal summary for equal retained-core size.

### E2 — Cross-project repetition is enough for promotion

**Open rival, currently weak.** Repeated structures across Ordivon may indicate
an invariant but can also reflect shared architecture, prompts, or researcher
priors.

### E3 — Readable summary equals internalized knowledge

**Rejected universal.** Immediate familiarity or restatement is not evidence of
retention or transfer.

## F — Error, update, and recovery

### F1 — Lightweight ex-ante decision records improve update quality

**Supported candidate for selected decisions.** Record the hypothesis,
confidence or ordering, decisive evidence, a counterevidence condition, exposure
boundary, and review trigger before consequential uncertain actions.

**Prediction:** on resolvable repeated decisions this improves calibration,
reduces hindsight rewriting, and makes failed paths reusable at acceptable
attention cost.

**Falsifier:** recording cost and behavioral distortion exceed gains in
calibration, diagnosis, or future search.

### F2 — Record every decision

**Rejected universal.** The monitoring burden can become a metacognitive
bureaucracy with negligible information value.

### F3 — Judge decision quality from realized outcome

**Rejected universal.** Noise, execution, and environment changes separate ex
ante decision quality from one ex post result.

## G — Timescale coordination

### G1 — Evidence-triggered asynchronous coordination

**Supported candidate, not established.** Fast Agent loops run without Human
synchronization until a declared trigger occurs: goal/value change, material
contradiction, high consequence, substantial uncertainty or model delta,
promotion candidate, or recovery escalation.

**Prediction:** this reduces Human interruption while preserving detection of
important changes better than every-turn review and fixed calendar review.

**Falsifier:** important changes are missed or detected too late often enough to
produce larger correction cost than the saved attention.

### G2 — Fixed-cadence review

**Open rival.** Calendar review may outperform event triggers when changes are
hard to classify online or when accumulated weak signals matter.

### G3 — Human approval for every Agent transition

**Rejected universal.** It serializes low-risk work through the scarcest
bandwidth and defeats Agent throughput without evidence of proportional safety.

## Cross-axis invariants currently worth retaining

The first synthesis supports four cross-axis distinctions strongly enough to
use in experiments:

1. **immediate joint performance is not retained Human learning;**
2. **offloading value depends on the future availability and learning objective;**
3. **delegation policy must be task- and failure-dependent because AI capability is jagged;**
4. **calibration, object-level skill, transfer, and recovery are separate outcomes.**

Everything more specific remains defeasible.


## Post-Round-1 hypothesis contraction

The hypotheses above remain useful, but their **validation burden is reclassified**. General claims about retrieval, offloading, metacognitive feedback, automation failure, and jagged AI capability should consume the external evidence base rather than default to individual replication.

The main Ordivon-specific hypotheses now carrying empirical burden are: A1 at the **knowledge-allocation** boundary rather than a learning-format contest; C1 at the **evidence-interface** boundary; D1 through **natural recovery incidents**; E1 at the **promotion-policy** boundary; and G1 through the already frozen **timescale coordination** experiment. F1 is an optional instrument for selected resolvable decisions, not a standing forecast program.

See [`EVIDENCE-TRANSPORT.md`](EVIDENCE-TRANSPORT.md) and [`CONTRACTION-20260814.md`](CONTRACTION-20260814.md).
