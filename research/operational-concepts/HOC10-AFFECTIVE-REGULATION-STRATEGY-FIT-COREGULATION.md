---
schema_version: 1
id: human.operational-concepts.hoc10
title: HOC10 — Affective Regulation, Strategy Fit and Co-Regulation
profile: research
lifecycle: completed
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
  - engineer
updated: 2026-08-18
summary: Reconstructs the practical affective-regulation layer downstream of HF21 and HOC1–HOC9. HOC10 separates affective state from regulation target, regulation from emotion reduction, regulation goal from hedonic improvement, strategy use from strategy effectiveness, expression change from experience/physiology/action change, strategy variability/switching from genuine context-sensitive flexibility, interpersonal support from co-regulation, and Agent-supported regulation from independent Human change. It introduces AffectiveRegulationTargetSpec, RegulationGoalProfile, StrategyUseEpisode, AffectiveRegulationOutcomeProfile, StrategySituationFitCase, RegulationFlexibilityEvidenceView, CoRegulationCase, AffectiveRegulationTrajectory and NextBestAffectiveRegulationAction. Strategy value is person-, situation-, intensity-, goal-, culture-, development- and horizon-dependent; no universal adaptive/maladaptive hierarchy is admitted. Negative emotion is not dysregulation, no-active-regulation and allowing expression are legitimate outcomes, and emotion support need not aim to change emotion. HOC10 uses an episode-first privacy architecture: no default continuous affect sensing, no global emotion-regulation score, explicit intervention authority, minimum evidence and short expiry. No prior HOC/Foundation is reopened and no HOC11 is preselected.
evidence_status: verified-synthesis
readiness: READY
related:
  - human.foundations.hf21
  - human.deep-foundations.hd2
  - human.operational-concepts.hoc4
  - human.operational-concepts.hoc5
  - human.operational-concepts.hoc6
  - human.operational-concepts.hoc10.sources
---
# HOC10 — Affective Regulation, Strategy Fit and Co-Regulation

## 0. Admission

HOC10 is admitted only after the Round-7 closure audit discovered an operational blind spot and Round 8 directly attacked the candidate against:

```text
HF21 direct projection
HOC4 load/fatigue/recovery regulation
HOC5 goals/motivation/action/self-regulation
HOC6 relation/support/coordination
ExperientialProjectionProtocol
NoNewHOC
```

The candidate survived because a substantive cross-domain action family remains after composition.

```text
OperationalUsefulness != FoundationStatus
FoundationOwnership != OperationalReconstructionCompletion
```

No existing HOC is reopened.

---

# 1. Core deletion

Reject the common collapse:

```text
negative emotion
→ bad state
→ regulate
→ reduce emotion
→ calm = success
```

Every arrow can fail.

Canonical separations:

```text
AffectiveState != RegulationTarget
NegativeEmotion != Dysregulation
Regulation != EmotionReductionOnly
RegulationGoal != HedonicImprovementOnly
StrategyUse != StrategyEffectiveness
ExpressionChange != ExperienceChange
StrategySwitching != Flexibility
EmotionSupport != EmotionRegulationByDefinition
```

---

# 2. Use questions

HOC10 answers recurring questions such as:

```text
What affective component, if any, is the Human trying to regulate?
What is the regulation goal: decrease, increase, maintain, tolerate, express or delay action?
What strategy/support was used and when?
Did the strategy affect experience, expression, physiology, action or relationship differently?
Was the strategy well matched to the current intensity, controllability, social context and Human goal?
Should the strategy continue, switch, stop, or should no active regulation occur?
Is another Human/Agent co-regulating rather than merely providing generic support?
```

These are practical questions, not emotion-theory questions.

---

# 3. AffectiveRegulationTargetSpec

```text
AffectiveRegulationTargetSpec = {
  Human,
  use_question,
  affective episode / mood / recurring context,
  declared affective component(s),
  regulation goal,
  relevant Human goal/value/relationship,
  situation/context,
  perceived controllability/changeability,
  affective intensity/history,
  time horizon,
  consequence level,
  support/co-regulation boundary,
  culture/development coordinates where relevant,
  clinical/nonclinical boundary,
  intervention authority/consent boundary,
  uncertainty
}
```

