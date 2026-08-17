---
schema_version: 1
id: human.foundations.hf21
title: HF21 — Affect, Emotion, Mood, Appraisal and Affective World Coupling
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
summary: Thin canonical foundation extraction from HD2. HF21 reconstructs affective world coupling as a history-dependent coordination process linking perceived world/body, goals/needs/values, appraisal and social context to partially dissociable feeling, physiological, motivational, cognitive, expressive, categorical and social components; separates emotion episode/category, affect, mood, appraisal, valence, arousal, action readiness, expression and regulation; and preserves plural emotion model families without reopening HF0–HF20.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.deep-foundations.hd2
  - human.deep-foundations.hd2.sources
  - human.foundations.hf21.sources
  - human.foundations.hf21.continuation
---
# HF21 — Affect, Emotion, Mood, Appraisal and Affective World Coupling

## 0. Admission history

HF21 is not a mechanically scheduled successor to HF20.

HD2 was admitted as a non-foundation deep route because affect/emotion/appraisal was a
repeated interface across HF4/HF5/HF14/HF20 and several downstream foundations. HD2 then
showed through cross-cultural, developmental, interoceptive, lesion, mood-learning,
expression and social-emotion falsifiers that the missing neighboring structure is real.

Therefore:

```text
NextFoundationAdmissionCondition(affective world coupling) = true
FoundationReopenCondition(HF0–HF20) = false
```

HF21 is the thin canonical extraction; HD2 remains the deep evidence/model owner.

---

# 1. Minimum affective world-coupling grammar

```text
PerceivedExternalState_t
+ PerceivedInternal/RegulatoryState_t
+ Goals / Needs / Values_t
+ Memory / LearnedSignificance / Concepts_t
+ Social / Relational / Norm Context_t
        ↕
Appraisal / AffectiveInference_t
        ↕
AffectiveEpisodeState_t
  ├─ valence-related state
  ├─ subjective/physiological activation
  ├─ physiological response
  ├─ action readiness
  ├─ attention / memory modulation
  ├─ conscious feeling
  ├─ expression / display
  ├─ category / concept attribution
  └─ social / communicative effects
        ↕
Action / Communication / Regulation / Learning_t
        ↕
World / Body / Relationship_{t+1}

Mood / persistent affective context
↔ biases later appraisal, expectation, learning and episodes
```

This is a typed coordination grammar, not one emotion theory.

---

# 2. Affect is not emotion

`Affect_D` must state what surface is meant, such as:

```text
experienced pleasantness/unpleasantness
positive/negative affect rating
activation-related state
broad affective response family
```

Therefore:

```text
Affect != EmotionByDefinition
```

---

# 3. Emotion episode is not emotion category

```text
EmotionEpisode_D
= temporally extended, context-linked coordination among a declared subset of
  affective, physiological, appraisal, experiential, motivational, cognitive,
  expressive and social components
```

An emotion category is a classification over episodes/cues.

```text
EmotionEpisode != EmotionCategory
```

---

# 4. Emotion category is not biological essence

```text
CategoryUsefulness != CategoryEssence
```

Distributed category-specific patterns can exist without one dedicated brain module,
physiological signature or facial configuration per label.

---

# 5. Feeling is not the whole episode

```text
Feeling != EmotionEpisodeTotality
```

Feeling is the declared conscious experiential component. An emotion episode may include
physiological, attentional, motivational or expressive changes not identical to that
experience.

---

# 6. Experience is not report

HF2 applies:

```text
AffectiveExperience != EmotionReport
```

Report can depend on concept selection, language, memory, confidence and communication
policy.

---

# 7. Appraisal is not emotion

```text
Appraisal_D
= evaluation/inference of significance relative to declared goals, needs, novelty,
  expectation, agency, control, responsibility, coping potential, norm, self or relation
```

Therefore:

```text
Appraisal != Emotion
AppraisalProcess != ExplicitAppraisalReport
```

---

# 8. Same event does not imply same emotion

```text
SameEventSurface != SameEmotionEpisode
```

