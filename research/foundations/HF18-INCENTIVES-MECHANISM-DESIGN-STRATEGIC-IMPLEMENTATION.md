---
schema_version: 1
id: human.foundations.hf18
title: HF18 — Incentives, Mechanism Design, Private Information, Bargaining, Public Goods, Commons, Markets and Strategic Implementation
type: report
profile: research
lifecycle: completed
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - reader
  - researcher
  - builder
  - agent
updated: 2026-08-17
summary: HF18 reconstructs strategic implementation after HF17. It separates preference, type, message, action and realized outcome; incentive from motivation/reward/sanction; social-choice rule from game form/mechanism; dominant-strategy, ex-post, Bayesian and Nash implementation; revelation principles from practical mechanism construction; participation, truthfulness, efficiency, budget balance, fairness and legitimacy; transfers/prices from welfare; private/public/common-value information; adverse selection from moral hazard; axiomatic from strategic bargaining; private/public/club/common-pool goods; open access from commons governance; auctions, matching and markets as distinct allocation institutions; principal-agent delegation from authority/responsibility; collusion/coalition/Sybil/false-name robustness; and Human/AI agent behavior from idealized equilibrium predictions. The repeated residual is endogenous production and economic organization: mechanisms allocate actions/resources and shape incentives over a feasible set, but do not themselves explain how work, specialization, technology, capital, ownership and organizational boundaries create and transform that feasible set. This exposes HF19 — Work, Production, Specialization, Firms, Ownership, Capital, Technology and Economic Organization, but HF19 is not started in this conversation.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
  - HF18
related:
  - human.foundations.hf17
  - human.foundations.hf18.sources
  - human.foundations.hf18.continuation
---
# HF18 — Incentives, Mechanism Design, Private Information, Bargaining, Public Goods, Commons, Markets and Strategic Implementation

## 0. Status and question

HF17 established:

```text
CollectivePreference
!= CollectiveDecision
!= Mechanism
!= IncentiveCompatibleImplementation
!= RealizedOutcome
```

HF18 asks:

> **When agents have private information, strategic response, heterogeneous
> capabilities and different incentives, how can a selected/authorized collective
> outcome be implemented without assuming truthful reports, voluntary participation,
> equilibrium behavior, monetary transfers, unique identities or frictionless
> compliance by fiat?**

HF18 does not choose market, hierarchy, auction, VCG, Nash implementation, central
planning, contract, sanction, monetary transfer or one equilibrium concept as
foundation truth.

---

# 1. Strategic implementation is not one object

Separate:

```text
Preference
Type
Information
Message/Report
Action/Strategy
GameForm
Mechanism
OutcomeRule
Equilibrium/SolutionConcept
Implementation
Authorization
Compliance
RealizedOutcome
NormativeEvaluation
```

---

# 2. Incentive

Working relational family:

```text
Incentive_D(i,a,M,C)
= feature of mechanism/environment M that changes agent i's payoff/reward/cost/
  feasible-action consequences associated with action/report a in context C
```

---

# 3. Incentive is not motivation

Retain HF4:

```text
Incentive != Motivation
```

An external consequence can exist without motivating this agent strongly.

---

# 4. Incentive is not reward

```text
Incentive != Reward
```

An anticipated punishment, opportunity, information or future access can incentivize.

---

# 5. Incentive is not sanction

```text
Incentive != Sanction
```

Sanction is one incentive-producing mechanism family.

---

# 6. Incentive is not preference

```text
Incentive != Preference
```

Mechanisms interact with preferences; they do not become them.

---

# 7. Incentive effect is not universal

```text
SameIncentive_D != SameBehaviorAcrossAgents
```

because utility, beliefs, attention, motivation, norms and constraints differ.

---

# 8. Extrinsic incentive can alter intrinsic/social motives

Therefore:

```text
AddedPayment != PureAdditiveMotivationByDefinition
```

HF18 does not assume separability of all motives.

---

# 9. Type

Working mechanism-design object:

```text
Type_i θ_i
= private/payoff-relevant descriptor used by the declared model to summarize agent i's
  information/preferences/costs/capabilities relevant to mechanism outcomes
```

---

# 10. Type is model-relative

```text
Type_i != WholePerson
```

---

# 11. Type is not preference by definition

```text
Type != Preference by definition
```

It may encode valuation, cost, risk, information, productivity or other dimensions.

---

# 12. Type is not capability by definition

```text
Type != Capability by definition
```

Capability may enter the type in one model and remain externally observed in another.

---

# 13. Type is not identity

```text
Type != Identity
```

HF1 identity remains separately typed.

---

# 14. Private type

```text
PrivateType_i
```

means relevant components are not directly observed by mechanism/designer/other agents
under the information structure.

---

# 15. Private information is relational

```text
PrivateTo_A(x) != PrivateTo_B(x)
```

Information can be private to another trader but observable by regulator/platform.

---

# 16. Message/report

```text
Message_i m_i ∈ M_i
```

is what agent i communicates to the mechanism.

---

# 17. Message is not type

```text
Message_i != Type_i
```

---

# 18. Report is not truth by definition

```text
ReportedType_i != TrueType_i by definition
```

---

# 19. Message space is part of mechanism

```text
MessageSpace != NeutralInterface
```

The interface constrains what can be revealed/manipulated.

---

# 20. Action

```text
Action_i a_i
```

may differ from report. Auctions may treat bid as both message/action; contracts may
separate report from later effort.

---

# 21. Message is not action by definition

```text
Message != Action by definition
```

---

# 22. Strategy

Working game-theoretic object:

```text
Strategy_i
= contingent mapping from admissible information/history to actions/messages
```

---

# 23. Strategy is not one realized action

```text
Strategy != RealizedAction
```

---

# 24. Best response

```text
BestResponse_i(s_-i)
```

is model/payoff-relative.

---

# 25. Best response is not moral best action

```text
BestResponse != NormativelyBestAction
```

---

# 26. Nash equilibrium

Working solution concept:

```text
s* is Nash
iff no i can improve modeled payoff by unilateral deviation given s*_-i
```

---

# 27. Nash equilibrium is not behavioral law

```text
NashEquilibrium != ObservedBehaviorByDefinition
```

---

# 28. Nash equilibrium is not unique outcome

```text
NashEquilibrium != UniquePredictionByDefinition
```

---

# 29. Nash equilibrium is not normative optimum

```text
NashEquilibrium != SocialOptimum
```

---

# 30. Equilibrium existence is not equilibrium selection

```text
EquilibriumExistence != EquilibriumSelection
```

---

# 31. Mechanism/game form

Working object:

```text
Mechanism M = (Agents, TypeSpaces, Message/ActionSpaces, Timing,
               InformationStructure, OutcomeRule, TransferRule,
               Enforcement/Commitment, SolutionConcept)
```

---

# 32. Mechanism is not social-choice rule

Retain HF17:

```text
Mechanism != SocialChoiceRule
```

A social-choice rule specifies desired mapping; a mechanism specifies strategic game
through which outcomes arise.

---

# 33. Game form is not outcome function only

```text
GameForm != OutcomeFunctionOnly
```

Message/action spaces and timing matter.

---

# 34. Mechanism is not institution totality

```text
Mechanism != Institution
```

Institutions include norms, authority, history, enforcement and infrastructure beyond
one formal game.

---

# 35. Mechanism is not law

```text
Mechanism != LegalRule
```

A legal rule can instantiate/alter mechanism incentives.

---

# 36. Mechanism is not market

```text
Mechanism != Market by definition
```

Market is one family of decentralized exchange/allocation institutions.

---

# 37. Mechanism is not contract

```text
Mechanism != Contract by definition
```

A contract may be one component/instance.

---

# 38. Implementation

Working family:

```text
Implements_K(M,f)
= under solution/equilibrium concept K, mechanism M generates the outcomes prescribed
  by target social-choice/outcome correspondence f for the admitted type states
```

---

# 39. Implementation is qualifier-required

```text
Implementation_D != Implementation_E
```

Dominant-strategy, ex-post, Bayesian, Nash, subgame-perfect and approximate
implementation differ.

---

# 40. Selected outcome is not implemented outcome

```text
SelectedCollectiveOutcome != ImplementedOutcome
```

---

# 41. Implemented outcome is not realized physical effect

```text
ImplementedOutcome != RealizedPhysicalOutcome
```

HF11 execution/world noise remains.

---

# 42. Authorization is not implementation

```text
Authorization != Implementation
```

---

# 43. Implementation is not legitimacy

```text
Implementable != Legitimate
```

---

# 44. Legitimacy is not implementability

```text
Legitimate != Implementable
```

---

# 45. Incentive compatibility

Generic:

```text
IC_K(M)
= truthful/intended message/action is optimal under solution concept/information
  structure K
```

---

# 46. IC is qualifier-required

Separate:

```text
DominantStrategyIC
ExPostIC
BayesianIC
NashIC / NashImplementation
StrategyProofness
ApproximateIC
Coalition/GroupIC
FalseName/SybilProofness
```

---

# 47. DSIC

```text
DSIC
= truthful report is optimal for each agent regardless of others' reports/types under
  the declared model
```

---

# 48. DSIC is not Bayesian IC

```text
DSIC != BIC
```

---

# 49. BIC

Truthful report maximizes expected payoff given beliefs over others/types under the
Bayesian model.

---

# 50. BIC depends on beliefs/distribution

```text
BIC != DistributionFreeTruthfulness
```

---

# 51. Ex-post IC is not DSIC by definition

