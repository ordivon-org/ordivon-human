---
schema_version: 1
id: human.deep-foundations.hd2
title: HD2 — Affect, Emotion, Mood, Appraisal and Affective World Coupling
type: research
profile: research
lifecycle: completed
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
  - builder
updated: 2026-08-17
summary: Deep reconstruction of affective world coupling after HD1/HF20. HD2 separates affect, emotion episode/category, mood, appraisal, valence, arousal, physiological response, interoception, action readiness, expression/display, conscious feeling, emotion attribution and regulation; compares discrete/basic, dimensional/core-affect, appraisal, constructionist, interoceptive/predictive, reinforcement/mood-learning, action-readiness, social-functional and evolutionary/defensive model families; and pressure-tests them across culture, development, amygdala lesions, psychopathology, sleep, social emotions, spontaneous expression and Human×AI. HD2 establishes a true missing neighboring affective structure and supports thin canonical extraction as HF21 without reopening HF0–HF20.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.deep-foundations.hd1.continuation
  - human.deep-foundations.hd2.sources
  - human.deep-foundations.hd2.continuation
  - human.foundations.hf4
  - human.foundations.hf5
  - human.foundations.hf14
  - human.foundations.hf20
---
# HD2 — Affect, Emotion, Mood, Appraisal and Affective World Coupling

## 0. Status and decision

HD2 began from the strongest residual left by HD1/HF20:

```text
perceived external state
+ perceived bodily/regulatory state
+ learned significance/value
+ social/relational context
+ appraisal
→ affective / emotional dynamics
→ attention / action / memory / communication
```

HF4 already separated value/reward/motivation and retained a thin affect surface. HF5
reconstructed interoception, pain, stress and regulatory state. HF14 used affect as one
welfare and moral-emotion surface. HF20 reconstructed perceptual world coupling. None of
those rounds independently owned the transformation among these surfaces.

HD2 finds that this is a genuine neighboring structure rather than detail debt.

```text
NextFoundationAdmissionCondition(affective world coupling) = true
FoundationReopenCondition(HF0–HF20) = false
```

A thin canonical extraction is therefore warranted as HF21. HD2 remains the deep evidence,
model-comparison and falsifier owner.

---

# 1. The first error: `Emotion` is not a single latent scalar or label

A typical emotion episode can involve some combination of:

```text
eliciting event / situation
perceptual interpretation
bodily / interoceptive state
relevance / appraisal
valence / activation profile
autonomic / endocrine response
action readiness
attention / memory modulation
facial / vocal / postural behaviour
conscious feeling
emotion concept / category label
social communication / inference
regulation
```

These components are often coupled but can dissociate.

Therefore:

```text
Emotion != OneScalar
Emotion != OneReadout
```

---

# 2. Minimum affective world-coupling grammar

HD2 retains a recurrent rather than strictly serial grammar:

```text
ExternalWorldState_t / SocialSituation_t
        ↓ HF20 perception
PerceivedExternalState_t

InternalPhysical/RegulatoryState_t
        ↓ HF5 / HF20 interoception
PerceivedInternalState_t

Goals / Needs / Values / LearnedSignificance_t
        ↓ HF4 + HF6/HF7/HF8
Context / Memory / Concepts / Relationship / Norms_t
        ↓
Relevance / Appraisal / AffectiveInference_t
        ↕
AffectiveEpisodeState_t
  ├─ valence-related state
  ├─ subjective / physiological activation
  ├─ autonomic / endocrine / motor preparation
  ├─ action readiness
  ├─ attention / perception bias
  ├─ memory / learning modulation
  ├─ conscious feeling
  ├─ expression / display
  ├─ category / concept attribution
  └─ social signalling / coordination effects
        ↓
Action / Communication / Regulation_t
        ↓
World / Body / Relationship_{t+1}
        ↺

Mood / persistent affective context
↔ biases appraisal, expectations, learning and future episodes

History / development / culture
→ updates concepts, appraisals, priors, expression norms and regulation policies
```

This is a typed coordination grammar, not one emotion theory.

---

# 3. Affect is broader than emotion

`Affect` is used inconsistently across literatures. HD2 retains it only as a declared
family term for valenced/activation-related experiential or functional states.

```text
Affect_D
```

must state whether it means:

```text
experienced pleasantness/unpleasantness
positive/negative affect rating
activation/arousal-related state
broad affective response family
```

Therefore:

```text
Affect != EmotionByDefinition
```

---

# 4. Emotion episode is not emotion category

Define minimally:

```text
EmotionEpisode_D
= temporally extended, context-linked trajectory in which a declared subset of
  appraisal, bodily, experiential, motivational, cognitive, expressive and social
  components becomes coordinated strongly enough for question D
```

An `EmotionCategory_D` is a classification over episodes or cues.

