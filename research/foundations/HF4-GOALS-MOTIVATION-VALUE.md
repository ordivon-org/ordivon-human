---
schema_version: 1
id: human.foundations.hf4
title: HF4 — Goals, Motivation, Value, Affect, Effort, Reward and Self-Regulation
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
summary: HF4 decomposes goals, preferences, multiple meanings of value, reward, wanting/liking, affect, effort, motivation, habits and self-regulation. It replaces a scalar motivation model with a contextual action-allocation profile, separates goal representation from implementation and attainment, distinguishes effort demand/cost/expenditure, and exposes bodily state regulation as the next foundation boundary.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
  - HF4
related:
  - human.foundations.hf3
  - human.foundations.hf4.sources
  - human.foundations.hf4.continuation
---
# HF4 — Goals, Motivation, Value, Affect, Effort, Reward and Self-Regulation

## 0. Status and question

HF4 continues directly from HF3.

HF3 established that Human priority and control depend on variables such as:

```text
Goal
Value
History
State
ActionDemand
```

without yet defining them.

HF4 asks:

> **Why does one possible action, goal or outcome receive more priority than
> another, and how should goals, values, rewards, affect, effort, motivation and
> self-regulation be represented without turning them into one scalar “drive”?**

HF4 is not a motivational personality test, not a utility function for a person,
not a hidden-preference inference engine and not a normative theory of the good
life.

Its purpose is to reconstruct a minimum grammar for **why and how Human action is
allocated**.

---

# 1. The first deletion: Motivation is not one quantity

Everyday language encourages sentences such as:

```text
He has high motivation.
She lacks motivation.
This reward increased motivation.
```

But those sentences may refer to very different observable changes:

```text
starting sooner
choosing one goal over another
working harder
persisting longer
tolerating larger costs
returning after failure
resisting an alternative
paying more for an option
seeking more information
```

These do not always covary.

HF4 therefore rejects:

```text
Motivation(H,t) = one scalar M
```

as a foundation primitive.

Instead it retains a **MotivationProfile**:

```text
MotivationProfile(H,G,t,context) = {
  direction,
  initiation readiness,
  vigor,
  persistence,
  cost tolerance,
  opportunity allocation,
  recovery / re-engagement
}
```

These coordinates are not assumed independent or exhaustive.

The durable result is simply:

```text
MotivationDimension_D
!= MotivationDimension_E
```

without evidence connecting them.

---

# 2. Goal

HF4 uses `Goal` for a represented target condition that can organize selection,
planning or action.

A minimum form is:

```text
Goal(G,H,t)
= representation of an end-state, avoided state, maintained condition or
  criterion that can organize Human policy/action at time t
```

Examples:

```text
obtain food
avoid pain
finish a paper
maintain body temperature
keep a promise
preserve cash runway
become competent at a skill
not open an app during study
```

Goals can concern acquisition, avoidance, maintenance or transformation.

## 2.1 Goal is not outcome

```text
Goal
= target representation / criterion

Outcome
= realized consequence/state
```

Therefore:

```text
Goal != Outcome
```

A goal can remain active after failure, disappear after success, or be abandoned
without ever being realized.

## 2.2 Goal is not behavior

The same goal can be pursued through different means.
The same behavior can serve different goals.

```text
Goal → many possible Means
Behavior → many possible Goals
```

Therefore observed action does not uniquely identify the goal.

---

# 3. Goal is a family of states, not one yes/no property

HF4 separates:

```text
GoalContent
GoalActivation
GoalPriority
GoalCommitment
GoalMaintenance
GoalImplementationPolicy
GoalProgress
GoalAttainment
```

## 3.1 Goal content

What condition is represented?

## 3.2 Goal activation

Is the representation currently influencing processing?

## 3.3 Goal priority

How strongly does it compete for attention/action relative to alternatives?

## 3.4 Goal commitment

How strongly is the actor disposed to continue pursuing it across difficulty,
time or opportunity change?

## 3.5 Goal maintenance

Is the relevant goal/rule kept active when it is needed to control action?

## 3.6 Implementation policy

What cue/action relation is prepared to realize the goal?

## 3.7 Progress / attainment

How close is the world state to the target criterion, and was it eventually
realized?

The central anti-collapse is:

```text
GoalContent
!= GoalActivation
!= GoalPriority
!= GoalCommitment
!= GoalMaintenance
!= ImplementationPolicy
!= GoalAttainment
```

---

# 4. Knowing the goal is not maintaining the goal

Goal-neglect experiments are a high-information falsifier.

People can understand and later describe a task rule while failing to keep it
active strongly enough to guide behavior at the critical moment.

So:

```text
GoalKnowledge != OnlineGoalControl
```

and:

```text
RememberedInstruction != MaintainedTaskGoal
```

This matters for Human assessment. A failure to act consistently with a stated
goal can arise from:

```text
insufficient activation
maintenance failure
attention capture
competing goal
weak implementation
habit
cost change
capability/resource constraint
opportunity change
```

rather than from `not really wanting it`.

---

# 5. Goal intention versus implementation intention

HF4 separates:

```text
GoalIntention:
“I intend to achieve G.”

ImplementationPolicy:
“If cue/context X occurs, perform action Y.”
```

Implementation-intention studies show that making a cue-action contingency
explicit can improve prospective execution or weaken a habitual response advantage
without necessarily increasing the represented value of the final goal.

Therefore:

```text
GoalStrength != ImplementationQuality
```

