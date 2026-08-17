---
schema_version: 1
id: human.foundations.hf14
title: HF14 — Morality, Harm, Welfare, Fairness, Justice, Rights, Duties, Responsibility and Legitimacy
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
summary: HF14 reconstructs normative evaluation without collapsing it into social conformity, law, preference, utility, equality or one moral theory. It separates moral judgment from normative truth; evaluative, deontic, rights, distributive, responsibility and legitimacy claims; harm event, harm experience and harm risk; welfare surfaces including affect, life satisfaction, preferences, functioning, capabilities and resources; equality, equity, need, merit/desert, priority, sufficiency, efficiency, outcome and procedural fairness; justice from fairness/law/welfare; legal and moral rights plus Hohfeldian claim/liberty/power/immunity relations; social expectation, commitment, promise, contract, legal duty and moral obligation; causal contribution, wrongdoing, moral responsibility, blame, punishment, legal liability and accountability; perceived/legal legitimacy and normative legitimacy; and Human–AI principal, recommender, executor, supervisor and institutional responsibility. The repeated residual is who or what can be a bearer of welfare, harm, rights, duties and moral consideration: moral standing, agency, patiency, sentience, interests, vulnerability and scope of concern.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
  - HF14
related:
  - human.foundations.hf13
  - human.foundations.hf14.sources
  - human.foundations.hf14.continuation
---
# HF14 — Morality, Harm, Welfare, Fairness, Justice, Rights, Duties, Responsibility and Legitimacy

## 0. Status and question

HF13 established a strict firewall:

```text
What society does
!= What society expects
!= What society approves
!= What society enforces
!= What law recognizes
!= What power can compel
!= What ought to be done
```

and compressed it to:

```text
Can != May != Ought
```

HF14 therefore asks:

> **What kinds of normative claims are humans actually making when they say that an
> action is wrong, a harm matters, an allocation is unfair, a person has a right, an
> agent is responsible, or an institution is legitimate?**

HF14 does **not** choose a single moral theory as Ordivon's ontology.

Instead it reconstructs the normative problem space strongly enough that competing
criteria remain visible and cannot be silently substituted for one another.

---

# 1. Normativity is not one scalar

HF14 rejects:

```text
NormativeValue(x) = one universal scalar
```

as a foundation ontology.

Different normative claims ask different questions.

---

# 2. Evaluative claims

Examples:

```text
good / bad
better / worse
beneficial / harmful
valuable / disvaluable
```

These compare states, outcomes, practices or traits under a declared evaluative
criterion.

---

# 3. Deontic claims

Examples:

```text
required
permitted
forbidden
optional
```

These concern what actions/omissions are normatively allowed or demanded.

---

# 4. Rights claims

Examples:

```text
A has a claim against B
A is free to do X
A has authority to alter relation R
A is protected against another actor changing R
```

These are relational structures, not generic positive values.

---

# 5. Responsibility claims

Examples:

```text
A caused X
A was responsible for task T
A is morally responsible for X
A is blameworthy
A is legally liable
A must answer for X
```

These are not synonyms.

---

# 6. Distributive claims

Examples:

```text
equal split
equity by contribution
priority to need
reward by desert
maximize total benefit
protect a minimum threshold
```

Multiple criteria can conflict.

---

# 7. Legitimacy claims

Examples:

```text
this authority may rule
this procedure may bind
this coercion is justified
this institution has a right to impose this decision
```

These require more than observed acceptance.

---

# 8. Normative claim typing

HF14 therefore uses:

```text
NormativeClaim_K(subject, object, criterion, context)
```

where `K` must identify the claim family.

---

# 9. Moral judgment

Working empirical object:

```text
MoralJudgment_K(H,X,t,C)
= Human H's current moral evaluation of X on judgment surface K under context C
```

Possible K includes:

```text
wrongness
permissibility
blameworthiness
punishment appropriateness
praise
obligation
fairness
rights violation
```

---

# 10. Moral judgment is not moral truth

The foundational distinction is:

```text
MoralJudgment(H,X) != NormativeTruth(X)
```

HF14 can study how humans judge without treating population judgment as final moral
authority.

---

# 11. Moral judgment is not preference

A Human can prefer an outcome while judging the act producing it wrong.

Thus:

```text
Preference != MoralJudgment
```

---

# 12. Moral judgment is not social norm belief

A person can judge prevailing practice immoral.

Thus:

```text
MoralJudgment != SocialNormBelief
```

---

# 13. Moral judgment is not legal judgment

A person can judge an act:

```text
legal but wrong
illegal but justified
```

Thus:

```text
MoralJudgment != LegalStatusJudgment
```

---

# 14. Moral emotion is not moral judgment

Disgust, anger, guilt or empathy can influence moral judgment without defining it.

Thus:

```text
MoralEmotion != MoralJudgment
```

---

# 15. Wrongness is not blameworthiness

Primary experiments show mental states and causal outcome relations contribute
differently to judgments of wrongness versus blame/punishment.

Thus:

```text
Wrongness != Blameworthiness
```

---

# 16. Blameworthiness is not punishment

One can judge an agent blameworthy while opposing punishment, or endorse preventive
restrictions without blame.

Thus:

```text
Blameworthiness != PunishmentAppropriateness
```

---

# 17. Permissible is not good

An action can be permissible without being ideal.

Thus:

```text
Permissible != Good
```

---

# 18. Not required is not forbidden

Deontic space contains optional actions.

Thus:

```text
NotRequired != Forbidden
```

---

# 19. Not forbidden is not recommended

```text
Permitted != Recommended
```

---

# 20. Moral judgment is context-sensitive

Intent, causal structure, foreseeability, outcome, action/omission, means/side-effect
and domain can change judgment.

Therefore:

```text
MoralJudgment_K(X,C1) != MoralJudgment_K(X,C2)
```

is possible without inconsistency.

---

# 21. Intent is a major but non-total input

Cushman's moral-judgment experiments support a strong role for agent mental states in
wrongness/permissibility.

But:

```text
Intent != MoralJudgmentTotality
```

---

# 22. Outcome matters differently across judgment surfaces

Harmful consequence and causal connection affect blame/punishment even when intent
is held similar.

Thus:

```text
OutcomeEffect_wrongness != OutcomeEffect_blame
```

---

# 23. Causation matters differently across surfaces

```text
CausalContribution
```

can increase blame while an attempted wrong remains morally wrong despite failure to
cause the intended harm.

Therefore:

```text
Wrongdoing != SuccessfulCausationRequirement
```

---

# 24. Foreseeability is separate from intent

An unintended consequence can be foreseeable.

Thus:

```text
Foreseeability != Intent
```

---

# 25. Foreseeability affects blame

Experiments manipulating intentionality and foreseeability independently show both
can influence cause/blame judgments.

Thus responsibility profiles must preserve both.

---

# 26. Hindsight can distort negligence judgment

Knowledge that a bad outcome occurred can increase perceived ex ante probability and
culpability.

Therefore:

```text
ExPostOutcomeKnowledge != ExAnteForeseeability
```

---

# 27. Moral luck is not outcome-only morality

Observers can change blame when outcomes differ, but beliefs about justification,
causality and mental state mediate much of the effect.

Thus:

```text
OutcomeDifference != MoralResponsibilityDifferenceByDefinition
```

---

# 28. Action and omission are not automatically equivalent in judgment

Human judgment often treats action and omission differently under some contexts.

HF14 does not elevate that empirical pattern to normative truth.

Thus:

```text
ActionOmissionJudgmentDifference != NormativePrincipleByDefault
```

---

# 29. Means and side effect can differ in judgment

Instrumental harm versus foreseen side-effect harm can produce different moral
judgments.

Again:

```text
ObservedJudgmentPattern != MoralTruth
```

---

# 30. Moral-domain effects exist

Intent can matter differently for harm versus purity/conventional violations.

Thus:

```text
MoralJudgmentMechanism_D != MoralJudgmentMechanism_E
```

---

# 31. MoralJudgmentProfile

```text
{
  judgment target,
  judgment type,
  agent intent/desire,
  belief/knowledge,
  causal contribution,
  outcome,
  foreseeability,
  action/omission,
  means/side-effect,
  control/alternatives,
  norm/law context,
  relationship,
  emotion,
  confidence,
  reasoning process,
  cultural/contextual scope
}
```

---

# 32. Harm is overloaded

HF14 separates:

```text
HarmfulEvent
HarmfulStateChange
HarmExperience
HarmRisk
HarmThreat
HarmRightsViolation
HarmJudgment
```

---

# 33. Harm event

Working descriptive relation:

```text
HarmfulStateChange_D(X→Y)
= change that worsens a declared welfare/interest/function/rights-relevant dimension
  for target Y under criterion D
```

This is criterion-relative and does not assume a single welfare theory.

---

# 34. Harm experience

```text
HarmExperience
```

may include pain, fear, humiliation, distress, grief or other adverse experience.

