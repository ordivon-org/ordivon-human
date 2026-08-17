---
schema_version: 1
id: human.deep-foundations.hd10a
title: HD10-A — Current-Use, Term Separation and Hidden-Assumption Inventory
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
summary: First deep round of HD10 Individual-Difference Architecture. HD10-A audits current Human repo usage before choosing any personality, temperament, psychometric or intelligence model. It finds a strong existing negative grammar—state != trait, capacity != observed performance, independent skill != situated capability != joint capability, measurement != construct—but no positive reusable grammar connecting person-specific distributions, response functions, trait descriptors, cognitive ability and within-person dynamics. Personality, temperament and intelligence are sparsely owned; capability/skill/performance are much more developed. HD10-A therefore separates measurement instrument, score/estimate, population covariance structure, person difference profile, within-person state dynamics, trait descriptor, disposition/response function, capacity, skill, competence, expertise, situated capability, joint capability and observed performance. No HF24 is admitted and no HF0–HF23 foundation is reopened.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.deep-foundations.hd10.continuation
  - human.deep-foundations.hd10a.sources
  - human.deep-foundations.post-hd9.direction-search
  - human.foundations.hf0
  - human.deep-foundations.hd7
---
# HD10-A — Current-Use, Term Separation and Hidden-Assumption Inventory

## 0. Decision

HD10-A does **not** select Big Five, HEXACO, CHC, `g`, temperament theory, latent-state-trait theory, CAPS, Whole Trait Theory or any other model family as ontology.

Its first result is narrower and more important:

```text
CurrentHuman
has strong anti-collapse rules for individual variation
but lacks one positive reusable PersonDifference grammar.
```

The current repo already knows many things that must **not** be collapsed:

```text
state != trait
capacity != observed performance
independent skill != situated capability != joint-system capability
measurement != construct
population average != individual state/effect
expertise != general intelligence
credential != competence
status != competence
productivity != worker trait
preference != timeless stable trait
resilience != one fixed trait
attachment security != person trait by definition
```

But it does not yet answer, in a model-independent way:

```text
What is a stable person difference?
What is stable when momentary behavior varies strongly?
What is the relation among a trait descriptor, a state distribution and a mechanism?
What does cognitive ability denote independently of a test score?
When is a repeated behavior a person property versus repeated context?
How should solo, supported and joint performance alter attribution of capability?
```

Therefore:

```text
HD10-A = term/assumption closure
HF24 = UNKNOWN / not admitted
FoundationReopenCondition(HF0–HF23) = false
```

---

# 1. Repo-current-use audit

The audit scanned the current Human foundation/deep-foundation/H0 markdown surface with exact-word matching where possible. Counts are navigation diagnostics, **not semantic coverage scores**.

Representative current counts:

```text
state                  910
capability             485
performance            318
skill                  271
preference             303
capacity               198
expertise              147
trait                   139
competence               87
habit                    72
ability                  60
intelligence             34
individual differences   30
personality               16
temperament                7
person-specific             7
aptitude                   0
talent                     0
```

Important qualification:

```text
Frequency != Ownership
Mention != Model
Negation != PositiveOntology
```

The distribution is nevertheless informative: the repo is rich in **state, performance, skill and capability grammar**, while the classic individual-difference vocabulary `personality`, `temperament`, `intelligence` and `person-specific` remains thin.

---

# 2. Current ownership map

## 2.1 HF0 already contains the negative skeleton

HF0 distinguishes statement roles including:

```text
state
process
disposition / trait
capacity
situated capability
experience
action
relation
context
outcome
observation / evidence
```

and already preserves:

```text
state != trait
capacity = maximum/latent ability only under declared conditions
capacity != typical performance
situated capability != internal skill
measurement != construct
```

Its cross-context falsifiers already include:

```text
fatigue/illness changes performance without proving trait/capacity change
expert denied access retains internal skill but loses situated feasibility
tool/AI support changes situated capability without becoming unaided skill
team result can exceed every member's independent capability
institution change can alter outcome without person-trait change
```

HD10 therefore must **consume HF0**, not rediscover it.

---

## 2.2 H0 Capability contains a mature applied decomposition

The legacy H0 Capability surface already distinguishes:

```text
underlying capacity
available capacity in current state
independent skill without external assistance
situated capability with ordinary tools/resources
joint-system capability with people/organizations/AI
observed performance
long-term transfer/recovery capability
```

This is one of the strongest existing positive structures relevant to HD10.

