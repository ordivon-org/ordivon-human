---
schema_version: 1
id: human.deep-foundations.post-hd15.sixth-generation-rerank.sources
profile: research
lifecycle: completed
source_role: evidence
visibility: public
owners:
  - ordivon-human
updated: 2026-08-18
summary: Primary-evidence ledger supporting the post-HD15 whole-Human re-ranking, especially the comparison between Music/Auditory Structural Cognition and Persistent Human-Agent Co-adaptation.
evidence_status: verified
readiness: READY
---
# Post-HD15 Fresh Re-Rank — Evidence Ledger

## Music / auditory structural cognition

### Sihvonen et al. 2024 — acquired amusia lesion network

J Neurosci. `Focal Brain Lesions Causing Acquired Amusia Map to a Common Brain Network.` PMID 38423761. DOI 10.1523/JNEUROSCI.1922-23.2024.

Independent prospective cohort of 97 stroke patients. Lesions causing amusia mapped to a common network centered on right superior temporal cortex and were distinct from the network causally associated with aphasia.

Use:

```text
MusicProcessing != LanguageProcessingByDefinition
SelectiveLesionNetworkEvidence = strong
```

### Dibbs & Moeller 2025 — isolated acquired amusia

Neurology. PMID 39889265. DOI 10.1212/WNL.0000000000213410.

Right temporal stroke with isolated acquired amusia provides high-value selective-case pressure.

### 2025 acquired amusia after right temporal resection

PMID 41313951.

Scale/key/contour/interval deficits coexisted with preserved speech-in-babble perception, music reward, and average tonal beat perception, musical imagery, memory and sophistication measures.

Use:

```text
MusicPerception != MusicReward != MusicImagery/Memory
```

### Hoarau et al. 2024 — congenital amusia beyond music

Neuropsychologia 202:108960. PMID 39032629. DOI 10.1016/j.neuropsychologia.2024.108960.

Wide task battery across pitch, music, speech, sound segregation and speech-in-noise. Supports pitch-centered vulnerability but also tests cross-domain auditory transfer rather than assuming music-specificity.

### Pitch/rhythm and verbal STM after TBI

PMID 34573194.

Pitch and rhythm deficits co-occurred only partially; verbal STM could remain intact when musical pitch/rhythm was impaired.

### Verbal vs musical STM after stroke

PMID 28088063.

Individual patients showed double dissociations between verbal and musical short-term memory.

### Bégel et al. 2017 — beat perception vs synchronization

Neuropsychologia 94:129–138. PMID 27914979. DOI 10.1016/j.neuropsychologia.2016.11.022.

Some beat-deaf individuals showed poor explicit rhythm/beat perception with relatively preserved synchronization and implicit temporal benefit.

Use:

```text
BeatPerception != BeatSynchronization
ExplicitTiming != ImplicitTiming
```

### Musical anhedonia

Mas-Herrero et al. 2014, Curr Biol. PMID 24613311. DOI 10.1016/j.cub.2014.01.068.

Healthy individuals can show low music pleasure with preserved music perception and preserved monetary reward responses.

Martínez-Molina et al. 2016, PNAS. PMID 27799544. DOI 10.1073/pnas.1611211113.

Specific musical anhedonia associated with reduced auditory-cortex/ventral-striatum coupling while monetary reward responses remain normal.

Use:

```text
MusicPerception != MusicReward
MusicReward != GenericReward
```

## Persistent Human-Agent co-adaptation

### Lee et al. 2026

Scientific Reports 16:13583. DOI 10.1038/s41598-026-42312-6.

Preregistered experiment plus follow-up survey. Passive AI copying reduced AI-independent self-efficacy, psychological ownership and meaningfulness relative to independent or human-first collaborative use; some effects persisted into a subsequent manual task.

Use:

```text
AIUseMode matters
AssistedPerformance != PersistentHumanCapacity
```

### Wu et al. 2025

Scientific Reports 15:15105. DOI 10.1038/s41598-025-98385-2.

Four online experiments, total N=3,562, testing performance augmentation and motivational effects in human–GenAI collaboration.

### Cognitive offloading 2026

Scientific Reports. `Cognitive offloading reduces internal memory processing in children.`

Use: external supports can improve supported recall while changing later internal-memory performance; developmental effects matter.

## Sleep / circadian

Liu et al. 2025, Communications Biology. PMID 41034492. DOI 10.1038/s42003-025-08812-3.

REM/SWS composition related differently to item-level vs category-level overnight memory transformation, supporting state/process plurality rather than one sleep scalar.

## Multimodal person recognition

Volfart et al. 2025, Scientific Reports. PMID 41345168. DOI 10.1038/s41598-025-27165-9.

Prosopagnosia case PS was severely impaired for natural-image face identity recognition while written-name identification was flawless.

Developmental phonagnosia and classical face/voice recognition dissociations provide additional modality-specific pressure.

---

# Ranking conclusion

The strongest **current marginal information** comes from Music/Auditory Structural Cognition because it combines selective lesion networks, within-domain double dissociations, perception-action dissociation, reward-perception dissociation and developmental variation while maintaining substantial ambiguity across HF20/HF8/HD12/HF11/HF4/HF21/HF23.

Human-Agent adaptation remains a high-priority open continent but currently has higher existing-owner absorption and thinner long-horizon causal evidence.