Possible target components:

```text
felt distress/valence
emotion intensity
emotion duration
expression/display
action readiness/impulse
attention/interference
relational escalation
affective recovery/tail
ability to tolerate/allow emotion
```

No target is universally preferred.

---

# 4. RegulationGoalProfile

```text
RegulationGoalProfile = {
  decrease?,
  increase?,
  maintain?,
  tolerate/allow?,
  express more accurately?,
  conceal/modulate expression?,
  delay action?,
  recover after episode?,
  preserve task performance?,
  preserve relationship?,
  solve external cause?,
  Human endorsement/provenance,
  conflicts with other goals,
  uncertainty
}
```

Canonical guard:

```text
RegulationGoal != FeelBetterByDefinition
```

Instrumental regulation can legitimately prioritize a non-hedonic outcome.

---

# 5. Regulation is not necessarily required

```text
AffectiveEpisodePresent
!= RegulationNeeded
```

Legitimate states include:

```text
NO_ACTIVE_REGULATION
ALLOW / EXPERIENCE
EXPRESS
OBSERVE / GATHER_INFORMATION
ACT_ON_EXTERNAL_PROBLEM
WAIT
```

A system must justify intervention rather than infer it from negative affect alone.

---

# 6. StrategyUseEpisode

```text
StrategyUseEpisode = {
  trigger/context,
  affective target,
  regulation goal,
  strategy family,
  timing,
  self-initiated / externally prompted,
  supporter/co-regulator if any,
  support/tool/Agent if any,
  intended endpoint,
  immediate outcome,
  delayed outcome,
  task/action effect,
  relationship effect,
  effort/cost,
  uncertainty,
  provenance
}
```

One strategy label does not imply one mechanism or outcome.

---

# 7. Strategy families

HOC10 may use strategy families such as:

```text
SITUATION_SELECTION
SITUATION_MODIFICATION
ATTENTION_REDIRECTION / DISTRACTION
REAPPRAISAL / REINTERPRETATION
ACCEPTANCE / ALLOWING
DECENTERING / MINDFUL ATTENTION when operationally specified
PROBLEM_SOLVING
SOCIAL_SHARING / SUPPORT_SEEKING
INTERPERSONAL_CO_REGULATION
EXPRESSION_MODULATION
PHYSIOLOGICAL/BODILY_REGULATION
BEHAVIORAL_DELAY
APPROACH / WITHDRAWAL where used regulatory
RUMINATION / WORRY / AVOIDANCE as observed patterns
NO_ACTIVE_REGULATION
```

This is a practical taxonomy, not one universal theory.

---

# 8. Strategy label is not effectiveness

```text
StrategyUse(S)
!= StrategyEffective(S)
```

Effectiveness is always indexed by:

```text
Human
Target
Goal
Situation
Intensity/history
Timing
Endpoint
Time horizon
Support
Culture/development where relevant
```

Therefore HOC10 rejects permanent labels such as:

```text
AdaptiveStrategy = reappraisal
MaladaptiveStrategy = suppression
```

without context.

---

# 9. AffectiveRegulationOutcomeProfile

```text
AffectiveRegulationOutcomeProfile = {
  experienced-affect change,
  expression/display change,
  physiological change if legitimately measured,
  action-readiness/action change,
  attention/cognitive-interference change,
  task/goal effect,
  relationship/social effect,
  immediate cost/benefit,
  delayed cost/benefit,
  rebound/recurrence,
  learning/update effect,
  support dependence,
  uncertainty
}
```

This operationalizes the HF21 endpoint firewall.

---

# 10. Endpoint success is plural

Examples:

```text
expression goal met
while experience goal not met

felt distress reduced
while external problem worsened

anger preserved
while impulsive action delayed

fear remains
while task performance succeeds
```

Therefore:

```text
OneEndpointSuccess != WholeRegulationSuccess
```

---

# 11. StrategySituationFitCase

```text
StrategySituationFitCase = {
  Human,
  affective target,
  regulation goal,
  strategy,
  situation features,
  controllability/changeability,
  affective intensity and persistence,
  social context / relationship,
  time pressure,
  culture/development coordinates if material,
  prior response history,
  immediate outcomes,
  delayed outcomes,
  plausible alternative strategies,
  fit hypothesis,
  uncertainty
}
```

