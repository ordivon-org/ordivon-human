---
schema_version: 1
id: human.operational-concepts.hoc3
title: HOC3 — Learning, Retention, Transfer, Modifiability and Scaffolding
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
summary: Reconstructs the practical Human learning layer downstream of frozen Human Foundations and HOC1/HOC2. HOC3 separates immediate practice performance, acquisition, delayed retention, transfer/generalization, relearning/savings, current capability and protocol-relative modifiability. It introduces LearningObjectiveSpec, LearningTargetSpec, LearningEvidenceBundle, LearningTrajectory, RetentionProfile, TransferSurface, ModifiabilityProfile, SupportDependenceTrajectory, LearningProgressView, TargetAttainmentEvidence, PracticeChallengeProfile, ScaffoldingPolicy and NextBestLearningAction. It treats tests/retrieval as potentially both measurements and interventions; subjective fluency and confidence as distinct from durable learning; support as potentially amplifying, scaffolding, substituting or deskilling; and support fading/tool removal as diagnostic when independent capability matters. It rejects one universal progress/mastery score, one global learning rate, practice quantity as learning, and the assumption that harder practice is always better. No Foundation is reopened and no engineering schema is prescribed.
evidence_status: verified-synthesis
readiness: READY
related:
  - human.operational-concepts.hoc1
  - human.operational-concepts.hoc2
  - human.foundations.hf6
  - human.foundations.hf7
  - human.deep-foundations.hd10d
---
# HOC3 — Learning, Retention, Transfer, Modifiability and Scaffolding

## 0. Practical-priority decision

Remaining HOC families were compared again by:

```text
practical decision value
cross-domain reuse
evidence maturity
Human–Agent leverage
misuse cost
```

Learning/modifiability wins HOC3 over regulation/recovery, trust/coordination and health/functioning because it directly controls a recurring Agent decision:

```text
help Human finish now?
help Human learn for later?
measure what is retained?
probe transfer?
fade support?
delegate instead of train?
```

The winning feature is temporal leverage:

```text
Support_t
can change both
Performance_t
and
IndependentCapability_{t+1}
```

These effects can point in different directions.

---

# 1. Core deletion

Reject the common chain:

```text
more practice
→ better practice performance
→ learning
→ retention
→ transfer
→ mastery
→ future capability
```

Every arrow requires evidence.

Canonical guards:

```text
Practice != Learning
PracticePerformance != RetainedLearning
Acquisition != Retention
Retention != Transfer
NearTransfer != FarTransfer
MorePractice != MoreTransfer
CurrentPerformance != Modifiability
AssistedPerformanceGain != IndependentLearningGain
SubjectiveFluency != DurableLearning
LearningProgress != ActivityCount
MasteryScore != HumanEssence
```

---

# 2. LearningObjectiveSpec

Operational learning cannot be optimized without declaring what change is desired.

```text
LearningObjectiveSpec = {
  target_domain,
  target_capability,
  independence_requirement,
  retention_horizon,
  transfer_targets,
  performance_criterion,
  reliability_criterion,
  acceptable_support,
  learning_deadline?,
  practice_budget?,
  consequence_profile?,
  maintenance_requirement?
}
```

Different objectives can conflict:

```text
maximize immediate task success
maximize durable independent retention
maximize broad transfer
minimize time-to-competence
maintain joint Human–Agent productivity
preserve verification capability
```

No single learning metric optimizes all of them.

---

# 3. LearningTargetSpec

A target must be typed.

```text
LearningTargetSpec = {
  task_family,
  knowledge/skill/strategy/representation target,
  prerequisite structure,
  target difficulty region,
  target contexts,
  target support boundary,
  transfer distance,
  evaluation protocol
}
```

Examples:

```text
remember factual relations
execute a motor/procedural skill
recognize a concept/category
solve a class of problems
verify a class of errors
coordinate a task role
```

Do not treat these as one learning mechanism.

---

# 4. LearningEvent

A learning-relevant event can be represented as:

```text
LearningEvent = {
  task/content,
  learner state,
  action/attempt,
  support,
  feedback,
  outcome,
  error class,
  retrieval demand,
  difficulty,
  spacing/history,
  time,
  confidence/fluency,
  consequence
}
```

A single event is evidence about exposure/performance, not proof of persistent learning.

---

# 5. LearningEvidenceBundle

