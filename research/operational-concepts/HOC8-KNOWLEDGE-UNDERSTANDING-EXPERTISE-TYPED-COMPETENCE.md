---
schema_version: 1
id: human.operational-concepts.hoc8
title: HOC8 — Knowledge, Understanding, Expertise and Typed Competence
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
summary: Reconstructs the operational epistemic-competence layer downstream of HF8/HF9 and HOC1–HOC7. HOC8 separates internal knowledge evidence, external knowledge access, joint epistemic capability, recall, familiarity, explanation, understanding, expertise, teaching capability, competence claims, recency and provenance. It introduces EpistemicTargetSpec, KnowledgeEvidenceProfile, KnowledgeBoundaryMap, KnowledgeAccessProfile, ExternalEpistemicSupportProfile, EpistemicAttributionCase, UnderstandingProfile, UnderstandingProbePlan, ExpertiseProfile, ExpertiseScopeMap, ExpertiseFreshnessView, TeachingCapabilityProfile, TypedCompetenceClaim, ExpertiseRoutingView, EpistemicCoverageGap, and NextBestEpistemicDevelopmentAction. Expertise is domain-/operation-specific and can improve problem representation while remaining fallible, poorly calibrated or hard to teach. Explanatory satisfaction and jargon are not understanding; external search/AI success is not internal knowledge; expert status is not authority; competence is always typed. No Foundation is reopened and no engineering schema is prescribed.
evidence_status: verified-synthesis
readiness: READY
related:
  - human.foundations.hf8
  - human.foundations.hf9
  - human.operational-concepts.hoc1
  - human.operational-concepts.hoc2
  - human.operational-concepts.hoc3
---
# HOC8 — Knowledge, Understanding, Expertise and Typed Competence

## 0. Admission

A post-HOC7 domain-coverage search found that most residual labels were composites or projections.

The surviving family is:

```text
Knowledge
Understanding
Expertise
Typed Competence
```

because it independently changes:

```text
routing
teaching
review assignment
verification design
novel-task delegation
knowledge refresh
Human–Agent support boundaries
```

while remaining under-specified by raw capability or confidence.

---

# 1. Core deletion

Reject:

```text
can answer
→ knows
→ understands
→ is expert
→ can teach
→ should decide
```

Canonical guards:

```text
Memory != Knowledge
Recall != KnowledgeTotality
Recognition != Recall
Familiarity != Understanding
CorrectAnswer != Understanding
Knowledge != CurrentRecall
KnowledgeAvailable != KnowledgeUsed
ExternalAnswerAccess != InternalKnowledge
SearchSuccess != InternalUnderstanding
JointEpistemicSuccess != IndividualKnowledge
KnowledgeBreadth != UnderstandingDepth
Explanation != Understanding
ExplanationFluency != ExplanationQuality
ExplanatorySatisfaction != Comprehension
Jargon != Completeness
PredictionAccuracy != CompleteUnderstanding
TransferSuccess != CompleteUnderstanding
ProceduralSuccess != ConceptualUnderstanding
Expertise != GeneralIntelligence
Expertise != Infallibility
Expertise != PerfectCalibration
Expertise != TeachingCapability
Expertise != Authority
YearsExperience != Expertise by definition
Competence != OneGlobalScalar
Credential != DemonstratedCompetence
```

---

# 2. EpistemicTargetSpec

Every HOC8 query begins with:

```text
EpistemicTargetSpec = {
  domain,
  target content/problem family,
  required epistemic operation,
  novelty/transfer distance,
  internal-vs-supported requirement,
  recency/freshness requirement,
  reliability criterion,
  consequence,
  evidence protocol,
  intended use
}
```

Possible operations:

```text
recognize
recall
explain
apply
predict
compare
diagnose error
reason counterfactually
select intervention
transfer
teach
verify
```

---

# 3. KnowledgeEvidenceProfile

Avoid `knows=true`.

```text
KnowledgeEvidenceProfile(H, Target, interval) = {
  recognition evidence,
  free-recall evidence,
  source/provenance knowledge,
  relational/structural knowledge,
  procedural/knowing-how evidence,
  application evidence,
  transfer evidence,
  error/boundary knowledge,
  recency,
  retrieval conditions,
  external support used,
  confidence/calibration,
  uncertainty/conflict
}
```

It is an evidence projection, not direct inspection of a hidden knowledge store.

---

# 4. Knowledge evidence is operation-specific

A Human can:

```text
recognize P
but not freely recall P
```

or:

```text
perform procedure Q
but not explain Q propositionally
```

