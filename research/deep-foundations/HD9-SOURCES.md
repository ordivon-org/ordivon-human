---
schema_version: 1
id: human.deep-foundations.hd9.sources
title: HD9 Organismic Systems, Health and Disease — Primary Evidence Ledger
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
summary: Primary-evidence ledger for HD9 across inflammatory heterogeneity, anatomical sepsis, human immunometabolism, organotypic vasculature, pancreas–vascular diabetes coupling, kidney cardio–kidney–metabolic proteogenomics, multimorbidity biomarkers and trajectories, longitudinal personalized setpoints, human gut physiology and controlled host–diet–microbiome interventions. The ledger constrains cross-system health/disease grammar rather than supporting one giant Body or one scalar Health model.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.deep-foundations.hd9
---
# HD9 — Primary Evidence Ledger

## Evidence rule

HD9 uses primary human observational, longitudinal, perturbational, single-cell, multi-omic
and randomized-intervention evidence for load-bearing biological claims. Clinical coding and
consensus definitions may be used as projections but do not become ontology by authority.

## S01 — Inflammation is shared yet disease/cell-state specific

Jiménez-Gracia, L. et al. (2026), **Interpretable inflammation landscape of circulating
immune cells.** Nature Medicine 32, 633–644.

More than 6.5 million PBMCs from 1,047 patients across 19 diseases were integrated. Shared
inflammatory programs coexist with disease- and cell-type-specific states.

Use:

```text
Inflammation != OneScalar
SharedInflammatoryProgram != OneDisease
```

Source: https://www.nature.com/articles/s41591-025-04126-3

## S02 — Sepsis immune state depends on anatomy and age

Ye, Q. et al. (2026), **Single-cell multi-omic landscape reveals anatomical-specific immune
features in adult and pediatric sepsis.** Nature Immunology 27, 150–165.

Multi-omic profiling of 281 adults/children with sepsis and controls found infection-source-
and age-specific immune programs plus shared plasma mediators.

Use:

```text
Sepsis != OneImmuneState
ClinicalSyndrome != MechanisticIdentity
```

Source: https://www.nature.com/articles/s41590-025-02345-x

## S03 — Immune-cell function is metabolically rewired in critical illness

**Metabolic adaptations rewire CD4+ T cells in a subset-specific manner in human critical
illness with and without sepsis.** Nature Immunology (2026 issue).

Human CD4 T-cell subsets showed distinct metabolic adaptation; Treg glycolytic flexibility
was associated with preserved suppressive phenotype and worse clinical illness.

Use:

```text
ImmuneState != IndependentOfMetabolism
CellularFitness != OrganismBenefit
```

Source: https://www.nature.com/articles/s41590-025-02390-6

## S04 — Vasculature is shared infrastructure with organotypic states

**An organotypic atlas of human vascular cells.** Nature Medicine (2024/2025).

Integrated single-cell data across 19 human organs/tissues identified shared and organotypic
vascular cell states and signaling programs.

Use:

```text
Vasculature != PassivePlumbing
SharedInfrastructure + LocalSpecialization
```

Source: https://www.nature.com/articles/s41591-024-03376-x

## S05 — Pancreatic vascular state differs by local compartment and diabetes

Craig-Schapiro, R. et al. (2025), **Single-cell atlas of human pancreatic islet and acinar
endothelial cells in health and diabetes.** Nature Communications 16, 1338.

Distinct islet/acinar endothelial programs and altered endothelial–stromal signaling in
diabetes demonstrate that endocrine disease cannot be localized to endocrine cells alone.

Use:

```text
EndocrineDisease != EndocrineCellOnlyMechanism
```

Source: https://www.nature.com/articles/s41467-024-55415-3

## S06 — Brain vascular disease is neurovascular and immune-interactive

**Single-cell atlas of the human brain vasculature across development, adulthood and disease.**
Nature (2024).

Over 600,000 cells across fetal/adult/control and five CNS pathologies showed altered vascular
states and immune-related endothelial–perivascular signaling.

