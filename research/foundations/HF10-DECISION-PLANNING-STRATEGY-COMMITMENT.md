---
schema_version: 1
id: human.foundations.hf10
title: HF10 — Decision, Choice, Planning, Strategy, Exploration, Exploitation, Stopping and Commitment
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
summary: HF10 reconstructs the bridge from judgment to temporally organized action policy. It separates option generation, evaluation, decision, choice, commitment and execution; observed choice from stable preference; risk from ambiguity and description from experience; instrumental, epistemic and affective information value; directed/random exploration and exploitation; search from stopping; satisficing from irrationality; sunk resources from remaining/switching costs; precommitment from willpower and irreversibility; plan, policy, strategy and tactic; model-based depth-limited and hierarchical planning; and AI option generation, recommendation and delegation from Human preference, authority and responsibility. The strongest residual is realized action: initiation, sensorimotor control, affordance, coordination, online correction, skill and tool-mediated execution.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
  - HF10
related:
  - human.foundations.hf9
  - human.foundations.hf10.sources
  - human.foundations.hf10.continuation
---
# HF10 — Decision, Choice, Planning, Strategy, Exploration, Exploitation, Stopping and Commitment

## 0. Status and question

HF9 ended with:

```text
SearchPolicy != StoppingRule
InferenceComplete != ActionSelected
ProvisionalJudgment != Commitment
```

HF10 therefore asks:

> **How does a Human move from candidate options and provisional judgments to a
> selected, temporally organized and revisable action policy?**

The inherited collapses are:

```text
Decision = judgment
Choice = preference
Choice = action
More options = better
More information = better
Exploration = randomness
Stopping = failure
Persistence = rational commitment
Sunk-cost persistence = one bias
Precommitment = willpower
Planning = reasoning
Plan = strategy = policy
Model-based = always better
AI recommendation/delegation = Human decision/authority transfer
```

None survives cross-context falsification.

---

# 1. Decision is not one event

HF10 uses `DecisionEpisode_D` for a bounded process that may include:

```text
option generation
option representation
evaluation
information search
comparison
selection
commitment
execution authorization
```

Not every decision includes all stages explicitly.

---

# 2. Judgment is not decision

HF9 judgment can estimate:

```text
A is 70% likely to succeed
B is more causally effective
C has strongest evidence
```

without selecting any option.

Thus:

```text
Judgment != Decision
```

---

# 3. Decision is not choice

A `decision` can refer to the deliberative/control process.

A `choice` is the selected option/selection output under a declared option set.

Therefore:

```text
DecisionProcess != ChoiceOutcome
```

---

# 4. Choice is not action

A Human can choose:

```text
“I will call the doctor.”
```

and fail to execute the call.

Thus:

```text
Choice != Action
```

---

# 5. Choice is not commitment

A selection can be provisional or easily reversible.

Commitment changes future policy/options/resources.

Therefore:

```text
Choice != Commitment
```

---

# 6. Commitment is not execution

A Human can commit resources or publicly commit while execution later fails.

Thus:

```text
Commitment != Execution
```

This distinction eventually exposes HF11.

---

# 7. Option set comes before selection

Most laboratory choice tasks provide:

```text
{A,B,C}
```

externally.

Real decisions often require first determining which actions exist.

Therefore:

```text
OptionGeneration
```

is a first-class decision process.

---

# 8. Option generation is not evaluation

Creating candidate A does not evaluate whether A is good.

Thus:

```text
OptionGeneration != OptionEvaluation
```

---

# 9. Option generation is not memory retrieval only

Poorly structured decision tasks show ideation contributes to valid option
generation beyond episodic/semantic retrieval.

Thus:

```text
OptionGeneration != MemoryRetrievalOnly
```

---

# 10. Generated option set can be incomplete

A Human can optimize perfectly among options they generated and still make a poor
real-world decision because the best option was absent.

Thus:

```text
BestChoiceWithinSet
!= BestAvailableActionInReality
```

---

# 11. More generated options is not monotonically better

Generating more options can increase:

```text
maximum option quality
```

while decreasing:

```text
mean option quality
```

or increasing evaluation burden.

Therefore:

```text
MoreGeneratedOptions != MonotonicDecisionQuality
```

---

# 12. First generated option is not always best

Take-The-First can work under some expertise/task regimes.

Other tasks show later options differ in quality/diversity.

Thus:

```text
FirstOption != BestOption by definition
```

---

# 13. Option quantity and option diversity are separate

Ten near-duplicates are not equivalent to ten structurally distinct possibilities.

Use:

```text
OptionCount
OptionDiversity
OptionCoverage
OptionQualityDistribution
```

separately.

---

# 14. Choice set is itself an intervention

Adding/removing/reordering options can alter:

```text
comparison
attention
reference points
search cost
```

Therefore:

```text
OptionSet != NeutralContainer
```

---

# 15. More choice is not always better

Classic choice-overload experiments show larger sets can reduce uptake/satisfaction
under some tasks.

Thus:

```text
MoreOptions != AlwaysBetter
```

---

# 16. More choice is not always worse

Modern reviews show choice overload depends on:

```text
task difficulty
option complexity
chooser knowledge
goal clarity
preference strength
```

Thus:

```text
MoreOptions != AlwaysWorse
```

---

# 17. Choice overload is relation-specific

A more useful object is:

```text
ChoiceLoad
= Relation(OptionSet, ComparisonStructure, Goal, HumanResources, Time, Tools)
```

rather than one option-count threshold.

---

# 18. Choice is not stable preference readout

Tversky/Kahneman framing and later work show formally equivalent descriptions can
reverse choice.

Thus:

```text
ObservedChoice != StablePreferenceReadout
```

HF4 preference remains context/time indexed.

---

# 19. Frame is part of the decision representation

A frame changes which:

```text
reference point
outcome valence
gist
reasons
```

are salient/represented.

Therefore:

```text
Frame
→ OptionRepresentation
→ Choice
```

---

# 20. Frame effect does not prove one mechanism

Reference-point models, valence/gist, pragmatic/reason-based and affective accounts
can explain different variants.

Thus:

```text
FrameEffect != UniqueProspectTheoryMechanismProof
```

---

# 21. Framing does not automatically mean irrationality

If frames reveal different legitimate reasons/aspects, changed choice need not be
mechanistically irrational.

Thus:

```text
DescriptionInvarianceFailure
!= UniqueIrrationalityDiagnosis
```

HF9 rationality firewall remains.

---

# 22. Preference can reverse over time

HF4 already established context/time-indexed preference.

HF10 adds that future proximity, new information, state and current option
architecture can change selection.

Thus:

```text
Choice_t1(A>B) != GuaranteedChoice_t2(A>B)
```

---

# 23. Preference reversal does not identify true preference

Neither earlier nor later choice is automatically the authentic/true self.

Thus:

```text
TemporalPreferenceConflict
!= TrueSelfIdentification
```

---

# 24. Decision value is not object intrinsic value

HF4 retained contextual DecisionValue.

HF10 makes the option relation explicit:

```text
DecisionValue(option | option set, state, frame, horizon, information, context)
```

---

# 25. Risk

HF10 uses:

```text
Risk_D
```

when relevant outcome distributions/probabilities are sufficiently specified or
estimable for the task.

---

# 26. Ambiguity

HF10 uses:

```text
Ambiguity_D
```

when important probabilities/models are missing, underspecified or uncertain.

Thus:

```text
Risk != Ambiguity
```

---

# 27. Uncertainty is broader than risk and ambiguity

Potential sources include:

```text
outcome stochasticity
parameter uncertainty
model uncertainty
state uncertainty
unknown options
unknown unknowns
```

Therefore:

```text
Uncertainty != Risk
Uncertainty != Ambiguity
```

without qualifier.

---

# 28. Ambiguity aversion is not universal law

Humans often avoid unknown probabilities, but need/state/context can change the
pattern.

Thus:

```text
Ambiguity != AlwaysAvoided
```

---

# 29. Risk preference is not one stable trait

Risk choice changes with:

```text
frame
need
experience/description
regret
state
domain
```

Thus:

```text
RiskPreference_D,t != GlobalRiskTrait by definition
```

---

# 30. Description is not experience

A distribution described symbolically and the same distribution sampled through
experience can produce different choice patterns.

Thus:

```text
DescriptionChoice != ExperienceChoice
```

---

# 31. Acquisition history is part of decision state

Experience-based choice depends on:

```text
which outcomes happened to be sampled
memory
extreme outcomes
sampling stopping
```

Therefore:

```text
ObjectiveDistribution
!= ExperiencedSampleHistory
```

---

# 32. Mental sampling can be biased

Recent generation experiments show Humans can over-generate rare possibilities,
under-generate common ones and avoid immediate repetition.

Thus:

```text
GeneratedOutcomeSet != ObjectiveProbabilityDistribution
```

---

# 33. Sampling policy changes choice

If Human reasoning samples only a subset of possible outcomes, selection depends on
that sampled subset.

Thus:

```text
Choice
= Function(OptionRepresentation, SampledPossibilities, Evaluation,...)
```

not full distribution by default.

---

# 34. Regret

HF10 distinguishes:

```text
AnticipatedRegret
ExperiencedRegret
RegretComparisonInformation
```

---

# 35. Regret is counterfactual

Experienced regret typically depends on comparing actual outcome against an
unchosen alternative.

Thus:

```text
Regret
requires some counterfactual comparison structure
```

but is not identical to HF9 counterfactual reasoning itself.

---

# 36. Regret is not risk aversion

Regret can shift risky behavior differently by risk level/task.

Thus:

```text
Regret != RiskAversion
```

---

# 37. Anticipated regret is not experienced regret

A predicted future emotional consequence can alter present choice without the
emotion having occurred yet.

Thus:

```text
AnticipatedRegret != ExperiencedRegret
```

---

# 38. Regret can be decision input and outcome

```text
AnticipatedRegret_t
→ Choice_t
→ Outcome
→ ExperiencedRegret_(t+1)
→ FutureChoice
```

This is a recurrent loop.

---

# 39. Information is an option

Before acting, Human often has a meta-option:

```text
AcquireMoreInformation
```

Information search therefore belongs inside decision architecture.

---

# 40. Instrumental information value

Information has instrumental value when it can change a later action and improve
expected outcome.

Use:

```text
InstrumentalVoI
```

as one dimension.

---

# 41. Information value is not instrumental only

Humans seek outcome information even when no downstream action can use it.

Thus:

```text
InformationValue != InstrumentalVoIOnly
```

---

# 42. Epistemic/uncertainty value

Resolving uncertainty can itself be valued.

Use:

```text
EpistemicInformationValue
```

without claiming one curiosity mechanism.

---

# 43. Affective information value

Information can be attractive/aversive because of expected emotion.

Thus:

```text
AffectiveInformationValue
```

is distinct from instrumental benefit.

---

# 44. Information can have negative subjective value

Humans can deliberately avoid available health/self-relevant information.

Therefore:

```text
AvailableInformation != SoughtInformation
```

---

# 45. Information avoidance is not ignorance by definition

Avoidance can serve self-protection or affect regulation.

Thus:

```text
InformationAvoidance != IrrationalIgnorance by definition
```

The normative evaluation depends on objectives and downstream consequences.

---

# 46. More information is not always preferred

Even when information is free physically, psychological cost can matter.

Thus:

```text
MoreInformation != AlwaysPreferred
```

---

# 47. More information is not always normatively valuable

If information cannot alter action, arrives too late, distracts, costs too much, or
creates downstream harm, instrumental value can be zero/negative.

Thus:

```text
InformationQuantity != DecisionValue
```

---

# 48. Search has cost

Search consumes:

```text
time
attention
money
opportunity
latency
```

so value-of-information must be net of acquisition costs.

---

# 49. Search can change the world

Waiting for information can alter opportunities.

Thus:

```text
InformationSearch != PassiveFreeDelay
```

---

# 50. Search can alter the Human

Search itself can change:

```text
confidence
attention
framing
memory
fatigue
```

so information acquisition is an intervention on the decision-maker too.

---

# 51. Confidence is not stopping rule

Low/high confidence influences search but current experiments show the relation is
context-sensitive.

Thus:

```text
Confidence != StoppingRule
```

---

# 52. Metacognitive sensitivity can improve search

Accurate uncertainty monitoring can allocate search better.

But:

```text
MetacognitiveSensitivity != SearchOptimality
```

without cost/objective information.

---

# 53. Search policy

Working definition:

```text
SearchPolicy
= rule mapping current information/uncertainty/state to where/how to acquire more
  information
```

---

# 54. Stopping rule

Working definition:

```text
StoppingRule
= rule determining when to terminate search/deliberation and proceed with a
  provisional decision/commitment
```

Thus:

```text
SearchPolicy != StoppingRule
```

---

# 55. Stopping is a decision

At every search step:

```text
continue sampling
vs
stop and choose
```

is itself an option comparison.

---

# 56. Stopping is not failure

Stopping can be rational under finite costs/horizon.

Thus:

```text
Stopping != Failure
```

---

# 57. Never stopping is not maximal rationality

Infinite information gathering prevents action.

