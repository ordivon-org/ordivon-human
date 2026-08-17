---
schema_version: 1
id: human.foundations.hf6
title: HF6 — Adaptation, Learning, Plasticity, Habituation, Sensitization, Resilience, Development and Aging
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
summary: HF6 reconstructs history-dependent Human change. It separates transient state change from persistent adaptation; practice performance from learning, retention and transfer; plasticity capacity from actual plastic change; habituation from fatigue, tolerance and extinction; sensitization by response channel; resilience by exposure/outcome/trajectory; developmental stage from chronological age; and aging from uniform decline. It introduces a typed ChangeProfile and transition-function update grammar. The next residual is memory: retention, forgetting, retrieval, interference, generalization and transfer.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
  - HF6
related:
  - human.foundations.hf5
  - human.foundations.hf6.sources
  - human.foundations.hf6.continuation
---
# HF6 — Adaptation, Learning, Plasticity, Habituation, Sensitization, Resilience, Development and Aging

## 0. Status and question

HF5 ended with:

```text
State_{t+1} = F_t(State_t, Input_t, Action_t)
```

and the observation that experience/history can change the future transition
function itself:

```text
F_t → F_{t+1}
```

HF6 asks:

> **What counts as persistent Human change, what changes, how long does it persist,
> how broadly does it transfer, when is it adaptive, and how do repeated exposure,
> development and aging alter the future response architecture of the Human?**

HF6 attacks these common collapses:

```text
state change = adaptation
practice gain = learning
learning = plasticity
response decrement = habituation
extinction = erasure
reduced drug response = habituation
strong stress response = low resilience
development = improvement
aging = decline
```

None survives cross-domain testing.

---

# 1. The formal HF6 move: parameters can change

HF5 modeled a changing state under a transition rule.
HF6 introduces an explicit parameter/history layer:

```text
State_{t+1} = F_{Theta_t}(State_t, Input_t, Action_t)
```

and:

```text
Theta_{t+1}
= U(Theta_t, Experience_t, Outcome_t, InternalState_t, Context_t)
```

`Theta` is not one biological parameter. It is a placeholder for whatever
persistent properties of the relevant Human subsystem alter future response:

```text
learned association
policy
sensorimotor mapping
synaptic/functional organization
muscle enzyme profile
thermoregulatory response
habit strength
stress-response tendency
strategy
skill
reserve
```

The foundation distinction is:

```text
StateChange
!=
TransitionFunctionChange
```

A temporary heart-rate increase is a state change.
A repeated-exposure change that alters the response to later heat/stress/training
may reflect a changed transition function.

---

# 2. Persistent change needs a ChangeProfile

HF6 rejects:

```text
changed = yes/no
```

A useful research representation is:

```text
ChangeProfile_D(H, intervention/history) = {
  target domain,
  induction history,
  onset latency,
  magnitude,
  persistence,
  specificity,
  transfer/generalization,
  reversibility,
  decay trajectory,
  reacquisition/savings,
  structural/functional evidence,
  performance consequence,
  cost/tradeoff,
  developmental stage
}
```

Two changes with equal immediate magnitude can differ radically in persistence or
transfer.

Thus:

```text
SameImmediateGain
!= SamePersistentChange
```

---

# 3. Adaptation is qualifier-required

`Adaptation` has several incompatible technical uses.

HF6 separates at least:

```text
A1 CurrentCompensation
A2 WithinLifetimePhysiologicalAdaptation
A3 LearnedBehavioralAdaptation
A4 Injury-related Reorganization / Compensation
A5 DevelopmentalAdaptation
A6 EvolutionaryAdaptation
```

HF6 focuses primarily on A2–A5.

Evolutionary adaptation concerns population-level heritable change across
generations and must not be silently imported into within-lifetime Human change.

Therefore:

```text
EvolutionaryAdaptation
!= WithinLifetimeAdaptation
```

---

# 4. Compensation is not persistent adaptation

Suppose heat exposure triggers sweating immediately.

That response may be:

```text
CurrentRegulatoryCompensation
```

rather than evidence that the Human has heat-acclimated.

If repeated heat exposure changes later sweating/circulatory/mitochondrial
responses, that supports a persistent adaptation claim.

Therefore:

```text
AcuteCompensation
!= PersistentAdaptation
```

A persistence criterion must be declared.

---

# 5. Adaptation is not necessarily improvement

Everyday language often makes `adaptation` positive.

HF6 rejects this.

A history-dependent change can:

```text
improve current fit
reduce future cost
increase tolerance
increase vulnerability
produce a tradeoff
be locally useful but globally costly
```

Examples include chronic stress changes, sensitization and some compensatory
strategies after injury.

Therefore:

```text
Adaptation != Improvement
Adaptation != WelfareGain
```

Use `adaptive for D under context C/timescale T` when benefit is claimed.

---

# 6. Learning begins by separating performance from change

A Human may perform better during practice because of:

```text
warm-up
strategy discovery
incentive
feedback
attention
arousal
short-lived motor priming
```

without retaining the gain.

Conversely, latent learning may not be fully expressed during acquisition.

Therefore:

```text
PracticePerformance
!= Learning
```

and:

```text
CurrentPerformance
!= Stored/PersistentCapability
```

---

# 7. Learning: working definition

HF6 uses:

> **Learning = experience-dependent change that alters later representation,
> inference, prediction, action policy or performance potential beyond the
> transient state generated by the experience itself.**

