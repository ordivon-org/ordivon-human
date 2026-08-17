---
schema_version: 1
id: human.deep-foundations.hd1
title: HD1 — Perception, Sensing, Active Sampling and Perceptual World Coupling
type: research
profile: research
lifecycle: completed
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
  - builder
updated: 2026-08-17
summary: Deep reconstruction of Human perceptual world coupling after HD0. HD1 separates distal world sources, proximal physical signals, sampling actions, receptors/transduction, sensory evidence, perceptual organization/content, awareness, attention, report and action; reconstructs active and multisensory perception; compares feedforward, Bayesian, predictive, recurrent, ecological, sensorimotor/enactive, active-inference and causal-inference model families; and pressure-tests them across modalities, development, deprivation, sensory substitution, neurological dissociation, culture and Human/machine comparison. HD1 establishes a true missing neighboring perceptual structure but does not reopen HF0–HF19.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.deep-foundations.hd0
  - human.deep-foundations.hd1.sources
  - human.deep-foundations.hd1.continuation
  - human.foundations.hf2
  - human.foundations.hf3
  - human.foundations.hf5
  - human.foundations.hf8
  - human.foundations.hf11
---
# HD1 — Perception, Sensing, Active Sampling and Perceptual World Coupling

## 0. Status and decision

HD1 began from an HD0 depth residual rather than a scheduled HF round.

The question was:

> Can HF2/HF3/HF5/HF8/HF11 represent the transformation from world/source through
> sensing and active sampling into perceptual content and action without arbitrary hidden
> choices, or is a missing neighboring foundation structure real?

HD1's answer is:

```text
The depth residual is real.
```

Existing HF rounds correctly preserve many downstream firewalls, but perception is
spread across them as an interface rather than reconstructed as its own world-coupling
process.

Therefore HD1 establishes:

```text
NextFoundationAdmissionCondition = satisfied
FoundationReopenCondition for HF0–HF19 = false
```

The result warrants a later **canonical extraction** of perception into the Human
Foundation library. HD1 itself remains the deep-research evidence owner; it does not
retroactively change the claims of HF0–HF19.

---

# 1. The first error: perception is not a single arrow from world to mind

A minimum perceptual loop must distinguish:

```text
DistalWorldState / Source
        ↓ interaction with body/sensor position
PhysicalField / Carrier
        ↓
ProximalSignalAtSensor
        ↓
Receptor / Sensor State
        ↓ transduction
SensoryEvidence
        ↓ channel-specific and cross-channel processing
PerceptualOrganization / Estimation
        ↓
PerceptualState / Content
        ↓
possible Awareness / Attention / Report
        ↓
Action / Sampling / Control
        ↓
changed sensor pose and/or world
        ↺
```

This already yields durable separations:

```text
DistalSource != ProximalSignal
ProximalSignal != ReceptorState
ReceptorState != SensoryEvidence
SensoryEvidence != PerceptualContent
PerceptualContent != ConsciousExperience
PerceptualContent != Attention
PerceptualContent != Report
PerceptualContent != Action
```

---

# 2. Distal source and proximal stimulus are not interchangeable

The same distal object/event can generate very different proximal stimulation under:

```text
illumination
viewpoint
distance
occlusion
head/eye/body movement
medium
noise
sensor orientation
```

Conversely, similar proximal stimulation can be consistent with materially different
world causes.

Therefore:

```text
SameWorldSource != SameProximalSignal
SameProximalSignal != SameWorldSource
```

Perception is partly a problem of extracting task-relevant invariants or estimating
latent causes under this many-to-many relation.

---

# 3. Sensor, receptor, modality and perceptual quality are different coordinates

A sensory modality cannot safely be identified by one feature alone.

Useful coordinates include:

```text
PhysicalCarrier_D
ReceptorClass_D
TransductionMechanism_D
Afferent/NeuralRoute_D
FunctionalInformation_D
SamplingAction_D
PhenomenalQuality_D
TaskRole_D
```

Sensory substitution provides a high-information falsifier because these coordinates can
separate.

A camera-to-tongue device can carry spatial information normally obtained visually,
while the proximal receptor and experienced quality may remain tactile. Training and
blindness can reorganize occipital involvement without making tongue receptors retinal.

Therefore:

```text
Modality_Physical != Modality_Receptor != Modality_NeuralRoute
Modality_Function != Modality_Phenomenal
InformationUsuallyVisual != VisualReceptorInputByDefinition
OccipitalRecruitment != VisualQualiaByDefinition
```

---

# 4. Transduction is not perception

Transduction converts physical interaction into biological sensory signals.

Examples differ radically:

```text
phototransduction
mechanotransduction
chemoreception
vestibular hair-cell transduction
visceral afference
```

But successful receptor activation does not itself establish:

```text
object recognition
source attribution
consciousness
attention
correct action
```

Thus:

```text
Transduction != PerceptualInference
```

---

# 5. Sensory evidence is observer-relative and noisy

The organism never receives the distal world state directly.

It receives evidence conditioned by:

```text
sensor physics
receptor sensitivity
sampling geometry
internal noise
adaptation
current physiological state
history
```

A useful generic observation model is:

```text
X_t ~ p(X | W_t, SampleAction_t, BodyState_t, SensorState_t)
```

where `X_t` is sensory evidence and `W_t` is some declared latent world property.

This is a model interface, not a claim that biological perception literally calculates
that probability distribution.

---

# 6. Sensation, percept and perceptual content need typed use

The word `sensation` is too ambiguous to carry foundational weight by itself.

It may refer to:

```text
raw-feeling vocabulary
modality-specific conscious quality
low-level sensory representation
psychophysical detection
```

HD1 therefore does not make `Sensation` a universal intermediate substance.

Use the more explicit coordinates:

```text
SensoryEvidence
PerceptualRepresentation_D
PerceptualContent_D
Experience_D
```

and state which is measured.

---

# 7. Perceptual content is not guaranteed truth

A perceptual state can be:

```text
accurate under one target
biased under another
uncertain
ambiguous
illusory
internally generated
```

Hence:

```text
PerceptualRepresentation != DistalReality
PerceptualContent != Truth
```

This reconnects directly to HF8 without reducing perception to belief.

---

# 8. Perception is not belief

Perceptual organization can influence action even when the person does not endorse a
proposition about what is present.

Likewise a person can know an illusion is an illusion and continue to experience it.

Therefore:

```text
PerceptualContent != Belief
PerceptualPersistenceUnderKnowledge != IrrationalBelief
```

---

# 9. Perception is not consciousness

HF2 already established this downstream firewall. HD1 supplies its upstream mechanism
surface.

Perceptual processing can support:

```text
discrimination
priming
action guidance
ensemble/statistical representation
```

without ordinary reportable visual experience in some paradigms.

Conversely conscious experience can contain imagery or illusion without matching a
current external source.

Therefore:

```text
Perception != ConsciousExperience
PerceptualProcessing != PerceptualAwareness
```

---

# 10. Perception is not attention

Attention can alter selection, precision, competition and downstream access, but it is
not identical to the represented perceptual property.

HD1 retains HF3:

```text
Salience != Priority != Attention != Awareness
```

and adds:

```text
PerceptualEvidence != AttentionalPriority
```

---

# 11. Perception is not report

A report requires additional:

```text
access
mapping
memory
choice
motor/language execution
```

No-report paradigms reduce some report confounds but do not produce theory-free access to
perception. A 2025 binocular-rivalry study found that the fixation shifts/saccades used
by a no-report procedure themselves changed the perceptual dynamics.

Therefore:

```text
NoReportProxy != PassiveMeasurement
MeasurementOfPerception may intervene on Perception
```

This is a direct instance of Human reflexivity.

---

# 12. Perception is not action, but action can be constitutive of evidence acquisition

Some perceptual tasks can be performed passively. Others require exploratory action to
create useful evidence.

Examples:

```text
eye movements
head movement
sniffing
whisking in other species
finger exploration
locomotion
```

HD1 distinguishes:

```text
ActionForWorldChange
ActionForEvidenceAcquisition
ActionForCalibration
ActionForReport
```

They can overlap but are not equivalent.

---

# 13. Active sensing

Define minimally:

```text
ActiveSensing_D
= action that materially changes the distribution/quality/location/timing
  of sensory evidence acquired for perceptual task D
```

This allows:

```text
SampleAction_t
→ Evidence_{t+1}
→ PerceptualUpdate_{t+1}
→ SampleAction_{t+1}
```

Human olfactory sniffing is an unusually clear case because sniff dynamics carry
fine-grained information about perceived odour properties and are modulated in real time.

---

# 14. Active sensing is not active inference

This firewall is essential.

```text
ActiveSensing
!= ActiveInference
```

Active sensing is a phenomenon/functional description.

Active inference is a specific formal/theoretical family connecting perception and action
through a generative model and free-energy/prediction-error machinery.

Evidence for active sensing therefore does not establish active inference.

---

# 15. Active sensing is not always superior to passive sensing

The generic claim:

```text
ActivePerception > PassivePerception
```

fails.

Classic tactile letter-recognition work found near-equivalent active and passive
performance under controlled conditions, even though movement strategy differed.
Other tasks show advantages from active movement, predictable movement or action-feedback
congruency.

Therefore:

```text
ActiveBenefit_D != ActiveBenefit_E
```

The benefit must be explained by the information and control structure of the task.

---

# 16. Sampling policy is part of the perceptual system state

Sampling can depend on:

```text
current uncertainty
goal
task relevance
learned regularity
body constraints
expected information gain
habit
cost
```

Thus the observation process is endogenous:

```text
WhatYouObserve
partly depends on
HowYouSample
```

This is a major reason passive dataset perception is not a complete model of situated
Human perception.

---

# 17. Feature detection is not object perception

Local sensory features can include:

```text
orientation
frequency
colour
motion
onset
texture
pressure
pitch
odour dimensions
```

Object/event perception requires organization beyond merely detecting features.

Thus:

```text
FeaturePresence != Objecthood
```

---

# 18. Binding and integration are different

`Binding` asks which features/signals belong together.

`Integration` asks how multiple estimates/evidence sources are combined once treated as
relevant to a common variable/source.

Therefore:

```text
Binding != Integration
```

and:

```text
Integration != AlwaysFuse
```

The organism must sometimes segregate signals.

---

# 19. Multisensory causal inference

A central multisensory problem is:

```text
Do signals x_A and x_B arise from one cause or multiple causes?
```

Bayesian causal-inference models explicitly separate:

```text
C = common cause
C = separate causes
```

and combine integration/segregation estimates according to inferred causal structure.
Human audiovisual EEG work supports temporally evolving representations consistent with
this family.

This yields:

```text
CueCombination != CueFusionByDefault
CrossModalSynchrony != CommonCauseByDefinition
```

---

# 20. Causal-inference computation does not require one neural implementation

A model can describe behavioural computation without uniquely specifying mechanism.

Artificial feedforward networks trained on visual-vestibular causal inference can develop
representational properties resembling known biological patterns and reproduce key
behavioural effects.

Therefore:

```text
BayesianBehavioralFit != ExplicitBayesianNeuron
CausalInferenceFunction != RecurrentImplementationByDefinition
```

---

# 21. Reliability / precision weighting is conditional, not universal fusion

When signals are judged to share a cause, more reliable signals often exert greater
influence.

But reliability weighting alone does not solve:

```text
which signals belong together?
which variable is being estimated?
which reference frame?
```

Hence:

```text
ReliabilityWeighting != CompleteMultisensoryPerception
```

---

# 22. Recalibration is not integration

Integration affects current combined estimates.

Recalibration changes later unimodal estimates or mapping after persistent discrepancy.

Visuo-proprioceptive experiments demonstrate that these can be measured separately and
can have different retention profiles.

Thus:

```text
Integration != Recalibration
Recalibration != MotorAdaptation
```

---

# 23. Perceptual learning is not sensory exposure

Training can change:

```text
sensitivity
precision
binding windows
causal priors
sampling policy
category boundary
recalibration
```

but these changes are not one process.

Therefore:

```text
PerceptualLearning_D != PerceptualLearning_E
Exposure != PerceptualLearningByDefinition
```

HF6 remains the general persistent-change owner.

---

# 24. Development changes the architecture of cue use

Adult multisensory behaviour must not be projected backward onto children.

Visual-haptic work shows young children can show modality dominance rather than adult-like
reliability-weighted integration, with integration changing substantially across later
childhood.

Sight-restoration work after early deprivation shows adult-like multisensory weighting can
still develop after prolonged visual deprivation when informative multisensory experience
becomes available.

Therefore:

```text
AdultIntegrationPolicy != ChildIntegrationPolicyByDefinition
DevelopmentalAge != FixedMechanism
EarlyAbsence != PermanentImpossibilityByDefinition
```

---

# 25. Sensory history changes later perceptual organization

Visual deprivation, restored sight, training and repeated cue discrepancy alter how
signals are weighted and routed.

Therefore the perceptual system is history-dependent:

```text
PerceptualPolicy_{t+1}
= U(PerceptualPolicy_t, SensoryHistory_t, Action_t, Error_t, Context_t)
```

This is a direct consumption of HF6, not a replacement for it.

---

# 26. Cross-cultural variation is real but does not license arbitrary perception

Classic cross-cultural geometric-illusion studies report substantial population
variation. Later intra-cultural tests also show that simple single-factor explanations
such as a universal `carpentered world` account are insufficient.

Therefore:

```text
PerceptualUniversalClaim requires transport evidence
CrossCulturalDifference != NoSharedPerceptualConstraint
```

HD1 does not build a culture theory; it records culture/ecology as a transport coordinate.

---

# 27. Perceptual constancy is a transformation problem

Stable useful perception frequently requires treating changing proximal signals as
properties of a persisting distal source.

Examples include approximate constancy across:

```text
viewpoint
illumination
distance
self-motion
```

Thus:

```text
Constancy != SameProximalSignal
```

Constancy can be treated through multiple model families and is not evidence for one
specific inference architecture.

---

# 28. Illusions are model discriminators, not simply perceptual failures

