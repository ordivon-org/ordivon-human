---
schema_version: 1
id: human.operational-concepts.hoc9
title: HOC9 — Habits, Routines, Automaticity and Contextual Behavioral Control
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
summary: Reconstructs persistent context-sensitive behavioral control downstream of HF4/HF10/HF11 and HOC3–HOC5. HOC9 separates repeated behavior, routine, habit-like control, automaticity, skill, implementation intention, convention, compulsion/addiction, and identity. It introduces BehavioralControlTargetSpec, RepetitionHistory, CueContextMap, ContextStabilityProfile, HabitEvidenceProfile, OutcomeSensitivityProbe, ControlModeProfile, RoutineSpec, RoutineReliabilityProfile, AutomaticityProfile, HabitGoalConflictCase, ContextShiftEvent, HabitFormationTrajectory, HabitMaintenanceTrajectory, RoutineBreakdownCase, HabitDisruptionPlan, HabitReplacementPlan, EnvironmentDesignIntervention, ExceptionalConditionOverride, AgentMediatedRoutineCase and NextBestHabitOperation. Repetition and outcome-insensitive responding are evidence but not definitions; devaluation validity must be checked; context stability can support habit formation and context changes can disrupt habitual performance; automaticity need not monotonically increase with practice; routines can be deliberate and beneficial without being habits; and efficient automatic control is not universally desirable. No Foundation is reopened and HOC10 is not preselected.
evidence_status: verified-synthesis
readiness: READY
related:
  - human.foundations.hf4
  - human.foundations.hf10
  - human.foundations.hf11
  - human.operational-concepts.hoc5
---
# HOC9 — Habits, Routines, Automaticity and Contextual Behavioral Control

## 0. Admission

A post-HOC8 operational-space search compared identity/self-model, habits/routines, pain/pleasure, narrative/meaning, creativity/imagination, accessibility and distributed activity.

Habit/routine/automaticity survived because HOC5 uses habit as a cause but does not reconstruct its evidence, context dependence, formation, breakdown or intervention grammar.

---

# 1. Core deletion

Reject:

```text
repeated often
→ habit
→ automatic
→ skilled
→ efficient
→ good
```

Canonical guards:

```text
RepeatedBehavior != Habit
BehaviorFrequency != HabitStrength by definition
OutcomeInsensitiveResponse != ProvenHabit
HabitLikeControl != NoGoal
Habit != Routine
Habit != Skill
Habit != Automaticity
Routine != Automaticity
Skill != Habit
Automaticity != Skill
Practice != AutomaticityGuarantee
Automaticity != AbsenceOfAgency
ImplementationIntention != Habit
Convention != IndividualHabit
Habit != Identity
Habit != AddictionByDefinition
Habit != CompulsionByDefinition
OldRoutine != GoodRoutine
EfficientRoutine != AppropriateRoutine
StableRoutine != ContextRobustRoutine
```

---

# 2. BehavioralControlTargetSpec

Every HOC9 query declares:

```text
BehavioralControlTargetSpec = {
  target behavior/action sequence,
  desired/undesired/neutral status from Human-authorized objective,
  contexts,
  cue candidates,
  outcome/reward structure,
  goal relation,
  time horizon,
  support/Agent boundary,
  consequence level,
  intended operation,
  evidence protocol
}
```

Possible operations:

```text
understand current control
preserve beneficial routine
build new routine
reduce unwanted habitual capture
increase automaticity where useful
restore deliberation in exceptional cases
recover after context change
redesign environment
```

---

# 3. RepetitionHistory

```text
RepetitionHistory(H, Behavior, interval) = {
  occurrence count,
  spacing,
  context distribution,
  cue co-occurrence,
  outcome history,
  deliberate/assigned context if known,
  interruption history,
  support/Agent involvement,
  recency,
  uncertainty
}
```

Repetition is learning history evidence, not habit identity.

---

# 4. Frequency is not enough

Repeated behavior can remain deliberately controlled.

Conversely, a cue-response association can influence behavior without maximal raw frequency.

Therefore:

```text
Frequency
is evidence about learning opportunity,
not a sufficient habit measure.
```

---

# 5. CueContextMap

```text
CueContextMap(H, Behavior, interval) = {
  temporal cues,
  spatial cues,
  preceding actions,
  object/interface cues,
  social cues,
  internal-state cues,
  device/tool cues,
  composite contexts,
  cue reliability,
  cue ambiguity,
  competing responses
}
```

The map describes observed candidate control inputs; it does not prove causal habit links.

---

# 6. Cue != context totality

A local cue can be embedded in a wider context.

```text
Cue
!= EntireContext
```

