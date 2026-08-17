---
schema_version: 1
id: human.foundations.hf11
title: HF11 — Action, Execution, Sensorimotor Control, Affordance, Skill, Coordination, Feedback and Tool Use
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
summary: HF11 reconstructs how selected policies/plans become realized situated effects. It separates action goal, action selection, motor preparation, initiation, motor command/control policy, movement trajectory, online correction, task outcome, reward consequence and sense of agency; motor abundance from noise; predictive/feedforward from feedback control; sensory/perceptual prediction, task and reward error; adaptation from skill and automaticity; affordance from object property or subjective belief; attunement from calibration; tool-mediated control/body-schema change from biological or personal identity extension; intra-person, interpersonal and human-machine coordination; remote command from immediate effect; and Human-in-the-loop/override/delegation from meaningful control, authority and responsibility. The strongest residual is coordination among independently modeling agents, exposing social interaction, joint action, communication, shared goals, roles and cooperation.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
  - HF11
related:
  - human.foundations.hf10
  - human.foundations.hf11.sources
  - human.foundations.hf11.continuation
---
# HF11 — Action, Execution, Sensorimotor Control, Affordance, Skill, Coordination, Feedback and Tool Use

## 0. Status and question

HF10 ended with:

```text
PlanQuality != Executability
DecisionCompetence != ExecutionCompetence
PlanKnowledge != SkillExecution
Commitment != Initiation
ActionSelection != RealizedAction
Execution != OpenLoopReplayOfPlan
```

HF11 therefore asks:

> **How does a selected policy/plan become realized physical, social or
> tool-mediated effect in a changing world?**

The inherited collapses are:

```text
Action = choice
Action = movement
Movement = outcome
Intention = initiation
Motor command = trajectory
Variability = noise
Feedback = correction after the fact
Motor control = feedback servo
Motor control = open-loop program
Error = one scalar
Adaptation = skill
Skill = explicit knowledge
Skill = habit
Practice = automaticity
Affordance = object property
Affordance = subjective belief
Tool extension = body/person extension
Coordination = independent controllers added together
Teleoperation delay = network nuisance
Human in loop = meaningful control
Delegation = authority/responsibility transfer
```

None survives cross-context falsification.

---

# 1. Action is qualifier-required

HF11 uses:

```text
Action(H, Goal_D, Context, t)
```

for an actor-relative, goal/effect-organized intervention or controlled behavior
that is evaluated at a declared scale.

An `Action` may contain many movements and may itself be a component of a larger
action.

---

# 2. Action is not choice

HF10 selection can occur without execution.

Thus:

```text
Choice != Action
```

---

# 3. Action is not intention

An intention can remain unexecuted.

Thus:

```text
Intention != Action
```

---

# 4. Action is not movement

A movement is a physical change in effector/body/tool state.

The same movement can serve different goals; one action can be implemented by many
movement patterns.

Thus:

```text
Action != Movement
```

---

# 5. Movement is not task outcome

A movement can be kinematically executed while failing the goal.

Thus:

```text
Movement != TaskOutcome
```

---

# 6. Task outcome is not reward outcome

The motor target can be hit but broader reward/value can be poor.

Thus:

```text
TaskOutcome != RewardOutcome
```

HF4 reward/value remains downstream and distinct.

---

# 7. Action scale matters

Examples:

```text
press key
open door
make tea
perform surgery
move house
```

can all be called actions at different temporal/compositional scales.

Therefore:

```text
Action_D
```

must declare the question/scale.

---

# 8. Action decomposition

HF11 minimum decomposition:

```text
ActionGoal / IntendedEffect
        ↓
ActionSelection
        ↓
Motor Preparation
        ↓
Initiation / Release
        ↓
Control Policy / Motor Commands
        ↓
Effector / Tool Movement
        ↓
Online State Estimation + Correction
        ↓
Task / Environmental Outcome
        ↓
Reward / Consequence
```

with experience/agency evidence alongside—not inside—the physical chain.

---

# 9. Action goal is not motor command

The goal can be invariant while muscle/joint commands vary.

Thus:

```text
ActionGoal != MotorCommand
```

---

# 10. Motor command is not movement trajectory

Body/environment dynamics mediate:

```text
command
→ trajectory
```

The same command can produce different movement under changed load/state.

Thus:

```text
MotorCommand != MovementTrajectory
```

---

# 11. Movement trajectory is not action identity

Two different trajectories can satisfy one action goal.

Therefore:

```text
MovementTrajectory != ActionIdentity
```

---

# 12. Environmental effect is not fully determined by movement

Object state, friction, partner action, tool state and disturbances matter.

Thus:

```text
MovementTrajectory
+ WorldState
→ EnvironmentalEffect
```

---

# 13. Voluntary action is not consciously micromanaged movement

Humans can consciously choose a goal while low-level trajectory corrections occur
without awareness.

Therefore:

```text
VoluntaryAction != ConsciousControlOfEveryCorrection
```

---

# 14. Ideomotor/action-effect family

A major theory family holds that learned representations of action effects can help
select/initiate actions expected to produce those effects.

HF11 retains this role.

---

# 15. Anticipated effect can control action selection

After learning:

```text
Action A → Effect E
```

representing E can facilitate A.

Thus action-effect prediction is a real control variable.

---

# 16. Action-effect representation is not action itself

```text
Represent(Effect E)
```

can occur without action, or can select different action routes depending on
context.

Thus:

```text
ActionEffectRepresentation != Action
```

---

# 17. Ideomotor evidence does not identify one associative mechanism

Rapid remapping and causal/propositional accounts can reproduce classic effects in
some paradigms.

Thus:

```text
IdeomotorEffect != UniqueBidirectionalAssociationProof
```

---

# 18. Goal versus movement representation remains separable

Action-effect studies distinguish representations of:

```text
target/effect
movement
response key/effector
action rule
```

Thus:

```text
GoalRepresentation != MovementRepresentation
```

---

# 19. Action-effect learning is not all action control

Reflex-like corrections, learned policies, stimulus-driven responses and
sensorimotor adaptation need not reduce to consciously represented desired effects.

Thus:

```text
ActionControl != IdeomotorControlOnly
```

---

# 20. Intention

HF11 treats intention as an action-related prospective state established in HF4/
HF10, not as the physical trigger of movement.

---

# 21. Intention is not motor preparation

A Human can intend an action before specific effector/trajectory preparation.

Thus:

```text
Intention != MotorPreparation
```

---

# 22. Motor preparation

Working definition:

```text
MotorPreparation
= pre-execution organization/configuration of action-relevant control state such
  that a selected movement/action can be rapidly released/executed
```

---

# 23. Preparation is not initiation

StartReact findings show a prepared action can be released by an unexpected
startling signal.

Thus:

```text
MotorPreparation != Initiation
```

---

# 24. Initiation

Working definition:

```text
Initiation
= transition from prepared/selected action state into overt control/execution
```

This is not motivation itself.

---

# 25. Commitment is not initiation

A committed actor may fail to initiate.

Clinical freezing/akinesia is a strong falsifier.

Thus:

```text
Commitment != Initiation
```

---

# 26. Initiation is not continuation

Starting a movement and sustaining/transitioning it are distinct control problems.

Thus:

```text
Initiation != Continuation
```

---

# 27. Initiation is not sense of willing

Movement generation and subjective volitional experience can be experimentally/
clinically separated.

Thus:

```text
MovementInitiation != SenseOfVolition
```

---

# 28. Readiness potential is evidence, not intention

Pre-movement cortical potentials depend on task/movement/method.

Therefore:

```text
ReadinessPotential != Intention
ReadinessPotential != FreeWill
```

