---
schema_version: 1
id: human.high-information.hf20-perceptual-sampling-r1
profile: research
lifecycle: active-search
source_role: research-frontier
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
  - engineer
updated: 2026-08-18
summary: First high-information round after HOC0–HOC10 stage closeout. HF20 Perception / Active Sampling / Perceptual Calibration is attacked as an information-gain leader, not a preselected HOC11. HOC2 can represent abstract evidence acquisition/verification and HOC5 can represent generic action choice, but neither reconstructs the embodied perceptual sampling policy that determines which sensory evidence becomes available through gaze/head/hand/body/tool movement, modality choice, exploration trajectory, stopping and calibration. Recent Human evidence shows eye-movement kinematics constrain perceptual access, active/passive exploration strategy changes sensory-substitution performance, head movement improves sound localization under asymmetric hearing, and perceptual uncertainty changes multisensory evidence accumulation. A first-pass strong unnumbered residual therefore survives: Perceptual Evidence Acquisition / Active Sampling & Calibration. It may still reduce into a protocol plus HOC2/HOC5/HF11/Media/World/Interface ownership; no HOC11 is admitted. The next destructive round should split sampling policy, perceptual uncertainty, multimodal cue weighting/integration, recalibration and assistive/sensory-substitution support and test which pieces have characteristic Human-side actions.
evidence_status: active-synthesis
readiness: RESEARCH_FRONTIER
related:
  - human.foundations.hf20
  - human.foundations.hf11
  - human.operational-concepts.hoc1
  - human.operational-concepts.hoc2
  - human.operational-concepts.hoc3
  - human.operational-concepts.hoc5
  - human.operational-concepts.hoc8
---
# Human High-Information Search — HF20 Perceptual Sampling R1

## 0. Boundary

This round does **not** ask what HOC11 should be.

It asks whether HF20 contains a high-value practical action grammar that current Human operational concepts do not already own.

Current frozen frontier:

```text
HF0–HF23 = preserved
HOC0–HOC10 = frozen
HOC11 = UNKNOWN / not admitted
NextHOC = UNKNOWN
NextOperationalRoute = UNKNOWN
```

---

# 1. HF20 practical inventory

HF20 contains at least these potentially practical objects:

```text
SamplingPolicy
SamplingAction
ActiveSensing
PerceptualEvidence
PerceptualUncertainty
Modality/Channel selection
Multisensory reliability / integration
Multisensory causal inference
Recalibration
Reference-frame selection
Body/peripersonal estimation
Sensory-substitution policy
Perceptual-learning history
Affordance coupling
```

These are not all one family.

---

# 2. Strongest reduction rival: HOC2 verification/evidence acquisition

HOC2 already says verification is discriminative evidence acquisition and can ask:

```text
What evidence would distinguish alternatives?
What independent channel can test the claim?
What test should be executed?
When is evidence sufficient?
When should checking stop?
```

So any candidate defined merely as:

```text
collect more perceptual evidence
```

would duplicate HOC2.

But HOC2 does not reconstruct the embodied acquisition policy itself.

Examples:

```text
look left vs right
move eyes/head vs remain fixed
press vs stroke vs lift object
change viewing angle
move closer
sample another sensory modality
change tool/contact trajectory
reorient head under asymmetric hearing
scan object contour vs local micro-features
```

These operations change the evidence distribution before HOC2 evaluates it.

Therefore:

```text
EpistemicEvidenceAcquisition
!= PerceptualSamplingPolicy totality
```

---

# 3. HOC5 action reduction is also incomplete

HOC5 can represent:

```text
goal: identify object
candidate action: look/move/touch
expected value/cost
choose action
```

But without HF20-specific operational structure it does not know:

```text
which movement changes which sensory evidence;
which sampling action is informative for which perceptual feature;
when active movement creates useful parallax/proprioceptive/auditory change;
when movement introduces confounds;
which modality/reliability relation applies;
when perception must be recalibrated after body/tool/environment change.
```

Thus:

```text
GenericActionSelection
!= PerceptualSamplingPolicy
```

in the same sense that HOC5 generic action machinery did not eliminate HOC9 habit control or HOC10 affective-regulation strategy semantics.

---

# 4. Perceptual sampling is intervention on the evidence channel

HF20's key structural point is:

```text
SamplingAction_t
→ changes ProximalSignal_{t+1}
→ changes SensoryEvidence_{t+1}
→ changes PerceptualState_{t+1}
```

Therefore a Human is not merely a passive receiver whose only practical decision is whether to trust a percept.

The Human can alter the evidence-generation process itself.

This creates a recurring practical question:

> Given a perceptual target, uncertainty and action/sampling costs, what sensing action should the Human perform next, and when should sensing stop or recalibrate?

---

# 5. Vision pressure — eye movements constrain perceptual access

Recent Human high-speed-vision evidence shows perceptual visibility can be predicted by lawful properties of saccadic eye-movement kinematics and sensorimotor contingencies.

