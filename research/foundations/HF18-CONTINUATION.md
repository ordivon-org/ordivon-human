---
schema_version: 1
id: human.foundations.hf18.continuation
title: Human Foundations Continuation after HF18
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
summary: Exact continuation after HF18. HF18 reconstructs strategic implementation under private information and incentives by separating type/message/action, mechanism/social choice, solution concepts, IC/IR/efficiency/budget/legitimacy, auctions/VCG/trade, bargaining, matching/markets, public goods/commons, adverse selection/moral hazard, principal-agent contracts, collusion/Sybil/false-name behavior and strategic Human/AI participation. Its repeated residual is production and economic organization: allocation and incentive-compatible implementation do not explain how work, technology, capital, ownership, specialization and firms create or transform the feasible set. Exact next frontier is HF19, intentionally deferred to a fresh conversation.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.foundations.hf18
  - human.foundations.hf18.sources
  - human.foundations.hf0-hf18.closeout
---
# Human Foundations Continuation after HF18

## HF18 completed result

HF18 starts from HF17's:

```text
CollectivePreference
!= CollectiveDecision
!= Mechanism
!= IncentiveCompatibleImplementation
!= RealizedOutcome
```

and reconstructs the strategic implementation layer without selecting markets,
auctions, VCG, Nash equilibrium, contracts, monetary transfers, hierarchy or central
planning by fiat.

Minimum grammar:

```text
[HF17]
Authorized collective target / allocation objective
        ↓
Who are the actual actors?
  HF1 identity + admission/Sybil rule
        ↓
Agent model
  ├─ preference/objective
  ├─ type/capability/cost
  ├─ information/beliefs
  ├─ outside option
  └─ learning/bounded rationality
        ↓
Mechanism/GameForm
  ├─ message/action spaces
  ├─ timing/repetition
  ├─ information/signals
  ├─ allocation/outcome rule
  ├─ transfers/prices
  ├─ monitoring/enforcement
  └─ commitment
        ↓
Strategic response
  report / conceal / signal / screen / bargain / collude / fork / exit
        ↓
Solution concept
  DS / ex-post / Bayesian / Nash / repeated / approximate
        ↓
Implementation properties
  IC / IR / budget / efficiency / stability / robustness
        ↓
HF14 constraints
  rights / fairness / legitimacy / responsibility
        ↓
Real execution [HF11]
        ↓
Realized outcome
        ↓
Learning / adaptation / institutional feedback
        ↺
```

## Incentive / type / message / strategy

Retain:

```text
Incentive != Motivation
Incentive != Reward
Incentive != Sanction
Incentive != Preference
SameIncentive_D != SameBehaviorAcrossAgents
AddedPayment != PureAdditiveMotivationByDefinition
Type_i != WholePerson
Type != Preference by definition
Type != Capability by definition
Type != Identity
Message_i != Type_i
ReportedType_i != TrueType_i by definition
MessageSpace != NeutralInterface
Message != Action by definition
Strategy != RealizedAction
BestResponse != NormativelyBestAction
```

A mechanism's `type` is a compressed model object, not a Human ontology. Reported type
is an endogenous strategic message, not ground truth by definition.

## Equilibrium / implementation

Retain:

```text
NashEquilibrium != ObservedBehaviorByDefinition
NashEquilibrium != UniquePredictionByDefinition
NashEquilibrium != SocialOptimum
EquilibriumExistence != EquilibriumSelection
Mechanism != SocialChoiceRule
GameForm != OutcomeFunctionOnly
Mechanism != Institution
Mechanism != LegalRule
Mechanism != Market by definition
Mechanism != Contract by definition
Implementation_D != Implementation_E
SelectedCollectiveOutcome != ImplementedOutcome
ImplementedOutcome != RealizedPhysicalOutcome
Authorization != Implementation
Implementable != Legitimate
Legitimate != Implementable
```

Implementation is always solution-concept-qualified. Formal implementation remains
upstream of HF11 physical execution and downstream of HF17 collective authorization.

## Incentive compatibility

Separate:

```text
DominantStrategyIC
ExPostIC
BayesianIC
NashImplementation
StrategyProofness
ApproximateIC
Coalition/GroupIC
FalseName/SybilProofness
```

Retain:

```text
DSIC != BIC
BIC != DistributionFreeTruthfulness
StrategyProofness != FactualTruthfulness
TruthfulEquilibrium != HumanHonestyTrait
IC != GoalAlignmentByDefinition
PrimaryIC != RobustToAllSecondaryGoals
Nonbossiness != Fairness
```

Current nonbossy-mechanism work is useful pressure showing that strategic robustness to
secondary objectives can require properties beyond ordinary strategy-proofness in the
studied domains.

## Revelation principle

Retain:

```text
RevelationPrinciple != PracticalMechanismConstruction
RevelationPrinciple_D != RevelationPrinciple_E
DirectRevelation != LowerOperationalComplexityByDefinition
TypeReportInterface != HumanCognitivelyNaturalInterface
RevelationPrinciple != EquilibriumFreeResult
```

Sugaya-Wolitzky is a key falsifier against an unqualified revelation principle:
communication revelation can fail generally for sequential equilibrium in multistage
games while holding in important subclasses/other solution concepts.

## Participation / IR

Retain:

```text
IndividualRationalityConstraint != Rationality_Normative
Participation != ConsentByDefinition
VoluntaryParticipation != LegitimacyByDefinition
OutsideOption != FixedNaturalBaselineByDefinition
```

Ex-ante, interim and ex-post IR must remain distinct.

## Efficiency / budget / transfer / price

Retain:

```text
Efficiency_D != Efficiency_E
Efficiency != WelfareByDefinition
Efficiency != Justice
Efficiency != Legitimacy
IC != Efficiency
IR != Efficiency
StrongBudgetBalance != WeakBudgetBalance
BudgetBalance != NoRealResourceCost
Transfer != Welfare
Payment != MoralValue
Price != Value by definition
WTP != WelfareMagnitudeByDefinition
MarketPrice != SocialWelfareScore
```

Do not use monetary/price variables as hidden welfare or moral scales.

## Auctions / VCG / bilateral trade

Retain:

```text
SecondPriceTruthfulness != UniversalAuctionTruthfulness
HighestBid != HighestWelfareByDefinition
Auction != Market
Auction != Bargaining
RevenueOptimal != WelfareOptimalByDefinition
MyersonOptimalAuction != UniversalAuctionDesign
VCG != OneMechanismInstance
VCGTruthful != BudgetBalancedByDefinition
VCGTruthful != DistributionallyFairByDefinition
VCGTruthful != CollusionProofByDefinition
VCGTruthful != SybilProofByDefinition
GrovesTeamBehavior != IntrinsicTeamIdentity
TruthfulValuationInModel != CostlessInstitution
MyersonSatterthwaite != TradeImpossible
MyersonSatterthwaite != UniversalMarketInefficiency
FirstBestOutcome != ImplementableOutcomeByDefinition
SecondBest_D != SecondBest_E
ApproximateImplementable != InferiorToUnimplementableIdealByDefinition
```

Myerson-Satterthwaite is the canonical HF18 impossibility pressure: in its bilateral-
trade setting, ex-post efficiency, Bayesian IC, IR and no outside subsidy cannot all
be obtained generally. It does not prove trade/markets impossible.

## Bargaining

Retain:

```text
Bargaining != Deliberation
Bargaining != Voting
Bargaining != CompetitivePriceTaking
BargainingOutcome != WelfareOptimumByDefinition
NashBargainingSolution != NashEquilibriumOfAnyBargainingGameByDefinition
NashBargaining != RubinsteinAlternatingOffers
BargainingPower != NormativeClaimStrength
DisagreementPoint != MorallyNeutralBaselineByDefinition
PositiveSurplus != AgreementGuarantee
```

Axiomatic bargaining and strategic bargaining process must not be collapsed.

## Matching / markets

Retain:

```text
Matching != Auction
Matching != PriceAllocationByDefinition
StableMatching != WelfareMaximumByDefinition
StableMatching != FairnessByDefinition
MechanismStrategyPropertySide_A != Side_B
Market != InstitutionFreeExchange
MarketOutcome != CollectiveVoteOutcome
DecentralizedAllocation != NoGovernance
PriceCoordination != CentralPlanning
CentralPlanning != OneUniformMechanism
CompetitiveEquilibriumEfficiency != UniversalMarketEfficiency
```

Market is an institutional family built on access/property/settlement/enforcement, not
an institution-free natural baseline.

