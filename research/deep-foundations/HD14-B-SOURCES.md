---
schema_version: 1
id: human.deep-foundations.hd14b.sources
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
summary: Primary evidence ledger for HD14-B rival spatial-navigation architectures. Sources cover selective DTD map formation versus map use, allocentric/egocentric access, hippocampal/entorhinal spatial coding and its limits, path integration under hippocampal lesions and cortisol perturbation, remote spatial memory after hippocampal damage, vestibular contributions, landmark/path-integration cue interaction, landmark-dependent shortcuts, graph learning, active/passive acquisition, sensory substitution/blindness and grid-like coding beyond self-navigation including imagined, olfactory, bodily self-location, social and non-spatial conceptual regimes. Evidence supports layered plural navigation architecture and leaves PathIntegrationStateUpdatingProjection and ReferenceFrameTransformationProjection as ownership-relevant residuals; no source establishes HF24.
evidence_status: verified
readiness: READY
related:
  - human.deep-foundations.hd14b
---
# HD14-B — Primary Evidence Ledger

## B1 / B5 / B6 — Cognitive maps and reference-frame use

### S01 — Iaria et al. 2010
`Developmental Topographical Disorientation: a newly discovered cognitive disorder.`
PMID: 20431873. DOI: 10.1007/s00221-010-2256-9.

120 DTD cases differed from controls mainly in orientation/navigation-domain measures, with cognitive-map formation a strong differentiator.

Use as positive selective-navigation evidence, not one-mechanism proof.

### S02 — Conson et al. 2018
`Selective map-following navigation deficit: A new case of developmental topographical disorientation.`
PMID: 29614925. DOI: 10.1080/13803395.2018.1451493.

Patient C.F. learned/followed routes, built cognitive maps and recognized landmarks but was selectively impaired in translating allocentric map information into egocentrically guided navigation.

Use:

```text
MapFormation != MapUse
AllocentricContent != EgocentricActionUse
```

### S03 — Ciaramelli et al. 2010
`Mental space travel: damage to posterior parietal cortex prevents egocentric navigation and reexperiencing of remote spatial memories.`
PMID: 20438261. DOI: 10.1037/a0019181.

Seven PPC-lesion patients preserved allocentric distance/proximity judgments but failed familiar route navigation requiring egocentric access/use.

Use:

```text
AllocentricKnowledgePreserved + EgocentricNavigationImpaired
```

### S04 — Gramann et al. 2005
`Evidence of separable spatial representations in a virtual navigation task.`
PMID: 16366784. DOI: 10.1037/0096-1523.31.6.1199.

Participants showed egocentric/allocentric strategy preferences but could switch without reduced accuracy when instructed.

Use:

```text
PreferredFrame != FixedCapabilityBoundary
```

---

# B1 / B4 — Map versus graph / landmark structure

### S05 — Foo et al. 2005
`Do humans integrate routes into a cognitive map? Map- versus landmark-based navigation of novel shortcuts.`
PMID: 15755239. DOI: 10.1037/0278-7393.31.2.195.

Shortcut success depended strongly on landmarks; displaced landmarks attracted responses; coarse survey knowledge emerged when landmarks were unreliable.

Use:

```text
ShortcutSuccess != AccurateMetricMapProof
PathIntegration != SufficientMetricMapGenerator
```

### S06 — Chrastil & Warren 2015
`Active and passive spatial learning in human navigation: acquisition of graph knowledge.`
PMID: 25419818. DOI: 10.1037/xlm0000082.

Participants acquired labeled graph knowledge supporting novel/shortest routes; decision making rather than idiothetic information was the main active contributor in that graph/route paradigm.

Use:

```text
GraphKnowledge != RouteReplay
GraphKnowledge != MetricSurveyKnowledge
```

### S07 — Warren et al. 2014
`From cognitive maps to cognitive graphs.`
PMID: 25389769. DOI: 10.1371/journal.pone.0112544.

Free exploration produced spatial knowledge consistent with a labeled graph: topological connections with local metric information; frequently chosen novel paths had not been traversed during learning.

Use:

```text
EnvironmentalGraphRepresentation = real representational family
```

---

# B2 — Hippocampal/entorhinal positive evidence

### S08 — Iaria et al. 2007
`Retrosplenial and hippocampal brain regions in human navigation: complementary functional contributions to the formation and use of cognitive maps.`
PMID: 17298595. DOI: 10.1111/j.1460-9568.2007.05371.x.

Human fMRI differentiated hippocampal contributions during formation/use of map-like spatial knowledge.

### S09 — Schinazi et al. 2013
`Hippocampal size predicts rapid learning of a cognitive map in humans.`
PMID: 23505031.

Right posterior hippocampal size predicted flexible spatial inference after participants learned connected campus routes.

### S10 — Hartley et al. 2003
`The well-worn route and the path less traveled: distinct neural bases of route following and wayfinding in humans.`
PMID: 12628177. DOI: 10.1016/S0896-6273(03)00095-3.

Wayfinding and route following recruited distinct patterns; accurate wayfinding involved hippocampal activity while route following related more strongly to caudate activity across participants.

---