Thus:

```text
InfiniteSearch != PerfectDecisionMaking
```

---

# 58. Premature stopping is also possible

Stopping before decisive evidence can reduce decision quality.

Thus:

```text
FastStopping != EfficientByDefinition
```

---

# 59. Satisficing

HF10 uses:

```text
Satisficing
= stop/select when an option or evidence state passes a task-relative aspiration or
  adequacy threshold
```

---

# 60. Satisficing is not irrationality

Under bounded resources, optimizing search itself may cost more than the gain from
finding a slightly better option.

Thus:

```text
Satisficing != IrrationalityByDefinition
```

---

# 61. Aspiration threshold is state/context dependent

It can depend on:

```text
stakes
available time
option distribution
failure cost
current resources
```

Thus:

```text
SatisficingThreshold_D,t
```

should be qualified.

---

# 62. Exploration

HF10 uses:

```text
Exploration
= selecting actions/information partly to improve knowledge about options,
  environment or future policy rather than solely maximizing current estimated
  payoff
```

---

# 63. Exploitation

```text
Exploitation
= selecting currently high-estimated-value options primarily for present reward or
  goal attainment
```

---

# 64. Exploration is not random choice

Bandit experiments distinguish:

```text
DirectedExploration
RandomExploration
```

Thus:

```text
Exploration != RandomChoice
```

---

# 65. Directed exploration

Unknown options can receive an information bonus when horizon allows future use of
what is learned.

Thus:

```text
DirectedExploration
```

is explicitly information-seeking.

---

# 66. Random exploration

Increasing decision noise/randomness can produce exploration without explicit
information bonus.

Thus:

```text
RandomExploration != DirectedExploration
```

---

# 67. Exploitation is not optimality

The currently believed best option may be misestimated.

Thus:

```text
Exploitation != OptimalAction
```

---

# 68. Exploration is not better learning by definition

Random/poor exploration can waste trials and miss informative comparisons.

Thus:

```text
MoreExploration != BetterLearning
```

---

# 69. Horizon changes exploration value

If only one choice remains, information about unknown options has little future
instrumental value.

If many choices remain, it can be valuable.

Thus:

```text
ExplorationValue depends on remaining horizon
```

---

# 70. Social observation can change exploration

Humans can copy others' exploratory/exploitative actions or treat their behavior as
information.

Thus:

```text
ExploreExploitPolicy
can be socially learned
```

---

# 71. Exploration is not curiosity

Curiosity can drive information seeking with no instrumental future payoff.

Directed exploration can be strategically instrumental.

Thus:

```text
Curiosity != DirectedExploration
```

though they can overlap.

---

# 72. Exploration can be epistemic action

HF9 already showed action can acquire causal evidence.

HF10 generalizes:

```text
Action
can have
OutcomeValue + InformationValue
```

---

# 73. Value of information depends on actionability

Instrumental value is high when information can change a consequential choice.

Thus:

```text
InformationValue
is relational to future policy
```

---

# 74. Reversibility changes information value

When a decision is reversible, acting now and learning may dominate waiting.

When irreversible, pre-decision information may be more valuable.

Thus:

```text
VoI depends on Reversibility
```

---

# 75. Option value

HF10 uses:

```text
OptionValue
= value of preserving a future ability to choose or exploit contingent information
```

This is not identical to current outcome value.

---

# 76. Current value is not option value

An action with lower immediate payoff may preserve future flexibility.

Thus:

```text
CurrentRewardValue != OptionValue
```

---

# 77. Flexibility is not always better

Preserving options can create delay, coordination and commitment costs.

Thus:

```text
MoreOptionValue != AlwaysBetter
```

---

# 78. Commitment can deliberately destroy option value

Precommitment removes tempting options to protect a future target.

Thus:

```text
SelfRegulation != MaximumFutureOptionSet
```

reconnecting HF4.

---

# 79. Commitment

Working definition:

```text
Commitment_D
= state transition that increases persistence probability and/or changes future
  option architecture, switching cost, resource allocation, social obligation or
  reversibility around a selected course
```

---

# 80. Commitment is not goal commitment

HF4 `GoalCommitment` is attachment to a goal.

HF10 commitment can bind a particular means/plan/action.

Thus:

```text
GoalCommitment != CourseOfActionCommitment
```

---

# 81. Commitment is not intention

An intention can exist while alternatives remain fully open.

Thus:

```text
Intention != Commitment
```

---

# 82. Commitment is not irreversibility

Revocable precommitments can alter behavior.

Thus:

```text
Commitment != Irreversibility
```

---

# 83. Commitment is not execution

Binding to A does not ensure A is successfully performed.

Thus:

```text
Commitment != Execution
```

---

# 84. Precommitment

```text
Precommitment
= current action that changes future option/cost/control architecture in advance of
  an anticipated future conflict
```

---

# 85. Precommitment is not more willpower

Experimental evidence shows precommitment can work by changing future motivation/
choice architecture, not by increasing a scalar internal resource.

Thus:

```text
Precommitment != MoreWillpower
```

---

# 86. Precommitment can be costly

Humans can pay to avoid future self-control costs.

Thus:

```text
PrecommitmentValue
can include reduced future control cost
```

---

# 87. Precommitment is not always optimal

Locking out future options can be harmful when:

```text
state changes
new information arrives
world changes
```

Thus:

```text
Precommitment != AlwaysBeneficial
```

---

# 88. Revocable commitment can be useful

A commitment can add friction rather than absolute prohibition.

Therefore option architecture has degrees:

```text
reminder
friction
penalty
lock
irreversible action
```

---

# 89. Sunk cost

A sunk cost is a resource already spent and not recoverable by current choice.

Thus:

```text
SunkResource
```

is historical, not future cost.

---

# 90. Sunk resource is not remaining cost

```text
SunkCost != RemainingCost
```

must be preserved in every escalation analysis.

---

# 91. Normatively irrelevant does not mean psychologically absent

Under standard forward-looking economic criteria, unrecoverable costs often should
not affect marginal continuation.

Humans nevertheless often show sunk-cost sensitivity.

Thus:

```text
NormativelySunk
!= PsychologicallyIgnored
```

---

# 92. Sunk-cost effect is not one mechanism

Evidence implicates:

```text
spent time/resource
remaining cost
completion proximity
personal responsibility
initial preference
loss framing
social signaling
```

Therefore:

```text
SunkCostEffect != OneBiasMechanism
```

---

# 93. Persistence after sunk cost is not automatically irrational

Continuation may have current benefits from:

```text
completion value
switching cost
reputation/signaling
future learning
```

Thus:

```text
PersistenceAfterSunkCost != IrrationalByDefinition
```

