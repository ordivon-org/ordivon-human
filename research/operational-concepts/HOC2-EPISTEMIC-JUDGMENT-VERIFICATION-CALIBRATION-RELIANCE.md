---
schema_version: 1
id: human.operational-concepts.hoc2
title: HOC2 — Epistemic Judgment, Verification, Calibration and Reliance
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
summary: Reconstructs the practical epistemic layer needed for Human and Human–Agent work. HOC2 separates first-order judgment, confidence level, calibration, metacognitive sensitivity, evidence sufficiency, verification capability, verification procedure, source/claim models, reliance, trust, deference and authority. It defines scoped JudgmentEstimate, CalibrationProfile, MetacognitiveSensitivityProfile, VerificationCapabilitySurface, VerificationCase, EvidenceSufficiency and ReliancePolicy. Verification is treated as discriminative error detection and evidence acquisition rather than ritual checking; confidence is a control input rather than accuracy; appropriate/selective reliance is outcome- and consequence-relative; source reliability is not claim truth; Human-in-the-loop is not verification guarantee. The round adds advice-timing, independent-first, disagreement, escalation, stopping, evidence-value, error-asymmetry, AI-confidence and reflexivity guards. No Foundation is reopened and no engineering schema is prescribed.
evidence_status: verified-synthesis
readiness: READY
related:
  - human.operational-concepts.hoc1
  - human.foundations.hf3
  - human.foundations.hf8
  - human.foundations.hf9
  - human.foundations.hf12
  - human.deep-foundations.hd10b
---
# HOC2 — Epistemic Judgment, Verification, Calibration and Reliance

## 0. Practical-priority decision

Before assigning HOC2, remaining operational families were compared against:

```text
practical decision value
cross-domain reuse
evidence maturity
Human–Agent leverage
cost of misuse
```

Candidate families included:

```text
learning / modifiability
fatigue / regulation / recovery
trust / reliance / coordination
health / functioning
epistemic judgment / verification / calibration
```

The epistemic family wins HOC2 because it is already a binding input to HOC1 readiness, recurs across research, learning, finance, health, engineering and governance, and determines whether Agent support is amplification or uncorrected error transmission.

This does not imply the other families are less real or permanently lower priority.

---

# 1. Core deletion

Delete the common operational collapse:

```text
Human knows answer
→ Human can answer
→ Human is confident
→ Human is calibrated
→ Human can verify others
→ Human should be trusted
→ Human should decide
```

None of these arrows is identity.

Canonical guards:

```text
Judgment != Confidence
Confidence != Accuracy
Calibration != MetacognitiveSensitivity
GenerationCapability != VerificationCapability
Verification != UnderstandingTotality
Trust != Reliance
Reliance != Deference
Expertise != Authority
SourceReliability != ClaimTruth
HumanInLoop != ErrorCorrectionGuarantee
```

---

# 2. EpistemicTargetSpec

Every operational epistemic judgment needs a declared target.

```text
EpistemicTargetSpec = {
  claim_or_question,
  target_type,
  domain,
  ground_truth_or_criterion,
  consequence_profile,
  time_horizon,
  evidence_budget,
  action_deadline,
  error_asymmetry,
  source/support context
}
```

Examples of target type:

```text
binary factual claim
numeric estimate
classification
causal hypothesis
forecast
plan feasibility
output correctness
source reliability
```

One generic confidence score cannot be interpreted without the target.

---

# 3. First-order JudgmentEstimate

```text
JudgmentEstimate(H, TargetSpec, EvidenceState, t)
```

may contain:

```text
selected answer / estimate
candidate alternatives
probability or interval where meaningful
reason/evidence summary
known assumptions
unresolved conflicts
```

It is the current epistemic output.

```text
JudgmentEstimate != BeliefState by definition
JudgmentEstimate != Decision/Commitment
```

A forced estimate can be produced without stable belief.

---

# 4. ConfidenceEstimate

```text
ConfidenceEstimate(H, Judgment, TargetSpec, t)
```

answers:

```text
How strongly does H currently endorse this judgment / how uncertain is H about it?
```

Confidence is operationally useful because it can control:

```text
act
verify
seek more evidence
escalate
defer
```

But:

```text
Confidence != Correctness
```

A high-confidence error and a low-confidence correct judgment are both possible and operationally important.

---

# 5. CalibrationProfile

Calibration is not confidence level.

```text
CalibrationProfile(H, Domain, Protocol, Interval)
→ relation between expressed confidence and empirical correctness / target attainment
```

Possible surfaces:

```text
absolute calibration
calibration curve
Brier-like loss where probability forecasts are meaningful
over/under-confidence bias
calibration by difficulty
calibration by source/support condition
calibration drift over time
```

A Human may have high mean confidence and good calibration, low confidence and good calibration, or poor calibration at any confidence level.

---

# 6. MetacognitiveSensitivityProfile

Calibration and metacognitive sensitivity answer different questions.

```text
MetacognitiveSensitivityProfile(H, Domain, Protocol, Interval)
```

asks whether confidence/uncertainty discriminates correct from incorrect first-order judgments on a trial-by-trial or case-by-case basis.

Operationally:

```text
Can H tell when H is likely wrong?
```

Therefore:

```text
ConfidenceLevel
!= Calibration
!= MetacognitiveSensitivity
```

A flat confidence scale can be globally calibrated yet weak at discriminating good and bad cases.

---

# 7. Calibration is decision-use dependent

Perfect global calibration is not enough when consequence is asymmetric.

Example:

```text
99 ordinary cases low consequence
1 catastrophic case
```

A profile can appear well calibrated in aggregate while failing exactly where verification matters.

So HOC2 requires where relevant:

```text
CalibrationByConsequence
CalibrationByDifficulty
CalibrationByErrorType
```

---

# 8. VerificationCapabilitySurface

Verification is reconstructed as a distinct capability surface.

```text
VerificationCapabilitySurface_H(
  TargetFamily,
  ErrorClass,
  State,
  Support,
  EvidenceAccess,
  TimeBudget
)
→ distribution of detection / discrimination / correction performance
```

Possible dimensions:

```text
error detection rate
false alarm rate
localization quality
explanation/diagnosis quality
correction success
source/evidence discrimination
rare-error sensitivity
verification latency
verification cost
transfer to novel error classes
support dependence
```

---

# 9. VerificationCapability != GenerationCapability

Minimal counterexamples:

```text
A can write correct code but is poor at reviewing subtle security defects.
B cannot generate a proof quickly but can detect invalid inference in a supplied proof.
C cannot independently solve a medical case but can notice a contradiction between recommendation and known allergy.
```

Thus:

```text
GenerationCapability_D
!= VerificationCapability_D
```

This is central for Human–Agent role allocation.

---

# 10. Verification is not ritual checking

Weak verification:

```text
"review it"
"double-check"
"think carefully"
"does this look right?"
```

can add effort without much discrimination.

Stronger verification asks:

```text
What failure modes are plausible?
What evidence would distinguish alternatives?
What independent channel can test the claim?
What invariant should hold?
Can the result be reproduced or recalculated?
What would falsify the current answer?
```

Canonical rule:

```text
VerificationQuality
depends on discriminative evidence,
not checklist length.
```

---

# 11. VerificationCase

A practical verification event can be represented as:

```text
VerificationCase = {
  target_claim_or_output,
  source,
  claimed_confidence?,
  verifier,
  verification_goal,
  error_classes_of_interest,
  available_evidence,
  independent_channels,
  procedure,
  findings,
  remaining_uncertainty,
  result_status,
  consequence_scope,
  expiry
}
```

This is a case object, not a permanent Human attribute.

---

# 12. Verification result statuses

Avoid a naked boolean `verified=true`.

Prefer statuses such as:

```text
SUPPORTED_WITHIN_SCOPE
CONTRADICTED
PARTIALLY_SUPPORTED
UNRESOLVED
INSUFFICIENT_EVIDENCE
NOT_INDEPENDENTLY_CHECKED
OUT_OF_SCOPE
```

A consumer may compress further, but the canonical object retains scope and evidence.

---

# 13. EvidenceSufficiency

