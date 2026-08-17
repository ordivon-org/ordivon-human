---
schema_version: 1
id: human.foundations.hf19
title: HF19 — Work, Production, Specialization, Firms, Ownership, Capital, Technology and Economic Organization
type: report
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
summary: Reconstructs work, production and economic organization without reducing work to employment, productivity to effort, capital to money, firms to one theory, ownership to possession, technology to tools, automation to substitution, or output/revenue to value and welfare.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
  - HF19
related:
  - human.foundations.hf18
  - human.foundations.hf19.sources
  - human.foundations.hf19.continuation
  - human.foundations.hf0-hf18.closeout
---
# HF19 — Work, Production, Specialization, Firms, Ownership, Capital, Technology and Economic Organization

## 0. Research contract

HF19 begins only after HF0–HF18 were frozen and the first Human Foundations cycle was
closed. The Git boundary was revalidated before this round:

```text
HEAD == main == origin/main == FETCH_HEAD
     == 0532f8eeb24c895722b558208facf1c62eaee857
```

No `FoundationReopenCondition` was observed. HF19 therefore does **not** reopen or
silently rewrite any previous foundation.

The inherited firewall is:

```text
Allocation
!= Exchange
!= IncentiveCompatibleImplementation
!= Production
!= EconomicOrganization
```

HF18 can explain how rules, contracts, bargaining, markets and incentives implement
outcomes under strategic behavior. It cannot by itself explain how work, tools, skills,
capital services, organizational routines, ownership/control and technology alter the
feasible set of future production.

HF19 uses the required order:

```text
term separation
→ competing models
→ cross-context falsification
→ deletion / transport audit
→ minimum surviving grammar
```

It does not assume a successor round.

---

# 1. The category error HF19 is repairing

A large fraction of economic language compresses different levels into one word:

```text
work        → employment / effort / hours / task / occupation
production  → output / revenue / value / GDP / transformation
productivity→ effort / skill / technology / efficiency / worker quality
technology  → tool / knowledge / invention / automation
capital     → money / asset / machine / skill / claim / infrastructure
firm        → legal person / hierarchy / contract nexus / asset set / team
ownership   → title / possession / use / control / residual claim
specialization → current task assignment / skill history / occupation
investment  → financial purchase / capacity creation
value       → output / price / revenue / surplus / welfare / moral value
```

These collapses survive in simple models because several variables covary. They fail
as soon as one changes while another is held fixed.

HF19 therefore treats economic organization as a **multi-layer production relation**,
not one scalar `economic_status` or one preferred theory of the firm.

---

# 2. Work, labor, effort, task, job, occupation and employment

## 2.1 Work is broader than employment

International labour statistics already require a separation between work and
employment. The ILO work framework includes own-use production, employment, unpaid
trainee work, volunteer work and other work activities; employment is the subset done
for pay or profit.

For HF19:

```text
Work_Broad
= sustained purposive activity directed at producing, providing, transforming,
  maintaining or completing an intended state/outcome
```

This is broader than economic work. When an economic boundary matters, qualify it:

```text
EconomicWork_D
= Work_Broad admitted by the production/economic boundary D
```

Therefore:

```text
Work != Employment
Paid != ProductiveByDefinition
Unpaid != Nonwork
Marketed != ProductiveByDefinition
```

The qualifier matters because statistical accounting boundaries are measurement
conventions, not a metaphysical partition of human activity.

## 2.2 Labor is a production-input projection, not the person

`Labor` is overloaded. HF19 reserves the economic input sense as:

```text
LaborService_D
= human productive service/input admitted by production model D
```

It may be measured using hours, persons, task units, effective labor, skill-adjusted
hours or another domain variable. None is the human being.

```text
Human != Labor
Person != HumanCapital
LaborHours != LaborServiceQuality
LaborInput_D != TotalHumanContribution
```

This preserves HF1's person boundary and prevents an economic input representation
from becoming an ownership or moral-standing claim.

## 2.3 Effort is not labor time

HF4 already reconstructed effort. HF19 consumes that distinction rather than
redefining it.

```text
Effort
= exertion/control-cost variable under a specified task and agent model

WorkTime
= elapsed or compensated time assigned to work
```

Possible combinations include:

```text
high hours + low effort intensity
low hours  + high effort intensity
high effort + low output
low effort  + high output through skill/tooling/automation
```

Therefore:

```text
Effort != Hours
Effort != Work
Effort != Output
Effort != Productivity
```

## 2.4 Task, job and occupation occupy different scales

```text
Task
= bounded unit of required activity or transformation under a workflow model

Job_D
= bundle of tasks, responsibilities and relations performed by one person in one
  work position under institutional boundary D

Occupation_D
= category grouping sufficiently similar jobs across positions/organizations
```

A task can move between people, teams, contractors or machines while the job remains.
A job can be redesigned while its occupation label remains. An occupation can persist
while its task composition changes radically.

```text
Task != Job != Occupation
TaskAutomation != JobElimination
OccupationLabel != CurrentTaskContent
```

## 2.5 Employment has at least two non-equivalent meanings

HF19 separates:

```text
Employment_Statistical
= work for pay or profit under the relevant labour-statistics standard

EmploymentRelation_LegalInstitutional
= employee-employer relation creating typed rights, obligations, authority and
  remuneration under a jurisdiction/institution
```

The first can include work for profit by independent workers. The second specifically
concerns an employee-employer relation.

The ILO's ICSE-18 further demonstrates that work status can be classified using at
least two different dimensions:

```text
Authority over the work/economic unit
Economic risk borne by the worker
```

It explicitly admits dependent contractors, employees, employers and independent
workers as different configurations.

Therefore:

```text
Employee != Contractor != DependentContractor != Partner != OwnerOperator
SameTask != SameEmploymentRelation
EmploymentStatus != AuthorityLevelByDefinition
EmploymentStatus != EconomicRiskByDefinition
```

---

# 3. Production, transformation, output, product, service and maintenance

## 3.1 Production is not exchange or allocation

HF19 uses a broad production operator:

```text
ProductionProcess_D:
  State_t × Inputs_t × Technology_t × Technique_t × Organization_t
  → Outputs_t × Byproducts_t × State_{t+1}
```

where inputs may include:

```text
materials
energy
labor services
capital services
information
skills
knowledge
access/rights
infrastructure services
intermediate products
```

and `Organization_t` can determine who decides, who coordinates, who controls assets,
how information travels, and how claims/incentives are assigned.

Production therefore changes states or feasible capabilities; exchange primarily
changes claims/possession/access between parties; allocation selects uses among
alternatives.

```text
Production != Exchange
Production != Allocation
OwnershipTransfer != PhysicalTransformation
MarketTransaction != ProductionByDefinition
```

The same production process can occur under an internal hierarchy, a market contract,
a cooperative, a household or peer production.

## 3.2 Transformation is broader than physical fabrication

A production-relevant transformation can change:

```text
physical state
location
information state
software state
knowledge state
health/condition of a user
availability/access
coordination state
maintained serviceability
```

This is why a service can be produced even when no durable object appears.

```text
Production != ManufacturingOnly
Output != TangibleGoodOnly
Service != Nonproduction
```

## 3.3 Output needs a boundary and quality dimension

```text
Output_D
= produced result admitted and measured under boundary D
```