or:

```text
state fact R
but not know its source/reliability
```

Therefore:

```text
KnowledgeEvidence_A
!= KnowledgeEvidence_B
```

---

# 5. Content knowledge and provenance knowledge are separate

```text
ContentKnowledge
!= SourceKnowledge
!= EvidenceKnowledge
```

A Human may know a fact but forget where it came from.

For low-stakes tasks this may be enough; for high-stakes claims, provenance/verification may be required.

---

# 6. KnowledgeBoundaryMap

A useful practical object is:

```text
KnowledgeBoundaryMap(H, Domain, t) = {
  supported-known regions,
  familiar-but-weak regions,
  uncertain regions,
  known unknowns,
  conflicting-model regions,
  stale regions,
  externally-accessible-only regions,
  unsupported claims,
  evidence gaps
}
```

This map is query-relative, not a complete inventory of a mind.

---

# 7. Known unknowns are valuable competence

A Human who correctly recognizes:

```text
I do not know this subproblem
```

can be safer/more useful than someone who produces fluent unsupported answers.

Thus:

```text
KnowledgeBoundaryAwareness
```

is a useful operational surface but remains distinct from knowledge breadth.

HOC2 calibration feeds this surface.

---

# 8. KnowledgeAvailable != KnowledgeUsed

Retained knowledge can fail to influence a current judgment because of:

```text
retrieval failure
attention
fluency
motivation
belief conflict
time pressure
misleading framing
```

Therefore a knowledge profile should not be rewritten solely from one bad judgment.

---

# 9. KnowledgeAccessProfile

```text
KnowledgeAccessProfile(H, Target, Context, t) = {
  internal access mode,
  retrieval latency,
  cue dependence,
  search/support availability,
  source reliability,
  access cost,
  offline/failure fallback,
  support dependence,
  attribution accuracy
}
```

This distinguishes knowledge possession from practical retrievability.

---

# 10. Internal versus external access

At least distinguish:

```text
INTERNAL_UNAIDED
INTERNAL_WITH_CUE
EXTERNAL_SEARCH
EXTERNAL_MEMORY
HUMAN_PARTNER
AI_AGENT
JOINT_WORKSPACE
```

because:

```text
ExternalAccess
can increase situated capability
without increasing internal knowledge.
```

---

# 11. ExternalEpistemicSupportProfile

```text
ExternalEpistemicSupportProfile(H, Target, Support, interval) = {
  support source,
  retrieval/generation role,
  reliability evidence,
  latency/cost,
  provenance visibility,
  verification requirement,
  availability,
  dependency,
  learning/internalization effects,
  attribution error risk
}
```

This connects HOC8 to HOC1/HOC2/HOC3.

---

# 12. External access can distort self-assessment

Internet-search experiments show that successful external retrieval can inflate estimates of internal knowledge, and later unaided performance can remain weaker than confidence implies.

Therefore:

```text
ExternalRetrievability
!= InternalKnowledge
```

and external support usage must remain visible in knowledge evidence.

---

# 13. Joint epistemic success can be misattributed

Working with knowledgeable Human/AI partners can make participants overestimate what they could later do alone.

Thus:

```text
TeamKnowledgeCapability
!= IndividualKnowledge
```

and:

```text
JointSuccess
!= IndividualCompetence
```

---

# 14. EpistemicAttributionCase

```text
EpistemicAttributionCase = {
  task/result,
  Human contribution,
  external source/Agent contribution,
  what information came from where,
  what Human verified,
  what Human internalized if later tested,
  current attribution confidence,
  attribution errors
}
```

This is especially useful after Agent-supported research or problem solving.

---

# 15. Attribution is not authorship totality

Knowing which source supplied information does not by itself settle:

```text
authorship
responsibility
ownership
credit
```

Those remain downstream institutional/normative questions.

---

# 16. UnderstandingProfile

HF8 established that understanding is multi-surface.
Operationally:

```text
UnderstandingProfile(H, Domain/Target, interval) = {
  explanation quality,
  structural/causal relations,
  prediction,
  counterfactual handling,
  boundary conditions,
  intervention reasoning,
  novel application,
  transfer/generalization,
  error diagnosis,
  model comparison,
  uncertainty/calibration,
  support dependence
}
```

No one surface is necessary/sufficient in every domain.

---

# 17. Understanding != explanation

A Human can generate a fluent explanation from memorized language while failing novel prediction or transfer.

A Human can also possess procedural/motor understanding that is not exhaustively verbalizable.

Therefore:

```text
ExplanationAbility
!= UnderstandingTotality
```

---

# 18. Explanation remains a strong probe

Attempting a detailed explanation can expose missing causal/structural links that self-ratings conceal.

Thus HOC8 keeps:

```text
EXPLANATION_PROBE
```

but interprets its outcome as evidence, not definition.

---

# 19. Feeling of understanding is fragile

People can substantially overestimate their explanatory depth before they try to explain mechanisms in detail.

Therefore:

```text
SelfRatedUnderstanding
!= DemonstratedUnderstanding
```

HOC2 calibration must remain attached to HOC8 self-assessment.

---

# 20. Jargon can inflate explanatory satisfaction

Recent experiments show technical jargon can make weak scientific explanations feel more satisfying to lay readers even while lowering comprehensibility.

Therefore:

```text
ExplanatorySatisfaction
!= Comprehension
```

and:

```text
TechnicalVocabulary
!= StructuralUnderstanding
```

---

# 21. Comprehensibility != truth

The reverse guard also matters:

```text
EasyToUnderstand
!= True
```

A clear false explanation can be comprehensible.

Understanding evaluation must preserve truth/evidence separately through HOC2.

---

# 22. UnderstandingProbePlan

```text
UnderstandingProbePlan(Target, Use) = {
  explanation probe?,
  prediction probe?,
  boundary-case probe?,
  counterfactual probe?,
  intervention probe?,
  novel transfer probe?,
  error-diagnosis probe?,
  compare-rival-model probe?,
  support removal/change?,
  confidence estimate?
}
```

Probe selection should match intended use.

---

# 23. Understanding depth is target-relative

A person may understand:

```text
how to use a system
```

without understanding:

```text
its physical mechanism
```

or understand:

```text
local mechanism
```

without broader system interactions.

Therefore:

```text
Understanding_D
!= Understanding_E
```

---

# 24. Breadth and depth are separate

```text
KnowledgeBreadth
!= UnderstandingDepth
```

A wide factual vocabulary can coexist with shallow causal understanding; narrow expertise can be deep.

---

# 25. ExpertiseProfile

HOC8 reconstructs:

```text
ExpertiseProfile(H, Domain, interval) = {
  scope/subdomains,
  acquired knowledge organization,
  problem-representation quality,
  cue/feature discrimination,
  pattern recognition,
  retrieval/search efficiency,
  structural analogy/transfer,
  judgment quality,
  verification/error diagnosis,
  adaptation to novelty,
  boundary awareness,
  calibration,
  teaching/communication evidence,
  recency/freshness,
  support/tool dependence,
  uncertainty
}
```

This is not a single expert score.

---

# 26. Expertise is domain-specific

```text
Expertise_D
!= GeneralIntelligence
!= GlobalReasoningSuperiority
```

An expert in one domain may be a novice in another.

Even within one discipline, subdomain boundaries matter.

---

# 27. Expertise changes representation

Classic and contemporary expert–novice research supports that experts can represent domain problems using deeper/selective structural features rather than the surface cues novices preferentially use in studied tasks.

Operational implication:

```text
Expertise
can change
ProblemRepresentation
→ SearchSpace / retrieval / action
```

---

# 28. Expertise can improve structural transfer

Experts can show greater spontaneous positive transfer when underlying structure matches despite surface differences in studied domains.

But:

```text
Expertise != UniversalTransfer
```

new domains and misleading prior schemas can still cause failure.

---

# 29. Expertise can also create blind spots

Prior domain organization can cause:

```text
schema-driven expectation
missed novelty
communication abstraction
stale convention
confidence inflation
```

Therefore ExpertiseProfile must include observed blind spots/failure classes where material.

---

# 30. Expertise != perfect calibration

Experts can possess genuinely greater domain knowledge while overestimating how completely they can explain details.

Thus:

```text
Expertise
and
ExpertiseSelfAssessment
```

remain separate.

---

# 31. ExpertiseScopeMap

```text
ExpertiseScopeMap(H,D) = {
  strong routine regions,
  strong novel/transfer regions,
  verification-only strengths,
  stale/weak subdomains,
  known blind spots,
  unsupported extensions,
  evidence dates
}
```

This prevents one expert label from transporting across the entire discipline.

---

# 32. ExpertiseFreshnessView

Knowledge can become stale when:

```text
standards change
software changes
law/policy changes
scientific evidence changes
practice stops
role changes
Agent/tool ecology changes
```

```text
ExpertiseFreshnessView(H,D,t)
```

tracks recency and update evidence without treating older expertise as zero.

