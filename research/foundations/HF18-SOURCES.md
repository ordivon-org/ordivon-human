---
schema_version: 1
id: human.foundations.hf18.sources
title: HF18 External Evidence and Source Ledger
type: evidence
profile: research
lifecycle: active
source_role: supporting
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
updated: 2026-08-17
summary: Primary mechanism-design, auction, bargaining, matching, public-goods, commons, information-asymmetry, principal-agent, Sybil/false-name and current AI-agent sources used to reconstruct strategic implementation after HF17. Production, firm-boundary and ownership sources are retained only as evidence for the HF19 residual.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
  - HF18
related:
  - human.foundations.hf18
  - human.foundations.hf17.sources
---
# HF18 External Evidence and Source Ledger

## Evidence rule

HF18 separates:

```text
Formal mechanism theorem
= result conditional on exact type/message/outcome/information/solution-concept assumptions

Experimental/field mechanism evidence
= observed behavior under a particular institutional/mechanism treatment

Historical/institutional economic evidence
= evidence about real organization, commons, enforcement or firm boundaries

Current AI-agent evidence
= model/version/environment-specific strategic behavior, not a Human behavioral law
```

Never infer:

```text
DSIC -> Fairness
Equilibrium -> ObservedBehavior
Efficiency -> Justice
Price -> Welfare
MechanismSuccess_D -> UniversalMechanismSuccess
LLMBehavior_ModelA -> UniversalAgentBehavior
```

---

# 1. Vickrey — second-price/private-value auction

## William Vickrey (1961)

- Title: *Counterspeculation, Auctions, and Competitive Sealed Tenders*
- Journal: Journal of Finance 16(1):8–37
- DOI: 10.1111/j.1540-6261.1961.tb02789.x
- Use: canonical primary source for second-price sealed-bid auction and dominant-strategy
  truthful bidding in the standard private-value setting.

### HF18 inference

```text
SecondPriceTruthfulness != UniversalAuctionTruthfulness
HighestBid != HighestWelfareByDefinition
```

---

# 2. Groves — incentives in teams

## Theodore Groves (1973)

- Title: *Incentives in Teams*
- Journal: Econometrica 41(4):617–631
- DOI: 10.2307/1914085
- Use: primary mechanism-design treatment of compensation/information revelation in
  team resource-allocation settings; core precursor to Groves/VCG mechanisms.

### HF18 inference

```text
TruthfulInformationInModel != IntrinsicTeamCooperation
Mechanism != TeamIdentity
```

---

# 3. Clarke — multipart pricing/public goods

## Edward H. Clarke (1971)

- Title: *Multipart Pricing of Public Goods*
- Journal: Public Choice 11:17–33
- DOI: 10.1007/BF01726210
- Use: primary pivotal-mechanism/public-good pricing contribution addressing strategic
  revelation of public-good values.

### HF18 inference

```text
PublicGoodSupport != TruthfulValuationByDefault
TransferRule is part of implementation
```

---

# 4. Myerson — optimal auction design

## Roger B. Myerson (1981)

- Title: *Optimal Auction Design*
- Journal: Mathematics of Operations Research 6(1):58–73
- DOI: 10.1287/moor.6.1.58
- Use: primary Bayesian auction design with seller expected-utility/revenue objective
  under private information.

### HF18 inference

```text
RevenueOptimal != WelfareOptimalByDefinition
MyersonOptimalAuction != UniversalAuctionDesign
DesignerObjective must be explicit
```

---

# 5. Myerson & Satterthwaite — bilateral-trade impossibility

## Roger B. Myerson & Mark A. Satterthwaite (1983)

- Title: *Efficient Mechanisms for Bilateral Trading*
- Journal: Journal of Economic Theory 29(2):265–281
- DOI: 10.1016/0022-0531(83)90048-0
- Use: buyer and seller have independent private valuations; characterizes BIC/IR
  mechanisms and proves general impossibility of ex-post efficient trade without
  outside subsidies in the admitted setting.

### HF18 inference

```text
FirstBestOutcome != ImplementableOutcomeByDefinition
MyersonSatterthwaite != TradeImpossible
MyersonSatterthwaite != UniversalMarketInefficiency
```

---

# 6. Sugaya & Wolitzky — revelation principle in multistage games

