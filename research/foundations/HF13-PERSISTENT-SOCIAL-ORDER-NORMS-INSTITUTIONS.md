---
schema_version: 1
id: human.foundations.hf13
title: HF13 — Social Norms, Conventions, Reputation, Status, Authority, Power, Sanctions and Institutions
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
summary: HF13 reconstructs persistent social order that can precede and outlive a current interaction. It separates behavioral regularity, convention, descriptive/empirical expectation, normative expectation, appropriateness judgment, social norm, personal normative belief, moral judgment, rule and law; direct history, gossip, reputation, credential and stereotype; status, prestige, dominance, expertise, influence, power, authority and legitimacy; sanction, punishment, reward, exclusion and enforcement; office, occupant, organization and institution; and de jure versus de facto control. It shows that prevalence, persistence, compliance, authority and institutional enforcement are descriptive social facts rather than proof of moral legitimacy. The repeated unresolved boundary is normative evaluation itself: harm, welfare, fairness, justice, rights, duties, responsibility and legitimacy.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
  - HF13
related:
  - human.foundations.hf12
  - human.foundations.hf13.sources
  - human.foundations.hf13.continuation
---
# HF13 — Social Norms, Conventions, Reputation, Status, Authority, Power, Sanctions and Institutions

## 0. Status and question

HF12 could explain current multi-agent interaction:

```text
partner models
shared goals
communication
roles
trust
joint action
```

but repeatedly encountered structures that were already present before a current
dyad met and that could remain after its members disappeared:

```text
language conventions
professional roles
reputation
social norms
status hierarchies
legal permissions
sanction systems
institutional authority
```

HF13 therefore asks:

> **What is persistent social order, and which distinct social objects are hidden by
> words such as norm, status, authority, power, rule and institution?**

The central constraint is normative discipline:

```text
What is common
!=
What is expected
!=
What is approved
!=
What is enforced
!=
What is legally valid
!=
What is morally justified
```

---

# 1. Persistent social order

Working family:

```text
PersistentSocialOrder
= socially maintained state/structure that can shape later agents' expectations,
  options, roles, permissions, incentives or evaluations beyond one current
  interaction episode
```

Examples include:

```text
conventions
norms
reputations
status relations
offices
rules
laws
sanction systems
institutions
```

---

# 2. Persistence is not permanence

A convention or institution can last for years and still tip rapidly.

Thus:

```text
Persistence != Irreversibility
```

---

# 3. Persistence is not legitimacy

A harmful arrangement may persist.

Therefore:

```text
Persistent != Legitimate
```

---

# 4. Persistence is not universal adoption

Persistent social structures can be:

```text
local
class-specific
profession-specific
network-specific
contested
```

Thus:

```text
Persistent != Universal
```

---

# 5. Social order can be distributed

No individual need carry the whole rule system.

Persistent order may be distributed across:

```text
human memory
records
software
rituals
signage
credentials
contracts
organizational roles
physical infrastructure
```

---

# 6. Current interaction state is insufficient

A stranger can enter an airport and know how to queue, enter a court and encounter
pre-existing authority, or enter a software system and be blocked by permissions.

Thus:

```text
CurrentInteractionState != PersistentSocialOrder
```

---

# 7. Regularity

Working definition:

```text
BehavioralRegularity_D
= repeated/statistically patterned behavior in a declared population/context/domain
```

---

# 8. Regularity is not convention

A repeated behavior can arise from identical physical constraints or independent
preferences.

Thus:

```text
BehavioralRegularity != Convention
```

---

# 9. Regularity is not social norm

A frequent behavior may be disliked or regarded as wrong.

Thus:

```text
BehavioralRegularity != SocialNorm
```

---

# 10. Frequency is not approval

Use separate variables:

```text
BehaviorFrequency
PerceivedBehaviorFrequency
Approval
PerceivedApproval
```

Therefore:

```text
Frequency != Approval
```

---

# 11. Actual frequency and perceived frequency differ

Humans can misestimate what others do.

Thus:

```text
ActualBehaviorFrequency != DescriptiveNormBelief
```

---

# 12. Convention

HF13 working relation:

```text
Convention_D(Population,Context)
= a socially stabilized coordination regularity among multiple viable alternatives,
  where participants' choice is materially supported by expectations about what
  others will use/do in that context
```

The definition does not require explicit agreement.

---

# 13. Convention is not habit

A habit can be individually learned and useful without depending on another person's
matching choice.

Thus:

```text
Convention != IndividualHabit
```

---

# 14. Convention is not explicit agreement

Large decentralized experiments produce common naming conventions without central
planning or population-wide negotiation.

Thus:

```text
Convention != ExplicitAgreement
```

---

# 15. Convention is not law

Driving on one side of the road can be both convention and law, but the two roles are
distinct.

Thus:

```text
Convention != Law
```

---

# 16. Convention is not social norm by definition

Many conventions coordinate among alternatives without strong appropriateness or
sanction expectations.

Thus:

```text
Convention != SocialNorm
```

---

# 17. Convention can be arbitrary relative to physical outcome

Different labels can coordinate equally well.

Therefore:

```text
ConventionContent need not be PhysicallyNecessary
```

---

# 18. Network topology matters

Large-group naming experiments show local versus globally mixing networks can produce
very different convergence patterns.

Therefore:

```text
ConventionEmergence
= f(local interaction, network topology, initial history, adaptation)
```

not merely individual preference.

---

# 19. Convention can emerge without shared global intent

Participants need not intend to create a population-wide convention.

Thus:

```text
ConventionEmergence != PopulationWideSharedGoalRequirement
```

---

# 20. Convention can tip

Committed minorities can overturn an established convention after a critical-mass
boundary under some experimental conditions.

Thus:

```text
EstablishedConvention != IrreversibleConvention
```

---

# 21. Majority is not causal explanation

Saying `the majority does X` does not explain why the majority emerged or remains.

Therefore:

```text
MajorityBehavior != ConventionMechanism
```

---

# 22. Convention path dependence

Different early histories can stabilize different conventions under similar later
conditions.

Thus:

```text
CurrentEnvironmentSame != ConventionSame
```

---

# 23. Intergenerational transmission

Transmission-chain and microculture experiments show behavior patterns can persist
across participant generations even when original members leave.

Thus:

```text
ConventionPersistence != OriginalMemberPersistence
```

---

# 24. Transmission is reconstructive

New generations can modify inherited practice while preserving recognizable
continuity.

Therefore:

```text
CulturalTransmission != LiteralCopyingOnly
```

---

# 25. ConventionProfile_D

Use:

```text
{
  population/context,
  viable alternatives,
  coordination payoff relation,
  observed frequency,
  perceived frequency,
  network structure,
  history/seed,
  convergence,
  local/global scope,
  switching cost,
  tipping evidence,
  transmission route,
  persistence/decay
}
```

---

# 26. Descriptive norm terminology is overloaded

Some literatures use `descriptive norm` to mean:

```text
belief about what most others do
```

HF13 therefore prefers:

```text
EmpiricalExpectation_D
```

when the expectation itself is the object.

---

# 27. Empirical expectation

Working definition:

```text
EmpiricalExpectation_D(A,P,C)
= A's belief/estimate about what members of population/reference group P actually
  do or will do in context C
```

