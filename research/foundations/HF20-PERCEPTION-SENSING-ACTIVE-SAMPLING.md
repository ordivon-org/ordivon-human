---
schema_version: 1
id: human.foundations.hf20
title: HF20 — Perception, Sensing, Active Sampling and Perceptual World Coupling
type: report
profile: research
lifecycle: completed
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - reader
  - researcher
  - builder
  - agent
updated: 2026-08-17
summary: Canonical foundation extraction from HD1. HF20 reconstructs the missing perceptual world-coupling layer between world/source and experience/attention/representation/action, separating distal source, proximal signal, sampling, transduction, sensory evidence, perceptual organization/content, awareness, report and action; preserving modality, multisensory, active-sensing, development and model-family plurality without reopening HF0–HF19.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.deep-foundations.hd1
  - human.deep-foundations.hd1.sources
  - human.foundations.hf20.sources
  - human.foundations.hf20.continuation
---
# HF20 — Perception, Sensing, Active Sampling and Perceptual World Coupling

## 0. Admission history

HF20 is not a mechanically scheduled successor to HF19.

After HF19, the next foundation remained UNKNOWN. HD0 identified perception as an
interface-rich/mechanism-thin depth residual and admitted HD1 as non-foundation research.
HD1 then established the canonical admission conditions:

```text
RepeatedResidual = true
NeighboringStructure = true
DecisionExplanationValue = true
NotEngineeringDebt = true
NotTerminologyChurn = true
CrossContextEvidencePressure = true
BoundarySafety = true
```

Therefore HF20 is a **thin canonical extraction** from HD1, not a second research pass.

HF0–HF19 are not reopened.

---

# 1. Minimum perceptual world-coupling grammar

```text
WorldState_t / DistalSource
+ BodyState_t
+ SensorState_t
+ SamplingPolicy_t
        ↓
SamplingAction_t
        ↓
PhysicalInteraction / ProximalSignal_t
        ↓
ReceptorState / Transduction_t
        ↓
SensoryEvidence_t
        ↓
PerceptualOrganization_t
        ↓
PerceptualState / Content_t
        ├→ possible Experience / Awareness
        ├→ Attention / priority
        ├→ Memory / recognition / epistemic use
        └→ Action / control / new sampling
                        ↓
              World/SensorState_{t+1}
                        ↺

History / development / learning
→ updates sampling, calibration, mapping, uncertainty and organization
```

This is a typed interface grammar, not one neural or computational theory.

---

# 2. Core source/evidence separations

```text
DistalSource != ProximalSignal
ProximalSignal != ReceptorState
ReceptorState != SensoryEvidence
SensoryEvidence != PerceptualContent
```

The same world source can produce different proximal signals under different viewpoint,
illumination, distance, medium, occlusion or sensor pose.

Similar proximal signals can also be compatible with different distal causes.

---

# 3. Transduction is not perception

```text
Transduction
= physical/sensory interaction → receptor/neural signal transformation
```

It does not by itself establish:

```text
feature organization
object/event identity
source attribution
awareness
attention
report
successful action
```

Therefore:

```text
Transduction != PerceptualOrganization
```

---

# 4. `Sensation` is not a safe universal primitive

The word can refer to:

```text
low-level sensory representation
psychophysical detectability
modality-specific conscious quality
subjective sensory feeling
```

HF20 therefore prefers explicit typed surfaces:

```text
SensoryEvidence_D
PerceptualRepresentation_D
PerceptualContent_D
Experience_D
```

rather than one unqualified `Sensation` node.

---

# 5. Perceptual content is not truth

```text
PerceptualContent != DistalReality
PerceptualContent != Truth
```

A perceptual estimate/content may be accurate, uncertain, ambiguous, illusory or
internally influenced depending on the declared target.

This reconnects to HF8's representation/truth firewall.

---

# 6. Perception is not belief

```text
PerceptualContent != Belief
```

Knowledge that an illusion is misleading does not necessarily remove the perceptual
appearance.

Perception can guide action without propositional endorsement.

---

# 7. Perception is not consciousness

HF20 preserves HF2:

```text
PerceptualProcessing != ConsciousExperience
PerceptualContent != PerceptualAwarenessByDefinition
```

Objective sensitivity/action guidance and ordinary reportable experience can dissociate.

---

# 8. Perception is not attention

HF20 preserves HF3:

```text
Perception != Attention
PerceptualEvidence != AttentionalPriority
Salience != Priority != Attention != Awareness
```

Attention may alter acquisition, weighting, competition and access without being the
perceptual content itself.

---

# 9. Perception is not report

```text
PerceptualContent != Report
```

Report additionally requires some combination of access, mapping, memory, decision and
motor/language execution.

No-report procedures are therefore measurement strategies, not direct ontology windows.

---

# 10. Measurement can alter perception

```text
MeasurementOfPerception may become InterventionOnPerception
```

Fixation, eye-movement instructions, head restraint, exploration restrictions, response
mapping and timing can alter sensory sampling or perceptual dynamics.

Each measurement should declare:

```text
Construct
MeasurementAction
SamplingRestriction
PotentialInterventionEffect
```

---

# 11. Perception is not action

But action can change perceptual evidence.

Distinguish:

```text
TaskAction
SamplingAction
CalibrationAction
ReportAction
```

These can overlap but are not identical.

---

# 12. Active sensing

```text
ActiveSensing_D
= action that materially changes the distribution, quality, location or timing
  of sensory evidence acquired for perceptual task D
```

Canonical loop:

```text
SamplingAction_t
→ SensoryEvidence_{t+1}
→ PerceptualUpdate_{t+1}
→ SamplingAction_{t+1}
```

---

# 13. Active sensing is not active inference

```text
ActiveSensing != ActiveInference
```

Active sensing is a phenomenon/functional role.

Active inference is one formal theory family for perception-action coupling.

Evidence that humans actively sample does not prove active inference.

---

# 14. Active sensing is not always better

```text
ActiveBenefit_D != ActiveBenefit_E
```

Active exploration helps only when its movement/sampling structure supplies task-relevant
information or useful control/calibration.

`Active > Passive` is not a Human universal.

---

# 15. Sampling policy is endogenous

What becomes observable depends partly on how the organism samples.

```text
SamplingPolicy_t
= f(goal, uncertainty, attention, history, body constraints, cost, expected information)
```

Therefore situated perception cannot always be reduced to passive presentation of a fixed
dataset sample.

---

# 16. Feature is not object

```text
Feature != Object
```

Feature detection does not settle:

```text
which features belong together
which source generated them
whether a continuing object/event exists
```

---

# 17. Binding is not integration

```text
Binding != Integration
```

Binding/segregation concerns which signals belong to one entity/event/source.

Integration concerns combining information once signals are treated as relevant to a
common estimated variable/source.

---

# 18. Integration is not mandatory fusion

```text
Integration != AlwaysFuse
CueCombination != CueFusionByDefinition
```

The perceptual system can preserve separate estimates or arbitrate between common and
separate causes.

---

# 19. Reliability is not source identity

```text
CueReliability != CommonCause
CrossModalSynchrony != CommonCauseByDefinition
```

Reliability/precision can affect weighting, but another problem remains: whether the cues
should be combined at all.

---

# 20. Multisensory causal inference

A useful model family represents:

```text
C = common source
C = separate sources
```

and conditions integration/segregation on uncertainty over `C`.

This is retained as a strong multisensory bridge model, not as total perceptual ontology.

---

# 21. Integration is not recalibration

```text
Integration != Recalibration
```

Integration changes a current combined estimate.

Recalibration changes later mappings/unimodal estimates after discrepancy/history.

---

# 22. Recalibration is not motor adaptation

```text
Recalibration != MotorAdaptation
```

A perceptual mapping can shift without the same changes in action policy, and action
adaptation can occur with distinct perceptual aftereffects.

---

# 23. Modality is multi-coordinate

Do not define modality by one coordinate.

Useful axes:

```text
PhysicalCarrier_D
ReceptorClass_D
TransductionMechanism_D
NeuralRoute_D
FunctionalInformation_D
SamplingAction_D
PhenomenalQuality_D
TaskRole_D
```

Therefore:

```text
Modality_Physical
!= Modality_Receptor
!= Modality_NeuralRoute
!= Modality_Function
!= Modality_Phenomenal
```

Sensory substitution and deprivation make these dissociations unavoidable.

---

# 24. Native channel is not task information

```text
TaskInformation != NativeSensorModality
```

A new sensory channel can provide information useful for tasks normally solved through
another modality.

But:

```text
SuccessfulSensorySubstitution != NativePhenomenologyByDefinition
```

---

# 25. Neural territory is not phenomenal modality

Cross-modal plasticity supports:

```text
CorticalArea != FixedPhenomenalQualityByDefinition
```

The interpretation of activity depends on input history, network coupling, task and
experience.

---

# 26. Missing a sense is not `normal system minus input`

```text
MissingSense
→ possible recalibration / cross-modal routing / strategy change / development change
```

Therefore:

```text
BlindSystem != SightedSystem - Vision
```

as a general mechanistic model.

---

# 27. Perceptual development is policy development

Adult cue use cannot be projected onto children by default.

```text
AdultIntegrationPolicy != ChildIntegrationPolicyByDefinition
```

Development can change:

```text
precision
cue dominance
integration windows
causal priors
calibration
sampling
reference-frame use
```

---

# 28. Sensory history remains active after development

```text
PerceptualPolicy_{t+1}
= U(PerceptualPolicy_t, SensoryHistory_t, Action_t, Error_t, Context_t)
```

This consumes HF6 persistent-change grammar.

---

# 29. Perceptual learning is typed

```text
PerceptualLearning_D != PerceptualLearning_E
Exposure != PerceptualLearningByDefinition
```

Learning may alter sensitivity, categorization, precision, causal priors, sampling,
reference frames or recalibration differently.

---

# 30. Reference frame is typed

Possible frames include:

```text
retinotopic
head-centred
body-centred
limb-centred
object-centred
allocentric / scene-relative
```

Therefore:

```text
ReferenceFrame_D != ReferenceFrame_E
```

Transformation among frames may be part of perceptual organization.

---

# 31. Body perception is estimation

HF20 generalizes HF5/HF11:

```text
PhysicalBodyState != BodyPercept
ProprioceptiveEvidence != ExactBodyState
```

Visual/proprioceptive discrepancy, recalibration and interoceptive domain differences
make transparent-body-readout models untenable.

---

# 32. Interoception is not one scalar sense

```text
InteroceptiveAbility_D != InteroceptiveAbility_E
```

Cardiac, respiratory and other internal-sensing tasks can dissociate across sensitivity,
precision and metacognition.

HF5 remains the regulation/interoception owner; HF20 supplies the general perceptual
world-coupling grammar.

---

# 33. Perceptual accuracy is endpoint-specific

```text
Detection
Discrimination
Estimation
Localization
Recognition
Segmentation
SourceAttribution
AffordanceEstimation
```

are non-equivalent task surfaces.

Therefore:

```text
PerceptualAccuracy_D != PerceptualAccuracy_E
TaskSuccess != VeridicalPerceptionTotality
```

---

# 34. Confidence is not accuracy

HF20 preserves HF3:

```text
Confidence != PerceptualAccuracy
```

Metacognition is downstream evidence about performance, not the percept itself.

---

# 35. Perceptual object is not necessarily physical object

```text
PerceptualObject_D != PhysicalObjectByDefinition
```

Perceptual organization may create/track surfaces, objects, events, agents, body parts or
scenes under task/context-dependent individuation.

---

# 36. Current evidence is not complete perceptual state

Occlusion and tracking require:

```text
CurrentSensoryEvidence != CompletePerceptualState
```

History/model structure can preserve continuity when current evidence is absent or
partial.

---

# 37. Same stimulus can support different percepts

Ambiguous/bistable perception establishes:

```text
SamePhysicalStimulus != SamePerceptualState
```

Perceptual dynamics can reflect competition and feedback across multiple levels.

---

# 38. Illusion is target-relative

```text
Illusion_D
= systematic divergence between perceptual estimate/content and declared target D
  under specified context
```

Therefore:

```text
Illusion != IrrationalityByDefinition
```

Illusions are high-information model discriminators.

---

# 39. Imagery, illusion and externally driven perception are distinct

```text
Imagery != Illusion != ExternallyDrivenPerception
```

Similar content or phenomenology does not prove identical generative mechanisms.

---

# 40. Affordance is relational

HF20 retains HF11:

```text
Affordance_D
= Relation(AgentCapability, Environment, Task)
```

and:

```text
Affordance != ObjectPropertyOnly
Affordance != SubjectiveBeliefOnly
```

Tool-integrated action can alter affordances without changing biological identity.

---

# 41. Model-family plurality