Define an illusion only relative to a declared target/property/measurement:

```text
Illusion_D
= systematic divergence between perceptual estimate/content and declared target D
  under a specified stimulus/context
```

Some Bayesian/efficient-decoding models can explain classes of illusions as consequences
of uncertainty and learned environmental statistics.

But no result supports:

```text
AllIllusions = BayesianOptimality
```

Different illusions recruit different mechanisms; even V1 representations differ across
illusion classes.

---

# 29. Imagery, illusion and externally driven perception are not one process

Laminar human fMRI shows that illusory and imagined visual content can recruit partially
different V1 depth profiles, despite both involving non-veridical/currently absent
features.

Therefore:

```text
Imagery != Illusion != ExternalPerception
```

Shared content does not establish shared generative mechanism.

---

# 30. Feedforward processing is real but not sufficient as universal perception ontology

Fast feedforward hierarchies can support substantial sensory discrimination and object
information.

They provide a strong benchmark and can solve some causal-inference-like tasks.

But human causal perturbation studies show that some perceptual organization requires
later feedback/recurrent processing.

Therefore:

```text
FeedforwardCapability != CompletePerception
```

without claiming that every percept requires the same recurrent loop.

---

# 31. Recurrent processing is a family, not a magic word

Human TMS work on contour integration finds an earlier critical window in higher visual
area V3B than in V1/V2, consistent with feedback being necessary for full contour
integration.

Recent EEG/fMRI work using backward masking also shows recurrence reshaping visual
representations across time and cortical levels.

But:

```text
Recurrence != ConsciousnessByDefinition
Recurrence != PredictionByDefinition
Recurrence != SameCircuitAcrossTasks
```

---

# 32. Predictive coding is not Bayesian perception in general

`Bayesian perceptual inference` is a computational family about uncertainty, likelihoods
and priors.

`Predictive coding` is a more specific family about how hierarchical predictions and
prediction errors may implement such inference.

Therefore:

```text
BayesianInference != PredictiveCoding
```

Audiovisual speech prediction-error results are compatible with predictive-coding ideas,
but do not establish universal predictive coding.

---

# 33. Ecological / affordance-oriented models preserve a distinct explanatory target

Ecological work emphasizes lawful information in organism-environment relations and
possibilities for action.

Classic stair-climbing experiments show perceived climbability scaling with
organism-environment fit rather than absolute stair geometry alone; aging work shows
strength/flexibility can improve the scaling beyond leg length alone.

Therefore:

```text
Affordance_D
= Relation(AgentCapability, Environment, Task)
```

and:

```text
Affordance != ObjectPropertyOnly
Affordance != SubjectiveBeliefOnly
```

This is compatible with HF11 and need not be reduced to an internal posterior variable.

---

# 34. Sensorimotor / enactive models preserve another distinct target

Sensorimotor accounts emphasize regularities linking:

```text
action
→ change in sensory input
```

and practical mastery of those contingencies.

Sensory substitution is especially relevant because task-relevant distal structure can be
learned through a new sensorimotor mapping.

But successful sensory substitution does not prove:

```text
Perception = SensorimotorMasteryTotality
```

because passive perception, internally generated percepts and modality-specific
phenomenology still require explanation.

---

# 35. Active inference remains a serious rival, not a foundation axiom

Active inference proposes a unified generative-model treatment of perception/action.
It has produced detailed formal accounts and testable applications, including
visuo-proprioceptive conflict and motor-control domains.

However its broad vocabulary overlaps many phenomena that alternative models also
explain.

HD1 therefore requires:

```text
ActiveInferenceClaim
→ unique prediction
→ alternative model comparison
→ empirical discrimination
```

before upgrading the framework.

---

# 36. Body perception and proprioception are estimates, not transparent body truth

HF11 already established:

```text
PhysicalBodyState != EstimatedBodyState
```

HD1 generalizes this as a perceptual rule.

Visuo-proprioceptive discrepancy causes integration and recalibration; multiple visual
signals can exert superposed influence.

Hence:

```text
ProprioceptiveEvidence != ExactBodyState
BodyPercept != BiologicalBodyState
```

---

# 37. Interoception is perceptual but not one global ability

HF5 reconstructed interoception as signal/representation/experience rather than direct
body readout.

A 2026 psychophysical study comparing cardiac and respiratory interoception finds little
cross-domain correlation in sensitivity/precision/metacognitive efficiency, despite some
shared confidence tendency.

Therefore:

```text
InteroceptiveAbility_D != InteroceptiveAbility_E
```

and a global `body awareness` scalar is not warranted.

---

# 38. Vestibular / visual perception demonstrates source ambiguity

Visual motion can arise from:

```text
self-motion
scene motion
both
```

while vestibular evidence carries different information.

This makes visual-vestibular self-motion a canonical causal-inference problem and
illustrates:

```text
SameOpticFlow != SameWorldCause
```

---

# 39. Touch demonstrates reference-frame construction

Active haptic shape perception accumulates tactile input across time and movement.
The same local tactile signal can correspond to different external positions depending on
body configuration and movement.

Therefore:

```text
LocalTactileInput != ExternalSpatialLocation
```

Perception must sometimes transform among receptor-, limb-, trunk-, object- and world-
relative coordinates.

---

# 40. Reference frame is typed

Do not ask for one `PerceptualCoordinateSystem`.

Possible task-relative frames include:

```text
retinotopic
head-centred
body-centred
limb-centred
object-centred
allocentric / scene-relative
```

A system may transform or combine frames.

Therefore:

```text
ReferenceFrame_D != ReferenceFrame_E
```

---

# 41. Perceptual accuracy is endpoint-specific

A person can be accurate at:

```text
detection
localization
discrimination
identification
source attribution
action guidance
confidence calibration
```

while inaccurate at another.

Thus:

```text
PerceptualAccuracy_D != PerceptualAccuracy_E
```

and:

```text
TaskSuccess != VeridicalPerceptTotality
```

---

# 42. Confidence is not perceptual accuracy

HF3's metacognitive firewall applies directly:

```text
Confidence != Accuracy
```

HD1 adds that sensory sensitivity, sensory precision and metacognitive efficiency can
dissociate across domains.

---

# 43. Detection, discrimination, estimation and recognition are different tasks

A minimal task taxonomy is:

```text
Detection: is something present?
Discrimination: are A and B different / which category?
Estimation: what value/location/property?
Recognition/Identification: what source/object/event?
Segmentation: which evidence belongs to which entity/event?
SourceAttribution: what caused the evidence?
AffordanceEstimation: what actions are possible?
```

Do not infer one from another.

---

# 44. Recognition is downstream of sensing but not purely perceptual by universal definition

Recognition can consume:

```text
perceptual evidence
memory
concepts
language
task goals
```

Thus the border between HD1 and HF8 is intentionally typed rather than territorial.

HD1 owns sensory/world coupling and perceptual organization; HF8 owns general
representation/knowledge/concept/understanding.

---

# 45. Perceptual object is not necessarily physical object

Perceptual organization can group evidence into:

```text
surface
object
event
agent
body part
scene
```

The grouping may differ from physical individuation.

Therefore:

```text
PerceptualObject_D != PhysicalObjectByDefinition
```

This is important for occlusion, camouflage, ambiguous figures and multisensory events.

---

# 46. Occlusion shows why current sensory evidence is not the whole perceived state

Tracking an object behind an occluder requires continuity across missing current evidence.

Therefore:

```text
CurrentSensoryEvidence != CompletePerceptualState
```

History and object/event models can maintain perceptual organization through temporary
absence.

---

# 47. Ambiguous and bistable perception separates stimulus from percept

Binocular rivalry is a particularly clean case:

```text
approximately stable physical stimulation
→ alternating perceptual dominance
```

Recent 7T fMRI finds local V1 competition plus higher-level parietal feedback contributing
to perceptually coherent resolution.

Thus:

```text
SameStimulus != SamePercept
```

and perceptual competition can span multiple levels.

---

# 48. Sensory substitution separates functional information from native channel

After training, people can use tactile or auditory substitutions for tasks normally
performed visually, including spatial/affordance judgments.

This demonstrates:

```text
TaskInformation != NativeSensorModality
```

while preserving:

```text
SuccessfulSubstitution != NativePhenomenologyByDefinition
```

---

# 49. Blindness / deprivation is not simply missing input

Visual deprivation can change routing, calibration and use of other modalities.
Short-term blindfolding can rapidly recruit occipital cortex for touch; congenital or
long-term blindness can produce different cross-modal organization.

Therefore:

```text
MissingChannel
→ system reorganization
```

rather than merely:

```text
NormalSystem - OneInput
```

---

# 50. Blindsight pressure

Lesion and masking work shows that objective visual discrimination/action-related effects
can dissociate from ordinary reported seeing.

But lesion-induced blindsight and transient suppression in neurologically healthy people
need not share identical pathways because chronic lesions can produce plastic changes.

Therefore:

```text
BlindsightPhenotype != OneUniversalMechanism
PerformanceWithoutReport != FullNormalPerception
```

---

# 51. Measurement is an intervention surface

HD1 generalizes the no-report result:

```text
EyeMovementInstruction
HeadRestraint
Fixation
ButtonMapping
ExplorationRestriction
StimulusTiming
```

can all alter perceptual sampling or dynamics.

Therefore every perceptual measurement should specify:

```text
MeasuredConstruct
MeasurementAction
SamplingRestriction
PossibleInterventionEffect
```

---

