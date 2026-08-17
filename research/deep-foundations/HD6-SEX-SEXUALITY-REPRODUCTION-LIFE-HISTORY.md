---
schema_version: 1
id: human.deep-foundations.hd6
title: HD6 — Sex, Sexuality, Reproduction, Reproductive Development and Life-History Transitions
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
summary: Deep reconstruction of the previously sparse Human sex/sexuality/reproduction domain after HD5/HF23. HD6 first performs a global residual scan and displaces the provisional narrative route because sexuality/reproduction has lower existing coverage and higher organismic/developmental centrality. It separates sex-related trait profiles, reproductive classes and social/gender classifications; puberty and reproductive maturation; desire, attraction, orientation identity, subjective/genital arousal, behavior, consent and romantic attachment; fertility, fecundability, conception, pregnancy, birth, lactation and parenthood; genetic, gestational and social parenthood; reproductive aging and chronological aging; and evolutionary function from individual goal or normative role. HD6 pressure-tests DSD, homes across sex-development variation, post-menarcheal anovulation, asexuality, identity-attraction-behavior discordance, genital-subjective arousal dissociation, contraception/ART, pregnancy versus non-gestational parenthood, fatherhood physiology and menopause. It concludes that sex/sexuality/reproduction is a foundationally important cross-layer domain, but not one missing peer foundation: its surviving structures compose HF1/HF4/HF5/HF6/HF10/HF14/HF16/HF21/HF22 plus organism/genetic variables. HF24 is not admitted; the strongest next global residual becomes genetic variation, heredity and individual-difference architecture.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.deep-foundations.hd5.continuation
  - human.deep-foundations.hd6.sources
  - human.deep-foundations.hd6.continuation
  - human.foundations.hf1
  - human.foundations.hf4
  - human.foundations.hf5
  - human.foundations.hf6
  - human.foundations.hf10
  - human.foundations.hf14
  - human.foundations.hf16
  - human.foundations.hf21
  - human.foundations.hf22
  - human.foundations.hf23.continuation
---
# HD6 — Sex, Sexuality, Reproduction, Reproductive Development and Life-History Transitions

## 0. Residual-scan result

HD5 provisionally localized narrative/imagination as the next route, but explicitly required
a global residual scan before committing.

The scan compared:

```text
narrative / imagination / fiction
sleep / dreaming
pain / suffering
sexuality / reproduction
lifespan / death
psychopathology
collective identity
genetics / individual differences
organismic systems
```

The result is asymmetric:

```text
sleep/pain             = already deeply represented across HF2/HF5/HF14/HF15
psychopathology        = strong falsifier axis, not obviously one missing object
narrative/imagination  = genuine residual, but has interfaces in HF1/HF7/HF8/HF9/HF23
sexuality/reproduction = almost absent despite connecting body, development, motivation,
                         relationships, population and life course
genetics/variation     = also highly sparse and becomes the next likely residual
```

Therefore HD6 legitimately displaces the provisional narrative route.

```text
LocalResidualAfterHD5 != GlobalHighestPriorityResidual
```

---

# 1. Domain boundary

HD6 studies a coupled domain containing:

```text
sex development and sex-related traits
reproductive anatomy/function
puberty and reproductive maturation
sexual desire / arousal / attraction / orientation / behavior
fertility / fecundability / conception
pregnancy / birth / lactation / postpartum
parenthood transitions
reproductive aging
mating–parenting allocation and life-history tradeoffs
```

It does **not** assume these are one variable or one subsystem.

---

# 2. First firewall — sex is not sexuality

```text
SexProfile != SexualityProfile
```

Sex-related biological development and sexual desire/attraction/identity/behavior are
causally related in some models but not definitionally identical.

---

# 3. Sexuality is not reproduction

```text
Sexuality != Reproduction
```

Sexual activity can occur without conception or reproductive intention, while conception
can occur without sexual intercourse through assisted reproductive technologies.

---

# 4. Reproduction is not parenthood

```text
Reproduction != Parenthood
```

A person can contribute gametes or gestate without occupying an enduring social-parent role;
a person can parent without genetic or gestational participation.

HF22 remains social/persistent-relation owner.

---

# 5. Biological sex is not one observed bit

For a declared biological/clinical question use a typed profile rather than one universal
scalar:

```text
SexRelatedTraitProfile_D = {
  sex-chromosome complement / mosaicism when relevant,
  gonadal development,
  steroidogenic pathway,
  hormone production,
  hormone receptor/action profile,
  internal reproductive anatomy,
  external genital anatomy,
  secondary sex characteristics,
  gamete production/function,
  fertility/reproductive capability,
  developmental stage,
  uncertainty
}
```

Different questions require different coordinates.

---

# 6. Reproductive sex class is not every sex-related trait

Human sexual reproduction is organized around two gamete classes, sperm and ova, but this
does not make every sex-related trait perfectly concordant in every individual.

Therefore:

```text
ReproductiveGameteClass
!= CompleteSexRelatedTraitProfile
```

and inability to produce gametes does not erase all other sex-development properties.

---

# 7. Chromosomal sex is not gonadal sex

Differences/disorders of sex development provide direct counterexamples to treating:

```text
ChromosomeProfile = GonadalDevelopment
```

as a definitional identity.

Thus:

```text
ChromosomalProfile != GonadalProfile
```

although chromosomal/genetic pathways strongly influence gonadal development.

---

# 8. Gonadal development is not external anatomy

Androgen synthesis/action and other developmental mechanisms intervene between gonadal
state and phenotypic anatomy.

Thus:

```text
GonadalProfile != ExternalGenitalPhenotype
```

---

# 9. Hormone concentration is not hormone action

```text
HormoneLevel != HormoneAction
```

Receptor sensitivity, binding, local metabolism, developmental timing and tissue-specific
response all matter.

Androgen-insensitivity cases are a decisive falsifier of concentration-only ontology.

---

# 10. One hormone is not sex

```text
Testosterone != MaleSex
Estradiol != FemaleSex
```

Both hormone families occur in all typical Humans in differing concentrations/contexts;
sex development depends on networks, receptors, timing and tissue context.