This supports:

```text
PerceptualAccess
is partly SamplingAction-conditioned.
```

not merely:

```text
Stimulus + fixed sensor → percept.
```

Operational implication:

```text
SamplingAction can be a bottleneck/intervention variable.
```

---

# 6. Sensory-substitution pressure — exploration strategy changes later perception

A 2025 visual-auditory sensory-substitution study compared different passive guidance/exploration strategies before active exploration.

Participants exposed to a micro-scanning strategy showed the strongest accuracy/confidence and carried the advantage into later active exploration under the studied setup.

Thus:

```text
Same substitution channel
+ different exploration policy
→ different perceptual performance
```

This is a strong deletion witness against treating the assistive channel/device alone as the owner.

---

# 7. Auditory pressure — moving the sensor/body can compensate for missing cues

2025 research on sound localization in single-sided deafness reported that allowing head movement improved localization accuracy in both affected and normal-hearing participants, with larger gains in the single-sided-deafness group alongside additional time/effort.

Thus:

```text
HeadMovement
can be a compensatory sensing strategy
```

with a real:

```text
information gain ↔ effort/time cost
```

tradeoff.

This is not just generic `hearing capability`.

---

# 8. Touch pressure — exploratory procedure is feature-specific

Human active touch uses different movement patterns for different information targets.

Recent work continues to show that tactile discrimination is dynamic and that prior information can alter the speed/pattern of haptic exploration.

This supports:

```text
PerceptualTarget(feature)
→ constrains useful SamplingAction
```

Examples include:

```text
pressing for compliance/deformability
stroking for texture
lifting for weight
contour following for shape
```

A generic `inspect object` action loses this structure.

---

# 9. Perceptual uncertainty is not only epistemic confidence

2025 audiovisual decision research found increasing visual uncertainty altered evidence accumulation rate in multisensory categorization under the studied design.

Therefore:

```text
PerceptualUncertainty
can alter evidence dynamics before metacognitive ConfidenceEstimate.
```

HOC2 remains downstream-relevant but should not collapse:

```text
sensory reliability / uncertainty
metacognitive confidence
claim-level evidence sufficiency
```

into one number.

---

# 10. Active sampling has cost

Active-sampling tasks can explicitly trade:

```text
more samples
→ potentially lower uncertainty
```

against:

```text
sampling time / physical effort / opportunity / monetary/task cost.
```

So the operational target cannot be:

```text
maximize information acquisition
```

without a cost/consequence model.

Candidate question:

```text
ExpectedPerceptualInformationGain
versus
SamplingCost / Delay / Risk / Fatigue
```

---

# 11. First-pass candidate: PerceptualSamplingTargetSpec

```text
PerceptualSamplingTargetSpec = {
  Human,
  perceptual target / task,
  relevant feature/source,
  current sensory channels,
  current support/tool,
  current sampling pose/state,
  current perceptual evidence,
  perceptual uncertainty/reliability,
  candidate sampling actions,
  expected information change,
  action/sampling cost,
  consequence/error asymmetry,
  stopping condition,
  calibration state,
  time horizon,
  uncertainty
}
```

This is provisional.

---

# 12. Candidate: SamplingActionCase

```text
SamplingActionCase = {
  target,
  action type,
  body/sensor/tool involved,
  trajectory / orientation / contact pattern,
  modality,
  timing,
  expected evidence consequence,
  actual evidence consequence,
  task effect,
  cost/effort,
  uncertainty
}
```

Possible action classes:

```text
LOOK / SACCADE / FIXATE
MOVE_HEAD
MOVE_BODY / CHANGE_VIEWPOINT
APPROACH / WITHDRAW
TOUCH / PRESS / STROKE / LIFT / TRACE
LISTEN / REORIENT
REPEAT_SAMPLE
CHANGE_MODALITY
USE_ASSISTIVE_CHANNEL
NO_MORE_SAMPLING
```

No action is universally preferred.

---

# 13. Candidate: SamplingPolicyView

```text
SamplingPolicyView = {
  use question,
  perceptual target,
  current state,
  action-selection rule/evidence,
  sampling history,
  information-gain pattern,
  cost pattern,
  stopping behavior,
  context dependence,
  support/tool dependence,
  uncertainty
}
```

Avoid assuming one stable `active sensing skill`.

---

# 14. Perceptual calibration may be a second residual

HF20 and HF11 distinguish:

```text
perceptual recalibration
motor adaptation
capability
```

A Human can change:

```text
body state
tool length/tool mapping
sensor modality
assistive device
VR scale/reference
terrain/environment
```

while continuing to use a stale perceptual action boundary.

Potential practical object:

```text
PerceptualCalibrationCase = {
  action/perceptual target,
  previous body/tool/environment relation,
  current relation,
  perceived boundary,
  demonstrated boundary,
  calibration evidence,
  recalibration exposure,
  transfer/persistence,
  safety margin,
  uncertainty
}
```

