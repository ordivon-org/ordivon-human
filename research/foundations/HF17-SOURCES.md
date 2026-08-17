---
schema_version: 1
id: human.foundations.hf17.sources
title: HF17 External Evidence and Source Ledger
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
summary: Primary formal social-choice, political-philosophy, moral-uncertainty and empirical deliberation/AI sources used to reconstruct normative pluralism, social ordering, voting, strategic manipulation, rights constraints, judgment aggregation, expertise, deliberation, representation, AI mediation and robust collective choice, and to expose strategic implementation as the next boundary.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
  - HF17
related:
  - human.foundations.hf17
  - human.foundations.hf16.sources
---
# HF17 External Evidence and Source Ledger

## Evidence rule

HF17 keeps four evidence classes separate:

```text
Formal theorem / characterization
= conditional mathematical result under exact input/domain/axiom assumptions

Normative/political philosophy
= candidate account of legitimacy, rights, expertise, plurality or moral uncertainty

Empirical collective-choice/deliberation evidence
= how people actually change, participate, deliberate, polarize or respond to process

AI-mediated influence evidence
= how model-assisted mediation/persuasion/feedback changes human judgments
```

Never infer:

```text
FormalImpossibility -> InstitutionalVerdict
EmpiricalAgreement -> NormativeTruth
Expertise -> Authority
AIEndorsement -> LegitimateDecision
```

---

# 1. Arrow — Social Choice and Individual Values

## Kenneth J. Arrow (1951; 2nd ed. 1963)

- Cowles Foundation Monograph 12
- Primary publisher/source: Yale/Cowles Foundation
- Use: foundational formulation of social welfare functions mapping profiles of
  individual orderings to a social ordering and the general possibility/impossibility
  result under a broad domain plus Pareto/unanimity, independence and non-dictatorship
  style conditions.

### HF17 inference

```text
ArrowImpossibility != AllCollectiveChoiceImpossible
ArrowTheorem != DemocracyImpossible
ArrowTheorem != DictatorshipNormativelyRequired
```

The theorem is always stored with input/output type and domain assumptions.

---

# 2. May — majority characterization

## Kenneth O. May (1952)

- Title: *A Set of Independent Necessary and Sufficient Conditions for Simple Majority Decision*
- Journal: Econometrica 20(4):680–684
- DOI: 10.2307/1907651
- Use: classic characterization of simple majority in a binary setting via anonymity,
  neutrality and positive responsiveness (with the exact original formalization).

### HF17 inference

```text
MayCharacterization != MajorityRuleOptimalForAllDomains
VotingAnonymity != EqualPoliticalStanding
VotingNeutrality != NormativeNeutrality
```

---

# 3. Gibbard — manipulation of voting schemes

## Allan Gibbard (1973)

- Title: *Manipulation of Voting Schemes: A General Result*
- Journal: Econometrica 41(4):587–601
- DOI: 10.2307/1914083
- Use: deterministic voting/manipulation theorem on unrestricted multi-alternative
  domains; demonstrates strategic-reporting impossibility for nontrivial schemes under
  the relevant assumptions.

### HF17 inference

```text
ManipulableRule != EveryElectionManipulated
GibbardSatterthwaite != VotingUseless
Ballot != RuleIndependentPreferenceMeasurement
```

---

# 4. Satterthwaite — strategy-proofness correspondence

## Mark Allen Satterthwaite (1975)

- Title: *Strategy-proofness and Arrow's conditions: Existence and correspondence
  theorems for voting procedures and social welfare functions*
- Journal: Journal of Economic Theory 10(2):187–217
- DOI: 10.1016/0022-0531(75)90050-2
- Use: proves every strategy-proof voting procedure in the stated unrestricted
  setting is dictatorial and links strategy-proofness conditions to Arrow-type social
  welfare conditions.

### HF17 inference

```text
StrategyProofness is domain/rule conditional
GibbardSatterthwaite != AllMechanismsManipulableInSameWay
```

---

# 5. Sen — Paretian liberal impossibility

## Amartya Sen (1970)

- Title: *The Impossibility of a Paretian Liberal*
- Journal: Journal of Political Economy 78(1):152–157
- DOI: 10.1086/259614
- Use: formal conflict, under the specified social-choice framework/domain, between a
  minimal liberal-rights condition and Pareto principle.