## Externalities / public goods / commons

Retain:

```text
ThirdPartyEffect != ExternalityByDefinition
Externality_D != Externality_E
NegativeExternality != MoralWrongByDefinition
PositiveExternality != RightToSubsidyByDefinition
PublicGood != GovernmentGood
GovernmentProvision != PublicGoodByDefinition
CollectivePreferenceForPublicGood != VoluntaryProvision
FreeRiding != ZeroContributionByDefinition
FreeRiding != IrrationalByDefinition
IndividuallyRationalFreeRide != MorallyPermissible
PublicGoodProblem != NoMechanismCanHelp
PublicGoodMechanismSuccess_D != Success_E
ClubGood != PurePublicGood
CommonPoolResource != PublicGood
Commons != OpenAccess
OpenAccess != SelfGovernedCommons
CommonPoolResource != InevitableCollapse
SelfGovernance != NoRules
CommonsProblem != StateControlRequiredByDefinition
CommonsProblem != PrivatizationRequiredByDefinition
Cooperation != EfficientEquilibriumByDefinition
OneShotIncentives != RepeatedGameIncentives
RepeatedInteraction != CooperationGuarantee
Monitoring != Enforcement
Enforcement != Compliance
MorePunishment != MoreCooperationByDefinition
SameFormalRule != SameBehaviorAcrossInstitutionalOrigins
```

Ostrom/Gardner and related evidence are retained specifically against the equation
`commons = open access = inevitable tragedy`.

## Information asymmetry / principal-agent

Retain:

```text
AdverseSelection != MoralHazard
AsymmetricInformation != MarketCollapseByDefinition
AdverseSelection != FraudByDefinition
Screening != Signaling
Signal != TypeTruthByDefinition
Competition != InformationSymmetry
MoralHazard != MoralWrongdoingByDefinition
HiddenAction != HiddenType
MoreMonitoring != BetterContractByDefinition
PrincipalAgent != EmployerEmployeeOnly
Principal != NormativeSuperior
Principal != LegitimateAuthorityByDefinition
EconomicAgentRole != HF1AgentOntology
Delegation != PreferenceAlignment
Contract != CompleteControl
OptimalContract_M != UniversalBestContract
Contract != ResponsibilityElimination
Output != Effort
PerformancePay != EffortObservation
MeasuredPerformance != WholeTaskValue
CommonValue != IndependentPrivateValue
HighestSignal != HighestTrueValueByDefinition
WinnersCurseBehavior != MechanismTheoryInvalidByDefinition
```

Akerlof/Rothschild-Stiglitz pressure hidden pre-contract type/quality; Holmström and
Grossman-Hart pressure hidden post-contract action/effort. Do not merge these into one
`information asymmetry` box.

## AI agents / collusion / Sybil

Retain:

```text
LLMAgent != PerfectEquilibriumSolver
SameMechanism + DifferentAgentModel != SameOutcomeDistribution
LLMStrategicBehavior != OneStablePolicyClass
GeneratedOutcomeSpace != FixedFiniteOptionSet
LLMEncodedPreference != HumanPreferenceByDefinition
AIAgentProxy != HumanPrincipal
AgentRewardFunction != UserWelfare
DeclaredPrimaryUtility != CompleteAIObjectiveByDefinition
Collusion != Cooperation
Communication != Collusion
IndividualIC != CoalitionIC
CoalitionProof != SybilProof
AIAgentCompetition != InevitableCollusion
PolicyText != IncentiveEnforcement
ApparentIdentityCount != UnderlyingActorCount
SybilIdentity != MoralBearerByDefinition
ForkedProcess != IndependentParticipantByDefinition
OneAccountOneVote != OnePersonOneVoteWithoutIdentityAssumption
SybilResistance != PerfectIdentityVerification
FixedAgentSet != FreeDigitalIdentityEnvironment
SybilProof != EfficiencyByDefinition
SybilProof != CoalitionProof
FalseNameProof != OrdinaryStrategyProofness
Capture != BriberyOnly
Capture != Collusion
DesignerObjective != SocialObjectiveByDefinition
PrincipalObjective != SocialObjectiveByDefinition
MechanismOptimizationSuccess != NormativeSuccess
AnnouncedRule != CredibleCommitmentByDefinition
CryptographicCommitment != InstitutionalLegitimacy
SelfEnforcement != LegalEnforceability
LegalEnforceability != EnforcementExecution
FormalSanction != CredibleSanction
```