Round 1 does not decide whether this belongs to HF20-space or HF11 action/affordance space.

---

# 15. Multisensory integration may reduce to a protocol rather than family

Potential practical questions:

```text
Which cue/source is reliable now?
Should cues be combined?
Are they likely generated by the same distal cause?
Has one modality recalibrated relative to another?
```

But this may reduce into:

```text
HF20 causal-inference projection
+ HOC2 evidence/reliability
+ task-specific perceptual target
```

No substantive generic action beyond:

```text
sample / reweight / separate / recalibrate
```

has yet been established.

Disposition:

```text
OPEN / likely subfamily or protocol
```

---

# 16. Sensory substitution is a pressure case, not owner

Sensory substitution combines:

```text
Media/Interface transduction
Human perceptual learning
SamplingPolicy
body/tool control
support dependence
```

Therefore:

```text
SensorySubstitutionDevice
!= Human perceptual capability
```

and:

```text
SupportedPerceptualPerformance
!= IndependentNative-SenseCapability
```

HOC1/HOC3 attribution remains mandatory.

---

# 17. Ownership boundaries

## Human/HF20 candidate owns

Potentially:

```text
organism-relative sampling strategy
perceptual evidence acquisition behavior
perceptual calibration/recalibration state
human-side multimodal reliability/integration use
```

## Media / Interface owns

```text
sensor/transducer/device realization
signal encoding
display/haptic/audio mapping
channel latency/bandwidth
```

## World owns

```text
distal source / external state
physical availability of information
world dynamics
```

## HF11 / action space owns

```text
motor execution
tool control
affordance/action boundary realization
```

## HOC2 owns

```text
claim-level evidence sufficiency
verification strategy
confidence/calibration/reliance
```

The central challenge is the coupling boundary, not stealing neighboring objects.

---

# 18. First-pass deletion tests

## D1 — same downstream goal/judgment, different sampling action

```text
same object-identification target
same initial evidence/confidence
same motor capability

A changes viewpoint
B remains fixed
```

If occlusion/parallax differs, available evidence and final decision can diverge.

Sampling policy matters before judgment.

## D2 — same device, different exploration strategy

Sensory-substitution evidence supports this directly.

## D3 — same hearing loss/capability, head movement allowed vs constrained

Localization can differ.

## D4 — same target feature, wrong exploratory procedure

A generic touch action can fail to acquire feature-relevant evidence despite intact capability.

These are nontrivial deletion witnesses.

---

# 19. First-pass reduction table

```text
HF20 practical object              R1 disposition
---------------------------------  ---------------------------------------------
SamplingPolicy / SamplingAction    STRONG SURVIVOR
ActiveSensing                      STRONG SURVIVOR / same family candidate
PerceptualUncertainty              composition coordinate, not standalone family
Multisensory weighting/integration OPEN subproblem
Causal-source inference            likely HF20 projection + HOC2
Recalibration                      STRONG SECONDARY RESIDUAL
Reference frame                    coordinate / pressure case
Sensory substitution               pressure case + cross-owner composition
Body perception/interoception      domain/target-specific pressure cases
Affordance coupling                boundary with HF11; unresolved owner
Perceptual learning                HOC3 + HF20 target-specific learning
```

---

# 20. Current survivor

Round 1 retains, unnumbered:

```text
Perceptual Evidence Acquisition
/ Active Sampling
/ Perceptual Calibration
```

This is not yet one proven family.

The current strongest core is:

```text
ActiveSamplingPolicy
```

because it changes the evidence-generation process itself and appears across vision, audition, touch, sensory substitution and assistive settings.

---

# 21. Why no HOC11 yet

Major unresolved reductions remain:

```text
SamplingPolicy
vs HOC2 VerificationProcedure
vs HOC5 ActionPolicy
vs HF11 motor/tool control
vs Media/Interface sensing realization

PerceptualCalibration
vs HF11 affordance/action calibration

MultisensoryIntegration
vs HOC2 evidence weighting
```

Until these are destructively resolved:

```text
HOC11 = UNKNOWN / not admitted
```

---

# 22. Next destructive round

Round 2 should directly attack:

```text
A. ActiveSamplingPolicy as independent Human operational family
B. PerceptualCalibration as same family vs HF11-owned neighbor
C. MultisensoryIntegration as protocol/coordinate vs substantive action owner
```

Required counterexamples:

```text
sampling changes but decision should not change;
decision changes with no sampling-policy information;
HOC2 generic verification fully reproduces sampling choice;
HOC5 generic action policy fully reproduces exploration choice;
Media/Interface implementation determines all apparent sampling benefit;
active sampling is worse than passive sampling;
extra sensing increases cost/error/overload;
calibration transfer fails across tools/tasks;
Human-Agent sensor control changes evidence without Human perceptual learning.
```

No roadmap beyond this tournament is selected.
