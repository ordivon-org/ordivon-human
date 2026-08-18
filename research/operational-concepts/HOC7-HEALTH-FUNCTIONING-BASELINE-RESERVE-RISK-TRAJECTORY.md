---
schema_version: 1
id: human.operational-concepts.hoc7
title: HOC7 — Health, Functioning, Personal Baseline, Reserve and Risk Trajectory
profile: research
lifecycle: completed
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
  - engineer
updated: 2026-08-18
summary: Reconstructs a non-diagnostic operational health/functioning layer downstream of HD9 and HOC1–HOC6. HOC7 separates biological/organismic evidence, symptoms, signs, biomarkers, functioning, disability-context interaction, diagnosis/classification, current severity, reserve, recovery, future risk, prognosis and treatment-response evidence. It introduces HealthFunctionTargetSpec, OrganismicEvidenceView, SymptomBurdenProfile, FunctionalStatusProfile, ParticipationContextView, SupportCompensationProfile, PersonalBaseline, BaselineDeviation, ChangePointHypothesis, ReserveProfile, HealthTrajectoryView, DiagnosticEvidenceBoundary, RiskScenarioSpec, OrganismicRiskEstimate, PrognosticTrajectoryView, HealthEvidenceBundle, HealthOperationalState, HealthEscalationBoundary and NextBestHealthOperation. Population reference and personal baseline are kept distinct; biomarkers are typed by intended use; screening/risk signals are not diagnoses; preserved functioning can coexist with disease or low reserve; disability is not disease and depends partly on environmental/support context; and high-stakes clinical interpretation remains outside autonomous HOC authority. No Foundation is reopened and no engineering schema is prescribed.
evidence_status: verified-synthesis
readiness: READY
related:
  - human.operational-concepts.hoc1
  - human.operational-concepts.hoc4
  - human.deep-foundations.hd9
---
# HOC7 — Health, Functioning, Personal Baseline, Reserve and Risk Trajectory

## 0. Practical-priority decision

A fresh residual scan after HOC0–HOC6 found no larger unreconstructed practical family than:

```text
health / functioning
personal baseline / change
reserve
current disease-related state
risk / prognosis
safety escalation boundary
```

HOC7 is therefore admitted as the next **operational** reconstruction.

This does **not** admit a new Human Foundation and does not convert Ordivon into an autonomous diagnostic system.

The high-level target is narrower:

> represent health-relevant state and functioning well enough to support monitoring, capability/readiness interpretation, evidence collection, support allocation and legitimate escalation without collapsing biomarker, symptom, diagnosis, disability, risk or Human worth.

---

# 1. Core deletion

Reject the common health collapse:

```text
abnormal number
→ disease
→ severity
→ disability
→ low capability
→ unsafe
→ treatment needed
```

Canonical guards:

```text
Health != NoDiagnosis
Health != StatisticalAverage
Health != WelfareTotality
Disease != Symptom
Disease != Sign
Disease != Biomarker
Disease != Diagnosis
Diagnosis != Mechanism
Diagnosis != Person
IllnessExperience != DiseaseMechanism
Biomarker != Mechanism
Biomarker != ClinicalOutcomeTotality
RiskFactor != Cause
RiskEstimate != CurrentDiseaseState
Prognosis != Diagnosis
ScreenPositive != DiseaseConfirmed
CurrentFunction != Reserve
Capability != BiologicalHealth
Disease != Disability
Disability != Disease
SupportPreservedFunction != BiologicalRecovery
SymptomsResolved != FullRecovery
PopulationReference != PersonalBaseline
PersonalBaseline != ImmutableSetpoint
```

---

# 2. HealthFunctionTargetSpec

Every operational health query must declare its target.

```text
HealthFunctionTargetSpec = {
  target domain/function,
  current-state vs trajectory vs future-risk question,
  time horizon,
  context/environment,
  support boundary,
  consequence level,
  evidence sources,
  intended use,
  authority/clinical boundary
}
```

Examples of intended use:

```text
track a known measurement over time
interpret a functional change
separate temporary state from persistent decline
plan accessibility/support
decide whether ordinary HOC4 regulation is enough
identify when professional clinical review is needed
```

Not every health question is diagnostic.

---

# 3. Six-layer operational separation

HOC7 retains at least:

```text
1. biological / organismic evidence
2. experienced symptom / illness evidence
3. observable functional performance
4. activity / participation in environment
5. clinical classification / diagnosis evidence
6. future risk / prognosis
```

These layers interact but are not identities.

---

# 4. OrganismicEvidenceView

```text
OrganismicEvidenceView(H, Domain, interval) = {
  measurements / biomarkers,
  observed signs,
  physiological/biological evidence,
  known diagnoses/conditions if supplied by legitimate source,
  interventions/exposures,
  personal baseline/reference context,
  trajectory/change evidence,
  uncertainty,
  provenance
}
```

This is evidence about organismic state, not the organism totality.

---

# 5. Biomarker is an evidence channel

HOC7 follows the FDA–NIH BEST distinction that biomarkers are measured indicators of biological/pathogenic/response processes, and are not by definition measures of how an individual feels, functions or survives.

Therefore:

```text
BiomarkerEvidence
!= SymptomBurden
!= FunctionalStatus
!= ClinicalOutcomeTotality
```

---

# 6. Biomarker purpose must be typed

At minimum preserve intended use where known:

```text
SUSCEPTIBILITY_RISK
DIAGNOSTIC
MONITORING
PROGNOSTIC
PREDICTIVE
RESPONSE
SAFETY
```

because the same measured characteristic can have different interpretation under different validated contexts of use.

```text
BiomarkerValue
without ContextOfUse
is weak evidence for action.
```

---

# 7. Diagnostic biomarker != diagnosis totality

Even when a biomarker is used diagnostically under a legitimate criterion:

```text
DiagnosticBiomarkerResult
!= CompleteDiseaseMechanism
!= CompletePersonState
```

and diagnostic interpretation can require additional evidence, population context, repeat testing or clinical assessment depending on the actual domain.

HOC7 does not invent those disease-specific rules.

---

# 8. Monitoring biomarker != clinical improvement

A monitoring marker can change while:

```text
symptoms
function
reserve
future risk
```

change differently.

Thus:

```text
MarkerImprovement
!= FunctionalRecovery
!= SymptomRecovery
```

unless the target-specific evidence supports that relation.

---

# 9. Response biomarker != proven benefit

A biological response to an intervention can occur without establishing the desired clinical outcome.

```text
BiologicalResponse
!= ClinicalBenefit by definition
```

This protects against overinterpreting mechanism-adjacent measurements.

---

# 10. SymptomBurdenProfile

```text
SymptomBurdenProfile(H, Domain, interval) = {
  symptom type,
  intensity/severity if reported,
  frequency,
  duration,
  triggers/context,
  interference with function,
  variability,
  associated features,
  uncertainty,
  source/provenance
}
```

A symptom is experienced/reported evidence, not a disease identity.

---

# 11. Symptom absence != no disease

Some pathological processes can be asymptomatic, subclinical or compensated.

Therefore:

```text
NoSymptoms != NoDisease
```

HOC7 does not infer disease from this possibility; it only prevents false reassurance by identity.

---

# 12. Symptom presence != one mechanism

Common symptoms can arise from many distinct causes and states.

```text
SameSymptom
!= SameMechanism
```

This is especially important for generic symptoms such as fatigue, pain, dizziness or reduced activity.

---

# 13. Clinical sign != symptom

```text
ClinicalSign
```

is externally observed/measured evidence.

```text
Symptom
```

is experienced/reported evidence.

```text
ClinicalSign != Symptom
```

They may agree, disagree or concern different aspects of state.

---

# 14. FunctionalStatusProfile

A central HOC7 object is:

```text
FunctionalStatusProfile(H, Domain, Context, Support, interval) = {
  body/function-relevant limitations if known,
  activity performance,
  task capability under specified conditions,
  participation restrictions/opportunities,
  variability,
  support dependence,
  compensation,
  effort/cost,
  reliability,
  trajectory,
  uncertainty
}
```

This consumes HOC1 capability and HOC4 state evidence without reducing health to capability.

---

# 15. Functioning is contextual

WHO ICF explicitly treats functioning/disability in context and includes environmental factors.

HOC7 therefore preserves:

```text
ObservedFunction
= Human × Task × Environment × Support × State × Opportunity
```

as an operational dependency, not a claim that Human disappears into context.

---

# 16. Capability != biological health

A person can maintain high task capability despite disease through:

```text
compensation
assistive technology
medication/treatment
practice
supportive environment
```

Another can have low observed performance because the environment is inaccessible despite relatively preserved biological function.

```text
Capability != BiologicalHealth
```

---

# 17. Disability != disease

HOC7 adopts the structural lesson from ICF:

```text
DisabilityExperience
can depend on
health condition/impairment × activity demands × environment × support × participation context
```

Therefore:

```text
Disease != Disability
Disability != Disease
```

and two people with similar diagnoses/impairments may experience different functional barriers.

---

# 18. ParticipationContextView

```text
ParticipationContextView(H, LifeDomain, interval) = {
  activities/roles desired or required,
  environmental facilitators,
  environmental barriers,
  assistive/support resources,
  access constraints,
  social/institutional constraints,
  participation achieved,
  participation desired,
  uncertainty
}
```

This is not a moral judgment about what participation should be desired.

---

# 19. SupportCompensationProfile

```text
SupportCompensationProfile(H, Function, interval) = {
  support/tool/intervention,
  function with support,
  function without support if legitimately known/tested,
  effort/cost,
  reliability,
  fallback,
  dependency,
  biological recovery evidence if any
}
```

This distinguishes preserved functioning from intrinsic recovery.

---

# 20. Support != recovery

```text
Mechanical/Pharmacologic/AssistiveSupport
!= BiologicalRecovery
```

A support can preserve function or participation while intrinsic impairment persists.

This is not a negative judgment; support-enabled functioning can be the correct long-term state.

---

# 21. PersonalBaseline

HOC4 retained baseline for state regulation; HOC7 generalizes it carefully for health/functioning:

```text
PersonalBaseline(H, Variable/Function, Context, BaselineInterval)
```

It can represent a stable-enough within-person reference under declared conditions.

Canonical:

```text
PersonalBaseline != PopulationReference
PersonalBaseline != OptimalState
PersonalBaseline != ImmutableSetpoint
```

---

# 22. PopulationReference

```text
PopulationReference(Measure, ReferencePopulation, Protocol)
```

answers where a measurement lies relative to a defined population/procedure.

It does not automatically answer:

```text
what is normal for this Human?
what is optimal?
what is dangerous?
what has changed?
```

---

# 23. Personal baselines can add signal

Longitudinal CBC research has shown patient-specific hematological setpoints can remain highly stable over long periods in healthy adults and can support personalized interpretation beyond population intervals in that domain.

HOC7 therefore admits personal baseline as a useful evidence object where longitudinal stability has been established.

It does **not** generalize the same stability to every biomarker or function.

---

# 24. Baseline deviation

```text
BaselineDeviation(H, Variable/Function, t) = {
  current observation,
  personal baseline estimate,
  deviation magnitude/direction,
  expected within-person variability,
  population-reference relation,
  context/exposure changes,
  measurement uncertainty
}
```

Deviation is evidence of change, not disease by identity.

---

# 25. ChangePointHypothesis

Often the most operationally useful question is:

```text
Has the Human's recent trajectory materially changed?
```

HOC7 introduces:

```text
ChangePointHypothesis(H, Target, interval)
```

with evidence for:

```text
new level
new trend
new variability
new support dependence
new symptom/function relation
```

This remains a hypothesis until evidence supports scope/cause.

---

# 26. Change point != diagnosis

A detected longitudinal change can reflect:

```text
measurement change
normal development
training
pregnancy
medication
acute illness
chronic disease
environment
behavior change
unknown cause
```

Therefore:

```text
ChangeDetected != DiseaseIdentified
```

---

# 27. ReserveProfile

HD9 and HOC4 already separated reserve from current function.

HOC7 retains:

```text
ReserveProfile(H, FunctionDomain, Challenge/LoadContext, interval)
```

as evidence about additional perturbation/load that can be tolerated before a specified function fails or requires compensation.

```text
CurrentFunction != Reserve
```

---

# 28. Preserved function can coexist with low reserve

A Human can perform normally at baseline while having reduced margin under challenge.

Thus:

```text
NormalCurrentFunction
!= HighReserve
```

This is one reason health cannot be modeled from resting/current performance alone.

---

# 29. Reserve is protocol-relative

```text
Reserve_D
!= Reserve_E
```

Cardiorespiratory, cognitive, renal, motor or social-functional reserves are not one common tank.

A challenge protocol must name the function being tested.

---

# 30. HealthTrajectoryView

```text
HealthTrajectoryView(H, Domain, interval) = {
  baseline,
  exposures,
  symptoms/signs,
  organismic evidence,
  function/participation,
  support/treatment history,
  compensation,
  reserve,
  recovery/remission/recurrence evidence,
  diagnoses/classifications if legitimately supplied,
  future-risk estimates,
  uncertainty
}
```

This is a multi-layer trajectory, not one health score.

---

# 31. Acute != chronic

```text
AcuteResponse
!= ChronicDisease
```

and:

```text
ChronicDisease
!= AcuteDiseaseForLonger
```

because persistent remodeling/adaptation and altered reserve can change state architecture over time.

HOC7 only retains this structural distinction; disease-specific mechanisms remain clinical/biological domain knowledge.

---

# 32. Recovery is endpoint-specific

HOC4 already reconstructed recovery operationally.

HOC7 extends it across health endpoints:

```text
symptom recovery
biomarker recovery
organ/function recovery
activity/participation recovery
reserve recovery
risk normalization/remission
```

These need not coincide.

---

# 33. Symptom resolution != full recovery

```text
SymptomsResolved
!= BiologicalStateRestored
!= FunctionalRecovery
!= ReserveRestored
!= FutureRiskNormalized
```

The same applies in reverse: some function can recover while symptoms or markers persist.

---

# 34. DiagnosisRecord

When a diagnosis comes from an appropriate legitimate source, HOC7 can represent:

```text
DiagnosisRecord = {
  label/system,
  source,
  date,
  evidence context if known,
  status/uncertainty if supplied,
  current relevance,
  related treatment/monitoring context
}
```

HOC7 does not independently upgrade observations into a diagnosis.

---

# 35. Diagnosis != mechanism

A diagnosis can be useful for:

```text
communication
care pathways
prognosis
classification
billing/public health
```

without being one mechanistic natural kind.

```text
Diagnosis != DiseaseMechanism
```

---

# 36. DiagnosticEvidenceBoundary

A critical HOC7 object is:

```text
DiagnosticEvidenceBoundary(TargetCondition, EvidenceState, AuthorityContext)
```

which records whether current evidence is:

```text
NOT_A_DIAGNOSTIC_QUERY
SCREENING_LEVEL_ONLY
MONITORING_SIGNAL
DIAGNOSTIC_CRITERIA_UNKNOWN_TO_CONSUMER
REQUIRES_CLINICAL_INTERPRETATION
CLINICIAN_DIAGNOSIS_PROVIDED
INSUFFICIENT_EVIDENCE
```

The purpose is to block autonomous overreach.

---

