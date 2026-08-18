---
schema_version: 1
id: human.deep-foundations.hd12a
profile: research
lifecycle: completed
source_role: research-decision
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
  - engineer
updated: 2026-08-18
summary: HD12-A reconstructs the vocabulary and hidden assumptions of Human temporal cognition before any timing theory is selected. It rejects `time perception` as one target and separates objective/physical temporal relations from Human judgments of duration, order, simultaneity, sequence, rhythm/beat, synchronization, prospective/retrospective duration, passage-of-time experience, intentional/causal temporal binding, circadian phase and future-oriented memory/planning. Task form is treated as constitutive evidence metadata: discrimination, bisection, estimation, reproduction, production, temporal-order judgment and simultaneity judgment can differ in memory, attention, motor and decision demands. Primary evidence shows TOJ and SJ can dissociate; duration judgment and passage-of-time experience can dissociate; retrospective duration depends strongly on remembered event structure; intentional binding is task-sensitive and not a transparent agency meter; absolute interval and beat-based timing can dissociate causally; auditory duration/sequence/beat relations need not generalize to vision; perceptual rhythm learning need not reduce to motor timing. `TemporalCognition` therefore remains an umbrella research space, not a primitive. The strongest provisional common object after A is `TemporalRelationEstimationEpisode`: Human evidence about a declared temporal target is transformed under context/prior, memory, attention, modality and response mapping into a judgment/action with accuracy, precision and bias separately typed. This is not HF24. HD12-B is admitted next for rival-model and measurement decomposition: dedicated clock/pacemaker-accumulator, multiple timing systems, state-dependent/distributed timing, Bayesian/contextual inference, memory/decision accounts, modality-specific hierarchies and action-prediction accounts must explain the same task battery without redefining `time`.
evidence_status: verified-synthesis
readiness: COMPLETE
related:
  - human.deep-foundations.hd12.continuation
  - human.deep-foundations.hd12a.sources
---
# HD12-A — Current-Use / Term Separation / Hidden-Assumption Inventory

## 0. Entry rule

HD12 is a deep route, not a Foundation.

```text
HD12Admission != HF24Admission
```

A does not select a timing theory. It asks what the field is actually measuring when it says `time perception`.

---

# 1. First separation — physical time is not Human temporal judgment

World-side objects may include:

```text
PhysicalDuration(e1,e2)
PhysicalOrder(e1,e2)
PhysicalSimultaneity(e1,e2,tolerance)
PhysicalPeriodicity(sequence)
Timestamp(event)
ClockTime
```

Human-side objects include judgments/experiences relative to evidence and task.

Therefore:

```text
PhysicalDuration != PerceivedDuration
ObjectiveOrder != ReportedOrder
ObjectiveSimultaneity != SubjectiveSimultaneity
TimestampAccuracy != HumanTemporalAccuracy
```

World retains objective temporal truth.

---

# 2. `time perception` is an umbrella, not a target

Current usage may refer to materially different questions:

```text
How long?
Which came first?
Were these simultaneous?
Is this interval longer than that one?
What rhythm is present?
Where is the beat?
Can I synchronize to it?
How fast does time seem to pass?
How long ago did this event feel?
When should I act?
Did my action and outcome feel temporally compressed?
```

These are not interchangeable.

Retain:

```text
TemporalCognition
= research umbrella
!= one primitive target
```

---

# 3. Duration

`Duration` concerns extent between temporal boundaries under a declared reference.

Separate:

```text
PhysicalDuration
PerceivedDuration
RememberedDuration
ProducedDuration
ReproducedDuration
VerbalEstimatedDuration
```

A Human may judge the same physical interval differently across tasks.

---

# 4. Interval timing

`IntervalTiming` is a task/process family for estimating/comparing/producing elapsed intervals.

It may include:

```text
discrimination
bisection
categorization
estimation
reproduction
production
```

Do not infer:

```text
SameNominalDuration
→ SameTimingProcess
```

because task-specific memory, motor and decision demands differ.

---

# 5. Estimation, reproduction and production are distinct

```text
TimeEstimation
= map experienced/remembered interval to symbolic/numeric/verbal response

TimeReproduction
= generate an interval judged to match a reference interval

TimeProduction
= generate an interval matching an instructed target duration
```