# 52. Human-machine comparison is a model test, not identity evidence

Artificial networks can:

```text
predict some human perceptual errors
show some similar adversarial biases
solve multisensory causal-inference tasks
```

Yet shared error patterns do not prove shared implementation.

Conversely machine failures can expose which invariances a human system has acquired.

Retain:

```text
SameOutput != SameRepresentation
SameError != SameMechanism
BetterBenchmarkAccuracy != MoreHumanLikePerception
```

---

# 53. Machine perception also makes the embodiment question explicit

A static image classifier receives a dataset sample.
A robot chooses sensor pose, moves, obtains temporal evidence and changes the scene.

Thus:

```text
ImageClassification != SituatedPerception
```

The relevant Human×AI comparison depends on whether the artificial system has:

```text
active sensing
persistent state
multimodal sensors
body/world interaction
calibration
uncertainty tracking
```

---

# 54. Competing model family F1 — feedforward / feature-computation

Core strength:

```text
fast hierarchical transformations
feature extraction
recognition benchmarks
```

Survives for early and many task-relevant computations.

Fails as a universal ontology where later feedback, active sampling, persistent context or
multisensory causal structure materially changes the percept.

Disposition: **retain as essential benchmark, reject Feedforward=PerceptionTotality**.

---

# 55. F2 — Bayesian perceptual inference

Core grammar:

```text
posterior ∝ likelihood × prior
```

Strength:

```text
uncertain measurements
cue weighting
ambiguous latent causes
many illusion/estimation phenomena
```

Limits:

```text
behavioural optimal-observer fit does not identify neural implementation;
priors/likelihoods can be flexible descriptions;
not every perceptual task requires an explicit Bayesian interpretation.
```

Disposition: **retain computational family; reject BayesianFit=NeuralOntology**.

---

# 56. F3 — predictive coding / predictive processing

Strength:

```text
hierarchical top-down prediction
bottom-up mismatch/error
context effects
feedback-sensitive phenomena
```

Limits:

```text
prediction-error signatures can have alternative explanations;
implementation details vary;
broad framework risks post-hoc flexibility.
```

Disposition: **retain rival implementation family; demand discriminative predictions**.

---

# 57. F4 — recurrent / interactive processing

Strength:

```text
contour integration
competition resolution
context-dependent refinement
feedback to early sensory areas
```

Limit:

```text
recurrence by itself does not specify represented probability, ecological variable,
phenomenal status or action policy.
```

Disposition: **retain architectural family; recurrence is not explanatory closure**.

---

# 58. F5 — ecological / affordance-oriented perception

Strength:

```text
organism-environment relation
action-scaled information
lawful task constraints
```

It directly resists object-property-only accounts.

Limit:

```text
not every recognition/illusion/imagery phenomenon is naturally exhausted by an
affordance description;
what counts as directly specified information is task-dependent and empirically testable.
```

Disposition: **retain action-relative world-coupling family**.

---

# 59. F6 — sensorimotor / enactive

Strength:

```text
active exploration
sensorimotor contingencies
sensory substitution
embodied calibration
```

Limit:

```text
passive perceptual capacities and conscious-quality differences prevent reducing all
perception to overt sensorimotor mastery.
```

Disposition: **retain for active/embodied perception; reject universal reduction**.

---

# 60. F7 — active inference

Strength:

```text
formal coupling of hidden-state inference, precision and action
explicit active sampling/control interpretation
```

Limit:

```text
great breadth makes empirical discrimination essential;
many observed behaviours are also predicted by control, Bayesian decision, RL or
sensorimotor models.
```

Disposition: **retain formal rival; no universal promotion**.

---

# 61. F8 — multisensory causal inference

Strength:

```text
integration versus segregation
uncertain common-cause inference
reliability-weighted estimates
```

Limit:

```text
not a complete theory of unisensory encoding, phenomenology, active sampling or object
recognition.
```

Disposition: **retain as a strong bridge model for multisensory organization**.

---

# 62. No winning universal theory

The evidence supports a plural architecture:

```text
feedforward transforms
+ recurrent interactions
+ uncertainty-sensitive estimation
+ causal-source arbitration
+ organism-environment scaling
+ active sampling
+ learning/recalibration
```

can all be real in different domains.

This does not imply an additive universal brain equation.

---

# 63. Cross-context falsifier matrix

