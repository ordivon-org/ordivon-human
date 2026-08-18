---
schema_version: 1
id: human.deep-foundations.hd14c
profile: research
lifecycle: completed
source_role: research-decision
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
  - engineer
updated: 2026-08-18
summary: HD14-C performs ownership extraction on the two process residuals left by HD14-B: PathIntegrationStateUpdatingProjection and ReferenceFrameTransformationProjection. Path integration is shown to be a genuine process distinct from raw vestibular/self-motion perception: posterior-parietal rTMS can disrupt vestibular-derived angular displacement while sparing velocity perception; acute TPJ lesions can impair vestibular-guided travelled-distance/spatial-orientation estimates while self-motion perception remains normal; right temporal lobectomy can selectively impair homing-vector turn integration despite preserved single-turn/single-distance reproduction and control spatial tasks. However path integration is not one invariant navigation mechanism: short/simple PI can survive hippocampal/MTL lesions, right temporal lesions disproportionately affect angular/homing components, translation and rotation recruit partly distinct mechanisms, vestibular/proprioceptive/optic-flow contributions differ by regime, and PI can be implemented through alternate/working-memory-supported strategies. After restoring HF20 sensory/perceptual integration and reference-frame organization, HF11 online body/world state estimation and locomotor/efference information, HF8 current spatial-relational content and HF3 temporary maintenance/readout, no peer spatial owner is required. PathIntegrationStateUpdatingProjection is retained as a cross-HF self-motion-derived spatial-state-estimation projection, HF20/HF11-centered with HF8 output content, not HF24. Reference-frame transformation is also genuine and selectively dissociable: imagery-neglect patients can preserve cognitive-map creation/use but fail egocentric↔allocentric transformation; a DTD patient can preserve route learning, landmark recognition and map construction but fail allocentric-map→egocentric navigation; PPC lesions can preserve allocentric distance/proximity judgments while impairing egocentric route navigation, whereas TGA can show the opposite frame-profile with allocentric route planning impaired and egocentric navigation spared after verbal/figural memory recovery; heading-disorientation cases can preserve object-location information yet fail integration with body-direction change. But transformation semantics are source/target spatial content plus current perceptual/body/action anchors, already owned by HF8/HF20/HF11, with HF3 task control as needed. ReferenceFrameTransformationProjection is retained as a cross-owner representational-interface projection, not HF24. SpatialRelationRepresentation remains HF8-owned; EnvironmentalGraphRepresentation remains HF8/HF7/HF9-centered; LandmarkSpatialRecalibrationProjection remains HF20-centered; grid-like codes remain generic relational-coordinate mechanisms rather than a spatial owner. Peer spatial deletion harm is not established. `SpatialNavigation→HF24 = CLOSED / NOT ADMITTED` on current evidence. `SpatialHF24ReopenCondition` requires future causal/lesion evidence showing a reusable spatial-state transformation process whose semantic/process choices remain necessary after HF20 sensory/perceptual organization, HF11 state estimation/action coordinates, HF8 spatial content/format and HF3 temporary maintenance/control are fully restored, or equivalent peer deletion harm; current value false. HD14-A→C is stage-complete research history; HD14-D is not admitted. HF24 remains globally UNKNOWN/not admitted; NextHumanDeepRoute returns to UNKNOWN for fresh whole-Human re-ranking.
evidence_status: verified-synthesis
readiness: COMPLETE
related:
  - human.deep-foundations.hd14a
  - human.deep-foundations.hd14b
  - human.deep-foundations.hd14c.sources
  - human.deep-foundations.hd14.continuation
---
# HD14-C — Cross-Regime Invariance, Selective Dissociation & Spatial Ownership Extraction

## 0. Entry

HD14-B left two ownership-relevant process residuals:

```text
R1 PathIntegrationStateUpdatingProjection
R2 ReferenceFrameTransformationProjection
```

C does not ask whether these processes are real.

They are.

C asks whether either requires a peer Human semantic owner after restoring:

```text
HF20 perceptual/sensory evidence, integration, calibration, reference-frame organization
HF11 locomotion, efference, sensorimotor control, online body/world state estimation
HF8 spatial relational content, representational format/structure
HF3 working memory, access, control, confidence/readout
```