---

# 33. Stale != false totality

An expert may retain durable conceptual structure while some facts/procedures are outdated.

```text
StaleKnowledgeRegion
!= NoExpertise
```

The correct action may be targeted refresh rather than global downgrade.

---

# 34. Years of experience is only evidence

```text
YearsExperience
!= Expertise by definition
```

Experience quantity can differ from deliberate practice, feedback quality, task diversity, recency and actual performance.

Use history as evidence/prior, not identity.

---

# 35. Credential is only evidence

```text
Credential
!= CurrentCompetence
!= AuthorityOutsideCredentialScope
```

Credentials may be strong institutional evidence under their legitimate scope but do not replace task-specific current evidence.

---

# 36. Expertise != authority

An expert can have epistemic weight without decision authority.

A legitimate authority can also require expert input while retaining the final decision role.

```text
Expertise != Authority
```

HOC6/HF13/HF17 remain authority owners.

---

# 37. Expertise != teaching capability

Experts can organize knowledge at levels of abstraction that are difficult for novices to follow.

Experimental work has shown beginners can sometimes give novices more immediately usable instructions on a target task, while expert instruction can support better transfer to a related task.

Therefore:

```text
Expertise
!= TeachingCapability
```

and teaching must have its own evidence.

---

# 38. TeachingCapabilityProfile

```text
TeachingCapabilityProfile(H, LearnerProfile, Target, interval) = {
  learner-state diagnosis,
  explanation comprehensibility,
  example selection,
  scaffolding/hint quality,
  misconception detection,
  feedback quality,
  challenge calibration,
  transfer support,
  adaptation to learner response,
  outcome evidence
}
```

This profile is relational to a learner/target.

---

# 39. Teaching clarity != transfer value

Simple concrete instruction may optimize immediate execution while more abstract structure may support later transfer.

Thus:

```text
ImmediateTeachingPerformance
!= LongTermTransferValue
```

HOC3 learning objective determines which matters.

---

# 40. Teaching fluency != teaching effectiveness

A charismatic or jargon-rich explanation can feel impressive without improving learner understanding.

```text
SpeakerFluency
!= LearnerUnderstandingGain
```

Teaching evidence should include learner outcome when stakes justify it.

---

# 41. TypedCompetenceClaim

Reject `H is competent`.

Use:

```text
TypedCompetenceClaim = {
  competence type,
  target/domain/role,
  criterion,
  conditions/support,
  evidence,
  recency,
  uncertainty,
  authority relevance if any
}
```

---

# 42. Competence families

Useful types include:

```text
TASK_COMPETENCE
ROLE_COMPETENCE
EPISTEMIC_COMPETENCE
DECISION_COMPETENCE
EXECUTION_COMPETENCE
VERIFICATION_COMPETENCE
TEACHING_COMPETENCE
LINGUISTIC/COMMUNICATION_COMPETENCE
```

Each is a composition over different HOCs.

---

# 43. Task competence

Mostly consumes:

```text
HOC1 CapabilitySurface
HOC4 state/readiness
HOC5 execution
```

HOC8 need not duplicate those measurements.

---

# 44. Epistemic competence

Can compose:

```text
KnowledgeEvidenceProfile
UnderstandingProfile
HOC2 calibration/verification
boundary awareness
```

This is useful for review/research/escalation routing.

---

# 45. Role competence

Consumes:

```text
role requirements from HOC6
+ capability/knowledge/verification/execution relevant to role
```

Therefore:

```text
RoleCompetence
!= RoleAssignment
```

---

# 46. Decision competence must remain domain/authority scoped

Good domain knowledge and reasoning may support decision quality but do not automatically grant legal/moral capacity or authority in every context.

```text
DecisionCompetenceEvidence
!= DecisionAuthority
```

---

# 47. ExpertiseRoutingView

A major practical output:

```text
ExpertiseRoutingView(TargetTask, CandidateParticipants) = {
  relevant scope match,
  knowledge/understanding evidence,
  verification strength,
  novelty/transfer evidence,
  freshness,
  teaching need if applicable,
  support dependence,
  calibration,
  conflicts of interest/authority boundary if externally supplied,
  uncertainty
}
```

It helps choose who should be consulted/review/teach—not who has moral authority.

---

# 48. Best performer != best reviewer

HOC2 already separates generation from verification.

HOC8 adds:

```text
BestGenerator
!= BestDomainExplainer
!= BestVerifier
!= BestTeacher
```

Routing should use the operation actually needed.

---

# 49. Best expert != best novice teacher

