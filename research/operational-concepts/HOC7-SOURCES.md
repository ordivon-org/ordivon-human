---
schema_version: 1
id: human.operational-concepts.hoc7.sources
title: HOC7 — Health, Functioning, Personal Baseline, Reserve and Risk Trajectory Evidence Ledger
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
summary: Evidence ledger for HOC7. Authoritative WHO ICF/WHODAS materials, the FDA–NIH BEST biomarker taxonomy, and primary longitudinal research on patient-specific hematological setpoints are used to pressure functioning-in-context, disability/environment interaction, biomarker context-of-use distinctions, risk/diagnostic/prognostic separation and personal-baseline interpretation. HOC7 remains a non-diagnostic Ordivon operational synthesis and does not substitute these sources for disease-specific clinical standards.
evidence_status: verified
readiness: READY
related:
  - human.operational-concepts.hoc7
---
# HOC7 Evidence Ledger

## 1. WHO — International Classification of Functioning, Disability and Health (ICF)

Official WHO resource:
https://www.who.int/standards/classifications/international-classification-of-functioning-disability-and-health

WHO describes ICF as a classification/terminology of health and health-related domains and explicitly includes environmental factors because functioning/disability occurs in context.

HOC7 use:

```text
Functioning is context-sensitive.
Disability experience cannot be inferred from diagnosis/impairment alone.
Environment/support remain first-class.
```

HOC7 does not import ICF as the complete Ordivon Human ontology.

---

## 2. WHO — WHODAS 2.0

Official WHO resource:
https://www.who.int/standards/classifications/international-classification-of-functioning-disability-and-health/who-disability-assessment-schedule

WHODAS 2.0 is grounded in ICF and assesses functioning across major life domains, including cognition, mobility, self-care, getting along, life activities and participation.

HOC7 use:

```text
FunctionalStatus can be measured across multiple life/activity domains.
Functioning != diagnosis list.
```

HOC7 does not freeze WHODAS as a mandatory Ordivon instrument.

---

## 3. WHO — Disability and Health

Official WHO resource:
https://www.who.int/news-room/fact-sheets/detail/disability-and-health

WHO describes disability as arising through interaction between health conditions and environmental/personal factors and emphasizes environmental barriers and inequities.

HOC7 use:

```text
Disease != Disability
SameCondition != SameDisabilityExperience
ParticipationContext matters.
```

---

## 4. FDA–NIH BEST Resource — biomarker taxonomy

FDA–NIH Biomarker Working Group.
`BEST (Biomarkers, EndpointS, and other Tools) Resource.`
NCBI Bookshelf / FDA / NIH, living glossary, last major listed glossary revision 2025.

Main resource:
https://www.ncbi.nlm.nih.gov/books/NBK326791/
Glossary:
https://www.ncbi.nlm.nih.gov/books/NBK338448/

The glossary defines biomarker as a measured characteristic indicating normal biological processes, pathogenic processes or responses to exposure/intervention and explicitly distinguishes biomarkers from measures of how an individual feels, functions or survives.

It separates categories including:

```text
susceptibility/risk
diagnostic
monitoring
prognostic
predictive
response
safety
```

HOC7 use:

```text
Biomarker != ClinicalOutcomeTotality
ContextOfUse matters.
Risk/diagnostic/prognostic/predictive evidence must remain distinct.
```

---

## 5. FDA–NIH BEST — diagnostic biomarker

https://www.ncbi.nlm.nih.gov/books/NBK402285/

Diagnostic biomarkers are used to detect/confirm a disease or condition or identify a subtype under a declared context of use.

HOC7 use:

```text
DiagnosticBiomarkerRole is typed.
One measurement outside an unspecified reference range is not automatically a diagnosis.
```

---

## 6. FDA–NIH BEST — monitoring biomarker

https://www.ncbi.nlm.nih.gov/books/NBK402282/

Monitoring biomarkers are measured repeatedly to assess disease/condition status or evidence of exposure/response.

HOC7 use:

```text
Repeated measurement can support trajectory monitoring.
MarkerChange != WholeFunction/OutcomeChange by identity.
```

---

## 7. FDA–NIH BEST — susceptibility/risk and prognostic biomarkers

Risk:
https://www.ncbi.nlm.nih.gov/books/NBK402288/

Prognostic:
https://www.ncbi.nlm.nih.gov/books/NBK402289/

BEST separates susceptibility/risk biomarkers for likelihood of developing a condition in someone without clinically apparent disease from prognostic biomarkers for likelihood of clinical events/progression in someone with the condition of interest.

HOC7 use:

```text
RiskEstimate != CurrentDiagnosis
SusceptibilityRisk != PrognosticRisk
```

---

## 8. FDA–NIH BEST — prognostic versus predictive

https://www.ncbi.nlm.nih.gov/books/NBK402284/

BEST distinguishes prognosis of future clinical course from a predictive biomarker's role in identifying differential favorable/unfavorable effects of exposure to an intervention.

HOC7 use:

```text
BadPrognosis != EvidenceTreatmentXWillHelp
PrognosticEvidence != PredictiveTreatmentEffectEvidence
```

---

## 9. Foy et al. 2025 — patient-specific hematological setpoints

Brody H. Foy et al.
`Haematological setpoints are a stable and patient-specific deep phenotype.`
Nature 637, 430–438 (2025).
DOI: 10.1038/s41586-024-08264-5
PMID: 39663453.

Nature:
https://www.nature.com/articles/s41586-024-08264-5
PubMed:
https://pubmed.ncbi.nlm.nih.gov/39663453/

Retained pressure:

```text
routine CBC indices in studied healthy adults showed stable person-specific setpoints over long periods;
patient-specific setpoints supported personalized reference intervals and improved interpretation for some conditions in retrospective analyses.
```

HOC7 use:

```text
PopulationReference != PersonalBaseline
WithinPopulationRange != NoMeaningfulWithinPersonChange
```

Transport ceiling:

```text
CBC-specific longitudinal stability
!= universal stable personal baseline for every biomarker/function.
```

---

# 10. Internal canonical evidence

HOC7 consumes:

```text
HD9 — organismic systems, health/disease/pathophysiology, biomarker/risk/diagnosis/recovery/multimorbidity boundaries
HF5 — state regulation/stress/fatigue/recovery
HF6 — adaptation/resilience/development
HF11 — capability/tool support
HF14–17 — welfare/rights/responsibility/governance boundaries
HD10 — person-specific projections/baselines
HOC1 — capability/readiness/bottleneck
HOC2 — evidence/calibration/verification
HOC3 — learning/modifiability/support dependence
HOC4 — state/load/recovery/personal baseline/reserve
HOC5 — goals/agency
HOC6 — care/coordination/role/authority handoffs
```

Inherited hard guards include:

```text
Health != NoDiagnosis != StatisticalAverage != WelfareTotality
Disease != Symptom != Sign != Biomarker != Diagnosis
Biomarker != Mechanism
RiskFactor != Cause
TreatmentResponse != MechanismProof
CurrentFunction != Reserve
SymptomsResolved != FullRecovery
PopulationReference != PersonalBaseline
PersonalBaseline != ImmutableSetpoint
Capability != BiologicalHealth
Disease != Disability
FutureRisk != CurrentStateSeverity
ScreenPositive != DiseaseConfirmed
```

---

# 11. Evidence ceiling

The external sources support structural distinctions and a limited set of empirical claims.
They do not supply disease-specific diagnostic/treatment rules for HOC7.

```text
HOC7
= non-diagnostic Ordivon operational synthesis
  + authoritative terminology/measurement boundaries
  + scoped longitudinal baseline evidence
  + explicit clinical-ownership firewall.
```

Any concrete consumer dealing with diagnosis, emergency triage, treatment or clinical risk must bind to validated domain-specific standards and legitimate professional/organizational authority rather than treating HOC7 labels as clinical rules.