```text
LearningEvidenceBundle(H, TargetSpec, interval) = {
  baseline evidence,
  acquisition curve,
  delayed retention,
  transfer/generalization,
  support-removal performance,
  relearning/savings,
  error-profile change,
  strategy/representation change,
  confidence/calibration change,
  authentic-task evidence,
  uncertainty
}
```

Not every domain needs every channel.

The bundle prevents one immediate metric from becoming `learning` by definition.

---

# 6. AcquisitionCurve

```text
AcquisitionCurve
```

tracks change during the learning/practice episode.

It can include:

```text
accuracy
latency
quality
error types
support required
attempt count
```

but:

```text
AcquisitionImprovement
!= DurableLearning
```

because temporary feedback, working memory, cueing, task familiarity and support can improve acquisition without surviving delay/removal.

---

# 7. RetentionProfile

```text
RetentionProfile(H, Target, DelaySchedule, RetrievalConditions)
```

asks what remains available after time/interference and under which retrieval conditions.

Possible fields:

```text
retention at delay d
retrieval latency
cue dependence
error recurrence
confidence
support requirement
change-point / decay uncertainty
```

Avoid one universal forgetting-rate parameter unless evidence supports that model for the target.

---

# 8. Retention is endpoint-relative

A learned structure may be retained in one form but not another.

Examples:

```text
recognition retained, free recall weak
trained motor sequence retained, transfer weak
concept recognition retained, explanation poor
```

Therefore:

```text
Retention_D != Retention_E
```

and `forgotten=true` is usually too coarse.

---

# 9. TransferSurface

```text
TransferSurface_H(
  LearnedTarget,
  NewTask/ContextDimensions,
  SupportBoundary,
  interval
)
→ effect of prior learning on new performance / learning
```

Useful dimensions can include:

```text
stimulus variation
representation change
context change
task-rule change
domain distance
novelty
support removal
partner/tool change
```

Transfer is a surface, not `yes/no`.

---

# 10. Transfer is a capability falsifier

A strong claim that training produced broad capability should survive relevant transfer tests.

But:

```text
TransferFailure
!= NoLearning
```

It contracts the scope of the learning/capability claim.

This protects highly specific but genuine expertise from being mislabeled as no learning.

---

# 11. Relearning / SavingsProfile

Loss of overt performance does not prove all prior change is gone.

```text
SavingsProfile(H, Target, RelearningProtocol)
```

can track:

```text
faster reacquisition
less support required
fewer errors
faster return to criterion
```

This is useful when retention tests look weak but prior learning may still affect future reacquisition.

---

# 12. LearningTrajectory — canonical operational object

```text
LearningTrajectory_H(Target, Protocol, interval)
```

integrates evidence across time without forcing one scalar.

A practical trajectory can include:

```text
baseline
acquisition
retention
transfer
relearning/savings
support dependence
error-profile evolution
confidence/calibration
practice exposure
```

Trajectory is a view over evidence, not a hidden inner learning substance.

---

# 13. ModifiabilityProfile

Current capability and response to intervention are separate.

```text
ModifiabilityProfile_H(Target | InterventionProtocol I, interval T) = {
  gain under I,
  support/hints required,
  learning rate within I,
  strategy change,
  delayed retention,
  transfer,
  error correction,
  support-fading response,
  uncertainty
}
```

Canonical guard:

```text
Modifiability_I
!= FixedPotential
```

A person can be highly modifiable under one protocol and weakly responsive under another.

---

# 14. Same baseline, different learning response

Minimal counterexample:

```text
A and B score 50 at baseline.
After structured feedback:
A reaches 85 and retains 80.
B reaches 70 and retains 52.
```

One baseline ability coordinate cannot substitute for the modifiability trajectory.

```text
SameCurrentCapability
!= SameFutureLearningTrajectory
```

---

# 15. LearningRate is protocol-relative

Do not store:

```text
H.learning_rate = 0.8
```

without qualification.

Prefer:

```text
LearningRate(H, Target, Protocol, Region, Interval)
```

because learning rate can change with:

```text
prior knowledge
state/fatigue
feedback
practice schedule
task difficulty
support
motivation
```

---

# 16. Subjective fluency is not learning

Practice can feel easy because of:

```text
recent exposure
blocked examples
recognition cues
answer availability
repeated study
AI generation
```

while delayed retention/transfer remains weak.

Conversely, effortful retrieval/interleaving can feel worse during practice while producing stronger delayed performance in some tasks.

Thus:

```text
EaseOfPractice
!= LearningQuality
```

and:

```text
ConfidenceDuringPractice
!= RetainedCapability
```

