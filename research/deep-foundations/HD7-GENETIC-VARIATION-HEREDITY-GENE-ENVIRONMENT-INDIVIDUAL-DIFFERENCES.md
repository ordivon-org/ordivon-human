---
schema_version: 1
id: human.deep-foundations.hd7
title: HD7 — Genetic Variation, Heredity, Gene–Environment Development and Individual Differences
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
summary: Deep reconstruction of Human genetic variation, heredity, gene regulation, genotype–environment interplay and individual differences after HD6. HD7 separates DNA sequence, gene, variant, allele, genotype, haplotype, germline and somatic genomic states, regulatory state, expression, molecular function, phenotype and measured trait; separates inheritance, de novo mutation, recombination and mosaicism; reconstructs association, linkage disequilibrium, fine-mapping, pleiotropy, direct and indirect genetic effects, penetrance/expressivity, rare/common architecture, heritability, gene–environment interaction/correlation and polygenic prediction; and pressure-tests ancestry/race, portability, population-to-individual inference and genetic authority. HD7 concludes that genetics/heredity is a foundationally important cross-cutting biological causal/inheritance layer rather than one missing peer Human foundation. HF24 is not admitted and HF0–HF23 remain unreopened. The strongest next global residual is evolution, phylogeny, population change and Human-specificity claims.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.deep-foundations.hd6.continuation
  - human.deep-foundations.hd7.sources
  - human.deep-foundations.hd7.continuation
  - human.foundations.hf0
  - human.foundations.hf1
  - human.foundations.hf6
  - human.foundations.hf8
  - human.foundations.hf14
  - human.foundations.hf15
  - human.foundations.hf16
  - human.foundations.hf23.continuation
---
# HD7 — Genetic Variation, Heredity, Gene–Environment Development and Individual Differences

## 0. Why HD7 exists

HD6 repeatedly required concepts that Human Foundations had only mentioned:

```text
genome / genotype
variant / allele
heritability
family resemblance
polygenic background
rare variants
gene regulation
gene × environment
population structure
individual differences
```

A repository-wide scan confirmed that these were not yet owned by a deep canonical route.

HD7 therefore asks:

> **How do inherited and acquired genomic differences participate in Human development and
> phenotypic variation without turning genes into traits, population statistics into
> individual essence, or prediction into authority?**

---

# 1. First firewall — gene is not trait

```text
Gene != Trait
```

A gene is a genomic functional/annotation unit under a declared molecular model.
A trait is a phenotype or measurement domain at another scale.

Many genes can influence one trait and one gene can influence many traits.

---

# 2. DNA sequence is not gene

```text
DNASequence != Gene
```

A genomic sequence contains coding and noncoding regions, regulatory elements, repeats,
structural organization and loci that may overlap multiple gene annotations.

---

# 3. Gene boundary is annotation/model relative

Alternative transcripts, promoters and overlapping transcriptional units force:

```text
GeneBoundary_D != GeneBoundary_E
```

HD7 therefore does not treat the word `gene` as one perfectly atomized physical object in
every analysis.

---

# 4. Variant is not gene

```text
Variant != Gene
```

A variant is a difference relative to a reference/alternative sequence representation at a
declared locus or structure.

Variants can occur inside, outside or across annotated genes.

---

# 5. Variant is not allele totality

```text
Variant != AlleleByDefinition
```

`Allele` usually denotes one alternative state at a locus/haplotype-defined unit; complex
structural and multi-allelic variation makes one-SNP language insufficient.

---

# 6. Reference allele is not normality

```text
ReferenceAllele != NormalAllele
```

Reference genomes are coordinate resources, not normative standards of Human biology.

---

# 7. Common is not benign

```text
CommonVariant != BenignByDefinition
```

Common variants can contribute to disease/trait differences.

---

# 8. Rare is not pathogenic

```text
RareVariant != PathogenicByDefinition
```

Most rare variants are not necessarily clinically causal, and pathogenicity inference
requires additional evidence.

---

# 9. Rare is not large effect

```text
Rare != LargeEffectByDefinition
```

Frequency and effect size are distinct coordinates, though evolutionary/demographic
processes can create statistical relations between them.

---

# 10. Common is not small effect by definition

```text
Common != SmallEffectByDefinition
```

Effect-size distribution must be empirically estimated for the declared phenotype/population.

---

# 11. Genotype is not phenotype

```text
Genotype != Phenotype
```

Phenotype arises through developmental, regulatory, environmental, stochastic and social
processes as well as genomic state.

---

# 12. Genotype is locus-relative

Use:

```text
Genotype_L(individual)
```

for allele configuration at declared locus L.

`Genotype` without locus/genomic scope can be ambiguous.

---

# 13. Haplotype is not genotype totality

```text
Haplotype != WholeGenotype
```

Haplotypes preserve linked allelic configuration over a declared genomic region/chromosome
copy.

---

# 14. Linkage is not causal interaction

```text
LinkageDisequilibrium != FunctionalInteraction
```

Two variants can be statistically correlated because of population/recombination history
without one mechanistically causing the other's phenotype association.

---

# 15. Germline genomic state is not every cell's genomic state

Somatic mutation and mosaicism force:

```text
GermlineGenome != EverySomaticCellGenomeState
```

A Human can contain multiple genetically distinct somatic lineages.

---

# 16. One biospecimen is not complete organism genomic state

```text
BloodGenotypeSample != EveryTissueGenomeState
SalivaGenotypeSample != EveryCellGenomeState
```

Most inherited variants are shared broadly, but tissue-restricted mosaic variants can be
missed.

---

# 17. Somatic mutation is not germline inheritance

```text
SomaticVariant != GermlineVariant
```

Somatic variants can affect the carrier organism without being transmissible through the
germline under ordinary inheritance.

---

# 18. Postzygotic is not inherited

```text
PostzygoticVariant != InheritedVariant
```

but early postzygotic variants can populate multiple tissues and potentially germline cells.

---