---

# 28. Empirical expectation is not actual behavior

Thus:

```text
EmpiricalExpectation != ActualFrequency
```

---

# 29. Normative expectation

Working definition:

```text
NormativeExpectation_D(A,P,C)
= A's belief/estimate about what relevant others in P think one should/ought to do,
  approve/disapprove, or may sanction in context C
```

The exact operationalization must be declared.

---

# 30. Normative expectation is not personal normative belief

A can believe:

```text
others think I should do X
```

while personally thinking X is wrong.

Thus:

```text
NormativeExpectation != PersonalNormativeBelief
```

---

# 31. Personal normative belief

Working family:

```text
PersonalNormativeBelief_D(A,C)
= A's own judgment that an action is required/permitted/forbidden/appropriate under
  a declared normative frame
```

This still does not prove moral truth.

---

# 32. Normative expectation is not moral truth

Thus:

```text
NormativeExpectation != MoralJustification
```

---

# 33. Empirical and normative expectations are distinct

Long-duration cooperation experiments measure and manipulate both independently.

Thus:

```text
EmpiricalExpectation != NormativeExpectation
```

---

# 34. They can interact

A rule may have stronger behavioral pull when agents believe both:

```text
others comply
and
others think compliance is expected/appropriate
```

without requiring both effects to be equal.

---

# 35. Frequency can update appropriateness belief

Recent experiments show descriptive frequency information can shift injunctive and
moral judgments, especially in conventional/fairness domains.

But influence is not identity.

Thus:

```text
DescriptiveInformation can update NormativeBelief
```

while:

```text
DescriptiveNorm != InjunctiveNorm
```

---

# 36. Frequency effect is domain-sensitive

Harm judgments can be less frequency-sensitive than conventional judgments.

Therefore:

```text
Frequency→NormativeUpdate_D != Frequency→NormativeUpdate_E
```

---

# 37. Social norm

HF13 working family:

```text
SocialNorm_D(P,C)
= socially maintained behavioral rule/expectation structure in population P and
  context C whose behavioral force depends materially on social expectations,
  approval/disapproval, conformity, reputation, sanction or internalized normative
  response
```

No one mechanism is required in every case.

---

# 38. Social norm is not behavior frequency

```text
SocialNorm != CommonBehavior
```

---

# 39. Social norm is not normative expectation alone

An isolated belief about others' approval need not constitute a stabilized norm.

Thus:

```text
SocialNorm != NormativeExpectationOnly
```

---

# 40. Social norm is not sanction only

Some norm compliance persists without active surveillance or material sanction.

Thus:

```text
SocialNorm != SanctionMechanismOnly
```

---

# 41. Social norm is not personal preference

```text
NormCompliance != PreferenceExpression by definition
```

---

# 42. Social norm is not morality

A norm can be regarded as immoral.

Thus:

```text
SocialNorm != MoralNorm
```

unless explicitly qualified.

---

# 43. Social norm is not legal rule

```text
SocialNorm != Law
```

although law can interact with social norms.

---

# 44. Norm strength is multidimensional

At least separate:

```text
prevalence
expectation convergence
approval strength
sanction likelihood
sanction severity
internalization
persistence
network reach
contestability
```

Thus:

```text
NormStrength != OneScalar by default
```

---

# 45. Norm compliance has plural causal routes

A Human may comply because of:

```text
personal agreement
empirical expectation
normative expectation
reputation concern
fear of punishment
habit
identity
coordination value
legal sanction
lack of alternatives
```

---

# 46. Same compliance does not identify motive

Therefore:

```text
ObservedCompliance != NormInternalization
```

---

# 47. Internalization

Working family:

```text
InternalizedNormResponse_D
= norm-consistent valuation/affect/decision tendency that can continue when immediate
  external observation/sanction is absent
```

---

# 48. Internalization is not moral correctness

```text
Internalized != Justified
```

---

# 49. Compliance under monitoring is not internalization

Thus:

```text
ComplianceWhenWatched != InternalizedNorm
```

---

# 50. Noncompliance is not absence of norm recognition

Agents can knowingly violate a norm.

Thus:

```text
NormViolation != NormIgnorance
```

---

# 51. Norm disagreement can coexist with norm knowledge

```text
KnowNorm(X)
+
DisapproveNorm(X)
```

is coherent.

---

# 52. Norm persistence can outlast payoff change

Long-term collective-risk experiments show stronger norms can resist erosion after
risk changes.

Thus:

```text
CurrentPayoffStructure != CurrentNormStrength
```

---

# 53. Norm persistence can be maladaptive

A once-useful rule may become costly after environment change.

Thus:

```text
HistoricalAdaptiveness != CurrentValue
```

---

# 54. Harmful norms are decisive falsifiers

Peer punishment can increase compliance with a welfare-reducing contribution rule.

Therefore:

```text
NormCompliance != WelfareImprovement
```

and:

```text
NormEnforcement != NormativeGood
```

---

# 55. Norm prevalence cannot settle ought

The foundational firewall is:

```text
IsCommon(X)
!=
Ought(X)
```

---

# 56. NormProfile_D

```text
{
  population/reference group,
  behavior/rule,
  context,
  actual frequency,
  empirical expectations,
  normative expectations,
  personal normative beliefs,
  appropriateness judgments,
  sanction expectations,
  actual enforcement,
  compliance motives,
  internalization evidence,
  dissent/violation,
  persistence/history,
  welfare/externality evidence,
  normative-status uncertainty
}
```

---

# 57. Rule

HF13 uses a broad descriptive working definition:

```text
Rule_D
= represented or externally encoded conditional constraint/prescription connecting
  specified conditions to required/permitted/forbidden actions or outcomes
```

---

# 58. Rule is not norm

A rule can exist on paper and be ignored.

Thus:

```text
Rule != SocialNorm
```

---

# 59. Rule is not practice

```text
WrittenRule != ActualPractice
```

---

# 60. Rule is not law

Organizations, games and software have rules that are not law.

Thus:

```text
Rule != Law
```

---

# 61. Rule validity and rule compliance differ

```text
RuleExists != RuleFollowed
```

---

# 62. Rule recognition and rule agreement differ

```text
RecognizeRule != EndorseRule
```

---

# 63. Policy

A policy may describe how an organization/agent chooses actions under states.

Thus:

```text
Policy != Norm
Policy != Law
```

although policies can implement either.

---

# 64. Protocol

A protocol coordinates interaction/technical procedure.

It can function conventionally or normatively but does not become a social norm by
name.

---

# 65. Law

HF13 does not freeze one jurisprudential definition across jurisdictions.

Minimal descriptive working family:

```text
LegalRule_D
= rule recognized within a declared legal/institutional system as carrying legal
  status, permissions/prohibitions or consequences under that system
```

---

# 66. Law is not morality

Children and adults can judge an enacted law to be unjust.

Therefore:

```text
LegalValidity != MoralRightness
```

---

# 67. Law is not compliance

```text
LawInForce != UniversalCompliance
```

---

# 68. Compliance with law has plural motives

Evidence supports roles for:

```text
moral agreement
perceived legitimacy
autonomous motivation
sanction severity
apprehension risk
habit
coordination
```