---

# 35. Pain is not harm totality

Psychological-harm experiments show harms can be recognized without physical pain or
bodily injury.

Thus:

```text
Pain != Harm
```

---

# 36. No pain does not imply no harm

Examples can include:

```text
fraud
privacy invasion
lost opportunity
reputational damage
future risk
```

under some normative accounts.

Thus:

```text
NoPain != NoHarm
```

---

# 37. Physical damage is not experienced harm

An injury can occur under anesthesia without contemporaneous pain.

Thus:

```text
PhysicalDamage != HarmExperience
```

---

# 38. Psychological harm is not physical damage

```text
PsychologicalHarm != PhysicalDamage
```

---

# 39. Harm risk is not realized harm

```text
RiskOfHarm != RealizedHarm
```

---

# 40. Expected harm is not observed harm

```text
ExpectedHarm != RealizedHarm
```

---

# 41. Harm probability and harm magnitude are separate

```text
RiskProfile = (probability, severity, uncertainty, reversibility, exposure)
```

rather than one label.

---

# 42. Harm severity is not wrongness

Necessary medical pain can be severe while justified under a declared criterion.

Thus:

```text
HarmSeverity != Wrongness
```

---

# 43. Wrongness is not harm amount only

Intent, rights, consent, alternatives and distribution can matter.

Thus:

```text
Wrongness != HarmMagnitudeOnly
```

---

# 44. Preference frustration is not harm by definition

A harmful preference can be frustrated beneficially; preferences may be uninformed,
adaptive or conflicting.

Thus:

```text
PreferenceFrustration != Harm by definition
```

---

# 45. Rights violation is not harm experience

Some rights accounts recognize violations even when the holder never experiences
distress.

Thus:

```text
RightsViolation != HarmExperience
```

---

# 46. Harm and rights violation can overlap

but neither reduces to the other.

---

# 47. Harm can be relational or opportunity-based

Loss of option/capability can matter even before an adverse experience occurs.

This links harm to capability and rights without collapsing them.

---

# 48. Harm can be reversible or irreversible

Record:

```text
reversibility
repairability
duration
trajectory
```

---

# 49. Harm can be distributed across time

Short-term pain can produce long-term benefit, or immediate benefit long-term harm.

Thus:

```text
CurrentValence != WholeHarmTrajectory
```

---

# 50. HarmProfile_D

```text
{
  target,
  affected dimension,
  event/state change,
  experienced adversity,
  physical/psychological/function/opportunity effect,
  probability,
  magnitude,
  duration,
  reversibility,
  uncertainty,
  consent,
  intent,
  foreseeability,
  alternatives,
  rights relation,
  distribution/externalities
}
```

---

# 51. Welfare is not one observed variable

HF14 rejects one foundation scalar `Welfare`.

Useful welfare surfaces include:

```text
experienced affect / pain / pleasure
life satisfaction / evaluative well-being
preference satisfaction
health/functioning
capabilities/opportunities
resources
relationships/social connection
meaning/purpose
security/autonomy
```

without asserting all belong to one universal theory.

---

# 52. Experienced utility

One family concerns moment-to-moment experienced quality.

---

# 53. Remembered utility

Another concerns retrospective evaluation.

---

# 54. Decision utility

Another concerns choice-revealed value/preferences.

These can dissociate.

---

# 55. Choice is not experienced welfare

Classic cold-pressor work showed participants can choose a longer total painful
experience when its ending is less painful.

Thus:

```text
Choice != ExperiencedWelfare
```

---

# 56. Remembered utility is not experienced utility

```text
RememberedUtility != ExperiencedUtility
```

---

# 57. Preference is not welfare totality

```text
PreferenceSatisfaction != WelfareTotality
```

---

# 58. Preference can be adaptive

Long-term conditions can change what people expect or prefer.

Thus:

```text
CurrentPreference != ContextIndependentWelfareMetric
```

---

# 59. Public preference is not patient welfare truth

Health-state valuation studies show systematic differences between affected patients
and general-population respondents.

Therefore:

```text
PopulationPreference != TargetExperiencedWelfare
```

---

# 60. Life satisfaction is not positive affect

Psychometric evidence distinguishes life satisfaction, positive affect and negative
affect.

Thus:

```text
LifeSatisfaction != PositiveAffect
```

---

# 61. Positive affect is not absence of negative affect

```text
PositiveAffect != -NegativeAffect
```

as a simple identity.

---

# 62. Resources are not welfare

Money, time, housing or tools can support welfare but do not constitute the whole
relation.

Thus:

```text
ResourceAmount != Welfare
```

---

# 63. Capability is not current outcome

A person may have valuable options they do not currently exercise.

Thus:

```text
CapabilitySet != CurrentFunctioning
```

---

# 64. Functioning is not capability

```text
CurrentFunctioning != OpportunityFreedom
```

---

# 65. Welfare and capability can conflict in measurement

A person can report high satisfaction while possessing very restricted options, or
have broad options while experiencing low affective well-being.

HF14 preserves both surfaces.

---

# 66. Welfare is time-indexed

```text
Welfare_D(t1) != Welfare_D(t2)
```

---

# 67. Welfare is domain-indexed

```text
Welfare_D != Welfare_E
```

---

# 68. Aggregated welfare is not distribution

Two populations can have same total score with radically different distributions.

Thus:

```text
AggregateWelfare != WelfareDistribution
```

---

# 69. WelfareProfile_D

```text
{
  subject(s),
  time horizon,
  experienced affect/pain,
  life satisfaction,
  preferences,
  health/functioning,
  capability/opportunities,
  resources,
  relationships,
  meaning/purpose,
  autonomy/security,
  uncertainty,
  adaptation/history,
  distribution across persons/time
}
```

---

# 70. Fairness is not equality

This is one of HF14's decisive separations.

Experiments show humans may regard achievement-based inequality as fair while
rejecting luck-based inequality.

Thus:

```text
Equality != Fairness
```

---

# 71. Inequality is not unfairness

```text
Inequality != Unfairness
```

---

# 72. Equality

Working descriptive allocation relation:

```text
Equality_D
= equality on declared metric D
```

Examples:

```text
resources
outcomes
opportunities
rights
votes
```

---

# 73. Equal resources are not equal welfare

Different needs can make identical resources produce unequal outcomes.

Thus:

```text
EqualResources != EqualWelfare
```

---

# 74. Equal outcomes are not equal opportunities

```text
EqualOutcome != EqualOpportunity
```

---

# 75. Equity is overloaded

HF14 uses `Equity_D` only with a declared proportionality criterion, such as
contribution/effort/claim.

---

# 76. Equity is not equality

```text
Equity != Equality
```

---

# 77. Need

HF5 already separated organismic need types.

HF14 uses:

```text
DistributiveNeed_D
```

for a normative reason to prioritize resources based on a target shortfall or
threshold relevant to the allocation domain.

---

# 78. Need is not merit

```text
Need != Merit
```

---

# 79. Need is not equal share

Objective-need experiments show allocators trade need against equality and self-
interest.

Thus:

```text
NeedPrinciple != EqualityPrinciple
```

---

# 80. Need is not one metric

Need can refer to:

```text
minimum survival threshold
health shortfall
urgency
capacity to benefit
lack of alternatives
```

which can conflict.

---

# 81. Merit

Working descriptive input:

```text
Merit_D
= achievement/contribution/performance evidence treated as allocation-relevant under
  criterion D
```

---

# 82. Merit is not moral desert by definition

```text
MeritEvidence != DesertConclusion
```

---

# 83. Desert

Working normative family:

```text
Desert_D(A,X)
= claim that A normatively deserves X in light of declared responsibility,
  contribution, conduct or other desert basis
```

HF14 does not endorse one desert basis.

---

# 84. Effort is not desert automatically

```text
Effort != Desert
```

---

# 85. Outcome is not desert automatically

Luck can affect outcome.

Thus:

```text
OutcomeAchievement != Desert
```

---

# 86. Priority

Prioritarian families give additional normative weight to benefits for worse-off
people.

HF14 records this as a competing criterion family rather than foundation truth.

---

# 87. Priority is not equality

```text
PriorityToWorseOff != Equality
```

---

# 88. Sufficiency

Sufficientarian families prioritize reaching a threshold.

Again, this is a normative model family, not settled ontology.

---

# 89. Sufficiency is not equality

```text
Sufficiency != Equality
```

---

# 90. Efficiency

Working allocation criterion:

```text
Efficiency_D
= producing more of declared valued output from available resources
```

---

# 91. Efficiency is not fairness

Participants may destroy a resource rather than personally choose an inequitable
allocation between equally deserving recipients.

Thus:

```text
Efficiency != Fairness
```

---

# 92. Fairness is not welfare maximization

```text
Fairness != AggregateWelfareMaximization
```

---

# 93. Fairness is not need only

```text
Fairness != NeedPrincipleOnly
```

---

# 94. Fairness is not merit only

