---
schema_version: 1
id: human.deep-foundations.hd14a.sources
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
summary: Primary evidence ledger for HD14-A term separation in Human spatial navigation. Sources establish separations among landmark, route and survey knowledge; allocentric and egocentric reference frames; route knowledge and allocentric map-like processing; landmark/place recognition and navigation; path integration, spatial updating, reorientation and landmark recalibration; visual/body-based navigation cues; active/passive and ecological/virtual acquisition; heading representations; cognitive-map/shortcut measurement; and topographical-disorientation phenotypes. Sources constrain terminology and measurement and do not select a navigation architecture or admit HF24.
evidence_status: verified
readiness: READY
related:
  - human.deep-foundations.hd14a
---
# HD14-A — Primary Evidence Ledger

## S01 — Kim & Bock 2021 — landmark/route/survey parallel acquisition

`Acquisition of landmark, route, and survey knowledge in a wayfinding task: in stages or in parallel?`
Psychological Research 85(5):2098–2106.
PMID: 32666265. DOI: 10.1007/s00426-020-01384-3.

Sixty participants repeatedly learned routes in a VR city. Landmark, route and survey knowledge all increased gradually from early trials, with correlations among them increasing over experience.

Use:

```text
Landmark→Route→Survey
!= mandatory fixed acquisition sequence
```

---

## S02 — Piccardi et al. 2021 — lab vs ecological route/landmark/survey assessment

`Overcoming navigational challenges: A novel approach to the study and assessment of topographical orientation.`
PMID: 34346039.

Laboratory and ecological batteries showed different correspondence across route, landmark, survey and landmark-ordering tasks; route performance was especially sensitive to testing context, plausibly reflecting missing proprioceptive/vestibular information in lab presentation.

Use:

```text
LabNavigation != EcologicalNavigationByDefinition
```

---

## S03 — Bonavita et al. 2025 — self-report vs actual DTD assessment

`Dual Assessment of Developmental Topographical Disorientation: Comparing Self-Reported Measures with Actual Navigational Performance.`
Brain Sciences 15(3):318.
PMID: 40149839. DOI: 10.3390/brainsci15030318.

Self-report and objective navigation battery identified partly different potential DTD cases; objective tests separated route, landmark, survey and landmark-ordering performance.

Use:

```text
SenseOfDirectionSelfReport != ActualNavigationPerformance
```

---

## S04 — Iaria & Barton 2010 — developmental topographical disorientation

`Developmental Topographical Disorientation: a newly discovered cognitive disorder.`
Experimental Brain Research.
PMID: 20431873. DOI: 10.1007/s00221-010-2256-9.

Large DTD series showed lifelong selective orientation/navigation difficulty despite broadly preserved cognition and no acquired lesion; map-formation measures strongly differentiated DTD from controls.

Use:

```text
GeneralCognitionPreserved != NavigationPreservedByDefinition
```

but do not define all DTD as one mechanism.

---

## S05 — Palermo et al. 2022 — DTD phenotype heterogeneity

`Where Am I? Searching for the Tangle in the Developmental Topographical Disorientation.`
PMID: 36278691.

Fifty-four DTD participants and matched controls were characterized across sense of direction, town knowledge, navigation strategies, left-right confusion and agnosic disorders.

Use:

```text
DTD != OnePhenotypeByDefinition
```

---

## S06 — Developmental landmark agnosia 2017

`Evidence of taxonomy for Developmental Topographical Disorientation: Developmental Landmark Agnosia Case 1.`
PMID: 29192795.

A child showed selective familiar-place/landmark recognition impairment with other object recognition spared, supporting separable landmark-recognition failure.

Use:

```text
LandmarkRecognition != NavigationTotality
```

---

## S07 — pure topographical disorientation 2011

`Pure topographical disorientation in a patient with right occipito-temporal lesion.`
PMID: 21206447.

Patient recognized landmarks, judged distances and described routes between landmarks but could not point to unseen landmarks or draw a map of his city.

Use:

```text
AllocentricMapLikeProcessing
!= RouteKnowledge
!= LandmarkRecognition
```

---

## S08 — topographic amnesia 1996

`Topographic amnesia: spatial memory disorder, perceptual dysfunction, or category specific semantic memory impairment?`
PMID: 8609511. DOI: 10.1136/jnnp.60.3.318.

Patient showed normal spatial learning but severe supramodal semantic impairment for familiar buildings/landmarks.

Use:

```text
PlaceSemanticKnowledge != SpatialLearning
```

---

## S09 — Nett et al. 2025 — allocentric vs egocentric spatial maps

`Behavioral investigation of allocentric and egocentric cognitive maps in human spatial memory.`
Neuropsychologia 217:109230.
PMID: 40721154. DOI: 10.1016/j.neuropsychologia.2025.109230.

Allocentric and participant-centered relations predicted different memory measures; feedback did not simply transfer across domains.

Use:

```text
AllocentricSpatialRepresentation != EgocentricSpatialRepresentation
```

---

## S10 — Gramann et al. 2005 — separable reference-frame strategies

