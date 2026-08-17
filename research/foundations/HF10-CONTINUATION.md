---
schema_version: 1
id: human.foundations.hf10.continuation
title: Human Foundations Continuation after HF10
type: handoff
profile: research
lifecycle: active
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
updated: 2026-08-17
summary: Exact continuation after HF10. HF10 reconstructs the bridge from judgment to temporally organized action policy through option generation, search, stopping, choice, commitment, planning, strategy and delegation. The repeated unresolved boundary is realized situated action: initiation, sensorimotor control, affordance, skill, coordination, feedback, error correction and tool-mediated execution.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.foundations.hf10
  - human.foundations.hf10.sources
---
# Human Foundations Continuation after HF10

## HF10 completed result

HF10's minimum decision/planning grammar is:

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
```

## Decision / choice

Retain:

```text
Judgment != Decision
DecisionProcess != ChoiceOutcome
Choice != Action
Choice != Commitment
Commitment != Execution
OptionGeneration != OptionEvaluation
OptionGeneration != MemoryRetrievalOnly
BestChoiceWithinSet != BestAvailableActionInReality
MoreGeneratedOptions != MonotonicDecisionQuality
OptionSet != NeutralContainer
ObservedChoice != StablePreferenceReadout
```

Observed choice remains evidence about current policy under a particular option set,
frame, state and history, not a timeless preference oracle.

## Framing / risk / ambiguity

Retain:

```text
FrameEffect != UniqueMechanismProof
DescriptionInvarianceFailure != UniqueIrrationalityDiagnosis
Risk != Ambiguity
Uncertainty != Risk
RiskPreference_D,t != GlobalRiskTrait
DescriptionChoice != ExperienceChoice
ObjectiveDistribution != ExperiencedSampleHistory
GeneratedOutcomeSet != ObjectiveProbabilityDistribution
```

Representation and acquisition history are causal parts of choice.

## Regret

Retain:

```text
Regret != RiskAversion
AnticipatedRegret != ExperiencedRegret
```

Regret can be both predicted policy input and later counterfactual outcome signal.
Do not freeze one regret utility term across all domains.

## Information value / search

Use plural information value:

```text
InformationValueProfile = {
  instrumental action value,
  epistemic/uncertainty-reduction value,
  affective value/cost,
  acquisition cost,
  delay/opportunity cost,
  reversibility/horizon relation
}
```

Retain:

```text
InformationValue != InstrumentalVoIOnly
AvailableInformation != SoughtInformation
InformationAvoidance != IrrationalIgnorance by definition
MoreInformation != AlwaysPreferred
InformationQuantity != DecisionValue
Confidence != StoppingRule
SearchPolicy != StoppingRule
Stopping != Failure
InfiniteSearch != PerfectDecisionMaking
Satisficing != IrrationalityByDefinition
```

## Exploration / exploitation

Retain:

```text
Exploration != RandomChoice
DirectedExploration != RandomExploration
Exploitation != OptimalAction
MoreExploration != BetterLearning
Curiosity != DirectedExploration
```

Exploration value depends on uncertainty, future horizon and whether acquired
information can influence later policy. Social observation can change explore/
exploit strategy.

## Option generation / overload

Retain:

```text
OptionCount != OptionDiversity
MoreOptions != AlwaysBetter
MoreOptions != AlwaysWorse
ChoiceOverload != UniversalOptionCountLaw
```

More options can increase maximum quality while reducing average quality and
raising comparison/evaluation cost.

## Commitment / sunk cost

Retain:

```text
GoalCommitment != CourseOfActionCommitment
Intention != Commitment
Commitment != Irreversibility
Commitment != Execution
Precommitment != MoreWillpower
Precommitment != AlwaysBeneficial
SunkCost != RemainingCost
SunkCost != CompletionValue
SunkCost != SwitchingCost
SunkCostEffect != OneBiasMechanism
PersistenceAfterSunkCost != IrrationalByDefinition
ObservedPersistence != CommitmentStrength
BehavioralStability != PreferenceStability
```

Persistence can reflect completion value, prospective switching cost,
responsibility, social signaling or inability to switch as well as sunk-cost
sensitivity.

## Planning / policy / strategy

Working distinctions:

```text
Plan
= represented prospective partial sequence/tree/subgoal structure

Policy
= state/information → action mapping

Strategy
= higher-level allocation rule for search/planning/policy across situations