Thus:

```text
EmotionEpisode != EmotionCategory
```

and different classification systems may carve the same episode space differently.

---

# 5. Emotion category is not biological essence

A label such as:

```text
fear
anger
sadness
guilt
pride
```

can be useful without implying one immutable physiological or neural essence.

Therefore:

```text
CategoryUsefulness != CategoryEssence
```

---

# 6. Feeling is not the whole emotion episode

A `Feeling_D` is the conscious experiential component declared by the model/question.

```text
Feeling != EmotionEpisodeTotality
```

An episode may include physiological preparation, attentional change or action readiness
before or without a fully articulated conscious category report.

Conversely a conscious feeling report can occur after the eliciting event and be shaped by
memory/concepts.

---

# 7. Report is not feeling

HF2 applies directly:

```text
AffectiveExperience != EmotionReport
```

Report additionally requires some combination of access, concept selection, language,
memory, confidence and communication policy.

---

# 8. Appraisal is not emotion

Define appraisal minimally:

```text
Appraisal_D
= evaluation/inference of an event, state or relation along declared significance
  dimensions relevant to goals, needs, agency, control, novelty, expectation,
  responsibility, norm, self or social relation
```

Appraisal can be rapid, partial and not necessarily verbal.

Therefore:

```text
Appraisal != Emotion
```

---

# 9. Appraisal is not always conscious judgment

An organism can differentially respond to novelty, controllability, agency or threat before
forming an explicit verbal judgment.

Thus:

```text
AppraisalProcess != ExplicitAppraisalReport
```

---

# 10. The same event can yield different emotions through different relational meaning

Emotion inference from situations is not reducible to valence/arousal alone. Human neural
patterns for inferred emotions can reflect high-dimensional event features such as agency,
goal relevance and situational structure.

Therefore:

```text
SameEventSurface != SameEmotionEpisode
```

when appraisal, relationship or goal state differs.

---

# 11. Emotion is not bodily state

Body state matters, but HD2 rejects:

```text
Emotion = PhysiologicalState
```

Respiratory-perturbation studies show groups with comparable measured respiratory,
cardiovascular and behavioural responses can report materially different suffocation fear
and stress.

Thus:

```text
SameMeasuredPhysiology != SameAffectiveExperience
```

---

# 12. Emotion is not interoception

HF5/HF20 distinguish internal physical state, interoceptive signal, representation,
performance and experience.

HD2 adds:

```text
InteroceptiveState != Emotion
```

because bodily evidence must interact with context, learned significance and appraisal.

---

# 13. But interoception can materially shape affective episodes

Psychopathology studies under breath-hold perturbation show that adaptive precision or
sensitivity to bodily change can differ across groups and can covary with distress/fear.

Therefore:

```text
Interoception is causal/input-relevant in some affective episodes
```

without becoming emotion identity.

---

# 14. Interoceptive accuracy is not emotional insight

Alexithymia research provides a useful dissociation: people can show relatively strong
performance/sensibility on some bodily tasks yet poorer metacognitive correspondence or
difficulty interpreting emotional arousal.

Thus:

```text
InteroceptiveAccuracy != EmotionalConceptualization
InteroceptiveAccuracy != MetaInteroceptiveAwareness
```

---

# 15. Valence is not emotion

Valence is itself overloaded. It can mean:

```text
experienced pleasantness/unpleasantness
stimulus evaluation
approach-compatible value
positive/negative affect rating
```

HD2 therefore uses:

```text
Valence_D
```

and rejects:

```text
Emotion = Valence
```

---

# 16. Negative valence is not avoidance

Anger is the canonical falsifier.

Dispositional and state-related anger can be negatively valenced while showing neural and
behavioural signatures associated with approach motivation.

Thus:

```text
NegativeValence != Avoidance
PositiveValence != ApproachByDefinition
```

---

# 17. Action tendency is not valence

Possible action readiness includes:

```text
approach
withdraw
attack
freeze
submit
seek support
repair
hide
explore
```

These do not map one-to-one onto pleasant/unpleasant feeling.

```text
ActionTendency != Valence
```

---

# 18. Action readiness is not executed action

An anger episode can prepare confrontation while action is inhibited by authority, risk,
norm, strategy or self-regulation.

Therefore:

```text
ActionReadiness != Action
```

HF11 remains the execution owner.

---

# 19. Arousal is not intensity

At least distinguish:

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

# 20. Dimensional affect is real but incomplete

Neural studies show valence and arousal explain meaningful variance in emotional
representations.

But categorical information can explain additional independent variance.

Therefore:

```text
ValenceArousalModel = useful projection
!= EmotionTotality
```

---

# 21. Discrete categories are real as discriminable patterns but need not be essences

