---
schema_version: 1
id: human.operational-concepts.hoc6
title: HOC6 — Trust, Coordination, Common Ground, Roles and Repair
profile: research
lifecycle: completed
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
  - engineer
updated: 2026-08-18
summary: Reconstructs the practical relational coordination layer for Human–Human and Human–Agent joint work. HOC6 separates trust, predictability, reliability, reliance, dependence, deference, authority and relationship state; common ground from identical knowledge; coordination from synchrony, cooperation and communication volume; role from subtask, competence, authority and responsibility; handoff from message delivery; communication repair from trust repair and relationship repair; and joint performance from joint capability. It introduces CollaborationTargetSpec, InterdependenceMap, JointOutcomeSpec, RoleContract, RoleCapabilityFit, CoordinationStateView, CommonGroundEstimate, CriticalCommonGroundSet, CommunicationChannelState, HandoffCase, MisunderstandingCase, RepairCapabilityProfile, TrustRelationProfile, DependenceProfile, TrustViolationCase, TrustRepairCase, RelationshipOperationalView, CoordinationLiabilitySet, CoordinationReadiness, JointCapabilitySurface and NextBestCoordinationAction. It treats clarification, acknowledgment, shared artifacts, role revision, redundancy, trust calibration, escalation and pause/no-intervention as operational actions while preserving authority, consent and Human–AI asymmetry. No Foundation is reopened and no engineering schema is prescribed.
evidence_status: verified-synthesis
readiness: READY
related:
  - human.operational-concepts.hoc1
  - human.operational-concepts.hoc2
  - human.operational-concepts.hoc5
  - human.foundations.hf12
  - human.foundations.hf22
---
# HOC6 — Trust, Coordination, Common Ground, Roles and Repair

## 0. Practical-priority decision

The remaining major candidates were compared again:

```text
trust / coordination / relationship operations
health / functioning / risk trajectory
```

Trust/coordination wins HOC6 because HOC1–HOC5 still lack a complete operational model for action whose outcome depends on multiple independently modeling participants.

The missing questions are:

```text
Do participants actually share the same joint outcome criterion?
Who depends on whom for what?
Are roles, authority and responsibility sufficiently clear?
What critical assumptions are mutually established versus merely privately believed?
Can misunderstandings be detected and repaired?
Is reliance calibrated to target-specific partner behavior?
Can a handoff survive delay, ambiguity and failure?
Is the current composition jointly capable, or merely individually capable?
```

Health/functioning remains a strong later candidate, but coordination is the higher cross-domain Human–Agent leverage point at the current frontier.

---

# 1. Core deletion

Reject the common collaboration collapse:

```text
same task
→ same goal
→ communication
→ shared understanding
→ trust
→ coordination
→ cooperation
→ good teamwork
```

Canonical guards:

```text
Copresence != Interaction
Interaction != Relationship
ParallelAction != JointAction
Synchrony != Coordination
Coordination != JointAction by definition
Coordination != Cooperation
Cooperation != Prosociality
SameGoalString != SharedGoal
SharedGoal != IdenticalInternalRepresentation
CommonGround != IdenticalKnowledge
MessageDelivered != CommunicationSuccess
NoRepair != MutualUnderstanding
Role != Subtask
Role != Capability
Role != Authority
Role != Responsibility
Trust != Predictability
Trust != Reliability
Trust != Reliance
Trust != Dependence
Trust != Deference
Trust != Authority
CommunicationRepair != TrustRepair != RelationshipRepair
JointPerformance != JointCapability
JointCapability != Sum(MemberCapabilities)
HumanUsesAI != HumanAITeam
Delegation != Teaming
```

---

# 2. CollaborationTargetSpec

Operational coordination starts with a declared collaborative target.

```text
CollaborationTargetSpec = {
  participant set,
  joint task/outcome,
  success criterion,
  consequence profile,
  horizon,
  environment,
  authority regime,
  communication constraints,
  support/tool ecology,
  termination/exit conditions
}
```

A group cannot be evaluated as coordinated without specifying what coupling is supposed to achieve.

---

# 3. ParticipantSet

Participants may include:

```text
Human
Human team
AI/Agent
software/tool actor
institutionally assigned role holder
```

HOC6 does not infer equal ontology or experience across participant types.

```text
Human–AI task relation
!= MutualHumanRelationship by default
```

---

# 4. JointOutcomeSpec

