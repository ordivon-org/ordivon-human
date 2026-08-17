---
schema_version: 1
id: human.deep-foundations.hd6.sources
title: HD6 Sex, Sexuality, Reproduction and Life-History — Primary Evidence Ledger
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
summary: Primary-evidence ledger for HD6 across differences of sex development, hormone-action dissociations, puberty and post-menarche reproductive maturation, multidimensional sexuality, genital/subjective arousal, asexual-spectrum heterogeneity, fertility/fecundability, pregnancy neuroplasticity, gestational versus parenting effects, fatherhood physiology and reproductive aging. The ledger constrains a typed cross-layer domain model rather than a one-bit sex ontology, one sexual-response cycle or one reproductive-purpose model.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.deep-foundations.hd6
---
# HD6 — Primary Evidence Ledger

## Evidence rule

HD6 uses primary clinical cohorts, longitudinal developmental studies, psychophysiology,
prospective preconception cohorts and longitudinal pregnancy/parenthood studies wherever
possible. Clinical labels and group means are evidence about declared populations and
mechanisms, not permission to infer one person's identity, capability, consent or normative
role.

The evidence is used to test **category boundaries**, not to produce a universal `sex score`
or reproductive prescription.

## S01 — Atypical genital development is phenotypically and etiologically heterogeneous

A multicenter US cohort of 92 infants with moderate-to-severe atypical genital development
recorded karyotype, diagnosis, anatomy and sex of rearing rather than treating one variable
as sufficient. Karyotypes included 46,XX, 46,XY and sex-chromosome abnormalities; diagnoses
and anatomic features varied within those groups.

Use:

```text
Karyotype != CompleteSexRelatedTraitProfile
OneObservedAnatomicFeature != Etiology
```

Source:
https://pubmed.ncbi.nlm.nih.gov/30623164/

## S02 — Complete androgen insensitivity separates chromosome profile, hormone action and phenotype

Rosa et al. (2002), **Complete androgen insensitivity syndrome caused by a novel mutation in
the ligand-binding domain of the androgen receptor: functional characterization.**

A 46,XY patient with complete androgen insensitivity had female external genitalia despite
testes and absence of a uterus, demonstrating the causal importance of receptor-mediated
androgen action.

Use:

```text
ChromosomalProfile != HormoneAction != ExternalPhenotype
HormoneLevel/Production != TissueResponse
```

Source:
https://pubmed.ncbi.nlm.nih.gov/12213902/

## S03 — DSD profiles resist one-bit reduction

The multicenter atypical-genital-development cohort demonstrates that karyotype, diagnosis,
internal structures, external anatomy and rearing classification are separately observed
coordinates in actual clinical practice.

Use: strengthens a typed profile rather than using `sex` as an explanation for the very
features used to classify it.

Source:
https://pmc.ncbi.nlm.nih.gov/articles/PMC6320240/

## S04 — Puberty is a trajectory rather than a birthday

A longitudinal study of 504 girls assessed Tanner stages every six months with hormonal and
anthropometric measures at defined pubertal milestones. Timing and endocrine profiles varied
across development.

Use:

```text
PubertalStage != ChronologicalAge
PhysicalDevelopment != OneHormoneTrajectory
```

Source:
https://pubmed.ncbi.nlm.nih.gov/32259819/

## S05 — Menstrual-cycle regularity develops after menarche

The WHO multicenter longitudinal adolescent study followed menstrual patterns for two years
and found substantial early post-menarcheal variation with increasing regularity across
cycles.

Use:

```text
Menarche != AdultCyclePattern
CycleRegularity = developmental outcome, not instantaneous switch
```

Source:
https://pubmed.ncbi.nlm.nih.gov/3721946/

## S06 — Ovulatory maturation is not identical to menarche

Zhang et al. (2008), **Onset of ovulation after menarche in girls: a longitudinal study.**
Daily urine hormones and menstrual records over two years showed progressive development of
ovulatory-appearing hormone patterns around and after menarche, with post-menarcheal luteal
patterns still differing from adult controls.

Use:

```text
Menarche != MatureOvulatoryFunction
BleedingEpisode != OvulationByDefinition
```

Source:
https://pubmed.ncbi.nlm.nih.gov/18252789/

## S07 — Adolescent reproductive endocrine maturation remains extended

Longitudinal endocrine studies following girls after menarche show continuing maturation of
gonadotropin/steroid dynamics and ovulatory frequency over subsequent years.

Use:

```text
Puberty != OneEvent
ReproductiveMaturation != MenarcheOnly
```

Sources:
- https://pubmed.ncbi.nlm.nih.gov/6798063/
- https://pubmed.ncbi.nlm.nih.gov/6231419/

## S08 — Sexual identity, attraction and behavior are not interchangeable

Fu et al. (2019), **Relationships Among Sexual Identity, Sexual Attraction, and Sexual
Behavior: Results from a Nationally Representative Probability Sample of Adults in the
United States.**

The probability sample directly measured identity, attraction and recent behavior and found
nonzero discordance, especially among younger adults, women and sexual-minority groups.

Use:

```text
SexualIdentity != SexualAttraction != SexualBehavior
```

Source:
https://pubmed.ncbi.nlm.nih.gov/30523472/

## S09 — Genital and subjective sexual arousal are distinct measures

Velten et al. (2016) measured continuous subjective arousal and vaginal photoplethysmography
and found substantial between-person variation in genital–subjective concordance, moderated
by excitation/inhibition measures.

Use:

```text
GenitalArousal != SubjectiveArousal
Concordance != FixedUniversalConstant
```

Source:
https://pubmed.ncbi.nlm.nih.gov/27379408/

## S10 — Sexual-response concordance is time- and measurement-sensitive

A concurrent thermography/plethysmography study found that the relation between self-reported
and genital responses changed over time and depended on the physiological measurement
method.

Use:

```text
SexualConcordance_D,t != OneTrait
MeasurementMethod changes inferred concordance
```

Source:
https://pubmed.ncbi.nlm.nih.gov/28919258/

## S11 — Instructions/attention can alter measured sexual-response relations

Experiments manipulating what participants attend to/report show that genital and subjective
responses and their apparent coherence depend partly on task instructions and interoceptive
awareness.

Use:

```text
ObservedArousalRelation != ContextFreeMechanismReadout
```

Sources:
- https://pubmed.ncbi.nlm.nih.gov/23841796/
- https://pubmed.ncbi.nlm.nih.gov/27789208/

## S12 — Asexuality is not zero on every sexuality dimension

Zheng & Su (2018), **Patterns of Asexuality in China: Sexual Activity, Sexual and Romantic
Attraction, and Sexual Desire.**

Asexual-spectrum participants were heterogeneous in sexual activity, solitary/dyadic desire
and romantic orientation.

Use:

```text
AsexualIdentity != ZeroSexualBehavior
AsexualIdentity != ZeroRomanticAttraction
AsexualIdentity != ZeroOfEveryDesireMeasure
```

Source:
https://pubmed.ncbi.nlm.nih.gov/29383460/

## S13 — Asexual identity, attraction and desire can change differently over time

Su & Zheng (2023) followed participants at three waves, one year apart, measuring
sexual/romantic orientation identity, attraction and desire.

Use:

```text
OrientationIdentityTrajectory != AttractionTrajectory != DesireTrajectory
```

Source:
https://pubmed.ncbi.nlm.nih.gov/35302908/

## S14 — Romantic and sexual dimensions separate within asexual populations

Carvalho & Rodrigues (2022) compared romantic and aromantic asexual adults and found
material differences in relationship histories, desire/sex-related experiences and future
relationship preferences.

Use:

```text
RomanticAttraction != SexualAttraction
RomanticRelationshipOrientation != SexualityTotality
```

Source:
https://pubmed.ncbi.nlm.nih.gov/35334025/

## S15 — Low desire without distress is not automatically disorder

Empirical work comparing asexual participants, people with clinically framed hypoactive
sexual desire disorder and people with nondistressing low desire shows distress and identity
cannot be inferred from desire magnitude alone.

Use:

```text
LowSexualDesire != DisorderByDefinition
LowDesire != AsexualIdentityByDefinition
```

Source:
https://pubmed.ncbi.nlm.nih.gov/25545124/

## S16 — Fecundability is probabilistic and age-related, not an age bit

Wesselink et al. (2017), **Age and fecundability in a North American preconception cohort
study.** 2,962 couples were followed prospectively for conception across menstrual cycles.
Female age was associated with declining per-cycle conception probability, especially at
later ages, while adjusted male-age effects were smaller in this sample.

Use:

```text
ChronologicalAge != FertilityBit
Fecundability = probability under conditions, not binary trait
```

Source:
https://pubmed.ncbi.nlm.nih.gov/28917614/

## S17 — Contemporary prospective cohort confirms age/time-to-pregnancy and miscarriage are separate outcomes