---

# 11. Sex-related group averages are not individual identity rules

```text
GroupMeanDifference_D
!= IndividualClassification_D
```

and:

```text
GroupMeanDifference_D
!= IndividualCapability_D
```

Overlap, developmental stage and context must be preserved.

---

# 12. Biological sex profile is not gender identity

HD6 keeps separate:

```text
BiologicalSexProfile
GenderIdentity
GenderRole / SocialClassification
LegalSexCategory
```

These can interact but occupy different biological, experiential, social and institutional
roles.

HF1/HF13 remain identity/social-order owners.

---

# 13. Gender identity is not inferred from one biological coordinate

```text
Karyotype != GenderIdentity
GenitalAnatomy != GenderIdentity
HormoneLevel != GenderIdentity
```

DSD outcome heterogeneity and ordinary variation forbid deterministic inference.

---

# 14. Social category is not biological mechanism

```text
SocialSex/GenderClassification
!= ReproductiveMechanism
```

Conversely biological descriptions do not automatically determine social roles.

---

# 15. Developmental sex differentiation is a sequence, not one timestamp

A minimal developmental chain may include:

```text
genetic/chromosomal state
→ gonadal differentiation
→ hormone synthesis/action
→ internal/external reproductive development
→ later pubertal maturation
→ adult reproductive state
```

Different components can diverge.

---

# 16. Developmental sequence is not destiny totality

Prenatal differentiation does not fully determine:

```text
adult identity
sexual orientation
sexual behavior
relationship pattern
fertility
```

These require separate evidence.

---

# 17. Puberty is not chronological age

```text
PubertalStage != ChronologicalAge
```

Age predicts maturation statistically but individual timing varies.

HF6's `ChronologicalAge != AgingMechanism` generalizes naturally here.

---

# 18. Puberty is not one event

Use:

```text
PubertalDevelopmentProfile = {
  HPG-axis activation,
  adrenal maturation when relevant,
  gonadotropin dynamics,
  gonadal steroid change,
  secondary sex characteristics,
  growth/body-composition change,
  reproductive-cycle/gamete maturation,
  psychosocial context,
  uncertainty
}
```

No one marker exhausts puberty.

---

# 19. Gonadarche is not adrenarche

```text
Gonadarche != Adrenarche
```

They involve partly distinct endocrine processes and can have different timings.

HD6 does not reduce puberty to one hormone trajectory.

---

# 20. Physical staging is not endocrine state

```text
TannerStage != HormoneProfile
```

Longitudinal pubertal studies show correlated but non-identical physical/hormonal trajectories.

---

# 21. Menarche is not complete reproductive maturation

```text
Menarche != MatureOvulatoryCycleByDefinition
```

Longitudinal post-menarche data show ovulatory function can mature over time.

---

# 22. Menarche is not fertility guarantee

```text
Menarche != Fertility
```

Menstrual bleeding, ovulation, gamete quality, reproductive anatomy, partner factors and
other conditions all matter.

---

# 23. One menstrual-cycle day is not one hormonal state

```text
CycleDay != HormoneStateByDefinition
```

Hormone profiles vary both between individuals and across cycles within individuals.

---

# 24. One hormone measurement is not reproductive state

```text
SingleHormoneMeasurement != ReproductiveState
```

Sampling timing, assay, cycle phase and individual baseline matter.

---

# 25. Reproductive state is dynamic

For relevant persons/contexts:

```text
ReproductiveState_t
= f(development, endocrine dynamics, gonadal state, anatomy, health, pregnancy status,
    lactation, medication/contraception, age, history, environment)
```

No universal scalar is admitted.

---

# 26. Sexuality requires decomposition

At minimum distinguish:

```text
SexualDesire
SexualAttraction
RomanticAttraction
SubjectiveSexualArousal
Genital/PhysiologicalArousal
SexualPleasure
SexualMotivation
SexualBehavior
SexualOrientationIdentity
PartnerPreference/TargetPattern
Consent
Distress/Impairment
```

These can covary without being identical.

---

# 27. Sexual orientation is multidimensional in measurement

Population evidence directly supports:

```text
SexualIdentity
!= SexualAttraction
!= SexualBehavior
```

Discordance is empirically observed.

---

# 28. Orientation identity is not behavior history

```text
OrientationIdentity != SexualBehaviorHistory
```

Behavior can vary with opportunity, culture, coercion, experimentation, relationship and
life stage.

---

# 29. Attraction is not identity label

```text
SexualAttractionPattern != OrientationIdentity
```

Identity is a self/social classification surface, not a direct readout of every attraction.

---

# 30. Attraction is not behavior

```text
SexualAttraction != SexualBehavior
```

Attraction can exist without action; behavior can occur without corresponding attraction.

---

# 31. Desire is not attraction

```text
SexualDesire != SexualAttraction
```

Desire can be solitary/general rather than target-specific; attraction is directed toward
classes/individuals under a declared criterion.

---

# 32. Sexual attraction is not romantic attraction

```text
SexualAttraction != RomanticAttraction
```

Asexual-spectrum evidence and relationship patterns force this distinction.

---

# 33. Sexual desire is not romantic attachment

```text
SexualDesire != RomanticAttachment
```

HF22 attachment/persistent relationship state remains separate from sexual motivation.

---

# 34. Romantic relationship is not sexual relationship

```text
RomanticRelation != SexualRelation
```

Relations may contain either, both or neither depending on participants and context.

---

# 35. Sexual relationship is not pair bond by definition

```text
SexualActivity != PairBond
```

Repeated or one-time sexual behavior does not establish attachment/commitment.

---

# 36. Physiological arousal is not subjective arousal

Laboratory psychophysiology provides direct evidence for:

```text
GenitalArousal != SubjectiveArousal
```

Their concordance varies across people, sex groups, measurement modality and context.

---

# 37. Arousal concordance is not one stable person trait

```text
SexualConcordance_D,t
```

can depend on stimulus, measurement, timing, inhibition/excitation, attention and experience.

---

# 38. Desire is not arousal

```text
SexualDesire != SexualArousal
```

