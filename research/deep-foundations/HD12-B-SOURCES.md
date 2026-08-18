---
schema_version: 1
id: human.deep-foundations.hd12b.sources
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
summary: Primary evidence ledger for HD12-B rival timing model tournament. Sources cover scalar timing in humans, temporal-context/Bayesian calibration, context-specific and context-invariant computations, state-dependent network-reset effects, interval-invariant learning transfer, modality-specific priors, causal beat/interval dissociations, premotor contributions to beat perception/imagery, perceptual-vs-motor rhythm learning, TOJ/SJ task dissociation and task-sensitive temporal binding. Evidence supports layered plural timing rather than one clock or complete heterogeneity.
evidence_status: verified
readiness: READY
related:
  - human.deep-foundations.hd12b
---
# HD12-B — Primary Evidence Ledger

## S01 — Rakitin et al. 1998 — scalar timing in humans

`Scalar expectancy theory and peak-interval timing in humans.`
Journal of Experimental Psychology: Animal Behavior Processes 24(1):15–33.
PMID: 9438963. DOI: 10.1037//0097-7403.24.1.15.

Human peak-interval performance across 8, 12 and 21 s intervals showed approximately centered/symmetric/scalar response distributions in the tested design; individual-trial analysis implicated substantial temporal-memory variability.

Use:

```text
scalar-clock family has genuine local empirical content
```

but:

```text
ScalarRegularity != OneClockOntology
```

---

## S02 — Sadibolova et al. 2025 — latent timing structure

`Uncovering the latent structure of human time perception.`
Cognition 257:106078.
PMID: 39938399. DOI: 10.1016/j.cognition.2025.106078.

Two online experiments, N=302 each, duration reproduction over 400–2400 ms / 1000–2000 ms.

Use:

```text
GeneralTimingFactor
+
CentralTendencyBiasFactor
```

as positive commonality evidence without identifying a biological clock.

---

## S03 — Jazayeri & Shadlen 2010 — temporal context calibration

`Temporal context calibrates interval timing.`
Nature Neuroscience 13(8):1020–1026.
PMID: 20581842. DOI: 10.1038/nn.2590.

Humans reproduced the same sample interval differently depending on the distribution from which intervals were drawn. Bayesian estimators incorporating temporal uncertainty/context accounted for bias and variance.

Use:

```text
SamePhysicalDuration + DifferentPrior
→ DifferentEstimate
```

and:

```text
CentralTendency != ClockRateByDefinition
```

---

## S04 — Pourmohammadi & Sanayei 2023 — context-specific and context-invariant computations

`Context-specific and context-invariant computations of interval timing.`
Frontiers in Neuroscience 17:1249502.
PMID: 37799342. DOI: 10.3389/fnins.2023.1249502.

N=41 healthy adults completed sensory/motor timing tasks with hand/eye effectors. Three-stage Bayesian fits did not transfer context-specific bias across task/effector, while temporal precision was more context-invariant across effectors.

Use:

```text
TimingAccuracyBias can be context specific
while
TimingPrecision can show shared structure
```

---

## S05 — Sadibolova, Sun & Terhune 2021 — state-dependent reset

`Using adaptive psychophysics to identify the neural network reset time in subsecond interval timing.`
Experimental Brain Research 239(12):3565–3572.
PMID: 34581840. DOI: 10.1007/s00221-021-06227-0.

Auditory 100/200 ms duration-discrimination thresholds improved when the inter-stimulus interval increased from 250 to 333 ms; matched pitch discrimination did not show the same effect.

Use:

```text
LocalNetworkHistory affects subsecond timing precision
```

supporting state-dependent/dynamic mechanisms.

---

## S06 — Guan, Xiong & Yu 2024 — interval-invariant transfer

`Double training reveals an interval-invariant subsecond temporal structure in the brain.`
Journal of Experimental Psychology: Human Perception and Performance 50(12):1225–1235.
PMID: 39480346. DOI: 10.1037/xhp0001254.

Double training enabled complete transfer of temporal interval-discrimination learning from a trained subsecond interval to a new interval exposed through an independent secondary task.

Use:

```text
IntervalSpecificMechanism
can coexist with
IntervalInvariantTemporalComponent
```

and pressure pure multiple-independent-clock models.

---

## S07 — Tonelli, Phan & Alais 2025 — modality-specific reliability weighting

`Sensory reliability takes priority over the central tendency effect in temporal and spatial estimation.`
Scientific Reports 15:38886.
PMID: 41198729. DOI: 10.1038/s41598-025-22651-6.

