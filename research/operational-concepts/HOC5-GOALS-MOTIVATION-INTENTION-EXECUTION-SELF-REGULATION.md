---
schema_version: 1
id: human.operational-concepts.hoc5
title: HOC5 — Goals, Motivation, Intention, Execution and Self-Regulation
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
summary: Reconstructs the practical action-allocation and execution layer downstream of frozen Human Foundations and HOC1–HOC4. HOC5 separates goal content, activation, priority, commitment, maintenance, progress and attainment; preference from endorsed value; motivation from one scalar drive; intention from implementation policy; initiation from continuation and completion; friction from low motivation; and procrastination from a stable trait. It introduces GoalPortfolio, GoalStateView, PreferenceSnapshot, MotivationProfile, ActionAllocationProfile, ImplementationPlan, ExecutionProfile, FrictionMap, GoalConflictView, ProgressEvidence, PrecommitmentPolicy, ExecutionFailureInference and NextBestExecutionAction. Plans, deadlines, reminders, incentives and Agent delegation are treated as interventions that can help or distort action; rigid plans can misfire outside intended conditions; progress feedback can cause coasting/shifting; deadline effects are not universal; and Agent convenience is not Human goal authority. No Foundation is reopened and no engineering schema is prescribed.
evidence_status: verified-synthesis
readiness: READY
related:
  - human.operational-concepts.hoc1
  - human.operational-concepts.hoc2
  - human.operational-concepts.hoc3
  - human.operational-concepts.hoc4
  - human.foundations.hf4
  - human.foundations.hf10
  - human.foundations.hf11
---
# HOC5 — Goals, Motivation, Intention, Execution and Self-Regulation

## 0. Practical-priority decision

Remaining major operational families were compared again:

```text
trust / coordination
health / functioning
goal / motivation / preference / execution
```

Goal/motivation/execution wins HOC5 because it remains the largest missing action-control bridge across HOC1–HOC4:

```text
Human can do it
+ Human is ready
+ evidence is sufficient
+ state is sustainable

but

will the target actually receive action?
will action start?
will it persist?
will the plan survive interruptions/conflict?
should the Agent remind, reduce friction, restructure, delegate or leave it alone?
```

Trust/coordination remains high-value, but HOC2 already reconstructed epistemic reliance. Health/functioning remains high-stakes and benefits from the HOC4 state/recovery boundary before operationalization.

This is practical ordering, not ontology.

---

# 1. Core deletion

Reject the common pipeline:

```text
want X
→ value X
→ goal X
→ intend X
→ motivated for X
→ act on X
→ persist
→ attain X
```

Every arrow can fail.

Canonical guards:

```text
Want != Goal
Goal != Preference
Preference != EndorsedValue
GoalContent != GoalActivation
GoalActivation != GoalPriority
GoalPriority != GoalCommitment
GoalKnowledge != GoalMaintenance
GoalIntention != ImplementationPolicy
Intention != Initiation
Initiation != Continuation
Continuation != Completion
Commitment != Initiation
LowAction != LowMotivation
LowEffort != LowMotivation
HighEffort != HighEndorsedValue
Motivation != Opportunity
Motivation != Capability
Motivation != Agency
Friction != LowMotivation
Procrastination != StableTrait by definition
GoalAttainment != GoalQuality
AgentExecution != HumanGoalAttainment by identity
```

---

# 2. GoalPortfolio

Humans commonly carry multiple active, dormant, conflicting and nested goals.

```text
GoalPortfolio(H, interval) = {
  candidate goals,
  active goals,
  suspended goals,
  completed/abandoned goals,
  hierarchy / means-end relations,
  conflicts,
  temporal horizons,
  ownership/provenance,
  uncertainty
}
```

Canonical guard:

```text
OneHuman != OneCurrentGoal
```

A portfolio is a practical view, not the Human's complete value system.

---

# 3. GoalStateView

For one goal `G`:

```text
GoalStateView(H,G,t) = {
  content,
  activation,
  priority,
  commitment,
  maintenance,
  implementation policy,
  progress evidence,
  attainment status,
  conflict/interdependence,
  current support,
  uncertainty
}
```

The dimensions must remain separable.

A goal can be:

