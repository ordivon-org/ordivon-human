---
schema_version: 1
id: human.deep-foundations.hd14a
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
summary: HD14-A reconstructs the vocabulary, measurement grammar and hidden assumptions of Human spatial navigation before selecting any cognitive-map, hippocampal-map, grid/place-cell, path-integration, landmark, allocentric, egocentric, cue-integration, reference-frame-transformation or embodied-navigation theory. It separates objective spatial relations from Human spatial representations; place from location; position from orientation and heading; bearing from heading; landmarks from landmark knowledge; paths from routes; locomotion from navigation; homing from wayfinding; spatial memory from navigation performance; place recognition from orientation; route, landmark, location and survey knowledge; egocentric from allocentric and more specific body/head/view-centered reference frames; reference-frame content from transformation process; path integration from landmark navigation, reorientation, spatial updating and recalibration; active acquisition from one undifferentiated active-navigation advantage; virtual/lab navigation from ecological navigation; sense of direction and confidence from actual performance; and DTD from one cognitive-map deficit. Primary evidence shows landmark/route/survey knowledge develops in overlapping parallel rather than mandatory stages; route and survey knowledge can forget at different rates; allocentric map processing can be selectively impaired while route descriptions and landmark recognition remain relatively preserved; landmark recognition itself can be selectively impaired; humans can switch between egocentric and allocentric reference frames; path integration tracks translation and rotation and can be implemented through continuous or configural updating; visual and body-based cues can combine in path integration; landmarks can both recalibrate and compete with path integration; reorientation cue use depends on target environment and cue configuration; active spatial learning decomposes into visual, vestibular, podokinetic and decision components with different contributions; lab/VR route knowledge can differ from ecological acquisition when proprioceptive/vestibular cues are absent; shortcut success does not transparently prove a metric cognitive map because landmark-based strategies can support shortcuts; map drawing, pointing, shortest-path behavior and hippocampal/RSC activity are measurement surfaces, not definitions. `CognitiveMap` is retained only as a theory-laden family label for spatial relational representations whose declared topology/metric/reference-frame/flexibility properties must be specified. The strongest provisional positive objects after A are `SpatialRelationRepresentation`, `ReferenceFrameTransformationProjection`, `PathIntegrationStateUpdatingProjection` and `LandmarkSpatialRecalibrationProjection`; none is HF24. HD14-B is admitted next for rival spatial-navigation architectures and measurement decomposition. HF24 remains UNKNOWN/not admitted.
evidence_status: verified-synthesis
readiness: COMPLETE
related:
  - human.deep-foundations.hd14.continuation
  - human.deep-foundations.hd14a.sources
---
# HD14-A — Current-Use / Term Separation / Hidden-Assumption Inventory

## 0. Entry rule

```text
HD14Admission != HF24Admission
```

A does not decide whether Humans have one `cognitive map system`.

It asks:

> When research says `space`, `place`, `orientation`, `navigation`, `cognitive map`, `path integration`, `allocentric`, `egocentric`, `route knowledge` or `sense of direction`, what exact world target, Human representation, task and information source are actually being measured?

---

# 1. Objective space is not Human spatial representation

World-side targets can include:

```text
Position_W(x)
Orientation_W(x)
Heading_W(x)
Distance_W(a,b)
Direction_W(a,b)
Adjacency_W(a,b)
Connectivity_W(a,b)
Topology_W(E)
Geometry_W(E)
Path_W(a,b)
```

Human-side constructs include estimated/remembered spatial relations, orientation state and action-relevant representations.

Therefore:

```text
ObjectiveSpace != HumanSpatialRepresentation
ObjectiveLocation != HumanLocalizationEstimate
WorldGeometry != CognitiveMapByDefinition
```

World retains objective geometry/topology.

---

# 2. `Space` is an umbrella unless scale and relation are typed

Spatial research ranges across:

```text
peripersonal reaching space
vista space
room/building scale
street/campus/city scale
nested environments
symbolic map space
virtual environment
```

A representation adequate for reaching is not automatically adequate for city navigation.

Thus:

```text
SpatialRepresentation_D
```

must declare environment scale and target relation.

---

# 3. Place is not location by definition

`Location` can mean a position or region in a declared coordinate/reference system.

`Place` usually adds some combination of:

```text
recognizable site identity
stable environmental context
functional/semantic significance
relational embedding
```

but the literature does not provide one universal necessary-and-sufficient definition.

Therefore:

```text
Place != LocationByDefinition
PlaceIdentity != CoordinateOnly
```

HD14 uses `Place_D` only with explicit task criteria.

---

# 4. Position

Use:

```text
Position_R(x,t)
= location of x relative to declared reference system R at time t
```

A Human position estimate may concern:

```text
self
landmark
object
start point
destination
```

and may be biased or uncertain.

```text
PhysicalPosition != EstimatedPosition
```

---

# 5. Orientation

`Orientation` is broader than position.

Use:

```text
Orientation_R(H,t)
= Human/body/view alignment relative to reference system R
```

A person can know location but be uncertain which way they face.

Thus:

```text
Orientation != Position
```

---

# 6. Heading / facing direction

`Heading` or facing direction is a directional component of orientation.

2025 naturalistic VR fMRI identified heading/facing-direction tuning in retrosplenial and superior parietal regions that generalized across perceptually different city versions and locations, relative to environmental axes.

This establishes a real directional representation but not a complete navigation system.

```text
HeadingRepresentation
!= NavigationTotality
```

---

# 7. Bearing is not heading

Use:

```text
Bearing_R(H,target)
= direction from current reference point/orientation toward a target
```

Heading concerns current facing direction; bearing concerns direction to another location/object.

Therefore:

```text
Bearing != Heading
```

One can face north while a target bears east.

---

# 8. Landmark

A `Landmark_D` is an environmental feature used as a spatial reference for task D.

It may support:

```text
recognition
orientation
route decision
place identification
position recalibration
```

The same visible object need not function as a landmark in every task.

Thus:

```text
VisibleObject != LandmarkByDefinition
LandmarkStatus = task/agent-relative functional role
```

---

# 9. Landmark recognition is not navigation

Patients can recognize familiar landmarks yet fail allocentric orientation/map use.

Conversely, developmental landmark agnosia can selectively impair recognition of familiar places/landmarks while other object recognition is spared.

Therefore:

```text
LandmarkRecognition != Navigation
LandmarkRecognition != SurveyKnowledge
```

Landmark recognition is one input/knowledge surface.

---

# 10. Landmark knowledge

Use:

```text
LandmarkKnowledge_D
= retained information about the identity/relevance of environmental reference features
  for declared navigation task D
```

This may include recognition without knowing relations among landmarks.

Therefore:

```text
LandmarkKnowledge
!= LandmarkLocationKnowledge
!= LandmarkOrderingKnowledge
```

---

# 11. Path

World-side:

```text
Path_W
= ordered geometric/topological trajectory through an environment
```

A path can exist independently of a Human knowing it.

Human path representation may encode:

```text
segments
turns
distances
directions
sequence
```

Therefore:

```text
Path_W != RememberedPath
```

---

# 12. Route

Use:

```text
Route_D
= action/traversal-relevant sequence connecting locations under task constraints
```

A route can be represented procedurally/egocentrically without metric survey knowledge.

Thus:

```text
Route != PathByDefinition
```

A geometric path is an environmental relation; a route is usually a navigational/traversal organization of such relations.

---

# 13. Route knowledge

Operational route knowledge can include:

```text
turn decisions at intersections
ordered landmark-action associations
segment sequence
route reproduction
```

It need not entail a global map-like representation.

Therefore:

```text
RouteKnowledge != SurveyKnowledge
```

---

# 14. Survey knowledge

Use provisionally:

```text
SurveyKnowledge_D
= knowledge of inter-location spatial/configurational relations
  sufficient for declared map-like inference task D
```

Possible measurements:

```text
pointing between unseen locations
map drawing
relative direction/distance
novel shortcut
configural reconstruction
```

No single measurement defines survey knowledge.

---

# 15. Landmark → route → survey is not a mandatory stage sequence

A 2021 repeated-learning experiment found landmark, route and survey knowledge all gradually increased from the first trial, with intercorrelations strengthening across experience.

Thus:

```text
LandmarkKnowledge
→ RouteKnowledge
→ SurveyKnowledge
```

is not a universal fixed developmental sequence.

Retain:

```text
Landmark / Route / Survey
= partially separable, interacting knowledge dimensions
```

---

# 16. Route and survey knowledge can have different retention dynamics

Long-delay studies show route and survey knowledge need not forget at identical rates.

Therefore:

```text
SpatialKnowledgeStrength
!= OneScalarMemoryStrength
```

HF7 memory remains typed by spatial content/task.

---

# 17. Landmark ordering is its own measurement surface

Knowledge of landmark order along a route can relate more strongly to survey knowledge than to landmark recognition or route choice in some paradigms.

Thus:

```text
LandmarkOrdering
!= LandmarkRecognition
!= RouteChoice
```

and order knowledge cannot be inferred from recognizing all landmarks.

---

# 18. Navigation

Use:

```text
Navigation_D
= maintenance/update/use of spatial information to regulate movement or action
  toward spatially defined task outcomes in environment D
```

This is a broad functional family.

Navigation can include:

```text
orientation
localization
wayfinding
homing
route following
reorientation
```

but is not identical to any one.

---

# 19. Locomotion is not navigation

Locomotion is bodily/vehicle movement.

A Human can locomote without knowing where they are going, or navigate symbolically without locomoting.

Thus:

```text
Locomotion != Navigation
```

HF11 owns movement/execution.

---

# 20. Wayfinding

Use:

```text
Wayfinding_D
= selecting/updating a route or sequence of movements toward a destination
  in an environment where the required trajectory is not wholly pre-specified
```

Wayfinding can use maps, signs, landmarks, remembered routes or inferred shortcuts.

Therefore:

```text
Wayfinding != RouteFollowingByDefinition
```

---

# 21. Homing

Use:

```text
Homing_D
= returning/directing toward a known start/home reference after displacement/travel
```

A homing vector task is a special navigation task.

```text
Homing != WayfindingTotality
```

---

# 22. Shortcut behavior is not transparent cognitive-map proof

Classic virtual-walking experiments show successful novel shortcuts can depend heavily on dispersed landmarks; displaced landmarks can attract shortcut choices, and coarse survey knowledge can be used when landmarks become unreliable.

Thus:

```text
NovelShortcutSuccess
!= AccurateMetricCognitiveMapByDefinition
```

Shortcut behavior is a probe, not ontology.

---

# 23. Spatial memory is not navigation

HF7 can preserve:

```text
landmark identity
route sequence
place familiarity
survey relations
```

without guaranteeing online orientation or successful movement.

Conversely, online sensorimotor updating can support temporary homing with weak long-term environmental knowledge.

Therefore:

```text
SpatialMemory != Navigation
```

---

# 24. Place recognition is not orientation

`PlaceRecognition_D` concerns identifying/familiarity/classifying a place or scene.

`Orientation_D` concerns current alignment/direction/reference relation.

Cases with landmark/place-recognition impairment and cases with preserved recognition but impaired allocentric orientation show dissociation.

Therefore:

```text
PlaceRecognition != Orientation
```

---

# 25. Topographical orientation

Use `TopographicalOrientation_D` for the ability to determine/use one's spatial relation to a large-scale familiar or unfamiliar environment under declared cue conditions.

It may consume:

```text
landmark recognition
location knowledge
reference-frame relations
heading
route/survey memory
```

but is not one primitive faculty.

---

# 26. Reference frame

A spatial reference frame specifies what coordinates/relations are anchored to.

At minimum distinguish:

```text
egocentric / observer-relative
allocentric / environment-object-relative
body-centered
head-centered
viewer-centered
object-centered
world/environment-centered
```

Terms are often used inconsistently, so exact anchor must be declared.

---

# 27. Egocentric is an umbrella, not one coordinate system

`Egocentric` can mean relative to:

```text
body axis
head
current gaze/viewpoint
current observer position
```

Therefore:

```text
Egocentric
!= BodyCenteredByDefinition
!= HeadCenteredByDefinition
!= ViewerCenteredByDefinition
```

HD14 evidence must name the anchor.

---

# 28. Allocentric

Use:

```text
AllocentricRepresentation_D
= spatial relation represented relative to an external/environmental/object-based frame
```

rather than current body orientation.

Allocentric does not necessarily imply globally metric, north-up or map-like.

Thus:

```text
Allocentric != MetricSurveyMapByDefinition
```

---

# 29. Egocentric and allocentric representations can be separable and transformable

Virtual navigation experiments identify participants using distinct egocentric/allocentric strategies while maintaining high accuracy and being able to switch when instructed.

Therefore:

```text
Egocentric != Allocentric
```

but also:

```text
EgocentricSkill != PermanentlyFixedSystemIdentity
```

The relation can involve strategy choice/transformation.

---

# 30. Reference-frame content is not reference-frame transformation

A Human can represent an allocentric relation without currently converting it to an egocentric action command.

Use:

```text
ReferenceFrameTransformation
= process mapping spatial content from frame R1 to frame R2 for task D
```

Therefore:

```text
ReferenceFrameContent != ReferenceFrameTransformation
```

RSC evidence is compatible with transformation roles but does not define the concept.

---

# 31. Reference frame is not neural area

Retrosplenial, parietal, hippocampal and thalamic regions can contribute differently to heading/reference-frame tasks.

Therefore:

```text
ReferenceFrame != NeuralArea
RSCActivity != AllocentricRepresentationByDefinition
```

Anatomy is implementation evidence.

---

# 32. Heading representation can use global environmental axes