Output may be represented as quantity, quality-adjusted quantity, completed service,
resolved case, maintained state, information product or another domain measure.

```text
MeasuredOutput_D != TotalEffect
GrossOutput != NetOutput
Quantity != Quality
Output != OutcomeValue
```

A system can increase counted units while reducing quality, resilience or downstream
welfare.

## 3.4 Product and service are output classes, not value judgments

A product can be a good or service under statistical/economic definitions. Services
can involve co-production with users and can change user conditions rather than
transfer a durable object.

```text
Product != GoodOnly
Service != FreeByDefinition
ServiceOutput != CustomerWelfare
```

## 3.5 Maintenance is productive without necessarily creating a new asset

Maintenance can preserve a productive or usable state:

```text
Maintenance_t
→ lower deterioration / restore serviceability / preserve option set
```

This differs from creating a new asset, but it can still be productive activity.

```text
Maintenance != NewInvestmentByDefinition
Maintenance != ZeroProduction
NoNewAsset != NoCreatedOrPreservedCapability
```

## 3.6 Production is dynamic

The minimum dynamic relation is:

```text
Resources_t
+ Capabilities_t
+ Technology_t
+ Organization_t
+ Work_t
→ Output_t
+ Learning_t
+ Wear_t
+ Knowledge_t
+ OrganizationalChange_t
+ ExternalEffects_t
→ FeasibleSet_{t+1}
```

This is the key distinction from HF18's fixed-feasible-set mechanism problems.
Production can **change the future feasible set**.

---

# 4. Productivity, efficiency and contribution

## 4.1 Productivity is a relation, not a trait

```text
Productivity_D
= OutputMeasure_D / InputMeasure_D
```

or a multi-input index/model of how outputs change relative to inputs.

Examples:

```text
LaborProductivity = output / labor input
CapitalProductivity = output / capital input
MultifactorProductivity = residual/index after measured labor and capital contributions
TaskThroughput = completed task units / time
```

Every productivity number inherits a production boundary, output quality rule,
input definition and aggregation rule.

```text
Productivity != Effort
Productivity != Skill
Productivity != WorkerTrait
Productivity != TechnologyOnly
Productivity != Welfare
```

## 4.2 Labor productivity is not the worker's marginal contribution

If worker A and worker B use different equipment, software, colleagues, customer
mixes, organizational routines or demand conditions, output per hour differs even if
human capability is identical.

```text
LaborProductivity
= property of worker × task × technology × capital × organization × demand/measurement
```

not a context-free property of the human.

## 4.3 Marginal product is model-relative

```text
MarginalProduct_i(M)
= change in modeled output from a specified marginal/counterfactual change in input i
  under model M and its held-fixed assumptions
```

In team production or nonseparable systems, individual contributions may be difficult
or impossible to identify directly.

```text
ObservedTeamOutput != DirectlyObservedIndividualMarginalProduct
Wage != MarginalProductByDefinition
Compensation != ContributionByDefinition
```

## 4.4 MFP/TFP is not a clean technology variable

Current OECD productivity guidance explicitly treats multifactor productivity as a
residual affected by management practices, organizational change, knowledge, network
effects, scale, market structure, adjustment costs and measurement error.

Therefore:

```text
MFPResidual != PureTechnology
Residual != CausalFactor
UnexplainedOutputGrowth != InnovationByDefinition
```

This is a major measurement firewall for HF19.

---

# 5. Technology, technique, tool, knowledge, skill and innovation

## 5.1 Technology is a feasible-transformation structure

HF19 needs a concept that can survive beyond hardware:

```text
Technology_D
= reproducible knowledge/method/artifact/process structure that changes the feasible
  relation between admitted inputs, actions and outputs in domain D
```

Equivalent economic projections may represent it as a production set, process set or
input-output opportunity set.

Technology may be embodied in machines/software or disembodied in procedures,
designs and codified knowledge.

```text
Technology != Tool
Technology != KnowledgeOnly
Technology != Technique
Technology != Innovation
```

## 5.2 Technique is a selected method within a possibility space

```text
Technique
= particular way/configuration of performing a transformation under available
  technology and organization
```

Two firms can have access to similar technology but choose different techniques.

```text
TechnologyAvailable != TechniqueSelected
TechniqueSelected != TechniqueExecutedCorrectly
```

## 5.3 Tool is a mediator, not capability by itself

HF11 already reconstructed tool use and calibration. HF19 consumes it:

```text
ToolAvailability
→ only an option

EffectiveToolUse
requires access + task fit + skill/calibration + workflow integration + reliability
```

Therefore:

```text
ToolAvailable != Capability
ToolAdopted != ProductivityGain
SameTool != SameOutput
```

## 5.4 Knowledge and skill remain distinct

HF8 and HF6/HF11 already separate knowledge, learning, skill and execution. HF19 adds
the economic relation:

```text
Knowledge can enter production through design, diagnosis, coordination or instruction.
Skill can change the feasible quality/speed/reliability of action.
Neither is reducible to hours supplied.
```

```text
Knowledge != Skill
Skill != Technology
HumanCapitalMeasure != SkillOntology
```

## 5.5 Technology can be endogenous

Arrow-style learning-by-doing and Romer-style endogenous technological change reject a
world in which technology must always arrive as an unexplained external parameter.

```text
Production_t → Experience_t → Capability/Technique_{t+1}
R&DInvestment_t → Knowledge/Technology_{t+1}
```

Therefore:

```text
Technology_t != ExogenousParameterByDefinition
Production != PassiveUseOfFixedTechnology
Learning != FormalTrainingOnly
```

## 5.6 Innovation requires novelty plus implementation under a boundary

OECD innovation measurement separates invention/idea from implemented product or
process change. HF19 therefore keeps:

```text
Idea != Invention != Innovation != Diffusion != Adoption != EffectiveIntegration
```

An innovation can fail commercially or socially; novelty is not value by definition.

```text
Innovation != Success
Innovation != WelfareImprovement
Innovation != TechnologyFrontierAdvanceByDefinition
```

---

# 6. Capital without the money collapse

## 6.1 Capital is not one homogeneous substance

`Capital` is too overloaded to be a primitive. HF19 uses typed projections.

### Physical capital

```text
PhysicalCapitalAsset
= durable produced asset that can supply productive services across periods

CapitalService_D
= flow of productive service from an admitted asset under D
```

```text
AssetStock != CapitalServiceFlow
PurchasePrice != ProductiveContribution
InstalledAsset != EffectiveUtilization
```

### Infrastructure

```text
Infrastructure
= durable enabling system whose services support many downstream activities/users
```

It can be privately, publicly, cooperatively or jointly governed. Infrastructure is
therefore not a synonym for privately owned firm capital.

### Human capital

Use only as an economic measurement projection:

```text
HumanCapital_D
= health/knowledge/skill/experience attributes admitted by model D because they affect
  future productive capability or returns
```

Hard firewall:

```text
HumanCapital_D != Human
HumanCapital_D != PropertyRightOverPerson
HumanCapital_D != MoralWorth
HumanCapital_D != CompleteCapability
```

### Knowledge/intangible capital

Some durable knowledge assets, software, R&D results, data structures or intellectual
property can provide future productive services under an accounting/economic model.
Their exact boundary is model- and accounting-standard-specific.

### Organizational capital

