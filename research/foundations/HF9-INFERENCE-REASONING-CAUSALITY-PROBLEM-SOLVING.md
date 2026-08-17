---
schema_version: 1
id: human.foundations.hf9
title: HF9 — Inference, Reasoning, Causality, Counterfactuals, Judgment and Problem Solving
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
summary: HF9 reconstructs Human transformations over representations. It separates inference from retrieval/association, reasoning from formal logic and normative criteria, deduction/induction/abduction/analogy, Type1-like and Type2-like process properties, working-memory constraints from reasoning identity, probabilistic reasoning from presentation format, heuristics from irrationality, judgment from decision, observation from intervention, prediction/correlation from causality, counterfactual simulation from causal truth, analogy into access/mapping/adaptation, problem representation from problem statement, search from problem solving, insight from Aha experience, expertise from general rationality, and AI-assisted judgment from independent reasoning. The residual is sequential option selection and commitment: decision, choice, planning, strategy, exploration/exploitation, stopping and commitment.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
  - HF9
related:
  - human.foundations.hf8
  - human.foundations.hf9.sources
  - human.foundations.hf9.continuation
---
# HF9 — Inference, Reasoning, Causality, Counterfactuals, Judgment and Problem Solving

## 0. Status and question

HF8 ended with a representational/epistemic architecture:

```text
Representation
Belief
Knowledge
Concept
Schema
Mental/World Model
Understanding
```

but left unanswered:

```text
Given E, why infer P?
Given P and Q, what follows?
Which explanation is better?
Did X cause Y?
What would happen if X changed?
How does an old solution apply to a new problem?
How is a new problem searched and re-represented?
```

HF9 therefore asks:

> **How does a Human transform one set of representations into another by
> inference, reasoning, causal/counterfactual modeling, judgment and problem
> solving?**

HF9 attacks these collapses:

```text
Inference = retrieval
Reasoning = formal logic
Logical error = irrational mechanism
Heuristic = bias
Probability error = no statistical competence
Correlation = causation
Counterfactual dependence = all causation
Analogy = surface similarity
Problem solving = brute-force search
Insight = mysterious Aha
Expert = generally rational
Human-in-loop = reliable AI correction
```

None survives the evidence.

---

# 1. Inference

HF9 uses:

```text
Inference(H, R_in → R_out, context, t)
```

for a process in which one or more representations/evidence states contribute to a
new representation, judgment, hypothesis or conclusion.

The definition is intentionally broader than formal deduction.

---

# 2. Inference is not retrieval

Retrieval makes previously retained content accessible.

Inference derives/adds/changes a representation using currently available content.

Thus:

```text
Retrieval(P) != Infer(Q from P)
```

although retrieval can supply premises to inference.

---

# 3. Inference is not association

Associative activation can make Q more accessible after P.

But inference usually implies some task-relative transformation/relation such as:

```text
support
entailment
likelihood
analogy
causal consequence
best explanation
```

Therefore:

```text
Association(P,Q) != Inference(P→Q)
```

without additional evidence.

---

# 4. Inference can be implicit or explicit

HF9 does not require every inference to be consciously verbalized.

A Human may arrive at:

```text
category judgment
causal expectation
solution candidate
```

without reporting intermediate steps.

Thus:

```text
Inference != ExplicitVerbalReasoning
```

---

# 5. Reasoning

HF9 uses `Reasoning_D` for coordinated inference over representations in a task
requiring relations among premises, hypotheses, possibilities or evidence.

It is a family term.

---

# 6. Reasoning is not formal logic

Formal logic provides normative systems for validity under declared semantics.

Human reasoning includes:

```text
deduction
probabilistic inference
causal inference
abduction
analogy
heuristic judgment
problem solving
```

Therefore:

```text
Reasoning != FormalLogic
```

---

# 7. Normative standard is not cognitive mechanism

For any reasoning task, distinguish:

```text
NormativeCriterion_N
DescriptiveProcess_P
ObservedResponse_R
TaskOutcome_O
```

A response can violate N without uniquely identifying P.

Thus:

```text
NormativeError != UniqueMechanismDiagnosis
```

---

# 8. Different tasks require different norms

Possible standards include:

```text
logical validity
probability coherence
Bayesian posterior
causal identification
predictive accuracy
calibration
ecological task success
loss minimization
```

Therefore:

```text
Rationality_N
```

must declare the norm.

---

# 9. Rationality is qualifier-required

HF9 rejects:

```text
Human is rational / irrational
```

as a foundation-level scalar.

Use:

```text
NormativeAccuracy_N
EcologicalPerformance_E
ResourceEfficiency
Calibration
Robustness
```

as separate dimensions.

---

# 10. Logical validity is not truth

An argument can be valid with false premises.

Therefore:

```text
LogicalValidity != PremiseTruth
LogicalValidity != ConclusionWorldTruth by itself
```

HF8 truth relations and HF9 inference relations remain separate.

---

# 11. Believability is not validity

Humans can be influenced by whether a conclusion is believable when judging
syllogistic validity.

Thus:

```text
Believability != LogicalValidity
```

and current reasoning can involve conflict between them.

---

# 12. Deduction

Working definition:

```text
Deduction
= inference evaluated against whether a conclusion follows necessarily from
  declared premises under a declared formal interpretation
```

This is a normative/operational definition, not a psychological algorithm.

---

# 13. Deductive competence is task-sensitive

Wason/conditional tasks show performance changes with:

```text
wording
content
perspective
feedback
actual card turning
instruction
```

Therefore:

```text
DeductiveTaskPerformance
!= PureDeductiveCapacityReadout
```

---

# 14. Wason performance is not one logic meter

Standard abstract selection tasks can produce low normative performance.

But interactive/feedback-rich or differently worded variants produce much better
performance.

Thus:

```text
WasonError != HumanLogicDeficit by definition
```

---

# 15. Task interpretation is part of reasoning

Before inference, the Human must decide what the conditional/task means.

So:

```text
ProblemStatement
→ Interpretation
→ Inference
```

and:

```text
LogicalFormSpecifiedByExperimenter
!= ParticipantInterpretedForm
```

necessarily.

---

# 16. Content effects are real

Social/deontic/causal content can dramatically change conditional-reasoning
performance.

Therefore:

```text
ReasoningProcess
is not always content-insensitive
```

---

# 17. But content effect does not identify one mechanism

Social-contract, pragmatic/relevance, decision-theoretic and other accounts can
sometimes predict overlapping facilitation patterns.

Thus:

```text
ContentEffect != UniqueDomainModuleProof
```

---

# 18. Same logical form can evoke different strategies

Syllogistic/conditional evidence supports rule-like, model-like, probabilistic and
content-sensitive strategies under different conditions.