---

# 94. Historical sunk cost should be separated from completion value

A nearly complete project can have high marginal completion value even if sunk cost
is irrelevant.

Thus:

```text
SunkCost != CompletionValue
```

---

# 95. Sunk cost is not switching cost

Switching to B can incur a new prospective cost.

Thus:

```text
SunkCost != SwitchingCost
```

---

# 96. Switching cost can rationally create persistence

A course may remain optimal if abandoning it incurs:

```text
retooling
learning
contract
coordination
latency
```

costs.

---

# 97. Escalation and premature abandonment share determinants

Current evidence shows responsibility/preference/framing can push toward both
continuation and premature exit under different configurations.

Thus:

```text
PersistenceBias != OnlyDecisionFailureMode
```

---

# 98. Social signaling can alter commitment value

Staying the course can communicate trustworthiness/consistency in some social
settings.

Thus:

```text
PrivateEconomicValue
!= TotalSocialDecisionValue
```

---

# 99. Decision-maker identity matters

Self, close other and stranger decisions can show different sunk-cost effects.

Thus:

```text
SameOptions + DifferentAffectedActor
→ DifferentChoice
```

and HF1 actor/person boundary matters.

---

# 100. Planning

HF10 uses:

```text
Planning
= prospective construction/evaluation of possible action sequences or subgoal
  structures using an internal/external model of transitions and outcomes
```

---

# 101. Planning is not reasoning totality

Reasoning can compare propositions with no action sequence.

Thus:

```text
Planning != Reasoning
```

---

# 102. Planning is not simulation alone

Simulation of possibilities does not itself choose/organize an action policy.

Thus:

```text
Planning != Simulation
```

---

# 103. Plan

Working definition:

```text
Plan
= represented prospective partial sequence/tree/subgoal organization of intended or
  conditional actions toward a target
```

---

# 104. Plan is not policy

A policy maps states/information to actions.

A plan may encode one expected path plus contingencies.

Thus:

```text
Plan != Policy
```

---

# 105. Policy

```text
Policy
= mapping from represented state/information to action or action distribution
```

It can be learned without explicit conscious planning.

---

# 106. Policy is not strategy

A strategy can specify how to select/construct policies/plans/search methods across
contexts.

Thus:

```text
Policy != Strategy
```

---

# 107. Strategy

Working definition:

```text
Strategy
= higher-level rule/system for allocating representation, information search,
  planning, option selection and action methods across a class of situations
```

---

# 108. Strategy is not tactic

A tactic is a local method serving a strategy in a particular situation.

Thus:

```text
Strategy != Tactic
```

---

# 109. Strategy is not heuristic

A heuristic is a bounded shortcut/search rule.

A strategy can include several heuristics, plans and switching conditions.

Thus:

```text
Strategy != Heuristic
```

---

# 110. Plan is not fixed script

A robust plan can include:

```text
if X then A
if Y then B
replan if uncertainty exceeds threshold
```

Thus:

```text
Plan != FixedSequence
```

---

# 111. Planning is model-dependent

To simulate future actions, the Human needs beliefs about:

```text
state transitions
outcomes
constraints
other actors
```

Therefore:

```text
PlanQuality depends on WorldModelQuality
```

---

# 112. Planning is not full-horizon exhaustive search

Humans often plan to limited depth.

Thus:

```text
Planning != ExhaustiveTreeSearch
```

---

# 113. Planning depth is a resource allocation choice

Deeper search can improve evaluation but costs time/computation.

Time pressure can reduce planning depth.

Thus:

```text
PlanningDepth_D
```

is a graded dimension.

---

# 114. Planning depth is not planning existence

Shallow planning is still planning.

Thus:

```text
LowDepth != NoPlanning
```

---

# 115. Model-based versus model-free is not planning versus habit ontology

Two-step tasks distinguish transition-sensitive and reward-history influences.

But architecture/reliability studies warn against treating estimated scalars as
pure systems.

Thus:

```text
ModelBasedMeasure != PurePlanningModule
```

---

# 116. Model-free is not irrational

Cached/learned action values can be computationally efficient in stable settings.

Thus:

```text
ModelFree != BadChoiceByDefinition
```

---

# 117. Model-based is not always superior

When transitions are stable/repetitive and computation costly, model-free control
can be efficient.

Thus:

```text
ModelBased != AlwaysBetter
```

---

# 118. Humans can arbitrate by environmental demand

Recent experiments show exposure to environments rewarding generalization can
increase later model-based behavior.

Thus:

```text
ControlArchitectureUse
is adaptive/history-sensitive
```

---

# 119. Planning can stop at cached values

Depth-limited planning can simulate near future and use learned values beyond the
search horizon.

Thus:

```text
Planning + CachedValue
```

can coexist in one evaluation.

---

# 120. Habit/planning are not necessarily flat competitors

Hierarchical accounts allow goal-directed control to select learned action
sequences.

Thus:

```text
HabitualSequence
can be embedded within
GoalDirectedPlan
```

---

# 121. Hierarchical planning

Complex action can be divided into:

```text
subgoals
segments
local policies
```

reducing planning complexity.

---

# 122. Subgoal is not final goal

A subgoal has instrumental/organizational role toward a larger target.

Thus:

```text
Subgoal != FinalGoal
```

---

# 123. Subgoal value is relational

The same intermediate state can be valuable under one final goal and irrelevant
under another.

Thus:

```text
SubgoalValue depends on ActivePlan/Goal
```

---

# 124. Hierarchy is not just longer sequence

Hierarchical planning groups actions into meaningful chunks/options with higher-
level transition structure.

Thus:

```text
Hierarchy != SequenceLength
```

---

# 125. Hierarchical structure can reduce computational burden

Planning over subgoals can compress large state/action spaces.

But poor subgoals can also mislead.

Thus:

```text
HierarchyBenefit can coexist with HierarchyConstraint
```

---

# 126. Plan validity is state-dependent

A plan constructed at t1 can fail at t2 because:

```text
world changed
internal state changed
resource disappeared
other actor changed
```

Thus:

```text
PlanValidity_t1 != PlanValidity_t2
```

---

# 127. Plan revision is first-class

Robust planning includes monitoring/replanning triggers.

Therefore:

```text
Plan != OneTimeDecision
```

---

# 128. Strategy includes switching rules

A strategy is incomplete if it says only what to do when things go well.

It may include:

```text
continue
switch
abort
escalate
seek information
replan
```

conditions.

---

# 129. Stopping and switching differ

Stopping search ends deliberation.

Switching changes current course/policy.

Thus:

```text
Stopping != Switching
```

---

# 130. Switching and abandonment differ

