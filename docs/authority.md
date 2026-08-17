---
schema_version: 1
id: human.authority
title: Human Content Authority
type: decision
profile: organization
lifecycle: active
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - maintainer
  - reader
  - builder
  - agent
updated: 2026-08-17
summary: Decision separating Human's mission, program state, question status, current applied answer, practice guidance, methods, ethics, supporting maps, evidence, and historical records.
evidence_status: not_applicable
readiness: READY
applies_to:
  - ordivon-human
related:
  - human.start
  - human.charter
  - human.program
  - human.questions
  - human.economy.current-report
  - human.methodology
  - human.privacy-ethics
---
# Human Content Authority

## Context

Human contains mission, program, question, report, practice, method, ethics,
system-map, evidence, closeout, code, and generated-result documents. They answer
different questions and cannot all define the current conclusion.

## Decision

- [`../README.md`](../README.md) is the reader entry and reading-path map.
- [`../CHARTER.md`](../CHARTER.md) owns mission and admission rules.
- [`RESEARCH-PROGRAM.md`](RESEARCH-PROGRAM.md) owns program state, evidence
  maturity, and reopening gates.
- [`../research/QUESTIONS.md`](../research/QUESTIONS.md) owns question status.
- [`../research/foundations/README.md`](../research/foundations/README.md) owns the Human Foundations programme entry; [`../research/foundations/HF0-PROBLEM-SPACE.md`](../research/foundations/HF0-PROBLEM-SPACE.md), [`../research/foundations/HF1-BOUNDARY-IDENTITY.md`](../research/foundations/HF1-BOUNDARY-IDENTITY.md), and [`../research/foundations/HF2-CONSCIOUSNESS-EXPERIENCE.md`](../research/foundations/HF2-CONSCIOUSNESS-EXPERIENCE.md) own the completed HF0/HF1/HF2 results respectively; and [`../research/foundations/HF2-CONTINUATION.md`](../research/foundations/HF2-CONTINUATION.md) owns the current exact foundation frontier.
- [`../research/economy/README.md`](../research/economy/README.md) owns the
  current conditional answer for `HUMAN-ECON-001`.
- [`../research/economy/PRACTICE-GUIDE.md`](../research/economy/PRACTICE-GUIDE.md)
  is an application aid and cannot override the current answer or local domain
  authority.
- [`../methods/METHODOLOGY.md`](../methods/METHODOLOGY.md) owns reusable
  inference discipline.
- [`PRIVACY-AND-ETHICS.md`](PRIVACY-AND-ETHICS.md) owns public-data and
  high-consequence limits.
- [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) owns the executable navigation for
  current public evidence; the code and generated artifacts own exact results.

## Evidence precedence

Primary sources, official documentation, analysis code, exact generated outputs,
and authorized empirical execution remain stronger owners for measurements and
calculations. Cases, closeouts, baselines, source reviews, methods studies, and
the Human System Atlas support or constrain the current answer; they do not
silently replace it.

E0–E9 are practical modules within one completed applied cycle. H0 and M0 are
lineage identifiers for supporting assets. Their numbering does not create
independent program status.

## Historical records

`E0-E9-CLOSEOUT.md`, the Human Atlas P0 closeout, Methods M0 closeout, and the
risk/continuity boundary preserve derivation and deletion decisions. Git history
preserves the former concept-first economy edition and deleted household-data
prototype. Historical instructions do not reactivate those routes.

## Consequences

A document may be useful without owning current status or conclusions. Phase
numbers, file age, confident language, and historical next steps do not override
the authority map above. New current-answer documents must state what they replace.

## Status

Accepted and active. Reopen when two managed sources claim the same current
responsibility or the project authority boundary changes.
