---
schema_version: 1
id: human.foundations.hf3
title: HF3 — Attention, Access, Working Memory, Metacognition, Confidence and Cognitive Control
type: report
profile: research
lifecycle: completed
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - reader
  - researcher
  - builder
  - agent
updated: 2026-08-17
summary: HF3 decomposes selective attention, access, working memory, metacognitive evaluation, confidence and cognitive control. It rejects attention as consciousness, working memory as a universal consciousness container, confidence as a consciousness scale, and cognitive control as exclusively conscious; it retains typed selection priority, downstream access, temporary maintenance, metacognitive monitoring and control as partially dissociable functions.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.foundations.hf2
  - human.foundations.hf3.sources
  - human.foundations.hf3.continuation
---
# HF3 — Attention, Access, Working Memory, Metacognition, Confidence and Cognitive Control

## 0. Status and question

HF3 continues from HF2's `AvailableFor_D` boundary.

HF2 established:

```text
Experience != Attention
Experience != Report
Experience != Recall
AvailableFor_D != AvailableFor_E
Phenomenon != Evidence != Inference != Theory
```

HF3 asks:

> **What mechanisms determine which information is selected, temporarily maintained,
> made available to a downstream process, evaluated by the system itself, assigned
> confidence, and used to control behaviour — and which of those mechanisms can
> dissociate from conscious experience?**

HF3 is not a theory of consciousness. It is a boundary reconstruction of six
frequently collapsed constructs:

```text
Attention
Access
WorkingMemory
Metacognition
Confidence
CognitiveControl
```

The round is complete when these constructs can be used without silently making
one the definition or mechanism of the others.

---

# 1. First result: attention is a family of selection functions

The simplest definition, `attention = consciousness directed at X`, fails.
Attention can be described at multiple levels:

```text
selection of sensory input
selection of internal representations
resource allocation
priority weighting
spatial orienting
feature selection
object selection
working-memory prioritization
action selection
```

Modern attention models also reject a clean binary `top-down vs bottom-up`
dichotomy. Current goals, physical salience and selection history can jointly
shape a priority landscape. Reward history can bias selection even when the
stimulus is no longer task-relevant.

Therefore HF3 retains:

```text
Attention_D(process, target, t, context)
```

where the domain `D` declares what is being selected or weighted.

Attention is a **control/selection relation**, not a synonym for experience.

---

# 2. Attention is not consciousness

Inattentional blindness provides the strongest ordinary-language falsifier.
A large unexpected object can occupy the visual field while a demanding task
causes it not to be explicitly noticed. Expert observers can show the same
failure even when their eyes fixate near the missed object.

But the reverse collapse is also wrong:

```text
unattended = unprocessed = unconscious
```

Selection can be partial, graded, object-specific and task-dependent. Unattended
information may still produce priming, physiological responses or limited
behavioural effects.

HF3 therefore retains:

```text
Attention != Experience
Attention != Reportability
Attention != Gaze
Attention != Awareness
```

and also:

```text
NoAttentionEvidence != NoProcessing
```

The precise relationship between attention and conscious experience remains
mechanism- and task-dependent. Some forms of attention appear strongly coupled
to conscious perception; others can operate without conscious awareness.

---

# 3. Salience, priority, attention and control must remain separate

HF2's state/content model needs a better account of why one representation wins
competition.

HF3 distinguishes:

```text
Salience
= stimulus/system property that increases competitive priority under a given
  mechanism.

Priority
= current relative weight for selection/action among alternatives.

Attention
= allocation/selection process implementing or modulating priority.

Control
= goal-/rule-/policy-sensitive regulation of processing and action.
```

These can interact without being identical.

A salient stimulus can fail to win selection because the task strongly biases
another item. A previously rewarded location can capture selection even when it
is currently irrelevant. A task goal can reweight selection before the target
appears.

Durable anti-law:

```text
Salience != Priority != Attention != Control
```

---

# 4. Priority is relational and history-dependent

A useful compressed form is:

```text
Priority(x,t)
= f(current goal, stimulus properties, value/reward history,
    selection history, learned regularities, current state, action demands)
```

This is intentionally not a single universal equation. Different tasks expose
different components.