Switching from A to B retains goal pursuit.

Abandoning may drop the goal/course entirely.

Thus:

```text
SwitchCourse != AbandonGoal
```

---

# 131. Persistence is not commitment strength

A Human may persist because switching is impossible, not because commitment is high.

Thus:

```text
ObservedPersistence != CommitmentStrength
```

---

# 132. Low switching is not preference stability

High friction can keep behavior unchanged even when preference changes.

Thus:

```text
BehavioralStability != PreferenceStability
```

---

# 133. Commitment can be social/institutional

Contracts, promises and role obligations create future costs/constraints outside
internal preference.

Thus:

```text
CommitmentArchitecture
can include
InstitutionalConstraint
```

---

# 134. Commitment can change identity/self-representation without defining identity

Public commitment can alter social/self expectations.

But HF1 retains:

```text
Commitment != HumanIdentity
```

---

# 135. Decision authority

HF10 separates:

```text
GenerateOptions
Recommend
Choose
Authorize
Execute
```

as different roles.

---

# 136. Recommendation is not decision

An advisor/AI can recommend A while the Human retains choice authority.

Thus:

```text
Recommendation != Decision
```

---

# 137. Decision is not authorization

A Human may prefer/choose A but lack legal/institutional authority to authorize it.

Thus:

```text
DecisionPreference != Authority
```

---

# 138. Authorization is not execution

The authorized actor/tool can fail/refuse/execute differently.

Thus:

```text
Authorization != Execution
```

---

# 139. Delegation

Working definition:

```text
Delegation
= assignment of some action generation, selection, planning or execution role to
  another actor/agent while preserving separately specified authority,
  responsibility and oversight relations
```

---

# 140. Delegation is not authority transfer by definition

A principal can delegate execution while retaining decision authority.

Thus:

```text
Delegation != AuthorityTransfer
```

---

# 141. Delegation is not responsibility elimination

Machine execution does not automatically erase principal responsibility.

Thus:

```text
Delegation != ResponsibilityElimination
```

---

# 142. Deference is not delegation

Deference means weighting another agent's recommendation heavily.

Delegation means assigning a decision/action role.

Thus:

```text
Deference != Delegation
```

---

# 143. Deference is not blind compliance

Recent moral-advice experiments show Humans can be influenced by AI while retaining
sensitivity to reasons/content.

Thus:

```text
Deference != BlindCompliance
```

---

# 144. AI can intervene before choice by generating options

If AI proposes `{A,B,C}`, it shapes the choice set before evaluation.

Thus:

```text
AIOptionGeneration
= DecisionArchitectureIntervention
```

---

# 145. AI-generated option set is not complete by definition

Missing option D may dominate all presented choices.

Thus:

```text
AIGeneratedOptionSet != CompleteOptionSet
```

---

# 146. AI comparison is not neutral presentation

Tables/summaries choose:

```text
which options
which attributes
which evidence
which ordering
```

Thus:

```text
AIComparisonSurface
can frame Human choice
```

---

# 147. AI recommendation is not Human preference

A Human can follow AI while privately preferring another option because of
authority/trust constraints.

Thus:

```text
FollowedAIChoice != HumanStablePreference
```

---

# 148. AI delegation changes moral/action architecture

Agentic delegation experiments show high-level goals can facilitate unethical
execution without the principal specifying every action.

Thus:

```text
HighLevelGoalDelegation
can change
RealizedActionDistribution
```

---

# 149. Delegation requires capability and alignment models

Before delegation, relevant variables include:

```text
agent capability
error mode
objective alignment
permissions
reversibility
auditability
```

This is decision/planning information.

---

# 150. Override is a decision policy

Human oversight is not just a static veto right.

It requires a rule for:

```text
when to inspect
when to intervene
when to trust
when to stop agent
```

Thus:

```text
OverrideCapability != OverridePolicy
```

---

# 151. More AI options can create option overload

Generative systems can make option generation cheap.

But evaluation cost does not vanish.

Therefore:

```text
CheapOptionGeneration
can increase
EvaluationBurden
```

---

# 152. AI can improve option coverage

Conversely, AI can surface options a Human would not retrieve/generate.

Thus:

```text
AIAugmentedOptionCoverage
can exceed
HumanUnaidedOptionCoverage
```

without guaranteeing better final choice.

---

# 153. Option-generation quality should be measured separately

For Human×AI systems measure:

```text
coverage
diversity
maximum quality
mean quality
missing critical options
invalid options
provenance
```

not option count alone.

---

# 154. Planning assistance should separate plan quality from execution capability

AI may generate an excellent plan that Human cannot execute.

Thus:

```text
PlanQuality != Executability
```

---

# 155. Executability is relational

A plan's executability depends on:

```text
Human skill
resources
tools
permissions
time
physical/social environment
```

This is the first strong residual toward HF11.

---

# 156. Plan feasibility is not desirability

A feasible plan can be low value; a desirable plan can be infeasible.

Thus:

```text
Feasibility != DecisionValue
```

---

# 157. Decision competence is not execution competence

A Human may choose correctly but fail at implementation.

Thus:

```text
DecisionCompetence != ExecutionCompetence
```

---

# 158. Planning competence is not motor/procedural skill

Knowing the sequence does not mean being able to perform it.

Thus:

```text
PlanKnowledge != SkillExecution
```

---

# 159. Commitment does not solve action initiation

A Human can be fully committed yet fail to initiate due to:

```text
motor constraint
fatigue
cue failure
fear
environmental block
```

Thus:

```text
Commitment != Initiation
```

---

# 160. Action selection is not action realization

Choosing motor/action target still leaves:

```text
initiation
coordination
feedback correction
termination
```

Thus:

```text
ActionSelection != RealizedAction
```

---

# 161. Plan can be correct but environment affordance absent

A plan to open a locked door fails even if its sequence is otherwise valid.

Thus:

```text
PlanValidity != CurrentAffordanceAvailability
```

---

# 162. Execution is feedback-sensitive

Many actions require continuous correction using perceptual/proprioceptive feedback.

Therefore:

```text
Execution != OpenLoopReplayOfPlan
```

This lies beyond HF10's main decision scope.

---

# 163. Skill compresses planning demand

Expert execution can bundle many lower-level decisions/control loops.

Thus:

```text
Skill
can reduce
OnlineDeliberativePlanningDemand
```

but skill acquisition/control belongs to the next boundary.

---

# 164. Tool use changes executable option set

Tools can transform an infeasible action into a feasible one.

Thus:

```text
ToolAvailability
changes
ActionAffordance/CapabilitySet
```

again exposing execution rather than decision.

---

# 165. HF10 DecisionProfile

