---
schema_version: 1
id: human.operational-concepts.hoc3.sources
title: HOC3 — Learning, Retention, Transfer, Modifiability and Scaffolding Evidence Ledger
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
summary: Evidence ledger for HOC3. Primary experimental and field evidence is used to pressure immediate performance versus delayed retention, retrieval/testing effects, transfer, fluency misprediction, interleaving/spacing, feedback, and AI support/scaffolding versus independent learning. These sources support specific operational separations; HOC3's full grammar remains an Ordivon synthesis constrained by canonical Human Foundations.
evidence_status: verified
readiness: READY
related:
  - human.operational-concepts.hoc3
---
# HOC3 Evidence Ledger

## 1. Roediger & Karpicke 2006 — retrieval/testing versus restudy

Henry L. Roediger III, Jeffrey D. Karpicke.
`Test-enhanced learning: Taking memory tests improves long-term retention.`
Psychological Science. 2006;17(3):249–255.
DOI: 10.1111/j.1467-9280.2006.01693.x
PMID: 16507066.

PubMed:
https://pubmed.ncbi.nlm.nih.gov/16507066/

Design pressure:

```text
students studied prose passages;
conditions included repeated testing without feedback versus repeated study;
final tests occurred after 5 minutes, 2 days or 1 week.
```

Retained evidence:

```text
repeated study could improve immediate performance;
repeated testing produced stronger delayed retention in the studied conditions;
repeated study could also increase confidence despite poorer delayed retention.
```

HOC3 use:

```text
ImmediatePracticePerformance != DelayedRetention
SubjectiveConfidence/Fluency != DurableLearning
RetrievalProbe can be both measurement and intervention
```

Do not infer universal superiority of testing for every target.

---

## 2. Butler 2010 — retrieval and transfer

Andrew C. Butler.
`Repeated testing produces superior transfer of learning relative to repeated studying.`
Journal of Experimental Psychology: Learning, Memory, and Cognition. 2010;36(5):1118–1133.
DOI: 10.1037/a0019902
PMID: 20804289.

PubMed:
https://pubmed.ncbi.nlm.nih.gov/20804289/

Four experiments compared repeated testing with repeated study and assessed delayed retention/transfer, including new inferential questions.

Retained pressure:

```text
retrieval practice effects can extend beyond exact practiced responses under some conditions;
transfer must still be measured rather than assumed.
```

HOC3 use:

```text
TransferSurface is a first-class learning outcome.
```

---

## 3. Kornell & Bjork 2008 — interleaving/spacing and metacognitive preference

Nate Kornell, Robert A. Bjork.
`Learning concepts and categories: Is spacing the "enemy of induction"?`
Psychological Science. 2008;19(6):585–592.
DOI: 10.1111/j.1467-9280.2008.02127.x
PMID: 18578849.

PubMed:
https://pubmed.ncbi.nlm.nih.gov/18578849/

Participants learned artist/category exemplars under massed versus interleaved/spaced presentation and were later tested on new exemplars.

Retained evidence:

```text
interleaved/spaced presentation improved induction in the studied paradigm;
participants nevertheless tended to judge massed practice as more effective.
```

HOC3 use:

```text
Preferred/EasierPractice != MostEffectiveLearningProtocol
PracticeDifficulty != LearningValue by definition
```

Do not generalize the exact interleaving effect to every domain; later work shows mechanism/outcome dependence.

---

## 4. Pashler et al. 2005 — feedback after errors and delayed retention

Harold Pashler, Nicholas J. Cepeda, John T. Wixted, Doug Rohrer.
`When does feedback facilitate learning of words?`
Journal of Experimental Psychology: Learning, Memory, and Cognition. 2005;31(1):3–8.
DOI: 10.1037/0278-7393.31.1.3
PMID: 15641900.

PubMed:
https://pubmed.ncbi.nlm.nih.gov/15641900/

In a Luganda–English word-pair experiment, corrective feedback after incorrect responses substantially improved later retention under the studied protocol.

HOC3 use:

```text
PracticeError != LearningFailure
Feedback design/timing is part of the learning protocol
```

Do not infer one feedback rule for all skills/domains.

---

## 5. Bastani et al. 2025 — AI support versus independent learning

Hamsa Bastani, Osbert Bastani, Alp Sungu, Haosen Ge, Özge Kabakcı, Rei Mariman.
`Generative AI without guardrails can harm learning: Evidence from high school mathematics.`
Proceedings of the National Academy of Sciences. 2025;122(26):e2422633122.
DOI: 10.1073/pnas.2422633122
PMID: 40560616.

Official article:
https://doi.org/10.1073/pnas.2422633122

Large randomized field experiment using GPT-4-based support during mathematics practice with subsequent unaided testing.

Retained pressure:

```text
AI access can substantially raise supported practice performance;
standard answer-oriented support need not raise later unaided performance and can harm it under the studied design;
pedagogically guardrailed support can change this learning effect.
```

HOC3 use:

```text
AssistedPerformanceGain != IndependentLearningGain
SupportPolicy is part of the learning intervention
```

Do not generalize the direction/magnitude to every domain or Agent design.

---

## 6. Wang et al. — Tutor CoPilot field RCT

Rose E. Wang, Ana T. Ribeiro, Carly D. Robinson, Susanna Loeb, Dora Demszky.
`Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise.`
EdWorkingPaper / Stanford SCALE research release; study reported 2024–2025.

Primary preprint:
https://arxiv.org/abs/2410.03017
Stanford SCALE record:
https://scale.stanford.edu/publications/tutor-copilot-human-ai-approach-scaling-real-time-expertise

Randomized live-tutoring deployment involving hundreds of tutors and over a thousand K–12 students in the reported analysis.

Retained pressure:

```text
AI support can act through the Human tutor rather than replace the tutor;
access to expert-like in-the-moment guidance improved student topic mastery in the reported trial;
tutors with support used more pedagogically useful moves such as guiding questions and less direct answer-giving.
```

HOC3 use:

```text
Agent support can scaffold Human teaching behavior;
support design changes the practice environment experienced by another Human.
```

Evidence is domain/deployment-specific and should not be treated as universal AI-tutoring proof.

---

# 7. Internal canonical evidence

HOC3 consumes:

```text
HF6 — learning / adaptation / retention / transfer / development
HF7 — memory / retrieval / forgetting / interference / generalization
HF8 — knowledge / understanding
HF11 — skill / execution / feedback / tool support
HD4 — social learning / teaching / cultural transmission
HD10-D — dynamic assessment / modifiability / capability surfaces
HD10-E — trajectory/support projections
HOC1 — capability / readiness / bottleneck / support removal
HOC2 — confidence / calibration / verification / evidence search
```

Inherited hard guards include:

```text
PracticePerformance != RetainedLearning
Acquisition != Retention
Retention != Transfer
MorePractice != MoreTransfer
JointPerformanceGain != HumanInternalLearningGain
CurrentPerformance != ModifiabilityProfile
ExternalAnswerAccess != InternalKnowledge
AIAssistedAnswer != HumanUnderstanding
CurrentPerformance != Skill
BareHumanCapability != HumanToolSystemCapability
```

---

# 8. Evidence ceiling

The cited studies establish specific effects under specific targets, protocols and populations.
They do not justify a universal learning algorithm.

```text
HOC3
= Ordivon operational synthesis
  + scoped empirical operators
  + explicit uncertainty/transport boundaries.
```

`NextBestLearningAction`, `ScaffoldingPolicy`, `LearningProgressView` and `SupportDependenceTrajectory` must be calibrated in each real consumer rather than assumed from the labels alone.
