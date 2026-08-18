---
schema_version: 1
id: human.operational-concepts.hoc0.inventory
title: HOC0 — Human Operational Concept Candidate Inventory
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
summary: First candidate inventory for Human Operational Concepts. It classifies legacy and foundation-derived Human concepts by practical utility and reconstruction need rather than ontological primitiveness. Strongly retained concepts include capability surface, skill, expertise, motivation profile, context-indexed preference, fatigue state, trust relation, confidence/calibration, personal baseline, learning/modifiability trajectory and bottleneck inference. Several common labels are retained only after qualification or splitting, including competence, readiness, workload, engagement, stress, health status, resilience, aptitude, personality profile and intelligence score. Unqualified potential, talent, global trust, global risk tolerance, energy score and one canonical UserProfile are rejected as canonical HOCs.
evidence_status: synthesized-from-canonical-foundations
readiness: READY
related:
  - human.operational-concepts.hoc0.layer
  - human.deep-foundations.hd10.closeout
---
# HOC0 — Candidate Inventory

## 0. Classification vocabulary

```text
RETAIN       — already has a strong operational referent; refine interface/evidence.
RECONSTRUCT  — useful concept, but current ordinary form is too ambiguous.
SPLIT        — one label hides several operationally distinct objects.
QUALIFY      — only valid with domain/target/context/support/time qualifier.
EVIDENCE_ONLY— useful as measurement coordinate or prior, not direct action truth.
REJECT       — do not make canonical HOC in unqualified form.
```

A concept may receive more than one disposition.

---

# 1. Highest-value retained family — Capability / Skill / Expertise

## CapabilitySurface — RETAIN / RECONSTRUCT

Practical question:

```text
What can H reliably achieve under declared task/state/support conditions?
```

Canonical direction:

```text
CapabilitySurface_H(
  TaskFamily,
  Difficulty,
  Novelty,
  State,
  TimeBudget,
  KnowledgeAccess,
  SupportBoundary
)
```

Why useful:

```text
task assignment
learning-vs-delegation decisions
support selection
Human×Agent attribution
capacity planning
recovery/transfer assessment
```

Hard guard:

```text
ObservedPerformance != Capability
JointCapability != IndependentCapability
```

Disposition: **top HOC candidate**.

---

## Skill — RETAIN / QUALIFY

Practical question:

```text
Has H learned reliable execution for task family D?
```

Use:

```text
training allocation
automation decisions
quality control
support removal
transfer tests
```

Must bind:

```text
domain
task family
quality criterion
reliability
conditions
support boundary
recency
```

Hard guard:

```text
Skill != OnePerformance
Skill != KnowledgeDescription
Skill != Habit
```

---

## Expertise — RETAIN / QUALIFY

Practical question:

```text
Does H possess deep domain organization that improves representation, search, judgment and verification in D?
```

Use:

```text
expert routing
review assignment
escalation
mentoring
verification weighting
```

Hard guards:

```text
Expertise_D != GeneralIntelligence
Expertise != Authority
Expertise != Infallibility
```

---

## Competence — SPLIT / QUALIFY

Unqualified `competence` is too overloaded.

Retain only typed variants such as:

```text
TaskCompetence
RoleCompetence
EpistemicCompetence
DecisionCompetence
ExecutionCompetence
LinguisticCompetence
```

Reject:

```text
Competence(H) = one general scalar
```

---

# 2. Action-allocation family — Goal / Intent / Priority / Motivation

## Goal — RETAIN

Practical question:

```text
What represented target currently organizes action?
```

Useful fields:

```text
content
activation
priority
commitment
maintenance status
time horizon
conflicts
```

Hard guards:

```text
Goal != Outcome
Goal != Behavior
Goal != Preference
```

---

## Intent — RETAIN / QUALIFY

Practical question:

```text
What action does H currently intend to initiate/complete?
```

Use:

```text
handoff
execution support
reminders
coordination
```

Hard guards:

```text
Intent != Action
Intent != ResponsibilityTotality
Intent != ConsentByDefinition
```

---

## Priority — RETAIN / RECONSTRUCT

Practical question:

```text
Given current competing demands, what receives scarce time/attention/action first?
```

Priority is relational and time-dependent.

Use:

```text
scheduling
triage
attention allocation
Agent planning
```

Reject:

```text
Priority = moral importance
Priority = permanent personal value rank
```

---

