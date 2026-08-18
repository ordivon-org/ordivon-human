---
schema_version: 1
id: human.high-information.sources.20260818
profile: research
lifecycle: active-search
source_role: evidence-index
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
updated: 2026-08-18
summary: External evidence index for the Human high-information / underexplored-space search after HOC0–HOC10 closeout. Sources are selected to pressure active perceptual sampling, sampling costs/stopping, sensory substitution, controller attribution, affordance/tool calibration and subsequent high-information spaces. The index is not a roadmap and source inclusion does not imply HOC admission.
evidence_status: verified
readiness: ACTIVE
---
# Human High-Information Search — Evidence Index

## HF20 / Active Sampling / Perceptual Calibration

### Akar, Deschamps & Roy 2025 — sensory-substitution exploration strategy

`Exploration strategies influence visual-auditory sensory substitution in a passive guidance setup.`
Acta Psychologica 260:105619.
DOI: 10.1016/j.actpsy.2025.105619.
PubMed: https://pubmed.ncbi.nlm.nih.gov/41014930/

Pressure used:

```text
same sensory-substitution device
+ different exploration guidance/policy
→ different accuracy/confidence and later active-exploration performance
```

Supports strategy relevance, but not unique Human ownership.

---

### Chen et al. 2025 — head movement and sound localization under single-sided deafness

`The role of head movement in sound localization compensation in individuals with single-sided deafness.`
Hearing Research 467:109409.
DOI: 10.1016/j.heares.2025.109409.
PubMed: https://pubmed.ncbi.nlm.nih.gov/40882584/

Pressure used:

```text
head movement allowed
→ improved localization accuracy
→ especially strong benefit in some SSD conditions
→ longer reaction time / extra effort
```

Supports active-sensing benefit/cost tradeoff.

---

### Petitet et al. 2021 — computational cost of active information sampling

`The computational cost of active information sampling before decision-making under uncertainty.`
Nature Human Behaviour 5:935–946.
DOI: 10.1038/s41562-021-01116-6.
https://www.nature.com/articles/s41562-021-01116-6

Five experiments showed a speed–efficiency tradeoff in active sampling and supported an additional cognitive-effort cost related to accumulated fatigue.

Used for:

```text
InformationGainMaximization != HumanSamplingObjective
MoreSampling != Free
```

---

### Juni, Gureckis & Maloney 2016 — explicit sampling cost and stopping

`Information sampling behavior with explicit sampling costs.`
Decision.
PMCID: PMC4942190.
https://pmc.ncbi.nlm.nih.gov/articles/PMC4942190/

Participants repeatedly chose whether to sample another perceptual cue or stop and act; additional samples improved expected accuracy but reduced reward. Participants over-sampled in one condition.

Used for:

```text
MoreSamples != BetterPolicy
Stopping is a cost/value decision.
```

---

### Ahmad & Yu 2014 — cost-sensitive active sensing control

`Cost-sensitive Bayesian control policy in human active sensing.`
Frontiers in Human Neuroscience 8:955.
PMCID: PMC4253738.
https://pmc.ncbi.nlm.nih.gov/articles/PMC4253738/

Models Human active sensing as sequential decisions among continuing, switching sensing location and stopping, with time/switch/error costs.

Used as formal pressure that sampling policy naturally composes inference + action + cost/stopping rather than requiring a Human trait.

---

### Active vs passive touch roughness study

`Active and passive touch differentially activate somatosensory cortex in texture perception.`
PMID: 20669167.
https://pubmed.ncbi.nlm.nih.gov/20669167/

Active and passive exploration showed different neural activation but no task-performance difference in the controlled roughness categorization task.

Used as direct falsifier of:

```text
Active > Passive
ActiveMovement -> BetterPerception
```

---

### Control over sampling / stopping

`Control over sampling boosts numerical evidence processing in human decisions from experience.`
PMID: 35266973.
https://pubmed.ncbi.nlm.nih.gov/35266973/

Used to distinguish control over stopping from control over which alternative to sample; supports treating stopping/decision control as an operational variable already compatible with HOC2/HOC5.

---

### Xiong et al. 2025 — robot active perception learned from Human demonstrations

`Vision in Action: Learning Active Perception from Human Demonstrations.`
arXiv:2506.15666.
https://arxiv.org/abs/2506.15666

The robot learns task-relevant search/tracking/focusing and active neck/camera actions from Human demonstrations and can execute an Agent-owned active-perception policy.

Used for:

```text
SamplingPolicy != HumanProperty
LearnedFromHuman != CurrentlyOwnedByHuman
AgentSelectedView != HumanActiveSampling
```

---

## HF11 / Tool / Affordance / Calibration pressure

### Day et al. 2017 — calibration to tool use during reaching

`Calibration to tool use during visually-guided reaching.`
Acta Psychologica 181:27–39.
PMID: 29040934.
https://pubmed.ncbi.nlm.nih.gov/29040934/

Participants calibrated reaching appropriately to the tool used during feedback/training, with carryover to post-test reaches.

Used to route action-boundary/tool calibration primarily to HF11.

---

### Franchak 2020 — calibration transfer can fail

`Calibration of perception fails to transfer between functionally similar affordances.`
Quarterly Journal of Experimental Psychology 73(9):1311–1325.
PMID: 32538309.
https://pubmed.ncbi.nlm.nih.gov/32538309/

Calibration for one doorway-passage affordance did not necessarily transfer to another functionally similar affordance when informational requirements differed.

Used for:

```text
CalibrationInTaskA != CalibrationInTaskB
NoGlobalCalibrationScore
```

---

### Franchak 2019 — development of affordance recalibration

`Development of affordance perception and recalibration in children and adults.`
Journal of Experimental Child Psychology.
PMID: 30870696.
https://pubmed.ncbi.nlm.nih.gov/30870696/

Body modification with a backpack created a need to recalibrate doorway-passage judgments; recalibration and risk biases varied developmentally.

Used as developmental pressure on action-boundary calibration.

---

### Withagen & Michaels 2005 — attunement vs calibration

`The role of feedback information for calibration and attunement in perceiving length by dynamic touch.`
JEP:HPP 31(6):1379–1390.
PMID: 16366796.
https://pubmed.ncbi.nlm.nih.gov/16366796/

Different feedback could produce recalibration and/or reattunement, supporting HF11's distinction:

```text
Attunement != Calibration
```

---

### Tool-induced tactile recalibration

`The recalibration of tactile perception during tool use is body-part specific.`
PMID: 28702834.
https://pubmed.ncbi.nlm.nih.gov/28702834/

Tool use recalibrated tactile distance perception on the tool-using hand but not cheek, supporting dimension/body-part specificity rather than global recalibration.
