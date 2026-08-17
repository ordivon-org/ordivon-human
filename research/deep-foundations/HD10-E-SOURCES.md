---
schema_version: 1
id: human.deep-foundations.hd10e.sources
title: HD10-E — Cross-Domain Person-Difference Evidence Ledger
type: evidence-ledger
profile: research
lifecycle: completed
source_role: evidence
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
updated: 2026-08-18
summary: Evidence ledger for HD10-E. Sources pressure cross-domain person representation using nonergodicity/person-specific theory, repeated cognitive structure, personality-health longitudinal reciprocity, person-specific daily personality-health networks, person-environment transactions, personality-social relationship process designs, idiographic measurement-model heterogeneity, developmental differences between cognition and personality, and prior HD10/HD9/HF evidence. The ledger supports a typed projection architecture rather than one fixed Person vector; it does not establish one universal dynamic-network ontology.
evidence_status: verified
readiness: READY
related:
  - human.deep-foundations.hd10e
  - human.deep-foundations.hd10.closeout
---
# HD10-E — Evidence Ledger

## Evidence rule

```text
Person != ProfileVector
BetweenPerson != WithinPerson
SharedCoordinate != PersonMechanism
Stable != Intrinsic
Trajectory != Essence
DynamicNetwork != CausalTruthByDefinition
RelationshipEffect != ActorTrait
SupportedCapability != IndependentCapability
```

---

# S01 — Molenaar: idiographic / nonergodic warning

Peter C. M. Molenaar. “A Manifesto on Psychology as Idiographic Science: Bringing the Person Back Into Scientific Psychology, This Time Forever.” *Measurement: Interdisciplinary Research and Perspectives* 2(4):201–218 (2004). DOI: `10.1207/S15366359MEA0204_1`.

Theoretical result:

Interindividual structures can be generalized to intraindividual structures only under stringent ergodic conditions.

HD10-E use:

```text
BetweenPersonStructure -> PersonProcess
requires bridge evidence.
```

This is a methodological/theoretical constraint, not an empirical claim that every psychological variable is maximally unique.

---

# S02 — Molenaar & Campbell: person-specific paradigm

Peter C. M. Molenaar & Cynthia G. Campbell. “The New Person-Specific Paradigm in Psychology.” *Current Directions in Psychological Science* 18(2):112–117 (2009). DOI: `10.1111/j.1467-8721.2009.01619.x`.

Use:

Clarifies the population-versus-individual inference distinction and motivates repeated within-person analysis when ergodicity is unsupported.

---

# S03 — repeated cognitive evidence

Florian Schmiedek, Martin Lövdén, Timo von Oertzen & Ulman Lindenberger. “Within-person structures of daily cognitive performance differ from between-person structures of cognitive abilities.” *PeerJ* 8:e9290 (2020). DOI: `10.7717/peerj.9290`. PMID: `32551201`. PMCID: `PMC7292017`.

Design:

```text
101 adults
9 cognitive tasks
~100 occasions over ~6 months
```

Result relevant to E:

Person-specific within-person structures differed from each other and from the modal between-person cognitive structure; g was less prominent within persons.

```text
PopulationAbilityStructure != PersonCognitiveDynamics
```

---

# S04 — personality and health, three longitudinal studies

Jing Luo, Bo Zhang, Ryne Estabrook et al. “Personality and health: Disentangling their between-person and within-person relationship in three longitudinal studies.” *Journal of Personality and Social Psychology* 122(3):493–522 (2022). DOI: `10.1037/pspp0000399`. PMCID: `PMC8867777`.

Samples:

```text
NAS   N=1,734
LISS  N=13,559
SATSA N=2,209
```

The analyses separated relatively stable between-person variation from within-person longitudinal deviations. Depending on trait/health outcome/model, changes in personality and health showed unidirectional or bidirectional relations; within-person effects were generally smaller than between-person associations.

HD10-E use:

```text
BetweenPersonPersonalityHealthAssociation
!= WithinPersonDynamicRelation
```

and cross-domain person states can co-develop.

---

# S05 — person-specific daily neuroticism–health networks

Dominic P. Kelly, Alexander Weigard & Adriene M. Beltz. “How are you doing? The person-specificity of daily links between neuroticism and physical health.” *Journal of Psychosomatic Research* 137:110194 (2020). DOI: `10.1016/j.jpsychores.2020.110194`. PMID: `32736131`. PMCID: `PMC7854827`.

Design:

```text
119 adults
75 occasions
12 daily neuroticism indicators
3 physical-health symptom indicators
person-specific GIMME-MS networks
```

Networks were heterogeneous. Health→neuroticism links were more frequent than reverse links in the sample, but the study did not recover one uniform group relation that characterized every individual.

Use:

```text
CrossDomainDynamics can be person-specific.
```

---

# S06 — 2026 person–environment transaction and personality continuity

Christopher R. Beam & Emily Schoenhofen Sharp. “Person-Environment Transaction Underlying Personality Development in Middle and Late Adulthood.” *Developmental Psychology* (2026). DOI: `10.1037/dev0002126`. PMID: `41609656`. PMCID: `PMC12857755`.

Using longitudinal Swedish Adoption/Twin Study of Aging data, reciprocal-effects models provided partial support for niche-picking/person→environment transaction contributions to continuity of neuroticism/openness/extraversion at different adult stages, alongside stable genetic and environmental variance.

HD10-E use:

```text
ObservedTraitContinuity
can be partly transactionally sustained.
```

Therefore stable expression is not automatically a purely internal constant.