Human RSC/thalamic and 2025 naturalistic-navigation studies show facing-direction signals can be anchored to global/environmental axes under some task structures.

This supports a real heading representation.

But:

```text
NeuralCompass
!= CognitiveMap
!= WayfindingSystem
```

---

# 33. Path integration

A neutral functional definition:

```text
PathIntegration_D
= updating an estimate of current spatial relation to a reference location/orientation
  using information generated during self-motion/traversal
```

Relevant inputs can include:

```text
proprioception
vestibular signals
motor/efference information
optic flow / visual self-motion
```

Therefore:

```text
PathIntegration != VestibularOnly
PathIntegration != IdiotheticOnlyByDefinition
```

---

# 34. Translation and rotation must be separated

Human path integration requires tracking components such as:

```text
translation / traveled displacement
rotation / heading change
```

These can have distinct biases and neural signatures.

Thus:

```text
PathIntegrationError
must type translation and rotation components
```

rather than one scalar error.

---

# 35. Continuous updating vs configural updating are rival implementations

A path-integration task can potentially be solved by:

```text
continuous self-position updating
```

or:

```text
remember route/configuration
→ compute return relation at query time
```

Recent eye-movement analog work explicitly distinguishes these possibilities.

Therefore:

```text
PathIntegrationTask
!= ContinuousOnlineUpdatingProof
```

---

# 36. Path integration does not imply cognitive map

Path integration can support online self-location relative to an origin without producing accurate global survey knowledge.

Classic novel-shortcut work found path integration alone in landmark-poor environments did not yield accurate shortcut behavior.

Thus:

```text
PathIntegration != CognitiveMap
```

---

# 37. Visual and body-based path evidence can combine

Immersive VR experiments manipulating visual gain show visual and interoceptive/self-motion information can jointly influence later homing even when the return occurs in darkness.

Therefore:

```text
PathIntegrationState
can be multimodal.
```

This does not make every navigation cue one system.

---

# 38. Landmark navigation

Use:

```text
LandmarkNavigation_D
= navigation in which identified environmental references materially constrain
  location/orientation/route estimates or actions
```

Landmarks may function as:

```text
beacons
route decision cues
orientation anchors
recalibration anchors
place identifiers
```

These roles should not be collapsed.

---

# 39. Landmark navigation and path integration can both integrate and compete

Human homing studies show visual landmarks and path integration can be near-optimally integrated for response variability while competing to determine response direction under large cue conflict.

Therefore:

```text
CueIntegration
!= CueCompetition
```

and both can occur in one behavioral response.

---

# 40. Spatial updating

Use:

```text
SpatialUpdating_D
= updating represented spatial relations as self, viewpoint, object or environment changes
```

It can concern:

```text
self-to-origin
object-to-self
heading
nested environments
gaze position
```

Therefore:

```text
SpatialUpdating != PathIntegrationByDefinition
```

Path integration is one updating family.

---

# 41. Nested environments show updating is not one global map refresh

Human navigation in nested environments can involve acquiring local representations without fully integrating them into one global representation and switching/reorienting between currently relevant environments.

Thus:

```text
SpatialUpdating
!= SimultaneousGlobalMapUpdateByDefinition
```

Hierarchical/local context matters.

---

# 42. Reorientation

Use:

```text
Reorientation_D
= recovering/establishing orientation after the currently usable orientation relation
  has been disrupted, lost or made uncertain
```

Typical cue families:

```text
geometric layout
landmarks/features
global axes
learned environmental relations
```

Therefore:

```text
Reorientation != ContinuousSpatialUpdating
```

---

# 43. Reorientation is not one geometry module by definition

Adult human conflict studies show geometric and feature/landmark cues can be adaptively combined; global and local geometric features can support reorientation under different conditions.

Therefore:

```text
Reorientation
!= GeometricModuleByDefinition
```

The operative cue depends on environment/task structure.

---

# 44. Target environment matters in reorientation

The same landmark array can support reorientation to local objects but fail for remote-city directions unless its structure/salience is increased.

Thus:

```text
ReorientationCueUtility
= target/environment-relative
```

and:

```text
CuePresent != CueUsed
```

---

# 45. Recalibration

Use:

```text
SpatialRecalibration_D
= correction/update of a spatial estimate or mapping using discrepancy with another cue/reference
```

Landmark-based correction of path-integration error is a canonical example.

Therefore:

```text
Recalibration != ReorientationByDefinition
```

One can recalibrate while never becoming disoriented.

---

# 46. Path-integration error and landmark correction are confidence-sensitive

2025 naturalistic freely moving VR work found homing error accumulated with path integration and was corrected by a briefly presented landmark; correction was smaller when participants were more confident in their self-motion-based estimate.