---

# 29. Initiation failure is not no goal

Parkinsonian freezing can occur despite an obvious goal to step.

Thus:

```text
InitiationFailure != GoalAbsence
```

---

# 30. Initiation can depend on preparatory postural organization

Successful gait initiation requires anticipatory postural adjustments.

Changing that preparation can rescue stepping in some freezing cases.

Thus:

```text
Goal + Commitment
are insufficient without
ExecutablePreparatoryState
```

---

# 31. Action knowledge is not skilled production

Apraxia provides strong dissociations.

A person can retain knowledge about tool function/action meaning yet fail to produce
correct purposeful movement.

Thus:

```text
ActionKnowledge != SkilledActionExecution
```

---

# 32. Praxis is not strength

Higher-order skilled-action deficit can occur without elementary weakness.

Thus:

```text
Strength != PraxisCapability
```

---

# 33. Praxis is not one mechanism

Apraxia subtypes separate:

```text
action sequencing
conceptual/mechanical knowledge
spatiotemporal production
modality-specific elicitation
dexterity
```

Therefore:

```text
Apraxia != OneActionDeficit
```

---

# 34. Gesture imitation is not general action competence

Some apraxic patients show severe gesture imitation deficits yet relatively intact
visually guided goal-directed movements.

Thus:

```text
GestureImitation != GoalDirectedExecution
```

---

# 35. Visual guidance can compensate for other control deficits

Better visually guided than no-vision performance can reflect altered sensory
weighting/control rather than intact internal motor representation.

Thus:

```text
GoodPerformanceWithVision != IntactUnaidedControl
```

---

# 36. Motor abundance

The body has many degrees of freedom and many joint/muscle configurations can
achieve equivalent task variables.

HF11 calls this:

```text
MotorAbundance
```

rather than assuming one canonical trajectory.

---

# 37. Same goal does not imply same movement

Pointing/walking experiments show large variability along goal-equivalent
dimensions while stabilizing task-relevant variables.

Thus:

```text
SameActionGoal != SameMovementTrajectory
```

---

# 38. Same outcome does not imply same coordination

Different joint/limb force combinations can produce similar endpoint outcomes.

Thus:

```text
SameTaskOutcome != SameCoordinationPattern
```

---

# 39. Variability is not noise by definition

Some variability lies in dimensions that leave goal outcome unchanged.

Therefore:

```text
MovementVariability != Noise
```

---

# 40. Functional variability can be useful

Goal-equivalent variability can permit robustness and flexibility under changing
constraints.

Thus:

```text
ZeroVariability != PerfectControl
```

---

# 41. More variability is not always good

Variability that changes task-relevant outcomes can be harmful.

Therefore:

```text
MoreMotorVariability != BetterFlexibility by definition
```

---

# 42. Coordination quality is structured variability

A useful profile separates:

```text
goal-equivalent variability
non-goal-equivalent variability
stability under perturbation
adaptability
```

rather than total variance alone.

---

# 43. Motor equivalence

HF11 retains:

```text
MotorEquivalence
= multiple control/movement realizations producing sufficiently equivalent
  task-level effects
```

---

# 44. Motor equivalence prevents trajectory ontology

A motor action cannot be defined solely by one nominal kinematic path.

Thus:

```text
ActionType != CanonicalTrajectory
```

---

# 45. Speed–accuracy tradeoff exists in execution

Time pressure can speed motor execution itself, not only upstream evidence
accumulation/choice.

Thus:

```text
SpeedAccuracyTradeoff != DecisionThresholdOnly
```

---

# 46. Faster is not better

Increasing speed often raises endpoint/trajectory error.

Thus:

```text
FasterMovement != BetterExecution
```

---

# 47. Slower is not automatically better

Time constraints, instability, fatigue and moving targets can make excessive delay
harmful.

Thus:

```text
SlowerMovement != BetterExecution by definition
```

---

# 48. Speed–accuracy relation is task/control specific

Use:

```text
SpeedAccuracyProfile_D
```

rather than a universal motor constant.

---

# 49. Feedback has delay

Sensory information arrives after physical events and through noisy channels.

Therefore a pure instantaneous-feedback controller is biologically impossible.

---

# 50. Feedback-only servo is insufficient

Delayed feedback alone can destabilize or limit rapid control.

Thus:

```text
MotorControl != FeedbackOnlyServo
```

---

# 51. Open-loop program is also insufficient

Unexpected target/hand perturbations can trigger rapid online corrections during
movement.

Thus:

```text
MotorControl != FeedforwardOpenLoopProgram
```

---

# 52. Feedforward control

Working definition:

```text
FeedforwardControl
= anticipatory command/policy generation based on current state/model before the
  consequences of the present command are fully sensed
```

---

# 53. Feedback control

```text
FeedbackControl
= ongoing adjustment based on sensed/estimated discrepancy or state during/after
  execution
```

---

# 54. Feedforward and feedback are not mutually exclusive systems

They can adapt jointly and operate in the same movement.

Thus:

```text
Feedforward != Feedback
but
Feedforward ⊕ Feedback can form one control loop
```

---

# 55. Forward models are a major competing model family

Internal predictive models can map command/state to predicted sensory consequences,
helping state estimation and rapid control.

HF11 retains this family.

---

# 56. Forward model is not motor control ontology

Alternative optimal-feedback, dynamical and ecological accounts explain overlapping
phenomena.

Therefore:

```text
ForwardModelTheory != AllMotorControl
```

---

# 57. Optimal feedback control is retained, not canonized

Optimal-feedback-control models explain goal-equivalent variability and selective
correction of task-relevant disturbances.

But evidence/task generalization is incomplete.

Thus:

```text
OptimalFeedbackControl
= major model family
!= foundation ontology
```

---

# 58. Feedback responses are hierarchically heterogeneous

Sensory feedback can generate fast automatic responses and slower context-sensitive
corrections.

Thus:

```text
FeedbackResponse != OneReflexLatency
```

---

# 59. Automatic feedback does not erase voluntary action

A consciously chosen action can contain automatic feedback corrections.

Thus:

```text
AutomaticCorrection != NonVoluntaryAction by definition
```

---

# 60. Online correction can occur without awareness

Visually shifted hand feedback changes reach trajectory even when the shift is not
consciously detected.

Thus:

```text
OnlineMotorCorrection != ConsciousAwareness
```

---

# 61. Online correction is not explicit replanning

Rapid corrections can be too fast/implicit to equate with a new conscious HF10
plan.

Thus:

```text
OnlineCorrection != ExplicitReplanning
```

---

# 62. Modality matters

Visual, proprioceptive, auditory and haptic feedback have different latencies,
precision and relevance.

Thus:

```text
Feedback_D != Feedback_E
```

---

# 63. State estimation

HF11 requires:

```text
EstimatedBodyWorldState_t
```

because the controller acts on incomplete/delayed/noisy sensory information, not
perfect physical state.

---

# 64. Physical state is not estimated state

```text
PhysicalState != EstimatedState
```

just as HF5 internal physical state was not interoceptive representation.

---

# 65. Proprioception is not direct body truth

Proprioceptive estimates can recalibrate under systematic visual discrepancy.

Thus:

```text
ProprioceptiveEstimate != ExactJoint/HandState
```

---

# 66. Motor adaptation can change perception

After visuomotor adaptation, perceived hand location shifts.

Therefore:

```text
MotorAdaptation != MotorCommandChangeOnly
```

---

# 67. Perception–action loop is bidirectional

```text
Perception
→ Control
→ Action
→ Changed sensory evidence
→ Perceptual recalibration
↺
```