Context can include location, time, sequence position, people, device, task state and internal state.

---

# 7. ContextStabilityProfile

```text
ContextStabilityProfile(H, Behavior, interval) = {
  recurring cue stability,
  location stability,
  temporal stability,
  sequence/predecessor stability,
  social/tool stability,
  variability intentionally introduced,
  context changes,
  behavior persistence under those changes
}
```

This helps distinguish behavior tied tightly to one ecology from behavior robust across varied contexts.

---

# 8. Stable context can support habitual automaticity

Human habit-building studies find greater context stability can predict/increase automaticity and repeated goal enactment under studied protocols.

HOC9 retains:

```text
StableContext
can facilitate
CueResponseLearning / Automaticity
```

not:

```text
StableContext guarantees habit.
```

---

# 9. Context change can disrupt habits

Naturalistic research on students changing university contexts found habitual behaviors were more likely to survive when relevant performance contexts remained stable, whereas changed circumstances disrupted some habitual behavior and increased alignment with current intentions.

HOC9 therefore treats:

```text
ContextShift
```

as a first-class intervention/falsifier.

---

# 10. Context dependence is not weakness by definition

A context-specific routine can be exactly what the Human wants.

```text
ContextSpecific
!= BadHabit
```

The question is whether the target behavior should transport to other contexts.

---

# 11. HabitEvidenceProfile

```text
HabitEvidenceProfile(H, Behavior, interval) = {
  repetition history,
  cue/context association evidence,
  automatic response activation evidence,
  intention-behavior dissociation if present,
  outcome/revaluation sensitivity evidence,
  context-shift sensitivity,
  cognitive-load/attention evidence,
  subjective automaticity if reported,
  response latency/fluency where relevant,
  competing-goal slips,
  measurement-validity checks,
  uncertainty
}
```

No single field is universally sufficient.

---

# 12. Habit-like control

Working operational definition:

```text
HabitLikeControl
= learned context/cue-sensitive response tendency
  whose current expression is less dependent on recomputing present outcome value
  than fully deliberative goal-directed control
```

This is a control-mode description, not a second internal agent.

---

# 13. Habit-like != goal absent

A Human can have:

```text
Goal: do not R
Habit-like cue: evokes R
```

Therefore:

```text
HabitLikeResponse
!= NoGoal
```

HOC5 GoalState remains authoritative for declared goals.

---

# 14. OutcomeSensitivityProbe

A classic diagnostic question is whether changing current outcome value or action-outcome relation changes behavior.

```text
OutcomeSensitivityProbe = {
  target outcome,
  manipulation/revaluation method,
  evidence manipulation actually changed value/contingency,
  subsequent response,
  control comparison,
  uncertainty
}
```

---

# 15. Devaluation validity is mandatory

Recent Human habit methodology demonstrates that ineffective outcome devaluation can make goal-directed behavior appear habitual.

Therefore:

```text
ObservedOutcomeInsensitivity
without validated devaluation
!= HabitEvidenceStrongEnough
```

This is a hard measurement guard.

---

# 16. Outcome sensitivity is not the only habit surface

Naturalistic context-cue habits may be hard to probe through laboratory devaluation.

Thus:

```text
NoDevaluationTest
!= NoHabitEvidence
```

HOC9 triangulates cue/context, repetition, slips, automaticity and intervention responses.

---

# 17. ControlModeProfile

```text
ControlModeProfile(H, Behavior, Context, t) = {
  current goal sensitivity,
  action-outcome model use,
  cue-response influence,
  cached/learned sequence contribution,
  planning depth if relevant,
  automaticity evidence,
  cognitive-control requirement,
  support/Agent mediation,
  uncertainty
}
```

Avoid binary `habit vs goal` when evidence supports mixtures.

---

# 18. Control can be mixed/hierarchical

Human planning can select learned/cached action sequences.

```text
GoalDirectedPlan
can contain
HabitualOrCachedSubsequence
```

Therefore:

```text
ModelBased
and
HabitLike
```

need not be flat mutually exclusive modules.

---

# 19. Model-free != habit identity

Two-step/model-based measures are useful research coordinates but not pure habit meters.

```text
ModelFreeEstimate
!= HabitStrengthByDefinition
```

Measurement reliability/task-model assumptions matter.

---

# 20. RoutineSpec

Routine is retained as an explicitly broader practical concept:

```text
RoutineSpec(H, Purpose/Context, interval) = {
  action sequence,
  trigger/start condition,
  ordering,
  optional/mandatory steps,
  decision points,
  expected duration,
  support/tools,
  completion condition,
  fallback,
  exceptional-condition override,
  ownership/provenance
}
```