Thus:

```text
SameFormalProblem != SameCognitiveAlgorithm
```

---

# 19. Mental models are a strong theory family

A mental-model account says reasoners construct representations of possibilities
consistent with premises and inspect what follows.

This explains many inference patterns and difficulty effects.

HF9 retains it as a major competitor.

---

# 20. Mental models are not final reasoning ontology

Some conditional effects require revisions/alternatives to simple mental-model
accounts.

Therefore:

```text
MentalModelMechanism != AllReasoning
```

---

# 21. Rule-based reasoning is also not globally sufficient

Evidence that good reasoners consider alternative models and that content changes
strategy prevents a single universal rule-engine theory from being frozen.

Thus:

```text
FormalRuleApplication != AllDeduction
```

---

# 22. Probabilistic/suppositional accounts remain rivals

Some conditional judgments are better modeled through:

```text
conditional probability
uncertainty
supposition
```

than classical material implication.

HF9 does not settle the rivalry globally.

---

# 23. Reasoning is multiply realizable

A correct conclusion can emerge from:

```text
formal rule
mental model
probabilistic inference
retrieved schema
analogy
heuristic
```

Therefore:

```text
CorrectAnswer != KnownReasoningMechanism
```

---

# 24. Wrong answer is also multiply realizable

Failure can arise from:

```text
misinterpretation
premise retrieval failure
working-memory overload
premature heuristic
incomplete model
belief interference
response mapping
```

Thus:

```text
WrongAnswer != IrrationalityMechanism
```

---

# 25. Type 1 / Type 2

HF9 preserves a useful process-property contrast.

Type1-like:

```text
rapid
autonomous/default
low deliberate control
low working-memory demand
```

Type2-like:

```text
hypothetical/deliberative
working-memory demanding
sequentially controlled
```

---

# 26. Type1/Type2 are not two literal boxes

Reviews and critiques show many dual-process theories differ materially.

Thus:

```text
Type1Like != OneSystem1Organ
Type2Like != OneSystem2Organ
```

and:

```text
TwoProcessProperties != TwoExhaustiveBrainSystems
```

---

# 27. Fast is not always Type 1 and slow is not always Type 2

Expert inference can become fast through learning.

Deliberation can also be fast on simple tasks.

Therefore:

```text
Latency != ProcessType by definition
```

---

# 28. Consciousness is not the sole boundary either

HF2/HF3 already showed consciousness/access/report are separable.

Therefore:

```text
Conscious != Type2 by definition
Unconscious != Type1 by definition
```

without task evidence.

---

# 29. Working memory supports demanding reasoning

When belief conflicts with logic or multiple alternatives must be maintained,
working-memory/executive load can impair performance.

Thus:

```text
WorkingMemoryResource
can constrain
Reasoning_D
```

---

# 30. Working memory is not reasoning ability

A Human with high working-memory capacity can still reason poorly because of:

```text
bad representation
wrong model
missing knowledge
poor strategy
misleading cue
```

Thus:

```text
Reasoning != WorkingMemoryCapacity
```

---

# 31. Resource demand is relation-specific

Reasoning load depends on:

```text
number of alternatives
representation format
content familiarity
external aids
learned schema
```

So:

```text
ReasoningDifficulty
= Relation(Task, Representation, HumanState, Tools)
```

not one intrinsic problem scalar.

---

# 32. External representation can reduce reasoning load

Diagrams, tables, natural-frequency trees and written scratch work can transform a
hard internal inference into an easier perceptual/relational operation.

Thus:

```text
ExternalRepresentation
can change
ReasoningAlgorithmRequired
```

---

# 33. Probabilistic reasoning

HF9 distinguishes:

```text
ProbabilityRepresentation
ProbabilityComputation
ProbabilityJudgment
Calibration
DecisionUnderRisk
```

The last belongs partly to a later decision boundary.

---

# 34. Probability format matters

Natural frequencies can transform:

```text
P(H)
P(D|H)
P(D|not H)
```

into nested count relations that are computationally easier to combine.

Therefore:

```text
SameStatisticalInformation
+ DifferentRepresentationFormat
→ DifferentHumanPerformance
```

---

# 35. Probability error is not no Bayesian capacity

Statistically naive Humans can produce Bayesian-consistent answers at much higher
rates under favorable frequency/set representations.

Thus:

```text
ProbabilityError
!= NoBayesianReasoningCapacity
```

---

# 36. Natural frequency is not magic

Frequency format can also create errors if it does not transparently encode the
relevant set relations.

Therefore:

```text
FrequencyFormat != BayesianCorrectnessGuarantee
```

---

# 37. Representation training differs from rule memorization

The core intervention can be:

```text
change information representation
```

rather than:

```text
teach formula only
```

HF9 therefore treats representation design as part of reasoning design.

---

# 38. Base-rate neglect is not universal blindness

Humans can use base rates and sample-size information appropriately in tasks where
relevance and sampling structure are clear.

Thus:

```text
BaseRateNeglect != UniversalBaseRateBlindness
```

---

# 39. Base-rate use can itself be misweighted

Different response formats can cause participants to overuse base-rate or frequency
information.

Thus:

```text
MoreBaseRateUse != AlwaysMoreAccurate
```

---

# 40. Judgment

HF9 uses `Judgment_D` for a current evaluation/estimate such as:

```text
how probable?
how causal?
which category?
which hypothesis better supported?
```

Judgment is an epistemic/evaluative output.

---

# 41. Judgment is not decision

A Human can judge:

```text
Option A has 70% success probability
```

while choosing B due to:

```text
values
cost
risk tolerance
constraints
```

Therefore:

```text
Judgment != Decision
```

---

# 42. Judgment is not belief

A task may force a numeric judgment without categorical belief endorsement.

Thus:

```text
Judgment_t != BeliefState_t by definition
```

---

# 43. Judgment is not confidence

The estimate and confidence in that estimate are separate.

Thus:

```text
Judgment != Confidence
```

HF3 metacognitive distinctions remain.

---

# 44. Heuristic

HF9 uses:

```text
Heuristic
= bounded strategy that uses a selected subset/ordering of information or operations
  to produce an inference/judgment with reduced search/computation
```

This is neutral with respect to rationality.

---

# 45. Heuristic is not bias

Tversky/Kahneman showed heuristics can produce systematic errors.

Gigerenzer/Goldstein showed simple heuristics can perform very well under matching
environment structures.

Therefore:

```text
Heuristic != Bias
```

---

# 46. Bias is an outcome relation

Working use:

```text
Bias_N
= systematic deviation relative to a declared normative/reference criterion N
```

A bias label should declare:

```text
criterion
task
environment
loss
```

---

# 47. A biased process can be useful elsewhere

