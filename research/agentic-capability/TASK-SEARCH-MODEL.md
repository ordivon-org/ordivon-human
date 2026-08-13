---
schema_version: 1
id: human.agentic-capability.task-search-model
title: Problem-Space Task Model for HUMAN-AI-001
type: protocol
profile: research
lifecycle: active
source_role: supporting
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - builder
  - agent
updated: 2026-08-14
summary: A problem-first interpretation of Host Task continuity in which a Task preserves a revisable search state rather than assuming its solution in advance.
evidence_status: not_applicable
readiness: READY
applies_to:
  - HUMAN-AI-001
related:
  - human.agentic-capability.current-report
---
# Problem-Space Task Model for HUMAN-AI-001

## Problem

Research Tasks are often written as implementation verbs even when the solution
is unknown. That converts an early hypothesis into a commitment and makes failed
experiments look like wasted work instead of information about the search space.

## Decision

For HUMAN-AI-001, a research Task is a **persistent problem-search state**:

```text
Task(t) = {
  problem,
  constraints,
  established evidence,
  candidate solutions,
  current frontier,
  rejected regions,
  unresolved regions,
  next information-gain actions
}
```

The problem is intended to remain more stable than any candidate solution.
Implementation is one possible experiment inside the Task, not the Task's
identity.

## Mapping to current Host continuity

| Host WorkingCheckpoint field | Search interpretation |
|---|---|
| `objective` | stable problem and affected decision |
| `frontier` | current strongest candidate models and search edge |
| `established` | facts, constraints, or distinctions that survived current attacks |
| `unresolved` | unknown or conflicting regions |
| `rejected` | searched paths currently not worth repeating |
| `constraints` | solution-space and authority boundaries |
| `nextActions` | highest expected information-gain searches or experiments |
| checkpoint revisions | durable continuity markers; the current Agent-facing Host surface exposes the current semantic checkpoint and bounded event metadata, not arbitrary prior semantic payloads |

Host remains a continuity system, not scientific authority. Runtime remains
physical execution evidence. The Human repository owns the research claims for
this cycle.

## What failure means

A failed candidate can be a successful search result when it:

- falsifies a mechanism;
- reveals a boundary condition;
- separates two previously coupled explanations;
- demonstrates unacceptable cost or fragility;
- shows that a simpler policy is sufficient.

The candidate is then moved into the rejected region with the evidence needed to
prevent unprincipled repetition.

## Completion

Research completion is not `100%` execution of an initial plan. A Task may close
when:

1. the affected decision has a sufficiently reliable conditional answer;
2. remaining uncertainty does not change action at the current consequence level;
3. further evidence has poor expected information gain;
4. the question is narrowed or delegated to another authority;
5. the current evidence falsifies the question's assumed mechanism;
6. lawful, ethical, measurement, or resource constraints make the remaining
   search unjustified.

A later contradiction can reopen the problem with its prior search history
intact.

## Anti-patterns

Do not encode these as research Task objectives:

- “implement the solution” before alternatives are compared;
- “finish all phases” when phase numbers are only historical identifiers;
- “collect more data” without a decision-changing uncertainty;
- “build a dashboard/platform/model” because the object is technically possible;
- “prove our hypothesis” rather than exposing it to a falsifier.

This protocol is deliberately thin. It does not require a new Host schema unless
future dogfood shows that current WorkingCheckpoint semantics cannot preserve the
needed search state.