The important foundation result is that attention cannot be modeled as a purely
sensory filter. It is coupled to what the organism is trying to accomplish, what
it has learned, and what action it is preparing.

This makes Human attention closer to an **action-oriented resource allocation
system** than to a spotlight moving over a picture.

---

# 5. Inattentional blindness: selection can gate report without deleting input

Classic gorilla-style paradigms show that unexpected objects can go unnoticed
when attention is occupied by another task. In expert radiologists, an enormous
unexpected gorilla was missed by most observers despite many looking directly at
its location.

The strongest HF3 inference is not:

```text
unattended object = no representation
```

It is:

```text
current task selection can prevent a stimulus from becoming available to the
specific downstream processes required for explicit detection/report.
```

Thus:

```text
AvailableFor_report
can fail
while
some lower-level processing remains intact.
```

This directly extends HF2's `AvailableFor_D` grammar.

---

# 6. Attentional blink: access is temporally competitive

In rapid serial visual presentation, a second target appearing roughly 200–500
ms after a first target is often harder to report. The attentional blink shows
that downstream access is not only spatially limited; it is temporally limited.

HF3 therefore adds a temporal dimension:

```text
AvailableFor_D(C,t)
```

is not simply a property of content. It depends on what the system is doing
around that time.

The attentional blink can arise from competition among target processing,
selection, consolidation and response-related processes. It therefore cannot be
used as a pure `consciousness off` switch.

Durable law:

```text
TemporalAccessFailure != AbsenceOfAllProcessing
```

and:

```text
ReportFailureAt_t != NoRepresentationAt_t
```

---

# 7. Access is not one hidden variable

HF2 deliberately introduced `AvailableFor_D` rather than a single `Access` bit.
HF3 strengthens that decision.

Candidate downstream domains include:

```text
D1 discrimination
D2 selection/attention guidance
D3 working-memory maintenance
D4 decision
D5 action planning
D6 verbal report
D7 confidence/metacognitive evaluation
D8 long-term encoding
D9 cognitive control
```

A content can be available to one domain and not another.

Therefore:

```text
Access_D != Access_E
```

unless an empirical relation is demonstrated.

The word `access` should always be treated as shorthand for an explicitly named
availability relation.

---

# 8. Phenomenal overflow remains unresolved, not assumed

The classic debate asks whether phenomenal content can exceed cognitive access.
HF3 does not settle the philosophical dispute.

The empirical issue is partly definition-sensitive: if access means working
memory, attention or report, apparent dissociations are easier to formulate. If
access means broad cognitive availability, the distinction becomes harder to
operationalize.

HF3 therefore retains the stronger methodological rule:

```text
Do not infer Experience = WorkingMemory.
Do not infer Experience > every form of Access.
Define the downstream access function being tested.
```

This preserves HF2's typed availability rather than replacing it with another
binary theory.

---

# 9. Working memory is temporary availability, not the universal seat of experience

Working memory is usually described as the temporary maintenance and
manipulation of information for current tasks.

HF3 separates:

```text
Experience
WorkingMemoryStorage
WorkingMemoryManipulation
WorkingMemoryPriority
WorkingMemoryReport
```

These are related but not identical.

Evidence from masking and delayed-response paradigms indicates that information
with little or no reported subjective visibility can sometimes influence delayed
performance and even retain multiple items or temporal order.

Therefore:

```text
WorkingMemory != ConsciousExperience
```

and:

```text
ConsciousExperience != GuaranteedWorkingMemoryStorage
```

The exact neural implementation is also not reduced to persistent firing. Some
working-memory representations can be activity-silent or stored in latent
synaptic/network states.

---

# 10. Working memory itself is heterogeneous

HF3 rejects a single `working memory` container.

At minimum distinguish:

```text
sensory trace / iconic or short-lived memory
active maintenance
latent / activity-silent maintenance
working-memory manipulation
priority within working memory
prospective action policy
```

This matters because an item can be:

```text
represented
but not currently prioritized;

maintained
but not verbally reportable;

usable for a delayed decision
but not consciously vivid;

consciously experienced
but not durably maintained.
```

Thus:

```text
Representation != Maintenance != Priority != Manipulation
```

---

# 11. Attention and working memory form a loop, not a hierarchy

