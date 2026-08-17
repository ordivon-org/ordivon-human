---
schema_version: 1
id: human.foundations.hf8.continuation
title: Human Foundations Continuation after HF8
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
summary: Exact continuation after HF8. HF8 reconstructs representation, knowledge, belief, concepts, schemas, mental/world models and understanding, then exposes operations over representations—reasoning, inference, causality, counterfactuals, judgment and problem solving—as the next boundary.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.foundations.hf8
  - human.foundations.hf8.sources
---
# Human Foundations Continuation after HF8

## HF8 completed result

HF8's minimum epistemic/representational grammar is:

```text
World / Task / Source
        ↓
Perception / Memory / Testimony / Tool Output
        ↓
Representation
  ├─ Vehicle / implementation
  ├─ Content
  ├─ Referent/target
  ├─ Format/structure
  └─ Uncertainty
        ↓
Epistemic relations
  ├─ Belief / credence
  ├─ Source attribution / provenance
  ├─ Evidence / reliability
  ├─ Knowing-that
  ├─ Knowing-how
  └─ Verification capability
        ↓
Organized structures
  ├─ Concepts
  ├─ Schemas
  └─ Mental/world models
        ↓
Use surfaces
  ├─ Recall
  ├─ Classification
  ├─ Explanation
  ├─ Prediction
  ├─ Counterfactual simulation
  ├─ Intervention
  ├─ Transfer
  ├─ Error detection
  └─ Action
        ↓
Feedback / evidence / error
        ↺
Revision
```

## Representation boundary

Retain:

```text
RepresentationalVehicle != RepresentationalContent
RepresentationalContent != ReferentExistence
Representation != Truth
RepresentedContent != WorldTruth
Represented(P) != Believes(P)
Representation != Experience
MentalModel != AllRepresentation
WorldModel != BeliefSet
CoherentModel != CompleteTrueModel
```

`Representation` remains a typed relation/family, not one neural/symbolic object.

## Knowledge / knowing

Retain:

```text
Memory != Knowledge
Knowledge != CurrentRecall
KnowingHow_D != KnowingThat(P)
OneSuccessfulAction != KnowingHow
KnowingThat(P) != RememberingLearningEpisode(P)
ContentKnowledge != SourceKnowledge
KnowledgeClaim != ActionAuthority
KnowledgeAvailable != KnowledgeUsedInJudgment
Knows(P) != Uses(P)
```

HF8 does not freeze one philosophical necessary/sufficient definition of
propositional knowledge.

## Belief

Use:

```text
Belief(H,P,t)
= current endorsement/treatment of P as world-descriptive for relevant cognition
  or action at t
```

while retaining:

```text
Belief != Memory
Belief != Representation
Belief != Confidence
Credence != CategoricalBelief
CorrectionRemembered != CorrectionBelieved
BeliefUpdate != MemoryUpdateOnly
ReliableSource != AutomaticallyTrueClaim
Correction != UniversalBackfire
Behavior != Belief
BeliefReport != Belief by definition
```

## Concepts

Concept representation remains plural:

```text
Prototype
Exemplar
Rule
Feature/relational structure
Schema-supported strategy
```

Retain:

```text
LexicalLabel != Concept
Concept != PrototypeOnly
Concept != ExemplarSetOnly
Concept != RuleOnly
SameCategoryAccuracy != SameRepresentationalStrategy
ConceptGeneralization != ExemplarRecognition
```

## Schema

Working definition:

```text
Schema
= organized prior relational/structural knowledge that constrains encoding,
  interpretation, inference, retrieval and integration in a domain
```

Retain:

```text
Schema != Concept
Schema != MemoryDatabase
Schema != Truth
SchemaCongruence != Veridicality
SchemaBenefit can coexist with SchemaBias
```

## Mental/world model

Retain:

```text
MentalModel
= representation preserving relevant relational/possibility structure for
  reasoning/simulation/prediction

WorldModel_D
= organized representation supporting prediction/explanation/simulation/
  intervention over domain D
```

without claiming one universal architecture.

## Understanding

Use a profile rather than one scalar:

```text
UnderstandingProfile_D = {
  relational organization,
  explanation,
  prediction,
  counterfactual reasoning,
  intervention planning,
  error detection,
  transfer/generalization,
  abstraction/compression,
  boundary awareness,
  uncertainty calibration,
  tool dependence
}
```

Strong anti-collapses:

```text
Understanding != Recall
Familiarity != Understanding
FeelingOfUnderstanding != DemonstratedUnderstanding
Expertise != PerfectUnderstandingCalibration
Explanation != Understanding
ExplanationLength != ExplanationQuality
PredictionAccuracy != CompleteUnderstanding
TransferSuccess != CompleteUnderstanding
Calibration != Understanding
ProceduralSuccess != ConceptualUnderstanding
Compression != Understanding
KnowledgeBreadth != UnderstandingDepth
```

## External / Human×AI epistemics

Retain:

```text
ExternalAnswerAccess != InternalKnowledge
SearchSuccess != Understanding
TeamKnowledgeCapability != IndividualKnowledge
JointSuccess != IndividualCompetence
AIAssistedAnswer != HumanUnderstanding
AIUse != Deskilling
AIUse != LearningGain
AssistedPerformance != LearnedCapability
AIEffect_D != AIEffect_E
Knowledge != Authority
```