### HF17 inference

```text
MinimalLiberty + Pareto can Conflict
SenParetianLiberalImpossibility != LibertyImpossible
SenParetianLiberalImpossibility != ParetoWorthless
```

---

# 6. List & Pettit — judgment aggregation impossibility

## Christian List & Philip Pettit (2002)

- Title: *Aggregating Sets of Judgments: An Impossibility Result*
- Journal: Economics & Philosophy 18(1):89–110
- DOI: 10.1017/S0266267102001098
- Use: generalizes the doctrinal/discursive dilemma; under interconnected agendas and
  specified rationality/systematicity conditions, individually rational judgment sets
  cannot always be aggregated into collectively rational judgments.

### HF17 inference

```text
JudgmentProfile != PreferenceProfile
IndividualJudgmentConsistency != CollectiveJudgmentConsistency
JudgmentAggregationImpossibility != CollectiveReasoningImpossible
```

---

# 7. List & Goodin — generalized Condorcet jury theorem

## Christian List & Robert E. Goodin (2001)

- Title: *Epistemic Democracy: Generalizing the Condorcet Jury Theorem*
- Journal: Journal of Political Philosophy 9:277–306
- DOI: 10.1111/1467-9760.00128
- Use: primary generalization of Condorcet-style epistemic democracy, clarifying
  competence/independence and truth-tracking conditions.

### HF17 inference

```text
MajorityAccuracyResult != MajorityNormativeAuthority
PreferenceVote != EpistemicJuryVote
MoreVoters != MoreIndependentEvidence
```

---

# 8. Condorcet — classical jury theorem and paradox

## Marquis de Condorcet (1785)

- Work: *Essai sur l'application de l'analyse à la probabilité des décisions rendues
  à la pluralité des voix*
- Use: historical primary source for majority truth-tracking under competence-type
  assumptions and majority-cycle/paradox foundations.

### HF17 inference

```text
TruthTaskMajority != ValueConflictMajority
IndividualTransitivity need not imply collective transitivity
```

---

# 9. Raz — value incommensurability

## Joseph Raz (1986)

- Title: *Value Incommensurability: Some Preliminaries*
- Proceedings of the Aristotelian Society 86:117–134
- DOI: 10.1093/aristotelian/86.1.117
- Use: primary philosophical analysis of value incommensurability and comparison.

### HF17 inference

```text
Incommensurability must be typed
LackOfCommonMeasure need not be encoded as numerical equality
```

---

# 10. Raz — The Morality of Freedom, Incommensurability

## Joseph Raz (1988 online edition metadata)

- Book DOI: 10.1093/0198248075.001.0001
- Chapter DOI: 10.1093/0198248075.003.0013
- Use: detailed primary account where incommensurable options are not simply better,
  worse or equal under the specified comparison relation.

### HF17 inference

```text
Incomparability != Indifference
```

---

# 11. Chang — The Possibility of Parity

## Ruth Chang (2002)

- Journal: Ethics 112(4)
- DOI: 10.1086/339673
- Use: primary proposal of parity as a fourth comparison relation distinct from
  better, worse and equal.

### HF17 inference

```text
Parity != Equality
Parity != Incomparability
```

Parity is retained as a competing account rather than foundation truth.

---

# 12. Chang — Hard Choices

## Ruth Chang (2017)

- Journal: Journal of the American Philosophical Association 3(1):1–21
- DOI: 10.1017/apa.2017.7
- Use: primary argument that hard choices need not result from ignorance or strict
  incomparability and may instead involve parity.

### HF17 inference

```text
HardChoice != EpistemicUncertaintyByDefinition
```

---

# 13. Chang — parity/imprecise comparability in population ethics

## Ruth Chang (2016)

- Journal: Theoria 82:182–214
- DOI: 10.1111/theo.12096
- Use: contrasts parity with imprecise comparability and connects comparison structure
  to population-ethics cases.

### HF17 inference

```text
Incomplete/NonstandardComparison need not imply irrational choice
```

---

# 14. Lockhart — moral uncertainty

## Ted Lockhart (2000)