If target is rapid novice instruction, an expert with poor pedagogical adaptation can be inferior to a less expert but better teacher.

If target is transfer/structural generalization, the ranking can reverse.

Thus routing is objective-relative.

---

# 50. EpistemicCoverageGap

```text
EpistemicCoverageGap(H/Team, TargetSpec) = {
  required knowledge/understanding operations,
  currently covered operations,
  unsupported/stale regions,
  external-access dependencies,
  missing verification,
  missing expertise,
  uncertainty
}
```

This helps decide whether to learn, search, consult, recruit, verify or defer.

---

# 51. Team epistemic coverage

A team can collectively cover a domain through distributed expertise.

```text
TeamEpistemicCoverage
!= EveryMemberKnowsEverything
```

HOC6 common-ground only needs critical coordination interfaces, not duplicated expertise everywhere.

---

# 52. Distributed expertise creates dependency

If only one participant knows a critical subsystem:

```text
EpistemicCoverage high
but
DependencyFragility high
```

HOC6 InterdependenceMap and HOC8 ExpertiseScopeMap should be used together.

---

# 53. Redundant expertise has value and cost

A second independent expert can improve:

```text
verification
continuity
error independence
```

but costs resources.

```text
MoreExpertiseDuplication
!= AlwaysBetter
```

Decision depends on consequence and correlated-error structure.

---

# 54. Agent expertise attribution

Do not label an Agent `expert` solely from general benchmark reputation.

A practical Agent expertise claim needs:

```text
task/domain evidence
version
support/tool configuration
failure classes
verification/calibration evidence
freshness
```

```text
ModelBrand != ExpertiseEvidence
```

---

# 55. Same model != same epistemic system

Tool access, retrieval corpus, system prompt, memory, policy and version can change what an Agent can know/use.

```text
SameBaseModel
!= SameOperationalKnowledgeAccess
```

HOC6 version guards apply.

---

# 56. AI answer quality != Human understanding

A Human can submit a strong AI-generated answer with weak internal understanding.

```text
AIAssistedAnswerQuality
!= HumanUnderstanding
```

This is not inherently bad if the objective is joint performance and verification is adequate.

---

# 57. Human understanding may grow with Agent use

Conversely:

```text
AIUse
```

can support learning/understanding when interaction policy promotes explanation, retrieval, feedback and transfer.

Therefore:

```text
AIUse != LearningHarm
AIUse != LearningGain
```

HOC3 trajectory evidence decides.

---

# 58. Competence drift

Knowledge/expertise can change through:

```text
learning
non-use
new standards
new tools
health/state change
role change
external automation
```

Typed competence claims require expiry/update rules.

---

# 59. Knowledge freshness

Freshness is not simply age.

A 30-year-old mathematical theorem may remain current; a 6-month-old API detail may be obsolete.

```text
KnowledgeFreshness
= target/change-rate/source/update dependent
```

---

# 60. Freshness evidence sources

Possible evidence:

```text
recent successful use
recent assessment
recent teaching/review
recent primary-source update
recent transfer to changed environment
```

Do not infer freshness from confidence.

---

# 61. Expertise and novelty

Routine expert performance and adaptive expert performance can diverge.

Thus ExpertiseProfile should distinguish:

```text
ROUTINE_REGION
ADAPTIVE/NOVEL_REGION
OUT_OF_SCOPE
```

rather than extrapolating routine excellence to unprecedented cases.

---

# 62. Novelty can reverse rankings

A novice may lack routine efficiency but avoid a domain expert's entrenched assumption in unusual cases.

This does not make novices globally superior.

```text
ExpertiseAdvantage
is task/novelty conditional.
```

---

# 63. Explanation quality needs receiver-relative evidence

An explanation can be correct yet incomprehensible to its receiver.

```text
ExplanationCorrectness
!= ExplanationComprehensibility
```

and:

```text
ComprehensibilityForA
!= ComprehensibilityForB
```

Teaching/communication evaluation is relational.

---

# 64. Jargon can be legitimate

HOC8 does not ban technical vocabulary.

In expert-expert communication, jargon can increase precision/efficiency.

The guard is:

```text
JargonPresence
!= EvidenceOfUnderstanding
```

and receiver comprehension must be separately assessed where relevant.

---

# 65. Explanation completeness is target-relative

A useful explanation need not include every mechanism.

```text
ExplanationCompleteness(TargetQuestion, Audience, Purpose)
```

is better than global completeness.

---

# 66. Understanding can be local yet useful

A Human can have a valid local model within an operating envelope while lacking deeper theory.