This definition deliberately requires later consequence.

It does not require:

```text
conscious awareness
verbal knowledge
immediate improvement
one neural mechanism
```

and does not include every maturational or injury-induced change.

Thus:

```text
Learning != ConsciousLearning
Learning != Maturation
Learning != AnyPlasticChange
```

---

# 8. Learning must be decomposed temporally

HF6 separates:

```text
Acquisition
OnlinePerformanceChange
Stabilization / Consolidation
Retention
Retrieval
Transfer / Generalization
Relearning / Savings
```

The sequence is not mandatory or strictly linear.

But a claim like:

```text
“training taught skill X”
```

is underspecified without knowing which of these were measured.

---

# 9. Acquisition is not retention

Acquisition asks:

```text
Did performance/representation change during exposure/practice?
```

Retention asks:

```text
Is a relevant change still detectable after the induction state and delay?
```

Therefore:

```text
Acquisition != Retention
```

A training protocol can produce large acquisition gains and poor retention, or
modest acquisition with strong later retention.

---

# 10. Consolidation is not mere time passage

Motor-memory experiments show that recently learned behavior can change in
vulnerability to interference after practice ends.

HF6 therefore uses:

```text
Consolidation
= post-acquisition process/change that increases stability, changes later
  expression, or reorganizes the retained representation
```

without assuming every task improves offline.

Thus:

```text
Consolidation != ElapsedTime
```

and:

```text
Consolidation != GuaranteedOfflineEnhancement
```

Some evidence is better described as stabilization than enhancement.

---

# 11. Retention is endpoint-specific

A skill can retain:

```text
accuracy
speed
strategy
coordination
conceptual rule
confidence
```

at different rates.

Therefore:

```text
Retention_D != Retention_E
```

A single post-test score cannot automatically represent all retained change.

---

# 12. Transfer is not learning itself

HF6 defines transfer as:

> **the effect of prior learning/adaptation on performance or learning in a
> materially different condition.**

Possible transfer dimensions include:

```text
stimulus
retinal/spatial location
response effector
context
task
modality
domain
novel problem
```

Thus use:

```text
Transfer_D→E
```

rather than `transfer=yes`.

---

# 13. Near transfer and far transfer are not equivalent

A trained visual orientation may transfer to a new location but not a new task.
A motor sequence may transfer between hands in one coordinate representation but
not another.

Therefore:

```text
NearTransfer
!= FarTransfer
```

and:

```text
Transfer_stimulus
!= Transfer_task
!= Transfer_domain
```

A broad capability claim requires the relevant transfer surface to be tested.

---

# 14. Specificity is not absence of plasticity

Highly specific learning can be a genuine persistent change.

Perceptual-learning studies show that training can become more specific with
increased difficulty or extensive practice.

Therefore:

```text
Specificity
!= NoLearning
```

and:

```text
Specificity
!= LowPlasticity
```

A system can be highly plastic while changing only the trained relation.

---

# 15. More training does not guarantee broader capability

One visual-learning study found extensive training increased specificity relative
to briefer training.

Hence:

```text
MorePractice
!= MoreTransfer
```

This is a major Human-learning boundary.

Training intensity can optimize:

```text
trained performance
```

while reducing or failing to increase:

```text
generalization
```

depending on task design.

---

# 16. Plasticity needs two meanings separated

`Plasticity` commonly means either:

```text
PlasticityCapacity
= ability/range/rate with which a system can change under specified induction

PlasticChange
= an observed structural/functional change that occurred
```

HF6 requires the distinction:

```text
PlasticityCapacity != PlasticChange
```

A failed induction protocol does not prove absence of plasticity capacity.

Likewise one observed neural change does not quantify total future plasticity.

---

# 17. Neural plasticity is not learning

Learning can involve plastic change, but neural plasticity also occurs with:

```text
injury
hormonal state
sensory deprivation
exercise
stress
homeostatic compensation
```

without fitting the learning definition.

Therefore:

```text
NeuralPlasticity != Learning
```

Conversely behavioral learning does not reveal one unique neural mechanism.

```text
BehavioralLearning
!= SpecificNeuralPlasticityMechanism
```

without mechanistic evidence.

---

# 18. Plasticity is typed by system and induction protocol

A 2025 human motor study found age-related differences in M1 change after paired
associative stimulation but not the same pattern after actual motor skill
acquisition.

Therefore:

```text
Plasticity_PAS
!= Plasticity_skill-learning
```

and more generally:

```text
Plasticity_D
!= Plasticity_E
```

without evidence.

There is no single universal Human `plasticity level`.

---

# 19. Habituation

HF6 uses `Habituation` for:

> **a history-dependent decrease in a specified response to repeated stimulation
> that cannot be adequately explained by receptor/sensory adaptation, motor
> failure, fatigue or changing stimulus input.**

Thus a claim must specify:

```text
Stimulus S
Response channel R
Repetition schedule
Recovery interval
```

and competing explanations.

---

# 20. Response decrement alone is not habituation

Suppose repeated responses get smaller.

Possible causes include:

```text
habituation
sensory receptor adaptation
muscle fatigue
reduced attention
expectation
changed task strategy
reduced stimulus intensity
```

Therefore:

```text
ResponseDecrement != ProvenHabituation
```