- Book: *Moral Uncertainty and its Consequences*
- DOI: 10.1093/oso/9780195126105.001.0001
- Use: early systematic primary treatment of how to act when uncertain about moral
  principles.

### HF17 inference

```text
MoralUncertainty is a distinct decision problem
```

---

# 15. Sepielli — equity among moral theories

## Andrew Sepielli (2013; first online 2012)

- Title: *Moral Uncertainty and the Principle of Equity among Moral Theories*
- Philosophy and Phenomenological Research 86:580–589
- DOI: 10.1111/j.1933-1592.2011.00554.x
- Use: primary alternative treatment of moral uncertainty and fairness among theories.

### HF17 inference

```text
MoralTheoryAggregation has competing rules
```

---

# 16. MacAskill, Bykvist & Ord — maximizing expected choiceworthiness

## *Moral Uncertainty* (2020), Chapter 2

- Book DOI: 10.1093/oso/9780198722274.001.0001
- Chapter DOI: 10.1093/oso/9780198722274.003.0003
- Use: argues for maximizing expected choiceworthiness when theories have the required
  interval-scale measurability and unit comparability.

### HF17 inference

```text
ExpectedChoiceworthiness != UniversalMoralUncertaintyRule
Scale assumptions are first-class
```

---

# 17. MacAskill, Bykvist & Ord — ordinal theories/social-choice analogy

## *Moral Uncertainty* (2020), Chapter 3

- DOI: 10.1093/oso/9780198722274.003.0004
- Use: applies social-choice analogy to ordinal theories and intertheoretic
  incomparability.

### HF17 inference

```text
MoralTheory != Voter
Analogy != PoliticalAuthorityTransfer
```

---

# 18. MacAskill, Bykvist & Ord — intertheoretic comparisons

## *Moral Uncertainty* (2020), Chapter 5

- DOI: 10.1093/oso/9780198722274.003.0006
- Use: primary analysis of unit comparability, structural/non-structural accounts and
  scale problems across moral theories.

### HF17 inference

```text
NumericalTheoryScore != IntertheoreticallyComparableScore
NormalizationRule != NeutralTechnicalStep
```

---

# 19. Estlund — epistemic dimension of democratic authority

## David Estlund (2003 anthology chapter)

- Chapter: *Beyond Fairness and Deliberation: The Epistemic Dimension of Democratic
  Authority*
- DOI: 10.1093/oso/9780195136593.003.0004
- Use: primary political-philosophy argument distinguishing epistemic quality from
  legitimate authority and resisting simple rule-by-the-expert inference.

### HF17 inference

```text
Expertise != Authority
BetterPoliticalKnowledge != LegitimateRuleAuthority
EpistemicQuality != Legitimacy
```

---

# 20. Fishkin et al. — America in One Room

## Fishkin, Siu, Diamond & Bradburn (2021)

- Title: *Is Deliberation an Antidote to Extreme Partisan Polarization? Reflections on
  “America in One Room”*
- American Political Science Review 115(4):1464–1481
- DOI: 10.1017/S0003055421000642
- Use: national field experiment with more than 500 US registered voters and a
  pre/post control; structured deliberation produced large depolarizing changes in
  policy attitudes and affective polarization.

### HF17 inference

```text
StructuredDeliberation can reduce polarization
OneDeliberationDesignWorks != DeliberationAlwaysWorks
```

---

# 21. Kramon — mechanism of deliberative depolarization

## Eric Kramon (2026)

- Title: *Why Do Deliberative Discussions Reduce Affective Polarization? Evidence from
  a Deliberation Experiment in Honduras*
- Perspectives on Politics, First View
- DOI: 10.1017/S1537592725104313
- Use: randomized perspective-taking design; out-partisan perspective defense produced
  more persistent depolarization while own-perspective deliberation modestly increased
  polarization.

### HF17 inference

```text
Deliberation != DepolarizationGuarantee
DeliberationEffect_D != DeliberationEffect_E
```

---

# 22. Fishkin — deliberative public consultation criteria

## James S. Fishkin (2021)

- PMID: 34905249
- DOI: 10.1002/hast.1316
- Use: primary methodological account of Deliberative Polling and design criteria for
  representative informed public consultation.