```text
JointOutcomeSpec = {
  declared joint criterion,
  acceptable partial outcomes,
  quality/reliability threshold,
  contribution constraints,
  completion condition,
  verification condition,
  consequence allocation
}
```

A shared goal requires enough relational acceptance of interdependent contributions toward the declared criterion; identical wording is insufficient.

```text
SameGoalString != SharedGoal
```

---

# 5. InterdependenceMap

HOC6 introduces:

```text
InterdependenceMap(Participants, JointTask)
```

with edges such as:

```text
A output required by B
A verifies B
A authorizes B
A supplies information to B
A blocks/unblocks B
A monitors B
A recovers B failure
A depends on B availability
```

Interdependence is operationally more informative than mere membership.

---

# 6. Interdependence is directional

```text
Dependence(A→B)
!= Dependence(B→A)
```

A Human may depend heavily on an Agent for retrieval while the Agent's task outcome depends little on Human generation capability but strongly on Human authorization.

Asymmetry is not coordination failure by itself.

---

# 7. DependencyCriticality

Each dependency can be qualified by:

```text
criticality
substitutability
latency tolerance
failure detectability
fallback availability
consequence
```

This distinguishes a convenient dependency from a single point of failure.

---

# 8. RoleContract

`Role` survives as a high-value operational relation.

```text
RoleContract(Participant, JointTask, interval) = {
  expected contributions,
  information access,
  monitoring obligations,
  communication obligations,
  decision scope,
  execution scope,
  authority if any,
  responsibility/accountability if any,
  handoff obligations,
  fallback/escalation obligations,
  start/end conditions
}
```

This is a practical contract/view, not necessarily a legal contract.

---

# 9. Role != subtask

A role can include:

```text
monitoring
signaling
fallback
verification
authority
responsibility
information stewardship
```

beyond the local subtask.

```text
Role != Subtask
```

---

# 10. RoleCapabilityFit

Assignment does not create capability.

```text
RoleCapabilityFit(P, RoleContract, t)
```

compares role demands with HOC1 capability/readiness and HOC2 verification ability.

Canonical:

```text
AssignedRole != RoleCapability
```

---

# 11. RoleAuthorityFit

A participant may be technically capable but lack legitimate decision authority.

```text
RoleAuthorityFit
```

must remain separate from capability.

```text
CanDecide != MayDecide
```

HF13/HF17/institutional owners remain authoritative for legitimacy.

---

# 12. Role ambiguity

A coordination failure can arise when participants disagree about:

```text
who acts
who verifies
who decides
who owns the handoff
who escalates
who can stop
```

This is `RoleAmbiguity`, not automatically low trust or incompetence.

---

# 13. CoordinationStateView

```text
CoordinationStateView(Participants, JointTask, t) = {
  joint outcome state,
  interdependence state,
  role state,
  participant availability/readiness,
  communication state,
  critical common-ground state,
  open handoffs,
  detected misunderstandings,
  repair state,
  trust/reliance/dependence state,
  unresolved conflict,
  authority/escalation state,
  coordination liabilities,
  uncertainty
}
```

It is a relational state view, not a group personality.

---

# 14. Coordination is not synchrony

Participants can be highly synchronous yet pursue different objectives.

They can also coordinate effectively through asynchronous complementary roles.

```text
Synchrony != Coordination
```

Therefore timestamps/behavioral similarity alone cannot establish good teamwork.

---

# 15. Coordination is not cooperation

Competitors can coordinate around shared rules, turns or physical constraints.

Cooperators can fail badly through poor coordination.

```text
Coordination != Cooperation
CooperativeIntention != SuccessfulCooperation
```

---

# 16. CommonGroundEstimate

HOC6 reconstructs common ground as an operational relational estimate:

```text
CommonGroundEstimate(A,B,Topic/Task,t)
```

which may include evidence that:

```text
A believes proposition p
B believes/accepts p
A has evidence B believes/accepts p
B has evidence A believes/accepts p
p was jointly established/acknowledged
p remains current enough for the task
```

Not every use needs full recursive belief modeling.

---

# 17. Common ground != shared database

```text
CommonGroundEstimate
!= IdenticalKnowledgeStores
```

Participants can coordinate with:

```text
partial overlap
role-specific knowledge
asymmetric expertise
partner-specific references
```

provided the critical relational assumptions are sufficiently aligned.

---

# 18. CriticalCommonGroundSet

Not all shared information matters equally.

HOC6 introduces:

```text
CriticalCommonGroundSet(JointTask)
```

for propositions/commitments whose mismatch can materially change coordination outcome.