# 19. De novo is not parentally inherited

```text
DeNovoVariant != ParentallyInheritedVariant
```

A de novo event can arise in parental gametogenesis, gametes, the zygote or early
postzygotic development depending on the case.

---

# 20. De novo is not causally sufficient

```text
DeNovo != PathogenicByDefinition
```

Many de novo variants are neutral or of uncertain impact.

---

# 21. Inheritance is not copying without recombination

For nuclear genomes:

```text
ParentalGenomes
→ meiosis / recombination / segregation / mutation
→ GameteGenome
→ ZygoticGenome
```

Therefore offspring genomes are reconstructed combinations, not byte-identical copies.

---

# 22. Genetic inheritance is not cultural inheritance

HD4 remains authoritative:

```text
GeneticInheritance != CulturalInheritance
```

Both can transmit variation across generations but use different substrates and mechanisms.

---

# 23. Genetic inheritance is not epigenetic inheritance totality

```text
DNASequenceInheritance != EpigeneticStateInheritance
```

Some chromatin/methylation states can persist across cell divisions; transgenerational
persistence in Humans requires mechanism- and evidence-specific claims.

---

# 24. DNA sequence is not gene expression

```text
DNASequence != GeneExpression
```

Expression depends on regulatory elements, transcription factors, cell type, developmental
state, environment, chromatin and other molecular conditions.

---

# 25. Gene expression is not protein function

```text
RNAExpression != ProteinAbundance != ProteinActivity
```

Translation, degradation, localization, modification and molecular interactions intervene.

---

# 26. Gene expression is state-specific

Use:

```text
Expression(gene, cell_type, state, time, environment)
```

rather than a context-free expression number.

---

# 27. eQTL is not universal expression effect

```text
eQTL_D != UniversalExpressionEffect
```

Single-cell studies show many regulatory effects are cell-type-, disease- or
perturbation-state dependent.

---

# 28. Regulatory variant is not trait mechanism totality

```text
RegulatoryAssociation
!= CompletePhenotypeMechanism
```

A regulatory change can participate in a causal pathway without exhausting the phenotype.

---

# 29. Epigenetic is not `non-genetic everything`

```text
Epigenetic != NonGeneticEverything
```

Use only for explicitly defined molecular chromatin/mark/regulatory-state phenomena.

---

# 30. DNA methylation is not gene silencing by definition

```text
DNAMethylation != GeneSilencingByDefinition
```

Effect depends on genomic location, cell type, regulatory context and other molecular
features.

---

# 31. Epigenetic state is not environmentally caused by definition

```text
EpigeneticState != EnvironmentalEffectByDefinition
```

Genetic variants can strongly influence methylation/chromatin states.

---

# 32. Environmentally associated epigenetic state is not causal memory by definition

```text
ExposureAssociatedEpigeneticMark
!= CausalBiologicalMemoryByDefinition
```

Reverse causality, cell-composition shifts and confounding must be considered.

---

# 33. Phenotype is not measurement

HF0 evidence grammar applies:

```text
Phenotype_D != ObservedMeasure_D
```

A questionnaire score, biomarker or diagnosis is one evidence projection of a phenotype.

---

# 34. Trait label is not natural kind

HF23 term discipline applies:

```text
HasTraitName != OneBiologicalMechanism
```

`Intelligence`, `depression`, `height`, `income` and other measured outcomes differ greatly
in mechanism and measurement structure.

---

# 35. Genetic association is not causation

```text
GeneticAssociation != CausalEffectByDefinition
```

Association can arise from causal variants, LD with causal variants, population structure,
assortative mating, indirect family effects or other biases.

---

# 36. GWAS hit is not causal variant

```text
GWASSentinelVariant != CausalVariantByDefinition
```

A lead SNP often tags a linked region rather than the functional variant itself.

---

# 37. GWAS locus is not causal gene

```text
GWASLocus != CausalGeneByDefinition
```

Regulatory variants can act over distance or through cell-type-specific mechanisms.

---

# 38. Fine-mapped variant is not experimentally proven mechanism

```text
StatisticalFineMapping != FunctionalValidation
```

Posterior causal probability narrows candidates but is not direct molecular intervention.

---

# 39. Functional perturbation improves causal evidence but remains context-specific

CRISPR/allelic perturbation can strongly test variant function, yet:

```text
CausalEffect_InCellState_D
!= UniversalOrganismEffect
```

Developmental and tissue context remain relevant.

---

# 40. Genetic effect size is not one constant across every context

Use:

```text
Beta_variant,phenotype,population,environment,age,measure
```

not one metaphysical effect size.

---

# 41. Gene–environment interaction

At a declared statistical scale:

```text
Effect(Genotype | Environment=A)
!= Effect(Genotype | Environment=B)
```

or the joint phenotype relation deviates from the specified additive/no-interaction model.

---

# 42. G×E is not `genes plus environment`

```text
GeneticMainEffect + EnvironmentalMainEffect
!= GxEByDefinition
```

Interaction requires environment-dependent genetic effect or equivalent model-specific
nonadditivity.

---

# 43. G×E is model-scale dependent

Interaction on one scale may disappear or change on another:

```text
GxE_additiveScale
!= GxE_multiplicativeScale
```

Declare outcome transform/model.

---

# 44. Environment is not one scalar

Potential exposures include:

```text
nutrition
infection
pollution
education
caregiving
stress
social position
medication
physical environment
age/developmental stage
```

`Environment` without declared exposure is not a useful causal primitive.

---

# 45. Gene–environment interaction is not gene–environment correlation

```text
GxE != rGE
```

Gene–environment correlation concerns statistical dependence between genotype-related
variation and environmental exposure.

---

# 46. Gene–environment correlation is not direct genetic causation

```text
GenotypeEnvironmentCorrelation
!= DirectGeneticEffectOnOutcome
```

Social/family processes can mediate the association.

---

# 47. Parental genotype can affect offspring environment

Family studies support:

```text
ParentGenotype
→ ParentPhenotype/Resources/Behavior
→ OffspringEnvironment
→ OffspringPhenotype
```

without requiring transmission of the relevant allele to the child.

---

# 48. Indirect genetic effect is not direct offspring genetic effect

```text
IndirectGeneticEffect
!= DirectGeneticEffect
```

This is crucial for education, social and behavioral phenotypes.

---

# 49. Genetic nurture is not nuclear-family process totality

Large Norwegian family/cousin analyses show estimated indirect genetic effects can reflect
multi-generational/dynastic social processes beyond the nuclear household.

Thus:

```text
IndirectGeneticEffect
!= NuclearFamilyGeneticNurtureOnly
```

---

# 50. Population GWAS effect is not direct genetic effect by definition

Within-sibship GWAS shows that unrelated-person estimates can contain:

```text
direct inherited effects
+ population stratification
+ assortative mating
+ indirect family effects
+ demographic/social processes
```

Therefore:

```text
GWASPopulationBeta != DirectEffectBetaByDefinition
```

---

# 51. Within-family estimate is not complete biological causality

```text
WithinFamilyAssociation != CompleteMechanisticEffect
```

It changes confounding structure but still requires phenotype/model/measurement and causal
interpretation.

---

# 52. Assortative mating is not population stratification

```text
AssortativeMating != PopulationStratification
```

Both can alter genotype–phenotype association structure through different mechanisms.

---

# 53. Population structure is historical

Allele-frequency/LD differences emerge through combinations of:

```text
migration
drift
founder events
selection
admixture
population size/history
assortative mating
```

Population structure is not one categorical essence.

---

# 54. Genetic ancestry is not race

```text
GeneticAncestry != Race
```

Ancestry is inferred from genetic relatedness/population history under declared reference
models; race is a social classification whose boundaries vary across place/history.

---

# 55. Genetic ancestry can be continuous/admixtured

```text
Ancestry != OneDiscreteLabelByDefinition
```

Large diverse biobanks show continuous ancestry proportions and admixture patterns.

---

# 56. Self-identified race/ethnicity is not genetic ancestry

```text
SelfIdentifiedRaceEthnicity != GeneticAncestry
```

The variables may correlate in specific populations while measuring different histories and
social/biological relations.

---

# 57. Population label is not homogeneous genome

```text
AncestryLabel_D != GenomicHomogeneity
```

Fine-scale population structure persists within broad labels.

---

# 58. Between-population allele-frequency difference is not trait-genetic difference

```text
AlleleFrequencyDifference
!= PhenotypicDifferenceMechanismByDefinition
```

One must establish variant-to-trait causal pathways and environmental/context effects.

---

# 59. PGS is a model output, not genome essence

Use:

```text
PGS_{model,weights,training_population,variant_set,phenotype_definition}(person)
```

not a context-free `genetic value`.

---

# 60. PGS is not destiny

```text
PolygenicScore != Outcome
```

It is a probabilistic predictor under a model and population/context.

---

# 61. PGS portability is not guaranteed

Large biobank studies show prediction accuracy changes along genetic ancestry continua and
between cohorts.

Therefore:

```text
PGSPerformance_D != PGSPerformance_E
```

---

# 62. Lower portability is not evidence of different Human kinds

```text
PGSPortabilityFailure
!= HumanKindBoundary
```

LD, allele frequency, training composition, environmental distribution and phenotype
measurement can all contribute.

---

# 63. Shared effect sizes can coexist with portability loss

Recent cross-population analyses find substantial conservation of many genetic effects while
fine-scale structure still affects prediction/calibration.

Thus:

```text
SharedBiologicalEffects
can coexist with
UnequalPredictivePerformance
```

---

# 64. Polygenic is not `many genes each independently causing trait`

```text
PolygenicArchitecture
!= IndependentGeneSumByDefinition
```

LD, pathways, pleiotropy, regulatory networks and interactions complicate the mapping.

---

# 65. Polygenic is not small total genetic influence

```text
Polygenic != LowHeritability
```

Many small effects can collectively explain substantial variance.

---

# 66. Monogenic is not single-variant certainty

```text
MonogenicDiseaseLabel
!= OneVariantGuaranteesPhenotype
```

Incomplete penetrance and variable expressivity are common even in classically monogenic
disorders.

---

# 67. Pathogenic variant is not guaranteed phenotype

```text
PathogenicVariant != DiseaseOutcome
```

Penetrance is a probability conditional on variant, phenotype definition, population,
age/time and other modifiers.

---

# 68. Penetrance is not variant-only constant

Use:

```text
Penetrance_D(variant | age, population, phenotype_definition, ascertainment, modifiers)
```

rather than one universal number.

---

# 69. Clinical-family penetrance is not population penetrance

Ascertainment through affected families can overestimate penetrance relative to genotype-
first population cohorts.

```text
Penetrance_clinic != Penetrance_populationByDefinition
```

---

# 70. Penetrance is not expressivity

```text
Penetrance != Expressivity
```

Penetrance asks whether a declared phenotype occurs; expressivity concerns degree/form among
carriers/affected persons.

---

# 71. Rare and common variation can jointly shape `monogenic` phenotypes

Population studies support:

```text
RareLargeEffectVariant
× PolygenicBackground
× OtherModifiers
→ Risk / Severity
```

Thus:

```text
Monogenic != PolygenicExcluded
```

---

# 72. Polygenic background can modify penetrance

Kidney disease and other genomic-condition studies show substantial risk gradients among
carriers of the same broad monogenic-risk class according to polygenic background.

Therefore:

```text
CarrierStatus != FixedRisk
```

---

# 73. Other rare variants can modify expressivity

Large biobank analyses of developmental-disorder loci show rare-variant burden can alter
phenotypic severity alongside common polygenic background.

```text
PrimaryRareVariant != CompleteGeneticBackground
```

---

# 74. Allelic expression can modify penetrance