```text
Fairness != MeritPrincipleOnly
```

---

# 95. Plural fairness ideals are empirically real

Production/allocation experiments show heterogeneous participants use different
fairness ideals.

Thus:

```text
PopulationFairnessJudgment != OneSharedFairnessRule
```

---

# 96. Fairness judgment is not fairness truth

```text
FairnessJudgment != NormativeFairnessTruth
```

---

# 97. Self-interest can alter fairness judgment

Role-dependent experiments show moral/fairness judgment can shift with one's stake.

Thus:

```text
FairnessReport can be MotivationallyBiased
```

---

# 98. Procedural fairness

Working empirical/normative family:

```text
ProceduralFairness
= fairness of how a decision is generated, including voice, consistency,
  impartiality, information quality, contestability and similar criteria depending
  on context
```

---

# 99. Outcome fairness

Working family:

```text
OutcomeFairness
= fairness of resulting distribution/treatment under declared distributive criteria
```

---

# 100. Procedural fairness is not outcome fairness

```text
ProceduralFairness != OutcomeFairness
```

Experiments show both independently affect reactions.

---

# 101. Fair procedure can make an unequal outcome more acceptable

This demonstrates causal relevance of procedure to human legitimacy/fairness
judgments without proving that fair process justifies every outcome.

---

# 102. Good outcome does not erase bad process

```text
BeneficialOutcome != FairProcedure
```

---

# 103. Fair procedure does not guarantee good outcome

```text
FairProcedure != BeneficialOutcomeGuarantee
```

---

# 104. Responsibility for inequity matters

When a random device selects between equally deserving recipients, people are more
willing to accept an inequitable but efficient outcome than when they personally
choose who loses.

Therefore:

```text
OutcomeDistributionSame
+
DecisionResponsibilityDifferent
→ FairnessChoiceDifferent
```

---

# 105. FairnessProfile_D

```text
{
  allocation target,
  metric of equality,
  opportunity state,
  need/threshold,
  contribution/merit,
  desert basis,
  worst-off position,
  sufficiency threshold,
  total efficiency/welfare,
  procedure,
  responsibility for allocation,
  randomness/luck,
  uncertainty,
  affected parties,
  externalities,
  expressed judgment
}
```

---

# 106. Justice is broader than one allocation rule

HF14 uses:

```text
Justice_D
```

as a family of normative judgments about institutions, distributions, procedures,
rights and responsibilities under a declared normative framework.

---

# 107. Justice is not equality

```text
Justice != Equality
```

---

# 108. Justice is not fairness only

Some justice theories centrally include rights, freedom, legitimacy or recognition.

Thus:

```text
Justice != FairnessOnly
```

---

# 109. Justice is not law

```text
Justice != LegalValidity
```

---

# 110. Justice is not welfare maximization

```text
Justice != AggregateWelfareMaximization
```

by foundation fiat.

---

# 111. Justice is not institutional stability

```text
StableInstitution != JustInstitution
```

retaining HF13.

---

# 112. Justice claims require criterion transparency

Instead of:

```text
Policy X is just
```

record:

```text
Policy X satisfies/fails criteria {rights, welfare, fairness, procedure, ...}
under framework F
```

when consensus is absent.

---

# 113. Justice disagreement is not empirical error only

Two fully informed agents can disagree because they assign different normative
priority to rights, welfare, desert or equality.

Thus:

```text
NormativeDisagreement != EmpiricalErrorOnly
```

---

# 114. Better empirical information does not guarantee normative convergence

```text
PerfectFacts != OneNormativeAnswer by definition
```

---

# 115. Normative framework must be explicit

HF14 uses:

```text
NormativeFramework F
```

to expose criterion selection rather than hide it inside one scalar score.

---

# 116. Consequence/welfare family

One family evaluates actions/institutions primarily by outcomes/welfare.

HF14 records but does not endorse it.

---

# 117. Rights/deontic family

One family gives constraints or permissions that may not reduce to aggregate
outcomes.

HF14 records but does not endorse it.

---

# 118. Fairness/distributive family

One family focuses on allocation structure.

---

# 119. Procedural family

One family gives independent normative weight to decision process.

---

# 120. Desert/responsibility-sensitive family

One family allows responsibility/contribution to alter claims.

---

# 121. Capability/opportunity family

One family evaluates what people are substantively able to do or be, not only
resources or reported satisfaction.

---

# 122. Relational/non-domination family

One family treats standing, social relations or arbitrary power as normatively
important beyond outcome quantities.

HF14 retains it as a candidate family, not settled ontology.

---

# 123. Normative theories are not empirical models only

Empirical evidence can test predictions about human judgments or outcomes, but does
not by itself prove a normative principle.

Thus:

```text
EmpiricalFit(F) != NormativeTruth(F)
```

---

# 124. Moral intuition is evidence about human cognition

```text
MoralIntuition
```

is an important psychological phenomenon.

But:

```text
MoralIntuition != NormativeProof
```

---

# 125. Reflective judgment is not normative proof either

More deliberation can change moral judgments, but:

```text
Deliberation != TruthGuarantee
```

---

# 126. Consensus is not normative proof

```text
MoralConsensus != MoralTruth by definition
```

---

# 127. Disagreement is not proof that nothing is true

```text
NormativeDisagreement != NormativeNihilismProof
```

HF14 remains neutral on metaethical truth conditions.

---

# 128. Moral uncertainty

When relevant normative frameworks conflict, record:

```text
NormativeUncertainty = {
  candidate frameworks,
  criterion conflicts,
  factual uncertainty,
  interpretation uncertainty,
  confidence/robustness,
  reversible options
}
```

rather than silently averaging them.

---

# 129. Robust normative choice

A decision can be supported by multiple materially different frameworks.

This can increase robustness without proving one framework true.

---

# 130. Rights is an overloaded word

HF14 separates at least:

```text
LegalRight
MoralRight
ClaimRight
Liberty/Privilege
Power
Immunity
```

---

# 131. Hohfeldian legal decomposition

For legal analysis, Hohfeld's primary framework distinguishes correlatives:

```text
claim-right ↔ duty
liberty/privilege ↔ no-right
power ↔ liability
immunity ↔ disability
```

HF14 uses this as a legal concept decomposition, not as universal moral ontology.

---

# 132. Claim-right

Working legal relational form:

```text
ClaimRight_K(A,B,X)
```

means A has a claim such that B bears a corresponding duty regarding X under system
K.

---

# 133. Right is not permission

A liberty to do X need not imply someone else owes assistance.

Thus:

```text
ClaimRight != Liberty
```

and more generally:

```text
Right != Permission
```

without qualification.

---

# 134. Liberty is not claim-right

```text
Liberty_A(X) != ClaimAgainst_B(X)
```

---

# 135. Legal power is not physical power

A legal power changes legal relations.

Thus:

```text
LegalPower != PhysicalCapability
```

---

# 136. Immunity is not invulnerability

Legal immunity means another lacks legal power to alter a relation in a declared
way, not that physical harm is impossible.

Thus:

```text
LegalImmunity != PhysicalInvulnerability
```

---

# 137. Legal right is not moral right

```text
LegalRight != MoralRight
```

---

# 138. Moral right is not current-system permission

```text
MoralRight != CurrentInstitutionalPermission
```

---

# 139. Right is not capability

One can possess a legal/moral right but lack practical means to exercise it.

Thus:

```text
Right != Capability
```

---

# 140. Capability is not right

Being able to do X does not imply being entitled to do X.

Thus:

```text
Capability != Right
```

---

# 141. Right is not interest

Interests may ground rights under some theories, but:

```text
Interest != Right by definition
```

---

# 142. Right is not absolute trump by definition

Different rights frameworks specify conflicts/exceptions differently.

HF14 does not assume:

```text
EveryRight > EveryOtherNormativeConsideration
```

---

# 143. Rights conflict

Two actors can hold claims that cannot both be fully realized under scarcity.

Thus rights analysis requires conflict/priority rules rather than labels only.

---

# 144. RightsProfile_K

```text
{
  holder,
  addressee,
  object/action,
  right type,
  legal/moral system,
  corresponding duty/no-right/liability/disability,
  scope,
  exceptions,
  waiver/transfer,
  enforcement,
  remedy,
  conflict with other claims,
  practical capability to exercise
}
```

---

# 145. Duty is overloaded

Separate:

```text
MoralDuty
LegalDuty
RoleDuty
PromissoryObligation
ContractualObligation
TaskDuty
```

---

# 146. Duty is not social expectation

```text
OthersExpect(X) != Duty(X)
```

---

# 147. Duty is not motivation

A person may have a duty and lack motivation to comply.

Thus:

```text
Duty != Motivation
```

---

# 148. Duty is not compliance

```text
DutyExists != DutyPerformed
```

---

# 149. Legal duty is not moral duty

```text
LegalDuty != MoralDuty
```

---

# 150. Role duty is not moral duty automatically

