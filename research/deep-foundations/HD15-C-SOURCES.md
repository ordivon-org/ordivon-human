---
schema_version: 1
id: human.deep-foundations.hd15c.sources
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
summary: Primary-evidence ledger for HD15-C ownership extraction. It concentrates on evidence that distinguishes scientific process reality from peer-owner specificity: somatoparaphrenia/covert-disownership dissociations from motor awareness and neglect; perspective-dependent and multisensory remission of disownership; affective-touch modulation after stroke; distributed lesion/disconnection patterns; shared temporal-integration mechanisms for body ownership and generic visuotactile simultaneity; local-versus-full-body ownership hierarchy; and prospective, retrospective, goal, regularity, control-detection, explicit/implicit and artificial-body agency dissociations. The evidence supports real local ownership and agency projections but does not establish peer deletion harm after HF1/HF2/HF3/HF8/HF10/HF11/HF20 plus World/HD12/HD14 are restored.
evidence_status: verified
readiness: READY
related:
  - human.deep-foundations.hd15c
  - human.deep-foundations.hd15b.sources
  - human.deep-foundations.hd15a.sources
---
# HD15-C — Primary Evidence Ledger

This ledger is incremental. HD15-A-SOURCES and HD15-B-SOURCES remain canonical for the full term-separation and rival-model batteries. C adds and reweights sources specifically for **ownership extraction**.

# 1. Body ownership — scientific target selectivity

## C01 — Vallar & Ronchi / pure somatoparaphrenic profiles

`What is mine? Behavioral and anatomical dissociations between somatoparaphrenia and anosognosia for hemiplegia.`
PMID: 22713395.
DOI: 10.3233/BEN-2012-110226.

Five patients showed rare somatoparaphrenia profiles dissociated from anosognosia for hemiplegia, with lesion patterns sparing many areas associated with anosognosia.

Use:

```text
DisturbedBodyOwnership
!= MotorUnawarenessByDefinition
```

Limit:

```text
selective clinical target
!= peer semantic owner
```

The patients still had other lesion-associated deficits and the evidence does not isolate a single ownership-specific transformation outside multisensory/representational architecture.

---

## C02 — Moro et al. 2016 — motor awareness vs disturbed ownership

`Motor versus body awareness: Voxel-based lesion analysis in anosognosia for hemiplegia and somatoparaphrenia following right hemisphere stroke.`
Cortex 83:62–77.
PMID: 27494375.
DOI: 10.1016/j.cortex.2016.07.001.

Multi-centre N=70 lesion analysis compared anosognosia for hemiplegia, disturbed sense of ownership and rare selective profiles.

Use:

```text
MotorAwarenessDeficit
!= DisturbedOwnership
```

The study supports distributed cortical/subcortical/white-matter contributions rather than one simple ownership module.

---

## C03 — Cataldo et al. 2025 — covert disownership after stroke

`Unveiling covert disownership after stroke: a neuropsychological and neural approach.`
Brain Communications 7(3):fcaf217.
PMID: 40585817.
DOI: 10.1093/braincomms/fcaf217.

105 stroke patients and 55 controls. About 30% of patients showed covert disownership on sensitive non-verbal/graded measures, affecting hands, arms, legs or face portions. The study assessed hand dexterity, strength, sensitivity and proprioception and identified distributed temporo-parietal/fronto-occipital and tract disconnections with body-part-dependent patterns.

Use:

```text
OwnershipDisturbance
= real and body-part-specific

VerbalInterview
!= sufficient ownership readout

DistributedNetworkImplementation
!= single semantic owner
```

---

# 2. Body ownership — causal/modulatory evidence weakens owner specificity

## C04 — Bolognini et al. 2014 — multisensory remission

`Multisensory remission of somatoparaphrenic delusion: My hand is back!`
Neurology: Clinical Practice 4(3):216–225.
PMID: 29473554.
DOI: 10.1212/CPJ.0000000000000033.

Somatoparaphrenic patients could experience a reliable rubber-hand illusion. Synchronous touches applied to the visible disowned hand and the opposite hidden hand produced immediate self-attribution of the disowned limb without repairing other sensorimotor or attentional disorders.

Use:

```text
OwnershipAttribution
can be selectively modulated by multisensory evidence
```

This is strong evidence for a real ownership target but also direct evidence that the transformation is penetrable by HF20-type multisensory integration rather than isolated from it.

---

## C05 — Fotopoulou/Jenkinson et al. 2011 — mirror reversal

`Mirror-view reverses somatoparaphrenia: dissociation between first- and third-person perspectives on body ownership.`
Neuropsychologia.
PMID: 22023911.
DOI: 10.1016/j.neuropsychologia.2011.10.011.

Ownership/disownership judgments of the same biological limb could alternate rapidly as direct first-person and mirror third-person views alternated.

Use:

```text
BiologicalParthood fixed
while OwnershipAttribution changes with Perspective
```