HD10 must not replace it with:

```text
one IQ score
one personality vector
one latent general ability
one assisted-output score
```

---

## 2.3 HF4 already rejects preference-as-trait

HF4 uses preference as a context-indexed comparative relation and explicitly rejects:

```text
ObservedChoice = StablePreferenceReadout
RiskPreference = one global risk trait
Motivation = stable personality property
```

Thus:

```text
StablePreference
```

cannot be silently reused as a generic `PersonTrait` definition.

---

## 2.4 HF6 already separates performance, learning, reserve and resilience

HF6 preserves:

```text
PracticePerformance != Learning
CurrentPerformance != Stored/PersistentCapability
Reserve_D != BaselinePerformance
Resilience_D != Resilience_E
Resilience != one fixed trait
```

Therefore stable individual differences in learning rate, reserve or resilience require their own domain/time/context typing rather than inheritance from a personality label.

---

## 2.5 HF9 already separates task competence, expertise and general reasoning

HF9 has strong local firewalls:

```text
DeductiveTaskPerformance != PureDeductiveCapacityReadout
Reasoning != WorkingMemoryCapacity
ProbabilityError != NoBayesianReasoningCapacity
Expertise_D != GeneralReasoningTrait
JointReasoningCapability != HumanIndependentReasoningCapability
```

This means HD10 cannot define intelligence by silently aggregating HF9 task performance.

---

## 2.6 HF11 already separates skill, intrinsic capacity and situated action capability

HF11 preserves:

```text
Strength != PraxisCapability
CurrentPerformance != Skill
Practice != AutomaticityGuarantee
BareHumanCapability_D != HumanToolSystemCapability_D
IntrinsicCapacity != SituatedActionCapability
```

Its working skill object is learned, domain-qualified and reliability/robustness-sensitive.

That makes:

```text
Skill != AbilityByDefinition
Skill != Trait
```

an HD10 requirement.

---

## 2.7 HF12/HF13/HF17 already type social and epistemic competence

Existing separations include:

```text
RoleAssignment != RoleCompetence
Credential != CurrentCompetence
Status != TaskCompetence
Expertise_D != Expertise_E
Expertise != Authority
Expertise != GeneralIntelligence
JointCapability != SumIndividualCapability
```

Therefore `competence` and `expertise` are already explicitly **domain-scoped** in several current foundations.

---

## 2.8 HF19 already falsifies worker-trait productivity

HF19 states that labor productivity depends on:

```text
worker
× task
× technology
× capital
× organization
× demand/measurement
```

and preserves:

```text
LaborProductivity != WorkerTrait
TechnologyAvailable != EffectiveCapability
```

This is a strong economic falsifier against decontextualized ability attribution.

---

## 2.9 HD7 already rejected `Individual Differences HF24`

HD7 defined the minimum relation:

```text
Difference_D(PersonA, PersonB, time, context, measure)
```

and rejected:

```text
IndividualDifference = PersonEssence
GeneticVarianceContribution = ImmutableRankOrder
GroupMeanAssociation = IndividualOutcome
```

It also rejected `Individual Differences` as HF24 because an individual difference is a relation under declared coordinates, not a subsystem.

HD10 therefore does **not** reopen that decision merely because the domain is now being studied more deeply.

---

# 3. The major current-use asymmetry

The current Human model is much better at saying:

```text
what changes now
what was observed
what task was performed
what support was available
what skill was learned
```

than at saying:

```text
what relatively persistent person-specific structure should be inferred
from many observations across changing contexts and time.
```

This creates the central HD10-A gap:

```text
Observation grammar       = strong
State grammar             = strong
Capability grammar        = strong
Learning/history grammar  = strong
Person-difference grammar = weak
```

---

# 4. Hidden assumption inventory

## H1 — `Trait` is mostly used negatively, not positively

The repo frequently rejects bad trait reductions:

```text
risk preference != global trait
resilience != one trait
reputation != verified trait
productivity != worker trait
attachment security != person trait
expertise != general reasoning trait
```

But this leaves a hole:

```text
If Trait is not those things, what is Trait?
```

Current truth:

```text
AntiTraitReduction != PositiveTraitOntology
```

---

## H2 — `Personality` has almost no owner

Outside HD10/direction-search material, `personality` mostly appears as:

```text
not a personality inventory
not a motivational personality test
personality may contribute to identity/self-representation
resilience is not one stable personality trait
```

