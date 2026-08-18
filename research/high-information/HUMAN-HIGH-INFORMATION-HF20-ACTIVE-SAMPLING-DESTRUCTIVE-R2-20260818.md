---
schema_version: 1
id: human.high-information.hf20-active-sampling-destructive-r2
profile: research
lifecycle: completed
source_role: research-decision
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
  - engineer
updated: 2026-08-18
summary: Round-2 destructive tournament against the HF20 ActiveSamplingPolicy survivor. The strongest composition rival succeeds: HF20 supplies the action-to-sensory-evidence mapping and distinctions; HOC2 supplies evidence value, verification depth and stopping; HOC5 supplies generic candidate-action allocation and cost tradeoffs; HF11 supplies motor/tool execution and affordance calibration; HOC1/HOC4 supply support/capability and fatigue/cost boundaries. Active sensing remains real and important, but the generic Human-side remainder is composition/routing rather than a unique substantive owner. Human evidence also falsifies `active > passive`: active and passive touch can yield similar task performance; sampling behavior is shaped by time, switch and cognitive-effort costs; and more sampling can be inefficient/oversampling. Human-Agent active-perception systems show the sampling controller can be an Agent/robot policy rather than the Human, so SamplingPolicy is controller-relative rather than a Human trait. PerceptualCalibration splits: affordance/action-boundary calibration is primarily HF11; sensory mapping/recalibration stays HF20; learning/transfer goes HOC3. Round 2 therefore rejects ActiveSamplingPolicy as HOC11 and retains an unnumbered PerceptualSamplingCompositionProtocol for consumers that must connect perceptual targets to sampling actions, evidence value, execution, attribution and stopping. HF20 remains scientifically rich but its generic new-HOC information gain falls sharply. The next information-gain leader becomes HF11 Action / Tool-Integrated Control / Affordance Calibration, without preselecting a new HOC.
evidence_status: verified-synthesis
readiness: COMPLETE
related:
  - human.high-information.hf20-perceptual-sampling-r1
  - human.foundations.hf20
  - human.foundations.hf11
  - human.operational-concepts.hoc2
  - human.operational-concepts.hoc5
---
# Human High-Information Search — HF20 Active Sampling Destructive Round 2

## 0. Starting hypothesis

Round 1 retained:

```text
Perceptual Evidence Acquisition
/ Active Sampling
/ Perceptual Calibration
```

with strongest core:

```text
ActiveSamplingPolicy
```

Round 2 asks whether that core is a Human operational family or a stable composition of already-owned objects.

No HOC numbering is assumed.

---

# 1. Strongest full-composition rival

Construct the decision as:

```text
HF20
→ what sampling action changes what sensory evidence for this perceptual target?

HOC2
→ what additional evidence is worth acquiring?
→ what uncertainty/failure mode is being reduced?
→ when is evidence sufficient?
→ when should sampling stop?

HOC5
→ which candidate action is selected under current goal, effort, delay and opportunity cost?

HF11
→ can the body/tool actually execute the sampling action?
→ what movement/control/affordance boundary applies?

HOC1
→ what support/capability is available?

HOC4
→ what load/fatigue/time burden does continued sampling impose?
```

This composition is materially stronger than the Round-1 reduction attempt.

---

# 2. What HOC2 already owns

HOC2 already reconstructs verification as evidence acquisition rather than ritual checking.

Its canonical questions include:

```text
what evidence would distinguish alternatives?
what independent channel can test the claim?
what discriminative test should be run?
what is the expected value of additional evidence?
when should checking stop?
```

It explicitly freezes:

```text
Continue evidence acquisition only while expected value exceeds relevant cost.
```

Therefore a putative HOC11 cannot be justified merely by:

```text
seek more evidence
choose another sample
stop when enough evidence exists
```

Those are already HOC2-level operations.

---

# 3. What HOC5 already owns

HOC5 already has:

```text
ActionAllocationProfile = {
  active goals,
  candidate actions,
  priorities,
  time allocation,
  attention allocation,
  effort allocation,
  switching,
  external constraints,
  uncertainty
}
```

and explicit stop/override/abandonment logic.

