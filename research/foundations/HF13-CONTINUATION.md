---
schema_version: 1
id: human.foundations.hf13.continuation
title: Human Foundations Continuation after HF13
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
summary: Exact continuation after HF13. HF13 reconstructs persistent social order by separating convention, social norm/expectation, reputation, status/prestige/dominance, power/authority/legitimacy, sanction/enforcement, law/rule, office/organization/institution and infrastructure. Its repeated unresolved boundary is normative evaluation itself: morality, harm, welfare, fairness, justice, rights, duties, responsibility and legitimacy.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.foundations.hf13
  - human.foundations.hf13.sources
---
# Human Foundations Continuation after HF13

## HF13 completed result

HF13 reconstructs persistent social order that can shape agents before a current
interaction begins and survive after current participants leave.

Minimum grammar:

```text
Repeated interaction / historical events
                ↓
     Behavioral regularities
        ↙              ↘
Coordination history   Evaluative history
      ↓                      ↓
 Convention              Reputation
      ↓                      ↓
Empirical expectations   partner-selection / trust inputs
      ↓                      ↓
        └───── Social expectations ─────┐
                                        ↓
                          Normative expectations
                                        ↓
                          Social norm structure
                         ↙        ↓        ↘
                    approval   conformity   sanction
                         \        ↓        /
                         compliance / violation
                                  ↓
                     feedback / reputation update
                                  ↺

Persistent roles/rules/resources
                ↓
            Office / Rule
          ↙        ↓        ↘
    Authority   Records   Enforcement
          \        ↓        /
             Institution
          ↙        ↓        ↘
   option sets   sanctions   infrastructure
          \        ↓        /
             de facto power
                  ↓
          current Human action
                  ↓
        future institutional state
                  ↺
```

The cross-cutting hierarchy remains:

```text
Expertise
  ↓ may generate
Prestige → Status → Influence

Threat/coercion
  ↓ may generate
Dominance → Status/Influence

Resource/option control
  ↓
Power

Recognized institutional decision scope
  ↓
Authority

Perceived entitlement to rule
  ↓
PerceivedLegitimacy

Moral/legal justification question
  ↓
[HF14 boundary]
NormativeLegitimacy
```

## Persistent order / convention

Retain:

```text
Persistence != Irreversibility
Persistent != Legitimate
Persistent != Universal
CurrentInteractionState != PersistentSocialOrder
BehavioralRegularity != Convention
BehavioralRegularity != SocialNorm
Frequency != Approval
ActualBehaviorFrequency != DescriptiveNormBelief
Convention != IndividualHabit
Convention != ExplicitAgreement
Convention != Law
Convention != SocialNorm
ConventionEmergence != PopulationWideSharedGoalRequirement
EstablishedConvention != IrreversibleConvention
MajorityBehavior != ConventionMechanism
CurrentEnvironmentSame != ConventionSame
ConventionPersistence != OriginalMemberPersistence
CulturalTransmission != LiteralCopyingOnly
```

Working relation:

```text
Convention_D(Population,Context)
= socially stabilized coordination regularity among multiple viable alternatives,
  materially supported by expectations about what others will use/do
```

Convention claims should preserve network/population, alternatives, coordination
relation, history, frequency/expectations, switching/tipping and transmission route.

## Empirical / normative expectations

Use:

```text
EmpiricalExpectation_D(A,P,C)
= A's belief/estimate about what members of P actually do/will do in C

NormativeExpectation_D(A,P,C)
= A's belief/estimate about what relevant others think should/ought to be done,
  approve/disapprove or may sanction in C

PersonalNormativeBelief_D(A,C)
= A's own normative judgment under a declared normative frame
```

Retain:

```text
EmpiricalExpectation != ActualFrequency
NormativeExpectation != PersonalNormativeBelief
NormativeExpectation != MoralJustification
EmpiricalExpectation != NormativeExpectation
DescriptiveNorm != InjunctiveNorm
Frequency→NormativeUpdate_D != Frequency→NormativeUpdate_E
```

Frequency information can causally alter normative beliefs without becoming
normative truth.

## Social norms

Working family:

```text
SocialNorm_D(P,C)
= socially maintained behavioral rule/expectation structure whose behavioral force
  depends materially on social expectations, approval/disapproval, conformity,
  reputation, sanction or internalized normative response
```

Retain:

```text
SocialNorm != CommonBehavior
SocialNorm != NormativeExpectationOnly
SocialNorm != SanctionMechanismOnly
NormCompliance != PreferenceExpression by definition
SocialNorm != MoralNorm
SocialNorm != Law
NormStrength != OneScalar by default
ObservedCompliance != NormInternalization
Internalized != Justified
ComplianceWhenWatched != InternalizedNorm
NormViolation != NormIgnorance
CurrentPayoffStructure != CurrentNormStrength
HistoricalAdaptiveness != CurrentValue
NormCompliance != WelfareImprovement
NormEnforcement != NormativeGood
IsCommon(X) != Ought(X)
```