A role may impose institutionally recognized obligations while the institution
itself is unjust.

Thus:

```text
RoleDuty != MoralDuty by definition
```

---

# 151. Commitment is not duty

HF10 commitment concerns persistence/policy relation.

Thus:

```text
Commitment != MoralDuty
```

---

# 152. Promise is not expectation only

Promise experiments show behavioral effects cannot always be reduced to changed
payoff expectations attributed to the partner.

Thus:

```text
Promise != MereExpectation
```

---

# 153. Promise is not valid moral obligation by definition

Coercive, impossible, fraudulent or wrongful promises show why promise occurrence and
valid duty must remain separate.

Thus:

```text
PromiseMade != ValidMoralDuty
```

---

# 154. Contract is not moral duty totality

```text
ContractualObligation != MoralObligationTotality
```

---

# 155. Duty conflict is possible

Examples:

```text
promise vs harm prevention
role duty vs rights constraint
legal duty vs moral objection
```

Therefore a duty label does not resolve priority.

---

# 156. ObligationProfile_K

```text
{
  bearer,
  beneficiary/addressee,
  content,
  source: moral/legal/role/promise/contract,
  validity conditions,
  knowledge/acceptance,
  scope,
  conflict,
  excuse/override conditions,
  fulfillment,
  remedy/accountability
}
```

---

# 157. Responsibility is not one relation

HF14 separates:

```text
CausalResponsibility
TaskResponsibility
RoleResponsibility
MoralResponsibility
Blameworthiness
LegalLiability
Accountability
```

---

# 158. Causal responsibility

Working descriptive relation:

```text
CausalContribution_D(A,X)
```

records how A's action/omission influenced outcome X under a causal model.

---

# 159. Causal contribution is not moral responsibility

```text
CausalContribution != MoralResponsibility
```

---

# 160. Moral responsibility is not wrongdoing

An agent can responsibly perform a permissible action.

Thus:

```text
MoralResponsibility != Wrongdoing
```

---

# 161. Wrongdoing is not blameworthiness

Excuses can reduce blame for a wrong action.

Thus:

```text
Wrongdoing != Blameworthiness
```

---

# 162. Blame is not punishment

```text
Blame != Punishment
```

---

# 163. Responsibility is not legal liability

```text
MoralResponsibility != LegalLiability
```

---

# 164. Accountability is not responsibility

An office-holder can owe explanation/review for a system outcome even where personal
moral blame is low.

Thus:

```text
Accountability != MoralResponsibility
```

---

# 165. Responsibility requires a profile

At minimum record:

```text
causal contribution
intent/desire
belief/knowledge
foreseeability
control
available alternatives
coercion/constraint
capacity
role/duty
authority
outcome
attempted prevention/repair
```

---

# 166. Intent is not responsibility totality

```text
Intent != MoralResponsibilityTotality
```

---

# 167. Outcome is not responsibility totality

```text
OutcomeSeverity != MoralResponsibility by definition
```

---

# 168. Foreseeability is not knowledge

```text
Foreseeability != ActualKnowledge
```

---

# 169. Knowledge is not control

An agent can know harm will occur but lack means to prevent it.

Thus:

```text
Knowledge != Control
```

---

# 170. Control is not causation

One can have control authority but never causally intervene, or causally affect an
outcome without broad control.

Thus:

```text
Control != CausalContribution
```

---

# 171. Nominal control is not effective control

AI manual-mode experiments show observers assign more human blame when a takeover
option merely exists, even when the human lacks time or practical ability to use it.

Thus:

```text
NominalControl != EffectiveControl
```

---

# 172. Override availability is not meaningful control

```text
OverrideAvailable != MeaningfulControl
```

retaining HF11 and strengthening it normatively.

---

# 173. Counterfactual control requires realistic accessibility

A theoretical action path that was impossible under latency/information/capability
constraints should not be treated as ordinary effective control.

---

# 174. Coercion is responsibility-relevant

Severe constraint can reduce perceived responsibility.

But experiments also show identification with an action can preserve responsibility
judgments even under strong constraint.

Therefore:

```text
Coercion != ZeroResponsibilityByDefinition
```

---

# 175. Alternative possibilities are not one binary

Record:

```text
physical alternative
informationally available alternative
legally available alternative
practically reachable alternative
socially costly alternative
```

---

# 176. Role is responsibility-relevant but not sufficient

```text
RoleAssignment != MoralResponsibilityByDefinition
```

---

# 177. Authority is responsibility-relevant but not sufficient

```text
DecisionAuthority != MoralResponsibilityTotality
```

---

# 178. Duty violation is responsibility-relevant but not sufficient

Knowledge, capacity, excuse and control still matter.

---

# 179. Negligence differs from intentional wrongdoing

Negligence can involve failure to exercise expected control despite no intent to
harm.

Thus:

```text
Negligence != IntentionalHarm
```

---

# 180. Negligence is not bad outcome only

Hindsight can inflate perceived foreseeability and negligence.

Thus:

```text
BadOutcome != NegligenceProof
```

---

# 181. Omission responsibility requires duty/opportunity analysis

Not acting is not automatically responsible omission.

Thus:

```text
NonAction != ResponsibleOmission by definition
```

---

# 182. Attempted harm can be wrong without realized harm

```text
FailedHarmAttempt can remain Wrongdoing
```

under many judgment systems.

---

# 183. Accidental harm can occur with low blame

```text
HarmOccurred != HighBlame
```

---

# 184. ResponsibilityProfile

```text
{
  actor(s),
  outcome/action,
  causal contribution,
  act/omission,
  intent/desire,
  beliefs/knowledge,
  foreseeability,
  effective control,
  alternatives,
  coercion/constraint,
  capacity,
  role,
  duties,
  decision authority,
  execution authority,
  supervision,
  outcome severity,
  attempt/prevention/repair,
  moral-responsibility judgment,
  blame,
  punishment,
  legal liability,
  accountability relation
}
```

---

# 185. Accountability

Working institutional/normative relation:

```text
Accountability_D(A,X,S)
= structured requirement that A answer for, disclose, justify, review, correct or
  bear specified consequences regarding X within system S
```

---

# 186. Accountability is not blame

```text
Accountability != Blame
```

---

# 187. Accountability is not punishment

```text
Accountability != Punishment
```

---

# 188. Accountability can exist without personal fault

System owners may owe audit/repair even when no individual acted culpably.

Thus:

```text
Accountability != PersonalFaultRequirement
```

---

# 189. Answerability is one accountability component

```text
Answerability != AccountabilityTotality
```

---

# 190. Auditability is not accountability totality

A log can show what happened without assigning who must respond.

Thus:

```text
Auditability != Accountability
```

---

# 191. Sanction is not accountability totality

```text
Sanction != Accountability
```

---

# 192. Repair is accountability-relevant

Restoration, correction and prevention of recurrence can matter separately from
blame/punishment.

---

# 193. AccountabilityProfile

```text
{
  accountable actor/office,
  object/outcome,
  answerability duty,
  evidence/logging,
  review authority,
  appeal,
  correction/remedy,
  sanction relation,
  transparency,
  affected parties,
  temporal horizon,
  closure criteria
}
```

---

# 194. Legitimacy revisited

HF13 separated:

```text
PerceivedLegitimacy
Legal/InstitutionalValidity
NormativeLegitimacy
```

HF14 owns the third as a normative question.

---

# 195. Normative legitimacy is not one empirical state

Working meta-definition:

```text
NormativeLegitimacy_F(Institution/Authority/Rule)
= justified entitlement to exercise specified authority/coercion under normative
  framework F
```

The framework must be declared.

---

# 196. Normative legitimacy is not perceived legitimacy

```text
PerceivedLegitimacy != NormativeLegitimacy
```

---

# 197. Normative legitimacy is not legal validity

```text
LegalValidity != NormativeLegitimacy
```

---

# 198. Normative legitimacy is not compliance

```text
Compliance != NormativeLegitimacy
```

---

# 199. Normative legitimacy is not democratic selection alone

Election/participation may be normatively relevant, but:

```text
MajoritySelection != NormativeLegitimacyByDefinition
```

---

# 200. Normative legitimacy is not good outcome alone

```text
BeneficialOutcome != NormativeLegitimacy
```

---

# 201. Normative legitimacy is not fair process alone

```text
FairProcedure != NormativeLegitimacyGuarantee
```

---

# 202. Procedure can matter independently of outcome

Human experiments show procedural fairness alters reactions/responsibility
attributions even holding outcome favorability as a separate variable.

Thus procedure is not reducible to outcome.

---

# 203. Outcome can matter independently of procedure

Thus legitimacy analysis needs both.

---

# 204. Rights constraints can matter independently of welfare

A policy can increase aggregate welfare while violating a rights constraint under a
rights-based framework.

Thus:

```text
WelfareImprovement != RightsCompatibility
```

---

# 205. Welfare and fairness can conflict