because goal state, agency, responsibility, controllability, relationship, memory and
conceptual interpretation can differ.

---

# 9. Emotion is not bodily state

```text
Emotion != PhysiologicalState
SameMeasuredPhysiology != SameAffectiveExperience
```

Bodily state is one input/component, not a sufficient emotion identity.

---

# 10. Emotion is not interoception

```text
InteroceptiveState != Emotion
```

HF5/HF20 remain owners of internal signal/perceptual structure. HF21 owns the affective
coordination in which interoceptive evidence can participate.

---

# 11. Interoceptive accuracy is not emotional insight

```text
InteroceptiveAccuracy != EmotionalConceptualization
InteroceptiveAccuracy != MetaInteroceptiveAwareness
```

Bodily performance, confidence/metacognition and emotion interpretation are separately
typed.

---

# 12. Valence is not emotion

Use `Valence_D` because valence can mean experienced pleasantness, stimulus evaluation or
positive/negative affect rating.

```text
Valence != Emotion
```

---

# 13. Valence is not motivational direction

```text
NegativeValence != Avoidance
PositiveValence != ApproachByDefinition
```

Anger is the canonical negative-valence/approach falsifier.

---

# 14. Action tendency is not valence or action

```text
ActionTendency != Valence
ActionReadiness != ExecutedAction
```

Approach, withdrawal, attack, freezing, hiding, repair or support-seeking can be inhibited,
redirected or strategically selected.

---

# 15. Arousal is typed

Separate:

```text
PhysiologicalActivation_D
SubjectiveArousal_D
CategoryIntensity_D
ExpressionIntensity_D
```

Therefore:

```text
Arousal != EmotionIntensityByDefinition
PhysiologicalArousal != SubjectiveArousalByDefinition
```

---

# 16. Dimension and category are non-exclusive projections

Valence/arousal and discrete category structure can each explain unique information.

Therefore:

```text
DimensionalModel != CategoryModel
```

but not:

```text
DimensionalModel XOR CategoryModel
```

by definition.

---

# 17. Emotion concept can influence perception

Emotion concepts can shape perceptual organization/category interpretation.

Thus:

```text
EmotionConcept != PassiveLabelOnly
```

But:

```text
ConceptInfluence != ConceptNecessityForAllAffect
```

---

# 18. Emotion attribution is not target experience

```text
EmotionAttribution != TargetEmotionExperience
```

Observed expression, situation and relationship are evidence used to infer another mind,
not transparent access to it.

---

# 19. Expression is not internal emotion

```text
Expression != EmotionExperience
```

Expression can be spontaneous, communicative, strategic, posed, amplified or suppressed.

---

# 20. Posed is not spontaneous expression

```text
PosedExpression != SpontaneousExpression
```

Performance on posed-expression recognition tasks is not direct evidence of naturalistic
emotion-reading accuracy.

---

# 21. Production, inference and classification are separate

```text
ExpressionProduction
!= EmotionInferenceAccuracy
!= ExpressionClassification
```

The three questions require different evidence.

---

# 22. Facial configuration is not universal emotion meaning

```text
FacialConfiguration != UniversalEmotionMeaning
```

Cultural/task/conceptual context can alter category and social-motive attribution.

---

# 23. Culture does not imply arbitrary affect

```text
CulturalVariation != NoSharedConstraint
SharedConstraint != UniversalCategoryMapping
```

Some dynamic/threat-related expression structure can recur while detailed category mapping
differs.

---

# 24. Static peak expression is not the whole signal

```text
StaticPeakFace != CompleteExpressionSignal
```

Timing, movement kinematics, intensity dynamics and context can carry information.

---

# 25. Social emotions require relational coordinates

For emotions such as shame, guilt, pride, envy or jealousy, useful models may require:

```text
self/other
agency
responsibility
norm
status
relationship
comparison
```

Therefore valence/arousal alone is generally insufficient for the declared social-emotion
question.

---

# 26. Shame is not guilt

```text
Shame != Guilt
```