NormProfile_D should preserve population/reference group, actual behavior,
empirical/normative expectations, personal normative beliefs, approval,
sanction expectation/enforcement, compliance motive, internalization evidence,
dissent, history and welfare/externalities.

## Rule / law

Retain:

```text
Rule != SocialNorm
WrittenRule != ActualPractice
Rule != Law
RuleExists != RuleFollowed
RecognizeRule != EndorseRule
Policy != Norm
Policy != Law
LegalValidity != MoralRightness
LawInForce != UniversalCompliance
LegalCompliance != LegitimacyResponseOnly
```

A law can be represented as legally valid within system S while simultaneously
judged morally wrong under standard M.

Use LawProfile_D with jurisdiction/system, issuing authority, text/scope/effective
date, formal-validity evidence, enforcement, actual practice, perceived legitimacy,
compliance, moral evaluation and appeal/review path.

## Reputation

Working relation:

```text
Reputation_D(B | Population P, Domain D, Time t)
= socially distributed evaluative information/expectation about B derived from past
  behavior, claims, records or third-party communication and capable of shaping
  future interaction policy
```

Retain:

```text
ReputationInformation != DirectInteractionHistory
DirectEvidence != ReputationEvidence
Reputation != VerifiedTrait
ConsensusReputation != GroundTruth
Reputation != Trust
Reputation != Status
Reputation_D != Reputation_E
Credential != Reputation
Credential != CurrentCompetence
Stereotype != IndividualReputation
```

Provenance is mandatory: direct observation, gossip, rating, credential, public
record, media report or algorithmic score are different evidence channels.

## Status / prestige / dominance / influence

Working relations:

```text
Status_D(A,P,C)
= socially conferred rank/esteem/respect position

Prestige_D
= status/influence substantially supported by voluntarily conferred deference,
  admiration or attention, often linked to valued skill/knowledge/contribution

Dominance_D
= status/influence substantially supported by threat, intimidation, coercive
  capability or imposed cost

Influence_D(A→B)
= realized/probabilistic change in B's belief/decision/action attributable to A
```

Retain:

```text
Status != Power
Status != Authority
Status != TaskCompetence
Status_D != Status_E
Expertise != Prestige
Prestige != Status
Dominance != Power
Dominance != Authority
HighRank != PrestigeOnly
HighRank != DominanceOnly
Influence != Power
Influence != Authority
```

Prestige and dominance can coexist and both can produce rank, but via different
relations and deference modes.

## Power

Working relation:

```text
Power_D(A→B,C)
= A's effective capability, under context C and available alternatives, to alter
  B's option set, access to valued resources, incentives, actions or outcomes
```

Retain:

```text
Power_D(A→B) != Power_D(A→C)
Power_D != Power_E
PositionalPower != SubjectivePower
SenseOfPower != EffectivePower
PerceivedControl != ActualControl
Power != Legitimacy
Power != Authority
Power != Status
CanForce(X) != MayRightfullyRequire(X)
```

Power claims should preserve controlled resource/options, target dependence,
alternatives/exit, enforcement capability, information asymmetry, formal position,
subjective power, realized influence and resistance capability.

## Authority

Working relation:

```text
Authority_D(A,S,C)
= socially/institutionally recognized decision/directive/permission scope assigned
  to actor/office A within system S and domain C
```

Retain:

```text
Authority != Expertise
ExpertInfluence != FormalAuthority
Authority != CoercivePower
DeJureAuthority != DeFactoPower
OfficeAuthority != OccupantPersonalTrait
Authority_D != Authority_E
```

`EpistemicAuthority_D` should remain explicitly distinguished from institutional
command/decision authority.

## Legitimacy

Separate:

```text
PerceivedLegitimacy
Institutional/LegalValidity
NormativeLegitimacy
```

Retain:

```text
PerceivedLegitimacy != FormalAuthority
PerceivedLegitimacy != NormativeLegitimacy
LegalValidity != NormativeLegitimacy
MoreCoerciveDisplay != MoreLegitimacy
Compliance != PerceivedLegitimacy
NonCompliance != IllegitimacyProof
```

Procedural/source features can causally change perceived legitimacy and compliance,
but acceptance remains descriptive evidence, not normative justification.

## Sanction / enforcement

Working family:

```text
Sanction_D
= socially/institutionally contingent consequence imposed or withheld in response to
  behavior relative to a rule/norm/decision
```