not a one-way perception→action pipeline.

---

# 68. Error is qualifier-required

HF11 rejects unqualified:

```text
Error
```

because multiple mismatches drive different processes.

---

# 69. Sensory prediction error

Working family:

```text
SensoryPredictionError
= observed sensory consequence - predicted sensory consequence
```

subject to representation/model details.

---

# 70. Perceptual prediction error

Current work proposes an error over estimated movement/perceptual state rather than
raw visual difference for some implicit adaptation phenomena.

HF11 retains this as a current rival refinement.

---

# 71. Task/performance error

```text
TaskError
= deviation of achieved task outcome from task target/criterion
```

---

# 72. Reward prediction error

```text
RewardPredictionError
= obtained reward/value consequence - predicted reward/value consequence
```

HF4/HF9 reward roles remain distinct.

---

# 73. These errors are not synonyms

```text
Sensory/PerceptualPredictionError != TaskError
TaskError != RewardPredictionError
```

---

# 74. Zero task error can coexist with prediction error

A deliberate aiming strategy can hit the target while the cursor/hand relation still
violates predicted movement consequences.

Thus:

```text
TaskSuccess != ZeroPredictionError
```

---

# 75. Prediction error can exist without utility loss

Unexpected sensory consequences may be corrected even when task reward remains
unchanged.

Thus:

```text
PredictionError != RewardLoss
```

---

# 76. Reward error can occur without motor error

A perfectly executed movement can receive unexpectedly low reward because the
environment changes.

Thus:

```text
RewardPredictionError != MotorExecutionError
```

---

# 77. Credit assignment is an action problem

When reward is poor, the Human must infer whether failure came from:

```text
choice
movement execution
world stochasticity
model error
```

Movement-error signals can alter downstream reinforcement learning.

---

# 78. Motor learning is not one error signal

Evidence supports interacting:

```text
prediction-error adaptation
explicit strategy
reinforcement/reward learning
task-error memories
use-dependent plasticity
```

Thus:

```text
MotorLearning != OneErrorSignal
```

---

# 79. Adaptation

In HF11 context:

```text
MotorAdaptation
= history-dependent recalibration of control/state estimation in response to
  systematic perturbation/change in body-world mapping
```

consistent with HF6.

---

# 80. Adaptation is not skill

Adaptation often restores prior performance under a perturbation.

Skill acquisition can expand precision/speed/reliability beyond prior performance
without an imposed perturbation.

Thus:

```text
MotorAdaptation != MotorSkillAcquisition
```

---

# 81. Adaptation is not all learning

```text
MotorLearning
⊃ adaptation
```

but also includes reinforcement, sequence learning, skill, calibration and other
history-dependent changes.

---

# 82. Explicit and implicit are measurement-sensitive

Visuomotor adaptation often contains explicit aiming and implicit recalibration.

But methods do not guarantee clean independent decomposition.

Thus:

```text
ExplicitStrategy + ImplicitRecalibration
!= GuaranteedIndependentAdditiveComponents
```

---

# 83. Explicit awareness is not implicit learning absence

A participant may know a perturbation exists while implicit recalibration still
occurs.

Thus:

```text
ExplicitKnowledge != NoImplicitAdaptation
```

---

# 84. No explicit report is not no strategy

Measurement limitations remain.

Thus:

```text
NoReportedStrategy != NoExplicitContribution
```

without sensitive protocol.

---

# 85. Skill

HF11 uses:

```text
Skill_D
= learned capability for reliably producing high-quality task-relevant effects
  under a class of conditions with characteristic efficiency, variability,
  robustness and control demands
```

---

# 86. Skill is not current performance

A single trial is insufficient.

Thus:

```text
CurrentPerformance != Skill
```

---

# 87. Skill is not action knowledge

Knowing what to do does not imply being able to do it.

Thus:

```text
ActionKnowledge != Skill
```

---

# 88. Skill is not explicit procedural description

A skilled pianist/surgeon can outperform their ability to verbally describe all
control details.

Thus:

```text
Skill != ExplicitProcedureKnowledge
```

---

# 89. Skill is not habit

A skill is an execution capability.

A habit-like controller is a policy/control mode from HF4/HF10.

Thus:

```text
Skill != Habit
```

---

# 90. Habit can use skill

A habitually selected action can still require high motor skill.

Thus:

```text
HabitSelection
can invoke
SkilledExecution
```

---

# 91. Goal-directed action can also be highly skilled

Skill does not imply habitual choice.

Thus:

```text
Skill != OutcomeInsensitiveControl
```

---

# 92. Skill is multidimensional

At minimum:

```text
accuracy
speed
variability
efficiency
robustness
adaptability
retention
transfer
feedback dependence
attention dependence
```

must not collapse to one score.

---

# 93. Skill performance and learning are distinct

Training manipulation can improve immediate performance without durable retention,
or improve retention/transfer without best acquisition score.

Thus:

```text
AcquisitionPerformance != Learning
```

---

# 94. Retention is not transfer

A skill can persist on the trained task without generalizing.

Thus:

```text
SkillRetention != SkillTransfer
```

---

# 95. Speed improvement can hide accuracy decline

Thus skill studies should preserve speed–accuracy functions.

```text
FasterAfterPractice != BetterSkill by itself
```

---

# 96. Automaticity

HF11 uses:

```text
Automaticity_D
= reduced dependence on explicit attention/executive control for stable execution
  under a declared task/dual-task context
```

---

# 97. Automaticity is not skill

A skill can remain attention-demanding.

Thus:

```text
Automaticity != Skill
```

---

# 98. Practice is not automaticity guarantee

Current 2026 sequence data show strong learning can coexist with persistent or
increased sequence-specific dual-task costs.

Thus:

```text
Practice != AutomaticityGuarantee
```

---

# 99. Automaticity is not no cognition

Reduced executive demand does not mean absence of perception/prediction/control.

Thus:

```text
Automaticity != NoCognitiveProcessing
```

---

# 100. Automaticity is not loss of agency

An automatic skilled movement can still be embedded in a voluntarily selected goal.

Thus:

```text
AutomaticExecution != AgentlessAction
```

---

# 101. Dual-task cost is evidence, not definition of all automaticity

Different secondary tasks create different interference.

Thus:

```text
LowDualTaskCost != UniversalAutomaticityProof
```

---

# 102. Attention focus can alter skill execution

External focus on movement effects often improves performance/learning relative to
internal focus in studied tasks.

But this is not a universal automaticity law.

---

# 103. More feedback is not always better learning

Feedback can help acquisition, retention or transfer differently depending on
schedule/type/control.

Thus:

```text
MoreFeedback != BetterSkillLearning by definition
```

---

# 104. Skill can redistribute feedforward/feedback dependence

Training without online visual feedback can improve feedforward control in some
precision tasks.

Thus:

```text
SkillLearning
can change
ControlArchitecture
```

---

# 105. Affordance

Because the term is historically overloaded, HF11 uses:

```text
Affordance_D(A,E,T)
= an action possibility available to actor/system A in environment E for task/action
  class T given current capabilities and relevant physical/social constraints
```

---

# 106. Affordance is not object feature only

A stair affords stepping for one body/capability and not another.

Thus:

```text
Affordance != ObjectFeatureOnly
```

---

# 107. Affordance is not subjective belief only

Believing a gap is jumpable does not make it physically jumpable.

Thus:

```text
Affordance != SubjectiveBeliefOnly
```

---

# 108. Objective action possibility and perceived affordance differ

Use:

```text
PhysicalActionPossibility
PerceivedAffordance
```

separately.

Thus:

```text
PhysicalPossibility != PerceivedAffordance
```

