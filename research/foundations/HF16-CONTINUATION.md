---
schema_version: 1
id: human.foundations.hf16.continuation
title: Human Foundations Continuation after HF16
type: handoff
profile: research
lifecycle: active
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
updated: 2026-08-17
summary: Exact continuation after HF16. HF16 reconstructs aggregation across bearers, variable populations and time by separating claim/welfare aggregation, total/average/distribution/priority, population identity/size/value, person-affecting/impersonal comparison, creation/non-creation, discount components, extinction/future loss and digital copy counting. Its repeated unresolved boundary is collective normative choice: aggregation across bearers is not aggregation across stakeholder preferences or moral theories and does not establish legitimate decision authority.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.foundations.hf16
  - human.foundations.hf16.sources
---
# Human Foundations Continuation after HF16

## HF16 completed result

HF16 begins from HF15's:

```text
WhoCounts
!= HowManyCount
!= HowClaimsCombine
!= WhichPopulationIsBetter
```

and reconstructs the population/temporal layer without choosing one population
axiology.

Minimum grammar:

```text
[HF15]
StandingProfile_F for candidate bearers
        ↓
Identity mapping across alternatives
  ├─ same persons
  ├─ different persons
  ├─ created/non-created
  └─ copied/forked/merged/restored
        ↓
PopulationState P
  ├─ N / composition
  ├─ welfare levels/changes
  ├─ distribution / worst-off / thresholds
  ├─ claims / rights / severity
  ├─ time / generations
  ├─ risk / uncertainty
  └─ institutions/resources
        ↓
Aggregation candidate A
  ├─ total / average
  ├─ critical-level
  ├─ prioritarian
  ├─ maximin / leximin
  ├─ sufficientarian
  ├─ full aggregation
  ├─ partial/nonaggregation
  ├─ person-affecting
  └─ impersonal/plural
        ↓
PopulationComparison_F,A(P,Q)
  ├─ P > Q
  ├─ Q > P
  ├─ tie
  ├─ incomparability
  └─ normative uncertainty
        ↓
Temporal/risk layer
  pure time ≠ growth ≠ opportunity cost ≠ risk ≠ rate uncertainty
        ↓
Future / creation / extinction / replication implications
        ↓
[HF17 boundary]
collective choice under plural/incomplete/uncertain normative orderings
```

## Aggregation

Separate:

```text
WelfareAggregation
ClaimAggregation
RiskAggregation
TemporalAggregation
PopulationAggregation
PreferenceAggregation
NormativeTheoryAggregation
```

Retain:

```text
MoralStanding != PopulationValue
Standing != ClaimStrength
ClaimStrength != WelfareMagnitude by definition
NumberAffected != AggregateMoralWeight by definition
OneMoreClaim != OneMoreUnitOfValue by definition
NumbersCount != FullAggregationByDefinition
NumbersDoNotAlwaysDecide != NumbersNeverMatter
Severity != NumberAffected
ManyTinyBenefits != IrrelevantByDefinition
ManyTinyBenefits != SevereHarmByDefinition
RelevantClaimThreshold != HarmDeniability
WelfareAggregation != ClaimAggregation
Aggregation != TotalUtilitarianism
```

Taurek-style nonaggregation, Voorhoeve-style partial/relevant-claims aggregation and
Halstead-style full aggregation remain competing model families.

## Welfare, distribution and priority

Retain:

```text
TotalWelfare != AverageWelfare
AverageWelfare != WelfareDistribution
SameTotalWelfare != SameWelfareDistribution
SameAverageWelfare != SamePopulationValue by definition
SameTotalWelfare != SamePopulationValue by definition
CriticalLevel != PersonalLifeWorthLivingThreshold by definition
CriticalLevelUtilitarianism != Sufficientarianism
PriorityToWorseOff != Equality
Prioritarianism != NonAggregation
PriorityToWorseOff != LexicalPriority
Maximin != Prioritarianism
Leximin != Maximin
Sufficiency != AverageWelfare
InequalityAversion != Prioritarianism by definition
EmpiricalPopulationPreference != PopulationEthicsTruth
```

Population-health experiments demonstrate real heterogeneity in inequality, total
versus average and critical-level preferences but do not resolve normative theory.

## Population size / identity

Use:

```text
PopulationSize(P)
PopulationIdentity(P,Q)
SamePersonComparison(P,Q,i)
```