This is a central HOC10 object.

---

# 12. StrategySituationFit is not intrinsic strategy quality

Current ambulatory evidence strongly pressures universal rankings.

```text
AverageEffect(S)
!= EffectForHumanEpisode(S,H,E)
```

and:

```text
HighIntensityEpisode
can change both strategy selection and apparent strategy effectiveness.
```

HOC10 therefore records situation difficulty rather than attributing outcome directly to Human regulation quality.

---

# 13. Situation controllability matters

```text
ChangeSituation
vs
ChangeInterpretation
```

are different regulatory options.

A reappraisal strategy can be useful under one controllability regime and poorly matched under another.

Therefore:

```text
ReappraisalFailure
!= LowRegulationSkillByDefinition
```

The consumer must inspect strategy–situation fit.

---

# 14. RegulationFlexibilityEvidenceView

HOC10 does **not** admit a global `RegulationFlexibilityProfile` by default.

Use:

```text
RegulationFlexibilityEvidenceView(H, ContextClass, interval) = {
  declared context dimensions,
  observed context changes,
  observed goal changes,
  strategy allocation changes,
  strategy persistence under stable contexts,
  switching under materially changed contexts,
  endpoint-specific outcome evidence,
  failed-fit recognition,
  switch/stop evidence,
  repertoire evidence,
  uncertainty
}
```

---

# 15. Variability and switching are not flexibility

```text
MoreStrategies != MoreFlexibility
MoreSwitching != MoreFlexibility
MoreVariability != MoreFlexibility
```

True flexibility evidence requires context.

A Human who constantly changes strategy in an unchanged context may be dysregulated, exploring rationally, learning, or simply responding to unmeasured changes.

HOC10 does not infer flexibility from entropy/counts alone.

---

# 16. Repertoire is not competence

```text
KnowsManyStrategies
!= SelectsWell
!= ImplementsWell
!= BenefitsFromThem
```

HOC8 may own knowledge of strategies.
HOC1 may own capability to implement a technique.
HOC10 owns the regulation-use/outcome relation.

---

# 17. CoRegulationCase

```text
CoRegulationCase = {
  target Human,
  supporter/co-regulator,
  relationship/role,
  affective target,
  regulation goal,
  interaction/strategy,
  Human endorsement/acceptance,
  authority/consent boundary,
  immediate affective outcome,
  delayed affective outcome,
  action/task effect,
  relational effect,
  dependence/support change,
  attribution: independent/situated/joint,
  uncertainty
}
```

This consumes HOC6 but is not reduced to HOC6.

---

# 18. Co-regulation is not generic support

```text
SupportPresent
!= CoRegulationOccurred
```

Co-regulation requires an affective target/process relation.

Likewise:

```text
EmpathicResponse
!= SuccessfulCoRegulation
```

and:

```text
CoRegulation
!= RelationshipQuality
```

---

# 19. Co-regulation can target self or other

Interpersonal emotion regulation can include:

```text
A uses B/social interaction to regulate A
A attempts to regulate B
A and B mutually influence affective regulation
```

HOC10 must record directionality.

```text
A→B
B→A
A↔B
```

rather than one undirected `support` field.

---

# 20. Developmental co-regulation

Children and adolescents may rely on caregivers or peers for regulation under regimes different from adults.

Therefore:

```text
SupportedAffectiveRegulation
!= IndependentAffectiveRegulation
```

and:

```text
CoRegulationDependence
!= DefectByDefinition
```

Use HOC1/HOC3 support attribution if independent capability matters.

---

# 21. AffectiveRegulationTrajectory

For repeated use questions:

```text
AffectiveRegulationTrajectory(H, TargetFamily, ContextClass, interval) = {
  recurring triggers,
  recurring regulation goals,
  strategy-use history,
  fit/misfit cases,
  endpoint trajectories,
  switch/stop history,
  co-regulation history,
  support dependence,
  learning/change evidence,
  uncertainty
}
```

This is not a global personality trait.

---

# 22. Short-term relief is not long-term benefit

```text
ShortTermRelief
!= DelayedBenefit
```

A strategy may reduce current distress while increasing:

```text
avoidance
relationship cost
rebound
future dependence
external problem persistence
```

or may impose short-term cost for later benefit.

HOC10 requires horizon declaration.

---

# 23. Expression control is not experience control

```text
CalmAppearance
!= CalmExperience
```

This is especially important in:

```text
workplace display rules
child/adolescent compliance
care settings
Human-Agent conversations
```

Systems must not use visible calm as the only regulation-success signal.

---

# 24. Negative emotion is not dysregulation

```text
Grief
Fear under real threat
Anger at injustice
Sadness after loss
```

can be contextually appropriate.

Therefore:

```text
NegativeEmotion != ProblemToFix
```

Affective regulation is judged relative to declared Human goals, context, welfare/rights boundaries and outcomes—not valence alone.

---

# 25. Positive emotion is not always the target either

Regulation may include:

```text
dampening excitement for concentration
reducing laughter in a solemn context
maintaining calm positive state
up-regulating confidence/enthusiasm
```

Again:

```text
PositiveValence != UniversalRegulationGoal
```

---

# 26. Emotion support boundary

A person/Agent may provide:

```text
listening
validation
presence
companionship
space for emotion
```

without trying to change the emotion.

Therefore:

```text
EmotionSupport != EmotionRegulationByDefinition
```

HOC6/HF22 may own the relation/support case if no regulation target exists.

---

# 27. HOC4 boundary

HOC4 owns:

```text
load
fatigue
sleep/circadian state
stress exposure/response
reserve
recovery
sustainable work state
```

HOC10 may consume HOC4 state because fatigue/sleep/stress changes affective regulation.

But:

```text
RecoveryAction != EmotionRegulationStrategyByDefinition
```

and no HOC4 reopen is required.

---

# 28. HOC5 boundary

HOC5 owns:

```text
regulation goal as Human goal
action allocation
implementation
execution
```

HOC10 owns the affect-specific regulation strategy/outcome grammar.

```text
HOC5 answers: which goal/action is selected?
HOC10 answers: how is affect being regulated and how did that regulation work?
```

The two compose.

---

# 29. HOC6 boundary

HOC6 owns:

```text
relationship
trust
role
authority
dependence
communication
repair
```

HOC10 owns:

```text
affective regulation through that relation.
```

```text
RelationshipRepair
!= EmotionRegulationByDefinition
```

---

# 30. HOC7 clinical boundary

HOC10 is non-diagnostic.

```text
DysregulationEvidence
!= Diagnosis
```

Clinical questions such as:

```text
suicidality
severe mood disorder
trauma disorder
substance use disorder
psychosis
medical causes of affective change
```

remain under health/clinical authority.

HOC10 can provide typed evidence and route/escalate.

---

# 31. HOC8 knowledge boundary

```text
KnowledgeOfReappraisal
!= EffectiveReappraisalUse
```

HOC8 owns strategy knowledge/understanding.
HOC10 owns strategy use and affective outcome.

---

# 32. HOC9 habit boundary

Repeated regulation patterns can become habitual/routinized.

But:

```text
HabitualAvoidance
!= AffectiveRegulationTotality
```

HOC9 owns context-sensitive behavioral control.
HOC10 owns affective regulation target/outcome.

---

# 33. Evidence bundle

```text
AffectiveRegulationEvidenceBundle = {
  self-report of affect/regulation goal,
  reported strategy use,
  contextual event evidence,
  behavioral/action evidence,
  expression evidence where relevant,
  relational/co-regulator evidence,
  task/performance outcome,
  delayed follow-up,
  physiological evidence only when justified,
  support/tool/Agent state,
  conflicting evidence,
  provenance,
  uncertainty
}
```

No single channel is privileged for every target.

---

# 34. Evidence ceiling

```text
SelfReportStrategyUse
→ supports reported strategy use
→ does not prove mechanism or effectiveness

VisibleExpressionChange
→ supports expression evidence
→ does not prove experience change

PhysiologicalChange
→ supports declared physiological endpoint
→ does not prove emotion category or subjective relief

AgentInferenceOfEmotion
→ supports model output only
→ does not transparently reveal Human experience
```

---

# 35. Update and expiry

## Episode state