Use:

```text
Neural != SeparateFromVascular/Immune
```

Source: https://www.nature.com/articles/s41586-024-07493-y

## S07 — Kidney tissue mechanisms cross cardio–kidney–metabolic traits

Hirohama, D. et al. (2025), **The proteogenomic landscape of the human kidney and
implications for cardio-kidney-metabolic health.** Nature Medicine 31, 3917–3929.

Whole-genome/RNA/proteomic analysis of 337 human kidneys prioritized tissue proteins linked to
kidney function, serum lipids, blood pressure and other CKM traits.

Use:

```text
KidneyState != KidneyOnlyConsequences
TissueState != PlasmaProxyByDefinition
```

Source: https://www.nature.com/articles/s41591-025-03872-8

## S08 — Multimorbidity biomarkers can be shared and pattern-specific

**Shared and specific blood biomarkers for multimorbidity.** Nature Medicine (2026 issue).

Longitudinal analysis of 54 biomarkers and chronic-disease patterns over 15 years found shared
and pattern-specific associations, externally validated in another aging cohort.

Use:

```text
Biomarker != DiseaseState
SharedBiomarker != OneDisease
```

Source: https://www.nature.com/articles/s41591-025-04038-2

## S09 — Disease trajectories branch over decades

Dervić, E. et al. (2024), **Unraveling cradle-to-grave disease trajectories from multilayer
comorbidity networks.** npj Digital Medicine 7, 56.

44 million Austrian inpatient records yielded many overlapping and diverging disease
trajectories spanning decades.

Use:

```text
Multimorbidity != StaticDiseaseCount
EarlyDiagnosisSet != FutureTrajectoryByDefinition
```

Source: https://www.nature.com/articles/s41746-024-01015-w

## S10 — Temporal order in multimorbidity matters

**Multiomics insight into disease trajectories of cardiometabolic diseases and cancer.**
Nature Communications (2025).

UK Biobank multistate analysis showed distinct order-dependent disease trajectories and shared/
specific multi-omic signatures across cardiometabolic disease and cancer.

Use:

```text
SameDiseasePair + DifferentOrder != SameState/PrognosisByDefinition
```

Source: https://www.nature.com/articles/s41467-025-67510-0

## S11 — Disease clusters are multi-resolution, not one natural partition

Beaney, T. et al. (2024), **Identifying multi-resolution clusters of diseases in ten million
patients with multimorbidity in primary care in England.** Communications Medicine 4, 102.

More than ten million primary-care patients and 212 diseases yielded clusters that depend on
co-occurrence/sequence representation and resolution.

Use:

```text
DiseaseCluster_D != FundamentalDiseaseKind
```

Source: https://www.nature.com/articles/s43856-024-00529-4

## S12 — Personal hematological setpoints are stable and diagnostically relevant

Foy, B. H. et al. (2025), **Haematological setpoints are a stable and patient-specific deep
phenotype.** Nature 637, 430–438.

Longitudinal routine CBC values show stable person-specific setpoints over years/decades;
individualized ranges can improve interpretation compared with one-size population intervals.

Use:

```text
PopulationReferenceRange != IndividualBaseline
NormalPopulationRange != NoMeaningfulWithinPersonChange
```

Source: https://www.nature.com/articles/s41586-024-08264-5

## S13 — Longitudinal multi-omics shows stable personal baselines plus perturbations

**Integration of molecular profiles in a longitudinal wellness profiling cohort.** Nature
Communications (2020).

Repeated proteomic, transcriptomic, metabolomic, immune and microbiome measurements showed
large between-person variation and lower within-person baseline variation, with perturbations
from lifestyle/infection.

Use:

```text
HealthyState != OnePopulationVector
```

Source: https://www.nature.com/articles/s41467-020-18148-7

## S14 — Gut physiology shapes microbiome composition/metabolism

Procházková, N. et al. (2024), **Gut physiology and environment explain variations in human
gut microbiome composition and metabolism.** Nature Microbiology 9, 3210–3225.