Dishabituation/spontaneous recovery/stimulus specificity can help discriminate
mechanisms, but no one criterion is universal proof in every system.

---

# 21. Habituation is response-channel specific

Repeated psychosocial stress provides an especially strong falsifier.

The same exposures can produce:

```text
HPA/cortisol habituation
+
inflammatory sensitization
```

Therefore:

```text
Habituation_HPA
!= Habituation_immune
```

and:

```text
HumanHabituated
```

is too coarse without a response domain.

---

# 22. Group habituation is not individual habituation

Repeated-stress studies show mean response decline while substantial subgroups do
not decline and some sensitize.

Thus:

```text
GroupMeanHabituation
!= IndividualHabituation
```

HF6 preserves heterogeneity rather than treating the population mean as one Human
transition function.

---

# 23. Habituation can recover

A response that decreases across closely spaced repeated stress sessions can
return after a longer interval.

Therefore:

```text
Habituation
!= PermanentLossOfResponse
```

and timescale belongs in the claim.

This directly exposes a memory/retention question:

> What exactly was retained during the reduced-response period, and what changed
> when the response returned?

HF6 does not yet solve that.

---

# 24. Sensitization

HF6 uses `Sensitization` for:

> **a history-dependent increase in responsiveness of a specified response system
> following prior exposure/history.**

The increased response may be:

```text
to the same stimulus
to anticipation of the stimulus
to related stimuli
```

under different mechanisms.

Thus:

```text
Sensitization_same
!= AnticipatorySensitization
!= GeneralizedSensitization
```

unless linked empirically.

---

# 25. Sensitization is not vigilance

Increased response may involve attention/vigilance, but these are not identical.

An inflammatory response can sensitize without being an attentional phenomenon.

Therefore:

```text
Sensitization != Attention
Sensitization != Vigilance
```

---

# 26. Habituation and sensitization can coexist

The important HF6 move is to reject one axis:

```text
fully habituated <------> fully sensitized
```

A Human can have:

```text
Response_A ↓
Response_B ↑
```

after the same repeated event.

So define a:

```text
RepeatedExposureProfile = {
  response channel → trajectory
}
```

rather than one `adapted` bit.

---

# 27. Tolerance

HF6 uses `Tolerance_D` for:

> **reduced effect in endpoint D from the same or comparable dose/exposure after
> prior repeated exposure.**

Tolerance may involve:

```text
pharmacokinetic change
pharmacodynamic change
learned/contextual compensation
behavioral adaptation
```

Therefore:

```text
Tolerance != Habituation
```

although both can produce response decline.

---

# 28. Tolerance itself is endpoint-specific

Caffeine studies show some physiological and subjective endpoints can develop
strong tolerance while other effects remain.

Thus:

```text
Tolerance_BP
!= Tolerance_subjective
!= Tolerance_performance
```

without evidence.

A claim that `the person is tolerant` must name the effect.

---

# 29. Learned/contextual tolerance further breaks simple biology-versus-learning

Human opioid work shows predictive context/ritual can contribute to diminished
drug effect.

Therefore:

```text
Tolerance
can include learned anticipatory compensation
```

and cannot always be classified as purely pharmacological internal adaptation.

This is another Human example of:

```text
Body regulation ↔ learned prediction
```

from HF5.

---

# 30. Extinction is not habituation

In conditioning:

```text
Cue CS predicts Outcome US
```

Extinction changes behavior when the cue is repeatedly presented without the
previous outcome.

That is not the same structure as a simple unconditioned response decrement from
repeating one stimulus.

Thus:

```text
Extinction != Habituation
```

---

# 31. Extinction is not erasure

Return-of-fear phenomena provide the decisive falsifier.

After successful extinction, conditioned responding can return through:

```text
SpontaneousRecovery
Renewal
Reinstatement
Reacquisition
```

Therefore:

```text
ExtinctionPerformance
!= OriginalMemoryErased
```

The system can preserve competing histories whose expression depends on context,
time and later events.

---

# 32. Return-of-response mechanisms must remain typed

HF6 retains:

```text
SpontaneousRecovery
= response return after time

Renewal
= response return with context shift

Reinstatement
= response return after unsignalled outcome/stressor exposure

Reacquisition
= rapid response recovery when cue-outcome pairing returns
```

These are not synonyms.

```text
SpontaneousRecovery
!= Renewal
!= Reinstatement
!= Reacquisition
```

This becomes one of the strongest reasons HF7 must study memory/retrieval.

---

# 33. Physiological adaptation is also multidimensional

Repeated heat or exercise can alter:

```text
sweating
circulatory strain
mitochondrial capacity
muscle enzyme expression
VO2-related performance
heat-shock proteins
```

at different rates.

Thus:

```text
HeatAdaptation_D
!= HeatAdaptation_E
```

There is no single `heat adapted = true` state covering every endpoint.

---

# 34. Detraining reveals persistence and decay profiles

Training creates changes with different decay rates.

Human endurance data show some cardiovascular performance changes decay relatively
quickly while muscle capillarization/metabolic adaptations can remain above
untrained levels much longer.

Therefore:

```text
AdaptationDecay_D
!= AdaptationDecay_E
```

and:

```text
Detraining != InstantReturnToBaseline
```

---

# 35. Reversibility is a dimension, not the opposite of adaptation

A real adaptation can later reverse.

Therefore:

```text
ReversibleChange != NotAdaptation
```

