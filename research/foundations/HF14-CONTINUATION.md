---
schema_version: 1
id: human.foundations.hf14.continuation
title: Human Foundations Continuation after HF14
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
summary: Exact continuation after HF14. HF14 reconstructs normative evaluation by separating moral judgment/truth, harm/risk, welfare surfaces, equality/equity/need/merit/desert/fairness/justice, typed rights and duties, causal/moral/legal responsibility and accountability, normative legitimacy and Human–AI responsibility. Its repeated unresolved boundary is the bearer and scope question: moral standing, moral agency, moral patienthood, sentience, interests, vulnerability, dignity and scope of concern.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.foundations.hf14
  - human.foundations.hf14.sources
---
# Human Foundations Continuation after HF14

## HF14 completed result

HF14 begins from HF13's:

```text
Can != May != Ought
```

and establishes that `ought` cannot itself be represented as one undifferentiated
scalar.

Minimum grammar:

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

## Moral judgment / truth

Use:

```text
MoralJudgment_K(H,X,t,C)
= Human H's current moral evaluation of X on judgment surface K
```

Retain:

```text
MoralJudgment != NormativeTruth
Preference != MoralJudgment
MoralJudgment != SocialNormBelief
MoralJudgment != LegalStatusJudgment
MoralEmotion != MoralJudgment
Wrongness != Blameworthiness
Blameworthiness != PunishmentAppropriateness
Permissible != Good
NotRequired != Forbidden
Permitted != Recommended
Intent != MoralJudgmentTotality
Wrongdoing != SuccessfulCausationRequirement
Foreseeability != Intent
ExPostOutcomeKnowledge != ExAnteForeseeability
OutcomeDifference != MoralResponsibilityDifferenceByDefinition
ActionOmissionJudgmentDifference != NormativePrincipleByDefault
ObservedJudgmentPattern != MoralTruth
MoralJudgmentMechanism_D != MoralJudgmentMechanism_E
```

Intent, outcome, causation and foreseeability are distinct judgment inputs. Human
judgment is empirical evidence about moral cognition, never self-authenticating moral
truth.

## Harm

Separate:

```text
HarmfulEvent
HarmfulStateChange
HarmExperience
HarmRisk
HarmThreat
RightsViolation
HarmJudgment
```

Retain:

```text
Pain != Harm
NoPain != NoHarm
PhysicalDamage != HarmExperience
PsychologicalHarm != PhysicalDamage
RiskOfHarm != RealizedHarm
ExpectedHarm != RealizedHarm
HarmSeverity != Wrongness
Wrongness != HarmMagnitudeOnly
PreferenceFrustration != Harm by definition
RightsViolation != HarmExperience
CurrentValence != WholeHarmTrajectory
```

Use HarmProfile_D with target, affected dimension, experience, physical/
psychological/function/opportunity effect, probability, magnitude, duration,
reversibility, uncertainty, consent, intent, foreseeability, alternatives, rights and
externalities.

## Welfare

HF14 does not freeze one welfare scalar.

Preserve at least:

```text
experienced affect / pain / pleasure
life satisfaction / evaluative well-being
preference satisfaction
health/functioning
capability/opportunities
resources
relationships
meaning/purpose
autonomy/security
```

Retain:

```text
Choice != ExperiencedWelfare
RememberedUtility != ExperiencedUtility
PreferenceSatisfaction != WelfareTotality
CurrentPreference != ContextIndependentWelfareMetric
PopulationPreference != TargetExperiencedWelfare
LifeSatisfaction != PositiveAffect
PositiveAffect != -NegativeAffect
ResourceAmount != Welfare
CapabilitySet != CurrentFunctioning
CurrentFunctioning != OpportunityFreedom
Welfare_D != Welfare_E
AggregateWelfare != WelfareDistribution
```

## Fairness / allocation

Preserve distinct criteria:

```text
Equality
Equity
Need
Merit
Desert
Priority to worse-off
Sufficiency
Efficiency/aggregate benefit
Procedural fairness
Outcome fairness
```