and:

```text
Intention != Policy
```

A useful representation is:

```text
Goal G
+ TriggerCondition X
+ PreparedAction Y
→ ImplementationPolicy(X → Y | G)
```

Implementation can fail even with strong commitment, and implementation support
can improve behavior without changing the person's endorsed goal.

---

# 6. Preference

HF4 uses `Preference` as a comparative relation under a declared choice context.

```text
Prefer_H(A,B | context,t)
```

means that under the relevant procedure and state, `A` is selected/ranked over
`B`.

Preference is evidence about current choice organization.

It is not automatically:

```text
stable trait
moral value
welfare
true desire
long-term goal
```

## 6.1 Preference is context-indexed

Choice can change with:

```text
delay
framing
magnitude
uncertainty
current physiological state
social information
available alternatives
effort requirement
```

Therefore:

```text
ObservedPreference(t1,context1)
!= TimelessPreference
```

---

# 7. Value is an overloaded family

HF4 finds `Value` to be one of the most dangerous words in Human research.

At least five meanings must be separated.

## V1 — Hedonic value / liking

The pleasant or unpleasant impact of an obtained/experienced outcome.

```text
Liking(O,H,t)
```

## V2 — Incentive salience / wanting

The degree to which a cue/outcome acquires motivational attraction and pulls
approach/seeking.

```text
Wanting(CueOrOutcome,H,t)
```

## V3 — Learned state/action value

A computational estimate learned from outcomes and prediction errors:

```text
V(s)
Q(s,a)
```

These are model variables for expected future consequences under a learning
architecture.

## V4 — Current decision value

A context/state-dependent integration relevant to a current choice:

```text
DecisionValue(option | state, context, t)
```

It may depend on:

```text
expected outcome
magnitude
probability
uncertainty
delay
effort
opportunity cost
social consequence
current need/state
learned history
```

## V5 — Endorsed / personal / normative value

A person's evaluative commitment such as:

```text
honesty matters
family matters
scientific truth matters
autonomy matters
```

This is not identical to momentary reward value or RL action value.

HF4 therefore forbids naked technical claims such as:

```text
“the value increased”
```

without declaring the value type.

---

# 8. Personal value is not current decision value

A person can endorse:

```text
Health is important.
```

while choosing an immediately pleasurable unhealthy option.

This does not logically show that health is `not truly valued`.

The immediate decision can reflect:

```text
current reward
habit
state
availability
delay
friction
implementation failure
attention capture
```

while an endorsed long-horizon value remains stable.

Therefore:

```text
EndorsedValue != CurrentDecisionValue
```

and:

```text
CurrentChoice != EndorsedValue
```

This distinction is essential for Human-facing systems: inferring a person's
normative values from observed clicks/choices alone is not licensed.

---

# 9. Reward is not one thing either

HF4 decomposes `Reward` by causal role.

## R1 — Reward cue / incentive cue

A signal predicting or associated with a desirable/reinforcing outcome.

## R2 — Anticipated reward

A represented future outcome whose expectation can influence current action.

## R3 — Obtained reward outcome

The actually received outcome.

## R4 — Hedonic response to reward

The experienced pleasant impact of receipt.

## R5 — Reinforcer

An outcome/event whose contingency changes future behavior in a relevant learning
process.

## R6 — Reward prediction error

Difference-like learning signal relating expected and obtained reward under a
specified model.

These are related but not identical.

```text
RewardCue
!= RewardExpectation
!= RewardReceipt
!= HedonicImpact
!= Reinforcement
!= PredictionError
```

---

# 10. Wanting is not liking

Wanting/liking studies in food and alcohol provide direct Human falsifiers.

The same outcome can be:

```text
wanted more
without being liked more
```

or:

```text
liked less
without an equal drop in wanting
```

The dissociation is not perfect in every study or domain, but it is sufficient to
reject the identity:

```text
Wanting = Liking
```

HF4 therefore retains:

```text
Wanting != Liking != Learning
```

This also blocks:

```text
Pleasure = Motivation
```

as a general model.

---

# 11. Reward prediction error is not pleasure

Prediction error has a learning role:

```text
expected outcome
vs
obtained outcome
→ update
```

It can influence future learned value and choice.

That is distinct from:

```text
How pleasurable is the obtained outcome now?
```

Therefore:

```text
RewardPredictionError != HedonicImpact
```

and:

```text
LearningSignal != RewardExperience
```

This is why HF4 rejects slogans such as:

```text
Dopamine = pleasure
```

or:

```text
Dopamine = reward
```

without specifying mechanism and experiment.

---

# 12. Motivation as action allocation

HF4's positive replacement for scalar motivation is:

```text
Motivation
= family of processes that allocate action, time and effort among competing
  possibilities as a function of goals, current state, learned value, expected
  outcomes, costs, uncertainty and context
```

The word can remain useful if its dimension is declared.

## 12.1 Direction

Toward what outcome or away from what state is behavior allocated?

## 12.2 Initiation

How readily is action started when an opportunity appears?

## 12.3 Vigor

How intensely/rapidly is action performed?

## 12.4 Persistence

How long is action continued under delay, failure or cost?

## 12.5 Cost tolerance

How much effort, delay, uncertainty, pain or opportunity loss is accepted?

## 12.6 Re-engagement

After interruption/failure, how readily does pursuit restart?

These can dissociate.

For example:

```text
high wanting
+ low willingness to work
```

or:

```text
strong goal endorsement
+ poor initiation
```

are coherent Human states.

---

# 13. Effort needs its own decomposition

`Effort` is often used to mean five different things.

HF4 separates:

```text
ObjectiveDemand
PerceivedDemand
SubjectiveEffort
EffortCost
WillingnessToWork
ActualEffortExpenditure
```

and keeps `Performance` separate again.

## 13.1 Objective demand

Externally measurable physical/cognitive requirement.

Examples:

```text
force level
number of operations
working-memory load
vigilance duration
```

## 13.2 Perceived demand

The Human's estimate of what the task requires.

## 13.3 Subjective effort

Experienced exertion while performing or anticipating the task.

## 13.4 Effort cost

How strongly effort requirement reduces current option value under a particular
choice state.

## 13.5 Willingness to work

Choice tendency to accept effort for an outcome.

## 13.6 Actual expenditure

Observed exertion produced.

Thus:

```text
ObjectiveDemand
!= SubjectiveEffort
!= EffortCost
!= WillingnessToWork
!= EffortExpenditure
!= Performance
```

---

# 14. Low effort does not diagnose low motivation

Suppose a person exerts little effort.

Possible explanations include:

```text
low goal priority
low expected benefit
high effort cost
high opportunity cost
fatigue
pain
low capability
low efficacy belief
poor implementation
missing permission/resource
different strategy
automation making effort unnecessary
```

Therefore:

```text
LowObservedEffort
!= LowMotivation
```

without a model of alternatives and capability.

Similarly:

```text
HighEffort
!= HighEndorsedValue
```

because coercion, necessity or poor tools can force costly action.

---

# 15. Effort is often a cost — but not only a cost

Prospective effort commonly discounts reward:

```text
more required effort
→ lower current choice value
```

but obtained effort can also change later evaluation of the outcome, and effort
training can alter later effort preference under some conditions.

Therefore HF4 rejects:

```text
Effort = always negative utility term
```

The correct approach is role-specific:

```text
ProspectiveEffortCost
PostEffortOutcomeEvaluation
LearnedEffortValue
Identity/meaning of effort
```

can differ.

This explains why `effort` can be avoided in one stage and valued in another.

---

# 16. Delay and effort are different transformations

HF4 rejects a single generic `cost` variable when delay and effort matter.

A prospective option can be transformed by:

```text
delay
physical effort
cognitive effort
uncertainty
risk
social cost
opportunity cost
```

and these transformations can have different functional forms.

A minimum notation is:

```text
DecisionValue_t(option)
= F(
    expected outcomes,
    delay,
    uncertainty,
    effort profile,
    opportunity alternatives,
    current state,
    learned history,
    social/institutional context
  )
```

`F` is deliberately unspecified.

HF4 does not canonize exponential, hyperbolic or any single discount equation as
Human ontology.

---

# 17. Preference reversal is not evidence of irrational essence

Intertemporal choices can change as delays, magnitude, framing or uncertainty
change.

This supports:

```text
CurrentPreference
= context/time-dependent relation
```

not:

```text
Human has one hidden permanent ordering that every observed choice reveals
```

Dynamic inconsistency can be behaviorally important, but HF4 does not define one
side of a preference reversal as the person's `true self` by default.

A later self can face a different:

```text
state
proximity
uncertainty
cue salience
opportunity set
```

and therefore compute a different current decision value.

---

# 18. Affect

HF4 uses `Affect` as a broad family of valenced/activated experiential and
physiological states that can alter valuation, attention, learning and action.

It does not retain one affect primitive.

At minimum distinguish:

```text
Valence
Arousal / activation
specific emotion episode
mood-like sustained state
approach/avoidance tendency
```

These can interact without identity.

---

# 19. Affect is not valence

Affect cannot be represented only as:

```text
positive ↔ negative
```

because activation/arousal and specific appraisal/action tendencies matter.

Thus:

```text
Affect != Valence
```

and:

```text
SameValence != SameActionTendency
```

Two unpleasant states can produce approach, avoidance, freezing, aggression,
information seeking or persistence depending on context and appraisal.

---

# 20. Valence is not approach/avoidance

Approach–avoidance conflict paradigms show that the same option can simultaneously
contain:

```text
reward attraction
+
threat/aversive consequence
```

The Human need not occupy one point on a single positive/negative motivation axis.

Therefore:

```text
PositiveValence != Approach
NegativeValence != Avoidance
```

and:

```text
ApproachActivation
and
AvoidanceActivation
can coexist
```

producing conflict and inhibition.

---

# 21. Affect changes value and decision dynamics

Reward/punisher outcomes can alter both subsequent choices and reported affect.

This creates a recurrent loop:

```text
Outcome
→ affective update
→ altered valuation / uncertainty / action allocation
→ next choice
→ new outcome
```

So affect is neither:

```text
mere passive report after action
```

nor:

```text
the complete explanation of choice
```

It is one state variable in a coupled valuation/control loop.

---

# 22. Goal-directed action and habit-like control

HF4 needs the goal/habit distinction because current action need not be recomputed
from current outcome value on every trial.

A useful operational contrast is:

```text
GoalDirectedControl
= action remains sensitive to current represented outcome value and action-outcome
  relation

HabitLikeControl
= cue-triggered response persists with reduced sensitivity to current outcome value
```

This is a control-mode distinction, not an identity of two complete Human systems.

## 22.1 Measurement warning