---

# 109. Perceived affordance is not action choice

A Human can perceive that A is possible and choose B.

Thus:

```text
PerceivedAffordance != SelectedAction
```

---

# 110. Affordance is capability-relative

HF1 capability grammar applies:

```text
Affordance
= Relation(ActorCapability, Environment, Tool, Task)
```

---

# 111. Tool changes affordance without changing bare body

A reacher can access a distant target using a stick.

Thus the relevant system may be:

```text
Human + Tool
```

for that action class.

---

# 112. Person-plus-object affordance

HF11 explicitly allows:

```text
Affordance(HumanToolSystem, E, T)
```

without claiming Human identity merges with tool.

---

# 113. Attunement

Working definition:

```text
Attunement_D
= learning/selecting which perceptual information is informative about a relevant
  affordance/action boundary
```

---

# 114. Calibration

```text
Calibration_D
= scaling perception/action to the actual current relation between capability and
  environmental/task demand
```

---

# 115. Attunement is not calibration

One concerns **which information** is used; the other concerns **how it is scaled**.

Thus:

```text
Attunement != Calibration
```

---

# 116. Calibration is not capability

A person can possess capability but miscalibrate it.

Thus:

```text
Calibration != Capability
```

---

# 117. Calibration can change rapidly

Tool-use studies show Humans recalibrate to changed person-plus-object capabilities
on short timescales.

---

# 118. Accurate affordance perception is not static

Body, fatigue, tool length, terrain and skill changes can move the action boundary.

Thus:

```text
AffordanceBoundary_t1 != AffordanceBoundary_t2
```

---

# 119. Affordance errors can cause execution failure despite good plan

A plan may assume an action is executable when current actor-tool-environment
relation does not afford it.

Thus:

```text
PlanValidity != AffordanceAvailability
```

---

# 120. Tool use

HF11 separates at least:

```text
ToolAvailability
ToolKnowledge
ToolSelection
ToolControlSkill
ToolControlIntegration
ToolEffect
```

---

# 121. Tool knowledge is not tool skill

Knowing how a hammer works does not imply skilled hammering.

Thus:

```text
ToolKnowledge != ToolSkill
```

---

# 122. Tool selection is not tool execution

HF10 may select the right tool while HF11 execution still fails.

Thus:

```text
ToolSelection != ToolExecution
```

---

# 123. Tool changes effective capability

```text
BareHumanCapability_D
!= HumanToolSystemCapability_D
```

when tool is functional and controlled.

---

# 124. Tool integration is dimension-specific

HF1 Extension vector remains:

```text
ControlIntegration
CapabilityIntegration
BodyRepresentationIntegration
OwnershipIntegration
BiologicalParthood
PersonalIdentityIntegration
```

These are not one variable.

---

# 125. Tool can change body schema

Repeated tool use can alter action-related body representations/kinematics.

Therefore:

```text
ToolUse → possible BodySchemaChange
```

---

# 126. Body-schema change is not biological incorporation

Thus:

```text
BodySchemaExtension != BiologicalParthood
```

---

# 127. Body-schema change is not personal-identity extension

Thus:

```text
BodySchemaExtension != PersonalIdentityExtension
```

---

# 128. Peripersonal/reachable-space change is not body-schema change by definition

Different tool-use paradigms can alter distinct spatial/body representations.

Thus:

```text
ReachableSpaceChange != BodySchemaChange by definition
```

---

# 129. Tool use is not distributed cognition by definition

A distributed-system description can be useful, but some tasks may remain well
explained by Human control of external instrument.

Thus:

```text
ToolUse != ExtendedMind by definition
```

---

# 130. Tool can enter effective control loop

A controlled tool may function as an extended effector in the task-level control
system.

Use:

```text
EffectiveEffectorSet_D(H,T)
```

from HF1/HF11.

---

# 131. Effective effector is not biological limb

Thus:

```text
EffectiveEffector != BiologicalLimb
```

---

# 132. Control integration is reversible

Put down the tool and the effective effector set changes.

Therefore:

```text
ControlIntegration_t
```

is context/time indexed.

---

# 133. Coordination

HF11 uses:

```text
Coordination_D
= structured coupling among multiple effectors/controllers/actors such that their
  degrees of freedom jointly stabilize or produce task-relevant effects
```

---

# 134. Coordination is not independent performance sum

Two high-performing hands can fail a bimanual task because coupling is wrong.

Thus:

```text
Coordination != Sum(IndependentEffectorPerformance)
```

---

# 135. More coupling is not always better

Some bimanual patterns require independence/differentiation.

Thus:

```text
MoreCoupling != BetterCoordination
```

---

# 136. Coordination is task-relative

The desired coupling pattern depends on task goal.

Use:

```text
Coordination_D(T)
```

---

# 137. Intrapersonal coordination

Includes:

```text
joints
muscles
limbs
eye-hand
posture-reaching
```

within one organism/control hierarchy.

---

# 138. Bimanual coordination is learned/plastic

Interhemispheric/functional coupling changes with task learning and injury.

Thus coordination architecture can be a learned capability.

---

# 139. Coordination is not synchrony

Two effectors can be coordinated with deliberate phase offset/asymmetry.

Thus:

```text
Coordination != Synchrony
```

---

# 140. Synchrony is one coordination surface

Rhythmic timing tasks can use phase/tempo synchrony as an operational measure, not
the definition of coordination.

---

# 141. Interpersonal coordination

When another person participates, each controller has independent sensing, goals,
uncertainty and control authority.

This is materially different from bimanual coordination.

---

# 142. Interpersonal coordination is not parallel action

Two people acting next to one another need not be jointly coordinating.

Thus:

```text
JointAction != ParallelIndividualActions
```

---

# 143. Shared goal can change motor control

A shared task goal can alter how each participant plans/predicts/adapts movement.

Thus social relation enters execution, not only post-hoc interpretation.

---

# 144. Communication can be a control signal

Partners can coordinate by:

```text
speech
gesture
movement exaggeration/predictability
implicit action cues
```

Thus:

```text
Communication can be ActionControlResource
```

---

# 145. Predictability can substitute for explicit communication

When speech/conventional signaling is unavailable, people can make actions more
predictable to aid coordination.

Thus:

```text
CoordinationChannel_D != CoordinationChannel_E
```

and channels can trade off.

---

# 146. Coordination is not shared representation by definition

Dynamical coupling can produce spontaneous synchrony with minimal explicit shared
goal representation.

Thus:

```text
BehavioralCoordination != ExplicitSharedRepresentation by definition
```

---

# 147. Joint action is not spontaneous synchrony

Conversely, a shared cooperative goal can exist without rhythmic synchrony.

Thus:

```text
JointAction != SpontaneousSynchrony
```

---

# 148. Joint action exposes another ontology layer

With another independent agent, one must model:

```text
partner goal
partner knowledge
partner action capability
role
communication
mutual prediction
```

Sensorimotor coordination alone is insufficient.

This becomes HF11's strongest residual.

---

# 149. Sense of agency

HF2/HF3/HF1 distinctions remain.

HF11 uses:

```text
SenseOfAgency
= experience/evidence that one's action/control contributed to an effect
```

without equating it to causal truth.

---

# 150. Sense of agency is not motor success

A task can succeed through automation/partner action while Human agency experience
is weak.

Thus:

```text
SenseOfAgency != MotorControlSuccess
```

---

# 151. Sense of agency is not causal responsibility

Subjective control experience can be wrong.

Thus:

```text
SenseOfAgency != CausalResponsibility
```

---

# 152. Prediction-match contributes but does not define agency

