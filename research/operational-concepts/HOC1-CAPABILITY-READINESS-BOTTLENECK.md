---
schema_version: 1
id: human.operational-concepts.hoc1
title: HOC1 — Capability, Readiness and Bottleneck Reconstruction
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
summary: Reconstructs CapabilitySurface, TaskReadiness and BottleneckInference as a coupled Human operational triad. CapabilitySurface is a support-, state-, task- and criterion-bounded distribution of achievable performance rather than a person scalar. TaskReadiness is a purpose- and consequence-relative near-term decision bundle comparing task demands against current capability, state, support, permission and verification requirements; it is not ability or moral authorization. BottleneckInference is a causal/action hypothesis about which currently alterable constraint, uncertainty or fragility most limits a declared outcome under a feasible intervention set; it is not the lowest component score. The round formalizes independent/situated/joint capability, demand profiles, capability margins, evidence ladders, paired support-removal/transfer tests, readiness modes, hard gates versus soft deficits, binding/marginal/fragility/uncertainty bottlenecks, intervention-value ranking, counterexamples, update/expiry rules and Human–Agent decision patterns. No Foundation is reopened and no engineering schema is prescribed.
evidence_status: verified-synthesis
readiness: READY
related:
  - human.operational-concepts.hoc0.layer
  - human.operational-concepts.hoc0.inventory
  - human.deep-foundations.hd10d
  - human.deep-foundations.hd10e
---
# HOC1 — Capability, Readiness and Bottleneck

## 0. Decision

HOC1 retains a three-object operational chain:

```text
CapabilitySurface
→ what outcomes are reliably reachable under declared conditions

TaskReadiness
→ whether attempting a declared task now, in a declared mode, is sufficiently supported

BottleneckInference
→ what currently alterable constraint / uncertainty / fragility most limits the target outcome
```

They answer different questions and must not collapse:

```text
Capability != Readiness
Readiness != Bottleneck
Bottleneck != LowestCapabilityComponent
```

The triad exists downstream of HF0–HF23.

```text
OperationalUsefulness != FoundationStatus
```

---

# 1. Why the old one-score model fails

A single `ability`, `readiness` or `performance` score hides several independent variables:

```text
task family
difficulty
novelty
quality criterion
time budget
state/fatigue
knowledge access
tool support
partner/Agent support
verification requirement
consequence/risk
opportunity / institutional permission
```

Minimal counterexample:

```text
H solves task X with AI in 5 min.
H cannot solve X independently.
H can reliably verify AI output.
```

There are at least three true claims:

```text
IndependentGenerationCapability = low/unknown
JointGenerationCapability       = high
VerificationCapability          = high
```

One `capability=high` or `capability=low` destroys useful information.

---

# 2. TaskSpec

Operational capability starts with a declared target.

```text
TaskSpec = {
  task_family,
  target_outcome,
  difficulty_or_demand_region,
  novelty,
  quality_criterion,
  reliability_criterion,
  latency_or_deadline?,
  cost_or_effort_constraint?,
  verification_requirement?,
  consequence_profile?,
  transfer_distance?,
  environment_scope
}
```

A task family should be broad enough for repeated evidence and narrow enough that success conditions remain meaningful.

```text
OneObservedTask != TaskFamilyCapability
```

---

# 3. SupportSpec

Capability attribution requires an explicit support boundary.

```text
SupportSpec = {
  external_memory,
  search_access,
  software/tools,
  AI_generation,
  AI_critique,
  human_collaborators,
  organizational_support,
  accommodations,
  prompts/scaffolds,
  information_access,
  time/resources
}
```

Canonical levels:

```text
IndependentCapability
SituatedCapability
JointCapability
```

These are not a moral ranking.

A joint system may be the correct optimization target for production while independent capability remains the correct target for resilience, authorship, verification, learning or tool-failure recovery.

---

# 4. StateSpec

Current reachable performance is state-sensitive.

```text
StateSpec = {
  fatigue/sleep state,
  pain/illness,
  affect/stress,
  attention/control availability,
  motivation/goal conflict,
  current workload,
  acute medication/substance effects where relevant,
  current confidence/calibration evidence
}
```

No field is mandatory across all domains.

```text
CurrentStateEffect != PersistentCapabilityChange
```