This separates HF1 objective body membership from ownership attribution and emphasizes reference-frame/representation dependence.

---

## C06 — Jenkinson et al. 2013 — perspective × attention

`Body ownership and attention in the mirror: insights from somatoparaphrenia and the rubber hand illusion.`
Neuropsychologia 51(8):1453–1462.
PMID: 23603022.
DOI: 10.1016/j.neuropsychologia.2013.03.029.

In a somatoparaphrenic patient, mirror-view ownership restoration depended on where spatial attention was directed; the same attention manipulation did not alter healthy/control-patient rubber-hand ownership in the same way.

Use:

```text
OwnershipAttribution interacts with Perspective and Attention
Interaction != Identity
```

---

## C07 — Jenkinson et al. 2020 — affective-touch rescue

`Welcoming back my arm: affective touch increases body ownership following right-hemisphere stroke.`
Brain Communications 2(1):fcaa034.
PMID: 32954292.
DOI: 10.1093/braincomms/fcaa034.

After calibration in 16 acute-stroke patients, a separate 26-patient experiment found increased limb ownership following experimenter-administered C-tactile-optimal affective touch. Lesion mapping linked failure to increase ownership to right insula/corpus-callosum damage.

Use:

```text
Interoceptive/AffectiveTouchEvidence
can modulate OwnershipAttribution
```

Limit:

```text
modulation != ownership-specific peer process
```

because HF20/HF5/HF21 supply the sensory/interoceptive/affective input and HF2/HF8 the ownership content/experience.

---

## C08 — D'Angelo et al. 2026 — shared causal temporal integration

`Parietal alpha frequency shapes own-body perception by modulating the temporal integration of bodily signals.`
Nature Communications 17:53.
DOI: 10.1038/s41467-025-67657-w.

Psychophysics, EEG, tACS and computational modeling showed that parietal alpha frequency causally changed temporal binding windows/sensitivity for both body ownership and visuotactile simultaneity judgments.

Use:

```text
TemporalIntegrationMechanism
= causally real

OwnershipSpecificity
= weakened because the manipulation also affects a generic multisensory task
```

This is a central HD15-C ownership-extraction result.

---

# 3. Part↔whole ownership

## C09 — Petkova et al. 2011 — integration across body segments

`From part- to whole-body ownership in the multisensory brain.`
Current Biology 21(13):1118–1122.
PMID: 21683596.
DOI: 10.1016/j.cub.2011.05.022.

Full-body ownership was associated with neural responses interpreted as integration of multisensory information across body segments; ventral premotor activity was stronger when a stimulated body part was attached to a body and carried information about full-body ownership.

Use:

```text
Part→WholeProcessReality = supported
```

but:

```text
NeuralPopulation != semantic owner
```

and the proposed mechanism is itself segment-level multisensory integration, matching HF20.

---

## C10 — Kondo et al. 2020 — local without coherent global ownership

`Scrambled body differentiates body part ownership from the full body illusion.`
Scientific Reports 10:5274.
PMID: 32210268.
DOI: 10.1038/s41598-020-62121-9.

Synchronous visuomotor stimulation of spatially scrambled hands/feet induced body-part ownership without corresponding coherent full-body ownership.

Use:

```text
LocalPartOwnership
can survive
without coherent FullBodyOwnership
```

---

## C11 — O'Kane, Chancel & Ehrsson 2024 — nonlinear hierarchy and global feedback

`Hierarchical and dynamic relationships between body part ownership and full-body ownership.`
Cognition 246:105697.
DOI: 10.1016/j.cognition.2023.105697.

Local synchrony mainly controlled local part ownership. Full-body ownership depended nonlinearly on coherently stimulated parts and global ownership fed back onto nonstimulated local parts.

Use:

```text
PartOwnership != FullBodyOwnership
Local→Global != linear sum
Global→Local feedback exists
```

Limit: healthy experimental hierarchy does not establish an owner-specific lesion/causal double dissociation beyond HF20/HF8/HF2.

---

# 4. Agency — existing-owner refinement

## C12 — Oi et al. 2024 — motor control / control detection / self-attribution

`Hierarchical analysis of the sense of agency in schizophrenia: motor control, control detection, and self-attribution.`
Schizophrenia 10:79.
PMID: 39343773.
DOI: 10.1038/s41537-024-00512-x.

Patients with schizophrenia were impaired in reaching/motor control and control detection while self-attribution was relatively less affected.

Use:

```text
MotorControl != ControlDetection != SelfAttribution
```

This supports layered agency evidence, not a peer owner beyond HF11/HF3/HF8/HF2.

---

## C13 — Schreiner et al. 2025 — goals vs predicted feedback

`Goals rather than predictions determine the sense of agency.`
iScience 28(6):112583.
PMID: 40510128.
DOI: 10.1016/j.isci.2025.112583.

Two experiments independently varied goal-feedback match and motor-activity appropriateness. Agency followed goal-feedback match under the tested design.