They can share negative valence while differing in self/social appraisal, action readiness
and measured neural/task structure.

---

# 27. Moral emotion is not moral judgment

HF14 remains authoritative:

```text
MoralEmotion != MoralJudgment
FeelingStrongly(X) != XIsNormativelyTrue
```

---

# 28. Amygdala is not fear

```text
Amygdala != Fear
AmygdalaActivity != FearExperience
```

Internal/interoceptive panic can occur despite bilateral amygdala damage.

---

# 29. Same emotion label can span different causal routes

```text
SameEmotionLabel != SameCausalMechanism
```

External threat and internal suffocation/panic provide a canonical example.

---

# 30. Defensive processing is not conscious fear

```text
DefensiveCircuit != FearFeelingByDefinition
```

Threat detection/action preparation can be studied across species without automatically
asserting identical phenomenal experience.

---

# 31. Evolutionary continuity is evidence-level specific

```text
HomologousDefensiveFunction != IdenticalPhenomenology
SelectedFunction != CurrentConsciousMotive
```

Comparative affect claims must state which level is supported.

---

# 32. Emotion regulation is not self-control or suppression only

```text
EmotionRegulation != SelfControlOnly
EmotionRegulation != Suppression
```

Targets can include situation, attention, appraisal, physiology, expression, action and
recovery.

---

# 33. Regulation endpoint is typed

```text
RegulationOfExpression
!= RegulationOfExperience
!= RegulationOfPhysiology
!= RegulationOfAction
```

Improvement/change on one endpoint does not imply equivalent change on the others.

---

# 34. Regulation can be relational

```text
EmotionRegulation != IntraIndividualProcessOnly
```

Caregivers, partners, groups and institutions can alter affective regulation conditions.

---

# 35. Development changes affective regulation

```text
AdultAffectiveRegulation != ChildAffectiveRegulationByDefinition
```

Caregiver buffering and developing regulatory circuits make developmental context a
mandatory transport coordinate.

---

# 36. Mood is not a long emotion

```text
Mood_D
= relatively persistent affective context with weaker immediate object/event binding and
  potential effects across multiple appraisals, expectations, learning events or choices
```

Therefore:

```text
Mood != LongEmotionByDefinition
DurationAlone != MoodCriterion
```

---

# 37. Mood is not momentary valence

```text
MomentaryValence != MoodByDefinition
```

A declared integration/persistence horizon is required.

---

# 38. Current outcome is not current affect

Affective state can reflect recent expectations and prediction errors, not only current
reward/earnings.

```text
CurrentOutcome != CurrentAffectiveState
```

---

# 39. Mood can alter learning without becoming learning

```text
Mood can bias LearningPolicy
Mood != LearningRate
```

HF6/HF10 remain learning/decision owners.

---

# 40. Affective dynamics are recurrent

```text
Outcome / Appraisal
→ Affect / Mood
→ Attention / Interpretation / Learning
→ changed Expectation
→ changed future Affect
↺
```

Affect is not merely a post-decision output.

---

# 41. Stress is not emotion

HF5 owns stress mechanisms.

```text
StressResponse != Emotion
```

Stress can alter affective probability and emotion can alter stress regulation without
identity.

---

# 42. Pain is not emotion

HF5 owns nociception/pain.

```text
PainExperience != EmotionCategoryByDefinition
```

Pain can contain unpleasant affect and evoke emotions without itself being one universal
emotion category.

---

# 43. Current organism state changes affective coupling

Sleep, fatigue, illness, drugs and hormonal/physiological state can alter affective
reactivity.

Therefore:

```text
SameStimulus + DifferentOrganismState
!= SameAffectiveResponseByDefinition
```

---

# 44. Pathology is not simply negative-valence excess

Affective disorders can involve:

```text
interoceptive updating
precision
context sensitivity
learning
regulation
persistence
```

Therefore:

```text
AffectivePathology != MeanNegativeValenceByDefinition
```

---

# 45. Emotion differentiation is representational

```text
EmotionDifferentiation != NumberOfPhysiologicalStates
```

