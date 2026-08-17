---
schema_version: 1
id: human.operational-concepts.hoc0.layer
title: HOC0 — Human Operational Concept Layer
profile: research
lifecycle: active
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
  - engineer
updated: 2026-08-18
summary: Establishes Human Operational Concepts (HOC) as a layer downstream of frozen HF0–HF23 foundations. HOC reconstructs non-primitive but practically useful concepts for decision support, personalization, learning, capability attribution, collaboration, safety and Human–Agent operation. Operational usefulness does not imply ontological primitiveness. Every HOC must declare its use question, type, scope, inputs, evidence ceiling, uncertainty, update/expiry rule, foundation dependencies, failure modes and forbidden inferences. HOC deliberately permits scoped profiles, scores, bundles and alerts when they are useful, but forbids treating them as the Human itself.
evidence_status: synthesized-from-canonical-foundations
readiness: READY
related:
  - human.deep-foundations.hd10.closeout
  - human.deep-foundations.hd10e
  - human.foundations.hf0
---
# HOC0 — Human Operational Concept Layer

## 0. Decision

Ordivon Human now separates three activities:

```text
HF  — Foundation reconstruction
HD  — deep search into unresolved reality
HOC — operational concept reconstruction
```

HOC exists because many concepts are highly useful even when they are not peer ontological primitives.

Examples:

```text
Capability
Skill
Expertise
Fatigue
Readiness
Trust
Confidence
MotivationProfile
Preference
Workload
Risk
HealthStatus
PersonalityProfile
```

The error is not using these concepts.

The error is silently treating them as:

```text
one intrinsic scalar
one timeless essence
one causal mechanism
one normative truth
or the Human itself.
```

---

# 1. HOC admission criterion

A concept may enter HOC when it passes all of the following:

```text
U1. It answers a recurring practical question.
U2. Using it can change a decision, allocation, interaction or intervention.
U3. Its inputs/evidence can be stated.
U4. Its scope can be bounded by domain/context/time/support/reference.
U5. Its uncertainty and evidence ceiling can be represented.
U6. Its update/expiry rule can be stated.
U7. Its dangerous inferences can be explicitly prohibited.
U8. It can be grounded in existing foundations/relations without pretending to be a new primitive.
```

Therefore:

```text
OperationalUsefulness != FoundationStatus
```

---

# 2. HOC rejection criterion

Reject or split an operational concept when:

```text
R1. it only works by hiding several incompatible ontological types in one number;
R2. it has no stable decision/use target;
R3. its score cannot be interpreted without reconstructing a different concept;
R4. it encourages unsupported essence/personality/moral judgments;
R5. it cannot specify when it becomes stale;
R6. it conflates independent Human properties with environmental, relational or Agent support;
R7. it is only a fashionable label for observations with no added action value.
```

---

# 3. Operational concept types

HOC does not force every concept into the same representation.

Retain at least these types:

```text
OperationalState
OperationalEstimate
OperationalProfile
OperationalSurface
OperationalTrajectory
OperationalRelation
OperationalBundle
OperationalIndex
OperationalAlert
OperationalDecisionVariable
```

Examples:

```text
FatigueState                → OperationalState
ConfidenceEstimate          → OperationalEstimate
MotivationProfile           → OperationalProfile
CapabilitySurface           → OperationalSurface
LearningTrajectory          → OperationalTrajectory
Trust(A→B,target)           → OperationalRelation
TaskReadiness               → OperationalBundle
RiskIndex                   → OperationalIndex
OverloadAlert               → OperationalAlert
Priority                    → OperationalDecisionVariable
```

The type is part of the meaning.

---

# 4. Minimal OperationalConceptSpec

Every HOC should eventually bind:

```text
OperationalConceptSpec = {
  name,
  operational_type,
  use_question,
  target_entity_or_relation,
  domain,
  context,
  time_scope,
  support_boundary,
  reference_or_threshold,
  required_inputs,
  optional_inputs,
  inference_method,
  uncertainty,
  evidence_ceiling,
  update_rule,
  expiry_rule,
  decision_effect,
  failure_modes,
  forbidden_inferences,
  foundation_dependencies,
  provenance
}
```

Not every consumer needs to store every field, but the concept cannot be canonical without answering them.

---

# 5. Operational concepts are purpose-relative

The same evidence can support different concepts for different uses.

Example:

```text
slow task performance
```

might inform:

```text
fatigue state
skill estimate
workload mismatch
poor tool fit
low task familiarity
execution bottleneck
```

but does not identify one of them by itself.

Therefore:

```text
Observation
→ OperationalInference(use question)
```

not:

```text
Observation
→ true hidden person label
```

---

# 6. HOC can use scores — but scores are interfaces, not essences