One can precede, follow or occur without the other depending on context/model.

HD6 does not promote one linear sexual-response cycle.

---

# 39. Arousal is not pleasure

```text
Arousal != Pleasure
```

Physiological activation does not establish positive valence or enjoyment.

HF21 valence/feeling remains separate.

---

# 40. Pleasure is not consent

```text
Pleasure != Consent
```

Consent is an authorization/decision relation, not a physiological or affective inference.

---

# 41. Arousal is not consent

A core safety firewall:

```text
GenitalArousal != Consent
SubjectiveArousal != Consent
```

No physiological response authorizes sexual action.

---

# 42. Desire is not consent

```text
Desire != Consent
```

A person can desire some sexual outcome yet refuse a particular act, partner, timing or
condition.

---

# 43. Prior behavior is not current consent

```text
PastSexualBehavior != CurrentConsent
RelationshipStatus != CurrentConsent
```

Consent is action/context/time specific.

HF10/HF14 authority boundaries apply.

---

# 44. Consent is not reproductive intention

```text
ConsentToSex != ConsentToReproduction
```

Likewise:

```text
ConsentToPregnancyAttempt != ConsentToEverySexualAct
```

Different actions/outcomes require separately typed authorization.

---

# 45. Sexual behavior is not reproduction

```text
SexualBehavior != Reproduction
```

Contraception, infertility and non-conceptive sexual activity falsify their identity.

---

# 46. Reproduction does not require sexual intercourse

Assisted reproductive technologies make:

```text
Conception != SexualIntercourseByDefinition
```

operationally undeniable.

---

# 47. Reproductive intention is not reproductive outcome

```text
IntentionToConceive != Conception
IntentionToAvoidPregnancy != NoPregnancyByDefinition
```

HF10 decision/outcome separation applies.

---

# 48. Fertility is not conception event

Use carefully:

```text
Fertility / ReproductiveCapability
!= ConceptionEvent
```

A person/couple can have reproductive capability without conceiving in a given interval.

---

# 49. Fecundability is not fertility totality

Use:

```text
Fecundability_D
= probability/rate of conception per declared exposure/time unit under conditions D
```

Therefore:

```text
Fecundability != BinaryFertilityTrait
```

---

# 50. Infertility is not sterility

```text
InfertilityCriterion_D != AbsoluteSterility
```

Clinical/time-window definitions and residual probability matter.

---

# 51. Conception is not pregnancy continuation

```text
Conception != OngoingPregnancy
```

Implantation and pregnancy loss separate stages.

---

# 52. Pregnancy is not live birth

```text
Pregnancy != LiveBirth
```

Pregnancy can end through miscarriage, stillbirth, termination or birth under different
clinical definitions.

---

# 53. Live birth is not parenthood totality

```text
LiveBirth != SocialParenthood
```

HF22 relation formation and institutional context remain separate.

---

# 54. Reproduction is multi-participant and pathway-relative

Potential roles include:

```text
gamete contributor
embryo/fetal genetic contributor
gestational carrier
birth parent
legal parent
social/caregiving parent
```

These roles can coincide or diverge.

---

# 55. Genetic parenthood is not gestational parenthood

```text
GeneticParenthood != GestationalParenthood
```

Donor-gamete and gestational-surrogacy pathways make the distinction explicit.

---

# 56. Gestational parenthood is not social parenthood

```text
GestationalParenthood != SocialParenthood
```

A gestational role does not define future caregiving relation.

---

# 57. Genetic parenthood is not social parenthood

HF22 already implies:

```text
GeneticRelatedness != Family/SocialKinship
```

HD6 applies the same firewall to parenthood.

---

# 58. Pregnancy is a major organismic state transition

Longitudinal Human imaging shows pregnancy accompanies large endocrine, physiological and
neuroplastic changes.

Thus:

```text
Pregnancy != ReproductiveOutcomeLabelOnly
```

It is a dynamic whole-organism state trajectory.

---

# 59. Pregnancy state is not one hormone level

```text
PregnancyState != ProgesteroneLevel
PregnancyState != EstradiolLevel
```

Multiple endocrine, immune, cardiovascular, metabolic and anatomical changes co-occur.

---

# 60. Pregnancy changes are not all motherhood effects

Studies comparing gestational mothers, non-gestational mothers and nulliparous controls
support separating:

```text
GestationEffects
ParentingEffects
```

rather than treating every maternal change as pregnancy-driven.

---

# 61. Motherhood is not pregnancy

```text
Motherhood/SocialMotherhood != Pregnancy
```

Non-gestational mothers and adoptive mothers are decisive boundary cases.

---

# 62. Fatherhood is not genetic contribution only

```text
Fatherhood_D != SpermContributionByDefinition
```

Social/legal/relational definitions vary; caregiving can occur with or without genetic
relatedness.

---

# 63. Parenthood can alter physiology without gestation

Longitudinal fatherhood studies show changes in testosterone and other hormones around
fatherhood/caregiving.

Therefore:

```text
BiologicalTransitionAroundParenthood
!= GestationOnly
```

---

# 64. Hormonal change is bidirectional with social behavior

In Human fathers, baseline testosterone can predict later partnering/fatherhood while
fatherhood/caregiving predicts subsequent declines.

Thus:

```text
Hormone → BehaviorOnly
```

is insufficient.

Use:

```text
HormoneState ↔ Social/ReproductiveState
```

under typed context.

---

# 65. Testosterone is not mating effort

```text
Testosterone != MatingEffort
```

It is one physiological variable associated with multiple processes and context-dependent
behaviors.

---

# 66. Testosterone is not masculinity

```text
TestosteroneLevel != MasculinityTotality
```

Social identity, morphology, behavior and hormone state are separate coordinates.

---

# 67. Parenthood is not one endocrine profile

Different cultural/ecological caregiving patterns can produce different hormone–behavior
relations.

```text
ParenthoodHormoneProfile_D != ParenthoodHormoneProfile_E
```

---

# 68. Pair bonding is not reproduction

```text
PairBond != Reproduction
```

Pair bonds can exist without children; reproduction can occur without durable pair bonds.