More evidence is not always required; available evidence can also be insufficient for a high-consequence decision.

```text
EvidenceSufficiency(TargetSpec, EvidenceState, DecisionRule)
```

asks:

```text
Is the current evidence adequate for the intended action and consequence level?
```

Therefore:

```text
EvidenceSufficiency
!= Truth
```

and:

```text
SameEvidence
can be sufficient for low-consequence action
and insufficient for high-consequence action.
```

---

# 14. Epistemic action modes

HOC2 retains an operational output family:

```text
ACT_ON_CURRENT_JUDGMENT
VERIFY_TARGETED
SEEK_MORE_EVIDENCE
REQUEST_INDEPENDENT_OPINION
ESCALATE_EXPERT
DEFER
REJECT_CURRENT_CLAIM
ABSTAIN_INSUFFICIENT_EVIDENCE
```

These are decision-support modes, not epistemic ontology.

---

# 15. Stopping and value of evidence

Verification/search is not free.

Continue only when expected value of additional evidence exceeds relevant cost under the downstream decision objective.

Idealized:

```text
ExpectedValueOfInformation
> time + resource + delay + opportunity + verification cost
```

HOC2 does not freeze one universal formula.

The important distinction is:

```text
MoreChecking != BetterDecision by definition
```

---

# 16. Uncertainty bottleneck from HOC1 connects directly to HOC2

HOC1 introduced `UncertaintyBottleneck`.

HOC2 provides its operational machinery:

```text
UncertaintyBottleneck
→ identify rival hypotheses
→ select discriminative evidence action
→ update Judgment / Confidence / VerificationCase
→ recompute readiness/bottleneck
```

Thus HOC1 and HOC2 form a closed practical loop.

---

# 17. SourceModel and ClaimModel must stay separate

A source can have a reliability profile:

```text
SourceReliabilityProfile(S, Domain, TaskType, Interval)
```

but:

```text
ReliableSource != AutomaticallyTrueClaim
UnreliableSource != AutomaticallyFalseClaim
```

Claim-level evidence must remain inspectable when stakes require it.

---

# 18. Provenance is operationally useful

A practical claim state may record:

```text
content
source
source type
retrieval time
supporting evidence
contradicting evidence
transformations/summaries
verification history
```

because two identical sentences can have different operational status depending on provenance and evidence.

But provenance alone is not truth.

---

# 19. Trust, Reliance, Deference and Authority

These must not collapse.

```text
Trust
= relational expectation/attitude about target-relevant partner behavior

Reliance
= behavioral use/dependence on partner output

Deference
= giving another judgment greater practical weight than one's own

Authority
= institutionally/normatively recognized decision right
```

Therefore:

```text
Trust != Reliance != Deference != Authority
```

HOC2 mainly owns epistemic reliance/deference policy; HF12/HOC relational work remains trust owner.

---

# 20. ReliancePolicy

```text
ReliancePolicy(H → Source S, TargetFamily, Context, History)
```

may specify:

```text
when advice is consulted
how much weight it receives
when independent judgment is required
when verification is mandatory
when disagreement triggers escalation
when source advice is rejected
```

Reliance is a policy/behavior, not evidence that trust is high.

---

# 21. SelectiveReliancePerformance

When ground truth is known, one useful evaluation is whether H tends to:

```text
accept beneficial/correct advice
reject harmful/incorrect advice
```

This can be summarized as `SelectiveReliancePerformance` or an application-specific `AppropriateReliance` metric.

But HOC2 guards:

```text
AppropriateReliance
requires objective/consequence definition
```

because false acceptance and false rejection may carry different costs.

---

# 22. Reliance can be rational under dependence without trust

If no viable alternative exists:

```text
Reliance = high
Trust = low
```

is coherent.

Likewise, H may trust a source but independently solve a task and therefore show low behavioral reliance.

So self-reported trust cannot substitute for reliance traces.

---

# 23. Advice timing is an operational variable

At least distinguish:

```text
AI_FIRST
HUMAN_FIRST_THEN_AI
INDEPENDENT_PARALLEL
AI_CRITIQUE_ONLY
HUMAN_CRITIQUE_OF_AI
```