Examples:

```text
target identity
current plan version
who has authority
whether task is already complete
safety constraint
handoff ownership
meaning of a local label
```

This avoids attempting to synchronize all knowledge.

---

# 19. Shared artifact != shared understanding

A document, task board or chat transcript can create a common reference surface.

But:

```text
SharedArtifact
!= SharedInterpretation
!= CommonGroundEstablished
```

Critical items may still require acknowledgment or testing.

---

# 20. Common-ground evidence modes

Possible evidence:

```text
explicit acknowledgment
successful partner-specific reference
correct dependent action
paraphrase / teach-back
shared artifact plus confirmed version
successful prior repeated convention
```

No single signal guarantees deep mutual understanding.

---

# 21. Human–AI common ground is a real operational problem

Current Human–AI referential-communication experiments show that modern LVLMs can differ substantially from Human partners in how they establish and use common ground across repeated interactive reference tasks.

HOC6 therefore refuses:

```text
LLM conversational fluency
→ Human-like common-ground capability
```

by default.

---

# 22. CommunicationChannelState

```text
CommunicationChannelState = {
  available channels,
  latency,
  bandwidth,
  persistence/logging,
  ambiguity,
  acknowledgement mechanism,
  interruption cost,
  access asymmetry,
  failure state
}
```

Communication affordances change coordination strategy.

---

# 23. Communication volume != coordination quality

More messages can improve alignment or create:

```text
noise
interruptions
attention cost
contradictory updates
stale duplicated instructions
```

Therefore:

```text
CommunicationVolume != CoordinationQuality
```

The relevant question is whether communication changes critical uncertainty/dependency state.

---

# 24. HandoffCase

HOC6 reconstructs handoff as a first-class relational object:

```text
HandoffCase = {
  sender,
  receiver,
  object/responsibility transferred,
  required context,
  version/state,
  completion criterion,
  authority scope,
  deadline/latency,
  acknowledgement,
  unresolved questions,
  fallback/escalation,
  status
}
```

---

# 25. Message delivery != handoff completion

A sender can transmit a message while the receiver:

```text
never sees it
misinterprets it
lacks permission
lacks capability
assumes a different version
never accepts responsibility
```

Thus:

```text
MessageDelivered != HandoffCompleted
```

---

# 26. Handoff statuses

Useful modes:

```text
PREPARED
SENT_NOT_ACKNOWLEDGED
ACKNOWLEDGED
ACCEPTED_WITH_QUESTIONS
ACCEPTED
IN_PROGRESS
COMPLETED
REJECTED
EXPIRED
FAILED / ESCALATED
```

These are operational summaries, not protocol mandates.

---

# 27. MisunderstandingCase

```text
MisunderstandingCase = {
  participants,
  topic/object,
  divergent interpretations/assumptions,
  first evidence of mismatch,
  consequence,
  confidence,
  repair status,
  residual ambiguity
}
```

Misunderstanding is not mere uncertainty.

```text
Misunderstanding != LowConfidence
```

---

# 28. No repair request != mutual understanding

Silence can mean:

```text
understood
failed to notice mismatch
felt unable to ask
assumed partner understood
low stakes
communication channel failure
```

Therefore:

```text
NoRepair != MutualUnderstanding
```

---

# 29. RepairEpisode

```text
RepairEpisode = {
  trigger,
  suspected mismatch,
  initiator,
  clarification request,
  repair proposal,
  evidence/check,
  accepted update,
  changed convention/artifact?,
  cost,
  residual uncertainty
}
```

Repair is more than repetition.

---

# 30. Repair can improve future coordination

Experimental dialogue work shows that feedback signaling understanding/misunderstanding changes how interlocutors coordinate meaning and adapt reference behavior.

Thus:

```text
Repair
can update future communication policy/common-ground state
```

rather than merely patching one message.

---

# 31. RepairCapabilityProfile

A robust team need not make zero mistakes.

```text
RepairCapabilityProfile(Participants, TaskFamily, interval) = {
  mismatch detection,
  repair initiation,
  clarification quality,
  willingness/permission to challenge,
  repair latency,
  repair success,
  recurrence rate,
  transfer to novel misunderstandings,
  cost
}
```

Canonical:

```text
CommunicationRobustness != NoMisunderstanding
```

---

# 32. More repair != better interaction

Frequent successful repair may indicate robustness—or severe upstream ambiguity.

```text
RepairCount
!= CoordinationQuality
```

Interpret repair together with mismatch frequency, severity and recurrence.