Retain:

```text
Equality != Fairness
Inequality != Unfairness
EqualResources != EqualWelfare
EqualOutcome != EqualOpportunity
Equity != Equality
Need != Merit
NeedPrinciple != EqualityPrinciple
MeritEvidence != DesertConclusion
Effort != Desert
OutcomeAchievement != Desert
PriorityToWorseOff != Equality
Sufficiency != Equality
Efficiency != Fairness
Fairness != AggregateWelfareMaximization
Fairness != NeedPrincipleOnly
Fairness != MeritPrincipleOnly
PopulationFairnessJudgment != OneSharedFairnessRule
FairnessJudgment != NormativeFairnessTruth
ProceduralFairness != OutcomeFairness
BeneficialOutcome != FairProcedure
FairProcedure != BeneficialOutcomeGuarantee
```

FairnessProfile_D must reveal which metric/criterion is being applied rather than
saying only `fair/unfair`.

## Justice

HF14 uses `Justice_D` as a framework-relative family of normative judgments about:

```text
distributions
procedures
institutions
rights
responsibilities
power/coercion
```

Retain:

```text
Justice != Equality
Justice != FairnessOnly
Justice != LegalValidity
Justice != AggregateWelfareMaximization
StableInstitution != JustInstitution
NormativeDisagreement != EmpiricalErrorOnly
PerfectFacts != OneNormativeAnswer by definition
EmpiricalFit(F) != NormativeTruth(F)
MoralIntuition != NormativeProof
Deliberation != TruthGuarantee
MoralConsensus != MoralTruth by definition
NormativeDisagreement != NormativeNihilismProof
```

Candidate normative model families remain visible rather than merged:

```text
consequence/welfare
rights/deontic constraints
distributive fairness
procedural fairness
desert/responsibility-sensitive
capability/opportunity
relational/non-domination
```

No family is made foundation truth.

## Rights

For legal analysis, Hohfeldian relations are retained as a useful typed decomposition:

```text
claim-right ↔ duty
liberty/privilege ↔ no-right
power ↔ liability
immunity ↔ disability
```

Retain:

```text
ClaimRight != Liberty
Right != Permission
LegalPower != PhysicalCapability
LegalImmunity != PhysicalInvulnerability
LegalRight != MoralRight
MoralRight != CurrentInstitutionalPermission
Right != Capability
Capability != Right
Interest != Right by definition
Right != AbsoluteTrump by definition
```

Use RightsProfile_K with holder, addressee, object/action, right type, system,
correlative relation, scope, exception, waiver/transfer, enforcement/remedy, conflicts
and practical exercise capability.

## Duties / obligations

Separate:

```text
MoralDuty
LegalDuty
RoleDuty
PromissoryObligation
ContractualObligation
TaskDuty
```

Retain:

```text
OthersExpect(X) != Duty(X)
Duty != Motivation
DutyExists != DutyPerformed
LegalDuty != MoralDuty
RoleDuty != MoralDuty by definition
Commitment != MoralDuty
Promise != MereExpectation
PromiseMade != ValidMoralDuty
ContractualObligation != MoralObligationTotality
```

Promises can exert behavioral force beyond partner payoff expectation, but HF14 does
not infer that every promise generates a valid moral duty.

## Responsibility

Separate:

```text
CausalResponsibility
TaskResponsibility
RoleResponsibility
MoralResponsibility
Blameworthiness
LegalLiability
Accountability
```

Retain:

```text
CausalContribution != MoralResponsibility
MoralResponsibility != Wrongdoing
Wrongdoing != Blameworthiness
Blame != Punishment
MoralResponsibility != LegalLiability
Accountability != MoralResponsibility
Intent != MoralResponsibilityTotality
OutcomeSeverity != MoralResponsibility by definition
Foreseeability != ActualKnowledge
Knowledge != Control
Control != CausalContribution
NominalControl != EffectiveControl
OverrideAvailable != MeaningfulControl
Coercion != ZeroResponsibilityByDefinition
RoleAssignment != MoralResponsibilityByDefinition
DecisionAuthority != MoralResponsibilityTotality
Negligence != IntentionalHarm
BadOutcome != NegligenceProof
NonAction != ResponsibleOmission by definition
HarmOccurred != HighBlame
```