A 2025 Rotterdam prospective preconception cohort followed 3,604 women and partners and
modeled fecundability, infertility/time-to-pregnancy and miscarriage separately.

Use:

```text
Fecundability != PregnancyLossRisk
AgeEffect_D != AgeEffect_E
```

Source:
https://pubmed.ncbi.nlm.nih.gov/41250147/

## S18 — AMH trajectory can inform menopause prediction but is not an exact clock

Gohari et al. (2016) used repeated AMH measurements over an average 6.5-year follow-up and
modeled individual time-to-menopause. Rates of AMH decline varied among women and across
cycles.

Use:

```text
AMH != ExactTimeToMenopause
SingleAMHMeasurement != ReproductiveAgeTotality
```

Source:
https://pubmed.ncbi.nlm.nih.gov/27326817/

## S19 — Pregnancy is a longitudinal whole-organism/neuroplastic transition

Pritschet et al. (2024), **Neuroanatomical changes observed over the course of a human
pregnancy.** Precision imaging from preconception through pregnancy and two years postpartum
showed widespread dynamic gray/white-matter and fluid-space changes.

Use:

```text
Pregnancy != ReproductiveOutcomeLabelOnly
PregnancyState != OneHormoneMeasurement
```

Source:
https://www.nature.com/articles/s41593-024-01741-0

## S20 — Pregnancy-related brain change replicates across a small longitudinal cohort

A 2025 Communications Biology study followed ten participants during pregnancy with repeated
MRI plus salivary/hair hormones and inflammatory markers, finding structural/microstructural
change associated with endocrine trajectories.

Use: pregnancy is a dynamic multivariable state; one measurement cannot exhaust it.

Source:
https://www.nature.com/articles/s42003-024-07414-9

## S21 — Gestation and parenting effects can be experimentally separated by comparison design

A 2025 Nature Communications study followed 127 first-time gestational mothers across five
MRI sessions and included 20 non-gestational mothers plus 32 nulliparous women. This design
explicitly separates gestational factors from parenting-related factors.

Use:

```text
GestationEffects != ParentingEffects
Motherhood != Pregnancy
```

Source:
https://www.nature.com/articles/s41467-025-55830-0

## S22 — Fatherhood can alter physiology without gestation

Gettler et al. (2011), **Longitudinal evidence that fatherhood decreases testosterone in
human males.** In a representative Filipino cohort, higher baseline waking testosterone
predicted subsequent partnered fatherhood; men who became partnered fathers then showed
larger testosterone declines than men remaining single nonfathers.

Use:

```text
ParenthoodBiologicalTransition != GestationOnly
HormoneState ↔ Social/ReproductiveState
```

Source:
https://pubmed.ncbi.nlm.nih.gov/21911391/

## S23 — Hormone–behavior relations are not one-way

Follow-up work in the same broad population related longitudinal testosterone changes around
marriage/fatherhood to later sexual behavior.

Use:

```text
HormoneLevel != MatingEffort
Hormone → BehaviorOnly is insufficient
```

Source:
https://pubmed.ncbi.nlm.nih.gov/24018138/

## S24 — Pairbond/fatherhood endocrine associations vary at population level

A large Cebu cohort (n=890) measured bioavailable testosterone, plasma testosterone and LH
by pairbond/fatherhood status and emphasized population variation in these associations.

Use:

```text
FatherhoodHormoneProfile_D != UniversalFatherhoodProfile
```

Source:
https://pubmed.ncbi.nlm.nih.gov/19651129/

## S25 — Reproductive roles and social roles must be separated

The combined pregnancy/non-gestational-mother and fatherhood longitudinal evidence shows
that gestation, genetic contribution, caregiving and social parenthood can have different
biological/social pathways.

Use:

```text
GeneticParenthood != GestationalParenthood != SocialParenthood
Pregnancy != Parenthood
```

Sources:
- https://www.nature.com/articles/s41467-025-55830-0
- https://pubmed.ncbi.nlm.nih.gov/21911391/

## S26 — Measurement/domain boundary

The evidence ledger does **not** establish:

```text
one scalar biological sex variable for every question
one hormone as the cause of sexuality or identity
one universal sexual-response sequence
one fixed concordance relation between genital and subjective arousal
one deterministic puberty timeline
one fertility threshold age
one universal parenting endocrine profile
one evolutionary fitness objective as an individual Human goal
one biological coordinate as a normative or legal role
```

It supports a typed, history-sensitive cross-layer domain model.
