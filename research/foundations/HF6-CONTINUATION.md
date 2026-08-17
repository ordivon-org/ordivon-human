---
schema_version: 1
id: human.foundations.hf6.continuation
title: Human Foundations Continuation after HF6
type: handoff
profile: research
lifecycle: active
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
updated: 2026-08-17
summary: Exact continuation after HF6. HF6 reconstructs history-dependent persistent change and exposes retained-but-unexpressed history as the next boundary: memory, retention, forgetting, consolidation, retrieval, interference, generalization and transfer.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
related:
  - human.foundations.hf6
  - human.foundations.hf6.sources
---
# Human Foundations Continuation after HF6

## HF6 completed result

HF6 extends HF5's state transition model:

```text
State_{t+1} = F_{Theta_t}(State_t, Input_t, Action_t)
```

with history-dependent update:

```text
Theta_{t+1}
= U(Theta_t, Experience_t, Outcome_t, InternalState_t, Context_t)
```

The durable distinction is:

```text
StateChange != TransitionFunctionChange
```

HF6 therefore represents persistent Human change with a typed `ChangeProfile_D`:

```text
{
  target domain,
  induction history,
  onset latency,
  magnitude,
  persistence,
  specificity,
  transfer/generalization,
  reversibility,
  decay trajectory,
  reacquisition/savings,
  structural/functional evidence,
  performance consequence,
  cost/tradeoff,
  developmental stage
}
```

## Learning / retention / transfer

HF6 retains:

```text
PracticePerformance
Acquisition
Consolidation / Stabilization
Retention
Retrieval
Transfer / Generalization
Relearning / Savings
```

as non-identical surfaces.

Strong anti-collapses:

```text
Practice != Learning
PracticePerformance != RetainedLearning
Acquisition != Retention
Acquisition != Consolidation
Consolidation != ElapsedTime
Consolidation != GuaranteedEnhancement
Retention != Transfer
NearTransfer != FarTransfer
Transfer_D != Transfer_E
Specificity != NoLearning
Specificity != LowPlasticity
MorePractice != MoreTransfer
TrainingGain != BroadCapability
```

## Plasticity

Retain:

```text
PlasticityCapacity
PlasticChange
```

and keep them separate:

```text
PlasticityCapacity != PlasticChange
NeuralPlasticity != Learning
BehavioralLearning != SpecificNeuralMechanism
Plasticity_D != Plasticity_E
Plasticity != NormativeGood
```

## Habituation / sensitization / tolerance / extinction

HF6 establishes:

```text
ResponseDecrement != ProvenHabituation
Habituation != Fatigue
Habituation != SensoryAdaptation
Habituation_D != Habituation_E
GroupMeanHabituation != IndividualHabituation
Habituation != PermanentResponseLoss

Sensitization != Attention
Sensitization != Vigilance
Sensitization_D != Sensitization_E
Habituation_A can coexist with Sensitization_B

Tolerance != Habituation
Tolerance_D != Tolerance_E

Extinction != Habituation
Extinction != Erasure
SpontaneousRecovery != Renewal != Reinstatement != Reacquisition
```

Repeated psychosocial stress is a high-information falsifier because the same
exposure history can produce cortisol/HPA habituation while another response
channel sensitizes.

## Physiological adaptation / recovery

Retain:

```text
AcuteCompensation != PersistentAdaptation
Adaptation_D != Adaptation_E
Detraining != InstantReturnToBaseline
ReversibleChange != NotAdaptation
FunctionalImprovement != Restitution
FunctionalImprovement != CompensationOnly
RestoredFunction != RestoredIdenticalMechanism
```

Adaptation is not inherently beneficial:

```text
Adaptation != Improvement
Adaptation != WelfareGain
```

## Development / aging

Retain:

```text
Maturation != Learning
SensitivePeriod_D != SensitivePeriod_E
SensitivePeriod_damage != SensitivePeriod_recovery
SensitivePeriod != AdultNoPlasticity
AdultPlasticity != NoDevelopmentalConstraint
Development != MonotonicImprovement
ChronologicalAge != AgingMechanism
Aging != UniformDecline
Aging != NoPlasticity
AgeEffect_D != AgeEffect_E
Maintenance != Reserve
```

Development and aging change both current `Theta` and the update process `U`.

## Resilience

Represent resilience as:

```text
ResilienceProfile(H, Exposure E, Outcome D, interval T)
```

rather than a single trait score.

Retain:

```text
Resilience != NoResponse
Resilience != FastRecoveryOnly
Resilience_D != Resilience_E
Resilience != one fixed trait
Resilience != PostTraumaticGrowth
ResilienceEvidence != JustificationForAdversity
```