---

# 5. CapabilitySurface — canonical object

```text
CapabilitySurface_H(TaskSpec, StateSpec, SupportSpec, interval)
→ distribution over achievable task-relevant outcomes
```

A useful projection can include:

```text
success probability / attainment rate
quality distribution
latency distribution
error profile
variability
reliability
resource/effort cost
verification quality
novelty tolerance
transfer distance
recovery after interruption/error
support dependence
uncertainty
```

The surface is not required to be mathematically continuous.
A sparse set of evidence-backed regions is acceptable.

---

# 6. CapabilitySurface is not a latent person essence

It is explicitly conditional:

```text
CapabilitySurface
= relation(
    Human persistent structure,
    current state,
    task demand,
    environment,
    support,
    criterion,
    history
  )
```

Therefore:

```text
Capability_D,C1 != Capability_D,C2 by identity
```

and:

```text
SupportedCapability != IndependentCapability
```

---

# 7. Capability axes should not be summed by default

A practical surface should preserve separate axes when trade-offs matter:

```text
accuracy / quality
speed
consistency
cost / effort
novelty
transfer
verification
recovery
```

Example:

```text
Person A: high speed, moderate errors
Person B: slower, near-zero errors
```

For emergency triage A may be preferable.
For financial reconciliation B may be preferable.

Thus:

```text
CapabilityRanking
requires
DecisionCriterion
```

---

# 8. Capability tiers are allowed

HOC can compress a surface into an operational tier:

```text
UNSUPPORTED
FRAGILE
CONDITIONALLY_RELIABLE
RELIABLE
ROBUST
```

but the tier must bind to:

```text
TaskSpec
SupportSpec
State/interval
criterion
source evidence
uncertainty
```

and remain drill-down capable.

```text
CapabilityTier != PersonIdentity
```

---

# 9. Evidence ladder for CapabilitySurface

Evidence strength increases approximately through:

```text
E0 self-report / claimed familiarity
E1 one observed task
E2 repeated similar tasks
E3 varied difficulty / context
E4 delayed retest
E5 novel transfer
E6 support removal / support substitution
E7 adverse-state / interruption / recovery tests
E8 authentic consequential task history
```

This is not a universal psychometric scale.
It is an operational evidence ordering.

Important:

```text
E1 can establish observed performance.
E1 cannot establish broad capability.
```

---

# 10. Support-removal matrix

For Human×Agent work, one of the highest-value experiments is:

```text
                 immediate        delayed        novel transfer
with support         A               B                C
without support      D               E                F
```

This distinguishes:

```text
joint/situated performance
independent retention
transfer
support dependence
possible internalization
```

A strong `A` with weak `D/E/F` supports high situated capability but weak evidence for independent skill acquisition.

---

# 11. Capability acquisition versus capability substitution

Agent/tool assistance can produce at least four patterns:

```text
Amplification
  independent capability stable, joint output higher

Scaffolding
  joint use increases later independent capability

Substitution
  joint output high, independent capability unchanged

Deskilling/dependency
  joint output high while later independent capability declines
```

One assisted-performance trace cannot distinguish them.

---

# 12. WHO ICF pressure

WHO ICF distinguishes what a person does in the current environment (`performance`) from capacity to execute a task/action in a standard or uniform environment, while explicitly representing environmental factors.

HOC1 retains the structural lesson:

```text
ActualContextPerformance
!= StandardizedCapacityEstimate
```

but generalizes beyond health/disability:

```text
standardized capacity
independent capability
situated capability
joint capability
```

are distinct operational questions.

---

# 13. TaskDemandProfile

Readiness and bottleneck inference require modeling the task side, not just the Human.

```text
TaskDemandProfile(TaskSpec) = {
  required knowledge,
  required skill,
  reasoning/problem complexity,
  sustained attention,
  physical/sensorimotor demand,
  time pressure,
  coordination demand,
  tool fluency,
  verification burden,
  novelty,
  consequence sensitivity,
  permission/resource requirements
}
```

Do not assume these are independent dimensions.

```text
TaskDifficulty != PersonIndependentScalar
```

A task can be easy for one support configuration and hard for another.

---

# 14. Capability–Demand relation

Operational readiness needs comparison between:

```text
CapabilitySurface(H, ...)
```

and:

```text
TaskDemandProfile(T)
```

but not necessarily subtraction of two scalars.

Use:

```text
CapabilityDemandFit = {
  requirements_satisfied,
  requirements_uncertain,
  requirements_unsatisfied,
  compensating_support,
  fragile_dependencies,
  evidence_quality
}
```

---

# 15. Hard gates versus soft deficits

Some requirements are hard gates:

```text
required credential / permission
minimum safety condition
mandatory information
required physical access
non-substitutable verification capability
```

Others are soft deficits:

```text
slower speed
higher effort
lower comfort
moderate uncertainty
```

A weighted average must not allow a high score on a soft dimension to hide a failed hard gate.

```text
ReadinessAggregate
must preserve
HardGateFailure
```

---

# 16. TaskReadiness — canonical object

TaskReadiness is not a property of a Human.

```text
TaskReadiness(H, TaskSpec, t, ExecutionMode, ConsequenceSpec)
→ decision-oriented near-term bundle
```

Its purpose is to answer:

```text
Should this task be attempted now in this mode,
with what support and verification,
under the declared objective and consequence tolerance?
```

---

# 17. Readiness components

A generic readiness bundle may inspect:

```text
capability-demand fit
current state / fatigue
knowledge/skill evidence
support availability
execution resources/time
permission/authority
coordination availability
verification capability
consequence/risk threshold
intent/goal alignment when relevant
critical uncertainty
```

Different consumers may omit irrelevant dimensions.

---

# 18. Readiness is purpose-relative

At least four distinct readiness questions exist:

```text
ExecutionReadiness
LearningReadiness
DelegationReadiness
VerificationReadiness
```

and in safety-sensitive contexts:

```text
SafetyReadiness
```

The same Human may be:

```text
not ready to execute independently
ready to learn with scaffolding
ready to verify an Agent output
ready for joint execution
```

Therefore:

```text
GlobalReadiness = rejected
```

---

# 19. Readiness modes

A useful operational output is categorical before scalar:

```text
READY_INDEPENDENT
READY_WITH_SUPPORT
READY_TO_LEARN
READY_TO_VERIFY_ONLY
DEFER_STATE
BLOCKED_RESOURCE_OR_PERMISSION
INSUFFICIENT_EVIDENCE
NOT_READY_FOR_CONSEQUENCE_LEVEL
```

These modes are more actionable than a single 0–100 number.

---

# 20. Optional readiness score

A consumer may produce a score for sorting or UI.

But canonical HOC1 requires:

```text
ReadinessScore
!= Ability
ReadinessScore
!= MoralPermission
ReadinessScore
!= StableHumanProperty
```

and hard gates must remain explicit.

---

# 21. Readiness expiry

Readiness is one of the shortest-lived HOCs.

It should usually expire when any material input changes:

```text
state/fatigue
support/tool availability
new task specification
deadline
environment
partner availability
permission
new evidence
risk/consequence level
```

Operational rule:

```text
Readiness is recomputed, not remembered as a trait.
```

---

# 22. Fatigue evidence and readiness

Sleep-loss research using the psychomotor vigilance test shows that behavioral alertness can degrade under acute and partial sleep deprivation, and brief PVT variants can track sleep-loss-related impairment.

HOC1 uses this only to support:

```text
CurrentState can materially shift readiness/performance.
```

It does not infer:

```text
PVT score = global readiness
```

or:

```text
subjective fatigue = objective performance loss
```

HF5's separation remains binding.

---

# 23. Readiness under Human×Agent support

Agent support can change readiness without changing Human internal skill.

Example:

```text
IndependentReadiness = NOT_READY
JointReadiness       = READY_WITH_SUPPORT
```

This is not contradictory.

The support should be named:

```text
AI generation
AI retrieval
AI critique
AI monitoring
human review
```

because different support types change different demands.

---

# 24. Verification is often the binding readiness variable

In high-consequence Agent use, independent generation skill may be unnecessary if the Human can reliably:

```text
define target
recognize error
check evidence
reject unsafe output
escalate uncertainty
```

Therefore:

```text
VerificationCapability
can be a readiness requirement
without
GenerationCapability
```

This is a major practical reason not to use one general capability score.

---

