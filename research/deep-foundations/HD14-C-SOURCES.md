---
schema_version: 1
id: human.deep-foundations.hd14c.sources
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
summary: Primary evidence ledger for HD14-C spatial ownership extraction. Sources focus on process-selective dissociations for path integration and reference-frame transformation rather than generic navigation correlations: posterior-parietal rTMS separating vestibular displacement/path integration from velocity perception; acute TPJ lesions separating vestibular-guided spatial orientation from preserved self-motion perception; right temporal lobectomy separating integrated homing from simple component reproduction; right posterior lesions impairing nonvisual egocentric updating; hippocampal/MTL lesions showing alternate short-path PI implementations; imagery-neglect and developmental topographical-disorientation cases preserving spatial representation while impairing egocentric↔allocentric transformation/use; PPC lesions preserving allocentric judgments while impairing egocentric navigation; TGA showing the opposite allocentric-selective profile; and retrosplenial heading-disorientation cases preserving object-location information while failing integration with changes in body direction. Evidence establishes real PI and reference-frame transformation processes but supports their allocation as HF20/HF11/HF8/HF3 projections/interfaces rather than HF24.
evidence_status: verified
readiness: READY
related:
  - human.deep-foundations.hd14c
---
# HD14-C — Primary Evidence Ledger

## S01 — Seemungal et al. 2008 — PI vs vestibular velocity perception

`Posterior parietal rTMS disrupts human Path Integration during a vestibular navigation task.`
Neuroscience Letters 437(2):88–92.
PMID: 18440143. DOI: 10.1016/j.neulet.2008.03.067.

Repetitive TMS over posterior parietal cortex disrupted vestibular-derived angular displacement/path-integration performance. Separate testing did not associate right PPC stimulation with vestibular velocity perception.

Use:

```text
VestibularVelocityPerception
!= VestibularDisplacementIntegration
```

This establishes an intermediate PI transform but not a peer semantic owner.

---

## S02 — Kaski et al. 2016 — self-motion perception preserved, spatial orientation impaired

`Temporoparietal encoding of space and time during vestibular-guided orientation.`
Brain 139(Pt 2):392–403.
PMID: 26719385. PMCID: PMC4805090. DOI: 10.1093/brain/awv370.

Among 18 acute right-hemisphere stroke patients, the four with TPJ damage showed contralesional impairment in travelled-distance/spatial-orientation judgments and motion-duration estimates. All tested lesion patients showed normal self-motion perception.

Use:

```text
SelfMotionPerception
!= VestibularGuidedSpatialOrientation
```

and retain a specialized sensory→spatial-state integration stage.

---

## S03 — Worsley et al. 2001 — integrated homing vs component reproduction

`Path integration following temporal lobectomy in humans.`
Neuropsychologia 39(5):452–464.
PMID: 11254927. DOI: 10.1016/S0028-3932(00)00140-8.

Right temporal lobectomy patients were impaired at estimating the turn needed to return to origin after a two-distance/one-turn route. They were also impaired at route-reproduction turn but the two deficits did not correlate. Single-distance and single-turn reproduction did not differ between groups; mental rotation and left-right orientation were included as controls.

Use:

```text
IntegratedHomingState
!= SimpleDistanceOrTurnReproduction
```

---

## S04 — Yamamoto et al. 2004 — linear locomotor PI after MTL lobectomy

`Path integration deficits during linear locomotion after human medial temporal lobectomy.`
PMID: 15165344.

Right but not left medial temporal lobectomy reduced consistency and produced systematic underregistration during blind walking to previously viewed targets.

Use as evidence that PI subcomponents can be lesion-sensitive and lateralized.

---

## S05 — Shrager et al. 2008 — short PI can survive hippocampal/entorhinal lesion

`Neural basis of the cognitive map: path integration does not require hippocampus or entorhinal cortex.`
PNAS.
PMID: 18687893. DOI: 10.1073/pnas.0805414105.

Patients with hippocampal or larger MTL lesions including entorhinal cortex performed short blindfolded path-integration pointing/distance estimates comparably to controls.

Use:

```text
PathIntegration != OneHippocampalEntorhinalImplementation
```

---

## S06 — Kim et al. 2013 — alternate/limited-demand PI implementation

`Contrasting effects on path integration after hippocampal damage in humans and rats.`
PNAS.
PMID: 23404706. DOI: 10.1073/pnas.1300869110.

Human MTL-lesion patients could perform accurately when paths were short/simple, consistent with alternative or working-memory-supported performance under limited demands.

Use:

```text
PathIntegration_D != PathIntegration_E by implementation
```

---

## S07 — Farrell & Robertson 2000 — nonvisual egocentric spatial updating

`The automatic updating of egocentric spatial relationships and its impairment due to right posterior cortical lesions.`
Neuropsychologia 38(5):585–595.
PMID: 10689036. DOI: 10.1016/S0028-3932(99)00123-2.

Blindfolded patients pointed to previously seen targets after body rotation. Right dorsal/posterior lesions impaired updating, with systematic underestimation of body rotation.