HF22 remains relationship owner.

---

# 69. Pair bonding is not marriage

```text
PairBond != LegalMarriage
```

HF13 institutional status and HF22 relationship state must remain distinct.

---

# 70. Reproductive behavior is institutionally mediated

Contraception, marriage law, healthcare access, assisted reproduction, adoption, parental
leave and inheritance systems can alter:

```text
options
costs
risks
timing
parental roles
```

Thus reproduction is Human×Institution, not biology alone.

---

# 71. Technology can decouple historically correlated processes

Modern technology makes separations operational:

```text
sex without conception
conception without intercourse
genetic parenthood without gestation
gestation without genetic parenthood
parenthood without biological reproduction
```

These are not edge cases to discard; they reveal ontology.

---

# 72. Contraception is not absence of sexuality

```text
ContraceptionUse != LowSexualityByDefinition
```

It modifies conception probability/intention pathways, not the definition of desire or
sexual activity.

---

# 73. Infertility is not absence of sexuality

```text
Infertility != Asexuality
```

Reproductive capability and attraction/desire/behavior are different dimensions.

---

# 74. Asexuality is not infertility

```text
Asexuality != Infertility
```

Asexual-spectrum identity/attraction patterns concern sexuality, not reproductive anatomy
or gamete function by definition.

---

# 75. Asexuality is heterogeneous

Primary studies show variation in:

```text
sexual desire
romantic attraction
sexual behavior
relationship status
```

among asexual-spectrum participants.

Therefore:

```text
AsexualIdentity != ZeroOfEverySexualVariable
```

---

# 76. Low desire is not pathology by definition

```text
LowSexualDesire != DisorderByDefinition
```

Distress/impairment and context matter.

HD6 avoids medicalizing identity or low-frequency sexual behavior without declared clinical
criteria.

---

# 77. Sexual behavior frequency is not sexual well-being

```text
MoreSex != BetterWellBeingByDefinition
```

Well-being is person/value/context relative and HF14 remains normative owner.

---

# 78. Reproductive success is not welfare

```text
MoreOffspring != GreaterWelfareByDefinition
```

Evolutionary fitness and individual well-being are different objectives.

---

# 79. Evolutionary function is not current individual goal

A crucial firewall:

```text
EvolutionaryFunction_D
!= CurrentHumanGoal
```

The existence of a reproductive evolutionary function does not imply a person wants
children, sex, partnership or pregnancy.

---

# 80. Evolutionary fitness is not normative value

```text
Fitness != MoralWorth
Fitness != HumanValue
Fitness != SocialDuty
```

HF14/HF15 remain normative/standing owners.

---

# 81. Life-history tradeoffs are model families, not moral prescriptions

Models can study allocation among:

```text
growth
maintenance
mating
parenting
survival
```

without implying that people ought to maximize reproductive output.

---

# 82. Mating versus parenting is not a universal zero-sum law

```text
MoreParentingEffort != LessMatingEffortByDefinition
```

Tradeoffs are resource/context/time dependent and can be weak or reversed in some settings.

---

# 83. Human life history is culturally mediated

Education, work, contraception, institutions, kin support, healthcare and technology alter
reproductive timing and parental investment.

Thus:

```text
BiologicalLifeHistory != CultureFreeTrajectory
```

---

# 84. Puberty is not adulthood

```text
Puberty != AdultSocialStatus
```

Biological reproductive maturation does not assign legal/social authority.

HF13/HF14 remain authority owners.

---

# 85. Reproductive capability is not consent capacity

```text
ReproductiveCapability != ConsentCapacity
```

Biological maturation cannot substitute for legal/developmental/decision-capacity criteria.

---

# 86. Fertility is age-related but probabilistic

Prospective preconception cohorts show fecundability changes with age, especially later
female reproductive age, but not as a deterministic age threshold.

Thus:

```text
Age != FertilityBit
```

---

# 87. Chronological age is not reproductive age

```text
ChronologicalAge != ReproductiveAge/State
```

Individuals of the same chronological age vary in ovarian reserve, cycle state, sperm
parameters and health/context.

---

# 88. Ovarian reserve is not fertility totality

```text
OvarianReserve != Fertility
```

Fertility additionally depends on ovulation, tubes/uterus, gamete quality, partner factors,
intercourse/ART timing and more.

---

# 89. AMH is not a reproductive clock

```text
AMH != ExactTimeToMenopause
```

Longitudinal studies show association/predictive value but substantial uncertainty and
model-dependent performance.

---

# 90. Menopause is not chronological aging

```text
Menopause != AgingTotality
```

It is a reproductive endocrine transition embedded within broader aging.

---

# 91. Menopause is not loss of sexuality

```text
Menopause != Asexuality
Menopause != EndOfSexualDesireByDefinition
```

Reproductive function and sexuality remain distinct.

---

# 92. Menopause is not loss of person capability totality

```text
Menopause != CapabilityLossTotality
```

No reproductive transition licenses assumptions about cognitive, social or moral status.

---

# 93. Male and female reproductive aging are not one symmetric process

```text
ReproductiveAging_Male
!= ReproductiveAging_Female
```

Mechanisms, timing and probability changes differ.

No one `reproductive age` scalar applies universally.

---

# 94. Reproductive transitions can reshape other systems

Pregnancy, puberty and menopause can interact with:

```text
metabolism
immune state
cardiovascular state
sleep
affect
brain plasticity
```

Therefore HD6 connects back to HF5/HF6/HF21 rather than isolating reproduction.

---

# 95. But reproductive state does not explain all simultaneous change

```text
ConcurrentChange != ReproductiveCauseByDefinition
```

Age, environment, stress, social transition and treatment can confound/mediate observed
associations.

---

# 96. Sex differences in disease are not one hormone effect

```text
SexDifference_Disease_D
!= OneSexHormoneEffect
```

Chromosomal, hormonal, anatomical, reproductive, behavioral and social exposures can
contribute.

---

# 97. Population sex difference does not define individual treatment

```text
PopulationSexDifference
!= IndividualClinicalDecisionByDefinition
```