HOC explicitly permits scores when useful.

Examples:

```text
0–1 confidence
0–100 readiness
risk tier
capability level
fatigue alert band
```

provided:

```text
Score
!= ConstructIdentity
```

and the score declares:

```text
what was aggregated
for what decision
under what reference
with what uncertainty
when it expires
```

This is a major difference from Foundations research: HOC optimizes decision usability, not ontological minimality.

---

# 7. HOC may deliberately compress reality

Operational concepts are allowed to lose information if the compression is useful and bounded.

```text
RichReality
→ PurposeBoundCompression
→ BetterDecision
```

is valid.

But:

```text
PurposeBoundCompression
!= FullWorldModel
```

A readiness score may be excellent for deciding whether to start a difficult task and terrible for explaining why the person is not ready.

A capability tier may be excellent for task assignment and terrible for inferring intelligence.

---

# 8. Every operational concept needs a decomposition path

A compressed HOC should support drilling down when stakes rise.

Example:

```text
TaskReadiness = LOW
```

must be decomposable into candidate contributors such as:

```text
available capacity
fatigue
knowledge gap
motivation/goal conflict
tool/support availability
time pressure
health state
confidence/calibration
external constraint
```

Thus:

```text
OperationalSummary
→ Evidence / component drill-down
```

is preferred over opaque labels.

---

# 9. Evidence ceilings are mandatory

Each HOC should state the strongest claim its evidence supports.

Examples:

```text
self-report fatigue
→ supports experienced fatigue state
→ does not uniquely identify physiological mechanism

AI-assisted task success
→ supports situated/joint capability
→ does not establish independent skill

personality inventory
→ supports scoped descriptive coordinate
→ does not establish causal personality mechanism

repeated accurate judgments
→ may support domain competence
→ does not create institutional authority
```

---

# 10. Update and expiry are first-class

Human operational concepts become dangerous when they persist longer than their evidence.

Different concepts need different temporal behavior:

```text
FatigueState            → minutes/hours
TaskReadiness           → minutes/days
MotivationProfile       → task/goal episode
Trust                   → interaction-history dependent
SkillEstimate           → slower update
ExpertiseProfile        → slow but domain-changing
HealthBaseline          → longitudinal, change-point aware
PersonalityCoordinate   → slow descriptive update, context bounded
```

Therefore:

```text
No timeless profile field by default.
```

---

# 11. Human×Agent attribution rule

Every HOC related to performance or capability must make support explicit.

```text
IndependentHuman
SituatedHuman
JointHumanAgent
```

must not collapse.

A useful operational system can still optimize joint performance while separately tracking what remains available after support removal.

---

# 12. Reflexivity rule

HOC outputs may alter the Human they model.

```text
OperationalEstimate_t
→ system policy
→ future opportunity / support / exposure
→ Human behavior / learning
→ OperationalEstimate_{t+1}
```

Therefore high-impact operational concepts should record when the system itself materially shaped the future evidence.

This is especially important for:

```text
ability labels
risk labels
personality personalization
readiness gating
learning recommendations
trust scores
```

---

# 13. Normative firewall

Operational evidence does not automatically authorize decisions.

```text
low capability estimate
!= lower moral worth

low trust estimate
!= permission to surveil

high expertise
!= authority

predicted low performance
!= legitimate exclusion

preference estimate
!= consent
```

HOC may inform normative/institutional decisions only through an explicit decision rule owned elsewhere.

---

# 14. HOC0 practical objective

The HOC program will reconstruct concepts that help answer questions such as:

```text
What can this Human reliably do now?
What can they do independently versus with support?
What is currently bottlenecking performance?
Are they ready to execute or learn this task?
What knowledge/skill should be trained versus delegated?
How confident should the system be in the Human's judgment?
What does this person currently prefer in this choice context?
How much does A trust B for target X?
Is observed decline likely transient, persistent or support-induced?
What evidence is stale?
```

These are practical questions, not primitive-ontology questions.

---

# 15. HOC relation to engineering

HOC is still research/modeling, not final product schema.

```text
Foundations
→ HOC reconstruction
→ consumer/use-case selection
→ engineering representation
```

Therefore:

```text
HOC != DatabaseSchema
```

The same HOC may have different implementations across learning, work, finance, health or Agent collaboration consumers.

---

# 16. HOC0 stop rule

HOC0 is complete when:

```text
operational-layer purpose is explicit;
admission/rejection criteria are explicit;
concept types are explicit;
minimal specification is explicit;
score/compression use is permitted but bounded;
evidence/update/expiry/reflexivity/normative firewalls are explicit;
and the first candidate inventory is classified.
```

No Foundation is reopened by HOC0.