---

# 1. Ownership rule

```text
SelectiveProcessEvidence
!= PeerFoundationByDefinition
```

A process can be:

```text
causally perturbable
lesion-sensitive
task-selective
computationally coherent
```

and still be a typed projection/interface inside existing Foundations.

C therefore requires:

```text
cross-regime recurrence
+
neighboring-owner resistance
+
peer deletion harm
```

for HF24.

---

# 2. R1 — Path integration is distinct from raw self-motion perception

Posterior-parietal rTMS selectively disrupts a vestibular displacement/path-integration task while not disrupting vestibular velocity perception.

Therefore:

```text
VestibularVelocityPerception
!= VestibularDisplacementIntegration
```

and:

```text
SelfMotionEvidence
!= PathIntegratedSpatialState
```

This is strong positive process evidence.

---

# 3. Acute TPJ lesion gives a stronger perceptual-state dissociation

In acute right-hemisphere stroke patients, TPJ lesions selectively impaired vestibular-guided spatial orientation/travelled-distance estimates for contralesional rotations while all tested lesion patients retained normal self-motion perception.

Thus:

```text
AmIMoving
!= WhereAmI_AfterMotion
```

at the tested vestibular processing level.

This establishes a conversion/integration stage between self-motion evidence and spatial-orientation content.

---

# 4. The output of PI is spatial state, not sensory velocity

A neutral decomposition is:

```text
SelfMotionEvidence_t
  ↓
Temporal / spatial accumulation or update
  ↓
EstimatedDisplacement_t
EstimatedPosition_t
EstimatedHeading_t
```

Therefore PI should not be reduced to one sensory channel.

---

# 5. Right temporal lesion separates integrated homing from component reproduction

Right temporal lobectomy patients can be selectively impaired at estimating the turn required to return to origin after a multi-segment route, while:

```text
single turn reproduction
single distance reproduction
mental rotation
left-right orientation controls
```

remain comparatively preserved.

Route-reproduction turn impairment also need not correlate with homing-vector impairment.

Thus:

```text
ComponentPerceptionOrReproduction
!= IntegratedHomingState
```

and:

```text
PathIntegrationFailure
!= GenericMentalRotationFailure
```

---

# 6. Path integration is not one invariant implementation

The reverse pressure is equally important.

Patients with hippocampal or larger MTL lesions can perform short/simple blindfolded path integration at control levels under some regimes.

Human performance under limited path length/configural demand can therefore recruit alternative or working-memory-supported solutions.

Thus:

```text
PathIntegration_D
!= PathIntegration_E mechanistically by default
```

and:

```text
HippocampalEntorhinalImplementation
!= PathIntegrationIdentity
```

---

# 7. Translation and rotation are separable update coordinates

Human path integration requires at least:

```text
translation / displacement accumulation
rotation / heading update
```

and neuropsychological/fMRI evidence does not support one undifferentiated scalar updater.

Right temporal lesions can disproportionately affect turn/homing components, while simple distance reproduction remains relatively intact.

Therefore:

```text
TranslationUpdate
!= RotationHeadingUpdateByDefinition
```

---

# 8. Egocentric body-relative updating also has selective lesion evidence

Right posterior cortical lesions can impair nonvisual updating of body-centred spatial relations after body rotation, producing systematic underestimation of the rotation performed.

This localizes a real updating function but also shows its dependence on:

```text
locomotor / proprioceptive input
body-centred spatial representation
```

rather than a free-standing navigation semantic object.

---

# 9. PI state updating can be passive or active

Vestibular displacement integration can be studied during passive whole-body rotation.

Walking/path-return tasks add:

```text
proprioception
podokinetic information
efference
motor execution
```

Therefore:

```text
PathIntegration
!= LocomotorControlByDefinition
```

and:

```text
PassivePI
!= ActiveLocomotorPIByDefinition
```

---

# 10. HF20 absorbs the sensory-to-spatial-perceptual transform

HF20 already owns:

```text
SensoryEvidence_D
Integration
PerceptualOrganization
ReferenceFrame_D
Calibration
CurrentCombinedEstimate
```

and explicitly rejects raw sensory evidence as exact body/world state.