---

# 17. PracticeDifficulty is not inherently good

HOC3 rejects a simplistic `harder = better` rule.

```text
Difficulty
can improve learning under some conditions
or simply produce failure/noise/frustration under others.
```

Therefore:

```text
PracticeDifficulty
!= DesirableDifficulty by definition
```

Difficulty is valuable only relative to target, prior skill, feedback, retention/transfer objective and learner state.

---

# 18. PracticeChallengeProfile

A useful operational object is:

```text
PracticeChallengeProfile(H, Target, TaskSet, Support)
```

which can describe:

```text
success/error region
retrieval effort
hint dependence
latency
error informativeness
frustration/fatigue cost
transfer opportunity
```

The goal is not a universal optimal difficulty percentage.

The goal is to select practice that creates informative, learnable errors and target-relevant change.

---

# 19. RetrievalProbe has two roles

A retrieval attempt can be:

```text
measurement
```

and simultaneously:

```text
learning intervention
```

So:

```text
AssessmentEvent
!= PureObservation by default
```

This matters for adaptive systems because the act of measuring knowledge can alter later retention.

---

# 20. Retrieval evidence

Primary experimental evidence shows that repeated retrieval/testing can improve delayed retention compared with repeated study in some verbal-learning settings; related work shows benefits can extend to transfer under studied conditions.

HOC3 therefore permits:

```text
RETRIEVAL_PROBE
```

as both evidence collection and learning action.

But it does not infer:

```text
retrieval practice is universally optimal
```

across every target/domain.

---

# 21. Feedback is not one thing

A feedback event can differ in:

```text
timing
correct-answer provision
error explanation
hint level
confidence targeting
specificity
actionability
source
```

Therefore:

```text
FeedbackPresent
!= FeedbackEffective
```

and feedback should be represented as part of the protocol, not as a Boolean.

---

# 22. Error can be useful evidence

A failed attempt can identify:

```text
missing prerequisite
misconception
retrieval failure
strategy error
discrimination failure
execution error
```

and, when followed by useful feedback, can contribute to learning.

Thus:

```text
PracticeError
!= LearningFailure by definition
```

But repeated uncorrected error can also stabilize the wrong response.

---

# 23. LearningBottleneckInference

HOC1 BottleneckInference can specialize to learning:

```text
LearningBottleneckInference(H, Target, Objective, t)
```

candidate bottlenecks include:

```text
missing prerequisite knowledge
retrieval weakness
poor discrimination
conceptual representation gap
procedural/skill deficit
feedback insufficiency
practice too narrow
transfer distance
state/fatigue
motivation/goal conflict
support overdependence
poor calibration
insufficient practice opportunity
```

Do not collapse these into `low aptitude`.

---

# 24. LearningProgressView

`Progress` is useful, but only as an operational compression.

```text
LearningProgressView = {
  target,
  baseline,
  current acquisition,
  retention evidence,
  transfer evidence,
  support dependence,
  target gap,
  uncertainty,
  trend,
  evidence age
}
```

Canonical guard:

```text
LearningProgress
!= SessionCount
!= TimeSpent
!= CompletionRate
```

Activity can support progress evidence but does not define it.

---

# 25. TargetAttainmentEvidence instead of universal mastery

`Mastery` is useful in applications but dangerous when treated as one global status.

Prefer:

```text
TargetAttainmentEvidence(H, TargetSpec, CriterionSpec)
```

with statuses such as:

```text
NOT_YET_DEMONSTRATED
DEMONSTRATED_WITH_SUPPORT
DEMONSTRATED_INDEPENDENTLY
RETAINED_AT_DELAY
TRANSFER_DEMONSTRATED
FRAGILE / INSUFFICIENT_EVIDENCE
```

A UI may call some of these `mastered`, but the canonical evidence remains typed.

---

# 26. SupportDependenceTrajectory

Agent/tool support can change both performance and learning.

```text
SupportDependenceTrajectory(H, Target, Support S, interval)
```

tracks:

```text
performance with support
performance without support
support frequency/intensity
hint depth
support-removal response
retention
transfer
```

This helps distinguish:

```text
Amplification
Scaffolding
Substitution
Deskilling/Dependency
```

from HOC1 across time.

---

# 27. ScaffoldingPolicy

A scaffold is support intended to enable learning/independent performance, not merely complete the current task.

```text
ScaffoldingPolicy(H, Target, Objective) = {
  support type,
  trigger,
  intensity,
  learner action required,
  feedback rule,
  fading criterion,
  transfer probe,
  failure/escalation rule
}
```