Therefore:

```text
LandmarkCorrection
!= AutomaticOverwrite
```

Internal confidence/precision can modulate cue incorporation.

HF3 metacognitive/task-state and HF20 cue integration remain separate layers.

---

# 47. Active navigation is not one manipulation

`ActiveNavigation` can add different components:

```text
self-propelled locomotion
podokinetic cues
vestibular cues
efference copy
decision making
attention to route relations
control over viewpoint/sampling
```

Therefore:

```text
ActiveNavigation != OneActiveBenefit
```

---

# 48. Active spatial learning components have different effects

Controlled virtual-maze work found visual input alone supported above-chance survey knowledge; podokinetic information improved angular accuracy, vestibular information alone did not add the same benefit, and decision making did not improve metric survey performance in that paradigm.

Separate graph/route work found decision making contributed under walking conditions while idiothetic information did not contribute in the same way.

Thus:

```text
ActiveBenefit_D
!= ActiveBenefit_E
```

and the word `active` is insufficient evidence metadata.

---

# 49. Vestibular cues can interact with landmark configuration

Motion-simulator work found vestibular cues improved route navigation depending on the landmark condition, especially proximal landmarks.

Therefore:

```text
VestibularContribution
is context/cue-configuration dependent.
```

---

# 50. Real navigation is not desktop VR by definition

Lab/online/VR batteries can differ from ecological navigation, especially in route knowledge when proprioceptive and vestibular information is absent.

Real-life performance can exceed virtual conditions for some survey tasks.

Thus:

```text
VirtualNavigation != RealNavigationByDefinition
DesktopVR != WholeBodyVR != RealEnvironment
```

Environment embodiment must be typed.

---

# 51. Active real-world performance is not just more visual input

Body-based/podokinetic information and controllable movement can alter learning independent of visual scene content.

Therefore:

```text
SameVisualSequence
!= SameSpatialLearningEpisode
```

HF20/HF11 contributions must be preserved.

---

# 52. Cognitive map

`CognitiveMap` is heavily overloaded.

Uses include:

```text
allocentric environment representation
metric survey representation
topological graph
relational map enabling shortcuts
hippocampal spatial code
latent relational representation beyond literal space
```

A does not treat these as identical.

---

# 53. Neutral HD14 use of `CognitiveMap_D`

When unavoidable, use:

```text
CognitiveMap_D
= theory-laden label for a Human spatial relational representation
  whose topology, metric content, reference frame, scale,
  acquisition history and supported inferences are explicitly declared
```

This definition intentionally does not build in:

```text
hippocampus
grid cells
metric accuracy
allocentricity
shortcut success
conscious imagery
```

---

# 54. Cognitive map is not all spatial representation

A remembered left turn after a landmark, current heading estimate or body-centered target direction is spatial representation without necessarily being map-like.

Thus:

```text
CognitiveMap != AllSpatialRepresentation
```

---

# 55. Cognitive map is not survey knowledge by definition

Survey knowledge is an operational knowledge family.

Cognitive map is a theory construct invoked to explain some survey/generalization behavior.

Therefore:

```text
SurveyKnowledge != CognitiveMapByDefinition
```

---

# 56. Cognitive map is not map drawing

Map drawing additionally requires:

```text
symbolic/external representation
perspective transformation
motor production
scale/layout choices
```

Thus:

```text
MapDrawingAccuracy
!= InternalCognitiveMapAccuracyByDefinition
```

HF23 and HF11 can enter the output.

---

# 57. Cognitive map is not hippocampal activity

Hippocampal/RSC activity can differ during formation/use of map-like knowledge, but neural activation does not settle representational ontology.

Therefore:

```text
HippocampalActivity
!= CognitiveMapByDefinition
```

and:

```text
PlaceCell / GridCell Evidence
!= OneHumanNavigationOwnerProof
```

---

# 58. Cognitive map need not be metrically accurate

Humans can use coarse configural/survey relations, labeled graph knowledge or landmark-guided strategies to produce flexible navigation.

Therefore:

```text
FlexibleNavigation
!= AccurateEuclideanMapByDefinition
```

and:

```text
GraphKnowledge
!= MetricSurveyKnowledge
```

---

# 59. Graph knowledge is another positive object

Active/passive navigation studies show participants can acquire labeled graph-like knowledge enabling novel and shortest routes, distinct from simply repeating a learned route.

Thus retain:

```text
EnvironmentalGraphRepresentation_D
```

as one possible spatial representational form, not as cognitive-map totality.

---

# 60. Sense of direction

`SenseOfDirection` is typically a self-report/subjective competence construct.

