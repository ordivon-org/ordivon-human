---
schema_version: 1
id: human.foundations.hf5
title: HF5 — Need, Homeostasis, Allostasis, Interoception, Satiety, Stress, Fatigue and Recovery
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
summary: HF5 reconstructs Human internal-state regulation. It separates physiological need from desire and psychological-need theories; regulated variables from setpoints and control loops; homeostasis from predictive allostasis; interoceptive signal, representation, accuracy, sensibility and bodily experience; hunger from satiation/satiety; stressor from stress response and allostatic load; fatigue experience from performance, effort cost and resource depletion; and recovery from rest, habituation and resilience. The residual boundary is history-dependent adaptation and plasticity.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
  - HF5
related:
  - human.foundations.hf4
  - human.foundations.hf5.sources
  - human.foundations.hf5.continuation
---
# HF5 — Need, Homeostasis, Allostasis, Interoception, Satiety, Stress, Fatigue and Recovery

## 0. Status and question

HF4 ended with a variable that had remained mostly opaque:

```text
HumanState_t
```

Yet hunger, satiety, sickness, fatigue, sleep loss, stress and pain repeatedly
changed wanting, reward sensitivity, effort cost, priority and self-regulation.

HF5 therefore asks:

> **What is the living Human regulating, how is internal state sensed and
> represented, how do internal regulatory states become experience and action,
> and what does it mean for a perturbed Human system to recover?**

The round attacks several common simplifications:

```text
Need = desire
Homeostasis = fixed setpoint thermostat
Allostasis = any state change
Interoception = conscious accurate body sensing
Stress = damage
Fatigue = depleted energy tank
Recovery = resting until baseline returns
```

None survives cross-system falsification.

---

# 1. Need is qualifier-required

`Need` is as overloaded as `Value` was in HF4.

HF5 separates at least four uses.

## N1 — Viability requirement

A condition/resource/process whose absence beyond some range threatens continued
functioning or survival.

Examples:

```text
oxygen
water
adequate temperature regulation
basic nutrient supply
sleep-related restorative functions
```

This does not require conscious desire.

## N2 — Regulatory need / deviation pressure

A current or predicted regulatory condition that recruits compensatory or
anticipatory processes.

Examples:

```text
rising osmotic pressure
falling available glucose in a local context
accumulating sleep pressure
thermal imbalance
```

## N3 — Experienced need state

A first-person state such as:

```text
thirst
hunger
air hunger
sleepiness
thermal discomfort
```

This is evidence about regulation, not identical to the underlying regulated
variable.

## N4 — Psychological basic need

A theoretical class such as autonomy, competence and relatedness in
Self-Determination Theory.

This use has substantial empirical support in motivation/well-being research but
is not automatically the same causal architecture as osmoregulation or
thermoregulation.

Therefore:

```text
ViabilityNeed
!= RegulatoryNeed
!= ExperiencedNeed
!= PsychologicalBasicNeed
```

without a demonstrated relation.

---

# 2. Need is not desire

A Human can biologically require something without consciously desiring it.

Examples:

```text
oxygen need during sleep
fluid regulation before explicit thirst
thermal regulation before strong discomfort
```

Conversely, a Human can strongly desire something that is not required for
short-horizon viability.

Therefore:

```text
Need != Desire
Need != Wanting
```

This extends Game R18 and HF4 from a biological-regulatory angle.

---

# 3. Need is not merely deficit

A deficit-only model says:

```text
Need = current deviation below target
```

but anticipatory regulation can begin before large error appears.

Examples include:

```text
drinking in anticipation of future loss
moving to shade before dangerous hyperthermia
sleep scheduling before catastrophic performance decline
feeding behavior guided by learned meal timing
```

Therefore:

```text
RegulatoryNeed
can depend on predicted future state
```

and:

```text
Need != PresentDeficitOnly
```

HF5 does not claim every need is predictive; it retains prediction as one possible
regulatory mechanism.

---

# 4. Regulated variable, target and viable range

The thermostat metaphor hides several distinctions.

HF5 separates:

```text
RegulatedVariable V
ViableRange R
Reference / Target T
Comparator / Error function E
Controller C
Effector set F
```

A simple local feedback relation is:

```text
Error_t = T_t - V_t
Controller(Error_t) → Effectors → change V
```

But HF5 does not assume:

```text
T_t = one fixed constant forever
```

Targets can vary with:

```text
circadian phase
activity
age
reproductive state
environment
disease
learned anticipation
```

depending on the regulated domain.

Thus:

```text
RegulatedVariable != Target
Target != FixedUniversalSetpoint
```