Representativeness can be efficient when similarity tracks class probability.

Recognition can be informative when recognition correlates with the criterion.

Thus:

```text
BiasInTask_A
!= GloballyBadStrategy
```

---

# 48. An accurate strategy can be fragile

A heuristic can perform well only while environmental cue validity is stable.

Therefore:

```text
CurrentAccuracy != RobustnessUnderShift
```

---

# 49. Ecological rationality

HF9 retains:

> strategy quality depends partly on fit between information-processing strategy
> and environmental structure.

Thus:

```text
Rationality_E
= Relation(Strategy, Environment, Objective, ResourceConstraint)
```

---

# 50. Ecological fit is not normative relativism

Some domains have hard constraints:

```text
probability coherence
physical impossibility
logical contradiction
```

Ecological success does not make contradictions true.

Therefore:

```text
EcologicalSuccess != TruthByDefinition
```

---

# 51. More computation is not always better

Complex models can overfit noisy/small samples or waste resources.

Thus:

```text
MoreInformation != BetterInference
MoreComputation != BetterInference
```

by definition.

---

# 52. Less-is-more can be real but scoped

Recognition-heuristic models show conditions where less knowledge can improve
inference.

But empirical critiques show Humans often use additional cues.

Thus:

```text
LessIsMoreEffect != UniversalRecognitionRule
```

---

# 53. Heuristic selection is itself a reasoning problem

A Human must choose:

```text
which cues?
which heuristic?
when to stop?
```

Causal knowledge can guide this selection.

This begins to expose the later strategy/decision boundary.

---

# 54. Induction

HF9 uses:

```text
Induction
= inference extending beyond logically entailed premises, typically from observed
  cases/evidence to uncertain generalization, prediction or latent structure
```

Its correctness is graded/probabilistic, not logical necessity.

---

# 55. Induction is not deduction with uncertainty

Deduction asks what must follow under premises.

Induction asks what is supported beyond the observed data.

Therefore:

```text
Induction != WeakDeduction
```

---

# 56. Generalization is one induction surface

From observed exemplars, a Human can infer category structure or future behavior.

HF8 concepts and HF9 induction are coupled:

```text
RepresentationStructure
→ GeneralizationPattern
```

---

# 57. Abduction

Working definition:

```text
Abduction
= inference that generates/selects candidate explanations or hidden causes that
  would make observed evidence intelligible
```

It is not guaranteed truth.

---

# 58. Abduction is not observation

A Human can infer hidden evidence/cause that was never observed.

Thus:

```text
InferredHiddenCause != ObservedCause
```

---

# 59. Explanatory inference can hallucinate structure

Sense-making under ignorance shows Humans may infer missing diagnostic evidence
from prior/base-rate cues and then reason using their own inferred evidence.

Thus:

```text
InferredEvidence != ObservedEvidence
```

and:

```text
CoherentExplanation != TruthGuarantee
```

---

# 60. Explanation generation and evaluation differ

HF8 already found explanation can improve hypothesis generation without equivalent
improvement in evaluation.

HF9 retains:

```text
HypothesisGeneration != HypothesisEvaluation
```

---

# 61. Best explanation is criterion-dependent

Candidate explanations can be judged by:

```text
fit
prior plausibility
simplicity
scope
mechanistic adequacy
predictive success
```

These can conflict.

Therefore:

```text
BestExplanation_CriterionA
!= BestExplanation_CriterionB
```

---

# 62. Causal inference

HF9 uses:

```text
CausalInference(X→Y)
```

for inference that X changes, produces, prevents or helps determine Y under a
specified causal model/intervention semantics.

---

# 63. Correlation is not causation

Two variables can covary because of:

```text
X→Y
Y→X
common cause Z
selection
measurement artifact
chance
```

Therefore:

```text
Correlation(X,Y) != Cause(X,Y)
```

---

# 64. Prediction is not causation

X can predict Y without manipulating X changing Y.

Thus:

```text
PredictivePower(X→Y)
!= CausalEffect(do(X)→Y)
```

---

# 65. Observation and intervention differ

Observing X=x preserves normal causes of X.

Intervening on X can break/alter those dependencies.

Human experiments support behavioral sensitivity to this distinction.

Thus:

```text
Observe(X=x) != Intervene(X=x)
```

---

# 66. Active intervention can improve causal learning

Interveners can identify causal structures more accurately than passive observers
in some probabilistic-chain tasks.

Therefore:

```text
Action
can be
InformationAcquisition
```

not only outcome production.

---

# 67. Active learning is not always better

Interventions can be:

```text
poorly chosen
confounded
costly
irreversible
```

Thus:

```text
Intervention != BetterEvidence by definition
```

The intervention policy matters.

---

# 68. Temporal order contributes causal evidence

Humans exploit temporal sequence when inferring causal structure.

But temporal precedence alone is insufficient.

Thus:

```text
TemporalPrecedence != Causation
```

---

# 69. Causal evidence bundle

A causal claim should distinguish:

```text
covariation
precedence
intervention
mechanism knowledge
confounding/common causes
alternative causes
counterfactual dependence
replication
```

No single channel is universally sufficient.

---

# 70. Causal judgment is not causal truth

Humans produce graded causal attributions influenced by:

```text
physics/model
expectations
normality
counterfactual alternatives
```

Therefore:

```text
CausalJudgment != CausalTruth
```

---

# 71. Counterfactual

HF9 uses:

```text
Counterfactual(H, actual world W, intervention/change X', query Y')
```

for representation/simulation of a relevant alternative to actuality.

---

# 72. Counterfactual is not belief

A Human can simulate:

```text
If X had not happened...
```

without believing X did not happen.

Thus:

```text
CounterfactualRepresentation != BeliefAboutActualWorld
```

---

# 73. Counterfactual reasoning is model-dependent

To answer what would happen under X', the Human needs assumptions about:

```text
what changes
what remains invariant
transition dynamics
background conditions
```

Thus:

```text
CounterfactualAnswer
= Function(Model, Intervention, Invariants)
```

not free imagination.

---

# 74. Counterfactual simulation supports causal judgment

Physical-event studies show actual-cause judgments can be predicted by simulating
whether outcomes would differ under relevant counterfactual changes.

Therefore counterfactual simulation is a major causal-reasoning mechanism family.

---

# 75. Counterfactual dependence is not all causation

Overdetermination, omissions and normative expectations complicate simple:

```text
If not X then not Y
```

criteria.

Thus:

```text
ButForDependence != CompleteCausationTheory
```

---

# 76. Expectations shape counterfactuals

For omissions, what people judge as the relevant alternative depends partly on
norms/expectations about what should normally happen.

Thus:

```text
CounterfactualSelection
is context-sensitive
```

---

