---
schema_version: 1
id: human.foundations.hf12
title: HF12 — Social Interaction, Joint Action, Communication, Shared Goals, Roles and Cooperation
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
summary: HF12 reconstructs the relational multi-agent layer that appears when independently modeling agents enter the same action loop. It separates co-presence, one-way influence, reciprocal interaction and mutual adaptation; parallel action, coordination, synchrony and joint action; identical individual goals, joint outcome criteria, shared goals, joint commitment and group-level action representation; signal production, communication, grounding, common-ground estimates, understanding and repair; task assignment, role, authority and responsibility; coordination, cooperation, competition, prosociality and altruism; trust, distrust, reliance, dependence and predictability; individual, joint and collective agency; aggregation, synergy and task-relative joint capability; and Human–AI tool use, delegation, supervision, collaboration and teaming. The strongest residual is persistent social order that outlives one interaction: conventions, norms, reputation, sanctions, status, authority, power and institutions.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
  - HF12
related:
  - human.foundations.hf11
  - human.foundations.hf12.sources
  - human.foundations.hf12.continuation
---
# HF12 — Social Interaction, Joint Action, Communication, Shared Goals, Roles and Cooperation

## 0. Status and question

HF11 ended with a repeated residual:

```text
one embodied controller
+ another independently modeling agent
```

The second agent brings independent:

```text
perception
belief/model
goals/subgoals
attention
capabilities
roles
authority
communication state
```

HF12 therefore asks:

> **What changes when action is no longer only situated control, but reciprocal
> action among agents who must predict, signal, align, divide roles, repair
> misunderstanding and sometimes cooperate despite non-identical states and goals?**

Inherited collapses under test:

```text
co-presence = interaction
influence = interaction
synchrony = joint action
coordination = joint action
same individual goal = shared goal
shared goal = identical internal representation
joint commitment = two individual commitments added together
communication = language
communication = information transmission
signal received = message understood
common ground = identical knowledge
no repair = mutual understanding
role = subtask
role = authority
coordination = cooperation
cooperation = prosociality = altruism
competition = no coordination
trust = reliance
trust = predictability
trust = one scalar
joint performance = joint capability
joint capability = sum of individual capability
human + AI performance = team
AI social response = human-equivalent social relation
```

None survives cross-context falsification.

---

# 1. Sociality is not one substance

HF12 does not introduce a scalar `Sociality`.

Instead it uses typed relational predicates and profiles.

```text
CoPresence
Influence
ReciprocalInteraction
MutualAdaptation
Communication
JointAction
Cooperation
TrustRelation
RoleRelation
```

are not synonyms.

---

# 2. Co-presence

Working definition:

```text
CoPresence(A,B,C,t)
= A and B are jointly present/reachable within a context C at time t in a way that
  can potentially support mutual perception or action
```

Co-presence can be physical, mediated or virtual.

---

# 3. Co-presence is not interaction

Two people can sit in the same train without affecting one another's current
behavior.

Thus:

```text
CoPresence != Interaction
```

---

# 4. One-way influence is not reciprocal interaction

A recorded lecture can strongly change a listener while the lecturer cannot be
changed by that listener in the episode.

Thus:

```text
Influence_A→B != ReciprocalInteraction(A,B)
```

---

# 5. Reciprocal interaction

HF12 working definition:

```text
ReciprocalInteraction_D(A,B,t1:t2)
= A's relevant state/action can change B's relevant state/action and B's resulting
  state/action can in turn change A within the declared interaction horizon/domain
```

This does not require symmetry.

---

# 6. Reciprocity is not equality

One participant may have more control, information or authority while the relation
remains reciprocal.

Thus:

```text
ReciprocalInteraction != SymmetricInfluence
```

---

# 7. Bidirectional coupling is a causal property

Live joint tapping and music experiments show that allowing both partners to adapt
to one another changes coordination relative to a prerecorded/unresponsive partner.

Therefore:

```text
BidirectionalCoupling != TwoParallelUnidirectionalResponses
```

---

# 8. Mutual adaptation

Working definition:

```text
MutualAdaptation_D(A,B)
= reciprocal history-dependent change in each agent's action/prediction policy as a
  function of the other's evolving behavior
```

---

# 9. Mutual adaptation is not synchrony

Partners can mutually adapt while maintaining deliberate temporal offset or
complementary trajectories.

Thus:

```text
MutualAdaptation != Synchrony
```

---

# 10. Mutual adaptation is not cooperation

Competitors adapt intensely to one another.

Thus:

```text
MutualAdaptation != Cooperation
```

---

# 11. Actual reciprocity and believed reciprocity differ

People process an otherwise identical signal differently when they believe it comes
from a live social partner rather than a recording.

Therefore:

```text
BelievedLiveInteraction != ActualReciprocity
```

---

# 12. Social-context belief is causally relevant

A participant's model of whether the partner is human/live/agent can alter:

```text
attention
prediction
error response
persistence
trust
```

without changing the physical stimulus.

---

# 13. Social response does not prove social ontology

If a Human responds socially to a machine or prerecorded stimulus, this establishes
something about the Human's partner model and behavior.

It does not by itself prove:

```text
the counterpart is a Human-equivalent social person
```

Thus:

```text
SocialResponseToX != XIsHumanEquivalentSocialAgent
```

---

# 14. Interaction has temporal depth

HF12 distinguishes:

```text
one-shot response
short reciprocal episode
repeated interaction
long-term relationship
institutionally structured relation
```

because history can change prediction, trust, norms and roles.

---

# 15. Interaction_D is qualifier-required

A relation may be interactive for:

```text
movement timing
information exchange
resource allocation
emotion regulation
```

but not another domain.

Thus:

```text
Interaction_D != Interaction_E
```

---

# 16. Parallel action

```text
ParallelAction(A,B)
= A and B act at the same time/context without their contributions jointly
  constituting the declared task outcome
```

---

# 17. Parallel action is not joint action

Two runners training side by side need not be jointly producing one task outcome.

Thus:

```text
ParallelAction != JointAction
```

---

# 18. Coordination

HF11 already defined coordination as structured coupling that stabilizes a task
variable.

HF12 retains it without equating it to joint action.

---

# 19. Synchrony

Synchrony is one measurable temporal/spatial relation among participants' behavior.

It can appear:

```text
spontaneously
competitively
ritually
cooperatively
accidentally
```

---

# 20. Synchrony is not joint action

Spontaneous interpersonal synchrony can occur without explicit shared motor goal.

Thus:

```text
Synchrony != JointAction
```

---

# 21. Joint action is not synchrony

Complex construction, surgery, conversation or turn-taking can be jointly organized
while deliberately asynchronous.

Thus:

```text
JointAction != Synchrony
```

---

# 22. Lower synchrony can improve joint work

Complex production tasks can benefit from division of labor that reduces moment-to-
moment synchrony.

Therefore:

```text
MoreSynchrony != BetterJointAction
```

---

# 23. Coordination is not sufficient for joint action

Two opponents can tightly coordinate their moves while competing.

Thus:

```text
Coordination != JointAction by definition
```

---

# 24. HF12 working definition of joint action

```text
JointAction_D(Agents,G,T)
= an episode in which multiple agents' contributions are organized as
  interdependent parts of producing or maintaining a declared joint task outcome G
  under task T
```

This is operational rather than metaphysically exhaustive.

---

# 25. Joint action requires contribution structure, not identical movement

Participants can have:

```text
complementary roles
asymmetric actions
turn-taking
leader/follower organization
```

while remaining in one joint action.

---

# 26. Interdependence is first-class

If one participant's action is irrelevant to the declared joint outcome, the case
may be co-action rather than genuine task-interdependent joint action.

Use:

```text
ContributionInterdependence_D
```

---

# 27. Shared outcome feedback can create dyadic control

Two-person control experiments show pairs can correct and learn a common output in
ways not reducible to one person's unilateral trajectory.

Thus:

```text
JointControl != OneControllerWithExtraEffector by definition
```

---

# 28. Joint action can create new affordances

The action boundary of a dyad can differ from each member acting alone.

Thus:

```text
JointAffordance_D(A,B,E)
!= Affordance_D(A,E) + Affordance_D(B,E)
```

by simple arithmetic.

---

# 29. Same physical output can have different social organization

Experiments using physically similar tasks under cooperative versus competitive
instructions show different agency/neural/behavioral organization.

Thus:

```text
SameMovementOutput != SameSocialActionStructure
```

---

# 30. Joint-action representation

Joint action can change how action–outcome relations are represented, including
group-level features spanning self and co-actor contributions.

Therefore:

```text
JointActionRepresentation
```

is a real research object.

---

# 31. Joint representation is not identical representation

Two participants may encode different features of the same joint episode.

Thus:

```text
JointRepresentation != IdenticalInternalRepresentation
```

---

# 32. Shared goal is not same goal string

Suppose:

```text
Goal_A = "win the championship"
Goal_B = "win the championship"
```

for two opponents.

The text is identical; the relation is competitive.

Therefore:

```text
Goal_A = G and Goal_B = G
!= SharedGoal(A,B,G) by definition
```

---

# 33. Individual goal content

HF12 preserves HF4 goal content separately for each agent:

```text
GoalContent_A
GoalContent_B
```

---

# 34. Joint outcome criterion

A joint task can specify a criterion:

```text
JointOutcomeCriterion(G)
```

such as both keypresses producing one chord or two agents moving one object.

---

# 35. Shared goal working relation

HF12 uses:

```text
SharedGoal_D(A,B,G)
```

when A and B each represent/accept their contributions as interdependent toward a
joint outcome criterion G within the declared task relation.

---

# 36. Shared goal does not require identical subgoals

A surgeon and assistant can pursue different immediate subgoals toward one joint
operation outcome.

Thus:

```text
SharedGoal != IdenticalSubgoalSet
```

---

# 37. Shared goal does not require equal motivation

One agent may care more about success.

Thus:

```text
SharedGoal != EqualGoalCommitment
```

---

# 38. Shared goal does not require equal authority

A leader and follower can share the task outcome while having asymmetric authority.

Thus:

```text
SharedGoal != EqualAuthority
```

---

# 39. Shared goal does not require synchrony

Turn-taking joint-action experiments directly separate shared-goal condition from
moment-to-moment simultaneous movement.

Thus:

```text
SharedGoal != Synchrony
```

---

# 40. Synchrony does not require shared goal

The converse is equally important:

```text
Synchrony != SharedGoal
```

---

# 41. Shared-goal manipulation changes partner-error processing

When partner contribution is needed for a shared goal, observed partner errors can
change the next action differently from individual-goal contexts.

Thus:

```text
PartnerErrorMeaning depends on GoalRelation
```

---

# 42. Human-partner belief and shared goal can dissociate

Recent turn-taking experiments manipulate:

```text
human vs computer partner belief
shared vs individual goal
```

separately, and find separable effects.

Therefore:

```text
SocialPartnerModel != SharedGoalStructure
```

---

# 43. Shared intentionality is not one established mechanism

The phrase can refer to several constructs:

```text
shared goal representation
joint attention
joint commitment
we-mode experience
common task model
```

HF12 does not collapse them.

---

# 44. Joint intention

HF12 uses a minimal operational family:

```text
JointIntention_D
= a coordinated set of individual intentions whose contents include participation
  in a joint task relation and expectations about complementary partner contribution
```

This is not assumed to be one group mind.

---

# 45. Joint intention is not two private intentions added together

If each agent intends only their own action without representing joint
interdependence, parallel coordinated success can occur without the same joint-
intentional structure.

Thus:

```text
JointIntention != Intention_A + Intention_B
```

---

# 46. Joint intention is not shared goal

A shared goal describes outcome/task relation.

Joint intention additionally concerns intended participation/contribution.

Thus:

```text
SharedGoal != JointIntention
```

---

# 47. Joint commitment

HF12 uses:

```text
JointCommitment_D
= interaction-relative persistence/obligation expectation around continuing,
  completing or properly exiting a joint course
```

without assuming legal or moral obligation by default.

---

# 48. Joint commitment is not equal persistence

Participants can differ in persistence threshold.

Thus:

```text
JointCommitment != SymmetricPersistence
```

---

# 49. Partner effort can alter persistence

Experiments show perceived partner effort can increase persistence in a joint task
when the partner is believed to be a person, with boundary conditions when the same
cue is attributed to an algorithm.

Thus:

```text
PerceivedPartnerInvestment
can change
JointPersistence
```

---

# 50. Partner effort is not sunk cost only

HF10 sunk-cost distinctions remain.

The relevant signal can indicate:

```text
partner commitment
reciprocity expectation
fairness
social obligation
```

rather than only historical resource loss.

---

# 51. Commitment is not moral duty by definition

A joint task may be trivial, harmful or coercive.

Thus:

```text
JointCommitmentEvidence != MoralObligationProof
```

---

# 52. We-mode experience is evidence, not ontology

Participants can report:

```text
"we controlled it"
```

but subjective collective agency does not establish one literal merged agent.

Thus:

```text
WeExperience != GroupPersonhood
```

---

# 53. Communication requires decomposition

HF12 rejects:

```text
sender → information → receiver
```

as sufficient social ontology.

---

# 54. Signal production

```text
SignalProduction(A,s,t)
```

= production of an observable event that may be used by another agent.

---

# 55. Signal is not message

A movement can be observable without being communicatively intended.

Thus:

```text
Signal != Message
```

---

# 56. Message

Working definition:

```text
Message_D
= signal/event treated within an interaction as carrying content or coordination
  relevance for another participant
```

---

# 57. Message is not meaning

The receiver may assign a different content than the sender intended.

Thus:

```text
Message != InterpretedMeaning
```

---

# 58. Meaning is not understanding

A receiver can partially decode a message without integrating the intended task
relation.

Thus:

```text
DecodedContent != MutualUnderstanding
```

---

# 59. Transmission is not communication success

A perfectly transmitted string can be misunderstood.

Therefore:

```text
SignalTransmissionSuccess != CommunicationSuccess
```

---

# 60. Communication is not language

Communication can use:

```text
speech
text
gesture
gaze
touch
movement timing
kinematic exaggeration
environmental modification
```

---

# 61. Language is one communication system

Thus:

```text
Communication != Language
```

---

# 62. Action can be communicative

Leaders can alter movement kinematics to make upcoming action more predictable to
followers even without explicit instruction to signal.

Therefore:

```text
InstrumentalAction
can simultaneously be
CommunicativeAction
```

---

# 63. Communicative action is not merely inefficient movement

Exaggerating a trajectory can reduce individual movement efficiency while improving
joint predictability.

Thus:

```text
IndividualMotorEfficiency != JointCommunicationValue
```

---

# 64. Predictability can substitute for explicit communication

When conventional communication is unavailable, pairs can constrain actions to make
them easier for the partner to predict.

---

# 65. Communication can release behavioral constraints

When richer communication becomes available, agents need not make every action as
stereotyped/predictable.

Thus:

```text
MoreCommunicationCapacity
can reduce
RequiredActionPredictability
```

---

# 66. Communication and predictability can coexist

Minimal reciprocal communication conditions show both strategies can operate
simultaneously.

Therefore:

```text
Communication != AlternativeToActionSignalingOnly
```

---

# 67. Communication channel is not communicative content

The same channel can carry multiple meanings, and the same meaning can be expressed
across channels.

Thus:

```text
Channel != Content
```

---

# 68. Communication channel availability shapes strategy

If speech is noisy, agents may increase gaze, gesture, redundancy or demonstrative
reference.

Thus:

```text
CommunicationPolicy
is channel- and context-adaptive
```

---

# 69. Turn-taking is not communication totality

Turn-taking structures temporal access to a channel.

It does not itself establish shared meaning.

Thus:

```text
TurnTaking != MutualUnderstanding
```

---

# 70. Grounding

HF12 uses:

```text
Grounding_D
= interactive process through which participants obtain enough evidence for the
  current purpose that a contribution has been attended to/interpreted sufficiently
  for continued coordinated action
```

---

# 71. Grounding is purpose-relative

The degree of understanding needed to continue casual conversation differs from
surgery or aviation.

Thus:

```text
GroundingCriterion_D != GroundingCriterion_E
```

---

# 72. Acknowledgment is not proof of understanding

"Okay" can be automatic, polite or mistaken.

Thus:

```text
Acknowledgment != VerifiedUnderstanding
```

---

# 73. Silence is not proof of understanding

No repair request can reflect:

```text
understanding
failure to notice misunderstanding
social reluctance
low stakes
time pressure
```

Thus:

```text
NoRepair != MutualUnderstanding
```

---

# 74. Common ground is overloaded

HF12 separates at least:

```text
SharedInteractionHistory
PartnerSpecificCommonGroundEstimate
ActualRepresentationalOverlap_D
BeliefOfMutualKnowledge_D
EstablishedReferenceConvention
```

---

# 75. Common ground is not identical representation

Participants can coordinate while storing different details, concepts or source
memories.

Thus:

```text
CommonGround != IdenticalInternalRepresentation
```

---

# 76. Common ground is relational

A fact can be common ground between A and B but not A and C.

Therefore:

```text
CommonGround_D(A,B) != CommonGround_D(A,C)
```

---

# 77. Common ground is history-sensitive

Repeated partner interaction allows shorter and more partner-specific references.

Thus:

```text
CommunicationPolicy_t
depends on
PartnerSpecificHistory
```

---

# 78. Personal common ground and local common ground differ

Friends can possess substantial pre-existing shared history while a task creates
new local conventions.

Thus:

```text
PersonalCommonGround != LocalTaskCommonGround
```

---