There is no canonical Human answer to:

```text
Personality = ?
```

This absence is real.

---

## H3 — `Temperament` is currently only a modifier

Temperament appears mostly as a developmental/contextual modifier in H0/HD3 and in the new direction-search evidence.

There is no current separation of:

```text
Temperament
Personality
Affectivity
Reactivity
SelfRegulation
EarlyEmergingDifference
DevelopmentalContinuity
```

The distinction remains unresolved.

---

## H4 — `Intelligence` is mostly an anti-equivalence label

Current usages are dominated by:

```text
Intelligence != Sentience
Intelligence != MoralAgency
Expertise != GeneralIntelligence
CollectiveIntelligence != one ontology
Cognition != Intelligence
```

The repo deliberately did not define the positive referent.

Thus:

```text
Intelligence != one currently owned Human primitive
```

and no future round may infer that `g`, CHC, reasoning, working memory or test score owns the word by default.

---

## H5 — `Ability` is semantically loose

Current `ability` usages include:

```text
ability to report
ability to change
memory ability
reasoning ability
language ability
verification ability
practical ability
independent ability
```

Many are ordinary-language capability expressions, not a single construct.

Therefore:

```text
Ability_D
```

must always declare `D`, task family, conditions and evidence surface until HD10-B determines whether any more specific common structure is justified.

---

## H6 — `Capacity` is overloaded across incompatible roles

The repo uses `capacity` for at least:

```text
maximum/latent task ability
current available capacity
physiological reserve/capacity
report capacity
learning/plasticity capacity
moral responsibility capacity
rights-holding capacity
welfare/pain/experience capacity
```

These are not one scalar object.

Required separation:

```text
TaskCapacity
PhysiologicalCapacity
LearningCapacity
ReportCapacity
Agency/ResponsibilityCapacity
Experience/WelfareCapacity
Legal/InstitutionalCapacity
```

Do not build `GeneralCapacity` by vocabulary alone.

---

## H7 — `Capability` is already relational and support-sensitive

Capability is one of the strongest existing structures and must remain:

```text
Capability_D(H, State, Task, Support, Context, interval)
```

rather than becoming an internal latent trait.

A capability can change because of:

```text
body state
tool availability
permission
social support
AI assistance
organization
task specification
```

without any matching change in an internal person trait.

---

## H8 — `Competence` has multiple homonyms

Current Human uses include:

```text
DecisionCompetence
ExecutionCompetence
TaskCompetence
EpistemicCompetence
RoleCompetence
LinguisticCompetence
```

while Self-Determination Theory uses `competence` in a psychological-need/satisfaction sense.

Therefore:

```text
TaskCompetence != FeltCompetence != CompetenceNeedSatisfaction
```

and `Competence` must remain qualified.

---

## H9 — `Expertise` is comparatively well typed

Current Human already treats expertise as:

```text
Expertise_D
= learned/history-dependent domain-specific organization and reliable epistemic/action advantage
```

with:

```text
Expertise_D != Expertise_E
Expertise != Authority
Expertise != GeneralIntelligence
Expertise != UniversalFlexibility
```

HD10 should preserve this as a successful anti-generalization pattern.

---

## H10 — `Individual difference` is a relation, but a person profile is missing

HD7's relation is strong:

```text
Difference_D(A,B,t,context,measure)
```

but pairwise difference alone does not give a reusable representation of one Human across repeated contexts.

Missing candidate:

```text
PersonDifferenceProfile
```

This is **not yet a foundation object**. It is a research placeholder for a typed bundle of relatively persistent distribution/response parameters.

---

## H11 — `Baseline` is strong in physiology, weak as a general Human concept

HD9 correctly separates:

```text
PopulationReferenceRange != IndividualBaseline
IndividualBaseline_t != ImmutableBiologicalSetpoint
```

HD10 must generalize the same caution:

```text
PersonBaseline_D
!= PopulationMean_D
!= Trait_D
!= Optimal_D
!= MaximumCapacity_D
```

A baseline is protocol/time-window/context dependent.

---

## H12 — `Potential` is under-specified

Current H0 uses `potential` cautiously, but the term remains dangerous.

A statement such as:

```text
Person P has high potential
```

is incomplete without:

```text
target domain
time horizon
training/intervention class
resources/support
opportunity
state constraints
criterion
uncertainty
```

Therefore:

```text
Potential != HiddenFixedCapacity
```

and HD10-A does not promote `Potential` to a canonical primitive.