```text
important but inactive
active but low priority
high priority but weakly maintained
strongly committed but poorly implemented
well implemented but blocked by opportunity
```

---

# 4. Goal provenance

A practical Human-support system should distinguish where a goal came from when relevant:

```text
explicit Human statement
inferred from repeated action
institutional obligation
social commitment
Agent suggestion
habitual routine
current task assignment
```

Do not silently promote inferred or assigned goals into endorsed Human goals.

```text
InferredGoal != EndorsedGoal
AssignedGoal != PersonalGoal
```

---

# 5. Goal ownership under Agent support

Agent systems can propose, operationalize or execute goals.

They must not silently transform:

```text
AgentRecommendation
```

into:

```text
HumanCommitment
```

or:

```text
AgentConvenience
```

into:

```text
HumanPriority
```

This becomes a hard HOC5 boundary.

---

# 6. PreferenceSnapshot

Preference remains useful as a current comparative relation:

```text
PreferenceSnapshot(H, ChoiceSet, Context, t)
```

Possible evidence:

```text
stated ranking
observed choice
willingness to pay/work/wait
repeated revealed choices
choice under changed framing/stakes
```

But:

```text
ObservedChoice != TimelessPreference
Preference != EndorsedValue
Preference != Welfare
Preference != Consent
```

---

# 7. Preference stability is empirical

A consumer may learn that a preference is stable across some contexts.

Then it can widen scope cautiously.

But stability is evidence-driven:

```text
CrossContextPreferenceStability
```

not assumed from one click, one purchase or one conversation.

---

# 8. MotivationProfile

HOC5 reconstructs motivation as action allocation rather than one drive level.

```text
MotivationProfile(H,G,t,Context) = {
  current goal priority,
  expected outcome value,
  expected efficacy/control,
  initiation tendency,
  persistence tendency,
  effort willingness,
  delay tolerance,
  uncertainty tolerance,
  opportunity cost,
  intrinsic interest / attraction where relevant,
  external incentive structure,
  habit/cue support or conflict,
  current state/fatigue influence,
  social/institutional pressure,
  commitment,
  uncertainty
}
```

Not every consumer needs every field.

---

# 9. Motivation is not one quantity

Two Humans may show equal output but different profiles:

```text
A: high interest + low external pressure
B: low interest + high external reward
```

or:

```text
A: wants outcome strongly, unwilling to pay effort cost
B: moderate outcome value, high willingness to work
```

Therefore:

```text
SameBehavior != SameMotivationProfile
```

---

# 10. Reward can raise effort without rewriting values

Experimental sustained-attention work shows higher rewards can increase task performance and effort under studied conditions while sustained attention itself is treated as effortful/costly.

HOC5 uses this only to support:

```text
Incentive
can alter current action allocation
without proving
EndorsedValue changed.
```

Thus:

```text
RewardEffect != ValueConversion
```

---

# 11. Motivation is opportunity-sensitive

A Human can strongly value and intend an outcome but lack:

```text
access
permission
money
time
tool
partner
information
physical opportunity
```

Therefore:

```text
NoAction
!= NoMotivation
```

HOC1/HOC4 external bottlenecks must remain visible.

---

# 12. Motivation is capability-sensitive without becoming capability

Low expected efficacy can rationally reduce effort allocation.

But:

```text
CapabilityEstimate
!= Motivation
```

and a wrong low capability estimate can itself suppress action.

This creates a reflexive loop:

```text
LowCapabilityBelief
→ LowerAttemptProbability
→ LessEvidence/Learning
→ PersistentLowCapabilityBelief
```

HOC5 must avoid treating the loop as proof of intrinsic inability.

---

# 13. Effort decomposition

At least separate:

```text
ObjectiveEffortDemand
SubjectiveEffort
EffortCost
WillingnessToWork
ActualEffortExpenditure
```

Then:

```text
ObjectiveDemand
!= SubjectiveEffort
!= EffortCost
!= WillingnessToWork
!= EffortExpenditure
!= Performance
```

This prevents `effort` from becoming a generic explanation.

---

# 14. ActionAllocationProfile

A practical operational object is:

```text
ActionAllocationProfile(H,t,OpportunitySet) = {
  active goals,
  candidate actions,
  current priorities,
  time allocation,
  attention allocation,
  effort allocation,
  switching tendencies,
  protected commitments,
  deferred goals,
  external constraints,
  uncertainty
}
```

This is closer to what an Agent needs than one motivation score.

---

# 15. Priority is relational

```text
Priority(x,t)
```

means relative allocation under current competing demands.

It does not mean:

```text
x is morally most important
x is the person's deepest value
x should always be done first
```

A low-priority but deeply valued long-horizon goal can coexist with an urgent short-term obligation.

---

# 16. GoalConflictView

```text
GoalConflictView(H,t) = {
  goals in conflict,
  shared means,
  resource conflicts,
  temporal conflicts,
  normative/role conflicts,
  short-vs-long-horizon conflicts,
  possible sequencing / compromise,
  uncertainty
}
```

Goal conflict is normal, not model failure.

---

# 17. Means can serve multiple goals

One action can support several goals, and one goal can have several means.

```text
Goal != Means
```

This enables practical leverage:

```text
choose a means that satisfies G1 and G2
```

rather than treating every goal as a separate task queue.

---

# 18. IntentionState

```text
IntentionState(H, Action/Goal, t)
```

captures current prospective commitment/orientation toward performing an action.

It is not:

```text
performed action
implementation plan
permission
consent for unrelated actions
```

Canonical:

```text
Intention != Action
Intention != ImplementationPolicy
```

---

# 19. Intention–action gap is an operational object

Instead of calling a Human inconsistent or lazy, model:

```text
IntentionActionGap(H,G,interval)
```

and ask which stage failed:

```text
opportunity never occurred
cue not recognized
goal not maintained
implementation unspecified
initiation failed
competing goal won
habit/cue captured action
state deteriorated
resource/permission absent
execution failed
plan was abandoned rationally
```

---

# 20. ImplementationPlan

HOC5 retains implementation planning as a practical tool:

```text
ImplementationPlan = {
  target goal/action,
  trigger/cue,
  planned response,
  context,
  start condition,
  completion criterion,
  fallback,
  stop/override condition,
  expiry,
  provenance/ownership
}
```

A simple form is:

```text
IF situation X,
THEN perform response Y.
```

But the plan remains an intervention, not a guarantee.

---

# 21. Planning can bridge intention and action

Randomized/field experiments on implementation intentions show that sufficiently specific if-then planning can improve goal pursuit under some tasks and populations, including initiation and shielding ongoing pursuit from interfering states.

HOC5 retains:

```text
ImplementationSupport
```

as a legitimate lever without concluding:

```text
AllGoalsNeedIfThenPlans
```

---

# 22. Planning effectiveness is person/protocol/task dependent

Experimental work comparing planning interventions found that spontaneous plan quality and intervention benefit can depend on planning skill/profile.

Therefore:

```text
PlanPresent != GoodPlan
```

and:

```text
SamePlanningIntervention
!= SameBenefitAcrossHumans
```

Planning itself has capability/fit requirements.

---

# 23. Rigid plans can misfire

Experiments on implementation intentions show planned responses can generalize to similar situations and sometimes impair performance when the planned response is inappropriate.

Therefore every plan should permit:

```text
override
context check
expiry
revision
```

where misgeneralization matters.

Canonical:

```text
AutomaticPlanExecution
!= AlwaysCorrectExecution
```

---

# 24. Cue quality matters

A plan with a vague trigger:

```text
when I have time
```

is operationally different from:

```text
when lecture ends at 16:00 and no urgent task exists
```

Useful plan quality can include:

```text
cue detectability
cue specificity
response feasibility
response sufficiency
conflict probability
fallback quality
```

No one universal plan-quality score is required.

---

# 25. ExecutionProfile

HOC5 reconstructs:

```text
ExecutionProfile(H, TaskFamily, Context, interval) = {
  initiation latency,
  initiation reliability,
  continuation/persistence,
  interruption recovery,
  plan adherence,
  adaptive deviation,
  completion reliability,
  time-estimation error,
  verification before completion,
  support dependence,
  abandonment/stop quality,
  uncertainty
}
```

It measures implementation/execution behavior, not moral character.

---

# 26. Initiation is distinct

A Human may:

```text
understand task
value goal
intend action
have capability
be physically ready
```