HF6 instead records:

```text
Reversibility
DecayHalfTime / trajectory
ResidualAfterDetraining
ReacquisitionRate
```

when evidence permits.

---

# 36. Improvement after injury does not reveal the mechanism of improvement

Post-stroke function can improve through:

```text
Restitution
Compensation
Reorganization
Strategy change
Assistive support
```

or mixtures.

Thus:

```text
FunctionalImprovement
!= Restitution
```

and:

```text
FunctionalImprovement
!= CompensationOnly
```

Kinematics and mechanism evidence are needed.

---

# 37. Compensation is not failure

Compensation can be the best available route to restored function.

HF6 rejects the normative collapse:

```text
normal-looking mechanism = good
compensatory mechanism = bad
```

The correct question is:

```text
What function is restored?
At what cost?
With what transfer/future capacity?
```

Therefore:

```text
Compensation != Maladaptation by definition
```

---

# 38. Restitution is not return to the identical prior system

Even apparently normalized movement can be supported by changed neural
organization.

Therefore:

```text
RestoredFunction
!= RestoredIdenticalMechanism
```

This extends HF5's:

```text
RecoveredFunction != SameInternalStateAsBefore
```

---

# 39. Development is a trajectory, not a stage label

HF6 defines `Development_D` as:

> **age/history-structured change in the organization and capability of domain D
> arising from interactions among maturation, learning, plasticity, body growth,
> environment, institutions and accumulated experience.**

This is not:

```text
child → adult = linear improvement
```

Different functions peak, reorganize or decline at different times.

---

# 40. Maturation is not learning

Some developmental change occurs reliably with biological maturation even without
the specific practice that defines learning.

Other change is experience-dependent.

Thus:

```text
Maturation != Learning
```

although maturation can change learning capacity and learning can alter
maturational trajectories.

---

# 41. Sensitive periods must be typed by function

Early visual deprivation shows different long-term effects across:

```text
acuity
global form
global motion
biological motion
```

Therefore:

```text
SensitivePeriod_D
!= SensitivePeriod_E
```

A Human does not have one global `critical period`.

---

# 42. Damage and recovery windows can differ

Developmental visual evidence suggests that:

```text
window of vulnerability to deprivation
```

and:

```text
window of capacity for recovery
```

need not be identical.

Therefore:

```text
SensitivePeriod_damage
!= SensitivePeriod_recovery
```

This is a major correction to the idea of one developmental gate that simply
closes.

---

# 43. Sensitive period does not mean adult immutability

Adult amblyopia perceptual-learning studies show substantial improvements after
the canonical early visual-development period.

Thus:

```text
SensitivePeriod
!= AdultNoPlasticity
```

But the reverse is also wrong:

```text
AdultPlasticity
!= NoDevelopmentalConstraint
```

Early deprivation can leave lasting deficits even when later training helps.

---

# 44. Development is not monotonic improvement

Lifespan implicit-skill studies produce different developmental curves depending
on task and metric.

Some raw learning measures change sharply around adolescence; other paradigms show
high efficiency in adolescence/adulthood and later decline.

Therefore:

```text
Development != MonotonicImprovement
```

and:

```text
OneAgeLearningCurve
```

is not licensed across skill domains.

---

# 45. Chronological age is an index, not a mechanism

`Age = 70` tells us elapsed chronological time.

It does not uniquely identify:

```text
brain state
vascular state
fitness
experience
reserve
disease
sleep
social environment
learning history
```

Therefore:

```text
ChronologicalAge != AgingMechanism
```

Age can correlate with causal processes without being their mechanistic identity.

---

# 46. Aging is multidimensional change

HF6 uses `Aging_D` for age-associated changes in domain D while keeping separate:

```text
ChronologicalAge
BiologicalState_D
Disease/Pathology
ExposureHistory
Practice/Experience
Reserve
Environment
```

Aging can include:

```text
loss
maintenance
compensation
selective preservation
continued learning
reorganization
```

not only decline.

---

# 47. Aging does not eliminate plasticity

Older adults can improve motor, cognitive and perceptual task performance.

Yet:

```text
rate of learning
amount of practice required
retention
transfer
induction response
```

may differ from younger adults.

Therefore:

```text
Aging != NoPlasticity
```

and:

```text
PlasticityAtOldAge
!= PlasticityAtYoungAge
```

without implying zero in either group.

---

# 48. Age effects are task- and mechanism-specific

Aging studies show:

```text
training gain may remain
far transfer may be weak
motor learning may remain despite reduced induced M1 plasticity
```

Thus:

```text
AgeEffect_D != AgeEffect_E
```

A single assay cannot establish an individual's global adaptive capacity.

---

# 49. Maintenance and reserve are different explanations

Stable performance in aging can arise because:

```text
Maintenance
= underlying system changed less than expected
```

or because:

```text
Reserve
= function remains better than expected despite underlying burden/change
```

Therefore:

```text
Maintenance != Reserve
```

and neither is simply the observed performance level.

---

# 50. Reserve is relational and domain-specific

HF6 uses a cautious placeholder:

```text
Reserve_D(H, burden, context)
```

for capacity/redundancy/alternative organization that helps preserve function in
D under perturbation.

This is not one measured substance.

Thus:

```text
Reserve_D != Reserve_E
```

and:

```text
HighBaselinePerformance != HighReserve
```