A routine can be deliberately executed and need not be habitual.

---

# 21. Habit != routine

```text
Routine
= recurrent organized behavior pattern / sequence

Habit
= learned context/cue-linked control tendency
```

A routine can be:

```text
fully deliberate
partly automatic
mostly habitual
institutionally mandated
Agent-mediated
```

---

# 22. Routine != institution/organizational routine

HOC9 primarily concerns Human-level recurrent action organization.

Organizational routines are owned by HF19/institutional/Host-like domains.

```text
IndividualRoutine
!= OrganizationalRoutine
```

though one can participate in the other.

---

# 23. RoutineReliabilityProfile

```text
RoutineReliabilityProfile(H, Routine, interval) = {
  start reliability,
  sequence completion,
  omission/substitution errors,
  timing variability,
  context dependence,
  interruption recovery,
  exception handling,
  support dependence,
  outcome quality,
  maintenance cost,
  uncertainty
}
```

This is often more useful than habit strength for operational workflows.

---

# 24. Routine reliability != habit strength

A checklist-supported deliberate routine can be highly reliable with low habit-like control.

A strong habit can be reliably triggered but yield poor task outcomes.

```text
RoutineReliability
!= HabitStrength
```

---

# 25. AutomaticityProfile

```text
AutomaticityProfile(H, Behavior/Skill, Context, interval) = {
  attentional demand,
  dual-task cost where appropriate,
  response initiation latency,
  subjective effort/control if relevant,
  need for conscious monitoring,
  interference susceptibility,
  context/cue dependence,
  error monitoring,
  transfer across conditions,
  uncertainty
}
```

Automaticity is multidimensional evidence, not a hidden percentage.

---

# 26. Automaticity != habit

A skilled sequence may become fluent/low-attention while still being deliberately selected.

A habitual response can be cue-triggered while execution itself remains attention-demanding.

```text
Automaticity
!= Habit
```

---

# 27. Practice != automaticity guarantee

Recent motor-sequence evidence shows extensive learning can coexist with persistent or increased sequence-specific dual-task costs.

Therefore:

```text
MorePractice
!= MonotonicAutomaticityIncrease
```

HOC3 learning and HOC9 automaticity remain separate trajectories.

---

# 28. Low dual-task cost is evidence, not definition

Some automatic behavior can still require attention under specific contexts.

```text
LowDualTaskCost
!= UniversalAutomaticityProof
```

Probe choice must match the behavior.

---

# 29. Skill != habit

Skill concerns learned capability/reliability in performing a task family.

Habit concerns selection/control tendency.

```text
SkilledButNonhabitual
```

and:

```text
HabituallySelectedButLowSkill
```

are both possible.

HOC1/HOC3 own skill evidence.

---

# 30. Implementation intention != habit

An if-then plan deliberately creates a prospective trigger-response policy.

It can eventually interact with automaticity/habit learning but:

```text
ImplementationPlanPresent
!= HabitFormed
```

HOC5 remains the owner of implementation intentions.

---

# 31. Convention != habit

A social convention depends on interdependent expectations/coordination.

An individual habit can exist without another participant matching it.

```text
Convention
!= IndividualHabit
```

HOC6/HF13 own convention/coordination aspects.

---

# 32. Habit != compulsion/addiction

Repeated unwanted behavior, craving and outcome insensitivity can appear in addiction/compulsion contexts, but HOC9 does not diagnose them.

```text
HabitEvidence
!= AddictionDiagnosis
!= CompulsionDiagnosis
```

If clinically consequential/persistent/severe, HOC7 health ownership may become relevant.

---

# 33. Habit != identity

A Human saying:

```text
I am the kind of person who does X
```

is a self-model/identity statement.

It may reinforce behavior, but:

```text
Habit
!= Identity
```

and breaking a habit does not require declaring a new identity.

---

# 34. HabitGoalConflictCase

```text
HabitGoalConflictCase = {
  current goal/value,
  competing habitual response,
  triggering context,
  action actually taken,
  awareness timing,
  control resources/state,
  consequence,
  intervention history,
  uncertainty
}
```

This specializes HOC5 IntentionActionGap.

---

# 35. Slip != low motivation

An unwanted habitual slip can occur under strong goal commitment.

```text
HabitSlip
!= LowMotivation
```

The useful intervention may target cues/context rather than values.

---

# 36. ContextShiftEvent

```text
ContextShiftEvent = {
  prior context,
  new context,
  changed cues,
  retained cues,
  behavior/routine change,
  goal/intention change,
  support/tool change,
  adaptation interval,
  uncertainty
}
```

Context shifts include:

```text
moving home
new school/job
new device/UI
travel
schedule change
new Agent/tool
new relationship/team
```

---

# 37. Context shift is a natural experiment

If behavior disappears after relevant context change while goals remain similar, that supports context dependence.

But:

```text
BehaviorChangeAfterMove
!= HabitProof
```

because opportunity, motivation and constraints may also change.

HOC5/HOC1 controls remain necessary.

---

# 38. HabitFormationTrajectory

```text
HabitFormationTrajectory(H, Behavior, interval) = {
  repetition history,
  context stability,
  cue-response evidence,
  automaticity evidence,
  goal dependence,
  interruptions,
  support,
  formation/degradation phases,
  uncertainty
}
```

This avoids a single universal `days to form habit` number.

---

# 39. No universal habit-formation duration

Formation depends on behavior complexity, repetition, context stability, motivation, difficulty and individual/context variation.

Therefore:

```text
HabitFormsInNdays
```

is rejected as a generic law.

---

# 40. Formation can reverse/degrade

Longitudinal evidence supports both formation and degradation trajectories.

```text
HabitStrength_t
```

need not rise monotonically with time.

Context instability, low repetition or changed conditions can weaken expression/automaticity.

---

# 41. HabitMaintenanceTrajectory

```text
HabitMaintenanceTrajectory = {
  current cue ecology,
  repetition continuity,
  interruptions,
  context shifts,
  reinstatement evidence,
  automaticity trend,
  goal relation,
  outcome quality,
  uncertainty
}
```

Maintenance is different from initial formation.

---

# 42. RoutineBreakdownCase

```text
RoutineBreakdownCase = {
  routine,
  failed/omitted step,
  context change,
  interruption,
  cue failure,
  state/load,
  tool/Agent change,
  exceptional condition,
  downstream consequence,
  recovery evidence
}
```

The breakdown need not indicate lost skill.

---

# 43. Routine breakdown != capability loss

```text
RoutineFailure
!= SkillLoss
!= MotivationLoss
```

A missing cue or context change can be enough.

---

# 44. Interruption recovery is first-class

Routines that work only without interruptions are operationally fragile.

Track:

```text
resume-point recovery
missed-step detection
state reconstruction
verification after interruption
```

This connects HOC9 to HOC5 ExecutionProfile.

---

# 45. ExceptionalConditionOverride

Beneficial automation/habit can become harmful when conditions change.

```text
ExceptionalConditionOverride = {
  routine/habit,
  exceptional trigger,
  stop/pause condition,
  required conscious check,
  alternate action,
  authority,
  expiry/update
}
```

---

# 46. Automatic routine needs an exception path

Examples:

```text
usual transfer/payment flow
but account/amount/risk unusually high

usual deployment flow
but production state changed

usual medication/support routine
but externally supplied clinical plan changed
```

HOC9 does not define domain safety rules; it ensures routine automation can yield control when those rules trigger.

---

# 47. Efficient routine != appropriate routine

Automation can reduce cognitive cost while propagating stale behavior.

```text
EfficientExecution
!= ContextualCorrectness
```

This mirrors HOC5 plan-rigidity and HOC8 stale-knowledge guards.

---

# 48. HabitDisruptionPlan

For an unwanted Human-endorsed target behavior:

```text
HabitDisruptionPlan = {
  target behavior,
  cue/context hypotheses,
  desired replacement/stop objective,
  environment changes,
  cue removal/alteration,
  competing response,
  friction changes,
  implementation support,
  monitoring/probe,
  consent/ownership,
  fallback,
  reassessment
}
```

---

# 49. Disruption is not always suppression

Often a more robust intervention is:

```text
replace cue-response relation
```

or:

```text
change environment
```

rather than relying entirely on momentary inhibition.

---

# 50. HabitReplacementPlan

```text
HabitReplacementPlan = {
  old cue/context,
  old response,
  Human-endorsed target,
  replacement response,
  cue plan,
  feasibility/capability,
  reward/outcome relation,
  repetition plan,
  context-generalization target,
  progress evidence,
  override
}
```

HOC9 does not assume replacement always dominates simple removal.

---

# 51. Replacement must be feasible

A replacement response that requires unavailable capability/time/resources will fail even if motivationally endorsed.

```text
ReplacementPlan
requires HOC1 feasibility/readiness.
```

---

# 52. EnvironmentDesignIntervention

```text
EnvironmentDesignIntervention = {
  target behavior,
  cue added/removed/repositioned,
  friction increased/decreased,
  default changed,
  tool/Agent behavior changed,
  expected control-path effect,
  Human authorization,
  reversibility,
  collateral effects,
  evidence plan
}
```