and still fail to begin.

So:

```text
Commitment != Initiation
```

Initiation can be a distinct operational bottleneck.

---

# 27. Continuation is distinct

Starting well does not imply persistence.

```text
Initiation != Continuation
```

Continuation can fail because of:

```text
state/fatigue change
feedback
unexpected cost
competing goals
interruptions
uncertainty
poor progress
new evidence
rational reprioritization
```

---

# 28. Completion is distinct

A task can remain nearly complete indefinitely because finalization has its own requirements:

```text
verification
formatting
submission
handoff
commit/release
permission
risk acceptance
```

So HOC5 may distinguish:

```text
CompletionBottleneck
```

from initiation and core execution.

---

# 29. Stopping quality matters

Persistence is not always good.

A robust ExecutionProfile should include whether H can:

```text
stop when objective is obsolete
abandon dominated plan
escalate after repeated failure
avoid sunk-cost persistence
```

Therefore:

```text
Persistence != Virtue by definition
```

---

# 30. FrictionMap

A central HOC5 object is:

```text
FrictionMap(H, Action/Goal, t)
```

candidate friction classes:

```text
unclear next action
high startup cost
context switching
missing tool/resource
information search burden
permission
coordination delay
physical inconvenience
UI/interface cost
uncertainty
fear/anticipated affect
high verification burden
state/fatigue
habitual distraction
```

Friction is operationally useful because reducing it can increase action without changing underlying values.

---

# 31. Friction != motivation

Example:

```text
Human strongly wants to submit form
but login flow is broken.
```

Reducing friction changes behavior while motivation may be unchanged.

```text
FrictionReduction
!= MotivationIncrease
```

This distinction is especially important for Agent automation.

---

# 32. Agent can reduce friction

Agent support can:

```text
retrieve information
prepare draft
fill reversible fields
schedule reminder
break task into next action
maintain context
execute low-level steps
coordinate with tools
```

and thereby increase goal attainment.

But:

```text
AgentDoingMore
!= HumanMotivationIncrease
```

and may reduce Human learning or independent execution capability depending on HOC3 objective.

---

# 33. Agent can also create friction

Agent systems can increase:

```text
review burden
notification load
choice overload
interruptions
verification demand
permission prompts
context switching
```

Therefore:

```text
AgentSupport != FrictionReduction by definition
```

---

# 34. ExecutionFailureInference

Instead of `user failed`, use:

```text
ExecutionFailureInference(H, Goal/Task, episode)
→ ranked hypotheses
```

candidate types:

```text
GOAL_NOT_ACTIVE
LOW_PRIORITY
GOAL_CONFLICT
LOW_EXPECTED_EFFICACY
HIGH_EFFORT_COST
FRICTION
STATE/FATIGUE
OPPORTUNITY_BLOCK
CAPABILITY_GAP
IMPLEMENTATION_GAP
INITIATION_GAP
PERSISTENCE_GAP
INTERRUPTION_RECOVERY_GAP
VERIFICATION/COMPLETION_GAP
RATIONAL_ABANDONMENT
INSUFFICIENT_EVIDENCE
```

This directly reuses HOC1 BottleneckInference.

---

# 35. Procrastination is a pattern, not one cause

HOC5 permits a scoped:

```text
DelayPattern(H, Target, interval)
```

when intended/valuable actions are repeatedly deferred.

But it rejects:

```text
Procrastination = one stable trait
```

as the default operational explanation.

Delay can arise from:

```text
aversiveness
uncertainty
implementation gap
competing rewards
state
friction
poor time estimation
fear/perfectionism-like processes
opportunity change
```

---

# 36. MCII / implementation support can reduce some delay patterns

A 2026 randomized trial in undergraduates found mental contrasting with implementation intentions improved willingness to initiate academic tasks and reduced task aversiveness relative to a positive-thinking control under the study protocol.

HOC5 uses this as scoped evidence that:

```text
DelayPattern
can be intervention-sensitive
```

and should not automatically be treated as fixed character.

---

# 37. Deadlines are not universal treatment

A 2026 replication of a classic procrastination/deadline experiment reported that deadline manipulations had negligible effects on its main performance/survey outcomes and did not reproduce the original pattern.

