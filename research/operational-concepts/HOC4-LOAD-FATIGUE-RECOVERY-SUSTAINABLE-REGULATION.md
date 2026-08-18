---
schema_version: 1
id: human.operational-concepts.hoc4
title: HOC4 — Load, Fatigue, Recovery and Sustainable Regulation
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
summary: Reconstructs the practical state-regulation layer for Human and Human–Agent work. HOC4 separates task demand, assigned load, exposure, experienced load, performance change, fatigue, sleep pressure, circadian phase, stressor, stress response, effort cost, reserve and recovery. It introduces RegulatoryStateView, LoadProfile, LoadCapacityMismatch, FatigueProfile, PerformanceMaintenanceCost, SustainableWorkEnvelope, RecoveryTargetSpec, RecoveryProfile, RecoveryActionSpec, StateRiskAlert and NextBestRegulationAction. Subjective fatigue is retained as actionable evidence but not an objective depletion gauge; preserved performance does not imply low strain; rest is an intervention rather than recovery itself; recovery is endpoint- and trajectory-specific; and interventions such as naps can create transient sleep-inertia costs. HOC4 connects directly to HOC1 readiness/bottleneck, HOC2 verification and HOC3 learning/scaffolding while rejecting one global energy, stress, workload, recovery or readiness scalar. No Foundation is reopened and no engineering schema is prescribed.
evidence_status: verified-synthesis
readiness: READY
related:
  - human.operational-concepts.hoc1
  - human.operational-concepts.hoc2
  - human.operational-concepts.hoc3
  - human.foundations.hf5
  - human.deep-foundations.hd9.closeout
---
# HOC4 — Load, Fatigue, Recovery and Sustainable Regulation

## 0. Practical-priority decision

Remaining high-value HOC families were compared again:

```text
regulation / fatigue / recovery
trust / coordination
health / functioning
```

Regulation/fatigue/recovery wins HOC4 because it is the most cross-cutting near-term control layer for HOC1–HOC3:

```text
Can H execute now?
Should consequence threshold be reduced?
Should verification depth increase?
Should learning continue or be deferred?
Should support be added?
Should task demand change?
Should H rest, sleep, switch task, stop or recover?
```

Trust/coordination remains important, but epistemic reliance was already partially reconstructed in HOC2. Health/functioning is high-stakes but benefits from first having a clean state/load/recovery grammar.

This ranking is operational, not foundational.

---

# 1. Core deletion

Reject the common state-collapse model:

```text
workload high
→ fatigue high
→ energy low
→ performance low
→ rest
→ recovered
```

Each arrow can fail.

Canonical guards:

```text
TaskDemand != AssignedLoad
AssignedLoad != ExperiencedLoad
ExperiencedLoad != Fatigue
Fatigue != SleepPressure
Fatigue != PerformanceDecline
Fatigue != ResourceRemaining
StressExposure != StressResponse
StressResponse != Damage
EffortCost != Fatigue
PerformanceMaintenance != NoStrain
Rest != Recovery
ElapsedTime != Recovery
MarkerBaselineReturn != WholeSystemRestoration
SubjectiveRecovery != ObjectiveRecovery
Recovery_D != Recovery_E
```

---

# 2. RegulationTargetSpec

Operational regulation starts by declaring what must remain viable.

```text
RegulationTargetSpec = {
  target_outcome_or_function,
  domain,
  consequence_profile,
  required_reliability,
  time_horizon,
  acceptable effort/cost,
  acceptable state range?,
  recovery requirement?,
  support/resources,
  interruption constraints?,
  maintenance requirement?
}
```

Examples:

```text
maintain vigilance for 2 h
complete a difficult reasoning task safely
study for durable retention
perform physical work without unacceptable error
remain available for emergency verification
recover enough for next-day operation
```

No general `energy` variable is required.

---

# 3. RegulatoryStateView

```text
RegulatoryStateView(H, TargetSpec, t)
```

is a scoped evidence view over state variables relevant to the target.