Action-effect prediction and feedback congruence are important evidence/mechanism
components.

But retrospective inference, context and partner contribution matter too.

Thus:

```text
PredictionMatch != SenseOfAgency definition
```

---

# 153. Joint agency can have individual and collective surfaces

During cooperative action:

```text
I did my part
We did it
Partner did it
```

can be distinct experiences/judgments.

Thus:

```text
IndividualAgencyExperience != CollectiveAgencyExperience
```

---

# 154. Teleoperation

HF11 treats teleoperation as a powerful execution falsifier because command,
physical effect and sensory feedback are spatially separated and delayed.

---

# 155. Remote command is not immediate effect

```text
HumanCommand_t
→ network/interface delay
→ robot/controller
→ remote movement
→ feedback delay
→ Human observation
```

Thus:

```text
RemoteCommand != ImmediateEffect
```

---

# 156. Latency is a control variable

Delay changes achievable speed, accuracy, stability and strategy.

Thus:

```text
Latency != NetworkNuisanceOnly
```

---

# 157. Latency can change strategy

At high delays, operators may adopt move-and-pause behavior to preserve accuracy.

Therefore:

```text
SameGoal + DifferentLatency
→ DifferentControlPolicy
```

---

# 158. Delay has direction/channel structure

Separate:

```text
command latency
visual feedback latency
haptic feedback latency
audio latency
jitter
packet loss/bandwidth
```

rather than one `ping` scalar.

---

# 159. Real-time haptics can partially compensate delayed visual control

Current teleoperation experiments show channel-specific latency matters.

Thus:

```text
FeedbackLatency_D != FeedbackLatency_E
```

---

# 160. More feedback is not always better teleoperation

Noisy/delayed feedback can destabilize/confuse.

Thus:

```text
MoreFeedback != BetterRemoteControl
```

---

# 161. Haptic feedback is not direct touch

The interface maps remote sensor state to local force/tactile display.

Thus:

```text
HapticFeedback != UnmediatedRemoteTouch
```

---

# 162. Teleoperation expertise matters

Experienced operators can adapt control strategies under delay better than novices.

Thus:

```text
TeleoperationCapability != InterfaceCapabilityOnly
```

---

# 163. Teleoperation expands effective action space

A Human can causally affect remote environment without biological-body movement at
that location.

HF1 control/causal extension therefore applies strongly.

---

# 164. Remote control extension is not bodily extension

```text
Causal/ControlExtension != BiologicalParthood
```

again.

---

# 165. Shared control

Human–robot shared control divides control contributions across layers.

Examples:

```text
Human chooses goal/trajectory region
robot stabilizes precise motion
Human tactical override
robot executes low-level servo
```

---

# 166. Shared control is not exclusive human control

Thus:

```text
SharedControl != HumanOnlyControl
```

---

# 167. Shared control is not exclusive machine control

The Human may still specify/alter goals or override.

Thus:

```text
SharedControl != MachineOnlyControl
```

---

# 168. Control allocation is typed

At least:

```text
GoalAuthority
ActionSelectionAuthority
TrajectoryControl
LowLevelStabilization
Monitoring
Override
Termination
```

may be assigned separately.

---

# 169. Human-in-the-loop is not meaningful control

A Human who cannot understand, observe, intervene in time or alter outcome may be
nominally present but operationally ineffective.

Thus:

```text
HumanInLoop != MeaningfulControlByDefinition
```

---

# 170. Override right is not override capability

A button or policy permission is insufficient if:

```text
Human cannot detect problem
latency too high
system acts too fast
interface inaccessible
```

Therefore:

```text
OverrideRight != EffectiveOverrideCapability
```

---

# 171. Override capability is not override policy

Even with effective control surface, Human must know when to intervene.

Thus:

```text
OverrideCapability != OverridePolicy
```

retaining HF10.

---

# 172. Automation can change task from execution to supervision

Human motor/control workload may shift from continuous manipulation to anomaly
monitoring and intermittent intervention.

Thus:

```text
Automation != WorkElimination
```

it can transform control role.

---

# 173. Supervision is not teaming

Supervisory architectures and cooperative shared-control/team architectures have
different information/control assumptions.

Thus:

```text
Supervision != Teaming
```

---

# 174. Goal command is not full action specification

Agentic systems can receive high-level:

```text
Achieve G
```

and generate lower-level actions themselves.

Thus:

```text
GoalCommand != CompleteActionSpecification
```

---

# 175. Delegated execution

HF10 defined delegation role assignment.

HF11 adds actual realized action by delegate.

---

# 176. Delegated execution is not delegated responsibility

A machine may physically execute while Human/institution retains responsibility.

Thus:

```text
DelegatedExecution != DelegatedResponsibility
```

---

# 177. Delegated execution is not authority transfer

Execution authority can remain bounded by Human-approved policy/permissions.

Thus:

```text
DelegatedExecution != FullAuthorityTransfer
```

---

# 178. Autonomous low-level action can coexist with Human high-level authority

This is common in control systems and AI agents.

Therefore autonomy is dimension/level-specific.

---

# 179. Machine autonomy is not Human absence

A Human can remain:

```text
principal
authorizer
monitor
interruptor
accountable party
```

without controlling every low-level action.

---

# 180. Human presence is not control

Conversely, nominal oversight can be practically ineffective.

Thus:

```text
HumanPresence != HumanControl
```

---

# 181. Executed effect must be attributed by causal chain

For Human×AI systems, distinguish:

```text
GoalSetter
OptionGenerator
DecisionMaker
Authorizer
Executor
LowLevelController
Monitor
Overrider
PhysicalEffectSource
ResponsiblePerson/Institution
```

rather than one `agent did X` field.

---

# 182. Tool and AI execution share structural similarities

Both can extend:

```text
causal reach
precision
speed
scale
```

but AI can additionally generate/select sub-actions, making agency/control extension
more than effector extension.

---

# 183. Tool extension and agent delegation differ

A hammer generally lacks independent goal modeling.

An AI agent may choose subgoals/actions.

Thus:

```text
ToolMediation != AgentDelegation
```

---

# 184. The autonomy dimension matters

HF1 Agent definition becomes relevant:

```text
Tool-like executor
↔ adaptive controller
↔ delegated agent
```

should not be flattened.

---

# 185. Execution Profile

HF11 proposes:

```text
ExecutionProfile_D = {
  action goal,
  selected action,
  preparation state,
  initiation latency,
  control policy,
  effectors/tools,
  movement trajectory,
  state estimates,
  feedforward contribution,
  feedback channels/latencies,
  online corrections,
  error types,
  task outcome,
  reward consequence,
  sense of agency,
  interruptions/recovery
}
```

---

# 186. ActionControlProfile

```text
ActionControlProfile_D = {
  controlled task variables,
  motor abundance / degrees of freedom,
  goal-equivalent variability,
  non-goal-equivalent variability,
  predictive model assumptions,
  feedback policy,
  sensory weighting,
  speed–accuracy relation,
  robustness to perturbation,
  adaptation history
}
```

---

# 187. SkillProfile

```text
SkillProfile_D = {
  task class,
  accuracy,
  speed,
  variability,
  efficiency,
  robustness,
  adaptability,
  retention,
  transfer,
  feedforward/feedback dependence,
  attention/dual-task dependence,
  tool dependence,
  calibration state
}
```

---

# 188. AffordanceProfile

```text
AffordanceProfile_D(A,E,T) = {
  physical action possibility,
  actor capability,
  tool/person-plus-object capability,
  perceived affordance,
  attuned information,
  calibration,
  uncertainty,
  selected action,
  success/failure boundary
}
```

---

# 189. ToolControlProfile