HOC5 therefore explicitly rejects:

```text
MoreDeadlines = BetterSelfControl
```

Deadlines are one intervention whose effect depends on task/population/structure.

---

# 38. PrecommitmentPolicy

HOC5 retains voluntary precommitment as a distinct tool:

```text
PrecommitmentPolicy(H,G) = {
  future option restricted,
  trigger,
  cost/penalty,
  reversibility,
  Human authorization,
  expiry,
  override conditions,
  evidence of benefit/harm
}
```

Precommitment changes the future choice architecture rather than merely increasing momentary inhibition.

---

# 39. Precommitment != coercion

A system cannot infer permission to restrict future Human options merely because doing so may improve predicted goal attainment.

```text
PredictedSelfControlBenefit
!= ConsentToRestriction
```

Human authorization and reversal rules are first-class.

---

# 40. ReminderPolicy

Reminders are another intervention, not evidence of low motivation.

```text
ReminderPolicy = {
  target,
  trigger/time,
  urgency,
  repetition rule,
  escalation rule,
  stop condition,
  Human preference,
  interruption cost
}
```

Too many reminders can become load/friction via HOC4.

---

# 41. ProgressEvidence

```text
ProgressEvidence(H,G,interval)
```

can include:

```text
objective subgoal completion
state/position relative to target
quality-adjusted output
verified milestone
remaining uncertainty
```

Progress is not simply activity count.

```text
Activity != Progress
```

---

# 42. Progress feedback changes allocation

Experimental work on multiple-goal striving shows better-than-needed progress toward one goal can cause reduced subsequent effort on that goal and resource shifting toward another goal.

HOC5 therefore treats progress feedback as an intervention on allocation, not a neutral display.

```text
ProgressSignal
can cause
Coasting / GoalShifting
```

---

# 43. Coasting is not necessarily failure

If a Human is ahead of target, reducing effort and reallocating resources can be rational.

```text
LowerEffortAfterProgress
!= MotivationLoss by definition
```

This is another reason one-dimensional motivation tracking fails.

---

# 44. Progress display can also mislead

Progress markers can:

```text
reduce uncertainty
increase persistence
```

or:

```text
create complacency
redirect attention
encourage gaming
```

depending on context.

Therefore:

```text
MoreProgressFeedback != BetterGoalAttainment by definition
```

---

# 45. GoalProgressView

A useful operational summary is:

```text
GoalProgressView = {
  target,
  verified current state,
  completed subgoals,
  remaining critical path,
  uncertainty,
  pace relative to horizon,
  blockers,
  next decision point,
  evidence age
}
```

Avoid fake precision when the target itself is qualitative/ambiguous.

---

# 46. Priority and progress should not collapse

A goal can be:

```text
high priority + little progress
low priority + nearly complete
```

so:

```text
GoalProgress != GoalPriority
```

Agent scheduling needs both.

---

# 47. Commitment is not sunk-cost persistence

Commitment can stabilize long-horizon pursuit across temporary fluctuations.

But new evidence can legitimately cause abandonment.

Therefore:

```text
Commitment
!= NeverReviseGoal
```

A useful system preserves both:

```text
commitment stability
```

and:

```text
revision/exit conditions
```

---

# 48. GoalRevisionEvent

```text
GoalRevisionEvent = {
  prior goal/state,
  new evidence/context,
  revision type,
  Human authorization,
  changed priority/criterion/horizon,
  downstream plan updates
}
```

Revision types can include:

```text
clarify
narrow
expand
resequence
suspend
abandon
replace
```

This avoids treating every changed goal as inconsistency.

---

# 49. Goal persistence across state change

HOC5 allows a long-horizon goal to persist while current motivation fluctuates.

```text
PersistentGoalCommitment
!= ConstantMomentaryMotivation
```

This is why an Agent may sometimes support execution of a previously endorsed goal despite low momentary initiation tendency—but only within Human-authorized policy.

---

# 50. Human agency / autonomy boundary

HOC5 must distinguish:

```text
Human chose goal
Human chose means
Human has meaningful override
Human is merely presented nominal choices
```

Choice count alone is not autonomy.

```text
NominalChoice != ActualControl
```

---

# 51. Autonomy support is not equivalent to unlimited choice