# 25. BottleneckInference — canonical object

A bottleneck is not the weakest-looking component.

Define:

```text
BottleneckInference(H, TargetOutcome, t, FeasibleInterventionSet)
→ ranked causal/action hypotheses
```

Each hypothesis should include:

```text
candidate_constraint
mechanism_or_pathway hypothesis
predicted outcome change if altered
feasible intervention
intervention cost/time
uncertainty
evidence
confounders / rival explanations
information needed to discriminate
expiry condition
```

---

# 26. Counterfactual criterion

Operationally, candidate `B` is a bottleneck only if a feasible change in `B` is expected to materially change the target outcome, conditional on the rest of the system.

Idealized form:

```text
BottleneckEffect(B_i)
≈ E[Y | do(Change B_i)] - E[Y | status quo]
```

HOC1 does not claim this quantity is usually identifiable from observation alone.
It is a target for causal reasoning and intervention tests.

---

# 27. Weakest-component fallacy

Suppose:

```text
skill = low
AI support fully compensates
verification = high
```

For the target:

```text
produce correct output with AI
```

low independent skill may not be the current bottleneck.

For the target:

```text
produce correct output with no AI
```

it may become binding.

Therefore:

```text
Bottleneck
is target- and support-relative.
```

---

# 28. Bottleneck types

HOC1 retains at least five operational types.

## 28.1 Binding bottleneck

A necessary requirement is below threshold.

Examples:

```text
missing permission
missing prerequisite knowledge
unavailable tool
unsafe fatigue state
```

## 28.2 Marginal bottleneck

Not a hard failure, but the best feasible improvement lever.

```text
Which change produces the most outcome gain per relevant resource?
```

## 28.3 Fragility bottleneck

Average performance is acceptable but one failure mode dominates reliability.

Examples:

```text
poor verification
single tool dependency
interruption recovery failure
one coordination handoff
```

## 28.4 Uncertainty bottleneck

The largest obstacle to choosing an action is missing discriminative evidence.

The next best action may be:

```text
measure / test / ask / run a cheap trial
```

rather than intervene on the Human.

## 28.5 Coordination / external bottleneck

The limiting variable lives outside the Human:

```text
resource
permission
partner
institution
interface
specification
```

This must not be rewritten as low Human capability.

---

# 29. Bottleneck sets

Multiple variables can be jointly binding.

```text
BottleneckSet = {B1, B2, ...}
```

Examples:

```text
knowledge gap + no search access
high skill + no permission
adequate Human + poor Agent interface + weak verification
```

Do not force one winner when interaction is supported.

---

# 30. Bottleneck is intervention-relative

A true causal constraint may be operationally irrelevant if it is not alterable within the decision horizon.

Example:

```text
long-term domain expertise is limiting,
but deadline is 30 minutes.
```

Immediate intervention set may favor:

```text
delegate
add retrieval support
reduce task scope
increase verification
```

Thus HOC1 distinguishes:

```text
CausalConstraint
!= BestCurrentLever
```

---

# 31. Bottleneck value

A practical ranking can consider:

```text
ExpectedOutcomeGain
× confidence
× reversibility
× time fit
× transfer value
```

against:

```text
cost
risk
opportunity cost
support dependence
```

HOC1 does not freeze one universal formula.
Different consumers have different utility functions and authority.

---

# 32. Information-gathering as an intervention

If two hypotheses remain plausible:

```text
H1 = knowledge gap
H2 = fatigue/attention state
```

then the optimal next move may be a discriminative test:

```text
small knowledge probe
short rest + retest
supported vs unsupported trial
```

Therefore BottleneckInference returns:

```text
next_best_evidence_action
```

when appropriate.

---

# 33. Bottleneck inference ladder

Confidence may increase through:

```text
B0 narrative guess
B1 correlational trace
B2 repeated co-variation
B3 within-person change
B4 targeted probe
B5 intervention / removal test
B6 replicated intervention across contexts
```

The label `bottleneck` should be accompanied by the evidence level or equivalent provenance.

---

# 34. Eight minimal counterexamples

## C1 — Low performance, intact capability

```text
high skill + severe fatigue → poor current performance
```

Bottleneck: state, not skill.

## C2 — High supported performance, weak independence