Retain:

```text
Punishment != SanctionTotality
Enforcement != PunishmentOnly
ReputationChange != FormalPunishment
Sanction != SocialNorm
CanPunish != LegitimatelyMayPunish
Sanction != CommunicationRepair
EnforcementSuccess != WelfareImprovement
MoreSanction != MoreIntrinsicCooperation
SanctionRemovalEffect_D != SanctionRemovalEffect_E
InstitutionChoice != NormativeLegitimacy
```

Record peer/third-party/centralized/automated sanction separately, including
trigger, severity/probability, procedural basis, appeal/override, compliance effect,
internalization effect, reputation effect, welfare/externality and legitimacy.

## Office / organization / institution / infrastructure

Working relations:

```text
Office_D
= persistent defined position carrying role/permissions/authority/duties and
  succession conditions independent of current occupant

Organization_D
= bounded coordinated multi-agent system with membership/role boundary,
  persistence mechanism and joint activity/resources

Institution_D
= persistent socially reproduced structure of rules, roles/offices, permissions,
  expectations, records, resources and enforcement/coordination mechanisms shaping
  recurring interactions beyond one current episode
```

Retain:

```text
Office != Occupant
Office != Person
Office != Organization
Organization != Institution
Organization != HumanIndividual
Institution != Building
Institution != Organization
Institution != RepeatedDyad
Institution != SanctionSystemOnly
InstitutionalMemory != Sum(CurrentMemberMemory)
DeJureInstitution != DeFactoInstitutionalPractice
CurrentInstitutionalRule != WholeInstitutionalState
InstitutionEffect != IncentiveEffectOnly
InstitutionExists != InstitutionLegitimate
InstitutionStable != WelfareImproving
Infrastructure != Institution
```

Institutions can externalize memory, permissions, authority and enforcement and can
survive member turnover.

## Human×AI institutional order

Retain:

```text
ParsablePolicy != ValidAuthority
ValidAuthority != MoralLegitimacy
AutomationOfRule != ValidationOfRule
HumanApproval != NormativeLegitimacy
AIEpistemicContribution != AIDecisionAuthority
AuthorityLabel != EffectiveAuthority
MachineExecution != MoralAuthorization
InstitutionalFidelity != NormativeCorrectness
```

Automation can change de facto power, speed, scale and observability while de jure
authority stays constant. Appeal, override, audit and reversibility are therefore
institutional architecture, not UX details.

## HF13 research objects

### ConventionProfile_D

```text
{
  population/context,
  viable alternatives,
  coordination relation,
  observed/perceived frequency,
  network topology,
  history/seed,
  convergence/scope,
  switching cost,
  tipping evidence,
  transmission route,
  persistence/decay
}
```

### NormProfile_D

```text
{
  population/reference group,
  behavior/rule,
  actual frequency,
  empirical expectations,
  normative expectations,
  personal normative beliefs,
  approval/appropriateness,
  sanction expectation/enforcement,
  compliance motive,
  internalization evidence,
  dissent/violation,
  history,
  welfare/externalities,
  normative-status uncertainty
}
```

### ReputationProfile_D

```text
{
  target/domain/audience,
  provenance,
  direct-history relation,
  content/evaluation,
  confidence/source incentives,
  cross-checking,
  update trajectory,
  persistence/decay,
  effect on trust/selection/sanction
}
```

### PowerProfile_D

```text
{
  holder/target/domain,
  resource/options controlled,
  dependence/alternatives/exit,
  enforcement capability,
  information asymmetry,
  formal position,
  perceived power,
  realized influence,
  resistance capability,
  authority/legitimacy relation
}
```

### AuthorityProfile_D

```text
{
  office/actor,
  institutional source,
  domain/scope,
  decision/directive rights,
  delegation rights,
  enforcement,
  appeal/review,
  de facto power,
  perceived legitimacy,
  normative-legitimacy question,
  contest/uncertainty
}
```

### InstitutionProfile_D

```text
{
  identity/scope,
  member boundary,
  offices/roles,
  formal rules,
  informal norms,
  authority source,
  resources/records,
  permissions/options,
  enforcement/sanctions,
  appeal/exit,
  de jure state,
  de facto practice,
  history/path dependence,
  turnover continuity,
  perceived legitimacy,
  welfare/externalities,
  normative-legitimacy question
}
```

## High-information falsifiers to preserve

