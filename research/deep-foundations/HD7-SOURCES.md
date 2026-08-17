---
schema_version: 1
id: human.deep-foundations.hd7.sources
title: HD7 Genetic Variation, Heredity and Individual Differences — Primary Evidence Ledger
type: source-review
profile: research
lifecycle: completed
source_role: evidence
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
updated: 2026-08-17
summary: Primary-evidence ledger for HD7 across heritability methods, within-family versus population GWAS, indirect genetic/dynastic effects, polygenic-score portability, fine-scale ancestry structure, gene–environment interaction, cell-state-specific regulation, epigenomic environmental/genetic effects, rare/common architecture, incomplete penetrance/expressivity, de novo variation, structural/repeat variation, pleiotropy, functional variant testing and somatic/mitochondrial mosaicism.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.deep-foundations.hd7
---
# HD7 — Primary Evidence Ledger

## Evidence rule

HD7 prioritizes primary human cohort, family, sequencing, single-cell and perturbation studies.
Its role is not to adjudicate every genetics methodology, but to pressure the Human world-
model boundaries among genomic state, regulation, phenotype, population statistics,
prediction and authority.

## S01 — Heritability varies by phenotype and estimation method

Ebeltoft, J. C. et al. (2025). **The genetic and environmental composition of socioeconomic
status in Norway.** Nature Communications 16, 4461.

More than 170,000 Norwegian adults were analyzed with four family- and genotype-based
heritability methods for education, occupation, income and wealth. Estimates varied by both
measure and method, even within a common national/cohort framework.

Use:

```text
Heritability != TraitEssence
HeritabilityEstimate = f(population, phenotype, method, assumptions)
```

Source: https://www.nature.com/articles/s41467-025-58961-6

## S02 — Population GWAS can mix direct and indirect/demographic effects

Howe, L. J. et al. (2022). **Within-sibship genome-wide association analyses decrease bias
in estimates of direct genetic effects.** Nature Genetics.

178,086 siblings across 19 cohorts were used to compare population and within-sibship GWAS
for 25 phenotypes. Estimates for several social/behavioral traits attenuated within families.

Use:

```text
PopulationGWASBeta != DirectGeneticEffectByDefinition
WithinFamilyDesign changes confounding structure
```

Source: https://www.nature.com/articles/s41588-022-01062-7

## S03 — Indirect genetic effects can be dynastic/social rather than nuclear-family only

Nivard, M. G. et al. (2024). **More than nature and nurture, indirect genetic effects on
children’s academic achievement are consequences of dynastic social processes.** Nature
Human Behaviour 8, 771–778.

37,117 parent–offspring trios plus related-family/cousin designs were used to distinguish
nuclear-family genetic nurture from broader dynastic processes.

Use:

```text
IndirectGeneticEffect != DirectGeneticEffect
IndirectGeneticEffect != NuclearFamilyProcessOnly
```

Source: https://www.nature.com/articles/s41562-023-01796-2

## S04 — PGS accuracy changes along continuous genetic ancestry

Ding, Y. et al. (2023). **Polygenic scoring accuracy varies across the genetic ancestry
continuum.** Nature 618, 774–781.

Large Los Angeles and UK biobank analyses showed individual-level PGS accuracy varies along
ancestry continua, including within broad ancestry labels.

Use:

```text
PGSPerformance_D != PGSPerformance_E
Ancestry != OneDiscreteHomogeneousGroup
```

Source: https://www.nature.com/articles/s41586-023-06079-4

## S05 — Fine-scale population structure matters while many effect sizes remain conserved

Myers, S. R. et al. (2025). **Fine-scale population structure and widespread conservation
of genetic effect sizes between human groups across traits.** Nature Genetics 57, 379–389.

Use: fine-scale structure can alter association/prediction while substantial cross-group
biological effect conservation can coexist.

```text
PopulationStructure != HumanKindBoundary
SharedEffects can coexist with PortabilityDifferences
```

Source: https://www.nature.com/articles/s41588-024-02035-8

## S06 — Genetic ancestry and self-identified race/ethnicity are distinct measurements

All of Us Research Program Genomics Investigators (2024). **Genomic data in the All of Us
Research Program.** Nature.

The diverse WGS dataset included continuous genetic ancestry inference and comparisons with
self-identified race/ethnicity.

Use:

```text
GeneticAncestry != SelfIdentifiedRaceEthnicity
Ancestry can be continuous/admixtured
```

Source: https://www.nature.com/articles/s41586-023-06957-x

## S07 — Large cross-population G×E atlas

2026 Nature study **A cross-population compendium of gene–environment interactions.**

440,210 European/Japanese participants with replication in 539,794 diverse participants;
age, sex and lifestyle exposures altered genetic effect patterns and polygenic prediction.

Use:

```text
GeneticEffect != ContextFreeConstant
GxE can affect portability/prediction
```

Source: https://www.nature.com/articles/s41586-025-10054-6

## S08 — Specific environment can change SNP heritability/effect architecture