| ID | Context | Collapse attacked | Surviving structure |
|---|---|---|---|
| P01 | same object under viewpoint/lighting change | source = proximal signal | distal/proximal separation |
| P02 | ambiguous figure/binocular rivalry | same stimulus = same percept | percept is state/context dependent |
| P03 | visual illusion | percept = physical property | target-relative divergence |
| P04 | imagery vs illusion | nonveridical content = one mechanism | internally generated routes differ |
| P05 | blindsight-like discrimination | task sensitivity = awareness | processing/access/experience separate |
| P06 | no-report rivalry with fixation shifts | proxy = passive measure | measurement changes sampling/percept |
| P07 | sniff modulation by odour percept | sensing = passive intake | sampling action is endogenous |
| P08 | active vs passive tactile letter recognition | active always better | active benefit is task-specific |
| P09 | predictable movement improves tactile precision | movement only gates sensation | bias and precision can change differently |
| P10 | visual-auditory conflict | multiple cues = fuse | causal inference / segregation |
| P11 | visual-vestibular self-motion conflict | optic flow = self-motion | source ambiguity |
| P12 | visuo-proprioceptive mismatch | proprioception = body truth | integration + recalibration |
| P13 | multiple visual cues + proprioception | strongest cue wins | superposed/contextual weighting possible |
| P14 | child visual-haptic integration | adult cue rule = Human rule | developmental policy change |
| P15 | restored sight after cataract | critical period = irreversible closure | later multisensory learning possible |
| P16 | tactile sensory substitution | modality = physical source only | modality coordinates dissociate |
| P17 | occipital TMS after substitution | cortical area = fixed phenomenal modality | developmental routing matters |
| P18 | action-scaled stair perception | environment property = affordance | agent-environment relation |
| P19 | crutch affordance | biological body = capability boundary | tool-integrated action system |
| P20 | haptic spatial reconstruction | skin coordinate = world coordinate | reference-frame transformation |
| P21 | cross-cultural illusion differences | one population = universal | transport coordinate required |
| P22 | recurrent contour integration TMS | feedforward = complete vision | task-specific feedback necessity |
| P23 | feedforward network solves causal inference | causal inference = explicit recurrence | computation != implementation |
| P24 | machine predicts human gloss errors | similar error = same mechanism | model similarity is partial |
| P25 | human/machine adversarial effects | adversarial = machine-only | shared susceptibility can coexist with differences |
| P26 | cardiac vs respiratory interoception | interoception = scalar | domain-specific abilities |
| P27 | occlusion tracking | current evidence = current percept | persistence/model-based continuity |
| P28 | perceptual learning | current performance = fixed sensor | history updates perceptual policy |
| P29 | audiovisual recalibration | integration = learning | current fusion != persistent recalibration |
| P30 | action feedback improves affordance calibration | perception = pre-action readout | action can calibrate perception |

The matrix rejects the naive collapses while preserving a common world-coupling grammar.

---

# 64. Minimum retained perceptual grammar

HD1's strongest reconstruction is:

```text
WorldState_t
+ Body/SensorState_t
+ SamplingPolicy_t
        ↓
SamplingAction_t
        ↓
PhysicalInteraction / ProximalSignals_t
        ↓
Transduction_t
        ↓
SensoryEvidence_t
        ↓
PerceptualOrganization_t
  ├─ feature extraction
  ├─ source/causal attribution
  ├─ integration/segregation
  ├─ reference-frame transform
  ├─ uncertainty/precision
  ├─ object/event/body organization
  └─ temporal continuity
        ↓
PerceptualState_t / Content_t
        ├────────→ possible Experience / Awareness
        ├────────→ Attention / priority update
        ├────────→ Memory / Representation / Recognition
        └────────→ Action / control / new sampling
                         ↓
                 World/SensorState_{t+1}
                         ↺

History / development / learning
        ↘ update sampling, calibration, priors, precision, mappings and organization
```

This is a typed grammar, not one neural model.

---

# 65. Core HD1 firewalls

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

PhysicalCarrier != ReceptorModality != NeuralRoute != FunctionalModality != PhenomenalModality
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
SamplingAction != WorldChangingActionByDefinition
BayesianInference != PredictiveCoding
Recurrence != Consciousness
Recurrence != PredictionByDefinition
Affordance != ObjectProperty
Affordance != SubjectiveBelief
SensorimotorMastery != PerceptionTotality

PerceptualAccuracy_D != PerceptualAccuracy_E
Confidence != Accuracy
TaskSuccess != VeridicalPerceptionTotality
Illusion != IrrationalityByDefinition
Imagery != Illusion != ExternallyDrivenPerception