Experimental work manipulating choice/autonomy support shows that meaningful choice context can alter motivation-related responses under studied conditions.

HOC5 retains:

```text
PerceivedControl / MeaningfulChoice
```

as possible motivational inputs, not as proof that maximizing option count is always beneficial.

---

# 52. Delegation policy

A Human goal can be pursued by Human, Agent or joint execution.

```text
ExecutionMode = {
  HUMAN_INDEPENDENT,
  HUMAN_WITH_SUPPORT,
  AGENT_DELEGATED,
  JOINT,
  HUMAN_VERIFY_ONLY
}
```

The correct mode depends on:

```text
capability/readiness
learning objective
state/load
verification
responsibility/authority
goal ownership
time/cost
support reliability
```

---

# 53. Delegating means does not delegate the goal by identity

Example:

```text
Human goal = submit accurate tax form
Agent action = prepare draft
```

The Human goal can remain Human-owned while execution is delegated.

```text
DelegatedExecution
!= DelegatedGoalOwnership
```

---

# 54. Agent must preserve stop/override authority where required

If Human remains responsible/authorized, an autonomous execution policy should preserve meaningful:

```text
inspection
pause
cancel
revision
scope limits
```

appropriate to the task.

```text
AgentAutonomy
!= HumanGoalAuthorityTransfer by default
```

---

# 55. NextBestExecutionAction

A central HOC5 output is:

```text
NextBestExecutionAction(
  H,
  Goal/Task,
  GoalState,
  MotivationProfile,
  ExecutionEvidence,
  Constraints
)
```

candidate actions:

```text
DO_NEXT_STEP
CLARIFY_GOAL
CLARIFY_NEXT_ACTION
REPRIORITIZE
RESOLVE_GOAL_CONFLICT
REDUCE_FRICTION
FORM_IMPLEMENTATION_PLAN
SET_REMINDER
ADD_CUE
ADD_TOOL/AGENT_SUPPORT
DELEGATE_REVERSIBLE_STEP
REQUEST_PERMISSION/RESOURCE
REDUCE_SCOPE
TAKE_BREAK / DEFER_STATE
PRECOMMIT_WITH_AUTHORIZATION
VERIFY_PROGRESS
REVISE_GOAL
ABANDON_RATIONALLY
COLLECT_MORE_EVIDENCE
NO_INTERVENTION
```

---

# 56. No intervention is a valid action

A Human-supporting Agent should not optimize every detected intention–action gap.

Possible reasons:

```text
Human chose not to act
priority legitimately changed
intervention cost > benefit
uncertainty too high
goal ownership unclear
behavior is private/low-stakes
```

So:

```text
DetectedGap
!= PermissionToNudge
```

---

# 57. Execution support can become manipulation

Friction reduction, reminders, defaults, incentives and precommitment can alter behavior.

The system must distinguish:

```text
supporting an endorsed goal
```

from:

```text
steering toward system/operator-preferred behavior
```

HOC5 therefore requires goal ownership/provenance and authority boundaries for high-impact interventions.

---

# 58. Personalization reflexivity

If an Agent predicts:

```text
H usually procrastinates
```

and always executes tasks early on H's behalf, it removes evidence about Human initiation capability and can reshape future habits/capabilities.

Thus:

```text
ObservedExecutionPattern
may be policy-conditioned.
```

HOC3 support-dependence logic applies directly.

---

# 59. Avoid moralized labels

Operationally prefer:

```text
initiation gap
friction
state mismatch
unclear next action
priority conflict
implementation gap
```

before labels such as:

```text
lazy
undisciplined
unmotivated
irresponsible
```

The latter may be social/normative judgments, not causal explanations.

---

# 60. Minimal counterexamples

## C1 — strong goal, no action

Human strongly wants to attend event but lacks transport.

```text
NoAction != NoMotivation
```

## C2 — low effort, high goal value

Agent automation makes manual effort unnecessary.

```text
LowEffort != LowValue
```

## C3 — high effort, low endorsement

Human works intensely under coercive institutional pressure.

```text
HighEffort != HighEndorsedValue
```

## C4 — intention, failed initiation

Human intends to start but cue never triggers / startup friction dominates.

```text
Intention != Initiation
```