Nine-day deep profiling in healthy adults, including transit time and intestinal pH, showed
host physiology/environment explain important microbiome/metabolite variation.

Use:

```text
MicrobiomeState != AutonomousMicrobialProperty
FecalComposition != HostIndependentCause
```

Source: https://www.nature.com/articles/s41564-024-01856-x

## S15 — Controlled host–diet–microbiome perturbation changes energy balance

Corbin, K. D. et al. (2023), **Host-diet-gut microbiome interactions influence human energy
balance: a randomized clinical trial.** Nature Communications 14, 3161.

Randomized crossover metabolic-ward feeding under controlled intake/activity altered fecal
energy loss, microbial biomass/metabolites and enteroendocrine measures.

Use:

```text
Host × Diet × Microbiome coupling is causal in bounded energy-balance domain
```

Source: https://www.nature.com/articles/s41467-023-38778-x

## S16 — Microbial abundance alone does not determine metabolic output

**Dietary fibre directs microbial tryptophan metabolism via metabolic interactions in the gut
microbiota.** Nature Microbiology (2024).

Defined/community experiments showed substrate-dependent pathway regulation can determine
metabolite output beyond abundance of nominal metabolizing taxa.

Use:

```text
TaxonAbundance != MetabolicFlux
MicrobiomeComposition != Function
```

Source: https://www.nature.com/articles/s41564-024-01737-3

## S17 — Resistant starch trial links microbiome, bile acids, barrier/inflammation and insulin resistance

**Resistant starch intake facilitates weight loss in humans by reshaping the gut microbiota.**
Nature Metabolism (2024).

Randomized crossover supplementation in people with overweight/obesity altered weight,
insulin resistance and microbial/bile-acid signatures, with mechanistic follow-up in mice.

Use:

```text
Microbiome interventions can couple metabolic + barrier + inflammatory axes
but Human causal attribution must preserve trial/animal evidence separation
```

Source: https://www.nature.com/articles/s42255-024-00988-y

## S18 — Salt perturbation couples gut microbial/metabolite state to blood-pressure sensitivity

**Gut microbiota-derived metabolite isovalerylcarnitine modulates salt sensitivity of blood
pressure and incident hypertension: a multicenter dietary salt intervention trial.** Nature
Communications (2025).

A controlled low-/high-salt intervention in 528 participants linked microbial/metabolite
changes with salt-sensitive blood-pressure response.

Use:

```text
GutEcology ↔ Diet/Exposure ↔ CardiovascularResponse
```

Source: https://www.nature.com/articles/s41467-025-67513-x

## S19 — Atherosclerosis is vascular + immune + lipid remodeling

**Integrated single-cell atlas of human atherosclerotic plaques.** Nature Communications
(2025).

Integrated plaque single-cell data identified specialized neutrophil, macrophage, endothelial
and fibromyocyte states in advanced lesions.

Use:

```text
Atherosclerosis != LipidLevelOnly
VascularDisease != OneCellType
```

Source: https://www.nature.com/articles/s41467-025-63202-x

## S20 — Multi-organ disease state can be modeled as system-specific trajectories

**Health octo tool matches personalized health with rate of aging.** Nature Communications
(2025).

Longitudinal cohorts were modeled across multiple bodily systems; system-specific disease
severity contributed differently to global outcomes.

Use cautiously as modeling evidence:

```text
Health != OneOrgan
OneCompositeScore != Ontology
```

Source: https://www.nature.com/articles/s41467-025-58819-x

---

# Evidence boundary

The ledger does **not** establish:

```text
one universal definition of health or disease;
that every inflammatory state is pathological;
that every biomarker is causal;
that multi-omics identifies mechanism automatically;
that microbiome differences are causal by default;
that all disease is systemic;
that organ-local explanations are obsolete;
that personalized baselines replace population evidence in every use;
that multimorbidity trajectories are deterministic;
that one network/health score is a biological essence;
or that biological health determines welfare, identity or moral standing.
```