## Takuo Sugaya & Alexander Wolitzky (2021; online 2020)

- Title: *The Revelation Principle in Multistage Games*
- Journal: Review of Economic Studies 88(3):1503–1540
- DOI: 10.1093/restud/rdaa041
- Use: shows communication revelation principle fails in general for sequential
  equilibrium in multistage games, while holding in important subclasses and under
  other stated solution concepts.

### HF18 inference

```text
RevelationPrinciple_D != RevelationPrinciple_E
RevelationPrinciple != PracticalMechanismConstruction
RevelationPrinciple != EquilibriumFreeResult
```

---

# 7. Nash — axiomatic bargaining

## John F. Nash Jr. (1950)

- Title: *The Bargaining Problem*
- Journal: Econometrica 18(2):155–162
- DOI: 10.2307/1907266
- Use: primary axiomatic bargaining solution based on feasible utility set and
  disagreement point.

### HF18 inference

```text
NashBargainingSolution != StrategicBargainingProcessByDefinition
DisagreementPoint is a first-class input
```

---

# 8. Rubinstein — alternating offers

## Ariel Rubinstein (1982)

- Title: *Perfect Equilibrium in a Bargaining Model*
- Journal: Econometrica 50(1):97–109
- DOI: 10.2307/1912531
- Use: primary strategic alternating-offers model producing subgame-perfect bargaining
  outcome under timing/impatience assumptions.

### HF18 inference

```text
NashBargaining != RubinsteinAlternatingOffers
BargainingPower can depend on time/patience/protocol
```

---

# 9. Gale & Shapley — matching/stability

## David Gale & Lloyd S. Shapley (1962)

- Title: *College Admissions and the Stability of Marriage*
- American Mathematical Monthly 69(1):9–15
- DOI: 10.1080/00029890.1962.11989827
- Use: primary deferred-acceptance/stable matching construction.

### HF18 inference

```text
Matching != Auction
StableMatching != WelfareMaximumByDefinition
StableMatching != FairnessByDefinition
```

---

# 10. Samuelson — pure public expenditure

## Paul A. Samuelson (1954)

- Title: *The Pure Theory of Public Expenditure*
- Review of Economics and Statistics 36(4):387–389
- DOI: 10.2307/1925895
- Use: foundational economic public-good condition and nonrival collective-consumption
  structure.

### HF18 inference

```text
PublicGood != GovernmentGood
Public-good ontology is about consumption/exclusion/rivalry structure, not provider identity
```

---

# 11. Falkinger, Fehr, Gächter & Winter-Ebmer — public-good mechanism experiment

## 2000

- Title: *A Simple Mechanism for the Efficient Provision of Public Goods: Experimental Evidence*
- American Economic Review 90(1):247–264
- DOI: 10.1257/aer.90.1.247
- Use: experimental reward/penalty mechanism generated public-good provision close to
  efficient levels in the tested design.

### HF18 inference

```text
PublicGoodProblem != NoMechanismCanHelp
PublicGoodMechanismSuccess_D != Success_E
```

---

# 12. Fehr & Gächter — punishment/public goods

## Ernst Fehr & Simon Gächter (2000)

- Title: *Cooperation and Punishment in Public Goods Experiments*
- American Economic Review 90(4):980–994
- DOI: 10.1257/aer.90.4.980
- Use: primary experimental evidence that punishment opportunities can alter
  cooperation in repeated public-good environments.

### HF18 inference

```text
SanctionChangesIncentives
MorePunishment != MoreCooperationByDefinition
```

---

# 13. Ostrom & Gardner — self-governing commons

## Elinor Ostrom & Roy Gardner (1993)

- Title: *Coping with Asymmetries in the Commons: Self-Governing Irrigation Systems Can Work*
- Journal of Economic Perspectives 7(4):93–112
- DOI: 10.1257/jep.7.4.93
- Use: field/experimental institutional evidence that common-pool appropriators can
  create/enforce their own rules under some conditions despite asymmetries.

### HF18 inference

```text
Commons != OpenAccess
SelfGovernance != NoRules
CommonPoolResource != InevitableCollapse
CommonsProblem != StateControlRequiredByDefinition
CommonsProblem != PrivatizationRequiredByDefinition
```

