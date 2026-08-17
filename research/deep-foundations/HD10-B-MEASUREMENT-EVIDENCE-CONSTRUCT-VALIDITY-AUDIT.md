---
schema_version: 1
id: human.deep-foundations.hd10b
title: HD10-B — Measurement, Evidence and Construct-Validity Audit
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
updated: 2026-08-18
summary: Second deep round of HD10 Individual-Difference Architecture. HD10-B reconstructs what different evidence channels can and cannot support before any personality/intelligence model adjudication. It separates observed response, score, reliability target, temporal stability, construct-validity evidence, cross-method convergence, discriminant structure, predictive utility, measurement invariance, ecological transport, causal evidence and mechanism. It shows that robust group effects can be poor individual-difference measures, high reliability can coexist with weak discriminability or wrong interpretation, prediction does not identify ontology, self/informant disagreement can reflect perspective/context rather than simple error, repeated/intensive sampling is required for within-person dynamics, neural/physiological signals need their own reliability, and Human×Agent performance must be support-boundary typed. HF24 remains UNKNOWN/not admitted and no HF0–HF23 FoundationReopenCondition is triggered.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.deep-foundations.hd10a
  - human.deep-foundations.hd10a.sources
  - human.deep-foundations.hd10b.sources
  - human.deep-foundations.hd10.continuation
  - human.foundations.hf0
  - human.foundations.hf6
---
# HD10-B — Measurement, Evidence and Construct-Validity Audit

## 0. Decision

HD10-B asks one question before comparing personality or intelligence theories:

> **What kind of Human claim is justified by each kind of measurement evidence?**

The round rejects the idea of one scalar `MeasurementQuality`.

A measure can be:

```text
internally consistent
but unstable across time;

stable across time
but insensitive to meaningful change;

excellent for detecting a within-person experimental effect
but poor for ranking persons;

predictive of an outcome
but causally opaque;

factorially invariant across groups
but not a universal causal ontology;

highly reliable
but invalid for the proposed interpretation;

low in cross-rater agreement
because perspectives/contexts genuinely differ,
not only because someone is wrong.
```

Therefore HD10-B establishes:

```text
EvidenceQuality = profile of fit between
measurement procedure × inference target × population × context × timescale × use
```

not one score.

At B close:

```text
HD10-A = complete
HD10-B = complete
HD10-C = next
HF24 = UNKNOWN / not admitted
FoundationReopenCondition(HF0–HF23) = false
```

---

# 1. The measurement target must be declared before reliability

`Reliability` is not one property until the intended variance is declared.

Possible targets include:

```text
item-response consistency
rater agreement
rank-order stability across sessions
absolute-score agreement
within-person state discrimination
between-person discrimination
trajectory/parameter recovery
classification consistency
prediction stability
```

The same instrument can score differently on these targets.

Thus:

```text
ReliableFor_X != ReliableFor_Y
```

and:

```text
ReplicableGroupEffect != ReliableIndividualDifferenceMeasure
```

is a durable HD10 firewall.

---

# 2. Core evidence decomposition

A Human measurement event is represented minimally as:

```text
Observation_O
= Observe(
    Person H,
    target domain D,
    PersonState_t,
    Situation_t,
    Task_t,
    Support_t,
    Rater/Observer_r,
    Instrument_I,
    Procedure_P,
    ScoringRule_S,
    Occasion_t,
    History_t,
    population/sample frame,
    noise/error sources
  )
```

This is not assumed additive.

A useful variance-source checklist is:

```text
stable person-related variance
transient person-state variance
situation variance
person × situation interaction
practice/retest history
support/tool variance
rater/perspective variance
instrument/item/task variance
administration/procedure variance
sampling variance
scoring/model variance
random/unknown error
```

Any claimed `Trait`, `Ability` or `PersonDifferenceProfile` must state which sources are intended signal and which are treated as nuisance.

---

# 3. Score is not the measured property itself

Retain from A:

```text
MeasurementInstrument
!= ObservedResponse
!= Score
!= TargetConstruct
```

HD10-B adds:

```text
ScoreInterpretation
```

as an explicit object.

```text
Score_S(O_1...O_n)
```

is generated under a scoring rule.

Then an interpretation claims something such as:

```text
Score -> current state
Score -> typical behavior
Score -> rank in a reference population
Score -> capacity estimate
Score -> probability of future outcome
Score -> latent construct estimate
```

