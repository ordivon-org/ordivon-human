---
schema_version: 1
id: human.deep-foundations.hd10a.sources
title: HD10-A — Evidence Ledger
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
summary: Primary/near-primary evidence ledger for HD10-A term separation. Sources constrain trait-state distribution claims, idiographic personality dynamics, population-versus-within-person cognitive structure, cross-cultural transport, temperament/personality developmental continuity, task-support/offloading boundaries and cognitive-ability model interpretation. They are used as falsifiers and boundary evidence, not as authority for a final personality or intelligence ontology.
evidence_status: verified
readiness: READY
related:
  - human.deep-foundations.hd10a
  - human.deep-foundations.hd10.continuation
  - human.deep-foundations.post-hd9.direction-search.sources
---
# HD10-A — Evidence Ledger

## Rule

```text
PublishedConstruct != HumanPrimitive
Questionnaire != Trait
FactorModel != Mechanism
PredictiveValidity != ConstructIdentity
CrossCulturalFit != UniversalOntology
AgentSupportedPerformance != HumanIndependentCapability
```

---

# S01 — Whole Trait Theory: descriptive trait versus explanatory mechanism

William Fleeson & Eranda Jayawickreme. “Whole Trait Theory.” *Journal of Research in Personality* 56 (2015): 82–92. DOI: `10.1016/j.jrp.2014.10.009`. PMCID: `PMC4472377`. PMID: `26097268`.

The paper explicitly separates:

```text
Trait_DES
= descriptive density distribution of corresponding personality states

Trait_EXP
= explanatory social-cognitive mechanisms proposed to generate those distributions
```

It also emphasizes wide within-person state variability together with stable between-person differences in distribution parameters.

HD10-A use:

```text
TraitDescriptor != Mechanism
ScalarTraitScore != FullStateDistribution
WithinPersonVariability != NoStableDifference
```

Do **not** infer that Whole Trait Theory is the final HD10 ontology.

---

# S02 — trait enactments depend on actors and situations

William Fleeson & Mary Kate Law. “Trait Enactments as Density Distributions: The Role of Actors, Situations, and Observers in Explaining Stability and Variability.” *Journal of Personality and Social Psychology* 109(6):1090–1104 (2015). DOI: `10.1037/a0039517`. PMCID: `PMC4673017`. PMID: `26348598`.

HD10-A use:

```text
StableAggregateBehavior
must be separated from
stable situations encountered
and from momentary person-state variability.
```

This directly pressures:

```text
StableBehavior = StableInternalTrait
```

---

# S03 — idiographic momentary personality profiles

Colin J. Lee & Emorie D. Beck. “Idiographic Momentary Profiles of Personality Facets.” *Journal of Personality and Social Psychology* 130(1):160–185 (2026 issue; final publication 2025). DOI: `10.1037/pspp0000568`. PMCID: `PMC12262167`. PMID: `40658546`.

Experience-sampling data from two samples (`N=245`, `15,833` surveys) were modeled as person-specific multivariate state profiles. Most individuals expressed multiple distinct momentary profiles, and situation characteristics predicted profile expression.

HD10-A use:

```text
PersonalityProfile != one static point
PersonSpecificDynamics != PopulationAverageDynamics
SituationSensitivity is first-class
```

---

# S04 — between-person cognitive structure is not within-person structure

Florian Schmiedek, Martin Lövdén, Timo von Oertzen & Ulman Lindenberger. “Within-person structures of daily cognitive performance differ from between-person structures of cognitive abilities.” *PeerJ* 8:e9290 (2020). DOI: `10.7717/peerj.9290`. PMCID: `PMC7292017`. PMID: `32551201`.

Design:

```text
101 young adults
9 cognitive tasks
~100 daily occasions over ~6 months
```

The authors report substantial divergence among individuals' within-person cognitive structures and from the modal between-person structure; `g` was less prominent within than between persons.

HD10-A use:

```text
PopulationCovarianceStructure
!= WithinPersonCognitiveArchitecture
```

This is a direct anti-ergodic falsifier for naive person-level interpretation of group psychometrics.

---

# S05 — Process Overlap Theory test: one latent factor does not identify one process

Tengfei Wang et al. “How Executive Processes Explain the Overlap between Working Memory Capacity and Fluid Intelligence: A Test of Process Overlap Theory.” *Journal of Intelligence* 9(2):21 (2021). DOI: `10.3390/jintelligence9020021`. PMCID: `PMC8167629`. PMID: `33917495`.

The tested model found that shared WMC/Gf variance was largely associated with a common EF factor rather than the proposed specific inhibition/shifting factors; the authors concluded their findings did not support the tested POT account of the WMC–Gf relationship.

HD10-A use:

```text
CognitiveFactorCovariance
!= IdentifiedElementaryMechanism
```

---

# S06 — further process-overlap pressure

Gidon T. Frischkorn & Claudia C. von Bastian. “In Search of the Executive Cognitive Processes Proposed by Process-Overlap Theory.” *Journal of Intelligence* 9(3):43 (2021). DOI: `10.3390/jintelligence9030043`. PMCID: `PMC8395920`. PMID: `34449666`.

The reported domain-general executive-process factors showed small/inconsistent relations with a domain-general fluid-intelligence factor, while general processing-speed factors showed stronger relations.

HD10-A use:

```text
FluidIntelligenceFactor
!= one established executive-process mechanism
```

---

# S07 — Tsimane Big Five transport falsifier

Michael Gurven et al. “How Universal Is the Big Five? Testing the Five-Factor Model of Personality Variation Among Forager–Farmers in the Bolivian Amazon.” *Journal of Personality and Social Psychology* (2013). PMCID: `PMC4104167`. PMID: `23245291`.