Prescott–Visscher supplies a distinct model in which accumulated information and
organization affect a firm's production possibility set and can be jointly produced
with current output.

HF19 generalizes carefully:

```text
OrganizationalCapital_D
= persistent organization-specific information/routines/relations/configurations that
  change future productive capability under D
```

This is not identical to current org chart or firm market value.

### Natural resources

Natural resources can be productive inputs or stocks. Whether a model calls a resource
stock “natural capital” is a projection choice; HF19 does not require that label.

## 6.2 Money and financial claims are not productive capital by identity

```text
Money
= monetary asset / settlement and purchasing-power instrument under a monetary system

FinancialClaim
= claim on future payments, ownership cash flows or another financial obligation/right
```

Money can finance acquisition of productive assets. A financial claim can finance an
enterprise or represent ownership. Neither fact makes the token/claim itself identical
to the underlying productive capital service.

```text
Money != Machine
FinancialClaim != UnderlyingProductiveAsset
Funding != Production
PortfolioPurchase != RealInvestmentByDefinition
```

## 6.3 Capital heterogeneity matters

Different assets provide different services, depreciation patterns, complementarities,
location constraints and redeployability.

```text
K_total scalar
```

may be useful in a macro model, but is not an ontological claim that all capital is one
interchangeable substance.

```text
AggregateCapital_M != HomogeneousReality
SameBookValue != SameProductiveService
SameCapitalStock != SameFeasibleSet
```

---

# 7. Investment, maintenance, depreciation and future options

## 7.1 Real investment and financial investment are distinct

```text
RealInvestment_D
= current resource commitment that creates or materially expands future productive
  asset/capability/service capacity under D

FinancialInvestment
= acquisition/holding of a financial claim with expected future return or other
  financial objective
```

Financial investment can fund real investment, but the two can occur separately.

```text
FinancialInvestment != RealCapitalFormation
SecurityPurchase != NewProductiveCapacityByDefinition
RealInvestment != OwnershipTransfer
```

## 7.2 Capability investment can be non-physical

Current sacrifice can expand future capacity through:

```text
training / learning
R&D
software/data creation
process redesign
relationship building
organizational learning
infrastructure
physical assets
```

Accounting standards may capitalize some and expense others. HF19 keeps accounting
classification separate from causal future-capability effects.

## 7.3 Depreciation has several layers

```text
PhysicalDeterioration
!= FunctionalObsolescence
!= EconomicValueDecline
!= AccountingConsumptionOfFixedCapital
```

Maintenance can slow some forms but not others.

## 7.4 Investment changes the option set

A production foundation needs an explicitly intertemporal view:

```text
CurrentResourceUse
→ FutureCapacity / FutureOptionality / FutureDependency
```

An investment can expand one feasible set while narrowing another through
irreversibility, debt, lock-in, asset specificity or maintenance burden.

```text
MoreInvestment != MoreOptionalityByDefinition
CapacityGain != FlexibilityGain
```

---

# 8. Specialization, division of labor and coordination

## 8.1 Current task allocation is not specialization history

```text
TaskAllocation_t
= who/what performs which tasks now

DivisionOfLabor_t
= structured partition of productive tasks across actors/units now

Specialization_{t0:t}
= history-dependent concentration of practice, knowledge, equipment or role that
  changes comparative capability/cost across tasks
```

Therefore:

```text
CurrentTaskAssignment != Specialization
Occupation != SpecializationLevel
Specialization != SkillByDefinition
```

## 8.2 Specialization can raise productivity through several mechanisms

Possible mechanisms include:

```text
learning-by-doing
reduced switching/setup cost
dedicated tools/capital
deeper task-specific knowledge
comparative advantage
parallelism
standardization
```

No one mechanism is definitional.

## 8.3 Specialization also creates coordination costs and dependencies

Becker–Murphy explicitly models the tradeoff between specialization gains and costs of
coordinating complementary specialized workers.

HF19 generalizes:

```text
NetSpecializationEffect
= LocalSpecializationGain
- CoordinationCost
- IntegrationCost
- BottleneckCost
- Dependency/FragilityCost
+ Learning/Scale/KnowledgeEffects
```

with signs and magnitudes domain-specific.

```text
MoreSpecialization != HigherSystemProductivityByDefinition
LocalEfficiency != SystemResilience
SpecializationGain != IndependenceGain
```

## 8.4 Dependency is not merely a defect

Complementarity means a specialist may become more productive precisely because other
specialists exist. The same architecture can increase total capability and mutual
dependency.

```text
HigherCapability + HigherDependency
```

is coherent.

This reconnects HF12/HF13: coordination, trust, role structure and power can all change
when specialization deepens.

---

# 9. Team production and attribution

## 9.1 Team production is not merely many independent producers added together

```text
TeamProduction_D
= production where joint configuration/interdependence makes output depend on the
  combination or coordination of multiple contributors under D
```

Possible sources:

```text
complementarity
shared state
shared equipment
workflow sequencing
knowledge integration
joint control
unobservable intermediate contribution
```

## 9.2 Individual marginal contribution may be latent or model-dependent

Alchian–Demsetz pressure-tests the simple attribution model: in team production,
individual marginal products may be costly to observe separately, creating monitoring
and incentive problems.

```text
TeamOutput != Sum(DirectlyObservedIndividualContributions)
```

This does not imply individual contribution is meaningless. It implies attribution may
require counterfactual/model assumptions.

## 9.3 Contribution, compensation and value capture must stay separate

```text
Contribution_M
!= Wage
!= RevenueShare
!= OwnershipShare
!= BargainingOutcome
!= MoralDesert
```

HF18 explains bargaining/incentive implementation; HF14 governs normative evaluation.
HF19 must not infer justice from production attribution.

---

# 10. Firm, market, hierarchy, hybrid, network and peer production

## 10.1 There is no single surviving universal theory of the firm

HF19 treats “firm” as a projection family because mature theories isolate different
mechanisms.

A minimum operational representation is:

```text
FirmView_D
= bounded economic organization under D, containing some persistent combination of
  participants, assets/access, decision rights, contracts/relations, routines,
  information flows and claims used to coordinate economic activity across time
```

This is deliberately not a legal definition and not a single causal theory.

```text
Firm != LegalPersonByDefinition
Firm != HierarchyOnly
Firm != ContractOnly
Firm != AssetOwnershipOnly
Firm != TransactionCostOnly
```

## 10.2 Market and firm are modes of coordination, not mutually exclusive substances

A physical production step can be coordinated by:

```text
spot price
long-term contract
employment relation
internal authority
partnership
franchise
platform rules
network relation
peer governance
cooperative governance
public administration
```

Real organizations frequently combine these.

```text
Market | Firm
```

is therefore not an exhaustive binary ontology.

## 10.3 Hierarchy is a decision-right structure

```text
Hierarchy_D
= ordered distribution of decision/review/override rights under D
```

It need not imply unlimited coercive authority, one command chain, ownership or moral
legitimacy.

```text
ManagerialAuthority != LegalSovereignty
Authority_D != UnlimitedFiat
Hierarchy != Ownership
Hierarchy != Legitimacy
```

## 10.4 Network is a relation pattern, not a governance solution by itself

```text
Network
= graph/pattern of persistent relations or dependencies among actors/units
```

A network can contain market exchanges, hierarchy, trust, contracts, platform rules or
peer coordination.