Thus:

```text
TimeEstimation != TimeReproduction != TimeProduction
```

A reproduction error can contain motor output variance that a verbal estimate does not.

---

# 6. Temporal order

`TemporalOrderJudgment` asks which event occurred first/second.

Its target is relational direction:

```text
A before B
B before A
```

not elapsed duration itself.

Therefore:

```text
Duration != TemporalOrder
```

---

# 7. Simultaneity

`SimultaneityJudgment` asks whether events are judged simultaneous under a task-defined tolerance/criterion.

A 2019 audiovisual study found rapid recalibration in TOJ but not SJ and no reliable within-person correlation between their points of subjective simultaneity.

Therefore:

```text
TemporalOrderJudgment
!= SimultaneityJudgmentByDefinition
```

and:

```text
PointOfSubjectiveSimultaneity_TOJ
!= PointOfSubjectiveSimultaneity_SJ
```

without evidence linking them.

---

# 8. Synchrony

Use `Synchrony_D` because it may mean:

```text
physical phase alignment
perceived simultaneity
cross-modal temporal correspondence
motor synchronization
interpersonal synchrony
neural phase locking
```

HF11 already freezes:

```text
Coordination != Synchrony
```

HD12 adds:

```text
PerceivedSynchrony != MotorSynchronization
```

---

# 9. Temporal resolution

Temporal resolution concerns sensitivity to temporal differences/boundaries, not absolute duration accuracy.

Possible measures:

```text
just-noticeable difference
order threshold
simultaneity window
gap detection
```

Therefore:

```text
TemporalResolution
!= DurationEstimateAccuracy
```

---

# 10. Temporal sequence

A sequence contains multiple ordered intervals/events.

Representational demands can include:

```text
item identity
order
interval pattern
relative timing
repetition/periodicity
```

Thus:

```text
SingleIntervalTiming
!= SequenceTimingByDefinition
```

---

# 11. Rhythm

`Rhythm` refers to structured temporal patterning across multiple events/intervals.

It need not contain a regular beat.

Therefore:

```text
Rhythm != Beat
```

---

# 12. Beat

Beat is a psychologically salient periodic pulse inferred/extracted from some rhythmic sequences.

2026 auditory/visual work supports a duration→sequence→beat hierarchy in audition but not the same hierarchy in vision.

Therefore:

```text
BeatPerception != DurationPerceptionByDefinition
TimingHierarchy_Auditory != TimingHierarchy_VisualByDefault
```

---

# 13. Meter

Meter concerns hierarchical grouping/accent structure relative to periodic pulses in music/rhythm research.

It is more structured than generic periodicity.

```text
Meter != Beat != Rhythm
```

Media retains external musical/artifact structure; HD12 only studies Human extraction/use of temporal structure.

---

# 14. Entrainment

`Entrainment_D` can refer to synchronization of neural, perceptual or motor dynamics to periodic input.

Do not collapse:

```text
NeuralEntrainment
PerceptualBeatExtraction
MotorSynchronization
```

A 2025 study found neural beat entrainment and working memory jointly predicted sensorimotor synchronization skill; this is evidence for composition, not identity.

---

# 15. Motor synchronization

Motor synchronization is a control/action target involving phase/tempo matching of action to an external/internal temporal structure.

HF11 owns execution/control.

HD12 keeps only the timing relation necessary to compare perception with action.

```text
BeatPerception != AbilityToTapInSynchrony
```

Classic beat batteries and causal stimulation studies support partial dissociation between perceptual and production/synchronization components.

---

# 16. Absolute interval vs beat-based timing

Cerebellar cTBS experiments selectively disrupted single-interval duration timing without equivalent disruption of beat-based relative timing.

Therefore:

```text
AbsoluteIntervalTiming
!= BeatBasedRelativeTiming
```

This directly falsifies one flat `timing ability` account.

---

# 17. Perceptual rhythm vs motor rhythm

2026 rhythm-learning experiments found reliable implicit learning when temporal structure was in visual perception, including without rhythmic motor timing, but not when temporal structure existed only in motor responses.

Thus:

```text
TemporalRhythmLearning
!= RepeatedMotorTiming
```

HF11 cannot absorb all rhythm learning.

---

# 18. Prospective timing

