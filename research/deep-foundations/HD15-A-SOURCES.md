---
schema_version: 1
id: human.deep-foundations.hd15a.sources
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
summary: Primary-evidence ledger for HD15-A term separation and measurement decomposition. Sources establish body-schema/body-image dissociations; proprioceptive drift versus ownership dissociations; body-part versus full-body ownership; ownership versus self-location and agency; structural/reference-frame constraints; proprioceptive, vestibular and developmental effects; somatoparaphrenia/anosognosia/neglect separations; active/passive movement; intentional-binding measurement limits; autonomic/threat readout limits; and virtual/robot/BMI perturbations. No source establishes one Bodily Self process, HF24 or HOC11.
evidence_status: verified
readiness: READY
related:
  - human.deep-foundations.hd15a
---
# HD15-A — Primary Evidence Ledger

## S01 — Kammers, van der Ham & Dijkerman 2006 — perception/action body representations

`Dissociating body representations in healthy individuals: differential effects of a kinaesthetic illusion on perception and action.`
Neuropsychologia 44(12):2430–2436.
PMID: 16750227.
DOI: 10.1016/j.neuropsychologia.2006.04.009.

Kinaesthetic illusion affected perceptual and action-oriented bodily judgments differently.

Use:

```text
PerceptualBodyRepresentation
!= ActionGuidingBodyRepresentation
```

Limit: does not prove exactly two exhaustive representations.

---

## S02 — Dijkerman-group neuropsychological case 2011 — body image vs body schema

`Evidence for dissociable representations for body image and body schema from a patient with visual neglect.`
PMID: 21780992.

A neuropsychological case showed different fake limbs could be incorporated into perceptual and action-related bodily representations simultaneously.

Use:

```text
BodyImageLikeRepresentation
!= BodySchemaLikeRepresentation
```

Limit: single-patient evidence; architecture, not prevalence.

---

## S03 — Dupraz et al. 2024 — ownership vs kinaesthetic illusion

`Body ownership and kinaesthetic illusions: Dissociated bodily experiences for distinct levels of body consciousness?`
Consciousness and Cognition 117:103630.
PMID: 38183843.
DOI: 10.1016/j.concog.2023.103630.

Two avatar experiments manipulated visuomotor synchrony. Ownership depended on synchrony, while kinaesthetic illusion did not follow the same dependency.

Use:

```text
ExplicitBodyOwnership
!= Kinaesthetic/BodySchemaLikeEffect
```

---

## S04 — Rohde, Di Luca & Ernst 2011 — drift vs ownership

`The Rubber Hand Illusion: feeling of ownership and proprioceptive drift do not go hand in hand.`
PLoS ONE 6:e21659.
PMID: 21738756.
DOI: 10.1371/journal.pone.0021659.

Proprioceptive drift occurred under conditions that did not generate corresponding subjective ownership; subjective ratings and drift followed different patterns.

Use:

```text
ProprioceptiveDrift != SubjectiveOwnership
```

---

## S05 — Abdulkarim & Ehrsson 2016 — no causal drift→ownership link

`No causal link between changes in hand position sense and feeling of limb ownership in the rubber hand illusion.`
PMID: 26555651.

Mechanical manipulation of sensed hand position toward/away from the rubber hand did not change ownership illusion strength.

Use:

```text
HandPositionSenseChange
!= CauseOfOwnershipChangeByDefinition
```

---

## S06 — Gallagher et al. 2021 — somatic RHI drift/report dissociation

`Dissociation of proprioceptive drift and feelings of ownership in the somatic rubber hand illusion.`
Acta Psychologica 212:103192.
PMID: 33137614.
DOI: 10.1016/j.actpsy.2020.103192.

Use:

```text
Drift and ownership report remain separable even in a nonvisual/somatic variant.
```

---

## S07 — O'Kane, Chancel & Ehrsson 2024 — body-part vs full-body ownership

`Hierarchical and dynamic relationships between body part ownership and full-body ownership.`
Cognition 246:105697.
DOI: 10.1016/j.cognition.2023.105697.

Local synchrony mainly controlled local part ownership; full-body ownership showed nonlinear dependence on the number of coherently stimulated parts and whole-body feedback onto parts.

Use:

```text
BodyPartOwnership != FullBodyOwnership
```

---

## S08 — Kondo et al. 2020 — scrambled-body separation

`Scrambled body differentiates body part ownership from the full body illusion.`
Scientific Reports 10.
PMID: 32210268.
DOI: 10.1038/s41598-020-62121-9.