# 37. Screening != diagnosis

```text
ScreenPositive
!= DiseaseConfirmed
```

A screening signal changes what evidence may be worth collecting; it does not establish the condition by itself unless a specific validated framework explicitly defines otherwise.

HOC7 does not guess disease-specific confirmatory pathways.

---

# 38. RiskScenarioSpec

`Risk` is reconstructed as a relation/scenario rather than a Human property.

```text
RiskScenarioSpec = {
  outcome,
  horizon,
  population/context,
  exposure/intervention state,
  competing events if relevant,
  prediction time,
  consequence,
  intended decision,
  model/evidence source
}
```

Without an outcome and horizon, `risk = high` is underspecified.

---

# 39. OrganismicRiskEstimate

```text
OrganismicRiskEstimate(H, RiskScenarioSpec, t) = {
  estimate / category,
  uncertainty,
  reference population,
  model/source,
  predictors/evidence used when available,
  calibration/validation scope,
  transport caveats,
  modifiable/nonmodifiable distinction if justified,
  update time
}
```

It is a prediction, not current state.

---

# 40. Risk estimate != current severity

```text
FutureRisk
!= CurrentDiseaseSeverity
```

A currently asymptomatic Human can have elevated future risk; a severely ill Human can have different future-risk questions depending on outcome/horizon.

---

# 41. Susceptibility/risk biomarker != prognostic biomarker

FDA–NIH BEST separates susceptibility/risk biomarkers in people without clinically apparent disease from prognostic biomarkers concerning future events/progression in people with the condition of interest.

HOC7 therefore keeps:

```text
SusceptibilityRisk
!= PrognosticRisk
```

unless a specific context supports overlap.

---

# 42. Prognostic != predictive-treatment-effect

```text
PrognosticEvidence
```

concerns likely future outcome under the relevant condition/context.

```text
PredictiveBiomarkerEvidence
```

concerns differential response to an exposure/intervention.

Therefore:

```text
BadPrognosis
!= EvidenceThatTreatmentXWillHelp
```

---

# 43. Risk factor != cause

```text
RiskFactor
!= Cause
```

A predictor may be causal, proxy, confounded, downstream or non-intervenable.

Therefore HOC7 never converts predictive feature importance into treatment recommendation by identity.

---

# 44. Prediction != intervention value

A highly predictive variable may be a poor intervention target.

```text
PredictiveImportance
!= CausalEffect
!= BestInterventionLever
```

HOC1/HOC2 causal/evidence firewalls remain active.

---

# 45. Risk model performance is scoped

Risk estimates should preserve where possible:

```text
population
setting
measurement protocol
horizon
outcome definition
model version
validation/calibration evidence
```

because:

```text
RiskModelPerformance_D
!= UniversalPerformance
```

---

# 46. PrognosticTrajectoryView

For repeated risk estimation:

```text
PrognosticTrajectoryView(H, Outcome, interval) = {
  sequence of risk estimates,
  changing evidence,
  interventions/exposures,
  function/reserve changes,
  model/version changes,
  uncertainty,
  observed outcomes
}
```

A changing prediction does not automatically mean underlying biology changed; model/input changes can matter.

---

# 47. Multimorbidity is not a disease count

HOC7 carries forward HD9:

```text
MultimorbidityState
!= NumberOfDiagnosesOnly
```

because order, shared mechanisms, treatment interactions, function, reserve and support can differ.

---

# 48. Same diagnosis set != same state

```text
SameDiagnosisSet
```

can coexist with different:

```text
symptom burden
function
reserve
trajectory
risk
support needs
```

Thus a diagnosis list is not a sufficient operational Human model.

---

# 49. HealthEvidenceBundle

A practical integrated evidence object is:

```text
HealthEvidenceBundle(H, Target, interval) = {
  self-report/symptoms,
  observations/signs,
  biomarkers/measurements,
  functional evidence,
  participation/environment evidence,
  baseline/trajectory evidence,
  known diagnosis records,
  treatment/support/exposure history,
  risk/prognostic evidence,
  provenance,
  measurement quality,
  uncertainty/conflict
}
```

It deliberately preserves contradictions.

---

# 50. Evidence disagreement is not data corruption by default

Examples:

```text
symptoms severe + biomarker normal
marker abnormal + function preserved
diagnosis present + participation high with support
risk high + current state asymptomatic
```

These can be legitimate multi-layer states.

```text
CrossLayerMismatch
!= InvalidData by definition
```

---

# 51. HealthOperationalState

For practical consumers, HOC7 permits scoped modes such as:

```text
STABLE_WITHIN_KNOWN_SCOPE
BASELINE_DEVIATION_TO_RECHECK
FUNCTION_CHANGE_TO_INVESTIGATE
SUPPORT_COMPENSATED_FUNCTION
RECOVERY_IN_PROGRESS
RESIDUAL_FRAGILITY_OR_LOW_RESERVE
KNOWN_CONDITION_MONITORING
RISK_SIGNAL_WITHOUT_CURRENT_DIAGNOSIS
CLINICAL_INTERPRETATION_REQUIRED
INSUFFICIENT_EVIDENCE
```

These are not diagnoses.

---

# 52. HealthStatus scalar is rejected