`ProspectiveTiming` means the Human knows during the interval that a duration judgment will be required.

This can increase deliberate temporal attention/monitoring.

Do not confuse with HF7 prospective memory.

```text
ProspectiveTiming
!= ProspectiveMemory
```

The former is timing under prior temporal-task awareness; the latter is remembering to execute an intention later.

---

# 19. Retrospective timing

`RetrospectiveTiming` means duration judgment is requested after an interval that was not originally experienced under an explicit timing instruction.

It can depend strongly on remembered contextual/event structure.

2025 naturalistic-event work found retrospective duration judgments changed with remembered event boundaries and forgetting over delay.

Thus:

```text
RetrospectiveDurationJudgment
!= OnlineClockReadoutByDefinition
```

and HF7 memory is a mandatory neighbor owner.

---

# 20. Prospective vs retrospective timing

Classic experimental work shows executive-control manipulations can shorten prospective reproductions while lengthening retrospective reproductions, consistent with different attention/context-memory contributions.

Therefore:

```text
ProspectiveTiming
!= RetrospectiveTiming
```

without evidence of one shared estimator.

---

# 21. Subjective passage of time

`PassageOfTimeJudgment` asks how fast/slow time seemed to pass, not how long the interval was.

2022 experiments changed perceived passage speed using visual change while leaving duration estimates relatively unaffected.

A 2026 emotion experiment likewise found affective ratings influenced passage-of-time judgments without corresponding duration-judgment effects in that design.

Therefore:

```text
SubjectivePassageOfTime
!= PerceivedDurationByDefinition
```

This is a major A-round separation.

HF2/HF21 are strong neighboring owners for experiential/affective aspects.

---

# 22. Temporal horizon

`TemporalHorizon` usually concerns how far into future/past a Human considers, values or plans.

That is primarily HF8/HF10/HF4 territory.

Therefore:

```text
TemporalHorizon
!= TimingAbility
```

and:

```text
FutureOrientation != TimePerception
```

---

# 23. Circadian phase and chronotype

Circadian phase is organismic timing relative to endogenous biological rhythms; chronotype is an individual pattern/preference/phase relation often measured behaviorally.

HF5 owns this state/regulation family.

```text
CircadianPhase != PerceivedDuration
Chronotype != TimingPrecision
```

Sleep/circadian state may modulate timing without owning temporal cognition.

---

# 24. Chronostasis

Chronostasis is an illusion in which the first percept after an action such as a saccade can appear temporally extended.

2024 evidence shows auditory input can reduce visual saccadic chronostasis.

Use it as a multisensory/action-boundary pressure case, not a general timing primitive.

```text
Chronostasis != SubjectivePassageOfTime
```

---

# 25. Temporal / intentional binding

`TemporalBinding_D` is task-dependent apparent attraction/compression of temporal relations between causally/action-related events.

Do not assume:

```text
TemporalBinding = SenseOfAgency
```

A 2024 preregistered-style experimental critique reported no evidence supporting a specifically `intentional` binding effect under its comparisons.

2025 work also found binding estimates vary across Libet-clock, interval-estimation and reproduction paradigms, with weak reliability/cross-task convergence.

Another 2025 study explicitly tested a spatial-working-memory explanation for Libet-clock binding.

Therefore:

```text
IntentionalBinding
!= TransparentAgencyMeter
```

HF1/HF11 retain agency/action ownership.

---

# 26. Timing accuracy, precision and bias

Every timing task should separate:

```text
Accuracy
Precision / Variability
Bias
CentralTendency
Scalar variability if modeled
ResponseCriterion
Confidence / Metacognition
```

Thus:

```text
AccurateMean != HighPrecision
LowBias != LowVariance
HighConfidence != AccurateTiming
```

HF3 owns metacognitive confidence/calibration.

---

# 27. Central tendency is not timing rate by definition

The 2025 large-sample latent-structure study supports:

```text
GeneralTimingFactor
+
CentralTendencyBiasFactor
```

across tested reproduction intervals.

Therefore a Human's pull toward the local interval distribution must be typed separately from raw timing sensitivity/rate.

```text
CentralTendencyBias
!= ClockRateByDefinition
```

---

# 28. Modality is a constitutive coordinate