with domain differences.

---

# 69. Moral agreement can outweigh perceived authority legitimacy

Law-compliance studies show personal morality can predict compliance more strongly
than authority legitimacy in some domains.

Thus:

```text
LegalCompliance != LegitimacyResponseOnly
```

---

# 70. Unjust law is a boundary object

An agent can simultaneously represent:

```text
This is legally valid under system S
This is morally wrong under standard M
```

without contradiction.

---

# 71. LawProfile_D

```text
{
  jurisdiction/system,
  issuing authority,
  rule text/content,
  effective date/scope,
  formal validity evidence,
  enforcement mechanism,
  actual practice,
  perceived legitimacy,
  compliance,
  moral evaluation,
  appeal/review path,
  uncertainty
}
```

---

# 72. Reputation

HF13 working relation:

```text
Reputation_D(B | Population P, Domain D, Time t)
= socially distributed evaluative information/expectation about B derived from past
  behavior, claims, records or third-party communication and capable of shaping
  others' future interaction policies
```

---

# 73. Reputation is not direct history

```text
ReputationInformation != DirectInteractionHistory
```

---

# 74. Direct and indirect information can conflict

Human helping experiments show direct personal experience often weighs differently
from reputation.

Thus:

```text
DirectEvidence != ReputationEvidence
```

---

# 75. Reputation is not truth

Gossip can be inaccurate or strategically manipulated.

Thus:

```text
Reputation != VerifiedTrait
```

---

# 76. Multiple gossip reports can improve robustness without guaranteeing truth

```text
MoreIndependentReports
can improve inference
```

but:

```text
ConsensusReputation != GroundTruth
```

---

# 77. Reputation is not trust

Reputation is socially available information/state about B.

Trust remains A→B relation under task/stakes.

Thus:

```text
Reputation != Trust
```

---

# 78. Reputation can influence trust

But influence does not collapse the constructs.

---

# 79. Reputation is not status

A person can have a reputation for dishonesty and still occupy high status or power.

Thus:

```text
Reputation != Status
```

---

# 80. Reputation is domain-specific

```text
Reputation_D != Reputation_E
```

A good surgeon can have a bad reputation as a manager.

---

# 81. Reputation has provenance

Record:

```text
direct observation
gossip
rating
credential
public record
media report
algorithmic score
```

because these channels have different reliability and incentives.

---

# 82. Credential is not reputation

A credential is an institutionally issued signal/record about qualification/status.

Thus:

```text
Credential != Reputation
```

---

# 83. Credential is not competence

A credential can be stale, fraudulent or weakly predictive.

Thus:

```text
Credential != CurrentCompetence
```

---

# 84. Stereotype is not reputation

A stereotype may assign expectations from category membership without person-specific
history.

Thus:

```text
Stereotype != IndividualReputation
```

---

# 85. Reputation can change behavior before first interaction

This makes it a persistent-social-order object rather than current-dyad memory.

---

# 86. Reputation can alter partner selection

Gossip and ostracism experiments show reputational information can change who is
chosen for interaction.

Thus:

```text
Reputation can modify OptionSet
```

---

# 87. Reputation can create incentives for current action

If current behavior will be observed and transmitted, future partner choice changes
current payoff structure.

Thus:

```text
FutureReputation
can be CurrentDecisionInput
```

---

# 88. ReputationProfile_D

```text
{
  target,
  domain,
  audience/network,
  source/provenance,
  direct-history relation,
  content/evaluation,
  confidence,
  source incentives,
  cross-checking,
  update history,
  persistence/decay,
  effect on trust,
  partner selection,
  sanctions/rewards
}
```

---

# 89. Hierarchy terminology requires separation

HF13 retains at least:

```text
Status
Prestige
Dominance
Influence
Power
Authority
Expertise
Leadership
```

---

# 90. Status

Working relation:

```text
Status_D(A,P,C)
= socially conferred rank/esteem/respect position of A within population P and
  context/domain C
```

---

# 91. Status is not power

Experimental work shows status and power have different downstream effects.

Thus:

```text
Status != Power
```

---

# 92. Status is not authority

A celebrity can have high status but no formal decision right over a court.

Thus:

```text
Status != Authority
```

---

# 93. Status is not competence

High-status participants in a familiar group need not be best on an unrelated quiz.

Thus:

```text
Status != TaskCompetence
```

---

# 94. Status is relational/domain-specific

```text
Status_D != Status_E
```

---

# 95. Prestige

Working family:

```text
Prestige_D
= status/influence supported substantially by voluntarily conferred deference,
  admiration or attention often linked to valued skill/knowledge/contribution
```

---

# 96. Prestige is not expertise

An expert can be unknown or disrespected.

Thus:

```text
Expertise != Prestige
```

---

# 97. Prestige is not status totality

```text
Prestige != Status
```

It is one route/basis of status in relevant models.

---

# 98. Prestige deference can be domain-specific

Someone prestigious in music need not receive deference in surgery.

---

# 99. Dominance

Working family:

```text
Dominance_D
= status/influence supported substantially by threat, intimidation, coercive
  capacity or imposed cost rather than freely conferred deference
```

---

# 100. Dominance is not power totality

Dominance can generate power, but resource/organizational control can exist without
interpersonal intimidation.

Thus:

```text
Dominance != Power
```

---

# 101. Dominance is not authority

```text
Dominance != Authority
```

A bully can dominate without recognized decision rights.

---

# 102. Prestige and dominance can both produce rank

Longitudinal and group experiments show both routes can predict influence/rank under
some contexts.

Therefore:

```text
HighRank != PrestigeOnly
HighRank != DominanceOnly
```

---

# 103. Prestige and dominance are not perfectly exclusive

Individuals/positions can display both.

Thus:

```text
Prestige_D and Dominance_D can coexist
```

---

# 104. Prestige is more closely tied to freely granted deference in relevant studies

Thus:

```text
DeferenceMode matters
```

for hierarchy claims.

---

# 105. Rule-breaking can change dominance/prestige impressions differently

This shows social norm relation and status route are coupled but not identical.

---

# 106. Influence

Working relation:

```text
Influence_D(A→B)
= realized or probabilistic change in B's belief/decision/action attributable to A
  in domain D
```

---

# 107. Influence is not power

A low-power expert can strongly influence a decision.

Thus:

```text
Influence != Power
```

---

# 108. Influence is not authority

Persuasion can work without decision rights.

Thus:

```text
Influence != Authority
```

---

# 109. Power

HF13 avoids one universal substance definition.

Minimal relational working family:

```text
Power_D(A→B,C)
= A's effective capability, under context C and available alternatives, to alter B's
  option set, access to valued resources, incentives, actions or outcomes in domain D
```

---

# 110. Power is relational

```text
Power_D(A→B) != Power_D(A→C)
```

---

# 111. Power is domain-specific

```text
Power_D != Power_E
```

---

# 112. Power depends on alternatives

If B has strong exit options, A's effective power can fall.

Thus:

```text
Power depends on Dependence/Alternatives
```

---

# 113. Positional and subjective power differ

Experience-sampling evidence shows formal/positional power and subjective sense of
power correlate but are not identical.

Thus:

```text
PositionalPower != SubjectivePower
```

