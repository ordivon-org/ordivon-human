---
schema_version: 1
id: human.foundations.hf9.continuation
title: Human Foundations Continuation after HF9
type: handoff
profile: research
lifecycle: completed
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
updated: 2026-08-17
summary: Exact continuation after HF9. HF9 reconstructs operations over representations—deduction, induction, abduction, analogy, probabilistic and causal inference, counterfactual simulation, judgment, heuristics, search and insight—then exposes the bridge from epistemic outputs to temporally organized action policy as the next boundary: decision, choice, planning, strategy, exploration/exploitation, stopping and commitment.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.foundations.hf9
  - human.foundations.hf9.sources
---
# Human Foundations Continuation after HF9

## HF9 completed result

HF9's minimum reasoning grammar is:

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
        ↓
Metacognitive confidence / conflict / verification
        ↓
[HF10 boundary]
Selection / stopping / commitment / action sequence
```

## Inference / reasoning

Retain:

```text
Inference != Retrieval
Inference != Association
Inference != ExplicitVerbalReasoning
Reasoning != FormalLogic
NormativeError != UniqueMechanismDiagnosis
LogicalValidity != PremiseTruth
Believability != LogicalValidity
DeductiveTaskPerformance != PureDeductiveCapacity
WasonError != HumanLogicDeficit by definition
SameFormalProblem != SameCognitiveAlgorithm
CorrectAnswer != KnownReasoningMechanism
WrongAnswer != IrrationalityMechanism
```

Reasoning is a family of transformations over representations, not one faculty.

## Rationality firewall

Separate:

```text
DescriptiveProcess
NormativeCriterion
ObservedResponse
Task/EnvironmentalOutcome
ResourceCost
```

Use `Rationality_N,E` only with a declared norm/environment.

Do not convert:

```text
violates logic/probability benchmark
```

into:

```text
identified irrationality mechanism
```

without process evidence.

## Type 1 / Type 2 and resources

Retain Type1-like and Type2-like process properties as useful shorthand, while
rejecting literal exhaustive two-box ontology.

```text
Type1Like != OneLiteralSystem1
Type2Like != OneLiteralSystem2
Latency != ProcessType
Reasoning != WorkingMemoryCapacity
Bounded != Irrational
```

Working-memory/executive resources constrain demanding reasoning, especially when
belief/default responses conflict with task norms.

## Probabilistic inference

Retain:

```text
ProbabilityRepresentation != ProbabilityContent
ProbabilityError != NoBayesianReasoningCapacity
FrequencyFormat != BayesianCorrectnessGuarantee
BaseRateNeglect != UniversalBaseRateBlindness
```

Natural-frequency/set representations are causal parts of many reasoning tasks,
not mere cosmetic formatting.

## Heuristics / ecological rationality

Working definition:

```text
Heuristic
= bounded strategy using selected information/operations to reduce search or
  computation
```

Retain:

```text
Heuristic != Bias
Heuristic != Irrationality
Simple != Inferior
Complex != Superior
MoreInformation != BetterInference by definition
MoreComputation != BetterInference by definition
CurrentAccuracy != RobustnessUnderShift
```

Evaluate strategy relative to norm, environment, objective, error cost and
resources.

## Deduction / induction / abduction

Retain distinct roles:

```text
Deduction
= necessity under declared premises/formal interpretation

Induction
= uncertain extension/generalization beyond entailed premises

