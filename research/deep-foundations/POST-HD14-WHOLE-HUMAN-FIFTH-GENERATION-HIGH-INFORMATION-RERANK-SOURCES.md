---
schema_version: 1
id: human.deep-foundations.post-hd14.fifth-generation-rerank.sources
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
summary: Primary-evidence ledger for the fresh post-HD14 whole-Human fifth-generation re-ranking. The ledger prioritizes Human experiments, lesions, causal perturbations, active/passive and Human-machine regimes. Bodily-self evidence covers body-part versus full-body ownership, ownership/self-location interaction, implicit versus explicit agency, motor-control/control-detection/self-attribution hierarchy, explicit-versus-implicit body-schema measures, stroke disownership, noninvasive causal perturbation and BMI agency. Comparison evidence covers Human-AI use/offloading, music/amusia, sleep/circadian ecological neurodynamics and person-recognition/prosopagnosia. The evidence supports HD15 as a high-information non-foundation route; no source establishes HF24 or HOC11.
evidence_status: verified
readiness: READY
related:
  - human.deep-foundations.post-hd14.fifth-generation-rerank
  - human.deep-foundations.hd15.continuation
---
# Post-HD14 Fifth-Generation Re-Ranking — Primary Evidence Ledger

# Bodily Self / ownership / agency / self-location

## B01 — O'Kane, Chancel & Ehrsson 2024 — body-part vs full-body ownership

`Hierarchical and dynamic relationships between body part ownership and full-body ownership.`
Cognition 246:105697.
DOI: 10.1016/j.cognition.2023.105697.

Human multisensory-illusion experiment manipulating synchronous/asynchronous visuotactile stimulation over multiple mannequin body parts. Local body-part ownership could be experienced relatively independently of full-body ownership; full-body ownership depended nonlinearly on the number of synchronously stimulated parts and also fed back onto unstimulated-part ownership.

Use:

```text
BodyPartOwnership != FullBodyOwnershipByDefinition
LocalOwnershipProcess != GlobalOwnershipProcessByDefinition
```

---

## B02 — Frisco et al. 2024 — spatial prediction / ownership / disownership

`I am where I believe my body is: The interplay between body spatial prediction and body ownership.`
2024.
PMID: 39666650.

Within-subject VR study comparing virtual rubber-hand and first-person full-body illusions under aligned/misaligned body positions. Both paradigms altered ownership; misaligned full-body conditions produced distinctive disownership and body-localization changes.

Use:

```text
BodyLocationEstimate can modulate OwnershipExperience
BodyOwnership != BodyLocationEstimate
```

---

## B03 — 2024 VR full-body active/passive study — motor prediction and self-location

`Predicting the bodily self in space and time.`
2024.
PMID: 38926514.

Full-body VR/motion-capture study compared passive full-body illusion, active movement and real-time avatar control. Motion control altered self-other identification and self-location relationships.

Use:

```text
PassiveMultisensoryOwnership
!= ActiveMotorPredictionContribution
```

---

## B04 — Applebaum et al. 2025 — implicit vs explicit agency

`The Body Knows Better: Sensorimotor signals reveal the interplay between implicit and explicit Sense of Agency in the human mind.`
Cognition 254:105992.
PMID: 39454392.
DOI: 10.1016/j.cognition.2024.105992.

One exploratory plus one preregistered experiment, total N=60. Virtual-hand temporal conflict was detectable from implicit hand kinematics; kinematic classification of sensorimotor congruence exceeded participants' explicit judgments.

Use:

```text
ImplicitSensorimotorConflictInformation
!= ExplicitAgencyJudgment
```

---

## B05 — Oi et al. 2024 — agency hierarchy in schizophrenia

`Hierarchical analysis of the sense of agency in schizophrenia: motor control, control detection, and self-attribution.`
Schizophrenia 10:79.
DOI: 10.1038/s41537-024-00512-x.

Human patient-control experiment. Schizophrenia participants were more impaired in motor-control components and sensorimotor control detection while agency evaluation/self-attribution was relatively less affected.

Use:

```text
MotorControl
!= ControlDetection
!= SelfAttributionByDefinition
ClinicalLabel != one AgencyMechanism
```

---

