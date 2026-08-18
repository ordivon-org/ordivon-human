---
schema_version: 1
id: human.deep-foundations.hd13c.sources
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
summary: Primary evidence ledger for HD13-C quantitative ownership extraction. Sources test numerosity-specific encoding against nonnumerical visual features and domain-general explanations; visual/auditory/cross-modal invariance; 2025 cross-format neural representation; tactile and congenital-blind subitizing; 2026 tactile object-individuation mechanisms; action-perception/cross-modal adaptation; approximate-quantity versus exact-verbal acalculia; estimation-output versus number-semantics dissociation; number-versus-time magnitude dissociation; and symbolic-versus-nonsymbolic neural separation. Evidence supports real local numerosity mechanisms and cross-modal interactions but not one peer numerical owner.
evidence_status: verified
readiness: READY
related:
  - human.deep-foundations.hd13c
---
# HD13-C — Primary Evidence Ledger

## S01 — Dolfi et al. 2024 — local numerosity encoding in dyscalculia

`Weaker number sense accounts for impaired numerosity perception in dyscalculia: Behavioral and computational evidence.`
Developmental Science 27(6):e13538.
PMID: 38949566. DOI: 10.1111/desc.13538.

Children with dyscalculia were matched to controls on age, IQ and visuospatial memory. Lower numerosity-comparison accuracy was linked to weaker numerosity encoding rather than stronger nonnumerical visual bias; spontaneous categorization likewise showed weaker number-based organization without increased continuous-feature reliance.

Use:

```text
VisualNumerosityDeficit
!= VisualFeatureBiasOnly
```

and retain a real local numerosity mechanism.

---

## S02 — Tokita, Ashitani & Ishiguchi 2013 — modality-dependent approximate judgment

`Is approximate numerical judgment truly modality-independent? Visual, auditory, and cross-modal comparisons.`
Attention, Perception, & Psychophysics 75(8):1852–1861.
PMID: 23913137. DOI: 10.3758/s13414-013-0526-x.

Auditory numerical discrimination was more precise than visual discrimination; cross-modal performance was intermediate and modality-dependent biases remained.

Use:

```text
CrossModalNumerosity
!= OneContextFreeAmodalProcess
```

---

## S03 — 2025 JNeurosci cross-sense/format numerosity

`Brain Representation of Numerosity across the Senses and Presentation Formats.`
Journal of Neuroscience.
PMID: 41151970. DOI: 10.1523/JNEUROSCI.1264-25.2025.

Multivariate fMRI across auditory/visual and sequential/simultaneous/symbolic/nonsymbolic formats found numerical representation throughout a dorsal pathway. Visual-auditory representations aligned in intraparietal/frontal regions only when presentation format was shared sequentially; posterior-to-anterior IPS representations shifted from sensory-modality to presentation-format influences.

Use:

```text
CrossModalAlignment
is conditional on presentation format.
```

---

## S04 — Gallace, Tan & Spence 2006 — tactile numerosity without visual-like subitizing break

`Numerosity judgments for tactile stimuli distributed over the body surface.`
Perception 35(2):247–266.
PMID: 16583769. DOI: 10.1068/p5380.

Simultaneous vibrotactile enumeration across the body did not show the classic visual subitizing slope discontinuity, although performance used the number of activated tactors rather than simple global intensity.

Use:

```text
TactileNumerosity != VisualNumerosityMechanismByDefinition
```

---

## S05 — Ferrand, Riggs & Castronovo 2010 — tactile subitizing in congenital blindness

`Subitizing in congenitally blind adults.`
Psychonomic Bulletin & Review 17(6):840–845.
PMID: 21169578. DOI: 10.3758/PBR.17.6.840.

Congenitally blind and sighted participants rapidly enumerated one-to-three stimulated fingers, with slower performance at larger sets.

Use with S04:

```text
TactileSubitizingSignature
is body/task/individuation dependent.
```

---

## S06 — 2026 tactile object-individuation fMRI

`Tactile object individuation on a fingertip is associated with neural representations in the bilateral inferior parietal lobule.`
NeuroImage.
PMID: 42235656. DOI: 10.1016/j.neuroimage.2026.122026.

Task-invariant tactile object-individuation substrate localized to bilateral IPL; within OI range, voxel patterns decoded numerosity and WM load across tasks, with quantity-specific decoding restricted to the OI range.

Use:

```text
SmallSetNumerosity
→ narrow object-individuation mechanism
```

rather than whole numerosity owner.

---

## S07 — Revkin et al. 2008 — small vs large estimation systems

`Does subitizing reflect numerical estimation?`
Psychological Science.
PMID: 18578852. DOI: 10.1111/j.1467-9280.2008.02130.x.

Matched-discrimination experiments found a strong precision discontinuity between small and large numerosities, violating a single Weberian estimation mechanism across the full range.