Recent human habit research shows that apparent outcome-insensitive behavior can
sometimes reflect ineffective devaluation or other task failures.

Therefore:

```text
OutcomeInsensitiveResponse
!= ProvenHabit
```

without confirming that outcome value actually changed for that person.

---

# 23. Goal does not eliminate habit

A Human can simultaneously have:

```text
Goal: do not perform response R
Habit-like cue: strongly triggers R
```

Behavior then depends on competition, attention, control, implementation support
and context.

So:

```text
GoalExists
!= GoalControlsEveryAction
```

and:

```text
HabitLikeResponse
!= NoGoal
```

This matters for self-regulation: repeated unwanted behavior does not prove absence
of a competing goal.

---

# 24. Intrinsic and extrinsic motivation are not simply inside versus outside

HF4 uses the intrinsic/extrinsic literature as a pressure test, not as a complete
motivational ontology.

External incentives can:

```text
increase immediate effort or performance
change perceived competence
change perceived control
displace an activity's meaning
alter later free-choice engagement
```

depending on contingency and context.

Therefore:

```text
MoreReward
!= MonotonicallyMoreMotivation
```

and:

```text
ExternalIncentive
!= PurelyAdditiveValueBonus
```

in all Human contexts.

---

# 25. Choice is not autonomy

Providing multiple buttons or alternatives does not necessarily create meaningful
autonomy.

HF4 retains from control/motivation experiments:

```text
ChoiceCount
!= ExperiencedAutonomy
!= ActualControl
```

A choice can be illusory, constrained, coercive or irrelevant to important costs.

Actual control over meaningful task consequences can alter motivational effects in
ways that nominal choice does not.

This reconnects directly to HF1:

```text
ObjectiveControl != SenseOfAgency != Autonomy
```

---

# 26. Motivation quality and motivation quantity differ

Two people can show similar effort while differing in:

```text
coercion
fear
personal endorsement
interest
social obligation
reward seeking
identity commitment
```

HF4 therefore separates:

```text
MotivationalQuantity
≈ how much action allocation occurs

MotivationalOrganization / Quality
≈ why/how that allocation is regulated and what goal/value relations sustain it
```

HF4 does not canonize one scale for motivational quality, but the distinction
prevents:

```text
same output = same motivation
```

---

# 27. Self-regulation

HF4 defines self-regulation broadly as:

```text
SelfRegulation
= processes by which a Human maintains, monitors, revises or implements a target
  relation across time despite changing internal state, competing goals and
  environmental alternatives
```

It can include:

```text
goal selection
goal maintenance
progress monitoring
conflict detection
attention control
implementation policies
environment design
precommitment
habit redesign
reappraisal
seeking social/tool support
recovery after failure
```

Self-regulation is therefore not identical to inhibitory willpower.

---

# 28. Self-control is a narrower case

HF4 uses `SelfControl` for cases where a currently available action tendency or
reward conflicts with another active target/value relation and regulation is
required to alter the immediate action.

Examples:

```text
short-term reward vs long-term goal
habit response vs current outcome value
craving vs dieting goal
immediate distraction vs study commitment
```

Thus:

```text
SelfControl ⊂ SelfRegulation
```

as a working relation, not a permanent taxonomy.

Some self-regulation problems have no temptation conflict at all; they may involve
remembering, planning, sequencing or environment setup.

---

# 29. Self-control is not a substance

HF4 does not retain the classic `willpower tank` as a foundation fact.

Performance after prior exertion can depend on:

```text
motivation
expectations
opportunity costs
fatigue
anticipated future demands
strategy
current reward
```

and registered tests have not reduced the phenomenon to one universally accepted
resource mechanism.

Therefore:

```text
SelfControlFailure
!= ProvenResourceDepletion
```

without independent evidence of a resource and its dynamics.

---

# 30. Precommitment reveals that self-regulation can alter the future option set

A Human need not wait for temptation and then `fight harder`.

Precommitment can change the future choice architecture:

```text
CurrentSelf
→ remove/raise cost of future tempting option
→ FutureSelf faces easier control problem
```

This is genuine self-regulation even though it reduces later choice freedom.

Therefore:

```text
SelfRegulation
!= MaximumMomentaryChoiceSet
```

and:

```text
LessFutureOptionCount
can increase
LongHorizonGoalControl
```

when the restriction is voluntarily chosen and properly scoped.

---

# 31. Environment design is part of situated self-regulation

HF1 established that capability is relational and tools can extend Human action.
HF4 now applies the same idea to regulation.

A Human can regulate by modifying:

```text
notifications
physical layout
defaults
calendar
money access
social commitments
website blockers
AI reminders
```

These are not internal inhibitory strength.

Thus:

```text
SelfRegulatoryCapability
= relation(Human, goals, strategies, tools, environment, state, context)
```

and:

```text
InternalWillpower != TotalSelfRegulatoryCapability
```

---

# 32. Motivation depends on opportunity

A person can value an outcome and be willing to work yet fail to act because:

```text
option unavailable
permission absent
information missing
capability insufficient
cost unaffordable
risk too high
```

Thus:

```text
Motivation != Opportunity
```

and:

```text
NoAction
!= NoMotivation
```

This reconnects HF4 to HF0/HF1's Resource → Option → Capability distinctions.

---

# 33. Motivation depends on efficacy beliefs without becoming them

If a Human expects that effort cannot affect the outcome, investing effort may be
poor policy even when the outcome is strongly desired.

So HF4 distinguishes:

```text
OutcomeValue
ExpectedActionEfficacy
EffortCost
```

A schematic choice term is:

```text
ActionAttractiveness
≈ expected outcome value
× perceived action-outcome efficacy
− effort/delay/risk/opportunity costs
```

This is not a universal utility equation.

Its role is to show why:

```text
high outcome value
+ near-zero expected efficacy
→ low willingness to work
```

without implying low desire or value.

---

# 34. Motivation is state-dependent

Human reward and effort experiments repeatedly show current internal state changes
valuation.

Examples include:

```text
hunger / satiety
sickness
fatigue
sleep state
stress
```

These can change:

```text
wanting
liking
effort cost
risk sensitivity
priority
action vigor
```

in partially dissociable ways.

Therefore:

```text
MotivationProfile_t
= function of current organismic state
```

not merely a stable personality property.

---

# 35. Hunger and satiety are direct falsifiers of stable reward value

The same food is not assigned the same current value across deprivation and
satiety.

This provides a clean Human example:

```text
SameOutcome
+ DifferentInternalState
→ DifferentWanting / Liking / Work / Intake
```

Therefore:

```text
RewardValue != OutcomeIntrinsicProperty
```

It is a relation among outcome, organism state, history and context.

---

# 36. Sickness separates effort from reward sensitivity

Experimental inflammatory sickness can change willingness to accept effort costs
without an equivalent change in reward sensitivity under the task.

This is particularly damaging to scalar motivation models.

If `motivation` were one number, the prediction would tend to be:

```text
reward response ↓
effort willingness ↓
```

as one coupled decline.

Instead the dimensions can move differently.

Thus:

```text
EffortSensitivity
!= RewardSensitivity
```

---

# 37. Fatigue is not identical to effort cost

Fatigue is an internal state/experience associated with prior exertion and changing
willingness/performance.

It can alter prospective effort cost, but the terms must remain separate:

```text
FatigueState
→ may change EffortCost
```

not:

```text
Fatigue = EffortCost
```

This becomes one of the principal reasons HF4 cannot finish the bodily-state
problem itself.

---

# 38. Effort can rise near a deadline despite fatigue

Deadline studies produce a useful falsifier for simple depletion accounts.

People can show decreasing effort over a long task and then increase effort as a
deadline approaches.

One plausible account is opportunity-cost change: competing activities become
less attractive relative to completing the focal task near the deadline.

Regardless of final theory, the empirical structure is enough to retain:

```text
FatigueState != FixedRemainingEffortResource
```

and:

```text
EffortAllocation
depends on alternatives and horizon
```

not just cumulative exertion.

---

# 39. Agency remains separate from motivation and success

HF1/HF3 already established:

```text
Agency != SenseOfAgency != Autonomy
```

HF4 adds:

```text
Motivation != Agency
```

A highly motivated Human may lack control, resources or opportunity.
A Human may have agency but choose not to act because current value is low.

Likewise:

```text
GoalAttainment != Agency
```

because success may result from luck, assistance or external automation.

HF4 therefore does not infer agency from outcome success.

---

# 40. Motivation failure is not one failure mode

The phrase:

```text
motivation failure
```

should be treated as a placeholder requiring decomposition.

Possible failure points include:

```text
Goal not represented
Goal not activated
Goal not maintained
Goal low priority
Outcome value low
Wanting weak
Expected efficacy low
Effort cost high
Delay too long
Opportunity cost high
Competing goal stronger
Habit dominates
Implementation policy missing
Capability/resource absent
Fatigue/stress/sickness state
Monitoring failure
Recovery failure
```

The practical implication is strong:

> **Interventions should target the failed relation, not merely try to “increase
> motivation.”**

---

# 41. Reward can alter attention without becoming the goal

HF3 showed reward/history-driven attentional capture.

HF4 clarifies:

```text
Cue has acquired incentive/selection value
```

does not imply:

```text
Human endorses cue pursuit as current goal
```

Thus:

```text
RewardCapture != GoalCommitment
```

This matters in addiction-like, habit-like and persuasive-interface contexts where
attention and wanting can become misaligned with endorsed values.

---

# 42. Goal conflict is normal, not model failure

Humans can hold multiple active goals:

```text
work
rest
social contact
health
money
curiosity
safety
```

A behavior policy emerges from competition/cooperation among them.

Therefore HF4 rejects:

```text
OneHuman = OneCurrentGoal
```

A useful representation is:

```text
ActiveGoalSet_t = {G1, G2, ... Gn}
```

with relations:

```text
conflict
support
shared means
mutual exclusion
hierarchy
```

Goal-system research shows even the mapping from a means to multiple goals can
change perceived instrumentality and choice.

---

# 43. Means are not goals

The same means can serve several goals:

```text
exercise
→ health
→ social connection
→ appearance
→ competition
```

and one goal can have several means.

So:

```text
Goal != Means
```

and:

```text
MeansValue
depends on currently active GoalSet
```

This helps explain why a behavior can lose motivation when its meaning or goal
link changes even if the physical action remains identical.

---

# 44. Value is learned and reconstructed

Current decision value is not simply retrieved from a permanent internal table.
It can be shaped by:

```text
prediction error
new social information
revaluation
state change
context
framing
memory retrieval
counterfactual comparison
```

Thus:

```text
Value_t
is a stateful estimate / relation
```

not a fixed object property.

This also means Human systems should preserve the conditions under which a value
estimate was elicited.

---