## B06 — Nisticò et al. 2025 — explicit ownership/agency vs implicit body schema

`Exploring specific alterations at the explicit and perceptual levels in sense of ownership, agency, and body schema in Functional Motor Disorder: A pilot comparative study with Irritable Bowel Syndrome.`
Cortex.
PMID: 39855052.
DOI: 10.1016/j.cortex.2024.12.023.

Pilot comparative study: 12 Functional Motor Disorder, 10 IBS and 15 healthy participants. Explicit embodiment/ownership/agency responses and implicit forearm/body-schema drift did not move as one variable across groups/conditions.

Use:

```text
ExplicitEmbodimentJudgment
!= ImplicitBodySchemaUpdate
```

Limit: small pilot sample; use as dissociation pressure, not population-general owner proof.

---

## B07 — Cataldo et al. 2025 — covert disownership after stroke

`Unveiling covert disownership after stroke: a neuropsychological and neural approach.`
Brain Communications 7(3):fcaf217.
PMID: 40585817.
DOI: 10.1093/braincomms/fcaf217.

105 stroke patients and 55 controls. Multiple body-ownership measures plus lesion/network analyses found covert disownership in body-part-specific forms and associated it with distributed bilateral disconnection patterns.

Use:

```text
BodyPartDisownership = lesion-sensitive Human phenomenon
SelectiveLesionability != one focal OwnershipCenter
SelectiveLesionability != PeerSemanticOwner
```

---

## B08 — Pryke et al. 2025 — causal prospective/retrospective agency perturbation

`The causal neural substrates underpinning prospective and retrospective sense of agency.`
Cortex.
PMID: 40398204.
DOI: 10.1016/j.cortex.2025.04.014.

Double-blind, sham-controlled crossover study in 104 healthy adults. Anodal stimulation targeted left dlPFC or left TPJ during an implicit agency task to causally test prospective/retrospective agency substrates.

Use:

```text
AgencyRelevantProcesses = causally perturbable
CausalPerturbability != HF24
```

---

## B09 — Bertoni et al. 2025 — BMI / premovement agency dynamics

`Pre-movement sensorimotor oscillations shape the sense of agency by gating cortical connectivity.`
Nature Communications 16:3594.
DOI: 10.1038/s41467-025-58683-9.

Combined an implanted BMI participant with healthy EEG-BMI experiments. Premovement low-alpha phase in motor systems predicted agency judgments and covaried with broader connectivity during manipulated intention/action-feedback relations.

Use:

```text
PreMovementSensorimotorState contributes to AgencyJudgment
BMIAction provides a strong Human-machine perturbation regime
```

---

## B10 — van der Goot et al. 2026 — temporal decomposition of sensorimotor conflict

`Neural responses to sensorimotor conflict in an embodied agency task.`
Cortex 201:64-80.
PMID: 42134064.
DOI: 10.1016/j.cortex.2026.03.023.

Preregistered Human EEG embodied-VR study. Visual feedback conflicts could be decoded early; later neural patterns generalized across anatomical and spatial conflict types, consistent with staged agency processing.

Use:

```text
EarlyConflictProcessing
!= LaterGeneralAgencyProcessingByDefinition
```

---

# Human–Agent adaptation / offloading comparison

## A01 — Lee et al. 2026 — passive AI use vs active collaboration

`Relying on AI at work reduces self-efficacy, ownership, and meaning while active collaboration mitigates the effects.`
Scientific Reports 16:13583.
DOI: 10.1038/s41598-026-42312-6.

Preregistered experiment with a reported primary analytic sample of N=269 plus follow-up survey N=270. Passive copy/paste AI use reduced self-efficacy, psychological ownership and work meaning relative to active Human-first collaboration/no-AI conditions; some effects persisted into a later manual task.

Use:

```text
AIUse != one intervention
PassiveDelegation != ActiveCollaboration
SupportedOutput != unchanged Human state
```

---

## A02 — Pearson et al. 2026 — Human reliance on AI guidance

`Examining human reliance on artificial intelligence in decision making.`
Scientific Reports 16:5345.
DOI: 10.1038/s41598-026-34983-y.

Preregistered experiment, final N=295. Participants judged real vs AI-generated faces with deliberately fallible Human- or AI-attributed guidance and reported confidence. Attitudes toward AI interacted with performance/reliance patterns.