---

# 14. Huang & Smith — dynamic common-pool exploitation

## 2014

- DOI: 10.1257/aer.104.12.4071
- Use: dynamic common-pool resource experiment/model showing intertemporal strategic
  extraction pressure and resource dynamics.

### HF18 inference

```text
OneShotIncentives != DynamicResourceIncentives
GovernanceRule interacts with regeneration/depletion dynamics
```

---

# 15. Noussair et al. — dynamic fishing game

## 2015

- DOI: 10.1257/aer.p20151018
- Use: experimental dynamic fishing/common-resource setting; evidence that strategic
  extraction cannot be inferred from one-shot static incentives alone.

### HF18 inference

```text
CommonInterestInSustainability != SustainableExtractionGuarantee
```

---

# 16. Kosfeld & Rustagi — leaders/punishment in commons

## 2015

- DOI: 10.1257/aer.20120700
- Use: field evidence linking leader/punishment behavior and cooperation/resource
  outcomes in common-pool governance.

### HF18 inference

```text
MorePunishment != MoreCooperationByDefinition
Leader/InstitutionType matters
```

---

# 17. Dal Bó — cooperation under continuation probability

## Pedro Dal Bó (2005)

- DOI: 10.1257/000282805775014434
- Use: primary experimental repeated-game evidence on continuation probability and
  cooperation.

### HF18 inference

```text
OneShotIncentives != RepeatedGameIncentives
RepeatedInteraction != CooperationGuarantee
```

---

# 18. Dal Bó & Fréchette — repeated cooperation

## Pedro Dal Bó & Guillaume R. Fréchette (2011)

- DOI: 10.1257/aer.101.1.411
- Use: experimental evidence on cooperation/equilibrium selection in infinitely
  repeated games.

### HF18 inference

```text
EquilibriumExistence != EquilibriumSelection
Learning/history matter for realized cooperation
```

---

# 19. Dal Bó, Foster & Putterman — institution origin

## 2010

- DOI: 10.1257/aer.100.5.2205
- Use: experimental evidence that democratic/endogenous choice of institutions can
  change cooperation relative to otherwise similar imposed institutional rules.

### HF18 inference

```text
SameFormalRule != SameBehaviorAcrossInstitutionalOrigins
```

This reconnects HF17 procedural legitimacy/origin with HF18 behavioral implementation.

---

# 20. Akerlof — lemons/adverse selection

## George A. Akerlof (1970)

- Title: *The Market for “Lemons”: Quality Uncertainty and the Market Mechanism*
- Quarterly Journal of Economics 84(3):488–500
- DOI: 10.2307/1879431
- Use: primary hidden-quality/adverse-selection model showing how asymmetric
  information can degrade exchange and remove high-quality sellers.

### HF18 inference

```text
AdverseSelection != MoralHazard
AdverseSelection != FraudByDefinition
AsymmetricInformation != MarketCollapseByDefinition
```

---

# 21. Rothschild & Stiglitz — competitive insurance under imperfect information

## Michael Rothschild & Joseph Stiglitz (1976)

- Title: *Equilibrium in Competitive Insurance Markets: An Essay on the Economics of Imperfect Information*
- Quarterly Journal of Economics 90(4):629–649
- DOI: 10.2307/1885326
- Use: primary screening/separating-contract analysis for privately known risk types.

### HF18 inference

```text
Competition != InformationSymmetry
Screening != Signaling
```

---

# 22. Holmström — moral hazard and observability

## Bengt Holmström (1979)

- Title: *Moral Hazard and Observability*
- Bell Journal of Economics 10(1):74–91
- JSTOR stable: 3003320
- Use: primary principal-agent moral-hazard analysis linking incentive contracts to
  observability/informative performance signals.

### HF18 inference

```text
HiddenAction != HiddenType
Output != Effort
MoreMonitoring != BetterContractByDefinition
```

---

# 23. Grossman & Hart — principal-agent problem

## Sanford J. Grossman & Oliver D. Hart (1983)

- Title: *An Analysis of the Principal-Agent Problem*
- Econometrica 51(1):7–45
- DOI: 10.2307/1912246
- Use: primary analysis of implementable actions and optimal contracts under
  principal-agent moral hazard/information constraints.

### HF18 inference