AdultIntegrationPolicy != ChildIntegrationPolicy
MissingSense != NormalSystemMinusInput
SameOutput != SameRepresentation
SameError != SameMechanism
ImageClassification != SituatedPerception
```

---

# 66. Reconnection to HF2

HF2 remains correct:

```text
PerceptualProcessing != Experience
Experience != Report
```

HD1 supplies the missing upstream perceptual process that HF2 intentionally treated as
input.

No HF2 claim must be reopened.

---

# 67. Reconnection to HF3

HF3 remains the owner of selection/access/metacognition/control.

HD1 adds the evidence-generation surface that attention selects over and sometimes helps
actively acquire.

```text
SamplingPolicy can be attention-sensitive
but Sampling != Attention
```

No HF3 reopening required.

---

# 68. Reconnection to HF5

HF5's interoception becomes one perceptual family with important special constraints:
internal sources, modality-specific channels and regulation loops.

HD1 reinforces rather than contradicts:

```text
InternalPhysicalState != InteroceptiveSignal != InteroceptiveRepresentation != Experience
```

No HF5 reopening required.

---

# 69. Reconnection to HF8

HD1 stops at perceptual organization/content and task-specific recognition interfaces.

HF8 continues into:

```text
belief
knowledge
concept
schema
mental model
understanding
```

Therefore:

```text
PerceptualRepresentation != GeneralEpistemicState
```

No HF8 reopening required.

---

# 70. Reconnection to HF11

HF11 already contains:

```text
Perception → Control → Action → changed sensory evidence → recalibration
```

HD1 expands the perception side and distinguishes evidence-acquisition actions from world-
changing task actions.

No HF11 reopening required.

---

# 71. Cross-project boundary with Media

Media can own signal/media/perceptual availability questions for mediated signals.

Human owns the organism-specific coupling among:

```text
body/sensor state
active sampling
sensory transduction
multisensory organization
perceptual learning
perception-action coupling
```

The overlap is intentional; ownership differs by question.

---

# 72. Cross-project boundary with World

World owns external physical reality/topology/resources.

Human perception owns the relation:

```text
WorldState
→ evidence available to this organism in this state and sampling policy
→ perceptual organization
```

Human perception does not redefine world truth.

---

# 73. Cross-project boundary with AI / Computer

Computer/AI projects own artificial sensors/models/runtime mechanisms.

Human uses artificial systems as:

```text
comparators
formal models
falsifiers
assistive/substitution systems
joint-perception components
```

Artificial similarity never grants Human-ontology identity.

---

# 74. Foundation admission test

HF19's `NextFoundationAdmissionCondition` is now checked.

```text
1. Repeated residual?             yes
   HF2/HF3/HF5/HF8/HF11 repeatedly consume perception as an unexplained interface.

2. Neighboring structure?        yes
   Source/signal/sampling/transduction/evidence/organization/percept cannot be represented
   by merely choosing one existing HF projection without hidden choices.

3. Decision/explanation value?   yes
   The distinctions change interpretation of awareness, measurement, active sensing,
   disability, sensory substitution, learning and Human×AI comparison.

4. Not engineering debt?         yes
   This is scientific representational debt.

5. Not terminology churn?        yes
   Cross-modal/developmental/lesion/active-sensing falsifiers force the distinctions.

6. Evidence pressure?            yes
   Multiple independent model families and modalities require the separation.

7. Boundary safety?              yes
   The reconstruction preserves experience, authority, personhood and normativity
   boundaries.
```

Therefore:

```text
NextFoundationAdmissionCondition = true
```

---

# 75. Reopen audit

No existing foundation is contradicted.

```text
A repeated category error caused by frozen claim?     no
B primary evidence falsifies frozen HF claim?         no
C missing neighboring distinction?                    yes, as extension not repair
D contradiction across frozen rounds?                 no
E consumer failure due existing foundation wording?   no
F normative authority leak?                           no
```

Disposition:

```text
Do not reopen HF0–HF19.
Admit a new neighboring perception foundation extraction.
```

---

# 76. What HD1 does not settle

HD1 does not settle:

```text
one neural code of perception
one universal Bayesian prior
one theory of phenomenal consciousness
one theory of objecthood
one theory of sensory modality identity
one universal active-inference model
one complete theory of perceptual development
one culture-free perceptual policy
```

These remain typed/open.

---

# 77. Strong residual after HD1

Perception creates a further bridge pressure:

```text
Perceived internal/external state
+ bodily regulation
+ learned significance
+ social/contextual appraisal
→ valenced affective state
→ action allocation
```

HF4 and HF5 contain important parts, but `Emotion / Affect / Mood / Appraisal` remain
interface-rich and mechanism-thin in the same sense that perception was before HD1.

This is now the strongest candidate for the next **deep route**, subject to the same
guard against automatic foundation promotion.

---

# 78. Final HD1 compression

Human perception is best retained as:

> a history-dependent, body- and sensor-relative process that actively or passively
> acquires partial evidence, organizes it into uncertain task-relevant perceptual states,
> arbitrates source/integration structure, and participates in a closed loop with action,
> learning and the external world.

In compact form:

```text
World
↔ Sampling / Body
↔ Sensing
↔ Perceptual Organization
↔ Perceptual State
↔ Action
↔ World

with History / Development updating the loop.
```

The result is deeper than `World → Percept` but intentionally weaker than one universal
perceptual theory.