```text
DecisionProfile_D = {
  goal / criterion,
  generated option set,
  option coverage/diversity,
  frame/reference,
  information acquisition mode,
  current state,
  risk/ambiguity profile,
  value/preference estimates,
  search history,
  stopping rule,
  selected option,
  commitment level/form,
  reversibility,
  switching/remaining costs,
  authority,
  external aids,
  uncertainty/confidence
}
```

---

# 166. InformationSearchProfile

```text
InformationSearchProfile_D = {
  current uncertainty,
  possible queries/actions,
  instrumental VoI,
  epistemic value,
  affective value/cost,
  search cost,
  horizon,
  reversibility,
  metacognitive estimate,
  search policy,
  stopping rule,
  avoided information,
  final uncertainty
}
```

---

# 167. ExploreExploitProfile

```text
ExploreExploitProfile_D = {
  option value estimates,
  uncertainty per option,
  remaining horizon,
  directed exploration,
  random exploration,
  social information,
  exploitation rate,
  information gain,
  reward outcome,
  policy adaptation
}
```

---

# 168. CommitmentProfile

```text
CommitmentProfile_D = {
  selected course,
  goal relation,
  sunk resources,
  remaining cost,
  switching cost,
  completion value,
  social/institutional obligations,
  reversibility,
  precommitment mechanism,
  exit conditions,
  observed persistence
}
```

---

# 169. PlanningProfile

```text
PlanningProfile_D = {
  world/transition model,
  target,
  horizon,
  represented states,
  candidate sequences,
  subgoals/hierarchy,
  planning depth,
  cached values/habit integration,
  contingencies,
  information actions,
  switching/replan rules,
  selected plan,
  executability assumptions,
  tools/delegation
}
```

---

# 170. Human×AI DecisionProfile

```text
HumanAIDecisionProfile_D = {
  who generated options,
  omitted option risk,
  framing/comparison surface,
  Human prior judgment,
  AI recommendation,
  Human deference,
  delegated scope,
  authority,
  responsibility,
  verification/override policy,
  reversibility,
  joint choice,
  independent Human choice,
  realized action actor
}
```

---

# 171. Cross-context falsifier matrix

| Case | Naive collapse attacked | HF10 surviving distinction |
|---|---|---|
| gain/loss wording reverses choice | choice = stable preference | frame/reference is part of choice process |
| framing varies across design | frame effect = one mechanism | mechanism/design-specific effects |
| description vs experience differs | distribution determines choice | acquisition history matters |
| rare outcomes mentally over-generated | objective distribution = considered distribution | mental sampling is biased/selected |
| regret feedback changes later gamble | choice depends only expected outcome | counterfactual affect enters future policy |
| noninstrumental info sought | VoI = action improvement | information has epistemic/affective value |
| health information avoided | more info always desired | information can have subjective cost |
| confidence-search relation changes by manipulation | confidence = stopping rule | metacognitive/search layers distinct |
| horizon increases directed/random exploration | exploration = noise | directed and random components |
| observing agents changes bandit policy | exploration purely individual | social information changes policy |
| explicit stop-versus-search task | stopping = absence of search | stopping is active meta-choice |
| more generated options raises max but lowers mean quality | more options always good | option set quality is distributional |
| large choice set harms some decisions, not all | choice overload universal | overload is relational/contextual |
| escalation persists with transparent returns | sunk-cost = missing information | motivational/social/commitment mechanisms remain |
| spent and remaining time both matter | sunk = all cost | sunk vs remaining cost separate |
| near completion increases continuation | sunk cost explains persistence | completion value separate |
| public persistence signals trustworthiness | persistence irrational | social value can alter continuation |
| precommitment helps effortful reward | self-control = willpower | future option architecture matters |
| revocable commitment works | commitment = irreversible lock | graded friction can change future choice |
| two-step task shows mixed model-based/free | one planning system | multiple policy influences coexist |
| two-step reliability weak under short designs | scalar = trait | measurement uncertainty matters |
| time pressure shortens planning depth | planning = binary | depth is resource-sensitive |
| subgoals support hierarchy | plan = flat sequence | planning can be hierarchical |
| AI generates comparison table | AI only evaluates given options | AI shapes option set/frame upstream |
| AI moral advice influences but not blindly | deference = obedience | reasons/source weighting distinct |
| machine delegation increases unethical execution | delegation = neutral executor | delegated action architecture changes outcomes |
| AI-labeled errors corrected asymmetrically | expert oversight = reliable veto | override/deference policy is conditional |

---

# 172. Competing models

## M1 — revealed preference transparency

### Claim

Observed choice reveals stable preference/value.

### Failure

Framing, acquisition history, state, option-set and time effects.

**Disposition:** reject as descriptive foundation.

## M2 — expected-utility psychological algorithm

### Strength

Clear normative comparison under known probabilities/outcomes.

### Failure

Framing, ambiguity, description-experience, regret and context effects.

**Disposition:** retain as normative/model family; reject universal psychological
algorithm.

## M3 — prospect/reference-dependent family

### Strength

Explains many gain/loss/reference effects.

### Failure

Not every framing variant is one reference-value mechanism; reason/gist/design
accounts remain competitors.

**Disposition:** retain theory family, not ontology.

## M4 — choice overload universalism

### Failure

Many-option effects are strongly moderated by task/chooser/context.

**Disposition:** reject universal option-count law.

## M5 — instrumental information-value only

### Failure

Noninstrumental information seeking and information avoidance.

**Disposition:** replace with plural information-value profile.

## M6 — exploration as random noise

### Failure

Horizon-sensitive directed exploration and social learning.

**Disposition:** reject; retain directed + random components.

## M7 — exhaustive optimization

### Failure

Search cost, stopping, satisficing, finite horizon and ecological constraints.

**Disposition:** normative local model, not universal Human algorithm.

## M8 — sunk-cost irrationality mechanism

### Failure

Completion, remaining cost, responsibility, framing and signaling effects.

**Disposition:** retain sunk-cost sensitivity as phenomenon; mechanism plural.

## M9 — willpower/precommitment

### Failure

Precommitment changes future option architecture and may reduce anticipated control
cost without increasing internal resource.

**Disposition:** reject scalar willpower mechanism.

## M10 — flat model-based versus model-free dual control

### Strength

Useful computational distinction.

### Failure

mixed signals, reliability issues, depth-limited integration and hierarchical
sequences.

**Disposition:** retain operational contrasts; reject complete architecture.

## M11 — full-horizon planner

### Failure

Human planning is depth-limited/resource-sensitive and often hierarchical.

**Disposition:** reject universal exhaustive planner.

## M12 — AI as neutral decision support