Individual evidence/condition remains required.

---

# 98. Sexual/reproductive data are highly privacy-sensitive

HD6 marks as sensitive:

```text
sexual orientation/identity
sexual behavior
fertility/infertility
pregnancy status
contraception
reproductive health
genetic parentage
DSD/intersex-related data
```

Description does not imply authorization to collect/use them.

---

# 99. Prediction does not confer reproductive authority

```text
PredictPregnancy/Fertility/Orientation
!= AuthorityToActOnPerson
```

HF0/HF14 authority firewalls apply.

---

# 100. Reproductive risk score is not destiny

```text
RiskEstimate_D != IndividualOutcome
```

Probability, uncertainty and intervention/context remain explicit.

---

# 101. Sexual orientation prediction is not identity determination

```text
ModelPredictionOfOrientation != PersonIdentity
```

A model cannot overwrite first-person identity or authorize differential treatment.

---

# 102. Sexual physiological measurement is not desire inference totality

```text
GenitalResponseMeasure != Desire
```

and not:

```text
GenitalResponseMeasure != Consent
```

This is both scientific and safety-critical.

---

# 103. Reproductive anatomy is not relationship role

```text
Anatomy != PartnerRole
Anatomy != ParentRole
```

Social roles are relational/institutional and remain HF22/HF13 concerns.

---

# 104. Reproductive capacity is not gender role

```text
CanGestate != WomanRoleByDefinition
CanProduceSperm != ManRoleByDefinition
```

Biological capability and social classification must not be fused.

---

# 105. Medical intervention changes state, not identity by definition

Hormonal/surgical/reproductive interventions can change anatomy, hormone state or fertility.

But:

```text
ChangedBiologicalState != ChangedPersonalIdentityByDefinition
```

HF1 identity criteria remain typed.

---

# 106. Sexual/reproductive state is history-dependent

```text
State_t
depends on
prenatal development + puberty + prior pregnancies + treatments + age + health + social context
```

HD6 therefore consumes HF6 history-dependent change.

---

# 107. Pregnancy history can have persistent effects

Repeated/previous pregnancy can alter later physiology/neurobiology.

Thus:

```text
PostPregnancyState != PrePregnancyStateByDefinition
```

for some endpoints and time horizons.

---

# 108. Parenthood history is not only biological history

```text
ParenthoodHistory
```

can alter time allocation, relationships, stress, identity and physiology without gestation.

This is a cross-HF process.

---

# 109. Reproductive system is not sexuality system

Even if endocrine pathways interact:

```text
ReproductivePhysiology
!= SexualityTotality
```

This prevents one giant `sexual/reproductive system` box.

---

# 110. Sexuality is not one biological subsystem either

Sexuality spans:

```text
motivation
perception
valence
identity
social relation
behavior
norm/institution
```

Thus:

```text
Sexuality != OneOrganSubsystem
```

---

# 111. Reproduction is not one social process either

Conception, gestation and gametogenesis are biological processes even though social
institutions strongly shape access/timing/meaning.

Thus:

```text
Reproduction != SocialConstructionTotality
```

---

# 112. Competing model F1 — one-bit biological sex

Core:

```text
Sex ∈ {male,female}
```

as one exhaustive variable for every biological question.

Strength:

```text
captures two-gamete reproductive-class distinction in many contexts
```

Failure:

```text
DSD/mosaicism/hormone-action/anatomical/fertility dissociations show one bit cannot encode
all sex-related biological traits
```

Disposition: **retain question-specific reproductive class; reject one-bit total profile**.

---

# 113. F2 — chromosomal determinism

Core:

```text
XX → all female-typical traits
XY → all male-typical traits
```

Failure: androgen-insensitivity, CAH, gonadal-development variation and mosaicism.

Disposition: **reject total determinism; retain strong developmental causal role**.

---

# 114. F3 — hormone-determinist sexuality

Core:

```text
one sex hormone level → desire/orientation/identity/behavior
```

Failure: multidimensional sexuality, within-group variability, context and receptor/action
complexity.

Disposition: **reject single-hormone ontology**.

---

# 115. F4 — linear sexual response cycle

Classic family:

```text
desire → arousal → orgasm → resolution
```

Strength: useful in some episodes/tasks.

Failure: desire/arousal ordering and concordance vary; responsive/contextual desire models
capture other trajectories.

Disposition: **retain as one episode model, not universal sequence**.

---

# 116. F5 — multidimensional sexuality model

Core:

```text
identity + attraction + desire + arousal + behavior + romanticity + context
```

Strength: survives population discordance and asexual-spectrum heterogeneity.

Limit: dimensions still require mechanistic explanation.

Disposition: **retain as minimum descriptive architecture**.

---

# 117. F6 — reproduction-as-sex model

Core:

```text
sexual behavior = reproduction pathway
```

Failure: contraception, non-conceptive sex, infertility and ART.

Disposition: **reject identity**.

---

# 118. F7 — pregnancy-as-parenthood model

Failure: non-gestational/social parents, adoption, donor/gestational pathways and fatherhood
physiology.

Disposition: **reject; type parent roles**.

---

# 119. F8 — endocrine life-history tradeoff model

Core:

```text
endocrine state helps allocate mating/parenting effort
```

Strength: longitudinal fatherhood/testosterone evidence.

Limit: associations vary across ecology/culture and do not make hormones direct motives.

Disposition: **retain question-relative causal model**.

---

# 120. F9 — reproductive aging as chronological age

Failure: ovarian reserve trajectories and individual fecundability variability.

Disposition: **retain age as predictor; reject age=state**.

---

# 121. F10 — pure biological reduction

Core:

```text
sexuality/reproduction fully explained by physiology
```

Failure: identity, consent, institutions, technology, relationships, cultural meaning.

Disposition: **reject total reduction**.

---

# 122. F11 — pure social construction totality

Core:

```text
sex/reproduction are only social categories
```

Failure: gametogenesis, pregnancy, endocrine maturation, anatomy and fertility have material
biological mechanisms.

Disposition: **reject total reduction; retain social mediation/classification layers**.

---