# 79. Stronger common ground can improve efficiency without perfect recall

Participants may communicate efficiently using partner-specific conventions while
later memory for the exact conversation remains partial.

Thus:

```text
CommunicativeEfficiency != CompleteSharedMemory
```

---

# 80. Common ground estimate can be wrong

Each partner represents what they think the other knows.

That estimate can diverge from actual partner knowledge.

Thus:

```text
CommonGroundEstimate != ActualSharedKnowledge
```

---

# 81. Perspective taking is not perfect

Referential tasks show partner perspective influences production/comprehension but
egocentric interference remains.

Thus:

```text
PartnerModelUse != PerfectPerspectiveTaking
```

---

# 82. Common ground does not fully determine reference choice

Own conceptualization, memory accessibility and partner perspective can jointly
influence referring expressions.

Thus:

```text
ReferenceChoice != CommonGroundLookupOnly
```

---

# 83. Multiparty common ground is not one shared database

With A, B and C, A can maintain partially distinct partner models.

Thus:

```text
CommonGround_Group
!= one identical knowledge set by definition
```

---

# 84. Participant role affects common-ground access

Speaker, addressee, side participant and overhearer can have different evidence and
commitment to what was established.

Thus:

```text
ExposureToConversation != SameCommonGroundStatus
```

---

# 85. Misunderstanding

HF12 working definition:

```text
Misunderstanding_D
= material divergence between participants' interpreted task/message state that can
  alter subsequent interaction if not corrected
```

---

# 86. Misunderstanding is not mere uncertainty

Both partners can be highly confident in incompatible interpretations.

Thus:

```text
Misunderstanding != LowConfidence
```

---

# 87. Repair

HF12 uses:

```text
RepairEpisode = {
  trouble source,
  detection/signal,
  clarification request or correction,
  repair proposal,
  uptake/evidence,
  updated common-ground estimate
}
```

---

# 88. Repair is not repetition only

Repair can involve:

```text
rephrase
specify
correct
ask clarification
change modality
establish new convention
```

---

# 89. Repair changes future communication

Experimental manipulation of misunderstanding feedback changes how dyads converge on
more systematic descriptions.

Thus:

```text
Repair != LocalPatchOnly
```

---

# 90. Communication breakdown can be productive

A detected misunderstanding can expose ambiguity and trigger better conventions.

Thus:

```text
Breakdown != PureCommunicationFailure
```

if successfully repaired.

---

# 91. But repair cost is real

Repair consumes time/attention and can damage trust under high stakes.

Thus:

```text
MoreRepair != BetterInteraction by definition
```

---

# 92. Repair capability is not zero-error communication

A robust interaction system can tolerate errors because it detects and repairs them.

Thus:

```text
CommunicationRobustness != NoMisunderstanding
```

---

# 93. Role

HF12 working definition:

```text
Role_D(A,R,C)
= context-relative bundle of expected contribution, information access,
  decision/action scope, coordination obligations and sometimes authority or
  responsibility associated with participant A
```

---

# 94. Role is not subtask

A role can include:

```text
who initiates
who observes
who decides
who signals
who verifies
who backs up
who may override
```

beyond one action assignment.

Thus:

```text
Role != Subtask
```

---

# 95. Role is not authority

A person can perform a technical role without final decision authority.

Thus:

```text
Role != Authority
```

---

# 96. Role is not responsibility

Execution role and accountability can be separated institutionally.

Thus:

```text
Role != Responsibility
```

---

# 97. Role changes action kinematics

Leader/follower experiments show asymmetric task roles can alter how movements are
made predictable and how imitation/interference occurs.

Thus:

```text
SameMotorTask + DifferentRole
→ DifferentControlPolicy
```

---

# 98. Leader is not simply faster agent

Leadership can concern:

```text
information access
reference setting
signaling responsibility
control authority
```

not raw speed or skill.

---

# 99. Follower is not passive

A follower predicts, adapts and can stabilize the pair.

Thus:

```text
Follower != PassiveReceiver
```

---

# 100. Roles can be complementary

Joint action often benefits from agents doing different things.

Therefore:

```text
RoleDifferentiation != CoordinationFailure
```

---

# 101. Role asymmetry can improve joint performance

Stable leader/follower organization can reduce ambiguity about who adapts to whom.

But:

```text
RoleAsymmetry != AlwaysBetter
```

---

# 102. Roles can switch dynamically

Information quality, environmental state or workload can make the best leader change
over time.

Thus:

```text
Role_t1 != Role_t2
```

is allowed within one joint task.

---

# 103. Flexible leadership can be self-organized

Group decision experiments show better-informed individuals can act earlier while
less-informed members wait and use social information.

Thus:

```text
Leadership != FormalAppointmentOnly
```

---

# 104. Role assignment is not role competence

Giving someone the leader role does not make them good at it.

Thus:

```text
AssignedRole != RoleCapability
```

---

# 105. Role expertise is learnable

Leader/follower expertise can become role-specific.

Thus:

```text
GeneralSkill != RoleSpecificSkill
```

---

# 106. Role expectation can persist beyond current action

Once roles become conventional, normative or institutionally assigned, they can
shape later interactions even without renegotiation.

This begins to expose HF13.

---

# 107. Coordination revisited

HF12 keeps:

```text
Coordination_D
= task-relative structured coupling
```

without moral valence.

---

# 108. Cooperation

HF12 working definition:

```text
Cooperation_D(A,B,G)
= interaction in which agents make contributions that are mutually supportive of a
  shared/joint outcome or mutually accepted benefit relation, rather than merely
  adapting to one another
```

This is descriptive, not automatically moral.

---

# 109. Cooperation is not coordination

Competitors coordinate.

Thus:

```text
Coordination != Cooperation
```

---

# 110. Cooperation is not synchrony

Cooperators can divide labor asynchronously.

Thus:

```text
Cooperation != Synchrony
```

---

# 111. Cooperation is not prosociality

A cooperative act can benefit only the cooperating coalition while harming others.

Thus:

```text
Cooperation != Prosociality
```

---

# 112. Cooperation is not altruism

Agents can cooperate for mutual self-benefit.

Thus:

```text
Cooperation != Altruism
```

---

# 113. Altruism is not required for joint action

Many joint tasks have aligned incentives.

Thus:

```text
JointAction != Altruism
```

---

# 114. Competition is not absence of coordination

Sports, bargaining and adversarial games require extensive mutual prediction and
adaptation.

Thus:

```text
Competition != NoCoordination
```

---

# 115. Competition and cooperation can share motor structure

Experiments can hold visuomotor task nearly constant while changing cooperative or
competitive stance.

Therefore:

```text
PhysicalCoordinationStructure
!= Incentive/SocialRelation
```

---

# 116. Cooperation can contain competition

Team members can cooperate against an opposing team.

Thus relational scale matters:

```text
Cooperation_within_Group
can coexist with
Competition_between_Groups
```

---

# 117. Mixed-motive interaction is normal

A relation can combine:

```text
shared benefit
private benefit
status competition
fairness concern
risk transfer
```

Therefore:

```text
Cooperation_D != PurePreferenceAlignment
```

---

# 118. Cooperative goal can change synchrony and performance

Object-movement experiments show explicit cooperative versus competitive framing
changes coordination/performance patterns.

Thus:

```text
CoordinationPolicy depends on IncentiveRelation
```

---

# 119. Prosocial outcome is not proof of cooperative intention

Accidental or strategic self-interested actions can help others.

Thus:

```text
ProsocialOutcome != CooperativeIntention
```

---

# 120. Cooperative intention is not proof of good outcome

Poor coordination can make cooperative attempts harmful.

Thus:

```text
CooperativeIntention != SuccessfulCooperation
```

---

# 121. Cooperation is not moral good by definition

A group can cooperate efficiently to produce harmful external effects.

Thus:

```text
Cooperation != NormativeGood
```

---

# 122. Joint success is not fair contribution

A task can succeed while one member free-rides.

Thus:

```text
JointSuccess != FairContribution
```

---

# 123. Fairness is not cooperation ontology

Fairness judgments can affect cooperation but remain separate normative/social
constructs.

Thus:

```text
Fairness != Cooperation
```

---

# 124. Trust is qualifier-required

HF12 rejects one scalar `trust`.

Use:

```text
Trust_D(A→B | Task, Stakes, History, Role, Context)
```

---

# 125. Trust is relational

A can trust B to:

```text
drive safely
keep a secret
calculate accurately
act benevolently
```

with different values.

Thus:

```text
Trust_D != Trust_E
```

---

# 126. Trust has target dimensions

Useful dimensions include expectations about:

```text
competence
predictability
integrity/benevolence
information honesty
reliability
```

without assuming these exhaust trust.

---

# 127. Trust is not predictability

A malicious opponent can be highly predictable.

Thus:

```text
Predictability != Trust
```

---

# 128. Predictability can support trust/reliance