Timing results can differ across:

```text
auditory
visual
tactile
multisensory
interoceptive
motor/action
```

Do not infer modality invariance from one task.

```text
Timing_Modal_A
!= Timing_Modal_B
```

unless transfer/common-factor evidence supports it.

---

# 29. Attention is a contributor, not timing by definition

HF3 already owns selection/access/control.

Attention manipulations can alter temporal judgments, including around eye movements.

Therefore:

```text
AttentionEffectOnTiming
!= AttentionIsTimingMechanism
```

---

# 30. Memory is a contributor, not duration by definition

HF7 already owns temporal-order memory and retrospective reconstruction.

```text
MemoryForWhen
!= DurationPerception
```

and:

```text
RememberedDuration
!= PerceivedDurationAtEncoding
```

without evidence linking them.

---

# 31. Affect/body state can modulate timing without owning it

2026 EEG work tests cardiac-phase and emotional influences on duration judgments; other passage-of-time experiments show affect may alter passage reports more strongly than duration estimates.

Therefore:

```text
AffectiveModulationOfTime
!= AffectiveOwnershipOfTiming
```

HF5/HF21 remain neighboring owners.

---

# 32. Task decomposition grammar

Every HD12 timing claim should minimally type:

```text
TemporalEvidenceEpisode = {
  objective temporal target,
  Human temporal target,
  task/paradigm,
  interval/range/timescale,
  modality,
  stimulus/event structure,
  prospective-vs-retrospective instruction,
  attention demand,
  working-memory demand,
  episodic-memory demand,
  motor/output demand,
  symbolic/numeric mapping demand,
  comparison/reference distribution,
  prior/context,
  feedback/training,
  response rule,
  accuracy,
  precision,
  bias,
  confidence/metacognition,
  organism state,
  affect/arousal,
  action/agency relation,
  support/tool/Agent contribution,
  uncertainty
}
```

This is a research evidence grammar, not a Foundation object.

---

# 33. Strongest provisional common object after A

The broad term `TemporalCognition` is too heterogeneous.

The strongest provisional reusable object is narrower:

```text
TemporalRelationEstimationEpisode
```

where a Human forms/uses a judgment/action about a declared temporal relation from noisy/contextual evidence.

Provisional form:

```text
TemporalRelationEstimationEpisode = {
  target_relation,
  evidence,
  temporal scale,
  modality,
  context/prior,
  memory contribution,
  attention/control contribution,
  action contribution,
  response mapping,
  estimate/judgment,
  accuracy,
  precision,
  bias,
  confidence
}
```

Status:

```text
PROVISIONAL RESEARCH OBJECT
!= HF24
```

It may still reduce into HF20/HF3/HF7/HF8/HF11 plus task-specific decision machinery.

---

# 34. Hidden-assumption inventory

A identifies at least these assumptions for destructive testing:

```text
H1  Time perception is one faculty.                         REJECT as terminology.
H2  Physical duration = perceived duration.                FALSIFIED.
H3  Duration = temporal order.                             REJECT.
H4  Order judgment = simultaneity judgment.                FALSIFIED as identity.
H5  One PSS measure transfers across TOJ/SJ.               FALSIFIED as default.
H6  All timing tasks measure one latent target.            OPEN / strongly pressured.
H7  Estimation = reproduction = production.                REJECT.
H8  Prospective timing = retrospective timing.             FALSIFIED as identity.
H9  Retrospective timing is direct clock readout.           REJECT.
H10 Passage of time = estimated duration.                  FALSIFIED as identity.
H11 Rhythm = beat.                                         REJECT.
H12 Beat perception = motor synchronization.               REJECT.
H13 Beat-based = interval-based timing.                    FALSIFIED as universal.
H14 Rhythm learning requires rhythmic action.              FALSIFIED in tested paradigm.
H15 Timing is modality-invariant.                          FALSIFIED as universal.
H16 Auditory timing hierarchy transfers to vision.         FALSIFIED in 2026 study.
H17 Subsecond and suprasecond require distinct clocks.     NOT ESTABLISHED.
H18 One general timing factor proves one mechanism.        REJECT inference.
H19 Central tendency = clock-rate distortion.              REJECT by definition.
H20 Accuracy = precision.                                  REJECT.
H21 Confidence = timing accuracy.                          REJECT.
H22 Intentional binding = sense of agency.                 STRONGLY PRESSURED / reject identity.
H23 Chronostasis = general subjective time.                REJECT.
H24 Circadian phase = time perception.                     REJECT.
H25 Temporal horizon = timing ability.                     REJECT.
H26 Memory for when = duration perception.                 REJECT.
H27 Motor timing owns all Human timing.                    FALSIFIED.
H28 Perceptual timing owns all Human timing.               FALSIFIED.
H29 Attention effect implies attention is clock.           REJECT inference.
H30 Agent timestamp/pacing = Human timing capability.      REJECT.
```