---

# 33. TrustRelationProfile

Trust remains target-specific and directional:

```text
TrustRelationProfile(A→B | TargetDimension, Task, Stakes, History, Role, Context)
```

Possible target dimensions:

```text
competence
predictability
integrity / adherence to agreed constraints
information honesty
confidentiality
availability
benevolence/care where relevant
```

Not every relation uses every dimension.

---

# 34. Trust != reliability

Observed reliability can support a trust judgment, but:

```text
ReliabilityEvidence != TrustState
```

Trust also depends on target, history, dependence, interpretation and stakes.

Likewise:

```text
Trust != Predictability
```

A harmful actor can be highly predictable.

---

# 35. Trust != reliance

HOC2 already established reliance as behavioral policy.

HOC6 adds the relational context:

```text
Trust(A→B)
can be high while Reliance(A→B) is low
```

because A has no need to rely on B.

Or:

```text
Trust low + Reliance high
```

because B is a non-substitutable dependency.

---

# 36. DependenceProfile

```text
DependenceProfile(A→B, Target, interval) = {
  required contribution,
  substitutability,
  alternatives,
  switching cost,
  failure consequence,
  monitoring/verification options,
  recovery path
}
```

Dependence is structural, not an attitude.

---

# 37. Dependence changes trust consequences

The same partner failure can matter differently when one participant is more exposed to or dependent on that partner.

Therefore:

```text
SamePartnerBehavior
+ DifferentDependence
→ DifferentOperationalImpact
```

Trust interpretation should preserve dependence context.

---

# 38. TrustCalibrationProfile

A useful operational projection can compare trust/reliance patterns with evidence of target-specific partner performance over time:

```text
TrustCalibrationProfile(A→B, Target, interval)
```

Possible cases:

```text
under-trust / under-reliance
roughly calibrated
selective calibrated reliance
over-trust / over-reliance
forced reliance under low trust
insufficient evidence
```

This remains a use-bound metric, not moral judgment.

---

# 39. Team trust is not uniformly valuable

Team research shows trust-performance relations depend on task and team structure; task interdependence and role/skill differentiation matter.

HOC6 therefore rejects:

```text
MoreTrust = BetterTeam universally
```

The operational goal is sufficient, calibrated trust/reliance for the dependency structure.

---

# 40. TrustViolationCase

```text
TrustViolationCase = {
  target relation,
  expected behavior,
  observed event,
  affected trust dimension,
  consequence,
  ambiguity/attribution,
  dependence context,
  prior history,
  immediate reliance change,
  repair need
}
```

Do not treat every performance error as the same trust violation.

---

# 41. Performance versus purpose/integrity violation

In Human–AI team studies, failures interpreted as cooperative-purpose/integrity violations can affect trust differently from ordinary performance errors.

HOC6 therefore permits typed violation hypotheses without assuming one universal taxonomy.

```text
ViolationType matters
```

when evidence supports it.

---

# 42. TrustRepairCase

```text
TrustRepairCase = {
  violation,
  repair target,
  repair action,
  evidence supplied,
  behavior change,
  apology/explanation/commitment if any,
  monitoring change,
  restored reliance?,
  restored trust?,
  residual dependence/risk,
  follow-up evidence
}
```

---

# 43. Trust repair != communication repair

```text
CommunicationRepair
```

fixes a mismatch in meaning/common ground.

```text
TrustRepair
```

changes expectations about future partner behavior after violation.

```text
RelationshipRepair
```

may concern longer-term commitment, attachment, conflict or relational state.

Thus:

```text
CommunicationRepair != TrustRepair != RelationshipRepair
```

---

# 44. Words alone do not restore reliability

An apology/explanation can alter Human trust/reliance, but:

```text
VerbalTrustRepair
!= ReliabilityRestored
```

High-consequence systems should demand behavior/evidence appropriate to the violated dimension.

---

# 45. Trust can spread through teams

Recent Human–Human–AI experiments show one Human teammate's expressed stance toward an AI can influence another Human's reliance/trust behavior toward that AI.

HOC6 therefore allows:

```text
TrustContagion / SocialTrustInfluence
```

as a relational/team process.

But:

```text
TeamSocialConsensus
!= CalibratedTrust
```

A confident teammate can spread overreliance as well as useful caution.

---

# 46. RelationshipOperationalView

For persistent participant-specific relations, HOC6 can project from HF22:

```text
RelationshipOperationalView(A,B,Domain,interval) = {
  interaction history,
  current availability,
  trust dimensions,
  dependence/interdependence,
  commitment expectations,
  conflict/rupture history,
  repair history,
  role/power asymmetry,
  coordination patterns,
  support/care where relevant,
  uncertainty
}
```

It is a consumer-scoped projection, not a total relationship score.

---

# 47. Relationship quality is endpoint-specific

A relation can be:

```text
excellent for technical coordination
poor for emotional support
highly dependable
low in trust on confidentiality
```

Therefore:

```text
RelationshipQuality_D != RelationshipQuality_E
```

No one global relationship-health score is canonical.

---

# 48. Relationship persistence != relationship goodness

A relation can persist because of:

```text
dependence
institutional role
constraint
history
attachment
shared resources
```

while being harmful or coercive.

```text
PersistentRelationship != HealthyRelationship
```

---

# 49. CoordinationLiabilitySet

HOC6 introduces a practical inventory of unresolved coordination hazards:

```text
CoordinationLiabilitySet = {
  unacknowledged handoffs,
  stale assumptions,
  unresolved misunderstandings,
  ambiguous roles,
  authority mismatch,
  missing fallback,
  single-point dependencies,
  trust/reliance mismatch,
  unresolved conflicts,
  version mismatch,
  unavailable participant,
  critical unknowns
}
```

This is deliberately a set, not one `coordination debt` scalar.

---

# 50. CoordinationReadiness

A central HOC6 object is:

```text
CoordinationReadiness(
  Participants,
  JointTask,
  t,
  ConsequenceSpec
)
```

It asks:

> Is this participant configuration sufficiently aligned, available, role-clear, grounded and repair-capable to begin/continue the joint task at the declared consequence level?

---

# 51. CoordinationReadiness components

Possible requirements:

```text
joint outcome sufficiently established
critical interdependencies known
role/contribution assignments
role capability fit
availability
communication channel
critical common ground
handoff status
monitoring/feedback
repair path
trust/reliance adequacy
fallback/redundancy
required authority
unresolved conflict level
```

Not all are required for every task.

---

# 52. CoordinationReadiness modes

Useful outputs:

```text
COORD_READY
READY_WITH_MONITORING
READY_WITH_CLARIFICATION
READY_AFTER_ROLE_ASSIGNMENT
READY_WITH_REDUNDANCY
BLOCKED_COMMON_GROUND
BLOCKED_HANDOFF
BLOCKED_ROLE_OR_AUTHORITY
BLOCKED_DEPENDENCY
BLOCKED_TRUST_RELIANCE
BLOCKED_COMMUNICATION
BLOCKED_PARTICIPANT_READINESS
INSUFFICIENT_EVIDENCE
```

A scalar may be layered on top, but cannot replace blockers.

---

# 53. CoordinationReadiness != team performance

A team can be ready and still fail due to stochastic events or task difficulty.

A poorly prepared team can occasionally succeed by luck.

```text
CoordinationReadiness != JointOutcome
```

---

# 54. JointCapabilitySurface

HOC1 introduced joint capability at the Human-support boundary.

HOC6 deepens it:

```text
JointCapabilitySurface(
  Participants,
  TaskSpec,
  RoleConfiguration,
  CommunicationPolicy,
  Support,
  interval
)
→ achievable joint outcomes
```

Relevant dimensions:

```text
quality
latency
reliability
coordination overhead
handoff loss
repair capability
complementarity
single-point fragility
role substitution
scaling with participant count
```

---

# 55. Joint capability is composition-sensitive

```text
SameMembers
+ DifferentRoleAllocation
→ DifferentJointCapability
```

and:

```text
SameIndividualCapabilities
+ DifferentCommunication/Repair
→ DifferentJointCapability
```

Therefore:

```text
JointCapability != Sum(MemberCapabilities)
```

---

# 56. Shared mental models are useful coordinates, not identity requirements

Human-team experiments have found task/team mental-model convergence associated with later team process/performance in specific collaborative simulations.

HOC6 keeps the useful lesson:

```text
critical model overlap/alignment can improve coordination
```

without requiring:

```text
all participants hold identical models
```

---

# 57. Complementarity can beat similarity

Different roles may require intentionally different local representations and expertise.

```text
UsefulCoordination
requires enough interface alignment
not maximal internal similarity.
```

Role differentiation is often a feature.

---

# 58. Human–AI teaming criteria

HOC6 uses `HumanAITeaming` only when there is at least:

```text
a declared joint outcome
meaningful contribution interdependence
role/contribution structure
interaction/feedback coupling
```