High-information evidence:

- Internet search can inflate estimates of internal knowledge;
- search-based learning can yield weaker later unaided memory despite comparable
  confidence;
- human/AI partner support can induce misattribution of joint success to individual
  competence;
- unguarded GPT-4 support can improve practice performance while worsening later
  unaided performance in a high-school mathematics field experiment;
- learning-oriented guardrails/scaffolds can materially change that trajectory;
- other structured educational AI interventions show neutral or positive outcomes,
  so `AI causes learning harm` is not retained as a general law.

## HF8 research objects

### RepresentationProfile_D

```text
{
  content scope,
  format/structure,
  fidelity/accuracy,
  compression,
  generalization,
  predictive adequacy,
  causal adequacy,
  retrievability,
  updateability,
  provenance links,
  uncertainty,
  action usefulness
}
```

### BeliefProfile

```text
{
  endorsement,
  credence/confidence,
  supporting evidence,
  source model,
  counterevidence,
  correction history,
  accessibility,
  action relevance,
  updateability,
  calibration
}
```

### KnowledgeProfile_D

```text
{
  factual/propositional content,
  procedural capability,
  source/provenance,
  verification ability,
  transfer/generalization,
  currency,
  reliability under perturbation,
  external dependencies,
  uncertainty
}
```

### UnderstandingProfile_D

```text
{
  relational coherence,
  explanation,
  prediction,
  counterfactuals,
  intervention,
  transfer,
  error detection,
  abstraction/compression,
  boundary awareness,
  calibration,
  tool dependence
}
```

## High-information falsifiers to preserve

- semantic/general knowledge despite severe episodic recollection impairment;
- skill knowing-how despite declarative-memory impairment;
- content recognition with source-monitoring failure;
- prototype-like versus exemplar-like versus rule-like category generalization;
- same category accuracy with different inferred representation strategy;
- schema-enhanced learning plus schema-consistent distortion;
- relational mental-model reasoning and systematic errors from omitted possibilities;
- illusion of explanatory depth before attempted explanation;
- expertise coexisting with explanatory overconfidence;
- explanation improving hypothesis generation but not evaluation;
- correction memory versus later belief regression;
- source reliability altering belief update;
- knowledge neglect in illusory-truth paradigms;
- Internet search increasing answer access/self-confidence but weakening later
  internal learning in some designs;
- human/AI partner knowledge misattribution;
- assisted GPT practice gain with worse unaided later math performance under
  unguarded design versus mitigated harm under scaffolded design.

## Exact next foundation

HF8 repeatedly needs operations over representations:

```text
infer conclusion
compare hypotheses
integrate evidence
attribute cause
simulate alternative
select explanation
solve novel problem
revise belief/model
```

These operations cannot be reduced to representation, memory or belief status.

Therefore the exact next round is:

# HF9 — Inference, Reasoning, Causality, Counterfactuals, Judgment and Problem Solving

## HF9 starting questions

1. What is inference relative to association, retrieval and explicit reasoning?
2. What is reasoning: rule application, mental-model construction, probabilistic
   update, heuristic search, simulation, or a family of processes?
3. How should deduction, induction, abduction and analogy be separated?
4. What is a causal representation relative to correlation/prediction?
5. How do intervention and observation support different causal inferences?
6. What is counterfactual reasoning relative to imagined possibility and causal
   dependence?
7. What separates explanation generation from explanation evaluation?
8. What is a heuristic, and when is it ecologically rational versus biased?
9. What is judgment relative to belief, confidence, value and decision?
10. What is problem solving relative to search, planning, representation change,
    insight and learned procedure?
11. How do attention/working-memory constraints alter reasoning without defining
    reasoning itself?
12. How do expertise, diagrams, software and AI change the inference/search space?
13. How should uncertainty and source/evidence quality propagate through inference?
14. What next boundary emerges after transformations among representations are
    reconstructed?

## Candidate HF9 falsifiers

- Wason/conditional reasoning;
- mental-model illusory inference;
- base-rate and Bayesian-update tasks;
- causal observation versus intervention;
- common-cause/confounding cases;
- counterfactual causal attribution;
- conjunction/availability/representativeness effects and their ecological
  boundary cases;
- analogical transfer;
- insight versus incremental problem solving;
- explanation-generation versus evaluation dissociations;
- expert/novice problem representation;
- diagram/external representation effects;
- AI-assisted reasoning versus independent reasoning after tool removal.

## Do not precommit

HF8 does not establish that:

- all inference is conscious;
- reasoning is one faculty;
- formal logic is the psychological mechanism of all deduction;
- mental-model theory explains every reasoning task;
- Bayesian updating is the universal Human algorithm;
- heuristics are intrinsically irrational;
- causal inference is only correlation detection;
- counterfactuals are always explicit verbal simulations;
- explanation generation guarantees explanation evaluation;
- problem solving is only search;
- expertise always improves reasoning;
- AI assistance necessarily improves or degrades independent reasoning.

## Stop rule

Do not schedule HF10 now. HF9 must expose a repeated neighboring distinction whose
absence creates category failures across materially different reasoning/inference
cases.