## MotivationProfile — RETAIN / RECONSTRUCT

Practical question:

```text
Why is action toward G likely/unlikely now, and what lever would change allocation?
```

Candidate components:

```text
current value
expected efficacy
control/opportunity
effort cost
urgency
intrinsic interest
social incentives
fatigue/state
habit/conflict
commitment
```

Use:

```text
learning support
task design
disengagement diagnosis
intervention selection
```

Hard guard:

```text
LowMotivation != CharacterDefect
```

---

## Preference — RETAIN / QUALIFY

Practical question:

```text
Given choice context C at time t, which option does H currently prefer?
```

Use:

```text
personalization
ranking
recommendation
choice support
```

Mandatory qualifiers:

```text
choice set
framing/context
state/time
confidence/evidence
```

Hard guards:

```text
Preference != Welfare
Preference != Consent
ObservedChoice != TimelessPreference
```

---

# 3. Regulation / execution-state family

## FatigueState — RETAIN / RECONSTRUCT

Practical question:

```text
Is reduced available performance currently consistent with fatigue, in which domain, and how reversible is it?
```

Use:

```text
work/rest allocation
safety gating
learning timing
workload adjustment
```

Represent separately:

```text
experienced fatigue
performance fatigue
physiological evidence
recovery trajectory
domain
```

Hard guards:

```text
Fatigue != LowSkill
Fatigue != LowMotivation
Fatigue != OneFuelGauge
```

---

## TaskReadiness — RECONSTRUCT / SPLIT

`Readiness` is highly useful but too broad as one latent Human property.

Reconstruct as a purpose-bound bundle:

```text
TaskReadiness(H, Task, t, Support)
= decision-oriented synthesis of:
  available capacity
  required skill/knowledge
  current fatigue/health state
  intent/goal alignment
  support/resource availability
  time/safety constraints
```

Use:

```text
start now / defer
self-execute / delegate
train first / execute first
```

Hard guard:

```text
ReadinessScore != Ability
```

---

## ExecutionProfile — RETAIN / RECONSTRUCT

Practical question:

```text
How reliably does H turn intention/plan into completed action under D?
```

Candidate dimensions:

```text
initiation latency
completion reliability
error recovery
interruptibility
verification
time estimation
support dependence
```

Use:

```text
Agent handoff
workflow design
reminder/escalation policy
```

---

## Workload — SPLIT / RECONSTRUCT

Do not use one unqualified workload scalar.

Separate at least:

```text
TaskDemand
AssignedLoad
ExperiencedLoad
AvailableCapacity
LoadCapacityMismatch
CumulativeLoad
```

Use:

```text
scheduling
safety
fatigue prevention
resource allocation
```

---

## Stress — SPLIT / QUALIFY

Separate:

```text
StressorExposure
Appraisal
StressResponse
StressBurden
Recovery
```

Do not infer one from another automatically.

---

## RecoveryProfile — RETAIN / RECONSTRUCT

Practical question:

```text
After disturbance D, how does relevant functioning return/change over time?
```

Use:

```text
rest planning
return-to-work/task
resilience assessment
intervention monitoring
```

---

## ResilienceProfile — RETAIN / QUALIFY

Retain only as:

```text
ResilienceProfile(H, Exposure, OutcomeDomain, Interval)
```

Hard guard:

```text
Resilience != OneTrait
```

---

# 4. Epistemic / judgment family

## ConfidenceEstimate — RETAIN / SPLIT

Separate:

```text
subjective confidence
stated probability
meta-confidence
calibration history
```

Use:

```text
verification allocation
escalation
Human–Agent arbitration
```

Hard guards:

```text
Confidence != Accuracy
Confidence != Authority
```

---

## CalibrationProfile — RETAIN

Practical question:

```text
When H expresses confidence c in domain D, how well does it correspond to empirical correctness/uncertainty?
```

Use:

```text
review intensity
routing
self-check prompts
confidence correction
```

This is often more useful operationally than raw confidence.

---

## KnowledgeState — RECONSTRUCT

Do not use `knows=true`.

A practical profile may separate:

```text
recognition
free recall
explanation
application
transfer
recency
source/provenance
confidence
```

Use:

```text
learning allocation
retrieval support
assessment
```

Hard guard:

```text
Knowledge != CurrentRecall
```

---

## UnderstandingProfile — RETAIN / RECONSTRUCT

Candidate evidence:

```text
prediction
explanation
boundary awareness
causal structure
transfer
error detection
counterfactual handling
```

Use:

```text
teaching depth
review assignment
safe delegation
```

---

## VerificationCapability — RECONSTRUCT

Practical question:

```text
Can H reliably detect/check errors in outputs from self, others or Agents in domain D?
```

Use:

```text
Agent delegation boundaries
human-in-the-loop design
review routing
```

This may be more useful than asking whether H can independently generate the output.

---

# 5. Learning / development family

## LearningTrajectory — RETAIN

Track:

```text
practice performance
retention
transfer
error change
strategy change
support use
```

not one `progress` number by default.

---

## ModifiabilityProfile — RETAIN

Practical question:

```text
How does H respond to intervention/training protocol I?
```

Use:

```text
curriculum adaptation
support intensity
intervention choice
```

Hard guard:

```text
Modifiability_I != FixedPotential
```

---

## LearningProgress — RECONSTRUCT

Useful as a product-facing summary if explicitly derived from:

```text
baseline
practice gain
retention
transfer
target competence
```

Reject progress based only on activity/completion counts.

---

## Aptitude — RECONSTRUCT / QUALIFY

Aptitude can be useful only as:

```text
Aptitude_D(H | target domain, learning opportunity, horizon, support)
= predictive estimate of future learning/performance under declared conditions
```

Hard guard:

```text
Aptitude != HiddenFixedPotential
```

---

## Potential — REJECT unqualified

Replace with one of:

```text
ModifiabilityProfile
CapabilityEnvelope
Aptitude_D
CounterfactualCapabilityUnderSupport
```

---

## Talent — REJECT unqualified

May survive only as informal communication label backed by typed evidence.

Do not canonicalize `Talent(H)`.

---

# 6. Relational / collaborative family

## Trust — RETAIN / QUALIFY

Canonical operational form:

```text
Trust(A→B, TargetDimension, Context, History)
```

Possible target dimensions:

```text
competence
reliability
honesty
benevolence
confidentiality
rule-following
```

Use:

```text
delegation
verification intensity
information sharing
coordination
```

Hard guards:

```text
Trust != Predictability
Trust != Reliance
Trust != MoralApproval
Trust != Permission
```

---

## Reliance — RETAIN / SPLIT FROM TRUST

Practical question:

```text
Is A behaviorally depending on B for target T?
```

Reliance can occur without trust and vice versa.

Use:

```text
dependency mapping
failure planning
Agent/tool resilience
```

---

## Dependence — RETAIN / QUALIFY

Represent resource/task-specific dependency rather than global interpersonal label.

Use:

```text
single-point-of-failure analysis
support planning
relationship risk
```

---

## CoordinationReadiness — RECONSTRUCT

Potential bundle of:

```text
role clarity
shared task representation
communication channel
availability
trust/reliance
capability complementarity
conflict state
```

Useful for team/Agent orchestration, not a person trait.

---

# 7. Health / functioning family

## PersonalBaseline — RETAIN

Use:

```text
change detection
health/functioning monitoring
state interpretation
```

Hard guards:

```text
PersonalBaseline != PopulationReference
PersonalBaseline != ImmutableSetpoint
```

---

## HealthStatus — SPLIT / RECONSTRUCT

Do not create one universal health scalar.

Operational consumers may instead use purpose-specific bundles:

```text
CurrentSymptomBurden
FunctionalStatus
OrganismicRiskEstimate
RecoveryStatus
ConditionTrajectory
PersonalBaselineDeviation
```

A UI may summarize these, but the summary is not canonical ontology.

---

## FunctionalStatus — RETAIN / QUALIFY

Practical question:

```text
What activities/participation can H currently sustain under ordinary context/support?
```

Keep separate from diagnosis and moral worth.

---

## Reserve — RETAIN / QUALIFY

```text
Reserve_D(H, burden, context)
```

Useful when challenge response reveals hidden headroom unavailable from resting baseline.

---

# 8. Personality / individual-difference family

## PersonalityCoordinate — EVIDENCE_ONLY / QUALIFY

Big Five / HEXACO-like coordinates may be used for:

```text
population comparison
weak personalization priors
research communication
```

but should not directly determine high-stakes policy.

Hard guard:

```text
PersonalityCoordinate != Mechanism
```

---

## PersonDifferenceSnapshot — RETAIN / RECONSTRUCT

A finite, task/use-specific bundle of current projections.