---

## H13 — `Aptitude` and `Talent` are effectively absent

Current canonical research has no meaningful owner for either term.

This is preferable to inventing them prematurely.

```text
AbsentVocabulary != MissingFoundation
```

HD10-B may only introduce them if measurement/evidence comparison requires a distinct object.

---

## H14 — Person-specific modeling is unexpectedly sparse

Despite a large Human library, exact `person-specific` usage remains rare.

The model therefore has a structural asymmetry:

```text
rich GenericHuman grammar
+ weak IndividualHuman parameter grammar
```

This is a genuine HD10 debt.

---

# 5. Required four-layer firewall

HD10-A establishes the most important separation for the whole route:

```text
MeasurementInstrument
!= ObservedResponse/Score
!= PopulationCovarianceStructure
!= PersonDifferenceProfile
!= WithinPersonStateDynamics
!= CausalMechanism
```

Each layer answers a different question.

## 5.1 Measurement instrument

```text
Instrument_I
= task/questionnaire/sensor/rating/protocol used to generate evidence
```

It is not the target construct.

## 5.2 Observed response / score

```text
Observation_O(H,t,I,C)
Score_S = scoring/transformation rule over observations
```

A score is an estimate/evidence product under a procedure.

## 5.3 Population covariance structure

```text
PopulationStructure_P
= statistical relation among measured variables across a declared population/sample
```

Examples include factor/covariance structures.

It is not automatically the architecture inside one person.

## 5.4 Person difference profile

Working placeholder:

```text
PersonDifferenceProfile(H,D,T,Cset)
= relatively persistent parameters/descriptors of H's distributions or response tendencies
  across declared domains, timescales and context families
```

This does not yet specify whether the parameters are causal.

## 5.5 Within-person dynamics

```text
PersonState_{t+1}
= F(PersonState_t,
    Situation_t,
    History_t,
    Goals_t,
    Supports_t,
    Stochasticity_t,
    ...)
```

Within-person transition/dynamic structure need not equal between-person covariance structure.

## 5.6 Mechanism

```text
Mechanism_M
= causal/process account producing or constraining observations, states and distributions
```

A latent factor may summarize covariance without being the mechanism.

---

# 6. Initial term firewall

## 6.1 State

```text
State_D(H,t,C)
```

= time-local condition/profile in domain D under context C.

```text
State != Trait
State != PersonIdentity
State != MeasurementByDefinition
```

---

## 6.2 State distribution

```text
StateDistribution_D(H | ContextDistribution, interval)
```

= distribution of state realizations over a declared observation/context distribution and interval.

Important:

```text
SameMean != SameDistribution
SameDistributionUnderObservedContexts
!= SameCounterfactualResponseFunction
```

---

## 6.3 Trait descriptor

Provisional, model-neutral:

```text
TraitDescriptor_D(H,T,Cset)
= relatively persistent descriptive summary of H's characteristic state/behavior distribution
  under declared domains/context family/timescale
```

It does **not** imply:

```text
essence
immutability
context independence
one causal mechanism
genetic determination
single scalar sufficiency
```

---

## 6.4 Disposition / response tendency

Because `Disposition:` is already used throughout research documents as an editorial verdict label, HD10 should avoid relying on the naked word in automated scans.

Substantive working object:

```text
ResponseTendency_D(H, SituationClass, History, State)
```

= conditional tendency/probability/profile of response under declared conditions.

This is closer to a counterfactual/conditional object than a retrospective trait summary.

```text
TraitDescriptor != ResponseTendency by definition
```

---

## 6.5 Personality

HD10-A does not define one final personality ontology.

Use temporarily as a **research-domain umbrella** for relatively characteristic patterns of thought, affect, motivation and behavior plus candidate mechanisms producing them.

```text
Personality != BigFiveByDefinition
Personality != TraitVectorByDefinition
Personality != Identity
Personality != MoralWorth
```

---

## 6.6 Temperament

Use provisionally for research on early-emerging individual differences in reactivity/regulation patterns across development.

Do not assume:

```text
Temperament = BiologicalOnly
Temperament = ChildhoodPersonalityByDefinition
Temperament != PersonalityByDefinition
```

The boundary is an empirical/developmental question for later HD10 rounds.

---

## 6.7 Ability

Provisional:

```text
Ability_D(H, ConditionSet)
= evidence-supported capability to perform a declared cognitive/action task family
  under specified conditions
```