A naked:

```text
health = 82
```

cannot preserve:

```text
symptoms
function
reserve
risk
diagnosis
participation
support
trajectory
```

which may move independently.

Therefore:

```text
OneHealthScore != CanonicalHealthState
```

A UI may compress for a declared purpose, but drill-down/evidence scope must remain available.

---

# 53. FunctionalStatus != HealthStatus totality

Functioning is one critical outcome/projection, not the whole organismic state.

```text
FunctionalStatus
!= BiologicalHealthTotality
```

A Human can function well while carrying latent/pathological risk or can function poorly because of environmental barriers rather than biological deterioration.

---

# 54. Participation != capacity

A Human may have capacity but lack opportunity/access.

Or may participate successfully through supports despite low unaided capacity.

```text
Participation
!= IndependentCapacity
```

This connects directly to HOC1 independent/situated/joint capability.

---

# 55. Health and HOC1 capability

HOC7 supplies health-relevant evidence to HOC1 but must not rewrite capability from diagnosis labels.

```text
Diagnosis
→ may update capability prior
```

but does not equal measured capability.

```text
Diagnosis != CapabilityEstimate
```

Task-specific evidence remains necessary.

---

# 56. Health and HOC4 state

HOC4 owns ordinary near-term load/fatigue/recovery regulation.

HOC7 takes over when evidence becomes more consistent with:

```text
persistent
recurrent
severe
unexplained
multi-system
function-limiting
known-condition-linked
or clinically consequential
```

state.

This is an ownership heuristic, not diagnostic criterion.

---

# 57. State effect != health trajectory change

One poor day can reflect temporary state.

Repeated/persistent change can justify a wider health/functioning query.

```text
OneStatePerturbation
!= ChronicHealthDecline
```

HOC7 should preserve the cheaper explanation until evidence requires expansion.

---

# 58. Health and HOC3 learning

Disease, symptoms, treatment, sleep, pain or accessibility can change learning performance.

But:

```text
PoorLearningUnderHealthBurden
!= LowLearningPotential
```

HOC3 modifiability remains intervention/state scoped.

---

# 59. Health and HOC5 goals

A health limitation can change feasible means, time horizon or state without invalidating a Human goal.

```text
HealthConstraint
!= GoalInvalidation
```

Agents should first consider:

```text
support
alternative means
scope/timing change
accessibility
```

before silently rewriting goals.

---

# 60. Health and HOC6 coordination

Care/support can involve multiple participants with different roles and authority.

HOC6 role/common-ground/handoff machinery applies, but HOC7 does not infer that family, caregiver, Agent or coordinator has medical decision authority.

```text
CareRole != ClinicalAuthority by definition
```

---

# 61. HealthEscalationBoundary

Because HOC7 is high-stakes, it explicitly represents when the operational layer should stop pretending to own interpretation.

```text
HealthEscalationBoundary = {
  trigger class,
  reason for uncertainty/concern,
  affected function/state,
  consequence,
  evidence/provenance,
  appropriate owner class,
  urgency only if supplied by validated domain rule or legitimate source,
  interim scope limitations
}
```

---

# 62. Appropriate owner classes

Depending on the context, handoff can be to:

```text
Human user for clarification
licensed clinician / clinical service
emergency service under externally validated emergency criteria
occupational/safety professional
accessibility/support owner
existing care team
```

HOC7 itself does not create emergency/diagnostic criteria from generic patterns.

---

# 63. Clinical interpretation required is a valid output

A strong system must be able to return:

```text
CLINICAL_INTERPRETATION_REQUIRED
```

instead of fabricating certainty.

This is not failure; it is correct ownership.

---

# 64. NextBestHealthOperation

Within legitimate non-diagnostic scope, HOC7 can propose operations such as:

```text
RECORD_OBSERVATION
VERIFY_MEASUREMENT_OR_PROVENANCE
COMPARE_PERSONAL_BASELINE
COMPARE_POPULATION_REFERENCE_IF_APPROPRIATE
REPEAT_MEASUREMENT_IF_ALREADY_AUTHORIZED/APPROPRIATE
TRACK_SYMPTOM_OR_FUNCTION_TRAJECTORY
ASSESS_CONTEXT/SUPPORT_BARRIER
ADD_OR_RESTORE_ACCESSIBILITY_SUPPORT
REDUCE_LOAD / USE_HOC4_REGULATION
COLLECT_FUNCTIONAL_EVIDENCE
REVIEW_EXISTING_CLINICAL_PLAN
REQUEST_CLINICAL_INTERPRETATION
ESCALATE_TO_APPROPRIATE_HEALTH/SAFETY_OWNER
NO_INTERVENTION / CONTINUE_MONITORING
```

It does not autonomously prescribe treatment.

---

# 65. NextBestHealthOperation != treatment recommendation

```text
OperationalMonitoringAction
!= MedicalTreatmentPlan
```

Medication changes, diagnosis-specific therapies and procedures remain outside generic HOC7 authority unless supplied by an appropriate external clinical plan/tool with its own authority and safeguards.

---

# 66. Treatment history can still be represented

```text
InterventionHistory = {
  intervention,
  source/authority,
  start/stop,
  adherence/exposure if known,
  observed response,
  adverse effects if reported,
  monitoring context
}
```

