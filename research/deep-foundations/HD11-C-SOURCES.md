---
schema_version: 1
id: human.deep-foundations.hd11c.sources
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
summary: Primary evidence ledger for HD11-C cross-regime invariance and ownership extraction. Sources cover congenital blindness/spatial representation, motor imagery, social/self mental-state reasoning, psychosis source/reality monitoring, lucid-dream source discrimination, and developmental pretense. Evidence supports structured internal modeling across regimes but also shows domain-specific operators and separable monitoring mechanisms, undermining broad ScenarioConstructionProcess as a peer Foundation.
evidence_status: verified
readiness: READY
related:
  - human.deep-foundations.hd11c
---
# HD11-C — Primary Evidence Ledger

## S01 — Aleman et al. 2001 — imagery tasks without visual experience

`Visual imagery without visual experience: evidence from congenitally totally blind people.`
NeuroReport 12(11):2601–2604.
PMID: 11496156.
DOI: 10.1097/00001756-200108080-00061.

Congenitally blind participants were able to perform pictorial and spatial imagery tasks despite never having ordinary visual experience, although accuracy differed from sighted controls.

Use:

```text
StructuredSpatialImageryLikePerformance
!= PriorVisualExperienceRequired.
```

---

## S02 — Cattaneo et al. / spatial imagery in congenitally blind 2015

`Spatial imagery relies on a sensory independent, though sensory sensitive, functional organization within the parietal cortex: a fMRI study of angle discrimination in sighted and congenitally blind individuals.`
Neuropsychologia 68:59–70 (2015).
PMID: 25575449.
DOI: 10.1016/j.neuropsychologia.2015.01.004.

Congenitally blind and sighted participants performed spatial imagery using tactile/auditory modalities; performance and brain organization supported sensory-independent but sensory-sensitive spatial processing.

Use:

```text
SpatialStructure != VisualFormat
```

while preserving modality/task effects.

---

## S03 — Noordzij et al. 2010 — metric spatial representations in blind people

`Structural properties of spatial representations in blind people: Scanning images constructed from haptic exploration or from locomotion in a 3-D audio virtual environment.`
Memory & Cognition 38:526–541.
PMID: 20551339.

Blind participants generated metrically structured spatial representations from nonvisual sources including haptic and locomotor/audio experience.

Use:

```text
MetricSpatialModel
can be constructed from nonvisual evidence.
```

---

## S04 — Gagnon et al. 2012 — tactile navigation in congenital blindness

`Activation of the hippocampal complex during tactile maze solving in congenitally blind subjects.`
Neuropsychologia 50(7):1663–1671.
PMID: 22483742.
DOI: 10.1016/j.neuropsychologia.2012.03.022.

Congenitally blind participants can build/manipulate spatial navigation representations using nonvisual information, with hippocampal-system engagement under tactile-maze conditions.

Use:

```text
SpatialNavigationModeling
!= VisualExperienceByDefinition.
```

---

## S05 — Nalborczyk, Alario & Longcamp 2025 — motor imagery inhibition

`Motor inhibition prevents motor execution during typing imagery: Evidence from an action-mode switching paradigm.`
Cognition 254:105997 (2025).
PMID: 39499975.
DOI: 10.1016/j.cognition.2024.105997.

N=49 alternated overt and imagined typing. Behavioral/modeling results support inhibitory mechanisms that keep imagined action from overt execution.

Use:

```text
MotorImagery
has motor-control/inhibition-specific structure.
```

This supports HF11 ownership rather than a generic scenario operator.

---

## S06 — action imagery sequence learning 2025

`Prediction processes in the acquisition of sequence representations.`
Neuropsychologia (2025).
PMID: 41038384.
DOI: 10.1016/j.neuropsychologia.2025.109288.

Action-imagery practice produced effector-dependent sequence representations not found in action-observation conditions, consistent with internally predicted action consequences.

Use:

```text
MotorImageryRepresentation
can be effector/action-control specific.
```

---

## S07 — Okanou et al. 2026 — forward models in visual motor imagery

`Visual motor imagery recruits forward models to predict the sensory consequences of imagined movement.`
Neuroscience 612:16–24 (2026).
PMID: 42425261.
DOI: 10.1016/j.neuroscience.2026.07.015.