Until HD10-B:

```text
Ability != TestScore
Ability != OneObservedPerformance
Ability != Knowledge
Ability != SkillByDefinition
Ability != IntelligenceByDefinition
```

---

## 6.8 Capacity

For performance contexts only:

```text
TaskCapacity_D(H, Conditions, SupportBoundary)
= inferred attainable/available performance envelope under a declared condition/support set
```

This remains different from moral/legal/experience capacities.

```text
TaskCapacity != TypicalPerformance
TaskCapacity != CurrentPerformance
TaskCapacity != FixedPotential
```

---

## 6.9 Skill

Retain HF11:

```text
Skill_D
= learned capability for reliably producing high-quality task-relevant effects
  under a class of conditions, with characteristic efficiency, variability,
  robustness and control demands
```

```text
Skill != CurrentPerformance
Skill != GeneralAbility
Skill != ExpertiseByDefinition
```

---

## 6.10 Competence

Use only qualified forms:

```text
TaskCompetence_D
EpistemicCompetence_D
DecisionCompetence_D
ExecutionCompetence_D
RoleCompetence_D
LinguisticCompetence_D
FeltCompetence / CompetenceNeedSatisfaction
```

No unqualified scalar competence.

---

## 6.11 Expertise

Retain current domain-qualified grammar:

```text
Expertise_D
```

as learned/history-dependent domain-specific organization and reliable advantage.

```text
Expertise_D != GeneralIntelligence
Expertise != Authority
```

---

## 6.12 Performance

```text
Performance_D(H, Task, t, State, Support, Context)
= observed task-relevant output/profile under one declared realization
```

```text
Performance != Ability
Performance != Capacity
Performance != Skill
Performance != Trait
Performance != IndependentCapability
```

---

## 6.13 Independent / situated / joint capability

Preserve:

```text
IndependentCapability_D(H, declared baseline support)
SituatedCapability_D(H, Tool/Resource/Institution/Context)
JointCapability_D(H1...Hn, Agents, Organization, Interaction)
```

The support boundary must be explicit.

---

## 6.14 Preference and habit

Preserve existing HF4 grammar:

```text
Preference_D,t,C != TraitByDefinition
HabitLikeControl != PersonalityTraitByDefinition
RepeatedBehavior != StablePreference
```

---

# 7. Minimal counterexamples

HD10-A requires any future model to survive at least these cases.

## F1 — same scalar trait score, different state distributions

Two people can share a questionnaire mean while differing in:

```text
variance
skew
multimodality
context sensitivity
transition dynamics
```

Therefore:

```text
SameTraitScore != SamePersonDifferenceProfile
```

---

## F2 — same average behavior, different situation coupling

Person A behaves similarly across contexts.
Person B behaves very differently but encounters contexts yielding the same average.

```text
SameObservedMean != SameResponseTendency
```

---

## F3 — stable context can imitate stable trait

A person repeatedly encounters the same institution, role or social niche.
Behavior is stable because the context is stable.

```text
StableBehavior != StableInternalDispositionByDefinition
```

---

## F4 — fatigue changes performance without erasing skill

```text
CurrentLowPerformance
!= LowSkill
!= LowTrait
!= LowLongTermCapacity
```

---

## F5 — tool/AI raises performance without internal learning

```text
SupportedPerformanceGain
!= IndependentCapabilityGain
!= RetainedSkillGain
```

---

## F6 — offloading improves immediate performance while impairing later memory

The same support can improve one capability surface while weakening another later state.

```text
HigherTaskPerformance_t
!= HigherInternalCapability_{t+1}
```

---

## F7 — expert denied permission/access

```text
InternalSkill preserved
SituatedCapability reduced
ObservedOutcome absent
```

Therefore:

```text
Capability != InternalTraitOnly
```

---

## F8 — same between-person factor structure, different within-person dynamics

Population covariance can fit a hierarchical ability model while repeated observations of individuals show substantially different covariance/dynamic structures.

```text
PopulationFactorStructure
!= WithinPersonArchitecture
```

---

## F9 — cultural transport can succeed locally and fail elsewhere

A cognitive battery can show strong invariance across some national samples while a personality inventory can fail expected factor recovery in another socioecological population.

Therefore neither:

```text
CrossCulturalUniversality = always true
```

nor:

```text
CrossCulturalTransport = impossible
```

is admissible.

---

## F10 — development preserves rank order while changing levels