but:

```text
TreatmentResponse
!= MechanismProof
```

---

# 67. Response can be symptom-specific

```text
SymptomResponse
!= PathologyResolution
```

and:

```text
BiomarkerResponse
!= FunctionalRecovery
```

A system should preserve exactly which endpoint changed.

---

# 68. Risk is not permission

A model predicting elevated health risk does not automatically justify:

```text
restriction
surveillance
employment exclusion
insurance action
loss of autonomy
```

```text
RiskPrediction
!= LegitimateAuthority
```

Normative/legal/governance owners remain separate.

---

# 69. Disease/disability is not moral worth

Canonical normative firewall:

```text
Disease != LowerMoralWorth
Disability != LowerMoralWorth
LowReserve != LowerMoralWorth
HealthRisk != MoralFault
BehaviorAssociatedRisk != Blame
```

---

# 70. Accessibility is not treatment failure

If environment modification or assistive technology restores desired participation:

```text
SuccessfulSupport
```

is a legitimate outcome even if intrinsic impairment remains.

The system should not treat support dependence as a defect to eliminate by default.

---

# 71. Support removal can be harmful/unnecessary

Unlike some learning probes in HOC3, health/accessibility supports should not be removed merely to measure unaided performance when removal creates unnecessary risk or burden.

```text
SupportRemovalForMeasurement
requires legitimate purpose + safety/consent
```

Independent capability is not always the correct target.

---

# 72. Measurement can perturb health behavior

Health monitoring itself can change:

```text
attention
anxiety
care seeking
activity
adherence
Agent/user decisions
```

Therefore:

```text
HealthEvidenceCollection
may be an intervention.
```

Avoid compulsive measurement or unnecessary alerting as default.

---

# 73. Alert fatigue / false alarm cost

A high-sensitivity monitoring policy can create:

```text
false positives
unnecessary follow-up
attention burden
anxiety
alert desensitization
```

while a high-specificity policy may miss early changes.

Thus:

```text
HealthAlertThreshold
is consequence/use-case specific.
```

HOC7 does not freeze one universal threshold.

---

# 74. Personalization can overfit

Personal baselines can be powerful, but sparse histories can overfit or encode unrecognized pathology.

Therefore:

```text
PersonalizedReference
!= AutomaticallyBetterReference
```

Population information and clinical context can remain essential.

---

# 75. Baseline quality requirements

A useful PersonalBaseline should preserve where possible:

```text
number/timing of observations
measurement protocol
state/context
known perturbations
within-person variability
change points
staleness
```

A single historical measurement is not a baseline by definition.

---

# 76. Population reference can also be wrong for the question

A value inside population reference can still represent a meaningful within-person change.

A value outside population reference can be stable for one individual.

Therefore:

```text
WithinPopulationRange
!= NoMeaningfulChange
```

and:

```text
OutsidePopulationRange
!= DiseaseByDefinition
```

---

# 77. Longitudinal evidence hierarchy

A rough operational ladder for a personal change claim:

```text
L0 one isolated observation
L1 repeated observations under mixed contexts
L2 repeated comparable observations
L3 stable baseline + one deviation
L4 repeated deviation / trend / change-point evidence
L5 linked functional/symptom/biological trajectory
L6 externally interpreted clinical significance
```

This is not a universal medical evidence grading system.

---

# 78. Function evidence hierarchy

```text
F0 self-reported limitation only
F1 one observed task
F2 repeated target tasks
F3 varied realistic contexts
F4 support-with/without comparisons where safe and appropriate
F5 longitudinal participation evidence
F6 clinically/occupationally validated assessment where required
```

Self-report remains legitimate evidence; higher levels answer different questions rather than invalidating experience.

---

# 79. Risk evidence hierarchy

A risk claim should preferably preserve:

```text
model/source
validation population
outcome definition
horizon
calibration/discrimination evidence if known
external validation if known
current input quality
transport uncertainty
```

A number without provenance is weak evidence.

---

# 80. Health evidence provenance

HOC7 strongly distinguishes:

```text
Human self-report
consumer wearable
home measurement
laboratory measurement
medical record
clinician interpretation
research-grade assay
Agent inference
```

These are not interchangeable authority classes.

---

# 81. Agent inference must be labeled

An Agent-derived hypothesis must remain:

```text
INFERRED / UNVERIFIED
```

rather than being written back as:

```text
diagnosis
confirmed condition
clinician finding
```

without the corresponding source.

---

# 82. Diagnostic contamination guard

A system can accidentally create circular evidence:

```text
Agent infers condition
→ label enters profile
→ later model treats profile label as confirmed evidence
→ confidence increases
```

HOC7 requires provenance so:

```text
AgentInference
cannot silently become
IndependentClinicalEvidence.
```

---

# 83. Model version / reference version matters

Risk estimates, reference intervals and classification criteria can change.

```text
SameLabel/ScoreName
!= SameOperationalMeaning across versions
```

Version/protocol should be retained when consequence warrants it.

---

# 84. Health trajectory is not destiny

A risk trajectory or chronic condition model describes current evidence and expected possibilities under a scope.