## Human × AI / capability

HF6 adds trajectory to HF1 capability:

```text
JointPerformanceGain != HumanInternalLearningGain
JointCapability != IndependentCapability
WithToolPerformance != WithoutToolCapability
SamePerformance != SameTransitionFunction
```

A tool-assisted Human can perform well now while having a very different future
learning/transfer profile from a Human who internalized the capability.

Useful falsifiers include:

```text
with-tool performance
immediate tool-removal performance
delayed tool-removal performance
novel-context transfer
interference/recovery
```

## High-information falsifiers to preserve

- perceptual learning with strong trained gains but weak transfer;
- greater training producing greater specificity in some paradigms;
- motor-memory interference immediately after acquisition but not after a delay;
- sleep-related stabilization without guaranteed enhancement;
- extinction followed by spontaneous recovery, renewal or reinstatement;
- repeated stress producing HPA habituation and inflammatory sensitization;
- dishabituation after repeated startle response decrement;
- endpoint-specific pharmacological tolerance;
- heat/exercise adaptations with different acquisition and detraining rates;
- post-stroke functional gain through varying mixtures of restitution and compensation;
- domain-specific developmental effects after early visual deprivation;
- meaningful adult amblyopia plasticity after an early sensitive period;
- different lifespan learning curves across tasks/metrics;
- retained older-adult learning with narrower/changed transfer;
- resilience trajectories despite strong acute stress responses;
- maintenance versus reserve as different routes to preserved function.

## Exact next foundation

HF6 repeatedly finds that a history-dependent change can remain causally present
without being expressed in current behavior:

```text
extinguished fear can return
habituated responses can recover
skills can survive delays but fail transfer
old skills can be rapidly reacquired
context can select one learned relation over another
adaptations can decay at different rates
```

HF6 can describe persistence/decay/transfer, but cannot yet explain the retained
history and its selective expression.

Therefore the exact next round is:

# HF7 — Memory, Retention, Forgetting, Consolidation, Retrieval, Interference, Generalization and Transfer

## HF7 starting questions

1. What is `Memory`: stored representation, persistent change in a transition
   function, ability to reconstruct prior information, or a typed family?
2. How should encoding/acquisition, storage, consolidation, retention and retrieval
   be separated?
3. What does forgetting mean: storage loss, retrieval failure, interference,
   context mismatch, changed policy, or several mechanisms?
4. Is retrieval a readout or a constructive/inferential process?
5. How should declarative/explicit, procedural/implicit and other memory systems be
   used without assuming one universal taxonomy?
6. What do spontaneous recovery, renewal and reinstatement imply about competing
   memories after extinction?
7. What is proactive/retroactive interference and when does it reflect competition
   rather than destruction?
8. What is savings/relearning when overt performance had apparently returned to
   baseline?
9. How should generalization/transfer be parameterized across stimulus, response,
   context, task, modality and domain?
10. When does retained memory become usable capability?
11. How do external tools/AI alter encoding, storage, retrieval cues and internal
    retention?
12. How does aging affect storage, retrieval, strategy and metacognitive memory
    judgments differently?
13. How should reconstruction, false memory and uncertainty be represented?
14. What next boundary is forced once stored history and its current expression are
    separated?

## Candidate HF7 falsifiers

- Ebbinghaus-style forgetting and savings;
- testing/retrieval-practice effects;
- context-dependent memory;
- state-dependent retrieval;
- proactive and retroactive interference;
- reconsolidation and memory updating;
- extinction with spontaneous recovery/renewal/reinstatement;
- amnesia with preserved procedural learning;
- implicit memory without explicit recall;
- false-memory/reconstructive paradigms;
- cue-dependent autobiographical retrieval;
- prospective memory;
- external-memory/cognitive-offloading paradigms;
- aging differences in recall versus recognition/retrieval support;
- transfer/generalization after retained learning.

## Do not precommit

HF6 does not establish that:

- memory is one storage location or one faculty;
- forgetting means physical deletion;
- successful retrieval proves unchanged stored representation;
- failed retrieval proves absent storage;
- consolidation is one neural mechanism;
- sleep always strengthens all memory;
- extinction stores an exact untouched original memory;
- explicit/declarative and implicit/procedural are exhaustive categories;
- memory is perfectly reconstructive or perfectly reproductive;
- transfer is always desirable or should be broad;
- external memory necessarily causes internal forgetting/deskilling;
- aging memory change is one uniform storage deficit.

## Stop rule

Do not schedule HF8 now. HF7 must expose a repeated neighboring distinction whose
absence causes category failures across materially different memory/history cases.