# B2/B3 — Hippocampal necessity limits

### S11 — Shrager et al. 2008
`Neural basis of the cognitive map: path integration does not require hippocampus or entorhinal cortex.`
PMID: 18687893. DOI: 10.1073/pnas.0805414105.

Patients with hippocampal or larger MTL lesions including entorhinal cortex performed short blindfolded path-integration pointing/distance estimates as accurately as controls.

Use:

```text
PathIntegration != HippocampalEntorhinalProcessOnly
```

### S12 — Kim et al. 2013
`Contrasting effects on path integration after hippocampal damage in humans and rats.`
PMID: 23404706. DOI: 10.1073/pnas.1300869110.

Human MTL-lesion patients could perform accurately when outward paths were short/simple, while rats with hippocampal lesions were impaired. Authors proposed working-memory-supported human performance under limited demands.

### S13 — Urgolites et al. 2017
`Map reading, navigating from maps, and the medial temporal lobe.`
PMID: 27911842.

Five patients with hippocampus-limited lesions performed like controls on map reading/navigation, including map-geographical coordinate conflict; a patient with larger MTL lesions showed impairment under maximal conflict.

Use:

```text
MapCoordinateTransformation != HippocampusNecessaryByDefinition
```

### S14 — Rosenbaum et al. 2000
`Remote spatial memory in an amnesic person with extensive bilateral hippocampal lesions.`
PMID: 11017178. DOI: 10.1038/79867.

Patient K.C. retained broad allocentric neighborhood/world spatial knowledge while losing detail/non-salient landmark information.

Use:

```text
Hippocampus != ExclusivePermanentStoreOfAllSpatialRelations
```

### S15 — Ryan et al. 2025
`Spatial updating in amnesia using an eye movement analogue of a path integration task.`
PMID: 41478320. DOI: 10.1016/j.neuropsychologia.2025.109354.

Two amnesic cases with different lesion patterns used distinct updating strategies; one extensive-MTL case retained accuracy with altered latency/revisit strategy, whereas another with additional posterior-parietal damage showed reduced accuracy.

Use as evidence for interactive/alternative implementations.

---

# B2/B3 — 2026 causal path-integration perturbation

### S16 — 2026 cortisol / path integration
`Cortisol treatment impairs path integration and alters grid-like representations in the male human entorhinal cortex.`
PMID: 41818192.

Within-subject cortisol/placebo study in 39 healthy men. Cortisol impaired virtual homing/path-integration performance and altered entorhinal grid-like representation; reported navigation pattern measured by landmark proximity was not affected in the same way.

Use:

```text
EntorhinalGridLikeProcess can contribute selectively to PI
```

without claiming navigation totality.

---

# B3 / B8 — self-motion and vestibular evidence

### S17 — Kearns et al. 2002
`Path integration from optic flow and body senses in a homing task.`
PMID: 11954696. DOI: 10.1068/p3311.

Optic flow and body senses both influenced path integration; rotational and translational visual-flow information contributed differently.

### S18 — Klatzky et al. 2019
`Vision and proprioception make equal contributions to path integration in a novel homing task.`
PMID: 31228680.

Loop-closure paradigm found optic flow and proprioception made roughly equal independent contributions; vestibular-only condition was near chance and cue combination was not ideal Bayesian integration.

Use:

```text
PathIntegration = multimodal
SpatialCueIntegration != UniversalBayesOptimality
```

### S19 — Cohen 2000
`Vestibular disorders and impaired path integration along a linear trajectory.`
PMID: 10798829.

Peripheral vestibular disorders impaired blind/eyes-closed straight-path maintenance relative to controls.

### S20 — Brandt et al. 2005
`Vestibular loss causes hippocampal atrophy and impaired spatial memory in humans.`
PMID: 16141283. DOI: 10.1093/brain/awh617.

Chronic bilateral vestibular loss was associated with bilateral hippocampal atrophy and virtual spatial-memory/navigation impairment.

### S21 — 2021 bilateral vestibulopathy real-space navigation
`Bilateral vestibulopathy causes selective deficits in recombining novel routes in real space.`
PMID: 33514827.

BVP patients were impaired at recombining novel routes while familiar-route retracing was normal; deficit severity tracked vestibular loss.

Use:

```text
NovelRouteRecombination can depend selectively on vestibular/self-motion architecture
```

---

# B7 — cue integration / recalibration

### S22 — Zhao & Warren 2015
`How you get there from here: interaction of visual landmarks and path integration in human navigation.`
PMID: 25944773. DOI: 10.1177/0956797615574952.

Landmarks and PI cues were near-optimally integrated to reduce response variability while competing for homing direction under conflict.

Use:

```text
CueIntegration != CueCompetition
```

### S23 — Scherer et al. 2024
`Not seeing the forest for the trees: combination of path integration and landmark cues in human virtual navigation.`
PMID: 38835838.

Complex landmark environments produced large individual differences; more landmarks could harm cue use for some participants.

Use:

```text
MoreLandmarks != BetterNavigationByDefinition
```

### S24 — Naveilhan et al. 2025
`Theta Activity Supports Landmark-Based Correction of Naturalistic Human Path Integration.`
PMID: 41006061. DOI: 10.1523/JNEUROSCI.1005-25.2025.