```text
ToolControlProfile_D = {
  tool availability,
  tool knowledge,
  tool skill,
  control mapping,
  effective effector set,
  body-schema effects,
  reachable-space effects,
  feedback channels,
  calibration,
  reversibility,
  failure modes
}
```

---

# 190. CoordinationProfile

```text
CoordinationProfile_D = {
  participants/effectors,
  task goal,
  coupling structure,
  timing relation,
  role/asymmetry,
  shared versus separate information,
  communication channels,
  prediction/adaptation,
  joint outcome,
  individual contributions,
  individual/collective agency evidence
}
```

---

# 191. TeleoperationProfile

```text
TeleoperationProfile_D = {
  command channel,
  command latency/jitter,
  remote controller,
  physical actuator,
  visual latency,
  haptic latency,
  bandwidth/loss,
  predictive display/control,
  Human skill,
  control strategy,
  task accuracy/speed,
  override,
  interruption/recovery
}
```

---

# 192. HumanAIExecutionProfile

```text
HumanAIExecutionProfile_D = {
  goal setter,
  planning actor,
  decision authority,
  authorization scope,
  delegated action scope,
  autonomous subgoal generation,
  executor,
  control latency,
  feedback/observability,
  monitor,
  override capability,
  override policy,
  termination authority,
  realized effect,
  causal contribution,
  responsibility assignment
}
```

---

# 193. Cross-context falsifier matrix

| Case | Naive collapse attacked | HF11 surviving distinction |
|---|---|---|
| ideomotor effect after action-effect learning | action = movement | anticipated effects can organize action |
| rapid remapping of action-effect relation | ideomotor = fixed association | causal/propositional rivals remain |
| prepared movement released by startle | preparation = initiation | motor preparation and release separate |
| Parkinson freezing despite goal to walk | intention = initiation | initiation is a control transition |
| apraxia with preserved tool knowledge | knowing = doing | conceptual action knowledge != production |
| gesture imitation impaired but visually guided reach preserved | praxis one faculty | modality/task control can dissociate |
| many joint patterns preserve endpoint | variability = noise | goal-equivalent abundance is functional |
| motor execution speeds under response urgency | SAT = decision only | motor process contributes |
| shifted hand feedback corrected without awareness | control = conscious | online corrections can be nonconscious |
| proprioception shifts after visuomotor adaptation | adaptation = motor command only | sensory estimate recalibrates |
| task success with residual prediction mismatch | task error = prediction error | error signals are typed |
| reward changes without movement error | motor error = reward error | reward prediction is separate |
| explicit + implicit adaptation nonadditivity | learning = independent modules | mechanisms interact/measurement matters |
| skilled learning without perturbation | skill = adaptation | skill acquisition broader |
| strong practice with persistent dual-task cost | practice = automaticity | automaticity is a separate profile |
| tool changes reach/action representation | tool external only | tool can enter effective control loop |
| body-schema change after tool use | tool = body | representation extension != biological parthood |
| person-plus-object recalibration | affordance = object feature | affordance is actor/tool/environment relation |
| two good limbs fail coupled task | coordination = individual ability sum | coupling architecture matters |
| partners coordinate via predictable movement when speech absent | communication = words only | action itself can signal/control partner |
| joint goal without synchrony | joint action = synchrony | shared task relation is distinct |
| remote control worsens with latency | command = action | command/effect/feedback are temporally separated |
| move-and-pause emerges under delay | latency = nuisance | delay changes control strategy |
| real-time haptics mitigates visual delay | feedback one channel | modality-specific feedback matters |
| robot autonomous precision + Human override | control exclusive | shared control is layered |
| Human nominally in loop but unable to intervene | presence = control | meaningful control requires effective intervention |
| high-level AI goal produces lower-level acts | command = specification | agent can generate execution policy |
| AI executes unethical delegated goal | executor = responsibility holder | execution and responsibility differ |

---

# 194. Competing action/control models

## M1 — command→movement pipeline

### Claim

Selected action produces a motor command that generates one intended trajectory.

### Failure

Motor abundance, online correction, sensory recalibration and environmental
perturbation.

**Disposition:** reject as complete ontology.

## M2 — ideomotor action-effect control

### Strength

Explains learned effect-based action selection and effect anticipation.

### Failure

Associative mechanism is not uniquely identified; not all low-level control reduces
to effect representation.

**Disposition:** retain major cognitive action-control family.

## M3 — stored motor program / feedforward execution

### Strength

Explains prepared/rapid skilled sequences and initiation phenomena.

### Failure

Online perturbation correction and variable trajectories require dynamic feedback/
state estimation.

**Disposition:** retain preparatory/feedforward components, reject open-loop totality.

## M4 — feedback servo

### Strength

Explains error correction.

### Failure

Sensory delay/noise and fast movement require prediction/feedforward.

**Disposition:** reject feedback-only account.

## M5 — forward/internal model

### Strength

Explains prediction, state estimation and adaptation.

### Failure

Not all skill/coordination/affordance phenomena require one explicit internal model;
model implementation remains theory-level.

**Disposition:** retain major model family.

## M6 — optimal feedback control

### Strength

Explains task-relevant correction and goal-equivalent variability.

### Failure

Task generalization/implementation are not universally settled.

**Disposition:** retain major model family.

## M7 — ecological/affordance control

### Strength

Explains actor-environment capability relation, attunement and calibration without
requiring exhaustive internal trajectory representation.

### Failure

`Affordance` is heavily overloaded and does not alone explain action-effect learning,
explicit planning or all neural adaptation evidence.

**Disposition:** retain relational affordance layer.

## M8 — one-error motor learning

### Failure

Prediction, task and reward errors plus explicit strategy interact/dissociate.

**Disposition:** reject.

## M9 — skill as automatized habit

### Failure

Skill can remain goal-directed/attention-demanding; practice does not guarantee
automaticity.

**Disposition:** reject.

## M10 — tool incorporation as literal body extension

### Failure

Body schema, reachable space, control integration, ownership and biological parthood
can dissociate.

**Disposition:** use HF1 Extension_D vector, not literal incorporation claim.

## M11 — independent-controller coordination

### Failure

Bimanual/interpersonal coupling creates task-level synergies and shared constraints.

**Disposition:** reject additive-controller model.

## M12 — Human-in-loop control

### Failure

Nominal presence does not establish observability, intervention latency, override
capability or authority.

**Disposition:** replace with typed control/authority architecture.

---

# 195. HF11 anti-laws

## Action / initiation

1. `Action != Choice`.
2. `Action != Intention`.
3. `Action != Movement`.
4. `Movement != TaskOutcome`.
5. `TaskOutcome != RewardOutcome`.
6. `ActionGoal != MotorCommand`.
7. `MotorCommand != MovementTrajectory`.
8. `MovementTrajectory != ActionIdentity`.
9. `VoluntaryAction != ConsciousControlOfEveryCorrection`.
10. `ActionEffectRepresentation != Action`.
11. `IdeomotorEffect != UniqueAssociativeMechanismProof`.
12. `GoalRepresentation != MovementRepresentation`.
13. `ActionControl != IdeomotorControlOnly`.
14. `Intention != MotorPreparation`.
15. `MotorPreparation != Initiation`.
16. `Commitment != Initiation`.
17. `Initiation != Continuation`.
18. `MovementInitiation != SenseOfVolition`.
19. `ReadinessPotential != Intention`.
20. `InitiationFailure != GoalAbsence`.

## Praxis / motor abundance

