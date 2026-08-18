---
schema_version: 1
id: human.operational-concepts.hoc2.sources
title: HOC2 — Epistemic Judgment, Verification, Calibration and Reliance Evidence Ledger
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
summary: Evidence ledger for HOC2. Primary empirical/formal research is used to pressure confidence-versus-accuracy, metacognitive sensitivity, information search, AI confidence cues, reliance and Human–AI metacognitive complementarity. These sources support specific separations; HOC2's full operational grammar remains an Ordivon synthesis constrained by canonical Human Foundations.
evidence_status: verified
readiness: READY
related:
  - human.operational-concepts.hoc2
---
# HOC2 Evidence Ledger

## 1. Pearson et al. — Human reliance on AI versus human guidance

Joe Pearson, Itiel E. Dror, Emma Jayes, Grace-Rose Whordley, Georgina Mason, et al., Sophie Nightingale.
`Examining human reliance on artificial intelligence in decision making.`
Scientific Reports 16, 5345 (2026).
Published 2026-02-05.

Official article:
https://www.nature.com/articles/s41598-026-34983-y

Design:

```text
N = 295
80 real/synthetic face judgments
human or AI guidance
50% correct / 50% incorrect guidance
trial-level confidence
```

Retained pressure:

```text
participants used correct guidance more than incorrect guidance overall;
self-reported always-use of guidance was associated with worse accuracy than selective/non-use groups under a 50%-accurate guidance regime;
positive attitudes toward AI could relate to poorer discriminability in the AI-guidance condition;
confidence and first-order accuracy remain separately measurable.
```

HOC2 use:

```text
Reliance != TrustAttitude
SelectiveReliance matters more than maximum reliance
Source framing/attitude can contaminate epistemic behavior
```

Do not generalize face-classification behavior to all AI domains.

---

## 2. Fregosi et al. — AI confidence calibration and Human reliance

Caterina Fregosi, Lucia Vicente, Andrea Campagner, Federico Cabitza.
`Too Sure for Our Own Good: A User Study on AI Confidence and Human Reliance.`
Proceedings of the AAAI Conference on Artificial Intelligence 40(21), 17445–17453 (2026).
DOI: 10.1609/aaai.v40i21.38798

Official article:
https://ojs.aaai.org/index.php/AAAI/article/view/38798

Design:

```text
within-subject experiment
N = 184
logic puzzles
well-calibrated versus miscalibrated AI confidence cues
```

Retained pressure:

```text
well-calibrated AI confidence cues improved Human decision accuracy more than miscalibrated confidence;
high expressed AI confidence could increase acceptance even when advice was wrong;
miscalibration can induce misuse/overreliance and disuse/conservatism patterns.
```

HOC2 use:

```text
AIConfidenceLevel != AICorrectness
AICalibration materially affects Human reliance
HumanRelianceResponse must be modeled separately from AI confidence
```

---

## 3. Li & Steyvers — joint metacognitive sensitivity

`Modeling the joint impact of human and AI metacognitive sensitivity on human–AI collaboration.`
Journal of Mathematical Psychology 129 (2026), 102988.
DOI: 10.1016/j.jmp.2026.102988

Official article:
https://www.sciencedirect.com/science/article/pii/S0022249626000192

Method:

```text
signal-detection-theoretic formal analysis
Monte Carlo simulation
empirical validation on Human–AI image classification
```

Retained pressure:

```text
metacognitive sensitivity is distinct from calibration;
Human and AI metacognitive sensitivity can determine joint accuracy;
useful uncertainty discrimination can create complementarity even when raw individual accuracy is not maximal.
```

HOC2 use:

```text
AIAccuracy != AIMetacognitiveSensitivity
BestIndividualAccuracy != BestTeamComposition by definition
```

---

## 4. Hu et al. — metacognitive sensitivity and active information search

Xiao Hu, Yahua Li, Xun Chen, Jianyuan Wu, Jingyi Shi, Qi Guo, Yunpeng Liu, Chunliang Yang, Liang Luo.
`Metacognitive sensitivity predicts the quality of information search in value-based decision making.`
Cognition 269 (2026), 106410.
Epub 2025-12-16.
DOI: 10.1016/j.cognition.2025.106410
PMID: 41406863.

PubMed:
https://pubmed.ncbi.nlm.nih.gov/41406863/

Across five experiments (total N=477), metacognitive sensitivity predicted aspects of information-search quality, including sampling and search termination under the studied conditions.

HOC2 use:

```text
metacognition is a control input for what to search and when to stop;
confidence/uncertainty should not be modeled only as post-hoc self-report.
```

Do not infer one universal causal mechanism for all information search.

---

## 5. Fernandes et al. — AI performance versus Human self-monitoring

Daniela Fernandes, Steeven Villa, Salla Nicholls, Otso Haavisto, Daniel Buschek, Albrecht Schmidt, Thomas Kosch, Chenxinran Shen, Robin Welsch.
`AI makes you smarter but none the wiser: The disconnect between performance and metacognition.`
Computers in Human Behavior 175 (2026), 108779.
DOI: 10.1016/j.chb.2025.108779

Publisher record:
https://www.sciencedirect.com/science/article/pii/S0747563225002262
Institutional publication record:
https://research.aalto.fi/en/publications/ai-makes-you-smarter-but-none-the-wiser-the-disconnect-between-pe/

Two large studies examined logical-reasoning performance and self-monitoring under AI assistance. AI-supported performance improved while participants' self-assessment could remain inaccurate/overestimated.

HOC2 use:

```text
JointTaskPerformance != HumanMetacognitiveAccuracy
AI-assisted success does not establish that the Human knows when the joint system is wrong.
```

---

# 6. Internal canonical evidence

HOC2 consumes:

```text
HF3 — metacognition, confidence, calibration, metacognitive sensitivity
HF8 — knowledge, provenance, source/evidence knowledge, understanding
HF9 — judgment, evidence search, causal evidence, AI advice timing, discriminative verification
HF12 — trust, reliance, dependence, Human–AI teaming
HD10-B — measurement/evidence ceilings
HD10-D/E — support-bound capability and scoped projections
HOC1 — readiness, verification bottleneck, uncertainty bottleneck
```

Inherited hard guards include:

```text
Confidence != Accuracy
ConfidenceLevel != Calibration != MetacognitiveSensitivity
Knowledge != CurrentRecall
ReliableSource != AutomaticallyTrueClaim
Judgment != Confidence
CausalJudgment != CausalTruth
Warning != CalibratedTrust
HumanInLoop != ErrorCorrectionGuarantee
Trust != Reliance
ReportedTrust != BehavioralReliance
TrustLevel != TrustCalibration
SituatedCapability != IndependentCapability
```

---

# 7. Evidence ceiling

External studies pressure selected operational distinctions; they do not prove HOC2 as one natural latent construct.

```text
HOC2
= Ordivon operational synthesis
  over multiple distinct evidence-backed constructs.
```

In particular:

```text
VerificationCapability
ReliancePolicy
EvidenceSufficiency
EpistemicRoleProfile
```

must be validated per use case rather than assumed from generic confidence or expertise measures.