- decentralized convention emergence without central planner/agreement;
- established convention tipping after committed-minority critical mass;
- transmitted microculture surviving participant replacement;
- empirical and normative expectations manipulated/measured separately;
- frequency information altering normative judgment without becoming identical to it;
- punishment stabilizing welfare-reducing norm-compliant behavior;
- unfair/selfish sanctions crowding out altruistic cooperation;
- temporary sanction/institution effects persisting after removal;
- direct experience and third-party reputation providing conflicting evidence;
- gossip/ostracism altering partner choice before direct interaction;
- prestige and dominance both producing rank through different deference routes;
- high status failing to predict competence on an unrelated task;
- status and power manipulations producing different downstream effects;
- positional and subjective power dissociating;
- power increasing illusory control;
- legitimate versus coercive authority structures producing different trust/
  cooperation responses;
- fairer enforcement changing compliance independently of pure material incentives;
- moral conviction constraining acceptance of authoritative/legal decisions;
- children distinguishing legal validity/regulation from moral rightness;
- formal authority surviving occupant change;
- institution/rule visibility changing newcomer behavior;
- AI recommendation versus AI decision role changing fairness/legitimacy judgments;
- symbolic AI authority labels failing to guarantee compliance;
- Human-in-loop judgment being shifted by early algorithmic advice;
- machine delegation increasing unethical execution without creating moral
  authorization;
- unsafe machine compliance to authority cues despite lack of valid authority.

## Exact next foundation

HF13 repeatedly reaches questions that cannot be settled by more descriptive social
measurement:

```text
Is this norm justified?
Is this punishment fair?
Does this authority have a right to command?
Does efficiency justify coercion?
When may a law be disobeyed?
What rights constrain institutions?
How should harms and benefits be distributed?
Who is responsible for institutional outcomes?
```

The decisive firewall is:

```text
What society does
!= What society expects
!= What society approves
!= What society enforces
!= What law recognizes
!= What power can compel
!= What ought to be done
```

Therefore the exact next round is:

# HF14 — Morality, Harm, Welfare, Fairness, Justice, Rights, Duties, Responsibility and Legitimacy

## HF14 starting questions

1. What is moral judgment relative to social norm, emotion, preference and law?
2. What is harm relative to pain, damage, risk, rights violation and preference
   frustration?
3. What is welfare relative to utility, preference satisfaction, capability,
   flourishing and experienced well-being?
4. What is fairness relative to equality, equity, need, desert and procedure?
5. What is justice relative to fairness, rights, law and institutional legitimacy?
6. What is a right relative to permission, claim, power, immunity and capability?
7. What is duty/obligation relative to expectation, commitment, contract and law?
8. What is responsibility relative to causation, agency, knowledge, control,
   authority, role and foreseeability?
9. What is accountability relative to responsibility, answerability and sanction?
10. What is normative legitimacy relative to perceived legitimacy, legality,
    democratic support, procedure and outcome?
11. How should conflicts among welfare, autonomy, fairness, rights and collective
    outcomes be represented without hiding the normative criterion?
12. How should Human×AI systems distinguish observed norms, encoded rules, legal
    authority and moral constraints?
13. When can an Agent appropriately refuse a formally authorized instruction because
    of higher-order safety/rights constraints?
14. What next boundary emerges after normative evaluation is rebuilt?

## Candidate HF14 falsifiers

- highly prevalent behavior judged morally wrong;
- legally valid law judged unjust or not morally binding;
- authoritative decision accepted procedurally but rejected on moral grounds;
- welfare-improving policy judged unfair because burdens/benefits differ;
- equal outcomes judged unfair when needs/contributions differ;
- unequal outcomes judged fair under some desert/need principles;
- accidental versus intentional harm with equal physical outcome;
- causal contribution without responsibility and responsibility without direct
  physical execution;
- coercion/ignorance/control changes in responsibility attribution;
- rights constraints overriding aggregate welfare gains;
- procedural fairness changing legitimacy despite equal outcome;
- legitimate procedure producing harmful outcome and beneficial outcome produced by
  illegitimate procedure;
- Human principal authorizing, AI executing and institution allocating
  responsibility differently;
- AI faithfully applying a formally valid rule that violates higher-order safety or
  rights constraints.

## Do not precommit

HF13 does not establish that:

- morality is social conformity;
- moral truth is majority belief;
- welfare equals preference satisfaction;
- fairness means equality;
- justice means welfare maximization;
- rights are absolute in every conflict;
- legal rights exhaust moral rights;
- responsibility is causal contribution;
- intent is necessary for all responsibility;
- authority creates moral duty by itself;
- democratic selection guarantees legitimacy;
- procedural fairness guarantees just outcomes;
- beneficial outcomes justify illegitimate means;
- normative legitimacy can be inferred from model training data, popularity or
  observed Human behavior;
- AI should maximize any one moral metric by foundation fiat.

## Stop rule

Do not schedule HF15 now. HF14 must expose a repeated neighboring distinction whose
absence creates category failures across materially different normative cases.