2025 Nature Communications study **Genome-wide gene-environment interaction study uncovers
162 vitamin D status variants using a precise ambient UVB measure.**

Use: ambient UVB/outdoor exposure strata changed estimated SNP heritability and supported
specific genotype–environment effects.

Source: https://www.nature.com/articles/s41467-025-65820-x

## S09 — Response eQTLs depend on perturbation state and cell type

2025 Nature Genetics study **Modeling heterogeneity in single-cell perturbation states
enhances detection of response eQTLs.**

Accounting for continuous per-cell perturbation state increased detected reQTLs; many were
cell-type specific.

Use:

```text
eQTL != UniversalExpressionEffect
RegulatoryEffect = cell/state/context qualified
```

Source: https://www.nature.com/articles/s41588-025-02344-6

## S10 — Brain allelic effects can depend on disease state

2025 Nature Genetics study **Cell state-dependent allelic effects and contextual Mendelian
randomization analysis for human brain phenotypes.**

2.35 million nuclei from 391 brains; substantial fractions of eQTL effects were disease-
dependent in some cell types.

Use:

```text
AllelicExpressionEffect_Disease != AllelicExpressionEffect_ControlByDefinition
```

Source: https://www.nature.com/articles/s41588-024-02050-9

## S11 — Human immune epigenome is shaped by genetics and exposures

2026 Nature Genetics study **Genetics and environment distinctively shape the human immune
cell epigenome.**

Single-cell methylation/accessibility analyses identified both exposure-associated and
genotype-associated regulatory states.

Use:

```text
EpigeneticState != EnvironmentalEffectByDefinition
Epigenome receives both genetic and environmental influence
```

Source: https://www.nature.com/articles/s41588-025-02479-6

## S12 — Rare coding variants contribute nontrivial complex-trait heritability

Pathan, N. et al. (2024). **A method to estimate the contribution of rare coding variants to
complex trait heritability.** Nature Communications 15, 1245.

31 UK Biobank traits were analyzed; many showed >5% estimated rare-variant heritability under
the method, with height especially high.

Use:

```text
CommonSNPArchitecture != GeneticArchitectureTotality
Rare != NegligibleByDefinition
```

Source: https://www.nature.com/articles/s41467-024-45407-8

## S13 — Rare and common variants jointly shape developmental-disorder phenotypes

2024 Nature Genetics study **Genetic modifiers of rare variants in monogenic developmental
disorder loci.**

419,854 UK Biobank participants: rare damaging variant burden and educational-attainment PGS
showed additive modification of related phenotypes.

Use:

```text
Monogenic != PolygenicExcluded
PrimaryRareVariant != CompleteGeneticBackground
```

Source: https://www.nature.com/articles/s41588-024-01710-0

## S14 — Polygenic risk modifies penetrance of monogenic kidney disease

Khan, A. et al. (2023). **Polygenic risk alters the penetrance of monogenic kidney disease.**
Nature Communications 14, 8318.

UK Biobank and All of Us carriers of ADPKD/COL4-associated variants showed large risk
gradients by genome-wide polygenic score.

Use:

```text
PathogenicVariant != FixedOutcomeProbability
CarrierStatus != FixedRisk
```

Source: https://www.nature.com/articles/s41467-023-43878-9

## S15 — Allelic expression can alter penetrance in monogenic immune disease

2024 Nature study **Monoallelic expression can govern penetrance of inborn errors of
immunity.**

Discordant relatives carrying the same mutation showed different allele-expression patterns
associated with affected/unaffected states.

Use:

```text
Genotype != Transcriptotype != Phenotype
```

Source: https://www.nature.com/articles/s41586-024-08346-4

## S16 — Multiple genetic mechanisms modify pathogenic-variant phenotype

2025 Nature Communications study **Investigating the sources of variable impact of
pathogenic variants in monogenic metabolic conditions.**

Biobank carriers showed incomplete penetrance and variation associated with pathogenic-
variant effect, polygenic background and interaction/background mechanisms.

Use:

```text
MonogenicLabel != OneCauseOneSeverity
```

Source: https://www.nature.com/articles/s41467-025-60339-7

## S17 — Common polygenic variation contributes within rare neurodevelopmental conditions

2024 Nature study **Examining the role of common variants in rare neurodevelopmental
conditions.**

Patients, parents and controls were used to study rare diagnoses together with polygenic
background and direct/indirect common-variant effects.

Use: rare/common and direct/indirect distinctions are simultaneously necessary.

Source: https://www.nature.com/articles/s41586-024-08217-y

## S18 — Rare coding disease associations across ancestries

2024 Nature Genetics **Rare coding variant analysis for human diseases across biobanks and
ancestries.** 748,879 individuals across three biobanks and diverse ancestry backgrounds.

Use: rare-variant effect comparisons can be meaningfully cross-population, while sensitivity
analysis remains necessary.

Source: https://www.nature.com/articles/s41588-024-01894-5

## S19 — Rare noncoding variation can have large quantitative-trait effects

2024 Nature Communications **Whole-genome sequencing in 333,100 individuals reveals rare
non-coding single variant and aggregate associations with height.**