```text
LocalUnderstanding
!= CompleteWorldModel
```

Operationally this can be sufficient if boundary conditions are known.

---

# 67. Boundary knowledge can dominate detail volume

For safe use, knowing:

```text
when a method fails
when assumptions break
when to escalate
```

can matter more than memorizing many details.

HOC8 therefore treats boundary awareness as a first-class understanding surface.

---

# 68. Unknown unknowns remain unavoidable

KnowledgeBoundaryMap can only represent evidenced gaps.

```text
NoKnownGap
!= CompleteKnowledge
```

A robust system preserves residual uncertainty and novelty risk.

---

# 69. Calibration and knowledge remain distinct

```text
HighKnowledge + poor calibration
LowKnowledge + good calibration
```

are both possible.

HOC2 owns calibration; HOC8 owns target knowledge/understanding evidence.

---

# 70. Verification and expertise remain distinct

An expert may generate well but miss certain error classes.

A specialized verifier may detect them better.

```text
ExpertiseProfile
!= VerificationCapabilitySurface
```

HOC2 must remain separate.

---

# 71. Knowledge and skill remain distinct

```text
KnowingThat
!= KnowingHow
```

but both can contribute to expertise.

HOC1/HOC3 own stable skill/capability evidence; HOC8 records epistemic organization and relationships to those capabilities.

---

# 72. Knowledge and learning remain distinct

```text
CurrentKnowledge
!= LearningRate
```

A novice may learn quickly; an expert may currently know much but update slowly in a changed domain.

HOC3 modifiability remains independent.

---

# 73. Knowledge and confidence remain distinct

```text
Confidence != Knowledge
```

HOC2 evidence can calibrate self-assessment but cannot substitute for target probes.

---

# 74. Competence and permission remain distinct

```text
CompetentToPerform
!= PermittedToPerform
```

HOC6/institutional authority must still gate regulated/high-impact actions.

---

# 75. Expertise labels can become self-fulfilling

If a system labels H an expert and routes only familiar tasks to H:

```text
expertise evidence grows only in old scope
novel transfer evidence remains missing
```

If it labels H a novice and never offers challenge:

```text
learning opportunity falls
```

Thus routing policy conditions future expertise evidence.

---

# 76. Anti-credentialism guard

Institutional credentialing can be legitimate and important.

But HOC8 refuses:

```text
CredentialPresent
→ all competence claims true
```

or:

```text
CredentialAbsent
→ no competence
```

without domain-specific rules.

---

# 77. Anti-amateur-overreach guard

The reverse error also matters: a few successful self-taught episodes do not erase the evidential value of deep professional training/experience in complex domains.

```text
FewSuccesses
!= BroadExpertise
```

Evidence scope must expand before the claim expands.

---

# 78. Expertise evidence ladder

Approximate operational ladder:

```text
X0 self-label / reputation only
X1 credential/experience history
X2 repeated routine-domain performance
X3 error diagnosis / verification evidence
X4 varied cases / structural transfer
X5 novel/adaptive cases
X6 teaching/mentoring outcomes if teaching is claimed
X7 longitudinal robust performance under changed tools/standards
```

This is not a universal professional licensing hierarchy.

---

# 79. Understanding evidence ladder

```text
U0 familiarity / self-rating
U1 accurate recall
U2 coherent explanation
U3 prediction on changed examples
U4 boundary/counterexample handling
U5 counterfactual/intervention reasoning
U6 novel transfer / error diagnosis
U7 robust performance under representational/support changes
```

Different domains may reorder or omit probes.

---

# 80. Knowledge evidence ladder

```text
K0 exposure claim
K1 recognition
K2 free recall
K3 source/evidence-aware recall
K4 correct application
K5 varied application / transfer
K6 stable access across time/context
```

Again, knowing-how/procedural targets require different evidence channels.

---

# 81. EpistemicCoverageGap actions

Possible actions:

```text
RETRIEVE_INTERNAL
SEARCH_EXTERNAL
REQUEST_SOURCE
CONSULT_EXPERT
REQUEST_SECOND_EXPERT
VERIFY_CLAIM
REFRESH_STALE_KNOWLEDGE
LEARN_TARGET
PRACTICE_TRANSFER
PROBE_UNDERSTANDING
ASK_FOR_BOUNDARY_CASES
CHANGE_EXPERT/REVIEWER
ADD_REDUNDANCY
DEFER_OUT_OF_SCOPE
```

---

# 82. NextBestEpistemicDevelopmentAction