Possible channels:

```text
sleep history / sleep opportunity
circadian timing
subjective sleepiness
subjective fatigue
pain / illness symptoms
stress exposure / appraisal
physiological indicators when justified
vigilance / reaction-time evidence
current performance trend
perceived effort
motivation/goal conflict
recent workload/exposure
recovery opportunity/history
```

The view is target-relative.

It is not a universal Human state vector.

---

# 4. Subjective state is evidence, not noise

HOC4 rejects two symmetric errors:

```text
subjective fatigue = objective depletion
```

and:

```text
subjective fatigue = irrelevant feeling
```

Subjective fatigue can alter:

```text
effort valuation
priority
willingness to continue
perceived difficulty
risk tolerance
support seeking
```

and may contain useful information about current state.

But:

```text
SubjectiveFatigue
!= ExactPerformanceLoss
!= OnePhysiologicalMechanism
```

---

# 5. Objective performance is also not the whole state

A Human can temporarily preserve target performance by increasing:

```text
effort
attention allocation
motivation
compensatory strategy
time
support
```

Therefore:

```text
StablePerformance
!= StableState
```

and:

```text
NoObservedDecline
!= NoAccumulatingCost
```

---

# 6. PerformanceMaintenanceCost

HOC4 introduces:

```text
PerformanceMaintenanceCost(H, Target, interval)
```

as an operational hypothesis/view over the additional cost required to preserve performance under changing state/load.

Possible evidence:

```text
higher subjective effort
longer latency
more verification
more breaks
more support
narrower task selection
increased error recovery effort
reduced spare attention
post-task recovery burden
```

This is not one hidden metabolic quantity.

Its purpose is to detect compensated strain before outcome failure.

---

# 7. TaskDemand

```text
TaskDemandProfile
```

from HOC1 describes what the task requires.

HOC4 keeps it separate from load actually imposed on the Human.

```text
TaskDemand
!= HumanLoad
```

A demanding task can impose low Human load if automated/delegated.
A nominally simple task can impose high load under interruption, uncertainty or poor interface conditions.

---

# 8. AssignedLoad

```text
AssignedLoad(H, interval)
```

captures externally or self-assigned work/exposure, such as:

```text
number of tasks
hours on task
concurrency
interruptions
responsibility burden
deadline density
coordination obligations
physical demand
information volume
```

It is an exposure description, not a Human state.

---

# 9. ExperiencedLoad

```text
ExperiencedLoad(H, Target, interval)
```

captures perceived/experienced demand or effort burden.

It may differ from assigned load because of:

```text
skill
familiarity
state
motivation
control
predictability
tool quality
support
stakes
```

Therefore:

```text
SameAssignedLoad
!= SameExperiencedLoad
```

---

# 10. CumulativeExposureProfile

Near-term regulation often depends on history.

```text
CumulativeExposureProfile(H, interval)
```

may include:

```text
wake duration
sleep restriction history
continuous time-on-task
recent high-consequence decisions
interruptions/context switches
physical work
emotional/social stressors
recovery opportunities
```

This is not a universal allostatic-load score.

---

# 11. LoadProfile

HOC4 therefore reconstructs:

```text
LoadProfile = {
  TaskDemand,
  AssignedLoad,
  ExperiencedLoad,
  CumulativeExposure,
  support/automation,
  uncertainty,
  evidence age
}
```

A consumer may compress this, but must preserve which layer the evidence belongs to.

---

# 12. LoadCapacityMismatch

```text
LoadCapacityMismatch(H, Target, t)
```

is a decision-oriented comparison between current demand/exposure and current capability/readiness/state.

It can include:

```text
requirements currently unsatisfied
requirements sustained only by compensation
fragile margins
state-sensitive failure risk
recovery debt / insufficient opportunity
unknowns
```

It is not:

```text
workload / capacity = one universal ratio
```

unless a specific consumer validates such a ratio.

---

# 13. FatigueProfile