# 45. Reward learning does not settle normative value

An action can be reinforced repeatedly while conflicting with a person's endorsed
values or long-term welfare.

Therefore:

```text
LearnedActionValue
!= EndorsedValue
!= Welfare
```

HF4 inherits HF0's normative firewall:

```text
ObservedPreference != Welfare
CurrentAdaptation != Desirability
Prediction != Authority
```

Reinforcement-learning success cannot determine what a Human ought to value.

---

# 46. Cross-context falsifier matrix

| Case | Naive collapse attacked | HF4 surviving distinction |
|---|---|---|
| alcohol priming raises wanting without liking | wanting = pleasure | wanting != liking |
| adulteration lowers liking without equal wanting change | liking = action desire | hedonic impact != incentive allocation |
| reward prediction error changes learning | dopamine/reward = pleasure | learning signal != hedonic receipt |
| hunger vs satiety | outcome has fixed reward value | current reward value is state-dependent |
| sickness raises effort sensitivity | motivation is one scalar | effort sensitivity != reward sensitivity |
| sleep deprivation raises wanting but lowers work | wanting = effort output | incentive desire != willingness/expenditure |
| effort discounting | desired outcome guarantees action | value can be outweighed by prospective effort cost |
| effort enhances later reward evaluation | effort is only negative cost | prospective cost != post-effort valuation |
| delay discounting | preference is timeless | preference/decision value depends on horizon/context |
| goal neglect | knowing goal = executing goal | goal knowledge != online maintenance/control |
| implementation intention | stronger action = stronger goal | implementation quality != goal value |
| habit-like slip | current outcome value always controls action | cue-driven control can compete with goal-directed control |
| ineffective devaluation falsely appears habitual | outcome-insensitive response = habit | manipulation validity must be demonstrated |
| approach–avoidance conflict | positive = approach, negative = avoid | reward and threat can be simultaneously active |
| contingent reward crowds out later free-choice | more reward = more motivation | incentive effects depend on control/meaning/contingency |
| actual versus illusory control | choice count = autonomy | meaningful control != nominal choice |
| precommitment | self-control = stronger momentary inhibition | regulation can restructure future options |
| deadline effort increase | fatigue = depleted fixed resource | effort allocation depends on horizon/opportunity cost |
| no action despite strong desire | action = motivation | opportunity/capability/efficacy can block behavior |
| high effort under coercion | effort = endorsement | effort output != personal value/autonomy |

---

# 47. Competing HF4 models

HF4 pressure-tests several broad model families.

## M1 — scalar drive model

```text
Motivation = one internal drive level
```

### Strength

Simple and sometimes useful for coarse descriptions of vigor.

### Failure

Wanting, effort willingness, reward sensitivity, persistence and liking can
dissociate.

**Disposition:** reject as general foundation ontology.

## M2 — reward maximizer

```text
Human chooses action with greatest reward
```

### Strength

Useful skeleton for controlled decision tasks.

### Failure

Requires explicit treatment of effort, delay, uncertainty, social/normative goals,
habits, state dependence and changing opportunity sets. `Reward` itself is
multirole.

**Disposition:** retain only as scoped decision model.

## M3 — expected utility / stable preference model

```text
choices reveal stable preference ordering
```

### Strength

Powerful normative/descriptive formalism in constrained settings.

### Failure

Preference reversals, state dependence, framing, habits and implementation gaps
show that observed choice is not a transparent readout of timeless personal value.

**Disposition:** scoped model, not Human ontology.

## M4 — goal-strength model

```text
stronger goal → more goal-consistent behaviour
```

### Strength

Captures one important factor.

### Failure

Goal neglect, implementation failure, habit conflict, opportunity/capability and
cost changes break the direct mapping.

**Disposition:** goal strength is one variable, not complete explanation.

## M5 — self-control resource model

```text
self-control uses finite resource → resource depletion → failure
```

### Strength

Historically productive and generates testable predictions.

### Failure

Motivation, expectations, opportunity cost, deadlines, task meaning and strategy
can change performance; no one resource mechanism is settled as foundation fact.

**Disposition:** retain as historical rival, reject as canonical Human primitive.

## M6 — goal-directed versus habit dual-control model

### Strength

Outcome sensitivity and cue-triggered behavior capture important dissociations.

### Failure

Human tasks show measurement difficulties, graded mixtures and cognitive-control
bottlenecks; not every behavior belongs cleanly to one box.

**Disposition:** retain typed control modes, not complete action ontology.

## M7 — motivational-quality / self-determination models

### Strength

Highlight autonomy, competence, meaning and source of regulation rather than only
reward magnitude.

### Failure

Do not by themselves replace effort, reward learning, state physiology or habit
mechanisms.

**Disposition:** retain as important projection.

## M8 — value-based / allostatic action allocation

### Strength

Integrates costs, benefits, internal state and predicted future needs.

### Failure

The exact bodily-state regulation, interoception and need architecture remains
underspecified and becomes HF5.

**Disposition:** strong rival scaffold, not final ontology.

---

# 48. Minimum HF4 grammar

HF4's minimum retained architecture is:

```text
Human State + World + History
        ↓
Candidate outcomes / threats / opportunities
        ↓
Reward prediction / affect / wanting / liking / learned value
        ↓
Contextual DecisionValue
   ↑ delay / risk / effort / opportunity / state
        ↓
ActiveGoalSet
        ↓
Goal priority + commitment + implementation policies
        ↓
MotivationProfile
   ├─ direction
   ├─ initiation
   ├─ vigor
   ├─ persistence
   ├─ cost tolerance
   └─ re-engagement
        ↓
Goal-directed / habit-like / automatic / delegated control routes
        ↓
Action
        ↓
Outcome
        ↓
Hedonic response + reinforcement + prediction error + affect
        ↓
Learning + state change + goal update
        ↺
```

Self-regulation can act at several nodes:

```text
select goal
change attention
create if-then policy
change environment
precommit
seek support/tool
monitor progress
revise strategy
recover after failure
```

This is not a single motivational pipeline.

---

# 49. HF4 anti-laws

## Goal

1. `Goal != Outcome`.
2. `Goal != Behavior`.
3. `GoalContent != GoalActivation`.
4. `GoalActivation != GoalPriority`.
5. `GoalPriority != GoalCommitment`.
6. `GoalKnowledge != GoalMaintenance`.
7. `GoalIntention != ImplementationPolicy`.
8. `GoalCommitment != GoalAttainment`.
9. `GoalExists != GoalControlsEveryAction`.
10. `Goal != Means`.

## Preference / value

11. `ObservedChoice != StablePreference`.
12. `Preference != EndorsedValue`.
13. `CurrentDecisionValue != EndorsedValue`.
14. `LearnedActionValue != Welfare`.
15. `Value` without type is underspecified.

## Reward

16. `Reward != Pleasure`.
17. `Reward != Value`.
18. `Wanting != Liking`.
19. `Liking != Learning`.
20. `PredictionError != RewardReceipt`.
21. `PredictionError != HedonicImpact`.
22. `Reinforcement != Endorsement`.
23. `Dopamine != pleasure/reward` without scoped mechanism.

## Motivation

24. `Motivation != one scalar`.
25. `Wanting != MotivationProfile`.
26. `LowAction != LowMotivation`.
27. `LowEffort != LowMotivation`.
28. `HighEffort != HighEndorsedValue`.
29. `Motivation != Opportunity`.
30. `Motivation != Capability`.
31. `Motivation != Agency`.

## Effort

32. `ObjectiveDemand != SubjectiveEffort`.
33. `SubjectiveEffort != EffortCost`.
34. `EffortCost != WillingnessToWork`.
35. `WillingnessToWork != ActualEffortExpenditure`.
36. `EffortExpenditure != Performance`.
37. `Effort != Motivation`.
38. `Effort != always negative value`.
39. `Fatigue != EffortCost`.
40. `Fatigue != fixed remaining resource`.

## Affect

41. `Affect != Valence`.
42. `Valence != Approach/Avoidance`.
43. `PositiveValence != Approach`.
44. `NegativeValence != Avoidance`.
45. `Affect != Motivation`.

## Habit / control

46. `GoalDirected != HabitLike`.
47. `OutcomeInsensitiveResponse != ProvenHabit`.
48. `HabitLikeResponse != NoGoal`.
49. `RewardCapture != GoalCommitment`.

## Self-regulation

50. `SelfRegulation != SelfControl`.
51. `SelfControlFailure != ProvenResourceDepletion`.
52. `InternalWillpower != TotalSelfRegulatoryCapability`.
53. `SelfRegulation != MaximumMomentaryChoiceSet`.
54. `SelfRegulation != GoalAttainment`.
55. `NominalChoice != Autonomy`.
56. `ChoiceCount != ActualControl`.
57. `MoreExternalReward != MonotonicallyMoreMotivation`.

## Normative / authority

58. `ObservedPreference != Welfare`.
59. `RewardLearning != NormativeValue`.
60. `BehavioralPrediction != Authority over goals/values`.

---

# 50. Human × AI implication

HF4 is directly relevant to Human-facing Agents.

An Agent should not infer:

```text
user clicked X
→ user values X
```

or:

```text
user did not finish task
→ user lacked motivation
```

or:

```text
user accepted reward
→ reward increased autonomous motivation
```

A safer representation separates:

```text
StatedGoal
InferredCurrentPreference
EndorsedValue
ObservedChoice
EffortDemand
ObservedEffort
Opportunity/Capability
CurrentState
Confidence/Uncertainty
```

and preserves disagreement among them.

---

# 51. AI assistance can modify motivation without modifying values

An Agent can change:

```text
friction
implementation cues
information availability
perceived efficacy
option set
feedback timing
```

thereby changing behavior even when the Human's endorsed values are unchanged.

This means successful Agent intervention does not prove:

```text
Human value changed
```

It may simply have changed:

```text
Resource → Option → Capability → Implementation
```

which reconnects HF4 to the broader Ordivon resource model.

---

# 52. Delegated regulation

Humans can externalize parts of self-regulation:

```text
calendar reminder
blocking tool
accountability partner
AI planner
financial lock
precommitment contract
```

HF1 already established that tool participation in capability does not make the
tool the person.

HF4 adds:

```text
ExternalRegulatorySupport
can increase
SituatedSelfRegulatoryCapability
```

without implying:

```text
InternalSelfControlSkill increased
```

This is important when evaluating learning or deskilling under Agent assistance.

---

# 53. Reconnection to HF3

HF3 modeled:

```text
Priority(x,t)
= f(goals, salience, value, history, state, action)
```

HF4 now decomposes three of those terms.

```text
Goal
→ content / activation / priority / commitment / maintenance / policy

Value
→ liking / wanting / learned value / decision value / endorsed value

State
→ remains unresolved bodily-regulation input
```