```text
RankOrderStability
!= MeanLevelStability
!= IndividualTrajectoryConstancy
!= Immutability
```

Temperament/personality continuity can coexist with developmental transformation.

---

## F11 — same cognitive score, different process organization

```text
SameTestScore
!= SameMechanism
!= SameWithinPersonCovariance
!= SameLearningPotential
```

---

## F12 — credential without competence / competence without credential

```text
Credential != CurrentCompetence
InstitutionalRecognition != PersonCapability
```

---

## F13 — same genome, different phenotype

From HD7:

```text
Same/NearSameInheritedGenome != SamePhenotypeTotality
GeneticVarianceContribution != ImmutableRankOrder
```

Thus genetics cannot close HD10 ontology by itself.

---

# 8. Measurement/ontology traps exposed by A

HD10-B must directly attack these traps.

```text
T1 questionnaire score -> trait essence
T2 factor loading -> causal mechanism
T3 population covariance -> individual architecture
T4 test score -> cognitive ability
T5 maximum observed score -> capacity ceiling
T6 repeated behavior -> stable disposition
T7 rank-order stability -> immutability
T8 predictive validity -> construct identity
T9 measurement invariance -> ontological universality
T10 non-invariance -> construct unreality
T11 supported output -> independent skill
T12 trait label -> explanation
T13 genetic prediction -> fixed person property
T14 low observed variance -> no contextual dependence
T15 broad factor -> one process
```

---

# 9. Initial model-independent architecture

HD10-A retains the following as a **research grammar**, not yet a canonical foundation:

```text
Person H
  |
  +-- PersonState_t,D
  |
  +-- History_t
  |
  +-- PersonBaseline_D,T,C
  |
  +-- StateDistribution_D,T,Cset
  |
  +-- ResponseTendency_D,SituationClass
  |
  +-- TraitDescriptor_D,T,Cset
  |
  +-- Capacity/Skill/Competence/Expertise profiles_D
  |
  +-- IndependentCapability_D
  +-- SituatedCapability_D
  +-- JointCapability_D

Situation_t
Support_t
Task_t
Institution_t
OtherAgents_t
       |
       v
ObservedPerformance_t
       |
       v
Measurement / Score / Estimate
       |
       v
Population statistics / factor structure / prediction
```

Critical arrows are **not identity arrows**.

The explanatory task is to determine which person-side quantities are:

```text
descriptive summaries
conditional response functions
learned structures
biological constraints
social/ecological adaptations
measurement artifacts
or causal mechanisms
```

---

# 10. Foundation audit

HD10-A strengthens the previous no-promotion result.

`IndividualDifference` itself remains:

```text
relation/projection
```

not a subsystem.

`PersonDifferenceProfile` remains only a candidate cross-foundation projection.

No current evidence shows that HF0–HF23 cannot represent the surviving pieces once typed correctly.

Therefore:

```text
NextFoundationAdmissionCondition(HF24) = false
FoundationReopenCondition(HF0–HF23) = false
HF24 = UNKNOWN
```

---

# 11. What HD10-A changes

Before A:

```text
individual differences
≈ psychometrics / personality / intelligence residual
```

After A:

```text
individual-difference architecture
=
measurement layer
+ population structure
+ person-specific descriptive profile
+ within-person state dynamics
+ conditional response tendencies
+ capacity/skill/capability surfaces
+ causal/developmental mechanisms

with strict non-identity among layers.
```

This is the durable result of the round.

---

# 12. Next frontier

HD10-A is complete.

Next:

```text
HD10-B — Measurement, Evidence and Construct-Validity Audit
```

HD10-B must determine what evidence can support claims about:

```text
traits
state distributions
response tendencies
personality/temperament
cognitive ability/intelligence
capacity
within-person dynamics
between-person factors
cross-cultural transport
supported versus independent capability
```

without converting instruments or statistical models into ontology.

HD10-B must still **not** choose a winning personality or intelligence theory.

---

# 13. Stop rule

HD10-A is complete when:

```text
current repo uses are mapped;
existing anti-collapse rules are preserved;
major lexical overloads are identified;
personality/temperament/intelligence ownership gaps are explicit;
measurement/population/person/dynamics/mechanism layers are separated;
capability/skill/expertise structures are protected from trait reduction;
minimal counterexamples are established;
no HF24 is admitted;
no HF0–HF23 reopen condition is created;
and the next round is measurement/evidence rather than model adjudication.
```

All conditions are met.