# 77. Normality is not causality

An abnormal event may draw causal attention without being the only cause.

Thus:

```text
Abnormality != CausalStrength
```

although it can affect causal judgment.

---

# 78. Causal reasoning can guide search

If a Human believes A causes B, they may inspect A before irrelevant variables.

Experimental work shows causal knowledge can make cue search more frugal and
accurate.

Thus:

```text
CausalModel
→ SearchPolicy
```

---

# 79. Analogy

HF9 uses:

```text
Analogy(Source S, Target T)
```

for transfer based on mapped relational structure between distinct cases.

---

# 80. Analogy is not surface similarity

Two problems can share surface features but require different solutions.

Two structurally analogous problems can look very different.

Thus:

```text
SurfaceSimilarity != StructuralAnalogy
```

---

# 81. Analogical transfer has stages

HF9 separates:

```text
SourceAccess
Mapping
Adaptation
Execution
TransferOutcome
```

Strong:

```text
SourceAccess != Mapping != Adaptation != TransferSuccess
```

---

# 82. Mapping success is not adaptation success

A Human may correctly recognize that two problems correspond structurally yet fail
to adapt the old solution procedure to target constraints.

Thus:

```text
SuccessfulMapping != SuccessfulTransfer
```

---

# 83. Source retrieval is a bottleneck

A useful analogy cannot help if the source is not retrieved/noticed.

Surface similarity can aid access even when it is not the basis of the final
structural mapping.

Thus:

```text
AccessCue != TransferRelation
```

---

# 84. Surface similarity can harm

Novices can spontaneously transfer inappropriate procedures when surface similarity
is high but structural relation is wrong.

Thus:

```text
SimilarityBenefit can coexist with SimilarityTrap
```

---

# 85. Expertise alters analogical representation

Experts are more likely in some domains to retrieve/map deep structural relations.

Thus:

```text
Expertise_D
can change
SimilarityMetric_D
```

---

# 86. Expertise is not general reasoning superiority

An expert in physics is not thereby expert in law, medicine or social causality.

Thus:

```text
Expertise_D != GeneralReasoningTrait
```

---

# 87. Problem representation

HF9 uses:

```text
ProblemRepresentation
= the currently active structured interpretation of initial state, constraints,
  relations, operators and target
```

This is not identical to the presented statement.

---

# 88. Problem statement is not problem representation

Two Humans can read identical text and construct different effective problems.

Thus:

```text
ProblemStatement != ProblemRepresentation
```

---

# 89. Problem representation defines search space

What the Human treats as:

```text
state
operator
constraint
goal
```

determines which moves even appear possible.

Thus:

```text
Representation
→ CandidateSearchSpace
```

---

# 90. Expertise changes problem representation

Physics experts classify around underlying principles, novices more by surface
objects/features.

Clinical experts also compress/select case information differently.

Therefore:

```text
SamePresentedProblem
→ DifferentProblemRepresentation
→ DifferentSearch
```

---

# 91. Search

HF9 uses:

```text
Search
= exploration of candidate states/operators/hypotheses within a currently
  represented problem space
```

Search can be internal or external/tool-mediated.

---

# 92. Search is not problem solving

A solver may need to change the representation itself rather than search harder.

Therefore:

```text
Search != ProblemSolving
```

---

# 93. Search can be systematic or heuristic

Examples:

```text
breadth/depth-like exploration
means–ends analysis
hill climbing
analogy-guided search
constraint propagation
```

HF9 does not canonize one search algorithm.

---

# 94. Search space can be wrong

If initial representation excludes the needed operator, infinite effort within the
same space cannot solve the problem.

Thus:

```text
MoreSearch != Solution
```

when representation is wrong.

---

# 95. Representational change

Working definition:

```text
RepresentationalChange
= revision of what states, relations, constraints or operators constitute the
  problem
```

This can create a new search space.

---

# 96. Insight often involves representational change

Matchstick and verbal-insight studies support constraint relaxation/re-encoding in
many insight tasks.

Thus representational change is a major mechanism family.

---

# 97. Insight is not representational change alone

Search after restructuring can still be difficult.

Experiments show search and restructuring can jointly determine solution.

Thus:

```text
InsightProblemSolving
!= RepresentationChangeOnly
```

---

# 98. Insight is not search alone

If the search space excludes the solution, more search cannot help.

Thus:

```text
InsightProblemSolving
!= SearchOnly
```

---

# 99. Aha is experience, not mechanism

A solution can feel sudden/confident.

But that subjective phenomenology does not uniquely identify the process that
produced it.

Thus:

```text
AhaExperience != InsightMechanism
```

---

# 100. Impasse is not necessary for all insight

Current experiments fail to support impasse as a universal prerequisite.

Thus:

```text
Impasse != NecessaryForInsight
```

---

# 101. Restructuring is not insight-exclusive

Representation change can occur during problems not reported as insight.

Thus:

```text
RepresentationalChange != InsightOnly
```

---

# 102. Insight can be trained indirectly

Training people to detect inconsistency between their interpretation and the
problem statement can improve novel insight performance.

Therefore:

```text
MetaRepresentationMonitoring
can improve
RepresentationChange
```

---

# 103. Problem-solving failure is a placeholder

A failure can be located at:

```text
problem interpretation
knowledge retrieval
representation
operator generation
search order
constraint handling
analogy retrieval
mapping
adaptation
evaluation
stopping
execution
```

Thus:

```text
ProblemSolvingFailure != OneMechanism
```

---

# 104. Problem-solving success is also underdetermined

A correct solution can arise from:

```text
memorized procedure
analogy
formal derivation
heuristic search
insight
external AI
trial-and-error
```

Thus:

```text
CorrectSolution != KnownProblemSolvingProcess
```

---

# 105. Expertise changes search efficiency

Deep problem representations can reduce irrelevant branching.

Thus expert advantage can come from:

```text
better search-space construction
```

not just faster raw search.

---

# 106. Expertise can also cause fixation

Strong domain schemas/learned solutions can over-prioritize familiar representations.

HF9 therefore rejects:

```text
Expertise == universal flexibility
```

though no single fixation law is canonized.

---

# 107. Reasoning and metacognition interact

HF3 confidence/control can influence:

```text
whether to continue search
whether to check an inference
whether to seek evidence
```

Thus:

```text
Metacognition
→ ReasoningControl
```

but:

```text
Metacognition != Reasoning
```

---

# 108. Confidence is not validity

A Human can be highly confident in an invalid inference.

Thus:

```text
ReasoningConfidence != NormativeCorrectness
```

---

# 109. Conflict detection is not correction

Detecting that an intuitive answer conflicts with another standard does not ensure
successful alternative reasoning.

Thus:

```text
ConflictDetection != SuccessfulCorrection
```

---

# 110. Slow deliberation is not automatically better

More time can allow model checking.

But it can also enable:

```text
rationalization
search in wrong space
overfitting
```

Therefore:

```text
MoreDeliberation != BetterReasoning by definition
```

---

# 111. Fast expert judgment can be high quality

Practice can compress reliable domain structure into rapid pattern recognition.

Thus:

```text
FastJudgment != HeuristicError
```

---

# 112. Rationality requires cost-sensitive analysis

In finite time, an inference process should be evaluated relative to:

```text
accuracy
latency
information cost
computation
error asymmetry
robustness
```

rather than accuracy alone.

---

# 113. Bounded rationality

HF9 retains the general idea that Humans operate under finite:

```text
time
information
memory
computation
```

and therefore cannot generally optimize over all possible inferences.

---

# 114. Bounded does not mean defective

Finite strategies can be well-adapted.

Thus:

```text
Bounded != Irrational
```

---

# 115. Heuristics can be algorithms

A heuristic need not be vague intuition.

Fast-and-frugal research provides explicit rules for:

```text
search
stopping
decision
```

Therefore:

```text
Heuristic != UnspecifiedGutFeeling
```

---

# 116. Search and stopping are separate

A strategy specifies not only:

```text
where to look
```

but also:

```text
when enough evidence has been seen
```

Thus:

```text
SearchPolicy != StoppingRule
```

This becomes a major residual beyond HF9.

---

# 117. Judgment and action are separate

Reasoning may terminate in a judgment.

Action still requires choosing whether/when to commit given:

```text
values
costs
risk
time
alternatives
```

Thus:

```text
InferenceComplete != ActionSelected
```

---

# 118. Problem solving often requires action sequencing

Many real problems require:

```text
choose next experiment
wait
collect data
act
observe
revise
```

rather than one static answer.

This crosses into planning/strategy.

---

# 119. Information gathering competes with acting

A Human can:

```text
search more
or
act now
```

The correct tradeoff depends on information value and action urgency.

HF9 can identify the dilemma but does not yet reconstruct decision policy.

---

# 120. Human×AI reasoning

AI can enter at:

```text
problem representation
hypothesis generation
search
evidence retrieval
calculation
critique
judgment
```

Each intervention can alter the Human reasoning path differently.

---

# 121. AI answer is not Human inference

If AI derives P and Human copies P:

```text
JointSystem produced conclusion P
```

but it does not follow that:

```text
Human independently inferred P
```

Thus:

```text
AIAssistedConclusion != HumanIndependentInference
```

---

# 122. Human-in-the-loop is not automatic safety

Experiments show Humans can follow erroneous AI recommendations.

Therefore:

```text
HumanInLoop != ErrorCorrectionGuarantee
```

---

# 123. AI timing changes cognition

Receiving AI advice before independent judgment can anchor or shape the initial
problem representation.

Receiving it after an independent judgment creates a different comparison task.

Thus:

```text
AIAdviceBeforeJudgment
!= AIAdviceAfterJudgment
```

---

# 124. Correct AI can improve judgment

Clinical experiments show valid AI advice can improve Human decisions in some
settings.

Therefore:

```text
AIAssistance != CognitiveHarm by definition
```

---

# 125. Incorrect AI can systematically mislead

The same dependency that provides improvement can transmit error.

Thus:

```text
AICorrectionBenefit
can coexist with
AutomationBiasRisk
```

---

# 126. Warning is not calibration

Generic warnings can fail to change advice weighting.

More targeted error-risk framing can help under some tasks but not eliminate bias.

Thus:

```text
Warning != CalibratedTrust
```

---

# 127. Cognitive forcing is not universally effective

Requiring delay/extra thought does not guarantee recovery from biased AI advice.

Thus:

```text
SlowDown != DebiasGuarantee
```

---

# 128. Structured AI interaction can improve reasoning process

Current randomized evidence shows structured protocols encouraging:

```text
articulation
brainstorming
benchmarking
critique
what-if questions
```

can outperform unguided AI use on some clinical reasoning measures.

Therefore:

```text
SameModel
+ DifferentHarness
→ DifferentJointReasoning
```

---

# 129. Harness is part of epistemic environment

A Human×AI system should model:

```text
when AI speaks
what it reveals
whether Human answers first
whether sources are shown
whether counterarguments are requested
whether final decision requires Human synthesis
```

These are causal variables, not interface cosmetics.

---

# 130. AI can widen hypothesis generation while degrading evaluation

Generative systems can produce many alternatives cheaply.

This can help if evaluation/verification remains strong.

It can hurt if volume overwhelms discrimination.

Thus:

```text
HypothesisCount != ReasoningQuality
```

---

# 131. AI can alter problem representation

Summarization or framing by AI can compress a problem before the Human has formed an
independent model.

Thus:

```text
AIProblemSummary
can become
ProblemRepresentationIntervention
```

---

# 132. Independent-first reasoning is one useful protocol, not a universal law

Having the Human form an initial judgment before AI can reduce some anchoring risks
and create an explicit comparison surface.

But in unfamiliar/high-complexity tasks, early AI scaffolding may be beneficial.

Thus:

```text
HumanFirst != AlwaysBest
AIFirst != AlwaysBest
```

---

# 133. Verification should be discriminative

`Check the answer` is weak.

Stronger verification asks:

```text
What evidence would distinguish alternatives?
What assumption is load-bearing?
What changes under intervention?
Can another method reproduce it?
```

This is HF9 reasoning, not merely HF8 provenance.

---

# 134. Reasoning tools change reachable search space

Calculators, code, simulators and AI make formerly expensive branches cheap.

Therefore:

```text
ToolSet
changes
EffectiveProblemSpace
```

and sometimes the optimal Human strategy.

---

# 135. Tool expansion can increase search debt

More possible tools/hypotheses can also create:

```text
branching explosion
evaluation burden
coordination cost
```

Thus:

```text
MoreOptions != EasierProblemSolving
```

---

# 136. Reasoning quality must include stopping

An agent that never stops searching never acts.

A premature stop can miss decisive evidence.

HF9 therefore identifies:

```text
StoppingPolicy
```

as a distinct unresolved construct.

---

# 137. Reasoning quality must include search allocation

Limited reasoning budget creates choices among:

```text
which hypothesis to test
which source to inspect
which simulation to run
```

This is already a resource-allocation/strategy problem.

---

# 138. Inference under uncertainty creates option values

Sometimes additional reasoning can change future choices.

Thus information/search has value only relative to downstream decision stakes.

HF9 can expose this relation but not finish the decision theory.

---

# 139. Judgment is often provisional

A Human may maintain:

```text
best current hypothesis
```