These are different claims requiring different evidence.

---

# 4. Validity belongs to an interpretation/use, not to a test name alone

Testing standards treat validity as an evidential/theoretical argument supporting the interpretation of scores for proposed uses.

HD10-B therefore rejects:

```text
Test X is valid
```

as insufficient.

Use instead:

```text
ValidityEvidence(
  Instrument,
  Score,
  Interpretation,
  Population,
  Context,
  Use
)
```

Examples:

```text
A personality scale may support rank-order description
without proving causal personality mechanisms.

A cognitive battery may support prediction of task performance
without supporting moral, educational or occupational authority.

A neural measure may track a group-level process
without supporting individual diagnosis.
```

---

# 5. Reliability is necessary for some inferences but not sufficient for validity

For rank-order individual-difference claims, insufficient reliability constrains observable associations and makes person-level interpretation unstable.

But:

```text
HighReliability != CorrectConstruct
HighReliability != ValidUse
HighReliability != CausalMechanism
```

A perfectly repeatable biased instrument remains biased.

A highly stable score can also encode:

```text
stable method variance
stable social environment
stable opportunity
stable response style
stable confounding
```

rather than the proposed internal trait.

---

# 6. The reliability paradox

Classic experimental cognitive tasks were often optimized for robust average effects with low between-person variability.

This creates a structural tension:

```text
ExperimentalGoal:
  maximize within-person effect consistency
  minimize unexplained between-person variance

IndividualDifferenceGoal:
  preserve stable between-person variance
  minimize measurement error relative to that variance
```

Hedge, Powell & Sumner found several classic tasks with robust experimental effects but surprisingly low test–retest reliability for individual differences.

Therefore:

```text
RobustStroopEffect
!= ReliableStroopDifferenceScoreAcrossPersons
```

and more generally:

```text
GoodExperimentalParadigm
!= GoodIndividualDifferenceInstrumentByDefinition
```

This is one of HD10-B's highest-value measurement firewalls.

---

# 7. A positive counterexample: cognitive ability can be measured reliably under stronger designs

HD10-B does not generalize the reliability paradox into `cognitive tests are unreliable`.

Robison et al. (2026) tested 24 cognitive measures twice in `N=255` young adults and reported:

```text
adequate-to-high task reliability for many measures
high construct-level reliability
measurement-structure invariance across occasions
limited practice effects for many measures
latent state-trait models with substantial stable trait-like variance
```

while also finding cases where common task labels did not map cleanly to one common variance source.

Thus:

```text
PoorTaskPsychometrics != Inevitable
```

but also:

```text
ReliableLatentFactor
!= OneCausalMechanism
```

The design of the measurement system matters.

---

# 8. Reliability targets must be separated

## 8.1 Internal consistency

Internal consistency asks whether item/task indicators covary in the declared sample/model.

It does not establish:

```text
temporal stability
cross-context stability
cross-rater agreement
causal unity
unidimensionality by itself
construct validity totality
```

Therefore:

```text
HighInternalConsistency != StableTrait
```

---

## 8.2 Test–retest rank stability

A test–retest correlation/ICC can ask whether persons retain relative positions across occasions.

```text
RankOrderStability
!= MeanLevelStability
```

Everyone can improve while ranks remain similar.

And:

```text
HighTestRetest
!= NoStateEffects
```

if stable persons also have occasion-specific deviations.

---

## 8.3 Absolute agreement

Absolute-score agreement is stronger/different than rank stability.

Practice effects can preserve rank while shifting the whole score distribution.

Therefore:

```text
RankStable != SameAbsoluteScore
```

---

## 8.4 Inter-rater reliability/agreement

Self and informant may observe different contexts and possess different information.

Low agreement can arise from:

```text
measurement error
self-presentation
informant bias
limited observability
relationship-specific behavior
context sampling differences
true perspective-specific information
```

Thus:

```text
SelfInformantDisagreement != ErrorOnly
```

---

## 8.5 Parameter reliability in intensive longitudinal models

For person-specific means, variances, state distributions, transition parameters or response functions, reliability depends on sufficient repeated observations and adequate context sampling.

One questionnaire occasion cannot estimate:

```text
within-person variance
state distribution shape
person-specific transition function
context-response slopes
```

without extremely strong model assumptions.