# 123. F12 — technological decoupling model

Core:

```text
technology changes coupling among sex, conception, genetics, gestation and parenting
```

Strength: contraception and ART make previously tight correlations separable.

Limit: technology does not erase underlying biology.

Disposition: **retain Human×Technology bridge**.

---

# 124. F13 — developmental/life-course model

Core:

```text
sex/reproductive state is a trajectory across prenatal development, puberty, adulthood,
pregnancy/parenthood and reproductive aging
```

Strength: fits longitudinal evidence and state transitions.

Limit: no universal trajectory applies to every person.

Disposition: **retain typed trajectory family**.

---

# 125. Cross-context falsifier matrix

| ID | Case | Collapse attacked | Surviving distinction |
|---|---|---|---|
| R01 | complete androgen insensitivity | XY = male-typical anatomy | chromosome != hormone action != phenotype |
| R02 | 46,XX CAH virilization | XX = female-typical external anatomy | chromosome != androgen exposure/action != anatomy |
| R03 | DSD multicenter phenotypic heterogeneity | sex = one observed bit | trait profile needed |
| R04 | pubertal hormone/physical trajectories | puberty = birthday | stage != chronological age |
| R05 | post-menarche anovulatory maturation | menarche = mature fertility | bleeding milestone != ovulatory maturity |
| R06 | menstrual hormone variability | cycle day = hormonal state | direct state evidence/uncertainty required |
| R07 | national identity-attraction-behavior survey | orientation = identity label | dimensions can discord |
| R08 | asexual-spectrum heterogeneity | asexual = zero sexuality variables | attraction/desire/behavior/romanticity separate |
| R09 | genital vs subjective arousal | body response = felt arousal | physiological != subjective |
| R10 | sexual activity with contraception | sex = conception | behavior != reproduction |
| R11 | ART conception | conception requires intercourse | conception pathway != sexual act |
| R12 | infertility with sexual desire/activity | fertility = sexuality | reproductive capability != sexuality |
| R13 | donor gamete | genetic parent = social/gestational parent | roles separate |
| R14 | gestational carrier | gestation = genetic parenthood | roles separate |
| R15 | adoption | parenthood = biological reproduction | social parenthood independent |
| R16 | gestational vs non-gestational mothers | motherhood effect = pregnancy effect | gestation vs parenting separated |
| R17 | longitudinal pregnancy MRI | pregnancy = outcome label | whole-organism transition |
| R18 | fatherhood testosterone decline | parent biology = gestation only | caregiving/social transition affects physiology |
| R19 | high pre-fatherhood T predicts later fatherhood | hormones only downstream | bidirectional selection/change |
| R20 | parenthood without pair bond | pair bond = reproduction | relation and reproduction separate |
| R21 | pair bond without children | pair bond = parenting | relationship != parenthood |
| R22 | age-fecundability cohort | fertility = age threshold | probabilistic age effect |
| R23 | same age, different AMH trajectories | chronological = reproductive age | state varies among same-age persons |
| R24 | menopause | reproductive transition = global aging | domain-specific aging |
| R25 | postmenopausal sexuality | menopause = asexuality | fertility/reproductive state != sexuality |
| R26 | physiologic arousal without consent | arousal = authorization | consent independent |
| R27 | desire without action | desire = behavior | motivation vs execution |
| R28 | romantic attraction without sexual attraction | romance = sexuality | affective/relationship dimensions separate |
| R29 | sexual behavior without romantic attachment | sex = pair bond | action != persistent relation |
| R30 | same social gender, varied biology | gender category = sex profile | social vs biological projections |
| R31 | same biological coordinate, varied identity | biology = identity | identity not deterministic readout |
| R32 | hormone therapy/surgery changes body state | biological change = identity change | state and identity typed separately |
| R33 | DSD person with infertility | reproductive capability = sex identity | function != identity |
| R34 | reproductive technology changes parent roles | parent = one biological relation | parenthood is typed relation bundle |
| R35 | cultural variation in paternal caregiving | fatherhood hormone law universal | ecology/care mediate relation |
| R36 | pregnancy history | state returns fully to baseline | persistent endpoint-specific change possible |

---

# 126. Minimum sex-related biological profile

For biological/clinical questions:

```text
SexBiologyProfile_D = {
  chromosomal/genomic sex-related coordinates,
  gonadal structure/function,
  steroidogenic pathways,
  hormone levels and timing,
  receptor/action sensitivity,
  internal reproductive anatomy,
  external genital anatomy,
  secondary sex traits,
  gametogenic function,
  fertility/reproductive capability,
  developmental/reproductive stage,
  interventions/history,
  uncertainty
}
```

Do not collect coordinates irrelevant to the question.

---

# 127. Minimum sexuality profile

```text
SexualityProfile_D = {
  sexual desire,
  sexual attraction/target pattern,
  romantic attraction if relevant,
  orientation identity if relevant,
  subjective arousal,
  physiological arousal if measured,
  pleasure/valence,
  behavior history/current behavior,
  consent/authorization for the specific act,
  relationship context,
  distress/impairment if clinically relevant,
  cultural/institutional context,
  uncertainty/privacy boundary
}
```

This is not a mandatory user schema.

---

# 128. Minimum reproduction profile

```text
ReproductionProfile_D = {
  reproductive intention,
  fertility/fecundability conditions,
  gamete source/function,
  conception pathway,
  gestational state/carrier,
  pregnancy course/outcome,
  birth/parturition,
  lactation if relevant,
  genetic parent relations,
  gestational parent relation,
  legal/social parent relations,
  care structure,
  reproductive aging state,
  technology/institutional supports,
  uncertainty
}
```

---

# 129. Minimum reproductive life-course loop

```text
Developmental biology / genetics
        ↓
Sex-related trait development
        ↓
Pubertal/reproductive maturation
        ↓
Dynamic reproductive + sexual state
        ↕
Relationships / institutions / technology / goals
        ↓
Sexual behavior and/or reproductive decisions
        ↓
Conception / nonconception / ART / pregnancy / parenting pathways
        ↓
Physiological + social + relational state change
        ↓
Later reproductive aging / future options
        ↺
```