Resource-allocation experiments directly show participants trading total efficiency
against equity.

Thus:

```text
WelfareCriterion != FairnessCriterion
```

---

# 206. Fairness and rights can conflict

Equal distribution can conflict with a prior claim-right or entitlement under some
frameworks.

Thus:

```text
FairnessCriterion != RightsCriterion
```

---

# 207. Rights can conflict with rights

Therefore:

```text
RightsPresent != DecisionSolved
```

---

# 208. Legitimacy requires explicit conflict resolution

When frameworks conflict, HF14 records the conflict rather than hiding it in one
score.

---

# 209. LegitimacyProfile_F

```text
{
  authority/institution/rule,
  claimed scope,
  authority source,
  procedure,
  participation/voice,
  rights constraints,
  welfare effects,
  distributive fairness,
  coercion/power,
  transparency,
  contestability,
  appeal/exit,
  accountability/remedy,
  affected parties,
  minority/worst-off effects,
  uncertainty,
  framework F,
  unresolved criterion conflicts
}
```

---

# 210. Human×AI responsibility must be role-decomposed

At minimum separate:

```text
Principal
GoalSetter
AuthoritySource
DataProvider
ModelBuilder
Planner
Recommender
Executor
Supervisor
Verifier
OverrideHolder
InstitutionOwner
```

---

# 211. AI execution is not AI responsibility by definition

```text
AIExecution != AIMoralResponsibility
```

---

# 212. Human authorization is not Human total responsibility by definition

```text
HumanAuthorization != HumanMoralResponsibilityTotality
```

though it can be highly relevant.

---

# 213. Human-in-loop is not Human responsibility by default

```text
HumanInLoop != HumanResponsibilityByDefault
```

---

# 214. Manual override availability is not meaningful control

Retain:

```text
ManualOverrideAvailable != MeaningfulControl
```

with direct AI blame evidence.

---

# 215. Blame attribution is not responsibility truth

AI mind-perception experiments show anthropomorphic mind attribution can shift blame
toward AI and away from human stakeholders.

Thus:

```text
ObservedBlameAllocation != ResponsibilityTruth
```

---

# 216. Anthropomorphic mind attribution is not moral agency

```text
AnthropomorphicMindAttribution != MoralAgency
```

---

# 217. Perceived agency is not effective control

```text
PerceivedAgency != EffectiveControl
```

---

# 218. Model autonomy is not moral authority

```text
OperationalAutonomy != MoralAuthority
```

---

# 219. AI competence is not authority

Retain HF13:

```text
AIEpistemicContribution != AIDecisionAuthority
```

---

# 220. Formal authorization is not moral permission

```text
FormalAuthorization != MoralPermission
```

---

# 221. Successful outcome is not ethical process

```text
SuccessfulOutcome != EthicalProcess
```

---

# 222. Ethical process is not successful outcome guarantee

```text
EthicalProcess != SuccessfulOutcomeGuarantee
```

---

# 223. Faithful execution is not normative correctness

Retain:

```text
InstitutionalFidelity != NormativeCorrectness
```

---

# 224. Human×AI responsibility can be distributed without becoming unowned

Distributed contribution requires explicit mapping rather than saying:

```text
"the system did it"
```

---

# 225. Automation can create responsibility gaps as measurement failures

A perceived gap may arise because existing categories fail to capture distributed
control/knowledge/authority.

HF14 first attempts decomposition before declaring metaphysical absence of
responsibility.

---

# 226. Responsibility gap is not automatically AI responsibility

```text
NoObviousHumanBlameTarget != AIMoralResponsibility
```

---

# 227. Responsibility gap is not automatically no accountability

An institution can preserve audit, answerability and remedy obligations even if
individual moral blame is uncertain.

Thus:

```text
UncertainMoralBlame != NoAccountability
```

---

# 228. Human×AI ResponsibilityProfile

```text
{
  normative target/outcome,
  principal/goal setter,
  authority source,
  model/data builders,
  planner/recommender,
  executor,
  supervisor/verifier,
  override holder,
  causal contributions,
  knowledge/foreseeability,
  effective control/latency,
  role duties,
  institutional obligations,
  system constraints,
  preventability,
  repair/remedy,
  moral-responsibility hypotheses,
  legal-liability status,
  accountability owner
}
```

---

# 229. Reflexivity is normative too

Calling someone:

```text
responsible
untrustworthy
undeserving
rights-incompetent
```

can change how institutions treat them.

Thus:

```text
NormativeClassification
may become
SocialIntervention
```

---

# 230. Blame can change future opportunity

Punishment, stigma and exclusion can create new causal pathways.

So responsibility measurement is not socially inert.

---

# 231. Rights attribution can alter capability

Granting/withholding rights changes option sets.

Thus:

```text
RightsJudgment_t
→ CapabilitySet_{t+1}
```

---

# 232. Agency judgment can alter rights judgment

Experiments on mental-impairment defenses show lower perceived agency can reduce
blame yet also reduce some rights attributed to the person through dangerousness
judgments.

Therefore:

```text
LowerResponsibilityJudgment
can coexist with
LowerRightsAttribution
```

---

# 233. This creates a major warning

Using low agency to excuse blame can inadvertently be used to deny standing/rights.

Thus:

```text
LowMoralAgency != LowMoralStanding by definition
```

---

# 234. Moral agency and moral patiency are distinct

Mind-perception research separates perceived:

```text
Agency
Experience
```

and these predict different moral judgments.

---

# 235. Moral agency

Working unresolved neighbor:

```text
MoralAgency_D
= capacity/status relevant to being held morally responsible for conduct in D
```

HF14 does not finalize its bearer conditions.

---

# 236. Moral patiency

Working unresolved neighbor:

```text
MoralPatiency_D
= capacity/status relevant to being a bearer of morally considerable harm/benefit or
  claims in D
```

HF14 does not finalize its bearer conditions.

---

# 237. Moral agency is not moral patiency

```text
MoralAgency != MoralPatiency
```

Infants or severely impaired humans are decisive conceptual pressure tests.

---

# 238. Responsibility capacity is not rights capacity

```text
ResponsibilityCapacity != RightsHoldingCapacity
```

---

# 239. Experience attribution is not agency attribution

```text
PerceivedExperience != PerceivedAgency
```

---

# 240. Perceived experience can influence moral standing judgments

Robot studies show attributed experiential mental life tracks moral-standing
judgments across development.

This does not prove robot sentience or actual moral standing.

---

# 241. Perceived moral standing is not actual moral standing

```text
PerceivedMoralStanding != MoralStandingTruth
```

---

# 242. Human category membership cannot be the only unresolved criterion

HF1 intentionally did not define rights/personhood by current cognitive agency.

HF14 now encounters non-human animals, impaired humans, future humans and AI as
boundary cases requiring explicit standing criteria.

---

# 243. Rights language silently presupposes a holder

Every rights claim needs:

```text
Who/what can be the holder?
```

HF14 cannot answer this merely by refining right types.

---

# 244. Harm language silently presupposes a subject of harm

Every welfare/harm claim needs:

```text
Who/what can be better or worse off?
```

---

# 245. Welfare language silently presupposes interests or welfare capacity

A rock and a child cannot simply be inserted into the same welfare function without
a theory of bearer/standing.

---

# 246. Responsibility language silently presupposes agency capacity

A storm can cause harm but is not ordinarily treated as a moral agent.

Thus:

```text
CausalAgent != MoralAgent
```

---

# 247. Dignity introduces another standing route

Some normative frameworks ground protection in dignity/status rather than
experienced welfare alone.

HF14 therefore cannot collapse standing into sentience by fiat.

---

# 248. Vulnerability introduces another standing-relevant dimension

Capacity to be harmed, exploited or dominated may matter independently of agency.

Again, no final criterion is chosen here.

---

# 249. Interests introduce another candidate relation

But:

```text
Interest != Preference
Interest != Right
```

and HF14 does not finalize which entities have morally relevant interests.

---

# 250. Scope of concern is the repeated residual

Across:

```text
rights
harm
welfare
responsibility
AI
animals
impaired humans
future persons
```

HF14 repeatedly must ask:

> **Who or what belongs inside the moral domain, in what role, and on what basis?**

This is not another fairness or responsibility variable.

---

# 251. Cross-context falsifier matrix