```text
minutes / hours / event-bound
```

Reassess after:

```text
major context change
affective intensity shift
new information
strategy switch
supporter/Agent change
sleep/fatigue/health change
```

## StrategySituationFit history

Use repeated episodes; update after contradictory outcome evidence.

## Trajectory

Longitudinal but scoped to target/context class.

No timeless affective-regulation profile by default.

---

# 36. Privacy architecture

HOC10 is episode-first.

```text
NoContinuousAffectSensingByDefault
NoGlobalEmotionRegulationScore
NoPermanentIntimateAffectDossier
```

Collect only what the declared use question needs.

Statuses may include:

```text
NOT_ASSESSED
NOT_RELEVANT
HUMAN_DECLINED
INFERRED_UNCONFIRMED
INSUFFICIENT_EVIDENCE
NO_ACTIVE_REGULATION
REGULATION_GOAL_UNCLEAR
OUTCOME_UNCLEAR
```

---

# 37. Intervention authority

```text
ObservedAffect
!= ConsentToIntervene
```

An Agent may observe/predict distress without authority to:

```text
reframe
calm
redirect
withhold information
change choices
contact others
```

unless a separate authority/consent rule permits it.

HOC5/HOC6/SupportedDecisionParticipationProtocol and Governance boundaries remain applicable.

---

# 38. Human–Agent attribution

Always separate:

```text
IndependentHumanRegulation
SituatedHumanRegulation
JointHumanAgentRegulation
```

Example:

```text
AI generates reappraisal alternatives
Human reports lower distress
```

supports situated/joint effectiveness.

It does not establish:

```text
Human independently acquired reappraisal capability.
```

HOC3 is needed for learning/transfer claims.

---

# 39. Agent can become a co-regulator

If an Agent repeatedly:

```text
validates
reframes
redirects attention
encourages delay
provides calming interaction
```

it may function as an external regulation support.

Record:

```text
AgentMediatedCoRegulationCase
```

through the generic CoRegulationCase with explicit non-human supporter attribution.

Do not infer mutual affective experience in the Agent.

---

# 40. Agent-era failure modes

```text
emotion misclassification
negative-affect suppression bias
calm/compliance optimization
inappropriate reappraisal
reassurance dependence
persistent intimate affect logging
intervention without consent
cultural mismatch
clinical condition masked by generic support
relationship problem reframed as individual emotional problem
external danger reframed as internal dysregulation
```

HOC10 exists partly to make these errors visible.

---

# 41. NextBestAffectiveRegulationAction

```text
NextBestAffectiveRegulationAction = {
  target,
  Human-endorsed regulation goal,
  candidate action,
  strategy family,
  expected target endpoint,
  situation-fit rationale,
  alternatives,
  expected cost/risk,
  support/authority requirements,
  evidence confidence,
  stopping/switch condition,
  reassessment time
}
```

This is recommendation structure, not autonomous authority.

---

# 42. Candidate actions

```text
NO_ACTIVE_REGULATION
CLARIFY_AFFECTIVE_TARGET
CLARIFY_REGULATION_GOAL
CHANGE_SITUATION
LEAVE_OR_PAUSE_SITUATION
REDIRECT_ATTENTION
REAPPRAISE_OR_REFRAME
ACCEPT_OR_TOLERATE
PROBLEM_SOLVE_CAUSE
SEEK_SOCIAL_SUPPORT
REQUEST_CO_REGULATION
MODULATE_EXPRESSION
DELAY_ACTION
USE_BODY_OR_PHYSIOLOGICAL_REGULATION
SWITCH_STRATEGY
STOP_COUNTERPRODUCTIVE_STRATEGY
ALLOW_EXPRESSION
MONITOR / REASSESS
ROUTE_CLINICAL_OR_SAFETY_OWNER
```

No action is universally preferred.

---

# 43. Strategy switching rule

Switching is justified only when evidence suggests:

```text
current strategy mismatched target/context
current strategy ineffective on declared endpoint
context/goal materially changed
strategy cost exceeds benefit
new evidence changes fit estimate
```

not simply because:

```text
more switching = more flexibility.
```

---

# 44. Stop-regulating rule

A Human/Agent should consider stopping regulation when:

```text
emotion is informative/appropriate
strategy is creating larger cost
external action is now better
regulation goal is no longer endorsed
intervention is intrusive
support is becoming coercive/dependency-producing
```

Thus:

```text
StopRegulating
can be successful regulation policy.
```

---

# 45. Context/culture/development transport

Every reusable claim should state material transport coordinates such as:

```text
culture/social display norms
developmental stage
relationship type
institution/work setting
stressor controllability
affective intensity
support regime
```

A population-average strategy effect is not imported as an individual rule without evidence.

---

# 46. Regulation and coping boundary

`Coping` can include broader adaptation to stressors:

```text
resource acquisition
problem solving
social change
meaning-making
avoidance
emotion regulation
```

Therefore:

```text
EmotionRegulation
subset/overlap with Coping depending taxonomy
!= CopingTotality
```

HOC10 does not claim all coping.

---

# 47. Regulation and resilience boundary

```text
EffectiveRegulationEpisode
!= Resilience
```

Resilience is a trajectory-level outcome/composite under perturbation.

Do not infer resilient personhood from one regulation episode.

---

# 48. Regulation and welfare boundary

```text
EmotionRegulationSuccess
!= WelfareTotality
```

A system can successfully reduce anxiety while harming autonomy, relationships, truth-seeking or long-run welfare.

HF14 and domain owners remain authoritative for normative evaluation.

---

# 49. Regulation and morality boundary

```text
Calmness != MoralGoodness
Anger != MoralFailure
EmotionalControl != ResponsibilityByDefinition
```

Moral judgment and responsibility belong to HF14.

---

# 50. Update through learning

Repeated strategy use can produce learning.

But:

```text
SuccessfulEpisode
!= LearnedIndependentSkill
```

HOC3 must establish retention/transfer/support fading if learning is claimed.

---

# 51. Regulation bottlenecks

Potential HOC10-local bottlenecks include:

```text
unclear affective target
unclear regulation goal
limited strategy repertoire
poor strategy selection
poor implementation
poor context discrimination
failure to switch/stop
misread endpoint
rebound/delayed cost
co-regulation mismatch
support/authority mismatch
```

Capability, knowledge and opportunity bottlenecks still route to HOC1/HOC8/HOC5.

---

# 52. Do not diagnose from strategy patterns

```text
FrequentRumination
FrequentSuppression
LowReappraisal
```

may be clinically relevant evidence in some settings.

They are not diagnoses.

```text
StrategyPattern != MentalDisorder
```

---

# 53. No universal `emotion regulation skill`

Reject:

```text
EmotionRegulationSkill = one scalar
```

because regulation performance is target/context/strategy/support dependent.

If a consumer needs capability, use a HOC1-style scoped capability surface with HOC10 tasks rather than inventing a global trait.

---

# 54. Optional scoped summary

A consumer may derive a bounded summary such as:

```text
RegulationOperationalView(H, TargetFamily, ContextClass, interval)
```

combining:

```text
common goals
common strategies
fit evidence
endpoint outcomes
switch/stop evidence
co-regulation/support dependence
uncertainty
```

It must drill down to episodes.

---

# 55. Reflexivity

HOC10 policies alter future evidence.

```text
Agent recommends reappraisal
→ Human changes interpretation
→ future emotion/use patterns change
→ model sees its own intervention effects
```

Therefore mark policy-conditioned episodes.

```text
ObservedRegulationPattern
may be intervention-conditioned.
```

---

# 56. Privacy firewall

```text
CanInferEmotion
!= PermissionToStoreEmotionProfile

CanPredictDistress
!= PermissionToIntervene

CanImproveImmediateAffect
!= PermissionToManipulateChoice
```

High-impact uses require explicit downstream authority.

---

# 57. Canonical forbidden inferences