No arrow is inevitable.

---

# 130. Reconnection to HF1

HF1 owns body/organism/person/identity distinctions.

HD6 adds a typed domain application:

```text
SexBiologyProfile != PersonalIdentityTotality
```

No HF1 reopening is required.

---

# 131. Reconnection to HF4

HF4 owns motivation/value/reward.

Sexual desire is one motivational domain, not a new motivation ontology.

```text
SexualDesire_D
is an HF4-domain state
```

but not reducible to generic `wanting` without target/context qualifiers.

---

# 132. Reconnection to HF5

HF5 owns organismic regulation/endocrine state.

Reproductive endocrine dynamics are a domain-specific regulatory system:

```text
HF5 Regulation
× reproductive organs/hormones
→ ReproductiveState
```

Adding an entire reproductive system to HF5 would overgrow the general foundation.

---

# 133. Reconnection to HF6

HF6 owns development/aging/plasticity.

Puberty, pregnancy history and reproductive aging are domain-specific trajectories:

```text
HF6 ChangeDynamics
× reproductive state variables
→ ReproductiveLifeCourse
```

---

# 134. Reconnection to HF10

Reproductive decisions require:

```text
option generation
risk/uncertainty
commitment
reversibility
information search
```

But:

```text
ReproductiveDecision != ReproductiveOutcome
```

HF10 remains decision owner.

---

# 135. Reconnection to HF14

Consent, reproductive autonomy, harm/welfare and fairness are normative/authority questions.

HD6 provides descriptive state only.

```text
BiologicalFunction != NormativeDuty
```

HF14 remains authority owner.

---

# 136. Reconnection to HF16

HF16 owns population/future-generation aggregation.

HD6 provides individual/couple reproductive mechanisms that can aggregate into demography.

```text
IndividualReproductiveProcess
!= PopulationFertilityRate
```

Aggregation is not identity.

---

# 137. Reconnection to HF21

Sexual arousal/pleasure and reproductive transitions interact with affect.

But:

```text
SexualArousal != EmotionCategory
```

and pregnancy/postpartum affective changes remain domain/context specific.

---

# 138. Reconnection to HF22

HF22 owns persistent relationships, attachment and care.

HD6 adds:

```text
SexualRelation != PersistentRelationship
ParenthoodRole may create/modify PersistentRelationship
```

but does not redefine attachment.

---

# 139. Reconnection to HF13/HF19

Institutions and economic organization shape reproduction through:

```text
law
healthcare
work
leave
inheritance
childcare
ART access
```

but these remain institutional/resource mechanisms rather than biological sex variables.

---

# 140. Reconnection to HD4

Sexual/reproductive norms and family forms can be culturally transmitted.

But:

```text
CulturalTransmission != ReproductiveBiology
```

HD4 owns cultural dynamics; HD6 supplies domain content.

---

# 141. Reconnection to HF23

Language supplies labels/categories such as sex, gender, orientation, parent and family.

But:

```text
HasLabel != BiologicalKindComplete
```

HF23 explains why inherited symbolic categories can compress heterogeneous mechanisms.

---

# 142. Foundation candidate A — `Biological Sex` HF24

Audit:

```text
Repeated residual?               yes
Scientifically deep?             yes
Clean neighboring object?        weak
Already representable?           largely as typed HF1/HF5 biological projection
Risk of one-bit essentialism?    high
```

A standalone `Biological Sex` foundation would either become a profile of many organismic
variables or incorrectly collapse them.

Disposition:

```text
Reject standalone BiologicalSex HF24.
```

---

# 143. Candidate B — `Sexuality` HF24

Audit:

```text
Repeated residual?              yes
But one object?                  no
```

Surviving dimensions distribute across:

```text
HF4 motivation
HF21 affect/arousal
HF1 identity
HF10 action/consent decision
HF22 relationships
HF13 norms/institutions
```

Disposition:

```text
Reject standalone Sexuality HF24.
```

---

# 144. Candidate C — `Reproductive State / Life History` HF24

This is stronger.

It captures:

```text
puberty
fertility
pregnancy
postpartum
reproductive aging
```

But the mechanism is domain-specific composition of:

```text
HF5 regulation
HF6 development/aging
organ anatomy/physiology
HF10 decisions
HF22 parent relations
HF16 demographic aggregation
```

Creating a peer HF here would set a precedent for separate immune, cardiovascular,
respiratory and metabolic foundations without a scale/object reason.

Disposition:

```text
Reject peer HF24; retain HD6 as cross-layer domain owner.
```

---

# 145. Candidate D — unified `Sex / Sexuality / Reproduction` HF24

Fails strongest.

The entire HD6 falsifier set demonstrates:

```text
SexProfile != Sexuality != Reproduction != Parenthood
```

Therefore one giant foundation would encode exactly the category collapses the research was
meant to remove.

Disposition: **reject**.

---

# 146. HD6 foundation decision

```text
NextFoundationAdmissionCondition(HF24) = false
FoundationReopenCondition(HF0–HF23) = false
```

The no-promotion reason differs from HD4:

```text
HD4: culture is a population-historical cross-foundation process
HD6: sex/sexuality/reproduction is a cross-layer biological-psychological-social domain
```

Both are deeply important without requiring peer-foundation promotion.

---

# 147. Deep importance again does not imply peer ontology

HD6 reinforces:

```text
DeepImportance != FoundationAdmission
DomainBreadth != OneFoundationalObject
```

A deep route can become the canonical domain owner while HF remains thin.

---

# 148. Reopen audit

No existing foundation is contradicted:

```text
A repeated category error caused by frozen claim?        false
B strong evidence contradicts frozen claim?              false
C missing neighboring peer object?                       false after decomposition
D contradiction across frozen rounds?                    false
E consumer failure caused by foundation wording?         false
F normative authority leak?                              false
```

HD6 primarily fills mechanism depth between already-correct abstractions.

---

# 149. HD6 canonical consumption grammar

For sex/sexuality/reproduction questions assemble only needed layers:

```text
identity/body/person        → HF1
motivation/desire           → HF4
regulation/endocrine state  → HF5
development/aging           → HF6
decision/consent            → HF10
normative autonomy/harm     → HF14
population aggregation      → HF16
affect/arousal/valence      → HF21
relationships/parent care   → HF22
symbolic categories         → HF23
sex/reproductive domain     → HD6
```

Do not invent one `SexualState` scalar.

---

# 150. Strongest residual exposed by HD6

HD6 repeatedly depends on variables that current Human still lacks in depth:

```text
genotype / variants
sex chromosomes
gene regulation
heritability
family resemblance
gene × environment interaction
developmental canalization
polygenic architecture
rare variants
population genetic structure
individual differences
```

HD0 already marked `Genetics / individual differences` as sparse with high falsifier
leverage, and HD6 now requires it directly for sex development, puberty timing, fertility and
variation.

This is a stronger next global residual than narrative.

---

# 151. Next deep route

Admit only as non-foundation research:

```text
HD7 — Genetic Variation, Heredity, Gene–Environment Development and Individual Differences
```

with explicit guard:

```text
HD7 != HF24
HF24 = UNKNOWN
```

No foundation number is advanced.

---

# 152. HD7 starting guard

Do not assume:

```text
Gene = Trait
GeneticAssociation = IndividualCause
Heritable = Immutable
Heritable = GeneticOnly
HighHeritability = LowEnvironmentalInfluence
PolygenicScore = Destiny
PopulationAlleleFrequency = IndividualIdentity
Ancestry = Race
FamilyResemblance = GeneticCauseOnly
TwinEstimate = UniversalConstant
GeneExpression = DNASequenceOnly
Epigenetic = NonGeneticEverything
SexChromosome = CompleteSexProfile
GeneticRisk = Disease
```

---

# 153. HD6 durable firewalls

```text
LocalResidualAfterHD5 != GlobalHighestPriorityResidual

SexProfile != SexualityProfile
Sexuality != Reproduction
Reproduction != Parenthood
ReproductiveGameteClass != CompleteSexRelatedTraitProfile
ChromosomalProfile != GonadalProfile
GonadalProfile != ExternalGenitalPhenotype
HormoneLevel != HormoneAction
OneHormone != Sex
GroupMeanDifference != IndividualClassification/Capability
BiologicalSexProfile != GenderIdentity != GenderRole != LegalSexCategory
Karyotype != GenderIdentity
SocialClassification != ReproductiveMechanism

PubertalStage != ChronologicalAge
Puberty != OneEvent
Gonadarche != Adrenarche
TannerStage != HormoneProfile
Menarche != MatureOvulatoryCycle
Menarche != Fertility
CycleDay != HormoneState
SingleHormoneMeasurement != ReproductiveState

SexualIdentity != SexualAttraction != SexualBehavior
SexualDesire != SexualAttraction
SexualAttraction != RomanticAttraction
SexualDesire != RomanticAttachment
RomanticRelation != SexualRelation
SexualActivity != PairBond
GenitalArousal != SubjectiveArousal
Desire != Arousal
Arousal != Pleasure
Pleasure != Consent
Genital/SubjectiveArousal != Consent
Desire != Consent
PastBehavior != CurrentConsent
RelationshipStatus != CurrentConsent
ConsentToSex != ConsentToReproduction

SexualBehavior != Reproduction
Conception != SexualIntercourse
ReproductiveIntention != ReproductiveOutcome
Fecundability != BinaryFertilityTrait
Infertility != Sterility
Conception != OngoingPregnancy
Pregnancy != LiveBirth
LiveBirth != SocialParenthood
GeneticParenthood != GestationalParenthood != SocialParenthood
Pregnancy != Parenthood
Motherhood != Pregnancy
ParenthoodTransition != GestationOnly

HormoneState ↔ Social/ReproductiveState
Testosterone != MatingEffort
Testosterone != MasculinityTotality
PairBond != Reproduction
PairBond != Marriage
ContraceptionUse != LowSexuality
Infertility != Asexuality
Asexuality != Infertility
AsexualIdentity != ZeroOfEverySexualVariable
LowSexualDesire != DisorderByDefinition
MoreSex != BetterWellBeing
MoreOffspring != GreaterWelfare
EvolutionaryFunction != CurrentGoal
Fitness != MoralWorth/Duty

Age != FertilityBit
ChronologicalAge != ReproductiveAge/State
OvarianReserve != Fertility
AMH != ExactTimeToMenopause
Menopause != AgingTotality
Menopause != Asexuality
ReproductiveAging_Male != ReproductiveAging_Female

PredictiveModel != Authority
GenitalResponseMeasure != Desire/Consent
ReproductiveCapability != ConsentCapacity
CanGestate != SocialGenderRoleByDefinition
ChangedBiologicalState != ChangedPersonalIdentityByDefinition

BiologicalSex HF24 rejected
Sexuality HF24 rejected
ReproductiveState HF24 rejected
Unified Sex/Sexuality/Reproduction HF24 rejected
```

---

# 154. Final HD6 compression

The Human sex/reproductive domain is not:

```text
male/female
→ sex drive
→ intercourse
→ child
```

It is closer to:

```text
Genetic / Developmental Inputs
        ↓
Typed Sex-Related Biological Profile
        ↓
Pubertal / Reproductive Maturation
        ↕
Dynamic Endocrine / Reproductive State
        ↕
Sexual Desire / Attraction / Arousal / Identity / Behavior
        ↕
Goals / Consent / Relationships / Norms / Technology
        ↓
Reproductive Decisions and/or Sexual Actions
        ↓
Conception / Nonconception / ART / Pregnancy / Birth
        ↓
Genetic / Gestational / Social Parenthood Pathways
        ↓
Physiological + Relational + Institutional Change
        ↓
Reproductive Aging / Changed Future Options
        ↺
```

No single layer defines the others.

The deepest result is therefore not HF24.

It is:

```text
Sex / sexuality / reproduction must be modeled as a typed cross-layer domain whose
biological, experiential, motivational, relational, reproductive and normative coordinates
remain separable while interacting dynamically across the life course.
```
