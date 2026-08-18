---
schema_version: 1
id: human.deep-foundations.hd11d.sources
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
summary: Primary evidence ledger for HD11-D. Sources are used to separate perceptual reality monitoring, retrospective source monitoring, metacognitive confidence, belief/endorsement, supposition, pretense and Agent-era source effects. Evidence supports a mandatory cross-owner reality/source grammar but not one peer Reality subsystem.
evidence_status: verified
readiness: READY
related:
  - human.deep-foundations.hd11d
---
# HD11-D — Primary Evidence Ledger

## S01 — Dijkstra et al. 2025 — neural basis of perceptual reality monitoring

`A neural basis for distinguishing imagination from reality.`
Neuron 113(15):2536–2542.e4 (2025).
PMID: 40480215.
DOI: 10.1016/j.neuron.2025.05.015.

Primary Human neuroimaging/psychophysics evidence.

Use:

```text
imagined/perceived sensory evidence can be intermixed;
reality judgment depends on first-order sensory strength plus higher-level classification.
```

Pressure:

```text
GenerationSource
!= SensorySignalStrength
!= RealityMonitoringJudgment.
```

---

## S02 — reality monitoring and metacognitive judgments 2024

`Reality monitoring and metacognitive judgments in a false-memory paradigm.`
PMID: 38007192.

Participants perceived or voluntarily imagined paired content, then classified source as perceived, imagined or new and gave confidence judgments.

Key result used:

```text
imagined items were sometimes externalized as perceived;
confidence did not reliably distinguish correct imagined-source judgments
from some incorrect externalized judgments.
```

Pressure:

```text
GenerationProvenance
!= SourceAttribution
Confidence
!= SourceCorrectness.
```

---

## S03 — Dijkstra, Mazor & Fleming 2024 — confidence does not rescue reality classification

`Confidence ratings do not distinguish imagination from reality.`
Journal of Vision 24(5):13 (2024).
PMID: 38814936.
DOI: 10.1167/jov.24.5.13.

Across two experiments, confidence criteria shifted with reality-decision criterion changes, showing limited metacognitive insight into imagery-induced perceptual reality-monitoring errors.

Use:

```text
MetacognitiveConfidence
!= CorrectRealityMonitoring.
```

---

## S04 — Dijkstra & Fleming 2022 — perceptual reality-monitoring framework

`Perceptual reality monitoring: Neural mechanisms dissociating imagination from reality.`
Neuroscience & Biobehavioral Reviews 135:104557 (2022).
PMID: 35122782.
DOI: 10.1016/j.neubiorev.2022.104557.

Review/theory source used only as model context, not admission evidence.

It proposes that higher-level circuits evaluate first-order sensory/cognitive factors and that perceptual reality monitoring shares computations with metacognition.

Pressure:

```text
RealityMonitoring
may be typed metacognitive classification over first-order evidence,
not a primitive content bit.
```

---

## S05 — Zhao & Osherson 2012 — supposing versus learning

`Updating: learning versus supposing.`
Cognition 124(3):373–378 (2012).
PMID: 22717167.
DOI: 10.1016/j.cognition.2012.05.001.

Three experiments compared conditional judgment under supposing B with belief probability after learning B.

Use:

```text
Suppose(B)
!= Learn(B is true)
```

and supports a non-belief/use stance relation.

---

## S06 — Byrne 2024 — reasoning under hypothetical impossibilities

`How people think about the truth of hypothetical impossibilities.`
Memory & Cognition 52(1):182–196 (2024).
PMID: 37787932.
DOI: 10.3758/s13421-023-01454-y.

Four experiments tested judgments under explicitly impossible conditionals.

Use:

```text
ReasonUnder(P)
can support structured consequence judgment
without Belief(P actual).
```

Supports HF9 inference + stance separation.

---

## S07 — Mazor, Firestone & Phillips 2026 — epistemic pretense

`Pretending Not to Know Reveals a Capacity for Model-Based Self-Simulation.`
Psychological Science 37(2):136–149 (2026).
PMID: 41632587.
DOI: 10.1177/09567976251409747.

Two experiments, total N=1,001 adults.

Participants with actual solution knowledge behaved under a simulated uninformed state while retaining detectable leakage.

Pressure:

```text
PretendStance
!= ActualBeliefState
ActualKnowledge can coexist with locally operative nonactual stance.
```

---

## S08 — Sanna & Lagnado 2025 — source reliability and belief update

`Belief updating in the face of misinformation: The role of source reliability.`
Cognition 258:106090 (2025).
PMID: 39986181.
DOI: 10.1016/j.cognition.2025.106090.

Four experiments tested belief updating with retractions and differently reliable sources.

Use:

```text
SourceModel
can causally alter BeliefUpdate
```

while:

```text
SourceReliability != BeliefStatus
```

by identity.

---

## S09 — Spearing et al. 2025 — AI source framing and misinformation influence

`Countering AI-generated misinformation with pre-emptive source discreditation and debunking.`
Royal Society Open Science 12(6):242148 (2025).
PMID: 40568555.
DOI: 10.1098/rsos.242148.

Two experiments, total N=1,223.

A misleading AI-generated article influenced reasoning regardless of alleged Human/AI source; source-focused inoculation altered general trust but did not alone remove the article's specific influence, whereas content debunking was more effective.

Use:

```text
SourceLabel/Trust
!= ContentInfluence
Knowing/BelievingSourceType
!= ImmunityToBeliefEffect.
```

Agent-era evidence for keeping provenance/source model separate from endorsement/content effects.

---

## S10 — AI-generated media labeling 2025

`Labeling AI-generated media online.`
PNAS Nexus / human survey experiments (2025).
PMID: 40519990.

Experimental labels indicating AI generation reduced belief in presented claims under tested conditions.

Use:

```text
SourceAttributionMetadata
can affect Belief
```

but therefore should be represented as an input to belief update, not belief itself.

---

## S11 — lucid-dream source discrimination 2025

`The roles of recollection and familiarity in the positive association between dream lucidity and reality monitoring: Evidence from ERPs and EEG.`
Consciousness and Cognition (2025).
PMID: 41167139.
DOI: 10.1016/j.concog.2025.103947.

Use:

```text
PhenomenalVividness
!= SourceDiscrimination.
```

Supports separation of rich internally generated experience from monitoring/classification.

---

## S12 — schizophrenia-spectrum source monitoring 2025

`A cognitive model of perceptual anomalies: The role of source monitoring, top-down influence and inhibitory processes for hallucinations in schizophrenia spectrum disorders and hallucinatory-like experiences in the general population.`
Comprehensive Psychiatry 138:152583 (2025).
PMID: 39929061.
DOI: 10.1016/j.comppsych.2025.152583.

Use:

```text
source-monitoring/perceptual anomaly patterns
are clinically relevant but do not reduce hallucination to one generation deficit.
```

---

# D synthesis

Primary evidence jointly forces:

```text
WorldTruth
!= Belief
!= Supposition/Pretend/FictionalStance

GenerationProvenance
!= CurrentSourceAttribution
!= RetrospectiveSourceMemory

PhenomenalRealness
!= RealityMonitoringJudgment
!= MetacognitiveConfidence
```

But it does not identify one peer Human subsystem owning all these distinctions.

The best current owner model is distributed, with a retained cross-owner composition grammar.