It may correlate with actual tasks but cannot define them.

2025 DTD assessment found self-report and objective battery classifications identified largely different candidate cases.

Therefore:

```text
SenseOfDirectionSelfReport
!= NavigationPerformance
```

---

# 61. Navigation confidence

Use:

```text
NavigationConfidence_D
= Human confidence in spatial judgment/performance for task D
```

HF3 owns metacognitive confidence.

Thus:

```text
NavigationConfidence != NavigationAccuracy
```

---

# 62. Strategy is not ability

People can preferentially use:

```text
landmark
egocentric route
allocentric survey
```

strategies and can sometimes switch frames without loss of accuracy.

Therefore:

```text
PreferredStrategy
!= MaximumCapability
```

and:

```text
ObservedStrategy
!= FixedArchitecture
```

---

# 63. Population averages can hide individual spatial bias

2026 VR path-integration work identified persistent individual left/right biases that can disappear when side conditions are averaged.

Therefore:

```text
PopulationMeanError
!= IndividualBiasProfile
```

Direction-specific bias belongs in the evidence grammar.

---

# 64. Topographical disorientation

`TopographicalDisorientation_D` is a phenotype label for difficulty orienting/navigating in large-scale environments under declared regime.

It is not one mechanism.

Possible deficits include:

```text
landmark recognition
route learning
allocentric relation processing
heading/reference-frame use
map formation/use
spatial imagery
cue integration
```

Thus:

```text
TopographicalDisorientation != OneCognitiveMapDeficitByDefinition
```

---

# 65. Developmental topographical disorientation is heterogeneous

DTD can appear with broadly preserved cognition, but individual cases differ in navigation strategy, landmark/place recognition, mental-map quality and other spatial processes.

Developmental landmark agnosia provides a distinct selective phenotype.

Therefore:

```text
DTD != OneMechanismByDefinition
```

and diagnostic label cannot identify semantic owner.

---

# 66. Allocentric map processing can dissociate from route knowledge

A pure topographical-disorientation case could recognize landmarks, judge distances and describe routes between city landmarks, yet could not point to unseen landmarks or draw a city map.

Therefore:

```text
AllocentricMapLikeProcessing
!= RouteDescription
!= LandmarkRecognition
```

This is one of HD14's strongest selective dissociations.

---

# 67. Landmark semantic knowledge can dissociate from spatial learning

A topographic-amnesia case showed normal spatial learning but severe recognition/semantic knowledge impairment for familiar buildings/landmarks across visual and verbal naming tests.

Thus:

```text
PlaceSemanticKnowledge
!= SpatialLearningByDefinition
```

HF7/HF8 semantic content and HF20 place perception must remain separable.

---

# 68. Navigation task score is a composition

Observed navigation performance can depend on:

```text
perceptual scene/landmark evidence
self-motion evidence
spatial representation
memory
reference-frame transformation
planning
attention/WM
motor execution
response format
strategy
confidence
external maps/GPS
```

Therefore:

```text
NavigationTaskScore
!= NavigationRepresentationByDefinition
```

---

# 69. Mandatory evidence grammar

Every HD14 claim should type:

```text
SpatialNavigationEvidenceEpisode = {
  objective spatial target,
  Human target construct,
  environment scale,
  familiar / novel environment,
  real / virtual / symbolic environment,
  active / passive acquisition,
  locomotion mode,
  sensory modalities available,
  optic-flow availability,
  vestibular availability,
  proprioceptive/podokinetic availability,
  efference/action information,
  landmark availability,
  landmark role,
  cue reliability/conflict,
  reference frame and exact anchor,
  heading/orientation demand,
  route / landmark / location / survey target,
  path-integration demand,
  reorientation/recalibration demand,
  memory delay,
  map/verbal/GPS/Agent support,
  planning demand,
  attention/WM demand,
  motor/output demand,
  accuracy,
  precision/variability,
  signed bias,
  confidence/self-report,
  strategy evidence,
  shortcut/transfer/generalization evidence,
  uncertainty
}
```

This is evidence grammar, not HF24.

---

# 70. Mandatory neighboring-owner map

```text
World
→ objective geometry / topology / positions / paths

HF20
→ scene/landmark perception
→ optic flow / self-motion sensory evidence
→ multisensory spatial integration
→ perceptual reference frames
→ reorientation/recalibration evidence

HF7
→ route/place/landmark memory
→ retention / forgetting / environmental learning history

HF8
→ spatial relational content
→ location relations
→ egocentric/allocentric representational content
→ cognitive-map / graph content where representational

HF11
→ locomotion
→ sensorimotor updating
→ movement execution / active sampling

HF3
→ attention / WM / confidence / strategy monitoring / readout

HF9
→ shortcut inference / route planning / spatial problem solving

HF23
→ external maps / verbal directions / spatial notation
```