A vestibular velocity signal becoming an estimated angular displacement/current spatial orientation is therefore naturally representable as:

```text
HF20 specialized perceptual-state integration projection
```

without a peer Foundation.

---

# 11. HF11 absorbs action-coupled state estimation

HF11 explicitly owns:

```text
Online State Estimation + Correction
EstimatedBodyWorldState_t
forward/internal-model state estimation
sensorimotor feedback
```

When PI uses active movement/efference/proprioceptive information, those source and control semantics are already HF11-owned.

Thus:

```text
ActionGeneratedSpatialUpdate
!= MissingSpatialOwnerByDefinition
```

---

# 12. HF8 absorbs the output spatial content

HF8 explicitly owns:

```text
SpatialContent
relational representation
format / structure
mental-model spatial relations
```

Therefore:

```text
EstimatedCurrentPosition
EstimatedHeading
OriginRelation
```

are typed spatial representational contents under HF8 once constructed/made available.

---

# 13. HF3 absorbs temporary maintenance/control when required

Short/simple PI can survive severe MTL memory impairment, consistent with alternate temporary-maintenance strategies.

Where tasks require holding:

```text
prior segment
turn sequence
origin relation
intermediate update state
```

HF3 working memory/access/control can contribute without becoming PI identity.

Thus:

```text
WorkingMemoryContribution
!= PathIntegrationOwner
```

---

# 14. R1 ownership result

Retain:

```text
PathIntegrationStateUpdatingProjection = {
  reference origin / anchor,
  current estimated position,
  current estimated heading,
  translation update,
  rotation update,
  self-motion evidence channels,
  active/passive regime,
  accumulated uncertainty/bias,
  temporary maintenance strategy,
  query/output
}
```

Ownership:

```text
primary process surface:
  HF20 perceptual integration / spatial orientation
  + HF11 active body/world state estimation where movement-generated

output content:
  HF8

temporary task support:
  HF3 where required
```

Status:

```text
CROSS-HF SELF-MOTION-DERIVED SPATIAL-STATE-ESTIMATION PROJECTION
!= HF24
```

---

# 15. R1 theorem

```text
SelectivePIImpairment
+
PreservedRawSelfMotionPerception
proves an intermediate spatial-state transform
```

but:

```text
IntermediateTransform
!= PeerSemanticOwner
```

when source evidence, state-estimation semantics and output content are already typed by HF20/HF11/HF8.

---

# 16. R2 — Reference-frame transformation is also a real process

A representation in one frame does not automatically guide action in another.

Use:

```text
ReferenceFrameTransformationProjection = {
  source spatial content,
  source frame/anchor,
  target frame/anchor,
  current self/body/view orientation,
  transform/update operation,
  resulting spatial content/action coordinate,
  uncertainty/error
}
```

---

# 17. Imagery-neglect patients provide direct transformation evidence

Right brain-damaged imagery-neglect patients can show no specific deficit in creating or using cognitive maps yet fail transformations:

```text
egocentric → allocentric
allocentric → egocentric
```

Therefore:

```text
MapContentPreserved
+
TransformationImpaired
```

is empirically possible.

This is among the strongest process-selective findings in HD14.

---

# 18. Developmental map-following deficit converges

A DTD patient could:

```text
learn/follow routes
recognize landmarks
build cognitive maps
```

but performance collapsed when allocentrically encoded map information had to guide navigation in a novel environment.

Thus:

```text
AllocentricRepresentationPreserved
+
AllocentricToEgocentricUseImpaired
```

can occur developmentally without acquired lesion.

---

# 19. PPC lesion evidence supplies one direction of frame dissociation

Patients with focal posterior-parietal lesions can preserve allocentric distance/proximity judgments while failing route navigation and some egocentric spatial access/use.

Thus:

```text
AllocentricRelationAccess
can survive
while EgocentricNavigationUse fails.
```

---

# 20. TGA supplies the opposite frame pressure

After transient global amnesia, patients can show prolonged allocentric route-planning deficits while egocentric navigation is not significantly impaired, despite recovery of verbal and figural memory measures.

Therefore:

```text
AllocentricNavigation
can fail
while EgocentricNavigation is relatively spared.
```