```text
PredictedTrajectory
!= FixedFuture
```

Interventions, environment, support, random variation and new evidence can change the future.

---

# 85. Health uncertainty can be irreducible near-term

Sometimes the correct state is:

```text
persistent unexplained symptoms
conflicting measurements
uncertain mechanism
```

HOC7 permits:

```text
UNRESOLVED / CLINICAL_INTERPRETATION_REQUIRED
```

without forcing a synthetic diagnosis.

---

# 86. Multiscale health ownership

Useful separations:

```text
cell/tissue/organ mechanism
whole-organism function
experienced symptom
activity/participation
social/environmental barrier
clinical classification
population risk
```

A cause at one scale does not erase relevant descriptions at another.

---

# 87. HealthOperationalState is not PersonDifferenceProfile

A chronic health feature may contribute to persistent individual differences, but current HOC7 state/trajectory evidence is not the Human's total person profile.

```text
HealthTrajectory
!= PersonIdentity
```

HD10 projection guards remain active.

---

# 88. Privacy minimum

Health data are highly sensitive.

Operational systems should collect/store only the health evidence needed for a legitimate target and access policy.

HOC7 does not require a maximal lifetime medical dossier.

---

# 89. Consent / authority boundary

A Human may authorize monitoring without authorizing:

```text
sharing
employer use
family access
clinical action
behavior restriction
```

Therefore:

```text
ConsentToMeasure
!= ConsentToAllDownstreamUses
```

---

# 90. Minimal counterexamples

## C1 — abnormal marker, no diagnosis

One measurement lies outside a reference interval without enough context to establish disease.

```text
AbnormalMeasurement != Disease
```

## C2 — disease, high function

Human has a diagnosed condition but functions well with treatment/support.

```text
Diagnosis != LowCapability
```

## C3 — no diagnosis, impaired function

Human has significant activity limitation but no current diagnostic label.

```text
NoDiagnosis != FullFunction
```

## C4 — normal population range, meaningful personal change

A value remains inside population reference but shifts substantially from a stable personal baseline.

```text
PopulationNormal != NoWithinPersonChange
```

## C5 — low reserve, normal current performance

Human performs normally at rest but fails under modest additional challenge.

```text
CurrentFunction != Reserve
```

## C6 — symptom resolved, recovery incomplete

Subjective symptom improves while function/reserve or other biological evidence remains abnormal.

```text
SymptomsResolved != FullRecovery
```

## C7 — risk high, current disease absent

A susceptibility/risk estimate concerns future possibility rather than current diagnosis.

```text
Risk != CurrentDisease
```

## C8 — same diagnosis, different participation

Two Humans with the same diagnosis experience different participation because support/environment differs.

```text
Diagnosis != DisabilityExperience
```

## C9 — Agent inference becomes circular label

Agent hypothesizes disease; downstream system treats hypothesis as confirmed history.

```text
Inference != IndependentEvidence
```

## C10 — support preserves function

Assistive support enables participation although intrinsic impairment remains.

```text
FunctionRestoredWithSupport != BiologicalRecovery
```

---

# 91. Update / expiry

## SymptomBurdenProfile

Fast/intermediate; update with meaningful symptom/context changes.

## FunctionalStatusProfile

Update with repeated function/participation/support changes.

## PersonalBaseline

Slow, change-point aware; do not chase noise.

## ReserveProfile

Update after relevant challenge/health/support changes; protocol-specific.

## HealthTrajectoryView

Longitudinal; preserve interventions and change points.

## DiagnosisRecord

Version/source aware; do not delete historical diagnosis merely because symptoms improve.

## OrganismicRiskEstimate

Expire/update with model version, new measurements, age/time horizon, intervention or material context change.

---

# 92. Reflexivity

Health models can change behavior and therefore future evidence:

```text
risk alert
→ care seeking / behavior change
→ outcome changes
```

or:

```text
low-risk label
→ monitoring declines
→ fewer observations
```

Thus:

```text
ObservedHealthTrajectory
may be policy-conditioned.
```

---

# 93. Anti-medicalization guard

Ordinary variation, temporary fatigue, sadness, performance fluctuation or preference difference should not be converted into health pathology merely because HOC7 exists.

```text
HumanVariation
!= DiseaseByDefault
```

HOC4/HOC5/HOC10-like ordinary functional explanations remain available.

---

# 94. Anti-underreaction guard

The opposite failure is also possible:

```text
persistent/severe/unexplained change
```

should not be endlessly reclassified as ordinary productivity/state noise when the operational evidence has crossed a legitimate health/safety escalation boundary.

HOC7 exists partly to support correct ownership transfer.

---

# 95. Normative firewall

```text
Health != HumanWorth
Disease != Blame
Disability != Inferiority
Risk != Guilt
Diagnosis != IdentityTotality
FunctionalLimitation != LackOfAgency
NeedForSupport != Failure
ClinicalConcern != PermissionToOverrideConsent by definition
PredictedPoorOutcome != LegitimateExclusion
```

---

# 96. Foundation / HOC dependency map