without committing to action.

Therefore:

```text
ProvisionalJudgment != Commitment
```

---

# 140. Commitment changes the future state space

Once an action is chosen:

```text
resources spent
options disappear
new information appears
```

so decision/commitment is not merely another belief update.

---

# 141. Reasoning and action form a loop

Real agents operate:

```text
Represent
→ Infer
→ Judge
→ Choose/Act
→ Observe
→ Update representation
↺
```

HF9 reconstructs the first three transitions but not the choice/action-policy layer
in full.

---

# 142. InferenceProfile

HF9 proposes:

```text
InferenceProfile_D = {
  input representations,
  target conclusion/hypothesis,
  inference family,
  normative criterion,
  assumptions,
  uncertainty,
  search/evidence history,
  resource/time budget,
  external aids,
  output judgment,
  confidence,
  alternative models,
  falsification surface
}
```

---

# 143. ProblemSolvingProfile

```text
ProblemSolvingProfile_D = {
  problem representation,
  goal/criterion,
  known operators,
  constraints,
  search space,
  strategy,
  analogy/source use,
  representational changes,
  external tools,
  evaluation function,
  stopping rule,
  solution status,
  transfer evidence
}
```

---

# 144. CausalInferenceProfile

```text
CausalInferenceProfile(X,Y) = {
  observational evidence,
  intervention evidence,
  temporal evidence,
  mechanism knowledge,
  confounders/alternatives,
  counterfactual model,
  normality/expectations,
  causal judgment,
  uncertainty,
  intervention validity
}
```

---

# 145. RationalityProfile

```text
RationalityProfile_N,E = {
  normative criterion N,
  environment E,
  accuracy,
  calibration,
  robustness,
  information cost,
  computation/time cost,
  error asymmetry,
  adaptation under shift
}
```

This replaces global `rational/irrational` labels.

---

# 146. Cross-context falsifier matrix

| Case | Naive collapse attacked | HF9 surviving distinction |
|---|---|---|
| Wason performance changes with wording/feedback | reasoning = pure logic | interpretation/task matters |
| same conditional form, different content performance | logical form determines process | content can change strategy |
| multiple syllogistic strategies | one reasoning algorithm | rules/models/probabilistic strategies can coexist |
| executive load hurts belief-logic conflict | reasoning = WM | WM constrains demanding correction |
| natural frequencies improve Bayes | statistical error = incapacity | representation format changes computation |
| frequency formats can also mislead | frequency = magic | set structure/response format matter |
| heuristics produce conjunction/base-rate errors | heuristics always good | systematic bias is real |
| fast-frugal strategy matches complex model | heuristics irrational | ecological fit matters |
| recognition heuristic violated in some cases | one heuristic universal | Humans integrate additional cues |
| interventions outperform observation | covariance = causation | intervention is distinct evidence |
| observed versus manipulated effect differs | X=x is X=x | causal semantics depend on how X obtained value |
| omission causation depends on expectation | but-for only | counterfactual selection is model/norm sensitive |
| mapping succeeds but transfer fails | analogy = noticing similarity | mapping != adaptation |
| experts transfer deep structure | expertise = more facts only | representation/search organization matters |
| surface similarity harms novices | similarity = transfer | surface cue can mislead |
| insight needs restructuring + search | insight = search or Aha | representation/search interaction |
| no impasse before some insight | impasse necessary | Aha phenomenology not mechanism definition |
| wrong AI before judgment reduces accuracy | human-in-loop = safe | advice timing and automation bias matter |
| correct AI improves clinician judgment | AI = cognitive harm | assistance can improve joint reasoning |
| generic warnings fail | warning = calibration | trust control requires mechanism-sensitive design |
| structured AI protocol improves process | interface irrelevant | harness changes reasoning causal path |

---

# 147. Competing reasoning models

## M1 — formal-rule engine

### Claim

Human reasoning applies symbolic inference rules.

### Strength

Explains explicit logical competence and rule training.

### Failure

Content/interpretation effects, probabilistic reasoning, analogy and model-based
patterns.

**Disposition:** retain locally; reject as complete ontology.

## M2 — mental models

### Claim

Reasoners construct possible situations and inspect what follows.

### Strength

Explains many conditional/syllogistic effects and alternative-load difficulty.

### Failure

Not all conditional patterns are captured without extensions; not all reasoning is
possibility simulation.

**Disposition:** major theory family, not universal identity.

## M3 — probabilistic/suppositional reasoning

### Strength

Captures graded conditional judgments and uncertainty.

### Failure

Does not by itself explain all deductive/deontic/causal tasks.

**Disposition:** retain competing family.

## M4 — dual-process

### Strength

Explains default-versus-deliberative conflict and working-memory effects.

### Failure

Literal two-system ontologies overcompress heterogeneous process properties.

**Disposition:** retain Type1-like/Type2-like dimensions.

## M5 — heuristics-and-biases

### Strength

Explains systematic judgment errors under uncertainty.

### Failure

Can overgeneralize from bias tasks and understate environmental fit.

**Disposition:** retain phenomena/mechanisms with explicit norms.

## M6 — ecological rationality / adaptive toolbox

### Strength

Explains why simple bounded strategies can be robust in structured environments.

### Failure

No heuristic is universally adaptive; strategy selection and shifting remain hard.

**Disposition:** retain environment-strategy relation.

## M7 — causal model / intervention semantics

### Strength

Explains why observation/intervention/counterfactual differ.

### Failure

Human causal judgments also depend on temporal cues, expectations and simplified
models.

**Disposition:** retain causal representation/intervention distinctions.

## M8 — counterfactual simulation

### Strength

Strong fit to graded actual-causation judgments in physical tasks.

### Failure

Relevant alternatives/normality are themselves selected; simple but-for condition
is incomplete.

**Disposition:** retain mechanism family.

## M9 — analogy as structural mapping

### Strength

Explains deep transfer and expert advantages.

### Failure

Source access and adaptation remain separate bottlenecks; surface cues matter.

**Disposition:** retain staged analogy model.

## M10 — search-space problem solving

### Strength

Formalizes operators/states/goals and incremental search.

### Failure

Insight and expertise show problem representation itself changes.

**Disposition:** retain search as one layer.

## M11 — representational-change insight

### Strength

Strong evidence in matchstick/verbal insight tasks.

### Failure

Search still matters and Aha/impasse are not universal.

**Disposition:** retain interaction model.

## M12 — AI-augmentation model

### Claim

AI simply improves Human reasoning by adding intelligence.

### Failure

Correct AI can help, wrong AI can bias, timing matters, and structure/harness
changes outcomes.

**Disposition:** replace with typed joint-reasoning model.

---

# 148. HF9 anti-laws

## Inference / reasoning