```text
AI solves most generation; Human verifies well
```

Joint capability high; independent generation capability unknown/low.

## C3 — Weak component, not a bottleneck

```text
mental arithmetic weak + calculator always permitted
```

Arithmetic fluency may not limit current task outcome.

## C4 — External binding gate

```text
Human fully capable + required permission absent
```

Bottleneck is institutional/authority, not Human readiness.

## C5 — Task specification bottleneck

```text
expert repeatedly produces wrong output because requirement is ambiguous
```

More training is the wrong intervention.

## C6 — Verification bottleneck

```text
Agent output usually excellent + Human cannot detect rare severe errors
```

Average joint performance can be high while deployment readiness remains low for high-consequence use.

## C7 — Motivation as rational allocation

```text
capability adequate + expected payoff near zero + competing urgent goal
```

Low initiation is not incapacity.

## C8 — Unknown beats assumed deficit

```text
one poor task result + no repeated evidence
```

Bottleneck may be evidence insufficiency itself.

---

# 35. Human–Agent capability matrix

For a task domain, preserve at least:

```text
Human independent generation
Human independent verification
Agent generation
Agent verification/critique
Human+Agent joint generation
Human+Agent joint verification
support-removal performance
transfer after supported practice
```

This reveals important asymmetries.

A Human can be weak at generation but strong at verification.
An Agent can be strong at generation but weakly calibrated.
The joint system can exceed both if roles are complementary.

---

# 36. AI learning pressure

A 2025 randomized field experiment in high-school mathematics found that GPT-4 support substantially improved assisted practice performance, while a less constrained GPT interface was associated with worse later unassisted exam performance than control; a guardrailed tutor mitigated the negative learning effect.

HOC1 uses this as direct evidence that:

```text
AssistedPerformanceGain
!= IndependentLearningGain
```

and that support design can alter the transition from situated to independent capability.

---

# 37. Dynamic learning pressure

Dynamic-assessment research motivates measuring response to assistance and learning trajectory rather than relying only on static snapshots.

HOC1 retains:

```text
CurrentCapabilitySurface
!= ModifiabilityProfile
```

Two Humans with similar current capability may have different:

```text
support required
learning rate
retention
transfer
```

This matters when deciding:

```text
train
scaffold
delegate
or redesign task
```

---

# 38. Capability and readiness can disagree legitimately

Examples:

```text
High persistent skill + acute fatigue
→ high underlying capability
→ low current readiness

Low independent skill + excellent tool support
→ low independent capability
→ high joint readiness

High capability + no permission
→ low execution readiness

Moderate current capability + high modifiability
→ high learning readiness
```

No contradiction exists.

---

# 39. Bottleneck and readiness relation

A useful decomposition:

```text
TaskReadiness
→ finds unmet/uncertain requirements
→ BottleneckInference
→ ranks why they matter and what to do
```

But BottleneckInference can also run without a readiness decision, e.g. for improving long-term learning or productivity.

---

# 40. Minimal operational outputs

## CapabilitySurfaceView

```text
{
  target,
  support_boundary,
  evidence_region,
  outcome_profile,
  transfer_scope,
  support_dependence,
  uncertainty,
  updated_at
}
```

## ReadinessView

```text
{
  task,
  mode,
  status,
  hard_gates,
  unmet_requirements,
  fragile_requirements,
  critical_unknowns,
  recommended_support,
  evidence_age,
  expires_at
}
```

## BottleneckView

```text
{
  target_outcome,
  candidate,
  bottleneck_type,
  intervention,
  expected_direction,
  confidence,
  rivals,
  next_evidence_action,
  expiry_condition
}
```

These are conceptual views, not mandated persistence schemas.

---

# 41. Update rules

## CapabilitySurface

Update when:

```text
new task evidence
transfer result
support removal result
persistent learning/decline
meaningful support ecology change
new state regime repeatedly changes performance
```

Do not rewrite persistent capability from one bad day.

## TaskReadiness

Recompute aggressively when material state/task/support/consequence inputs change.

## BottleneckInference

Expire after:

```text
intervention
major evidence update
task redesign
support change
state recovery
change in target outcome
```

---

# 42. Reflexivity

Readiness and bottleneck labels can shape future evidence.

