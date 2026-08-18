---
schema_version: 1
id: human.deep-foundations.hd11b.sources
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
summary: Primary evidence ledger for HD11-B rival-model comparison, emphasizing scene construction versus memory/future projection, imaginative creation from retrieved elements, aphantasia dissociations, internal-attention perceptual decoupling, reality monitoring and epistemic pretense. Evidence constrains rivals but does not by itself establish HF24.
evidence_status: verified
readiness: READY
related:
  - human.deep-foundations.hd11b
---
# HD11-B — Evidence Ledger

## S01 — Ye et al. 2024 — retrieval versus imaginative creation

`Using imagination and the contents of memory to create new scene and object representations: A functional MRI study.`
Neuropsychologia 204:109000 (2024).
PMID: 39271053.
DOI: 10.1016/j.neuropsychologia.2024.109000.

Participants learned room/object associations, then separately retrieved associated elements and imaginatively combined them into new scene/object content.

Use:

```text
MemoryMaterial contributes to imagination,
but retrieval and imaginative creation are experimentally separable phases.
```

Supports M3 as contributor and M6 as possible construction residual.

---

## S02 — Hassabis et al. 2007 — hippocampal amnesia and novel scene construction

`Patients with hippocampal amnesia cannot imagine new experiences.`
PNAS 104(5):1726–1731.
PMID: 17229836.
DOI: 10.1073/pnas.0610561104.

Patients with bilateral hippocampal damage were markedly impaired at constructing coherent imagined experiences.

Use:

```text
Scenario/scene construction has selective neuropsychological vulnerability.
```

Not used to claim one hippocampal imagination module.

---

## S03 — Mullally et al. 2012 — spatial scene representation dissociation

`Attenuated boundary extension produces a paradoxical memory advantage in amnesic patients.`
Current Biology 22(4):261–268.
PMID: 22264610.
DOI: 10.1016/j.cub.2012.01.001.

Patients with bilateral hippocampal damage could generate semantic/contextual information about what might lie beyond a view while showing impoverished spatial scene representation.

Use:

```text
SemanticKnowledgeAvailable
!= SpatialSceneConstructionIntegrity.
```

This is one of the strongest selective-dissociation pressures for M6.

---

## S04 — Palombo et al. 2018 — scene construction versus future projection

`Medial Temporal Lobe Contributions to Episodic Future Thinking: Scene Construction or Future Projection?`
Cerebral Cortex 28(2):447–458.
PMID: 27913433.
DOI: 10.1093/cercor/bhw381.

MTL activity varied with scene-construction demand when future demands were matched; future versus present orientation did not show the same effect when scene demand was matched.

Use:

```text
SceneConstruction != FutureProjection.
```

---

## S05 — Gaesser et al. 2013 — novel construction versus re-imagination

`Imagining the future: evidence for a hippocampal contribution to constructive processing.`
Hippocampus 23(12):1150–1161.
PMID: 23749314.
DOI: 10.1002/hipo.22152.

Novel imagined-event construction elicited greater posterior hippocampal activity than re-imagining previously constructed events after accounting for novelty/subsequent memory effects.

Use:

```text
InitialConstruction != ReInstantiationByDefinition.
```

---

## S06 — Speed et al. 2025 — aphantasia and semantic mental simulation

`Dissociating voluntary mental imagery and mental simulation: Evidence from aphantasia.`
Memory & Cognition 53:2674–2685.
PMID: 40493310.
DOI: 10.3758/s13421-025-01731-y.

Use:

```text
ConsciousVoluntaryVisualImagery
!= MentalSimulationByDefinition.
```

Pressure against imagery-only M6 and in favor of cross-format substrate/process separation.

---

## S07 — Dijkstra et al. 2025 — reality monitoring

`A neural basis for distinguishing imagination from reality.`
Neuron 113(15):2536–2542.e4.
PMID: 40480215.
DOI: 10.1016/j.neuron.2025.05.015.

Use:

```text
GenerationSource
!= SignalStrength
!= RealityJudgment.
```

Supports keeping reality monitoring orthogonal to scenario construction.

---

## S08 — perceptual decoupling / internal attention 2025

`Perceptual Decoupling Underlies Internal Shielding Benefit during Switches between External and Internal Attention: Evidence from Early Sensory Event-related Potential Components.`
Journal of Cognitive Neuroscience (2025).
PMID: 40136307.

Internal selection showed reduced early sensory responses and switching/internal-shielding effects.

Use:

```text
PerceptualDecoupling is a plausible internal-attention mechanism
but is broader than imagination/scenario construction.
```

Supports M4 locally, rejects it as identity.

---

## S09 — Mazor, Firestone & Phillips 2026 — epistemic pretense

`Pretending Not to Know Reveals a Capacity for Model-Based Self-Simulation.`
Psychological Science 37(2):136–149.
PMID: 41632587.
DOI: 10.1177/09567976251409747.

N=1,001 across two game-based experiments. Pretenders reproduced broad and subtle patterns of genuinely uninformed behavior while retaining systematic traces of simplified/biased simulation.

Use:

```text
PretendedState != ActualBeliefState
Pretence can involve forward simulation of a simplified self-model.
```

Strong pressure against pure stance-without-process accounts.

---

## S10 — developmental amnesia scene construction

`Scene construction in developmental amnesia: an fMRI study.`
PMID: 24231038.

A developmental-amnesia case with hippocampal damage showed preserved scene construction with distributed network recruitment and residual hippocampal considerations.

Use:

```text
HippocampalDamage != UniversalSceneConstructionLoss.
```

Prevents anatomical overclaim and motivates C-round developmental/plasticity testing.

---

## S11 — constructive possibility judgments after hippocampal damage

`Deciding what is possible and impossible following hippocampal damage in humans.`
Hippocampus (2017).
PMID: 27997994.

Patients with bilateral hippocampal damage performed comparably on semantic possibility judgments but were selectively impaired on constructive possibility judgments, with controls reporting flexible internal scene construction.

Use:

```text
SemanticPossibilityKnowledge
!= ConstructiveScenarioModeling.
```

---

## S12 — self-generated states show network heterogeneity 2025

`Distinct distributed brain networks dissociate self-generated mental states.`
PMID: 40060698. Preprint record.

Precision fMRI found scene-like and speech-like imagined states associated with different distributed association-network patterns.

Use cautiously:

```text
SelfGeneratedMentalState != OneSensoryImageryModule.
```

Supports M5 umbrella heterogeneity, not a no-process conclusion.

---

# Evidence synthesis

Current evidence supports this asymmetric conclusion:

```text
1. scene/scenario construction can be experimentally and neuropsychologically distinguished
   from simple retrieval, semantic knowledge and future orientation;

2. memory and hippocampal systems are major contributors but not sufficient definitions;

3. perceptual decoupling and reality monitoring are important mechanisms but broader/different targets;

4. pretense requires more than a verbal stance label;

5. broad imagination remains heterogeneous across modality, use and phenomenal format.
```

Therefore evidence currently favors a bounded functional ScenarioConstructionProcess while withholding peer-Foundation admission.