Use:

```text
MotorImageryUpdate
is naturally modeled through HF11 forward/action models.
```

This is current evidence against assigning motor simulation to a generic cross-domain scenario owner.

---

## S08 — self/other mental-state reasoning 2026

`Hierarchical systems in the default mode network when reasoning about self and other mental states.`
Social Cognitive and Affective Neuroscience (2026).
PMID: 42301939.
DOI: 10.1093/scan/nsag047.

Primary fMRI/MVPA work found both agent-specific and agent-general patterns for self/other mental-state inference.

Use:

```text
SocialMentalSimulation
contains agent/mentalizing-specific organization.
```

Supports HF1/HF12 ownership rather than spatial-scene identity.

---

## S09 — Aleksandrowicz et al. 2025 — source monitoring and perceptual anomalies

`A cognitive model of perceptual anomalies: The role of source monitoring, top-down influence and inhibitory processes for hallucinations in schizophrenia spectrum disorders and hallucinatory-like experiences in the general population.`
Comprehensive Psychiatry 138:152583 (2025).
PMID: 39929061.
DOI: 10.1016/j.comppsych.2025.152583.

Empirical samples included schizophrenia-spectrum patients with/without auditory hallucinations, healthy controls and nonclinical high/low hallucinatory-like-experience groups. Patient groups showed increased source-monitoring errors and false perceptions; the relationships did not reduce to one hallucination-specific construction deficit.

Use:

```text
SourceMonitoringFailure
!= ScenarioGenerationFailureByDefinition.
```

---

## S10 — speaking-induced suppression / agency in schizophrenia 2024

`Impaired speaking-induced suppression predicts degraded agency and hallucination severity in schizophrenia.`
PMID: 39417139.

MEG study linking speech/self-monitoring measures with agency and hallucination severity.

Use:

```text
SelfAgency/SourceMonitoring
is a separable hallucination-relevant axis.
```

---

## S11 — dream lucidity and source discrimination 2025

`The roles of recollection and familiarity in the positive association between dream lucidity and reality monitoring: Evidence from ERPs and EEG.`
Consciousness and Cognition (2025).
PMID: 41167139.
DOI: 10.1016/j.concog.2025.103947.

Participants imagined or perceived items and later made source judgments. Higher trait lucidity was associated with better aspects of source accuracy and electrophysiological markers despite high subjective vividness.

Use:

```text
PhenomenalVividness
!= SourceDiscrimination
```

and supports monitoring as orthogonal to generation.

---

## S12 — Fast & Riggs 2024 — pretend-play conventional norms

`Preschoolers negatively evaluate conventional norm violations in pretend play.`
Journal of Experimental Child Psychology 241:105861 (2024).
PMID: 38354448.
DOI: 10.1016/j.jecp.2024.105861.

Preschoolers used their knowledge of conventions to evaluate behavior within pretend contexts.

Use:

```text
PretendWorld
can preserve local conventional constraints.
```

This supports local stipulation/rule maintenance but not one generic construction engine.

---

## S13 — Buchsbaum et al. 2012 — pretense and causal counterfactual reasoning

`The power of possibility: causal learning, counterfactual reasoning, and pretend play.`
Philosophical Transactions of the Royal Society B 367:2202–2212 (2012).
PMID: 22734063.

Controlled child study found causally coherent pretend inferences related to counterfactual causal reasoning even after several covariates.

Use:

```text
Pretence
can recruit causal/counterfactual model structure.
```

Supports HF9 contribution rather than independent proof of M6.

---

# C synthesis

Across these primary studies:

```text
1. structured internal spatial models can survive absent visual experience;
2. motor imagery carries motor-control-specific prediction/inhibition structure;
3. social mental simulation carries agent/mentalizing-specific structure;
4. pretend worlds preserve local constraints but overlap causal/social mechanisms;
5. psychosis and lucid-dream evidence dissociate reality/source monitoring from content generation.
```

Therefore the cross-regime commonality is real but too abstract:

```text
structured representation + domain-specific update + control + stance/monitoring
```

and does not justify one new cross-domain ScenarioConstruction semantic owner.