`Fatigue` survives as a high-value operational family only after typing.

```text
FatigueProfile(H, Domain, t, interval) = {
  subjective fatigue,
  task-specific performance change,
  vigilance/attention change where relevant,
  effort-cost shift,
  sleepiness/sleep pressure evidence,
  physical/physiological evidence where justified,
  cross-domain spillover evidence,
  recovery response,
  uncertainty
}
```

Do not require all channels.

---

# 14. Fatigue is domain-sensitive

Examples:

```text
cognitive fatigue
physical fatigue
visual fatigue
social/emotional exhaustion
sleepiness
motor fatigue
```

may correlate without being identical.

```text
Fatigue_D != Fatigue_E
```

A consumer must state which target is affected.

---

# 15. Mental fatigue can cross domains

Controlled experimental evidence shows demanding cognitive activity can alter subsequent physical endurance/perceived effort under studied conditions.

HOC4 therefore permits:

```text
CrossDomainFatigueEffect
```

without concluding:

```text
all fatigue is one common resource
```

Cross-domain influence does not establish ontological identity.

---

# 16. Sleep pressure and circadian phase remain separate

```text
SleepPressure
!= CircadianDrive
!= SubjectiveSleepiness
!= SubjectiveFatigue
!= Performance
```

Operationally, the same amount of prior wake can have different consequences at different circadian phases.

A Human may also underestimate impairment during some sleep-restricted biological-night conditions.

Thus time-of-day can be a state modifier without being a personality feature.

---

# 17. SleepHistoryView

A practical non-medical view may include:

```text
recent sleep opportunity/duration if known
wake duration
sleep restriction streak
nap timing/duration
circadian/clock-time context
subjective sleepiness
objective vigilance evidence if available
```

HOC4 does not diagnose sleep disorders from these fields.

---

# 18. Subjective–objective mismatch is first-class

```text
StateMismatch = {
  subjective_state,
  objective_task evidence,
  direction of mismatch,
  target/consequence,
  uncertainty
}
```

Examples:

```text
feels fine + vigilance impaired
feels exhausted + target performance preserved
feels recovered + verification still impaired
```

Mismatch should trigger targeted evidence, not automatic disbelief of either channel.

---

# 19. Stress needs a typed operational grammar

Reject `stress = high` as canonical.

Keep separate:

```text
StressorExposure
StressAppraisal
StressResponse
SubjectiveStressExperience
StressBurdenTrajectory
RecoveryTrajectory
```

Acute stress response may sometimes support action and does not equal damage.

```text
StressResponse != Damage
```

---

# 20. StressorExposure is relational

The same event can differ in operational stress impact depending on:

```text
controllability
predictability
stakes
history
relationship
resources
current state
```

Therefore:

```text
StressorProperty
!= StressResponseMagnitude
```

---

# 21. EffortCostShift

HOC4 retains:

```text
EffortCostShift(H, Target, t)
```

for cases where the same output becomes subjectively or behaviorally more costly.

This can influence:

```text
persistence
task switching
motivation
support seeking
speed/accuracy tradeoff
```

But:

```text
EffortCostShift
!= Fatigue by definition
```

It can be one fatigue-related consequence or signal.

---

# 22. ReserveProfile

`Reserve` is useful when challenge reveals headroom unavailable from resting observations.

```text
ReserveProfile(H, Domain, ChallengeProtocol, interval)
```

can summarize:

```text
performance margin under increasing demand
compensation before failure
recovery after challenge
support sensitivity
```

It is challenge/protocol dependent.

```text
Reserve != HiddenFixedTank
```

---

# 23. SustainableWorkEnvelope

HOC4 introduces a high-value practical object:

```text
SustainableWorkEnvelope_H(
  TargetFamily,
  ConsequenceLevel,
  Support,
  Horizon
)
```

It describes the evidence-supported region in which work can continue while maintaining declared acceptable bounds on:

```text
quality/reliability
error risk
state burden
recovery requirement
future capability/learning impact where relevant
```