---

# 5. Homeostasis

HF5 retains `Homeostasis` as:

> **the coordinated regulation that keeps viability-relevant internal variables
> or relations within functionally acceptable bounds despite perturbation.**

This is broader than perfect constancy.

It allows:

```text
ranges
oscillation
context-dependent targets
multiple effectors
behavioral effectors
cross-system tradeoffs
```

Therefore:

```text
Homeostasis != StaticConstancy
```

and:

```text
Homeostasis != OneThermostat
```

---

# 6. Regulatory loops are plural and coupled

One variable may be controlled through several effectors.

Likewise one effector can affect several regulated variables.

For example heat regulation interacts with:

```text
skin blood flow
sweating
blood pressure
fluid volume
behavior
activity level
```

Thus:

```text
RegulatorySystem
= interacting network of loops
```

rather than:

```text
one sensor → one controller → one effector
```

This matters because protecting one variable can worsen another.

```text
dehydration
→ conserve fluid
→ reduce sweating / heat dissipation
→ raise thermal risk
```

is a cross-regulatory tradeoff.

---

# 7. Behavioral regulation is regulation

A Human does not regulate only through autonomic/endocrine effectors.

Behavior can often act earlier and more powerfully:

```text
seek water
seek food
move to shade
put on clothing
stop exercising
sleep
change posture
seek social support
```

Therefore:

```text
BehavioralRegulation
is part of
OrganismicRegulation
```

and not merely a downstream consequence of physiology.

This reconnects HF5 to HF4 action allocation.

---

# 8. Allostasis

HF5 retains `Allostasis` only in a narrow useful role:

> **coordinated, context-sensitive and often anticipatory change in regulatory
> activity/targets/effectors that preserves viability or functional capacity under
> changing predicted demands.**

This is not a replacement word for all homeostasis.

A useful contrast is:

```text
Reactive correction:
observed deviation → compensatory action

Predictive / anticipatory regulation:
expected future demand → prepare before large deviation
```

Both can coexist.

Therefore:

```text
Feedback != Allostasis
Prediction != Homeostasis
```

are false dichotomies.

The better rule is:

```text
Feedback regulation
and
anticipatory regulation
can cooperate in one system
```

---

# 9. Allostasis is not any state change

If all state change is called allostasis, the term loses explanatory value.

HF5 therefore requires at least:

```text
regulatory target / function
context or predicted demand
coordinated effectors
change that improves future regulation under that demand
```

before `allostatic` is a useful claim.

So:

```text
StateChange != Allostasis
```

---

# 10. Allostatic load

HF5 uses `AllostaticLoad` for accumulated cost/risk associated with repeated,
prolonged, poorly terminated, poorly compensated or otherwise dysregulated
regulatory activation across systems.

Importantly:

```text
AcuteAdaptiveResponse
!= AllostaticLoad
```

A strong acute response can be useful.
A modest but chronically unresolved response can be costly.

Allostatic load is therefore fundamentally temporal and multi-system.

---

# 11. Allostatic load is not one universal score

Empirical allostatic-load research combines biomarkers differently across
studies.

Thus:

```text
AllostaticLoadConcept
!= UniversalAllostaticLoadMetric
```

A measured index must declare:

```text
which systems
which markers
which thresholds
which timescale
which population
```

before interpretation.

No single cortisol measurement can establish chronic allostatic load.

---

# 12. Interoception begins below experience

HF5 rejects:

```text
Interoception = consciously feeling the body
```

as too narrow.

A minimum chain is:

```text
InternalPhysicalState
→ receptor/transduction
→ afferent signal
→ central representation / integration
→ possible action/regulation
→ possible bodily experience
→ possible report
```

Not every internal signal becomes conscious.

Therefore:

```text
InteroceptiveSignal != InteroceptiveExperience
```

---

# 13. Interoceptive representation is not direct readout

Internal sensing is noisy, partial and distributed.

Central representations can integrate:

```text
afferent signals
prior expectations
context
attention
memory
action consequences
```

HF5 therefore allows predictive/inferential models of interoception as rivals
without assuming every bodily feeling is hallucinated inference.

The durable law is:

```text
PeripheralState != CentralRepresentation
```

and:

```text
CentralRepresentation != DirectPerfectCopy
```

---

# 14. Interoceptive performance, belief and metacognition

Heartbeat paradigms demonstrate at least:

```text
InteroceptiveAccuracy
InteroceptiveSensibility
MetaInteroceptiveAwareness
```

can dissociate.

HF5 therefore defines:

```text
InteroceptiveAccuracy
= performance on a declared task estimating internal state

InteroceptiveSensibility
= self-reported belief/tendency regarding bodily perception

MetaInteroceptiveAccuracy
= correspondence between confidence and objective interoceptive performance
```

and retains:

```text
Accuracy != Sensibility != MetaAccuracy
```

---

# 15. Interoception is domain-specific unless shown otherwise

Accurately detecting heartbeat does not automatically establish equivalent
accuracy for:

```text
hunger
thirst
respiration
pain
temperature
bladder state
fatigue
```

Therefore:

```text
InteroceptiveAbility_D
!= InteroceptiveAbility_E
```

without evidence.

HF5 rejects one universal `body awareness score` as a foundation primitive.

---

# 16. Hunger

HF5 defines hunger minimally as a state that increases food-seeking/consumption
priority through physiological, learned, cognitive and affective processes.

It is not identical to one energy variable.

```text
Hunger != EnergyDeficit
```

because meal timing, cues, expectation, learned context and induced sensations can
change hunger/desire even without identical physiological deficits.

---

# 17. Satiation versus satiety

HF5 separates:

```text
Satiation
= within-meal processes contributing to meal termination

Satiety
= post-meal state reducing subsequent food-seeking/consumption over an interval
```

Thus:

```text
Satiation != Satiety
```

Neither is simply:

```text
no hunger
```

because hedonic wanting, learned cues and context can remain active.

---

# 18. Satiety is not liking

A food can remain pleasant after physiological need has fallen.

Likewise a satiated Human can still experience cue-triggered wanting.

Therefore:

```text
Satiety != Liking
Satiety != Wanting
```

This reconnects directly to HF4.

---

# 19. Thirst

Thirst is an experienced motivational/interoceptive state within a larger
body-fluid control system.

The wider system includes:

```text
osmolality
blood volume
hormonal signals
brainstem/hypothalamic processing
behavioral drinking
kidney regulation
```

Thus:

```text
ThirstExperience != Osmolality
```

and:

```text
DrinkingBehavior != ThirstExperience
```

A Human can drink anticipatorily or because of social/contextual cues before
strong thirst.

---

# 20. Thermoregulation

Temperature regulation provides a powerful falsifier of purely internal
physiological control.

A Human can regulate by:

```text
moving
changing clothing
changing activity
seeking shade/heat
changing fluid intake
```

before dangerous core-temperature deviation occurs.

Thus:

```text
BehavioralThermoregulation
!= AutonomicThermoregulation
```

but both belong to the same broader regulatory problem.

---

# 21. Thermal sensation versus discomfort

Thermal sensation answers approximately:

```text
How warm/cold does this feel?
```

Thermal discomfort answers:

```text
How aversive / action-demanding is this thermal state?
```

These can dissociate.

Therefore:

```text
ThermalSensation != ThermalDiscomfort
```

HF5 treats discomfort as one possible bridge from internal/environmental state to
behavioral regulation.

---

# 22. Sleep need and sleep pressure

Sleep provides another strong counterexample to one-state-variable models.

The two-process framework separates:

```text
Process S
= sleep-wake-dependent homeostatic pressure

Process C
= circadian timing influence
```

Therefore:

```text
SleepPressure != CircadianDrive
```

A person can be physiologically sleep-deprived while circadian wake drive
partially masks subjective sleepiness.

---

# 23. Sleep pressure is not subjective fatigue

Subjective fatigue/sleepiness, objective vigilance and EEG slow-wave dynamics can
move differently.

Thus:

```text
SleepPressure
!= SubjectiveSleepiness
!= SubjectiveFatigue
!= Performance
```

Slow-wave activity is an important indicator of sleep homeostasis, not the same
thing as `sleep need` itself.

---

# 24. Circadian regulation is a boundary condition on homeostasis

Many internal variables follow rhythms.

This means a target/reference can depend on phase:

```text
T = T(circadian_phase, activity, context)
```

rather than being one constant.

HF5 therefore retains:

```text
HomeostaticRegulation
can be phase-dependent
```

without treating circadian rhythm as allostasis by definition.

---

# 25. Pain is not nociception

Pain provides one of HF5's most important subjectivity falsifiers.

Nociception concerns neural encoding/processing of noxious stimulation.

Pain is an unpleasant sensory/emotional experience associated with or resembling
that associated with actual or potential tissue damage.

Therefore:

```text
Nociception != Pain
TissueDamage != Pain
```

This means a bodily regulatory signal cannot be inferred directly from subjective
experience, or vice versa.

---

# 26. Pain report is another downstream channel

HF2 already established:

```text
Experience != Report
```

HF5 applies it to pain:

```text
PainExperience != PainReport
```

Inability to communicate does not logically establish absence of pain.

Likewise verbal pain intensity does not uniquely identify tissue damage or one
nociceptive signal magnitude.

---

# 27. Stress needs a typed grammar

HF5 rejects naked technical use of `stress`.

At minimum distinguish:

```text
Stressor
Appraisal / inferred demand
StressResponse
StressMediator
SubjectiveStressExperience
RecoveryTrajectory
ChronicStressExposure
AllostaticLoad
```

These can correlate while remaining different objects.

---

# 28. Stressor

A `Stressor` is an event/condition that perturbs or threatens valued/regulated
states under a particular organism/context.

The same event need not generate the same stress response across Humans.

Thus:

```text
StressorProperty
!= StressResponseMagnitude
```

because appraisal, controllability, predictability, history and state matter.

---

# 29. Acute stress response can be adaptive

Acute mobilization can support:

```text
attention
energy availability
cardiovascular output
immune redistribution
action readiness
memory/plasticity
```

Therefore:

```text
StressResponse != Damage
```

The relevant question is often trajectory:

```text
appropriate activation?
appropriate magnitude?
appropriate duration?
appropriate termination?
appropriate recovery?
```

---

# 30. Stress hormone is not stress

Cortisol, catecholamines and other mediators are components of some stress
responses.

Therefore:

```text
Cortisol != Stress
```

One hormone level cannot fully represent:

```text
stressor
subjective state
multiple physiological systems
chronic load
recovery
```

HF5 treats biomarkers as scoped evidence channels.

---

# 31. Stress response has a trajectory

A more useful representation is:

```text
baseline
→ anticipatory rise
→ response peak/profile
→ termination
→ recovery
→ possible adaptation / residual change
```

Two Humans with the same peak can differ in:

```text
onset speed
recovery speed
overshoot
habituation
residual load
```

Thus:

```text
PeakResponse != WholeStressResponse
```

---

# 32. Fatigue

HF5 finds `Fatigue` to be another qualifier-required family.

At least distinguish:

```text
SubjectiveFatigue
TaskSpecificPerformanceFatigue
PhysiologicalFatigue
CentralMotorFatigue
CognitiveFatigue
Sleepiness
EffortCostShift
```

These need not covary perfectly.

---

# 33. Subjective fatigue

Working definition:

```text
SubjectiveFatigue
= experienced sense of reduced readiness/capacity or increased cost associated
  with continued exertion or wakeful functioning
```

This is a first-person state.

It is not identical to objective performance decline.

```text
SubjectiveFatigue != PerformanceDecline
```

---

# 34. Performance fatigue

A task can show declining output/accuracy/speed over time.

That decline can arise from:

```text
muscle physiology
attention
strategy
motivation
pain
heat
sleep pressure
learning/interference
```

Thus:

```text
PerformanceDecline != OneFatigueMechanism
```

---

# 35. Fatigue is not one fuel gauge

The tempting model is:

```text
Resource R starts full
work consumes R
fatigue reports remaining R
rest refills R
```

HF5 rejects this as a universal foundation model.

Why?

Because:

```text
subjective fatigue can rise without proportional performance loss
performance can be preserved despite fatigue
incentives can temporarily alter effort allocation
deadline proximity can increase effort after prolonged work
cognitive fatigue can alter later physical effort valuation
```

Therefore:

```text
FatigueExperience != ResourceRemaining
```

without independent resource evidence.

---

# 36. Fatigue can be regulatory without being fake

Rejecting a simple fuel gauge does not imply fatigue is unreal or irrelevant.

A fatigue signal may still summarize/integrate:

```text
prior exertion
sleep pressure
metabolic/immune state
expected future demand
opportunity cost
pain
thermal state
confidence in continued performance
```

and influence behavior.

HF5 therefore retains fatigue as a **state/evidence/control variable family**,
not as a proven one-dimensional depleted substance.

---

# 37. Fatigue is domain-sensitive

HF5 does not assume:

```text
CognitiveFatigue = PhysicalFatigue
```

Yet cross-domain effects exist: prolonged cognitive work can alter subsequent
physical-effort valuation.

Therefore:

```text
Fatigue_D != Fatigue_E
```

but:

```text
Fatigue_D can modulate Cost_E
```

under some conditions.

This is a relation to investigate, not an identity.

---

# 38. Recovery

`Recovery` is frequently treated as obvious, but HF5 finds it underspecified.

Recovery from what?

Possible targets include:

```text
subjective fatigue
performance
heart rate / cortisol
sleep pressure
muscle force
inflammation
pain
attention
working memory
motivation
```

Therefore:

```text
Recovery_D
```

must specify the property/domain.

---

# 39. Recovery is not rest

`Rest` is an intervention/context.

`Recovery` is a change in a target property.

Thus:

```text
Rest != Recovery
```

Rest can fail to restore one endpoint while restoring another.

Likewise active exercise can sometimes improve mental-fatigue outcomes differently
from passive rest.

---

# 40. Recovery is not time passage

The passage of time can coincide with recovery, non-recovery or deterioration.

Therefore:

```text
ElapsedTime != RecoveryAmount
```

A recovery claim needs longitudinal evidence about the relevant variable.

---

# 41. Return to baseline is not complete restoration

Suppose cortisol returns to pre-stressor level.

This does not prove:

```text
all neural states restored
all immune states restored
all learned associations erased
future stress response unchanged
subjective state restored
```

Therefore:

```text
MarkerBaselineReturn
!= WholeSystemRestoration
```

The system may have learned/adapted while the marker normalizes.

---

# 42. Recovery can include compensation and reorganization

A Human may regain function through a changed internal organization.

Thus:

```text
RecoveredFunction
!= SameInternalStateAsBefore
```

This becomes especially important in injury, chronic stress, learning and aging.

HF5 therefore treats recovery as a trajectory, not a rewind operation.

---

# 43. Habituation is not recovery

Repeated exposure can reduce future response magnitude.

That is `Habituation` only under specific learning criteria.

Recovery concerns return/change after one response episode.

Therefore:

```text
Habituation != Recovery
```

A system can recover fully from each episode without habituating across episodes,
or habituate despite incomplete recovery.

---

# 44. Adaptation is not recovery

Adaptation means the system changes such that future interaction with a recurring
condition differs.

Recovery means some target property moves toward a post-perturbation functional
state.

Thus:

```text
Adaptation != Recovery
```

A Human can adapt by changing baseline/strategy/capacity rather than returning to
its previous configuration.

---

# 45. Resilience is not no response

A resilient system can mount a strong response and recover effectively.

Thus:

```text
Resilience != LowStressResponse
```

Resilience can involve:

```text
maintained function
rapid recovery
successful adaptation
flexible strategy change
preserved future capacity
```

under adversity.

This already points beyond HF5.

---

# 46. Recovery profiles are multidimensional

HF5 therefore uses:

```text
RecoveryProfile(event, H) = {
  subjective recovery,
  performance recovery,
  physiological recovery,
  behavioral re-engagement,
  capacity restoration,
  residual structural change,
  future response change
}
```

The dimensions need not move together.

---

# 47. Internal state is not one vector with fixed meaning

HF4 had:

```text
HumanState_t
```

HF5 improves it to a layered state representation:

```text
PhysicalState
RegulatoryState
RepresentedState
ExperiencedState
ActionAllocationState
```

For example:

```text
osmotic change
→ regulatory signals
→ central representation
→ thirst experience
→ drinking priority
```

The arrows can be modulated and do not imply identity.

---

# 48. Minimum regulation grammar

HF5's minimum reusable grammar is:

```text
World + Body + History
        ↓
Physical / viability-relevant variables
        ↓
Sensors / internal signals
        ↓
Central representations / estimates
        ↓
Regulatory comparison / prediction
        ↓
Priority / need state / affect / action allocation
        ↓
Effectors
   ├─ autonomic
   ├─ endocrine
   ├─ immune
   ├─ motor
   ├─ cognitive
   └─ behavioral/environmental
        ↓
Changed Body + Changed World
        ↓
New internal evidence
        ↺
```

Over longer time:

```text
Repeated loop
→ learning / habituation / sensitization / plasticity / structural change
→ changed future regulator
```

The second loop is the residual HF5 cannot finish.

---

# 49. Need should be modeled as relation

A useful formal placeholder is:

```text
Need_D(H,t | viability/function domain D)
```

rather than:

```text
Need(H)=one list
```

A need claim should declare:

```text
what function/viability domain?
what timescale?
what evidence?
what failure consequence?
what regulatory mechanism?
```

This prevents importing a biological `need` criterion into psychological or
normative domains without evidence.

---

# 50. Psychological basic needs stay separate

Self-Determination Theory proposes autonomy, competence and relatedness as basic
psychological needs.

HF5 does not reject that research program.

It simply refuses this equation:

```text
AutonomyNeed
has same mechanism as
OsmoticWaterNeed
```

without evidence.

Thus:

```text
PsychologicalBasicNeed
!= PhysiologicalRegulatoryNeed
```

The common word `need` marks a theoretical analogy, not automatic mechanistic
identity.

---

# 51. Need satisfaction is not necessarily classic satiation

Some psychological-need evidence suggests unmet needs can increase corresponding
desire while surplus satisfaction does not simply extinguish the motive in the
same way as a classic deficit-correction model would predict.

Therefore HF5 retains:

```text
PsychologicalNeedDynamics
may differ from
PhysiologicalDeficitCorrection
```

This is exactly why qualifier-required terminology matters.

---

# 52. Cross-context falsifier matrix

| Case | Naive equivalence attacked | HF5 surviving distinction |
|---|---|---|
| anticipatory drinking | need = current conscious deficit | regulation can precede strong experienced need |
| satiated food still liked | satiety = no reward | satiety != liking |
| cue-induced food wanting | hunger = energy deficit | learned/contextual signals alter food motivation |
| thirst ratings vary among similar physiology | subjective need = physical variable | experience != regulated variable |
| thermal discomfort drives behavior | homeostasis = autonomic physiology | behavioral regulation is part of control |
| dehydration suppresses sweating | each variable independently regulated | coupled regulatory loops trade off |
| circadian wake drive masks sleep pressure | sleepiness = sleep need | Process S != Process C != report |
| pain without proportional tissue damage | pain = nociception | experience != nociceptive/tissue state |
| acute stress improves action readiness | stress = damage | adaptive response != chronic load |
| cortisol normalizes after stress | marker baseline = total recovery | one endpoint != whole-system restoration |
| high fatigue with maintained performance | fatigue = performance loss | experience != output |
| incentive changes performance despite fatigue | fatigue = depleted fixed fuel | effort allocation can change without proving refill |
| mental fatigue changes later physical effort valuation | fatigue is domain-isolated | cross-domain cost modulation without identity |
| passive rest vs exercise recovery differ | rest = recovery | intervention != recovered endpoint |
| repeated stress response shrinks | recovery = habituation | within-episode recovery != across-episode adaptation |
| resilient strong responder | resilience = weak response | resilience can involve effective response + recovery |
| psychological need satisfaction | all need = biological deficit | psychological-need theory requires separate mechanism |

---

# 53. Competing models

## M1 — fixed-setpoint thermostat

```text
one regulated variable
one fixed setpoint
error correction
```

### Strength

Excellent local model for some feedback processes.

### Failure

Circadian targets, multiple effectors, behavioral regulation, interacting loops and
anticipatory responses exceed the simple form.

**Disposition:** retain as local control model, reject as complete Human
regulation ontology.

## M2 — predictive allostasis as primary regulator

### Strength

Explains anticipation, flexible targets and coordinated resources.

### Failure

Feedback remains ubiquitous and allostasis lacks one universally agreed precise
operational definition.

**Disposition:** retain as strong rival/complement, not final ontology.

## M3 — direct interoceptive readout

```text
body state → accurate conscious feeling
```

### Failure

Signal, representation, task accuracy, self-report sensibility, metacognition and
experience dissociate.

**Disposition:** reject.

## M4 — need-as-drive

```text
deficit → drive magnitude → action
```

### Strength

Useful coarse model in some biological contexts.

### Failure

Predictive regulation, learned/contextual hunger, psychological need theories,
action alternatives and multiple state dimensions.

**Disposition:** reject as universal model.

## M5 — stress-is-harm

### Failure

Acute stress can be adaptive; damage depends on duration, context, recovery and
chronic load.

**Disposition:** reject.

## M6 — fatigue-as-resource-gauge

```text
fatigue ∝ resource depletion
```

### Failure

Subjective fatigue, performance, reward, opportunity, sleep pressure and domain
transfer dissociate.

**Disposition:** reject as universal foundation; retain specific physiological
resource constraints where independently measured.

## M7 — recovery-as-baseline-return

### Failure

Different endpoints recover at different rates, and adaptation/plasticity can
change the system despite baseline normalization of one marker.

**Disposition:** reject as complete recovery model.

---

# 54. HF5 anti-laws

## Need

1. `Need != Desire`.
2. `Need != Wanting`.
3. `Need != PresentDeficitOnly`.
4. `ViabilityNeed != ExperiencedNeed`.
5. `PhysiologicalRegulatoryNeed != PsychologicalBasicNeed`.
6. `Need` without domain/timescale is underspecified.

## Regulation