Mere tool invocation is insufficient.

```text
HumanUsesAI != HumanAITeam
```

---

# 59. Human–AI role asymmetry is allowed

A Human can own:

```text
goal
normative judgment
authority
verification
```

while an Agent owns:

```text
retrieval
generation
monitoring
execution of delegated means
```

or vice versa for some operational dimensions.

```text
Team != EqualRole
```

---

# 60. Human–AI relational asymmetry remains explicit

A Human may form a persistent subjective relationship to an Agent or system.

HOC6 can model Human-side expectations, dependence and interaction history without inferring reciprocal sentience/attachment.

```text
HumanPerceivedConnectionToAI
!= MutualExperiencedRelationship
```

---

# 61. CoordinationFailureInference

HOC1 BottleneckInference specializes here as:

```text
CoordinationFailureInference(Participants, JointTask, Episode)
```

candidate hypotheses:

```text
JOINT_OUTCOME_MISMATCH
INTERDEPENDENCE_UNKNOWN
ROLE_AMBIGUITY
ROLE_CAPABILITY_MISMATCH
AUTHORITY_MISMATCH
COMMON_GROUND_GAP
STALE_STATE/VERSION
HANDOFF_FAILURE
COMMUNICATION_CHANNEL_FAILURE
MISUNDERSTANDING
REPAIR_FAILURE
TRUST_RELIANCE_MISMATCH
DEPENDENCY_FRAGILITY
PARTICIPANT_STATE/READINESS
INCENTIVE/GOAL_CONFLICT
EXTERNAL_CONSTRAINT
INSUFFICIENT_EVIDENCE
```

---

# 62. Do not diagnose trust when coordination is broken

Example:

```text
A and B both trust each other
but each assumes the other owns final submission.
```

The failure is role/handoff ambiguity.

```text
CoordinationFailure != TrustFailure by definition
```

---

# 63. Do not diagnose communication when authority is broken

A team can communicate perfectly but still be blocked because nobody has authority to approve the action.

```text
CommunicationSuccess != ActionAuthority
```

---

# 64. Do not diagnose capability when common ground is broken

Two individually capable participants can fail because they operate on different task versions.

```text
IndividualCapabilityHigh
+ CommonGroundGap
→ JointFailure
```

without any Human skill deficit.

---

# 65. NextBestCoordinationAction

```text
NextBestCoordinationAction(
  Participants,
  JointTask,
  CoordinationState,
  ConsequenceSpec,
  Constraints
)
```

candidate actions include:

```text
CLARIFY_JOINT_OUTCOME
EXTERNALIZE_CRITICAL_STATE
REQUEST_ACKNOWLEDGEMENT
CHECK_COMMON_GROUND
TEACH_BACK / PARAPHRASE
ASSIGN_ROLE
REASSIGN_ROLE
CLARIFY_AUTHORITY
CLARIFY_RESPONSIBILITY
RESOLVE_HANDOFF
REPAIR_MISUNDERSTANDING
REPAIR_TRUST_WITH_EVIDENCE
CALIBRATE_RELIANCE
ADD_MONITORING
ADD_REDUNDANCY
ADD_FALLBACK
REDUCE_INTERDEPENDENCE
CHANGE_COMMUNICATION_CHANNEL
ESCALATE_AUTHORITY
PAUSE_JOINT_TASK
CHANGE_PARTNER/AGENT
COLLECT_MORE_EVIDENCE
NO_INTERVENTION
```

---

# 66. Externalizing state is often cheaper than synchronizing minds

Rather than making every participant remember everything, coordination can use:

```text
shared task state
versioned artifact
explicit owner
status marker
checklist
handoff record
```

HOC6 retains this as an operational strategy.

But:

```text
ExternalizedState != CommonUnderstanding
```

so critical interpretation may still require grounding.

---

# 67. Acknowledgment is useful but not proof

```text
"got it"
```

can mean message received, not necessarily correctly understood.

For high-consequence ambiguous handoffs, stronger evidence may require:

```text
paraphrase
correct dependent action
independent verification
```

---

# 68. Redundancy can improve robustness and increase load

Adding a second verifier or duplicate channel can reduce single-point fragility while increasing:

```text
coordination overhead
review time
conflict resolution burden
```

Therefore:

```text
MoreRedundancy != BetterTeam universally
```

HOC4 load costs remain relevant.

---

# 69. Reducing interdependence is a valid coordination intervention