Use:

```text
ClassicalPredictionMatch
!= total AgencyArchitecture
```

HF10 goal content and HF11 action/control both remain necessary.

---

## C14 — Pryke, Jayachandran & Martin 2025 — causal prospective/retrospective contributions

`The causal neural substrates underpinning prospective and retrospective sense of agency.`
Cortex 188:53–67.
PMID: 40398204.
DOI: 10.1016/j.cortex.2025.04.014.

Double-blind sham-controlled crossover N=104 manipulated dlPFC/TPJ activity while prospective action-choice and retrospective outcome-valence cues were varied.

Use:

```text
ProspectiveAgencyEvidence
!= RetrospectiveAgencyEvidence
```

Causal differentiation refines the HF11/HF3/HF8 architecture but does not escape it.

---

## C15 — Takada et al. 2026 — regularity vs prediction during control exploration

`The role of regularity detection and prediction in the exploration of sense of agency.`
Consciousness and Cognition 138:103980.
PMID: 41447989.
DOI: 10.1016/j.concog.2025.103980.

Across two motor-adaptation/control-exploration experiments, updating the internal model did not significantly change subsequent control detection under the tested paradigm; regularity detection had stronger explanatory value during exploration.

Use:

```text
Prediction != universal agency source
RegularityDetection can dominate by regime
```

---

## C16 — Mariano et al. 2026 — explicit/implicit agency split in VR

`My avatar moves with me, so I am the one acting: Avatar responsiveness supports implicit sense of agency in virtual reality.`
PLoS ONE 21(6):e0351839.
PMID: 42330024.
DOI: 10.1371/journal.pone.0351839.

Two independent VR experiments, total N=70. Explicit agency was stronger for active than passive movement in both still and responsive-avatar conditions. Intentional binding appeared only with responsive avatar movement and at the shortest action-outcome delay.

Use:

```text
ExplicitAgencyJudgment
!= IntentionalBinding
```

This strengthens HF3/HD12 readout separation rather than peer-owner pressure.

---

## C17 — 2026 control-change detection — perceptual sensitivity vs metacognition

`Perceptual sensitivity, but not metacognitive monitoring, is shaped by increases and decreases in control.`
Experimental Brain Research.
PMID: 42053621.

Control-increase and control-decrease detection engage different perceptual evidence patterns while confidence/metacognitive monitoring need not mirror those changes.

Use:

```text
ControlDetectionProcess
!= MetacognitiveMonitoringByDefinition
```

This maps naturally to HF11/HF20 vs HF3 rather than a new agency owner.

---

# 5. Measurement separations retained from A/B

HD15-C continues to rely on prior primary evidence establishing:

```text
ProprioceptiveDrift != Ownership
Ownership != Agency
SelfLocation != Ownership
PartOwnership != FullBodyOwnership
IntentionalBinding != AgencyByDefinition
ThreatSCR != Ownership
```

These dissociations are evidence for typed targets and projections.

They are not evidence that every target requires a peer Foundation.

---

# 6. Evidence synthesis for ownership extraction

## BodyOwnershipCausalInferenceProjection

Evidence status:

```text
ProcessReality = STRONG
CrossRegimeRecurrence = STRONG
CausalPerturbation = STRONG
ClinicalSelectivity = STRONG
OwnerSpecificity = NOT ESTABLISHED
NeighborResistance = FAIL
PeerDeletionHarm = FAIL
```

Allocation:

```text
HF20-centered
+ HF8/HF2/HF3/HF1
```

## PartWholeOwnershipIntegrationProjection

Evidence status:

```text
ProcessReality = STRONG
ExperimentalLocalGlobalDissociation = STRONG
NonlinearHierarchy = STRONG
CleanOwnerSpecificClinicalDoubleDissociation = NOT ESTABLISHED
NeighborResistance = FAIL
PeerDeletionHarm = FAIL
```

Allocation:

```text
HF20/HF8-centered
+ HF2
```

## AgencyCueIntegrationProjection

Evidence status:

```text
ProcessReality = STRONG
ProspectiveRetrospectiveDissociation = STRONG
Goal/Prediction/RegularityPlurality = STRONG
ExplicitImplicitDissociation = STRONG
NeighborResistance = VERY STRONG FAIL
PeerDeletionHarm = FAIL
```

because HF11 already explicitly owns sense-of-agency evidence and rejects prediction-match identity.

Allocation:

```text
HF11-centered
+ World/HF10/HF20/HF8/HF3/HF2/HD12
```

---

# 7. Source-level conclusion

No primary source in the HD15-A/B/C ledger establishes:

```text
one bodily-self peer process
neighboring-owner resistance
or peer deletion harm
```

after the existing Foundations are restored.

The evidence instead supports:

```text
real local mechanisms
+ selective target dissociations
+ cross-process interactions
+ layered composition
```

Therefore current evidence supports candidate-specific closure rather than HF24 admission.