Possible support types:

```text
cue
hint
partial step
worked example
question
retrieval prompt
error feedback
critique
external memory
AI explanation
AI generation
```

These are not equivalent.

---

# 28. Support fading is a diagnostic operation

If independent capability is an objective, periodically reducing/removing support can answer:

```text
What remains without S?
```

This is not always required.

If the true objective is durable joint-system performance and the support is reliably available, forcing full independence may be wasteful.

Therefore:

```text
SupportFadingRequirement
is objective-relative.
```

---

# 29. Learning versus delegation

A practical Agent must sometimes choose:

```text
teach / scaffold
```

versus:

```text
delegate / automate
```

A useful comparison depends on:

```text
future recurrence of task
value of independent capability
learning cost
current deadline
support reliability
verification need
transfer value
risk of deskilling
authorship/responsibility needs
```

There is no universal rule that Human should learn every delegable task.

---

# 30. Delegation can be rational and still create learning debt

When Human stops practicing a capability because a tool handles it:

```text
joint capability may rise
independent capability may remain stable, grow, or decline
```

HOC3 does not moralize this.

It records the tradeoff when independence/recovery matters.

A consumer may track:

```text
IndependentCapabilityMaintenanceRisk
```

without calling all delegation `deskilling`.

---

# 31. AI answer provision and AI tutoring are different support policies

`AI support` is too coarse.

Distinguish at least:

```text
ANSWER_PROVISION
HINTING
SOCRATIC_QUESTIONING
ERROR_FEEDBACK
CRITIQUE
RETRIEVAL_SUPPORT
EXAMPLE_GENERATION
PLANNING_SUPPORT
```

These change Human practice and error distributions differently.

---

# 32. Agent support can increase current performance while harming independent learning

HOC1 already retained primary randomized evidence that unconstrained GPT support can improve assisted practice while producing worse later unaided performance under studied conditions, whereas guardrailed tutoring mitigated that effect.

HOC3 consumes that result as a design pressure:

```text
OptimizeImmediateSuccess
!= OptimizeIndependentLearning
```

---

# 33. Agent support can also scaffold Human expertise

Field evidence from Tutor CoPilot shows that AI can support tutors' in-the-moment pedagogical decisions and improve student learning outcomes under a specific tutoring deployment.

HOC3 uses this to retain another possibility:

```text
Agent support
can improve a Human's effective teaching behavior
without replacing the Human role.
```

But the effect should not be generalized to every support design or every domain.

---

# 34. NextBestLearningAction

A central HOC3 operational output is:

```text
NextBestLearningAction(H, Target, Objective, EvidenceState, Constraints)
```

Candidate actions include:

```text
ATTEMPT_UNAIDED
RETRIEVAL_PROBE
STUDY_EXAMPLE
REVIEW_EXPLANATION
REQUEST_HINT
PROVIDE_HINT
PROVIDE_FEEDBACK
PRACTICE_VARIATION
INTERLEAVE_CATEGORIES
SPACE_REVIEW
REDUCE_DIFFICULTY
INCREASE_CHALLENGE
FADE_SUPPORT
SUPPORT_REMOVAL_TEST
DELAYED_RETENTION_TEST
NOVEL_TRANSFER_TEST
RELEARNING_PROBE
REST/DEFER_STATE
DELEGATE_FOR_NOW
STOP_TARGET_ATTAINED_WITHIN_SCOPE
```

HOC3 does not assert every action applies to every target.

---

# 35. NextBestLearningAction is objective-relative

Example:

```text
Deadline = 10 minutes
Task unlikely to recur
```

best action may be:

```text
DELEGATE_FOR_NOW
```

while:

```text
Task recurs daily
Independent verification critical
```

may justify:

```text
PRACTICE + SUPPORT_FADING + TRANSFER_TEST
```

So:

```text
BestLearningAction
!= BestImmediateTaskAction
```

---

# 36. Spacing/interleaving are candidates, not commandments

Primary experiments show that spaced/interleaved presentation can improve retention or category induction in particular paradigms, sometimes despite learners judging blocked/massed practice as more effective.

HOC3 retains:

```text
spacing
interleaving
```

as candidate practice operators.

But:

```text
SpacingAlwaysBetter = rejected
InterleavingAlwaysBetter = rejected
```

because benefit depends on target structure, discrimination requirements, interval and outcome.

---

# 37. Learner preference is not learning effectiveness