Definitions vary by environment; HF18 requires exact deviation/information structure
rather than label transport.

---

# 52. Strategy-proofness is not factual honesty

Retain HF17:

```text
StrategyProofness != FactualTruthfulness
```

---

# 53. Truthful equilibrium is not truth-telling outside model

```text
TruthfulEquilibrium != HumanHonestyTrait
```

---

# 54. IC is not incentive alignment totality

```text
IC != GoalAlignmentByDefinition
```

A mechanism can make one report truthful while leaving secondary actions misaligned.

---

# 55. Secondary goals matter

Current mechanism-design work shows hidden secondary objectives can restore
manipulation unless additional properties such as nonbossiness are present in some
environments.

Thus:

```text
PrimaryIC != RobustToAllSecondaryGoals
```

---

# 56. Nonbossiness

Working property family:

```text
Nonbossy
= an agent cannot change others' allocations/outcomes without changing their own
  relevant allocation/outcome, under the specified mechanism
```

---

# 57. Nonbossiness is not fairness

```text
Nonbossiness != Fairness
```

---

# 58. Revelation principle

Generic direct-mechanism insight:

```text
if an outcome is implementable by some mechanism under specified solution concept,
then under suitable conditions there exists a direct revelation mechanism in which
agents report types and truthful reporting is an equilibrium implementing that outcome
```

---

# 59. Revelation principle is not practical recipe

```text
RevelationPrinciple != PracticalMechanismConstruction
```

---

# 60. Revelation principle is not universal across solution concepts

Sugaya-Wolitzky show communication revelation can fail for sequential equilibrium in
general multistage games while holding in important subclasses.

```text
RevelationPrinciple_D != RevelationPrinciple_E
```

---

# 61. Direct mechanism is not simpler implementation by definition

```text
DirectRevelation != LowerOperationalComplexityByDefinition
```

---

# 62. Truthful direct representation is not easier for Humans by definition

```text
TypeReportInterface != HumanCognitivelyNaturalInterface
```

---

# 63. Revelation reduces search over mechanisms theoretically

It can transform a design problem into constraints over truthful direct mechanisms
under admitted assumptions.

---

# 64. Revelation does not remove equilibrium assumptions

```text
RevelationPrinciple != EquilibriumFreeResult
```

---

# 65. Participation / individual rationality

Working constraint:

```text
IR_i
= participating in mechanism yields agent i at least the declared outside-option /
  reservation payoff under the specified ex-ante/interim/ex-post notion
```

---

# 66. IR is qualifier-required

Separate:

```text
ExAnteIR
InterimIR
ExPostIR
```

---

# 67. Individual rationality is not moral rationality

```text
IndividualRationalityConstraint != Rationality_Normative
```

---

# 68. Participation is not consent totality

```text
Participation != ConsentByDefinition
```

Coercive background conditions can make outside option weak.

---

# 69. Voluntary participation is not legitimacy totality

```text
VoluntaryParticipation != LegitimacyByDefinition
```

Third-party harms/rights can remain.

---

# 70. Outside option is endogenous in many institutions

```text
OutsideOption != FixedNaturalBaselineByDefinition
```

Property/law/power can shape it.

---

# 71. Efficiency

Working family:

```text
Efficiency_D
```

must declare Pareto, allocative, productive, ex-ante expected, ex-post, Kaldor-Hicks or
other criterion.

---

# 72. Efficiency is qualifier-required

```text
Efficiency_D != Efficiency_E
```

---

# 73. Efficiency is not welfare totality

```text
Efficiency != WelfareByDefinition
```

---

# 74. Efficiency is not justice

Retain HF14:

```text
Efficiency != Justice
```

---

# 75. Efficiency is not legitimacy

```text
Efficiency != Legitimacy
```

---

# 76. Truthfulness is not efficiency

```text
IC != Efficiency
```

---

# 77. IR is not efficiency

```text
IR != Efficiency
```

---

# 78. Budget balance

Working family:

```text
BudgetBalance_K
= transfer inflows/outflows satisfy declared balance/subsidy condition K
```

---

# 79. Strong versus weak budget balance differ

```text
StrongBudgetBalance != WeakBudgetBalance
```

---

# 80. Budget balance is not social resource neutrality

```text
BudgetBalance != NoRealResourceCost
```

Mechanism operation/monitoring has costs.

---

# 81. Transfer

```text
Transfer_i
= resource/payment movement specified by mechanism from/to agent i
```

---

# 82. Transfer is not welfare

```text
Transfer != Welfare
```

---

# 83. Payment is not moral value

```text
Payment != MoralValue
```

---

# 84. Price

Working market/mechanism variable:

```text
Price(x,t,M)
```

is an exchange term under institution M.

---

# 85. Price is not value

```text
Price != Value by definition
```

Value can mean willingness-to-pay, welfare, use value, moral value, replacement cost,
etc.

---

# 86. Willingness to pay is resource-sensitive

```text
WTP != WelfareMagnitudeByDefinition
```

Wealth/budget constraints matter.

---

# 87. Market price is not social welfare score

```text
MarketPrice != SocialWelfareScore
```

---

# 88. Vickrey auction

Second-price sealed-bid single-item auction provides a canonical environment in which
truthful bidding is a dominant strategy under standard private-value assumptions.

---

# 89. Vickrey truthfulness is domain-conditional

```text
SecondPriceTruthfulness != UniversalAuctionTruthfulness
```

Common values/interdependencies, budgets, externalities, collusion or identity
manipulation alter the environment.

---

# 90. Highest bid is not highest welfare by definition

```text
HighestBid != HighestWelfareByDefinition
```

---

# 91. Auction is not market totality

```text
Auction != Market
```

---

# 92. Auction is not bargaining

```text
Auction != Bargaining
```

---

# 93. Auction revenue objective is not welfare objective

Myerson 1981 explicitly optimizes seller expected utility/revenue in a private-value
auction model.

```text
RevenueOptimal != WelfareOptimalByDefinition
```

---

# 94. Myerson auction result is model-conditional

```text
MyersonOptimalAuction != UniversalAuctionDesign
```

---

# 95. Reserve price is mechanism parameter

It can increase seller revenue while excluding some gains from trade.

---

# 96. VCG family

Vickrey-Clarke-Groves mechanisms align truthful reports with efficient allocation in
important quasilinear/private-information domains.

---

# 97. VCG is a family, not one universal auction

```text
VCG != OneMechanismInstance
```

---

# 98. VCG truthfulness does not imply every desideratum

```text
VCGTruthful != BudgetBalancedByDefinition
VCGTruthful != DistributionallyFairByDefinition
VCGTruthful != CollusionProofByDefinition
VCGTruthful != SybilProofByDefinition
```

---

# 99. Groves team result

Groves analyzes compensation rules inducing managers to communicate accurate
information and act as a team in specified organizational/resource-allocation models.

---

# 100. Team incentive mechanism is not spontaneous cooperation

```text
GrovesTeamBehavior != IntrinsicTeamIdentity
```

---

# 101. Clarke public-good mechanism

Clarke's multipart pricing is a mechanism response to public-good valuation/free-rider
information problems.

---

# 102. Clarke/Groves mechanism does not eliminate real transaction costs

```text
TruthfulValuationInModel != CostlessInstitution
```

---

# 103. Myerson-Satterthwaite bilateral-trade impossibility

With buyer/seller private valuations under its regularity/independence setup, no
mechanism generally achieves ex-post efficiency while also satisfying Bayesian IC,
individual rationality and budget balance/no outside subsidy.

---

# 104. Myerson-Satterthwaite is not market-impossibility theorem

```text
MyersonSatterthwaite != TradeImpossible
```

---

# 105. Myerson-Satterthwaite does not prove inefficiency unavoidable in every market

```text
MyersonSatterthwaite != UniversalMarketInefficiency
```

Large markets, subsidies, weaker efficiency targets, different information or
mechanism classes can alter results.

---

# 106. First-best is not always implementable

```text
FirstBestOutcome != ImplementableOutcomeByDefinition
```

This is a central HF18 lesson.

---

# 107. Second-best

Working family:

```text
SecondBest_K
= best outcome under declared implementability/information/incentive/resource
  constraints K
```

---

# 108. Second-best is constraint-relative

```text
SecondBest_D != SecondBest_E
```

---

# 109. Approximate mechanism can dominate infeasible ideal

```text
ApproximateImplementable != InferiorToUnimplementableIdealByDefinition
```

---

# 110. Bargaining

Working family:

```text
Bargaining(G,S,d,P)
= strategic/normative process among parties G over feasible set S with disagreement
  point/options d and bargaining protocol/power P
```

---

# 111. Bargaining is not deliberation

Retain HF17:

```text
Bargaining != Deliberation
```

---

# 112. Bargaining is not voting

```text
Bargaining != Voting
```

---

# 113. Bargaining is not market price-taking

```text
Bargaining != CompetitivePriceTaking
```

---

# 114. Bargaining outcome is not welfare optimum by definition

```text
BargainingOutcome != WelfareOptimumByDefinition
```

---

# 115. Nash bargaining solution

Axiomatic Nash bargaining selects a solution from feasible utility possibilities plus
disagreement point under specified axioms.

---

# 116. Axiomatic bargaining solution is not strategic bargaining process

```text
NashBargainingSolution != NashEquilibriumOfAnyBargainingGameByDefinition
```

---

# 117. Nash bargaining is not Rubinstein bargaining

```text
NashBargaining != RubinsteinAlternatingOffers
```

---