HF20 retains as question-relative rivals:

```text
feedforward / feature-computation
Bayesian perceptual inference
predictive coding / predictive processing
recurrent / interactive processing
ecological / affordance-oriented
sensorimotor / enactive
active inference
multisensory causal inference
```

No family defines `Perception` universally.

---

# 42. Bayesian inference is not predictive coding

```text
BayesianInference != PredictiveCoding
```

A Bayesian computational fit does not uniquely determine implementation.

Predictive coding is a more specific implementation/theory family with additional
commitments about hierarchical predictions and error signalling.

---

# 43. Recurrence is not consciousness or prediction

```text
Recurrence != ConsciousnessByDefinition
Recurrence != PredictionByDefinition
```

Recurrent processing can be causally important for some perceptual organization while
remaining insufficient to identify phenomenology or computational objective.

---

# 44. Sensorimotor mastery is not total perception

```text
SensorimotorContingencyMastery != PerceptionTotality
```

It is strongly relevant to active exploration and sensory substitution but does not by
itself settle passive perceptual capacities, imagery or phenomenal modality.

---

# 45. Human-machine comparison is a falsifier, not identity evidence

```text
SameOutput != SameRepresentation
SameError != SameMechanism
BetterBenchmarkAccuracy != MoreHumanLikePerception
ImageClassification != SituatedPerception
```

Artificial models are useful for isolating computational sufficiency and shared
statistical vulnerabilities, but cannot establish Human mechanism identity by similarity
alone.

---

# 46. Reconnection to HF2–HF11

HF20 fills an upstream bridge rather than replacing prior foundations:

```text
HF2  owns experience / consciousness boundaries
HF3  owns attention / access / metacognition / control
HF5  owns regulation / interoception / organismic state
HF6  owns persistent learning / history-dependent change
HF8  owns general representation / belief / knowledge / understanding
HF11 owns action / control / affordance / tool-mediated execution
```

HF20 owns:

```text
world/source ↔ sampling/sensing ↔ perceptual organization/content ↔ downstream use
```

---

# 47. Cross-project ownership

```text
World:
external reality / physical state

Media:
mediated signal / representation / perceptual availability questions

Human HF20:
organism-relative sensing, sampling, integration, calibration and perceptual organization

AI / Computer:
artificial sensor/model/runtime mechanisms
```

Overlap is question-relative; none becomes universal owner of perception.

---

# 48. Durable HF20 firewalls

```text
DistalSource != ProximalSignal
ProximalSignal != ReceptorState
ReceptorState != SensoryEvidence
SensoryEvidence != PerceptualContent
PerceptualContent != Truth
PerceptualContent != Belief
Perception != Consciousness
Perception != Attention
Perception != Report
Perception != Action

Transduction != Perception
Feature != Object
Binding != Integration
Integration != FusionByDefault
Integration != Recalibration
Recalibration != MotorAdaptation
CueReliability != CommonCause
CrossModalSynchrony != CommonCauseByDefinition

ActiveSensing != ActiveInference
ActiveSensing != ActiveAlwaysBetter
BayesianInference != PredictiveCoding
Recurrence != Consciousness
Recurrence != PredictionByDefinition
Affordance != ObjectProperty
Affordance != SubjectiveBelief
SensorimotorMastery != PerceptionTotality

PhysicalCarrier != ReceptorModality != NeuralRoute != FunctionalModality != PhenomenalModality
AdultIntegrationPolicy != ChildIntegrationPolicy
MissingSense != NormalSystemMinusInput
PerceptualAccuracy_D != PerceptualAccuracy_E
Confidence != Accuracy
SameOutput != SameRepresentation
SameError != SameMechanism
ImageClassification != SituatedPerception
```

---

# 49. Foundation status

```text
HF0–HF19 reopen = false
HF20 admission = satisfied through HD1
HF20 status = complete / READY
```

The deep evidence/model owner remains HD1. HF20 is the reusable canonical compression.

---

# 50. Stop rule

Do not expand HF20 into a complete neuroscience/psychophysics encyclopedia.

Reopen HF20 only if later evidence shows that its minimum distinctions themselves cause
repeated cross-context category errors or cannot represent materially different
perceptual cases without hidden choices.

The strongest **deep** residual after HD1/HF20 is affect/emotion/appraisal. That residual
does not automatically imply HF21.