```text
HF1  organism/body/person boundaries
HF2  experience/reportability boundaries
HF5  regulation/stress/fatigue/recovery
HF6  adaptation/resilience/development
HF11 action/capability/tool support
HF14–17 rights/welfare/responsibility/governance
HF19 work/environment/institutional context
HF21 affect/illness experience interactions
HD9  organismic health/disease/pathophysiology substrate
HD10 personal differences/baseline projections
HOC1 capability/readiness/bottleneck
HOC2 evidence/calibration/verification
HOC3 learning/modifiability
HOC4 state/load/recovery/baseline
HOC5 goals/agency/execution
HOC6 care/team roles/coordination/authority handoffs
```

No new Foundation is required.

---

# 97. Canonical forbidden inferences

```text
Health != NoDiagnosis
Health != StatisticalAverage
Health != WelfareTotality
Disease != Symptom
Disease != Sign
Disease != Biomarker
Disease != Diagnosis
Diagnosis != Mechanism
Diagnosis != Person
IllnessExperience != DiseaseMechanism
Biomarker != Mechanism
Biomarker != ClinicalOutcomeTotality
DiagnosticBiomarkerResult != CompleteDiseaseState
MarkerImprovement != ClinicalBenefit
BiologicalResponse != ClinicalBenefit by definition
NoSymptoms != NoDisease
SameSymptom != SameMechanism
Capability != BiologicalHealth
Disease != Disability
Disability != Disease
Participation != IndependentCapacity
SupportPreservedFunction != BiologicalRecovery
PopulationReference != PersonalBaseline
PersonalBaseline != OptimalState
PersonalBaseline != ImmutableSetpoint
ChangeDetected != DiseaseIdentified
CurrentFunction != Reserve
NormalCurrentFunction != HighReserve
SymptomsResolved != FullRecovery
Diagnosis != CapabilityEstimate
ScreenPositive != DiseaseConfirmed
RiskEstimate != CurrentDiseaseState
FutureRisk != CurrentSeverity
SusceptibilityRisk != PrognosticRisk
Prognosis != TreatmentResponsePrediction
RiskFactor != Cause
PredictiveImportance != CausalEffect
TreatmentResponse != MechanismProof
OneHealthScore != CanonicalHealthState
AgentInference != IndependentClinicalEvidence
ConsentToMeasure != ConsentToAllDownstreamUses
HealthRisk != MoralFault
```

---

# 98. Operational reasoning grammar

A Human-supporting Agent can use HOC7 as:

```text
1. Declare HealthFunctionTargetSpec and intended use.
2. Separate current biological evidence, symptoms, functioning, diagnosis records and future risk.
3. Preserve evidence provenance/authority.
4. Type biomarkers by context of use instead of treating every measurement as diagnostic.
5. Compare personal baseline and population reference separately where each is legitimate.
6. Detect baseline deviations/change points without converting them directly to disease.
7. Project FunctionalStatusProfile in the actual environment/support context.
8. Project ReserveProfile only from appropriate challenge/trajectory evidence.
9. Build HealthTrajectoryView when the question is longitudinal.
10. Represent risk with explicit outcome/horizon/model/validation scope.
11. Check DiagnosticEvidenceBoundary before making any diagnostic-like statement.
12. If within non-diagnostic authority, choose NextBestHealthOperation such as verify/track/support/monitor.
13. If persistent/severe/unexplained/clinically consequential evidence exceeds HOC ownership, produce HealthEscalationBoundary and hand off to the appropriate legitimate owner.
14. Never convert diagnosis, disability, risk or support need into moral worth, consent or authority claims.
```

This is a reasoning grammar, not a diagnostic or treatment engine.

---

# 99. HOC7 stop rule

HOC7 is complete because it has:

```text
separated biological evidence, symptom experience, function/participation, diagnosis and future risk;
reconstructed HealthFunctionTargetSpec and OrganismicEvidenceView;
typed biomarkers by context of use;
reconstructed SymptomBurdenProfile and ClinicalSign boundary;
reconstructed FunctionalStatusProfile and ParticipationContextView using environment/support-sensitive functioning;
reconstructed SupportCompensationProfile and preserved support-vs-recovery distinction;
reconstructed PersonalBaseline, PopulationReference, BaselineDeviation and ChangePointHypothesis;
retained protocol-relative ReserveProfile;
reconstructed HealthTrajectoryView across acute/chronic/recovery/remission/recurrence evidence;
added DiagnosisRecord and explicit DiagnosticEvidenceBoundary;
reconstructed RiskScenarioSpec, OrganismicRiskEstimate and PrognosticTrajectoryView;
separated susceptibility/risk, prognostic, predictive and diagnostic evidence;
reconstructed HealthEvidenceBundle and non-diagnostic HealthOperationalState;
added HealthEscalationBoundary as an ownership-transfer guard;
introduced NextBestHealthOperation while prohibiting autonomous generic treatment prescription;
made accessibility/support and disability-context interaction explicit;
added provenance, circular-inference, privacy, consent, alert-fatigue, overpersonalization and anti-medicalization guards;
connected HOC7 back to HOC1–HOC6;
and preserved moral, authority and clinical-practice boundaries.
```

No Foundation reopen condition is triggered.

```text
FoundationReopenCondition(HF0–HF23) = false
NextDeepRoute = UNKNOWN
```

HOC7 does not preselect HOC8.