```text
Network != DecentralizedByDefinition
Network != MarketByDefinition
Network != NoAuthority
```

## 10.5 Peer production is a genuine production organization class

Benkler's open-source/peer-production work falsifies a simple market-versus-managerial-
hierarchy exhaustive dichotomy for information production.

HF19 uses:

```text
PeerProduction_D
= distributed production where contribution and task matching are not primarily
  organized by ordinary employment hierarchy or spot-market price signals under D
```

It can still have maintainers, rules, reputation, modular architecture and asymmetric
control.

```text
PeerProduction != NoGovernance
VolunteerContribution != NoIncentives
OpenSource != NoOwnershipOrLicensingStructure
```

---

# 11. Competing models of firms and economic organization

HF19 does not merge these models into one giant theory. It stores their question,
strength and failure boundary.

## Model F1 — Production-function / price-taking firm

```text
Firm = transformation unit choosing inputs/output under a production function and prices
```

Useful for:

- cost/output optimization;
- marginal conditions;
- aggregate growth/productivity benchmarks.

Fails when the question is:

- why the firm boundary exists;
- who has authority/control;
- why contracts are incomplete;
- why internal organization differs;
- why peer production works.

Disposition: **retain as benchmark, reject as complete firm ontology**.

## Model F2 — Coase transaction-cost substitution

```text
Firm exists where directing resources inside organization can avoid some costs of using
market price contracting, until internal organization costs offset the gain.
```

Useful for:

- market/firm boundary;
- contracting/coordination costs;
- why internal direction can substitute for repeated market exchange.

Fails as a total ontology because:

- internal authority itself needs explanation;
- team production and ownership/control have additional structure;
- hybrid/peer forms exist;
- “transaction cost” does not encode all production capability.

Disposition: **retain as boundary theory, reject Firm=TransactionCostOnly**.

## Model F3 — Simon employment/authority

```text
Employment relation trades a specified zone of future decision discretion/authority
rather than contracting every future action ex ante.
```

Useful for:

- incomplete future task specification;
- managerial authority and adaptation;
- employment versus sale of fully specified service.

Pressure:

- authority is bounded by contract/institution/law;
- independent contractors and partners can perform same tasks;
- Alchian–Demsetz denies that firm has a uniquely coercive fiat power.

Disposition: **retain typed managerial authority; reject unlimited-fiat interpretation**.

## Model F4 — Alchian–Demsetz team-production/monitoring

```text
Joint production + costly attribution of marginal product → monitoring and residual-claim
arrangements can organize team inputs.
```

Useful for:

- nonseparable team output;
- monitoring incentives;
- why contribution measurement matters.

Pressure:

- not every firm has hard-to-separate team production;
- monitoring does not explain all ownership/investment boundaries;
- its anti-authority semantics conflicts with ordinary authority language unless rights
  are typed carefully.

Disposition: **retain for team-production architecture; reject universalization**.

## Model F5 — Jensen–Meckling agency / nexus of contracts

```text
Firm structure reflects contracts/claims and agency costs among principals, agents,
creditors and equity holders.
```

Useful for:

- separation of ownership/control;
- debt/equity incentives;
- monitoring/bonding/residual-loss analysis.

Pressure:

- contract nexus does not exhaust routines, identity, authority, production technology or
  peer/cooperative forms;
- agency-cost efficiency is not legitimacy.

Disposition: **retain agency/claim projection; reject Firm=ContractNexusOnly**.

## Model F6 — Williamson transaction-cost governance

```text
Market, hybrid and hierarchy are alternative governance structures whose comparative
costs/adaptation properties vary with transaction attributes such as specificity and
uncertainty.
```

Useful for:

- hybrid governance;
- asset specificity;
- comparative institutional choice.

Pressure:

- production capabilities can change endogenously with organization;
- institutional legitimacy and power are outside pure cost minimization;
- peer/community production is not naturally exhausted by the triad.

Disposition: **retain comparative-governance projection; reject universal efficiency
ranking**.

## Model F7 — Grossman–Hart / Hart–Moore property-rights theory

```text
Incomplete contracts make residual control rights over assets consequential; ownership
changes ex-post control and ex-ante investment incentives.
```

Useful for:

- integration/nonintegration;
- asset ownership;
- specific investment incentives;
- partnership/cooperative control variants.

Pressure:

- model ownership is an analytical residual-control construct, not the entire legal/social
  bundle of ownership;
- human capital is nonalienable in the model tradition and cannot be treated like owned
  physical assets;
- control-right efficiency does not settle justice/legitimacy.

Disposition: **retain residual-control projection; reject Ownership=ResidualControlTotality**.

## Model F8 — Organizational-capital / capability accumulation

```text
Persistent organization-specific information/routines/relations alter future production
possibilities and can be accumulated jointly with output.
```

Useful for:

- history dependence;
- why copying physical capital does not copy productivity;
- growth and adjustment costs.

Pressure:

- “capital” can become an everything-residual if not typed;
- routines can be maladaptive as well as valuable;
- organizational value is context-dependent.

Disposition: **retain persistent-capability state; reject capitalization of every
organizational difference**.

## Model F9 — Specialization / coordination-cost model

```text
narrower task concentration can raise local productivity while increasing coordination
cost among complementary specialists
```

Useful for:

- division of labor;
- knowledge depth;
- team size and coordination tradeoffs.

Pressure:

- specialization effects depend on learning, task structure, market/organization and
  technology;
- dependency/resilience is not represented by productivity alone.

Disposition: **retain as tradeoff model, reject SpecializationAlwaysGood**.

## Model F10 — Peer-production model

```text
modularity/granularity/integration cost and distributed matching can make nonproprietary
peer production competitive with firms/markets in some information domains
```

Useful for:

- open-source and distributed information production;
- contribution without ordinary wage hierarchy;
- alternative task matching.

Pressure:

- integration/governance cost remains;
- not all goods are modular, cheap to duplicate or remotely integrable;
- peer systems can develop concentrated authority/status.

Disposition: **retain as distinct organization form, reject PeerProductionUniversalism**.

## Model F11 — Complementarity / modern manufacturing model

```text
technology, strategy, work practices and organization may form complementary bundles,
so isolated adoption can underperform coordinated system change
```

Useful for:

- why same machine/software has different value across firms;
- clustered organizational change;
- scope/flexibility transitions.

Pressure:

- complementarity is domain- and parameter-specific;
- co-adoption does not prove causal complementarity.

Disposition: **retain complementarity relation; reject “best practice independently
additive” assumption**.

## Model F12 — Task-based automation model

```text
production contains tasks; automation reallocates some tasks from labor to capital/
technical systems, while new tasks can reinstate human labor
```

Useful for:

- automation versus augmentation;
- labor demand and task composition;
- job recomposition.

Pressure:

- real systems include quality, learning, organizational redesign and demand effects;
- AI can advise rather than execute;
- “capital” may be rented service rather than owned asset.

Disposition: **retain task reallocation; reject Automation=WholeJobSubstitution**.

---

# 12. Ownership, possession, title, access, use and control

## 12.1 Ownership is a rights bundle/projection family

Minimum separations:

```text
LegalTitle
Possession
Access
UseRight
ExclusionRight
TransferRight
IncomeClaim
ResidualClaim
DecisionRight
ResidualControlRight
Liability/Risk
GovernanceRight
```