Family studies of monogenic immune disorders show expression bias between wild-type and
mutant alleles can track discordant clinical phenotype.

Thus:

```text
Genotype != Transcriptotype
```

---

# 75. Transcriptotype is not phenotype

```text
AllelicExpressionState != ClinicalOutcomeByDefinition
```

It is one mechanistic intermediate.

---

# 76. Variant pathogenicity annotation is not immutable truth

```text
VariantClassification_t
```

can change with evidence, functional testing, population data and disease definitions.

---

# 77. Predicted loss-of-function is not observed functional null by definition

```text
PredictedLoF != CompleteLossOfFunction
```

Alternative splicing, transcript usage, nonsense-mediated decay and tissue context can
matter.

---

# 78. Pleiotropy

Use:

```text
Variant/Gene affects multiple phenotypic domains
```

under declared causal/statistical criterion.

---

# 79. Pleiotropy is not one trait in disguise

```text
Pleiotropy != TraitIdentity
```

Shared variant associations do not mean two outcomes are the same construct.

---

# 80. Shared genetic correlation is not shared mechanism totality

```text
GeneticCorrelation != MechanisticIdentity
```

Correlation can arise through pleiotropic variants, mediated pathways, LD or measurement
structure.

---

# 81. Heritability is population variance decomposition

At a declared population/environment/time/model:

```text
h²_D = Var(genetic contribution under model D) / Var(phenotype under D)
```

The exact variance component depends on method and assumptions.

---

# 82. Heritability is not an individual property

```text
Heritability != PercentOfPersonCausedByGenes
```

One person is not `60% genetic and 40% environmental`.

---

# 83. Heritability is not immutability

```text
Heritable != Immutable
```

A phenotype can be highly heritable in one environment and still respond strongly to
intervention.

---

# 84. High heritability does not imply low environmental importance

```text
HighHeritability
!= LowEnvironmentalImportance
```

Uniform environments can reduce environmental variance while environmental interventions
still shift the trait mean.

---

# 85. Low heritability does not imply genetic irrelevance

```text
LowHeritability
!= NoGeneticMechanism
```

Measurement error, heterogeneous environments and rare/nonadditive effects can change
variance estimates.

---

# 86. Heritability is not causal effect size

```text
Heritability != InterventionEffect
```

Variance decomposition does not answer what will happen if one changes a gene or
environment.

---

# 87. Heritability is method-dependent

Family pedigree, twin/ACE, IBD, GREML, SNP heritability and LD-score approaches estimate
different components under different assumptions.

Therefore:

```text
Heritability_MethodA != Heritability_MethodBByDefinition
```

---

# 88. Method differences are empirical, not philosophical only

A 2025 Norwegian study applying four methods to the same broad population and administrative
SES measures produced materially different estimates across methods and phenotypes.

Thus:

```text
HeritabilityEstimate
= function(phenotype, population, method, assumptions, measurement)
```

---

# 89. SNP heritability is not total narrow-sense heritability

```text
SNPHeritability != TotalAdditiveGeneticVarianceByDefinition
```

Array/imputation coverage and variant-frequency spectrum matter.

---

# 90. Missing heritability is not one missing gene

```text
MissingHeritability != MissingSingleCause
```

Rare variation, imperfect tagging, structural variation, interactions, measurement and model
limits can contribute.

---

# 91. Rare variants can contribute substantial complex-trait variance

Large sequencing analyses estimate nontrivial heritability from rare coding variants for
many complex traits.

Therefore common-SNP architecture is incomplete.

---

# 92. Noncoding rare variants can have large effects

Whole-genome sequencing studies identify rare regulatory/noncoding variants with measurable
large effects on height.

Thus:

```text
CodingVariant != FunctionalVariantTotality
```

---

# 93. Structural variants are not SNPs

```text
CNV / inversion / repeat variation != SNP
```

Variant representation itself is multi-class.

---

# 94. Tandem repeat variation is not captured by biallelic SNP ontology

```text
MultiAllelicRepeatVariation != BinaryVariant
```

Human genomic variation requires more than one variant data type.

---

# 95. Mitochondrial genome variation is not nuclear genotype

```text
mtDNAVariation != NuclearGenotype
```

Heteroplasmy and tissue-specific mtDNA mosaicism add another genomic layer.

---

# 96. Genome is not static across life

Somatic mutations accumulate and clones expand/contract.

```text
SomaticGenomeState_t1 != SomaticGenomeState_t2ByDefinition
```

for some tissues/lineages.

---

# 97. Genetic identity is not organism identity

HF1 remains authoritative:

```text
SameOrganism != SameEveryCellGenomeState
```

Somatic mosaicism occurs without producing a new Human individual for each clone.

---

# 98. Same genome does not imply same phenotype

Monozygotic twins and cloned/engineered cell contexts demonstrate:

```text
Same/near-same inherited genome
!= SamePhenotypeTotality
```

Environment, stochastic development and somatic variation remain.

---

# 99. Different genomes do not imply different Human kind

```text
GenomicDifference != HumanKindDifferenceByDefinition
```

All Humans differ genomically; the question is effect at a declared locus/domain.

---

# 100. Individual difference is not trait essence

Use:

```text
Difference_D(PersonA, PersonB, time, context, measure)
```

rather than `PersonA has more essence X`.

---

# 101. Genetic contribution to individual differences is not fixed trait ranking

```text
GeneticVarianceContribution
!= ImmutableRankOrder
```

Development and environment can change observed distributions and ranks.

---

# 102. Group average is not individual prediction

```text
GroupMeanGeneticAssociation
!= IndividualOutcome
```

Prediction uncertainty and within-group variation remain first-class.

---

# 103. Between-group genetic association is especially nonportable

Population structure, environment, phenotype definition and LD can differ.

```text
Association_GroupA
!= Association_GroupBByDefinition
```

---

# 104. Ancestry-adjusted is not confounding-free by definition

```text
AdjustedForPCs != AllPopulationStructureRemoved
```

Fine-scale geographic/social structure can remain.