Because advice timing changes:

```text
anchoring
independent evidence generation
comparison task
verification burden
learning opportunity
```

No timing is universally optimal.

---

# 24. Independent-first is a useful but non-universal guard

For some tasks:

```text
Human initial judgment
→ AI advice
→ disagreement comparison
```

preserves an independent evidence channel.

But it can be wasteful or impossible when:

```text
Human has little generation capability
time is scarce
AI is being used precisely as retrieval/tool support
```

So:

```text
IndependentFirst != UniversalBestPractice
```

---

# 25. Disagreement is information

A Human–Agent disagreement should not be treated only as a failure.

```text
DisagreementCase
```

can trigger:

```text
source re-evaluation
independent evidence
error-class search
expert escalation
uncertainty increase
```

The system should avoid silently averaging incompatible answers when consequence is high.

---

# 26. Human-in-the-loop is not a safety claim

A Human can be present yet fail to:

```text
notice the error
understand the error
have enough time
override the system
possess authority
possess independent evidence
```

Therefore:

```text
HumanInLoop
!= VerificationCapability
!= EffectiveOverrideCapability
!= Authority
!= SafetyGuarantee
```

---

# 27. Verification fragility

A joint system can have excellent average accuracy but poor readiness if:

```text
rare catastrophic errors
are precisely the errors the Human cannot detect.
```

This is a `FragilityBottleneck` from HOC1.

So verification evaluation should sample relevant error classes, not only average outputs.

---

# 28. AI confidence cues are inputs, not truth

AI/system confidence can affect Human reliance.

HOC2 separates:

```text
AIConfidenceLevel
AICalibration
AIMetacognitiveSensitivity
HumanInterpretationOfAIConfidence
HumanRelianceResponse
```

A high-confidence wrong AI output is especially dangerous when Human reliance is confidence-responsive.

---

# 29. AI calibration versus AI metacognitive sensitivity

An AI confidence system can be:

```text
well calibrated in aggregate
but poor at discriminating its correct and incorrect cases
```

or vice versa.

Recent formal/empirical Human–AI work reinforces that metacognitive sensitivity is a distinct determinant of joint accuracy.

Therefore:

```text
AIAccuracy
!= AICalibration
!= AIMetacognitiveSensitivity
```

---

# 30. Human metacognition can degrade under AI support

Improved task performance under AI does not imply improved self-monitoring.

HOC2 therefore separates:

```text
JointTaskPerformance
HumanSelfAssessmentAccuracy
HumanMetacognitiveSensitivity
```

and prohibits using AI-assisted correctness as evidence that the Human knows when the system is wrong.

---

# 31. Confidence cue contamination

Observed Human confidence under AI support can partly reflect:

```text
own evidence
AI answer
AI confidence display
source framing
prior attitudes
social/anthropomorphic cues
```

So:

```text
HumanConfidenceWithAI
!= PureIndependentMetacognition
```

A calibration profile should name the support/advice regime.

---

# 32. Metacognition and information search

Metacognitive sensitivity is operationally relevant not only after a decision.

It can influence:

```text
what evidence to search
when to stop searching
when to request help
```

This supports HOC2's use of confidence/uncertainty as a control signal rather than a decorative report.

---

# 33. VerificationProcedure families

HOC2 does not force one procedure but retains common families:

```text
independent reproduction
alternative-method recomputation
source/provenance check
constraint/invariant check
counterexample/falsifier search
adversarial review
cross-source triangulation
unit/scale/range check
simulation/test execution
expert second opinion
support-removal check
```

The best procedure depends on error class and target.

---

# 34. Verification should target likely failure modes

Generic checking wastes attention.

A better procedure begins with:

```text
ErrorModel(Target, Source, Context)
```

Examples:

```text
LLM factual hallucination
wrong unit
stale information
hidden assumption
unsupported causal leap
off-by-one implementation
permission mismatch
confident but fabricated citation
```

Then selects discriminative tests.

---

# 35. Error asymmetry

A verifier can be good at catching false positives and poor at false negatives, or vice versa.

Therefore:

```text
VerificationCapability
must preserve error class / consequence asymmetry
```

where material.

This directly affects readiness thresholds.

---

# 36. Verification cost and depth

Retain at least three practical depths:

```text
LIGHT_CHECK
TARGETED_CHECK
INDEPENDENT_RECONSTRUCTION
```

These correspond to increasing independence/cost, not guaranteed certainty.

High-consequence tasks may require deeper verification; low-consequence reversible tasks may rationally use lighter checks.

---

# 37. Epistemic escalation ladder

A useful action ladder is:

```text
accept
light-check
targeted-check
independent reproduce
seek second source
seek expert
abstain / stop
```

The ladder should be selected by consequence, uncertainty, evidence availability and cost.

---

# 38. Verification does not grant authority

A Human may verify that a model output is factually correct while lacking the authority to execute it.

Likewise an expert may have epistemic weight without institutional decision rights.

```text
VerificationSuccess
!= ExecutionAuthority
```

---

# 39. EpistemicRoleProfile

For Human–Agent collaboration, a useful scoped role profile may distinguish:

```text
generation
retrieval
judgment
verification
error diagnosis
uncertainty estimation
source evaluation
final synthesis
escalation
```

This is more actionable than `Human is expert` or `AI is smarter`.

---

# 40. Complementarity is role-specific

Human–Agent complementarity can arise even when one side has lower average accuracy if it has useful metacognitive sensitivity or catches different error classes.

Thus:

```text
BestIndividualAccuracy
!= BestTeamComposition by definition
```

Joint-system design should evaluate complementary error and uncertainty structure.

---

# 41. Minimal counterexamples

## C1 — high accuracy, poor calibration

H is usually correct but cannot identify the rare cases where H is wrong.

High first-order performance does not imply good verification allocation.

## C2 — low generation, high verification

H cannot generate a complex answer but can discriminate valid from invalid outputs with evidence.

Do not remove H from the loop solely because generation is weak.

## C3 — high confidence, wrong

Confidence cannot be action authority without calibration/verification evidence.

## C4 — low confidence, correct

Low confidence may rationally trigger verification while the underlying judgment is correct.

## C5 — trusted source, false claim

Source reputation does not settle claim truth.

## C6 — distrusted source, true claim

Rejecting by source identity alone can lose correct information.

## C7 — high trust, low reliance

H trusts S but has independent capability and does not need S for this task.

## C8 — low trust, high reliance

H depends on S because no alternative exists.

## C9 — Human present, no effective verification

Human reviews output but lacks time/evidence/error model.

`HumanInLoop` is not a substantive safety condition.

## C10 — AI raises performance, lowers metacognitive accuracy

Joint task success can coexist with poorer self-assessment.

---

# 42. Evidence ladder for VerificationCapability

Approximate operational ordering:

```text
V0 self-report: "I can check this"
V1 detects obvious seeded errors
V2 repeated known error classes
V3 mixed correct/incorrect blind trials
V4 novel error variants
V5 realistic time/resource constraints
V6 adversarial/rare critical errors
V7 independent verification under changed tools/sources
V8 consequential field history
```

Do not infer broad verification capability from one easy review task.

---

# 43. Calibration evidence ladder

```text
C0 one confidence statement
C1 repeated confidence + outcome pairs
C2 adequate difficulty range
C3 calibration by error class
C4 calibration under changed support/source conditions
C5 temporal stability/drift
C6 consequential naturalistic history
```

The calibration claim is always protocol/domain scoped.

---

# 44. Update / expiry

## JudgmentEstimate

Update with material new evidence or changed target.

## ConfidenceEstimate

Fast-expiring; update with evidence, state or support changes.

## CalibrationProfile

Slow/intermediate; update from repeated scored cases, detect drift.

## MetacognitiveSensitivityProfile

Requires repeated cases and should not jump from one error.

## VerificationCapabilitySurface

Update after varied blind verification evidence, transfer/support changes or persistent learning/decline.

## ReliancePolicy

Update when source reliability, support regime, consequence or Human capability changes.

---

# 45. Reflexivity

Epistemic systems shape future Human evidence.