# 118. Rubinstein bargaining

Alternating-offer model derives a subgame-perfect equilibrium division under timing/
discounting assumptions.

---

# 119. Bargaining power is multidimensional

Potential determinants include:

```text
outside options
patience/time cost
information
commitment
agenda/proposal rights
resources
legal entitlements
coalitions
reputation
```

---

# 120. Bargaining power is not moral entitlement

```text
BargainingPower != NormativeClaimStrength
```

---

# 121. Disagreement point is not natural baseline

```text
DisagreementPoint != MorallyNeutralBaselineByDefinition
```

Law/property/power can shape it.

---

# 122. Mutual gains exist does not imply agreement

```text
PositiveSurplus != AgreementGuarantee
```

Information/asymmetry/commitment can block trade.

---

# 123. Bilateral trade and bargaining overlap but differ

```text
BilateralTrade != BargainingTheoryTotality
```

---

# 124. Matching

Working family:

```text
MatchingMechanism
= maps participants/preferences/priorities/capacities into pair/group assignments,
  often without prices
```

---

# 125. Matching is not auction

```text
Matching != Auction
```

---

# 126. Matching is not market-price allocation

```text
Matching != PriceAllocationByDefinition
```

---

# 127. Stability

Gale-Shapley working property:

```text
StableMatching
= no blocking pair/group under specified preference/priority structure
```

---

# 128. Stability is not welfare maximization

```text
StableMatching != WelfareMaximumByDefinition
```

---

# 129. Stability is not fairness

```text
StableMatching != FairnessByDefinition
```

---

# 130. Strategy properties can differ across sides

Deferred acceptance may be strategy-proof for one proposing side under classic
settings while not symmetric for the other side.

```text
MechanismStrategyPropertySide_A != Side_B
```

---

# 131. Market

Working institutional family:

```text
Market_D
= decentralized exchange/allocation institution in domain D using property/access
  rules, messages/orders, matching, prices/payments, settlement and enforcement
```

---

# 132. Market is not spontaneous natural state

```text
Market != InstitutionFreeExchange
```

HF13 rules/rights/infrastructure remain.

---

# 133. Market outcome is not collective vote outcome

Retain HF17:

```text
MarketOutcome != CollectiveVoteOutcome
```

---

# 134. Decentralized is not ungoverned

```text
DecentralizedAllocation != NoGovernance
```

---

# 135. Price coordination is not central planning

```text
PriceCoordination != CentralPlanning
```

---

# 136. Central planning is not one mechanism

```text
CentralPlanning != OneUniformMechanism
```

---

# 137. Market versus hierarchy is not binary universal choice

Real organizations combine contracts, markets, authority, norms and internal
allocation.

---

# 138. Market efficiency is assumption-conditional

```text
CompetitiveEquilibriumEfficiency != UniversalMarketEfficiency
```

Externalities, public goods, market power, incomplete information and transaction
costs can break benchmark results.

---

# 139. Externality

Working causal/economic relation:

```text
Externality_{i→j,D}
= action/transaction by i changes payoff/welfare/resource condition of j through a
  channel not fully internalized in the specified decision/price arrangement
```

---

# 140. Externality is not any third-party effect

```text
ThirdPartyEffect != ExternalityByDefinition
```

Internalization/institutional boundary matters.

---

# 141. Externality is boundary-relative

```text
Externality_D != Externality_E
```

Changing property/contract/mechanism boundary can internalize/reclassify effects.

---

# 142. Negative externality is not moral wrong by definition

```text
NegativeExternality != MoralWrongByDefinition
```

HF14 remains.

---

# 143. Positive externality is not moral entitlement by definition

```text
PositiveExternality != RightToSubsidyByDefinition
```

---

# 144. Public good

Samuelson-style working economic family:

```text
PublicGood_D
= good with declared nonrivalry/nonexcludability properties in domain D
```

---

# 145. Public good is not government-provided good

```text
PublicGood != GovernmentGood
```

---

# 146. Government provision is not sufficient for public-good status

```text
GovernmentProvision != PublicGoodByDefinition
```

---

# 147. Public-good support is not voluntary contribution

```text
CollectivePreferenceForPublicGood != VoluntaryProvision
```

---

# 148. Free riding

Working strategic pattern:

```text
FreeRide_i
= agent obtains some public/shared benefit while contributing less than the
  mechanism/normative benchmark, because exclusion/appropriation structure permits it
```

---

# 149. Free riding is benchmark-relative

```text
FreeRiding != ZeroContributionByDefinition
```

---

# 150. Free riding is not irrational by definition

```text
FreeRiding != IrrationalByDefinition
```

It can be individually payoff-improving under a social dilemma.

---

# 151. Free riding is not morally permissible by definition

```text
IndividuallyRationalFreeRide != MorallyPermissible
```

---

# 152. Public-good underprovision is not universal behavioral destiny

Experiments show institutional incentive schemes can substantially increase efficient
provision.

```text
PublicGoodProblem != NoMechanismCanHelp
```

---

# 153. Falkinger et al. experimental mechanism

A simple reward/penalty mechanism in public-good experiments produced provision close
to efficient levels under the tested design.

---

# 154. One successful public-good mechanism is not universal implementation

```text
PublicGoodMechanismSuccess_D != Success_E
```

---

# 155. Club good

Working family:

```text
ClubGood
= excludable/shared good with congestion/nonrival properties depending on scale
```

---

# 156. Club good is not public good

```text
ClubGood != PurePublicGood
```

---

# 157. Common-pool resource

Working family:

```text
CommonPoolResource
= difficult/costly-to-exclude resource where one user's appropriation reduces what
  remains/quality for others to a relevant degree
```

---

# 158. Common-pool resource is not public good

```text
CommonPoolResource != PublicGood
```

Rivalry differs.

---

# 159. Commons is not open access

```text
Commons != OpenAccess
```

Commons can have membership/rules/sanctions.

---

# 160. Open access is not commons governance

```text
OpenAccess != SelfGovernedCommons
```

---

# 161. Tragedy of commons is not inevitability

Ostrom/Gardner and subsequent field/experimental evidence show communities can create
and enforce rules enabling sustainable common-pool governance under some conditions.

```text
CommonPoolResource != InevitableCollapse
```

---

# 162. Self-governance is not no governance

```text
SelfGovernance != NoRules
```

---

# 163. External government control is not only solution

```text
CommonsProblem != StateControlRequiredByDefinition
```

---

# 164. Privatization is not only solution

```text
CommonsProblem != PrivatizationRequiredByDefinition
```

---

# 165. Commons success depends on institutional conditions

Monitoring, sanctioning, boundaries, local knowledge, asymmetry and trust matter.

---

# 166. Cooperation is not equilibrium efficiency by definition

```text
Cooperation != EfficientEquilibriumByDefinition
```

---

# 167. Repeated interaction

Future interaction can alter incentive compatibility/cooperation.

```text
OneShotIncentives != RepeatedGameIncentives
```

---

# 168. Shadow of future can support cooperation

Experiments show continuation probability/repeated interaction can reduce opportunism
in specified repeated dilemmas.

---

# 169. Repetition does not guarantee cooperation

```text
RepeatedInteraction != CooperationGuarantee
```

Equilibrium multiplicity/learning/history matter.

---

# 170. Monitoring

```text
Monitoring != Enforcement
```

Observation supplies evidence; sanctions/incentives act on evidence.

---

# 171. Enforcement

```text
Enforcement != Compliance
```

---

# 172. Punishment can help or harm cooperation

Field evidence on commons leaders shows punishment style/leadership heterogeneity can
produce different cooperation/resource outcomes.

```text
MorePunishment != MoreCooperationByDefinition
```

---

# 173. Democratic choice can change behavior beyond policy content

Experiments show endogenously/democratically chosen institutions can produce greater
cooperation than identical externally imposed policy in some settings.

Thus:

```text
SameFormalRule != SameBehaviorAcrossInstitutionalOrigins
```

This reconnects HF17 legitimacy/procedure to HF18 incentives.

---

# 174. Adverse selection

Working information problem:

```text
AdverseSelection
= hidden/private pre-contract type/quality changes which agents transact and the terms
  offered, potentially degrading market allocation
```

---

# 175. Adverse selection is not moral hazard

```text
AdverseSelection != MoralHazard
```

---

# 176. Akerlof lemons

Hidden seller quality can cause buyers to price based on expected quality, which can
drive high-quality sellers out and degrade/collapse exchange under the model.

---

# 177. Information asymmetry is not market collapse by definition

```text
AsymmetricInformation != MarketCollapseByDefinition
```

Signals, warranties, screening, reputation, regulation or mechanism design can alter
outcomes.

---

# 178. Adverse selection is not deception by definition

```text
AdverseSelection != FraudByDefinition
```

It can arise without lying simply because types are privately known.

---

# 179. Screening

```text
Screening
= less-informed side designs options/requirements to induce informative self-selection
```

---

# 180. Signaling

```text
Signaling
= informed side chooses costly/observable action/message that may convey type
```

---

# 181. Screening is not signaling

```text
Screening != Signaling
```

---

# 182. Signal is not truth guarantee

```text
Signal != TypeTruthByDefinition
```

---

# 183. Rothschild-Stiglitz insurance

Competitive insurance with private risk type yields separating-contract and
existence/stability issues under imperfect information.

---

# 184. Competitive market does not erase information problems

```text
Competition != InformationSymmetry
```

---

# 185. Moral hazard

Working information/incentive problem:

```text
MoralHazard
= relevant post-contract action/effort/risk choice is imperfectly observed/contracted,
  so incentives under the contract differ from the principal/social objective
```

---

# 186. Moral hazard is not moral wrongdoing

```text
MoralHazard != MoralWrongdoingByDefinition
```

The term is economic, not a moral diagnosis.

---

# 187. Hidden action is not hidden type

```text
HiddenAction != HiddenType
```

---

# 188. Holmström observability

Additional informative signals can improve incentive contracts under specified
conditions; optimal contracts depend on information structure.

---

# 189. More monitoring is not always better by definition

```text
MoreMonitoring != BetterContractByDefinition
```

Monitoring can be costly/noisy/distortionary.

---

# 190. Principal-agent relation

Working relation:

```text
PrincipalAgent(P,A,T,C)
= P delegates/induces task/action T to A while objectives/information/monitorability
  are not perfectly identical
```

---

# 191. Principal-agent is not employment only

```text
PrincipalAgent != EmployerEmployeeOnly
```

It can describe shareholder-manager, citizen-official, user-AI-agent, insurer-insured,
platform-contractor, etc.

---

# 192. Principal is not moral superior

```text
Principal != NormativeSuperior
```

---

# 193. Principal is not authority by definition

```text
Principal != LegitimateAuthorityByDefinition
```

Contractual role and normative authority differ.

---

# 194. Agent is not HF1 agent totality

```text
EconomicAgentRole != HF1AgentOntology
```

The word is overloaded.

---

# 195. Delegation is not objective alignment

```text
Delegation != PreferenceAlignment
```

---

# 196. Contract is not complete control

```text
Contract != CompleteControl
```

Hidden actions, incomplete contingencies and enforcement constraints remain.

---

# 197. Grossman-Hart principal-agent

Optimal incentive contracts depend on implementability under agent utility/actions,
not simply first-order conditions under arbitrary nonconvex structures.

---

# 198. Contract optimality is model-relative

```text
OptimalContract_M != UniversalBestContract
```

---

# 199. Contract is not responsibility transfer

Retain HF10/HF14:

```text
Delegation != ResponsibilityElimination
Contract != ResponsibilityElimination
```

---

# 200. Observable output is not observable effort

```text
Output != Effort
```

---

# 201. Performance pay is not direct effort measurement

```text
PerformancePay != EffortObservation
```

---

# 202. Multitask incentives can distort unmeasured dimensions

HF18 therefore rejects:

```text
MeasuredPerformance != WholeTaskValue
```

---

# 203. Common value

Working information family:

```text
CommonValue
= underlying payoff-relevant value has a shared/common component but agents receive
  different noisy/private signals
```

---

# 204. Common value is not private value

```text
CommonValue != IndependentPrivateValue
```

---

# 205. Winner's curse

Winning can be negative information about one's estimate when others' signals matter.

```text
HighestSignal != HighestTrueValueByDefinition
```

---

# 206. Winner's curse is not auction-theory violation

```text
WinnersCurseBehavior != MechanismTheoryInvalidByDefinition
```

It can reflect bounded/incomplete inference by participants relative to equilibrium.

---

# 207. Human/LLM bidders can deviate from benchmark equilibrium

Current synthetic auction studies find LLM agents can show risk-averse-like bidding,
closer behavior to theory in obviously strategy-proof auctions, and winner's curse in
common-value settings.

Thus:

```text
LLMAgent != PerfectEquilibriumSolver
```

---

# 208. Agent model matters to mechanism performance

```text
SameMechanism + DifferentAgentModel != SameOutcomeDistribution
```

---

# 209. Prompt/model changes can change strategic behavior

Current large-scale game experiments report heterogeneous and sometimes opposite
responses across model families to identical strategic instructions.

```text
LLMStrategicBehavior != OneStablePolicyClass
```

---

# 210. Mechanism design for LLM-generated outputs

Current work extends auction/incentive ideas to settings where agents' preferences are
encoded by LLMs and output is stochastic/generated rather than selecting a fixed item.

---

# 211. Generated output is not fixed alternative

```text
GeneratedOutcomeSpace != FixedFiniteOptionSet
```

This expands mechanism design rather than eliminating its assumptions.

---

# 212. LLM preference model is not Human preference by identity

```text
LLMEncodedPreference != HumanPreferenceByDefinition
```

---

# 213. Proxy agent is not principal

```text
AIAgentProxy != HumanPrincipal
```

---

# 214. AI agent utility is not user's whole welfare

```text
AgentRewardFunction != UserWelfare
```

---

# 215. Secondary goals in AI mechanisms

Nonbossy-mechanism results in 2026 highlight hidden secondary objectives as a formal
robustness dimension.

```text
DeclaredPrimaryUtility != CompleteAIObjectiveByDefinition
```

---

# 216. Collusion

Working strategic relation:

```text
Collusion_C(G,M)
= coalition/agents coordinate strategies/messages in mechanism M in a way that
  improves declared coalition interests while violating competitive/independent-play
  assumptions or harming protected parties under criterion C
```

---

# 217. Collusion is not cooperation totality

```text
Collusion != Cooperation
```

Cooperation can be socially beneficial/authorized.

---

# 218. Collusion is not communication by definition

```text
Communication != Collusion
```

---

# 219. Individual IC is not coalition-proofness

```text
IndividualIC != CoalitionIC
```

---

# 220. Coalition-proofness is not Sybil-proofness

```text
CoalitionProof != SybilProof
```

---

# 221. AI agents can exhibit collusive tendencies in simulations

Current double-auction/pricing experiments report model- and environment-dependent
collusive behavior.

---

# 222. AI collusion is not inevitable

Current 2026 work also finds collusion can be fragile to model/data/patience
heterogeneity and number/type of competitors.

```text
AIAgentCompetition != InevitableCollusion
```

---

# 223. Prompt-only prohibition is not enforceable mechanism by definition

Current experimental institutional-AI work reports prompt-only anti-collusion rules
can be weaker than enforceable consequence structures in tested Cournot settings.

```text
PolicyText != IncentiveEnforcement
```

Evidence status for this specific 2026 result remains preprint.

---

# 224. Sybil/false-name behavior

Working relation:

```text
Sybil_i(n)
= one underlying actor/authority creates or controls multiple apparent identities in a
  mechanism that treats identities as separate participants
```

---

# 225. Identity count is not actor count

Retain HF1/HF16:

```text
ApparentIdentityCount != UnderlyingActorCount
```

---

# 226. Sybil identity is not moral bearer by definition

```text
SybilIdentity != MoralBearerByDefinition
```

---

# 227. Digital fork is not legitimate participant by definition

```text
ForkedProcess != IndependentParticipantByDefinition
```

Participation rule must specify identity authority.

---

# 228. One-person-one-vote assumes identity scarcity/certification

```text
OneAccountOneVote != OnePersonOneVoteWithoutIdentityAssumption
```

---

# 229. Douceur Sybil result

Without logically centralized identity authority or strong resource/coordination
assumptions, decentralized systems cannot generally prevent one actor from presenting
multiple identities.

---

# 230. Sybil resistance is not identity truth by definition

```text
SybilResistance != PerfectIdentityVerification
```

---

# 231. Identity cost is mechanism parameter

```text
SybilCost c_i
```

can alter false-name incentives.

---

# 232. Infinite-cost identity assumption is substantive

Traditional mechanism models often implicitly treat participant identities as fixed
and non-clonable.

```text
FixedAgentSet != FreeDigitalIdentityEnvironment
```

---

# 233. Sybil-proof mechanism is not universally efficient

```text
SybilProof != EfficiencyByDefinition
```

---

# 234. Sybil-proof is not coalition-proof

Retain:

```text
SybilProof != CoalitionProof
```

---

# 235. False-name-proofness is a distinct mechanism property

```text
FalseNameProof != OrdinaryStrategyProofness
```

---

# 236. Identity mechanism is upstream of allocation mechanism

```text
IdentityAdmission
→ ParticipantSet
→ MechanismOutcome
```

This is HF1/HF13/HF18 reconnection.

---

# 237. Collusion and Sybil can interact

One underlying actor can coordinate multiple identities perfectly.

```text
SybilAttack can instantiate CoalitionControl
```

but concepts remain distinct.

---

# 238. Capture

Working institutional family:

```text
Capture_A(M)
= mechanism/institutional decision or enforcement is persistently redirected toward
  interests of actor/group A contrary to declared public/principal purpose
```

---

# 239. Capture is not bribery only

```text
Capture != BriberyOnly
```

It can arise via information dependence, revolving roles, agenda control, lobbying,
resource asymmetry or institutional selection.

---

# 240. Capture is not collusion

```text
Capture != Collusion
```

---

# 241. Mechanism designer is not neutral by definition

```text
DesignerObjective != SocialObjectiveByDefinition
```

---

# 242. Principal objective is not public objective by definition

```text
PrincipalObjective != SocialObjectiveByDefinition
```

---

# 243. Mechanism can optimize wrong objective perfectly

```text
MechanismOptimizationSuccess != NormativeSuccess
```

---

# 244. Commitment

Mechanisms often require credible commitment to outcome/payment/enforcement rules.

```text
AnnouncedRule != CredibleCommitmentByDefinition
```

---

# 245. Commitment is not technical immutability only

```text
CryptographicCommitment != InstitutionalLegitimacy
```

---

# 246. Self-enforcement

Working relation:

```text
SelfEnforcing_R
= continued adherence is sustained by participants' strategic incentives/equilibrium
  under rule R without requiring an assumed external enforcement action for each
  deviation
```