---

# 9. Practice/retest history is causal, not merely nuisance

Repeating a test can change the Human being measured.

Possible retest effects include:

```text
strategy discovery
automaticity
memory of items
reduced novelty
fatigue
motivation change
proactive interference
learning
response calibration
```

Therefore:

```text
MeasurementOccasion_2
!= PassiveReplicationOfOccasion_1
```

HD10-B retains HF6:

```text
PracticePerformance != Learning
```

and adds:

```text
RetestChange != TraitChangeByDefinition
RetestStability != NoLearningByDefinition
```

A longitudinal design must model measurement history as part of the environment.

---

# 10. Trait-like stability requires more than one repeated score

Evidence for a relatively persistent person difference can strengthen through:

```text
repeated occasions
multiple items/tasks
multiple contexts
multiple raters/methods
sufficient timescale
known measurement error
stable or modeled scoring structure
```

But there is no universal threshold after which `trait` becomes ontologically proven.

Use:

```text
EvidenceForPersistentDifference_D
```

rather than:

```text
TraitProof
```

---

# 11. Experience sampling / ecological momentary evidence

Intensive longitudinal measurement is uniquely useful for distinguishing:

```text
between-person mean differences
within-person variability
state distribution shape
context sensitivity
transition/dependence over time
```

Personality-state research shows substantial within-person variability even where stable between-person differences exist.

Thus:

```text
HighWithinPersonVariability
!= NoIndividualDifference
```

because relatively stable distribution parameters can still differ.

But:

```text
ESMFrequency != EcologicalValidityAutomatically
```

Smartphone prompts can still alter behavior, miss important contexts, burden participants, or oversample accessible states.

Sampling policy must be part of the evidence model.

---

# 12. Within-person claims require within-person evidence

HD10-B strengthens A's firewall:

```text
BetweenPersonAssociation
!= WithinPersonAssociation
```

and:

```text
PopulationFactorStructure
!= PersonTransitionDynamics
```

Schmiedek et al.'s repeated cognitive data showed substantial divergence between within-person structures and the modal between-person cognitive ability structure.

Therefore:

```text
GroupPsychometrics -> IndividualDynamics
```

requires additional assumptions/evidence; it is not a default inference.

---

# 13. Self-report evidence ceiling

Self-report can directly/privilegedly access some surfaces such as:

```text
self-beliefs
felt states
self-concept
subjective preference
reported typical behavior
experienced effort
```

but it can be affected by:

```text
memory reconstruction
current state
reference-group effects
language/interpretation
social desirability
self-presentation
limited introspective access
response style
identity commitments
```

Therefore:

```text
SelfReport != DirectReadoutOfMechanism
SelfReport != BehaviorTotality
SelfReport != ErrorByDefinition
```

For first-person experience, self-report may carry evidence unavailable to external observation; for causal mechanism it remains indirect.

---

# 14. Informant-report evidence ceiling

Informants can provide:

```text
cross-occasion observation
public behavior
social impact
reputation-like regularity
comparison across targets
```

but evidence depends on:

```text
acquaintanceship
relationship context
observability
informant incentives
shared stereotypes
context exposure
question wording
```

Studies of self-informant personality ratings show moderate rather than perfect agreement and method-dependent differences.

Therefore:

```text
InformantReport != ObjectiveTruth
SelfReport != PrivilegedTruthForAllTraits
```

Multi-informant evidence can add information rather than merely average away disagreement.

---

# 15. Cross-method convergence and discriminant evidence

HD10-B adopts a multi-method logic:

For candidate construct X, useful evidence includes whether:

```text
Measure_X_method1
correlates/converges with
Measure_X_method2
```

while remaining distinguishable from neighboring construct Y.

But:

```text
ConvergentValidity != ConstructIdentity
DiscriminantValidity != MechanismProof
```

Convergence can be inflated by shared method variance.

Lack of convergence can reflect:

```text
different timescales
different contexts
different perspectives
poor reliability
construct mismatch
real multidimensionality
```

rather than simple invalidity.

---

# 16. Behavioral-task evidence ceiling

Behavioral tasks provide strong evidence about:

```text
performance under a declared task/protocol
response distributions
speed/accuracy tradeoffs
strategy-dependent effects
learning curves
perturbation sensitivity
```

They do not automatically establish:

```text
general ability
everyday behavior
trait-level stability
cross-context competence
one cognitive mechanism
```

Required metadata:

```text
task demands
trial count
score construction
speed/accuracy criterion
practice history
motivation/incentive
state
support/tools
reliability for the intended individual-difference metric
```

---

# 17. Ability measurement requires a task-sampling argument

`Ability_D` is inferred from performance over a task family, not observed directly.

A credible ability claim should state:

```text
target domain D
task universe / sampling frame
difficulty range
support boundary
time constraints
scoring rule
reliability
practice history
state conditions
transfer evidence
```

Therefore:

```text
OneTaskScore != Ability_D
```

A latent ability estimate may reduce task-specific noise, but:

```text
LatentAbilityFactor
!= CausalProcessByDefinition
```

---

# 18. Maximum performance, typical performance and capability are different targets

A test may aim at:

```text
TypicalPerformance
MaximumPerformance
LearningPotential
CurrentAvailableCapacity
IndependentCapability
SituatedCapability
```

These targets are not interchangeable.

Examples:

```text
person can perform maximally under strong incentive
but not typically;

person performs poorly during illness
but retains learned skill;

person performs strongly with AI/tool support
but not independently;

person initially scores low
but learns rapidly under feedback.
```

Therefore:

```text
MaximumPerformance != TypicalBehavior
LearningRate != CurrentAbilityScore
SupportedPerformance != IndependentCapability
```

---

# 19. Learning/transfer evidence ceiling

HF6 already established transfer as a capability falsifier.

HD10-B uses:

```text
training gain
retention
near transfer
far transfer
novel task transfer
tool removal
```

as distinct evidence surfaces.

A broad capability claim requires broader transfer evidence.

```text
PracticeGain
!= RetainedLearning
!= Transfer
!= GeneralAbilityIncrease
```

---

# 20. Real-world outcome evidence ceiling

Real-world outcomes can establish useful predictive/ecological relations but are strongly multiply caused.

Examples:

```text
academic attainment
income
job performance
relationship stability
health behavior
accidents
creative output
```

Each depends on more than individual internal structure:

```text
Person × Opportunity × Institution × Resources × Support × Selection × Environment
```

Therefore:

```text
PredictsOutcome != InternallyCausesOutcome
OutcomeCorrelation != TraitIdentity
```

Predictive utility remains valuable but must not be converted into essence.

---

# 21. Digital trace evidence ceiling

Smartphone/log traces can provide high-volume naturalistic evidence about:

```text
mobility
communication patterns
app use
activity timing
media consumption
interaction frequency
```

Stachl et al. showed that smartphone behavioral logs could predict questionnaire-assessed Big Five dimensions above chance in cross-validation.

But the inference chain is:

```text
DigitalBehaviorTrace
→ model prediction
→ target score/label
```

not:

```text
DigitalTrace
→ direct observation of personality essence
```

Required guards:

```text
PredictionOfQuestionnaireScore != IndependentConstructValidation
DigitalTrace != ContextFreePersonProperty
PlatformBehavior != WholeBehavior
HighPrediction != Mechanism
```

And digital trace collection itself raises privacy/selection effects.

---

# 22. Physiological evidence ceiling

Physiological measures can index mechanisms or state constraints at another explanatory scale:

```text
heart rate / HRV
endocrine signal
immune/metabolic marker
autonomic response
sleep/circadian measure
```

But HD9 already established:

```text
Biomarker != Mechanism
PopulationReference != IndividualBaseline
```

HD10-B adds:

```text
PhysiologicalCorrelateOfTraitScore
!= TraitImplementationByDefinition
```

A physiological measure needs its own:

```text
reliability
state sensitivity
protocol dependence
sampling window
causal interpretation
```

before being used as individual-difference evidence.

---

# 23. Neural evidence ceiling

Neural data are not privileged over behavioral/self-report measurement merely because they are biological.

Task-fMRI evidence is a strong warning: common tasks can show robust average activation while person-level activation reliability remains low.

Thus:

```text
RobustGroupBrainActivation
!= ReliableIndividualBrainMarker
```

and:

```text
ReliableNeuralMarker
!= PsychologicalConstructIdentity
```

Resting/connectivity or multivariate measures may have better reliability in some designs, but every neural metric requires its own person-level measurement audit.

---

# 24. Prediction is not explanation

A model can predict:

```text
trait score
future task performance
job outcome
clinical risk
```

without identifying:

```text
causal mechanism
intervention target
ontological primitive
```

Therefore:

```text
PredictiveValidity
!= CausalValidity
!= MechanismProof
!= NormativeAuthority
```

This preserves HD7's broader:

```text
Prediction != Mechanism != Authority
```

---

# 25. Construct validity is a network of evidence, not one coefficient

HD10-B uses `ConstructValidityEvidence` as a profile including where relevant:

```text
content/task coverage
response-process evidence
internal structure
reliability/precision
convergent evidence
discriminant evidence
cross-rater/method evidence
criterion/predictive evidence
known-groups/perturbation evidence
longitudinal stability/change sensitivity
cross-context transport
cross-cultural/group comparability
consequences/use validity concerns
```

No item is universally mandatory in the same way for every construct.

But:

```text
OneCorrelation != ConstructValidityClosure
```

---

# 26. Measurement invariance — what it can establish

Under a declared latent measurement model, invariance testing can ask whether aspects of the measurement relation are sufficiently similar across:

```text
groups
languages
cultures
raters
time/occasions
```

Depending on model/constraints, this may support comparison of factor relations, variances or means.

Therefore measurement invariance is important evidence for transport/comparability.

---

# 27. Measurement invariance — what it cannot establish

Even strict invariance does not prove:

```text
construct is a natural kind
construct has one mechanism
within-person dynamics match factor structure
same causes operate in all groups
model is uniquely correct
all cultures/populations are covered
```

Thus:

```text
MeasurementInvariance
!= OntologicalUniversality
```

Conversely:

```text
NonInvariance
!= ConstructUnreality
```

because non-invariance may reveal translation differences, reference frames, response styles, different item relevance, real structural differences or model misspecification.

---

# 28. Cross-cultural transport requires scoped claims

The evidence is deliberately mixed.

Examples:

```text
Big Five inventory structure can fail expected recovery in one socioecological population;

some WISC-V/CHC-aligned factor structures can show strong invariance across several national standardization samples.
```

Therefore the correct inference is conditional:

```text
TransportEvidence(Model, Instrument, PopulationA, PopulationB)
```

not:

```text
Universal
```

or:

```text
CultureSpecificByDefinition
```

---

# 29. Change sensitivity and stability can conflict

A measure optimized to produce stable rank ordering may be insensitive to meaningful within-person change.

A state measure optimized for change sensitivity may have low long-interval test–retest correlation for valid reasons.

Thus:

```text
LowTemporalStability
!= PoorMeasureByDefinition
```

if the target is genuinely dynamic.

Before judging reliability, declare:

```text
TargetExpectedPersistence
```

---

# 30. Trait/state decomposition is model-dependent evidence, not observed fact

Repeated measurement can support decomposition into:

```text
stable person component
occasion/state component
task-specific component
error
```

but the exact decomposition depends on:

```text
model
sampling interval
context distribution
number of occasions
task battery
measurement invariance
```

Therefore:

```text
EstimatedTraitVariance
!= MetaphysicalTraitAmount
```

---

# 31. Same observed reliability can hide different realities

Two tests can both have `r=.8` test–retest reliability while differing in:

```text
absolute measurement error
score variance
practice shift
ceiling/floor effects
population heterogeneity
context restriction
item sampling
```

Therefore:

```text
SameReliabilityCoefficient
!= SameMeasurementQualityProfile
```

---

# 32. Restricted range and context selection matter

Individual-difference reliability/prediction can change across populations because the amount of between-person variance changes.

Examples:

```text
elite samples
clinical samples
age-restricted cohorts
screened job applicants
university convenience samples
```

Thus:

```text
Reliability_D,PopulationA
!= Reliability_D,PopulationB by definition
```

No instrument receives context-free reliability metadata.

---

# 33. Person-specific evidence needs context coverage

Repeated measures of one person across only one narrow recurring situation do not establish broad response tendencies.

Required distinction:

```text
TemporalSamplingBreadth
ContextSamplingBreadth
TaskSamplingBreadth
```

A dense but narrow trace can estimate one local dynamic extremely well while supporting little generalization.

---

# 34. Multi-method disagreement is a research object

When:

```text
SelfReport != InformantReport != TaskPerformance != DigitalTrace
```

HD10-B rejects immediately averaging them into one latent score.