Retain:

```text
PopulationSize != PopulationValue
AdditionalPositiveLife != AutomaticPopulationImprovement
AdditionalPositiveLife != AutomaticNeutrality
FixedPopulationRule != VariablePopulationRule by default
SamePopulationSize != SamePopulationIdentity
SameAverageWelfare != SamePeople
SamePeopleComparison != DifferentPeopleComparison
IdentityChange != MoralIrrelevance
```

Bearer counting depends on HF1 identity and HF15 standing before aggregation.

## Non-identity

Parfit-style identity-affecting cases establish the category boundary:

```text
NoSamePersonWorseOff != NoNormativeProblem by definition
```

Separate:

```text
identity fact
same-person better/worse relation
population comparison
normative principle
```

Retain:

```text
PersonAffectingComparison != WholePopulationEthics
ImpersonalPopulationValue != WelfareOfOnePerson
ImpersonalValue != TotalUtilitarianism
```

Narrow, wide, comparative, conditional and asymmetric person-affecting views remain
separate candidates.

## Existence / creation

Retain:

```text
Nonexistence != WelfareStateOfExistingPerson
CreationBenefit != OrdinaryBenefitToExistingPerson by definition
NonCreation != Death
PreventExistence != KillExistingBearer
LifeWorthLiving != LifeRequiredToCreate
GoodPossibleLife != DutyToCreate by definition
ObservedProcreationIntuition != CorrectCreationEthics
CreationEthics != PopulationCountOnly
```

HF16 does not settle procreation asymmetry, neutral/critical levels or possible-person
standing.

## Repugnant and impossibility pressures

Retain:

```text
RepugnantConclusionCase != ObservedPopulationOutcome
IntuitionAgainstRepugnantConclusion != NormativeProof
AvoidClassicRepugnantConclusion != AdequatePopulationEthics
RepugnantConclusion != TotalUtilitarianismOnly
ImpossibilityTheorem != OneTheoryWinner
FormalConsistency != NormativeAdequacy
Intuition != Axiom
CompletePopulationOrdering != CorrectPopulationOrdering
Incomparability != Irrationality by definition
Incomparable(P,Q) != EqualValue(P,Q)
UncertainOrdering != Indifference
```

Arrhenius-style impossibility results reveal trade-offs among axioms; generalized
repugnant-conclusion results show that avoiding the classic form cannot serve as a
single theory-selection rule.

## Time / discounting

HF16 separates:

```text
DescriptiveIndividualDiscounting
PureTimePreference
ConsumptionGrowth/WealthEffect
OpportunityCostOfCapital
RiskAdjustment
DiscountRateUncertainty
Mortality/ExtinctionHazard
SocialDiscountRate
MonetaryDiscounting
WelfareDiscounting
```

Retain:

```text
TemporalDistance != DiscountFactor by definition
TemporalDistance != LowerMoralStanding
LaterBenefit != SmallerBenefit by definition
DescriptiveTimePreference != SocialDiscountRate
PureTimePreference != OpportunityCost
PureTimePreference != ConsumptionGrowthEffect
PureTimePreference != RiskAdjustment
PureTimePreference != ExtinctionHazard
PositiveSocialDiscountRate != FuturePeopleMatterLessByDefinition
ZeroPureTimePreference != ZeroDiscountRateForAllConsequences
DiscountingMoney != DiscountingWelfare
ExpertMedianDiscountRate != CorrectNormativeDiscountRate
DecliningDiscountRate != HyperbolicHumanPreferenceByDefinition
DiscountRateUncertainty != PureTimePreference
DecliningRateModelResult != UniversalNormativeRule
FutureGenerationWeight != TimeOnly
TemporalDistance != WelfareLevel
TemporalDistance != OutcomeUncertainty
TemporalDistance != IdentityDifference
PsychologicalConnectednessDiscount != PureSocialTimePreference
FutureGeneration != OnePerson
FutureWelfareMean != FutureWelfareDistribution
MoralConcernForFuture != SocialDiscountRate
PsychologicalTemporalDiscountingOfConcern != NormativeDiscountRate
```

Ramsey, Ramsey-style social discounting, expert SDR decomposition and uncertain-rate
models remain different claims rather than one `discount rate` fact.

## Risk / expected value

Use:

```text
EV_F(Action) = Σ_s Pr(s|Action,M) * V_F(s)
```

only after probability model `M` and evaluative framework `F` are specified.

Retain:

```text
ExpectedValue != NormativeFramework
LargeExpectedValue != ActionAutomaticallyJustified
ExistenceProbability != MoralStanding
ExpectedPopulationSize != RealizedPopulationSize
ExpectedFutureWelfare != CertainFutureWelfare
TailProbability != TailMoralMagnitude
```

Rights, legitimacy, distribution and authority remain live even when expected value
is large.

## Extinction / existential loss

Retain:

```text
NearExtinction != Extinction
Extinction != CurrentDeathsOnly
ExistentialLoss != LostFutureWelfareOnly by definition
PotentialFutureScale != SettledExistentialValue
ExistentialRisk != ExpectedValueOnly
ObservedExtinctionJudgment != ExtinctionValueTruth
ExtinctionValue != FuturePopulationSizeOnly
ExistentialRiskReduction != LexicallyDominantDuty by definition
Irreversibility != MoralMagnitude by definition
```

Separate current catastrophe from permanent future loss. Candidate future-loss
components include foregone future welfare/claims, cultural/institutional continuity,
knowledge/projects, option value and trajectory loss. Which count and how remains
framework-relative.

## Digital replication / replacement

Retain:

```text
Replacement != Survival
FunctionallyEquivalentCopy != SameIndividual
Replacement != CompensationByDefinition
Copy != SameIndividual by definition
BranchingContinuity != NumericalIdentity
InstanceCount != BearerCountUntilIdentitySpecified
ForkCount != PersonCountByDefinition
Backup != ContinuationByDefinition
Merge != IdentityRestorationByDefinition
SurvivalRelation != NumericalIdentity by definition
OSProcessCount != MoralBearerCount
HardwareInstance != MoralBearer by definition
Copyable != MorallyReplaceable by definition
N copies != N independent welfare draws
PopulationSize != Resilience
PopulationDiversity != PopulationSize
PopulationState != PopulationValue
```

Canonical order:

```text
physical instance
→ HF1 identity
→ HF15 standing
→ bearer set
→ HF16 aggregation
```

Never count OS processes directly as patients.

## Canonical profiles

### PopulationComparisonProfile

```text
{
  alternatives P,Q,
  framework,
  bearer/standing rule,
  identity mapping,
  population sizes,
  welfare levels/changes,
  distribution/worst-off/thresholds,
  claim types/strengths,
  rights/constraints,
  same-person vs different-person structure,
  created/non-created bearers,
  critical/neutral levels,
  time,
  uncertainty/probability,
  aggregation rule,
  result/incomparability,
  paradox pressures
}
```

### TemporalDiscountProfile

```text
{
  object discounted,
  horizon,
  pure time preference,
  growth/wealth effect,
  opportunity cost,
  risk adjustment,
  rate uncertainty,
  extinction hazard,
  social rate,
  declining rule,
  welfare vs monetary units,
  justification,
  sensitivity
}
```

### DigitalPopulationProfile

```text
{
  prior entity,
  physical instances,
  continuity relation,
  HF1 identity,
  HF15 standing,
  fork/copy/merge/restore history,
  shared resources,
  correlated failures,
  welfare dependence,
  bearer count,
  aggregation rule,
  replacement/survival assumptions
}
```

### ExtinctionLossProfile

```text
{
  current harms/deaths,
  survivors/recovery,
  permanent extinction,
  future population scenarios,
  future welfare/claims,
  cultural/institutional/knowledge loss,
  option value,
  future quality,
  standing assumptions,
  population axiology,
  risk/model uncertainty,
  rights/legitimacy constraints
}
```

## High-information falsifiers to preserve

- one death versus arbitrarily many tiny benefits;
- one death versus many substantial permanent impairments;
- same total welfare with very unequal distribution;
- same average welfare with different population sizes;
- extra positive-welfare lives lowering average welfare;
- priority to worse-off versus lexical maximin;
- critical-level social contribution versus life-worth-living threshold;
- classic and generalized repugnant cases;
- Arrhenius-style axiom impossibility;
- identity-affecting climate/reproductive policy;
- same number/different people population;
- no same person worse off yet predictably worse future conditions;
- procreation asymmetry cases;
- descriptive human concern declining with future temporal distance;
- expert disagreement over social discount-rate components;
- declining certainty-equivalent rates generated by rate uncertainty rather than
  psychological hyperbolicity;