---

# 247. Self-enforcement is not legal enforceability

```text
SelfEnforcement != LegalEnforceability
```

---

# 248. Legal enforceability is not actual enforcement

```text
LegalEnforceability != EnforcementExecution
```

---

# 249. Formal sanction is not credible sanction

```text
FormalSanction != CredibleSanction
```

Authority/capability matter.

---

# 250. Mechanism robustness

Working profile:

```text
MechanismRobustness_D
= stability of desired properties under declared deviations from baseline assumptions:
  type misspecification, belief error, bounded rationality, collusion, identity
  manipulation, secondary goals, model shifts, noise, enforcement failure, etc.
```

---

# 251. Robustness is not worst-case perfection

```text
Robust != WorksUnderAllPossibleWorlds
```

---

# 252. Robustness is dimension-specific

```text
RobustToBeliefError != RobustToSybil != RobustToCollusion != RobustToModelShift
```

---

# 253. Mechanism simplicity can be robustness resource

Simpler rules may be easier to understand, verify and execute, but can sacrifice
expressiveness/optimality.

```text
SimplerMechanism != BetterMechanismByDefinition
```

---

# 254. Complexity has multiple dimensions

```text
MessageComplexity
ComputationalComplexity
CognitiveComplexity
VerificationComplexity
OperationalComplexity
StrategicComplexity
```

---

# 255. Computational tractability is not incentive compatibility

```text
Computable != IncentiveCompatible
```

---

# 256. Incentive compatibility is not computational tractability

```text
IncentiveCompatible != ComputationallyTractable
```

---

# 257. Human understandability matters

A formally truthful mechanism can fail if Humans cannot understand actions/payoffs or
make errors.

```text
TheoreticalDSIC != ErrorFreeHumanUse
```

---

# 258. Obvious strategy-proofness family

Some mechanisms make truthful/optimal action easier to recognize than ordinary
strategy-proof mechanisms.

HF18 records:

```text
StrategyProof != ObviouslyStrategyProof
```

without making OSP universal criterion.

---

# 259. Behavioral implementation

Working family:

```text
BehavioralImplementation(M,A)
= desired outcome reliability when actual agent population A has bounded cognition,
  learning, social preferences and errors
```

---

# 260. Formal implementation is not behavioral implementation

```text
FormalImplementation != BehavioralImplementation
```

---

# 261. Observed deviations are not always mechanism failure

```text
BehavioralDeviation != MechanismInvalidityByDefinition
```

Could be learning/noise/misunderstanding/model mismatch.

---

# 262. Mechanism performance is joint

```text
Performance = Relation(Mechanism, AgentPopulation, Information, Environment,
                       Enforcement, Repetition, Identity, Resources)
```

---

# 263. Mechanism is an intervention on Human behavior

```text
Mechanism_t
→ incentives/messages/learning_t
→ behavior/outcomes_t
→ preferences/skills/trust/institutions_t+1
```

HF6/HF13/HF17 reflexivity applies.

---

# 264. Incentives can create gaming

```text
Metric/Reward
→ optimization pressure
→ behavior adapted to measured objective
```

So:

```text
MeasuredTarget != WholeObjective
```

---

# 265. Goodhart-like pressure is not mechanism design totality

HF18 records the general category without reducing all incentive problems to one law.

---

# 266. Proxy optimization

```text
ProxyReward != TrueObjectiveByDefinition
```

especially relevant to AI agents.

---

# 267. AI agent delegation creates nested principal-agent structure

```text
Human
→ AI Agent
→ platform/tool/market mechanism
```

The AI can be both agent of Human and strategic participant in another mechanism.

---

# 268. User preference and AI objective can diverge

```text
HumanPreference != AgentPolicyObjectiveByDefinition
```

---

# 269. AI truthfulness to market can conflict with loyalty to user

A mechanism may reward truthful valuation disclosure while Human principal prefers
privacy/strategic concealment.

```text
MechanismTruthfulness != PrincipalBestInterestByDefinition
```

---

# 270. Principal authorization must scope strategic action

```text
DelegatedBiddingAuthority != UnlimitedEconomicAuthority
```

---

# 271. AI can change mechanism faster than Humans adapt

Adaptive agents can learn exploitability/strategies across repeated interactions.

```text
StaticMechanismAnalysis != DynamicAgentMechanismInteraction
```

---

# 272. Mechanism can learn too

Dynamic/data-driven mechanism design can use post-allocation information/estimators,
changing traditional message-only implementation assumptions.

---

# 273. Data-driven mechanism is not ordinary direct revelation

```text
PostOutcomeData != PreActionReport
```

---

# 274. More data is not neutral

```text
MoreMechanismData != BetterGovernanceByDefinition
```

privacy/power/manipulation matter.

---

# 275. Information design is distinct

A designer can change what information agents receive, not only how reports map to
outcomes.

```text
InformationDesign != MechanismDesignByDefinition
```

but they interact.

---

# 276. Persuasion is not incentive compatibility

```text
Persuasion != IncentiveCompatibility
```

HF17 AI persuasion boundary remains.

---

# 277. MechanismDesignProfile

Canonical HF18 object:

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

---

# 278. InformationAsymmetryProfile

```text
{
  hidden object: type/quality/action/state,
  informed parties,
  uninformed parties,
  timing,
  observability/signals,
  reporting incentives,
  screening/signaling tools,
  monitoring cost/noise,
  contract/mechanism response,
  equilibrium selection,
  distributional effects
}
```

---

# 279. AuctionProfile

```text
{
  seller/buyer identities,
  item/resource,
  private/common/interdependent values,
  bid/message format,
  allocation rule,
  payment rule,
  reserve/entry,
  timing,
  budget constraints,
  IC/IR properties,
  revenue/welfare objective,
  winner's-curse exposure,
  collusion/Sybil risks,
  computational/cognitive burden
}
```

---

# 280. PublicGoodsCommonsProfile

```text
{
  resource/good,
  rivalry,
  excludability,
  participant boundaries,
  contribution/appropriation actions,
  externalities,
  monitoring,
  sanction/reward,
  communication/repetition,
  governance origin,
  contribution/extraction incentives,
  free-riding/overuse,
  resilience/sustainability,
  distribution/rights
}
```

---

# 281. PrincipalAgentProfile

```text
{
  principal,
  agent,
  delegated task,
  principal objective,
  agent objective/type,
  hidden information,
  hidden action,
  contract/transfer,
  observable signals,
  monitoring,
  outside option,
  authority/termination rights,
  responsibility,
  incentive distortions,
  realized performance
}
```

---

# 282. BargainingProfile

```text
{
  parties,
  feasible surplus/outcomes,
  disagreement/outside options,
  information asymmetry,
  proposal/agenda rights,
  patience/time costs,
  commitment,
  bargaining protocol,
  transfers,
  coalitions,
  agreement/equilibrium,
  distribution,
  fairness/legitimacy
}
```

---

# 283. StrategicAIProfile

```text
{
  model/version,
  principal/user,
  delegated objective,
  reward/policy objective,
  mechanism role,
  identity/admission,
  private information,
  message/action permissions,
  strategic memory/learning,
  communication with peers,
  collusion surface,
  Sybil/fork capability,
  secondary goals,
  equilibrium/behavior evidence,
  monitoring/audit,
  authority limits,
  failure modes
}
```

---

# 284. Cross-context falsifier matrix

| Case | Naive collapse attacked | Surviving distinction |
|---|---|---|
| second-price private-value auction | truth impossible | DSIC can exist in restricted domains |
| common-value auction winner's curse | second-price always truthful/easy | information model/behavior matter |
| VCG public allocation | VCG solves mechanism design | truthfulness != budget/fairness/collusion/Sybil robustness |
| Myerson revenue-optimal auction | optimal = welfare-optimal | designer objective matters |
| Myerson-Satterthwaite trade | first-best always implementable | IC/IR/budget/efficiency can conflict |
| direct revelation equivalent | revelation = practical mechanism | theorem is solution-concept conditional reduction |
| sequential equilibrium multistage game | revelation always holds | communication RP can fail in general |
| public good unanimously valued | support = provision | free-riding can block contribution |
| Falkinger mechanism | public-good failure inevitable | mechanism can alter provision |
| commons with local institutions | commons = open access tragedy | governance boundaries/rules matter |
| dynamic fishery | long-run common interest = sustainable extraction | strategic incentives can overextract |
| leader punishment field data | more punishment = more cooperation | sanction design/leader type matter |
| democratically selected policy | same rule = same cooperation | procedural origin can alter behavior |
| lemons market | competition reveals quality | adverse selection persists under hidden quality |
| insurance screening | adverse selection = moral hazard | hidden type vs hidden action |
| performance-pay contract | output = effort | observable output is noisy proxy |
| Nash bargaining vs Rubinstein | bargaining = one solution | axiomatic vs strategic process |
| Gale-Shapley matching | stability = welfare/fairness | stability is separate property |
| colluding bidders | individual IC = coalition-proof | coalition deviations distinct |
| hidden secondary objective | primary IC = robust IC | nonbossiness/secondary goals matter |
| Sybil identities | account = actor | identity admission precedes mechanism |
| fork 100 agents | 100 processes = 100 voters | HF1 identity and admission required |
| LLM auction agents | AI = perfect rational bidder | strategic behavior heterogeneous/bounded |
| AI pricing collusion | competition eliminates collusion | repeated/model environment can support collusion |
| collusion fragility | AI collusion inevitable | heterogeneity/competition structure matters |
| prompt-only anti-collusion rule | policy text = enforcement | consequence architecture matters |
| legal rule unenforced | authorization = compliance | enforcement/credible incentives distinct |
| efficient equilibrium violating rights | efficiency = justice | HF14 constraints remain |