`Evidence of separable spatial representations in a virtual navigation task.`
J Exp Psychol Hum Percept Perform 31(6):1199–1213.
PMID: 16366784. DOI: 10.1037/0096-1523.31.6.1199.

Participants preferred egocentric or allocentric path-integration frames but could use nonpreferred frames without reduced accuracy when instructed.

Use:

```text
PreferredReferenceFrame != FixedCapabilityBoundary
```

---

## S11 — RSC reference-frame EEG 2015

`EEG correlates of spatial orientation in the human retrosplenial complex.`
PMID: 26163801. DOI: 10.1016/j.neuroimage.2015.07.009.

Different egocentric and allocentric navigation conditions recruited distinct oscillatory/network signatures, with evidence consistent with retrosplenial transformation roles.

Use as mechanism evidence, not reference-frame definition.

---

## S12 — Lu et al. 2025 — human facing-direction representation

`A Neural Compass in the Human Brain during Naturalistic Virtual Navigation.`
Journal of Neuroscience.
PMID: 40825653.

Naturalistic VR fMRI found RSC and superior-parietal facing-direction tuning stable across perceptually different city versions, locations and task phases, aligned to principal environmental axes.

Use:

```text
HeadingRepresentation = real spatial object
HeadingRepresentation != NavigationTotality
```

---

## S13 — Chadwick & Spiers? 2016 — translation and rotation in path integration

`Which way and how far? Tracking of translation and rotation information for human path integration.`
PMID: 27238897. DOI: 10.1002/hbm.23265.

Human path integration was decomposed into translation and rotation tracking rather than one undifferentiated homing variable.

Use:

```text
PathIntegrationError must type translational and rotational components.
```

---

## S14 — visual influence on path integration 2011

`Visual influence on path integration in darkness indicates a multimodal representation of large-scale space.`
PNAS.
PMID: 21199934. DOI: 10.1073/pnas.1011843108.

Visual gain adaptation influenced subsequent path integration performed in darkness, consistent with combined visual and motion-related/interoceptive information.

Use:

```text
PathIntegration != IdiotheticOnlyByDefinition
```

---

## S15 — Naveilhan et al. 2025 — landmark recalibration of path integration

`Theta Activity Supports Landmark-Based Correction of Naturalistic Human Path Integration.`
Journal of Neuroscience 45(45):e1005252025.
PMID: 41006061. DOI: 10.1523/JNEUROSCI.1005-25.2025.

Accumulated homing errors were corrected by brief landmark presentation; correction depended partly on confidence in self-motion-derived estimates.

Use:

```text
PathIntegration != LandmarkRecalibration
LandmarkCorrection != AutomaticOverwrite
```

---

## S16 — Zhao & Warren 2015 — cue integration and competition

`How you get there from here: interaction of visual landmarks and path integration in human navigation.`
Psychological Science.
PMID: 25944773. DOI: 10.1177/0956797615574952.

Landmarks and path integration were near-optimally integrated to reduce response variability while competing for homing direction under larger cue conflicts.

Use:

```text
CueIntegration != CueCompetition
```

---

## S17 — landmarks in path integration 2012

`The effect of landmarks in human path integration.`
PMID: 22426426.

Landmarks can interfere with origin tracking unless target knowledge changes task allocation.

Use:

```text
LandmarkPresence != LandmarkBenefitByDefinition
```

---

## S18 — eye/gaze path-integration analog 2024

`Spatial updating of gaze position in younger and older adults - A path integration-like process in eye movements.`
Cognition.
PMID: 38875941. DOI: 10.1016/j.cognition.2024.105835.

The study explicitly contrasts continuous updating of current position with configural/route representation used at query time.

Use:

```text
PathIntegrationTask != ContinuousUpdatingProof
```

---

## S19 — amnesia and gaze spatial updating 2025

`Spatial updating in amnesia using an eye movement analogue of a path integration task.`
PMID: 41478320. DOI: 10.1016/j.neuropsychologia.2025.109354.

Two amnesic cases with different lesion patterns used distinct updating strategies/performance profiles, supporting interactive hippocampal/parietal contributions rather than one mechanism.

---

## S20 — nested environments 2003

`Human navigation in nested environments.`
PMID: 12776750. DOI: 10.1037/0278-7393.29.3.398.

Participants could acquire local spatial representations without integrating them into one global system and appeared to reorient/switch between nested environments.

Use:

```text
SpatialUpdating != SimultaneousGlobalMapUpdateByDefinition
```

---

## S21 — Ratliff & Newcombe 2008 — adaptive combination in reorientation

`Reorienting when cues conflict: evidence for an adaptive-combination view.`
Psychological Science 19(12):1301–1307.
PMID: 19121141. DOI: 10.1111/j.1467-9280.2008.02239.x.

Conflict experiments show adults combine geometry and feature cues adaptively rather than requiring one geometric module.

Use:

```text
Reorientation != GeometricModuleByDefinition
```

---

## S22 — principal vs local/medial geometry 2013