---

# 105. Genetic principal components are coordinates, not races

```text
GeneticPC != RaceCategory
```

They summarize axes of genotype covariance in a particular dataset/reference.

---

# 106. Ancestry inference is reference-dependent

```text
GeneticAncestryEstimate_D
```

changes with reference populations, marker set and statistical model.

---

# 107. Genetic ancestry is not nationality

```text
GeneticAncestry != Nationality
```

Nationality is institutional/legal/social classification.

---

# 108. Genetic ancestry is not culture

```text
GeneticAncestry != Culture
```

HD4 cultural inheritance is independent though historically correlated processes can
interact.

---

# 109. Genetic ancestry is not identity totality

```text
GeneticAncestry != Personal/SocialIdentity
```

HF1 remains identity owner.

---

# 110. Behavioral/social phenotypes require stronger confounding discipline

Within-family evidence shows larger attenuation for traits such as educational attainment,
age at first birth, smoking and depressive symptoms than for many molecular phenotypes.

Thus:

```text
SocialPhenotypeGWAS
requires explicit indirect/demographic pathways
```

---

# 111. Biology and society can become statistically entangled

For some traits:

```text
Genotype
→ phenotype
→ social response/environment
→ future phenotype
```

and:

```text
ParentGenotype
→ family/social environment
→ child phenotype
```

Therefore social structure can become part of genotype–phenotype association without being
encoded directly in DNA.

---

# 112. Genetic prediction can become self-altering

If a PGS affects treatment, education, insurance or behavior, then:

```text
Prediction
→ intervention/social response
→ outcome distribution
```

The prediction system becomes part of the causal environment.

---

# 113. Predictive accuracy is not causal understanding

```text
PGSAccuracy != MechanisticUnderstanding
```

A distributed predictor can work without identifying each causal pathway.

---

# 114. Causal understanding is not clinical utility by definition

```text
MechanisticInsight != ActionableBenefitByDefinition
```

Effect size, intervention availability, calibration and harms matter.

---

# 115. Genetic risk is not disease

```text
GeneticRisk != Disease
```

Risk is probabilistic and endpoint/time dependent.

---

# 116. Genetic risk is not fate

```text
RiskScore != Fate
```

Even high-risk rare variants may show incomplete penetrance.

---

# 117. Genetic risk is not moral responsibility

```text
GeneticRisk != Blame
```

HF14 responsibility remains causal/control/knowledge/role dependent.

---

# 118. Genetic similarity is not moral similarity

```text
GeneticRelatedness != MoralStanding
```

HF15 remains standing owner.

---

# 119. Genetic relatedness is not family totality

HF22 remains authoritative:

```text
GeneticRelatedness != SocialKinship/Family
```

---

# 120. Genetic prediction does not confer authority

```text
CanPredictTrait_D
!= AuthorityToRank/RestrictPerson
```

HF0/HF14 authority firewalls apply.

---

# 121. Genomic data are unusually identifying and persistent

Unlike many transient measurements, germline variation is largely stable and correlated with
biological relatives.

Therefore access/consent models must account for:

```text
individual privacy
familial inference
future reinterpretation
secondary findings
population/group implications
```

---

# 122. Consent to sequencing is not consent to every future inference

```text
ConsentToGenotyping/Sequencing
!= ConsentToAnySecondaryInference
```

Purpose, scope and governance remain distinct.

---

# 123. Relative inference is not relative authorization

```text
CanInferRelativeRisk
!= AuthorityToExposeRelativeInformation
```

Genomic information has relational privacy effects.

---

# 124. Genetic discoverability is not social legitimacy

```text
DiscoverableDifference
!= LegitimateDiscrimination
```

Description cannot produce rights/role allocation automatically.

---

# 125. Competing model F1 — one-gene/one-trait determinism

Core:

```text
Gene X → Trait Y
```

Strength: approximates some high-penetrance molecular disorders under narrow definitions.

Failure: pleiotropy, polygenicity, penetrance, regulation and environmental modifiers.

Disposition: **retain only for validated narrow mechanisms; reject as general Human model**.

---

# 126. F2 — Mendelian categorical inheritance

Core:

```text
dominant / recessive / X-linked classes
```

Strength: powerful for many variant–disease relations.

Limit: penetrance/expressivity, modifier background and complex traits remain.

Disposition: **retain inheritance grammar, reject phenotype certainty**.

---

# 127. F3 — infinitesimal/polygenic additive model

Core:

```text
Phenotype ≈ sum many small additive genetic effects + residual
```

Strength: useful statistical approximation for many complex traits.

Failure: rare large effects, structural variants, interactions and indirect effects.

Disposition: **retain model family, not ontology totality**.

---

# 128. F4 — rare-variant/core-gene model

Core:

```text
rare damaging variants in constrained/core genes drive substantial phenotype
```

Strength: strong for selected diseases/traits.

Limit: penetrance and common background matter.

Disposition: **retain alongside polygenic architecture**.

---

# 129. F5 — omnigenic/network-distributed influence family

Core:

```text
regulatory networks spread small effects across many genes
```

Strength: explains broad polygenicity.

Limit: not every trait architecture is equally diffuse; functional mechanisms remain
question-specific.

Disposition: **retain as hypothesis family**.

---

# 130. F6 — heritability-as-trait-property model

Core:

```text
Trait X is 70% genetic
```

Failure: population/method/environment dependence.

Disposition: **reject**.

---

# 131. F7 — direct-GWAS-effect model

Core:

```text
GWAS beta = direct biological effect
```

Failure: within-family attenuation, stratification, assortative mating, indirect effects.

Disposition: **reject by default; directness requires design/evidence**.

---

# 132. F8 — fixed-effect-across-context model

Core:

```text
variant effect constant across environments/cell states/populations
```

Failure: G×E, reQTL, disease-state eQTL and portability evidence.

Disposition: **use only after invariance test**.

---

# 133. F9 — purely environmental epigenetics

