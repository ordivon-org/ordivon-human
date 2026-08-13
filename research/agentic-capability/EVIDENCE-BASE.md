---
schema_version: 1
id: human.agentic-capability.evidence-base
title: HUMAN-AI-001 Evidence Base
type: evidence
profile: research
lifecycle: active
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - reader
  - agent
updated: 2026-08-14
summary: First bounded evidence synthesis for HUMAN-AI-001 across cognitive offloading, AI-assisted learning, human automation, capability distribution, calibration, and transfer.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-AI-001
related:
  - human.agentic-capability.current-report
  - human.agentic-capability.hypotheses
---
# HUMAN-AI-001 Evidence Base

## Scope

This is an evidence map, not a claim that the literatures below form one mature
theory of agentic Human capability. The current cycle uses them to constrain
candidate mechanisms and identify what must be measured in Human × Ordivon
dogfood.

Evidence is transported only to the structural claim its design can support.
Short laboratory tasks do not establish long-term professional deskilling;
knowledge-work field experiments do not define an education policy; one Human
case does not establish population effects.

## Evidence map

| Source | Design / population | Supports | Does not establish |
|---|---|---|---|
| Ngai & Gilbert (2026), *Metacognitive training facilitates optimal cognitive offloading*, DOI `10.1186/s41235-026-00714-0` | two controlled experiments, N=164 and N=416 | prediction + feedback can improve metacognitive calibration and reminder-choice optimality; prediction alone was ineffective in the replication | real-world cross-domain durability of the intervention |
| Goldberg & Magen (2026), *Cognitive offloading reduces internal memory processing in children*, DOI `10.1038/s41598-026-44574-6` | 40 children and 40 adults; external-store availability manipulation | external aids can remove immediate performance gaps while expected availability reduces later internal recall and reported encoding strategy use | that all external tools or AI cause long-term cognitive decline |
| Fellers & Storm (2026), *Offloading reduces prospective memory learning*, DOI `10.1037/xlm0001630` | two prospective-memory experiments | reminders can improve offloaded performance while later removal impairs the previously offloaded target | magnitude or persistence for complex professional skills |
| Kestin et al. (2025), *AI tutoring outperforms in-class active learning*, DOI `10.1038/s41598-025-97652-6` | randomized crossover experiment in an authentic physics course | a deliberately scaffolded AI tutor can produce greater measured learning gains in less median time than the comparison sessions | generic benefit from unrestricted answer-generating AI or long-term transfer |
| Liu et al. (2026), *AI Assistance Reduces Persistence and Hurts Independent Performance*, arXiv `2604.04721` | randomized controlled trials, total N=1,222 across math and reading tasks | direct AI assistance can raise immediate performance while worsening subsequent unassisted performance and persistence after brief exposure | peer-reviewed long-horizon professional deskilling; the paper is a preprint |
| Dell'Acqua et al. (2026), *Navigating the Jagged Technological Frontier*, DOI `10.1287/orsc.2025.21838` | preregistered experiment with 758 knowledge workers | AI gains are task-contingent; strong benefits appeared on in-frontier tasks while correctness fell on a selected outside-frontier task | a stable frontier for future models or a universal delegation taxonomy |
| Griffiths et al. (2024), *Operator selection for human-automation teaming*, DOI `10.1016/j.apergo.2024.104288` | simulated air-traffic-control supervision plus manual skill test | stronger manual conflict-detection skill predicted faster and more accurate automation-failure intervention | that full manual expertise is necessary or sufficient for every supervisory role |
| Parasuraman & Manzey (2010), *Complacency and bias in human use of automation*, Human Factors | review of human-automation evidence | automation bias/complacency and competing-attention risks are established human-factors concerns | a single optimal automation level for all work |
| Hutchins (1995), *How a Cockpit Remembers Its Speeds* | distributed-cognition analysis of cockpit work | useful cognitive function may be distributed across people and external representations; system capability is a legitimate unit of analysis | that individual retained skill no longer matters |
| Roediger-style test-enhanced-learning transfer literature; meta-analysis indexed under PMID `29733621` | meta-analysis across transfer tests | retrieval practice can improve transfer beyond re-exposure under many conditions | universal far transfer or benefit for every inference structure |

## Mixed evidence that blocks a universal deskilling claim

The cycle deliberately retains contradictory clinical evidence rather than using
one alarming result as a universal mechanism.

- A 2025 multicentre observational colonoscopy study (PMID `40816301`) reported
  lower unassisted adenoma-detection rates after clinicians had been exposed to
  AI assistance. Its observational before/after design cannot isolate every
  causal explanation.
- A 2026 prospective multicentre pragmatic study (PMID `42235541`) did **not**
  find a significant pre-versus-post-removal decrement after CADe exposure in
  the studied endoscopists.

The correct retained conclusion is therefore narrower: **deskilling is a
measurable failure mode, not a universal consequence of automation.** Each domain
needs removal, transfer, or intervention evidence.

## Calibration evidence

Current metacognitive and forecasting work supports a narrower mechanism than
“write confidence numbers and become better at reasoning”:

1. confidence can be systematically biased;
2. repeated predictions tied to resolving feedback can improve calibration in
   some tasks;
3. calibration improvement is distinct from object-level skill improvement;
4. the benefit may not generalize to every dimension of foresight or judgment.

This is why HUMAN-AI-001 treats confidence as one observation in an update loop,
not as a Human-quality score.

## Transfer evidence

Learning promotion requires evidence beyond familiarity. Meta-analytic and
experimental retrieval-practice work supports active recall and varied
application as useful tools for transfer, while other experiments show that
retrieval can impair particular forms of relational inference. The mechanism is
therefore conditional: active reconstruction is a stronger test than rereading,
but successful recall on the trained representation still does not prove broad
transfer.

## Evidence-to-question mapping

| Question | Strongest current constraints |
|---|---|
| A Learning allocation | offloading benefit/cost; AI tutoring versus direct-answer effects; transfer evidence |
| B Capability attribution | distributed cognition; offloading removal; assisted/unassisted AI experiments |
| C Judgment/calibration | metacognitive prediction + feedback; automation bias; jagged frontier |
| D Delegation/deskilling | human-factors failure intervention; mixed clinical deskilling evidence; jagged frontier |
| E Distillation/promotion | retrieval/transfer literature; offloading internal-memory costs |
| F Error/update/recovery | calibration feedback; separation of outcome from capability state |
| G Timescale coordination | adaptive/flexible automation evidence constrains but does not yet select a winning cadence |

## Source policy for the next round

Prefer preregistered experiments, randomized studies, longitudinal/removal tests,
field experiments, mature human-factors work, and primary studies with an
explicit intervention or failure condition. Use theory and review articles to
map mechanisms, not to inflate causal certainty.

New evidence enters only when it can change a competing hypothesis, an experiment
contract, or a decision about Human–Agent allocation.