In real-time human-agent collaboration, predictable agents can reduce coordination
load and increase reliance/trust measures.

Thus:

```text
Predictability
can be one trust-relevant input
```

but not the construct itself.

---

# 129. Trust is not reliance

A Human can rely because there is no alternative while distrusting the partner.

Thus:

```text
Trust != Reliance
```

---

# 130. Reliance is behavioral policy

```text
Reliance_D(A→B)
= degree to which A allows B's output/action to determine A's own choice/action in
  domain D
```

---

# 131. Reliance is not compliance

In automation research, following an action recommendation and relying on a
no-action recommendation can be behaviorally distinct.

Thus:

```text
Compliance != Reliance
```

in that operational family.

---

# 132. Attitudinal trust and behavioral reliance can dissociate

2026 scheduling experiments found explanation manipulations could increase reliance
or perceived ability without matching changes in measured attitudinal trust.

Thus:

```text
ReportedTrust != BehavioralReliance
```

---

# 133. Trust is not calibrated trust

High trust in an unreliable partner is not successful calibration.

Thus:

```text
TrustLevel != TrustCalibration
```

---

# 134. Trust calibration is task/history dependent

Errors, reliability shifts and explanations can alter later monitoring and reliance.

Use:

```text
TrustCalibrationProfile_D
```

rather than one trait.

---

# 135. Distrust is not simply low trust by definition

Humans can actively monitor, suspect or verify rather than merely assign a low
positive score.

HF12 keeps:

```text
TrustEvidence
DistrustEvidence
```

separable when measurement supports it.

---

# 136. Dependence

Working relation:

```text
Dependence_D(A→B)
= degree to which A's relevant outcome/capability depends on B's action/resource/
  information under current alternatives
```

---

# 137. Dependence is not trust

A patient can depend heavily on a clinician while uncertain about them.

Thus:

```text
Dependence != Trust
```

---

# 138. Dependence can alter trust consequences

Human–AI team experiments show the role that exposes the Human to greater risk from
AI action can alter trust responses after violations.

Thus:

```text
SameAIBehavior + DifferentDependence
→ DifferentTrustUpdate
```

---

# 139. Trust is not understanding

Explanations can raise perceived ability or reliance without ensuring deep model
understanding.

Thus:

```text
Trust != Understanding
```

---

# 140. Explanations can be social cues as well as epistemic aids

A rationale can change perceived competence even when recommendation content is
held constant.

Therefore:

```text
ExplanationEffect != KnowledgeGainOnly
```

---

# 141. Trust can rise when independent evaluation is weak

Recent AI experiments show trust can increase in conditions where task language is
harder to evaluate independently.

Thus:

```text
HigherTrust != BetterIndependentVerification
```

---

# 142. Trust can spread through team structure

Human–AI team experiments indicate experience with one teammate/agent can influence
trust toward others under some structures.

Therefore:

```text
TrustUpdate
can be socially/generalization mediated
```

rather than partner-local only.

---

# 143. Trust repair is not communication repair

Communication repair fixes message/common-ground divergence.

Trust repair concerns expectations about future partner behavior.

Thus:

```text
CommunicationRepair != TrustRepair
```

---

# 144. Successful explanation is not guaranteed trust repair

After high-stakes AI violations, different repair strategies can have limited or
context-dependent effects.

Thus:

```text
Explanation/Apology != TrustRestorationGuarantee
```

---

# 145. Trust can be manipulated by non-performance social cues

Perceived warmth, animacy or social framing can change trust-related judgments even
when task competence is separately manipulated.

Thus:

```text
TrustEvidence != CapabilityEvidence
```

---

# 146. Anthropomorphism is not trust

A system can be anthropomorphized yet distrusted, or trusted instrumentally without
humanlike attribution.

Thus:

```text
Anthropomorphism != Trust
```

---

# 147. Trust is not moral approval

One can trust an opponent to act consistently against one's interests.

Thus:

```text
Trust_D != MoralApproval
```

depending on trust definition/domain.

---

# 148. Collective agency experience

HF11 separated individual and collective sense of agency.

HF12 keeps:

```text
SenseOfJointAgency_D
```

as a first-person/social evidence channel.

---

# 149. Joint agency is not synchrony

When synchronization quality is held similar, richer relational structure among
partners' contributions can alter joint-agency reports.

Thus:

```text
SenseOfJointAgency != SynchronyScore
```

---

# 150. Joint agency is not causal contribution

Participants can over- or underestimate their own/partner contributions.

Thus:

```text
SenseOfJointAgency != CausalAttributionTruth
```

---

# 151. Collective agency is not group personhood

A team can experience/describe `we did it` without becoming one biological or legal
person.

Thus:

```text
CollectiveAgencyExperience != GroupPersonhood
```

---

# 152. Causal contribution should remain decomposed

For a joint outcome record:

```text
participant actions
interaction effects
shared tools
external constraints
```

rather than one undifferentiated group cause.

---

# 153. Joint capability

HF12 uses:

```text
JointCapability_D(Group,Task,Context)
= task-relative capacity of a multi-agent configuration to achieve an outcome under
  its current composition, interaction structure, tools, communication and roles
```

---

# 154. Joint capability is not sum of member capabilities

Interaction can create:

```text
synergy
process loss
error correction
information pooling
coordination overhead
```

Thus:

```text
JointCapability != Sum(IndividualCapabilities)
```

---

# 155. Group performance is not joint capability totality

A single observed outcome may reflect luck or one member's dominance.

Thus:

```text
CurrentGroupPerformance != JointCapability
```

---

# 156. Aggregation and interaction must be separated

A nominal group can pool independent answers without interaction.

An interacting group can additionally create relational effects.

Thus:

```text
AggregationGain != InteractionSynergy
```

---

# 157. Synergy

Working operational definition:

```text
Synergy_D
= group performance gain beyond a declared counterfactual aggregation baseline
  attributable to interaction/process rather than member count alone
```

---

# 158. Synergy is not guaranteed

Interacting groups can underperform nominal groups due to:

```text
coordination cost
communication overhead
conflict
dominance
shared error
```

Thus:

```text
GroupInteraction != PositiveSynergy
```

---

# 159. Task complexity changes synergy

Large preregistered experiments show interacting-group advantages can emerge for
more complex tasks while disappearing for simpler tasks.

Thus:

```text
Synergy_D depends on TaskStructure
```

---

# 160. More communication is not always better group performance

Communication has overhead.

Thus:

```text
MoreCommunication != HigherGroupEfficiency
```

---

# 161. Turn-taking structure can matter independently of communication quantity

Groups with balanced/structured turn-taking can outperform groups with similar or
higher raw communication volume.

Therefore:

```text
CommunicationQuantity != CollaborationQuality
```

---

# 162. Joint capability can include cognitive offloading

A partner can take over part of a cognitive workload, reducing interference for the
other agent.

Thus:

```text
JointCapability
can exceed
IndependentCognitiveCapacity
```

for the task.

---

# 163. Joint capability can create new affordances

Dyads can physically pass through, lift, monitor or control configurations not
available to either member alone.

Thus:

```text
JointAffordance != IndividualAffordanceUnion only
```

because interdependence can create new action modes.

---

# 164. Joint capability is composition-sensitive

Changing one member can alter:

```text
skill coverage
communication fit
trust
role allocation
```

so:

```text
SameAverageSkill != SameJointCapability
```

---

# 165. Joint capability is process-sensitive

Same members can perform differently under changed communication/role structures.

Thus:

```text
SameMembers != SameJointCapability
```

---

# 166. Collective intelligence is an index family, not ontology

Group-performance factor models can be useful summaries.

But evidence varies on whether one universal factor is sufficient, and task/process
structure matters.

Therefore:

```text
CollectiveIntelligenceScore != JointCapabilityOntology
```

---

# 167. Human×AI co-performance is not automatically a team

HF12 distinguishes:

```text
ToolUse
Delegation
Supervision
Collaboration
Teaming
SocialInteraction
```

---

# 168. Human×tool

A tool primarily extends execution/capability under Human control and normally lacks
independent goal modeling.

HF11 owns this case.

---

# 169. Delegation

A Human/principal assigns planning/action scope to another agent.

HF10/HF11 own authority/execution distinctions.

---

# 170. Supervision

Human monitors a comparatively autonomous process and intervenes intermittently.

Thus:

```text
Supervision != Teaming
```

retaining HF11.

---

# 171. Collaboration

HF12 uses a broad operational family for systems in which Human and AI each make
material task contributions and exchange information/actions.

This alone does not establish social symmetry.

---

# 172. Teaming

Working operational definition:

```text
HumanAITeaming_D
= sustained interdependent Human–AI joint task organization in which both sides
  maintain task-relevant state, adapt contributions to one another and occupy
  explicit/implicit roles toward a joint outcome
```

without claiming Human-equivalent personhood for AI.

---

# 173. Teaming is not UI co-presence

Thus:

```text
HumanUsesAI != HumanAITeam
```

---

# 174. Teaming is not delegation alone

A one-way assignment can be delegation without reciprocal adaptation.

Thus:

```text
Delegation != Teaming
```

---

# 175. Teaming is not supervision alone

A Human may supervise a machine whose policy does not model/adapt to the Human as a
partner.

Thus:

```text
Supervision != Teaming
```

---

# 176. Teaming is not anthropomorphism

A Human can perceive an AI socially without task interdependence, and can team with
a non-anthropomorphic system.

Thus:

```text
Anthropomorphism != Teaming
```

---

# 177. Human×AI trust is not Human×Human trust by default

Source cues, perceived animacy, expertise, opacity and controllability differ.

Therefore:

```text
Trust_HumanAI,D
!= Trust_HumanHuman,D by assumption
```

---

# 178. AI explanations can alter reliance without understanding

Thus in Human×AI teams:

```text
ExplainabilitySurface
can change
Role/Trust/DeferencePolicy
```

without improving independent verification.

---

# 179. AI misunderstanding is a team-level event only under interdependence

If an AI produces an error no Human depends on, it is not necessarily a team
communication breakdown.

Thus:

```text
ModelError != TeamMisunderstanding by definition
```

---

# 180. Human–AI misunderstanding can reduce trust and performance

Experiments comparing Human–AI and Human–Human teams show omission/ambiguity can
alter trust and collaborative performance.

Thus:

```text
CommunicationReliability
is a HumanAITeamCapability dimension
```

---

# 181. AI can induce unhealthy social dependence without good teamwork

Sycophantic or overly affirming systems can increase user preference/dependence while
worsening judgment or responsibility-taking.

Therefore:

```text
UserPreferenceForAI != HealthyTeamRelation
```

---

# 182. Social smoothness is not epistemic quality

An agreeable partner can be pleasant but wrong.

Thus:

```text
InteractionFluency != EpistemicReliability
```

---

# 183. Team performance is not Human autonomy

A Human–AI system can perform well while Human independent capability, authority or
understanding decreases.

Thus:

```text
JointPerformance != HumanAutonomy
```

---

# 184. Human autonomy is not maximum independent action

Delegation can be autonomy-enhancing when chosen, reversible and aligned with goals.

Thus:

```text
Autonomy != NoDependence
```

---

# 185. Team role allocation must remain typed

For Human×AI:

```text
Goal setting
option generation
planning
information acquisition
execution
verification
monitoring
override
communication repair
```

may be distributed separately.

---

# 186. Symmetry is not required for teaming

A Human and AI can have complementary roles.

Thus:

```text
Team != EqualRole
```

---

# 187. Complementarity is not automatic synergy

Different capabilities can still interact badly.

Thus:

```text
ComplementaryCapabilities != PositiveSynergyGuarantee
```

---

# 188. Mutual modeling is graded

Participants can model:

```text
partner capability
partner goal
partner uncertainty
partner attention
partner role
```

with different accuracy.

Thus:

```text
PartnerModel_D != PartnerModel_E
```

---

# 189. Theory of mind is not joint action

Mental-state inference can support coordination but is neither necessary nor
sufficient for every form of joint behavior.

Thus:

```text
TheoryOfMind != JointAction
```

---

# 190. Partner modeling can be strategically selective

Only partner states relevant to current action may need representation.

Thus:

```text
SuccessfulJointAction != CompletePartnerModel
```

---

# 191. Common ground and partner model interact

A speaker chooses messages based partly on:

```text
what I know
what I think you know
what I think we established
what the task currently requires
```

These are not one memory store.

---

# 192. Social prediction can create self-fulfilling dynamics

Expecting a partner to be competent/uncooperative can change one's own behavior,
which changes the partner's response.

Thus:

```text
PartnerBelief
can become
InteractionIntervention
```

---

# 193. Reflexivity becomes dyadic

HF0's reflexivity principle strengthens:

```text
Observation/Judgment of Partner
→ changed own behavior
→ changed partner behavior
→ changed evidence about partner
```

---

# 194. Social measurement is intervention-prone

Asking about trust, responsibility or common ground can itself alter the relation.

Thus:

```text
SocialMeasurement != PassiveObservation by default
```

---

# 195. Heterogeneity matters

Two dyads with identical task structure can differ in:

```text
partner models
communication conventions
trust history
skill complementarity
role preference
```

Thus:

```text
DyadStructureSame != InteractionDynamicsSame
```

---

# 196. Relationship history is not current interaction state

Long-term partners can coordinate using conventions unavailable to strangers.

Thus:

```text
CurrentInteractionState != RelationshipHistory
```

---

# 197. Repeated interaction can create persistent relational state

Examples:

```text
trust
reputation
shared labels
expectations
roles
conventions
```

This is a key bridge beyond HF12.

---

# 198. Common convention is not current communication

A pre-existing convention can coordinate strangers who never negotiated it in the
current episode.

Thus:

```text
Convention != CurrentInteractionAgreement
```

---

# 199. Reputation is not direct trust history

A can act toward B based on reports or observations of B's past behavior toward
others.

Thus:

```text
ReputationInformation != DirectInteractionHistory
```

---

# 200. Norm is not shared goal

A social norm can constrain behavior even when current participants do not share a
joint outcome.

Thus:

```text
SocialNorm != SharedGoal
```

---

# 201. Norm is not cooperation

Norms can enforce harmful or wasteful behavior.

Thus:

```text
NormCompliance != Cooperation
NormCompliance != NormativeGood
```

---

# 202. Sanction is not communication repair

Sanctions change incentives/status/options around compliance rather than merely
fixing misunderstanding.

Thus:

```text
Sanction != Repair
```

---

# 203. Authority can pre-exist interaction

A role can carry institutionally established decision rights independent of whether
current partners personally agree.

Therefore:

```text
Authority != CurrentDyadicInfluence
```

---

# 204. Power is not coordination skill

An actor can control resources/options without being the best coordinator.

Thus:

```text
Power != CoordinationCapability
```

---

# 205. Institution is not a large joint action

Institutions persist across episodes and members, encode roles/rules/sanctions and
shape future option sets.

Thus:

```text
Institution != OneJointActionEpisode
```

---

# 206. Social order can outlive participants

Conventions and institutions can persist despite turnover.

This cannot be represented only as current common ground among fixed agents.

---

# 207. Network structure can shape conventions

Large decentralized coordination experiments show shared conventions can emerge
without centralized leadership or explicit population-wide intent.

Thus:

```text
ConventionEmergence != CentralPlannerRequirement
```

---

# 208. Norms can be path-dependent

Collective-risk experiments show exposure history can strengthen cooperation norms
that persist when conditions later change.

Thus:

```text
CurrentPayoffStructure != CurrentNormStrength
```

---

# 209. Punishment can stabilize bad norms

Peer-sanction opportunities can support wasteful contributions when the prevailing
norm favors them.

Thus:

```text
SanctionEnforcement != WelfareImprovement
```

---

# 210. Formal institutions can reshape later behavior

Centralized cooperation-enforcing institutions can produce spillovers beyond the
immediate game.

Therefore:

```text
InstitutionalExposure
can change
FutureSocialPolicy
```

---

# 211. Reputation changes future partner choice/action

Indirect information about others' behavior can alter cooperation even without
personal interaction.

Thus:

```text
CurrentInteractionBehavior
can depend on
ThirdPartyHistory
```

---

# 212. Persistent social order is HF12's strongest residual

HF12 explains current relational coordination.

It cannot fully explain why a stranger enters an interaction already constrained by:

```text
language conventions
professional role
reputation
law
status hierarchy
property rights
sanction rules
institutional authority
```

These structures are not recreated from scratch in each interaction.

---

# 213. SocialInteractionProfile

```text
SocialInteractionProfile_D = {
  participants,
  co-presence mode,
  coupling direction,
  reciprocal adaptation,
  partner models,
  history,
  channels,
  latency,
  task relation,
  asymmetries,
  current outcome
}
```

---

# 214. JointActionProfile

```text
JointActionProfile_D = {
  participants,
  joint outcome criterion,
  individual goals,
  shared-goal evidence,
  contribution interdependence,
  joint intentions,
  commitment/persistence,
  role structure,
  coordination policy,
  feedback,
  joint outcome,
  individual contributions,
  agency evidence
}
```

---

# 215. CommunicationProfile

```text
CommunicationProfile_D = {
  signal producer,
  intended recipient,
  channel,
  message/content hypothesis,
  interpretation,
  common-ground estimate,
  acknowledgment/grounding evidence,
  misunderstanding,
  repair sequence,
  latency/cost,
  effect on joint action
}
```

---

# 216. CommonGroundProfile

```text
CommonGroundProfile_D(A,B) = {
  shared interaction history,
  actual evidence exposure,
  A-model-of-B,
  B-model-of-A,
  partner-specific conventions,
  actual overlap estimate,
  uncertainty,
  grounding evidence,
  known mismatch/repair
}
```