`Reorienting in virtual 3D environments: do adult humans use principal axes, medial axes or local geometry?`
PMID: 24223869. DOI: 10.1371/journal.pone.0078985.

Adult reorientation can depend on different geometric information, pressuring one global-axis account.

---

## S23 — target dependence of reorientation cues 2014

`Use of geometric properties of landmark arrays for reorientation relative to remote cities and local objects.`
PMID: 24245534.

Identical/similar landmark arrays differed in reorientation usefulness depending on whether the target concerned local objects or remote city directions and on array salience.

Use:

```text
ReorientationCueUtility = target/environment-relative
```

---

## S24 — Chrastil & Warren 2013 — active/passive survey knowledge components

`Active and passive spatial learning in human navigation: acquisition of survey knowledge.`
J Exp Psychol Learn Mem Cogn 39(5):1520–1537.
PMID: 23565781. DOI: 10.1037/a0032382.

Visual, vestibular, podokinetic and decision components were manipulated separately. Podokinetic information improved metric survey angular accuracy; vestibular information and decision making did not provide the same benefit in that paradigm.

Use:

```text
ActiveNavigation != OneManipulation
```

---

## S25 — Chrastil & Warren 2015 — graph/route knowledge components

`Active and passive spatial learning in human navigation: acquisition of graph knowledge.`
PMID: 25419818.

Decision making contributed to route/graph learning under walking conditions; participants acquired labeled graph knowledge enabling novel/shortest routes.

Use:

```text
GraphKnowledge != LearnedRouteReplay
MetricSurveyKnowledge != GraphKnowledgeByDefinition
```

---

## S26 — vestibular × landmarks 2021

`Vestibular cues improve landmark-based route navigation: A simulated driving study.`
PMID: 34018119.

Vestibular benefits depended on landmark configuration, demonstrating interaction rather than universal vestibular gain.

---

## S27 — Foo et al. 2005 — shortcuts do not transparently prove maps

`Do humans integrate routes into a cognitive map? Map- versus landmark-based navigation of novel shortcuts.`
PMID: 15755239. DOI: 10.1037/0278-7393.31.2.195.

Participants' novel shortcuts depended strongly on landmarks; displaced landmarks attracted responses; coarse survey knowledge appeared when landmarks were unreliable.

Use:

```text
ShortcutSuccess != AccurateMetricCognitiveMapProof
```

---

## S28 — active/passive acquisition of graph/survey differs

`Active and passive spatial learning in human navigation: acquisition of survey knowledge.` and `... acquisition of graph knowledge.`
PMIDs: 23565781, 25419818.

Together they show the components of `active navigation` contribute differently to metric survey versus graph/route knowledge.

---

## S29 — route/survey forgetting 2008

`Differentiated forgetting rates of spatial knowledge in humans in the absence of repeated testing.`
PMID: 18720220. DOI: 10.1080/09658210802286931.

Route knowledge declined more than survey knowledge over delay without repeated testing.

Use:

```text
SpatialKnowledgeStrength != OneScalar
```

---

## S30 — body-based route/survey without vision 2004

`Acquisition of route and survey knowledge in the absence of vision.`
PMID: 15111279.

Blindfolded walking supported accurate route components; more complex pathway completion produced distinct errors and evidence compatible with survey-like representation.

Use:

```text
SpatialKnowledge != VisualFormat
RouteComponents != SurveyInference
```

---

## S31 — real vs virtual ecological validity 2015

`Ecological validity of virtual environments to assess human navigation ability.`
PMID: 26074831.

Real-life performance exceeded virtual conditions for some survey tasks; hybrid conditions sometimes better approximated real navigation.

Use:

```text
VirtualNavigation != RealNavigationByDefinition
```

---

## S32 — Iaria et al. 2007 — map formation vs use neural contributions

`Retrosplenial and hippocampal brain regions in human navigation: complementary functional contributions to the formation and use of cognitive maps.`
PMID: 17298595. DOI: 10.1111/j.1460-9568.2007.05371.x.

Different hippocampal/RSC contributions were reported during map formation/use.

Use only as implementation evidence:

```text
HippocampalActivity != CognitiveMapDefinition
```

---

## S33 — neural head direction / global reference frame 2016

`The Human Retrosplenial Cortex and Thalamus Code Head Direction in a Global Reference Frame.`
PMID: 27307227.

Human heading-related signals incorporated global landmarks/body-based orientation cues.

Use:

```text
HeadingRepresentation != LocationRepresentation
```

---

# A synthesis

The primary evidence forces at least:

```text
LandmarkRecognition != Navigation
RouteKnowledge != SurveyKnowledge
Egocentric != Allocentric
ReferenceFrameContent != ReferenceFrameTransformation
PathIntegration != LandmarkNavigation
PathIntegration != Reorientation
SpatialUpdating != PathIntegrationByDefinition
Recalibration != Reorientation
Navigation != Locomotion
SenseOfDirection != NavigationAccuracy
```

and turns `CognitiveMap` into a theory-laden umbrella requiring explicit representational properties.

No source here establishes HF24.