21. `ActionKnowledge != SkilledActionExecution`.
22. `Strength != PraxisCapability`.
23. `Apraxia != OneActionDeficit`.
24. `GestureImitation != GoalDirectedExecution`.
25. `GoodPerformanceWithVision != IntactUnaidedControl`.
26. `SameActionGoal != SameMovementTrajectory`.
27. `SameTaskOutcome != SameCoordinationPattern`.
28. `MovementVariability != Noise`.
29. `ZeroVariability != PerfectControl`.
30. `MoreMotorVariability != BetterFlexibility`.
31. `ActionType != CanonicalTrajectory`.

## Control / feedback

32. `SpeedAccuracyTradeoff != DecisionThresholdOnly`.
33. `FasterMovement != BetterExecution`.
34. `SlowerMovement != BetterExecution by definition`.
35. `MotorControl != FeedbackOnlyServo`.
36. `MotorControl != FeedforwardOpenLoopProgram`.
37. `Feedforward != Feedback`.
38. `ForwardModelTheory != AllMotorControl`.
39. `OptimalFeedbackControl != foundation ontology`.
40. `FeedbackResponse != OneReflexLatency`.
41. `AutomaticCorrection != NonVoluntaryAction by definition`.
42. `OnlineMotorCorrection != ConsciousAwareness`.
43. `OnlineCorrection != ExplicitReplanning`.
44. `Feedback_D != Feedback_E`.
45. `PhysicalState != EstimatedState`.
46. `ProprioceptiveEstimate != ExactBodyState`.

## Error / learning

47. `MotorAdaptation != MotorCommandChangeOnly`.
48. `Sensory/PerceptualPredictionError != TaskError`.
49. `TaskError != RewardPredictionError`.
50. `TaskSuccess != ZeroPredictionError`.
51. `PredictionError != RewardLoss`.
52. `RewardPredictionError != MotorExecutionError`.
53. `MotorLearning != OneErrorSignal`.
54. `MotorAdaptation != MotorSkillAcquisition`.
55. `ExplicitStrategy + ImplicitRecalibration != GuaranteedIndependentAdditivity`.
56. `ExplicitKnowledge != NoImplicitAdaptation`.
57. `NoReportedStrategy != NoExplicitContribution`.

## Skill / automaticity

58. `CurrentPerformance != Skill`.
59. `ActionKnowledge != Skill`.
60. `Skill != ExplicitProcedureKnowledge`.
61. `Skill != Habit`.
62. `Skill != OutcomeInsensitiveControl`.
63. `AcquisitionPerformance != Learning`.
64. `SkillRetention != SkillTransfer`.
65. `FasterAfterPractice != BetterSkill by itself`.
66. `Automaticity != Skill`.
67. `Practice != AutomaticityGuarantee`.
68. `Automaticity != NoCognitiveProcessing`.
69. `AutomaticExecution != AgentlessAction`.
70. `LowDualTaskCost != UniversalAutomaticityProof`.
71. `MoreFeedback != BetterSkillLearning by definition`.

## Affordance / tool

72. `Affordance != ObjectFeatureOnly`.
73. `Affordance != SubjectiveBeliefOnly`.
74. `PhysicalPossibility != PerceivedAffordance`.
75. `PerceivedAffordance != SelectedAction`.
76. `Attunement != Calibration`.
77. `Calibration != Capability`.
78. `PlanValidity != AffordanceAvailability`.
79. `ToolKnowledge != ToolSkill`.
80. `ToolSelection != ToolExecution`.
81. `BareHumanCapability_D != HumanToolSystemCapability_D`.
82. `BodySchemaExtension != BiologicalParthood`.
83. `BodySchemaExtension != PersonalIdentityExtension`.
84. `ReachableSpaceChange != BodySchemaChange by definition`.
85. `ToolUse != ExtendedMind by definition`.
86. `EffectiveEffector != BiologicalLimb`.

## Coordination

87. `Coordination != Sum(IndependentEffectorPerformance)`.
88. `MoreCoupling != BetterCoordination`.
89. `Coordination != Synchrony`.
90. `JointAction != ParallelIndividualActions`.
91. `BehavioralCoordination != ExplicitSharedRepresentation by definition`.
92. `JointAction != SpontaneousSynchrony`.
93. `SenseOfAgency != MotorControlSuccess`.
94. `SenseOfAgency != CausalResponsibility`.
95. `IndividualAgencyExperience != CollectiveAgencyExperience`.

## Teleoperation / AI

96. `RemoteCommand != ImmediateEffect`.
97. `Latency != NetworkNuisanceOnly`.
98. `MoreFeedback != BetterRemoteControl`.
99. `HapticFeedback != UnmediatedRemoteTouch`.
100. `TeleoperationCapability != InterfaceCapabilityOnly`.
101. `SharedControl != HumanOnlyControl`.
102. `SharedControl != MachineOnlyControl`.
103. `HumanInLoop != MeaningfulControlByDefinition`.
104. `OverrideRight != EffectiveOverrideCapability`.
105. `OverrideCapability != OverridePolicy`.
106. `Automation != WorkElimination`.
107. `Supervision != Teaming`.
108. `GoalCommand != CompleteActionSpecification`.
109. `DelegatedExecution != DelegatedResponsibility`.
110. `DelegatedExecution != FullAuthorityTransfer`.
111. `MachineAutonomy != HumanAuthorityAbsence`.
112. `HumanPresence != HumanControl`.
113. `ToolMediation != AgentDelegation`.

---

# 196. Minimum HF11 grammar

```text
Goal / Selected Policy / Plan
        ↓
Action Goal / Intended Effect
        ↓
Action Selection
        ↓
Motor Preparation
        ↓
Initiation / Release
        ↓
Control Policy / Commands
   ↙ predictive/feedforward       ↘
Estimated Body/World State ← Sensory Feedback
        ↓                         ↑
Effector / Tool / Robot Movement
        ↓
Task / Environmental Effect
        ↓
Reward / Consequence
        ↓
Error Signals
  ├─ sensory/perceptual prediction
  ├─ task/performance
  └─ reward prediction
        ↓
Online correction + adaptation + learning
        ↺
```

Across longer history:

```text
Repeated execution
→ calibration / adaptation / skill / automaticity
→ changed future action-control architecture
```

---

# 197. Situated capability grammar

HF1 capability can now be expanded:

```text
SituatedActionCapability_D
= Relation(
    Actor,
    Goal,
    BodyState,
    Skill,
    Tool,
    Environment,
    Affordance,
    Feedback,
    Latency,
    Authority,
    Partner/Agent,
    Context
  )
```

Thus:

```text
IntrinsicCapacity != SituatedActionCapability
```

---

# 198. Reconnection to HF10

HF10 outputs:

```text
Choice / Commitment / Plan / Policy
```

HF11 adds:

```text
Initiation / Control / Movement / Outcome
```

Therefore:

```text
DecisionPolicy != ExecutionPolicy
```

and:

```text
PlanSuccess requires Executability + Control
```

---

# 199. Reconnection to HF9

HF9 causal/intervention reasoning can choose informative actions.

HF11 determines whether the intervention is physically realized accurately enough
to support causal inference.

Thus:

```text
InterventionIntent != InterventionFidelity
```

---

# 200. Reconnection to HF8

Action effects depend on world models and representations of body/tool/task.

But representation correctness is not execution skill.

Thus:

```text
WorldModelQuality != MotorControlQuality
```

---

# 201. Reconnection to HF7

Skill/action history is retained through multiple memory/learning systems.

But current retrieval of procedural knowledge is not current execution.

Thus:

```text
ProceduralMemoryEvidence != SkilledExecution
```

---

# 202. Reconnection to HF6

Adaptation, skill and automaticity are forms of history-dependent transition change.