This is not one fixed number of hours per day.

---

# 24. Sustainable != Maximum

A Human may be able to achieve a short maximum performance burst outside the sustainable envelope.

```text
MaximumCapability
!= SustainableCapability
```

Likewise a workload can be sustainable for one day but not for repeated days.

```text
Sustainable_Horizon1
!= Sustainable_Horizon2
```

---

# 25. SustainableWorkEnvelope is consequence-relative

For low-consequence reversible tasks, the envelope can tolerate more fatigue/error uncertainty.

For:

```text
medical decisions
financial execution
safety-critical control
irreversible production changes
```

acceptable envelope can contract because verification/error thresholds are stricter.

Thus:

```text
SameHumanState
→ different Readiness by ConsequenceSpec
```

which connects directly to HOC1.

---

# 26. StateRiskAlert

HOC4 permits alerts when evidence indicates current state/load may invalidate normal assumptions.

```text
StateRiskAlert = {
  target,
  trigger evidence,
  affected capability/readiness dimension,
  consequence level,
  confidence,
  recommended action,
  expiry/recheck
}
```

Possible statuses:

```text
MONITOR
REDUCE_LOAD
ADD_SUPPORT
INCREASE_VERIFICATION
DEFER_HIGH_CONSEQUENCE_TASK
RECOVERY_NEEDED
INSUFFICIENT_EVIDENCE
```

This is not a medical diagnosis.

---

# 27. RecoveryTargetSpec

Recovery is meaningless without a target.

```text
RecoveryTargetSpec = {
  disturbed property/function,
  pre-event/personal baseline if relevant,
  desired functional endpoint,
  time horizon,
  consequence threshold,
  acceptable compensation?,
  evidence channels
}
```

Examples:

```text
restore vigilance
reduce subjective fatigue
restore physical performance
restore verification reliability
restore sleep opportunity
reduce stress-response burden
```

---

# 28. RecoveryProfile

```text
RecoveryProfile(H, Event/Exposure, TargetSpec, interval) = {
  subjective recovery,
  target performance recovery,
  physiological recovery where relevant,
  capability/readiness restoration,
  residual fragility,
  compensation/reorganization,
  recurrence/change-point evidence,
  uncertainty
}
```

Different endpoints can recover at different rates.

---

# 29. Rest is an intervention, not an outcome

```text
Rest
```

means an intervention/context with reduced or changed demand.

```text
Recovery
```

means target-relevant change after perturbation.

Therefore:

```text
Rest != Recovery
```

A break can help one function while leaving another unchanged.

---

# 30. Breaks can restore performance without identical wellbeing effects

Controlled vigilance experiments show rest breaks can improve post-break performance, while some break contents affect subjective distress/wellbeing differently from performance.

HOC4 therefore keeps:

```text
PerformanceRecovery
!= SubjectiveRecovery
```

and treats break content/duration as intervention parameters.

---

# 31. RecoveryActionSpec

```text
RecoveryActionSpec = {
  action_type,
  target,
  duration,
  timing,
  environment,
  expected benefit,
  transient costs,
  contraindications/constraints where known,
  evidence confidence,
  reassessment time
}
```

Candidate action types can include:

```text
REST_BREAK
TASK_SWITCH
REDUCE_LOAD
SLEEP_OPPORTUNITY
NAP
FOOD/HYDRATION where relevant
PHYSICAL_MOVEMENT
ENVIRONMENT_CHANGE
SOCIAL/COORDINATION RELIEF
STOP / DEFER
```

HOC4 does not prescribe medical treatment.

---

# 32. Recovery intervention can have transient cost

A nap may improve later alertness/performance yet cause immediate sleep inertia.

Thus:

```text
RecoveryIntervention
!= ImmediateReadinessIncrease
```

A recent 2026 randomized crossover nap study found immediate post-nap impairment in several performance measures, with stronger sleep-inertia effects after the longer nap condition under that protocol.

Operational implication:

```text
recovery action timing
must include re-entry latency / transient impairment
```

---

# 33. Acute recovery can be incomplete

Controlled sleep-restriction research shows that increasing one-night recovery sleep can improve neurobehavioral outcomes without necessarily restoring every measured outcome to baseline after accumulated restriction.

Therefore:

```text
OneRecoveryEpisode
!= FullRestoration
```

and:

```text
FeelsBetter
!= AllFunctionsRecovered
```

---

# 34. Recovery is not rewind

After recovery a Human may reach functional adequacy through:

```text
restoration
compensation
changed strategy
adaptation
support
```

while internal state is not identical to the pre-event state.

```text
RecoveredFunction
!= SameInternalStateAsBefore
```

---

# 35. RecoveryDebt / RecoveryNeedInference

HOC4 permits a cautious operational inference:

```text
RecoveryNeedInference(H, Target, t)
```

when accumulated exposure/state evidence suggests continued operation has declining expected value or increasing risk.

It should include:

```text
why recovery is inferred
which target is affected
what evidence is missing
what action is feasible
when to reassess
```

Do not treat it as a universal body debt scalar.

---

# 36. NextBestRegulationAction

```text
NextBestRegulationAction(
  H,
  Target,
  StateEvidence,
  LoadProfile,
  ConsequenceSpec,
  Constraints
)
```

candidate actions include:

```text
CONTINUE
CONTINUE_WITH_MONITORING
REDUCE_LOAD
NARROW_SCOPE
TASK_SWITCH
ADD_TOOL/AGENT_SUPPORT
ADD_VERIFICATION
TAKE_BREAK
SLEEP/RECOVERY_OPPORTUNITY
DEFER_HIGH_CONSEQUENCE_TASK
STOP
COLLECT_STATE_EVIDENCE
ESCALATE_HEALTH/SAFETY_CONCERN
```

This is a decision-support family, not medical advice by default.

---

# 37. NextBestRegulationAction is objective-relative

Example:

```text
Human fatigued
low-consequence creative brainstorming
```

may support:

```text
continue with lighter demand
```

while the same state before an irreversible financial action may support:

```text
add independent verification / defer
```

Thus:

```text
FatigueState
does not map to one universal action.
```

---

# 38. HOC1 connection — readiness

HOC4 supplies state evidence to:

```text
TaskReadiness
```

but does not replace it.

```text
HighFatigueProfile
can lower Readiness
```

only relative to:

```text
task demand
support
consequence
verification
```

Therefore:

```text
Fatigue != NotReady by definition
```

---

# 39. HOC1 connection — bottleneck

When performance falls, HOC4 can help distinguish:

```text
state bottleneck
persistent skill/capability bottleneck
external demand bottleneck
support bottleneck
uncertainty bottleneck
```

One poor session should not rewrite persistent capability if state evidence is plausible.

---

# 40. HOC2 connection — verification

Fatigue/state can affect:

```text
error detection
confidence
metacognitive sensitivity
verification latency
willingness to check
```

So high-consequence systems should not assume verification capacity is invariant across state.

A verifier can itself become the fragile component.

---

# 41. HOC3 connection — learning

Learning evidence is state-conditioned.

Fatigue/sleep loss can change:

```text
practice performance
attention
motivation
delayed retention opportunity
support seeking
```

Therefore:

```text
PoorLearningSession
!= LowModifiability by definition
```

HOC3 can return `REST/DEFER_STATE`; HOC4 supplies the state/regulation reasoning behind it.

---

# 42. State-aware practice scheduling

A Human-supporting Agent may choose to:

```text
use low-state periods for review/light tasks
reserve difficult acquisition/verification for stronger state periods
schedule delayed retention probes separately from acquisition
```

but only when evidence supports a stable enough pattern.

Do not convert limited observations into permanent chronotype/personality labels.

---

# 43. PersonalBaseline

HOC4 retains:

```text
PersonalBaseline(H, Variable/Function, Context, interval)
```