Use:

```text
GuidanceSource
× HumanPriorAttitude
can alter reliance/performance
```

---

## A03 — Fellers & Storm 2026 — offloading and later unaided prospective memory

`Offloading reduces prospective memory learning.`
Journal of Experimental Psychology: Learning, Memory, and Cognition.
PMID: 42241083.
DOI: 10.1037/xlm0001630.

Across two experiments, reminders improved performance on the offloaded prospective-memory task. After reminders were removed, performance on the previously offloaded task fell below the baseline of participants who had never used reminders.

Use:

```text
SupportedPerformance != LaterIndependentPerformance
Offloading can change learning/retention trajectory
```

---

# Music comparison

## M01 — Sihvonen et al. 2024 — acquired amusia lesion network

`Focal Brain Lesions Causing Acquired Amusia Map to a Common Brain Network.`
Journal of Neuroscience 44(15):e1922232024.
PMID: 38423761.
DOI: 10.1523/JNEUROSCI.1922-23.2024.

Lesion-network mapping from published lesion cases was tested in an independent prospective cohort of 97 stroke patients with repeated imaging and music/language assessment. Lesions causing amusia converged on a network centered on right superior temporal cortex and distinguishable from the aphasia network.

Use:

```text
MusicProcessing != LanguageProcessingByDefinition
```

---

# Sleep / circadian comparison

## S01 — Wang et al. 2026 — week-long naturalistic intracranial neurodynamics

`A week in the life of the human brain reveals stable states punctuated by chaotic-like transitions.`
Nature Communications 17:7215.
PMID: 42248858.
DOI: 10.1038/s41467-026-73347-y.

Twenty neurosurgical participants had near-continuous intracranial recordings over approximately 3–12 days with video/behavioral annotation. Slow dynamics related to circadian rhythm, heart rate and conscious/sleep state; sleep deprivation altered transition dynamics.

Use:

```text
EcologicalLongTimescaleStateDynamics = measurable
Sleep/Circadian candidate has strong evidence availability
```

But this does not overcome existing HF2/HF5/HF6/HF7/HD9 ownership by itself.

---

# Multimodal person-recognition comparison

## P01 — Barton et al. 2025 — acquired prosopagnosia variants

`Imagery and perception in acquired prosopagnosia: Functional variants and their relation to structure.`
Cortex 183:330-348.
PMID: 39645440.
DOI: 10.1016/j.cortex.2024.11.011.

Observations accumulated over 2.5 decades in 23 acquired-prosopagnosia patients. Occipitotemporal lesion profiles could show impaired facial-shape perception with relatively mild imagery impairment, supporting functional variants rather than one prosopagnosia mechanism.

Use:

```text
FacePerception != FaceImagery != FaceIdentityMemoryByDefinition
```

---

## P02 — 2025 congenital prosopagnosia MEG study

`Frequency-specific neural abnormalities in congenital prosopagnosia revealed by magnetoencephalography during face perception.`
Scientific Reports.
PMID: 40866518.
DOI: 10.1038/s41598-025-16958-7.

Three congenital-prosopagnosia participants versus seventeen controls. Early face detection was preserved while a later right anterior temporal alpha-band abnormality survived correction.

Use:

```text
EarlyFaceDetection != LaterFaceIdentityProcessing
```

Limit: extremely small clinical sample; treat as preliminary dissociation evidence.

---

# Evidence synthesis

The primary-evidence pattern is:

```text
Bodily Self candidate
→ multiple internally dissociable processes
→ strong healthy + lesion + psychiatric + causal + Human-machine regimes
→ large owner-boundary ambiguity
→ high deep-route value
→ low evidence for one new primitive owner

Human–Agent adaptation
→ very high current perturbation value
→ strong existing HF/HOC consumption paths

Music
→ real selective lesion/network evidence
→ narrower existing-owner allocation

Sleep/circadian
→ strong ecological/long-timescale evidence
→ strong existing physiological/experience/memory ownership

Person recognition
→ real component dissociations
→ narrower HF20/HF7/HF8/HF22 allocation
```

No source in this ledger admits HF24 or HOC11.
