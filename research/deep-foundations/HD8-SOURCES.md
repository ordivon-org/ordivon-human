---
schema_version: 1
id: human.deep-foundations.hd8.sources
title: HD8 Evolution, Phylogeny and Human Specificity — Primary Evidence Ledger
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
updated: 2026-08-18
summary: Primary-evidence ledger for HD8 across ancient-DNA selection and demography, drift/admixture, adaptive introgression, convergent lactase-persistence evolution, malaria tradeoffs and coevolution, archaic ancestry, nonhuman social/cultural capacities, comparative primate molecular regulation and Human-specific developmental changes. The ledger constrains selection/adaptation and Human-specificity claims without turning evolution into progress, optimality or normative purpose.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.deep-foundations.hd8
---
# HD8 — Primary Evidence Ledger

## Evidence rule

HD8 prioritizes primary genomic, ancient-DNA, comparative, behavioural and functional studies
for load-bearing empirical claims. Theory terms such as adaptation, exaptation, niche
construction and multilevel selection are compared as model families; the ledger does not
pretend one experiment settles their full conceptual scope.

## S01 — Ancient DNA can recover selection signals later obscured by drift/admixture

Pandey, D. et al. (2024), **Leveraging ancient DNA to uncover signals of natural selection
in Europe lost due to admixture or drift.** Nature Communications 15, 9772.

708 ancient samples spanning ~7,000 years were analysed with multi-locus selection scans.
Some candidate signals were detectable only in earlier periods and later obscured by neutral
drift or demographic admixture.

Use:

```text
NoPresentDaySelectionSignal != NoHistoricalSelection
Drift/Admixture can erase historical signatures
```

Source: https://www.nature.com/articles/s41467-024-53852-8

## S02 — Ancient genomes separate selection from ancestry turnover

Irving-Pease, E. K. et al. (2024), **The selection landscape and genetic legacy of ancient
Eurasians.** Nature.

More than 1,600 imputed ancient genomes were used to model ancestry-specific allele-frequency
trajectories and selection across the transition to farming/pastoralism.

Use:

```text
AlleleFrequencyChange != SelectionByDefinition
AncestryAdmixture must be modeled
```

Source: https://www.nature.com/articles/s41586-023-06705-1

## S03 — Denisovan-like introgression supplied Tibetan EPAS1 adaptive variation

Huerta-Sánchez, E. et al. (2014), **Altitude adaptation in Tibetans caused by introgression
of Denisovan-like DNA.** Nature 512, 194–197.

The Tibetan EPAS1 haplotype is best explained by Denisovan/Denisovan-related introgression
rather than incomplete lineage sorting and carries a strong high-altitude selection signal.

Use:

```text
SourceOfVariation != SelectiveProcess
Introgression + later selection = adaptive introgression
```

Source: https://www.nature.com/articles/nature13408

## S04 — Admixture can itself mediate local adaptation

Jeong, C. et al. (2014), **Admixture facilitates genetic adaptations to high altitude in
Tibet.** Nature Communications 5, 3281.

Sherpa/Tibetan population-genetic analyses show high-altitude ancestry enrichment at EPAS1
and EGLN1, illustrating adaptation through migration/admixture-mediated access to variants.

Use:

```text
Adaptation != NewMutationRequired
MigrationSource != SelectionMechanism
```

Source: https://www.nature.com/articles/ncomms4281

## S05 — Lactase persistence is convergent adaptation

Tishkoff, S. A. et al. (2007), **Convergent adaptation of human lactase persistence in
Africa and Europe.** Nature Genetics 39, 31–40.

Distinct African regulatory variants on different haplotype backgrounds were associated with
adult lactase persistence and functional promoter enhancement, separate from the major
European variant.

Use:

```text
SameAdaptivePhenotype != SameMutation/History
ConvergentEvolution != HomologyOfDerivedVariant
```

Source: https://www.nature.com/articles/ng1946

## S06 — Cultural practice does not fully specify selective mechanism

Evershed, R. P. et al. (2022), **Dairying, diseases and the evolution of lactase persistence
in Europe.** Nature 608, 336–345.

~7,000 pottery fat residues, ancient allele trajectories and contemporary cohort analyses
show widespread milk use long before high lactase-persistence frequency; famine/pathogen and
demographic proxies better explained parts of the inferred selection pattern than milk-use
intensity alone.

Use:

```text
CulturePresent != SelectiveMechanismFullySpecified
CurrentBehaviorAssociation != HistoricalFitnessEffect
```

Source: https://www.nature.com/articles/s41586-022-05010-7

## S07 — Ancient genomes directly constrain timing of Neanderthal admixture

Sümer, A. P. et al. (2024), **Earliest modern human genomes constrain timing of Neanderthal
admixture.** Nature.