Interleaved auditory/visual estimation data were better explained by reliability/task-sensitive modality priors than a single supra-modal prior. For temporal estimation, audition was the dominant modality in the reported design.

Use:

```text
TemporalPrior != OneGlobalPriorByDefinition
```

and:

```text
BayesianReliabilityWeighting != TimingSpecificOwner
```

because analogous principles were tested in spatial estimation.

---

## S08 — Grube et al. 2010 — absolute vs beat-based causal dissociation

`Transcranial magnetic theta-burst stimulation of the human cerebellum distinguishes absolute, duration-based from relative, beat-based perception of subsecond time intervals.`
Frontiers in Psychology 1:171.
PMID: 21833234. DOI: 10.3389/fpsyg.2010.00171.

Use:

```text
AbsoluteIntervalTiming != BeatBasedRelativeTiming
```

as a causal-dissociation pressure against flat timing ability.

---

## S09 — Lazzari et al. 2025 — premotor causal contribution to beat perception

`Topography of Functional Organization of Beat Perception in Human Premotor Cortex: Causal Evidence From a Transcranial Magnetic Stimulation (TMS) Study.`
Human Brain Mapping 46(7):e70225.
PMID: 40344601. DOI: 10.1002/hbm.70225.

Online rTMS over right caudal dorsal premotor cortex selectively modulated beat-perception performance in the reported experiments.

Use:

```text
MotorPlanningCircuit can causally contribute to perceptual beat prediction
```

without implying overt motor timing owns beat perception.

---

## S10 — Lazzari et al. 2025 — premotor causal contribution to beat imagery

`Imagining the beat: causal evidence for dorsal premotor cortex (dPMC) role in beat imagery via transcranial magnetic stimulation (TMS).`
NeuroImage 323:121593.
PMID: 41248776. DOI: 10.1016/j.neuroimage.2025.121593.

TMS over dPMC modulated internally maintained beat-imagery performance; SMA stimulation did not show the same effect.

Use:

```text
Action-prediction circuitry can contribute without overt action
```

but remains region/task specific.

---

## S11 — Weng et al. 2026 — perceptual vs motor rhythm learning

`Perceptual Temporal Structure Supports Rhythm Learning and Enhances Theta Oscillations When Perception and Action Are Dissociated.`
Brain Sciences 16(5):489.
PMID: 42192800. DOI: 10.3390/brainsci16050489.

Visual-only temporal structure supported reliable implicit rhythm learning whereas motor-only temporal structure did not in the tested design.

Use:

```text
TemporalRhythmLearning != MotorTimingOnly
```

---

## S12 — Mohammad Alipour, Butler & Grahn 2026 — modality hierarchy

`Duration, Sequence and Beat Perception across Modalities.`
Multisensory Research.
PMID: 42155997. DOI: 10.1163/22134808-bja10194.

Auditory data supported a duration→sequence→beat hierarchy; visual data did not support the same hierarchy.

Use:

```text
TimingArchitecture_Auditory != TimingArchitecture_Visual by default
```

---

## S13 — Recio et al. 2019 — TOJ vs SJ dissociation

`Dissociating the sequential dependency of subjective temporal order from subjective simultaneity.`
PLoS One 14:e0223184.
PMID: 31596862. DOI: 10.1371/journal.pone.0223184.

Use:

```text
TOJ != SJ by default
```

as a task-level challenge to whole-domain clocks.

---

## S14 — retrospective event-boundary study 2025

`Retrospective duration judgments of naturalistic events depend on memories of event boundaries.`
PMID: 41491329. DOI: 10.3758/s13423-025-02833-z.

Use:

```text
RetrospectiveDuration
= strongly memory/event-structure mediated
```

and preserve HF7 ownership.

---

## S15 — de Azevedo et al. 2025 — temporal-binding task dependence

`Temporal binding: Task-dependent variations and reliability across experimental paradigms.`
Attention, Perception, & Psychophysics.
PMID: 39702700.

Four paradigms produced different binding expressions and weak cross-task convergence/reliability.

Use:

```text
TemporalBindingTask_A != TemporalBindingTask_B by default
```

---

# B synthesis

Primary evidence rules out both extremes:

```text
OneGlobalClock
```

and:

```text
NoSharedTemporalStructureAtAll
```

The strongest current synthesis is layered and plural:

```text
local temporal evidence
+
transferable/abstract temporal relation where demonstrated
+
context/reliability calibration
+
memory/control/readout layers
```

This is a research architecture and cross-HF projection, not HF24.