It concerns the granularity/structure with which episodes are represented or categorized.
HF8 remains representation owner.

---

# 46. Emotion language is not affect

```text
EmotionLanguage != Affect
EmotionLanguage can modify EmotionRepresentation
```

Language/symbol remains a separate candidate deep domain.

---

# 47. Emotion inference is not facial recognition

```text
EmotionInference != FacialRecognition
```

Humans can infer emotions from situations, goals and relations even without a visible
expression.

---

# 48. Human×AI affect boundary

Artificial systems can generate:

```text
emotion labels
empathetic text
expressive faces/voices
affect-conditioned policies
emotion predictions
```

These do not establish:

```text
experienced valence
felt emotion
mood
sentience
```

Therefore:

```text
AffectiveSimulation != AffectiveExperience
AIEmotionDisplay != EvidenceOfFeelingByDefinition
```

HF2/HF15 govern experience/sentience evidence.

---

# 49. Model-family plurality

HF21 retains question-relative use of:

```text
discrete/basic category models
dimensional/core-affect models
appraisal models
psychological construction / conceptualization
interoceptive/predictive models
reinforcement/value/mood-learning models
action-readiness models
social-functional/communication models
evolutionary/defensive-system models
component-process/dynamical models
```

No family owns `Emotion` universally.

---

# 50. Reconnection to prior foundations

```text
HF2  experience / consciousness
HF3  attention / access / metacognition
HF4  goals / value / reward / motivation
HF5  regulation / interoception / stress / pain
HF6  persistent learning/development
HF7  memory
HF8  representation / concepts
HF10 decision
HF11 action
HF12 interaction / communication
HF13 norms / social order
HF14 welfare / morality
HF15 sentience / standing
HF20 perception / sensing
```

HF21 owns the affective coordination bridge among these surfaces. It does not replace them.

---

# 51. Durable HF21 firewalls

```text
Affect != Emotion
EmotionEpisode != EmotionCategory
EmotionCategory != BiologicalEssence
Feeling != EmotionEpisodeTotality
AffectiveExperience != EmotionReport
Appraisal != Emotion
AppraisalProcess != ExplicitAppraisalReport

Emotion != PhysiologicalState
Emotion != Interoception
InteroceptiveAccuracy != EmotionalInsight
Valence != Emotion
NegativeValence != Avoidance
ActionTendency != Valence
ActionReadiness != Action
Arousal != EmotionIntensity
PhysiologicalArousal != SubjectiveArousal

Dimension != Category
EmotionConcept != PassiveLabelOnly
ConceptInfluence != ConceptNecessityForAllAffect
EmotionAttribution != TargetExperience
Expression != EmotionExperience
PosedExpression != SpontaneousExpression
ExpressionProduction != EmotionInferenceAccuracy != ExpressionClassification
FacialConfiguration != UniversalEmotionMeaning

Shame != Guilt
MoralEmotion != MoralJudgment
Amygdala != Fear
SameEmotionLabel != SameCausalMechanism
DefensiveCircuit != FearFeeling
HomologousFunction != IdenticalPhenomenology

EmotionRegulation != Suppression
RegulationOfExpression != RegulationOfExperience != RegulationOfPhysiology
Mood != LongEmotion
MomentaryValence != Mood
StressResponse != Emotion
PainExperience != EmotionCategory
SamePhysiology != SameFeeling
AffectiveSimulation != AffectiveExperience
```

---

# 52. Foundation status

```text
HF0–HF20 reopen = false
HF21 admission = satisfied through HD2
HF21 status = complete / READY
HF22 = UNKNOWN / not admitted
```

---

# 53. Stop rule

Do not expand HF21 into an encyclopedic catalogue of emotions, psychiatric disorders or
brain regions.

Reopen only if later evidence shows that its minimum distinctions repeatedly cause
category errors or cannot represent materially different affective cases without hidden
choices.

The strongest next deep residual is social cognition / other-mind modeling / attachment /
persistent relations. That does not automatically imply HF22.