Synchronous scrambled body-parts could induce part ownership without full-body ownership, whereas normal layout supported both.

Use:

```text
LocalPartOwnership can survive without coherent FullBodyOwnership.
```

---

## S09 — Maselli & Slater 2014 — ownership vs self-location

`Sliding perspectives: dissociating ownership from self-location during full body illusions in virtual reality.`
Frontiers in Human Neuroscience 8:693.
PMID: 25309383.
DOI: 10.3389/fnhum.2014.00693.

Third-person perspective could shift self-location without corresponding ownership; spatial overlap changed ownership differently.

Use:

```text
SelfLocation != BodyOwnership
```

---

## S10 — Frisco et al. 2024/2025 — spatial prediction and ownership/disownership

`I am where I believe my body is: The interplay between body spatial prediction and body ownership.`
PMID: 39666650.

VR rubber-hand and first-person full-body paradigms manipulated body alignment and measured localization, embodiment/disembodiment questionnaire and skin conductance.

Use:

```text
BodyLocationEstimate interacts with ownership/disownership
without identity.
```

---

## S11 — Kalckert & Ehrsson 2012 — ownership vs agency

`Moving a Rubber Hand that Feels Like Your Own: A Dissociation of Ownership and Agency.`
Frontiers in Human Neuroscience.
PMID: 22435056.

Passive synchronous movement abolished agency while leaving ownership; anatomical incongruence reduced ownership more than agency.

Use:

```text
BodyOwnership != SenseOfAgency
```

---

## S12 — Costantini & Haggard 2007 — ownership reference-frame constraints

`The rubber hand illusion: sensitivity and reference frame for body ownership.`
Consciousness and Cognition 16:229–240.
PMID: 17317221.
DOI: 10.1016/j.concog.2007.01.001.

Ownership depended on spatial/anatomical relations and hand-centered congruence, not synchrony in an unconstrained coordinate-free way.

Use:

```text
TemporalSynchrony alone != ownership condition set
ReferenceFrame matters.
```

---

## S13 — Tsakiris et al. 2010 — corporeal constraint

`Hands only illusion: multisensory integration elicits sense of ownership for body parts but not for non-corporeal objects.`
Experimental Brain Research.
PMID: 19820918.
DOI: 10.1007/s00221-009-2039-3.

Passive visuotactile synchrony induced ownership for plausible hand-like targets but not arbitrary noncorporeal objects.

Use:

```text
StructuralBodyPrior can constrain passive ownership illusions.
```

---

## S14 — Ma & Hommel 2015 — active noncorporeal proxy ownership

`Body-ownership for actively operated non-corporeal objects.`
Consciousness and Cognition.
PMID: 26094223.

Active sensorimotor contingencies produced ownership reports for noncorporeal virtual proxies.

Use:

```text
CorporealAppearance != universally necessary under active-control regimes.
```

Together S13+S14 forbid a universal one-factor structural or sensorimotor theory at term-separation stage.

---

## S15 — Walsh et al. 2011 — proprioceptive contribution

`Proprioceptive signals contribute to the sense of body ownership.`
Journal of Physiology.
PMID: 21521765.
DOI: 10.1113/jphysiol.2011.204941.

Movement-derived proximal proprioceptive evidence could support illusory ownership despite local digital nerve block; active movement did not universally strengthen ownership over passive movement.

Use:

```text
Proprioception contributes
but
Proprioception != ownership
Active > Passive is not universal.
```

---

## S16 — Chancel et al. 2023 — proprioceptive uncertainty

`Proprioceptive uncertainty promotes the rubber hand illusion.`
Cortex.
PMID: 37269634.
DOI: 10.1016/j.cortex.2023.04.005.

Tendon-vibration manipulation of proprioceptive noise increased ownership-illusion probability and was captured by a Bayesian causal-inference model.

Use:

```text
Reliability/uncertainty of sensory evidence matters.
```

It supports a rival model; it does not settle HD15 architecture.

---

## S17 — Lopez et al. 2012 — vestibular/nonvisual ownership

`Tactile and vestibular mechanisms underlying ownership for body parts: a non-visual variant of the rubber hand illusion.`
Neuroscience Letters.
PMID: 22322072.
DOI: 10.1016/j.neulet.2012.01.055.

Use:

```text
BodyOwnership != VisualOwnershipByDefinition
Vestibular evidence can modulate ownership.
```

---

## S18 — Cowie et al. 2013 — developmental dissociable pathways