ResponsibilityProfile must preserve causation, action/omission, intent, belief/
knowledge, foreseeability, effective control, alternatives, coercion, capacity,
role/duty, authority, outcome and repair/prevention.

## Accountability

Working relation:

```text
Accountability_D(A,X,S)
= structured requirement that A answer for, disclose, justify, review, correct or
  bear specified consequences regarding X within system S
```

Retain:

```text
Accountability != Blame
Accountability != Punishment
Accountability != PersonalFaultRequirement
Answerability != AccountabilityTotality
Auditability != Accountability
Sanction != Accountability
```

Accountability can remain well-defined even when personal moral blame is uncertain.

## Normative legitimacy

Working meta-definition:

```text
NormativeLegitimacy_F(X)
= justified entitlement of X to exercise specified authority/coercion under declared
  normative framework F
```

Retain:

```text
PerceivedLegitimacy != NormativeLegitimacy
LegalValidity != NormativeLegitimacy
Compliance != NormativeLegitimacy
MajoritySelection != NormativeLegitimacyByDefinition
BeneficialOutcome != NormativeLegitimacy
FairProcedure != NormativeLegitimacyGuarantee
WelfareImprovement != RightsCompatibility
WelfareCriterion != FairnessCriterion
FairnessCriterion != RightsCriterion
RightsPresent != DecisionSolved
```

Use LegitimacyProfile_F with authority source/scope, procedure, voice, rights,
welfare, distribution, coercion, transparency, contestability, appeal/exit,
accountability, affected parties, minority/worst-off effects and unresolved framework
conflicts.

## Moral uncertainty

When candidate normative frameworks disagree, record:

```text
candidate frameworks
criterion conflicts
factual uncertainty
interpretive uncertainty
robust conclusions
reversibility/appeal
```

Do not silently average normative frameworks into one hidden score.

## Human×AI responsibility

Separate at least:

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

Retain:

```text
AIExecution != AIMoralResponsibility
HumanAuthorization != HumanMoralResponsibilityTotality
HumanInLoop != HumanResponsibilityByDefault
ManualOverrideAvailable != MeaningfulControl
ObservedBlameAllocation != ResponsibilityTruth
AnthropomorphicMindAttribution != MoralAgency
PerceivedAgency != EffectiveControl
OperationalAutonomy != MoralAuthority
AIEpistemicContribution != AIDecisionAuthority
FormalAuthorization != MoralPermission
SuccessfulOutcome != EthicalProcess
EthicalProcess != SuccessfulOutcomeGuarantee
InstitutionalFidelity != NormativeCorrectness
NoObviousHumanBlameTarget != AIMoralResponsibility
UncertainMoralBlame != NoAccountability
```

Manual override availability is a decisive falsifier: observers can increase blame
merely because an override is nominally present even where effective intervention is
not possible.

## Reflexivity

Normative classification is intervention-prone:

```text
blame label
rights label
desert label
standing label
```

can alter later treatment, punishment, capability and opportunity.

Therefore:

```text
NormativeClassification may become SocialIntervention
```

and the classification must not be treated as passive measurement of moral truth.

## High-information falsifiers to preserve

- attempted intentional harm without realized harm;
- accidental harm with severe outcome but innocent intent;
- foreseeability manipulated independently of intent;
- hindsight outcome information changing negligence judgment;
- severe coercion combined with agent identification;
- psychological harm without physical injury;
- longer painful episode chosen because the ending improves;
- life satisfaction dissociating from positive/negative affect;
- patient versus general-public health-state valuation;
- achievement-based versus luck-based inequality;
- objective need versus equality in allocation;
- equity-versus-efficiency resource destruction;
- random allocation reducing responsibility for inequity;
- procedural fairness changing reactions under identical outcome dimensions;
- legally valid/authoritative decision rejected on moral grounds;
- Hohfeldian claim versus liberty/power/immunity relations;
- promise-keeping effects not reducible to payoff expectation;
- nominal AI manual mode increasing human blame without effective control;
- anthropomorphic mind attribution shifting blame from Humans to AI;
- mental-impairment defense reducing blame while sometimes reducing attributed
  rights;
