---
schema_version: 1
id: human.foundations.hf17.continuation
title: Human Foundations Continuation after HF17
type: handoff
profile: research
lifecycle: completed
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
updated: 2026-08-17
summary: Exact continuation after HF17. HF17 reconstructs collective normative choice by separating preference, moral judgment, normative reason, value pluralism, incommensurability/incomparability, moral uncertainty, social ordering, voting rules, strategic manipulation, agenda, rights/minority constraints, representation, expertise/authority, deliberation, consensus, legitimacy, robust governance and AI mediation. Its repeated residual is strategic implementation under private information and incentives: a legitimate collective choice rule does not itself elicit truthful types, induce participation, prevent free riding, align bargaining or make the selected outcome self-enforcing.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.foundations.hf17
  - human.foundations.hf17.sources
---
# Human Foundations Continuation after HF17

## HF17 completed result

HF17 begins from HF16's deepest firewall:

```text
AggregationAcrossBearers
!= AggregationAcrossPreferences
!= AggregationAcrossNormativeTheories
!= LegitimateCollectiveChoice
```

and reconstructs collective normative choice without selecting one voting rule,
consensus model, deliberative process, expert regime or moral-uncertainty calculus by
fiat.

Minimum grammar:

```text
Collective decision question Q
        ↓
Who is affected? [HF15]
Who is authorized to participate/decide? [HF13/HF14]
        ↓
Input types kept separate
  ├─ preference
  ├─ moral judgment
  ├─ factual belief/probability
  ├─ normative reason
  ├─ interest/claim
  └─ expertise/evidence
        ↓
Comparability structure
  ordinal / cardinal / incomplete / parity / incomparable
        ↓
Option + agenda formation
        ↓
Information / deliberation / persuasion / bargaining
        ↓
Reported inputs
        ↓
Collective rule
  ├─ majority/plurality/scoring/approval
  ├─ Condorcet/randomization
  ├─ judgment aggregation
  ├─ consensus/compromise
  └─ theory-uncertainty/robustness rule
        ↓
Rights / minority / constitutional constraints
        ↓
Collective output
  ├─ ordering
  ├─ selected action
  ├─ common-ground statement
  └─ unresolved/incomparable
        ↓
Authorization / legitimacy
        ↓
Execution
        ↓
Revision / appeal / learning
        ↺
```

## Preference, judgment, reason and welfare

Retain:

```text
Preference != Welfare
Preference != Interest
Preference != MoralJudgment
Preference != NormativeReason
MoralJudgment != NormativeTruth
NormativeReason != Vote
Vote != TruePreference by definition
Vote != MoralJudgment
ReportedPreference != LatentPreference by definition
ObservedChoice != StablePreference
OrdinalPreference != CardinalUtility
CardinalUtility != Welfare by definition
Cardinality != InterpersonalComparability
InterpersonalComparability != IntertheoreticComparability
```

A ballot, report or observed choice is an elicited/strategic output, not a transparent
readout of welfare, interest or moral truth.

## Disagreement, pluralism, incommensurability and incomparability

Retain:

```text
EmpiricalDisagreement != NormativePluralism
EmpiricalAgreement != NormativeMonism
NormativePluralism != AnythingGoes
NormativePluralism != PreferenceHeterogeneity
ValuePluralism != IncomparabilityByDefinition
Incommensurability != Incomparability by definition
Incomparability != Uncertainty
Uncertainty != Incomparability
Indifference != Incomparability
Parity != Equality
Parity != Incomparability
HardChoice != EpistemicUncertaintyByDefinition
IncompleteOrdering != Irrationality by definition
ForcedCompletion != DiscoveryOfLatentTrueOrdering
```

Do not silently convert `incomparable`, `unknown` or `parity` into numerical ties.

## Moral uncertainty

Working relation:

```text
MoralUncertainty(H,{F_j},C)
= uncertainty over which normative framework/principle is correct/applicable
```

Retain:

```text
MoralUncertainty != InterpersonalMoralDisagreement
MoralUncertainty != EmpiricalUncertainty
TheoryCredence != VoterSupport
CredenceInTheory != DecisionAuthority
ExpectedChoiceworthiness != UniversalMoralUncertaintyRule
NumericalTheoryScore != IntertheoreticallyComparableScore
RepresentationScaleChoice != MoralImportance
NormalizationRule != NeutralTechnicalStep
MoralTheory != Voter
```

Expected-choiceworthiness methods require explicit scale/comparability assumptions;
ordinal or lexically structured theories cannot be averaged naively.

## Social choice types

Separate:

```text
SocialWelfareFunction: preference-profile -> social ordering
SocialChoiceFunction: preference/type-profile -> selected alternative/set
JudgmentAggregation: judgment-profile -> collective judgment set
CollectiveDecision: institution authorizes a policy/action
```

Retain:

```text
ArrowSWF != HF16PopulationWelfareFunction by definition
SocialOrdering != IndividualOrdering
SocialOrdering != SharedBelief
CollectiveDecision != Consensus
PopulationOrdering != CollectiveDecision
SocialOrdering != CollectiveDecision
OutcomeValueFunction != VotingRule
VotingRule != Legitimacy
WinningAlternative != NormativeTruth
MajorityPreference != NormativeTruth
```

## May / majority characterization

May's classic characterization is a binary-domain result with exact formal
conditions such as anonymity, neutrality and positive responsiveness.

Retain:

```text
MayCharacterization != MajorityRuleOptimalForAllDomains
VotingAnonymity != EqualPoliticalStanding
VotingNeutrality != NormativeNeutrality
MonotonicityProperty != Legitimacy
```

## Condorcet / epistemic majority

Condorcet-style jury results can make majority extremely effective at truth tracking
when the decision is a truth task and competence/dependence assumptions are met.

Retain:

```text
MajorityAccuracyResult != MajorityNormativeAuthority
MoreVoters != MoreIndependentEvidence
PreferenceVote != EpistemicJuryVote
Expertise_D != Expertise_E
EpistemicAccuracy != PoliticalLegitimacy
```

Do not import truth-tracking results into irreducible value conflict without an
argument that the task actually has a truth-like target and the epistemic assumptions
hold.

## Arrow

Arrow's theorem concerns a specified mapping from profiles of individual orderings to
a social ordering over at least three alternatives under a broad domain and specified
conditions.

Retain:

```text
ArrowImpossibility != AllCollectiveChoiceImpossible
ArrowTheorem != DemocracyImpossible
ArrowTheorem != DictatorshipNormativelyRequired
ArrowIIA != EverydayIrrelevanceIntuition
UniversalDomain != EmpiricalPreferenceDomain
```

The theorem identifies a property/domain conflict; it does not choose which condition
an institution should relax.

## Condorcet cycles / agenda

Even individually transitive preferences can yield cyclic pairwise majority.

Retain:

```text
IndividualRationalOrderings != TransitiveMajorityOrdering
CondorcetCycle != IndividualIrrationality
Agenda != NeutralContainer
PluralityWinner != MajorityPreferenceWinner by definition
ScoringRule != CardinalUtilityAggregation
ApprovalSet != CompletePreferenceOrdering
RandomizedChoice != ProceduralFailureByDefinition
EqualChance != EqualOutcome
```

Option generation and agenda order are upstream components of collective decision,
not neutral presentation details.

## Gibbard-Satterthwaite / strategy

Retain:

```text
StrategyProofness != FactualTruthfulness
ManipulableRule != EveryElectionManipulated
GibbardSatterthwaite != VotingUseless
GibbardSatterthwaite != AllMechanismsManipulableInSameWay
Ballot != RuleIndependentPreferenceMeasurement
```

The theorem family establishes strategic-reporting trade-offs on specified
unrestricted deterministic multi-alternative domains. Domain restrictions,
randomization and mechanisms with richer message/transfer structures are different
objects.