Core:

```text
epigenome = environmental record
```

Failure: genetic control of methylation/chromatin and cell-type specificity.

Disposition: **reject**.

---

# 134. F10 — ancestry-as-discrete-biological-race

Failure: admixture/continuity/fine-scale structure and social classification mismatch.

Disposition: **reject**.

---

# 135. F11 — PGS-as-individual-genetic-value

Failure: model/training/cohort/ancestry dependence and probabilistic prediction.

Disposition: **reject; use exact model-conditioned score**.

---

# 136. F12 — monogenic/polygenic dichotomy

Failure: rare/common modifier studies.

```text
MonogenicMechanism
and
PolygenicBackground
can coexist
```

Disposition: **reject exclusive dichotomy**.

---

# 137. F13 — static-genome individual

Failure: somatic mosaicism, clonal expansion and mtDNA heteroplasmy.

Disposition: **retain germline genome as major stable inherited substrate; reject every-cell
identity**.

---

# 138. F14 — developmental systems model

Core:

```text
Genome
× RegulatoryState
× Development
× Environment
× Stochasticity
× SocialFeedback
→ PhenotypeTrajectory
```

Strength: survives most HD7 falsifiers.

Limit: too general to substitute for domain-specific mechanism.

Disposition: **retain as HD7 integration grammar, not universal equation**.

---

# 139. Cross-context falsifier matrix

| ID | Case | Collapse attacked | Surviving distinction |
|---|---|---|---|
| G01 | one gene associated with many phenotypes | gene = one trait | pleiotropy |
| G02 | thousands of loci for one complex trait | trait = one gene | polygenicity |
| G03 | noncoding functional variants | gene effect = coding sequence only | regulation matters |
| G04 | CNV/repeat associations | variant = SNP | multi-class variation |
| G05 | rare coding heritability | common SNPs = genetic architecture totality | rare variation contributes |
| G06 | rare noncoding height effects | rare functional = coding only | regulatory rare variants |
| G07 | same rare disease variant, variable phenotype | pathogenic variant = guaranteed disease | incomplete penetrance/expressivity |
| G08 | kidney monogenic variant + PGS gradient | monogenic excludes polygenic | background modifies risk |
| G09 | developmental-disorder rare burden + PGS | one rare variant = complete genetic cause | rare/common modifiers |
| G10 | allele-specific expression in immune disease | genotype = transcript state | expression mediates penetrance |
| G11 | clinic vs population ascertainment | penetrance = universal constant | ascertainment/context |
| G12 | four heritability methods in same broad cohort | heritability = one number | method dependence |
| G13 | environmental intervention on heritable trait | heritable = immutable | intervention still possible |
| G14 | within-sibship attenuation | population GWAS = direct effect | indirect/demographic effects |
| G15 | parental nontransmitted effects | child's genotype = all genetic association | indirect genetic effect |
| G16 | cousin/dynastic results | genetic nurture = nuclear family only | multigenerational social process |
| G17 | fine-scale population structure | broad ancestry label = homogeneous | continuous/local structure |
| G18 | PGS accuracy ancestry continuum | PGS = portable score | model/population dependence |
| G19 | shared effect sizes + portability loss | portability loss = different biology totality | LD/training/context matter |
| G20 | admixed individuals | ancestry = one discrete class | continuous mixture |
| G21 | self-ID vs genetic ancestry | race/ethnicity = ancestry | social vs genetic projection |
| G22 | cross-population G×E | genetic beta = context-free | environment-dependent effects |
| G23 | response eQTL under infection | eQTL = universal | perturbation state matters |
| G24 | brain disease-dependent eQTL | regulatory effect = disease-invariant | cell/disease state matters |
| G25 | immune exposure epigenome | epigenetic = environmental only | genetics + exposure both matter |
| G26 | identical twins diverge phenotypically | same inherited genome = same phenotype | environment/stochasticity |
| G27 | brain somatic mosaicism | one Human = one cell genome | multiple somatic lineages |
| G28 | mtDNA heteroplasmy | genome = nuclear diploid genome only | mitochondrial variation |
| G29 | de novo mutation across pedigree | inherited variation only | mutation creates new variation |
| G30 | postzygotic de novo fraction | de novo = parental germline only | developmental timing matters |
| G31 | lead SNP tags causal region | GWAS hit = causal variant | LD/fine-mapping required |
| G32 | CRISPR state-specific allele effect | functional variant = universal organism effect | context-specific causality |
| G33 | genetic correlation across traits | shared genetics = same trait | pleiotropy/measurement separate |
| G34 | PGS predicts without mechanism | prediction = explanation | predictive vs causal surface |
| G35 | risk carriers without disease | genetic risk = disease | probability vs state |
| G36 | genetic relative inference | individual's data = only individual privacy | relational privacy |
| G37 | ancestry-associated allele frequency | frequency difference = phenotypic mechanism | causal bridge required |
| G38 | population mean difference | group result = individual classification | within-group heterogeneity |
| G39 | same genotype under different environments | genotype = fixed phenotype | developmental/context dependence |
| G40 | different phenotype definitions | same trait name = same heritability | measurement/construct dependence |
| G41 | age-specific genetic effects | effect = lifespan constant | time/development dimension |
| G42 | somatic clonal expansion with aging | genetic state fixed from conception | acquired genomic history |

---

# 140. Minimum genomic-state grammar

```text
GenomicState_D = {
  reference/coordinate system,
  germline nuclear sequence/variant state,
  haplotypes when relevant,
  mitochondrial sequence/heteroplasmy when relevant,
  somatic mosaic/clonal variants when relevant,
  structural/repeat variation,
  developmental/tissue sampling scope,
  uncertainty / calling quality
}
```

Do not collect the whole genome when the question needs one locus.

---

# 141. Minimum genotype-to-phenotype grammar