Different systems bundle them differently.

```text
Ownership != Possession
Ownership != Use
Ownership != Access
Ownership != ControlByDefinition
Ownership != ResidualIncomeClaim
ResidualControl != ResidualIncomeClaim
```

An owner can lease an asset to another possessor/user. A lender can hold a security
interest without ordinary use. A cooperative can distribute governance and claims
differently from an investor-owned corporation.

## 12.2 Residual control is a powerful model, not the whole ontology

Grossman–Hart define ownership in their model through residual rights over assets when
specific rights are costly to enumerate. Hart–Moore then use asset control to study
firm boundaries and investment.

HF19 preserves the theorem-level insight without promoting the model definition into a
universal legal definition:

```text
Ownership_PRT(M) = ResidualControlRights under model M
```

not:

```text
AllRealWorldOwnership = ResidualControlOnly
```

## 12.3 Possessing a productive resource does not imply owning it

Cases:

```text
leased machine
rented cloud GPU
licensed software
borrowed tool
API subscription
franchise asset
company laptop used by employee
```

all separate current productive access from legal ownership.

This becomes critical for AI:

```text
AIServiceAccess != OwnedAICapital
```

## 12.4 Ownership efficiency and ownership legitimacy remain firewalled

A property-rights model can predict which allocation of control improves a modeled
investment incentive. That does not establish whether the ownership arrangement is
just, legitimate or morally permissible.

```text
EfficientOwnership_M
!= JustOwnership
!= LegitimateOwnership
!= DeservedOwnership
```

HF14/HF17 retain authority over the normative layer.

---

# 13. Incomplete contracts, asset specificity and hold-up

## 13.1 Incomplete contract does not mean no contract

```text
IncompleteContract_D
= agreement whose enforceable specified terms do not exhaust all future relevant
  actions/states/contingencies under D
```

Reasons can include:

```text
unforeseeability
verification cost
writing/enforcement cost
complexity
adaptation needs
ambiguous quality
```

```text
IncompleteContract != InformalAgreement
IncompleteContract != ContractFailure
```

## 13.2 Asset specificity is relational

```text
AssetSpecificity_D
= degree to which an investment/resource loses value or productive fit when redeployed
  to alternative counterparties/uses under D
```

It is not simply “specialized asset” as an intrinsic label.

```text
Specificity != PhysicalUniqueness
Specificity_D1 != Specificity_D2
```

## 13.3 Hold-up is an ex-post bargaining/investment problem

A canonical structure is:

```text
Party invests ex ante
→ investment raises joint surplus in a relationship
→ future terms cannot be fully committed
→ ex-post bargaining can appropriate part of investment return
→ ex-ante investment incentive changes
```

```text
HoldUpRisk != FraudByDefinition
HoldUp != VerticalIntegrationAlwaysOptimal
SpecificInvestment != HoldUpInevitable
```

Ownership, contract design, reputation, repeated interaction and alternative governance
can change the problem.

---

# 14. Scale, scope, complementarity and network effects

## 14.1 Returns to scale and economies of scale differ

```text
ReturnsToScale_M
= how modeled output changes when a specified vector of inputs is scaled

EconomiesOfScale_D
= how unit/average cost changes with output scale under D
```

Prices, fixed costs, utilization and organization can make cost-scale behavior differ
from a pure production-function scaling property.

```text
ReturnsToScale != EconomiesOfScale
LargeFirm != ScaleEconomy
ScaleEconomy_D != InfiniteEfficientSize
```

Coase already supplies the counterforce: internal organization costs and errors can
rise with firm size.

## 14.2 Economies of scope are joint-production relations

```text
EconomiesOfScope_D(A,B)
when joint production of A and B uses fewer admitted costs/resources than producing
A and B separately under D
```

```text
Scope != Scale
Multiproduct != ScopeEconomyByDefinition
Diversification != ProductiveSynergyByDefinition
```

## 14.3 Complementarity is a marginal interaction, not co-occurrence

A useful economic definition is:

```text
Complementarity_D(X,Y)
when increasing X raises the return/value of increasing Y (and/or vice versa) under D
```

Technology, training, workflow redesign and incentives may therefore be complements.

```text
CoAdoption != Complementarity
Complementarity != Indispensability
Complementarity_D != Complementarity_E
```

## 14.4 Network effects are not production economies by identity

Demand-side/user-side network effects can increase a product's value with more users.
That differs from producing each unit more cheaply at larger scale.

```text
NetworkEffect != EconomiesOfScale
NetworkEffect != NetworkOrganization
```

---

# 15. Automation, substitution, augmentation and recomposition

## 15.1 Automation is task/process-level transfer of execution/control

```text
Automation_D
= transfer of some task/process execution, monitoring, decision or control function
  from a human/manual arrangement to a technical system under D
```

It can be partial.

```text
Automation != FullHumanRemoval
Automation != AIByDefinition
AIUse != AutomationByDefinition
```

## 15.2 Substitution and complementarity can coexist

Task-based automation models show a displacement effect when capital/technology takes
over tasks previously performed by labor, while new tasks can create a reinstatement
effect.

At the same time, AI assistance can raise a human worker's throughput or quality.

Therefore one system can simultaneously exhibit:

```text
Task A: human substitution
Task B: human augmentation
Task C: new human oversight
Task D: new machine-only task
Task E: removed task
```

```text
Automation != LaborSubstitutionOnly
TaskSubstitution != OccupationElimination
ProductivityGain != LaborDemandGain
ProductivityGain != LaborShareGain
```

## 15.3 Automation can change learning, not only current output

The 2025 *Generative AI at Work* field study found context-specific heterogeneous
productivity gains and evidence of faster learning for less experienced workers.
It also found small quality declines for some highly skilled workers.

The correct HF19 inference is narrow:

```text
AIConfiguration_D can change
  throughput + quality + learning trajectory + experience distribution
```

not:

```text
AI universally raises productivity
AI universally equalizes skill
AI universally deskills work
```

## 15.4 AI has typed economic roles

The same artificial system can occupy different roles simultaneously:

```text
Tool
DecisionSupport
AutomationComponent
AugmentationSystem
DelegatedAgent
PurchasedService
IntermediateInput
OwnedOrLeasedCapitalService
OrganizationalInfrastructure
Knowledge/RoutineCarrier
Monitoring/ControlSystem
```

Its role depends on ownership/access, task delegation, control, persistence, accounting
boundary and production architecture.

Therefore:

```text
AI != LaborByDefinition
AI != CapitalByDefinition
AI != EmployeeByDefinition
AI != ToolOnly
AI != AutonomousEconomicAgentByDefinition
```

A rented API can be an intermediate purchased service in one accounting projection and
a capability-bearing infrastructure component in another without contradiction.

---

# 16. Value creation, value capture, output, revenue, profit and welfare

## 16.1 These quantities are not synonyms

Keep at least:

```text
Physical/ServiceOutput
AccountingOutput_D
ValueAdded_SNA
Revenue
AccountingProfit
EconomicProfit_M
Surplus_M
ValueCreated_M
ValueCaptured_M
Consumer/ProducerSurplus_M
Welfare_N
MoralValue_N
```

where `M` denotes model-relative and `N` normative evaluation where appropriate.

## 16.2 Revenue can change without production changing