First ask whether disagreement maps onto:

```text
private versus public states
home versus work context
maximum versus typical performance
short versus long timescale
observer access
support differences
social desirability
measurement error
```

Discordance can itself falsify a unitary construct model.

---

# 35. Human×Agent measurement requires explicit support boundaries

Agent-era traces separate variables historically bundled in traditional assessment:

```text
problem identification
option generation
retrieval
memory
reasoning
verification
execution
persistence
coordination
```

A supported task score must record:

```text
model/agent identity
available tools
memory access
prompt/instruction boundary
autonomy/delegation level
Human contribution
agent contribution
verification burden
independent follow-up performance
```

Therefore:

```text
HumanAgentOutcome
!= HumanAbilityScore
```

without an attribution model.

---

# 36. AI-assisted gain needs transfer/removal tests

Wu et al. (2025) found immediate GenAI collaboration gains in several tasks but little consistent spillover to subsequent solo performance.

This provides the measurement principle:

```text
AssistanceEffect
= SupportedPerformance_withAI - SupportedPerformance_withoutAI
```

is not equivalent to:

```text
HumanLearningEffect
```

To infer internal capability change, measure:

```text
later solo performance
retention
novel transfer
tool removal
strategy knowledge
verification ability
```

---

# 37. Measurement can alter the person

HF0's reflexivity rule applies strongly to individual differences.

Labels such as:

```text
high IQ
low ability
introvert
ADHD
high potential
low performer
```

can alter:

```text
self-model
opportunity
teacher/employer expectations
practice allocation
motivation
social treatment
```

Therefore:

```text
AssessmentResult
can become FutureContext
```

and measurement is not always causally inert.

---

# 38. Measurement consequences are separate from validity evidence

A score may be statistically informative while its use is unfair, harmful or outside its validated scope.

Keep separate:

```text
MeasurementAccuracy
PredictiveUtility
DecisionRule
InstitutionalUse
NormativeLegitimacy
```

HF14–HF18 retain the normative/institutional ownership.

---

# 39. Minimum evidence profile for a stable individual-difference claim

For a claim such as:

```text
H differs relatively persistently from relevant others in D
```

record at minimum:

```text
Target construct/domain D
Instrument/task/rater
Score definition
Reference population / comparison set
Timescale
Context/task/support boundary
Reliability target + estimate/uncertainty
Repeat occasions or stability evidence
State/practice controls
Cross-method evidence if relevant
Generalization/transport limits
Predictive or criterion evidence if claimed
Causal status: descriptive / predictive / causal unknown
```

---

# 40. Stronger profile for person-specific dynamics

For:

```text
PersonState_{t+1} = F(PersonState_t, Situation_t, ...)
```

require:

```text
many observations per person
sufficient temporal resolution
context variation
measurement model stable enough for repeated use
lag/ordering logic
missingness/compliance audit
reactivity audit
uncertainty on person-specific parameters
out-of-sample or held-out prediction where feasible
```

A cross-sectional questionnaire does not satisfy this by itself.

---

# 41. Stronger profile for ability/capacity claims

Require where relevant:

```text
multiple tasks / task sampling
reliability of task and latent estimate
difficulty coverage
speed/accuracy decomposition
practice effects
state sensitivity
support boundary
retention/transfer
external criterion
```

And preserve:

```text
TestScore != Ability
Ability != CapacityByDefinition
Capacity != TypicalPerformance
```

---

# 42. Stronger profile for personality/temperament claims

Require where relevant:

```text
self-report
informant report
repeated state sampling
context exposure
longitudinal stability/change
cross-cultural measurement comparability
behavior/outcome relation
method variance
```

No one channel is universal gold standard.

---

# 43. Evidence ladder — without treating it as a linear proof hierarchy

A useful audit sequence is:

```text
Observation quality
→ score reproducibility/precision
→ internal structure
→ cross-method convergence/discrimination
→ temporal/context transport
→ criterion/prediction
→ perturbation/intervention
→ mechanism discrimination
```

But this is not a strict ladder because different constructs expose different evidence surfaces.

The durable rule is:

```text
EvidenceForClaim_X
must match Claim_X.
```

---

# 44. Minimal counterexample matrix