`Children's responses to the rubber-hand illusion reveal dissociable pathways in body representation.`
Psychological Science.
PMID: 23538915.
DOI: 10.1177/0956797612462902.

Children 4–9 showed adult-like sensitivity to visual-tactile synchrony for one measure but stronger visual capture of hand position; explicit embodiment related differently to these pathways.

Use:

```text
VisualTactileOwnershipPath
!= VisualProprioceptiveLocalizationPath
Adult cue weighting is not developmentally fixed.
```

---

## S19 — Cowie et al. 2016 — continued development to ~10–11 years

`The development of multisensory body representation and awareness continues to 10 years of age: Evidence from the rubber hand illusion.`
Journal of Experimental Child Psychology.
PMID: 26601752.
DOI: 10.1016/j.jecp.2015.10.003.

Use:

```text
Bodily multisensory weighting has a developmental trajectory.
```

---

## S20 — Martinaud et al. 2017 — anosognosia vs disturbed ownership lesion analysis

`Motor versus body awareness: Voxel-based lesion analysis in anosognosia for hemiplegia and somatoparaphrenia following right hemisphere stroke.`
Cortex.
PMID: 27494375.
DOI: 10.1016/j.cortex.2016.07.001.

Multi-centre N=70 lesion study explicitly compared anosognosia, disturbed ownership and rare selective profiles.

Use:

```text
MotorAwarenessDeficit
!= DisturbedBodyOwnershipByDefinition
```

---

## S21 — Fotopoulou/Jenkinson et al. 2011 — mirror reversal of somatoparaphrenia

`Mirror-view reverses somatoparaphrenia: dissociation between first- and third-person perspectives on body ownership.`
Neuropsychologia.
PMID: 22023911.
DOI: 10.1016/j.neuropsychologia.2011.10.011.

In somatoparaphrenic cases, ownership judgments of the same limb could change rapidly between direct and mirror views.

Use:

```text
FirstPersonPerspective != ThirdPersonBodyRecognition
Somatoparaphrenia != immutable biological-body representation loss
```

---

## S22 — Cataldo et al. 2025 — covert post-stroke disownership

`Unveiling covert disownership after stroke: a neuropsychological and neural approach.`
Brain Communications 7(3):fcaf217.
PMID: 40585817.
DOI: 10.1093/braincomms/fcaf217.

105 stroke patients and 55 controls. Body-part-specific covert disownership was associated with distributed disconnection patterns.

Use:

```text
Disownership is lesion-sensitive and part-specific
but
DistributedImplementation != one semantic owner.
```

---

## S23 — Romano et al. 2015 — robot hand drift without ownership

`The robot hand illusion: inducing proprioceptive drift through visuo-motor congruency.`
Neuropsychologia 70:414–420.
PMID: 25446964.
DOI: 10.1016/j.neuropsychologia.2014.10.033.

Synchronous human–robot movement shifted proprioceptive hand localization without corresponding ownership modulation.

Use:

```text
VisuomotorCongruence can change localization without ownership.
```

---

## S24 — Slater et al. 2013 — full-body ownership building blocks

`The building blocks of the full body ownership illusion.`
Frontiers / immersive VR study.
PMID: 23519597.

Manipulated perspective, visual body appearance, visuotactile and sensorimotor contingencies.

Use:

```text
FullBodyOwnership depends on interacting perspective/structure/cue relations.
```

---

## S25 — Imaizumi & Tanno 2019 — binding and explicit agency can coincide

`Intentional binding coincides with explicit sense of agency.`
Consciousness and Cognition 67:1–15.
PMID: 30471470.
DOI: 10.1016/j.concog.2018.11.005.

Within-person trial-by-trial associations occurred between explicit agency ratings and temporal binding in tested auditory/visual action-outcome tasks.

Use:

```text
IntentionalBinding can covary with AgencyJudgment
```

but covariance is not identity.

---

## S26 — Ruess, Thomaschke & Kiesel 2020 — expectancy pressure on binding

`Acting and reacting: Is intentional binding due to sense of agency or to temporal expectancy?`
Journal of Experimental Psychology: Human Perception and Performance.
PMID: 31697161.
DOI: 10.1037/xhp0000700.

Manipulated delay/predictability and compared agency judgment with temporal-expectancy signatures.

Use:

```text
IntentionalBinding has non-agency explanatory competitors.
```

---

## S27 — Poonian & Cunnington 2013 — binding for observed actions

`Intentional binding in self-made and observed actions.`
Experimental Brain Research.
PMID: 23575956.
DOI: 10.1007/s00221-013-3505-5.