Multivariate studies can classify induced fear, happiness, sadness, anger, disgust or
surprise above chance and can generalize across induction methods.

This supports:

```text
EmotionCategory can correspond to distributed discriminable pattern
```

but not:

```text
EachEmotion = OneDedicatedBrainModule
```

---

# 22. Category and dimension can coexist

Some neural/model-comparison studies are best captured by both categorical and dimensional
features.

Thus the binary:

```text
Discrete OR Dimensional
```

is often too strong.

HD2 retains:

```text
CategoryStructure + DimensionalStructure
```

as potentially non-exclusive projections.

---

# 23. Emotion concepts can alter emotion perception

2024 EEG/fMRI work shows conceptual emotion knowledge predicts perceptual representation
of body expressions and modulates ventral visual encoding.

Therefore:

```text
EmotionConcept != PassiveLabelAfterPerception
```

Concepts can participate in upstream perceptual organization.

---

# 24. But concept influence does not prove all affect is concept-generated

HD2 rejects the reverse leap:

```text
ConceptAffectsPerception
→ AllAffectRequiresLanguageConcept
```

Nonverbal infants, animals, bodily perturbations and rapid defensive responses prevent
such a universal conclusion.

---

# 25. Emotion attribution is not emotion experience

When observing another person:

```text
ObservedCue
→ EmotionAttribution
```

is an inference about the other, not direct access to their feeling.

Therefore:

```text
EmotionAttribution != TargetEmotionExperience
```

---

# 26. Expression is not emotion experience

Facial/vocal/postural behaviour can be:

```text
spontaneous
communicative
strategic
posed
suppressed
amplified
```

Thus:

```text
Expression != InternalEmotionByDefinition
```

---

# 27. Posed expression is not spontaneous expression

Large preregistered cross-cultural studies show emotion recognition is systematically
different for posed versus spontaneous dynamic expressions.

Therefore:

```text
PosedExpression != SpontaneousExpression
```

and laboratory recognition accuracy on posed faces cannot be transported directly to
natural emotion-reading accuracy.

---

# 28. Expression recognition is not expression production

Separate questions:

```text
Q1 what does an expresser produce while feeling/communicating?
Q2 what internal state does the perceiver infer?
Q3 how does the perceiver classify a visible pattern?
```

Therefore:

```text
ExpressionProduction
!= EmotionInferenceAccuracy
!= ExpressionClassification
```

---

# 29. Facial configuration is not pancultural emotional meaning

Remote-culture studies show that prototypical Western facial configurations do not map
uniformly to the same emotion/social-intention labels without conceptual/task scaffolding.

A gasping `fear` face can be interpreted as threat/anger in a Melanesian context.

Thus:

```text
FacialConfiguration != UniversalEmotionMeaning
```

---

# 30. Culture changes mapping without implying arbitrary affect

Cross-cultural evidence also shows partial similarities, especially for some threat-related
signals and broad dynamic structure.

Therefore:

```text
CulturalVariation != NoSharedConstraint
SharedConstraint != UniversalCategoryMapping
```

---

# 31. Emotion communication is dynamic

Dynamic facial-expression work shows receivers use temporally distinct movement components
for category versus intensity information, with both shared and culture-specific patterns.

Thus:

```text
StaticPeakFace != CompleteExpressionSignal
```

---

# 32. Social emotion requires relational representation

Shame, guilt, pride, embarrassment, envy and jealousy cannot be represented by valence and
arousal alone without losing:

```text
self-evaluation
other-evaluation
agency
responsibility
norm
status
relationship
```

Therefore:

```text
SocialEmotion_D
requires declared relational/social appraisal coordinates
```

---

# 33. Shame is not guilt

Human fMRI studies during social moral evaluation show shame and guilt ratings can map to
different neural response patterns and social-evaluative contexts.

Thus:

```text
Shame != Guilt
```

without claiming one invariant neural signature for either emotion.

---

# 34. Moral emotion is not moral judgment

HF14 remains correct:

```text
MoralEmotion != MoralJudgment
```

HD2 supplies the affective machinery that can bias or inform judgment without defining
normative truth.

---

# 35. Emotion does not confer normative authority

```text
FeelingStrongly(X)
!= XIsMorallyTrue
```

Likewise:

```text
Disgust != Wrongness
Anger != Desert
Empathy != Justice
```

HF14 remains normative owner.

---

# 36. Fear is not amygdala activation

Bilateral amygdala-damage cases are a decisive category-error falsifier.

CO2 inhalation can evoke intense fear and panic in people with bilateral amygdala damage.

Therefore:

```text
Amygdala != Fear
AmygdalaActivity != FearExperience
```

---

# 37. External-threat fear and internal panic can recruit different pathways

The same lesion cases distinguish:

```text
ExteroceptiveThreatProcessing
!= InteroceptiveSuffocation/PanicRoute
```

Therefore `fear` can group episodes with materially different causal architecture.

---

# 38. Defensive/survival processing is not felt fear by definition

A circuit that detects looming threat, prepares escape or changes autonomic state is
important to emotion research but does not, by that fact alone, establish conscious fear.

Thus:

```text
DefensiveCircuit != FearFeelingByDefinition
```

This is critical for comparative animal and AI work.

---

# 39. Evolutionary continuity does not imply phenomenal equivalence

Conserved threat-detection and action systems can support evolutionary continuity at a
functional level.

But:

```text
HomologousDefensiveFunction != IdenticalSubjectiveExperience
```

Comparative affect claims must state the evidence level.

---

# 40. Development changes affect regulation architecture

Caregiver presence in children can modulate amygdala reactivity, amygdala-prefrontal
connectivity and behavioural regulation; similar buffering is weaker/different in
adolescence.

Thus:

```text
AdultSelfRegulation != ChildAffectRegulationByDefinition
```

---

# 41. Regulation can be relational

A child can be regulated through another person.

Therefore:

```text
EmotionRegulation != IntraIndividualSelfControlOnly
```

and:

```text
RegulatoryCapability can be relationally scaffolded
```

This reconnects to HF12 and exposes a deeper social-cognition/attachment residual.

---

# 42. Emotion regulation is not emotion suppression

Regulation can alter:

```text
situation selection
situation modification
attention
appraisal / interpretation
expression
physiological response
action
recovery
```

Therefore:

```text
EmotionRegulation != Suppression
```

---

# 43. Regulation target is typed

One can reduce expression without reducing feeling, or reduce subjective distress without
identically changing autonomic activation.

Thus:

```text
RegulationOfExpression
!= RegulationOfExperience
!= RegulationOfPhysiology
!= RegulationOfAction
```

---

# 44. Mood is not a long emotion

Define minimally:

```text
Mood_D
= relatively persistent affective context that is less tightly bound to one immediate
  object/event than a prototypical emotion episode and can bias expectation, appraisal,
  attention, learning or choice over multiple events
```

Therefore:

```text
Mood != LongEmotionByDefinition
```

Duration alone is insufficient.

---

# 45. Mood is not momentary valence

Momentary happiness and other affect ratings can change quickly with outcomes and
expectation errors.

Mood-like context requires a declared persistence/integration horizon.

Thus:

```text
MomentaryValence != MoodByDefinition
```

---

# 46. Affective state can integrate reward history

Human computational work shows momentary subjective well-being is influenced by recent
reward expectations and prediction errors, not simply current accumulated earnings.

This establishes:

```text
CurrentOutcome != CurrentAffectiveState
```

because recent history matters.

---

# 47. Mood can bias future learning

Positive-mood induction can change learning-rate-like behaviour without simply improving
all task performance.

Therefore:

```text
Mood
→ can modify learning policy
```

while:

```text
Mood != LearningRate
```

HF6/HF10 remain learning/decision owners.

---

# 48. Affective dynamics are bidirectional

A general loop is:

```text
Outcome / Appraisal
→ Affect / Mood
→ Attention / Interpretation / Learning
→ changed future expectation
→ changed future Affect
↺
```

This makes affect a dynamical context, not merely a readout after decision.

---

# 49. Stress is not emotion

HF5 owns stressor/stress-response/allostatic-load distinctions.

HD2 retains:

```text
StressResponse != Emotion
```

Stress can change emotional probability/intensity and emotion can alter stress regulation,
but the constructs are not interchangeable.

---

# 50. Pain is not emotion but contains affective experience

HF5 already established:

```text
Nociception != Pain
```

HD2 adds only the boundary:

```text
PainExperience != EmotionCategoryByDefinition
```

although pain has unpleasant affective dimensions and can evoke fear, anger or sadness.

---

# 51. Sleep/wake state alters affective coupling

Sleep deprivation can increase emotional reactivity and alter prefrontal-amygdala coupling.

Therefore:

```text
SameStimulus + DifferentSleepState
!= SameAffectiveResponseByDefinition
```

This is an altered-state pressure on fixed trait interpretations.

---

# 52. Pharmacological/altered-state perturbation can separate affective components

Controlled MDMA studies measure separable changes in neural threat-response circuits,
self-report affect and behaviour.

The methodological lesson is:

```text
DrugEffectOnCircuit
!= DrugEffectOnFeeling
!= DrugEffectOnSocialBehavior
```

unless separately shown.

---

# 53. Psychopathology is not simply “too much negative emotion”

Transdiagnostic interoception studies show altered adaptive precision/updating under bodily
perturbation across anxiety, depression, eating and substance-use groups.

Thus pathology can involve:

```text
precision
updating
context sensitivity
regulation
learning
```

not only mean valence.

---

# 54. Same physiology can yield different clinical affective response

Respiratory challenge studies show heightened suffocation fear/stress in clinical groups
without matching group differences in measured respiratory/cardiovascular responses.

Thus:

```text
AffectivePathology != PhysiologicalHyperreactivityByDefinition
```

---

# 55. Emotion differentiation is a representational property, not emotion count

A person may distinguish anger, shame, disappointment and anxiety finely or collapse them
into broad `bad` states.

This is about representation/category granularity, not necessarily number of bodily
states.

```text
EmotionDifferentiation != NumberOfPhysiologicalStates
```

HF8 owns the general representational machinery.

---

# 56. Language can scaffold emotion categories without owning affect

Emotion words/concepts can shape categorization, memory, communication and even perception.

But affective episodes can occur without full verbal labeling.

Thus:

```text
EmotionLanguage != Affect
EmotionLanguage can modify EmotionRepresentation
```

This leaves language/symbol research as a separate deep candidate.

---

# 57. Emotion recognition from context does not require visible expression

Humans can infer another person's emotional state from situational information alone.
Neural representations can generalize partly between facially perceived and situationally
inferred emotion.

Therefore:

```text
EmotionInference != FacialRecognition
```

---

# 58. Other-mind affect inference is a social-cognition bridge

Inferring another's emotion requires some combination of:

```text
observed behaviour
situation model
goals
beliefs
agency
relationship
norms
```

This is not fully owned by HF12's interaction grammar.

HD2 therefore exposes a strong next residual in social cognition / mentalizing / persistent
relations.

---

# 59. Basic/discrete model family F1

Core claim family:

```text
some emotion categories correspond to partly distinct coordinated response patterns
```

Strengths:

```text
discriminable neural patterns for several induced categories
category-specific action/social functions
some cross-context/cross-cultural regularities
```

Limits:

```text
no one-to-one facial mapping across cultures
category patterns are distributed rather than one module
within-category heterogeneity is large
external versus internal fear can differ causally
```

Disposition: **retain category structure; reject immutable one-program-per-label ontology**.

---

# 60. Dimensional/core-affect family F2

Core claim family:

```text
valence / activation-related dimensions capture important shared affective structure
```

Strengths:

```text
explains broad covariance across emotions
neural evidence for valence/arousal information
useful for mood and welfare surfaces
```

Limits:

```text
cannot uniquely distinguish many emotions
negative valence does not determine approach/avoidance
dimensions miss agency, controllability, norm and social meaning
```

Disposition: **retain low-dimensional projection; reject total reduction**.

---

# 61. Appraisal family F3

Core claim family:

```text
emotion differentiation depends on evaluation of events relative to goals, agency,
control, novelty, responsibility, norm and coping potential
```

Strengths:

```text
explains same-event/different-emotion cases
captures high-dimensional situational emotion inference
naturally represents social emotions
```

Limits:

```text
appraisal dimensions/the ordering are not uniquely fixed across theories
some affective/defensive responses precede explicit appraisal reports
appraisal alone does not specify physiology, feeling or expression
```

Disposition: **retain relational-evaluation mechanism family**.

---

# 62. Psychological-construction / conceptualization family F4

Core claim family:

```text
emotion categories emerge from more general affective/interoceptive/perceptual processes
plus learned conceptual/cultural organization
```

Strengths:

```text
concept effects on body-expression perception
cross-cultural category variation
shared dimensional neural structure
```

Limits:

```text
category-specific distributed patterns exist
nonverbal development/comparative affect prevents language-essentialism
concept influence does not prove concept sufficiency
```

Disposition: **retain conceptual construction as a real mechanism; reject all-affect-is-labeling**.

---

# 63. Interoceptive / predictive family F5

Core claim family:

```text
bodily evidence, expected body state and precision/updating participate in affective feeling
and regulation
```

Strengths:

```text
breath-hold/interoceptive perturbation effects
psychopathology precision differences
internal-threat panic dissociation
```

Limits:

```text
same measured physiology can yield different emotion
interoceptive abilities are domain-specific
not every emotion is driven mainly by visceral perturbation
```

Disposition: **retain body-state inference as major bridge, not emotion ontology**.

---

# 64. Reinforcement/value/mood-learning family F6

Core claim family:

```text
reward expectation, prediction error and recent outcome history shape momentary affect and
persistent mood context, which can feed back into learning/choice
```

Strengths:

```text
large-sample computational fit for momentary happiness
mood manipulation can alter learning
```

Limits:

```text
reward-history models do not explain full social/category structure
reward prediction error != pleasure (HF4)
mood != RL state by definition
```

Disposition: **retain dynamic valuation-learning bridge**.