---

# 53. Environment design can support self-regulation

A Human need not solve every habit conflict through internal inhibitory effort.

```text
SelfRegulation
can include
EnvironmentDesign
```

This already follows HF4 and is operationalized here.

---

# 54. Environment design can become manipulation

Changing cues/defaults/friction changes behavior.

Therefore:

```text
CanImproveGoalAttainment
!= PermissionToRedesignHumanEnvironment
```

HOC5 goal ownership/consent constraints remain mandatory.

---

# 55. CuePolicy

For supportive Agents/interfaces:

```text
CuePolicy = {
  target action,
  cue type,
  timing/context,
  repetition,
  salience,
  stop/expiry,
  Human preference,
  interruption/load cost,
  adaptation logic
}
```

CuePolicy differs from ReminderPolicy when the goal is stable contextual triggering rather than explicit notification.

---

# 56. More cues != better habit

Too many cues can:

```text
create noise
increase interruption load
reduce discriminability
become ignorable
```

HOC4 load/attention constraints apply.

---

# 57. Context generalization can be a target or a bug

For some behaviors:

```text
perform anywhere
```

is desired.

For others:

```text
perform only in specific context
```

is safer.

Thus:

```text
MoreGeneralization
!= BetterHabit universally
```

---

# 58. Habit portability

```text
HabitPortabilityProfile(H, Behavior) = {
  contexts where response persists,
  contexts where it weakens,
  new cues adopted,
  goal-control re-emergence,
  uncertainty
}
```

Useful during relocation, travel, new devices or workflow redesign.

---

# 59. Routine portability differs

A written/checklist routine may transfer well across contexts even when habitual cueing does not.

```text
RoutinePortability
!= HabitPortability
```

---

# 60. AgentMediatedRoutineCase

Persistent Agents can become part of a Human routine:

```text
AgentMediatedRoutineCase = {
  Human goal,
  Human cue,
  Agent trigger/action,
  Human review/override,
  repeated workflow,
  independent Human contribution,
  dependency,
  learning effects,
  failure/absence behavior,
  ownership/authority
}
```

---

# 61. Agent can become the cue

Examples:

```text
Agent notification → Human action
Agent opens workspace → Human begins study
Agent asks check-in question → Human reviews plan
```

This can create a stable useful scaffold.

But:

```text
AgentCueDependence
!= InternalHabitStrength
```

---

# 62. Agent can become the routine executor

If the Agent performs the behavior automatically:

```text
HumanRoutine
may become
Human–Agent SystemRoutine
```

This does not mean Human acquired the habit/skill.

```text
SystemRoutineReliability
!= HumanHabit
```

---

# 63. Automation can erase evidence

When Agent always triggers/executes a routine, there may be little evidence about:

```text
Human cue detection
Human initiation
Human unaided routine reliability
```

HOC3/HOC5 support-dependence guards apply.

---

# 64. Agent routine changes can be abrupt context shifts

A new Agent version, notification policy, UI, tool or memory behavior can remove previously stable cues.

```text
AgentVersionChange
can induce
ContextShiftEvent
```

HOC6 version guards and HOC9 routine portability interact.

---

# 65. Habit support should follow the target

If the consumer objective is:

```text
joint system reliability
```

Agent-mediated routine may be ideal.

If objective is:

```text
Human independent self-initiation
```

persistent Agent cueing may hide the target capability.

HOC3 objective determines whether to fade support.

---

# 66. Habit formation can reduce cognitive load

Well-formed routines/habits can reduce repeated deliberation in stable environments.

This can free resources for other tasks.

But:

```text
LowerDeliberationCost
!= BetterOutcome under changed context
```

---

# 67. Habit can preserve behavior when motivation fluctuates

A Human may continue an endorsed beneficial behavior even when momentary motivation is low because contextual control carries execution.

```text
StableBehavior
with low momentary motivation
!= contradiction
```

This is one practical benefit of habit-like control.

---

# 68. Habit can preserve unwanted behavior too

Likewise:

```text
Goal changed
but cue-response tendency persists
```

HOC9 explains why preference/goal revision may not immediately change behavior.

---

# 69. Routine as memory scaffold

Sequences/checklists can externalize prospective memory demands.

```text
RoutineSupport
can reduce
working/prospective-memory burden
```

without being internal memory gain.

HOC7/HF7 external-memory distinctions remain.

---

# 70. Routine as verification scaffold

A verification routine can improve reliability by ensuring repeatable checks.

But repeated checking can itself become stale if failure modes change.

```text
VerificationRoutine
!= VerificationAdequacyForever
```

HOC2 evidence freshness applies.