```text
GenomicState
+ RegulatoryArchitecture
+ Cell/TissueState
+ DevelopmentalHistory
+ Environment/Exposure
+ OtherGeneticBackground
+ StochasticProcesses
+ Social/InstitutionalFeedback
→ MolecularIntermediate(s)
→ Organ/Behavioral/SystemPhenotype
→ ObservedMeasure
```

Every arrow can be many-to-many.

---

# 142. Minimum heritability claim

A valid statement needs:

```text
Phenotype definition
Population
Age/time range
Environment/context
Method/model
Variant scope
Estimate + uncertainty
```

Without these:

```text
"X is N% genetic"
```

is incomplete.

---

# 143. Minimum GWAS claim

```text
Phenotype
Cohort/sample
Ancestry/population structure handling
Variant set/reference
Association model
Effect estimate + uncertainty
Replication
Fine-mapping/functional status
Direct/indirect-effect evidence
```

---

# 144. Minimum PGS claim

```text
Score construction/training GWAS
Phenotype definition
Target population/cohort
Ancestry distribution
Calibration/discrimination metric
Baseline comparator
Absolute vs relative risk
Uncertainty
Intervention/decision threshold if any
```

---

# 145. Minimum penetrance claim

```text
Variant/class
Phenotype criterion
Age/time horizon
Population/ascertainment
Genetic modifiers
Environment/treatment context
Estimate + uncertainty
```

---

# 146. Reconnection to HF0

HF0's projection discipline becomes essential:

```text
GenomeData != HumanOntology
GeneticMeasure != ConstructTotality
```

Genetics is one evidence/causal layer, not a replacement for Human modeling.

---

# 147. Reconnection to HF1

HF1 owns organism/person identity.

HD7 adds:

```text
GenomeIdentity != PersonIdentity
SomaticClone != NewHumanIndividualByDefinition
```

No HF1 reopening required.

---

# 148. Reconnection to HF5/HF6

Genotype shapes regulatory and developmental possibilities, but HF5/HF6 own current
regulation and history-dependent change.

```text
GenomicConstraint
× HF5 Regulation
× HF6 Development
→ phenotype trajectory
```

Genetics does not replace development.

---

# 149. Reconnection to HF8

Genetic knowledge is representation/evidence about biological state.

```text
GeneticTestResult != BiologicalStateTotality
```

Interpretation, uncertainty and future reclassification remain HF8-relevant.

---

# 150. Reconnection to HF10

Genetic information can change options/decisions, but:

```text
RiskPrediction != Decision
```

and decision quality depends on actionability, preferences, uncertainty and harms.

---

# 151. Reconnection to HF14/HF15

```text
Genotype != MoralWorth
GeneticRisk != Responsibility
GeneticRelatedness != MoralStanding
```

No normative authority leaks from genetics.

---

# 152. Reconnection to HF16

Population genetics and demography can change future allele distributions, but HF16 owns
population/temporal normative aggregation.

```text
AlleleFrequencyChange != PopulationWelfareChange
```

---

# 153. Reconnection to HF22

```text
GeneticRelatedness != Family
```

HD7 supplies biological relatedness; HF22 supplies persistent social relation/kinship.

---

# 154. Reconnection to HD4

Genetic and cultural inheritance can interact:

```text
Genes
↔ DevelopmentalEnvironment
↔ Culture
```

but:

```text
GeneticInheritance != CulturalInheritance
```

HD4 remains cultural-process owner.

---

# 155. Reconnection to HD6

HD6 sex/reproduction consumes HD7 variables for sex-development pathways, puberty timing,
fertility and reproductive variation.

But:

```text
GeneticSexCoordinate != CompleteSexProfile
```

remains intact.

---

# 156. Foundation candidate A — `Genome / Genomic State` HF24

Audit:

```text
Repeated residual?                  yes
Stable object?                      yes at molecular/organism scale
Human-functional peer object?       weak
Already part of organism substrate? substantially
Risk of one-genome simplification?  high due mosaicism
```

A genomic-state representation is useful, but making it a peer Human foundation would mix
molecular implementation level with functional/relational Human ontology without a clean
neighboring-scale need.

Disposition:

```text
Reject GenomicState HF24.
```

---

# 157. Candidate B — `Genetic Inheritance / Heredity` HF24

Inheritance is deeply important, but its core dynamics are:

```text
population/lineage transmission
recombination
segregation
mutation
selection/history
```

This is a cross-generational biological process analogous in form (not mechanism) to HD4
cultural inheritance.

It spans HF1 organism continuity, HF6 development and later population/evolution layers
rather than defining one Human-level subsystem.

Disposition:

```text
Reject standalone Heredity HF24;
retain HD7 as canonical cross-cutting causal/inheritance owner.
```

---

# 158. Candidate C — `Individual Differences` HF24

Fails the object test most strongly.

```text
IndividualDifference
```

is a relation between persons under a declared domain/measure, not a subsystem.

Differences can arise from:

```text
genetics
development
environment
learning
culture
institutions
stochasticity
tools
relationships
```

Disposition: **reject**.

---

# 159. Candidate D — `Nature / Nurture` HF24

Fails because the dichotomy itself is misleading:

```text
GeneticEffect
EnvironmentalEffect
GxE
rGE
IndirectGeneticEffect
DevelopmentalMediation
```

cannot be represented as two independent boxes.

Disposition: **reject**.

---

# 160. HD7 foundation decision

```text
NextFoundationAdmissionCondition(HF24) = false
FoundationReopenCondition(HF0–HF23) = false
```

HD7 joins HD4 and HD6 as a deep owner without peer-HF promotion, for a third distinct reason:

```text
HD4 = cross-foundation population-historical cultural process
HD6 = cross-layer biological/psychological/social domain
HD7 = cross-cutting biological causal/inheritance substrate and process
```

---

# 161. Why no existing foundation reopens

```text
HF0 projection/evidence discipline                  survives
HF1 typed identity                                  survives mosaicism
HF6 history-dependent development                   strengthened
HF8 representation/knowledge                        survives test interpretation
HF14 normative authority firewall                   strengthened
HF16 population aggregation                         remains separate
HF22 kinship != genetics                            strengthened
```