Peer-reviewed AI mechanism work is separated from current auction/collusion/workshop
preprints. The durable conclusion is only that model/harness/identity/communication
structure are mechanism-relevant variables; no universal AI rationality/collusion
claim is frozen.

## Behavioral / computational robustness

Retain:

```text
Robust != WorksUnderAllPossibleWorlds
RobustToBeliefError != RobustToSybil != RobustToCollusion != RobustToModelShift
SimplerMechanism != BetterMechanismByDefinition
Computable != IncentiveCompatible
IncentiveCompatible != ComputationallyTractable
TheoreticalDSIC != ErrorFreeHumanUse
StrategyProof != ObviouslyStrategyProof
FormalImplementation != BehavioralImplementation
BehavioralDeviation != MechanismInvalidityByDefinition
MeasuredTarget != WholeObjective
ProxyReward != TrueObjectiveByDefinition
HumanPreference != AgentPolicyObjectiveByDefinition
MechanismTruthfulness != PrincipalBestInterestByDefinition
DelegatedBiddingAuthority != UnlimitedEconomicAuthority
StaticMechanismAnalysis != DynamicAgentMechanismInteraction
PostOutcomeData != PreActionReport
MoreMechanismData != BetterGovernanceByDefinition
InformationDesign != MechanismDesignByDefinition
Persuasion != IncentiveCompatibility
```

## Canonical profiles

### MechanismDesignProfile

```text
{
  agent identities/admission rule,
  type spaces,
  private/public information,
  preferences/utility representation,
  message/action spaces,
  timing/repetition,
  outcome/allocation rule,
  transfer/payment rule,
  monitoring/enforcement,
  commitment assumptions,
  target social-choice/outcome rule,
  solution/equilibrium concept,
  IC notion,
  participation/IR notion,
  budget balance,
  efficiency notion,
  rights/fairness/legitimacy constraints,
  computational/cognitive complexity,
  collusion/coalition robustness,
  Sybil/false-name robustness,
  behavioral/model robustness,
  realized outcomes/failures
}
```

Also preserve:

```text
InformationAsymmetryProfile
AuctionProfile
PublicGoodsCommonsProfile
PrincipalAgentProfile
BargainingProfile
StrategicAIProfile
```

## High-information HF18 falsifiers

- truthful second-price bidding under standard private values versus common-value/
  budget/collusion/Sybil pressure;
- VCG truthfulness versus budget/fairness/coalition/Sybil desiderata;
- Myerson revenue optimum versus welfare optimum;
- Myerson-Satterthwaite first-best impossibility;
- direct revelation equivalence versus multistage sequential-equilibrium failure;
- unanimous public-good preference with voluntary free-riding;
- Falkinger mechanism substantially changing provision;
- self-governing commons versus open-access tragedy;
- dynamic resource overextraction despite shared long-term interest;
- democratically chosen versus externally imposed equivalent rule producing different
  cooperation;
- Akerlof hidden quality versus Holmström hidden action;
- output/performance signal versus effort;
- Nash bargaining versus Rubinstein strategic bargaining;
- Gale-Shapley stability versus welfare/fairness;
- individually IC mechanism defeated by coalition/collusion;
- ordinary strategy-proof mechanism vulnerable to hidden secondary goals;
- one actor presenting many Sybil identities;
- one digital fork appearing as many mechanism participants;
- LLM agents showing model-dependent winner's curse/strategic behavior;
- AI collusion observed in some simulations but fragile under heterogeneity in others;
- prompt-only anti-collusion instruction versus enforceable consequence structure;
- formally DSIC mechanism producing Human errors/misunderstanding;
- efficient implemented allocation violating HF14 fairness/rights.

## Repeated residual after HF18

HF18 can now represent:

```text
who the actual strategic actors are,
what they know privately,
what they can report/do,
which mechanism maps messages/actions to outcomes,
which equilibrium/solution concept is assumed,
which IC/IR/budget/efficiency/stability properties hold,
how collusion/Sybil/model mismatch pressure the design,
and how the intended implementation differs from real execution.
```

But across auctions, public goods, commons, contracts, matching and markets, a new gap
repeatedly remains:

```text
Where do the goods/services/resources being allocated come from?
What is work rather than merely incentive to work?
How do technology and tools transform inputs into outputs?
How does specialization change capability/productivity?
Why do teams/firms exist rather than every task being a market transaction?
What is ownership relative to possession, contract and residual control?
How do physical/human/knowledge/organizational capital differ from money?
How do incomplete contracts and ownership affect investment?
How does automation/AI substitute, complement or reorganize Human work?
How does production change the feasible set instead of merely allocating it?
```

The decisive firewall is:

```text
Allocation
!= Exchange
!= IncentiveCompatibleImplementation
!= Production
!= EconomicOrganization
```

Therefore the exact next round is:

# HF19 — Work, Production, Specialization, Firms, Ownership, Capital, Technology and Economic Organization

**HF19 is intentionally not started in this conversation.**

Use [`HF0-HF18-CYCLE-CLOSEOUT-20260817.md`](HF0-HF18-CYCLE-CLOSEOUT-20260817.md)
as the compact cycle index before opening HF19.

## HF19 starting questions

1. What is work relative to action, effort, task and employment?
2. What is production relative to exchange/allocation?
3. What is output relative to welfare/value/revenue?
4. What is productivity relative to effort and capability?
5. What is technology relative to tools, knowledge and capital?
6. What is capital, and why is money not capital by definition?
7. What is specialization relative to current task assignment and persistent skill?
8. What is team production and why is marginal contribution difficult to observe?
9. What is a firm relative to market, organization and legal person?
10. What are transaction and coordination costs?
11. Why do some transactions move inside organizational authority rather than prices?
12. What is ownership relative to possession, access, legal title and residual control?
13. What is an incomplete contract and how does ownership alter investment incentives?
14. What is hold-up / asset specificity?
15. What are scale, scope and complementarity?
16. What is automation relative to substitution, complementarity and capability
    extension?
17. When is AI a tool, worker-like service, delegated agent, organizational member or
    capital asset?
18. What is value creation relative to value capture?
19. How do production systems change Human capability, dependency, power and welfare?
20. What next boundary, if any, emerges after production/economic organization?

## Candidate HF19 falsifiers

- same labor hours, different output because capital/technology;
- same output, different Human effort because automation;
- high effort, low productivity under poor tool/process;
- team output where individual marginal contributions are not separately observable;
- freelancer, employee and partner doing similar tasks under different authority/
  ownership/residual claims;
- same transaction coordinated through market contract versus firm hierarchy;
- asset owner versus physical possessor;
- complete-contract benchmark versus incomplete-contract hold-up;
- open-source peer production without ordinary wage/firm hierarchy;
- specialization raising productivity while increasing dependency;
- AI tool in one organization versus autonomous contractor/agent in another;
- capital investment expanding future feasible set rather than reallocating current
  resources.

## Do not precommit

HF18 does not establish that:

- all work is employment;
- labor hours measure work/value/productivity;
- output equals value or revenue;
- productivity equals effort;
- capital means money;
- firms exist only because transaction costs;
- hierarchy is superior to markets or peer production;
- private ownership is universally efficient/legitimate;
- ownership equals possession;
- incomplete contracts explain all firm boundaries;
- specialization is always beneficial;
- scale economies are universal;
- automation always substitutes Human labor;
- AI is simply labor or simply capital;
- technology is exogenous;
- production growth is welfare growth;
- efficient production determines just distribution.

## Fresh-conversation resume protocol

When Human Foundations resumes in a new conversation:

```text
1. Verify repo: /root/projects/ordivon-human
2. Verify main == origin/main at the final HF18-cycle-closeout commit.
3. Read research/foundations/HF0-HF18-CYCLE-CLOSEOUT-20260817.md.
4. Read research/foundations/HF18-CONTINUATION.md.
5. Do NOT rerun HF0–HF18 unless an explicit FoundationReopenCondition is found.
6. Open Runtime workspace from exact main for HF19.
7. Adopt Host task:human-foundations-hf19-<date>, goal:human-foundations.
8. Start HF19 term separation/falsification directly.
9. Do not pre-plan HF20.
```

## Stop rule

This conversation closes the HF0–HF18 cycle. Do not start HF19 here.
HF19 must expose any later frontier itself.