Use:

```text
StoredTargetRelation
!= UpdatedBodyCenteredRelation
```

---

## S08 — Palermo et al. 2012 — direct ego↔allo transformation deficit

`Cognitive maps in imagery neglect.`
Neuropsychologia 50(5):904–912.
PMID: 22310104. DOI: 10.1016/j.neuropsychologia.2012.01.030.

Twenty-eight right-brain-damaged patients and controls were tested on map creation/use. Imagery-neglect patients showed no specific deficit in creating or using a cognitive map but failed transformation between egocentric and allocentric environmental representations.

Use:

```text
SpatialMapContentPreserved
+
ReferenceFrameTransformationImpaired
```

This is direct evidence that transformation is a distinct process.

---

## S09 — Conson et al. 2018 — developmental allocentric→egocentric map-use deficit

`Selective map-following navigation deficit: A new case of developmental topographical disorientation.`
PMID: 29614925. DOI: 10.1080/13803395.2018.1451493.

Patient C.F. learned and followed routes, built cognitive maps and recognized landmarks but showed a dramatic deficit when allocentrically encoded map information had to guide navigation in a novel environment.

Use:

```text
AllocentricRepresentationPreserved
+
AllocentricToEgocentricUseImpaired
```

---

## S10 — Ciaramelli et al. 2010 — allocentric preserved, egocentric navigation impaired

`Mental space travel: damage to posterior parietal cortex prevents egocentric navigation and reexperiencing of remote spatial memories.`
PMID: 20438261. DOI: 10.1037/a0019181.

Seven focal PPC-lesion patients were unimpaired on allocentric distance/proximity judgments but failed route navigation; left-lesioned patients also showed weaker landmark sequencing.

Use:

```text
AllocentricJudgmentPreserved
+
EgocentricNavigationImpaired
```

---

## S11 — parietal lesion virtual-reality study 2008

`Egocentric memory impaired and allocentric memory intact as assessed by virtual reality in subjects with unilateral parietal cortex lesions.`
PMID: 18789955.

Twenty-four unilateral parietal-lesion patients were strongly impaired on a virtual egocentric maze while allocentric virtual-park learning was normal.

Use as convergent frame-selective evidence.

---

## S12 — TGA 2019 — allocentric impaired, egocentric spared

`Prolonged allocentric navigation deficits indicate hippocampal damage in TGA.`
PMID: 30552301.

Eighteen TGA patients showed impaired allocentric but not egocentric route planning three days after onset, despite recovery of verbal and figural memory. Allocentric error/shortcut deficits remained detectable at follow-up.

Use with S10/S11 as opposite frame pressure:

```text
AllocentricNavigation
can fail with EgocentricNavigation relatively spared.
```

---

## S13 — Gomez et al. 2011 — allocentric preserved, egocentric updating impaired

`Spatial deficits in an amnesic patient with hippocampal damage: questioning the multiple trace theory.`
Hippocampus.
PMID: 21805527. DOI: 10.1002/hipo.20968.

Patient M.R. was preserved on three allocentric immediate-spatial tasks while impaired on five egocentric-updating tasks.

Use as additional frame/update dissociation.

---

## S14 — Hashimoto et al. 2010 — heading disorientation integration deficit

`Heading disorientation: a new test and a possible underlying mechanism.`
European Neurology 63(2):87–93.
PMID: 20090342. DOI: 10.1159/000276398.

Three heading-disorientation patients with right retrosplenial involvement performed well when retaining card locations but poorly when integrating those locations with changes in body direction.

Use:

```text
StoredSpatialLocations
!= IntegrationWithBodyDirectionChange
```

---

## S15 — Takahashi et al. 1997 — pure retrosplenial directional disorientation

`Pure topographic disorientation due to right retrosplenial lesion.`
PMID: 9270578.

Patients could identify familiar buildings/landscapes but had severe difficulty recovering directional relationships between distant familiar locations.

Use:

```text
LandmarkRecognitionPreserved
+
DirectionalOrientationImpaired
```

---

## S16 — map-following in right brain damage 2012

`Map-following skills in left and right brain-damaged patients with and without hemineglect.`
PMID: 23036103. DOI: 10.1080/13803395.2012.727385.

Right-brain-damaged patients, especially with neglect, showed map-following deficits; some right-brain-damaged patients without neglect also showed specific impairment, supporting a right-sided contribution to superimposing allocentric map information onto current space.

---

# C synthesis

The evidence supports both:

```text
PathIntegrationStateUpdatingProjection = real
ReferenceFrameTransformationProjection = real
```

and rejects:

```text
RawVestibularPerception = PI
SpatialRepresentation = FrameTransformation
```

But after restoring HF20/HF11/HF8/HF3, both are representable as typed state-estimation/interface projections.

Therefore:

```text
SpatialNavigation→HF24
= CLOSED / NOT ADMITTED
```

No source in this ledger establishes peer spatial deletion harm.