Sometimes the best solution is not better communication but architecture:

```text
make components more independent
clarify interfaces
remove unnecessary shared state
```

Thus:

```text
BetterCoordination
can come from
less required coordination.
```

---

# 70. Conflict is not always coordination failure

Disagreement can expose:

```text
hidden assumptions
competing evidence
role conflict
value conflict
```

HOC2/HOC6 may treat structured disagreement as useful information.

```text
NoDisagreement != GoodTeam
```

---

# 71. Psychological/social smoothness != epistemic quality

A highly agreeable or sycophantic Agent can feel easy to collaborate with while reducing challenge, responsibility-taking or error detection.

Therefore:

```text
InteractionPleasantness
!= CoordinationQuality
!= EpistemicQuality
```

---

# 72. Trust repair can overcorrect

If repair messaging increases reliance without correcting the underlying failure mode, the relation can become more dangerous.

```text
RestoredReliance
!= RestoredSafety
```

Trust repair should be paired with relevant behavioral evidence in high-stakes contexts.

---

# 73. Relationship repair may rationally end in separation

A successful repair process need not restore the prior relation.

Possible outcomes:

```text
continue unchanged
continue with monitoring
continue with reduced dependence
change roles
set boundary
suspend
end relation
```

```text
RelationshipRepairSuccess
!= RelationshipContinuation by definition
```

---

# 74. Coordination history matters

Repeated interaction can create:

```text
shorter references
local conventions
role expectations
trust/distrust
known failure patterns
faster repair
```

but:

```text
MoreHistory != BetterCoordination
```

bad conventions and entrenched miscalibration can also persist.

---

# 75. New participant invalidates some local common ground

When team composition changes, partner-specific conventions and assumptions may no longer transport.

Therefore:

```text
TeamCompositionChange
→ selective CommonGround / Role / Trust revalidation
```

not full reset and not blind carryover.

---

# 76. Version changes matter

Human–Agent systems can change behavior after:

```text
model update
prompt/policy update
tool update
permission change
```

Historical trust/reliance evidence may become partially stale.

```text
SameAgentName
!= SameOperationalPartnerVersion
```

---

# 77. Update / expiry

## CoordinationStateView

Fast-expiring with task, role, availability, state or communication changes.

## CommonGroundEstimate

Update after grounding/repair/version changes; critical assumptions may expire rapidly.

## RoleContract

Version when allocation/authority/responsibility changes.

## TrustRelationProfile

Intermediate/slow but target-specific; update with consequential behavior and violations/repair.

## DependenceProfile

Update with alternatives/support architecture changes.

## RelationshipOperationalView

Longer horizon, but preserve recent rupture/repair and asymmetry.

## JointCapabilitySurface

Update after changed composition/role/communication/tool regime or repeated performance evidence.

---

# 78. Reflexivity

Coordination models alter the relation they observe.

Examples:

```text
system labels B untrusted
→ routes fewer tasks to B
→ less new evidence about B
```

or:

```text
system forces acknowledgements
→ handoff failures fall
→ observed communication behavior changes
```

Thus:

```text
ObservedCoordinationEvidence
may be policy-produced.
```

---

# 79. Avoid trust surveillance as default

Private relational attitudes should not be inferred or scored merely because traces are available.

For many consumers, the useful object is narrower:

```text
Can this dependency be relied upon for this task under these stakes?
```

not:

```text
How much does Human trust every person/system?
```

---

# 80. Normative firewall

```text
Trust != MoralApproval
Cooperation != MoralGood
RelationshipPersistence != RelationshipHealth
Dependence != Consent
Role != Authority
RoleCapability != LegitimateAuthority
CoordinationEfficiency != Fairness
JointSuccess != FairContribution
TrustPrediction != PermissionToManipulate
RelationshipModel != PermissionToIntervene
HumanRelianceOnAI != TransferOfHumanAuthority
```

---

# 81. Foundation / HOC dependency map

```text
HF4  goals / incentives / commitment
HF8  representation / partner knowledge
HF9  inference / perspective/evidence
HF10 decision / commitment / stopping
HF11 execution / coordination / tools
HF12 interaction / joint action / communication / roles / trust
HF13 norms / authority / institutions
HF14–17 rights / responsibility / legitimacy / governance
HF18 incentives / mechanism interaction
HF22 persistent relationship state
HF23 symbolic communication resources
HOC1 capability / readiness / bottleneck / joint support
HOC2 calibration / verification / reliance / deference
HOC3 learning / role-specific learning
HOC4 state / workload / monitoring burden
HOC5 goal ownership / execution / delegation
```