```text
system says NOT_READY
→ fewer opportunities
→ less practice
→ future observed capability lower
```

or:

```text
system says skill bottleneck
→ excessive training
→ hidden resource/permission problem persists
```

Therefore high-impact HOC consumers should distinguish:

```text
ObservedEvidence
SystemPolicyProducedEvidence
```

where material.

---

# 43. Normative / authority firewall

HOC1 cannot by itself authorize exclusion or coercion.

```text
LowCapabilityEstimate != LowMoralWorth
NotReady != NoRightToChoose
BottleneckInference != PermissionToIntervene
HighExpertise != Authority
RiskPrediction != LegitimateExclusion
```

A downstream decision rule must own normative/authority questions.

---

# 44. Foundation dependency map

```text
HF3  attention/control/confidence
HF4  goal/motivation/preference/effort
HF5  fatigue/stress/regulation/recovery
HF6  learning/transfer/modifiability
HF7  retention/retrieval
HF8  knowledge/understanding
HF9  reasoning/problem solving
HF10 planning/decision
HF11 skill/execution/tool use/capability relation
HF12 coordination/joint capability
HF13 permission/authority/institution
HF19 work/task/technology/organization
HF20 perception/sensing
HF21 affect/appraisal
HD9  organismic health trajectory
HD10 person-specific projections and support boundaries
World environment/resources/exposure
Tools/Agents support ecology
```

No new Foundation is required.

---

# 45. Forbidden inferences

```text
ObservedPerformance != Capability
Capability != Intelligence
Capability != MoralWorth
CurrentCapability != Modifiability
SituatedCapability != IndependentCapability
JointCapability != SumIndividualCapability
Readiness != Ability
Readiness != Intent
Readiness != Permission
Readiness != PermanentTrait
ReadinessScore != Ontology
Bottleneck != WeakestComponent
Bottleneck != Correlate
Bottleneck != DefectInsideHuman
CausalConstraint != BestCurrentLever
OneFailedTask != StableCapabilityDeficit
AIOutputQuality != HumanSkill
AssistedPerformanceGain != IndependentLearningGain
VerificationCapability != GenerationCapability
TaskDifficulty != PersonIndependentScalar
```

---

# 46. Operational decision grammar

A Human-supporting Agent can use the triad as:

```text
1. Declare TargetOutcome and TaskSpec.
2. Declare proposed SupportSpec / execution mode.
3. Project relevant CapabilitySurface.
4. Compare with TaskDemandProfile.
5. Produce TaskReadiness with hard gates and unknowns.
6. If not ready / fragile, run BottleneckInference.
7. Choose among:
     clarify
     gather evidence
     teach/practice
     rest/recover
     add support/tool
     delegate
     reduce demand/scope
     add verification
     coordinate
     obtain permission/resource
     defer/stop
8. Observe result.
9. Update the appropriate object only at its proper timescale.
```

This is a reasoning grammar, not a mandatory workflow engine.

---

# 47. Why HOC1 is practically stronger than one UserProfile

A static profile asks:

```text
Who is this person?
```

HOC1 asks:

```text
What can be done?
Can it be done now in this mode?
What is blocking the outcome?
What is the cheapest informative or corrective next move?
```

For Agent support, these are usually more actionable questions.

---

# 48. HOC1 stop rule

HOC1 is complete because it has:

```text
reconstructed CapabilitySurface as a conditional support-bounded operational surface;
separated independent/situated/joint capability;
introduced TaskSpec, SupportSpec, StateSpec and TaskDemandProfile;
retained multidimensional outcome/reliability/transfer/verification axes;
defined capability evidence and support-removal testing;
reconstructed TaskReadiness as a short-lived purpose/consequence-relative bundle;
separated readiness modes and hard gates from soft deficits;
reconstructed BottleneckInference as intervention-sensitive causal/action hypotheses;
separated binding, marginal, fragility, uncertainty and external bottlenecks;
made information gathering a legitimate bottleneck action;
added counterexamples, update/expiry and reflexivity rules;
and preserved the normative/authority firewall.
```

No `HF24` or `HD11` follows.

```text
FoundationReopenCondition(HF0–HF23) = false
NextDeepRoute = UNKNOWN
```

The next HOC route is not forced by HOC1. A later practical-priority comparison should select it.