Abduction
= generation/selection of candidate hidden causes/explanations
```

Do not collapse:

```text
Induction != WeakDeduction
InferredEvidence != ObservedEvidence
CoherentExplanation != TruthGuarantee
HypothesisGeneration != HypothesisEvaluation
```

## Causality

Retain:

```text
Correlation != Causation
Prediction != CausalEffect
Observation != Intervention
Intervention != BetterEvidence by definition
TemporalPrecedence != Causation
CausalJudgment != CausalTruth
```

Causal evidence should preserve observation/intervention, temporal order,
confounding, mechanism assumptions and alternative causes.

## Counterfactuals

Retain:

```text
CounterfactualRepresentation != ActualBelief
ButForDependence != CompleteCausationTheory
Abnormality != CausalStrength
```

Counterfactual judgments depend on a model of what changes, what remains invariant
and which alternatives are considered. Physical-event/omission findings do not
license a universal counterfactual theory of all Human causal judgment.

## Analogy

Retain staged structure:

```text
SourceAccess
→ Mapping
→ Adaptation
→ Execution
→ TransferOutcome
```

with:

```text
SurfaceSimilarity != StructuralAnalogy
SourceAccess != Mapping
Mapping != Adaptation
SuccessfulMapping != SuccessfulTransfer
AccessCue != TransferRelation
```

Expertise can change which similarity/structure is represented without becoming a
general reasoning trait.

## Problem solving / insight

Working structure:

```text
ProblemStatement
→ ProblemRepresentation
→ SearchSpace
→ Search / OperatorApplication
↕
RepresentationalChange
→ Evaluation
```

Retain:

```text
ProblemStatement != ProblemRepresentation
Search != ProblemSolving
MoreSearch != Solution
Insight != SearchOnly
Insight != RepresentationChangeOnly
AhaExperience != InsightMechanism
Impasse != NecessaryForInsight
RepresentationalChange != InsightOnly
```

## Human×AI reasoning

Retain:

```text
AIAssistedConclusion != HumanIndependentInference
HumanInLoop != ErrorCorrectionGuarantee
AIAdviceBeforeJudgment != AIAdviceAfterJudgment
Warning != CalibratedTrust
SlowDown != DebiasGuarantee
SameAIModel + DifferentHarness != SameReasoningOutcome
HumanFirst != AlwaysBest
AIFirst != AlwaysBest
```

Correct AI can improve Human judgment; erroneous AI can induce automation bias;
interaction order, warning design and structured critique protocols change the
joint reasoning path.

## HF9 research objects

### InferenceProfile_D

```text
{
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

### ProblemSolvingProfile_D

```text
{
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

### CausalInferenceProfile

```text
{
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

### RationalityProfile_N,E

```text
{
  norm N,
  environment E,
  accuracy,
  calibration,
  robustness,
  information cost,
  compute/time cost,
  error asymmetry,
  adaptation under shift
}
```

## High-information falsifiers to preserve

- Wason performance changing with wording, perspective, interaction and feedback;
- identical formal structures producing different content-sensitive strategies;
- working-memory load selectively impairing reasoning under belief/logic conflict;
- natural-frequency/set representations greatly changing Bayesian-task accuracy;
- frequency formats also producing errors when set structure/response mapping is
  poor;
- classic heuristic biases alongside fast-and-frugal success in fitting
  environments;
- recognition-heuristic deviations where Humans use additional cues;
- interventions versus observations producing different causal learning;
- observed versus manipulated values being treated differently;
- causal judgments about physical events/omissions varying with counterfactual
  alternatives and expectations;
- structural analogical transfer versus misleading surface similarity;
- successful mapping followed by adaptation failure;
- expert/novice deep-versus-surface problem representation;
- insight requiring interaction of representational change and search;
- Aha/impasse failing as universal mechanism markers;
- incorrect AI advice reducing Human accuracy, especially as a function of timing;
- valid AI improving clinician judgment in some tasks;
- generic warnings/cognitive forcing failing to guarantee calibration;
- structured AI interaction improving reasoning-process quality over unguided AI
  in a current randomized trial.

## Exact next foundation

Across deduction, Bayesian inference, causal learning, analogy, heuristic search,
problem solving and Human×AI reasoning, HF9 repeatedly reaches the same boundary:

```text
several plausible actions / queries / solution paths exist
```

but inference alone does not specify:

```text
which to choose
whether to gather more information
when to stop
how to sequence actions
whether to explore or exploit
when to commit
when to switch or abandon
```

HF4 provides goal/value/motivation; HF9 provides inference/judgment/search.
The missing bridge is **temporally organized option selection and action policy**.

Therefore the exact next round is:

# HF10 — Decision, Choice, Planning, Strategy, Exploration, Exploitation, Stopping and Commitment

## HF10 starting questions

1. What is decision relative to judgment, choice, action and policy?
2. What is choice relative to HF4 preference/DecisionValue?
3. What is planning relative to reasoning, simulation and prospective memory?
4. What is strategy relative to plan, heuristic, policy and tactic?
5. When should a Human acquire more information rather than act?
6. What is value of information relative to uncertainty, stakes and reversibility?
7. What is exploration relative to exploitation?
8. What is a stopping rule across search, evidence gathering and execution?
9. What is commitment relative to intention, goal commitment and actual action?
10. How do sunk cost, switching cost and option value affect continuation?
11. How do risk, ambiguity, regret and reference points alter choice?
12. How should planning horizon and temporal abstraction be represented?
13. How do AI/tools alter option generation, planning, delegation and override?
14. What next boundary emerges after sequential decision/action policy is rebuilt?

## Candidate HF10 falsifiers

- judgment-choice dissociations;
- risky-choice framing/reference effects;
- preference reversals;
- value-of-information and information-avoidance tasks;
- multi-armed-bandit exploration/exploitation;
- satisficing/stopping/search tasks;
- sunk-cost/escalation-of-commitment paradigms;
- precommitment and option restriction from HF4;
- model-based/planning versus habitual control;
- hierarchical planning and horizon effects;
- plan failure under changing internal state;
- AI-generated option sets causing improvement versus choice overload;
- AI planning/delegation and Human override/deference.

## Do not precommit

HF9 does not establish that:

- decision is judgment;
- choice reveals stable preference/value;
- maximizing expected utility is the psychological algorithm of all choice;
- more options are always better;
- more information is always worth acquiring;
- exploration is irrational waste;
- exploitation is always efficient;
- planning is explicit verbal simulation;
- a plan is a fixed script;
- commitment is equivalent to goal strength;
- sunk costs should psychologically or normatively determine continuation;
- AI-generated plans improve independent Human planning by default;
- delegating action removes Human responsibility/authority questions.

## Stop rule

Do not schedule HF11 now. HF10 must expose a repeated neighboring distinction whose
absence creates category failures across materially different decision/planning
cases.

## Supersession — HF10 complete

HF10 has completed the decision/choice/planning/strategy boundary selected here.
Current continuation is owned by
[`HF10-CONTINUATION.md`](HF10-CONTINUATION.md). This file remains the canonical
record of why HF10 emerged from HF9.