---

# S07 — personality/social-relationship process separation

Katharina Geukes, Simon M. Breil, Roos Hutteman, Steffen Nestler, Albrecht C. P. Küfner & Mitja D. Back. “Explaining the longitudinal interplay of personality and social relationships in the laboratory and in the field: The PILS and the CONNECT study.” *PLOS ONE* 14(1):e0210424 (2019). DOI: `10.1371/journal.pone.0210424`.

The PERSOC-oriented designs separate actor, partner and relationship-level behavior/perception processes and study reciprocal personality–relationship development.

HD10-E use:

```text
RelationshipSpecificEffect != ActorTrait
```

and social individual differences can reside at dyadic rather than person-only level.

---

# S08 — idiographic measurement structures can differ across persons

Cara J. Arizmendi & Kathleen M. Gates. “Clustering Individuals Based on Similarity in Idiographic Factor Loading Patterns.” *Multivariate Behavioral Research* 60(1):90–114 (2025 issue; online 2024). DOI: `10.1080/00273171.2024.2374826`. PMID: `39044482`. PMCID: `PMC11754526`.

Idiographic factor models estimate individual-level measurement structures; the paper develops clustering of persons by similarity in person-specific loading patterns and demonstrates recovery in simulation plus empirical illustration.

HD10-E use:

```text
OneGlobalMeasurementStructure
and
EveryPersonCompletelyUnique
```

are both unnecessarily strong extremes.

The architecture can support shared, subgroup and person-specific structures.

---

# S09 — cognition/personality developmental comparison

Daniel A. Briley & Elliot M. Tucker-Drob. “Comparing the Developmental Genetics of Cognition and Personality over the Life Span.” *Journal of Personality* 85(1):51–64 (2017; online 2015). DOI: `10.1111/jopy.12186`. PMID: `26045299`. PMCID: `PMC4670606`.

The synthesis shows cognition and personality both become more rank-order stable with age but display different developmental patterns in genetic/environmental contributions and timing.

HD10-E use:

```text
SimilarDifferentialStability
!= SameDevelopmentalArchitecture
```

No genetic estimate is treated as person essence.

---

# S10 — person-specific versus shared structures are not binary

Cara J. Arizmendi & Kathleen M. Gates (S08), plus person-specific modeling traditions, support multi-level structure:

```text
population-shared
subgroup-shared
person-specific
```

rather than assuming either complete homogeneity or complete uniqueness.

---

# S11 — HD10-C internal evidence

Canonical:

```text
HD10-C-PERSONALITY-TEMPERAMENT-TRAIT-STATE-PERSON-SITUATION-RIVAL-MODELS.md
```

Retained:

```text
PersonalityDescription
!= StateDistribution
!= SituationExposureDistribution
!= ConditionalResponseStructure
!= PersonalityMechanismConfiguration
!= DevelopmentalTrajectory
```

and:

```text
Trait-D != Trait-R != Trait-M
```

---

# S12 — HD10-D internal evidence

Canonical:

```text
HD10-D-COGNITIVE-ABILITY-INTELLIGENCE-RIVAL-MODELS.md
```

Retained:

```text
PositiveManifold
!= GeneralFactorEstimate
!= CognitiveProcessProfile
!= ModifiabilityProfile
!= CognitiveCapabilitySurface
```

and:

```text
TaskDemandSamplingDistribution_B
```

as the cognitive counterpart to situation-exposure sampling.

---

# S13 — HF4 motivation/preferences

Canonical HF4 establishes:

```text
MotivationProfile(H,G,t,context)
Preference_D,t,C
ObservedChoice != StablePreferenceReadout
```

This directly falsifies a timeless universal motivation/person-preference vector.

---

# S14 — HF6 change/trajectory

Canonical HF6 establishes:

```text
ChangeProfile_D(H, intervention/history)
ResilienceProfile(H, Exposure, Outcome, interval)
Reserve_D(H, burden, context)
```

and:

```text
PracticePerformance != RetainedLearning
Retention != Transfer
TrainingGain != BroadCapability
Persistent != Permanent
```

This provides the change/trajectory projection class.

---

# S15 — HF22 dyadic state

Canonical HF22 establishes:

```text
RelationState_D(A,B,t)
RelationState_D(A→B) != RelationState_D(B→A)
AttachmentSecurity != PersonTraitByDefinition
```

This is the decisive relation-specific falsifier against person-only profile ownership.

---

# S16 — HD9 organismic baseline/trajectory

Canonical HD9 establishes:

```text
PopulationReference != IndividualBaseline
IndividualBaseline != ImmutableSetpoint
Health != one scalar
Disease/Health require trajectories/history
```

and supports long-lived personal biological baselines that remain shiftable through development, training, medication, disease and aging.

---

# S17 — H0/HF capability support boundaries

Canonical capability research establishes:

```text
IndependentCapability
!= SituatedCapability
!= JointCapability
!= ObservedPerformance
```

which is essential for Agent-era person representation.

---

# Evidence synthesis

The cross-domain evidence does **not** support one universal fixed Person vector.

It supports:

```text
shared population coordinates
+ typed person-specific baselines/distributions
+ conditional response functions
+ trajectories/modifiability
+ relation-specific states
+ support-relative capability
+ external exposure links
+ cross-domain coupling models
```

with level, scope and evidence made explicit.

The key conclusion is architectural rather than psychometric:

```text
PersonDifferenceArchitecture
= query/projection family over underlying Human reality
```

not another latent super-trait.