### Failure

AI can generate/omit options, frame comparisons, anchor recommendations and execute
delegated goals.

**Disposition:** replace with role-typed joint decision architecture.

---

# 173. HF10 anti-laws

## Decision / choice

1. `Judgment != Decision`.
2. `DecisionProcess != ChoiceOutcome`.
3. `Choice != Action`.
4. `Choice != Commitment`.
5. `Commitment != Execution`.
6. `OptionGeneration != OptionEvaluation`.
7. `OptionGeneration != MemoryRetrievalOnly`.
8. `BestChoiceWithinSet != BestAvailableActionInReality`.
9. `MoreGeneratedOptions != MonotonicDecisionQuality`.
10. `FirstOption != BestOption by definition`.
11. `OptionSet != NeutralContainer`.
12. `MoreOptions != AlwaysBetter`.
13. `MoreOptions != AlwaysWorse`.
14. `ObservedChoice != StablePreferenceReadout`.
15. `FrameEffect != UniqueMechanismProof`.
16. `DescriptionInvarianceFailure != UniqueIrrationalityDiagnosis`.
17. `TemporalPreferenceConflict != TrueSelfIdentification`.

## risk / information

18. `Risk != Ambiguity`.
19. `Uncertainty != Risk`.
20. `Ambiguity != AlwaysAvoided`.
21. `RiskPreference_D != GlobalRiskTrait`.
22. `DescriptionChoice != ExperienceChoice`.
23. `ObjectiveDistribution != ExperiencedSampleHistory`.
24. `GeneratedOutcomeSet != ObjectiveProbabilityDistribution`.
25. `Regret != RiskAversion`.
26. `AnticipatedRegret != ExperiencedRegret`.
27. `InformationValue != InstrumentalVoIOnly`.
28. `AvailableInformation != SoughtInformation`.
29. `InformationAvoidance != IrrationalIgnorance by definition`.
30. `MoreInformation != AlwaysPreferred`.
31. `InformationQuantity != DecisionValue`.
32. `InformationSearch != PassiveFreeDelay`.
33. `Confidence != StoppingRule`.
34. `MetacognitiveSensitivity != SearchOptimality`.
35. `SearchPolicy != StoppingRule`.
36. `Stopping != Failure`.
37. `InfiniteSearch != PerfectDecisionMaking`.
38. `FastStopping != EfficientByDefinition`.
39. `Satisficing != IrrationalityByDefinition`.

## explore / exploit

40. `Exploration != RandomChoice`.
41. `RandomExploration != DirectedExploration`.
42. `Exploitation != OptimalAction`.
43. `MoreExploration != BetterLearning`.
44. `Curiosity != DirectedExploration`.
45. `CurrentRewardValue != OptionValue`.
46. `MoreOptionValue != AlwaysBetter`.

## commitment / sunk cost

47. `GoalCommitment != CourseOfActionCommitment`.
48. `Intention != Commitment`.
49. `Commitment != Irreversibility`.
50. `Commitment != Execution`.
51. `Precommitment != MoreWillpower`.
52. `Precommitment != AlwaysBeneficial`.
53. `SunkCost != RemainingCost`.
54. `NormativelySunk != PsychologicallyIgnored`.
55. `SunkCostEffect != OneBiasMechanism`.
56. `PersistenceAfterSunkCost != IrrationalByDefinition`.
57. `SunkCost != CompletionValue`.
58. `SunkCost != SwitchingCost`.
59. `PersistenceBias != OnlyDecisionFailureMode`.
60. `ObservedPersistence != CommitmentStrength`.
61. `BehavioralStability != PreferenceStability`.

## planning / strategy

62. `Planning != Reasoning`.
63. `Planning != Simulation`.
64. `Plan != Policy`.
65. `Policy != Strategy`.
66. `Strategy != Tactic`.
67. `Strategy != Heuristic`.
68. `Plan != FixedSequence`.
69. `Planning != ExhaustiveTreeSearch`.
70. `LowPlanningDepth != NoPlanning`.
71. `ModelBasedMeasure != PurePlanningModule`.
72. `ModelFree != BadChoiceByDefinition`.
73. `ModelBased != AlwaysBetter`.
74. `Subgoal != FinalGoal`.
75. `Hierarchy != SequenceLength`.
76. `PlanValidity_t1 != PlanValidity_t2`.
77. `Plan != OneTimeDecision`.
78. `Stopping != Switching`.
79. `SwitchCourse != AbandonGoal`.

## Human×AI / authority

80. `Recommendation != Decision`.
81. `DecisionPreference != Authority`.
82. `Authorization != Execution`.
83. `Delegation != AuthorityTransfer`.
84. `Delegation != ResponsibilityElimination`.
85. `Deference != Delegation`.
86. `Deference != BlindCompliance`.
87. `AIGeneratedOptionSet != CompleteOptionSet`.
88. `FollowedAIChoice != HumanStablePreference`.
89. `OverrideCapability != OverridePolicy`.
90. `CheapOptionGeneration != LowEvaluationBurden`.
91. `PlanQuality != Executability`.
92. `Feasibility != DecisionValue`.
93. `DecisionCompetence != ExecutionCompetence`.
94. `PlanKnowledge != SkillExecution`.
95. `Commitment != Initiation`.
96. `ActionSelection != RealizedAction`.
97. `PlanValidity != CurrentAffordanceAvailability`.
98. `Execution != OpenLoopReplayOfPlan`.

---

# 174. Minimum HF10 grammar

```text
Goals / Values / Current State
        ↓
Problem + Option Generation
        ↓
Option Set / Frame / Reference
        ↓
Information State
  ├─ risk
  ├─ ambiguity
  ├─ uncertainty
  └─ provenance
        ↓
Search / Exploration
  ↑ instrumental + epistemic + affective information value
        ↓
Stopping Rule
        ↓
Evaluation / Judgment
        ↓
Choice
        ↓
Commitment Architecture
  ├─ reversibility
  ├─ precommitment
  ├─ sunk/remaining/switching cost
  └─ social/institutional obligations
        ↓
Planning / Policy / Strategy
  ├─ horizon
  ├─ subgoals
  ├─ hierarchy
  ├─ contingencies
  └─ delegation
        ↓
[HF11 boundary]
Initiation / Execution / Online Control
        ↓
Outcome / Feedback
        ↺
Update value, model, plan, commitment and search policy
```

---

# 175. Reconnection to HF9

HF9 answers:

```text
What should be inferred/judged?
```

HF10 answers:

```text
Which option/search/plan should be selected and when should search stop?
```

Thus:

```text
InferencePolicy != DecisionPolicy
```