without burden/trajectory evidence.

---

# 51. Resilience must be represented as a trajectory

HF5 separated resilience from recovery.
HF6 strengthens the representation:

```text
ResilienceProfile(H, Exposure E, Outcome D, interval T)
```

Possible trajectory patterns include:

```text
Resistance / maintenance
Deviation + rapid recovery
Deviation + slow recovery
Adaptation to new functional mode
Delayed deterioration
Persistent dysfunction
```

No one pattern defines all resilience research.

---

# 52. Resilience is not no response

Prospective police data provide a strong falsifier: people with favorable
resilient/recovery trajectories mounted substantial cortisol responses to a
laboratory challenge, while a blunted response was associated with a less
favorable later distress trajectory in that cohort.

Therefore:

```text
Resilience != WeakStressResponse
```

A robust response can be part of effective regulation.

---

# 53. Resilience is domain-specific

A person resilient on depressive-symptom trajectory after adversity need not be
similarly resilient in:

```text
physical function
social function
pain
anxiety
health burden
```

Thus:

```text
Resilience_D != Resilience_E
```

without evidence.

---

# 54. Exposure must be represented

A stable outcome under low perturbation is not automatically stronger resilience
than the same outcome under severe perturbation.

Therefore a resilience claim requires:

```text
Exposure
Baseline
Outcome domain
Trajectory
Timescale
```

HF6 rejects resilience scores that ignore actual adversity/exposure when used as
causal proof.

---

# 55. Growth is not resilience by default

Some people may show performance/function above a prior baseline after adversity.

HF6 requires a measured domain and counterfactual caution before calling this
`growth`.

Thus:

```text
Resilience != PostTraumaticGrowth
```

and:

```text
SelfReportedGrowth != ObjectiveImprovement
```

without supporting evidence.

---

# 56. Adaptation can create tradeoffs

A persistent change that improves one demand can reduce flexibility elsewhere.

Examples include:

```text
highly specific perceptual expertise
compensatory movement strategies
stress-system recalibration
resource allocation to one function
```

Therefore:

```text
AdaptiveGain_D
can coexist with
Cost_E
```

HF6 introduces no assumption of global optimization.

---

# 57. Plasticity also creates vulnerability

The ability to change is not synonymous with the ability to improve.

Plastic systems can acquire:

```text
maladaptive habits
fear associations
pain amplification
biased priors
compensatory patterns with long-term cost
```

Thus:

```text
Plasticity != Good
```

and:

```text
LowPlasticity != Bad
```

without a domain/timescale/value criterion.

---

# 58. Change is multi-timescale

HF6 requires at least:

```text
within-trial
within-session
hours
sleep/wake interval
days/weeks
months/years
developmental lifespan
```

A process can appear persistent at one timescale and transient at another.

Therefore:

```text
Persistent_T1
!= Persistent_T2
```

unless the timescale is declared.

---

# 59. Reversibility is also timescale-dependent

A change may be:

```text
rapidly reversible
slowly reversible
partially reversible
functionally compensated but structurally persistent
effectively irreversible on the observed horizon
```

HF6 therefore avoids binary:

```text
reversible / irreversible
```

when longitudinal evidence is limited.

---

# 60. Path dependence

History matters not only through current state but through what was learned,
retained or structurally changed.

Two Humans at apparently similar current performance may have different future
responses because their histories differ.

Formally:

```text
ObservedState_A(t) ≈ ObservedState_B(t)
```

need not imply:

```text
F_A,t ≈ F_B,t
```

This is **path dependence**.

---

# 61. Same performance can hide different transition functions

Example:

```text
Person A: skilled through deep retained learning
Person B: temporarily performs well with external guidance
```

Their present scores may match.

But under:

```text
novel context
feedback removal
time delay
stress
```

future behavior can diverge.

Therefore:

```text
SamePerformance
!= SameCapability
!= SameTransitionFunction
```

This reconnects to the Human-AI problem directly.

---

# 62. Change evidence needs separate surfaces

HF6 retains a `ChangeEvidenceBundle`:

```text
training/acquisition curve
immediate post-test
delayed retention
novel transfer test
reversal/detraining
relearning/savings
behavior
subjective report
physiological/neural evidence
mechanism intervention
```

No one surface proves all change dimensions.

---

# 63. Neural change is evidence, not identity

fMRI/TMS/EEG/structural changes can support a plasticity mechanism claim.

But:

```text
NeuralMarkerChange != PlasticityTotality
```

and:

```text
NeuralReorganization != BehavioralBenefit
```

without a validated relation.

Likewise behavioral improvement does not uniquely localize mechanism.

---

# 64. Transfer is the capability falsifier

HF6 elevates transfer testing because Human systems often confuse:

```text
performance on familiar protocol
```

with:

```text
reusable capability
```

A useful capability claim should ask:

```text
Can the change survive time?
Can it survive context shift?
Can it survive tool/feedback removal?
Can it apply to new stimuli/tasks?
Can the Human recover after interference?
```

Transfer failure does not erase the learned skill, but it contracts the capability
claim.

---

# 65. Training-specific expertise and general capability must be separate

HF6 therefore uses:

```text
TrainedPerformance_D
RetainedSkill_D
TransferCapability_{D→E}
```

as different surfaces.

This is especially important for standardized-test practice, coding benchmarks,
AI-assisted task performance and rehabilitation.

---