for change detection.

Canonical guards:

```text
PersonalBaseline
!= PopulationReference
!= ImmutableSetpoint
```

A useful baseline may itself drift after development, training, illness, medication, chronic exposure or environmental change.

---

# 44. BaselineDeviation

```text
BaselineDeviation(H, Target, t)
```

can be operationally useful even when the value remains inside population reference range.

Conversely, a population-outlying value can be normal for a particular Human.

Interpretation remains target/evidence dependent.

---

# 45. Change-point beats permanent label

For state regulation, a change-point question is often more actionable than classification:

```text
Has this Human materially departed from their recent functional/state trajectory?
```

This supports:

```text
recheck
reduce load
investigate cause
```

without asserting a disease or permanent trait.

---

# 46. Health boundary

HOC4 is not a health/disease diagnostic layer.

If state disturbance becomes:

```text
persistent
severe
unexplained
multi-system
function-limiting
or safety-relevant
```

ownership can move toward health/functioning/clinical interpretation.

Thus:

```text
FatigueProfile
!= Diagnosis
StateRiskAlert
!= DiseaseClaim
```

---

# 47. Burnout boundary

HOC4 does not use `burnout` as a synonym for high fatigue or workload.

If a future consumer needs occupational burnout, it should be reconstructed as its own scoped occupational construct rather than inferred from one fatigue score.

```text
Fatigue != Burnout by definition
```

---

# 48. Motivation boundary

A Human can stop because of:

```text
fatigue
low value
low expectancy
opportunity cost
competing goals
frustration
pain
external interruption
```

Therefore:

```text
StoppedWorking
!= Fatigued
!= Unmotivated
```

MotivationProfile remains separate.

---

# 49. Workload cannot be inferred from calendar occupancy alone

Eight scheduled hours can contain:

```text
routine low-demand work
high-stakes continuous verification
interrupt-heavy coordination
long idle/recovery periods
```

So:

```text
ScheduledTime
!= AssignedLoadTotality
!= ExperiencedLoad
```

Calendar/time traces are evidence, not workload truth.

---

# 50. Agent support changes load distribution

AI can:

```text
reduce generation demand
increase verification demand
reduce search cost
increase monitoring burden
create interruption/context-switch cost
reduce coordination cost
increase information volume
```

Therefore:

```text
AgentUse
!= WorkloadReduction by definition
```

The relevant object is the changed `LoadProfile`.

---

# 51. Automation can hide load rather than remove it

A Human supervising reliable automation may have low continuous activity but high consequence responsibility and rare-event vigilance demand.

Thus:

```text
LowActionFrequency
!= LowOperationalLoad
```

and HOC2 verification fragility may dominate.

---

# 52. Recovery of one channel can coexist with degradation elsewhere

Examples:

```text
subjective fatigue improves, vigilance still poor
heart rate normalizes, stress appraisal remains high
physical soreness improves, cognitive fatigue worsens
```

Therefore RecoveryProfile must preserve endpoint multiplicity.

---

# 53. State estimation evidence ladder

Approximate operational ordering:

```text
S0 one subjective report
S1 repeated subjective report / short trace
S2 one target performance probe
S3 repeated target performance + subjective state
S4 relevant exposure/sleep/load history
S5 changed-demand / break / recovery probe
S6 replicated within-person state-response pattern
S7 consequential naturalistic history
```

This is not a universal medical evidence hierarchy.

---

# 54. Recovery evidence ladder

```text
R0 reports feeling better
R1 one post-intervention performance measure
R2 repeated target endpoint recovery
R3 multiple relevant endpoints
R4 delayed recheck / sustained recovery
R5 return under realistic demand
R6 replicated recovery response across episodes
```

A recovery claim should name its target and evidence level.

---

# 55. Minimum operational modes

A state-aware system can use:

```text
STATE_WITHIN_EXPECTED_RANGE
COMPENSATED_HIGH_LOAD
FATIGUE_EVIDENCE
STATE_MISMATCH
RECOVERY_IN_PROGRESS
RECOVERY_INCOMPLETE
TRANSIENT_POST_RECOVERY_IMPAIRMENT
SUSTAINABILITY_CONCERN
INSUFFICIENT_EVIDENCE
```

These are purpose-bound summaries.

---

# 56. Minimal counterexamples

## C1 — tired but accurate

H reports severe fatigue while preserving accuracy through increased effort.

```text
SubjectiveFatigue != PerformanceFailure
```

## C2 — feels fine but impaired

Sleep-restricted H reports moderate alertness while vigilance is materially degraded.

```text
SubjectiveAlertness != FullObjectiveCapacityReadout
```

## C3 — low scheduled hours, high load

Two hours of continuous safety-critical monitoring can exceed six hours of routine low-demand work on relevant dimensions.

```text
TimeOnCalendar != Load
```

## C4 — break helps performance, not distress

A rest intervention can improve task performance while subjective wellbeing changes differently.

```text
PerformanceRecovery != SubjectiveRecovery
```

## C5 — nap creates transient impairment

Recovery action improves later state but produces sleep inertia immediately after waking.

```text
RecoveryAction != ImmediateReadinessGain
```

## C6 — one long recovery period is incomplete

Accumulated sleep restriction can leave residual neurobehavioral deficits after one recovery night.

```text
OneRecoveryEpisode != FullRestoration
```

## C7 — same task, different load

Expert with good tool support experiences low load; novice without support experiences high load.

```text
TaskDemand != HumanLoad
```

## C8 — automation changes rather than removes load

AI generates output rapidly but requires intense rare-error verification.

```text
Automation != LoadElimination
```

---

# 57. Update and expiry

## RegulatoryStateView

Fast-expiring. Recompute with material state/exposure changes.

## FatigueProfile

Fast/intermediate depending on domain. Do not persist as trait.

## LoadProfile

Update with task/support/assignment/context changes.

## SustainableWorkEnvelope

Slow/intermediate; update only after enough repeated evidence and revise when task/support/consequence ecology changes.

## RecoveryProfile

Update longitudinally after interventions/exposure end.

## PersonalBaseline

Slow update with change-point awareness; do not chase short noise.

---

# 58. Reflexivity

A state-aware Agent changes the state it predicts.

```text
Agent predicts fatigue
→ reduces workload
→ future performance improves
```

This does not prove the original fatigue model was wrong.

Conversely:

```text
Agent sees good performance
→ keeps increasing load
→ Human compensates
→ hidden cost accumulates
```

Therefore:

```text
ObservedStateTrajectory
may be policy-conditioned.
```

---

# 59. Anti-overprotection guard

State support can become harmful if every weak signal causes task removal.

Possible failure:

```text
minor fatigue report
→ system blocks challenging activity
→ fewer opportunities / lower autonomy
```

So HOC4 must preserve:

```text
uncertainty
consequence level
reversibility
Human preference/agency
```

and avoid converting state evidence into paternalistic authority.

---

# 60. Normative firewall

```text
Fatigue != Incapacity by definition
LowReadinessEstimate != LossOfAutonomy
HighWorkload != Employer/AgentPermissionToControl
StateRiskPrediction != Authority
RecoveryRecommendation != MedicalOrder
LowSustainableEnvelope != LowMoralWorth
```

High-stakes safety or medical decisions require their own legitimate decision rules and professional boundaries where applicable.

---

# 61. Foundation / HOC dependency map

```text
HF3  attention / control / metacognition
HF4  effort / motivation / goal conflict
HF5  regulation / sleep pressure / stress / fatigue / recovery
HF6  adaptation / resilience / trajectory
HF10 stopping / decision
HF11 execution / feedback / tool use
HF19 work/task/technology/organization
HF21 affect / appraisal / action readiness
HD9 organismic health / functional trajectory boundary
HD10 person-specific baselines / projections
HOC1 capability / readiness / bottleneck
HOC2 verification / calibration / evidence sufficiency
HOC3 learning / support dependence / practice scheduling
```