In a Tsimane sample (`n=632`) using a translated 44-item Big Five Inventory, the authors did not find robust support for the expected five-factor model across the reported reliability, stability, validity and factor-structure tests.

HD10-A use:

```text
TranslatedInventory != GuaranteedCrossCulturalStructure
MeasurementTransport != OntologyTransport
```

This is not proof that Big Five structure never transports.

---

# S08 — positive counterexample: WISC-V/CHC-aligned factor invariance across three Western national samples

Linda K. Byrne et al. “Cross-National Generalizability of WISC-V and CHC Broad Ability Constructs across France, Spain, and the US.” *Journal of Intelligence* (2023). PMCID: `PMC10455271`. PMID: `37623542`.

Using nationally representative WISC-V standardization samples from France, Spain and the US, the study reported strict factorial invariance for the tested five-factor scoring model across the pairwise national comparisons.

HD10-A use:

```text
CrossPopulationMeasurementTransport can succeed
```

but:

```text
MeasurementInvariance
!= one causal mechanism
!= individual within-person architecture
!= unrestricted species-wide universality
```

The authors themselves note the Western/industrialized scope of the samples and need for broader testing.

---

# S09 — temperament/personality continuity with developmental change

Whitney R. Ringwald, Katherine M. Lawson, Aleksandra Kaurin & Richard W. Robins. “Linking Temperament and Personality Traits from Late Childhood to Adulthood by Examining Continuity, Stability, and Change.” *Journal of Personality and Social Psychology* 130(5):1047–1061 (2026 issue; final publication 2025). DOI: `10.1037/pspp0000576`. PMCID: `PMC12802452`. PMID: `40965930`.

Longitudinal sample:

```text
674 Mexican-origin youth
ages ~10–26
Rothbart temperament assessments ages 10–16
Big Five assessments ages 14–26
```

The study reports developmental continuity between several temperament/personality dimensions while also finding mean-level developmental changes.

HD10-A use:

```text
Temperament/PersonalityContinuity
!= TerminologicalIdentityByDefinition

RankOrderStability
!= MeanLevelStability
!= Immutability
```

---

# S10 — long-horizon personality stability is partial, not identity

Sarah E. Hampson & Lewis R. Goldberg et al. “A First Large-Cohort Study of Personality-Trait Stability Over the 40 Years Between Elementary School and Midlife.” PMCID: `PMC2247365`. PMID: `17014298`.

The study followed `N=799` participants from childhood teacher ratings to midlife self-report. Long-interval stability differed materially by trait and was lower than short-term adult stability.

HD10-A use:

```text
LongTermPredictiveContinuity
!= FixedTraitIdentity
```

---

# S11 — temperament can show early stability while remaining developmental

“Differential stability of temperament and personality from toddlerhood to middle childhood.” PMCID: `PMC2902199`. PMID: `20634996`.

Prospective longitudinal data across toddlerhood, early childhood and middle childhood supported consistency in broad positive emotionality, negative emotionality and constraint dimensions.

HD10-A use:

```text
EarlyEmergence != GeneticOnly
Stability != NoDevelopment
```

---

# S12 — cognitive offloading separates immediate performance from later memory

Sandra Grinschgl, Frank Papenmeier & Hauke S. Meyerhoff. “Consequences of cognitive offloading: Boosting performance but diminishing memory.” *Quarterly Journal of Experimental Psychology* 74(9):1477–1496 (2021). DOI: `10.1177/17470218211008060`. PMCID: `PMC8358584`.

Across two experiments (`N=172` each), increased offloading was associated with stronger immediate task performance but poorer subsequent memory for offloaded information.

HD10-A use:

```text
SupportedPerformance_t
!= InternalMemoryState_{t+1}
!= RetainedLearning
```

This is a pre-Agent but directly Agent-relevant capability falsifier.

---

# S13 — current Human repo as primary internal evidence

The HD10-A current-use audit directly inspected canonical Human research, especially:

```text
HF0-PROBLEM-SPACE.md
HF4-GOALS-MOTIVATION-VALUE.md
HF6-ADAPTATION-PLASTICITY-DEVELOPMENT.md
HF9-INFERENCE-REASONING-CAUSALITY-PROBLEM-SOLVING.md
HF11-ACTION-EXECUTION-SENSORIMOTOR-CONTROL.md
HF12-SOCIAL-INTERACTION-JOINT-ACTION-COMMUNICATION.md
HF13-PERSISTENT-SOCIAL-ORDER-NORMS-INSTITUTIONS.md
HF17-NORMATIVE-PLURALISM-SOCIAL-CHOICE-GOVERNANCE.md
HF19-WORK-PRODUCTION-ECONOMIC-ORGANIZATION.md
HD7-GENETIC-VARIATION-HEREDITY-GENE-ENVIRONMENT-INDIVIDUAL-DIFFERENCES.md
H0 systems/CAPABILITY.md
```

The internal audit is evidence about **Ordivon's current ontology**, not empirical evidence about Humans.

---

# Evidence synthesis for A

The evidence supports a cautious common denominator:

```text
People can exhibit relatively persistent between-person differences
while also showing large within-person variability.

Observed stability can reside in distribution parameters,
conditional response structure, developmental trajectories,
or stable context—not necessarily in one fixed internal scalar.

Population factor structures can be useful and transport across some populations,
but they cannot automatically be treated as person-level causal architecture.

Performance depends on state, task and support;
external support can improve immediate outcomes without equivalent internal learning.
```

This justifies term separation and the four-layer firewall. It does **not** choose the final HD10 model.