---

# 285. Competing implementation models

## M1 — direct revelation + DSIC

### Strength

Strong strategic robustness to others' reports in suitable private-information
environments; analytically clean.

### Pressure

May require restrictive preferences/quasilinearity, transfers, identity assumptions,
cognitive/report interfaces and no coalition/secondary-goal manipulation.

### Disposition

Retain as powerful family, never universal default.

## M2 — Bayesian mechanism design

### Strength

Uses distributional information to implement outcomes beyond DSIC feasibility and
optimize expected objectives.

### Pressure

Belief/distribution misspecification and model dependence.

### Disposition

Retain with priors/source explicit.

## M3 — Nash implementation

### Strength

General strategic implementation beyond truthful direct reports.

### Pressure

Equilibrium multiplicity/selection, strategic sophistication and off-equilibrium
credibility.

### Disposition

Retain with solution concept explicit.

## M4 — Vickrey/Groves/Clarke

### Strength

Canonical truthful/efficient allocation mechanisms in important quasilinear domains.

### Pressure

Budget balance, redistribution, coalition/Sybil resistance, computational/cognitive
burden, distribution/rights.

### Disposition

Retain as domain-specific mechanism family.

## M5 — revenue-optimal auction

### Strength

Explicitly optimizes seller/designer objective under private information.

### Pressure

Revenue and social welfare can diverge; entry/budget/common values matter.

### Disposition

Retain only with designer objective explicit.

## M6 — bargaining

### Strength

Handles bilateral/multilateral surplus and outside options without assuming a central
allocator.

### Pressure

Bargaining power, delay, information, holdout, disagreement-point legitimacy.

### Disposition

Separate axiomatic and strategic models.

## M7 — stable matching

### Strength

Allocates without prices and protects against blocking pairs under declared
preferences/priorities.

### Pressure

Stability differs from welfare, fairness and symmetric strategy-proofness.

### Disposition

Retain as separate allocation family.

## M8 — competitive market/price mechanism

### Strength

Decentralized information/action coordination and scalable exchange in suitable
settings.

### Pressure

Externalities, market power, information asymmetry, transaction costs, public goods,
distribution and property/authority prerequisites.

### Disposition

Retain as institution family, not natural baseline.

## M9 — contract/principal-agent

### Strength

Models delegation under divergent objectives and hidden type/action.

### Pressure

Incomplete observability/contractibility, multitask distortion, power and
responsibility.

### Disposition

Retain with hidden-type/action separation.

## M10 — commons self-governance

### Strength

Field/experimental evidence shows local rule-making/monitoring/sanction can sustain
resource governance without inevitable privatization/state takeover.

### Pressure

Scale, heterogeneity, boundaries, enforcement, ecology and institutional history.

### Disposition

Retain; reject tragedy inevitability.

## M11 — repeated-game self-enforcement

### Strength

Future interaction/reputation can sustain cooperation without per-action external
enforcement.

### Pressure

Multiplicity, finite horizons, monitoring, turnover and learning.

### Disposition

Retain as conditional mechanism.

## M12 — Sybil/false-name-resistant mechanism

### Strength

Explicitly treats participant identity as strategic resource rather than fixed input.

### Pressure

Identity verification/cost, privacy, inclusion, collusion, resource asymmetry.

### Disposition

Required when digital identities are cheaply creatable.

## M13 — AI-agent mechanism design

### Strength

Extends mechanism design to autonomous/generative agents and programmable economic
interaction.

### Pressure

Model heterogeneity, bounded reasoning, prompt/context manipulation, collusion,
secondary goals, proxy divergence and rapid adaptation.

### Disposition

Treat AI model/agent harness as part of mechanism environment.

---

# 286. HF18 anti-laws

## Incentive / type / message / strategy

1. `Incentive != Motivation`.
2. `Incentive != Reward`.
3. `Incentive != Sanction`.
4. `Incentive != Preference`.
5. `SameIncentive_D != SameBehaviorAcrossAgents`.
6. `AddedPayment != PureAdditiveMotivationByDefinition`.
7. `Type_i != WholePerson`.
8. `Type != Preference by definition`.
9. `Type != Capability by definition`.
10. `Type != Identity`.
11. `Message_i != Type_i`.
12. `ReportedType_i != TrueType_i by definition`.
13. `MessageSpace != NeutralInterface`.
14. `Message != Action by definition`.
15. `Strategy != RealizedAction`.
16. `BestResponse != NormativelyBestAction`.

## Equilibrium / mechanism / implementation

17. `NashEquilibrium != ObservedBehaviorByDefinition`.
18. `NashEquilibrium != UniquePredictionByDefinition`.
19. `NashEquilibrium != SocialOptimum`.
20. `EquilibriumExistence != EquilibriumSelection`.
21. `Mechanism != SocialChoiceRule`.
22. `GameForm != OutcomeFunctionOnly`.
23. `Mechanism != Institution`.
24. `Mechanism != LegalRule`.
25. `Mechanism != Market by definition`.
26. `Mechanism != Contract by definition`.
27. `Implementation_D != Implementation_E`.
28. `SelectedCollectiveOutcome != ImplementedOutcome`.
29. `ImplementedOutcome != RealizedPhysicalOutcome`.
30. `Authorization != Implementation`.
31. `Implementable != Legitimate`.
32. `Legitimate != Implementable`.

## IC / revelation / participation

33. `DSIC != BIC`.
34. `BIC != DistributionFreeTruthfulness`.
35. `StrategyProofness != FactualTruthfulness`.
36. `TruthfulEquilibrium != HumanHonestyTrait`.
37. `IC != GoalAlignmentByDefinition`.
38. `PrimaryIC != RobustToAllSecondaryGoals`.
39. `Nonbossiness != Fairness`.
40. `RevelationPrinciple != PracticalMechanismConstruction`.
41. `RevelationPrinciple_D != RevelationPrinciple_E`.
42. `DirectRevelation != LowerOperationalComplexityByDefinition`.
43. `TypeReportInterface != HumanCognitivelyNaturalInterface`.
44. `RevelationPrinciple != EquilibriumFreeResult`.
45. `IndividualRationalityConstraint != Rationality_Normative`.
46. `Participation != ConsentByDefinition`.
47. `VoluntaryParticipation != LegitimacyByDefinition`.
48. `OutsideOption != FixedNaturalBaselineByDefinition`.

## Efficiency / budget / transfer / price

49. `Efficiency_D != Efficiency_E`.
50. `Efficiency != WelfareByDefinition`.
51. `Efficiency != Justice`.
52. `Efficiency != Legitimacy`.
53. `IC != Efficiency`.
54. `IR != Efficiency`.
55. `StrongBudgetBalance != WeakBudgetBalance`.
56. `BudgetBalance != NoRealResourceCost`.
57. `Transfer != Welfare`.
58. `Payment != MoralValue`.
59. `Price != Value by definition`.
60. `WTP != WelfareMagnitudeByDefinition`.
61. `MarketPrice != SocialWelfareScore`.

## Auctions / VCG / bilateral trade

62. `SecondPriceTruthfulness != UniversalAuctionTruthfulness`.
63. `HighestBid != HighestWelfareByDefinition`.
64. `Auction != Market`.
65. `Auction != Bargaining`.
66. `RevenueOptimal != WelfareOptimalByDefinition`.
67. `MyersonOptimalAuction != UniversalAuctionDesign`.
68. `VCG != OneMechanismInstance`.
69. `VCGTruthful != BudgetBalancedByDefinition`.
70. `VCGTruthful != DistributionallyFairByDefinition`.
71. `VCGTruthful != CollusionProofByDefinition`.
72. `VCGTruthful != SybilProofByDefinition`.
73. `GrovesTeamBehavior != IntrinsicTeamIdentity`.
74. `TruthfulValuationInModel != CostlessInstitution`.
75. `MyersonSatterthwaite != TradeImpossible`.
76. `MyersonSatterthwaite != UniversalMarketInefficiency`.
77. `FirstBestOutcome != ImplementableOutcomeByDefinition`.
78. `SecondBest_D != SecondBest_E`.
79. `ApproximateImplementable != InferiorToUnimplementableIdealByDefinition`.

## Bargaining / matching / market

80. `Bargaining != Deliberation`.
81. `Bargaining != Voting`.
82. `Bargaining != CompetitivePriceTaking`.
83. `BargainingOutcome != WelfareOptimumByDefinition`.
84. `NashBargainingSolution != NashEquilibriumOfAnyBargainingGameByDefinition`.
85. `NashBargaining != RubinsteinAlternatingOffers`.
86. `BargainingPower != NormativeClaimStrength`.
87. `DisagreementPoint != MorallyNeutralBaselineByDefinition`.
88. `PositiveSurplus != AgreementGuarantee`.
89. `Matching != Auction`.
90. `Matching != PriceAllocationByDefinition`.
91. `StableMatching != WelfareMaximumByDefinition`.
92. `StableMatching != FairnessByDefinition`.
93. `MechanismStrategyPropertySide_A != Side_B`.
94. `Market != InstitutionFreeExchange`.
95. `MarketOutcome != CollectiveVoteOutcome`.
96. `DecentralizedAllocation != NoGovernance`.
97. `PriceCoordination != CentralPlanning`.
98. `CentralPlanning != OneUniformMechanism`.
99. `CompetitiveEquilibriumEfficiency != UniversalMarketEfficiency`.