Therefore the improved priority relation is:

```text
Priority(x,t)
= f(
    ActiveGoalSet,
    incentive salience,
    expected outcomes,
    current DecisionValue,
    affect,
    reward/selection history,
    current organismic state,
    action demands
  )
```

Again this is a structural relation, not a fitted universal equation.

---

# 54. Reconnection to Game Foundations

Game R18 already separated:

```text
Need
Want
Desire
Goal
Preference
Utility
Value
```

HF4 strengthens the Human side by showing why these distinctions matter
empirically.

A player's selected action may reflect:

```text
current incentive
learned habit
implementation policy
state-dependent reward value
social goal
long-horizon commitment
```

rather than one static utility number.

Thus Game utility models can remain useful local abstractions without becoming
Human ontology.

---

# 55. Reconnection to Finance / Resource foundations

HF4 also clarifies resource allocation.

A Human does not allocate resources solely by abstract value.

Actual allocation depends on:

```text
current goals
expected return
risk/uncertainty
delay
effort
liquidity/opportunity
state
implementation friction
```

Therefore:

```text
Value != Allocation
```

without the intermediate choice/control machinery.

This mirrors:

```text
Resource != Option != Capability != Effect
```

from the broader Ordivon world model.

---

# 56. What HF4 does not establish

HF4 does not establish:

- one universal motivational equation;
- that all goals are conscious;
- that all action is goal-directed;
- that all habits are unconscious;
- that outcome-insensitive behaviour is always habit;
- that stable preferences never exist;
- that delay discounting is irrational;
- one correct temporal-discount function;
- that dopamine has no role in pleasure under every condition;
- that wanting/liking are perfectly separable in every Human domain;
- that effort is always aversive;
- that effort always increases later value;
- that rewards always undermine intrinsic motivation;
- that rewards always increase motivation;
- one universal taxonomy of intrinsic/extrinsic motivation;
- that autonomy is identical to choice;
- that self-control never has biological resource constraints;
- that ego depletion is wholly motivational;
- that fatigue is purely an opportunity-cost signal;
- that allostasis is the final theory of bodily regulation;
- that an Agent can infer a person's true values from behaviour;
- that normative values are reducible to learned reward value.

---

# 57. The boundary HF4 cannot finish

HF4 repeatedly found that the same external outcome or goal receives different
current motivational weight depending on:

```text
hunger / satiety
fatigue
sleep state
sickness
stress
pain
arousal
bodily need
```

These states alter:

```text
wanting
liking
reward responsiveness
effort cost
priority
persistence
self-regulation
```

but HF4 has no adequate foundation model for the body's regulation itself.

The unresolved terms now are:

```text
Need
Homeostasis
Allostasis
Interoception
Satiety
Arousal
Stress
Fatigue
Recovery
```

This is not merely `motivation again`.

It is the problem of how a living Human estimates, predicts and regulates its own
internal viability/state across time.

---

# 58. Exact next foundation

HF4 therefore selects:

# HF5 — Need, Homeostasis, Allostasis, Interoception, Satiety, Stress, Fatigue and Recovery

HF5 should ask:

1. What is a biological/psychological need, and how does it differ from desire,
   wanting, deficit and goal?
2. Is homeostasis fixed-point regulation or a family of feedback processes?
3. What does allostasis add through anticipatory/predictive regulation?
4. What is interoception: sensing internal state, inference about internal state,
   or both under different models?
5. How do hunger, thirst, pain, temperature, sleep pressure and sickness alter
   value without becoming identical to reward?
6. What is satiety relative to liking, wanting and need reduction?
7. What is stress relative to threat, arousal, load and adaptive mobilization?
8. What is fatigue: experienced state, performance decrement, effort-cost shift,
   protective regulation or several constructs?
9. What is recovery and how does it differ from rest or mere time passage?
10. How do physiological and cognitive resource constraints interact without
    inventing one universal `energy` account?
11. Which internal-state signals are first-person, physiological or inferred?
12. What next boundary is forced after bodily regulation is decomposed?

HF5 should not predefine HF6.

---

# 59. HF4 synthesis

HF4 began from:

```text
Why does one goal/action win?
```

The answer is not:

```text
because motivation was higher
```

The smallest model that survives cross-paradigm falsification is:

```text
Goals
→ represented targets with activation, priority, commitment, maintenance and
  implementation states

Value
→ qualifier-required family: liking, wanting, learned value, decision value,
  endorsed/normative value

Reward
→ qualifier-required cue/expectation/outcome/reinforcer/learning-signal roles

Affect
→ multidimensional state influencing valuation and action, not equal to valence
  or approach/avoidance

Effort
→ objective demand, subjective exertion, prospective cost, willingness and actual
  expenditure are distinct

Motivation
→ multidimensional allocation of direction, initiation, vigor, persistence,
  cost tolerance and re-engagement

SelfRegulation
→ temporal regulation of goal pursuit through monitoring, policies, environment,
  precommitment, tools and recovery
```

The deepest compression is:

```text
Human action is not read directly from Value.

Current action emerges from a recurrent relation among:
Goal × State × LearnedHistory × ExpectedOutcome × Cost × Opportunity ×
Implementation × Habit × Control.
```

And the strongest residual is now the **organismic state** term itself.

HF4 therefore closes by moving Human Foundations from cognition/action allocation
back into the living-body regulation problem in HF5.