7. `RegulatedVariable != Target`.
8. `Target != FixedUniversalSetpoint`.
9. `Homeostasis != StaticConstancy`.
10. `Homeostasis != OneThermostat`.
11. `BehavioralRegulation != AutonomicRegulation`.
12. `StateChange != Allostasis`.
13. `Feedback != only regulation`.
14. `Prediction != only regulation`.
15. `AcuteAdaptiveResponse != AllostaticLoad`.
16. `AllostaticLoadConcept != UniversalAllostaticLoadMetric`.

## Interoception

17. `InternalPhysicalState != AfferentSignal`.
18. `AfferentSignal != CentralRepresentation`.
19. `CentralRepresentation != BodilyExperience`.
20. `InteroceptiveSignal != InteroceptiveExperience`.
21. `InteroceptiveAccuracy != Sensibility`.
22. `InteroceptiveAccuracy != MetaInteroceptiveAccuracy`.
23. `InteroceptiveAbility_D != InteroceptiveAbility_E`.

## Hunger / thirst / temperature / sleep / pain

24. `Hunger != EnergyDeficit`.
25. `Satiation != Satiety`.
26. `Satiety != Liking`.
27. `Satiety != Wanting`.
28. `ThirstExperience != Osmolality`.
29. `DrinkingBehavior != ThirstExperience`.
30. `ThermalSensation != ThermalDiscomfort`.
31. `SleepPressure != CircadianDrive`.
32. `SleepPressure != SubjectiveFatigue`.
33. `SlowWaveActivity != SleepNeed itself`.
34. `Nociception != Pain`.
35. `TissueDamage != Pain`.
36. `PainExperience != PainReport`.

## Stress

37. `Stressor != StressResponse`.
38. `StressResponse != StressExperience`.
39. `StressMediator != Stress`.
40. `Cortisol != Stress`.
41. `AcuteStressResponse != Damage`.
42. `StressResponse != AllostaticLoad`.
43. `PeakResponse != WholeStressTrajectory`.

## Fatigue

44. `SubjectiveFatigue != PerformanceDecline`.
45. `Fatigue != SleepPressure`.
46. `Fatigue != EffortCost`.
47. `Fatigue != ResourceRemaining`.
48. `PerformanceDecline != OneFatigueMechanism`.
49. `Fatigue_D != Fatigue_E`.

## Recovery / adaptation

50. `Rest != Recovery`.
51. `ElapsedTime != RecoveryAmount`.
52. `MarkerBaselineReturn != WholeSystemRestoration`.
53. `RecoveredFunction != SameInternalStateAsBefore`.
54. `Habituation != Recovery`.
55. `Adaptation != Recovery`.
56. `Resilience != NoStressResponse`.
57. `Recovery_D != Recovery_E` without evidence.

---

# 55. Human × AI implication

HF5 gives strong constraints for Human-facing Agents.

An Agent must not infer:

```text
user says “tired”
→ objective capacity is depleted by X%

user reports no pain
→ no nociception / no injury

heart rate/cortisol high
→ user is psychologically stressed

user skipped a meal
→ hunger intensity known
```

A safer record separates:

```text
ObservedPhysiology
SelfReport
Behavior
Context
ModelInference
Uncertainty
```

and declares the endpoint being inferred.

---

# 56. Agent support can alter regulation without changing internal capacity

An Agent can help a Human regulate by changing:

```text
schedule
environment
sleep opportunity
work/rest timing
hydration reminders
heat exposure
information load
precommitment
stressful task structure
```

This can improve situated regulation without proving intrinsic biological capacity
has changed.

Thus HF1's capability distinction remains:

```text
InternalCapacity
!= SituatedRegulatoryCapability
```

---

# 57. Measurement rule

Any HF5 claim should declare:

```text
1. regulated domain / construct
2. timescale
3. physical variable or subjective state
4. evidence channel
5. intervention/perturbation
6. expected feedback or predictive path
7. behavioral/autonomic/endocrine effectors
8. false-positive / false-negative paths
9. recovery endpoint
10. history / prior exposure
```

This avoids one-marker explanations.

---

# 58. Reconnection to HF4

HF4 had:

```text
DecisionValue
= F(outcomes, delay, uncertainty, effort, opportunity, state, history)
```

HF5 expands `state` into:

```text
PhysicalState
RegulatoryState
InteroceptiveRepresentation
ExperiencedState
```

Thus:

```text
same outcome
+ different regulatory state
→ different current value / action allocation
```

without turning state into a single motivation scalar.

---

# 59. Reconnection to HF2 / HF3

HF2 established:

```text
Experience != Evidence
```

HF5 gives bodily examples:

```text
Pain != Nociception
Thirst != Osmolality
Fatigue != Performance
```