## Sen / rights

Sen's Paretian-liberal result pressures simultaneous minimal liberty and Pareto
requirements under its formal assumptions.

Retain:

```text
SenParetianLiberalImpossibility != LibertyImpossible
SenParetianLiberalImpossibility != ParetoWorthless
RightsProfile != AggregatePreference
Right != ExtraVoteByDefinition
MinorityPosition != NormativeTruth
MajorityPosition != NormativeTruth
MinorityProtection != UniversalMinorityVeto
ConstitutionalConstraint != NormativeTruth
RightsConstraint != LexicalPriorityByDefinition
```

Rights can constrain ordinary aggregation without becoming an unqualified universal
veto by foundation fiat.

## Judgment aggregation

When collective inputs are logically related propositions rather than one ranking,
use judgment-aggregation grammar.

Retain:

```text
JudgmentProfile != PreferenceProfile
IndividualJudgmentConsistency != CollectiveJudgmentConsistency
JudgmentAggregationImpossibility != CollectiveReasoningImpossible
PropositionwiseMajority != CollectiveRationalityByDefinition
PremiseBasedProcedure != ConclusionBasedProcedure
PreferenceAggregation != JudgmentAggregation
ReasonAggregation != JudgmentAggregation
AgreementOnConclusion != AgreementOnReasons
```

List-Pettit-style impossibility is a distinct problem from Arrow preference
aggregation.

## Consensus / compromise

Consensus is qualifier-required: unanimity, near-unanimity, absence of objection,
working agreement and endorsement are different states.

Retain:

```text
Consensus != OneUniversalState
Consensus != Truth
Consensus != LegitimacyByDefinition
Consensus != FreeAgreementByDefinition
UnanimousReport != UnanimousLatentPreference
Unanimity != NormativeTruth
Dissent != DeliberationFailureByDefinition
Compromise != Consensus
Compromise != NormativeTruth
```

## Deliberation

Working family:

```text
Deliberation_D(G,Q,C)
= structured reciprocal exchange/evaluation of reasons, evidence and perspectives
  under declared process design D
```

Retain:

```text
Bargaining != Deliberation
Persuasion != Deliberation
InformationProvision != Deliberation
Discussion != DeliberationByDefinition
Deliberation != DepolarizationGuarantee
OneDeliberationDesignWorks != DeliberationAlwaysWorks
DeliberationEffect_D != DeliberationEffect_E
UnderstandOpposingReason != AdoptOpposingConclusion
ReducedAffectivePolarization != PreferenceConvergence
PreferenceConvergence != NormativeTruth
PostDeliberationPreference != PreexistingPreferenceReadout
PreferenceChange != ManipulationByDefinition
StablePreference != WellInformedPreferenceByDefinition
InformedPreference != NormativelyAuthoritativePreferenceByDefinition
Participation != EffectiveInfluence
Voice != DecisionAuthority
VoteRight != AgendaControl
```

Preserve Fishkin/America-in-One-Room as a strong positive structured-deliberation case
and Kramon's Honduras perspective-treatment result as a falsifier against universal
depolarization. Deliberation is an intervention that can alter preferences, knowledge,
affect and future participation.

## Representation

Separate:

```text
StatisticalRepresentativeness
PoliticalRepresentation
DescriptiveRepresentation
SubstantiveRepresentation
AuthorizedRepresentation
DelegatedRepresentation
SymbolicRepresentation
```

Retain:

```text
RepresentativeSample != PoliticalRepresentative
DescriptiveRepresentation != Authorization
Authorization != Accountability
PreferenceMirroring != PoliticalRepresentationTotality
DelegateRepresentation != TrusteeRepresentation
DemographicSample != AffectedStakeholders
AffectedStakeholder != VoterByDefinition
```

## Expertise / authority

Working:

```text
Expertise_D(H)
= demonstrated domain-specific epistemic competence under declared conditions
```

Retain:

```text
Expertise_D != GeneralIntelligence
Expertise != Authority
EpistemicCorrectness != Authorization
EpistemicWeight != PoliticalPowerByDefinition
Expertise != Consensus
ExpertConsensus != NormativeTruth
EpistemicAdviceWeighting != Epistocracy
BetterPoliticalKnowledge != LegitimateRuleAuthority
EpistemicQuality != Legitimacy
ProceduralFairness != OutcomeFairness
LegitimateProcedure != SubstantivelyCorrectOutcomeByDefinition
GoodOutcome != LegitimateProcedure
Legitimacy != Compliance
Compliance != Agreement
PublicAcceptance != NormativeLegitimacy
```

Expertise can rationally alter evidence weighting on factual questions without
creating political or moral authorization.

## AI-mediated collective choice

Roles must remain explicit:

```text
OptionGenerator
InformationRetriever
FactSummarizer
ArgumentGenerator
PerspectiveSummarizer
PreferenceElicitor
Clusterer
Mediator
ConsensusStatementGenerator
VotingRuleAnalyzer
RecommendationGenerator
Authorizer
Executor
Auditor
```

Retain:

```text
AIMediator != CollectiveDecisionAuthority
AISummary != NeutralRepresentationByDefinition
CommonGroundStatement != AuthorizedCollectiveDecision
StatementEndorsement != InstitutionalLegitimacy
MaximizeApproval != PreserveAllMinorityClaimsByDefinition
AIPersuasion != Deliberation
PersuasionEffect != EpistemicImprovementByDefinition
MorePersuasiveAI != MoreTruthfulAI
PerceivedAutonomousJudgment != InfluenceFreeJudgment
InferredPreference != Consent
PredictedVote != CastVote
AISimulatedCitizen != AuthorizedRepresentative
AIGeneratedCompromise != HumanCommitment
AIRecommendation != CollectiveDecision
Execution != Authorization
HumanInLoop != MeaningfulControlByDefinition
```

Tessler et al. is the positive scalable common-ground case. Lin et al., Hackenburg et
al. and Glickman/Sharot are essential falsifiers showing that conversational AI can
also persuade, trade factuality against persuasion and amplify Human judgment biases.

Therefore AI mediation must expose agenda/option generation, compression, factuality,
minority coverage, persuasion, preference inference, ratification, authorization and
execution separately.

## Robust governance

Working family:

```text
RobustDecision(A,{F_j},{M_k})
= A remains acceptable/non-dominated under a declared set of plausible normative
  frameworks and empirical models
```

Retain:

```text
CrossTheoryRobustness != NormativeTruth
RobustAcrossTheories != ConsensusAmongPeople
HumanConsensus != CrossTheoryRobustness
CrossTheoryDominance != Authority
MinimaxRegret != MoralTruth
Precaution != Truth
Revisability != GovernanceFailureByDefinition
Irrevocability != Legitimacy
Appeal != Veto
SelectedOutcome != ErasureOfDissent
```

HF17 allows collective decisions to preserve dissent, uncertainty and review triggers
rather than pretending authorization erased disagreement.

## Canonical profiles

### CollectiveChoiceProfile

```text
{
  decision question,
  affected population/stakeholders,
  authorized electorate/participants,
  representation/sampling model,
  input type,
  ordinal/cardinal/comparability assumptions,
  option-generation/agenda process,
  information conditions,
  deliberation design,
  voting/aggregation rule,
  strategic incentives,
  rights/minority constraints,
  expertise/advisory roles,
  AI mediation roles,
  social ordering/selected outcome,
  dissent/minority report,
  legitimacy/authority basis,
  execution authority,
  revision/appeal,
  uncertainty/robustness
}
```

### PreferenceAggregationProfile

```text
{
  agents,
  preference concept,
  report mechanism,
  ordinal/cardinal structure,
  domain restrictions,
  agenda/options,
  aggregation rule,
  anonymity/neutrality/monotonicity,
  Pareto/unanimity property,
  IIA-like property,
  strategy-proofness/manipulability,
  cycles/ties,
  output type
}
```