---

# 65. Action-readiness / motivational-direction family F7

Core claim family:

```text
emotion organizes readiness for context-relevant action
```

Strengths:

```text
anger/approach dissociation from valence
fear/escape, guilt/repair, shame/hide-type hypotheses
```

Limits:

```text
one emotion can support multiple actions depending on context
readiness can be inhibited
same action can arise from different emotions
```

Disposition: **retain action allocation component; reject action=emotion identity**.

---

# 66. Social-functional / communication family F8

Core claim family:

```text
expressive and emotional processes can coordinate social interaction by conveying threat,
submission, affiliation, need, commitment, status or repair signals
```

Strengths:

```text
dynamic expression structure
social emotions
context-sensitive inference
```

Limits:

```text
expression can be posed/strategic
cultural mappings differ
private feeling and public display can dissociate
```

Disposition: **retain social function, separate expression from experience**.

---

# 67. Evolutionary / defensive-system family F9

Core claim family:

```text
some affective architectures build on conserved systems for threat, reward, care,
attachment, exploration and bodily regulation
```

Strengths:

```text
conserved subcortical threat/action systems
functional continuity across species
```

Limits:

```text
homology does not prove identical subjective feeling
current cultural/social emotions add higher-level representations
selected function != current conscious motive
```

Disposition: **retain comparative functional history; preserve evidence-level firewall**.

---

# 68. Component-process / dynamical family F10

HD2's own minimum grammar is closest to a component-process/dynamical stance:

```text
emotion episode
= changing coordination among multiple partially dissociable components over time
```

But this is deliberately thin.

It does not decide that one specific component ordering, appraisal list or neural network is
universally correct.

Disposition: **retain as coordination grammar, not grand theory**.

---

# 69. No universal winner

The strongest evidence is compatible with a plural structure:

```text
low-dimensional affective dimensions
+ category-specific distributed patterns
+ appraisal/event features
+ bodily/interoceptive evidence
+ learned concepts
+ action readiness
+ social signaling
+ reward-history dynamics
```

These are not mutually exclusive in every episode.

---

# 70. Cross-context falsifier matrix

| ID | Context | Collapse attacked | Surviving structure |
|---|---|---|---|
| A01 | anger + left frontal approach signatures | negative valence = avoidance | valence != motivational direction |
| A02 | bilateral amygdala lesion + CO2 panic | amygdala = fear | internal fear/panic can bypass canonical external-threat route |
| A03 | same breath-hold physiology, different clinical fear | body state = feeling | bodily response != affective experience |
| A04 | cardiac interoceptive performance vs alexithymia | body accuracy = emotion insight | performance/metacognition/conceptualization separate |
| A05 | emotion concepts alter body-expression perception | concept = downstream label | concept can shape perceptual representation |
| A06 | Himba sorting without supplied emotion concepts | posed face = universal category | task/concept/culture affect mapping |
| A07 | Trobriand `fear` gasping face as threat/anger | fear face = universal fear meaning | facial configuration != pancultural emotion meaning |
| A08 | posed vs spontaneous expression recognition | posed stimulus = natural emotion readout | expression ecology matters |
| A09 | dynamic expression timing/intensity | static peak face = full signal | temporal expression structure matters |
| A10 | neural valence/arousal + categories | dimension OR category | both projections can carry unique information |
| A11 | discrete category decoding across induction methods | categories = arbitrary labels only | distributed category structure can be discriminable |
| A12 | situation-based emotion inference | emotion = facial recognition | event/appraisal inference matters |
| A13 | abstract event features beyond valence/arousal | emotion = valence/arousal | agency/control/goal/social structure needed |
| A14 | shame vs guilt neural/context differences | all negative moral affect = one state | social emotions require relational coordinates |
| A15 | maternal buffering in children | regulation = self-control | regulation can be relational/scaffolded |
| A16 | child vs adolescent buffering difference | adult regulation = child regulation | developmental architecture changes |
| A17 | reward expectation/prediction-error happiness | current outcome = current affect | recent expectation/history matters |
| A18 | positive mood changes learning | mood = passive readout | mood can bias future learning |
| A19 | sleep deprivation emotional hyperreactivity | emotion = fixed trait | current organism state changes coupling |
| A20 | altered-state pharmacology | circuit change = feeling change | neural/subjective/social endpoints separate |
| A21 | interoceptive precision differences in psychopathology | disorder = negative valence mean | updating/precision/context sensitivity matter |
| A22 | pain vs nociception | noxious signal = affective experience | sensory/affective experience separation |
| A23 | expression suppression/posing | expression = internal state | public display can dissociate |
| A24 | contextual emotion inference | cue meaning = cue alone | situation/relationship modifies attribution |
| A25 | social evaluation shame/guilt | emotion = private bodily state | self/other/norm structure matters |
| A26 | external vs internal fear routes | one label = one mechanism | category can span multiple causal routes |
| A27 | defensive processing without report | defensive action = conscious fear | function != feeling |
| A28 | spontaneous autistic expression differences | expression atypicality = absent emotion | production/interpretation/experience distinct |
| A29 | emotion inference from face vs situation | input modality = emotional representation | abstract emotion representation can generalize |
| A30 | culture-specific dynamic facial expectations | universal expression dictionary | shared + local structure coexist |
| A31 | mood persistence across events | mood = long event emotion | object specificity/history horizon matter |
| A32 | AI-generated emotional language/display | affect display = affective experience | behavioral simulation != sentient feeling evidence |