Together with PPC evidence, this rejects one undifferentiated spatial-frame system.

---

# 21. Heading disorientation isolates integration with body-direction change

Patients with right retrosplenial involvement can retain spatial locations of surrounding objects when no body-direction update is required, yet perform poorly when they must integrate those locations with changes in body direction.

Thus:

```text
StoredSpatialLocations
!= UpdatedBodyRelativeSpatialRelation
```

This is transformation/updating evidence rather than representation-loss evidence.

---

# 22. Retrosplenial topographical disorientation is an interface phenotype

Classic retrosplenial cases can recognize familiar buildings/landmarks but fail to use that preserved information for directional orientation.

Therefore:

```text
LandmarkRecognitionPreserved
+
DirectionalOrientationImpaired
```

again supports an interface/transformation role.

---

# 23. But transformation is not one frame-specific content store

The same architecture can require:

```text
allocentric → egocentric

egocentric → allocentric

body-relative update after rotation

map-coordinate → geographical/action coordinate
```

Different tasks can recruit different anchors and operations.

Therefore:

```text
ReferenceFrameTransformation
!= OneFixedMatrixByDefinition
```

---

# 24. HF8 owns source and target representational content

HF8 already separates:

```text
RepresentationalContent
Format / Structure
SpatialContent
relational model
```

Thus source-frame and target-frame contents are representational projections, not new ontological entities.

---

# 25. HF20 owns perceptual frame anchors

HF20 explicitly types reference frames including:

```text
retinotopic
head-centred
body-centred
limb-centred
object-centred
allocentric / scene-relative
```

and owns perceptual mapping/calibration across them.

Thus the current perceptual/body-relative anchor is already part of HF20's ontology.

---

# 26. HF11 owns action-coordinate realization

When transformed spatial content must guide locomotion/pointing/action, HF11 owns:

```text
EstimatedBodyWorldState
control mapping
action coordinates
motor execution
```

The action frame is not an unowned spatial semantic layer.

---

# 27. R2 is best represented as a cross-owner interface

Therefore:

```text
ReferenceFrameTransformationProjection
→ HF8 source/target spatial content
+ HF20 perceptual/current-frame anchors
+ HF11 action-coordinate realization when action-guiding
+ HF3 temporary task control/readout as needed
```

Status:

```text
CROSS-OWNER REPRESENTATIONAL-INTERFACE PROJECTION
!= HF24
```

---

# 28. Why selectivity does not rescue HF24

The strongest transformation cases show that a process can fail selectively while source representations survive.

This establishes:

```text
TransformationProcess != RepresentationContent
```

but it does not establish:

```text
TransformationProcess = PeerHumanOwner
```

A typed interface can be selectively lesionable without becoming a new semantic Foundation.

---

# 29. SpatialRelationRepresentation final allocation

After A/B/C:

```text
SpatialRelationRepresentation
→ HF8
```

including typed:

```text
location
direction
distance
adjacency/connectivity
graph relation
survey/configural relation
reference-frame relation
```

Status:

```text
HF8 PROJECTION
!= HF24
```

---

# 30. EnvironmentalGraphRepresentation final allocation

```text
EnvironmentalGraphRepresentation
→ HF8 relational structure
+ HF7 learned environmental history
+ HF9 route/shortcut inference/use
```

Status:

```text
CROSS-HF REPRESENTATIONAL PROJECTION
!= HF24
```

---

# 31. LandmarkSpatialRecalibrationProjection final allocation

HF20 already owns:

```text
integration
cue reliability
common-cause separation
recalibration
reference frames
```

Thus:

```text
LandmarkSpatialRecalibrationProjection
→ HF20-centered
+ HF8 spatial content
+ HF3 confidence/precision/readout where relevant
```

Status:

```text
!= HF24
```

---

# 32. Grid-like code remains non-owner

Grid-like codes recur across spatial and non-spatial relational spaces.

Thus:

```text
GridLikeRelationalCoordinateCodeProjection
= reusable neural/computational coordinate mechanism family
!= SpatialNavigationSemanticOwner
```

No HF24 pressure remains from grid coding alone.

---

# 33. Cross-regime ownership matrix