### HF17 inference

```text
Deliberation requires process design
RepresentativeSample != PoliticalRepresentative
```

---

# 23. Wu et al. — participatory decision-making field experiment

## Wu, Mai, Zhuang & Yi (2024)

- PMID: 39187711
- DOI: 10.1038/s41562-024-01964-y
- Use: large-scale randomized participatory-budgeting intervention reaching more than
  20 million people in China; treatment increased several civic-engagement behaviors
  outside budgeting months later.

### HF17 inference

```text
DecisionProcedure can change FutureParticipation
Procedure != PassivePreferenceMeasurement
```

---

# 24. Tessler et al. — AI common-ground mediation

## Tessler et al. (2024)

- PMID: 39418380
- DOI: 10.1126/science.adq2852
- Science 386(6719):eadq2852
- Use: 5,734 participants; AI mediator generated/refined group statements from
  individual opinions/critiques. Participants preferred AI statements over human
  mediator statements; views often converged; minority critiques were incorporated
  alongside majority positions; replicated in a representative virtual UK citizens'
  assembly.

### HF17 inference

```text
AI can facilitate common-ground formation
CommonGroundStatement != AuthorizedCollectiveDecision
AIMediator != CollectiveDecisionAuthority
```

---

# 25. Lin et al. — AI political persuasion in elections

## Lin et al. (2025)

- PMID: 41345316
- DOI: 10.1038/s41586-025-09771-9
- Nature 648:394–401
- Use: preregistered experiments in US 2024, Canada 2025 and Poland 2025 elections
  plus a ballot-measure context. Conversational AI advocacy significantly shifted
  candidate/policy preferences, with effects larger than typical video-ad effects in
  the study comparison; some claims were inaccurate.

### HF17 inference

```text
AIMediationCapability overlaps PersuasionCapability
PersuasionEffect != EpistemicImprovementByDefinition
```

---

# 26. Hackenburg et al. — levers of political persuasion

## Hackenburg et al. (2025)

- PMID: 41343633
- DOI: 10.1126/science.aea3884
- Science 390(6777):eaea3884
- Use: three large experiments, N=76,977, across 19 LLMs and 707 political issues;
  post-training/prompting strongly affected persuasion, and configurations increasing
  persuasion could reduce factual accuracy.

### HF17 inference

```text
MorePersuasiveAI != MoreTruthfulAI
Persuasion design is a governance variable
```

---

# 27. Argyle et al. — testing political persuasion theories with AI

## Argyle et al. (2025)

- PMID: 40314974
- PMCID: PMC12067286
- DOI: 10.1073/pnas.2412815122
- Use: original experiments using LLMs to test message customization/elaboration in
  political persuasion; customization/interaction were not clearly more persuasive
  than generic messages in this setting.

### HF17 inference

```text
Personalization != PersuasionGainByDefinition
```

---

# 28. Glickman & Sharot — Human-AI feedback loops

## Glickman & Sharot (2025; online 2024)

- PMID: 39695250
- PMCID: PMC11860214
- DOI: 10.1038/s41562-024-02077-2
- Use: experiments with N=1,401 found Human-AI interactions could amplify perceptual,
  emotional and social judgment biases more than Human-Human interaction and that
  participants were often unaware of the influence magnitude.

### HF17 inference

```text
PerceivedAutonomousJudgment != InfluenceFreeJudgment
AI mediation is not observationally neutral
```

---

# 29. Current AI-deliberation participation penalty — preprint

## Jungherr & Rauchfleisch (2025)

- arXiv:2503.07690
- Use: preregistered representative German survey experiment (N=1,850) found lower
  willingness to participate and lower quality ratings when deliberation tasks were
  described as AI-facilitated rather than human-facilitated, moderated by AI attitudes.

### HF17 inference

```text
AI facilitation can change participation itself
```

Evidence status: preprint; retained as current design evidence, not canonical causal
law.

---

# 30. Participatory process changes civic engagement — causal field evidence

## Wu et al. bridge

- Evidence pointer: source #23 (`PMID 39187711`, DOI
  `10.1038/s41562-024-01964-y`); not a duplicate counted source.
