---
schema_version: 1
id: human.operational-concepts.hoc1.sources
title: HOC1 — Capability, Readiness and Bottleneck Evidence Ledger
profile: research
lifecycle: completed
source_role: evidence
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
updated: 2026-08-18
summary: Evidence ledger for HOC1. Primary and authoritative evidence is used to pressure capability/performance separation, state-sensitive readiness, dynamic/modifiability assessment and Human–AI supported-versus-independent performance. The sources do not establish HOC1's full operational grammar by themselves; the grammar is an Ordivon synthesis constrained by HF/HD foundations.
evidence_status: verified
readiness: READY
related:
  - human.operational-concepts.hoc1
---
# HOC1 Evidence Ledger

## 1. WHO International Classification of Functioning, Disability and Health (ICF)

Authority: World Health Organization.

Official ICF page:
https://www.who.int/standards/classifications/international-classification-of-functioning-disability-and-health

Official browser, Activities and Participation qualifiers:
https://apps.who.int/classifications/icfbrowser/Browse.aspx?code=d

Retained evidence:

```text
functioning/disability occurs in context;
environmental factors are explicit;
performance describes what a person does in the current environment;
capacity describes ability to execute a task/action under a uniform/standard environment.
```

HOC1 use:

```text
ActualContextPerformance != StandardizedCapacityEstimate
Environment/support must be explicit in capability interpretation.
```

Do not import:

```text
ICF = complete Human capability ontology
standardized capacity = independent skill by definition
```

---

## 2. Basner & Dinges — adaptive-duration PVT under sleep restriction

Mathias Basner, David F. Dinges.
`An adaptive-duration version of the PVT accurately tracks changes in psychomotor vigilance induced by sleep restriction.`
Sleep. 2012.
PMID: 22294809.
DOI: 10.5665/sleep.1620

Retained evidence:

```text
behavioral alertness is state-sensitive to sleep restriction;
brief repeated operational measurements can track a state-related performance change.
```

HOC1 use:

```text
current state can materially shift readiness;
state-sensitive evidence may expire rapidly.
```

Do not infer:

```text
PVT = global readiness
PVT = general capability
```

---

## 3. Basner, Mollicone & Dinges — brief PVT validation

Mathias Basner, Daniel Mollicone, David F. Dinges.
`Validity and Sensitivity of a Brief Psychomotor Vigilance Test (PVT-B) to Total and Partial Sleep Deprivation.`
Acta Astronautica. 2011.
PMID: 22025811.
PMCID: PMC3197786.
DOI: 10.1016/j.actaastro.2011.07.015

Design included controlled total and partial sleep-deprivation protocols.

Retained evidence:

```text
brief measures can show useful sensitivity to sleep-loss-related alertness impairment;
measurement duration/metric choice changes sensitivity.
```

HOC1 use:

```text
Readiness evidence must name the measured function and metric;
one state assay cannot stand for all capability/readiness dimensions.
```

---

## 4. Bastani et al. — generative AI performance versus later independent learning

Hamsa Bastani, Osbert Bastani, Alp Sungu, Haosen Ge, Özge Kabakcı, Rei Mariman.
`Generative AI without guardrails can harm learning: Evidence from high school mathematics.`
Proceedings of the National Academy of Sciences. 2025;122(26):e2422633122.
PMID: 40560616.
PMCID: PMC12232635.
DOI: 10.1073/pnas.2422633122

Primary randomized field experiment with nearly 1,000 high-school students.

Key pressure:

```text
GPT-supported practice performance improved substantially;
a standard GPT interface was followed by worse unassisted exam performance than control;
a guardrailed tutor mitigated the negative learning effect.
```

HOC1 use:

```text
AssistedPerformanceGain != IndependentLearningGain
Support design affects the situated→independent capability transition.
```

Do not generalize one education experiment to all AI-supported domains.

---

## 5. Bonte & Brem — dynamic learning-potential framework

Milene Bonte, Silvia Brem.
`Unraveling individual differences in learning potential: A dynamic framework for the case of reading development.`
Developmental Cognitive Neuroscience. 2024;66:101362.
PMID: 38447471.
PMCID: PMC10925938.
DOI: 10.1016/j.dcn.2024.101362

Retained pressure:

```text
static snapshots can miss meaningful individual differences in learning trajectory;
short-term dynamic learning trajectories can provide information relevant to longer-term development.
```

HOC1 use:

```text
CurrentCapabilitySurface != ModifiabilityProfile
same baseline does not imply same learning response.
```

---

# 6. Internal canonical evidence

HOC1 also consumes the already-frozen Ordivon Human research:

```text
research/h0/systems/CAPABILITY.md
research/foundations/HF5-NEED-REGULATION-RECOVERY.md
research/foundations/HF6-ADAPTATION-PLASTICITY-DEVELOPMENT.md
research/foundations/HF11-ACTION-EXECUTION-SENSORIMOTOR-CONTROL.md
research/deep-foundations/HD10-D-COGNITIVE-ABILITY-INTELLIGENCE-RIVAL-MODELS.md
research/deep-foundations/HD10-E-CROSS-DOMAIN-PERSON-DIFFERENCE-ARCHITECTURE.md
```

Durable guards inherited:

```text
SubjectiveFatigue != PerformanceDecline
PracticePerformance != RetainedLearning
Retention != Transfer
JointCapability != IndependentCapability
CurrentPerformance != Skill
BareHumanCapability != HumanToolSystemCapability
Calibration != Capability
TaskDifficulty != PersonIndependentScalar
CurrentPerformance != ModifiabilityProfile
SituatedCapability != IndependentCapability
```

---

# 7. Evidence ceiling

The external sources support specific separations and pressure tests, not the claim that one published framework already contains HOC1.

```text
HOC1
= Ordivon operational synthesis
  constrained by canonical Human Foundations
  and pressure-tested against authoritative/primary evidence.
```

`BottleneckInference` in particular is a synthesized operational object. Its causal claim must be established per case by evidence/intervention rather than by naming the construct.