# 66. Human × AI: assisted performance is not Human learning

Suppose an Agent enables a Human to complete a task faster.

That establishes:

```text
JointSystemPerformance ↑
```

It does not automatically establish:

```text
HumanInternalLearning ↑
```

or:

```text
HumanTransferCapability ↑
```

HF6 requires delayed/transfer/tool-removal evidence if internalized learning is the
claim.

---

# 67. Delegation can change the learning trajectory

AI/tool use may:

```text
reduce practice
increase feedback quality
increase task variety
remove low-value repetition
change error distribution
externalize memory
support metacognition
```

Therefore Agent assistance can either increase or reduce different forms of Human
learning/plasticity.

There is no foundation law:

```text
MoreAssistance = MoreLearning
```

or:

```text
MoreAssistance = Deskilling
```

The relevant ChangeProfile must be measured.

---

# 68. Tool removal is an informative falsifier

For a Human×AI task:

```text
WithToolPerformance
WithoutToolImmediatePerformance
WithoutToolDelayedPerformance
NovelTransferPerformance
```

answer different questions.

Thus:

```text
JointCapability
!= IndependentCapability
```

but both are real capability surfaces from HF1.

HF6 adds the history dimension:

```text
JointUse_t
can change
IndependentCapability_{t+1}
```

positively, negatively or negligibly.

---

# 69. Developmental effects constrain Human-AI learning too

Learning environment effects can depend on developmental stage, prior skill and
current reserve.

Therefore:

```text
SameTrainingProtocol
!= SameLearningEffectAcrossHumans
```

HF6 rejects one universal pedagogy inferred from one age group or one task.

---

# 70. Aging and tools: compensation versus capacity

External tools may preserve function in aging by compensation even when internal
capacity declines.

That does not make the improvement unreal.

But it should be represented as:

```text
SituatedCapability maintained/increased
```

rather than silently claiming:

```text
InternalCapacity restored
```

HF1 and HF6 therefore align:

```text
Capability relation
+
ChangeProfile
```

is more informative than one performance score.

---

# 71. Normative firewall

HF6 does not equate:

```text
adaptation
learning
resilience
plasticity
```

with:

```text
normative improvement
health
wisdom
autonomy
welfare
```

Examples:

```text
maladaptive learning
pain sensitization
coercive skill acquisition
highly effective harmful habit
resilient performance under exploitative conditions
```

show why.

Therefore:

```text
FunctionalAdaptation != NormativeGood
```

and:

```text
ResilienceEvidence != JustificationForMoreAdversity
```

---

# 72. Cross-context falsifier matrix

| Case | Naive collapse attacked | Surviving distinction |
|---|---|---|
| practice gain disappears later | performance = learning | acquisition != retention |
| second motor task disrupts recent first skill | learning complete at practice end | acquisition != consolidation |
| sleep stabilizes without adding gain | consolidation = enhancement | stabilization != enhancement |
| visual improvement fails similar-task transfer | learning = general capability | retained skill != transfer |
| extensive training increases specificity | more practice = more general | practice magnitude != transfer breadth |
| HPA response decreases but IL-6 rises | person habituated/sensitized globally | response-channel trajectories differ |
| startle response dishabituates | decrement = fatigue | habituation != effector exhaustion |
| caffeine effect diminishes with repeated dose | tolerance = habituation | pharmacological/contextual tolerance distinct |
| fear returns after extinction | extinction = erasure | expression change != memory deletion |
| heat adaptation decays at different rates | one adaptation variable | persistence is endpoint-specific |
| stroke task use improves via trunk strategy | improvement = restitution | compensation can produce function |
| early visual deprivation affects functions differently | one critical period | sensitive period is domain-specific |
| adult amblyopia improves after training | critical period = no adult plasticity | constraint != absolute closure |
| lifespan learning curves differ by task/metric | development = monotonic gain | developmental trajectory is domain/measure-specific |
| older adults improve trained task but not transfer | aging = no learning | learning persists; transfer can narrow |
| resilient police show strong cortisol response | resilience = low response | response magnitude != resilience trajectory |
| depression resilience does not generalize to health/function | resilience = global trait | resilience is outcome-domain specific |
| stable cognition despite brain change | maintenance = reserve | different mechanisms can preserve function |

---

# 73. Competing HF6 models

## M1 — state-only Human

```text
current state determines next response
```

### Failure

Training, deprivation, repeated stress, injury and age history produce different
future responses at similar current states.

**Disposition:** reject as complete model.

## M2 — practice-performance model

```text
performance improved during practice → learning occurred
```

### Failure

Retention and transfer can fail.

**Disposition:** reject.

## M3 — learning-as-general-capability

```text
trained improvement → broad capability improved
```

### Failure

Perceptual/motor learning can be highly specific.

**Disposition:** reject.

## M4 — plasticity-is-learning

### Failure

Plastic change can follow injury/stress/physiology without learning, and behavioral
learning does not identify one plastic mechanism.

**Disposition:** reject.

## M5 — one repeated-exposure axis

```text
habituation ↔ sensitization
```

### Failure

Different systems can habituate and sensitize simultaneously.

**Disposition:** reject.

## M6 — extinction-as-erasure

### Failure

Renewal, reinstatement, spontaneous recovery and reacquisition.

**Disposition:** reject as general account.

## M7 — adaptation-is-good

### Failure