- extinction versus near-extinction with identical/similar immediate deaths;
- extinction judgment changing when long-term future consequences become salient;
- fork one digital patient into many processes;
- kill-and-replace with functionally equivalent copy;
- backup/restore without agreed identity criterion;
- many copies sharing one correlated failure mode;
- public population-ethics preferences heterogeneous across total/average,
  inequality and critical-level dimensions.

## The repeated residual after HF16

HF16 can produce framework-relative population rankings, including explicit
incomparability and uncertainty.

It cannot answer:

```text
Which framework has authority when citizens/stakeholders disagree?
How should individual preferences/moral judgments be aggregated?
How should normative theories be combined under moral uncertainty?
What does majority rule establish?
How should minority rights constrain aggregation?
How do strategic voting, agenda and framing affect collective choice?
When does expertise provide evidence rather than authority?
What is legitimate collective action when rankings are incomplete?
How can AI support deliberation without acquiring hidden decision authority?
```

The decisive firewall is:

```text
AggregationAcrossBearers
!= AggregationAcrossPreferences
!= AggregationAcrossNormativeTheories
!= LegitimateCollectiveChoice
```

Therefore the exact next round is:

# HF17 — Normative Pluralism, Moral Uncertainty, Incommensurability, Social Choice, Collective Decision, Voting, Deliberation and Robust Governance

## HF17 starting questions

1. What is preference aggregation relative to welfare/claim aggregation?
2. What is a social ordering relative to one individual's preference or moral
   judgment?
3. What is empirical disagreement relative to normative pluralism?
4. What is incommensurability relative to incomparability and uncertainty?
5. How can moral uncertainty be represented without arbitrary score normalization?
6. What exactly does Arrow-style impossibility establish and not establish?
7. What is majority rule relative to legitimacy, truth and minority rights?
8. What is strategic voting/manipulation relative to genuine preference?
9. How do agenda, framing and option generation alter collective outcomes?
10. What is constitutional/rights constraint relative to social aggregation?
11. How should minority claims be represented?
12. What is deliberation relative to information, persuasion, conformity and power?
13. When should expertise affect epistemic weight without transferring authority?
14. What is consensus relative to agreement, conformity and legitimacy?
15. How should institutions choose when social/normative rankings are incomplete?
16. What makes a decision robust across plausible moral frameworks?
17. What roles can AI play in elicitation, option generation, summarization,
    deliberation and execution without hidden authority?
18. What next boundary emerges only after collective normative choice is rebuilt?

## Candidate HF17 falsifiers

- Condorcet/majority cycle across three alternatives;
- majority choice violating a protected minority claim;
- strategic misreport changing the winner;
- agenda order changing pairwise outcome;
- identical population outcomes ranked differently by voting rule;
- empirical expert minority with better factual evidence but no delegated authority;
- apparent consensus generated by conformity/coercion;
- deliberation improving factual accuracy while increasing value polarization;
- incomplete individual ordering but institution requiring action;
- moral theories whose numerical scores are not intertheoretically comparable;
- expected-theory-score result changing under arbitrary scale normalization;
- AI-generated agenda omitting a minority-protective alternative;
- AI summary framing changing votes despite no formal authority;
- fair procedure producing substantively bad outcome;
- attractive outcome produced through illegitimate procedure.

## Do not precommit

HF16 does not establish that:

- majority rule is legitimate by definition;
- majority preference is normative truth;
- one-person-one-vote is sufficient for every collective domain;
- utilitarian preference aggregation is correct;
- Arrow's theorem proves democracy impossible;
- dictatorship is required by social-choice impossibility;
- consensus is truth;
- deliberation always improves decisions;
- expertise implies political authority;
- citizens' raw preferences are normatively decisive;
- moral theories can be averaged on arbitrary numerical scales;
- incomplete rankings must be artificially completed;
- constitutional rights are lexically absolute in every framework;
- compromise is moral truth;
- AI should infer hidden preferences without authorization;
- AI recommendation or optimization creates collective decision authority.

## Stop rule

Do not schedule HF18 now. HF17 must expose a repeated neighboring distinction across
materially different collective-choice cases.