A learner may prefer:

```text
answers
blocked examples
fluent restudy
low-error practice
```

because they feel easier.

That preference is useful UX evidence but cannot by itself select the learning protocol.

```text
PreferredLearningActivity
!= MostEffectiveLearningActivity
```

Nor does the reverse imply learner preference should be ignored; motivation and adherence matter.

---

# 38. Learning efficiency needs a denominator

Do not use `learning efficiency` naked.

Possible definitions include:

```text
retained gain / practice time
transfer gain / practice time
criterion attainment / attempts
independent gain / support cost
```

Different definitions rank interventions differently.

---

# 39. LearningOpportunity and exposure

Observed learning depends partly on whether practice opportunities occurred.

```text
NoObservedGain
```

can reflect:

```text
low modifiability
poor protocol
insufficient exposure
state interference
wrong target measurement
```

Therefore:

```text
NoGainUnderI
!= NoCapacityToLearn
```

---

# 40. Calibration joins HOC3

HOC2 confidence/calibration becomes useful in learning because Humans can misjudge what they have retained.

A learning system should distinguish:

```text
PerformanceEstimate
Confidence
ActualDelayedRetention
```

and use mismatch as evidence for practice selection.

---

# 41. Verification learning is a first-class target

A Human may not need to independently generate every output but may need to learn to:

```text
recognize plausible failure
check evidence
spot contradictions
escalate uncertainty
```

Therefore HOC2 `VerificationCapabilitySurface` can itself be a HOC3 LearningTarget.

This is especially important in Human–Agent systems.

---

# 42. Error-profile learning

Improvement should not be summarized only by average accuracy.

A useful trajectory can ask:

```text
Which errors disappeared?
Which persist?
Which new errors emerged?
Are severe errors becoming rarer?
Is speed improvement creating new error classes?
```

This connects HOC3 to HOC2 consequence-sensitive verification.

---

# 43. Learning can be maladaptive relative to a different objective

Learning is experience-dependent change, not necessarily improvement.

Examples:

```text
bad habit acquisition
maladaptive avoidance
overfitting to benchmark cues
learning to exploit test format
AI dependency
```

So:

```text
LearningOccurred
!= DesiredCapabilityImproved
```

LearningObjectiveSpec must own the value criterion.

---

# 44. Benchmark learning / overfitting guard

Repeated success on a narrow benchmark can reflect:

```text
memorization
format adaptation
cue exploitation
strategy specialization
```

without broad transfer.

Therefore:

```text
BenchmarkGain
!= BroadCapabilityGain
```

Use novel-transfer and changed-representation probes when broad capability is claimed.

---

# 45. Learning status modes

A practical output can use modes such as:

```text
BASELINE_ONLY
ACQUIRING
ACQUIRED_NOT_YET_RETAINED
RETAINED_NARROW
TRANSFER_PARTIAL
TRANSFER_ROBUST
SUPPORT_DEPENDENT
RELEARNING_EVIDENCE
DECLINING / DECAYING
INSUFFICIENT_EVIDENCE
```

These are operational summaries, not fundamental learning states.

---

# 46. Update rules

## LearningTrajectory

Update with meaningful practice/intervention and delayed evidence.

## RetentionProfile

Update on delayed probes; avoid rewriting from immediate performance.

## TransferSurface

Update only with materially new transfer conditions.

## ModifiabilityProfile

Update after enough intervention-response evidence; protocol-specific.

## SupportDependenceTrajectory

Update when support intensity/type or support-removal evidence changes.

## LearningProgressView

Can update frequently but must preserve whether evidence is acquisition-only versus delayed/transfer evidence.

---

# 47. Expiry / staleness

Learning evidence can become stale when:

```text
long non-use interval
major health/state change
major task/tool change
new domain requirements
support ecology changes
```

But staleness does not prove capability vanished.

A stale profile should trigger new evidence, not automatic downgrade to zero.

---

# 48. Reflexivity

Adaptive learning systems create the evidence they later observe.

```text
system predicts low ability
→ gives easier tasks
→ fewer difficult-transfer observations
→ model continues predicting low ability
```

or:

```text
system provides every answer
→ immediate success rises
→ independent attempts disappear
→ future independent evidence worsens
```

Thus:

```text
LearningData
is policy-conditioned.
```

Exposure/support history must be retained where material.

---

# 49. Avoid self-fulfilling aptitude labels

HOC3 therefore rejects using a low `aptitude` estimate to permanently reduce opportunity.