Use:

```text
SmallSetApprehension != LargeSetApproximateEstimation
```

---

## S08 — Anobile et al. 2016 — action/perception adaptation

`A shared numerical representation for action and perception.`
eLife.
PMID: 27504969. DOI: 10.7554/eLife.16161.

Finger-tapping adaptation biased subsequent visual numerosity estimates for sequential and simultaneous stimuli and different judgment tasks.

Use as positive action↔perception coupling evidence, not owner identity.

---

## S09 — Togoli et al. 2020 — action/auditory numerosity in congenital blindness

`The shared numerical representation for action and perception develops independently from vision.`
Cortex.
PMID: 32580065. DOI: 10.1016/j.cortex.2020.05.004.

Finger-tapping adaptation altered auditory numerosity estimates in sighted and congenitally blind participants.

Use:

```text
VisualExperience != NecessaryForActionPerceptionNumerosityInteraction
```

but do not infer a peer owner.

---

## S10 — Lemer et al. 2003 — approximate quantity vs exact number words

`Approximate quantities and exact number words: dissociable systems.`
Neuropsychologia 41(14):1942–1958.
PMID: 14572527. DOI: 10.1016/S0028-3932(03)00123-4.

Two acalculic cases showed complementary quantity/verbal profiles: one parietal quantity-deficit case had approximation/subitizing/comparison impairments; one semantic/verbal-deficit case preserved approximation/nonsymbolic numerosity.

Use:

```text
ApproximateQuantityProcessing
!= ExactVerbalNumberProcessing
```

---

## S11 — exact vs approximate calculation in global aphasia

`Dissociation of exact and approximate calculation in severe global aphasia.`
PMID: 19452030.

Severe global aphasia coexisted with relatively preserved numerical comprehension and approximate calculation despite impaired exact calculation.

Use:

```text
LanguageLoss
!= ApproximateQuantityLossByDefinition
```

---

## S12 — Revkin et al. 2008 — estimation output vs number semantics

`Verbal numerosity estimation deficit in the context of spared semantic representation of numbers: a neuropsychological study of a patient with frontal lesions.`
Neuropsychologia 46(10):2463–2475.
PMID: 18502452. DOI: 10.1016/j.neuropsychologia.2008.04.011.

A frontal-lesion patient showed severe verbal numerosity-estimation abnormalities despite intact number processing and semantic representation; detailed testing localized the problem to translation from intact semantics to output.

Use:

```text
NumerosityEstimationScore
!= NumerosityRepresentation
```

---

## S13 — Cappelletti, Freeman & Cipolotti 2011 — number vs time double dissociation

`Numbers and time doubly dissociate.`
Neuropsychologia 49(11):3078–3092.
PMID: 21807010. DOI: 10.1016/j.neuropsychologia.2011.07.014.

Two parietal-lesion patients showed selective number and time deficits in opposite directions, with asymmetric cross-dimensional interaction.

Use:

```text
NumericalMagnitude != TemporalMagnitude
SharedMagnitudeInteraction != OneGeneralMagnitudeMechanism
```

---

## S14 — Kutter et al. 2018 — symbolic vs nonsymbolic number neurons

`Single Neurons in the Human Brain Encode Numbers.`
Neuron 100(3):753–761.e4.
PMID: 30244883. DOI: 10.1016/j.neuron.2018.08.036.

Human single-neuron recordings found distinct neuron groups selective for nonsymbolic or symbolic number rather than one group coding both formats identically.

Use:

```text
SymbolicCode != NonsymbolicCodeByDefinition
```

---

## S15 — Cappelleti et al./patient batteries — parietal quantity is not uniformly lost

`Numeracy skills in patients with degenerative disorders and focal brain lesions: a neuropsychological investigation.`
PMID: 22122516. DOI: 10.1037/a0026328.

A comprehensive battery across 36 acquired brain-disorder patients reported intact number-quantity processing in all tested patients, including some with parietal lesions, while calculation profiles varied.

Use:

```text
ParietalLesion != QuantityLossByDefinition
```

---

# C synthesis

The evidence supports all of the following simultaneously:

```text
local numerosity-specific perceptual mechanisms are real
small-set and large-set numerosity mechanisms can differ
symbolic and nonsymbolic codes can differ
cross-modal/action numerosity interactions are real
cross-modal numerical representations can align conditionally
```

but not:

```text
one modality-/format-/action-invariant peer numerical process.
```

Best ownership:

```text
QuantitativeRelationRepresentation → HF8
QuantitativeCodeMappingProjection → HF8 + HF23 + HF6
ApproximateNumerosityEstimationProjection → HF20-centered deep projection
ActionNumerosity contribution → HF11
Task/readout/control contribution → HF3
```

No source in this ledger establishes HF24.
