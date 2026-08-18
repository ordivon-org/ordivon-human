---
schema_version: 1
id: human.deep-foundations.hd12a.sources
profile: research
lifecycle: completed
source_role: evidence
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
updated: 2026-08-18
summary: Primary evidence ledger for HD12-A term separation. Sources establish separations among duration, temporal order, simultaneity, sequence/beat timing, perceptual versus motor rhythm, prospective versus retrospective duration, passage-of-time experience, chronostasis and task-sensitive temporal/intentional binding. The ledger constrains terminology and measurement; it does not select a timing theory or admit HF24.
evidence_status: verified
readiness: READY
related:
  - human.deep-foundations.hd12a
---
# HD12-A — Primary Evidence Ledger

## S01 — Sadibolova et al. 2025

`Uncovering the latent structure of human time perception.`
Cognition 257:106078.
PMID: 39938399. DOI: 10.1016/j.cognition.2025.106078.

Two experiments, N=302 each, duration reproduction across approximately 400–2400 ms.

Use:

```text
GeneralTimingFactor + CentralTendencyBiasFactor
TimingPerformance != PureClockReadout
```

No inference that the general factor is one biological clock.

---

## S02 — Recio et al. 2019

`Dissociating the sequential dependency of subjective temporal order from subjective simultaneity.`
PLoS One 14:e0223184.
PMID: 31596862. DOI: 10.1371/journal.pone.0223184.

Rapid recalibration was observed in temporal-order judgments but not simultaneity judgments; individual PSS measures from the two tasks were not significantly correlated.

Use:

```text
TOJ != SJ by default
PSS_TOJ != PSS_SJ by default
```

---

## S03 — Mohammad Alipour, Butler & Grahn 2026

`Duration, Sequence and Beat Perception across Modalities.`
Multisensory Research.
PMID: 42155997. DOI: 10.1163/22134808-bja10194.

Use:

```text
Auditory timing supports duration→sequence→beat hierarchy in the studied data;
visual timing did not show the same hierarchy.
```

Pressure against one modality-invariant scalar.

---

## S04 — Grube et al. 2010

`Transcranial magnetic theta-burst stimulation of the human cerebellum distinguishes absolute, duration-based from relative, beat-based perception of subsecond time intervals.`
Frontiers in Psychology 1:171.
PMID: 21833234. DOI: 10.3389/fpsyg.2010.00171.

Cerebellar cTBS selectively impaired single-interval duration timing relative to beat-based tasks in the reported experiment.

Use:

```text
AbsoluteIntervalTiming != BeatBasedRelativeTiming
```

---

## S05 — Weng et al. 2026

`Perceptual Temporal Structure Supports Rhythm Learning and Enhances Theta Oscillations When Perception and Action Are Dissociated.`
Brain Sciences 16(5):489.
PMID: 42192800. DOI: 10.3390/brainsci16050489.

Use:

```text
visual-only temporal structure supported reliable implicit rhythm learning;
motor-only temporal structure did not in the tested paradigm.
```

Pressure:

```text
RhythmLearning != MotorRepetition
```

---

## S06 — Jording et al. 2022

`Dissociating passage and duration of time experiences through the intensity of ongoing visual change.`
Scientific Reports 12:8226.
PMID: 35581249. DOI: 10.1038/s41598-022-12063-1.

Visual change manipulated passage-of-time reports while duration estimates were comparatively unaffected.

Use:

```text
SubjectivePassageOfTime != DurationJudgment
```

---

## S07 — Bratzke 2026

`Emotional pictures and time: The effects of arousal and valence on the perception of duration and the subjective passage of time.`
Attention, Perception, & Psychophysics 88:98.
PMID: 41876805. DOI: 10.3758/s13414-026-03241-8.

In the reported design, affective ratings influenced passage-of-time judgments while duration judgments did not show the same effect.

Use as replication pressure for the passage/duration separation.

---

## S08 — Block-task prospective/retrospective timing experiment

`Prospective and retrospective duration judgments: an executive-control perspective.`
PMID: 15283475.