Brief landmark presentation corrected accumulated homing error; correction depended partly on confidence in the current self-motion estimate.

Use:

```text
LandmarkCorrection != AutomaticOverwrite
```

---

# B8 — active/passive and sensory substitution

### S25 — Chrastil & Warren 2013
`Active and passive spatial learning in human navigation: acquisition of survey knowledge.`
PMID: 23565781. DOI: 10.1037/a0032382.

Visual information supported above-chance survey knowledge; podokinetic walking information improved angular accuracy; vestibular information and decision making did not produce the same effect in that survey paradigm.

### S26 — Chrastil & Warren 2015
PMID: 25419818.

Decision making contributed to graph/route knowledge in walking conditions while idiothetic information did not contribute in the same way.

Together S25/S26 show:

```text
ActiveNavigation != OneIntervention
```

### S27 — Chebat et al. 2023
`Activation of human visual area V6 during egocentric navigation with and without visual experience.`
PMID: 36863342. DOI: 10.1016/j.cub.2023.02.025.

Congenitally blind and sighted participants used sensory substitution for egocentric navigation, with navigation-related cortical recruitment despite absent visual experience.

### S28 — Ruggiero et al. 2018
`Congenital blindness limits allocentric to egocentric switching ability.`
PMID: 29340716. DOI: 10.1007/s00221-018-5176-8.

Congenital blindness altered switching between allocentric/egocentric spatial representations rather than abolishing all spatial coding.

### S29 — Pasqualotto et al. 2016
`Sensory Substitution: The Spatial Updating of Auditory Scenes "Mimics" the Spatial Updating of Visual Scenes.`
PMID: 27148000.

Blindfolded participants learned scenes via sensory substitution and showed allocentric-perspective advantages after egocentric acquisition plus map information.

Use:

```text
SpatialRepresentationContent != VisualFormat
```

---

# B2 — grid-like coding beyond self-navigation

### S30 — Horner et al. 2016
`Grid-like Processing of Imagined Navigation.`
PMID: 26972318. DOI: 10.1016/j.cub.2016.01.042.

Human entorhinal grid-like signals appeared during actual virtual and imagined navigation of the same paths.

### S31 — Bao et al. / visual space 2018
`Hexadirectional coding of visual space in human entorhinal cortex.`
PMID: 29311746. DOI: 10.1038/s41593-017-0050-8.

Entorhinal sixfold signals appeared during controlled visual tracking, suggesting grid-like coding along continuous visual dimensions beyond locomotor navigation.

### S32 — Raithel et al. 2023
`Recruitment of grid-like responses in human entorhinal and piriform cortices by odor landmark-based navigation.`
PMID: 37506703. DOI: 10.1016/j.cub.2023.06.087.

Humans learned an odor-landmark environment; entorhinal and piriform grid-like responses aligned to the same grid orientation.

### S33 — Stangl et al. 2024
`Changes in spatial self-consciousness elicit grid cell-like representation in the entorhinal cortex.`
PMID: 38489383. DOI: 10.1073/pnas.2315758121.

Illusory drifts in perceived self-location induced via visuotactile bodily stimulation elicited entorhinal grid-cell-like representation even without conventional movement through environmental visual cues.

### S34 — 2023 social tracking
`Entorhinal grid-like codes and time-locked network dynamics track others navigating through space.`
PMID: 36720865.

Grid-like codes tracked another individual's movement while participants observed and later retraced paths.

### S35 — 2026 non-spatial conceptual grid code
`Development of non-spatial grid-like neural codes tracks inference and intelligence.`
PMID: 41887217.

N=203, ages 8–25. Entorhinal grid-like codes represented a two-dimensional non-spatial knowledge map, strengthened with age and tracked inferential reasoning/assimilation.

Use:

```text
GridLikeCode != SpatialNavigationSemanticOwner
```

---

# B synthesis

Primary evidence supports:

```text
LayeredPluralSpatialNavigationArchitecture
```

rather than one cognitive map, one hippocampal system, one PI system, one landmark system, one reference-frame pair, one Bayesian integrator or one embodied process.

Two process residuals warrant ownership extraction:

```text
PathIntegrationStateUpdatingProjection
ReferenceFrameTransformationProjection
```

No source in this ledger establishes HF24.


## S36 — Urgolites et al. / human map reading and hippocampus

`Map reading, navigating from maps, and the medial temporal lobe.`
PMID: 27911842.

Hippocampus-limited lesions spared map-reading navigation under repeated map→geographical coordinate transformation, while a larger MTL lesion was impaired under maximal coordinate conflict.

This source is also used to separate hippocampal memory contribution from generic reference-frame transformation.

## S37 — bilateral vestibulopathy novel-route recombination

`Bilateral vestibulopathy causes selective deficits in recombining novel routes in real space.`
PMID: 33514827.

Patients retraced familiar routes normally yet were impaired when recombining novel routes; impairment covaried with vestibular-loss severity.

This is a strong C-round candidate for dissociating stored route memory from flexible self-motion-supported spatial recombination.