---

# 217. RoleProfile

```text
RoleProfile_D = {
  role holder,
  expected contribution,
  information access,
  initiation/signaling duties,
  decision authority,
  execution scope,
  monitoring/backup duty,
  responsibility relation,
  competence,
  switch conditions
}
```

---

# 218. CooperationProfile

```text
CooperationProfile_D = {
  participants,
  shared/joint benefit relation,
  private incentives,
  externalities,
  contribution structure,
  reciprocity expectation,
  fairness/norm evidence,
  coordination quality,
  defection options,
  joint outcome
}
```

---

# 219. TrustProfile

```text
TrustProfile_D(A→B) = {
  task/domain,
  stakes,
  dependence,
  alternatives,
  competence expectation,
  predictability expectation,
  integrity/benevolence expectation,
  uncertainty,
  direct history,
  reputation/social information,
  reported trust,
  behavioral reliance/compliance,
  monitoring,
  verification,
  calibration error,
  update after success/failure
}
```

---

# 220. JointCapabilityProfile

```text
JointCapabilityProfile_D = {
  member capabilities,
  capability complementarity,
  task complexity,
  role allocation,
  communication/repair,
  trust/dependence,
  aggregation baseline,
  interaction synergy/loss,
  joint affordances,
  robustness,
  transfer/reconfiguration
}
```

---

# 221. HumanAITeamProfile

```text
HumanAITeamProfile_D = {
  Human role,
  AI role,
  joint outcome,
  interdependence,
  Human model of AI,
  AI model/state about Human when available,
  option/planning/execution allocation,
  communication channels,
  common-ground/task-state evidence,
  trust/reliance,
  verification,
  repair,
  authority,
  override,
  adaptation direction,
  joint capability,
  Human autonomy/capability effects
}
```

---

# 222. Cross-context falsifier matrix

| Case | Naive collapse attacked | HF12 surviving distinction |
|---|---|---|
| live reciprocal tapping outperforms unresponsive partner | co-presence = interaction | bidirectional coupling/mutual adaptation matter |
| prerecorded speech believed live changes social processing | actual reciprocity = social context | believed partner model separate from physical reciprocity |
| spontaneous synchrony without instructed shared goal | synchrony = shared goal | synchrony and shared goal separate |
| complex joint construction benefits from reduced synchrony | more synchrony = better joint action | complementary division can outperform synchrony |
| shared vs individual goal alters partner-error response | partner presence = joint goal | goal relation has independent causal role |
| human-vs-computer belief and shared goal manipulated separately | sociality = goal structure | partner model and shared goal dissociate |
| joint action-outcome learning encodes group-level relation | joint = individual actions added | joint representation can span contributions |
| partner effort increases persistence only under social attribution | commitment = sunk cost | perceived partner investment alters joint persistence |
| leader changes movement to signal without instruction | communication = language | instrumental movement can communicate |
| no communication increases action predictability | coordination = fixed motor policy | communication resources change action policy |
| rich communication removes predictability constraint | more predictable = always better | signaling channel substitutes for behavioral constraint |
| partner-specific shared labels shorten references | common ground = generic memory | common ground is relation/history specific |
| speaker still shows egocentric interference | common ground = perfect perspective | partner model is fallible |
| misunderstanding feedback induces systematic reference convergence | repair = repetition | repair changes convention/common-ground state |
| leader/follower roles change kinematics | role = label | role changes control/signaling obligations |
| self-organized informed leaders improve collective decisions | leader = formal authority | leadership can emerge from information quality |
| same visuomotor task under competition/cooperation differs | coordination = cooperation | incentive/social relation distinct from motor structure |
| cooperative group can harm outsiders | cooperation = prosociality | coalition cooperation need not be broadly prosocial |
| AI explanation raises reliance but not attitudinal trust | trust = reliance | trust and reliance dissociate |
| higher dependency role changes AI trust after violation | trust = partner property | trust is relation/task/dependence specific |
| joint-agency ratings differ at matched synchrony | agency = timing | joint agency depends on richer action relation |
| real group beats nominal group only on some tasks | group = positive synergy | aggregation, interaction and task complexity separate |
| dyad gains affordance unavailable alone | group capability = sum | joint affordances can emerge relationally |
| Human+AI misunderstanding harms performance/trust | AI error = individual model defect only | team communication state matters under interdependence |
| sycophantic AI increases preference/dependence despite worse judgment | preference/trust = healthy teaming | social smoothness can conflict with epistemic/autonomy value |
| convention emerges in decentralized population | coordination = current agreement | persistent social conventions can emerge beyond dyad |
| punishment enforces wasteful behavior | norm enforcement = good cooperation | norms/sanctions can stabilize harmful equilibria |
| institution exposure alters later prosociality | institution = current interaction rule | institutional history changes future policy |

---

# 223. Competing models

## M1 — social interaction as co-presence

### Failure

Recorded/unresponsive versus live reciprocal partners produce different adaptation,
while mere co-presence can produce no interaction.

**Disposition:** reject.

## M2 — interaction as bidirectional physical coupling only

### Strength

Explains mutual adaptation.

### Failure

Beliefs about social/live partners can alter processing even when stimuli are held
constant; communication and institutional roles can mediate without continuous
physical coupling.

**Disposition:** retain causal coupling dimension, reject as full social ontology.

## M3 — synchrony theory of joint action

### Failure

Synchrony can occur without shared goal, and asynchronous/complementary division can
support better joint action.

**Disposition:** reject synchrony as definition; retain one coordination surface.

## M4 — shared goal as identical individual goal

### Failure

Competitors can possess identical goal strings; partners can share a joint outcome
while holding different subgoals.

**Disposition:** replace with relational interdependence + joint outcome criterion.

## M5 — group mind / identical representation

### Failure

Partner-specific memory/common-ground asymmetry and role differentiation.

**Disposition:** reject literal identical-state requirement; retain relational joint
representations where evidenced.

## M6 — communication as Shannon transmission

### Strength

Useful for channel capacity/noise.

### Failure

Does not by itself represent intended meaning, grounding, misunderstanding, repair
or action-based signaling.

**Disposition:** retain transmission layer only.

## M7 — communication as language

### Failure

Gesture, gaze, kinematics and action predictability coordinate behavior.

**Disposition:** reject.

## M8 — common ground as identical shared knowledge store

### Failure

Partner models are partial/fallible; exposure roles and conceptualizations differ.

**Disposition:** replace with partner-indexed estimates/history/grounding evidence.

## M9 — role as task assignment

### Failure

Roles alter signaling, information, authority, monitoring and fallback obligations.

**Disposition:** reject flat assignment model.

## M10 — cooperation as prosocial altruism

### Failure

Mutualism, coalition behavior and mixed incentives.

**Disposition:** separate cooperation/prosociality/altruism.

## M11 — competition as no coordination

### Failure

Adversaries continuously predict/adapt and may tightly synchronize.

**Disposition:** reject.

## M12 — trust as one scalar

### Failure

Domain, dependence, source, competence/integrity, report/reliance and calibration
dissociate.

**Disposition:** use typed TrustProfile.

## M13 — trust as reliance

### Failure

Behavioral reliance can be forced, and explanation manipulations can change reliance
without equivalent trust change.

**Disposition:** reject.

## M14 — collective performance as member ability sum

### Failure

Nominal-group baselines, synergy/process loss and task complexity effects.

**Disposition:** use task-relative JointCapability with aggregation baseline.

## M15 — one general collective-intelligence ontology

### Strength

Useful predictive factor in some datasets.

### Failure

Factor structure and process dependence vary; group capability is task/configuration
relative.

**Disposition:** retain as index/model family, not ontology.

## M16 — Human+AI co-use as team

### Failure

Tool use, one-way delegation and supervision need not contain reciprocal joint-task
organization.

**Disposition:** use role/interdependence/mutual-adaptation criteria.

## M17 — anthropomorphic response as Human-equivalent social relation

### Failure

Human social perception can be triggered by labels, liveness beliefs, warmth cues or
interface behavior independently of counterpart ontology.

**Disposition:** separate Human response from counterpart status.

## M18 — dyadic interaction explains social order

### Failure

Conventions, reputation, sanctions, authority and institutions shape strangers
before current interaction and persist beyond member turnover.

**Disposition:** reject as complete social ontology; this exposes HF13.

---

# 224. HF12 anti-laws

## Interaction

1. `CoPresence != Interaction`.
2. `Influence_A→B != ReciprocalInteraction(A,B)`.
3. `ReciprocalInteraction != SymmetricInfluence`.
4. `BidirectionalCoupling != TwoParallelUnidirectionalResponses`.
5. `MutualAdaptation != Synchrony`.
6. `MutualAdaptation != Cooperation`.
7. `BelievedLiveInteraction != ActualReciprocity`.
8. `SocialResponseToX != XIsHumanEquivalentSocialAgent`.
9. `Interaction_D != Interaction_E`.