Binding-like interval compression also occurred when observing others' actions.

Use:

```text
IntentionalBinding != self-agency-specific by definition.
```

---

## S28 — Kong et al. 2024 — direct challenge to “intentional” binding

`No evidence in favor of the existence of "intentional" binding.`
Journal of Experimental Psychology: Human Perception and Performance.
PMID: 38635224.
DOI: 10.1037/xhp0001204.

Primary experimental work challenged whether the standard temporal compression effect contains a specifically intentional component under the tested controls.

Use:

```text
IntentionalBinding != transparent AgencyMeter
```

---

## S29 — Seghezzi, Parés-Pujolràs & Haggard 2026 — binding changes during learning

`Intentional binding decreases during learning: Implications for sense of agency.`
Quarterly Journal of Experimental Psychology 79(3):612–629.
PMID: 40454440.
DOI: 10.1177/17470218251349521.

Use:

```text
Binding is history/task dependent.
```

---

## S30 — Kilteni et al. 2015 — threat physiology vs ownership

`Defensive activation during the rubber hand illusion: Ownership versus proprioceptive drift.`
PMID: 25960069.

Threat potentiated defensive responses, but the relation among threat, ownership and drift was non-identical.

Use:

```text
ThreatPhysiology != Ownership
```

---

## S31 — virtual-hand impact/threat experiment 2013 — affective resonance can dissociate

`The virtual-hand illusion: effects of impact and threat on perceived ownership and affective resonance.`
PMID: 24046762.

Threat could evoke physiological involvement even when synchronicity/ownership was weak.

Use:

```text
SCR/AffectiveResonance != BodyOwnershipByDefinition
```

---

## S32 — Applebaum et al. 2025 — implicit kinematics vs explicit agency

`The Body Knows Better: Sensorimotor signals reveal the interplay between implicit and explicit Sense of Agency in the human mind.`
Cognition 254:105992.
PMID: 39454392.
DOI: 10.1016/j.cognition.2024.105992.

Virtual-hand conflict could be decoded from kinematics better than participants explicitly classified the conflict.

Use:

```text
ImplicitSensorimotorInformation != ExplicitAgencyJudgment
```

---

## S33 — Oi et al. 2024 — motor control / control detection / attribution hierarchy

`Hierarchical analysis of the sense of agency in schizophrenia: motor control, control detection, and self-attribution.`
Schizophrenia 10:79.
DOI: 10.1038/s41537-024-00512-x.

Use:

```text
MotorControl != ControlDetection != SelfAttribution
```

Clinical label does not identify one mechanism.

---

## S34 — Pryke et al. 2025 — causal agency perturbation

`The causal neural substrates underpinning prospective and retrospective sense of agency.`
Cortex.
PMID: 40398204.
DOI: 10.1016/j.cortex.2025.04.014.

Double-blind sham-controlled crossover N=104 targeted dlPFC/TPJ during an implicit agency task.

Use:

```text
Agency-relevant processes are causally manipulable
but prospective and retrospective evidence need not be one process.
```

---

## S35 — Bertoni et al. 2025 — BMI premovement agency dynamics

`Pre-movement sensorimotor oscillations shape the sense of agency by gating cortical connectivity.`
Nature Communications 16:3594.
DOI: 10.1038/s41467-025-58683-9.

Implanted and EEG-BMI paradigms related premovement sensorimotor state to later agency judgments.

Use:

```text
BMI separates intention-related Human state from ordinary limb execution.
```

---

## S36 — van der Goot et al. 2026 — temporally staged conflict processing

`Neural responses to sensorimotor conflict in an embodied agency task.`
Cortex 201:64–80.
PMID: 42134064.
DOI: 10.1016/j.cortex.2026.03.023.

Preregistered embodied-VR EEG work found early conflict-specific and later more generalized processing patterns.

Use:

```text
Agency-related processing is temporally decomposable.
```

---

# Evidence synthesis

The primary-evidence ledger forces the following minimum architecture:

```text
physical body facts
!= body-state estimate
!= body schema/image/model family
!= ownership
!= self-location
!= perspective
!= agency
!= actual control
!= temporal binding
!= threat physiology
```

Strong direct dissociations exist across:

```text
part vs whole
ownership vs localization
ownership vs agency
implicit vs explicit readout
perception vs action representation
motor awareness vs ownership
first vs third person perspective
developmental cue weighting
biological vs proxy control
```

No source establishes one Bodily Self semantic owner, HF24, or HOC11.