No new Foundation is required.

---

# 82. Canonical forbidden inferences

```text
SameGoalString != SharedGoal
SharedGoal != IdenticalInternalRepresentation
CommonGround != IdenticalKnowledge
SharedArtifact != SharedUnderstanding
MessageDelivered != CommunicationSuccess
MessageDelivered != HandoffCompleted
NoRepair != MutualUnderstanding
Synchrony != Coordination
Coordination != Cooperation
Cooperation != MoralGood
Role != Subtask
Role != Capability
Role != Authority
Role != Responsibility
AssignedRole != RoleCapability
Trust != Reliability
Trust != Predictability
Trust != Reliance
Trust != Dependence
Trust != Deference
Trust != Authority
Dependence != Trust
ReportedTrust != BehavioralReliance
MoreTrust != BetterTeam universally
TeamSocialConsensus != CalibratedTrust
VerbalTrustRepair != ReliabilityRestored
CommunicationRepair != TrustRepair != RelationshipRepair
RepairCount != CoordinationQuality
RelationshipPersistence != RelationshipHealth
JointPerformance != JointCapability
JointCapability != Sum(MemberCapabilities)
HumanUsesAI != HumanAITeam
Delegation != Teaming
Team != EqualRole
HumanPerceivedConnectionToAI != MutualExperiencedRelationship
InteractionPleasantness != CoordinationQuality
RestoredReliance != RestoredSafety
NoDisagreement != GoodTeam
MoreCommunication != BetterCoordination
MoreRedundancy != BetterTeam universally
```

---

# 83. Operational reasoning grammar

A Human-supporting Agent can use HOC6 as:

```text
1. Declare CollaborationTargetSpec / JointOutcomeSpec.
2. Identify participants and build InterdependenceMap.
3. Establish RoleContracts and check RoleCapabilityFit / authority boundaries.
4. Identify CriticalCommonGroundSet rather than synchronizing everything.
5. Project CommonGroundEstimate from acknowledgements, actions, artifacts and history.
6. Inspect open HandoffCases and CommunicationChannelState.
7. Compute CoordinationReadiness with explicit blockers.
8. If fragile/blocked, run CoordinationFailureInference.
9. Choose NextBestCoordinationAction:
     clarify
     acknowledge
     externalize state
     repair
     reassign role
     calibrate reliance
     add monitoring/redundancy/fallback
     reduce interdependence
     escalate/pause/change partner
     no intervention
10. Track trust/reliance/dependence separately.
11. Treat violations and repair as target-specific episodes.
12. Update JointCapabilitySurface only after enough composition-specific evidence.
13. Preserve Human goal ownership, authority, consent and Human–AI asymmetry throughout.
```

This is a reasoning grammar, not a universal team-management engine.

---

# 84. HOC6 stop rule

HOC6 is complete because it has:

```text
reconstructed collaboration target, participant and dependency structure;
introduced InterdependenceMap and dependency criticality;
reconstructed RoleContract, RoleCapabilityFit and role/authority distinctions;
reconstructed CoordinationStateView;
reconstructed CommonGroundEstimate and CriticalCommonGroundSet without shared-database ontology;
made shared artifacts, acknowledgements and channel state evidence rather than understanding guarantees;
reconstructed HandoffCase and handoff status;
reconstructed MisunderstandingCase, RepairEpisode and RepairCapabilityProfile;
reconstructed TrustRelationProfile, DependenceProfile and TrustCalibrationProfile;
separated reliability/predictability/trust/reliance/dependence/deference/authority;
reconstructed TrustViolationCase and TrustRepairCase;
separated communication, trust and relationship repair;
reconstructed RelationshipOperationalView without one relationship score;
introduced CoordinationLiabilitySet;
reconstructed CoordinationReadiness with explicit blocker modes;
deepened JointCapabilitySurface as composition/role/communication/repair dependent;
formalized Human–AI teaming criteria and asymmetry;
introduced CoordinationFailureInference and NextBestCoordinationAction;
made reduced interdependence, externalized state, redundancy and NO_INTERVENTION legitimate actions;
added composition/version-change, reflexivity, privacy and normative guards;
and connected the multi-participant relational layer back to HOC1–HOC5.
```

No Foundation reopen condition is triggered.

```text
FoundationReopenCondition(HF0–HF23) = false
NextDeepRoute = UNKNOWN
```

HOC6 does not preselect HOC7.