### JudgmentAggregationProfile

```text
{
  agenda/propositions,
  logical dependencies,
  individual consistency assumptions,
  premise/conclusion/proposition aggregation,
  independence/systematicity assumptions,
  collective consistency/completeness,
  dissent retention,
  output
}
```

### DeliberationProfile

```text
{
  participants/selection,
  affected-group coverage,
  initial preference/judgment profile,
  information symmetry,
  briefing provenance,
  facilitation,
  perspective-taking design,
  turn-taking/voice balance,
  power/coercion risks,
  AI role,
  factuality audit,
  pre/post preference/knowledge change,
  affective polarization,
  reason quality,
  minority incorporation,
  consensus/convergence,
  downstream participation,
  durability
}
```

### MoralUncertaintyProfile

```text
{
  candidate theories,
  credences/uncertainty,
  ordinal/cardinal theory structure,
  intratheory scale invariances,
  intertheory comparability assumptions,
  normalization rule,
  candidate decision rules,
  fanaticism/swamping risk,
  rights/lexical constraints,
  robust dominance,
  incomparabilities,
  selected action/uncertainty
}
```

### AICollectiveChoiceProfile

```text
{
  model/version,
  objective,
  role,
  user-input provenance,
  option-generation authority,
  summary/compression policy,
  minority coverage,
  persuasion/factuality evidence,
  preference-inference use,
  endorsement process,
  human ratification,
  authorization boundary,
  execution boundary,
  audit/contestability,
  appeal/revision
}
```

## High-information falsifiers to preserve

- binary majority choice satisfying May-style conditions;
- Condorcet truth task with independent competent voters;
- Condorcet majority cycle despite individually transitive orderings;
- Arrow unrestricted-domain social ordering;
- strategic misreport under Gibbard-Satterthwaite setting;
- agenda order changing pairwise outcome;
- Sen minimal-liberty/Pareto conflict;
- doctrinal/discursive dilemma with individually consistent judgments;
- unanimous report caused by coercion/conformity;
- majority outcome violating a protected minority claim;
- expert minority with superior factual evidence but no delegated authority;
- statistically representative sample without political authorization;
- America in One Room structured-deliberation depolarization;
- Honduras own-perspective deliberation modestly increasing polarization relative to
  stronger out-partisan perspective-taking effects;
- participatory-budgeting intervention changing later civic participation;
- AI common-ground mediator improving endorsed statements;
- AI common-ground statement without institutional authorization;
- conversational AI shifting candidate/policy preferences;
- more persuasive AI configurations reducing factual accuracy;
- Human-AI feedback loop amplifying biases while users underperceive influence;
- expected-moral-score ranking changing under arbitrary scale transformation;
- incomparable alternatives incorrectly encoded as ties;
- legitimate process producing substantively bad outcome;
- substantively attractive outcome produced by illegitimate process.

## Repeated residual after HF17

HF17 can now represent:

```text
who participates,
what type of input they provide,
how options/agendas are generated,
how information and deliberation change those inputs,
which voting/judgment/theory rule is applied,
which rights/minority constraints bind,
what outcome is authorized,
and how dissent/revision are preserved.
```

But across voting, deliberation, representation, public goods and AI mediation, a
new gap repeatedly remains:

```text
Why would agents report private information truthfully?
Why participate at all?
Why contribute to a public good rather than free ride?
Why comply with an authorized outcome?
How do hidden actions/types change contracts/delegation?
How do bargaining positions determine distribution?
How do prices/transfers change behavior?
Can the selected collective outcome actually be implemented as an equilibrium?
How do collusion/capture/Sybil/copying defeat the mechanism?
```

The decisive firewall is:

```text
CollectivePreference
!= CollectiveDecision
!= Mechanism
!= IncentiveCompatibleImplementation
!= RealizedOutcome
```

Therefore the exact next round is:

# HF18 — Incentives, Mechanism Design, Private Information, Bargaining, Public Goods, Commons, Markets and Strategic Implementation

## HF18 starting questions

1. What is an incentive relative to motivation, preference, reward and sanction?
2. What is a private type relative to preference, information and capability?
3. What is a message/report relative to true type?
4. What is a game form/mechanism relative to a social-choice rule?
5. What is implementation relative to selection, authorization and execution?
6. What distinguishes dominant-strategy, Bayesian and Nash incentive compatibility?
7. What is truthful revelation and what exactly does the revelation principle imply?
8. What are participation/individual-rationality constraints?
9. What is an externality relative to ordinary third-party effect?
10. Why can unanimous preference for a public good coexist with free-riding?
11. What distinguishes common-pool resources from public goods?
12. What is bargaining relative to deliberation and social choice?
13. What are transfers/prices relative to welfare, resources and power?
14. What is market allocation relative to voting and planning?
15. How do adverse selection and moral hazard arise from hidden information/action?
16. What is principal-agent structure relative to delegation/authority?
17. What is self-enforcement relative to legal enforceability?
18. How do collusion, capture and strategic coalitions pressure-test mechanisms?
19. How do Sybil identities, digital copies/forks and AI agents alter participation and
    allocation mechanisms?
20. When can an AI truthfully represent a Human's preferences/types and when can it
    strategically optimize against the mechanism?
21. What next boundary emerges only after strategic implementation is rebuilt?

## Candidate HF18 falsifiers

- unanimous support for a public good but individual free-riding;
- majority-approved tax/contribution rule with evasion incentives;
- strategy-proof direct revelation on one domain versus impossibility on another;
- truthful direct mechanism versus strategically equivalent indirect mechanism;
- bidder hiding private valuation in an auction;
- common-value auction/winner's-curse information structure;
- adverse-selection insurance/credit market;
- moral-hazard contract after hidden action;
- principal delegates to a more skilled agent with divergent objective;
- common-pool resource overextraction despite common long-run interest;
- bargaining where all agree surplus exists but disagree over distribution;
- decentralized market clearing without a collective vote over individual trades;
- efficient allocation violating rights/distribution constraints;
- transfer-based truthful mechanism facing budget/redistribution constraints;
- colluding agents defeating individually incentive-compatible mechanism;
- Sybil identities/forks multiplying apparent participants;
- AI agent strategically reporting a user's preference to maximize platform reward;
- AI participants coordinating to game allocation/voting mechanisms.

## Do not precommit

HF17 does not establish that:

- every social problem is a mechanism-design problem;
- rational agents always maximize one scalar utility;
- preferences/types are fixed and exogenous;
- dominant-strategy truthfulness is always feasible or necessary;
- Nash equilibrium is a behavioral law;
- the revelation principle supplies a practical mechanism;
- monetary transfers are always legitimate or available;
- VCG mechanisms are universal solutions;
- auctions/markets are inherently efficient, fair or legitimate;
- central planning is inherently inferior or superior;
- public goods require state provision;
- commons inevitably collapse;
- free riding is irrational by definition;
- prices measure welfare or moral value;
- efficient equilibrium is just or legitimate;
- contracts eliminate power/information asymmetry;
- legal enforceability equals self-enforcement;
- AI agents truthfully report user interests by default;
- strategic robustness equals normative legitimacy.

## Stop rule

Do not schedule HF19 now. HF18 must expose a repeated neighboring distinction across
materially different mechanism/allocation/implementation cases.

## Supersession — HF18 complete

HF18 has completed the strategic-implementation boundary selected here. Current
continuation is owned by [`HF18-CONTINUATION.md`](HF18-CONTINUATION.md), with the
first-cycle compact index in
[`HF0-HF18-CYCLE-CLOSEOUT-20260817.md`](HF0-HF18-CYCLE-CLOSEOUT-20260817.md).
This file remains the canonical record of why HF18 emerged from HF17.