---

# 35. Agent-era attribution

For externally supported timing:

```text
AgentTimestampAccuracy
!= HumanTemporalPerception

AgentReminderSuccess
!= HumanProspectiveTiming

AgentPacingBenefit
!= HumanIndependentTimingGain

ExternalBeatCue
!= InternalBeatGenerationCapability

LatencyCompensation
!= HumanTemporalRecalibration
```

Support provenance must be explicit.

---

# 36. Neighbor-owner map after A

```text
World → objective temporal relations
HF2   → temporal phenomenology / passage experience
HF3   → attention, WM, metacognition
HF5   → circadian/homeostatic state
HF7   → temporal memory/order/retrospective reconstruction
HF8   → temporal representation/model
HF9   → temporal inference
HF10  → future-oriented choice/planning/stopping
HF11  → motor timing/synchronization/action prediction
HF20  → sensory/perceptual temporal evidence
HF21  → affective modulation
Media → external rhythm/music/meter artifact
```

No HF24 extraction is allowed before these are fully consumed.

---

# 37. A-round Foundation gate

```text
F1 stable reusable timing object
→ PROVISIONAL only

F2 cross-regime recurrence
→ PASS for temporal-judgment phenomena

F3 existing-owner composition gap
→ UNRESOLVED

F4 coherent causal/state architecture
→ UNRESOLVED

F5 neighboring-owner resistance
→ UNRESOLVED

F6 evidence grammar
→ PASS / strengthened

F7 Agent-era diagnostic value
→ PASS but secondary

F8 deletion harm
→ UNRESOLVED
```

Therefore:

```text
HF24 = UNKNOWN / not admitted
```

---

# 38. HD12-B admission

A has generated enough clean competing structures for a rival-model round.

Admit:

```text
HD12-B — Rival Timing Models,
         Measurement Decomposition
         & Cross-Task Falsification
```

Mandatory rivals:

```text
B1 Pacemaker / accumulator / scalar-clock family
B2 Multiple specialized timing systems
B3 State-dependent / distributed population timing
B4 Bayesian / contextual temporal inference
B5 Memory + decision / task-construction accounts
B6 Modality-specific hierarchical timing
B7 Action-prediction / motor-system timing
B8 Heterogeneous family / no peer timing owner
```

No rival is canonical at B entry.

---

# 39. B-round common battery

Each rival must explain, without changing definitions ad hoc:

```text
B1  subsecond/suprasecond duration reproduction + central tendency
B2  duration discrimination versus reproduction
B3  TOJ versus SJ dissociation
B4  auditory duration→sequence→beat hierarchy versus visual failure
B5  interval-based versus beat-based causal dissociation
B6  visual-only rhythm learning versus motor-only failure
B7  prospective versus retrospective timing
B8  event-boundary effects on retrospective duration
B9  passage-of-time versus duration dissociation
B10 chronostasis
B11 intentional/temporal binding task dependence
B12 ADHD selective reproduction deficit
B13 affect/cardiac modulation
B14 Agent-supported pacing/timestamps without Human capability gain
```

---

# 40. Canonical frontier after A

```text
HF0–HF23 = preserved
HF24 = UNKNOWN / not admitted
FoundationReopenCondition(HF0–HF23) = false

HD12-A = completed
HD12-B = next admitted round
HD12 = active deep route

TemporalCognition
= heterogeneous research umbrella

TemporalRelationEstimationEpisode
= provisional research object
= not HF24

NextDeepRoute after HD12 = UNKNOWN

HOC0–HOC10 = frozen
HOC11 = UNKNOWN / not admitted
```