No new Foundation is required.

---

# 62. Canonical forbidden inferences

```text
TaskDemand != AssignedLoad
AssignedLoad != ExperiencedLoad
ScheduledTime != Workload
ExperiencedLoad != Fatigue
Fatigue != SleepPressure
Fatigue != PerformanceDecline
Fatigue != ResourceRemaining
Fatigue != LowMotivation
Fatigue != Burnout
StressExposure != StressResponse
StressResponse != Damage
Cortisol/OneMarker != Stress
EffortCost != Fatigue
StablePerformance != StableState
NoPerformanceDecline != NoCost
Rest != Recovery
ElapsedTime != RecoveryAmount
SubjectiveRecovery != ObjectiveRecovery
MarkerBaselineReturn != WholeSystemRestoration
RecoveredFunction != SameInternalStateAsBefore
OneRecoveryEpisode != FullRestoration
RecoveryIntervention != ImmediateReadinessIncrease
PersonalBaseline != PopulationReference
PersonalBaseline != ImmutableSetpoint
AgentUse != WorkloadReduction
Automation != LoadElimination
FatigueProfile != Diagnosis
StateRiskAlert != DiseaseClaim
```

---

# 63. Operational reasoning grammar

A Human-supporting Agent can use HOC4 as:

```text
1. Declare RegulationTargetSpec and consequence threshold.
2. Build current RegulatoryStateView from available evidence.
3. Build LoadProfile: demand, assignment, experience, cumulative exposure, support.
4. Compare with HOC1 Capability/Readiness using LoadCapacityMismatch.
5. If mismatch/fragility appears, determine whether it is:
     state
     capability
     support
     external demand
     verification
     uncertainty
6. Build FatigueProfile only with typed evidence.
7. If continuing, estimate SustainableWorkEnvelope / compensation burden.
8. If recovery is needed, declare RecoveryTargetSpec.
9. Choose NextBestRegulationAction or RecoveryActionSpec.
10. Account for transient recovery costs such as sleep inertia when relevant.
11. Reassess target-specific performance/state after intervention.
12. Update HOC1 readiness, HOC2 verification assumptions and HOC3 learning schedule.
13. Escalate persistent/severe/unexplained state disturbance to the appropriate health/safety owner rather than diagnosing inside HOC4.
```

This is a reasoning grammar, not a medical or occupational-control engine.

---

# 64. HOC4 stop rule

HOC4 is complete because it has:

```text
separated task demand, assignment, experienced load and cumulative exposure;
reconstructed RegulatoryStateView and LoadProfile;
reconstructed LoadCapacityMismatch without one universal workload ratio;
retained FatigueProfile as multi-channel/domain-scoped evidence rather than a fuel gauge;
made subjective–objective state mismatch first-class;
introduced PerformanceMaintenanceCost for compensated strain;
separated sleep pressure, circadian phase, fatigue and performance;
reconstructed typed stress exposure/response/burden grammar;
retained protocol-relative ReserveProfile;
introduced SustainableWorkEnvelope as horizon/consequence/support-relative;
introduced StateRiskAlert without medical diagnosis;
reconstructed RecoveryTargetSpec, RecoveryProfile and RecoveryActionSpec;
separated rest, recovery, subjective recovery and objective functional recovery;
made transient recovery costs such as sleep inertia explicit;
introduced RecoveryNeedInference and NextBestRegulationAction;
connected state/load/recovery directly to HOC1 readiness, HOC2 verification and HOC3 learning;
retained PersonalBaseline/change-point logic;
added automation/load redistribution, reflexivity and anti-overprotection guards;
and preserved health, authority and autonomy boundaries.
```

No Foundation reopen condition is triggered.

```text
FoundationReopenCondition(HF0–HF23) = false
NextDeepRoute = UNKNOWN
```

HOC4 does not preselect HOC5.