## Joint action / goal / commitment

10. `ParallelAction != JointAction`.
11. `Synchrony != JointAction`.
12. `JointAction != Synchrony`.
13. `MoreSynchrony != BetterJointAction`.
14. `Coordination != JointAction by definition`.
15. `JointControl != OneControllerWithExtraEffector by definition`.
16. `SameMovementOutput != SameSocialActionStructure`.
17. `JointRepresentation != IdenticalInternalRepresentation`.
18. `Goal_A=G and Goal_B=G != SharedGoal(A,B,G) by definition`.
19. `SharedGoal != IdenticalSubgoalSet`.
20. `SharedGoal != EqualGoalCommitment`.
21. `SharedGoal != EqualAuthority`.
22. `SharedGoal != Synchrony`.
23. `Synchrony != SharedGoal`.
24. `SocialPartnerModel != SharedGoalStructure`.
25. `JointIntention != Intention_A + Intention_B`.
26. `SharedGoal != JointIntention`.
27. `JointCommitment != SymmetricPersistence`.
28. `JointCommitmentEvidence != MoralObligationProof`.
29. `WeExperience != GroupPersonhood`.

## Communication / common ground / repair

30. `Signal != Message`.
31. `Message != InterpretedMeaning`.
32. `DecodedContent != MutualUnderstanding`.
33. `SignalTransmissionSuccess != CommunicationSuccess`.
34. `Communication != Language`.
35. `IndividualMotorEfficiency != JointCommunicationValue`.
36. `Communication != AlternativeToActionSignalingOnly`.
37. `Channel != Content`.
38. `TurnTaking != MutualUnderstanding`.
39. `GroundingCriterion_D != GroundingCriterion_E`.
40. `Acknowledgment != VerifiedUnderstanding`.
41. `NoRepair != MutualUnderstanding`.
42. `CommonGround != IdenticalInternalRepresentation`.
43. `CommonGround_D(A,B) != CommonGround_D(A,C)`.
44. `PersonalCommonGround != LocalTaskCommonGround`.
45. `CommunicativeEfficiency != CompleteSharedMemory`.
46. `CommonGroundEstimate != ActualSharedKnowledge`.
47. `PartnerModelUse != PerfectPerspectiveTaking`.
48. `ReferenceChoice != CommonGroundLookupOnly`.
49. `ExposureToConversation != SameCommonGroundStatus`.
50. `Misunderstanding != LowConfidence`.
51. `Repair != RepetitionOnly`.
52. `Repair != LocalPatchOnly`.
53. `Breakdown != PureCommunicationFailure`.
54. `MoreRepair != BetterInteraction by definition`.
55. `CommunicationRobustness != NoMisunderstanding`.

## Role

56. `Role != Subtask`.
57. `Role != Authority`.
58. `Role != Responsibility`.
59. `Leader != FastestAgent`.
60. `Follower != PassiveReceiver`.
61. `RoleDifferentiation != CoordinationFailure`.
62. `RoleAsymmetry != AlwaysBetter`.
63. `Leadership != FormalAppointmentOnly`.
64. `AssignedRole != RoleCapability`.
65. `GeneralSkill != RoleSpecificSkill`.

## Cooperation / competition

66. `Coordination != Cooperation`.
67. `Cooperation != Synchrony`.
68. `Cooperation != Prosociality`.
69. `Cooperation != Altruism`.
70. `JointAction != Altruism`.
71. `Competition != NoCoordination`.
72. `PhysicalCoordinationStructure != Incentive/SocialRelation`.
73. `Cooperation_D != PurePreferenceAlignment`.
74. `ProsocialOutcome != CooperativeIntention`.
75. `CooperativeIntention != SuccessfulCooperation`.
76. `Cooperation != NormativeGood`.
77. `JointSuccess != FairContribution`.
78. `Fairness != Cooperation`.

## Trust / dependence

79. `Trust_D != Trust_E`.
80. `Predictability != Trust`.
81. `Trust != Reliance`.
82. `Compliance != Reliance`.
83. `ReportedTrust != BehavioralReliance`.
84. `TrustLevel != TrustCalibration`.
85. `Dependence != Trust`.
86. `Trust != Understanding`.
87. `ExplanationEffect != KnowledgeGainOnly`.
88. `HigherTrust != BetterIndependentVerification`.
89. `CommunicationRepair != TrustRepair`.
90. `Explanation/Apology != TrustRestorationGuarantee`.
91. `TrustEvidence != CapabilityEvidence`.
92. `Anthropomorphism != Trust`.
93. `Trust_D != MoralApproval`.

## Joint agency / capability

94. `SenseOfJointAgency != SynchronyScore`.
95. `SenseOfJointAgency != CausalAttributionTruth`.
96. `CollectiveAgencyExperience != GroupPersonhood`.
97. `JointCapability != Sum(IndividualCapabilities)`.
98. `CurrentGroupPerformance != JointCapability`.
99. `AggregationGain != InteractionSynergy`.
100. `GroupInteraction != PositiveSynergy`.
101. `MoreCommunication != HigherGroupEfficiency`.
102. `CommunicationQuantity != CollaborationQuality`.
103. `SameAverageSkill != SameJointCapability`.
104. `SameMembers != SameJointCapability`.
105. `CollectiveIntelligenceScore != JointCapabilityOntology`.

## Human×AI

106. `HumanUsesAI != HumanAITeam`.
107. `Delegation != Teaming`.
108. `Supervision != Teaming`.
109. `Anthropomorphism != Teaming`.
110. `Trust_HumanAI,D != Trust_HumanHuman,D by assumption`.
111. `ModelError != TeamMisunderstanding by definition`.
112. `UserPreferenceForAI != HealthyTeamRelation`.
113. `InteractionFluency != EpistemicReliability`.
114. `JointPerformance != HumanAutonomy`.
115. `Autonomy != NoDependence`.
116. `Team != EqualRole`.
117. `ComplementaryCapabilities != PositiveSynergyGuarantee`.
118. `TheoryOfMind != JointAction`.
119. `SuccessfulJointAction != CompletePartnerModel`.

## Persistent-social-order residual

120. `CurrentInteractionState != RelationshipHistory`.
121. `Convention != CurrentInteractionAgreement`.
122. `ReputationInformation != DirectInteractionHistory`.
123. `SocialNorm != SharedGoal`.
124. `NormCompliance != Cooperation`.
125. `NormCompliance != NormativeGood`.
126. `Sanction != Repair`.
127. `Authority != CurrentDyadicInfluence`.
128. `Power != CoordinationCapability`.
129. `Institution != OneJointActionEpisode`.
130. `ConventionEmergence != CentralPlannerRequirement`.
131. `CurrentPayoffStructure != CurrentNormStrength`.
132. `SanctionEnforcement != WelfareImprovement`.

---

# 225. Minimum HF12 grammar

```text
Agent A state/model/goals             Agent B state/model/goals
        ↓                                      ↓
        └──── perception / prediction / partner models ────┐
                                                           ↓
                                               Reciprocal Interaction
                                            ↙                     ↘
                                   Action / Signal         Action / Signal
                                            ↘                     ↙
                                       Mutual Adaptation
                                              ↓
                                   Joint Task Representation
                                  ↙           ↓           ↘
                         individual goals  shared goal  role structure
                                  \           ↓           /
                                   Communication / Grounding
                                  ↙           ↓           ↘
                           common-ground   repair      trust/dependence
                                  \           ↓           /
                                    Coordination Policy
                                              ↓
                        cooperation / competition / mixed motive
                                              ↓
                                       Joint Action
                                              ↓
                                      Joint Outcome
                                              ↓
                             individual + joint agency evidence
                                              ↓
                             learning / trust / convention update
                                              ↺
```

Across repeated interaction:

```text
interaction history
→ partner-specific expectations
→ shared labels / conventions
→ trust / reputation
→ role stabilization
→ norm / sanction / institution effects
```

The last line is the HF13 boundary.

---

# 226. Reconnection to HF11

HF11 explains:

```text
how one controller realizes action
```

HF12 explains:

```text
how multiple independently modeling controllers organize interdependent action
```

Thus:

```text
MotorCoordination != SocialJointAction
```

---

# 227. Reconnection to HF10

Joint action requires multiple decision/planning policies.

Each participant can retain:

```text
own option set
own stopping rule
own commitment
own plan
```

while coordinating under a joint task.

Thus:

```text
JointPlan != OnePrivatePlanCopiedAcrossAgents
```

---

# 228. Reconnection to HF9

Partner modeling uses inference under uncertainty.

Communication creates evidence about another agent but not direct access to their
mind.

Thus:

```text
PartnerReport != PartnerMentalStateTruth
```

---

# 229. Reconnection to HF8

Common ground, shared goals and role models are representations.

But:

```text
SharedTaskFunction
does not require
IdenticalRepresentationalVehicles
```

---

# 230. Reconnection to HF7

Partner-specific common ground and trust rely on memory of:

```text
who said what
who acted how
which convention was established
```

Thus source/context memory becomes socially functional.

---

# 231. Reconnection to HF6

Interaction policies change through history.

```text
PartnerHistory
→ updated trust / role / signaling / cooperation policy
```

so social relations are adaptive trajectories.

---

# 232. Reconnection to HF5

Stress, fatigue and threat can alter:

```text
trust
communication tolerance
repair
coordination
cooperation
```

without changing formal task roles.

---

# 233. Reconnection to HF4

Each participant retains individual:

```text
goals
values
motivation
preferences
```

while joint structure adds relations among them.

Thus:

```text
SharedGoal != SharedValueSystem
```

---

# 234. Reconnection to HF3

Joint work reallocates attention and working memory between:

```text
task
partner
communication
monitoring
```

but:

```text
JointAttention != JointAction
```

---

# 235. Reconnection to HF2

Joint agency, trust feelings and social connectedness are experiential/evidence
channels.

They remain distinct from objective causal relation or authority.

---

# 236. Reconnection to HF1

HF1 actor/agent/person/authority distinctions are essential.

A group/task system may be an effective joint agent at one functional scale without
becoming one HumanIndividual or one legal/moral person.

Thus:

```text
JointTaskSystem != HumanIndividual
```

---

# 237. Normativity firewall

HF12 strictly separates:

```text
successful coordination
successful cooperation
prosocial outcome
fairness
moral legitimacy
legal authority
```

No arrow among these is automatic.

---

# 238. Cooperation evidence does not justify coercion

A system can increase collective output while reducing participant autonomy or
rights.

Thus:

```text
HigherJointPerformance != LegitimateSocialArrangement
```

---

# 239. Trust evidence does not authorize access

High trust does not itself grant:

```text
permission
legal authority
data access
control rights
```

Thus:

```text
Trust != Authorization
```

---

# 240. Shared goal evidence does not settle responsibility

Multiple agents can share a goal while contributions/responsibility remain unequal.

Thus:

```text
SharedGoal != SharedResponsibilityEqually
```

---

# 241. Group capability does not erase individual rights

Joint-system efficiency is descriptive capability evidence.

It is not a criterion for reducing members to replaceable components.

---

# 242. What HF12 does not establish

HF12 does not establish:

- one final metaphysical definition of social interaction;
- that reciprocal coupling is necessary for every social influence episode;
- that synchrony is unimportant;
- that every shared goal requires explicit mutual awareness;
- one final theory of shared intentionality;
- one group mind or group person;
- that common ground is fully measurable;
- that language is unnecessary for complex human coordination;
- that all misunderstanding is beneficial if repaired;
- one universal role taxonomy;
- that hierarchy is inherently good or bad;
- that cooperation is morally good;
- that competition is socially bad;
- one scalar trust construct;
- that distrust is merely inverse trust;
- one universal trust-repair technique;
- that collective intelligence is unreal or useless;
- that group synergy is generally positive;
- that Human×AI teaming is socially equivalent to Human×Human teaming;
- that AI anthropomorphism should be maximized or minimized by foundation fiat;
- that efficient Human×AI joint performance preserves Human understanding or
  autonomy;
- that a current dyadic interaction model explains conventions, norms, reputation,
  sanctions, power or institutions.

---

# 243. The residual HF12 cannot finish

HF12 can explain agents negotiating and coordinating **inside an interaction**.

But many social facts arrive before the interaction begins:

```text
which language means what
who is licensed to decide
what counts as acceptable behavior
who has a good reputation
what punishment follows violation
who owns a resource
which role carries authority
what status differences are recognized
which institution controls exit/options
```

These facts can:

- persist when participants change;
- coordinate strangers who have never met;
- constrain behavior without current communication;
- alter incentives and authority;
- be enforced by third parties;
- preserve harmful as well as beneficial equilibria;
- be encoded in material, legal, technical and organizational structures.

This is not merely more common ground or a larger joint action.

It is **persistent social order**.

---

# 244. Cross-domain evidence for the residual

Primary experiments show:

```text
local interactions can generate population-wide conventions
minorities can tip established conventions after a critical mass
reputation from third parties changes cooperation
sanctions can enforce even welfare-reducing norms
formal institutions alter cooperation and later social behavior
collective risk can produce norms that persist after conditions change
```

The common feature is:

```text
current social behavior depends on socially persistent structures
that are not reducible to current dyadic state
```

---

# 245. Convention is a persistent coordination object

A convention can be used by agents who did not personally negotiate it.

Therefore the next layer must represent:

```text
population/history/network-level persistence
```

not only partner-specific common ground.

---

# 246. Reputation is a socially distributed state

Information about B can travel through:

```text
observation
gossip
records
ratings
institutional credentials
```

and influence A before A has direct evidence.

This cannot be reduced to direct trust history.

---

# 247. Norms introduce expected/appropriate behavior

A norm is not only prediction of what others do.

It can involve expectations about what agents regard as appropriate and what
sanctions follow violation.

HF12 deliberately does not finish that ontology.

---

# 248. Power introduces option asymmetry

An interaction can look cooperative while one actor controls:

```text
resources
exit
sanctions
information
authority
```

HF12 roles identify the asymmetry but do not yet explain persistent power structure.

---

# 249. Institutions externalize social memory/control

Rules, records, permissions and sanctions can persist outside any one person's
current memory or intention.

This is structurally analogous to external memory/tool support, but with collective
authority and enforcement.

---

# 250. Exact next foundation

HF12 therefore selects:

# HF13 — Social Norms, Conventions, Reputation, Status, Authority, Power, Sanctions and Institutions

HF13 should ask:

1. What is a convention relative to habit, coordination equilibrium and explicit
   agreement?
2. What is a social norm relative to statistical regularity, expectation,
   appropriateness judgment and law?
3. What is norm compliance relative to preference, fear of sanction and strategic
   conformity?
4. What is reputation relative to direct history, gossip, credential and stereotype?
5. What is status relative to role, prestige, dominance and authority?
6. What is authority relative to influence, expertise, permission and coercive
   capacity?
7. What is power relative to capability, dependence, control over options/resources
   and legitimate authority?
8. What is sanction relative to punishment, incentive, enforcement and repair?
9. How do conventions/norms emerge, persist, tip and decay across networks?
10. How do harmful norms and institutions remain stable?
11. What is an institution relative to repeated interaction, organization, rule,
    office and infrastructure?
12. How do formal/technical institutions externalize memory, permissions and
    enforcement?
13. How should Human×AI systems interact with institutional authority, norms and
    machine-enforced rules without treating observed practice as legitimate by
    default?
14. What next boundary emerges after persistent social order is rebuilt?

HF13 should not predefine HF14.

---

# 251. Candidate HF13 falsifiers

- decentralized convention emergence without central planner;
- convention tipping after minority critical mass;
- identical statistical frequency with different appropriateness expectations;
- third-party reputation affecting first interaction;
- direct experience overriding or interacting with reputation;
- punishment increasing cooperation under one norm but enforcing harmful behavior
  under another;
- institution-induced behavior persisting after institution removal;
- cooperative norm persistence after collective-risk manipulation changes;
- expertise without authority versus authority without expertise;
- prestige versus coercive dominance;
- nominal legal permission without practical power and practical power without
  legitimate authority;
- network/organizational role surviving member turnover;
- AI system enforcing a policy that is common but illegitimate;
- automated institutional rule changing options before any Human–AI negotiation.

---

# 252. HF12 synthesis

HF12 began with:

```text
another agent enters the action loop
```

The surviving architecture is not `two controllers + synchrony`.

It requires:

```text
reciprocal interaction
partner modeling
shared/joint versus individual goals
interdependent contributions
joint intention/commitment
multi-channel communication
grounding/common-ground estimates
misunderstanding/repair
roles and asymmetric information/authority
coordination/cooperation/competition distinctions
trust/dependence/reliance calibration
joint agency and joint capability
Human×AI role/interdependence architecture
```

The deepest compressions are:

```text
CoPresence != Interaction
Synchrony != JointAction
SameGoal != SharedGoal
Communication != Transmission != Understanding
CommonGround != IdenticalKnowledge
Role != Subtask != Authority
Coordination != Cooperation != Prosociality != Altruism
Trust != Reliance != Dependence
JointCapability != Sum(IndividualCapability)
HumanUsesAI != HumanAITeam
```

But once repeated interactions stabilize expectations and third-party structures
constrain strangers, the social world can no longer be represented as a collection
of current dyads.

The next question becomes:

> **How do conventions, norms, reputations, statuses, authorities, powers,
> sanctions and institutions persist beyond individual interactions and reshape the
> option space of agents who enter them?**

That is the HF13 persistent-social-order boundary.