---

# 71. Routines can accumulate technical debt

A routine may persist after:

```text
underlying tool changes
objective changes
risk changes
better method appears
```

HOC9 calls this:

```text
RoutineStaleness
```

not a Human trait.

---

# 72. RoutineStalenessView

```text
RoutineStalenessView = {
  routine version,
  original objective,
  current objective,
  environment/tool changes,
  current outcome quality,
  exception frequency,
  known obsolete steps,
  review date,
  uncertainty
}
```

---

# 73. OldRoutine != good routine

Persistence is evidence of history, not current optimality.

```text
OldRoutine
!= GoodRoutine
```

This applies at Human and organizational levels.

---

# 74. Habit monitoring can create the behavior it measures

Repeated self-monitoring, reminders or prompts can become new cues.

Thus:

```text
HabitMeasurement
may be HabitIntervention
```

Reflexivity must be logged in longitudinal studies/products.

---

# 75. Self-report automaticity is evidence, not ground truth

Feeling that a behavior is automatic can be useful.

But:

```text
SubjectiveAutomaticity
!= CompleteControlMechanismEvidence
```

Use alongside behavioral/context/intervention evidence when stakes justify it.

---

# 76. HabitEvidence can be sparse

Naturalistic systems may not have validated devaluation experiments or cognitive-load probes.

Then HOC9 should output:

```text
HABIT_LIKE_HYPOTHESIS
```

with uncertainty rather than claiming a proven habit.

---

# 77. Control-state modes

Useful operational modes include:

```text
DELIBERATIVE_GOAL_DOMINANT
MIXED_CONTROL
CUE_CONTEXT_DOMINANT
ROUTINE_RELIABLE
ROUTINE_FRAGILE
AUTOMATICITY_HIGH_WITHIN_SCOPE
HABIT_GOAL_CONFLICT
CONTEXT_SHIFT_DISRUPTION
ROUTINE_STALE
INSUFFICIENT_EVIDENCE
```

These are summaries, not brain modules.

---

# 78. HabitFormationEvidence ladder

Approximate:

```text
H0 repeated behavior only
H1 repeated in stable cue/context
H2 subjective/behavioral automaticity evidence
H3 cue-response association / context disruption evidence
H4 intention-behavior dissociation or controlled-load evidence
H5 valid outcome-sensitivity/revaluation probe where appropriate
H6 repeated multi-method evidence / intervention response
```

Not every naturalistic habit needs H5; different paradigms answer different questions.

---

# 79. Routine evidence ladder

```text
R0 claimed routine
R1 repeated sequence observed
R2 stable trigger/order/completion
R3 interruption/exception behavior observed
R4 cross-context portability tested
R5 longitudinal reliability/staleness evidence
```

Routine evidence need not prove habit.

---

# 80. Automaticity evidence ladder

```text
A0 subjective fluency only
A1 reduced initiation latency/effort
A2 reduced monitoring requirement in target context
A3 dual-task/interference evidence where valid
A4 cross-condition evidence
A5 retained automaticity after material context/support changes
```

Again, no universal single automaticity test.

---

# 81. NextBestHabitOperation

```text
NextBestHabitOperation(
  H,
  TargetBehavior,
  GoalState,
  HabitEvidence,
  RoutineState,
  Context,
  Constraints
)
```

candidate actions:

```text
KEEP_ROUTINE
MONITOR_ONLY
CLARIFY_HUMAN_GOAL
COLLECT_CUE_CONTEXT_EVIDENCE
VALIDATE_OUTCOME_SENSITIVITY
STABILIZE_CONTEXT
ADD_DISCRIMINATIVE_CUE
REDUCE_CUE_NOISE
BUILD_ROUTINE
SIMPLIFY_ROUTINE
ADD_CHECKLIST/EXTERNAL_STATE
PRACTICE_SEQUENCE
DESIGN_ENVIRONMENT
REMOVE/ALTER_TRIGGER
INCREASE_FRICTION_FOR_UNWANTED_RESPONSE
REDUCE_FRICTION_FOR_TARGET_RESPONSE
ADD_REPLACEMENT_RESPONSE
FORM_IMPLEMENTATION_PLAN
ADD_EXCEPTION_OVERRIDE
INTERRUPT_AUTOMATIC_PATH
REQUIRE_CONSCIOUS_CHECK
TEST_CONTEXT_PORTABILITY
REFRESH_STALE_ROUTINE
RECOVER_AFTER_CONTEXT_SHIFT
FADE_AGENT_CUE_IF_INDEPENDENCE_IS_TARGET
ADD_AGENT_CUE_IF_SYSTEM_RELIABILITY_IS_TARGET
ESCALATE_HEALTH/SAFETY_OWNER_IF_BEHAVIOR_IS_CLINICALLY_CONSEQUENTIAL
NO_INTERVENTION
```

