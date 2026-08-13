---
schema_version: 1
id: human.agentic-capability.current-report
title: HUMAN-AI-001 — Human Capability Under Agentic Intelligence
type: report
profile: research
lifecycle: active
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - reader
  - practitioner
  - researcher
  - builder
  - agent
updated: 2026-08-14
summary: Active problem-driven research on what humans should learn, retain, delegate, verify, and recover when agent systems can explore and iterate faster than human learning.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-AI-001
related:
  - human.questions
  - human.program
  - human.methodology
  - human.agentic-capability.hypotheses
  - human.agentic-capability.experiments
---
# HUMAN-AI-001 — Human Capability Under Agentic Intelligence

> **Status:** active research cycle. The problem is admitted and the first
> evidence synthesis is complete. Several structural findings are retained;
> allocation thresholds, synchronization rules, promotion gates, and any
> implementation remain provisional until prospective Human × Agent dogfood.

## Problem

When an Agent system can search, experiment, code, and execute much faster than a
human can learn, what should the human internalize, understand, externalize, or
delegate? How can the joint system grow while preserving enough judgment,
verification, transfer, recovery, and autonomy for ordinary failure and provider
change not to become destructive?

The wrong objective is to make Human learning run at Agent speed. The research
object is the **allocation and coordination problem across different capability
layers and timescales**.

## Why this is now an admitted Human problem

This is no longer a generic question about AI or education. Agentic work creates a
real decision pressure: the system can produce more intermediate evidence,
implementation detail, and local conclusions than one person can read or retain.
The person must decide what deserves scarce internal learning, what may remain in
recoverable external history, what can be delegated, and when a result requires
human escalation.

The cycle consumes existing H0 distinctions rather than creating a new total
model of a person:

```text
independent capability
situated capability with ordinary tools
joint Human–Agent capability
verification and intervention capability
transfer capability
recovery capability
```

## First retained findings

### 1. Joint output and retained human capability are different outcomes

A Human–Agent system can be substantially more capable than the unaided person.
That is a real system capability, not a fake result. It does not establish that
the person has internally acquired the knowledge or skill that produced the
joint output.

Therefore an evaluation that matters for learning or resilience should declare
which layer it measures instead of collapsing all performance into one score.

### 2. Cognitive offloading has both benefits and internal costs

External memory and reminders can improve task performance. Experimental work
also shows that expected external availability can reduce internal encoding and
that performance on previously offloaded prospective-memory tasks can fall when
reminders are removed. Offloading is therefore neither inherently harmful nor a
free capability gain.

A brief metacognitive intervention combining **prediction with feedback** has
also improved calibration and reminder-selection optimality in controlled
experiments. This supports training delegation choice rather than forbidding
externalization.

### 3. AI learning effects depend on the interaction policy and target outcome

Carefully scaffolded AI tutoring can improve measured learning and reduce time
on task in a bounded educational setting. Separate randomized experiments show
that easy access to complete AI answers can improve immediate performance while
reducing persistence and subsequent unassisted performance.

The relevant comparison is therefore not `AI versus no AI`. It is:

```text
interaction policy
× task
× learner state
× immediate-output objective
× retained-learning objective
```

### 4. High automation creates leverage and a failure-intervention problem

Automation can improve throughput and reduce workload. Human-factors evidence
also documents automation bias, vigilance loss, and out-of-the-loop failure
modes. In a 2024 simulated air-traffic-control experiment, better manual
conflict-detection skill predicted faster and more accurate intervention when
automation failed, while leaving substantial unexplained variance.

This rejects both extremes:

- preserve every manual skill at full independent proficiency;
- retain only abstract goals and judgment while allowing all task substrate to
  decay.

The amount of intervention-capable substrate that is worth retaining remains a
task- and consequence-dependent empirical question.

### 5. AI capability is jagged, so delegation cannot be assigned by apparent task difficulty alone

A preregistered knowledge-work experiment found large gains on tasks inside the
AI capability frontier and worse correctness on a selected task outside it.
This means apparently similar work can have opposite delegation value.

Human review policy therefore needs evidence about the actual task–Agent pair,
not a blanket category such as “analysis”, “coding”, or “creative work”.

### 6. Calibration can improve without making the underlying task ability identical

Metacognitive and forecasting research supports repeated prediction plus
resolving feedback as a way to improve calibration. Feedback can change
confidence–accuracy alignment even when it does not establish a change in the
underlying task capacity.