```text
NegativeEmotion != Dysregulation
PositiveEmotion != RegulationSuccess
EmotionIntensity != Pathology
EmotionExpression != Experience
CalmExpression != CalmExperience

EmotionRegulation != Suppression
EmotionRegulation != EmotionReductionOnly
EmotionRegulation != SelfControlTotality
EmotionRegulation != CopingTotality

RegulationGoal != HedonicImprovementOnly
StrategyUse != StrategyEffectiveness
AverageStrategyEffect != IndividualStrategyEffect
ShortTermRelief != LongTermBenefit
ExpressionControl != ExperienceControl

MoreStrategies != MoreFlexibility
MoreSwitching != MoreFlexibility
MoreVariability != MoreFlexibility

Reappraisal != AlwaysGood
Suppression != AlwaysBad
Acceptance != PassivityByDefinition
Distraction != AvoidanceByDefinition
Rumination != ReflectionByDefinition

CoRegulation != RelationshipQuality
CoRegulation != DependencyDefect
SupportiveIntent != RegulationSuccess
EmotionSupport != EmotionRegulationByDefinition

ObservedAffect != ConsentToIntervene
DistressPrediction != PermissionToNudge
EmotionOptimization != HumanWelfare
EmotionPrediction != Diagnosis

AgentSupportedRegulationGain != IndependentHumanLearningGain
AIEmotionInference != HumanExperiencedEmotion
```

---

# 58. Foundation / HOC dependency map

```text
HF2  first-person experience boundary
HF3  attention/access/metacognition
HF4  goals/value/motivation/self-regulation
HF5  physiological regulation/stress/interoception/pain
HF7  memory/history
HF8  representation/reappraisal concepts
HF10 decision/planning
HF11 action
HF12 interaction/communication
HF14 welfare/normative firewall
HF21 affect/emotion/mood/appraisal/regulation ontology
HF22 persistent relationship

HOC1 capability/support/readiness
HOC2 confidence/evidence/reliance
HOC3 learning/transfer/support dependence
HOC4 load/fatigue/recovery
HOC5 goals/action allocation/execution
HOC6 relations/roles/trust/dependence
HOC7 health/clinical boundary
HOC8 knowledge/understanding
HOC9 habitual regulation patterns/contextual control
```

No new Foundation is required.

---

# 59. Operational reasoning grammar

```text
1. Declare the exact affective-regulation use question.
2. Build AffectiveRegulationTargetSpec; do not infer a target from valence alone.
3. Elicit/verify RegulationGoalProfile and Human endorsement.
4. Determine whether active regulation is needed at all.
5. Build StrategyUseEpisode for observed/planned strategy and timing.
6. Preserve experience/expression/physiology/action endpoints separately.
7. Build StrategySituationFitCase using intensity, controllability, social context, goal and prior outcomes.
8. If repeated evidence matters, use RegulationFlexibilityEvidenceView; never infer flexibility from switching/count alone.
9. If another Human/Agent participates, build CoRegulationCase with directionality, consent and support attribution.
10. Compare immediate and delayed outcomes.
11. Select NextBestAffectiveRegulationAction: preserve, change situation, redirect attention, reappraise, accept, problem-solve, seek support, co-regulate, modulate expression, delay action, switch/stop strategy, allow emotion, monitor, or route.
12. Reassess after context/intensity/support changes.
13. Never optimize calmness/positive affect as Human welfare by default.
14. Never infer intervention authority from emotion detection.
```

---

# 60. Stop rule

HOC10 is complete because it has:

```text
separated affective state from regulation target;
separated regulation from emotion reduction;
reconstructed RegulationGoalProfile including non-hedonic goals;
reconstructed StrategyUseEpisode and strategy timing;
reconstructed endpoint-specific AffectiveRegulationOutcomeProfile;
made StrategySituationFitCase first-class;
rejected intrinsic universal strategy rankings;
reconstructed context-conditioned RegulationFlexibilityEvidenceView while rejecting switching/variability proxies;
reconstructed CoRegulationCase with directional relational support and attribution;
added episode-first privacy and intervention-authority boundaries;
retained NO_ACTIVE_REGULATION and ALLOW_EXPRESSION as legitimate outcomes;
separated emotion support from emotion regulation;
connected regulation to HOC1–HOC9 without reopening any prior family;
added Human-Agent external-regulation attribution and manipulation guards;
and reconstructed NextBestAffectiveRegulationAction without one universal optimization target.
```

```text
OperationalReopenCondition(HOC0–HOC9) = false
FoundationReopenCondition(HF0–HF23) = false
NextHOC = UNKNOWN
NextOperationalRoute = UNKNOWN
```