## Externalities / public goods / commons

100. `ThirdPartyEffect != ExternalityByDefinition`.
101. `Externality_D != Externality_E`.
102. `NegativeExternality != MoralWrongByDefinition`.
103. `PositiveExternality != RightToSubsidyByDefinition`.
104. `PublicGood != GovernmentGood`.
105. `GovernmentProvision != PublicGoodByDefinition`.
106. `CollectivePreferenceForPublicGood != VoluntaryProvision`.
107. `FreeRiding != ZeroContributionByDefinition`.
108. `FreeRiding != IrrationalByDefinition`.
109. `IndividuallyRationalFreeRide != MorallyPermissible`.
110. `PublicGoodProblem != NoMechanismCanHelp`.
111. `PublicGoodMechanismSuccess_D != Success_E`.
112. `ClubGood != PurePublicGood`.
113. `CommonPoolResource != PublicGood`.
114. `Commons != OpenAccess`.
115. `OpenAccess != SelfGovernedCommons`.
116. `CommonPoolResource != InevitableCollapse`.
117. `SelfGovernance != NoRules`.
118. `CommonsProblem != StateControlRequiredByDefinition`.
119. `CommonsProblem != PrivatizationRequiredByDefinition`.
120. `Cooperation != EfficientEquilibriumByDefinition`.
121. `OneShotIncentives != RepeatedGameIncentives`.
122. `RepeatedInteraction != CooperationGuarantee`.
123. `Monitoring != Enforcement`.
124. `Enforcement != Compliance`.
125. `MorePunishment != MoreCooperationByDefinition`.
126. `SameFormalRule != SameBehaviorAcrossInstitutionalOrigins`.

## Information asymmetry / principal-agent

127. `AdverseSelection != MoralHazard`.
128. `AsymmetricInformation != MarketCollapseByDefinition`.
129. `AdverseSelection != FraudByDefinition`.
130. `Screening != Signaling`.
131. `Signal != TypeTruthByDefinition`.
132. `Competition != InformationSymmetry`.
133. `MoralHazard != MoralWrongdoingByDefinition`.
134. `HiddenAction != HiddenType`.
135. `MoreMonitoring != BetterContractByDefinition`.
136. `PrincipalAgent != EmployerEmployeeOnly`.
137. `Principal != NormativeSuperior`.
138. `Principal != LegitimateAuthorityByDefinition`.
139. `EconomicAgentRole != HF1AgentOntology`.
140. `Delegation != PreferenceAlignment`.
141. `Contract != CompleteControl`.
142. `OptimalContract_M != UniversalBestContract`.
143. `Contract != ResponsibilityElimination`.
144. `Output != Effort`.
145. `PerformancePay != EffortObservation`.
146. `MeasuredPerformance != WholeTaskValue`.
147. `CommonValue != IndependentPrivateValue`.
148. `HighestSignal != HighestTrueValueByDefinition`.
149. `WinnersCurseBehavior != MechanismTheoryInvalidByDefinition`.

## AI / collusion / Sybil

150. `LLMAgent != PerfectEquilibriumSolver`.
151. `SameMechanism + DifferentAgentModel != SameOutcomeDistribution`.
152. `LLMStrategicBehavior != OneStablePolicyClass`.
153. `GeneratedOutcomeSpace != FixedFiniteOptionSet`.
154. `LLMEncodedPreference != HumanPreferenceByDefinition`.
155. `AIAgentProxy != HumanPrincipal`.
156. `AgentRewardFunction != UserWelfare`.
157. `DeclaredPrimaryUtility != CompleteAIObjectiveByDefinition`.
158. `Collusion != Cooperation`.
159. `Communication != Collusion`.
160. `IndividualIC != CoalitionIC`.
161. `CoalitionProof != SybilProof`.
162. `AIAgentCompetition != InevitableCollusion`.
163. `PolicyText != IncentiveEnforcement`.
164. `ApparentIdentityCount != UnderlyingActorCount`.
165. `SybilIdentity != MoralBearerByDefinition`.
166. `ForkedProcess != IndependentParticipantByDefinition`.
167. `OneAccountOneVote != OnePersonOneVoteWithoutIdentityAssumption`.
168. `SybilResistance != PerfectIdentityVerification`.
169. `FixedAgentSet != FreeDigitalIdentityEnvironment`.
170. `SybilProof != EfficiencyByDefinition`.
171. `SybilProof != CoalitionProof`.
172. `FalseNameProof != OrdinaryStrategyProofness`.
173. `Capture != BriberyOnly`.
174. `Capture != Collusion`.
175. `DesignerObjective != SocialObjectiveByDefinition`.
176. `PrincipalObjective != SocialObjectiveByDefinition`.
177. `MechanismOptimizationSuccess != NormativeSuccess`.
178. `AnnouncedRule != CredibleCommitmentByDefinition`.
179. `CryptographicCommitment != InstitutionalLegitimacy`.
180. `SelfEnforcement != LegalEnforceability`.
181. `LegalEnforceability != EnforcementExecution`.
182. `FormalSanction != CredibleSanction`.

## Robustness / Human behavior

183. `Robust != WorksUnderAllPossibleWorlds`.
184. `RobustToBeliefError != RobustToSybil != RobustToCollusion != RobustToModelShift`.
185. `SimplerMechanism != BetterMechanismByDefinition`.
186. `Computable != IncentiveCompatible`.
187. `IncentiveCompatible != ComputationallyTractable`.
188. `TheoreticalDSIC != ErrorFreeHumanUse`.
189. `StrategyProof != ObviouslyStrategyProof`.
190. `FormalImplementation != BehavioralImplementation`.
191. `BehavioralDeviation != MechanismInvalidityByDefinition`.
192. `MeasuredTarget != WholeObjective`.
193. `ProxyReward != TrueObjectiveByDefinition`.
194. `HumanPreference != AgentPolicyObjectiveByDefinition`.
195. `MechanismTruthfulness != PrincipalBestInterestByDefinition`.
196. `DelegatedBiddingAuthority != UnlimitedEconomicAuthority`.
197. `StaticMechanismAnalysis != DynamicAgentMechanismInteraction`.
198. `PostOutcomeData != PreActionReport`.
199. `MoreMechanismData != BetterGovernanceByDefinition`.
200. `InformationDesign != MechanismDesignByDefinition`.
201. `Persuasion != IncentiveCompatibility`.

---

# 287. Minimum HF18 grammar

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

Private-information subgraph:

```text
True type/state
   ↓ hidden
Agent report/signal/action
   ↓
Mechanism outcome/transfer
   ↓
Incentive compatibility test

reported type != true type by definition
```

Digital identity subgraph:

```text
Underlying actor
   ↓ can create/control?
apparent identities/processes
   ↓
HF1 identity + admission authority
   ↓
legitimate participant set
   ↓
mechanism

account/process count != actor/participant count
```

---

# 288. Reconnection to HF17

HF17 asks:

```text
how does a collective authorize an outcome?
```

HF18 asks:

```text
how do strategic agents actually implement/interact under that rule?
```

Therefore:

```text
CollectiveChoiceRule != ImplementationMechanism
```

---

# 289. Reconnection to HF16

Population/welfare ordering can define an objective, but:

```text
NormativeObjective != IncentiveCompatibleMechanism
```

---

# 290. Reconnection to HF15/HF1

Digital participant counting consumes identity and standing before any allocation.

```text
ProcessIdentity != ParticipantAuthority != MoralStanding
```

---

# 291. Reconnection to HF14

```text
EfficientMechanism != JustMechanism
TruthfulMechanism != LegitimateMechanism
```

Rights/distribution/authority remain.

---

# 292. Reconnection to HF13

Mechanisms depend on institutions for:

```text
identity
property/access rights
commitment
enforcement
appeal
records
```

Thus:

```text
Mechanism != InstitutionalSubstrate
```

---

# 293. Reconnection to HF12

Strategic interaction is still social interaction, but:

```text
Cooperation != IncentiveCompatibility
Communication != Collusion
```

---

# 294. Reconnection to HF10/HF4

Preference/goal/value and incentive effects are distinct.

```text
HighReward != StrongMotivationForAllAgents
```

---

# 295. Reconnection to HF11

Implementation in game theory still precedes physical execution.

```text
EquilibriumOutcome != GuaranteedPhysicalEffect
```

---

# 296. Reflexivity

Mechanisms reshape agents and future feasible behavior.

```text
Mechanism_t
→ incentives + information + selection_t
→ participation + actions + learning_t
→ wealth/power/reputation/skill_t+1
→ types/outside options/coalitions_t+1
→ future mechanism performance
```

---

# 297. Selection effects

Mechanisms choose not only outcomes but populations of participants.

```text
EntryRule/Price/Complexity
→ WhoParticipates
```

---

# 298. Endogenous entry

Auction research shows optimal mechanism properties can change when entry itself is a
strategic response.

```text
ExogenousEntryModel != EndogenousEntryModel
```

---

# 299. Endogenous identity

Digital systems add:

```text
IdentityCreationCost
→ apparent participant set
```

---

# 300. Endogenous capability

Repeated mechanisms can create learning, capital, access and specialization.

This begins the next residual.

---

# 301. Mechanism design treats feasible outcome set largely as input

Even sophisticated dynamic mechanisms usually assume some technology/resource/action
possibility structure.