The problem was missing mechanism depth, not false frozen claims.

---

# 162. Strongest new residual: evolution and phylogeny

Once HD7 exists, several questions can no longer remain implicit:

```text
How do allele frequencies change across generations?
What is natural selection versus drift?
What does adaptation mean at population level?
What is genetic fitness versus Human welfare?
How should Human-specific claims be tested comparatively?
Which traits are homologous, convergent or culturally derived?
How do gene–culture coevolution and niche construction work?
What does evolutionary explanation explain — and not explain?
```

HD0 already rated evolution/comparative Human as sparse, central and high-falsifier-leverage.

HD7 makes that residual unavoidable.

---

# 163. Next deep route

Admit as non-foundation research only:

```text
HD8 — Evolution, Phylogeny, Population Change, Natural Selection and Human Specificity
```

with:

```text
HD8 != HF24
HF24 = UNKNOWN
```

---

# 164. HD8 starting guard

Do not assume:

```text
Evolution = Progress
Adaptation = Optimality
NaturalSelection = IntentionalDesign
Fitness = Welfare
Fitness = MoralWorth
HeritableTrait = Adaptation
CurrentFunction = HistoricalSelectionCause
CommonTrait = AdaptiveTrait
HumanUnique = HumanUniversal
HumanUnique = NoAnimalPrecursor
Gene = UnitOfSelectionTotality
Selection = AlleleFrequencyChangeTotality
Drift = NoiseOnly
EvolutionaryExplanation = ProximateMechanism
BiologicalFunction = NormativePurpose
```

---

# 165. Narrative remains unresolved, not rejected

HD5's narrative/imagination residual remains real.

But after HD7:

```text
Evolution/comparative Human
```

has greater global dependency because it constrains claims throughout perception, affect,
sociality, culture, language, sexuality and genetics.

The post-HD7 global residual scan has now been run. Evolution/comparative Human remains the strongest next dependency after comparison with narrative/imagination, broader organism systems, collective identity, sleep/dreaming and psychopathology, so HD8 is confirmed rather than merely provisional.

---

# 166. HD7 durable firewalls

```text
Gene != Trait
DNASequence != Gene
Variant != Gene
ReferenceAllele != Normality
Rare != Pathogenic != LargeEffect
Common != Benign != SmallEffect
Genotype != Phenotype
LD != FunctionalInteraction
GermlineGenome != EverySomaticCellGenomeState
SomaticVariant != GermlineVariant
DeNovo != Inherited != PathogenicByDefinition
GeneticInheritance != CulturalInheritance
DNASequence != GeneExpression
RNAExpression != ProteinActivity
GeneExpression = context/state dependent
 eQTL != UniversalExpressionEffect
Epigenetic != NonGeneticEverything
Phenotype != Measure
TraitLabel != NaturalKind

GeneticAssociation != CausalEffect
GWASHit != CausalVariant
GWASLocus != CausalGene
FineMapping != FunctionalValidation
PopulationGWASBeta != DirectGeneticEffectByDefinition
WithinFamilyAssociation != CompleteMechanism

GxE != GeneticMainEffect + EnvironmentalMainEffect
GxE != rGE
IndirectGeneticEffect != DirectGeneticEffect
IndirectGeneticEffect != NuclearFamilyNurtureOnly
AssortativeMating != PopulationStratification

GeneticAncestry != Race
GeneticAncestry != Nationality != Culture != Identity
Ancestry != OneDiscreteLabel
PopulationLabel != GenomicHomogeneity
AlleleFrequencyDifference != PhenotypicMechanism

PGS != Destiny
PGS != IndividualGeneticValue
PGSPerformance_D != PGSPerformance_E
PGSPortabilityFailure != HumanKindBoundary
Prediction != Mechanism != Authority

Monogenic != PhenotypeCertainty
Monogenic != PolygenicExcluded
PathogenicVariant != DiseaseOutcome
Penetrance != Expressivity
Penetrance_D != universal constant
Genotype != Transcriptotype != Phenotype
PredictedLoF != FunctionalNullByDefinition

Heritability != IndividualProperty
Heritable != Immutable
HighHeritability != LowEnvironmentalImportance
LowHeritability != NoGeneticMechanism
Heritability != InterventionEffect
Heritability_MethodA != Heritability_MethodB
SNPHeritability != TotalHeritability
MissingHeritability != MissingSingleCause

GeneticVarianceContribution != FixedIndividualRank
GroupAssociation != IndividualOutcome
GenomeIdentity != PersonIdentity
GeneticRelatedness != MoralStanding != Family
GeneticRisk != Disease != Fate != Blame
GeneticPrediction != LegitimateAuthority
ConsentToSequencing != ConsentToEveryFutureInference
```

---

# 167. Final HD7 compression

The rejected Human genetics model is:

```text
Gene
→ Trait
→ Person type
```

The surviving architecture is closer to:

```text
Population / Lineage History
        ↓
Inherited Genomic Variation
+ De Novo Variation
        ↓
Germline Genomic State
        ↓
Development + Recombination History + Somatic Mosaicism
        ↓
Cell/Tissue Regulatory State
        ↕
Environment / Exposure / Social Context
        ↓
Expression / Molecular Function
        ↓
Organism / Cognitive / Behavioral Phenotype
        ↓
Measurement / Diagnosis / Social Response
        ↺
Future Environment / Reproduction / Selection
```

with additional pathways:

```text
ParentGenotype → OffspringEnvironment
PopulationStructure → AssociationEstimate
ModelTrainingPopulation → PGSPerformance
```

The core result is therefore:

> **Genetic variation constrains and participates in Human development; it does not encode a
> complete person, trait, destiny, social identity or normative rank. Genetic effects are
> pathway-, population-, developmental-, cell-state- and environment-qualified, and genetic
> evidence must remain separated from causal mechanism, prediction and authority.**