| Regime | Selective result | Ownership consequence |
|---|---|---|
| posterior-parietal rTMS | PI/displacement impaired, vestibular velocity perception spared | real sensory→spatial transform; not raw HF20 input |
| acute TPJ stroke | spatial orientation/travelled distance impaired, self-motion perception normal | specialized spatial-state integration |
| right temporal lobectomy | homing/route turn integration impaired; single turn/distance and control tasks preserved | integrated state update != component perception |
| hippocampal/MTL lesion | short/simple PI can be preserved | no single invariant hippocampal PI implementation |
| right posterior lesion | body-centred updating after rotation impaired | HF20/HF11 state-update specialization |
| imagery neglect | map creation/use preserved, ego↔allo transformation impaired | real transformation process |
| selective DTD | route/landmark/map formation preserved, map→egocentric navigation impaired | transformation/interface deficit |
| PPC lesions | allocentric judgments preserved, egocentric route navigation impaired | frame-specific access/use dissociation |
| TGA | allocentric route planning impaired, egocentric relatively spared after general memory recovery | opposite frame dissociation |
| heading disorientation | object locations retained, integration with body-direction change impaired | body-direction transformation/update deficit |

The matrix demonstrates real process selectivity but no peer owner surviving HF20/HF11/HF8/HF3 restoration.

---

# 34. Deletion test

Delete hypothetical:

```text
HF24 Spatial Navigation / Spatial State
```

while retaining:

```text
World
→ objective geometry/topology/paths

HF20
→ spatial sensory evidence
→ self-motion perception
→ perceptual reference frames
→ multisensory integration/recalibration
→ specialized spatial-orientation estimate

HF11
→ locomotion/action
→ efference/proprioceptive action evidence
→ online EstimatedBodyWorldState
→ control mapping

HF8
→ current position/heading/spatial relations
→ allocentric/egocentric content
→ graph/survey representations

HF7
→ route/place/landmark memory

HF3
→ working memory/access/control/confidence/readout

HF9
→ route planning/shortcut/graph inference

HF23
→ maps/verbal directions/GPS symbols
```

Then retain typed projections:

```text
PathIntegrationStateUpdatingProjection
ReferenceFrameTransformationProjection
LandmarkSpatialRecalibrationProjection
```

All major HD14 phenomena remain representable without hidden peer spatial semantics.

Therefore:

```text
PeerSpatialFoundationDeletionHarm
= NOT ESTABLISHED
```

---

# 35. C ownership theorem

```text
A process can be selectively lesionable
and still be an interface/projection
rather than a peer semantic owner.
```

Applied here:

```text
SelfMotionEvidence → SpatialState
```

and:

```text
SpatialContent_FrameA → SpatialContent_FrameB
```

are real transformations.

But their source/target semantics are already owned by HF20/HF11/HF8.

---

# 36. Foundation gate after C

For `SpatialNavigation / spatial-state process → HF24`:

```text
F1 stable reusable object
→ PASS for narrow PI and frame-transformation projections

F2 cross-regime recurrence
→ PASS for spatial updating/transformation phenomena

F3 cannot compose from existing owners
→ FAIL at peer-owner level

F4 coherent causal/state architecture
→ PASS for local projections
→ FAIL for one whole spatial-navigation process

F5 neighboring-owner resistance
→ FAIL

F6 evidence grammar
→ STRONG PASS

F7 Agent-era value
→ PASS but admission-secondary

F8 peer deletion harm
→ FAIL
```

Therefore:

```text
SpatialNavigation→HF24
= CLOSED / NOT ADMITTED
```

---

# 37. SpatialHF24ReopenCondition

Reopen only if future evidence shows a reusable process whose semantic/process choices cannot be represented after restoring HF20/HF11/HF8/HF3.

A strong example would be:

```text
one lesion / perturbation / intervention
selectively disrupts the same latent spatial-state transformation
across materially different regimes such as:

  passive vestibular displacement integration
  active locomotor path integration
  allocentric→egocentric map use
  egocentric→allocentric environmental reconstruction

while preserving:

  raw/self-motion sensory perception
  multisensory calibration
  body/world action-state estimation
  source and target spatial representations
  working-memory/control/readout
  motor execution
```