```text
Contract != CompleteControl
OptimalContract_M != UniversalBestContract
FirstBest != ImplementableByDefinition
```

---

# 24. Douceur — Sybil attack

## John R. Douceur (2002)

- Title: *The Sybil Attack*
- IPTPS 2002
- DOI: 10.1007/3-540-45748-8_24
- Primary repository: Microsoft Research
- Use: shows decentralized identity systems cannot generally prevent one entity from
  presenting multiple identities without logically centralized certification or
  strong resource/coordination assumptions.

### HF18 inference

```text
ApparentIdentityCount != UnderlyingActorCount
OneAccountOneVote != OnePersonOneVoteWithoutIdentityAssumption
FixedAgentSet != FreeDigitalIdentityEnvironment
```

---

# 25. Dütting et al. — mechanism design for LLMs

## Paul Dütting, Vahab Mirrokni, Renato Paes Leme, Haifeng Xu & Song Zuo

- Original work: WWW 2024 / arXiv:2310.10826
- Extended abstract: IJCAI 2025, pages 10885–10890
- DOI: 10.24963/ijcai.2025/1210
- Use: mechanism design where preferences over stochastically generated content are
  encoded by LLMs; token-level generated outcome and incentive properties extend
  beyond fixed alternative/item allocation.

### HF18 inference

```text
GeneratedOutcomeSpace != FixedFiniteOptionSet
LLMEncodedPreference != HumanPreferenceByDefinition
```

---

# 26. Nonbossy mechanisms — robustness to secondary goals

## 2026 Journal of Economic Theory

- Title: *Nonbossy mechanisms: Mechanism design robust to secondary goals*
- DOI: 10.1016/j.jet.2026.106187
- Use: current peer-reviewed formal work showing strategy-proofness may be insufficient
  when agents possess secondary objectives; nonbossiness becomes relevant in the
  studied domains.

### HF18 inference

```text
PrimaryIC != RobustToAllSecondaryGoals
DeclaredPrimaryUtility != CompleteAIObjectiveByDefinition
Nonbossiness != Fairness
```

---

# 27. Synthetic LLM auction participants — current preprint

## *Learning from Synthetic Labs: Language Models as Auction Participants* (2025)

- Evidence status: arXiv/preprint
- Use: synthetic auction experiments report risk-averse-like bidding, behavior closer
  to benchmark theory in obviously strategy-proof settings and winner's-curse-like
  behavior in common-value settings.

### HF18 inference

```text
LLMAgent != PerfectEquilibriumSolver
CommonValue != IndependentPrivateValue
HighestSignal != HighestTrueValueByDefinition
```

Transport limit: model/prompt/auction specific; do not generalize to all agents.

---

# 28. Predictive strategic models of LLM agents — current workshop evidence

## *Towards Predictive Models of Strategic Behaviour in LLM Agents* (ICLR workshop 2026)

- Evidence status: workshop/current empirical evidence
- Use: large synthetic strategic-decision corpus reports substantial model-family
  heterogeneity and sometimes opposite responses to the same strategic environment.

### HF18 inference

```text
SameMechanism + DifferentAgentModel != SameOutcomeDistribution
LLMStrategicBehavior != OneStablePolicyClass
```

---

# 29. LLM-agent collusion in double auctions — current preprint

## 2025

- Evidence status: preprint
- Use: reports model/environment-dependent collusive tendencies in repeated double
  auction simulations.

### HF18 inference

```text
IndividualIC != CoalitionIC
AI-agent communication/repetition can alter market outcomes
```

---

# 30. Fragility of AI-agent collusion — current working paper

## 2025–2026

- Evidence status: SSRN/current working paper
- Use: reports that AI-agent collusion can be fragile to model/data/patience
  heterogeneity and competitor composition.

### HF18 inference

```text
AIAgentCompetition != InevitableCollusion
RobustToCollusion is environment-specific
```

---

# 31. Institutional AI / enforceable anti-collusion — current preprint

## 2026

- Evidence status: preprint only
- Use: experimental Cournot-style AI-agent settings compare prompt-only policy
  instructions with enforceable consequence/institution structures.

### HF18 inference

```text
PolicyText != IncentiveEnforcement
```

Do not promote this result beyond its current preprint/domain status.