Examples:

```text
Agent always answers first
→ Human independent judgment practice falls
→ future verification may weaken

system labels Human as poorly calibrated
→ forces extra checking
→ observed error rates change

AI confidence display
→ Human reliance changes
→ confidence/reliance evidence becomes policy-dependent
```

Therefore:

```text
ObservedEpistemicBehavior
may be intervention-produced.
```

---

# 46. Normative firewall

```text
BetterCalibration != GreaterMoralWorth
Expertise != Authority
VerificationCapability != RightToControl
LowMetacognitiveSensitivity != JustificationForPaternalism
RelianceMetric != Consent
PredictionOfError != PermissionToExclude
```

HOC2 informs epistemic allocation; governance/rights remain elsewhere.

---

# 47. Foundation dependency map

```text
HF3  metacognition / confidence / control
HF7  memory / retrieval / source memory
HF8  knowledge / provenance / understanding
HF9  judgment / causal inference / evidence search
HF10 decision / stopping / commitment
HF11 execution / tool use / calibration
HF12 trust / reliance / joint action / roles
HF13 authority / institution
HF17 governance / legitimacy
HD10-B measurement / evidence ceilings
HD10-D ability / support boundaries
HD10-E scoped projections
HOC1 readiness / bottleneck / verification requirement
```

No new Foundation is required.

---

# 48. Canonical forbidden inferences

```text
Confidence != Accuracy
Calibration != MetacognitiveSensitivity
Judgment != Confidence
Judgment != Belief by definition
Judgment != Decision
Knowledge != CurrentRecall
SourceReliability != ClaimTruth
Trust != Reliance
Reliance != Deference
Deference != Authority
VerificationCapability != GenerationCapability
VerificationSuccess != UnderstandingTotality
VerificationSuccess != Authority
HumanInLoop != ErrorCorrectionGuarantee
AIAssistedAccuracy != HumanMetacognitiveAccuracy
AIConfidence != AICorrectness
AIAccuracy != AICalibration
AICalibration != AIMetacognitiveSensitivity
HighAverageAccuracy != LowCatastrophicErrorRisk
MoreChecking != BetterDecision
Explanation != Verification
Warning != Calibration
```

---

# 49. Operational reasoning grammar

A Human-supporting Agent can use HOC2 as:

```text
1. Declare EpistemicTargetSpec.
2. Record current JudgmentEstimate before/after external advice as needed.
3. Capture ConfidenceEstimate separately.
4. Identify consequence/error asymmetry.
5. Project Calibration / MetacognitiveSensitivity only if evidence supports it.
6. Determine VerificationReadiness from HOC1 + VerificationCapabilitySurface.
7. Select verification depth and error model.
8. Run discriminative VerificationCase.
9. Return scoped status + remaining uncertainty.
10. Decide whether to act, seek evidence, escalate, defer or abstain.
11. Update reliance policy from outcome history without converting it into global trust.
12. Preserve support/advice regime so future calibration evidence remains interpretable.
```

This is a reasoning grammar, not a mandatory workflow engine.

---

# 50. HOC2 stop rule

HOC2 is complete because it has:

```text
separated judgment, confidence, calibration and metacognitive sensitivity;
reconstructed verification as a distinct support/task/error-class capability surface;
separated generation and verification;
reconstructed verification cases, scoped results and evidence sufficiency;
made confidence/uncertainty a control variable for evidence search and stopping;
separated source reliability from claim truth;
separated trust, reliance, deference and authority;
reconstructed reliance as a policy and selective-reliance performance as an outcome metric;
made advice timing and disagreement explicit operational variables;
rejected Human-in-loop as a verification guarantee;
added error-model, asymmetry, verification-depth and escalation grammar;
incorporated AI confidence / calibration / metacognitive sensitivity distinctions;
added update/expiry/reflexivity/normative firewalls;
and connected HOC2 directly to HOC1 readiness and uncertainty bottlenecks.
```

No Foundation reopen condition is triggered.

```text
FoundationReopenCondition(HF0–HF23) = false
NextDeepRoute = UNKNOWN
```

HOC2 does not preselect HOC3.