## C5 — good implementation, low motivation change

Specific cue-action plan increases execution without changing goal value.

```text
ImplementationGain != MotivationIncrease
```

## C6 — deadline does not help

A deadline manipulation fails to change procrastination/performance in a replication.

```text
Deadline != UniversalSelfControlTool
```

## C7 — progress reduces focal effort

Ahead-of-target feedback causes coasting and shift toward another goal.

```text
LowerEffort != GoalAbandonment
```

## C8 — rigid if-then plan misfires

Cue triggers planned response in a similar context where a different response is required.

```text
PlanAutomaticity != ContextualOptimality
```

## C9 — Agent completes task, Human goal unresolved

Agent submits a draft Human never endorsed.

```text
TaskCompletion != HumanGoalAttainment
```

## C10 — rational abandonment

New evidence makes original goal dominated.

```text
Abandonment != SelfRegulationFailure by definition
```

---

# 61. Evidence ladder for goal/action inference

Approximate ordering:

```text
G0 one inferred goal from one behavior
G1 explicit statement
G2 repeated statement / planning behavior
G3 choices consistent across opportunities
G4 costly commitment / repeated resource allocation
G5 longitudinal pursuit under changing contexts
```

But even strong evidence about goal commitment does not establish welfare or moral value.

---

# 62. Evidence ladder for execution bottlenecks

```text
E0 narrative guess
E1 one missed action
E2 repeated same-stage failure
E3 changed-friction/opportunity probe
E4 implementation-plan intervention
E5 within-person repeated intervention
E6 transfer to changed contexts
```

The label `procrastination`, `low motivation` or `poor execution` should not jump ahead of the evidence.

---

# 63. Update / expiry

## GoalStateView

Update when Human revises goal, context/obligation changes, or strong contradictory evidence emerges.

## PreferenceSnapshot

Fast/intermediate; expiry depends on choice domain and state sensitivity.

## MotivationProfile

Fast-expiring around task/state/opportunity changes.

## ActionAllocationProfile

Fast-expiring; priorities can change within hours/minutes.

## ExecutionProfile

Slower; requires repeated episodes and domain scope.

## FrictionMap

Update aggressively with interface/tool/context changes.

## PrecommitmentPolicy / ReminderPolicy

Versioned and explicitly authorized; expire when target or Human preference changes.

---

# 64. HOC1 connection

Capability/readiness prevents motivation from becoming a catch-all explanation.

```text
Can do?
Ready now?
```

must be checked separately from:

```text
Will allocate action?
```

---

# 65. HOC2 connection

Goal pursuit may require epistemic actions:

```text
verify progress
reassess assumptions
request evidence
escalate uncertainty
```

A strong commitment should not suppress HOC2 falsification/verification.

```text
Commitment != EvidenceImmunity
```

---

# 66. HOC3 connection

Execution policy changes learning:

```text
Human attempts
Agent hints
Agent answers
Agent executes
```

produce different future capability trajectories.

Therefore `NextBestExecutionAction` and `NextBestLearningAction` can disagree legitimately.

---

# 67. HOC4 connection

Low initiation/persistence may reflect state/load rather than goal value.

```text
Fatigue != LowMotivation
```

HOC4 supplies state evidence before HOC5 infers action-allocation failure.

---

# 68. Normative firewall

```text
Preference != Welfare
Preference != Consent
PredictedGoal != AuthorizedGoal
HighMotivation != MoralDuty
LowMotivation != MoralFailure
GoalCommitment != PermissionToOverrideHuman
PredictedSelfControlBenefit != ConsentToPrecommitment
DetectedIntentionActionGap != PermissionToNudge
ProductivityGoal != HumanWelfare
AgentRecommendation != HumanPriority
```

---

# 69. Foundation dependency map

```text
HF3  attention / control / goal maintenance
HF4  goals / preference / motivation / effort / self-regulation
HF5  state/fatigue/need
HF8  representations / self-model / knowledge
HF9  reasoning about means/evidence
HF10 decision / planning / stopping / commitment
HF11 initiation / execution / feedback / tool use
HF12 social commitments / roles / coordination
HF13 institutional obligation / authority
HF14–17 normative/rights/governance boundaries
HF19 work/production context
HF21 affect/appraisal/action readiness
HOC1 capability/readiness/bottleneck
HOC2 evidence/verification/reliance
HOC3 learning/scaffolding/support dependence
HOC4 state/load/recovery
```