and the residual cannot be described as a typed cross-owner interface.

Equivalent peer deletion counterexamples are admissible.

Current:

```text
SpatialHF24ReopenCondition = false
```

---

# 38. Agent/tool status

```text
GPSRouteSuccess
!= HumanSurveyKnowledge

LiveMapFollowing
!= IndependentHumanReferenceFrameTransformation

AgentDeadReckoning
!= HumanPathIntegration

ToolSupportedArrival
!= IndependentHumanNavigationCapability
```

Tool-mediated spatial success does not reopen HF24.

---

# 39. Positive reconstruction after HD14

HD14 does not conclude that navigation is `nothing but other HFs` in a dismissive sense.

It reconstructs a positive architecture:

```text
LayeredPluralSpatialNavigationArchitecture
= best whole-domain synthesis

SpatialRelationRepresentation
→ HF8

EnvironmentalGraphRepresentation
→ HF8 + HF7 + HF9

PathIntegrationStateUpdatingProjection
→ HF20/HF11-centered state-estimation projection
  with HF8 output content and HF3 task support

ReferenceFrameTransformationProjection
→ cross-owner HF8/HF20/HF11 interface projection

LandmarkSpatialRecalibrationProjection
→ HF20-centered

GridLikeRelationalCoordinateCodeProjection
→ reusable neural/computational mechanism family
```

These are useful scientific objects.

---

# 40. HD14 stage-closeout decision

```text
HD14-A
= term separation / evidence grammar

HD14-B
= rival architecture tournament

HD14-C
= ownership extraction
```

The remaining residuals are retained as typed projections/interfaces and no peer spatial owner survives the deletion test.

Therefore:

```text
HD14
= STAGE COMPLETE
```

and:

```text
HD14-D
= NOT ADMITTED
```

---

# 41. HF24 remains globally unknown

Closing spatial navigation as the candidate does not prove that Human Foundations are exhausted.

Canonical:

```text
HF24
= UNKNOWN / not admitted
```

Only:

```text
SpatialNavigation→HF24
= CLOSED / NOT ADMITTED
```

is established.

---

# 42. No frozen Foundation reopen

HD14-C does not falsify HF0–HF23.

Instead, HF20/HF11/HF8/HF7/HF3/HF9/HF23 distinctions explain the selective cases once typed projections are allowed.

Thus:

```text
FoundationReopenCondition(HF0–HF23)
= false
```

---

# 43. Next Human route

Do not automatically inherit post-HD13 rank #2.

Human-Agent adaptation, psychopathology, sleep/circadian, music/auditory structure and other open continents remain candidates, not roadmap authority.

Canonical:

```text
NextHumanDeepRoute
= UNKNOWN / fresh whole-Human re-ranking required
```

---

# 44. Canonical frontier after HD14-C

```text
HF0–HF23 = preserved
HF24 = UNKNOWN / not admitted
FoundationReopenCondition(HF0–HF23) = false

HD14-A = completed
HD14-B = completed
HD14-C = completed
HD14 = STAGE COMPLETE
HD14-D = NOT ADMITTED

SpatialNavigation→HF24
= CLOSED / NOT ADMITTED

SpatialHF24ReopenCondition
= false

LayeredPluralSpatialNavigationArchitecture
= retained whole-domain synthesis
= composition, not Foundation

SpatialRelationRepresentation
→ HF8

EnvironmentalGraphRepresentation
→ HF8 + HF7 + HF9

PathIntegrationStateUpdatingProjection
= retained cross-HF state-estimation projection
= HF20/HF11-centered + HF8 content + HF3 task support
= not HF24

ReferenceFrameTransformationProjection
= retained cross-owner representational-interface projection
= HF8/HF20/HF11-centered
= not HF24

LandmarkSpatialRecalibrationProjection
→ HF20-centered

GridLikeRelationalCoordinateCodeProjection
= retained mechanism family
= not spatial semantic owner

NextHumanDeepRoute
= UNKNOWN / fresh whole-Human re-ranking required

HOC0–HOC10 = frozen
HOC11 = UNKNOWN / not admitted

WholeHumanOperationalClosure = NOT ESTABLISHED
WholeHumanExhaustion = NOT CLAIMED
```