Tactic
= local method serving a strategy/plan
```

Retain:

```text
Planning != Reasoning
Planning != Simulation
Plan != Policy
Policy != Strategy
Strategy != Tactic
Strategy != Heuristic
Plan != FixedSequence
Planning != ExhaustiveTreeSearch
LowPlanningDepth != NoPlanning
ModelBasedMeasure != PurePlanningModule
ModelFree != BadChoiceByDefinition
ModelBased != AlwaysBetter
Subgoal != FinalGoal
Hierarchy != SequenceLength
PlanValidity_t1 != PlanValidity_t2
Plan != OneTimeDecision
Stopping != Switching
SwitchCourse != AbandonGoal
```

Human planning can be depth-limited, hierarchical and can combine prospective
simulation with learned/cached action values.

## Human×AI decision/delegation

Separate roles:

```text
GenerateOptions
Frame/Compare
Recommend
Choose
Authorize
Execute
Monitor/Override
```

Retain:

```text
Recommendation != Decision
DecisionPreference != Authority
Authorization != Execution
Delegation != AuthorityTransfer
Delegation != ResponsibilityElimination
Deference != Delegation
Deference != BlindCompliance
AIGeneratedOptionSet != CompleteOptionSet
FollowedAIChoice != HumanStablePreference
OverrideCapability != OverridePolicy
PlanQuality != Executability
```

AI can intervene upstream by defining the option set and downstream by executing
high-level goals. These are distinct causal/authority roles.

## HF10 research objects

### DecisionProfile_D

```text
{
  goal/criterion,
  generated option set,
  option coverage/diversity,
  frame/reference,
  acquisition mode,
  state,
  risk/ambiguity,
  preference/value estimates,
  search history,
  stopping rule,
  selected option,
  commitment,
  reversibility,
  switching/remaining costs,
  authority,
  external aids,
  uncertainty/confidence
}
```

### InformationSearchProfile_D

```text
{
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

### CommitmentProfile_D

```text
{
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

### PlanningProfile_D

```text
{
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

## High-information falsifiers to preserve

- formally equivalent gain/loss frames producing preference reversals;
- framing effects remaining design/mechanism-sensitive rather than one theory
  fingerprint;
- description versus experience producing different risky choice;
- generated possible outcomes differing systematically from objective
  distributions;
- regret feedback altering later policy with risk/task boundaries;
- noninstrumental information seeking;
- active information avoidance under self-protective/affective conditions;
- metacognitive sensitivity predicting search quality while confidence-search
  relations remain context-sensitive;
- directed and random exploration dissociating with future horizon;
- social observation changing explore/exploit behavior;
- explicit search-versus-stop decisions in self-paced learning;
- option generation improving maximum option quality while increasing evaluation
  burden;
- conditional rather than universal choice overload;
- escalation persisting despite transparent future returns;
- spent and remaining costs independently affecting continuation;
- completion, responsibility and social signaling affecting persistence;
- precommitment and revocable precommitment improving some future choice conflicts;
- mixed model-based/model-free influences and weak scalar measurement reliability;
- depth-limited planning under time pressure;
- hierarchical subgoal representation and learned action sequences;
- AI-generated comparison/option surfaces framing decisions;
- AI advice producing conditional rather than blind deference;
- machine delegation changing realized unethical action rates without settling
  responsibility transfer.

## Exact next foundation

HF10 repeatedly finds that choice/commitment/planning do not determine realized
action.

A Human can have:

```text
correct decision
strong commitment
valid plan
```

and still fail because action must be initiated and controlled in a body/environment.
Conversely, skilled actions can unfold with little explicit online planning.

The missing relation is:

```text
Selected Policy / Plan
→ Realized Situated Effect
```

which depends on:

```text
Action initiation
Sensorimotor control
Affordances
Skill
Coordination
Feedback / prediction error / online correction
Tool use
```

Therefore the exact next round is:

# HF11 — Action, Execution, Sensorimotor Control, Affordance, Skill, Coordination, Feedback and Tool Use

## HF11 starting questions

1. What is action relative to choice, intention, policy, movement and outcome?
2. What is initiation relative to motivation and commitment?
3. What is action selection relative to motor command/trajectory?
4. What is an affordance relative to objective option, perceived action
   possibility and current capability?
5. How do feedforward prediction and feedback correction interact?
6. What is sensory prediction error relative to task/outcome error?
7. What is skill relative to knowledge, habit, automaticity and motor control?
8. How does practice reduce/reshape online planning and attention demands?
9. How do proprioception/body representation constrain action?
10. What is coordination across limbs, tools, people and agents?
11. When does a tool enter the effective control loop without becoming biological
    body or Human identity?
12. How do latency, noise, interruption and recovery alter execution?
13. In Human×AI delegated execution, how should command, authority, control,
    monitoring, override and realized effect be separated?
14. What next boundary emerges after situated action/control is rebuilt?

## Candidate HF11 falsifiers

- intended/selected action versus failed initiation;
- motor adaptation under visuomotor perturbation;
- visual/proprioceptive feedback conflict;
- sensory prediction error versus outcome/task error;
- speed–accuracy tradeoffs;
- skilled versus novice movement control;
- automaticity/practice effects;
- affordance perception changing with body/tool/capability;
- tool-use control/body-schema extension;
- bimanual/interpersonal coordination;
- remote/robotic teleoperation latency;
- AI executor with Human monitor/override;
- correct plan with failed execution versus skilled execution with minimal explicit
  deliberation.

## Do not precommit

HF10 does not establish that:

- action is movement;
- choice necessarily initiates action;
- motor control is purely feedforward or purely feedback;
- affordance is only an objective environmental property;
- affordance is only subjective perception;
- skill is explicit knowledge;
- skill is habit;
- automatic action is agentless action;
- tool use literally incorporates every tool into the biological body;
- faster action is better action;
- feedback is always beneficial despite delay/noise;
- AI execution transfers responsibility or authority by default.

## Stop rule

Do not schedule HF12 now. HF11 must expose a repeated neighboring distinction whose
absence creates category failures across materially different action/control cases.