---

# 114. Perceived power is not actual control

```text
SenseOfPower != EffectivePower
```

---

# 115. Power can create illusory control

Experimental power manipulations can increase perceived control over outcomes beyond
actual influence.

Thus:

```text
PerceivedControl != ActualControl
```

---

# 116. Power is not legitimacy

A coercive actor can have high effective power and low legitimacy.

Thus:

```text
Power != Legitimacy
```

---

# 117. Power is not authority

```text
Power != Authority
```

though recognized authority may provide power.

---

# 118. Power is not status

```text
Power != Status
```

supported by differential experimental effects.

---

# 119. Power is not moral entitlement

```text
CanForce(X) != MayRightfullyRequire(X)
```

---

# 120. PowerProfile_D

```text
{
  holder,
  target,
  domain,
  resource/option controlled,
  dependence,
  alternatives/exit,
  enforcement capability,
  information asymmetry,
  formal position,
  perceived power,
  realized influence,
  resistance capability,
  legitimacy/authority relation
}
```

---

# 121. Authority

HF13 working relation:

```text
Authority_D(A,S,C)
= socially/institutionally recognized decision/directive/permission scope assigned
  to actor/office A within system S and context/domain C
```

This is descriptive institutional authority, not yet moral legitimacy.

---

# 122. Authority is not expertise

A judge may have legal authority over a case without being the best medical expert.

An expert may know best without decision authority.

Thus:

```text
Authority != Expertise
```

---

# 123. Epistemic authority requires qualification

Some literatures call trusted expertise `epistemic authority`.

HF13 records:

```text
EpistemicAuthority_D
```

separately from institutional decision authority.

---

# 124. Expertise can affect compliance without formal authority

Health-advice experiments show perceived expertise can drive deference.

Thus:

```text
ExpertInfluence != FormalAuthority
```

---

# 125. Authority is not coercive capacity

An authority can retain formal decision rights while lacking practical enforcement.

Thus:

```text
Authority != CoercivePower
```

---

# 126. Formal authority and practical power can dissociate

Therefore record:

```text
DeJureAuthority
DeFactoPower
```

separately.

---

# 127. Authority is scoped

```text
Authority_D != Authority_E
```

A physician's authority over clinical treatment does not grant authority over a
patient's bank account.

---

# 128. Authority can attach to office rather than occupant identity

When occupants change, decision rights can persist.

Thus:

```text
OfficeAuthority != OccupantPersonalTrait
```

---

# 129. Authority can be delegated

Delegation can alter operational scope while underlying institutional authority and
responsibility remain structured separately.

Retain HF10/HF11:

```text
Delegation != ResponsibilityElimination
```

---

# 130. Authority can be contested

Recognition may vary across audiences.

Thus:

```text
AuthorityRecognition_Audience1 != AuthorityRecognition_Audience2
```

---

# 131. AuthorityProfile_D

```text
{
  office/actor,
  institutional source,
  domain/scope,
  subjects/objects governed,
  decision/directive rights,
  delegation rights,
  enforcement mechanism,
  appeal/review path,
  de facto power,
  perceived legitimacy,
  normative-legitimacy question,
  uncertainty/contest
}
```

---

# 132. Legitimacy is overloaded

HF13 separates:

```text
PerceivedLegitimacy
Institutional/LegalValidity
NormativeLegitimacy
```

---

# 133. Perceived legitimacy

Working descriptive object:

```text
PerceivedLegitimacy_D(A,S)
= degree to which an observer/group regards an authority/rule/institution as
  appropriately entitled to issue decisions or expect deference in domain D
```

---

# 134. Perceived legitimacy can causally alter compliance

Fairer authority procedures/actions can increase compliance beyond material incentive
channels in experiments.

Thus:

```text
PerceivedLegitimacy can be CausalDecisionInput
```

---

# 135. Perceived legitimacy is not authority

```text
PerceivedLegitimacy != FormalAuthority
```

A formally valid office can be seen as illegitimate.

---

# 136. Perceived legitimacy is not normative legitimacy

Popularity or acceptance does not establish moral rightness.

Thus:

```text
PerceivedLegitimacy != NormativeLegitimacy
```

---

# 137. Legal validity is not normative legitimacy

```text
LegalValidity != NormativeLegitimacy
```

---

# 138. Moral conviction can constrain deference

Naturalistic/experimental evidence shows deeply held moral commitments can reduce
acceptance of otherwise authoritative decisions.

Thus:

```text
PerceivedAuthorityLegitimacy does not erase MoralEvaluation
```

---

# 139. More visible coercive power can reduce perceived legitimacy

Recent protest experiments show force displays can increase illegitimacy perception
and resistance.

Therefore:

```text
MoreCoerciveDisplay != MoreLegitimacy
```

---

# 140. Corruption information can reduce perceived institutional legitimacy

Thus legitimacy is historically and informationally updated, not a static property of
office names.

---

# 141. Legitimacy is not compliance

Agents may comply despite low legitimacy due to sanctions or dependence.

Thus:

```text
Compliance != PerceivedLegitimacy
```

---

# 142. Noncompliance is not proof of illegitimacy

A legitimate rule can be violated for self-interest, error or inability.

Thus:

```text
NonCompliance != IllegitimacyProof
```

---

# 143. LegitimacyProfile_D

```text
{
  target authority/rule/institution,
  audience,
  domain,
  procedural fairness evidence,
  outcome fairness evidence,
  source/history,
  perceived entitlement to rule,
  obligation-to-obey report,
  compliance behavior,
  coercive incentives,
  moral disagreement,
  legal validity,
  normative-legitimacy status
}
```

---

# 144. Sanction

Working family:

```text
Sanction_D
= socially/institutionally contingent consequence imposed or withheld in response to
  behavior relative to a rule/norm/decision
```

Sanctions may be negative or positive in broad usage.

---

# 145. Punishment is one sanction family

```text
Punishment != SanctionTotality
```

---

# 146. Reward can enforce behavior too

Thus:

```text
Enforcement != PunishmentOnly
```

---

# 147. Exclusion/ostracism can function as sanction

Partner-choice experiments show reputational information and exclusion can alter
cooperation.

---

# 148. Reputation loss can be sanction-like

But:

```text
ReputationChange != FormalPunishment
```

---

# 149. Peer and centralized sanctioning differ

Record:

```text
PeerSanction
ThirdPartySanction
CentralizedSanction
AutomatedSanction
```

---

# 150. Sanction is not norm

```text
Sanction != SocialNorm
```

It can support or oppose a norm.

---

# 151. Sanction is not legitimacy

```text
CanPunish != LegitimatelyMayPunish
```

---

# 152. Sanction is not repair

HF12 repair changes understanding/common ground.

HF13 sanction changes costs/status/access in relation to rule enforcement.

Thus:

```text
Sanction != CommunicationRepair
```

---

# 153. Enforcement success is not welfare success

Harmful-norm experiments are decisive.

```text
EnforcementSuccess != WelfareImprovement
```

---

# 154. Sanctions can crowd out cooperation

Experiments show sanctions perceived as selfish/unfair can reduce altruistic
cooperation.

Thus:

```text
MoreSanction != MoreIntrinsicCooperation
```