Use:

```text
CodingSequence != FunctionalVariationTotality
```

Source: https://www.nature.com/articles/s41467-024-52579-w

## S20 — Copy-number variation contributes diverse Human phenotypes

Hujoel, M. L. A. et al. (2024). **Protein-altering variants at copy number-variable regions
influence diverse human phenotypes.** Nature Genetics 56, 569–578.

Use:

```text
GeneticVariant != SNPOnly
```

Source: https://www.nature.com/articles/s41588-024-01684-z

## S21 — Tandem-repeat variation is multi-allelic and phenotype-associated

2024 Nature Communications **A phenome-wide association study of tandem repeat variation in
168,554 individuals from the UK Biobank.**

Use:

```text
VariantOntology != BiallelicSNPOnly
```

Source: https://www.nature.com/articles/s41467-024-54678-0

## S22 — De novo mutation is multi-class and includes postzygotic events

2025 Nature **Human de novo mutation rates from a four-generation pedigree reference.**

Five sequencing technologies across a 28-member four-generation pedigree estimated multiple
classes of de novo events; a fraction of SNVs were inferred postzygotic.

Use:

```text
DeNovo != ParentallyInherited
DeNovo != GermlineOnly
```

Source: https://www.nature.com/articles/s41586-025-08922-2

## S23 — Somatic mosaicism reveals distinct cellular lineages within one Human brain

Chung, C. et al. (2024). **Cell-type-resolved mosaicism reveals clonal dynamics of the human
forebrain.** Nature 629, 384–392.

Use:

```text
OneHuman != OneIdenticalGenomeAcrossEveryCell
SomaticClone != NewHumanIndividual
```

Source: https://www.nature.com/articles/s41586-024-07292-5

## S24 — Mosaic structural variants accumulate in hematopoietic cell lineages

2024 Nature Genetics **Cell-type-specific consequences of mosaic structural variants in
hematopoietic stem and progenitor cells.**

Use: somatic genomic state changes across age/tissue and can undergo clonal expansion.

Source: https://www.nature.com/articles/s41588-024-01754-2

## S25 — Mitochondrial DNA mosaicism adds another within-person genomic layer

An, J. et al. (2024). **Mitochondrial DNA mosaicism in normal human somatic cells.** Nature
Genetics.

Use:

```text
Genome != NuclearDiploidSequenceOnly
mtDNAVariation can be tissue/cell heterogeneous
```

Source: https://www.nature.com/articles/s41588-024-01838-z

## S26 — Pleiotropy is widespread across complex-trait association data

Qi, G. et al. (2024). **Genome-wide large-scale multi-trait analysis characterizes global
patterns of pleiotropy and unique trait-specific variants.** Nature Communications 15, 6985.

Use:

```text
OneVariant != OneTraitByDefinition
GeneticCorrelation/Pleiotropy != TraitIdentity
```

Source: https://www.nature.com/articles/s41467-024-51075-5

## S27 — Population-specific variants can illuminate causal mechanisms without creating
biological races

2024 Nature Genetics **Population-specific putative causal variants shape quantitative
traits.** Approximately 260,000 Japanese participants; fine-mapping identified coding,
splicing and noncoding candidates including variants rare/absent in other populations.

Use:

```text
PopulationSpecificVariant != PopulationEssence
Diverse cohorts improve mechanism discovery
```

Source: https://www.nature.com/articles/s41588-024-01913-5

## S28 — Functional editing can connect sequence variants to state-specific molecular effects

2025 Nature **Precisely defining disease variant effects in CRISPR-edited single cells.**

DNA edit identity, transcriptome and surface protein were measured in single cells; selected
variants showed state-specific functional effects.

Use:

```text
StatisticalAssociation != FunctionalValidation
FunctionalEffect_D != UniversalOrganismEffect
```

Source: https://www.nature.com/articles/s41586-025-09313-3

## S29 — Cell-state abundance itself can be genetically associated

2024 Nature Genetics **Identifying genetic variants that influence the abundance of cell
states in single-cell data.**

Use: genotype can alter phenotype through cellular-composition/state pathways rather than
only changing per-cell expression.

Source: https://www.nature.com/articles/s41588-024-01909-1

## S30 — Genetic effects on immune states are context and cell-state specific

2025 Nature Genetics **Deciphering state-dependent immune features from multi-layer omics
data at single-cell resolution.**

Use: host genetics, somatic mutations, infection state and cell type jointly structure
observed molecular phenotype.

Source: https://www.nature.com/articles/s41588-025-02266-3

---

# Evidence boundary

The ledger does **not** establish:

```text
one universal heritability number for any Human trait
one causal interpretation of every GWAS locus
one sufficient PGS for individual destiny
one discrete race partition of Human genomes
one universal eQTL effect across cell states
one monogenic/polygenic dichotomy
one guarantee of disease from pathogenic-variant status
one universal gene×environment interaction model
one complete explanation of individual differences by genetics
```

Its purpose is to constrain the HD7 cross-cutting genetics/heredity grammar and the HF24
admission decision.