| Case | Naive collapse attacked | HF14 surviving distinction |
|---|---|---|
| failed intentional harm judged wrong despite no outcome | wrongdoing = realized harm | intent/wrongdoing and outcome separate |
| accidental harm forgiven more than intentional harm | harm = blame | harm occurrence and blameworthiness separate |
| foreseeability changes blame independent of intent | intent = responsibility | foreseeability is separate input |
| bad outcome increases hindsight negligence | outcome = ex ante foreseeability | ex post outcome distorts responsibility evidence |
| coercion reduces but does not uniformly erase responsibility | no alternative = zero responsibility | control, identification and constraints are multidimensional |
| psychological humiliation/fear judged harmful | harm = physical damage | psychological harm is distinct |
| longer painful episode chosen when ending improves | choice = welfare | decision/remembered/experienced utility dissociate |
| life satisfaction separates from affect | well-being = happiness scalar | welfare profile is multidimensional |
| patients and public value health states differently | public preference = patient welfare | standpoint/adaptation matter |
| achievement inequality accepted, luck inequality rejected | fairness = equality | merit/source of inequality matters |
| objective need changes allocations | fairness = equal split | need is independent distributive criterion |
| reward destroyed rather than unequal allocation | fairness = efficiency | equity can conflict with total welfare |
| random device reduces reluctance to inequity | outcome fairness only | responsibility/procedure changes fairness response |
| fair procedure changes reactions at same outcome | justice = outcome | procedure is independent dimension |
| legal rule judged unjust | law = morality | legal validity and moral judgment separate |
| promise effect exceeds partner-expectation effect | duty = social expectation | promissory relation has additional normative force in behavior |
| Hohfeld claim right versus liberty | right = permission | right types have distinct correlatives |
| manual mode increases human blame without usable control | nominal control = responsibility | effective control must be measured |
| mind attribution shifts blame toward AI | blame = responsibility truth | anthropomorphism affects attribution |
| mental-impairment defense lowers blame but also rights | low agency = low standing | moral agency and moral patiency/rights separate |
| robot experiential mind attribution predicts standing judgment | standing = biological category only | perceived experience is standing-relevant but not truth |

---

# 252. Competing normative model families

## M1 — morality as social conformity

### Failure

HF13 established harmful norms and unjust laws.

**Disposition:** reject categorically.

## M2 — morality as preference satisfaction

### Failure

Preferences can conflict, adapt, be uninformed, and dissociate from experienced
welfare or rights.

**Disposition:** retain preference as one evaluative surface, reject as universal
ontology.

## M3 — morality as aggregate welfare maximization

### Strength

Makes outcome tradeoffs explicit.

### Failure as complete foundation

Rights, fairness, distribution and procedure can independently matter under major
normative frameworks and human judgments.

**Disposition:** retain as normative model family, not foundation truth.

## M4 — morality as equality

### Failure

Need, contribution, luck, merit, desert and efficiency produce justified-inequality
judgments in many cases.

**Disposition:** reject equality as fairness totality.

## M5 — morality as fairness

### Failure

Rights, harm, welfare, duty and legitimacy are not reducible to allocation fairness.

**Disposition:** fairness is one normative family.

## M6 — morality as law

### Failure

Legal validity and moral rightness dissociate.

**Disposition:** reject.

## M7 — rights as generic permissions

### Failure

Claim, liberty, power and immunity have different relational structures.

**Disposition:** use typed rights.

## M8 — duties as expectations

### Failure

Promises affect behavior beyond attributed expectations; legal/social expectations
can be rejected as morally invalid.

**Disposition:** separate expectation and obligation source.

## M9 — responsibility as causation

### Failure

Intent, knowledge, foreseeability, control, coercion, duty and role all matter.

**Disposition:** reject.

## M10 — responsibility as intent

### Failure

Negligence and foreseeable unintended harm.

**Disposition:** reject intent-only model.

## M11 — responsibility as bad outcome

### Failure

Failed attempts and accidental harms.

**Disposition:** reject.

## M12 — responsibility as nominal control

### Failure

AI manual-mode falsifier.

**Disposition:** require effective control and reachable alternatives.

## M13 — accountability as blame/punishment

### Failure

Institutions can owe answerability, audit and remedy without personal culpability.

**Disposition:** separate.

## M14 — legitimacy as good outcomes

### Failure

Unfair procedure, rights violations and coercion.

**Disposition:** reject outcome-only legitimacy.

## M15 — legitimacy as fair procedure

### Failure

A fair procedure can produce harmful or rights-violating outcomes.

**Disposition:** retain procedure as one criterion.

## M16 — legitimacy as democratic popularity

### Failure

Majorities can support unjust norms/rules.

**Disposition:** separate perceived/democratic support from normative legitimacy.

## M17 — one hidden weighted moral score

### Failure

Weights themselves are normative commitments and can hide rights/fairness/welfare
conflicts.

**Disposition:** require criterion transparency and explicit uncertainty.

## M18 — AI execution transfers responsibility to AI

### Failure

Execution, authority, control, knowledge and moral agency are distinct.

**Disposition:** role-decompose Human×AI systems.

## M19 — human-in-loop guarantees human responsibility

### Failure

Nominal override may be unusable; real control/knowledge may lie elsewhere.

**Disposition:** reject label-only responsibility.

## M20 — moral agency determines moral standing

### Failure

Infants, impaired humans and moral-patient cases; mental-impairment evidence shows
agency reductions can lower blame while rights questions remain.

**Disposition:** reject as complete standing rule; exposes next boundary.

## M21 — sentience/experience alone determines standing

### Strength

Experience is strongly relevant to many harm/patiency judgments.

### Why HF14 does not freeze it

Rights/dignity/interests/future persons and uncertain machine/animal cases require a
separate standing analysis.

**Disposition:** candidate model, not HF14 conclusion.

---

# 253. HF14 anti-laws

## Moral judgment / deontic structure

1. `MoralJudgment != NormativeTruth`.
2. `Preference != MoralJudgment`.
3. `MoralJudgment != SocialNormBelief`.
4. `MoralJudgment != LegalStatusJudgment`.
5. `MoralEmotion != MoralJudgment`.
6. `Wrongness != Blameworthiness`.
7. `Blameworthiness != PunishmentAppropriateness`.
8. `Permissible != Good`.
9. `NotRequired != Forbidden`.
10. `Permitted != Recommended`.
11. `Intent != MoralJudgmentTotality`.
12. `Wrongdoing != SuccessfulCausationRequirement`.
13. `Foreseeability != Intent`.
14. `ExPostOutcomeKnowledge != ExAnteForeseeability`.
15. `OutcomeDifference != MoralResponsibilityDifferenceByDefinition`.
16. `ActionOmissionJudgmentDifference != NormativePrincipleByDefault`.
17. `ObservedJudgmentPattern != MoralTruth`.
18. `MoralJudgmentMechanism_D != MoralJudgmentMechanism_E`.

## Harm

19. `Pain != Harm`.
20. `NoPain != NoHarm`.
21. `PhysicalDamage != HarmExperience`.
22. `PsychologicalHarm != PhysicalDamage`.
23. `RiskOfHarm != RealizedHarm`.
24. `ExpectedHarm != RealizedHarm`.
25. `HarmSeverity != Wrongness`.
26. `Wrongness != HarmMagnitudeOnly`.
27. `PreferenceFrustration != Harm by definition`.
28. `RightsViolation != HarmExperience`.
29. `CurrentValence != WholeHarmTrajectory`.

## Welfare

30. `Choice != ExperiencedWelfare`.
31. `RememberedUtility != ExperiencedUtility`.
32. `PreferenceSatisfaction != WelfareTotality`.
33. `CurrentPreference != ContextIndependentWelfareMetric`.
34. `PopulationPreference != TargetExperiencedWelfare`.
35. `LifeSatisfaction != PositiveAffect`.
36. `PositiveAffect != -NegativeAffect`.
37. `ResourceAmount != Welfare`.
38. `CapabilitySet != CurrentFunctioning`.
39. `CurrentFunctioning != OpportunityFreedom`.
40. `Welfare_D != Welfare_E`.
41. `AggregateWelfare != WelfareDistribution`.

## Fairness / justice

42. `Equality != Fairness`.
43. `Inequality != Unfairness`.
44. `EqualResources != EqualWelfare`.
45. `EqualOutcome != EqualOpportunity`.
46. `Equity != Equality`.
47. `Need != Merit`.
48. `NeedPrinciple != EqualityPrinciple`.
49. `MeritEvidence != DesertConclusion`.
50. `Effort != Desert`.
51. `OutcomeAchievement != Desert`.
52. `PriorityToWorseOff != Equality`.
53. `Sufficiency != Equality`.
54. `Efficiency != Fairness`.
55. `Fairness != AggregateWelfareMaximization`.
56. `Fairness != NeedPrincipleOnly`.
57. `Fairness != MeritPrincipleOnly`.
58. `PopulationFairnessJudgment != OneSharedFairnessRule`.
59. `FairnessJudgment != NormativeFairnessTruth`.
60. `ProceduralFairness != OutcomeFairness`.
61. `BeneficialOutcome != FairProcedure`.
62. `FairProcedure != BeneficialOutcomeGuarantee`.
63. `Justice != Equality`.
64. `Justice != FairnessOnly`.
65. `Justice != LegalValidity`.
66. `Justice != AggregateWelfareMaximization`.
67. `StableInstitution != JustInstitution`.
68. `NormativeDisagreement != EmpiricalErrorOnly`.
69. `PerfectFacts != OneNormativeAnswer by definition`.
70. `EmpiricalFit(F) != NormativeTruth(F)`.
71. `MoralIntuition != NormativeProof`.
72. `Deliberation != TruthGuarantee`.
73. `MoralConsensus != MoralTruth by definition`.
74. `NormativeDisagreement != NormativeNihilismProof`.