```text
NextBestEpistemicDevelopmentAction(
  H,
  Target,
  IntendedUse,
  KnowledgeEvidence,
  UnderstandingProfile,
  ExpertiseProfile,
  Constraints
)
```

candidate actions include the above plus:

```text
EXPLAIN_FROM_MEMORY
PREDICT_BEFORE_LOOKUP
COMPARE_RIVAL_MODELS
DIAGNOSE_ERROR
TEACH_BACK
UPDATE_FROM_PRIMARY_SOURCE
SUPPORT_REMOVAL_CHECK
NO_INTERVENTION
```

This is not always a learning action; it can be evidence acquisition or routing.

---

# 83. Primary-source refresh can be a special action

When knowledge freshness matters in fast-moving domains:

```text
UPDATE_FROM_PRIMARY_SOURCE
```

may be preferred over generic recall practice.

This connects HOC8 to provenance and HOC2 verification.

---

# 84. Teaching back is a probe, not proof

```text
TEACH_BACK
```

can reveal gaps and test communicability.

But memorized fluent teaching can still mask weak transfer.

```text
SuccessfulTeachBack
!= CompleteUnderstanding
```

---

# 85. Out-of-scope recognition is a strong expert behavior

An expert who says:

```text
this is outside my subdomain
```

may be displaying better expertise calibration than one who answers everything.

So:

```text
Refusal/Deference
can be positive evidence
```

when scope judgment is accurate.

---

# 86. Expertise routing should preserve conflicts

A highly qualified expert can still have:

```text
conflict of interest
institutional dependency
advocacy role
```

HOC8 can carry externally supplied conflict metadata but does not adjudicate ethics/authority by itself.

---

# 87. Team expertise and common ground

Distributed expertise does not require everyone to understand every detail.

HOC6 CriticalCommonGroundSet should contain:

```text
interfaces
assumptions
handoff meanings
decision-relevant summaries
```

while deeper local expertise can remain specialized.

---

# 88. Expert explanation creates compression risk

Experts may omit steps they experience as obvious.

This can produce:

```text
correct-but-inaccessible explanation
```

for novices.

TeachingCapabilityProfile should track omitted-prerequisite failures separately from factual error.

---

# 89. Novice-friendly explanation can omit transferable structure

Conversely, concrete instruction can produce immediate success without a reusable structural model.

```text
ImmediateInstructionSuccess
!= TransferableUnderstanding
```

HOC3 retention/transfer tests decide.

---

# 90. Knowledge state is versioned

Every high-impact KnowledgeEvidenceProfile should preserve:

```text
observed_at
valid_through / staleness policy if any
target/version
support regime
source/provenance
```

because fast-changing domains can invalidate factual expertise without erasing deeper competence.

---

# 91. Update / expiry

## KnowledgeEvidenceProfile

Update from new valid probes, learning, corrected evidence and major environment changes.

## KnowledgeAccessProfile

Fast update with support/search/tool changes.

## UnderstandingProfile

Intermediate; update after varied explanatory/predictive/transfer/error-diagnosis evidence.

## ExpertiseProfile

Slow/intermediate; require repeated domain evidence. Update scope/freshness aggressively when standards/tools change.

## TypedCompetenceClaim

Expiry depends on domain change rate and evidence consequence.

---

# 92. Reflexivity

Epistemic labels influence future evidence:

```text
label expert
→ route hard tasks/reviews
→ more expertise evidence
```

or:

```text
label novice
→ route only trivial tasks
→ no evidence of higher capability
```

Thus:

```text
ObservedExpertiseEvidence
may be routing-policy conditioned.
```

---

# 93. Privacy / dignity boundary

A system should not build a total map of what a Human knows merely because it can test them.

Collect only epistemic evidence relevant to legitimate consumer purposes.

```text
CanAssess != ShouldAssessEverything
```

---

# 94. Normative firewall

```text
Knowledge != MoralWorth
Ignorance != MoralFault by definition
Expertise != Authority
Expertise != HumanValue
Competence != Consent
Competence != RightToControlOthers
Credential != MoralRank
LowUnderstanding != PermissionToManipulate
EpistemicPrediction != LegitimateExclusion
```

---

# 95. Foundation / HOC dependency map

```text
HF7  memory/retrieval/source/context
HF8  knowledge/belief/concept/schema/mental model/understanding
HF9  reasoning/problem representation/analogy/causality
HF11 skill/action/tool use
HF23 language/symbol/explanation
HD10 individual-difference projection safeguards
HOC1 capability/readiness/bottleneck
HOC2 confidence/calibration/verification/reliance
HOC3 learning/retention/transfer/modifiability
HOC4 state/fatigue impacts on access/performance
HOC5 goals/motivation affect knowledge use
HOC6 role/common-ground/expert routing/authority
HOC7 health effects and high-stakes boundary examples
```