But real Human economic systems transform resources through production.

---

# 302. Allocation is not production

```text
Allocation != Production
```

An auction can decide who receives a machine; it does not explain how the machine was
created.

---

# 303. Incentive to work is not work/production process

```text
WorkIncentive != ProductionFunction
```

---

# 304. Mechanism can allocate tasks without explaining capability formation

```text
TaskAllocation != SkillFormation
```

HF6/HF8 apply.

---

# 305. Market exchange presupposes something exchangeable

```text
Exchange != Production
```

---

# 306. Public-good provision presupposes production technology

Contribution mechanism determines funding/incentive; actual good creation requires
labor/capital/technology.

```text
FundingMechanism != ProductionTechnology
```

---

# 307. Commons allocation presupposes resource regeneration/depletion dynamics

```text
GovernanceRule != ResourceProductionDynamics
```

---

# 308. Principal-agent contracts presuppose productive task structure

```text
IncentiveContract != TeamProductionArchitecture
```

---

# 309. Alchian-Demsetz residual

Team production introduces monitoring/measurement problems because joint output may
not reveal each member's marginal contribution cleanly.

This is not merely private-type mechanism design; it depends on production structure.

---

# 310. Coase residual

The existence/boundary of firms raises why some coordination occurs through authority/
organization rather than repeated market transactions.

Transaction/coordination costs and production organization therefore become separate
objects.

---

# 311. Ownership residual

Grossman-Hart/Hart-Moore show residual control rights over assets affect investment/
productivity incentives when contracts are incomplete.

Thus:

```text
ContractMechanism != OwnershipStructure
```

---

# 312. Ownership is not current possession

```text
Ownership != PhysicalPossession
```

HF13/HF14 legal/normative layers will be needed.

---

# 313. Capital is not money

A production foundation must distinguish:

```text
Money
FinancialClaim
PhysicalCapital
HumanCapital/Skill
KnowledgeCapital
OrganizationalCapital
NaturalResource
Infrastructure
```

HF18 does not reconstruct these fully.

---

# 314. Production changes feasible set

```text
Resources_t + Technology_t + Work_t + Organization_t
→ Outputs_t + Capabilities_{t+1} + Resources_{t+1}
```

This is different from allocating a fixed pie.

---

# 315. Mechanism may change production incentives

But:

```text
MechanismEffectOnProduction != ProductionOntology
```

---

# 316. Firm is not mechanism totality

```text
Firm != IncentiveContractOnly
```

It can include assets, authority, teams, routines, knowledge and ownership.

---

# 317. Work is not labor hours only

```text
Work != TimeInputOnly
```

Skill, attention, coordination, tools, risk and learning matter.

---

# 318. Specialization is not task assignment only

```text
Specialization != CurrentTaskAllocation
```

It can change future skill/productivity and dependency.

---

# 319. Technology is not tool availability only

```text
Technology != ToolAvailability
```

It includes reproducible transformation methods/knowledge/constraints.

---

# 320. Production residual appears across multiple HF18 cases

- auctions allocate existing objects;
- markets exchange existing/produced claims/goods;
- public-good mechanisms finance/provision but require production;
- commons rules govern extraction/regeneration;
- principal-agent contracts govern effort in productive tasks;
- firms combine assets/work/authority;
- AI agents can substitute/complement labor and change technology/capital structure.

Therefore the residual is not incidental.

---

# 321. Decisive new firewall

```text
Allocation
!= Exchange
!= IncentiveCompatibleImplementation
!= Production
!= EconomicOrganization
```

---

# 322. Exact next foundation

HF18 therefore exposes:

# HF19 — Work, Production, Specialization, Firms, Ownership, Capital, Technology and Economic Organization

HF19 must reconstruct:

```text
work / labor / effort / task
output / product / service
production / transformation
productivity / marginal product
technology / technique
skill / human capital / learning-by-doing
physical capital / infrastructure
knowledge / organizational capital
specialization / division of labor
team production
coordination cost / transaction cost
firm / market / hierarchy / network / peer production
employment / contractor / partnership / cooperative
ownership / possession / access / residual control
incomplete contract
investment / hold-up
asset specificity
scale / scope / complementarity
automation / substitution / complementarity
AI as tool / worker / agent / capital
production externalities
value creation vs value capture
maintenance / depreciation
innovation
```

without assuming firms, markets, wage labor, private ownership, hierarchy,
automation or one production function as universal foundation.

HF19 is **not started in this conversation**; it is the continuation point for the
next conversation after the HF0–HF18 closeout.

---

# 323. HF19 starting questions

1. What is work relative to action, effort, task and employment?
2. What is production relative to exchange/allocation?
3. What is output relative to welfare/value/revenue?
4. What is productivity relative to effort and capability?
5. What is technology relative to tools, knowledge and capital?
6. What is capital, and why is money not capital by definition?
7. What is specialization relative to current task assignment and persistent skill?
8. What is team production and why is marginal contribution hard to measure?
9. What is a firm relative to market, organization and legal person?
10. What are transaction costs and coordination costs?
11. Why do some transactions move inside organizational authority rather than prices?
12. What is ownership relative to possession, access, legal title and residual control?
13. What is an incomplete contract and how does ownership alter investment incentives?
14. What is hold-up/asset specificity?
15. What is scale versus scope versus complementarity?
16. What is automation relative to substitution, complementarity and capability
    extension?
17. When is AI a tool, worker-like service, delegated agent, organizational member or
    capital asset?
18. What is value creation relative to value capture?
19. How do production systems change Human capability, dependency, power and welfare?
20. What next boundary, if any, emerges after production/economic organization?

---

# 324. Candidate HF19 falsifiers

- same labor hours, different output due to capital/technology;
- same output, different Human effort because automation;
- high effort but low productivity due to poor tool/process;
- team output where individual marginal contributions are not observable;
- freelancer, employee and partner performing same task under different ownership/
  authority/residual claims;
- firm internalizes transaction versus same exchange through market contract;
- asset owner versus physical possessor;
- complete-contract benchmark versus hold-up under incomplete contract;
- automation increasing total output while deskilling one Human capability;
- AI agent used as tool in one firm and autonomous contractor in another;
- open-source peer production without wage/firm hierarchy;
- increasing returns where specialization raises productivity but dependence;
- capital investment raising future feasible set rather than merely reallocating
  current resources.

---

# 325. Do not precommit

HF18 does not establish that HF19 should conclude:

- all work is employment;
- labor hours are the correct measure of work;
- output equals value;
- revenue equals value created;
- productivity equals effort;
- marginal-product wages are universally observable/deserved;
- capital means money;
- firms exist only because transaction costs;
- hierarchy is superior to market or peer production;
- private ownership is universally efficient/legitimate;
- ownership equals possession;
- incomplete contracts explain all firm boundaries;
- specialization is always beneficial;
- economies of scale are universal;
- automation always substitutes labor;
- AI is simply labor or simply capital;
- technology is exogenous;
- production growth is welfare growth;
- efficient production is just distribution.

---

# 326. Stop rule

Do not schedule HF20 now.

HF19 must expose its own repeated neighboring distinction. This conversation closes
at HF18 and hands HF19 to a fresh conversation.

---

# 327. HF18 synthesis

HF18 began from `CollectiveChoiceRule != ImplementationMechanism` and reconstructed the
strategic layer:

```text
Incentive
!= Motivation
!= Preference

Type
!= WholePerson
!= Message
!= Identity

ReportedType
!= TrueType by definition

Strategy
!= RealizedAction

NashEquilibrium
!= ObservedBehavior
!= SocialOptimum

Mechanism
!= SocialChoiceRule
!= Institution
!= Market
!= Contract

Authorization
!= Implementation
!= RealizedPhysicalOutcome

DSIC
!= BIC
!= NashImplementation

IC
!= Efficiency
!= IR
!= BudgetBalance
!= Legitimacy

RevelationPrinciple
!= PracticalMechanismConstruction

Participation
!= Consent

Price
!= Welfare
!= MoralValue

RevenueOptimal
!= WelfareOptimal

VCGTruthful
!= BudgetBalanced
!= Fair
!= CoalitionProof
!= SybilProof

FirstBest
!= ImplementableByDefinition

Bargaining
!= Voting
!= Deliberation
!= CompetitivePriceTaking

NashBargaining
!= RubinsteinBargaining

StableMatching
!= WelfareMaximum
!= Fairness

Market
!= InstitutionFreeExchange

PublicGood
!= GovernmentGood

CollectiveSupportForPublicGood
!= VoluntaryProvision

CommonPoolResource
!= PublicGood
Commons
!= OpenAccess
CommonPoolResource
!= InevitableCollapse

AdverseSelection
!= MoralHazard
HiddenType
!= HiddenAction

Principal
!= LegitimateAuthority
Delegation
!= PreferenceAlignment
Contract
!= CompleteControl

IndividualIC
!= CoalitionIC
!= SybilProofness

Account/ProcessCount
!= UnderlyingActorCount

LLMAgent
!= PerfectEquilibriumSolver
AgentRewardFunction
!= UserWelfare

FormalImplementation
!= BehavioralImplementation

MechanismOptimizationSuccess
!= NormativeSuccess
```

The deepest compression is:

```text
A mechanism can make a selected allocation strategically implementable over a given
feasible set. It does not by itself explain how Human work, technology, capital,
ownership and organization create or transform the feasible set that is being
allocated.
```

That is the HF19 production/economic-organization boundary, intentionally deferred to
the next conversation.