1. `Inference != Retrieval`.
2. `Inference != Association`.
3. `Inference != ExplicitVerbalReasoning`.
4. `Reasoning != FormalLogic`.
5. `NormativeError != UniqueMechanismDiagnosis`.
6. `LogicalValidity != PremiseTruth`.
7. `Believability != LogicalValidity`.
8. `DeductiveTaskPerformance != PureDeductiveCapacity`.
9. `WasonError != HumanLogicDeficit`.
10. `LogicalFormSpecified != ParticipantInterpretation`.
11. `ContentEffect != UniqueDomainModuleProof`.
12. `SameFormalProblem != SameCognitiveAlgorithm`.
13. `MentalModelMechanism != AllReasoning`.
14. `FormalRuleApplication != AllDeduction`.
15. `CorrectAnswer != KnownReasoningMechanism`.
16. `WrongAnswer != IrrationalityMechanism`.

## Process/resource

17. `Type1Like != OneLiteralSystem1`.
18. `Type2Like != OneLiteralSystem2`.
19. `Latency != ProcessType`.
20. `Conscious != Type2 by definition`.
21. `Reasoning != WorkingMemoryCapacity`.
22. `ReasoningDifficulty != ProblemIntrinsicScalar`.
23. `MoreDeliberation != BetterReasoning`.
24. `FastJudgment != HeuristicError`.
25. `Bounded != Irrational`.

## probability/judgment

26. `ProbabilityRepresentation != ProbabilityContent`.
27. `ProbabilityError != NoBayesianReasoningCapacity`.
28. `FrequencyFormat != BayesianCorrectnessGuarantee`.
29. `BaseRateNeglect != UniversalBaseRateBlindness`.
30. `MoreBaseRateUse != AlwaysMoreAccurate`.
31. `Judgment != Decision`.
32. `Judgment != Belief by definition`.
33. `Judgment != Confidence`.

## heuristic/rationality

34. `Heuristic != Bias`.
35. `Heuristic != Irrationality`.
36. `BiasInTask_A != GloballyBadStrategy`.
37. `CurrentAccuracy != RobustnessUnderShift`.
38. `EcologicalSuccess != TruthByDefinition`.
39. `MoreInformation != BetterInference`.
40. `MoreComputation != BetterInference`.
41. `LessIsMoreEffect != UniversalRecognitionRule`.
42. `Heuristic != UnspecifiedGutFeeling`.

## induction/abduction

43. `Induction != WeakDeduction`.
44. `InferredHiddenCause != ObservedCause`.
45. `InferredEvidence != ObservedEvidence`.
46. `CoherentExplanation != TruthGuarantee`.
47. `HypothesisGeneration != HypothesisEvaluation`.
48. `BestExplanation_A != BestExplanation_B` across criteria.

## causality/counterfactuals

49. `Correlation != Causation`.
50. `Prediction != CausalEffect`.
51. `Observation != Intervention`.
52. `Intervention != BetterEvidence by definition`.
53. `TemporalPrecedence != Causation`.
54. `CausalJudgment != CausalTruth`.
55. `CounterfactualRepresentation != ActualBelief`.
56. `ButForDependence != CompleteCausationTheory`.
57. `Abnormality != CausalStrength`.

## analogy/problem solving

58. `SurfaceSimilarity != StructuralAnalogy`.
59. `SourceAccess != Mapping`.
60. `Mapping != Adaptation`.
61. `SuccessfulMapping != SuccessfulTransfer`.
62. `AccessCue != TransferRelation`.
63. `Expertise_D != GeneralReasoningTrait`.
64. `ProblemStatement != ProblemRepresentation`.
65. `Search != ProblemSolving`.
66. `MoreSearch != Solution`.
67. `Insight != RepresentationChangeOnly`.
68. `Insight != SearchOnly`.
69. `AhaExperience != InsightMechanism`.
70. `Impasse != NecessaryForInsight`.
71. `RepresentationalChange != InsightOnly`.
72. `ProblemSolvingFailure != OneMechanism`.
73. `CorrectSolution != KnownProblemSolvingProcess`.

## Human×AI

74. `AIAssistedConclusion != HumanIndependentInference`.
75. `HumanInLoop != ErrorCorrectionGuarantee`.
76. `AIAdviceBeforeJudgment != AIAdviceAfterJudgment`.
77. `AIAssistance != CognitiveHarm by definition`.
78. `Warning != CalibratedTrust`.
79. `SlowDown != DebiasGuarantee`.
80. `SameAIModel + DifferentHarness != SameReasoningOutcome`.
81. `HypothesisCount != ReasoningQuality`.
82. `HumanFirst != AlwaysBest`.
83. `AIFirst != AlwaysBest`.
84. `MoreOptions != EasierProblemSolving`.

## residual/choice boundary

85. `SearchPolicy != StoppingRule`.
86. `InferenceComplete != ActionSelected`.
87. `ProvisionalJudgment != Commitment`.
88. `ReasoningQuality != InfiniteSearch`.

---

# 149. Minimum HF9 grammar

```text
World / Problem / Evidence
        ↓
Problem / Evidence Representation
        ↓
Candidate Models / Hypotheses / Premises
        ↓
Inference Operations
  ├─ Deduction
  ├─ Induction
  ├─ Abduction
  ├─ Analogy
  ├─ Probabilistic inference
  ├─ Causal inference
  └─ Counterfactual simulation
        ↓
Search / Comparison / Evaluation
  ↑ goals + norms + resources + heuristics + tools
        ↓
Judgment
  ├─ validity
  ├─ probability
  ├─ causal strength
  ├─ explanatory support
  └─ solution adequacy
        ↓
Metacognitive confidence / conflict / verification
        ↓
[unresolved next layer]
Selection / stopping / commitment / action sequence
        ↓
World feedback
        ↺
Representation / model revision
```

---

# 150. Human×AI joint reasoning grammar

```text
Human initial representation
        ↓
Human independent hypothesis?   ← protocol choice
        ↓
AI input
  ├─ summary
  ├─ hypotheses
  ├─ evidence
  ├─ calculation
  └─ recommendation
        ↓
Human comparison / verification / counterfactual test
        ↓
Joint judgment
        ↓
Independent or delegated choice
```

The order is causal.

---

# 151. Reasoning evidence bundle

For a strong reasoning claim, record where relevant:

```text
problem wording/content
participant interpretation
input representation format
prior knowledge/belief
reasoning time
working-memory/load
allowed tools
candidate alternatives generated
search history
normative criterion
current answer
confidence
counterexample sensitivity
transfer
independent replication
```

---

# 152. Causal reasoning evidence bundle