- robot experiential-mind attribution tracking perceived moral standing.

## Exact next foundation

HF14 can now type:

```text
harm
welfare
rights
duties
responsibility
legitimacy
```

but each repeatedly requires bearer conditions:

```text
Who can be harmed?
Who has welfare?
Who can hold rights?
Who can bear duties?
Who can be blameworthy?
Who deserves direct moral consideration?
```

The same capacity cannot answer all six:

- infants can hold strong claims with little responsibility capacity;
- severe impairment can lower blame without erasing protection claims;
- animals can have welfare without human-like institutional agency;
- corporations can hold legal powers/rights without established sentience;
- future persons can be affected before they exist;
- AI can exhibit high task agency while sentience/interests remain uncertain.

Primary mind-perception evidence further separates agency from experience and shows
that human standing judgments are sensitive to those dimensions without proving that
human perception equals normative truth.

Therefore the exact next round is:

# HF15 — Moral Standing, Moral Agency, Moral Patienthood, Sentience, Interests, Vulnerability, Dignity and Scope of Concern

## HF15 starting questions

1. What is moral standing relative to legal personhood, social recognition and
   biological species membership?
2. What is moral patienthood relative to capacity for experience, welfare, interests,
   vulnerability and rights?
3. What is moral agency relative to general agency, intention, understanding,
   control and responsibility capacity?
4. Can moral agency and moral patiency vary independently?
5. What is sentience relative to consciousness, valenced experience, nociception and
   report?
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
13. What evidence could justify expanding or contracting moral scope of concern?
14. What next boundary emerges after standing/bearer conditions are rebuilt?

## Candidate HF15 falsifiers

- infant/high-rights case with low responsibility capacity;
- severe mental impairment reducing blame without eliminating protection claims;
- temporary unconsciousness/coma with persistent rights;
- nonhuman animal valenced experience without human language;
- corporation/legal person with rights/powers but no established phenomenal
  experience;
- future-person harm where the target does not exist at action time;
- artificial system with high apparent agency but uncertain experience;
- robot appearance/mind attribution shifting standing judgment without sentience
  evidence;
- expressed machine preference with uncertain welfare capacity;
- sentient target with low planning/agency;
- highly capable agent with no verified sentience;
- vulnerability/dependence generating protection claims without reciprocal duty
  capacity;
- legal recognition changing while welfare/experience evidence is held constant.

## Do not precommit

HF14 does not establish that:

- only humans have moral standing;
- all humans/nonhumans have identical standing;
- biological species membership alone settles standing;
- sentience is necessary/sufficient for every right;
- agency is necessary for rights;
- intelligence determines moral worth;
- language/report is necessary for interests;
- preference expression proves welfare capacity;
- legal personhood implies moral patienthood;
- corporations have or lack moral standing in the same manner as humans;
- current AI systems are conscious or non-conscious by fiat;
- behavioral self-report proves machine sentience;
- anthropomorphic appearance establishes standing;
- uncertainty requires either full inclusion or full exclusion;
- dignity reduces to sentience/welfare;
- vulnerability alone determines moral status.

## Stop rule

Do not schedule HF16 now. HF15 must expose a repeated neighboring distinction whose
absence creates category failures across materially different bearer/standing cases.

## Supersession — HF15 complete

HF15 has completed the moral-standing/bearer boundary selected here. Current
continuation is owned by [`HF15-CONTINUATION.md`](HF15-CONTINUATION.md). This file
remains the canonical record of why HF15 emerged from HF14.