So once HF20 supplies candidate sampling actions and their perceptual consequences, HOC5 can select among them as means.

The generic action-choice layer is not missing.

---

# 4. What HF20 already supplies directly

HF20 itself is unusually operational for a Foundation.

It already distinguishes:

```text
TaskAction
SamplingAction
CalibrationAction
ReportAction
```

and defines:

```text
ActiveSensing
= action that materially changes the distribution, quality, location or timing
  of sensory evidence acquired for a perceptual task.
```

It also gives the core loop:

```text
SamplingAction_t
→ SensoryEvidence_{t+1}
→ PerceptualUpdate_{t+1}
→ SamplingAction_{t+1}
```

and the endogenous-policy relation:

```text
SamplingPolicy_t
= f(goal, uncertainty, attention, history, body constraints, cost, expected information)
```

This is not merely ontology; it already specifies the missing perceptual coupling semantics.

That weakens the case for duplicating it as an HOC family.

---

# 5. Full reconstruction without a new family

A practical consumer can build:

```text
PerceptualSamplingDecision = {
  perceptual target,                     # HF20
  current perceptual evidence,           # HF20
  current perceptual uncertainty,        # HF20
  rival perceptual hypotheses/needs,     # HF20/HOC2
  candidate sampling actions,            # HF20
  predicted evidence consequence,        # HF20
  verification value/error asymmetry,    # HOC2
  stopping threshold/criterion,          # HOC2
  action cost/effort/delay,               # HOC5/HOC4
  executable body/tool constraints,      # HF11/HOC1
  selected sampling action,              # HOC5
  realized execution,                    # HF11
  observed evidence update,              # HF20
  attribution/support regime,            # HOC1/HOC3
  uncertainty
}
```

No unique Human-side variable is left unexplained.

---

# 6. The substantive actions are not uniquely owned by the candidate

Round 1 listed:

```text
LOOK
SACCADE
FIXATE
MOVE_HEAD
MOVE_BODY
CHANGE_VIEWPOINT
APPROACH
TOUCH
PRESS
STROKE
LIFT
TRACE
REORIENT
CHANGE_MODALITY
USE_ASSISTIVE_CHANNEL
REPEAT_SAMPLE
STOP_SAMPLING
```

These are real actions.

But their ownership decomposes:

```text
why this sensory action is useful
→ HF20

whether more evidence is worth its cost
→ HOC2

which means/action to choose now
→ HOC5

how body/tool executes it
→ HF11
```

The existence of a recurring action list does not by itself prove a new owner.

---

# 7. `Active > Passive` is directly falsified

HF20 already warns:

```text
ActiveSensing != ActiveAlwaysBetter
```

Human touch evidence strengthens this.

In a controlled roughness-categorization experiment, active exploration and passive surface movement produced no task-performance difference even though neural activation patterns differed.

Therefore:

```text
ActiveMovementOccurred
!= PerceptualBenefit
```

and:

```text
ActiveSensingBenefit
is target/procedure/context dependent.
```

This is exactly what the composition rival predicts.

---

# 8. Sampling has explicit and cognitive cost

Human active-information-sampling research shows sampling policy responds to:

```text
sample cost
switching cost
time pressure
cognitive effort
fatigue
uncertainty
reward/error stakes
```

A Nature Human Behaviour series found that active information sampling exhibits a speed–efficiency tradeoff and that adding cognitive-effort cost improves explanation of Human sampling behavior; effort cost was related to accumulated fatigue.

Other perceptual-motor sampling experiments show Humans can over-sample under some explicit cost regimes.

Therefore:

```text
MoreSamples != BetterPolicy
```

and:

```text
InformationGainMaximization
!= HumanSamplingObjectiveByDefinition
```

These costs are already representable by HOC2/HOC4/HOC5.

---

# 9. Control over stopping can matter without creating a new Human family

Human evidence also shows that having control over *when to stop* information sampling can improve choice accuracy and evidence processing in some tasks, while control over which alternatives to sample alone did not produce the same effects in that experiment.

This is important, but it maps naturally to:

```text
HOC2 stopping / evidence sufficiency
+ HOC5 action control
```

rather than requiring one new perceptual owner.

---