~45,000-year-old early modern Human genomes were used to resolve ancestry and admixture
history during temporal overlap with Neanderthals.

Use:

```text
ArchaicAncestry = historical gene flow evidence, not species-tree simplicity
```

Source: https://www.nature.com/articles/s41586-024-08420-x

## S08 — Present-day genomes retain a mosaic of archaic fragments

Skov, L. et al. (2020), **The nature of Neanderthal introgression revealed by 27,566
Icelandic genomes.** Nature.

Millions of inferred archaic fragments reveal heterogeneous Neanderthal/Denisovan-related
ancestry across present-day genomes.

Use:

```text
HumanEvolution != PureBranchingTree
LocalGenealogy != SpeciesTreeByDefinition
```

Source: https://www.nature.com/articles/s41586-020-2225-9

## S09 — Archaic immune variants can show adaptive retention

Yao, Z. et al. (2023), **Dissecting human population variation in single-cell responses to
SARS-CoV-2.** Nature.

Single-cell immune-response analyses found introgressed archaic haplotypes enriched among
some regulatory effects and highlighted retained immune loci with population-specific
frequency patterns.

Use:

```text
Introgressed != AdaptiveByDefinition
but some IntrogressedLoci can show adaptive retention
```

Source: https://www.nature.com/articles/s41586-023-06422-9

## S10 — Genome-wide archaic ancestry is not globally beneficial

McArthur, E. et al. (2021), **Quantifying the contribution of Neanderthal introgression to
the heritability of complex traits.** Nature Communications.

Detectable Neanderthal ancestry was depleted for heritability contributions across most
traits, while selected retained subsets contributed to specific phenotypic domains.

Use:

```text
AdaptiveIntrogression_D != ArchaicAncestryOverallAdaptive
```

Source: https://www.nature.com/articles/s41467-021-24582-y

## S11 — Sickle-cell protection depends on parasite genotype

Band, G. et al. (2022), **Malaria protection due to sickle haemoglobin depends on parasite
genotype.** Nature 602, 106–111.

Host HbS protection against severe malaria showed strong association with parasite-genome
variation.

Use:

```text
FitnessEffect_HostVariant != HostOnlyConstant
CoevolutionaryEnvironment matters
```

Source: https://www.nature.com/articles/s41586-021-04288-3

## S12 — Adaptive variants can show negative epistasis/tradeoffs

Williams, T. N. et al. (2005), **Negative epistasis between the malaria-protective effects
of alpha+-thalassemia and the sickle cell trait.** Nature Genetics 37, 1253–1257.

Each polymorphism protected against malaria when inherited separately, but combined
protection was reduced toward baseline.

Use:

```text
SelectedVariantEffect != ContextFreeBenefit
Adaptation != GlobalOptimality
```

Source: https://www.nature.com/articles/ng1660

## S13 — Long-term balancing selection can preserve malaria-resistance variation

Malaria Genomic Epidemiology Network (2015), **A novel locus of resistance to severe malaria
in a region of ancient balancing selection.** Nature 526, 253–257.

Large multi-centre African case–control analyses identified a severe-malaria resistance
locus near glycophorins in a region with evidence of ancient balancing selection.

Use:

```text
Selection != FixationByDefinition
BalancingSelection != DirectionalSelection
```

Source: https://www.nature.com/articles/nature15390

## S14 — Chimpanzees can socially acquire a skill they fail to innovate alone

van Leeuwen, E. J. C. et al. (2024), **Chimpanzees use social information to acquire a skill
they fail to innovate.** Nature Human Behaviour 8, 891–902.

Naive chimpanzees learned a sequential puzzle skill from trained group members after failing
to independently innovate it during prolonged prior exposure.

Use:

```text
SocialLearningBeyondIndependentInnovation != HumanUnique
TaskFailure != SpeciesIncapacity
```

Source: https://www.nature.com/articles/s41562-024-01836-5

## S15 — Bumblebees independently falsify a strong Human-only learning criterion

Bridges, A. D. et al. (2024), **Bumblebees socially learn behaviour too complex to innovate
alone.** Nature 627, 572–578.

Naive observer bees acquired a two-step task socially although extended independent exposure
failed to produce the complete behaviour.

Use:

```text
SimilarFunctionalCapacity can evolve in distant lineages
FunctionalSimilarity != SharedRecentMechanism
```

Source: https://www.nature.com/articles/s41586-024-07126-4

## S16 — Wild orangutan diet repertoires can be culturally dependent

Howard-Spink, E. et al. (2025), **Culture is critical in driving orangutan diet development
past individual potentials.** Nature Human Behaviour 10, 243–254 (2026 issue).

An empirically calibrated agent-based model using >12 years of wild Sumatran orangutan data
showed adult-like diet breadth emerged reliably by key developmental milestones only with
social-learning processes.