## Rights / duties

75. `ClaimRight != Liberty`.
76. `Right != Permission`.
77. `LegalPower != PhysicalCapability`.
78. `LegalImmunity != PhysicalInvulnerability`.
79. `LegalRight != MoralRight`.
80. `MoralRight != CurrentInstitutionalPermission`.
81. `Right != Capability`.
82. `Capability != Right`.
83. `Interest != Right by definition`.
84. `Right != AbsoluteTrump by definition`.
85. `OthersExpect(X) != Duty(X)`.
86. `Duty != Motivation`.
87. `DutyExists != DutyPerformed`.
88. `LegalDuty != MoralDuty`.
89. `RoleDuty != MoralDuty by definition`.
90. `Commitment != MoralDuty`.
91. `Promise != MereExpectation`.
92. `PromiseMade != ValidMoralDuty`.
93. `ContractualObligation != MoralObligationTotality`.

## Responsibility / accountability

94. `CausalContribution != MoralResponsibility`.
95. `MoralResponsibility != Wrongdoing`.
96. `Wrongdoing != Blameworthiness`.
97. `Blame != Punishment`.
98. `MoralResponsibility != LegalLiability`.
99. `Accountability != MoralResponsibility`.
100. `Intent != MoralResponsibilityTotality`.
101. `OutcomeSeverity != MoralResponsibility by definition`.
102. `Foreseeability != ActualKnowledge`.
103. `Knowledge != Control`.
104. `Control != CausalContribution`.
105. `NominalControl != EffectiveControl`.
106. `OverrideAvailable != MeaningfulControl`.
107. `Coercion != ZeroResponsibilityByDefinition`.
108. `RoleAssignment != MoralResponsibilityByDefinition`.
109. `DecisionAuthority != MoralResponsibilityTotality`.
110. `Negligence != IntentionalHarm`.
111. `BadOutcome != NegligenceProof`.
112. `NonAction != ResponsibleOmission by definition`.
113. `HarmOccurred != HighBlame`.
114. `Accountability != Blame`.
115. `Accountability != Punishment`.
116. `Accountability != PersonalFaultRequirement`.
117. `Answerability != AccountabilityTotality`.
118. `Auditability != Accountability`.
119. `Sanction != Accountability`.

## Legitimacy

120. `PerceivedLegitimacy != NormativeLegitimacy`.
121. `LegalValidity != NormativeLegitimacy`.
122. `Compliance != NormativeLegitimacy`.
123. `MajoritySelection != NormativeLegitimacyByDefinition`.
124. `BeneficialOutcome != NormativeLegitimacy`.
125. `FairProcedure != NormativeLegitimacyGuarantee`.
126. `WelfareImprovement != RightsCompatibility`.
127. `WelfareCriterion != FairnessCriterion`.
128. `FairnessCriterion != RightsCriterion`.
129. `RightsPresent != DecisionSolved`.

## Human×AI

130. `AIExecution != AIMoralResponsibility`.
131. `HumanAuthorization != HumanMoralResponsibilityTotality`.
132. `HumanInLoop != HumanResponsibilityByDefault`.
133. `ManualOverrideAvailable != MeaningfulControl`.
134. `ObservedBlameAllocation != ResponsibilityTruth`.
135. `AnthropomorphicMindAttribution != MoralAgency`.
136. `PerceivedAgency != EffectiveControl`.
137. `OperationalAutonomy != MoralAuthority`.
138. `AIEpistemicContribution != AIDecisionAuthority`.
139. `FormalAuthorization != MoralPermission`.
140. `SuccessfulOutcome != EthicalProcess`.
141. `EthicalProcess != SuccessfulOutcomeGuarantee`.
142. `InstitutionalFidelity != NormativeCorrectness`.
143. `NoObviousHumanBlameTarget != AIMoralResponsibility`.
144. `UncertainMoralBlame != NoAccountability`.

## Standing residual

145. `LowMoralAgency != LowMoralStanding by definition`.
146. `MoralAgency != MoralPatiency`.
147. `ResponsibilityCapacity != RightsHoldingCapacity`.
148. `PerceivedExperience != PerceivedAgency`.
149. `PerceivedMoralStanding != MoralStandingTruth`.
150. `CausalAgent != MoralAgent`.
151. `Interest != Preference`.
152. `Interest != Right`.

---

# 254. Minimum HF14 grammar

```text
World / Event / Policy / Institution
                ↓
          Empirical model
   ┌────────────┼─────────────┐
   ↓            ↓             ↓
Consequences   Agency      Social/institutional facts
   ↓         mental states     ↓
Harm/Welfare  control       law/authority/norm
   ↓            ↓             ↓
   └──────── Normative candidate reasons ───────┐
                                                ↓
                                  NormativeFramework F
                                  /      |       \
                               welfare fairness rights
                                  \      |       /
                              procedure / duty / desert
                                       ↓
                            Deontic/evaluative judgment
                       permitted / required / forbidden
                              good / bad / better
                                       ↓
                    responsibility / rights / legitimacy
                                       ↓
                         decision / action / institution
                                       ↓
                          outcomes + new evidence
                                       ↺
```

Responsibility subgraph:

```text
Outcome
  ↑
causal contribution
  ↑
action / omission
  +
intent / belief / knowledge
  +
foreseeability
  +
effective control / alternatives / coercion
  +
role / duty / authority
  ↓
ResponsibilityProfile
  ├─ causal responsibility
  ├─ moral responsibility
  ├─ blameworthiness
  ├─ punishment
  ├─ legal liability
  └─ accountability
```

Rights subgraph:

```text
Legal/Moral system K
        ↓
rights relation
 ├─ claim ↔ duty
 ├─ liberty ↔ no-right
 ├─ power ↔ liability
 └─ immunity ↔ disability
        ↓
practical exercise depends on capability/institution
```

---

# 255. Reconnection to HF13

HF13 tells us:

```text
what is socially stabilized
```

HF14 tells us that this is only normative evidence/input, never automatic
justification.

Retain:

```text
SocialNorm != MoralNorm
LegalValidity != MoralRightness
Power != Legitimacy
InstitutionExists != InstitutionLegitimate
```

---

# 256. Reconnection to HF12

Shared goals/cooperation do not settle moral status.

```text
SharedGoal != SharedMoralJustification
Cooperation != NormativeGood
```

---

# 257. Reconnection to HF11

Effective control and reachable alternatives matter for responsibility.

Thus:

```text
ActionControlProfile
feeds
ResponsibilityProfile
```

but does not determine it alone.

---

# 258. Reconnection to HF10

Decision quality has separate:

```text
epistemic quality
instrumental quality
normative quality
```

Thus:

```text
OptimalUnderUtilityModel != MorallyPermissible by definition
```

---

# 259. Reconnection to HF9

Normative reasoning is still inference over representations, but normative premises
cannot be smuggled in as empirical facts.

Thus:

```text
ValidInference + False/UnjustifiedNormativePremise
!= NormativeCorrectness
```

---

# 260. Reconnection to HF8

Belief about moral truth is not moral truth.

```text
Believes(Ought X) != Ought X
```

---

# 261. Reconnection to HF7

Remembered harm, promise or precedent can be inaccurate.

```text
MoralMemoryReport != HistoricalNormativeFact
```

---

# 262. Reconnection to HF6

Moral preferences/judgments can change through development and social history.

Change does not by itself prove moral progress or decline.

```text
MoralJudgmentChange != MoralProgressByDefinition
```

---

# 263. Reconnection to HF5

Pain, fatigue, threat and stress are welfare/harm-relevant states but are not
complete normative verdicts.

```text
PainEvidence != WrongnessVerdict
```

---

# 264. Reconnection to HF4

Values/preferences motivate action but:

```text
EndorsedValue != MoralTruth
Preference != Right
```

---

# 265. Reconnection to HF3/HF2

Confidence, salience and emotional intensity can alter moral judgment without
constituting truth.

```text
MoralConfidence != MoralCorrectness
EmotionalIntensity != HarmMagnitude
```

---

# 266. Reconnection to HF1

HF1 deliberately separated:

```text
HumanIndividual
Person
Agent
LegalPerson
```

HF14 now shows why that was necessary:

```text
MoralStanding
MoralAgency
RightsHolding
Responsibility
```

cannot be inferred from one identity label.

---

# 267. Normativity firewall for Ordivon

Any normative output should separate at least:

```text
Empirical facts
Affected subjects
Harm/welfare evidence
Rights/duties
Fairness/distribution
Responsibility/control
Legal/institutional status
Candidate normative framework
Conflict/uncertainty
Decision authority
```