No HF24 extraction before this allocation.

---

# 71. Agent/tool attribution

```text
GPSRouteSuccess
!= HumanSurveyKnowledge

TurnByTurnNavigation
!= IndependentWayfindingCapability

MapAppRecognition
!= InternalCognitiveMap

AgentPlannedRoute
!= HumanRoutePlanning

ToolSupportedArrival
!= IndependentHumanNavigationCompetence
```

External navigation support must be typed in the evidence episode.

---

# 72. Hidden-assumption inventory

```text
H1  Space = Human spatial representation.                       REJECT.
H2  Place = coordinate location.                               REJECT identity.
H3  Orientation = position.                                    REJECT.
H4  Heading = bearing.                                         REJECT.
H5  Visible salient object = landmark.                         REJECT.
H6  Landmark recognition = navigation.                         REJECT.
H7  Route = geometric path.                                    REJECT identity.
H8  Route knowledge = survey knowledge.                        REJECT.
H9  Landmark→route→survey is a mandatory acquisition sequence. FALSIFIED as universal.
H10 Landmark ordering = landmark recognition.                  REJECT.
H11 Locomotion = navigation.                                   REJECT.
H12 Route following = wayfinding.                              REJECT identity.
H13 Homing = navigation totality.                              REJECT.
H14 Spatial memory = navigation ability.                       REJECT.
H15 Place recognition = orientation.                           REJECT.
H16 Egocentric = body-centered only.                           REJECT.
H17 Allocentric = accurate metric survey map.                  REJECT.
H18 Reference-frame content = transformation process.          REJECT.
H19 Preferred reference frame = fixed architecture.            REJECT.
H20 RSC/hippocampus = reference frame/cognitive map itself.    REJECT inference.
H21 Path integration = vestibular/idiothetic only.             REJECT.
H22 Path integration task = continuous online updating proof.  REJECT.
H23 Path integration = cognitive map.                          REJECT.
H24 Landmark navigation = path integration.                    REJECT.
H25 Cue integration = cue competition.                         REJECT identity.
H26 Spatial updating = path integration.                       REJECT identity.
H27 Reorientation = continuous spatial updating.               REJECT.
H28 Reorientation = geometric module.                          REJECT identity.
H29 Recalibration = reorientation.                             REJECT.
H30 Active navigation = one intervention.                      REJECT.
H31 Active > passive universally.                              REJECT.
H32 Virtual navigation = real navigation.                      REJECT identity.
H33 Cognitive map = all spatial representation.                REJECT.
H34 Cognitive map = survey knowledge.                          REJECT identity.
H35 Cognitive map = map drawing ability.                       REJECT.
H36 Cognitive map = hippocampal activity.                      REJECT.
H37 Shortcut success proves metric cognitive map.              REJECT inference.
H38 Flexible navigation requires accurate Euclidean map.       REJECT.
H39 Sense of direction = navigation accuracy.                  REJECT.
H40 Confidence = navigation competence.                        REJECT.
H41 DTD = one cognitive-map deficit.                           REJECT.
H42 Navigation task score = one navigation mechanism.          REJECT.
H43 Population-average error = individual mechanism.           REJECT.
H44 GPS/tool success = independent Human navigation.           REJECT.
```

---

# 73. Positive objects surviving A

A does not retain one `NavigationSystem`.

It retains four provisional research objects/projections:

```text
SpatialRelationRepresentation
ReferenceFrameTransformationProjection
PathIntegrationStateUpdatingProjection
LandmarkSpatialRecalibrationProjection
```

All remain non-Foundation.

---

# 74. SpatialRelationRepresentation

Use provisionally:

```text
SpatialRelationRepresentation = {
  entities/locations,
  relation type,
  scale,
  topology/metric content,
  reference frame,
  precision,
  provenance/acquisition history,
  current accessibility
}
```

This is under strong HF8 ownership pressure.

Status:

```text
PROVISIONAL HF8-LEANING RESEARCH OBJECT
!= HF24
```

---

# 75. ReferenceFrameTransformationProjection

```text
ReferenceFrameTransformationProjection = {
  source frame,
  target frame,
  represented spatial relation,
  transformation/update demand,
  cue inputs,
  accuracy/bias,
  strategy,
  uncertainty
}
```

Likely ownership:

```text
HF8 representational relation
+ HF20 perceptual frame evidence
+ HF11 action frame if movement output
```

Status:

```text
DEEP SCIENTIFIC PROJECTION
!= HF24
```