---

# 71. Minimum retained affective grammar

HD2's strongest reusable reconstruction is:

```text
AffectiveEpisode_D(t0:t1) = {
  ElicitingSituation_D,
  PerceivedExternalState_D,
  PerceivedInternalState_D,
  GoalNeedValueContext_D,
  AppraisalProfile_D,
  ValenceProfile_D,
  ActivationProfile_D,
  PhysiologicalResponse_D,
  ActionReadiness_D,
  AttentionMemoryBias_D,
  Feeling_D,
  ExpressionDisplay_D,
  CategoryConcept_D,
  SocialFunction_D,
  Regulation_D,
  LearningUpdate_D
}
```

No field is automatically required at the same resolution for every question. The point is
to prevent one component from silently standing for all others.

---

# 72. Core HD2 firewalls

```text
Affect != Emotion
EmotionEpisode != EmotionCategory
EmotionCategory != BiologicalEssence
Feeling != EmotionEpisodeTotality
AffectiveExperience != EmotionReport
Appraisal != Emotion
AppraisalProcess != ExplicitAppraisalReport

Emotion != BodilyState
Emotion != Interoception
InteroceptiveAccuracy != EmotionalInsight
Valence != Emotion
NegativeValence != Avoidance
ActionTendency != Valence
ActionReadiness != Action
Arousal != EmotionIntensity
PhysiologicalArousal != SubjectiveArousal

Dimension != Category
Category != DedicatedBrainModule
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
DefensiveCircuit != FearFeeling
HomologousFunction != IdenticalPhenomenology
EmotionRegulation != Suppression
RegulationOfExpression != RegulationOfExperience != RegulationOfPhysiology
Mood != LongEmotion
MomentaryValence != Mood
StressResponse != Emotion
PainExperience != EmotionCategory

SamePhysiology != SameFeeling
SameEmotionLabel != SameCausalRoute
SameExpression != SameInternalState
SameAffectWord != SameEpisodeStructure
AIEmotionDisplay != AffectiveExperience
```

---

# 73. Reconnection to HF2

HF2 remains experience/consciousness owner.

HD2 adds:

```text
AffectiveEpisode can contain a conscious feeling component
but EmotionEpisode != ConsciousExperience
```

No HF2 reopening required.

---

# 74. Reconnection to HF3

Affect can bias attention, priority, confidence and metacognition.

But:

```text
Affect != Attention
EmotionSalience != AttentionAllocationByDefinition
```

HF3 remains attention/control owner.

---

# 75. Reconnection to HF4

HF4 remains owner of:

```text
goal
preference
value
reward
wanting/liking
effort
motivation
self-regulation
```

HD2 expands the affect node into a full episode/coordination grammar.

HF4 does not require repair.

---

# 76. Reconnection to HF5

HF5 remains owner of internal regulation, stress, interoception, fatigue, pain and recovery.

HD2 consumes bodily/interoceptive state as one input/component of affective episodes.

```text
RegulatoryState != Emotion
```

No HF5 reopening required.

---

# 77. Reconnection to HF6/HF7/HF8

Affective learning and emotion concepts depend on history, memory and representation.

But:

```text
AffectiveLearning != MemoryTotality
EmotionConcept != EmotionEpisode
```

HF6/HF7/HF8 remain general history/memory/representation owners.

---

# 78. Reconnection to HF10/HF11

Emotion can change option generation, valuation, stopping, risk perception and action
readiness.

Yet:

```text
Emotion != Decision
ActionReadiness != ExecutedAction
```

HF10/HF11 remain decision/action owners.

---

# 79. Reconnection to HF12/HF13

Emotion expression, contagion, shame, guilt, status threat and caregiver buffering expose
strong relational structure.

HF12/HF13 already own interaction/communication/norm/institution surfaces, but not the
internal model of another mind or persistent attachment/care relation.

This is a major post-HD2 residual.

---

# 80. Reconnection to HF14/HF15

Affect contributes to welfare and sentience evidence but does not define all welfare or
moral status.