No new Foundation is required.

---

# 96. Canonical forbidden inferences

```text
Recall != KnowledgeTotality
Recognition != Recall
Familiarity != Understanding
CorrectAnswer != Understanding
Knowledge != CurrentRecall
KnowledgeAvailable != KnowledgeUsed
ExternalAnswerAccess != InternalKnowledge
SearchSuccess != InternalUnderstanding
JointSuccess != IndividualKnowledge
KnowledgeBreadth != UnderstandingDepth
Explanation != Understanding
ExplanationFluency != ExplanationQuality
ExplanatorySatisfaction != Comprehension
Jargon != Completeness
PredictionAccuracy != CompleteUnderstanding
TransferSuccess != CompleteUnderstanding
ProceduralSuccess != ConceptualUnderstanding
Expertise != GeneralIntelligence
Expertise != Infallibility
Expertise != PerfectCalibration
Expertise != TeachingCapability
Expertise != Authority
YearsExperience != Expertise
Credential != CurrentCompetence
Credential != AuthorityOutsideScope
Competence != OneGlobalScalar
RoleCompetence != RoleAssignment
DecisionCompetence != DecisionAuthority
BestPerformer != BestReviewer
BestExpert != BestTeacher
ModelBrand != ExpertiseEvidence
SameBaseModel != SameOperationalKnowledgeAccess
AIAssistedAnswerQuality != HumanUnderstanding
SuccessfulTeachBack != CompleteUnderstanding
NoKnownGap != CompleteKnowledge
```

---

# 97. Operational reasoning grammar

A Human-supporting Agent can use HOC8 as:

```text
1. Declare EpistemicTargetSpec and intended operation.
2. Build KnowledgeEvidenceProfile rather than `knows=true`.
3. Separate internal, cued, external-search, Human-partner and Agent-supported access.
4. Build KnowledgeBoundaryMap including stale/unknown/external-only regions.
5. If understanding matters, choose a purpose-specific UnderstandingProbePlan.
6. Keep explanation, prediction, transfer, intervention and error-diagnosis evidence separate.
7. If an expert label is needed, build ExpertiseProfile + ExpertiseScopeMap + freshness evidence.
8. Separate Expertise from TeachingCapability and HOC2 VerificationCapability.
9. Express competence only as TypedCompetenceClaim with target/criterion/context/evidence.
10. For routing, use ExpertiseRoutingView instead of reputation alone.
11. If epistemic coverage is missing, use EpistemicCoverageGap to choose search, consultation, learning, verification, refresh or deferral.
12. Preserve external-source/Agent contribution with EpistemicAttributionCase.
13. Update/expire claims when domain/tool/version changes.
14. Never convert expertise/competence into authority, worth or consent.
```

This is a reasoning grammar, not an exam engine or universal expertise ranking.

---

# 98. HOC8 stop rule

HOC8 is complete because it has:

```text
reconstructed current knowledge as evidence profiles rather than knows=true;
separated recognition, recall, provenance, application, transfer and procedural knowledge evidence;
introduced KnowledgeBoundaryMap and knowledge-access/support profiles;
made external/Agent epistemic support and attribution first-class;
reconstructed UnderstandingProfile and purpose-specific UnderstandingProbePlan;
kept explanation, prediction, counterfactual, transfer, intervention and error diagnosis distinct;
made explanatory-depth illusion and jargon/comprehensibility failures operationally explicit;
reconstructed ExpertiseProfile, ExpertiseScopeMap and ExpertiseFreshnessView;
retained expert structural problem-representation/transfer advantages while preserving blind spots and calibration failures;
separated expertise from teaching and reconstructed TeachingCapabilityProfile;
reconstructed TypedCompetenceClaim rather than one competence score;
introduced ExpertiseRoutingView and EpistemicCoverageGap;
handled distributed/team expertise and dependency fragility;
made Human–Agent/Internet knowledge misattribution explicit;
added freshness/version, routing-reflexivity, privacy and normative guards;
and connected the epistemic-competence layer back to HOC1–HOC7.
```

No Foundation reopen condition is triggered.

```text
FoundationReopenCondition(HF0–HF23) = false
NextDeepRoute = UNKNOWN
```

HOC8 does not preselect HOC9.