| Case | Bad inference | Surviving distinction |
|---|---|---|
| robust Stroop mean effect, poor retest ranking | robust effect = good individual-difference test | group robustness != rank reliability |
| high alpha, changing ranks over months | internal consistency = temporal stability | consistency != stability |
| stable ranks + everyone improves | retest reliability = no change | rank stability != mean stability |
| same test score, different task/process profiles | score = mechanism | equifinal score paths |
| self/informant disagreement by context | one rater must be invalid | perspective/context can differ |
| dense ESM in one narrow setting | many observations = general trait | density != context breadth |
| factor invariant across countries | invariant = universal causal kind | comparability != ontology |
| factor non-invariant after translation | construct unreal | instrument/translation/context may differ |
| smartphone logs predict Big Five questionnaire | logs reveal essence | prediction target remains questionnaire construct |
| task-fMRI robust activation, poor ICC | neural signal = person biomarker | group neural effect != individual reliability |
| high reliability biomarker with weak behavior relation | reliability = validity | reliable measure may miss target construct |
| AI raises task output, solo performance unchanged | assisted output = human ability | situated/joint != independent capability |
| repeat test raises score | score gain = trait growth | practice effect != trait change |
| high job performance in rich support | performance = internal ability | context/support contribute |
| trait score predicts outcome | prediction = causal mechanism | predictive != causal validity |

---

# 45. HD10-B canonical measurement grammar

```text
TargetClaim
  ↓
EvidenceTarget
  ↓
Instrument / Task / Rater / Trace
  ↓
Observation
  ↓
Scoring / Estimation Model
  ↓
Score / Parameter Estimate
  ↓
Reliability / Precision profile
  ↓
ValidityEvidence profile
  ├─ internal structure
  ├─ convergent/discriminant
  ├─ temporal stability/change sensitivity
  ├─ cross-method/rater
  ├─ context/task transport
  ├─ cross-group invariance
  ├─ criterion/prediction
  └─ perturbation/intervention
  ↓
Scoped Interpretation
  ↓
PersonDifferenceProfile / StateDistribution /
ResponseTendency / Ability / Capability claim
```

No arrow is an identity arrow.

---

# 46. What B now permits HD10-C to do

Before B, rival model comparison could accidentally reward a model merely because it owns a popular test battery.

After B, every model must declare:

```text
what observations it treats as evidence;
which variance it explains;
what reliability target it requires;
what cross-method disagreements it predicts;
whether it claims between-person or within-person structure;
what transport it expects;
what would falsify the measurement model versus the substantive model.
```

This makes genuine model comparison possible.

---

# 47. Foundation audit

HD10-B discovers a major **method/evidence layer**, not a new peer Human subsystem.

Psychometrics/measurement remains cross-cutting:

```text
it applies to every HF,
but does not become HF24 merely because it is foundational to inference.
```

`PersonDifferenceProfile` remains a cross-foundation projection candidate.

No current contradiction requires reopening HF0–HF23.

Therefore:

```text
NextFoundationAdmissionCondition(HF24) = false
FoundationReopenCondition(HF0–HF23) = false
HF24 = UNKNOWN / not admitted
```

---

# 48. Next frontier

HD10-B is complete.

Next:

```text
HD10-C — Rival Model Families I:
Personality / Temperament / Trait–State / Person×Situation Architecture
```

C should now compare at minimum:

```text
lexical trait-descriptive models
Five-Factor / Big Five families
HEXACO/alternative broad-trait families
temperament traditions
social-cognitive / CAPS-like models
Whole Trait / density-distribution models
latent state-trait models
dynamic / idiographic models
```

while **deferring the cognitive-ability/intelligence model family** to a separate later round if needed, so personality and intelligence are not forced into one theory prematurely.

C must use the B evidence firewall and must not infer ontology from psychometric popularity.

---

# 49. Stop rule

HD10-B is complete because it has:

```text
separated reliability targets;
separated reliability from validity;
separated score interpretation from instrument;
mapped evidence ceilings for self-report, informant, task, ESM, longitudinal,
physiology, neural data, real-world outcomes, digital traces and Human×Agent traces;
separated prediction from mechanism;
separated invariance from ontology;
made within-person claims require within-person evidence;
made support boundaries explicit for capability measurement;
built falsifiers for common measurement category errors;
kept model adjudication deferred;
kept HF24 UNKNOWN;
and triggered no FoundationReopenCondition.
```

All conditions are met.