Local gain can impose other costs; sensitization or harmful habit learning can be
persistent.

**Disposition:** reject normatively.

## M8 — resilience-as-trait

### Failure

Trajectory depends on exposure, outcome domain, time and background stressors.

**Disposition:** retain trait predictors as possible causes, reject resilience
itself as one fixed trait.

## M9 — development-as-maturation-to-peak

### Failure

Different domains have different trajectories and experience-dependent sensitive
periods.

**Disposition:** reject as full model.

## M10 — aging-as-uniform-loss

### Failure

Older adults retain learning/plasticity with domain-specific losses, compensation,
reserve and transfer differences.

**Disposition:** reject.

---

# 74. HF6 anti-laws

## Persistent change

1. `StateChange != TransitionFunctionChange`.
2. `AcuteCompensation != PersistentAdaptation`.
3. `Adaptation != Improvement`.
4. `Adaptation != WelfareGain`.
5. `EvolutionaryAdaptation != WithinLifetimeAdaptation`.
6. `Adaptation_D != Adaptation_E` without evidence.

## Learning / transfer

7. `Practice != Learning`.
8. `PracticePerformance != RetainedLearning`.
9. `Acquisition != Retention`.
10. `Acquisition != Consolidation`.
11. `Consolidation != ElapsedTime`.
12. `Consolidation != GuaranteedEnhancement`.
13. `Retention_D != Retention_E`.
14. `Retention != Transfer`.
15. `NearTransfer != FarTransfer`.
16. `Transfer_D != Transfer_E`.
17. `Specificity != NoLearning`.
18. `Specificity != LowPlasticity`.
19. `MorePractice != MoreTransfer`.
20. `TrainingGain != BroadCapability`.

## Plasticity

21. `PlasticityCapacity != PlasticChange`.
22. `NeuralPlasticity != Learning`.
23. `BehavioralLearning != SpecificNeuralMechanism`.
24. `Plasticity_D != Plasticity_E`.
25. `Plasticity != NormativeGood`.

## Habituation / sensitization / tolerance / extinction

26. `ResponseDecrement != ProvenHabituation`.
27. `Habituation != Fatigue`.
28. `Habituation != SensoryAdaptation`.
29. `Habituation_D != Habituation_E`.
30. `GroupMeanHabituation != IndividualHabituation`.
31. `Habituation != PermanentResponseLoss`.
32. `Sensitization != Attention`.
33. `Sensitization != Vigilance`.
34. `Sensitization_D != Sensitization_E`.
35. `Habituation_A` can coexist with `Sensitization_B`.
36. `Tolerance != Habituation`.
37. `Tolerance_D != Tolerance_E`.
38. `Extinction != Habituation`.
39. `Extinction != Erasure`.
40. `SpontaneousRecovery != Renewal != Reinstatement != Reacquisition`.

## Recovery / physiological adaptation

41. `Detraining != InstantReturnToBaseline`.
42. `ReversibleChange != NotAdaptation`.
43. `FunctionalImprovement != Restitution`.
44. `FunctionalImprovement != CompensationOnly`.
45. `Compensation != Maladaptation by definition`.
46. `RestoredFunction != RestoredIdenticalMechanism`.

## Development / aging

47. `Development != MonotonicImprovement`.
48. `Maturation != Learning`.
49. `SensitivePeriod_D != SensitivePeriod_E`.
50. `SensitivePeriod_damage != SensitivePeriod_recovery`.
51. `SensitivePeriod != AdultNoPlasticity`.
52. `AdultPlasticity != NoDevelopmentalConstraint`.
53. `ChronologicalAge != AgingMechanism`.
54. `Aging != UniformDecline`.
55. `Aging != NoPlasticity`.
56. `AgeEffect_D != AgeEffect_E`.
57. `Maintenance != Reserve`.
58. `HighPerformance != HighReserve`.

## Resilience

59. `Resilience != NoResponse`.
60. `Resilience != FastRecoveryOnly`.
61. `Resilience_D != Resilience_E`.
62. `Resilience != one fixed trait`.
63. `Resilience != PostTraumaticGrowth`.
64. `ResilienceEvidence != JustificationForAdversity`.

## Human × AI / capability

65. `JointPerformanceGain != HumanInternalLearningGain`.
66. `JointCapability != IndependentCapability`.
67. `WithToolPerformance != WithoutToolCapability`.
68. `SamePerformance != SameTransitionFunction`.
69. `TrainingProtocolSame != LearningEffectSameAcrossHumans`.
70. `FunctionalAdaptation != NormativeGood`.

---

# 75. Minimum HF6 grammar

The surviving architecture is:

```text
Current state S_t
       ↓
Transition function F_Theta_t
       ↓
Action / regulation / performance
       ↓
Outcome + experience + feedback
       ↓
Update process U
       ↓
Theta_{t+1}
       ↓
Changed future transition function F_Theta_(t+1)
```

Observed change should then be tested across:

```text
acquisition
retention
transfer
context shift
interference
detraining/reversal
relearning
```

Development and aging change both:

```text
Theta
```

and the available:

```text
UpdateProcess U
```

itself.

---

# 76. Human trajectory representation

HF6 therefore recommends a trajectory object rather than one state score:

```text
HumanTrajectory_D = {
  baseline,
  perturbation/exposure history,
  current state,
  learned/adapted parameters,
  change capacity,
  retention/decay profile,
  transfer surface,
  reserve/maintenance evidence,
  future vulnerability,
  uncertainty
}
```