Use:

```text
CulturallyDependentRepertoire != HumanUniqueByDefinition
```

Source: https://www.nature.com/articles/s41562-025-02350-y

## S17 — Comparative primate brains show conservation plus Human-divergent regulation

Comparative single-cell transcriptomic analysis of human, chimpanzee, gorilla, macaque and
marmoset middle temporal gyrus identified 57 homologous cell types, broad conservation and a
smaller set of human-divergent regulatory relationships.

Use:

```text
HumanSpecificRegulation != WholeSystemDiscontinuity
Conservation + divergence can coexist
```

Source: https://www.nature.com/articles/s41559-023-02186-7

## S18 — Mammalian cortical regulatory syntax can be conserved while CREs diverge

Zemke, N. R. et al. (2023), **Conserved and divergent gene regulatory programs of the
mammalian neocortex.** Nature.

Single-cell multiomics across human, macaque, marmoset and mouse showed extensive regulatory
conservation together with lineage-specific candidate cis-regulatory elements.

Use:

```text
DerivedRegulation != EntirelyNovelSystem
HumanSpecificCRE != CompleteHumanTraitMechanism
```

Source: https://www.nature.com/articles/s41586-023-06819-6

## S19 — Human/chimp organoids expose developmental regulatory divergence

Kanton, S. et al. (2019), **Organoid single-cell genomic atlas uncovers human-specific
features of brain development.** Nature 574, 418–422.

Human, chimpanzee and macaque cerebral organoid comparisons found different developmental
timing and cell-state-specific gene-expression/chromatin-accessibility trajectories.

Use:

```text
HumanDerivedDevelopmentalState can emerge from homologous developmental systems
OrganoidEvidence != InVivoIdentityByDefinition
```

Source: https://www.nature.com/articles/s41586-019-1654-9

## S20 — Hybrid human–chimp systems separate cis/trans regulatory divergence

Agoglia, R. M. et al. (2021), **Primate cell fusion disentangles gene regulatory divergence
in neurodevelopment.** Nature.

Human–chimp tetraploid hybrid stem-cell/organoid systems allowed cis/trans regulatory effects
to be compared within shared cellular environments and identified lineage-divergent
regulatory effects.

Use:

```text
SpeciesDifference can be decomposed mechanistically
```

Source: https://www.nature.com/articles/s41586-021-03343-3

## S21 — Human-specific and ape-specific genes can act synergistically

Xing, L. et al. (2024), **Functional synergy of a human-specific and an ape-specific
metabolic regulator in human neocortex development.** Nature Communications 15, 3468.

Human-specific ARHGAP11B and ape-specific GLUD2 jointly altered metabolic/progenitor dynamics
in experimental models.

Use:

```text
EvolutionaryNovelty != NoPrecursor
DerivedComponent + OlderSystem can create derived phenotype
```

Source: https://www.nature.com/articles/s41467-024-47437-8

## S22 — Human brain molecular evolution is cell-type specific, not whole-brain novelty

Comparative single-cell analysis across primates identified broad homologous cell classes
with a subset of human-specific expression/connectivity shifts.

Use:

```text
HumanSpecific_D must declare cell type/level
```

Source: https://www.nature.com/articles/s41559-023-02186-7

## S23 — Human cortical regulatory changes can coexist with conserved syntax

Multiomic comparison across mammals found transposable elements contributed strongly to
human-specific candidate regulatory elements while regulatory syntax remained broadly
conserved.

Use:

```text
HumanSpecificChange != NoDeepHomology
```

Source: https://www.nature.com/articles/s41586-023-06819-6

## S24 — Ancient selection trajectories depend on historical ancestry backgrounds

Irving-Pease et al. reconstructed selection at LCT, FADS and HLA-related regions through
ancient ancestry-specific trajectories rather than treating current population frequencies as
one continuous lineage.

Use:

```text
PresentPopulation != UnchangedHistoricalPopulation
```

Source: https://www.nature.com/articles/s41586-023-06705-1

## S25 — Different genetic routes can converge under related cultural pressures

The African/European lactase-persistence study functionally tested different regulatory
variants that converge on adult LCT expression.

Use:

```text
ConvergentPhenotype != SharedDerivedMutation
```

Source: https://www.nature.com/articles/ng1946

---

# Evidence boundary

The evidence ledger does **not** establish:

```text
that every Human trait is an adaptation;
that selection is the dominant mechanism at every locus/time;
that drift is always dominant;
that archaic introgression was globally beneficial;
that one comparative animal capacity makes Human and nonhuman cognition identical;
that Human culture is not exceptional in scale/open-endedness;
that one human-specific molecular difference explains Human cognition;
that evolutionary function supplies moral or social purpose.
```

It supports the typed HD8 population-historical and comparative inference grammar.