---

# 155. Sanction removal does not have one universal trajectory

Some cooperation collapses when enforcement disappears; other interventions can
preserve more cooperation after removal.

Thus:

```text
SanctionRemovalEffect_D != SanctionRemovalEffect_E
```

---

# 156. Sanctioning institutions can be selected

People may migrate toward sanctioning institutions under public-goods competition.

Thus institutional structure is itself an option/selection object.

---

# 157. Institutional selection is not moral endorsement

Choosing an enforcement institution for instrumental benefit does not establish moral
legitimacy.

Thus:

```text
InstitutionChoice != NormativeLegitimacy
```

---

# 158. SanctionProfile_D

```text
{
  enforcer,
  target,
  triggering rule/norm,
  sanction type,
  severity,
  probability,
  cost to enforcer,
  centralized/peer/automated,
  procedural basis,
  appeal/override,
  immediate compliance effect,
  long-term/internalization effect,
  reputation effect,
  welfare/externality effect,
  perceived legitimacy
}
```

---

# 159. Office

Working definition:

```text
Office_D
= persistent socially/institutionally defined position carrying a bundle of roles,
  permissions, authority, duties and succession conditions independent of one
  particular occupant
```

---

# 160. Office is not occupant

```text
Office != Occupant
```

---

# 161. Office persistence enables member turnover

```text
Occupant_t1 != Occupant_t2
```

while:

```text
Office_t1 ≈ Office_t2
```

under declared institutional continuity.

---

# 162. Office is not personhood

```text
Office != Person
```

---

# 163. Office is not organization

A president/CEO/maintainer role can exist within a larger organization.

Thus:

```text
Office != Organization
```

---

# 164. Organization

Working family:

```text
Organization_D
= bounded coordinated multi-agent system with some membership/role boundary,
  persistence mechanism and joint activity/resources under a declared identity
```

---

# 165. Organization is not institution

An organization is an actor/system that can instantiate institutions.

An institution can span many organizations and individuals.

Thus:

```text
Organization != Institution
```

---

# 166. Organization is not group person by default

```text
Organization != HumanIndividual
```

and legal personhood, when present, is a separate legal status.

---

# 167. Organization identity is typed

HF1 applies:

```text
SameOrganization
```

requires declared criteria such as charter/legal continuity, not same membership.

---

# 168. Institution

HF13 working family:

```text
Institution_D
= persistent socially reproduced structure of rules, roles/offices, permissions,
  expectations, records, resources and enforcement/coordination mechanisms that
  shapes recurring classes of interaction beyond one current episode
```

---

# 169. Institution is not building

Physical infrastructure can support an institution, but:

```text
Institution != Building
```

---

# 170. Institution is not organization

```text
Institution != Organization
```

A market institution can span many firms; an organization can contain multiple
institutional rule systems.

---

# 171. Institution is not repeated interaction only

```text
Institution != RepeatedDyad
```

because roles/rules can persist across participants.

---

# 172. Institution is not formal rulebook only

Effective institutions can contain:

```text
formal rules
informal norms
records
technical constraints
sanctions
practices
```

---

# 173. Institution is not enforcement only

```text
Institution != SanctionSystemOnly
```

---

# 174. Institution can externalize social memory

Records, ledgers, credentials, registries and archives preserve state beyond current
human memory.

Thus:

```text
InstitutionalMemory != Sum(CurrentMemberMemory)
```

---

# 175. Institution can externalize authority

Permissions can attach to office/credential rather than personal relationship.

---

# 176. Institution can externalize option constraints

Examples:

```text
access control
eligibility
tax schedule
queue system
property registry
software permission
```

shape options before current negotiation.

---

# 177. Formal and effective institutions differ

A rule may be formally declared yet practically unenforced.

Thus:

```text
DeJureInstitution != DeFactoInstitutionalPractice
```

---

# 178. Institutional persistence is history-dependent

Temporary incentives or enforcement can leave behavioral spillovers.

Thus:

```text
CurrentInstitutionalRule != WholeInstitutionalState
```

---

# 179. Institution can change preferences/expectations

Institutional exposure can alter later cooperation even when original enforcement
ends.

Therefore institutions are not only static constraint surfaces.

---

# 180. Institutions can crowd out or crowd in motives

Sanction design and perceived fairness can change voluntary cooperation.

Thus:

```text
InstitutionEffect != IncentiveEffectOnly
```

---

# 181. Institution is not necessarily legitimate

```text
InstitutionExists != InstitutionLegitimate
```

---

# 182. Institution is not necessarily welfare-improving

```text
InstitutionStable != WelfareImproving
```

---

# 183. Institution can encode harmful norms

Automated or formal enforcement can make harmful behavior more stable rather than
more justified.

---

# 184. InstitutionProfile_D