# 10. Human-Agent falsifier — the sampling controller need not be Human

Modern active-perception robotic systems make the ownership problem explicit.

A robot can learn:

```text
search
track
focus
change viewpoint
move camera/neck
```

as a policy while the Human merely provides demonstrations or receives resulting observations.

Therefore:

```text
SamplingPolicy
!= HumanProperty
```

The correct type is:

```text
SamplingController ∈ {
  Human,
  Agent,
  Interface,
  JointHumanAgentSystem
}
```

and:

```text
AgentSelectedView
!= HumanActiveSampling
```

This is a strong category test against HOC11.

---

# 11. Human demonstration does not transfer ownership

If a robot learns gaze/search behavior from Human demonstrations:

```text
HumanDemonstratedSamplingPolicy
→ learned AgentSamplingPolicy
```

but:

```text
LearnedFromHuman
!= CurrentlyOwnedByHuman
```

Likewise, if an Agent chooses camera views and the Human judges the result:

```text
HumanPerceptualDecision
can depend on
AgentSamplingPolicy
```

without the Human possessing or executing that sampling policy.

This makes controller attribution mandatory.

---

# 12. Sensory-substitution evidence remains valuable but does not restore HOC status

The 2025 sensory-substitution study remains a strong demonstration that exploration strategy matters.

But its decomposition is:

```text
interface/transduction mapping
→ Media/Interface

which exploration action changes useful evidence
→ HF20

whether/when to seek evidence
→ HOC2

action choice
→ HOC5

hand/tool execution
→ HF11

learning/transfer
→ HOC3

support attribution
→ HOC1
```

Thus:

```text
StrategyMatters
!= NewHumanOwner
```

---

# 13. Head-movement localization remains a pressure case, not family proof

The 2025 single-sided-deafness study showed that head movement improved localization accuracy, with greater improvement in the SSD group for some conditions and longer reaction times under head-movable conditions.

This is exactly a:

```text
information benefit
↔ time/effort cost
```

sampling case.

But again the full decision is expressible with HF20 + HOC2/HOC5 + HF11.

---

# 14. PerceptualCalibration does not rescue one unified family

Round 1's secondary residual was:

```text
PerceptualCalibrationCase
```

Round 2 splits it.

## 14.1 Affordance/action-boundary calibration

HF11 already defines:

```text
Calibration
= scaling perception/action to the actual current relation
  between capability and environmental/task demand
```

and separates:

```text
PhysicalActionPossibility
PerceivedAffordance
```

Tool-use and body-change experiments show that Humans recalibrate reach/action judgments after changes in tool/body configuration, and such calibration can be task-specific with limited transfer.

This is primarily HF11 action/affordance calibration.

## 14.2 Sensory/perceptual mapping recalibration

HF20 owns:

```text
Integration != Recalibration
Recalibration != MotorAdaptation
```

Cross-modal/sensory mapping shifts remain HF20.

## 14.3 Learning/retention/transfer

Whether recalibration persists or transfers belongs to HOC3.

Therefore:

```text
PerceptualCalibration
!= OneIndependentOperationalFamily
```

It is typed by what is being recalibrated.

---

# 15. Calibration transfer is itself task/information specific

Human affordance research shows recalibration can fail to transfer even between functionally similar actions when the informational requirements differ.

Therefore reject:

```text
CalibratedOnce
→ CalibratedGenerally
```

and:

```text
OnePerceptualCalibrationScore
```

This strengthens typed HF11/HF20 ownership rather than one new HOC.

---

# 16. Multisensory integration also remains below HOC-family threshold

Possible actions:

```text
sample another modality
keep cues separate
combine cues
reweight cue reliability
recalibrate after discrepancy
```

But at generic level this reduces to:

```text
HF20 perceptual causal/integration model
+ HOC2 evidence/reliability/stopping
+ HOC5 choice where action is required
```

No stable extra substantive owner has emerged.

Disposition:

```text
MultisensoryIntegration
= Foundation-rich purpose-specific projection / subproblem
```

not HOC11 evidence.

---

# 17. What survives: PerceptualSamplingCompositionProtocol

A useful unnumbered protocol remains:

```text
PerceptualSamplingCompositionProtocol = {
  use_question,
  perceptual_target,
  sampling_controller,
  current_evidence,
  current_perceptual_uncertainty,
  available_sensory_channels,
  candidate_sampling_actions,
  predicted_HF20_evidence_effects,
  HOC2_evidence_value_and_stopping,
  HOC5_action_allocation,
  HF11_execution_requirements,
  HOC1_support_and_capability,
  HOC4_cost/fatigue_constraints,
  tool/interface/media_dependencies,
  World_information_availability,
  realized_sampling_action,
  evidence_update,
  Human/Agent attribution,
  update/expiry,
  uncertainty
}
```

This protocol is useful because consumers otherwise repeatedly cross the same ownership boundary.

But:

```text
CrossOwnerCompositionProtocol
!= HumanOperationalFamily
```

---

# 18. Protocol substitution test

Delete the protocol but keep all owners explicit.

The consumer can still reconstruct the correct action by manually composing:

```text
HF20 + HOC2 + HOC5 + HF11 + HOC1/HOC4
```

What is lost is:

```text
consistent controller attribution
consistent target/action/evidence linkage
consistent stopping/cost fields
consistent ownership routing
```

No unique Human substantive state or action disappears.

Therefore:

```text
PerceptualSamplingCompositionProtocol
= protocol
```

not HOC.

---

# 19. Final deletion test

Hold fixed:

```text
perceptual target
HF20 action→evidence model
HOC2 evidence value/stopping
HOC5 candidate actions/costs
HF11 execution capability
```

Delete the candidate family label `ActiveSamplingPolicy`.

No decision variable disappears.

The policy can be derived/composed.

Therefore:

```text
A3 stable substantive hole
= FAIL at generic Human-family level
```

and:

```text
A9 deletion harm
= FAIL at family level
= PASS only for protocol convenience/safety
```

---

# 20. Round-2 firewalls

```text
ActiveSensing != AlwaysBetter
ActiveMovement != PerceptualBenefit
MoreSamples != BetterPolicy
MoreInformation != BetterDecisionByDefinition

SamplingPolicy != HumanTrait
SamplingControl != PerceptualCapability
HumanPerceptualSuccess != HumanSelectedSamples
AgentSelectedView != HumanActiveSampling
HumanDemonstration != HumanCurrentOwnership

SensorCoverage != HumanPerceptualAccess
PerceptualUncertainty != MetacognitiveConfidence
SamplingCost != MotorCostOnly

PerceptualCalibration != MotorCalibrationByDefinition
AffordanceCalibration != SensoryMappingRecalibration
CalibrationInTaskA != CalibrationInTaskB
ToolUse != GlobalBody/PerceptualCalibration
```

---

# 21. Admission result

```text
ActiveSamplingPolicy as independent Human HOC
= REJECT / DECOMPOSE
```

Retain:

```text
PerceptualSamplingCompositionProtocol
= unnumbered
```

and typed subproblems:

```text
HF20 sensory/perceptual recalibration
HF11 affordance/action-boundary calibration
HOC3 recalibration learning/transfer
```

Thus:

```text
HOC11 = UNKNOWN / not admitted
```

---

# 22. Information-gain update

HF20 remains a rich scientific area.

But for the specific question:

```text
Does HF20 hide another generic Human HOC?
```

Round 2 sharply lowers the posterior.

Current estimate:

```text
HF20 generic-new-HOC information gain
= LOW after R2

HF20 domain/consumer information gain
= HIGH
```

This distinction matters.

---

# 23. Pivot

The next highest-information Human-side space becomes:

```text
HF11 — Action / Tool-Integrated Control / Affordance Calibration
```

Not because it must yield a new HOC, but because Round 2 repeatedly routed the strongest calibration residual into HF11.

The next search should begin from:

```text
AffordanceCalibration
ToolIntegratedControl
OnlineCorrection / ExecutionFragility
ActionBoundaryRecalibration
Human–Agent / assistive tool control
```

and attack them against existing HOC1/HOC3/HOC5/HOC8/HOC9 plus Runtime/Interface/World ownership.

No HOC11 or other numbering is preselected.