Attention selects what enters or remains privileged in working memory.
Working memory also stores goals/templates that bias subsequent attention.

A useful loop is:

```text
Goal / task set
      ↓
Priority configuration
      ↓
Attention / selection
      ↓
Candidate representation
      ↓
Working-memory maintenance / manipulation
      ↓
Updated goal / policy
      ↓
Priority configuration ...
```

This means `attention -> working memory` is not a one-way ladder.

HF3 retains:

```text
Attention ↔ WorkingMemory
```

with task preparation and action policy as additional mediators.

---

# 12. Metacognition is monitoring/evaluation of one's own processing

HF3 defines metacognition operationally as:

```text
Metacognition_D
= a system-level process that evaluates or represents the quality,
  uncertainty, success, failure or reliability of another cognitive process.
```

Examples:

```text
confidence in a perceptual choice
certainty that a memory is accurate
recognition that one does not know
monitoring whether a plan is working
judging whether to seek more evidence
```

This is broader than confidence alone.

Metacognitive knowledge can be relatively stable:

```text
“I am usually poor at estimating this.”
```

while metacognitive experience is local:

```text
“I am only 60% confident on this trial.”
```

HF3 therefore distinguishes:

```text
MetaKnowledge
MetaExperience
MetaMonitoring
MetaControl
```

---

# 13. Metacognition is not identical to consciousness

The blindsight literature provides a strong pressure test.
Objective discrimination can survive with poor confidence discrimination. Other
experiments show metacognitive sensitivity can dissociate from first-order task
accuracy, and rare cases even report metacognitive discrimination when first-order
performance is near chance.

The durable result is:

```text
FirstOrderPerformance != MetacognitiveSensitivity
```

and:

```text
MetacognitiveSensitivity != ConsciousnessBit
```

Metacognition may provide valuable evidence about a subject's access to its own
processing, but it is itself an inferential capacity with task-specific limits.

---

# 14. Confidence is not accuracy

Confidence answers a different question from accuracy.

```text
Accuracy
= did the decision match the target/criterion?

Confidence
= how strongly does the system endorse its own decision?
```

A subject can be:

```text
correct + low confidence
wrong + high confidence
```

Therefore:

```text
Confidence != Accuracy
```

This is not merely noise. Confidence is influenced by evidence, decision criteria,
priors, self-models and the system's estimate of its own reliability.

---

# 15. Confidence needs at least three dimensions

HF3 separates:

```text
ConfidenceLevel
= reported degree of certainty.

Calibration
= relationship between confidence and empirical correctness probability.

MetacognitiveSensitivity
= ability to discriminate one's own correct from incorrect trials.
```

A person can be systematically overconfident but still rank correct trials above
incorrect ones.

Conversely, average confidence can be reasonable while trial-by-trial
metacognitive sensitivity is poor.

Therefore:

```text
ConfidenceLevel != Calibration != MetacognitiveSensitivity
```

Metacognitive efficiency additionally asks how much metacognitive sensitivity is
obtained relative to first-order task performance.

---

# 16. Confidence is not a direct consciousness meter

A conscious percept can be vivid but uncertain.
A decision can be unconscious or weakly conscious yet accompanied by confidence
that is informative about objective performance.

Blindsight, degraded perception and confidence paradigms therefore do not license:

```text
high confidence = high consciousness
low confidence = low consciousness
```

Confidence is better treated as evidence about the system's estimate of the
reliability of a particular decision or representation.

Thus:

```text
Confidence != ExperienceQuality
Confidence != ConsciousnessLevel
```

---

# 17. Metacognitive access can dissociate from first-order access

A crucial HF3 pattern is:

```text
FirstOrderDecision = successful
MetacognitiveJudgment = poor
```

or the reverse.

This means that a representation can be sufficient to guide a task while the
system has limited ability to evaluate the reliability of that guidance.

This extends HF2:

```text
AvailableFor_action
!= AvailableFor_metacognition
```

Likewise:

```text
AvailableFor_discrimination
!= AvailableFor_confidence-report
```

without evidence establishing the coupling.

---

# 18. Cognitive control is not exclusively conscious

Traditional models often treat cognitive control as a high-level conscious
function. But masked-task and response-inhibition studies show that unconscious
stimuli can sometimes influence task-set preparation or inhibitory control.