```text
observational data
interventions
confounders
mechanism assumptions
time order
counterfactual alternatives
normality expectations
causal estimate
uncertainty
external tools/model
```

---

# 153. Problem-solving evidence bundle

```text
initial representation
solution operators considered
search trajectory
representational changes
analogy source/mapping/adaptation
hints/tools
Aha/phenomenology
solution correctness
latency
novel transfer
recovery after perturbation
```

---

# 154. Reconnection to HF8

HF8 provides:

```text
Representation / Belief / Knowledge / Model
```

HF9 provides:

```text
operations transforming them
```

Thus:

```text
WorldModel_t
+ InferencePolicy_t
→ WorldModel_(t+1)
```

is more informative than one static model score.

---

# 155. Reconnection to HF7

Memory determines which premises/cases are retrievable.

Reasoning determines what follows from retrieved content.

Therefore:

```text
Retrieval != Inference
```

but retrieval ecology strongly shapes inference inputs.

---

# 156. Reconnection to HF6

Reasoning strategies can be learned and automatized.

Therefore:

```text
ReasoningProcess_t
```

can change with history.

Expert fast judgment may be the product of deep prior learning rather than a
separate innate faculty.

---

# 157. Reconnection to HF5

Stress/fatigue/arousal can alter:

```text
search persistence
working-memory availability
stopping threshold
```

without changing formal inference validity itself.

Thus internal state is a reasoning-condition variable.

---

# 158. Reconnection to HF4

HF4 goals/value affect:

```text
which question is asked
which evidence is worth acquiring
how long to reason
what error matters
```

Therefore reasoning is not value-free in resource allocation, even when validity
criteria themselves are normative/epistemic.

---

# 159. Reconnection to HF3

Attention selects evidence/model components; working memory maintains alternatives;
metacognition controls checking.

But:

```text
Attention != Reasoning
WorkingMemory != Reasoning
Metacognition != Reasoning
```

They are supporting/control processes.

---

# 160. Reconnection to HF2

Aha, certainty, doubt and conflict are first-person experiences.

They can provide useful metacognitive evidence but are not direct proof of:

```text
validity
truth
causality
solution quality
```

---

# 161. Reconnection to HF1

A JointHumanAIReasoningSystem can solve problems the Human cannot solve alone.

But:

```text
JointReasoningCapability != HumanIndependentReasoningCapability
```

and identity remains separate.

---

# 162. What HF9 does not establish

HF9 does not establish:

- one universal Human reasoning algorithm;
- that reasoning is uniquely human;
- that all inference is conscious;
- that formal logic is psychologically irrelevant;
- that Wason errors are only misunderstanding;
- that mental models are the final deduction theory;
- that dual-process distinctions are useless;
- that Type 1/Type 2 are literal exhaustive systems;
- that working memory explains all reasoning differences;
- that natural frequencies always improve Bayesian reasoning;
- that humans are Bayesian by default;
- that heuristics are always adaptive;
- that biases are artifacts;
- that ecological success replaces normative truth;
- that correlation never provides causal evidence;
- that intervention alone identifies causation;
- that counterfactual simulation explains all causal judgment;
- that all analogy is explicit;
- that experts always transfer better;
- that insight requires impasse;
- that insight is a single mechanism;
- that problem solving is reducible to search;
- that AI assistance improves or harms reasoning by default;
- that warnings or forced deliberation reliably debias AI use;
- that independent-first or AI-first interaction is universally optimal.

---

# 163. The residual HF9 cannot finish

Across all HF9 domains, a repeated neighboring problem remains.

After inference/problem solving generates candidate options, the Human must still:

```text
choose which option to pursue
choose which experiment/query to run next
allocate finite search budget
decide whether more information is worth its cost
stop searching
plan a sequence of actions
trade exploration against exploitation
commit despite uncertainty
revise or abandon a plan after feedback
```

These are not merely inference operations.

They transform epistemic possibilities into **temporally organized action policy**.

HF4 modeled goals/value/motivation and HF9 modeled inference/search, but the bridge:

```text
judgment / candidate solution
→ selected action sequence
```

has not been reconstructed directly.

---

# 164. Exact next foundation

HF9 therefore selects:

# HF10 — Decision, Choice, Planning, Strategy, Exploration, Exploitation, Stopping and Commitment

HF10 should ask:

1. What is a decision relative to judgment, choice, action and policy?
2. What is choice relative to preference/value from HF4?
3. What is planning relative to reasoning, simulation and action sequence?
4. What is a strategy relative to plan, heuristic, policy and tactic?
5. What determines whether to gather more information or act now?
6. What is value of information relative to uncertainty and action stakes?
7. How should exploration and exploitation be separated in Human behavior?
8. What is a stopping rule, and how does it differ across search, evidence and
   action?
9. What is commitment relative to intention, goal commitment and irreversible
   action?
10. How do sunk costs, switching costs and option value change continuation?
11. How should risk, uncertainty, ambiguity and regret enter choice without
    collapsing into value?
12. How do planning horizons and temporal abstraction work?
13. How do external tools/AI change option generation, planning and delegation?
14. What next boundary emerges after sequential choice/action policy is rebuilt?

HF10 should not predefine HF11.

---

# 165. Candidate HF10 falsifiers

- judgment-choice dissociations;
- framing/reference effects under risky choice;
- preference reversals;
- value-of-information and information-avoidance tasks;
- exploration/exploitation bandits;
- stopping/search-satisficing tasks;
- sunk-cost and escalation-of-commitment paradigms;
- precommitment from HF4;
- planning versus habitual/model-free action;
- hierarchical planning/horizon effects;
- plan failure under changing state;
- delegated/AI planning versus independent execution;
- AI option generation increasing choice quality versus choice overload;
- human override/deference under uncertain AI recommendations.

---

# 166. HF9 synthesis

HF9 began with:

```text
How does a Human transform representations?
```

The surviving answer is not `formal logic` or one reasoning faculty.

It is a family of bounded, representation-sensitive transformations:

```text
Deduction
Induction
Abduction
Analogy
Probabilistic inference
Causal inference
Counterfactual simulation
Heuristic search
Problem-space search
Representational change
```

whose quality must be evaluated against declared norms, environments and resource
constraints.

The deepest compression is:

```text
ReasoningQuality
!= FormalCorrectnessAlone
!= EcologicalSuccessAlone
!= ComputationalEffort
```

and:

```text
Problem solving is not search over a fixed space;
it is recurrent construction of the space, search within it, evaluation of what
was found, and revision when the space itself is wrong.
```

But reasoning still stops one layer before agency in time:

> **Once several plausible judgments, solutions or information-gathering moves
> exist, which one should the Human actually choose, when should search stop, and
> how should choices be organized into a plan?**

That is the HF10 decision/planning/strategy boundary.