---

# 82. Keep routine is a valid action

Operational systems should not continuously optimize stable beneficial routines.

```text
ObservedHabit
!= ProblemToFix
```

A reliable low-cost routine may be exactly the desired state.

---

# 83. No intervention is also valid

If:

```text
Human goal unclear
behavior low-stakes
habit inference weak
intervention cost high
privacy/autonomy concerns dominate
```

then:

```text
NO_INTERVENTION
```

is correct.

---

# 84. Habit optimization is not productivity maximization

A system must not convert every repetitive behavior into an optimization target.

```text
ProductivityOpportunity
!= HumanAuthorizationToShapeHabit
```

---

# 85. Dark-pattern boundary

Cue engineering, friction, defaults and repetition can be used to manipulate Human behavior for operator goals.

HOC9 therefore requires:

```text
Human-endorsed objective
transparent/legitimate authority
reversibility where feasible
stop/override
```

for significant behavioral shaping.

---

# 86. Persuasive interface != Human preference

A behavior repeated because a system engineered salience/default/friction is not automatically evidence that Human values it.

```text
BehaviorFrequencyUnderPersuasiveDesign
!= EndorsedPreference
```

HOC5 preference/goal boundaries remain active.

---

# 87. Routine dependency can be intentional

A Human may intentionally choose a checklist, reminder, Agent or environmental cue as a permanent support.

```text
SupportDependence
!= Defect
```

The independence target must be explicitly declared before fading support.

---

# 88. Habit and state interact

Fatigue/stress/load can alter control allocation, cue capture and conscious monitoring.

```text
HabitExpression_t
depends partly on current state
```

without turning habit into fatigue.

HOC4 supplies state evidence.

---

# 89. Habit and learning interact

Repeated behavior can strengthen cue-response relations; changes in habits are learning/history-dependent.

But:

```text
LearningOccurred
!= HabitFormed
```

HOC3 owns broader learning/retention/transfer.

---

# 90. Habit and knowledge interact

Knowing that a routine is obsolete does not guarantee immediate behavioral change.

```text
KnowledgeOfBetterAction
!= BetterActionSelected
```

HOC8 epistemic state and HOC9 control state remain distinct.

---

# 91. Habit and coordination interact

Team workflows can rely on participant routines.

If one Human/Agent changes routine unexpectedly, handoffs can fail.

HOC6 should model the dependency; HOC9 models the participant routine.

---

# 92. Habit and health interact

Medication, rehabilitation, sleep or health-monitoring behaviors may be routinized.

But HOC9 cannot convert habit evidence into medical advice.

HOC7 retains clinical boundary.

---

# 93. Habit and identity interact without identity

Identity labels can motivate or stabilize behavior, and repeated behavior can update self-models.

But:

```text
IdentityNarrative
!= HabitMechanism
```

The post-HOC8 identity residual remains separate.

---

# 94. Update / expiry

## CueContextMap

Update aggressively after environment/tool/schedule changes.

## HabitEvidenceProfile

Slow/intermediate; require repeated evidence and note method changes.

## RoutineReliabilityProfile

Update after failures, interruptions, redesign or context shifts.

## AutomaticityProfile

Update after training, long non-use, context change or changed task complexity.

## HabitFormationTrajectory

Longitudinal; preserve formation/degradation phases.

## RoutineStalenessView

Review when objective/tool/risk/version changes.

---

# 95. Reflexivity

Any HOC9 policy can change future evidence:

```text
Agent reminder becomes cue
cue redesign changes context
habit label changes self-monitoring
routine automation removes Human initiation evidence
```

Therefore:

```text
ObservedHabitEvidence
may be policy-conditioned.
```

---

# 96. Privacy boundary

Behavioral traces can expose intimate routines.

Collect only target-relevant cue/context history.

```text
CanInferRoutine
!= PermissionToMapDailyLife
```

---

# 97. Normative firewall

```text
Habit != MoralFault
Habit != Character
Habit != Identity
AutomaticBehavior != NoAgencyByDefinition
UnwantedHabit != ConsentToIntervention
BeneficialPrediction != AuthorityToManipulate
RoutineCompliance != EndorsedValue
BehaviorFrequency != Preference
HabitStrength != HumanWorth
```

---

# 98. Foundation / HOC dependency map