The correct inference is not that “unconscious control” is unlimited.

It is:

```text
Some control computations
can be triggered or modulated without conscious report of the triggering
information.
```

Therefore:

```text
CognitiveControl != Consciousness
```

and:

```text
UnconsciousInfluence != UnlimitedUnconsciousAgency
```

The latter boundary is important: demonstrating a local unconscious control
operation does not establish that a whole multi-step goal can be maintained,
revised and normatively evaluated without conscious access.

---

# 19. Task relevance is a causal variable, not a nuisance variable

A recurring HF3 result is that task relevance changes what is selected, maintained
and reported.

The same stimulus can have different downstream consequences depending on:

```text
current goal
instruction
reward structure
expected action
selection history
available capacity
```

No-report paradigms do not automatically remove task effects; they often replace
one task with another proxy-generating task.

Therefore:

```text
TaskRelevance
must be modeled explicitly.
```

This is especially important when interpreting neural signatures.

A difference between report and no-report may reflect:

```text
conscious experience
attention
working-memory demand
metacognitive evaluation
motor/report preparation
task relevance
```

or combinations of them.

---

# 20. Automatic action guidance is a real downstream path

HF2 already allowed `AvailableFor_action-selection`.
HF3 now gives it a stronger role.

Visual stimuli can automatically activate motor representations, prime responses,
trigger attentional orienting and alter ongoing action selection without requiring
an explicit conscious report of the triggering stimulus.

Thus a useful path is:

```text
stimulus
→ representation
→ automatic action bias
→ behaviour
```

which may bypass:

```text
explicit report
metacognitive confidence
verbal reasoning
```

This does not mean the action is “fully unconscious” in every sense. It means the
specific action-selection pathway need not require all the downstream functions
listed above.

Durable law:

```text
ActionGuidance != Report
ActionGuidance != Metacognition
ActionGuidance != ConsciousControl
```

---

# 21. Attention itself is not one thing

HF3 rejects a single attention variable.

Useful axes include:

```text
spatial vs feature vs object
external vs internal
endogenous vs exogenous
sustained vs transient
selection vs suppression
perceptual vs working-memory
current-goal vs history/value driven
```

The old dichotomy:

```text
TopDown
vs
BottomUp
```

is insufficient.

A more durable selection grammar is:

```text
Priority
= f(
    current goals,
    physical/sensory properties,
    reward/value history,
    selection history,
    learned regularities,
    current state,
    action requirements
)
```

This is compatible with Media MF2 but expands beyond media perception into
Human action, motivation and control.

---

# 22. The HF3 dissociation matrix

| Case | Naive collapse attacked | Surviving distinction |
|---|---|---|
| inattentional blindness | attention = all perception | selection can gate explicit detection while lower processing remains |
| expert gorilla | looking at location = noticing | gaze/location != attention target != report |
| attentional blink | report failure = no processing | temporal access/consolidation limits are selective |
| nonconscious WM | WM = conscious content | maintenance can dissociate from ordinary report |
| multiple-item nonconscious delay | WM = conscious workspace | storage/use can exceed subjective visibility |
| blindsight | performance = awareness | first-order performance != subjective/metacognitive access |
| blind insight | metacognition requires successful task | metacognitive sensitivity can dissociate from first-order accuracy |
| high-confidence error | confidence = accuracy | confidence is an inferential endorsement |
| low-confidence correct | weak confidence = absent experience | experience can be present with uncertainty |
| task-set priming | cognitive control = conscious | some control can be unconsciously triggered |
| unconscious inhibition | inhibition = conscious executive act | local control computations can occur without report |
| reward capture | attention = current goal only | selection history/value can bias priority |
| no-report task | no-report = no task effects | proxy and task relevance remain causal variables |
| WM prioritization | WM = passive storage | selection and policy preparation shape maintenance/use |

---

# 23. HF3 anti-laws