Executive-control demands shortened prospective reproductions while increasing retrospective reproductions in the reported experiments.

Use:

```text
ProspectiveTiming != RetrospectiveTiming
```

---

## S09 — retrospective naturalistic event boundaries 2025

`Retrospective duration judgments of naturalistic events depend on memories of event boundaries.`
PMID: 41491329. DOI: 10.3758/s13423-025-02833-z.

Participants judged durations of daily-event videos immediately and after seven days; retrospective duration related to remembered event structure and memory change.

Use:

```text
RetrospectiveDuration != DirectOnlineClockReadout
```

and preserve HF7 ownership.

---

## S10 — Kong et al. 2024

`No evidence in favor of the existence of "intentional" binding.`
Journal of Experimental Psychology: Human Perception and Performance 50(6):626–635.
PMID: 38635224. DOI: 10.1037/xhp0001204.

Use:

```text
IntentionalBinding != SenseOfAgencyByDefinition
```

and treat intentionality-specific interpretations as falsifiable.

---

## S11 — de Azevedo et al. 2025

`Temporal binding: Task-dependent variations and reliability across experimental paradigms.`
Attention, Perception, & Psychophysics.
PMID: 39702700.

Four paradigms showed task-dependent binding expressions and limited convergence/reliability across measures.

Use:

```text
TemporalBindingTask_A != TemporalBindingTask_B by default
```

---

## S12 — Siebertz & Jansen 2025

`Is the temporal binding effect in the Libet clock-task based in spatial working memory? A correlational and a dual-task approach.`
Consciousness and Cognition 134:103909.
PMID: 40737795. DOI: 10.1016/j.concog.2025.103909.

Use as alternative-mechanism pressure on Libet-clock binding, especially HF3 spatial-WM demand.

---

## S13 — Zhai et al. 2024

`Sound reduces saccadic chronostasis illusion.`
Vision Research 215:108344.
PMID: 38109820. DOI: 10.1016/j.visres.2023.108344.

Use:

```text
Chronostasis is action/multisensory context-sensitive;
chronostasis != general subjective passage of time.
```

---

## S14 — H-BAT beat perception/production 2013/2014

`The Harvard Beat Assessment Test (H-BAT): a battery for assessing beat perception and production and their dissociation.`
PMID: 24324421.

Use as measurement precedent for separating perceptual beat sensitivity from beat production/synchronization.

---

## S15 — Noboa et al. 2025

`Neural entrainment to the beat and working memory predict sensorimotor synchronization skills.`
Scientific Reports 15:10466.
PMID: 40140677. DOI: 10.1038/s41598-025-93948-9.

Use:

```text
SensorimotorSynchronizationSkill
can depend on multiple contributors;
NeuralEntrainment != MotorSynchronization by identity.
```

---

## S16 — causal premotor beat-perception study 2025

`Topography of Functional Organization of Beat Perception in Human Premotor Cortex: Causal Evidence From a Transcranial Magnetic Stimulation (TMS) Study.`
PMID: 40344601.

Right caudal dorsal premotor stimulation selectively modulated beat perception in the reported experiments.

Use to pressure a strict perception-versus-motor-region ownership collapse: motor planning circuitry can causally contribute to perception without making beat perception identical to overt motor synchronization.

---

## S17 — Arslanova et al. 2026

`Dissecting emotional and cardiac contributions to duration perception: Evidence from two EEG experiments.`
Neuropsychologia 109550.
PMID: 42468848. DOI: 10.1016/j.neuropsychologia.2026.109550.

Use as current bodily/affective modulation pressure.

```text
BodyStateEffectOnDuration != TimingOwnerByDefinition
```

---

# A synthesis

The evidence forces:

```text
Duration
!= Order
!= Simultaneity
!= Rhythm/Beat
!= MotorSynchronization
!= PassageOfTime
```

and:

```text
TemporalTask
is part of the evidence model,
not a transparent window onto one latent clock.
```

No source here is sufficient for HF24 admission.