- Use: procedure-as-intervention bridge into reflexivity and HF18 endogenous
  participation.

---

# 31. Majority epistemics has conditional strengths

May's binary characterization and Condorcet/List-Goodin truth-tracking results jointly
support a positive lesson:

```text
MajorityRule has defensible properties under declared domains
```

while Arrow/Gibbard/Sen/List-Pettit show different failures outside or alongside those
conditions.

### HF17 methodological inference

```text
OneImpossibilityTheorem != UniversalProcedureRejection
OnePositiveTheorem != UniversalProcedureSelection
```

---

# 32. Social-choice impossibilities are non-equivalent

The source corpus exposes different objects:

```text
Arrow: preference profile -> social ordering
Gibbard/Satterthwaite: strategic report -> selected alternative
Sen: liberal protected choice + Pareto ordering
List/Pettit: logically connected judgment sets -> collective judgment set
```

### HF17 inference

Never cite one theorem as if it proved the others.

---

# 33. Deliberation evidence is bidirectional and design-sensitive

Fishkin et al. provide a strong structured-deliberation depolarization case; Kramon
2026 shows the effect depends on active out-partisan perspective engagement and that
own-perspective deliberation can modestly increase polarization.

### HF17 inference

```text
DeliberationEffect requires ProcessProfile
```

---

# 34. AI-deliberation evidence is also bidirectional

Tessler et al. shows AI can improve common-ground statement formation; Lin,
Hackenburg and Glickman/Sharot show AI can persuade, introduce factuality trade-offs
and amplify human biases.

### HF17 inference

```text
AI can be both FacilitationResource and Preference/JudgmentIntervention
```

Therefore role/authority/provenance must be explicit.

---

# 35. Source-level synthesis

The strongest surviving distinctions are:

```text
Preference != Welfare != MoralJudgment != NormativeReason
Vote != TruePreference by definition
ReportedPreference != LatentPreference by definition

EmpiricalDisagreement != NormativePluralism
NormativePluralism != AnythingGoes
Incommensurability != Incomparability by definition
Incomparability != Uncertainty
Indifference != Incomparability
Parity != Equality

TheoryCredence != VoterSupport
ExpectedChoiceworthiness != UniversalMoralUncertaintyRule
NumericalTheoryScore != IntertheoreticallyComparableScore
NormalizationRule != NeutralTechnicalStep

SocialOrdering != CollectiveDecision
OutcomeValueFunction != VotingRule
VotingRule != Legitimacy
MajorityPreference != NormativeTruth

MayCharacterization != UniversalMajorityRule
MajorityAccuracyResult != MajorityNormativeAuthority
ArrowTheorem != DemocracyImpossible
GibbardSatterthwaite != VotingUseless
SenParetianLiberalImpossibility != LibertyImpossible
JudgmentAggregationImpossibility != CollectiveReasoningImpossible

Agenda != NeutralContainer
Ballot != RuleIndependentPreferenceMeasurement
RightsProfile != AggregatePreference

Consensus != Truth
Consensus != Legitimacy
Consensus != FreeAgreementByDefinition
Deliberation != Persuasion
Deliberation != Bargaining
Deliberation != DepolarizationGuarantee
Participation != EffectiveInfluence

RepresentativeSample != PoliticalRepresentative
Expertise != Authority
EpistemicQuality != Legitimacy
LegitimateProcedure != CorrectOutcome
GoodOutcome != LegitimateProcedure

AIMediator != CollectiveDecisionAuthority
AISummary != NeutralRepresentationByDefinition
CommonGroundStatement != AuthorizedCollectiveDecision
AIPersuasion != Deliberation
MorePersuasiveAI != MoreTruthfulAI
InferredPreference != Consent

CrossTheoryRobustness != NormativeTruth
PopulationAggregation != PreferenceAggregation
CollectiveDecisionProcedure != PopulationAxiology

CollectiveChoiceRule != ImplementationMechanism
AuthorizedDecision != IncentiveCompatibleCompliance
PrivateType != ReportedType by definition
```

The repeated residual is strategic implementation: after a collective authorizes an
outcome, rules still shape reporting, participation, contribution, bargaining and
compliance. That is the HF18 mechanism-design boundary.