Aptitude, if used, remains:

```text
Aptitude_D(H | target, horizon, support, opportunity)
```

with active exploration/probe opportunities where consequence permits.

---

# 50. Normative firewall

```text
SlowLearning != LowMoralWorth
LowCurrentModifiabilityUnderI != NoRightToLearn
PredictedLowReturn != LegitimateExclusion
LearningOptimization != PermissionToManipulate
HighCapability != DutyToPerform
SupportDependence != PersonalFailure
```

Education/work/governance rights remain downstream.

---

# 51. Foundation dependency map

```text
HF3  attention / metacognition / confidence / control
HF4  motivation / effort / goal maintenance
HF5  fatigue / state / recovery
HF6  learning / adaptation / transfer
HF7  retention / forgetting / retrieval / interference
HF8  knowledge / understanding
HF9  reasoning / problem solving
HF10 planning / decision / exploration
HF11 skill / execution / tool support
HF12 teaching / social learning / joint action
HF20 perception / active sampling
HD4  social learning / teaching / culture
HD10-D modifiability / capability surfaces
HD10-E scoped trajectories / support projections
HOC1 capability / readiness / bottleneck
HOC2 confidence / verification / calibration
```

No new Foundation is required.

---

# 52. Canonical forbidden inferences

```text
Practice != Learning
PracticePerformance != RetainedLearning
Acquisition != Retention
Retention != Transfer
Specificity != NoLearning
MorePractice != MoreTransfer
EaseOfPractice != LearningQuality
ConfidenceDuringPractice != RetainedCapability
CurrentCapability != Modifiability
Modifiability_I != FixedPotential
LearningRate_I != GlobalLearningRate
FeedbackPresent != FeedbackEffective
PracticeError != LearningFailure
TransferFailure != NoLearning
LearningProgress != ActivityCount
TargetAttainment != PersonEssence
AssistedPerformanceGain != IndependentLearningGain
SupportDependence != Deskilling by definition
AIUse != LearningGain
BenchmarkGain != BroadCapabilityGain
PreferredLearningActivity != MostEffectiveLearningActivity
NoGainUnderI != NoCapacityToLearn
LearningOccurred != DesiredCapabilityImproved
```

---

# 53. Operational reasoning grammar

A Human-supporting Agent can use HOC3 as:

```text
1. Declare LearningObjectiveSpec and LearningTargetSpec.
2. Establish baseline capability/evidence.
3. Choose whether immediate task success or future learning dominates.
4. Project current LearningTrajectory / Modifiability evidence.
5. Diagnose LearningBottleneckInference if needed.
6. Choose NextBestLearningAction.
7. Record support/feedback/practice details.
8. Avoid judging learning from practice performance alone.
9. Schedule/collect delayed retention evidence when durable learning matters.
10. Probe relevant transfer when broad capability is claimed.
11. Fade/remove support when independence is an objective.
12. Update SupportDependenceTrajectory.
13. Recompute HOC1 CapabilitySurface/Readiness and HOC2 VerificationCapability as learning changes.
14. Stop, maintain, delegate or continue according to the declared objective.
```

This is a reasoning grammar, not a mandatory tutoring workflow.

---

# 54. HOC3 stop rule

HOC3 is complete because it has:

```text
separated practice, acquisition, retention, transfer, relearning and current performance;
reconstructed LearningObjectiveSpec and LearningTargetSpec;
reconstructed LearningEvidenceBundle and LearningTrajectory;
made RetentionProfile and TransferSurface explicit;
retained protocol-relative ModifiabilityProfile without hidden potential;
reconstructed LearningProgress as evidence-bound compression;
replaced universal mastery with TargetAttainmentEvidence;
reconstructed SupportDependenceTrajectory and ScaffoldingPolicy;
made support fading/removal objective-relative diagnostic tools;
formalized learning-vs-delegation tradeoffs;
separated AI answer provision from tutoring/scaffolding modes;
introduced NextBestLearningAction;
kept spacing/interleaving/retrieval/feedback as conditional operators rather than universal rules;
made subjective fluency/preferences distinct from durable learning;
connected calibration and verification learning from HOC2;
added benchmark-overfitting, exposure/reflexivity and self-fulfilling-label guards;
and preserved normative/authority boundaries.
```

No Foundation reopen condition is triggered.

```text
FoundationReopenCondition(HF0–HF23) = false
NextDeepRoute = UNKNOWN
```

HOC3 does not preselect HOC4.