---

# 32. Sybil-proof mechanisms — current formal preprint

## 2024

- Evidence status: preprint
- Use: formal mechanism-design treatment where participant identity creation is
  strategic rather than fixed.

### HF18 inference

```text
FalseNameProof != OrdinaryStrategyProofness
SybilProof != EfficiencyByDefinition
```

---

# 33. Cost of Sybils / false-name proofness — current formal preprint

## 2023

- Evidence status: preprint
- Use: analyzes identity-creation cost, credible commitments and false-name-proof
  mechanisms.

### HF18 inference

```text
IdentityCreationCost is a mechanism parameter
SybilProof != CoalitionProof
```

---

# 34. Coase — Nature of the Firm [HF19 residual only]

## Ronald H. Coase (1937)

- Title: *The Nature of the Firm*
- Economica 4(16):386–405
- DOI: 10.1111/j.1468-0335.1937.tb00002.x
- HF18 use: residual evidence only. Explains why production/coordination sometimes
  moves inside firm authority rather than repeated market contracting.

### Boundary inference

```text
Mechanism/MarketExchange != EconomicOrganizationTotality
```

Full reconstruction is deferred to HF19.

---

# 35. Alchian & Demsetz — team production [HF19 residual only]

## Armen A. Alchian & Harold Demsetz (1972)

- Title: *Production, Information Costs, and Economic Organization*
- American Economic Review 62(5):777–795
- Use: team production, monitoring and difficulty attributing marginal contributions.

### Boundary inference

```text
IncentiveContract != TeamProductionArchitecture
TaskAllocation != ProductionContributionMeasurement
```

---

# 36. Grossman & Hart — ownership/residual control [HF19 residual only]

## Sanford J. Grossman & Oliver D. Hart (1986)

- Title: *The Costs and Benefits of Ownership: A Theory of Vertical and Lateral Integration*
- Journal of Political Economy 94(4):691–719
- DOI: 10.1086/261404
- Use: incomplete contracts and residual control rights alter investment incentives
  and integration boundaries.

### Boundary inference

```text
ContractMechanism != OwnershipStructure
```

---

# 37. Hart & Moore — property rights / firm boundaries [HF19 residual only]

## Oliver Hart & John Moore (1990)

- Title: *Property Rights and the Nature of the Firm*
- Journal of Political Economy 98(6):1119–1158
- DOI: 10.1086/261729
- Use: ownership/property rights and incomplete contracts as determinants of firm
  boundaries and investment incentives.

### Boundary inference

```text
Ownership != CurrentPossession
ProductionOrganization requires asset-control structure
```

---

# 38. Source-level synthesis

The primary/formal corpus establishes that mechanism properties are plural and
assumption-conditional:

```text
DSIC != BIC != NashImplementation
IC != IR != Efficiency != BudgetBalance
Efficiency != Justice != Legitimacy
RevelationPrinciple != PracticalMechanism
VickreyTruthfulness != UniversalAuctionTruthfulness
RevenueOptimal != WelfareOptimal
VCGTruthful != BudgetBalanced/Fair/CoalitionProof/SybilProof
FirstBest != ImplementableByDefinition
Bargaining != Voting != Deliberation
StableMatching != WelfareMaximum/Fairness
PublicGood != GovernmentGood
CommonPoolResource != PublicGood
Commons != OpenAccess
AdverseSelection != MoralHazard
HiddenType != HiddenAction
Principal != LegitimateAuthority
IndividualIC != CoalitionIC != SybilProofness
FormalImplementation != BehavioralImplementation
```

The experimental/field corpus establishes that behavior depends on institutional
origin, repetition, monitoring, sanctions and local governance rather than one static
payoff table alone.

The AI-agent corpus establishes only a narrower current conclusion:

```text
AgentModel/Prompt/Harness/InformationEnvironment are mechanism-relevant variables
```

not a universal model of AI rationality or collusion.

Finally, Coase/Alchian-Demsetz/Grossman-Hart/Hart-Moore are deliberately **not** used to
finish production theory inside HF18. They supply the repeated boundary evidence that
allocation/mechanism design presupposes and reshapes, but does not reconstruct,
production technology, team organization, ownership and firm boundaries. That is the
HF19 frontier.