HF3 established typed access and metacognition.

HF5 applies it to interoception:

```text
body signal may guide regulation/action
without
accurate report or meta-awareness
```

Therefore bodily regulation is deeply coupled to cognition but not reducible to
conscious access.

---

# 60. Reconnection to World / Resource

The body is not merely a container of cognition.

It is a resource-constrained, self-regulating system that must continuously
allocate:

```text
water
heat
oxygen
metabolic substrate
attention
time
recovery opportunity
behavioral options
```

while dealing with uncertainty and future demands.

This produces a deep connection:

```text
Regulation
= resource allocation under viability constraints across time
```

but HF5 does not reduce physiology to finance-style utility optimization.

---

# 61. What HF5 does not establish

HF5 does not establish:

- one universal definition of biological or psychological need;
- that psychological basic needs are false;
- that physiological and psychological needs share one mechanism;
- that every regulated variable has a fixed setpoint;
- that every regulated variable lacks a target;
- that allostasis replaces homeostasis;
- that predictive coding is the final theory of interoception;
- that heartbeat-task accuracy generalizes to all bodily sensing;
- that hunger is merely learned cognition;
- that hunger is merely metabolic deficit;
- that thirst always tracks osmolality linearly;
- that sleep pressure is one molecule;
- that slow-wave activity is sleep need itself;
- that pain is independent of tissue/nociceptive processes;
- that all stress is beneficial;
- that chronic stress is harmless;
- one universal allostatic-load biomarker bundle;
- that fatigue has no physiological resource constraints;
- that fatigue is purely motivational or opportunity-cost based;
- that rest never helps recovery;
- that active recovery is always superior;
- that resilience is one stable personality trait;
- that return to baseline has no meaning;
- one final model of recovery.

---

# 62. The residual HF5 cannot finish

HF5 repeatedly discovers that regulatory response is history-dependent.

Examples:

```text
same repeated stressor
→ smaller response (habituation)

repeated/chronic stress
→ altered future response architecture

training
→ changed thermoregulation / effort capacity

sleep history
→ changed homeostatic pressure dynamics

recovery
→ may restore function while leaving changed future response

adversity
→ can produce resilience or vulnerability
```

The object changing is no longer only the current state.

It is the **system's future transition function**.

A useful abstraction is:

```text
State_{t+1} = F_t(State_t, Input_t, Action_t)
```

where experience/history can modify:

```text
F_t → F_{t+1}
```

That is a plasticity/adaptation problem.

---

# 63. Exact next foundation

HF5 therefore selects:

# HF6 — Adaptation, Learning, Plasticity, Habituation, Sensitization, Resilience, Development and Aging

The next round should ask:

1. What is `Adaptation`: current compensation, persistent changed response,
   learning, structural change, or any improved fit?
2. How is physiological adaptation different from learning?
3. What is plasticity relative to adaptation and capability change?
4. How should habituation differ from extinction, fatigue, tolerance and reduced
   sensory response?
5. What is sensitization relative to vigilance, learning and pathology?
6. What is resilience: maintenance, recovery, adaptation, resistance or growth?
7. How do beneficial short-term adaptations become maladaptive over longer
   timescales?
8. How does developmental stage constrain possible adaptation?
9. How does aging change regulation, plasticity, recovery and reserve?
10. How should irreversible versus reversible change be represented?
11. When is a new baseline evidence of adaptation versus unresolved load?
12. What is retained capability versus transient state after training/practice?
13. How should historical path dependence be represented in Human identity and
    capability?
14. What next boundary is forced after transition-function change is decomposed?

HF6 should not predefine HF7.

---

# 64. HF5 synthesis

HF5 began from:

```text
What is Human State?
```

and found that `state` is not one variable.

The minimum surviving architecture is:

```text
Physical state
→ internal signals
→ representations/estimates
→ regulatory comparison/prediction
→ affect/need/priority
→ autonomic/endocrine/immune/behavioral effectors
→ changed body + world
→ new evidence
```

while first-person states such as:

```text
hunger
thirst
pain
fatigue
thermal discomfort
stress
```

are neither mere noise nor direct readouts of one physiological variable.

The deepest compression is:

```text
The living Human does not merely act on the world.
The Human must continuously regulate the conditions that make future action and
continued functioning possible.
```

And regulation is not a static thermostat.

It is:

```text
multi-variable
multi-effector
behaviorally extended
context-sensitive
partly predictive
history-dependent
```

HF5 closes exactly where the current regulatory system itself begins to change
through experience and time — the HF6 adaptation/plasticity boundary.