1. `Attention != Experience`.
2. `Attention != Gaze`.
3. `Attention != Awareness`.
4. `Attention != Reportability`.
5. `Salience != Priority`.
6. `Priority != Attention`.
7. `Attention != CognitiveControl`.
8. `CurrentGoal != CompletePriorityState`.
9. `TopDown != BottomUp` is not an exhaustive taxonomy.
10. `NoAttentionEvidence != NoProcessing`.
11. `TemporalAccessFailure != NoRepresentation`.
12. `Access` without a declared downstream function is underspecified.
13. `Access_D != Access_E` without evidence.
14. `WorkingMemory != ConsciousExperience`.
15. `ConsciousExperience != GuaranteedWorkingMemoryStorage`.
16. `Representation != Maintenance != Priority != Manipulation`.
17. `WorkingMemory != one homogeneous container`.
18. `FirstOrderPerformance != MetacognitiveSensitivity`.
19. `Metacognition != Consciousness`.
20. `Confidence != Accuracy`.
21. `ConfidenceLevel != Calibration != MetacognitiveSensitivity`.
22. `Confidence != ExperienceQuality`.
23. `Confidence != ConsciousnessLevel`.
24. `CognitiveControl != Consciousness`.
25. `UnconsciousInfluence != UnlimitedUnconsciousAgency`.
26. `ActionGuidance != Report`.
27. `ActionGuidance != Metacognition`.
28. `TaskRelevance != MeasurementNuisance`.
29. `NoReport != NoTaskEffect`.
30. `NeuralActivityInControlNetwork != ConsciousControl`.
31. `Decodability != FunctionalAvailability`.
32. `FunctionalAvailability_D != PhenomenalPresence`.

---

# 24. Minimum HF3 grammar

HF3 retains the following compact model:

```text
Human H at time t
        │
        ├─ StateProfile
        │
        ├─ Experience(H,C,t)
        │
        ├─ Priority(x,t | goals, salience, history, value, action)
        │       ↓
        │    Attention_D
        │       ↓
        │    selected / suppressed representations
        │       ↓
        │    AvailableFor_D(C,H,t)
        │       ├─ discrimination
        │       ├─ working-memory maintenance
        │       ├─ action selection
        │       ├─ report
        │       └─ metacognitive evaluation
        │
        ├─ WorkingMemory
        │       ↔ attention / task preparation
        │
        ├─ Metacognition
        │       ├─ monitoring
        │       ├─ confidence
        │       └─ meta-control
        │
        └─ CognitiveControl
                ├─ task set
                ├─ inhibition
                ├─ policy selection
                └─ conflict regulation
```

The arrows are possible causal relations, not identities.

---

# 25. A better access grammar

HF2 gave:

```text
AvailableFor_D(C,H,t)
```

HF3 adds three qualifiers:

```text
AvailabilityStrength
AvailabilityDuration
AvailabilityReliability
```

So a useful research claim can become:

```text
AvailableFor_action-selection
= strong
= 400 ms
= reliable

AvailableFor_verbal-report
= weak
= < 1 s
= unreliable

AvailableFor_metacognitive-evaluation
= absent
```

This is far more informative than:

```text
access = yes
```

It also allows cross-case comparisons without pretending that all downstream
functions share one capacity.

---

# 26. Confidence as a control input

Confidence should not be treated only as a measurement emitted after cognition.
It can itself change behaviour.

A simplified loop is:

```text
evidence
→ first-order decision
→ confidence / uncertainty estimate
→ decide whether to act, defer, seek more evidence or revise
→ new evidence
```

This turns metacognition into a control process:

```text
Monitoring
→ Control
```

rather than only:

```text
Monitoring
→ Report
```

This matters for Human-AI systems because an agent can ask a human not merely
“What is your answer?” but:

```text
How certain are you?
What would change your mind?
Should we gather more evidence?
```

HF3 does not treat these questions as perfect windows into consciousness. They
measure particular metacognitive judgments under particular protocols.

---

# 27. Cognitive control is hierarchical and resource-constrained

HF3 does not reduce control to PFC activation.

Control can involve:

```text
task-set maintenance
conflict monitoring
response inhibition
policy selection
error monitoring
switching
resource allocation
working-memory prioritization
```

Some can be automatic or habitual; some depend heavily on conscious task
representation; some are learned and become relatively automatic.

Therefore:

```text
Control = family of regulation mechanisms
```

not a single faculty.

The same task can migrate along the automaticity/conscious-control continuum with
practice.

---

# 28. Cross-scale Human implication