---

# 268. Do not silently optimize one moral proxy

Examples of forbidden collapses:

```text
maximize happiness only
maximize preference satisfaction only
maximize equality only
maximize compliance only
maximize legal validity only
maximize user approval only
```

unless the application explicitly chooses that criterion and accepts its limits.

---

# 269. Higher-order constraints must remain visible

An instruction can be:

```text
formally authorized
instrumentally useful
popular
```

and still conflict with rights/safety/moral constraints.

Thus:

```text
Authorization != EthicalClearance
```

---

# 270. Refusal can be normatively structured

An Agent refusing an instruction should not merely say `policy says no` when the
actual justification is a higher-order rights/safety constraint.

Relevant objects include:

```text
authority source
instruction scope
harm risk
rights constraint
duty conflict
uncertainty
appeal/escalation path
```

---

# 271. But refusal authority is itself normative/institutional

An Agent does not gain unrestricted moral sovereignty merely because it can detect a
conflict.

Thus:

```text
SafetyConcern != UnlimitedOverrideAuthority
```

---

# 272. Normative uncertainty should increase reversibility where possible

This is a decision principle candidate, not moral truth:

when severe/irreversible harm and deep normative uncertainty coexist, preserving
reversibility/appeal can be instrumentally robust across frameworks.

HF14 records the design inference without elevating it to universal moral law.

---

# 273. What HF14 does not establish

HF14 does not establish:

- one final metaethical theory of moral truth;
- that moral judgment is objective or subjective in one universal sense;
- that all harms can be reduced to pain or preference frustration;
- one scalar welfare measure;
- that utility, happiness, life satisfaction or preference satisfaction is welfare
  totality;
- that fairness is equality;
- that inequality is injustice;
- that need, merit, desert or priority always dominate one another;
- one complete theory of justice;
- that rights are absolute trumps;
- that legal rights exhaust moral rights;
- one source of moral duty;
- that promises always generate valid obligations;
- one necessary-and-sufficient condition for moral responsibility;
- that alternate possibilities are necessary for all responsibility;
- that intent is necessary for all blame or liability;
- that causal contribution is sufficient for responsibility;
- that accountability requires blame;
- that democratic procedure or beneficial outcomes alone create legitimacy;
- that AI currently has or lacks moral agency/standing as a foundation fiat;
- that anthropomorphic perception is evidence of actual machine consciousness;
- that Human biological membership is the only possible basis of moral standing;
- that sentience alone is the final standing criterion.

---

# 274. The repeated residual HF14 cannot finish

HF14 can type a right, harm, welfare state, duty and responsibility relation.

But each repeatedly asks for a **bearer condition**:

```text
Who can be harmed?
Who can have welfare?
Who can hold a claim-right?
Who deserves direct moral consideration?
Who can bear duties?
Who can be blameworthy?
Who counts when aggregating welfare?
```

The answers do not line up on one axis.

An infant may have strong moral claims while weak responsibility capacity.

A corporation may possess legal rights/powers while lacking ordinary human
experience.

An animal may have experience and welfare without human-like institutional agency.

An AI may display planning and language while its experience/interests remain
uncertain.

This is not a minor edge case.

It is the standing boundary hidden inside every normative relation.

---

# 275. Agency and experience dissociate

Primary mind-perception work identifies separable perceived dimensions of agency and
experience that predict different moral judgments.

Therefore:

```text
AgencyCapacity != ExperienceCapacity
```

---

# 276. Moral typecasting is evidence of cognitive coupling, not ontology

Humans tend to perceive moral agents and moral patients as contrasting roles.

But:

```text
PerceivedAgentPatientTradeoff != ActualMoralStandingStructure
```

---

# 277. Reduced agency can lower blame while increasing rights exclusion

Mental-impairment experiments are a decisive falsifier for:

```text
MoralAgency = MoralStanding
```

because reduced agency lowered responsibility/blame yet could lead to fewer rights
through increased dangerousness perceptions.

---

# 278. Robot standing judgments track attributed experiential mind

Developmental work finds robot moral-standing judgments vary with attributed
experiential mental life.

Again:

```text
PerceivedExperience → StandingJudgment
```

is an empirical causal relation, not proof of actual sentience or standing.

---

# 279. Moral standing needs its own foundation

HF14 therefore selects:

# HF15 — Moral Standing, Moral Agency, Moral Patienthood, Sentience, Interests, Vulnerability, Dignity and Scope of Concern

HF15 must ask what makes an entity:

```text
morally considerable
capable of welfare/harm
eligible to hold claims/rights
eligible to bear duties/responsibility
inside or outside a scope of concern
```

without presupposing that all these conditions coincide.

---

# 280. HF15 starting questions

1. What is moral standing relative to legal personhood, social recognition and
   biological species membership?
2. What is moral patienthood relative to capacity for experience, welfare, interests,
   vulnerability and rights?
3. What is moral agency relative to general agency, intentional action,
   understanding, control and responsibility capacity?
4. Can moral agency and moral patiency vary independently?
5. What is sentience relative to consciousness, valenced experience and report?
6. What is an interest relative to preference, goal, need, welfare and capability?
7. Can an entity have interests without current preferences or reports?
8. What is vulnerability relative to dependence, powerlessness and capacity for
   harm?
9. What is dignity relative to welfare, autonomy, status and rights?
10. How should infants, severe cognitive impairment, nonhuman animals, organizations,
    future persons and artificial systems pressure-test standing criteria?
11. How should uncertainty about sentience/standing affect action without treating
    uncertainty as proof either way?
12. How do legal standing and moral standing interact without collapsing?
13. What evidence could justify changing the moral scope of concern?
14. What next boundary emerges after standing/bearer conditions are rebuilt?

---

# 281. Candidate HF15 falsifiers

- infant/high-rights case with low responsibility capacity;
- severe mental impairment lowering blame without eliminating protection claims;
- temporary unconsciousness/coma with persistent rights;
- nonhuman animal pain/learning without human language;
- corporation/legal person with rights/powers but no established phenomenal
  experience;
- future-person harms where target does not yet exist at action time;
- robot/AI high perceived agency but uncertain experience;
- robot/AI social appearance shifting standing judgments without evidence of
  sentience;
- systems with expressed preferences but uncertain welfare capacity;
- sentient target with little planning/agency;
- highly capable agent with no verified sentience;
- vulnerability/dependence generating protection claims without reciprocal duty
  capacity;
- legal recognition changing while underlying welfare/experience evidence is held
  constant.

---

# 282. Do not precommit

HF14 does not establish that HF15 should conclude:

- only humans have moral standing;
- all living things have equal standing;
- sentience is sufficient for every right;
- agency is necessary for rights;
- language is necessary for interests;
- intelligence determines moral worth;
- legal personhood implies sentience;
- corporations have or lack moral standing in the same way as humans;
- current AI systems are conscious or non-conscious by fiat;
- behavioral self-report proves machine sentience;
- uncertainty about standing requires either full inclusion or full exclusion;
- dignity is reducible to welfare;
- vulnerability alone determines rights.

---

# 283. Stop rule

Do not schedule HF16 now.

HF15 must expose a repeated neighboring distinction whose absence creates category
failures across materially different bearer/standing cases.

---

# 284. HF14 synthesis

HF14 began with:

```text
Can != May != Ought
```

and found that `ought` itself is not one scalar.

The surviving structure is:

```text
MoralJudgment != NormativeTruth
Wrongness != Blame != Punishment
Permissible != Good

Pain != Harm
Risk != RealizedHarm
Harm != Wrongness

Choice != Welfare
Preference != WelfareTotality
LifeSatisfaction != Affect
Resources != Capability != Functioning

Equality != Fairness
Equity != Equality
Need != Merit != Desert
Fairness != Efficiency != Welfare
ProceduralFairness != OutcomeFairness
Justice != Equality != Law != WelfareMaximization

ClaimRight != Liberty != Power != Immunity
LegalRight != MoralRight
Right != Capability

SocialExpectation != Duty
LegalDuty != MoralDuty
Promise != MereExpectation
PromiseMade != ValidMoralDuty

CausalContribution != MoralResponsibility
Wrongdoing != Blameworthiness
Responsibility != Liability != Accountability
NominalControl != EffectiveControl

PerceivedLegitimacy != LegalValidity != NormativeLegitimacy
BeneficialOutcome != LegitimateProcess
FairProcedure != LegitimateOutcomeGuarantee

AIExecution != AIMoralResponsibility
HumanInLoop != HumanResponsibilityByDefault
FormalAuthorization != MoralPermission
ObservedBlameAllocation != ResponsibilityTruth
```

Yet every harm, welfare, rights and responsibility relation still requires a bearer:

```text
Who can suffer?
Who can be better or worse off?
Who can hold rights?
Who can owe duties?
Who can be responsible?
Who belongs in the moral scope?
```

That repeated residual is the HF15 moral-standing boundary.