This is a research coordinate set, not a permanent profile schema.

---

# 77. Relation to HF1 capability

HF1 defined capability relationally.
HF6 now adds time/history:

```text
Capability_D(t+1)
can differ from
Capability_D(t)
```

because:

```text
practice
injury
recovery
adaptation
tooling
aging
```

change the Human and/or situated system.

Thus capability is not only context-relative; it is trajectory-dependent.

---

# 78. Relation to HF4 motivation

HF4 showed motivation/action allocation depends on state and history.
HF6 explains one meaning of `history`:

```text
prior reward
habit learning
sensitization
training
extinction
```

can change the future weight of cues and actions.

Therefore:

```text
CurrentMotivationProfile
is partly path-dependent
```

without being fixed by history.

---

# 79. Relation to HF5 regulation

HF5 modeled a current regulation loop.
HF6 adds:

```text
RepeatedRegulation
→ changed regulator
```

Examples:

```text
heat acclimation
stress habituation
stress sensitization
exercise adaptation
pain/fear learning
```

Thus:

```text
Regulation
↔ Adaptation
```

across timescales.

---

# 80. Relation to Game / Media / Finance

Game and Media already encounter:

```text
learning
skill
adaptation
attention history
```

HF6 adds the Human constraint that trained behavioral competence can be highly
specific and history-dependent.

Finance/resource models should similarly avoid:

```text
one successful decision
→ durable skill
```

without delayed/transfer evidence.

The shared abstraction is:

```text
History changes future option/capability structure
```

not just current state.

---

# 81. What HF6 does not establish

HF6 does not establish:

- one universal biological definition of adaptation;
- that all persistent change is learning;
- that all learning is beneficial;
- that all learning requires conscious awareness;
- that every practice gain reflects learning;
- one universal consolidation mechanism;
- that sleep always enhances every memory/skill;
- that transfer should always be broad;
- that specificity means poor learning;
- one universal plasticity score;
- that adult plasticity equals childhood plasticity;
- that sensitive periods are fiction;
- that every response decrement is habituation;
- that every response increase is sensitization;
- that habituation and sensitization are exact opposites;
- that drug tolerance is purely learned or purely pharmacological;
- that extinction always preserves the original memory unchanged;
- that recovery after injury must use the original mechanism;
- that compensation is necessarily maladaptive;
- that development is purely maturation;
- one universal lifespan learning curve;
- that aging is only chronological time;
- that older adults retain every type of plasticity equally;
- one universal reserve or resilience score;
- that resilience is desirable under every social condition;
- that any neural marker is plasticity itself.

---

# 82. The residual HF6 cannot finish

HF6 repeatedly needs concepts it has deliberately treated only operationally:

```text
Retention
Forgetting
Consolidation
Retrieval
Interference
Context dependence
Generalization
Transfer
Relearning / Savings
```

Why?

Because:

```text
extinguished fear can return
habituated responses can recover
training can be retained without transfer
transfer can disappear while trained performance remains
physiological adaptations can decay at different rates
old skills can persist across years
context can select which learned relation is expressed
```

HF6 can describe the ChangeProfile, but not what it means for past information/
structure to remain available yet currently unexpressed.

The next problem is therefore not merely `more plasticity`.

It is **memory and persistence of history**.

---

# 83. Exact next foundation

HF6 therefore selects:

# HF7 — Memory, Retention, Forgetting, Consolidation, Retrieval, Interference, Generalization and Transfer

HF7 should ask:

1. What is memory: stored representation, changed transition function, ability to
   reproduce prior information, or a family of these?
2. What separates encoding/acquisition from storage, consolidation, retention and
   retrieval?
3. Does forgetting mean information loss, access failure, interference, context
   mismatch or changed policy?
4. What is retrieval relative to reconstruction?
5. How should implicit/procedural and declarative/explicit memory distinctions be
   used without creating one universal taxonomy?
6. What does spontaneous recovery after extinction imply about competing memories?
7. What is interference: overwriting, competition, context-sensitive retrieval or
   multiple mechanisms?
8. What is savings/relearning when overt performance had returned to baseline?
9. How should transfer and generalization be parameterized across stimulus,
   response, context, task and domain?
10. When does a retained memory become usable capability?
11. How do external tools/AI change encoding, retrieval and internal retention?
12. How does aging change memory storage versus retrieval versus strategy?
13. How should memory uncertainty and reconstruction be represented?
14. What next boundary emerges after stored history and its expression are
    reconstructed?

HF7 should not predefine HF8.

---

# 84. HF6 synthesis

HF6 began from:

```text
History changes F_t.
```

It now refines this into:

```text
Experience / exposure
→ possible persistent parameter/structural change
→ changed future transition function
```

but any persistent-change claim must specify:

```text
what changed
how induced
how long retained
how specific
where it transfers
how it decays
whether it returns/relearns
what function it improves or costs
```

The deepest compression is:

```text
Human change is not one trajectory from less capable to more capable.

It is a history-dependent remodeling of multiple response systems, with different
rates of acquisition, retention, transfer, decay and compensation across domains
and life stages.
```

And the hardest remaining question is now:

> **How can history remain causally present when the learned/adapted response is
> not currently expressed?**

That is the HF7 memory/retention/retrieval boundary.