Human judgment should therefore be evaluated separately for:

```text
object-level correctness
confidence calibration
error detection
update behavior
intervention quality
```

### 7. Internalization needs transfer evidence, not readable summaries

Retrieval-practice research supports active reconstruction and application as
stronger evidence of retained learning than passive re-exposure. Transfer is not
universal, and retrieval can have boundary conditions.

For this cycle, a candidate Human stable-core item has not earned promotion just
because it can be restated immediately. The minimum evaluation surface is:

```text
assisted performance
unassisted reconstruction
novel or varied transfer
verification of a seeded error
recovery when an expected aid is removed
```

The exact burden depends on why the knowledge is being retained.

## Seven active problem axes

| Axis | Question | Current status |
|---|---|---|
| A — Learning allocation | What should be internalized, understood, externalized, or delegated? | active; policy not yet established |
| B — Capability attribution | How should independent, situated, joint, verification, transfer, and recovery capability be separated? | core distinctions retained; measurement under test |
| C — Judgment and calibration | How can Human judgment remain reliable without reviewing every Agent step? | active; consequence-sensitive audit is provisional |
| D — Delegation and deskilling | What distinguishes leverage, rational dependency, fragile dependency, and harmful deskilling? | active; no universal independence target |
| E — Distillation and promotion | What Agent output should enter the Human stable world model? | active; transfer-based promotion is provisional |
| F — Error, update, and recovery | How should wrong judgments become low-cost evidence rather than identity commitments? | active; lightweight protocol under test |
| G — Timescale coordination | Which Agent changes should interrupt the slower Human loop? | active; state-change triggering remains a hypothesis |

See [`HYPOTHESES.md`](HYPOTHESES.md) for competing models and
[`EXPERIMENTS.md`](EXPERIMENTS.md) for the falsification plan.

## Current candidate operating model

The following is deliberately **not** yet a retained invariant:

```text
fast Agent exploration and execution
        ↓
recoverable evidence and search history
        ↓
selective distillation
        ↓
Human reconstruction / challenge / transfer
        ↓
candidate world-model promotion
        ↓
decision, delegation, or further experiment
```

The current hypothesis is that Human and Agent loops should not be forced to run
at the same cadence. The synchronization boundary may be driven by meaningful
changes in evidence, risk, goals, contradictions, or recoverability rather than
by every Agent turn or a fixed calendar. This must be tested prospectively.

## What is explicitly not established

This cycle does **not** establish:

- a universal fraction of work that should be delegated to AI;
- a universal list of skills every person must preserve;
- a numerical Human capability score;
- a proven `Human Learning Harness` architecture;
- that AI use necessarily causes deskilling;
- that more independent ability is always preferable to greater joint capability;
- that a state-change synchronization policy is superior in every domain;
- that a short laboratory effect transports directly to long-term education or
  professional expertise.

## Search-state model

Research Tasks in this cycle are treated as problem-search states rather than
pre-solved work tickets:

```text
Problem
+ Constraints
+ Established evidence
+ Candidate solutions
+ Search frontier
+ Rejected regions
+ Unknown regions
+ Next information-gain actions
```

The problem may remain stable while candidate solutions are revised or deleted.
Failed paths remain evidence because they shrink the search space. See
[`TASK-SEARCH-MODEL.md`](TASK-SEARCH-MODEL.md).

## Evidence and next empirical burden

The first evidence base spans cognitive offloading, metacognition, AI tutoring,
human–automation teaming, knowledge-work field experiments, calibration, and
learning transfer. See [`EVIDENCE-BASE.md`](EVIDENCE-BASE.md).

The next burden is **prospectively frozen Human × Ordivon dogfood**, not another
conceptual chapter. The experiments must compare competing allocation,
distillation, review, delegation, and synchronization policies using actual
work while separating immediate joint output from retained Human capability.

## Reopening and closure

This cycle remains active while at least one of the seven problem axes contains a
decision-changing uncertainty that can be tested. A proposed mechanism is
narrowed or deleted when it adds no predictive, transfer, recovery, or decision
value over a simpler policy.

The cycle can close without implementing a new platform. A `Human Learning
Harness` is admitted only if repeated experiments expose a persistent problem
that existing Human, Host, Harness, and ordinary learning tools cannot solve at
lower cost.