HF11 specifies their execution-level manifestations.

```text
ControlPolicy_t
→ practice/perturbation
→ ControlPolicy_(t+1)
```

---

# 203. Reconnection to HF5

Fatigue, pain, temperature and regulatory state alter capability, calibration,
feedback weighting and execution robustness.

Thus:

```text
SamePlan + DifferentHumanState
→ DifferentExecutability
```

---

# 204. Reconnection to HF4

Goal/value/motivation select and sustain action but do not supply motor skill.

Thus:

```text
Motivation != Skill
GoalCommitment != Initiation
WantingOutcome != CapabilityToProduceOutcome
```

---

# 205. Reconnection to HF3

Attention/WM/control affect movement preparation, skill acquisition and correction,
but skilled feedback control can become partially automatic.

Thus:

```text
Attention != MotorControl
Metacognition != Execution
```

---

# 206. Reconnection to HF2

Sense of agency, effort and control are experiences/evidence channels.

They do not directly equal objective causal contribution or movement fidelity.

---

# 207. Reconnection to HF1

HF11 makes HF1 extension concrete:

```text
Tool/Robot can increase CausalIntegration + CapabilityIntegration + ControlIntegration
without BiologicalParthood or PersonalIdentityIntegration
```

and Human×AI task system remains distinct from HumanIndividual.

---

# 208. What HF11 does not establish

HF11 does not establish:

- one universal definition of action across every scale;
- that ideomotor theory explains all action selection;
- one motor-initiation center;
- readiness potential as a free-will marker;
- that apraxia maps cleanly to one modern component model;
- one unique optimal movement trajectory;
- that all movement variability is functional;
- that speed–accuracy tradeoffs have one mechanism;
- one universal forward model implementation;
- optimal-feedback-control theory as final motor ontology;
- that all online correction is unconscious;
- one universal sensory prediction error representation;
- that 2026 perceptual-prediction-error results settle all adaptation;
- clean additive explicit/implicit motor-learning modules;
- that adaptation is the main form of skill learning;
- one universal operational measure of automaticity;
- that external attentional focus always improves skill;
- one final Gibsonian/cognitive definition of affordance;
- that all tool use changes body schema;
- that body-schema change means tool ownership/incorporation;
- that all coordination requires shared representation;
- that synchrony implies cooperation;
- that haptics always improves teleoperation;
- one universal safe latency threshold across remote-control tasks;
- that Human-in-the-loop guarantees meaningful control;
- that shared control resolves authority/responsibility;
- that machine execution implies machine moral/legal responsibility.

---

# 209. The residual HF11 cannot finish

HF11 can model one actor, one body, one tool or even a tightly coupled controller.

But materially different cases repeatedly break that boundary:

```text
two people carry a sofa
surgeon + assistant coordinate instruments
musicians perform together
Human supervises/teams with autonomous robot
Human and AI negotiate a joint task
```

Each participant has independently evolving:

```text
perception
belief/model
goals/subgoals
attention
capabilities
roles
authority
incentives
communication state
```

Coordination can fail even when every individual's motor control is excellent,
because participants disagree about goal, role, timing, meaning or expectation.

Conversely, communication and shared task structure can make mediocre independent
controllers highly effective together.

This residual is not another sensorimotor-control problem.

It is the emergence of **relations among agents**.

---

# 210. Cross-domain evidence for the residual

Interpersonal coordination studies repeatedly require:

```text
predict partner
signal intent
align timing
represent shared task
allocate roles
adapt to partner
```

Communication can substitute for movement predictability, and action itself can
serve communicative function.

Therefore:

```text
MotorCoordination
is insufficient for
JointAction
```

---

# 211. Shared goal is not identical individual goals

Two agents can each want outcome G yet fail to represent/commit to acting **together**
for G.

Thus:

```text
Goal_A = G and Goal_B = G
!= SharedGoal(A,B,G) by definition
```

---

# 212. Joint action is not synchronized movement

Participants can act asynchronously while jointly pursuing one task.

Thus:

```text
JointAction != Synchrony
```

---

# 213. Communication is not language only

Movement timing, gaze, gesture, environmental manipulation and explicit language can
all alter partner prediction/action.

Thus communication becomes its own foundation boundary.

---

# 214. Role is not movement assignment

A role can encode:

```text
authority
information responsibility
expected action class
monitoring obligation
fallback responsibility
```

beyond one motor subtask.

---

# 215. Cooperation is not coordination

Agents can coordinate successfully while competing; cooperation implies alignment
on some joint outcome/benefit/normative relation beyond mere temporal coupling.

Thus:

```text
Coordination != Cooperation
```

---

# 216. Exact next foundation

HF11 therefore selects:

# HF12 — Social Interaction, Joint Action, Communication, Shared Goals, Roles and Cooperation

HF12 should ask:

1. What is interaction relative to co-presence, influence and reciprocal coupling?
2. What is joint action relative to parallel action and sensorimotor coordination?
3. What is a shared goal relative to identical individual goals?
4. What is joint intention/commitment relative to individual intention?
5. What is communication relative to signaling, information transfer and action?
6. How do explicit language, gesture, gaze and action-based signaling differ?
7. What is common ground/shared representation, and how can it be wrong or partial?
8. What is a role relative to task assignment, authority and responsibility?
9. What is cooperation relative to coordination, competition and prosociality?
10. How do turn-taking, prediction and repair stabilize interaction?
11. How do trust/dependence and uncertainty about another agent alter joint action?
12. How should Human×AI joint action distinguish tool use, delegation, teamwork and
    social interaction?
13. When does a multi-agent system have a joint capability not attributable to any
    individual member?
14. What next boundary emerges after relational multi-agent action is rebuilt?

HF12 should not predefine HF13.

---

# 217. Candidate HF12 falsifiers

- spontaneous synchrony without shared goal;
- shared goal without synchronous movement;
- same individual goal versus genuine joint task commitment;
- coordination through action predictability when speech is unavailable;
- communication reducing the need for behaviorally constrained predictability;
- implicit action-based signaling versus explicit speech/gesture;
- joint action with asymmetric information;
- role switching and dynamic role allocation;
- coordination failure from common-ground mismatch;
- communication repair after misunderstanding;
- cooperative versus competitive coordination with similar movement structure;
- individual versus collective sense of agency;
- Human×AI teaming versus tool use/supervision/delegation;
- joint success despite weak individual capability and joint failure despite strong
  individual capability.

---

# 218. HF11 synthesis

HF11 began with:

```text
A plan exists. How does it become effect?
```

The surviving answer is not `execute(plan)`.

Situated action requires a layered recurrent system:

```text
action goal
selection
preparation
initiation
predictive/feedforward control
feedback/state estimation
motor abundance/coordination
typed error signals
adaptation/skill
affordance calibration
tool mediation
online correction
```

and, in remote/autonomous systems:

```text
latency
shared control
monitoring
override
delegated execution
```

The deepest compressions are:

```text
Action != Movement != Outcome
Intention != Initiation
SameGoal != SameTrajectory
Variability != Noise
MotorControl != FeedforwardOnly != FeedbackOnly
Error != OneScalar
Adaptation != Skill != Automaticity
Affordance != ObjectProperty != SubjectiveBelief
ToolControlIntegration != Biological/PersonalIdentityExtension
HumanInLoop != MeaningfulControl
```

But once another independently modeling agent enters the loop, action execution no
longer reduces to one situated controller.

The next question becomes:

> **How do multiple agents form, communicate, maintain and repair enough shared task
> structure to act together despite distinct beliefs, goals, roles and authority?**

That is the HF12 social interaction/joint-action boundary.