If price doubles while physical quantity and quality are unchanged:

```text
Revenue ↑
PhysicalOutput =
```

If market power changes price, value captured may change without a matching change in
productive contribution.

```text
Revenue != Output
Revenue != ValueCreated
Revenue != Welfare
```

## 16.3 Accounting value added is a statistical construct

National accounts use value-added/accounting boundaries to avoid double counting and
connect production with income. This is not identical to philosophical or welfare
value.

```text
AccountingValueAdded != MoralValue
GDPContribution != WelfareContribution
ProductionGrowth != WelfareGrowthByDefinition
```

## 16.4 Value creation and capture can be modeled separately

Brandenburger–Stuart provide one formal cooperative-game account of value created with
suppliers/buyers and of added value constraining capture under specified conditions.
HF19 keeps the separation while not universalizing their exact model.

```text
ValueCreated_M != ValueCaptured_M
ValueCaptured_M != ProductiveContributionByDefinition
```

Capture can depend on bargaining position, ownership, alternatives, market power,
contracts, institutions and timing — many already reconstructed in HF13/HF18.

## 16.5 Production efficiency does not settle distribution

A production system can be highly productive while distributing claims, risk,
authority or welfare in many different ways.

```text
EfficientProduction_M
!= FairDistribution
!= LegitimateAuthority
!= HighWorkerWelfare
```

This preserves the normative firewall from HF14–HF17.

---

# 17. Economic organization as the surviving integration layer

## 17.1 Minimum definition

```text
EconomicOrganization_D
= persistent configuration of
  productive tasks,
  participants/capabilities,
  assets/access,
  technology/techniques,
  information flows,
  decision/authority/control rights,
  contracts and relational commitments,
  ownership/claims,
  coordination mechanisms,
  monitoring/incentives,
  maintenance/investment,
  and boundaries with markets/networks/institutions
that shapes production, exchange and future productive capability under D.
```

It is intentionally broader than `Firm`.

## 17.2 Organization is itself production-relevant

```text
Same people
+ same physical assets
+ same nominal technology
```

can produce different outcomes under different:

```text
workflow
information routing
task allocation
incentives
authority
integration
maintenance
quality control
learning loops
```

Therefore:

```text
Organization != WrapperAroundProduction
Organization is one input/state of effective production capability
```

## 17.3 Organization can accumulate and decay

```text
Routines_t + relationships_t + shared representations_t + interfaces_t
→ OrganizationalCapability_{t+1}
```

but turnover, obsolete routines, technical change or institutional disruption can also
erode it.

```text
OrganizationalPersistence != OrganizationalValue
OldRoutine != GoodRoutine
```

## 17.4 Economic organization changes power and dependency as well as output

HF13/HF14 connections:

```text
TaskDivision
Ownership
AccessControl
Specialization
Monitoring
ExitOptions
```

can change bargaining power, dependency, vulnerability and authority even when total
output rises.

Therefore production analysis must not hide distributional/institutional effects in a
single efficiency scalar.

---

# 18. Cross-context falsification matrix

The following cases attack the candidate collapses directly.

| Case | Context | Observation | Collapse falsified |
|---|---|---|---|
| F01 | own-use household work | productive service occurs without pay/profit | `Work = Employment` |
| F02 | volunteer/open-source work | output exists without ordinary wage relation | `Work = WageLabor` |
| F03 | same programmer task as employee/contractor/partner | task constant, relation changes | `Task = EmploymentStatus` |
| F04 | dependent contractor | commercial contract can coexist with economic dependence | `Contractor = Independent` |
| F05 | same hours, newer machine/software | output differs with capital/technology | `Hours = ProductiveContribution` |
| F06 | poor workflow, high effort | effort high while throughput low | `Effort = Productivity` |
| F07 | automated process, same output | human effort falls while output remains | `Output = HumanEffort` |
| F08 | AI assistance | same worker changes throughput under tool configuration | `Productivity = WorkerTrait` |
| F09 | AI novice/expert heterogeneity | same tool has different effects by experience | `ToolEffect = Constant` |
| F10 | AI quality/throughput tradeoff | throughput can rise while quality falls for subgroup | `ProductivityMetric = TotalValue` |
| F11 | team surgery/software/research | joint result cannot be read as separable observed products | `TeamOutput = ObservableIndividualMarginalProducts` |
| F12 | market outsourcing vs internal team | same physical transformation, governance changes | `Production = GovernanceForm` |
| F13 | Coase internalization boundary | market contracting and internal direction have different costs | `Market = CostlessDefault` |
| F14 | Williamson franchise/long contract | hybrid sits between spot market and hierarchy | `Market | Hierarchy` exhaustive |
| F15 | Linux/open source | large information product without standard wage hierarchy/spot prices | `Production = FirmOrMarketOnly` |
| F16 | leased machine | user/possessor differs from legal owner | `Ownership = Possession` |
| F17 | rented cloud/API | productive access without ownership | `ProductiveInput = OwnedCapital` |
| F18 | shareholder vs manager | residual claim and operational control can separate | `IncomeClaim = Control` |
| F19 | cooperative/partnership | governance/control can be bundled differently | `Firm = InvestorOwnedCorporation` |
| F20 | specific supplier investment | ex-post bargaining changes ex-ante investment incentives | `ContractPrice = FullOrganizationProblem` |
| F21 | reusable general machine vs dedicated tooling | redeployability changes relationship dependence | `AssetSpecificity = AssetPrice` |
| F22 | cash balance vs CNC machine | both called capital colloquially, only one directly supplies machine service | `Capital = Money` |
| F23 | financial security purchase | claim changes hands without new productive asset | `FinancialInvestment = RealInvestment` |
| F24 | training/R&D/process redesign | future productive capability expands without new machine | `Investment = PhysicalAssetPurchase` |
| F25 | maintenance | future serviceability preserved without new gross asset | `NoNewAsset = NoProductionEffect` |
| F26 | organizational routines | same people/assets can produce differently after process redesign | `Capital+Labor = CompleteProductionState` |
| F27 | specialization | task focus raises local speed but creates integration dependence | `SpecializationGain = SystemGain` |
| F28 | supply-chain bottleneck | highly efficient specialists fail when complement unavailable | `LocalProductivity = Resilience` |
| F29 | scale-up | internal coordination/error cost can rise with size | `BiggerFirm = MoreEfficient` |
| F30 | multi-product platform/factory | joint resources can create scope economies without simple volume scaling | `Scope = Scale` |
| F31 | complementary tech+training | isolated tool adoption underperforms bundled change | `TechnologyEffect = AdditiveToolEffect` |
| F32 | network effect product | user value grows with network independent of unit production cost | `NetworkEffect = ScaleEconomy` |
| F33 | price increase, same output | revenue rises without more physical/service output | `Revenue = Output` |
| F34 | bargaining-power shift | capture changes without matching production change | `ValueCapture = ValueCreation` |
| F35 | polluting/high-harm production | measured output can rise while welfare falls | `ProductionGrowth = WelfareGrowth` |
| F36 | innovative but failed process | novelty/implementation exists without commercial success | `Innovation = Success` |
| F37 | same technology, missing skill/integration | availability does not yield same effective capability | `TechnologyAvailable = Productivity` |
| F38 | learning by doing | production changes future capability | `Production = StaticTransformationOnly` |
| F39 | R&D-generated technique | technology changes through intentional investment | `Technology = ExogenousByDefinition` |
| F40 | AI advice rather than execution | AI can affect work without automating the task | `AIUse = Automation` |