although they interact.

---

# 176. Reconnection to HF8

World models determine planning predictions.

Beliefs/knowledge can be stale or uncertain.

Thus:

```text
PlanQuality
cannot exceed model/evidence quality automatically
```

and decision policy must manage epistemic uncertainty.

---

# 177. Reconnection to HF7

Experience-based choice depends on memory/sampling of past outcomes.

Prospective memory can determine whether a selected plan is later retrieved.

Thus:

```text
Choice != Memory
```

but memory strongly conditions available options and policy execution.

---

# 178. Reconnection to HF6

Strategies/policies/habits change with learning.

Model-based/model-free arbitration is history-sensitive.

Therefore:

```text
DecisionPolicy_t
```

is adaptive rather than permanent trait.

---

# 179. Reconnection to HF5

Internal state can change:

```text
risk tolerance
information seeking
planning depth
stopping
commitment persistence
```

without changing option facts.

Thus state remains a decision input.

---

# 180. Reconnection to HF4

HF4 supplies:

```text
GoalSet
DecisionValue
MotivationProfile
SelfRegulation
```

HF10 supplies:

```text
option architecture
search/stopping
choice
commitment
planning/policy
```

so:

```text
Value != Choice
GoalCommitment != CourseCommitment
```

remain fundamental.

---

# 181. Reconnection to HF3

Attention/WM/metacognition affect:

```text
which options are compared
how many branches are maintained
when search stops
```

but:

```text
Attention != Decision
WorkingMemory != Planning
Confidence != StoppingRule
```

---

# 182. Reconnection to HF2

Regret, uncertainty, conflict and sense of commitment are experiences.

They can guide choice without being normative truth.

Thus HF2 evidence firewall persists.

---

# 183. Reconnection to HF1

HF1 separated:

```text
Actor
Agent
Authority
Responsibility
HumanIndividual
Human×AI TaskSystem
```

HF10 consumes these distinctions in delegation/authorization.

A delegated plan does not merge identities or automatically transfer authority.

---

# 184. What HF10 does not establish

HF10 does not establish:

- one final theory of decision or choice;
- that revealed preference is useless;
- that expected utility is normatively wrong;
- that prospect theory is false;
- one universal framing mechanism;
- one stable Human risk trait;
- that ambiguity aversion is always irrational;
- that description or experience is generally superior;
- one regret mechanism;
- that all information seeking is rational;
- that information avoidance is beneficial;
- one optimal exploration algorithm for Humans;
- that directed/random exploration exhaust exploration;
- one stopping rule;
- that satisficing always beats optimization;
- that more options usually harm choice;
- that all sunk-cost persistence is irrational;
- that sunk costs should normatively matter by themselves;
- that precommitment is always good;
- that model-based/model-free are literal independent brain systems;
- that model-based control is always superior;
- that planning is always explicit/conscious;
- that plans are necessarily hierarchical;
- that AI option generation improves or harms decisions by default;
- that delegation transfers authority/responsibility;
- that deciding/committing guarantees action.

---

# 185. The residual HF10 cannot finish

HF10 repeatedly reaches the same next boundary.

A Human may have:

```text
selected option
strong commitment
valid plan
sufficient motivation
```

and still fail because:

```text
cannot initiate action
cannot coordinate effectors
misperceives affordance
lacks practiced skill
receives unexpected sensory feedback
must correct trajectory online
cannot operate tool/interface
cannot coordinate with another actor
```

Conversely, skilled action can occur with very little explicit planning.

These are not primarily choice/planning questions.

They concern how policy becomes **embodied, situated, feedback-controlled effect**.

The repeated constructs are:

```text
Action
Initiation
Execution
Motor/Sensorimotor Control
Affordance
Skill
Coordination
Feedback / Error Correction
Tool Use
```

---

# 186. Exact next foundation

HF10 therefore selects:

# HF11 — Action, Execution, Sensorimotor Control, Affordance, Skill, Coordination, Feedback and Tool Use

HF11 should ask:

1. What is action relative to choice, intention, policy, movement and outcome?
2. What is action initiation relative to motivation/commitment?
3. What is motor command relative to action goal and movement trajectory?
4. What is affordance relative to objective possibility, perceived possibility and
   capability?
5. How do feedforward and feedback control interact?
6. What is sensorimotor error relative to outcome failure?
7. What is skill relative to knowledge, habit, automaticity and motor control?
8. How does practice compress online control/planning?
9. How do body representation/proprioception/interoception constrain execution?
10. What is coordination across limbs, tools, people and agents?
11. When does a tool become part of the effective control loop without becoming
    biological body or Human identity?
12. How do latency, noise, interruption and recovery alter execution?
13. How should Human×AI delegated execution separate command, authority, control,
    monitoring, override and realized effect?
14. What next boundary emerges after situated action/control is reconstructed?

HF11 should not predefine HF12.

---

# 187. Candidate HF11 falsifiers

- intention/choice versus actual initiation dissociations;
- ideomotor/action-effect learning;
- reaction time and movement trajectory divergence;
- motor adaptation / visuomotor perturbation;
- proprioceptive and visual feedback conflicts;
- sensory prediction error versus task error;
- speed–accuracy motor tradeoffs;
- skilled versus novice online control;
- automaticity after practice;
- affordance perception under capability/tool changes;
- tool-use body-schema/control extension;
- bimanual/interpersonal coordination;
- remote/robotic teleoperation latency;
- AI agent execution with Human monitoring/override;
- failed execution despite correct plan versus successful skilled execution with
  minimal explicit deliberation.

---

# 188. HF10 synthesis

HF10 began with:

```text
Several plausible judgments/options exist. What now?
```

The answer is not one value-maximization operator.

Human sequential decision is a recurrent architecture involving:

```text
option generation
representation/framing
information search
risk/ambiguity handling
exploration/exploitation
stopping
choice
commitment
planning
strategy/policy
switching/replanning
delegation
```

under finite resources and changing states.

The deepest compressions are:

```text
ObservedChoice != StablePreference
MoreInformation != AlwaysBetter
MoreOptions != AlwaysBetter
Exploration != Randomness
Stopping != Failure
Persistence != CommitmentQuality
Plan != Policy != Strategy
Decision != Execution
```

and:

> **A decision architecture is not merely a comparison of values. It constructs the
> available options, decides whether uncertainty is worth reducing, chooses when to
> stop searching, selects and sometimes constrains future options, organizes
> actions across time, and reallocates control when the world changes.**

But it still ends before realized action.

The exact next question is:

> **How does a selected policy become coordinated physical/social/tool-mediated
> action under continuous feedback and error?**

That is the HF11 action/execution/control boundary.