HF3 adds an important bridge to Human Foundations beyond neuroscience.

At the individual scale:

```text
attention → selection
working memory → temporary state
metacognition → monitoring
confidence → uncertainty estimate
control → regulation
```

At the social scale, analogous processes can appear in distributed form:

```text
institutional attention
collective information filtering
organizational memory
collective confidence
procedural control
```

HF3 does not claim these are literally the same mechanisms.
It only establishes a reusable question:

> Which properties are intrinsic to the individual mechanism, and which are
> emergent from a larger system?

This prevents an accidental jump from neural terminology to social ontology.

---

# 29. Human × AI implication

HF3 substantially changes the way an Agent should represent a Human interaction.

A system should not collapse:

```text
UserAttention
UserUnderstanding
UserConfidence
UserAgreement
UserIntent
UserExperience
```

into one latent state.

For example:

```text
User answered correctly
!= User understood deeply

User sounded confident
!= User was accurate

User did not respond
!= User did not notice

User noticed
!= User retained it

User retained it
!= User agrees
```

A Human-facing Agent should therefore maintain typed evidence and uncertainty.

This is a direct extension of HF2's `EvidenceBundle` and `AvailableFor_D`.

---

# 30. Relation to Media MF2

Media MF2 established that attention is selective allocation/biasing of finite
perceptual/cognitive processing and acquisition resources, and that:

```text
salience != priority != attention
attention != gaze != awareness
```

HF3 independently reaches a compatible but broader Human result.

Human attention is not merely a perceptual spotlight. It can allocate priority to:

```text
external stimuli
internal representations
working-memory contents
actions
policies
social cues
reward-linked objects
```

The cross-foundation interface is therefore:

```text
Media:
Signal → perceptual selection → possible experience → downstream use

Human:
World/internal state → priority → attention → availability → WM/action/
metacognition/control
```

The common abstraction is **selective allocation under finite capacity and
competing priorities**.

But Human adds agency, goals, history, value, self-monitoring and control.

---

# 31. Competing models

## M1 — Attention-is-consciousness

```text
attended = conscious
unattended = unconscious
```

**Disposition:** reject. Inattentional blindness, unconscious attention effects
and multiple attention mechanisms falsify the identity.

## M2 — Working-memory-is-consciousness

```text
conscious = stored in working memory
```

**Disposition:** reject as ontology. Nonconscious working-memory effects and
conscious content that is not durably maintained provide counterpressure.

## M3 — Access-is-one-bit

```text
access ∈ {0,1}
```

**Disposition:** reject. HF2/HF3 retain typed downstream availability.

## M4 — Confidence-is-consciousness

```text
confidence ≈ degree of consciousness
```

**Disposition:** reject. Confidence, calibration and metacognitive sensitivity
are separable and can dissociate from first-order performance and experience.

## M5 — Metacognition-is-consciousness

```text
metacognitive report = awareness itself
```

**Disposition:** reject. Metacognition is a monitoring/evaluation capacity with
its own failure modes.

## M6 — Cognitive-control-is-consciousness

```text
conscious control = all control
```

**Disposition:** reject. Local control computations can be triggered by
nonconscious information.

## M7 — Attention-is-a-spotlight

```text
one spotlight moves through space
```

**Disposition:** reject as foundation ontology. Attention is multi-domain,
history-sensitive and action-coupled.

## M8 — Attention is only top-down

**Disposition:** reject. Salience, reward history, statistical learning and
selection history also shape priority.

## M9 — Attention is only bottom-up

**Disposition:** reject. Current goals and task preparation strongly alter
selection.

## M10 — One neural network owns control/access

**Disposition:** reject. Network activity is evidence for mechanisms under a
protocol, not an ontology primitive.

---

# 32. HF3 evidence hierarchy

HF3 inherits HF2's evidence discipline but adds mechanism-specific checks.

For an attention/access claim, report:

```text
1. target construct
2. downstream function D
3. task relevance
4. temporal window
5. selection manipulation
6. subjective report / confidence status
7. first-order performance
8. metacognitive measure
9. working-memory demand
10. motor/report demand
11. alternative processing paths
12. known false-negative / false-positive routes
```

For metacognition claims additionally report:

```text
first-order sensitivity
confidence scale
metacognitive sensitivity
calibration
bias
metacognitive efficiency
```

A confidence rating without first-order performance cannot establish metacognitive
accuracy.

---

# 33. HF3 high-information falsifiers

The following cases are retained because they attack different links rather than
merely repeating the same paradigm:

```text
inattentional blindness
attentional blink
change blindness / partial report
blindsight + confidence
blind insight
attribute amnesia
nonconscious working memory
working-memory prioritization
confidence errors
metacognitive sensitivity dissociation
unconscious task-set priming
unconscious inhibition
reward/history-driven attention
no-report task relevance
automatic action guidance
```

The important property is **cross-paradigm convergence**.

---

# 34. What HF3 establishes

HF3 establishes a compact set of durable distinctions:

```text
Attention
= selective allocation / weighting process

Priority
= context-sensitive relative selection weight

Access
= incomplete shorthand; must specify downstream D

WorkingMemory
= temporary maintenance/manipulation system, not universal consciousness

Metacognition
= monitoring/evaluation of cognitive processing

Confidence
= an inferential endorsement/uncertainty estimate, not accuracy or consciousness

CognitiveControl
= family of regulation mechanisms, some of which can operate without conscious
  report
```

And the central relation is:

```text
Priority
→ Attention
→ Availability_D
→ downstream process
```

with recurrent feedback from:

```text
WorkingMemory
Metacognition
Confidence
Control
Goals
History
Value
```

---

# 35. What HF3 does not establish

HF3 does not establish:

- that attention is necessary for every conscious experience;
- that attention is sufficient for consciousness;
- that attention is always unconscious or always conscious;
- that working memory is necessary for all experience;
- that working memory is never unconscious;
- that phenomenal consciousness definitely overflows every form of access;
- that metacognition is necessary for consciousness;
- that confidence directly measures subjective experience;
- that high confidence means high accuracy;
- that low confidence means weak experience;
- that cognitive control is globally conscious or globally unconscious;
- that PFC activity defines access or consciousness;
- that one priority-map implementation is universal;
- that no-report removes all task relevance or metacognitive effects;
- that a single neural signature identifies any construct across all tasks;
- that first-order performance reveals the whole cognitive state;
- that metacognitive performance is a fixed trait independent of task/context;
- that Human social or organizational attention is literally the same mechanism
  as neural attention.

---

# 36. HF3 synthesis

HF2 asked:

```text
What can a conscious content be available for?
```

HF3 answers:

> **Availability is produced by a family of selective, temporary, evaluative and
> regulatory mechanisms rather than one global access gate.**

The compact structure is:

```text
World / internal generation
        ↓
Representations
        ↓
Priority competition
  ↑ goals / value / history / state
        ↓
Attention / selection
        ↓
AvailableFor_D
   ├─ discrimination
   ├─ working memory
   ├─ action
   ├─ report
   └─ metacognition
        ↓
First-order decision
        ↓
Confidence / monitoring
        ↓
Control / revise / seek evidence / act
        ↺
```

This is not a linear consciousness pipeline.
It is a **recurrent control architecture with multiple partially dissociable
availability routes**.

The deepest HF3 compression is:

```text
Attention selects.
Working memory preserves/manipulates.
Metacognition evaluates.
Confidence quantifies/expresses endorsement or uncertainty.
Control regulates.
Access must specify what downstream system is being served.
None of these is identical to Experience.
```

---

# 37. The next boundary

HF3 initially expected the next problem to be “executive function”.
The research does not support that as a sufficiently clean next foundation.

Instead, the repeated residual is now:

```text
Goal
Value
Motivation
Emotion/Affect
Effort
Reward
Self-regulation
Agency
```

These variables repeatedly determine priority and control but cannot be reduced
to attention or metacognition.

The next question is therefore:

> **How do goals, values, motivation, affect, effort and reward generate and
> regulate selective Human action, and how do they interact with agency and
> self-control without collapsing into a single “motivation” variable?**

Exact next foundation:

```text
HF4 — Goals, Motivation, Value, Affect, Effort, Reward and Self-Regulation
```

HF4 is not pre-expanded beyond this boundary. Its falsifiers must determine the
actual surviving distinctions.