```text
PositiveAffect != WelfareTotality
NegativeAffect != HarmTotality
Emotion != MoralStanding
```

HF14/HF15 remain normative/bearer owners.

---

# 81. Reconnection to HF20

HF20 provides:

```text
world/body → perceptual evidence/content
```

HD2 provides:

```text
perceived world/body + goals/values/context
→ affective coordination
```

The bridge is recurrent because affect changes sampling/attention and therefore future
perception.

```text
Perception ↔ Affect
```

without identity.

---

# 82. Human×AI boundary

Artificial systems can produce:

```text
emotion labels
empathetic language
facial/vocal emotional displays
affective predictions
emotion-conditioned policies
```

These are observable functional/communicative surfaces.

They do not establish:

```text
experienced valence
felt emotion
mood
sentience
```

Therefore:

```text
AffectiveSimulation != AffectiveExperience
```

HF2/HF15 evidence rules continue to govern any sentience claim.

---

# 83. Cross-project boundary

```text
Human HD2/HF21:
affective coordination in embodied/social humans

Media:
representation/transmission of emotional cues and induced audience effects

Game:
affective dynamics inside rule-bound player/agent systems

AI / Computer:
artificial affect recognition/generation mechanisms

World:
external situations and physical/social states
```

No project owns `emotion` universally.

---

# 84. Foundation admission audit

HF20's continuation required a repeated neighboring residual. HD2 checks it explicitly.

```text
1. Repeated residual?             yes
   HF4/HF5/HF14/HF20 all consume affect/emotion without independent mechanism closure;
   HF2/HF3/HF7/HF8/HF10/HF11/HF12 also depend on it downstream.

2. Genuine neighboring structure? yes
   appraisal, affective dimensions, physiological/interoceptive components, action
   readiness, feeling, expression, category and mood cannot be represented by one existing
   HF view without hidden choices.

3. Decision/explanation value?   yes
   distinctions change interpretation of regulation, welfare, social communication,
   psychopathology, development and Human×AI affect claims.

4. Not engineering debt?         yes
   scientific representational debt.

5. Not terminology churn?        yes
   lesion, culture, development, physiology, expression and neural-model falsifiers force
   separations.

6. Multi-context evidence?       yes
   culture, lesions, physiology, development, mood-learning, expression, social emotion.

7. Boundary safety?              yes
   conscious feeling, moral truth, authority and AI sentience remain separately governed.
```

Therefore:

```text
NextFoundationAdmissionCondition = true
```

---

# 85. Reopen audit

No existing HF claim is contradicted.

```text
FoundationReopenCondition A repeated error from existing frozen claim?   false
B strong evidence contradicts frozen claim?                              false
C missing neighboring distinction?                                       true — extension
D contradiction across frozen rounds?                                    false
E consumer failure due wording of existing foundation?                   false
F normative authority leak?                                              false
```

Disposition:

```text
Do not reopen HF0–HF20.
Extract a new thin HF21 affect/emotion foundation.
```

---

# 86. What HD2 does not settle

HD2 does not establish:

```text
one canonical emotion list
one autonomic signature per emotion
one brain region per emotion
one universal appraisal sequence
one universal core-affect coordinate system
one universal constructionist account
one universal interoceptive/predictive account
one RL account of mood
one cross-cultural expression dictionary
one animal-human phenomenology mapping
one test for AI emotion experience
```

These remain open/model-relative.

---

# 87. Strongest residual after HD2

HD2 repeatedly requires a model of:

```text
what another person believes/feels/intends
how self and other are represented
how caregiver-child regulation becomes internalized
how attachment, trust, care and persistent dyads change state
how social evaluation creates shame/guilt/pride/status threat
how relationships persist across interactions
```

HF12 owns interaction/joint action/communication, but this deeper `other-mind + persistent
relation` bridge remains interface-rich and mechanism-thin.

Therefore the strongest next **deep route** is:

```text
HD3 — Social Cognition, Other-Mind Modeling, Attachment, Care and Persistent Relations
```

HD3 is research only.

```text
HD3 != HF22
```

---

# 88. Final HD2 compression

Human affect is best retained not as a universal emotion list, bodily readout or two-axis
coordinate, but as a history-dependent coordination process linking perceived world/body,
needs/values, appraisal and social context to partially dissociable experiential,
physiological, motivational, cognitive, expressive and communicative changes over time.

In compact form:

```text
Perception / Body / Value / Context
        ↕
Appraisal / Affective Inference
        ↕
Affective Episode
  [feeling + physiology + action readiness + cognition + expression + category]
        ↕
Action / Communication / Regulation / Learning
        ↕
World / Body / Relationship

Mood/history provide slower context across episodes.
```

This is deeper than `stimulus → emotion label`, but intentionally weaker than one grand
emotion theory.