```text
{
  identity/scope,
  participant/member boundary,
  offices/roles,
  formal rules,
  informal norms,
  authority source,
  resources,
  records/memory,
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

---

# 185. Infrastructure

Physical/technical infrastructure can implement institutional constraints.

Examples:

```text
turnstile
identity provider
payment network
court registry
API authorization
```

---

# 186. Infrastructure is not institution

```text
Infrastructure != Institution
```

because the same infrastructure can implement different rules, and many institutions
persist through changing infrastructure.

---

# 187. But infrastructure can make rules executable

Institutional power can become mechanically enforced through code and architecture.

Thus:

```text
RuleText
→ InfrastructureConstraint
→ ReducedOptionSet
```

is one important institutional pathway.

---

# 188. Machine-readable rule is not legitimate rule

For Human×AI systems:

```text
ParsablePolicy != ValidAuthority
ValidAuthority != MoralLegitimacy
```

---

# 189. Automated enforcement intensifies authority mistakes

If an encoded rule is wrong, stale or illegitimate, automation can increase scale and
speed of error.

Thus:

```text
AutomationOfRule != ValidationOfRule
```

---

# 190. Human-in-the-loop does not solve institutional legitimacy automatically

HF11 retained:

```text
HumanInLoop != MeaningfulControl
```

HF13 adds:

```text
HumanApproval != NormativeLegitimacy
```

---

# 191. AI advice and AI authority must remain distinct

An AI can provide expert advice without possessing institutional decision authority.

Thus:

```text
AIEpistemicContribution != AIDecisionAuthority
```

---

# 192. AI-labeled advice does not automatically command compliance

Recent experiments find symbolic/expert labeling alone can fail to raise compliance.

Thus:

```text
AuthorityLabel != EffectiveAuthority
```

---

# 193. AI in judicial/institutional decision processes changes perceived legitimacy

Public experiments show legitimacy/fairness judgments depend on whether AI recommends
or decides and on social context.

Thus:

```text
AutomationLevel is an InstitutionalDesignVariable
```

---

# 194. AI can become enforcement substrate without becoming moral authority

A system may:

```text
detect violation
block action
rank applicants
apply penalty
```

while:

```text
NormativeAuthority remains elsewhere
```

---

# 195. Delegating unethical action to AI shows policy/authority separation

Human principals can use machine executors to realize unethical goals at higher
rates.

Thus:

```text
MachineExecution != MoralAuthorization
```

---

# 196. AI can inherit bad institutions faithfully

A perfectly accurate executor of an unjust policy still produces unjust outcomes.

Therefore:

```text
InstitutionalFidelity != NormativeCorrectness
```

---

# 197. AI can amplify de facto power

Automation increases:

```text
speed
scale
consistency
monitoring reach
```

which can increase effective power without changing legal authority.

Thus:

```text
Automation can change DeFactoPower while DeJureAuthority stays constant
```

---

# 198. Appeal and override are institutional surfaces

For executable rules record:

```text
who can appeal
who can override
latency
burden of proof
reversibility
```

not only nominal human oversight.

---

# 199. Institutional authority and moral agency remain separate

An AI executor can occupy an operational role without automatically becoming the
bearer of institutional responsibility or moral legitimacy.

---

# 200. Cross-context falsifier matrix

| Case | Naive collapse attacked | HF13 surviving distinction |
|---|---|---|
| decentralized naming convention converges | convention = explicit agreement | conventions can emerge from local coordination |
| committed minority flips established convention | persistence = permanence | convention stability and tipping are separate |
| microculture survives participant replacement | social order = same people | transmitted practice can outlive members |
| empirical and normative expectations manipulated separately | norm = common behavior | descriptive and injunctive expectation differ |
| frequency information changes moral/injunctive judgments | descriptive = injunctive | causal coupling does not imply identity |
| harmful public-good contribution punished into stability | enforcement = social good | bad norms can be stabilized |
| collective-risk history strengthens later norm | current incentive = norm state | norm state is path-dependent |
| direct experience outweighs conflicting reputation | reputation = direct history | provenance matters |
| multiple gossip reports improve cooperation but can be manipulated | consensus = truth | reputation requires source/provenance confidence |
| prestige and dominance both yield rank | status = one route | multiple rank mechanisms exist |
| high-status group member not best on unrelated quiz | status = competence | status is domain/social relation |
| status and power manipulate perspective taking differently | status = power | rank esteem and resource control differ |
| elected monitor induces more cooperation than random monitor | sanction power = authority | legitimacy/source of authority changes response |
| fairer enforcement raises compliance without changing material channel | compliance = coercion | perceived legitimacy has independent effect |
| moral conviction limits acceptance of court ruling | authority = moral trump | moral evaluation constrains deference |
| unjust law judged invalid/violable morally | law = morality | legal and moral evaluation dissociate |
| sanction perceived unfair crowds out altruism | more sanction = more cooperation | enforcement can change motivation negatively |
| institution chosen competitively | institution = imposed structure | agents can select institutional regime |
| institutional exposure spills into later behavior | institution = current incentive | institutional history alters policy |
| office authority survives occupant change | authority = personal influence | authority can attach to persistent office |
| AI decision role lowers perceived legitimacy versus human decider | automation = neutral implementation | institutional legitimacy depends on role allocation |
| AI follows unsafe authority cues | encoded authority cue = valid order | machine compliance does not validate authority |
| AI carries unethical delegated goals | execution = authorization | implementation and normative authority separate |

---

# 201. Competing models

## M1 — social order as repeated current interaction

### Failure

Conventions, offices, reputation and laws can affect strangers before direct
interaction.

**Disposition:** reject as complete model.

## M2 — convention as explicit agreement

### Failure

Large decentralized experiments create global conventions without central agreement.

**Disposition:** reject explicit-agreement necessity.

## M3 — convention as majority frequency

### Failure

Frequency does not explain coordination dependence, history or tipping.

**Disposition:** retain frequency as evidence, not ontology.

## M4 — social norm as common behavior

### Failure

Empirical and normative expectations dissociate; harmful behavior can be common but
condemned.

**Disposition:** reject.

## M5 — social norm as sanction threat

### Failure

Normative expectations/internalized responses can influence behavior absent immediate
material punishment.

**Disposition:** retain sanctions as one mechanism.

## M6 — norm as moral truth

### Failure

Bad norms can be enforced and persist.

**Disposition:** reject categorically.

## M7 — law as morality

### Failure

Unjust-law judgments and moral-conviction constraints on authority.

**Disposition:** reject.

## M8 — reputation as direct experience

### Failure

Gossip/third-party records change first interactions.

**Disposition:** reject; retain provenance-separated reputation.

## M9 — reputation as truth

### Failure

Manipulated gossip and source conflict.

**Disposition:** reject.

## M10 — status as competence

### Failure

Naturally high-status members need not be best on novel task.

**Disposition:** reject.

## M11 — status as power

### Failure

Experimental status and power manipulations produce different outcomes.

**Disposition:** separate esteem/rank from resource/option control.

## M12 — prestige as status totality

### Failure

Dominance also produces rank/influence under some contexts.

**Disposition:** retain prestige/dominance as routes/model families.

## M13 — power as authority

### Failure

Coercive actors can lack recognized right; formal authorities can lack practical
power.

**Disposition:** separate de facto power from de jure authority.

## M14 — authority as expertise

### Failure

Expert recommendation and institutional decision rights dissociate.

**Disposition:** separate epistemic and institutional authority.

## M15 — legitimacy as compliance

### Failure

Agents can comply under threat while rejecting legitimacy, or disobey legitimate
rules.

**Disposition:** reject behavioral readout.

## M16 — legitimacy as popularity

### Failure

Perceived legitimacy is descriptive belief; normative justification is a different
question.

**Disposition:** preserve normative firewall.

## M17 — sanctions as always cooperation-enhancing

### Failure

Crowding-out and harmful-norm enforcement.

**Disposition:** use outcome/motive-sensitive SanctionProfile.

## M18 — institution as organization

### Failure

Institutions span organizations; organizations contain multiple rule systems.

**Disposition:** separate.

## M19 — institution as rulebook

### Failure

De facto norms, records, authority, infrastructure and enforcement affect actual
behavior.

**Disposition:** reject text-only model.

## M20 — institution as current incentives

### Failure

Path dependence and post-removal spillovers.

**Disposition:** institution has historical state.

## M21 — automated enforcement as neutral execution

### Failure

Automation changes scale, de facto power, perceived legitimacy, oversight and
responsibility surfaces.

**Disposition:** treat automation as institutional architecture.

## M22 — existing social order as normative authority

### Failure

Unjust laws, harmful norms, coercive power and illegitimate institutions.

**Disposition:** reject. This exposes HF14.

---

# 202. HF13 anti-laws

## Persistent order / convention

1. `Persistent != Irreversible`.
2. `Persistent != Legitimate`.
3. `Persistent != Universal`.
4. `CurrentInteractionState != PersistentSocialOrder`.
5. `BehavioralRegularity != Convention`.
6. `BehavioralRegularity != SocialNorm`.
7. `Frequency != Approval`.
8. `ActualBehaviorFrequency != DescriptiveNormBelief`.
9. `Convention != IndividualHabit`.
10. `Convention != ExplicitAgreement`.
11. `Convention != Law`.
12. `Convention != SocialNorm`.
13. `ConventionEmergence != PopulationWideSharedGoalRequirement`.
14. `EstablishedConvention != IrreversibleConvention`.
15. `MajorityBehavior != ConventionMechanism`.
16. `CurrentEnvironmentSame != ConventionSame`.
17. `ConventionPersistence != OriginalMemberPersistence`.
18. `CulturalTransmission != LiteralCopyingOnly`.

## Norms / expectations

19. `EmpiricalExpectation != ActualFrequency`.
20. `NormativeExpectation != PersonalNormativeBelief`.
21. `NormativeExpectation != MoralJustification`.
22. `EmpiricalExpectation != NormativeExpectation`.
23. `DescriptiveNorm != InjunctiveNorm`.
24. `SocialNorm != CommonBehavior`.
25. `SocialNorm != NormativeExpectationOnly`.
26. `SocialNorm != SanctionMechanismOnly`.
27. `NormCompliance != PreferenceExpression by definition`.
28. `SocialNorm != MoralNorm`.
29. `SocialNorm != Law`.
30. `NormStrength != OneScalar by default`.
31. `ObservedCompliance != NormInternalization`.
32. `Internalized != Justified`.
33. `ComplianceWhenWatched != InternalizedNorm`.
34. `NormViolation != NormIgnorance`.
35. `CurrentPayoffStructure != CurrentNormStrength`.
36. `HistoricalAdaptiveness != CurrentValue`.
37. `NormCompliance != WelfareImprovement`.
38. `NormEnforcement != NormativeGood`.
39. `IsCommon(X) != Ought(X)`.

## Rule / law

40. `Rule != SocialNorm`.
41. `WrittenRule != ActualPractice`.
42. `Rule != Law`.
43. `RuleExists != RuleFollowed`.
44. `RecognizeRule != EndorseRule`.
45. `Policy != Norm`.
46. `Policy != Law`.
47. `LegalValidity != MoralRightness`.
48. `LawInForce != UniversalCompliance`.
49. `LegalCompliance != LegitimacyResponseOnly`.

## Reputation

50. `ReputationInformation != DirectInteractionHistory`.
51. `DirectEvidence != ReputationEvidence`.
52. `Reputation != VerifiedTrait`.
53. `ConsensusReputation != GroundTruth`.
54. `Reputation != Trust`.
55. `Reputation != Status`.
56. `Reputation_D != Reputation_E`.
57. `Credential != Reputation`.
58. `Credential != CurrentCompetence`.
59. `Stereotype != IndividualReputation`.

## Status / prestige / dominance / influence

60. `Status != Power`.
61. `Status != Authority`.
62. `Status != TaskCompetence`.
63. `Status_D != Status_E`.
64. `Expertise != Prestige`.
65. `Prestige != Status`.
66. `Dominance != Power`.
67. `Dominance != Authority`.
68. `HighRank != PrestigeOnly`.
69. `HighRank != DominanceOnly`.
70. `Influence != Power`.
71. `Influence != Authority`.

## Power / authority / legitimacy

72. `Power_D(A→B) != Power_D(A→C)`.
73. `Power_D != Power_E`.
74. `PositionalPower != SubjectivePower`.
75. `SenseOfPower != EffectivePower`.
76. `PerceivedControl != ActualControl`.
77. `Power != Legitimacy`.
78. `Power != Authority`.
79. `Power != Status`.
80. `CanForce(X) != MayRightfullyRequire(X)`.
81. `Authority != Expertise`.
82. `ExpertInfluence != FormalAuthority`.
83. `Authority != CoercivePower`.
84. `OfficeAuthority != OccupantPersonalTrait`.
85. `PerceivedLegitimacy != FormalAuthority`.
86. `PerceivedLegitimacy != NormativeLegitimacy`.
87. `LegalValidity != NormativeLegitimacy`.
88. `MoreCoerciveDisplay != MoreLegitimacy`.
89. `Compliance != PerceivedLegitimacy`.
90. `NonCompliance != IllegitimacyProof`.

## Sanction / enforcement

91. `Punishment != SanctionTotality`.
92. `Enforcement != PunishmentOnly`.
93. `ReputationChange != FormalPunishment`.
94. `Sanction != SocialNorm`.
95. `CanPunish != LegitimatelyMayPunish`.
96. `Sanction != CommunicationRepair`.
97. `EnforcementSuccess != WelfareImprovement`.
98. `MoreSanction != MoreIntrinsicCooperation`.
99. `SanctionRemovalEffect_D != SanctionRemovalEffect_E`.
100. `InstitutionChoice != NormativeLegitimacy`.

## Office / organization / institution / infrastructure

101. `Office != Occupant`.
102. `Office != Person`.
103. `Office != Organization`.
104. `Organization != Institution`.
105. `Organization != HumanIndividual`.
106. `Institution != Building`.
107. `Institution != Organization`.
108. `Institution != RepeatedDyad`.
109. `Institution != SanctionSystemOnly`.
110. `InstitutionalMemory != Sum(CurrentMemberMemory)`.
111. `DeJureInstitution != DeFactoInstitutionalPractice`.
112. `CurrentInstitutionalRule != WholeInstitutionalState`.
113. `InstitutionEffect != IncentiveEffectOnly`.
114. `InstitutionExists != InstitutionLegitimate`.
115. `InstitutionStable != WelfareImproving`.
116. `Infrastructure != Institution`.

## Human×AI institutional order

117. `ParsablePolicy != ValidAuthority`.
118. `ValidAuthority != MoralLegitimacy`.
119. `AutomationOfRule != ValidationOfRule`.
120. `HumanApproval != NormativeLegitimacy`.
121. `AIEpistemicContribution != AIDecisionAuthority`.
122. `AuthorityLabel != EffectiveAuthority`.
123. `MachineExecution != MoralAuthorization`.
124. `InstitutionalFidelity != NormativeCorrectness`.

---

# 203. Minimum HF13 grammar

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

Cross-cutting hierarchy:

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

---

# 204. Reconnection to HF12

HF12 relations are episodes.

HF13 explains how episode histories become:

```text
conventions
reputations
roles
offices
norms
institutional rules
```

that constrain later interactions.

Thus:

```text
RelationshipHistory != Institution
```

but relationship histories can feed institutional/persistent order.

---

# 205. Reconnection to HF11

Institutions change action affordances:

```text
PhysicallyPossibleAction
```

may be:

```text
permitted
forbidden
blocked
sanctioned
```

at a social/institutional level.

Thus:

```text
PhysicalAffordance != InstitutionalPermission
```

---

# 206. Reconnection to HF10

Institutions reshape:

```text
OptionSet
SearchCost
CommitmentCost
SwitchingCost
Authorization
```

before a decision begins.

Therefore:

```text
InstitutionalArchitecture
is DecisionArchitecture
```

for many tasks.

---

# 207. Reconnection to HF9

Reputation and authority are inferential objects.

Humans infer hidden traits/credibility from incomplete social evidence.

Thus:

```text
ReputationEvidence != TraitTruth
AuthorityClaim != ValidAuthorityProof
```

---

# 208. Reconnection to HF8

Norms and institutions require representations of:

```text
rules
roles
categories
permissions
prohibitions
exceptions
```

but representation of a rule does not make it valid.

---

# 209. Reconnection to HF7

Institutions externalize memory through:

```text
records
registries
precedents
contracts
credentials
```

while:

```text
PersistentRecord != VerifiedTruth
```

continues to apply.

---

# 210. Reconnection to HF6

Norms and institutions are history-dependent systems.

```text
History
→ changed social transition function
```

is an HF6-style persistent-change process at a social scale.

---

# 211. Reconnection to HF4

Compliance behavior is still action allocation under values/goals/costs.

Social structure modifies:

```text
incentive
expected sanction
reputation value
identity value
moral value
```

but does not replace individual motivation.

---

# 212. Reconnection to HF1

Office, organization, institution and person are typed identities.

```text
SameOffice != SameOccupant
SameOrganization != SameMembers
Institution != HumanIndividual
```

---

# 213. Reflexivity becomes institutional

A reputation score, status classification or institutional judgment can alter the
future behavior it purports to measure.

Thus:

```text
InstitutionalMeasurement
may become
InstitutionalIntervention
```

---

# 214. Classification can create path dependence

Examples:

```text
credit score
risk category
credential
professional ranking
```

can alter future opportunities, which alter later evidence.

Therefore:

```text
Classification_t
→ OptionSet_{t+1}
→ Outcome_{t+1}
→ Evidence_{t+2}
```

---

# 215. Institutional feedback can become self-reinforcing

This does not mean all institutional classifications are self-fulfilling, only that
causal feedback must be considered.

---

# 216. Heterogeneity matters

Different members may experience the same institution through different:

```text
status
power
sanction exposure
exit options
legal rights
resource dependence
```

Thus:

```text
SameFormalRule != SameEffectiveConstraint
```

---

# 217. Equality of rule text is not equality of effect

```text
SameRuleText
+
DifferentResources/Power
→ DifferentActionSets
```

This becomes a major normative boundary.

---

# 218. Descriptive institutional success is not justice

An institution can be:

```text
stable
predictable
efficient
widely obeyed
```

and still distribute harm or rights unjustly.

Therefore:

```text
Stable + Efficient + CompliedWith
!=
Just
```

---

# 219. The strongest residual is not another social-mechanism layer

HF13 repeatedly reaches questions that cannot be answered by more descriptive
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

These are normative questions.

---

# 220. Perceived legitimacy cannot answer normative legitimacy

Even unanimous acceptance cannot by itself prove that a rule ought to exist.

Thus:

```text
EveryoneBelievesLegitimate(X)
!=
XIsNormativelyLegitimate
```

---

# 221. Moral judgment is not social norm

A person can morally reject prevailing norm.

Thus:

```text
MoralJudgment != SocialNormBelief
```

---

# 222. Moral norm is not statistical norm

```text
MoralOught != MajorityBehavior
```

---

# 223. Fairness is not equal outcomes by definition

HF13 encounters fairness repeatedly in legitimacy/sanction evidence but does not
freeze a fairness ontology.

This remains unresolved.

---

# 224. Welfare is not compliance

```text
HigherCompliance != HigherWelfare
```

---

# 225. Harm is not sanction

A sanction may be harmful but some harms are not sanctions.

Thus:

```text
Harm != Sanction
```

---

# 226. Rights are not permissions in one current system by definition

Institutional permission is descriptive/legal status.

A moral/legal rights ontology requires separate reconstruction.

---

# 227. Duty is not social expectation

```text
OthersExpect(X) != IHaveDuty(X)
```

without declared normative grounding.

---

# 228. Responsibility is not causal contribution only

HF1 already separated causal actor from responsible person.

HF13 institutional cases make the gap unavoidable:

```text
caused
executed
authorized
failed to supervise
benefited
had duty to prevent
```

can belong to different actors.

---

# 229. Efficiency is not legitimacy

```text
EfficientInstitution != LegitimateInstitution
```

---

# 230. Democratic selection is not sufficient normative proof

Election/choice can increase perceived legitimacy, but:

```text
SelectedByMajority != MorallyPermissibleByDefinition
```

---

# 231. Expertise is not moral authority

```text
KnowsBestAboutMeans != HasRightToChooseEnds
```

---

# 232. Power is not right

The deepest HF13 firewall remains:

```text
Can
!=
May
!=
Ought
```

---

# 233. Cross-domain evidence for the residual

HF13's own primary falsifiers include:

```text
harmful norm + effective sanction
unjust law + legal recognition
formal authority + moral objection
procedural legitimacy + compliance effect
power + low perceived legitimacy
AI enforcement + unfair/unsafe result
```

Across all of them, the missing variable is not another empirical social relation.
It is **normative evaluation**.

---

# 234. Exact next foundation

Therefore HF13 selects:

# HF14 — Morality, Harm, Welfare, Fairness, Justice, Rights, Duties, Responsibility and Legitimacy

HF14 must reconstruct rather than assume:

```text
moral judgment
harm
benefit/welfare
fairness
equality/equity
desert
justice
right
permission
prohibition
duty/obligation
responsibility/accountability
legitimacy
conflict among values/rights
```

---

# 235. HF14 starting questions

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

---

# 236. Candidate HF14 falsifiers

- highly prevalent behavior judged morally wrong;
- unjust law recognized as law but rejected as morally binding;
- authority decision accepted procedurally but rejected on moral grounds;
- welfare-improving policy judged unfair because burdens/benefits are distributed
  differently;
- equal outcomes judged unfair when contributions/needs differ;
- unequal outcomes judged fair under some desert/need principles;
- accidental harm versus intentional harm with equal physical outcome;
- causal contribution without responsibility and responsibility without direct
  physical execution;
- coercion/ignorance reducing responsibility;
- rights constraints overriding aggregate welfare gains;
- procedural fairness changing legitimacy despite identical outcomes;
- legitimate procedure producing harmful outcome and beneficial outcome produced by
  illegitimate procedure;
- Human principal authorizing action, AI executing action and institution allocating
  responsibility differently;
- AI faithfully applying a formally valid rule that violates higher-order safety or
  rights constraint.

---

# 237. Do not precommit

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
- moral legitimacy can be inferred from model training data or observed Human
  behavior;
- AI should maximize any single moral metric by foundation fiat.

---

# 238. Stop rule

Do not schedule HF15 now.

HF14 must expose a repeated neighboring distinction whose absence creates category
failures across materially different moral/normative cases.

---

# 239. HF13 synthesis

HF13 began with persistent social order and found that one word such as `norm` or
`authority` hides several different causal objects.

The surviving structure is:

```text
Regularity
!= Convention
!= SocialNorm
!= Rule
!= Law

ActualFrequency
!= EmpiricalExpectation
!= NormativeExpectation
!= PersonalNormativeBelief
!= MoralJustification

DirectHistory
!= Reputation
!= Credential
!= Stereotype

Status
!= Prestige
!= Dominance
!= Expertise
!= Influence
!= Power
!= Authority

FormalAuthority
!= DeFactoPower
!= PerceivedLegitimacy
!= NormativeLegitimacy

Sanction
!= Norm
!= Repair
!= Legitimacy

Office
!= Occupant
!= Organization
!= Institution
!= Infrastructure
```

Persistent order matters because it alters the option space of agents who did not
create it. But persistence provides no moral warrant.

The decisive final boundary is:

```text
What society does
!=
What society expects
!=
What society enforces
!=
What law permits
!=
What power can compel
!=
What ought to be done
```

HF13 can model the first five.

The sixth is HF14.