```text
HF3  attention/control
HF4  goals/motivation/habit-like control/self-regulation
HF6  learning/adaptation/history
HF7  prospective memory/cues
HF8  knowledge/self-model
HF10 planning/model-based/cached/hierarchical control
HF11 skill/automaticity/action/tool control
HF13 convention boundary
HF19 organizational routine boundary
HOC1 capability/readiness
HOC2 verification/check routines
HOC3 learning/support dependence
HOC4 state/load/recovery
HOC5 goal/action/friction/implementation/precommitment
HOC6 team workflow/roles/handoffs
HOC7 health/accessibility boundary
HOC8 knowledge/freshness/competence
```

No new Foundation is required.

---

# 99. Canonical forbidden inferences

```text
RepeatedBehavior != Habit
Frequency != HabitStrengthByDefinition
OutcomeInsensitiveResponse != ProvenHabit
HabitLikeControl != NoGoal
Habit != Routine
Habit != Skill
Habit != Automaticity
Routine != Automaticity
Skill != Habit
Automaticity != Skill
Practice != AutomaticityGuarantee
Automaticity != AbsenceOfAgency
ImplementationIntention != Habit
Convention != IndividualHabit
Habit != AddictionByDefinition
Habit != CompulsionByDefinition
Habit != Identity
RoutineReliability != HabitStrength
MorePractice != MonotonicAutomaticityIncrease
ModelFreeEstimate != HabitStrengthByDefinition
StableContext != HabitGuarantee
ContextSpecific != BadHabit
BehaviorChangeAfterContextShift != HabitProof
MoreGeneralization != BetterHabit
OldRoutine != GoodRoutine
EfficientRoutine != AppropriateRoutine
SystemRoutineReliability != HumanHabit
SupportDependence != Defect
BehaviorFrequencyUnderPersuasiveDesign != EndorsedPreference
ObservedHabit != ProblemToFix
ProductivityOpportunity != HumanAuthorizationToShapeHabit
```

---

# 100. Operational reasoning grammar

A Human-supporting Agent can use HOC9 as:

```text
1. Declare BehavioralControlTargetSpec and Human-authorized objective.
2. Build RepetitionHistory and CueContextMap without calling repetition habit.
3. Inspect ContextStabilityProfile and context-shift history.
4. Build HabitEvidenceProfile from multiple evidence channels.
5. If using outcome devaluation/revaluation, validate that the manipulation actually changed the outcome relation/value.
6. Infer ControlModeProfile as mixed/uncertain rather than forcing binary goal/habit modules.
7. If the object is a recurrent workflow, build RoutineSpec + RoutineReliabilityProfile separately.
8. If low-attention execution matters, build AutomaticityProfile separately from skill/habit.
9. Localize HabitGoalConflictCase or RoutineBreakdownCase when behavior conflicts with current goal/outcome.
10. Choose NextBestHabitOperation: preserve, stabilize, redesign cues/environment, replace response, add override, test portability, recover after context shift, change Agent support, or do nothing.
11. Re-evaluate after tool/schedule/location/Agent version changes because cue ecology may have changed.
12. Never infer preference, identity, diagnosis, moral fault or intervention authority from behavioral regularity alone.
```

This is a reasoning grammar, not a behavior-control engine.

---

# 101. HOC9 stop rule

HOC9 is complete because it has:

```text
separated repeated behavior, habit, routine, automaticity and skill;
introduced BehavioralControlTargetSpec and RepetitionHistory;
reconstructed CueContextMap and ContextStabilityProfile;
reconstructed HabitEvidenceProfile with explicit measurement uncertainty;
made OutcomeSensitivityProbe and devaluation-validity checks first-class;
reconstructed mixed/hierarchical ControlModeProfile;
reconstructed RoutineSpec and RoutineReliabilityProfile independently of habit;
reconstructed AutomaticityProfile independently of skill/practice;
added HabitGoalConflictCase, ContextShiftEvent and RoutineBreakdownCase;
reconstructed formation, maintenance, degradation and portability trajectories;
added ExceptionalConditionOverride and routine-staleness guards;
reconstructed HabitDisruptionPlan, HabitReplacementPlan and EnvironmentDesignIntervention;
made cue policy and context redesign legitimate but autonomy-constrained interventions;
reconstructed Agent-mediated routines and Human-versus-system routine attribution;
connected habit control to learning, state, goals, coordination, health and epistemic freshness;
added measurement reflexivity, behavioral privacy and anti-manipulation guards;
and retained NO_INTERVENTION / KEEP_ROUTINE as legitimate outcomes.
```

No Foundation reopen condition is triggered.

```text
FoundationReopenCondition(HF0–HF23) = false
NextDeepRoute = UNKNOWN
```

HOC9 does not preselect HOC10.