No new Foundation is required.

---

# 70. Canonical forbidden inferences

```text
Goal != Preference
Preference != EndorsedValue
Preference != Welfare
Preference != Consent
GoalContent != GoalActivation
GoalActivation != GoalPriority
GoalPriority != GoalCommitment
GoalKnowledge != GoalMaintenance
GoalIntention != ImplementationPolicy
Intention != Action
Intention != Initiation
Commitment != Initiation
Initiation != Continuation
Continuation != Completion
LowAction != LowMotivation
LowEffort != LowMotivation
HighEffort != HighValue
Motivation != Opportunity
Motivation != Capability
Motivation != Agency
Friction != LowMotivation
FrictionReduction != MotivationIncrease
AgentSupport != FrictionReduction by definition
Procrastination != StableTrait by definition
Deadline != UniversalSelfControlTool
PlanPresent != GoodPlan
AutomaticPlanExecution != AlwaysCorrectExecution
Progress != Activity
GoalProgress != GoalPriority
LowerEffortAfterProgress != MotivationLoss
Persistence != Virtue
Abandonment != Failure by definition
DelegatedExecution != DelegatedGoalOwnership
TaskCompletion != HumanGoalAttainment
AgentRecommendation != HumanCommitment
DetectedGap != PermissionToNudge
```

---

# 71. Operational reasoning grammar

A Human-supporting Agent can use HOC5 as:

```text
1. Establish GoalPortfolio / GoalStateView with provenance and uncertainty.
2. Separate current PreferenceSnapshot from endorsed goal/value when relevant.
3. Project MotivationProfile and ActionAllocationProfile only for the current opportunity/context.
4. Check HOC1 capability/readiness and HOC4 state before inferring low motivation.
5. If intention exists but action does not, localize the IntentionActionGap.
6. Build FrictionMap and ExecutionFailureInference.
7. Choose among:
     clarify goal
     clarify next action
     resolve conflict
     reduce friction
     form implementation plan
     cue/remind
     add support
     delegate reversible means
     obtain resource/permission
     defer state
     precommit with authorization
     verify progress
     revise/abandon goal
     no intervention
8. Observe execution at initiation, continuation, completion and stopping stages separately.
9. Update GoalProgressView without confusing activity with progress.
10. Recompute priorities because progress can cause coasting/shifting.
11. Preserve Human override/goal ownership when Agent acts.
12. Update HOC3 learning/support-dependence effects if execution is increasingly delegated.
```

This is a reasoning grammar, not a productivity-control engine.

---

# 72. HOC5 stop rule

HOC5 is complete because it has:

```text
reconstructed GoalPortfolio and GoalStateView;
separated goal content/activation/priority/commitment/maintenance/progress/attainment;
retained PreferenceSnapshot without timeless preference/welfare claims;
reconstructed multidimensional MotivationProfile and ActionAllocationProfile;
separated effort demand, experience, cost, willingness and expenditure;
reconstructed IntentionActionGap instead of moralized failure labels;
reconstructed ImplementationPlan with cue, fallback, override and expiry;
retained implementation intentions as conditional intervention, not universal rule;
added plan-rigidity/misgeneralization guards;
reconstructed ExecutionProfile across initiation/continuation/completion/stopping;
introduced FrictionMap and ExecutionFailureInference;
reconstructed procrastination as a scoped delay pattern rather than one trait;
retained deadline/precommitment/reminder interventions with non-universality and authorization guards;
reconstructed ProgressEvidence/GoalProgressView and coasting/shifting effects;
made rational goal revision/abandonment legitimate;
introduced NextBestExecutionAction including NO_INTERVENTION;
made Human goal ownership/provenance and Agent delegation boundaries explicit;
connected execution to HOC1–HOC4;
and preserved autonomy, consent, welfare and authority firewalls.
```

No Foundation reopen condition is triggered.

```text
FoundationReopenCondition(HF0–HF23) = false
NextDeepRoute = UNKNOWN
```

HOC5 does not preselect HOC6.