---

# 76. PathIntegrationStateUpdatingProjection

```text
PathIntegrationStateUpdatingProjection = {
  origin/reference,
  current self-position estimate,
  heading estimate,
  translation update,
  rotation update,
  sensory/self-motion sources,
  accumulated uncertainty/bias,
  update strategy,
  homing/query output
}
```

It remains a major rival process family.

Ownership unresolved among HF20/HF11/HF8.

```text
!= HF24 at A
```

---

# 77. LandmarkSpatialRecalibrationProjection

```text
LandmarkSpatialRecalibrationProjection = {
  prior spatial estimate,
  landmark/reference evidence,
  cue reliability/conflict,
  correction magnitude,
  reference frame,
  resulting estimate,
  uncertainty/confidence
}
```

Strong HF20/HF8/HF3 ownership pressure.

```text
!= HF24
```

---

# 78. What `CognitiveMap` becomes after term separation

After A:

```text
CognitiveMap
= umbrella/theory-family term
```

unless explicitly expanded into:

```text
SpatialRelationRepresentation
with declared:
  topology,
  metric content,
  reference frame,
  scale,
  update process,
  supported inference,
  uncertainty.
```

This is the key semantic cleanup of A.

---

# 79. A-round Foundation gate

```text
F1 stable reusable spatial object
→ PARTIAL
  SpatialRelationRepresentation is stable but HF8-leaning

F2 cross-regime recurrence
→ PASS for navigation phenomena

F3 cannot compose from existing owners
→ UNRESOLVED / doubtful

F4 coherent causal architecture
→ UNRESOLVED

F5 neighboring-owner resistance
→ UNRESOLVED

F6 evidence grammar
→ STRONG PASS

F7 Agent-era value
→ secondary

F8 peer deletion harm
→ UNRESOLVED
```

Therefore:

```text
HF24 = UNKNOWN / not admitted
```

---

# 80. Why HD14-B is justified

A leaves several live rival architectures:

```text
unitary cognitive-map / survey representation
hippocampal-entorhinal map architecture
path-integration / self-motion-primary architecture
landmark-route / graph navigation architecture
allocentric-egocentric dual/reference-frame architecture
reference-frame transformation architecture
Bayesian/reliability-weighted cue integration architecture
embodied/enactive sensorimotor architecture
layered plural / no-peer-owner architecture
```

No rival wins at A.

---

# 81. Admit HD14-B

```text
HD14-B
— Rival Spatial-Navigation Architectures,
  Measurement Decomposition
  & Cross-Task Falsification
```

Every rival must face one common battery rather than selecting favorable tasks.

---

# 82. HD14-B mandatory battery

```text
B1  DTD with broadly preserved general cognition
B2  landmark agnosia vs preserved other object recognition
B3  preserved landmark recognition/route description with impaired allocentric map use
B4  landmark-route-survey parallel acquisition
B5  differential route/survey forgetting
B6  egocentric vs allocentric strategy switching
B7  reference-frame transformation demands
B8  heading representations independent of location/view details
B9  path integration translation vs rotation
B10 continuous vs configural path-updating strategies
B11 multimodal visual + self-motion path integration
B12 landmark/path-integration integration + competition
B13 landmark correction of accumulated homing error
B14 geometry/feature conflict in reorientation
B15 target-environment dependence of reorientation cues
B16 nested-environment updating without one global simultaneous map
B17 active-learning visual/vestibular/podokinetic/decision dissociations
B18 real/ecological vs desktop/VR route/survey differences
B19 shortcut success under landmark dependence
B20 graph knowledge / novel route behavior without full metric map
B21 blindness/nonvisual/sensory-substitution navigation
B22 self-report/confidence vs objective navigation dissociation
B23 individual side bias hidden by population averaging
B24 GPS/tool-supported success without unaided spatial knowledge
```

---

# 83. Canonical frontier after A

```text
HF0–HF23 = preserved
HF24 = UNKNOWN / not admitted
FoundationReopenCondition(HF0–HF23) = false

HD14-A = completed
HD14-B = next admitted round
HD14 = active

CognitiveMap
= theory-laden umbrella unless typed

SpatialRelationRepresentation
= provisional HF8-leaning research object
= not HF24

ReferenceFrameTransformationProjection
= retained deep projection
= not HF24

PathIntegrationStateUpdatingProjection
= retained deep projection
= ownership unresolved
= not HF24

LandmarkSpatialRecalibrationProjection
= retained deep projection
= not HF24

NextHumanDeepRoute after HD14 = UNKNOWN

HOC0–HOC10 = frozen
HOC11 = UNKNOWN / not admitted
```