Use:

```text
personalization context
handoff
learning adaptation
```

Hard guard:

```text
Snapshot != Person
```

Must be versioned and scoped.

---

## IntelligenceScore / g — EVIDENCE_ONLY / QUALIFY

Can be useful as:

```text
GeneralAbilityCoordinate(H; Battery, Population, Model)
```

but should not substitute for:

```text
capability surface
knowledge
learning response
expertise
verification ability
```

---

# 9. Risk / safety family

## Risk — RECONSTRUCT as relation/scenario, not Human property

Prefer:

```text
Risk(Scenario, Outcome, Probability/Uncertainty, Exposure, Horizon)
```

rather than:

```text
H.risk = high
```

---

## RiskTolerance / RiskPreference — QUALIFY heavily

Retain only:

```text
RiskPreference(H, ChoiceDomain, Stakes, Framing, Horizon, State)
```

Hard guard:

```text
NoSingleGlobalRiskTrait
```

---

## SafetyReadiness — RECONSTRUCT

A purpose-specific gating bundle may be useful for high-consequence tasks, but must state the task/hazard and decision rule.

---

# 10. Common product labels that need caution

## Engagement — SPLIT / EVIDENCE_ONLY

`Engagement` often conflates:

```text
attention
time-on-task
participation
persistence
interest
affect
compliance
```

Use only if the consumer explicitly defines which combination matters.

Do not infer motivation or learning from engagement alone.

---

## Energy — REJECT unqualified

The everyday label may summarize felt activation, fatigue or available effort, but canonical HOC should use typed state variables.

---

## UserProfile — REJECT as one canonical object

Allow:

```text
PersonDifferenceSnapshot
PreferenceSnapshot
CapabilitySnapshot
LearningSnapshot
CurrentStateBundle
```

for declared consumers.

Do not build one permanent universal user vector.

---

# 11. First-pass priority matrix

## Tier A — highest immediate operational value

```text
CapabilitySurface
Skill
Expertise
TaskReadiness
ExecutionProfile
FatigueState
MotivationProfile
Confidence/Calibration
LearningTrajectory
ModifiabilityProfile
Trust/Reliance
PersonalBaseline
BottleneckInference
```

These directly alter Human–Agent decisions.

## Tier B — high value, narrower or more context-sensitive

```text
Goal
Intent
Priority
Preference
KnowledgeState
UnderstandingProfile
VerificationCapability
Workload
RecoveryProfile
ResilienceProfile
FunctionalStatus
Reserve
CoordinationReadiness
Aptitude_D
```

## Tier C — useful mainly as scoped evidence/prior

```text
PersonalityCoordinate
GeneralAbilityCoordinate
PersonDifferenceSnapshot
RiskPreference
Engagement composite
```

## Reject unqualified canonical forms

```text
Potential
Talent
GlobalCompetence
GlobalReadiness
GlobalTrust
GlobalRiskTolerance
EnergyScore
UniversalHealthScore
OneUserProfile
```

---

# 12. New high-value concept discovered by practical audit — BottleneckInference

The foundations repeatedly imply a concept that old H0 did not fully canonicalize:

```text
BottleneckInference(H, TargetOutcome, t)
```

Practical question:

```text
What currently limits the target outcome enough that changing it is likely to improve performance/capability?
```

Candidate bottleneck classes:

```text
organismic state
attention/control
knowledge
skill
reasoning
motivation/goal conflict
execution
support/tool availability
relationship/coordination
institutional permission/resource
measurement/task mismatch
```

This is not a Human trait.

It is a **decision-oriented causal hypothesis** with uncertainty.

Use:

```text
what to train
what to rest
what to delegate
what tool to provide
what constraint to remove
what evidence to collect next
```

This may become one of the most valuable HOC concepts for Ordivon Human.

---

# 13. HOC0 outcome

The practical audit shows that many familiar Human concepts should be **recovered**, not discarded.

The correct transformation is:

```text
vague label
→ use question
→ typed operational construct
→ bounded evidence
→ update/expiry
→ decision effect
→ drill-down path
```

rather than:

```text
vague label
→ Foundation
```

Recommended first detailed reconstruction family:

```text
HOC1 — Capability, Readiness & Bottleneck
```

because it directly connects:

```text
Human state
skill/knowledge
support/Agent attribution
learning vs delegation
execution timing
resource allocation
```

and already has strong foundations plus legacy H0 material.