No candidate single-collapse theory survives this matrix.

---

# 19. Cross-context model comparison

| Question | Production function | Coase/TCE | Simon authority | Team production | Property rights | Org capital | Peer production | Task automation |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| input-output efficiency | strong | weak | weak | medium | medium | medium | medium | strong |
| why internalize | weak | strong | medium | medium | strong | medium | weak | weak |
| employment discretion | weak | medium | strong | medium | medium | weak | weak | medium |
| contribution observability | weak | weak | weak | strong | medium | medium | medium | medium |
| ownership/control | weak | medium | weak | medium | strong | weak | medium | weak |
| specific investment | weak | strong | weak | weak | strong | medium | weak | medium |
| history/routines | weak | weak | medium | medium | medium | strong | medium | medium |
| nonmarket/nonhierarchical production | weak | weak | weak | weak | medium | medium | strong | medium |
| automation/task recomposition | medium | weak | medium | medium | medium | medium | medium | strong |
| legitimacy/justice | out | out | out | out | out | out | out | out |

`out` is deliberate: HF14–HF17 own normative authority. No economic-organization model
is permitted to generate legitimacy by optimization.

---

# 20. What survives the falsification

The minimum HF19 grammar is not one firm definition. It is a typed production system:

```text
Human/Agent
  ├─ performs Work_Broad
  ├─ may supply LaborService_D
  ├─ exerts Effort under task/control conditions
  ├─ occupies Task / Job / Occupation projections
  └─ may be Employee / Contractor / Partner / OwnerOperator / Volunteer / ...

ProductionSystem_D
  ├─ Inputs
  ├─ Technology
  ├─ Technique
  ├─ Organization
  ├─ Work/Labor services
  ├─ Capital services / infrastructure / intermediate inputs
  ├─ Outputs / services / maintained states / byproducts
  └─ dynamic effects on learning, wear, knowledge and future feasible sets

EconomicOrganization_D
  ├─ TaskAllocation / DivisionOfLabor / Specialization
  ├─ Coordination / information flow
  ├─ Contracts / employment relations
  ├─ Authority / decision / override rights
  ├─ Ownership / access / use / control / claims
  ├─ Monitoring / incentives
  ├─ Market / hierarchy / hybrid / network / peer modes
  └─ investment / maintenance / adaptation
```

### Core separations

```text
Work != Employment
Labor != Human
Effort != Hours
Task != Job != Occupation
Employment_Statistical != EmploymentRelation

Production != Exchange != Allocation
Transformation != OwnershipTransfer
Output != Revenue != Profit
Output != Value != Welfare
Maintenance != NoProduction

Productivity != Effort
LaborProductivity != WorkerTrait
MFP != PureTechnology
MarginalProduct_M != DirectlyObservedContribution

Technology != Technique != Tool
Knowledge != Skill != Technology
Innovation != Invention != Adoption != Success
Technology != ExogenousByDefinition

CapitalAsset != CapitalService
Capital != Money
FinancialClaim != ProductiveAsset
HumanCapital_D != Human
OrganizationalCapital_D != FirmValue
RealInvestment != FinancialInvestment
Investment != OwnershipTransfer

TaskAllocation != Specialization
SpecializationGain != NetSystemGain
TeamOutput != ObservableIndividualMarginalProduct

Firm != LegalPerson
Firm != TransactionCostOnly
Firm != ContractOnly
Firm != AssetOnly
Market != Hierarchy != Hybrid != Network != PeerProduction
Hierarchy != UnlimitedAuthority
PeerProduction != NoGovernance

Ownership != Possession != Access != Use
ResidualControl != ResidualClaim
IncompleteContract != NoContract
AssetSpecificity != IntrinsicAssetLabel
HoldUp != IntegrationAlwaysOptimal

ReturnsToScale != EconomiesOfScale
Scale != Scope
Complementarity != CoOccurrence
NetworkEffect != ScaleEconomy

Automation != FullHumanRemoval
Automation != SubstitutionOnly
AI != LaborByDefinition
AI != CapitalByDefinition
AIUse != AutomationByDefinition
TaskAutomation != JobElimination

ValueCreation_M != ValueCapture_M
Revenue != ValueCreated
ValueCapture != Contribution
ProductionEfficiency != Justice
ProductionGrowth != WelfareGrowth
```

---

# 21. Dynamic production state

A compact dynamic representation for future Human consumers is:

```text
P_t = ProductionState(
  resources,
  human_capabilities,
  labor_services,
  technology,
  techniques,
  capital_services,
  infrastructure,
  information,
  task_architecture,
  organization,
  contracts,
  ownership_control,
  incentives,
  demand_boundary,
  environment
)

(P_t, action/work_t)
→ {
    output_t,
    quality_t,
    costs_t,
    external_effects_t,
    learning_t,
    depreciation_t,
    organizational_change_t,
    claims/capture_t
  }
→ P_{t+1}
```

This representation is **not** a mandatory database schema. It is a view grammar for
asking what changed and which theory is appropriate.

---

# 22. Human × AI economic-organization matrix

A single AI deployment should be typed along several independent axes:

```text
Role:
  tool | advisor | automator | delegated_agent | coordinator | monitor | infrastructure

Task relation:
  substitute | complement | create | remove | recompose | quality-control

Control:
  human_selects | human_reviews | shared | machine_executes | external_provider_controls

Ownership/access:
  owned | leased | licensed | API_service | open | shared

State effect:
  current_output | human_learning | org_learning | knowledge_capture | dependency | lock-in

Economic relation:
  intermediate_service | capital_service | labor-complement | contractor-like_service |
  internal_infrastructure | market_platform
```

No single label such as `AI worker`, `AI capital` or `AI tool` can substitute for these
axes.

### Hard Human × AI firewalls

```text
DelegatedAgency != EmploymentStatus
ModelAutonomy != LegalPersonhood
AIProductivityGain != HumanCapabilityGain
AIOutput != HumanContribution
AIServiceAccess != AssetOwnership
HumanReview != HumanControlByDefinition
AutomationRate != WelfareGain
```

---

# 23. Measurement and transport audit

Every HF19 measurement must state:

```text
unit of analysis
production boundary
output definition
quality adjustment
input definition
capital-service assumption
time horizon
organization/governance context
ownership/access context
price versus quantity treatment
externality/welfare exclusions
```

## 23.1 Statistical standards are not universal ontology

ILO, SNA and OECD definitions are invaluable because they enforce operational
separations. They remain measurement frameworks.

Never infer:

```text
OutsideGDPBoundary -> NotRealWork
NotEmployment -> NotProductive
AccountingAsset -> PhilosophicalCapitalPrimitive
MFP -> PureTechnology
```

## 23.2 Formal models are conditional

Never infer:

```text
CobbDouglasFit_D -> UniversalProductionFunction
CoaseBoundaryModel -> FirmEssence
PropertyRightsOptimal_D -> UniversalOwnershipOptimum
TaskAutomationModel -> UniversalLaborOutcome
```

## 23.3 Firm evidence transports poorly without organization state

Two nominally similar firms can differ in:

```text
technology vintage
workflow
capital utilization
worker composition
management
market power
contracts
regulation
quality targets
organizational capital
```

A productivity coefficient is not automatically a transferable human prescription.

## 23.4 AI evidence is configuration-specific

Current AI productivity studies are informative falsifiers but weak universal laws.
Transport requires at least:

```text
model/version
interface
prompt/workflow
human skill distribution
task distribution
quality metric
adoption stage
organizational incentives
review/control design
```

---

# 24. Deletion audit

A distinction survives only if deleting it causes repeated prediction/explanation/
decision errors.

## Delete `Work != Employment`

Failure: own-use, volunteer, unpaid trainee and other productive activity disappears.
**Keep.**

## Delete `Effort != Productivity`

Failure: tooling, capital, organization and skill effects are misattributed to effort.
**Keep.**

## Delete `Task != Job`

Failure: automation of one task is misread as elimination of an occupation/job.
**Keep.**

## Delete `CapitalAsset != CapitalService`

Failure: idle/obsolete/poorly integrated assets are treated as equivalent productive
input.
**Keep.**

## Delete `Money != ProductiveCapital`

Failure: financing claims and production capacity become indistinguishable.
**Keep.**

## Delete `Ownership != Possession/Access/Control`

Failure: leases, licenses, firms, cooperatives, security interests and API services are
misrepresented.
**Keep.**

## Delete multiple firm models

Failure: Coase, authority, team production, agency, property rights, org capital and peer
production are forced into one mechanism and lose their explanatory targets.
**Keep plural views.**

## Delete `Specialization != CurrentTaskAllocation`

Failure: learning/history and dependency are lost.
**Keep.**

## Delete `Scale != Scope != NetworkEffect`

Failure: three different economic mechanisms are confused.
**Keep.**

## Delete `ValueCreation != Capture`

Failure: bargaining/ownership outcomes are read as productive contribution.
**Keep.**

## Delete `ProductionEfficiency != Welfare/Justice`

Failure: descriptive economics acquires normative authority.
**Keep as hard firewall.**

---

# 25. Reconnection to HF0–HF18

HF19 adds a new layer; it does not replace prior rounds.

```text
HF4  Effort/value/self-regulation
  → effort can be one work input/state, never productivity by identity

HF6  Learning/development
  → production can create skill and capability through history

HF8  Knowledge/representation
  → knowledge can be a productive input/state but is not technology totality

HF10 Decision/planning/delegation
  → production systems allocate decision and delegated agency

HF11 Action/tool use
  → tool-mediated execution becomes an economic production relation only under a
    production boundary

HF12 Joint action/roles/cooperation
  → team production and division of labor are specialized economic projections

HF13 Power/authority/institutions
  → firm authority, ownership/control and dependency cannot be reduced to efficiency

HF14 Welfare/fairness/justice
  → output/productivity/value capture do not settle welfare or justice

HF15 Moral standing
  → HumanCapital never turns a person into an ownable asset

HF17 Collective governance
  → economic-organization choice can require legitimate collective procedures beyond
    cost minimization

HF18 Strategic implementation
  → incentives/contracts/markets shape production, but do not constitute the whole
    production technology/organization state
```

The durable bridge is:

```text
Intent / capability / action
→ joint work
→ institutional and strategic coordination
→ production and economic organization
→ outputs + future capability + claims + external effects
```

---

# 26. FoundationReopenCondition audit

HF19 tested the frozen foundation interfaces for contradiction.

### A. Repeated category error across domains?
No. Previous distinctions such as effort, skill, agency, authority, welfare and
legitimacy were reusable and prevented economic collapses.

### B. Strong primary evidence directly falsifying a frozen claim?
No.

### C. Missing neighboring distinction causing repeated representational failure?
HF19 itself supplies the missing production/economic-organization distinctions. It does
not reveal a defect inside HF0–HF18.

### D. Contradiction across frozen rounds?
No.

### E. Applied consumers require hidden arbitrary choices because a foundation is wrong?
No concrete evidence in this round.

### F. Normative authority leak from insufficient boundary?
No; HF14–HF17 firewalls remained sufficient when explicitly preserved.

Result:

```text
FoundationReopenCondition = false
```

HF0–HF18 remain frozen.

---

# 27. HF19 stop test

HF19 is complete when the following questions no longer force category collapse:

- Can unpaid work be represented without calling it employment? **Yes.**
- Can the same task appear under employee, contractor, partner and peer relations? **Yes.**
- Can productivity change without effort changing? **Yes.**
- Can production change future capability/technology rather than only consume fixed
  resources? **Yes.**
- Can money/financial claims be separated from productive capital services? **Yes.**
- Can human capital be used as an economic projection without reifying the person as an
  asset? **Yes.**
- Can specialization increase local productivity while increasing dependency and
  coordination cost? **Yes.**
- Can team output exist when individual marginal contributions are not directly
  observable? **Yes.**
- Can Coase, Simon, Alchian–Demsetz, agency, property-rights, organizational-capital and
  peer-production theories coexist as question-relative views? **Yes.**
- Can ownership be separated from possession/access/use/control/claims? **Yes.**
- Can incomplete contracts, specificity and hold-up be represented without declaring
  integration universally optimal? **Yes.**
- Can scale, scope, complementarity and network effects remain distinct? **Yes.**
- Can automation substitute, augment and recompose tasks simultaneously? **Yes.**
- Can AI occupy different economic roles without being universally labeled labor or
  capital? **Yes.**
- Can output/revenue/value creation/value capture/welfare stay separate? **Yes.**
- Can efficient production remain normatively non-authoritative? **Yes.**

The stop condition is satisfied.

---

# 28. HF19 result

HF19 rejects the idea that economic production is adequately represented as:

```text
LaborHours + Money → Output → Revenue
```

The surviving model is dynamic and organizational:

```text
people/capabilities
+ work/labor services
+ resources/capital services
+ technology/techniques
+ information/knowledge
+ task architecture
+ ownership/access/control
+ contracts/incentives
+ organization/governance
+ maintenance/investment
→ production process
→ outputs/services/maintained states + byproducts/external effects
→ learning + depreciation + organizational/technological change
→ future feasible set
```

Economic organization determines not only **how much is produced**, but also:

```text
who performs which tasks
who can decide/override
who owns/accesses/uses assets
who bears risk/dependency
who learns
who captures claims/surplus
which future options become easier or harder
```

The canonical HF19 firewalls are therefore:

```text
Work != Employment
Effort != Productivity
Task != Job
Production != Exchange != Allocation
Output != Revenue != Value != Welfare
Technology != Tool
Capital != Money
CapitalAsset != CapitalService
HumanCapital != Human
Specialization != CurrentTaskAllocation
Firm != OneTheory
Market != Hierarchy != Hybrid != Network != PeerProduction
Ownership != Possession != Access != Control
Investment != FinancialPurchase
Scale != Scope != NetworkEffect
Automation != SubstitutionOnly
AI != LaborOrCapitalByDefinition
ValueCreation != ValueCapture
ProductionEfficiency != JusticeOrLegitimacy
```

HF19 is **READY** as Human Foundations' canonical production/economic-organization
view library.

No HF20 is selected or scheduled here. The continuation document preserves only the
post-HF19 stop/reopen protocol and a residual watch discipline; a later round requires a
new repeated boundary, not curriculum momentum.
