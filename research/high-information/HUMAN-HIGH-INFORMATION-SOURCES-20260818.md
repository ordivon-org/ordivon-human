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


## HF11 / Action / Tool-Integrated Control — Round 3 additions

### Villavicencio, Tsay & de la Malla 2025 — training configuration changes what/how motor adaptation learns

`Target configuration determines how and what we learn during sensorimotor adaptation.`
npj Science of Learning 10, 89 (2025).
https://www.nature.com/articles/s41539-025-00379-2

Used for:

```text
TrainingConfiguration can change explicit/implicit contribution and learned mapping.
SuccessfulAdaptationInOneTrainingGeometry != GenericCorrectControlRepresentation.
```

Supports HF11 + HOC3 context/transfer decomposition rather than a global calibration profile.

---

### Trout et al. 2025 — shared human-machine bionic-hand control

`Shared human-machine control of an intelligent bionic hand improves grasping and decreases cognitive burden for transradial amputees.`
Nature Communications 16, 10418 (2025).
https://www.nature.com/articles/s41467-025-65965-9

Machine control autonomously conformed individual prosthetic digits to contact while Human sEMG input retained proportional grasp regulation. Shared control improved grasping/dexterity measures and reduced cognitive burden under the study conditions.

Used for:

```text
JointPerformanceGain != HumanIndependentControlGain
MachineControlContribution != HumanSkill
Task/GraspControl can be continuously shared.
```

---

### Kang et al. 2025 — online exoskeleton controller adaptation

`Online Adaptation Framework Enables Personalization of Exoskeleton Assistance During Locomotion in Patients Affected by Stroke.`
IEEE Transactions on Robotics 41:4941–4959 (2025).
PMID: 40958952.
https://pubmed.ncbi.nlm.nih.gov/40958952/

The online framework adapted a user-state estimator and reported improved gait-phase estimation/assistance timing after short adaptation.

Used for:

```text
ControllerAdaptation != HumanLearning
DeviceModelImprovement can improve joint performance without equivalent Human-internal change.
```

---

### Campbell et al. 2024/2025 — user-in-loop myoelectric control

`Screen Guided Training Does Not Capture Goal-Oriented Behaviours: Learning Myoelectric Control Mappings From Scratch Using Context Informed Incremental Learning.`
IEEE Transactions on Neural Systems and Rehabilitation Engineering.
PMID: 40030708.
https://pubmed.ncbi.nlm.nih.gov/40030708/

A zero-shot adaptive user-in-the-loop approach achieved higher online throughput despite lower offline classification accuracy than the screen-guided baseline in the reported experiment.

Used for:

```text
OfflineDecoderAccuracy != OnlineHumanToolControlQuality
ModelMetric != JointFunctionalPerformance
```

---

### EDAN assistive robot 2025 — Human command plus shared/whole-body machine control

`An assistive robot that enables people with amyotrophia to perform sequences of everyday activities.`
Scientific Reports (2025).
https://www.nature.com/articles/s41598-025-89405-2

Participants with severe motor impairments used sEMG interfaces plus shared-control templates and whole-body coordination to complete sequences of everyday tasks. Shared control guided/constrained task-relevant motion while users remained command sources; automatic whole-body coordination handled additional degrees of freedom.

Used for:

```text
HumanCommand != HumanLowLevelControl
TaskAuthority != MotorControlContribution
SharedControl != CompleteAutonomyTransfer
```

---

### Reichert et al. 2025 — adaptive assistive-device correction concept

`iAssistADL: Intelligent Assistive Device for Patients with Neurodegenerative Movement Disorder: Concepts and First Implementations.`
IEEE ICORR 2025.
PMID: 40644128.
https://pubmed.ncbi.nlm.nih.gov/40644128/

The proposed system separates intended Human motion from pathological components and applies corrective forces through an assistive device.

Used as a conceptual pressure case for:

```text
HumanActionIntent != RealizedUnassistedMovement
AssistiveCorrection != HumanMotorCapability
```

---

### 2026 robust + online adaptive feedback control

`When Anticipation Is Not Enough: A Mixture of Robust and Adaptive Feedback Control Strategies Improves Reaching in Dynamic Environments.`
PMID: 42150876.
https://pubmed.ncbi.nlm.nih.gov/42150876/

Participants relied on different mixtures of anticipatory, robust and online adaptive control under consistent versus unpredictable force-field environments.

Used for:

```text
MoreFeedforward != BetterControlByDefinition
OnlineCorrectionValue is environment-dependent.
```

---

### Scientific Reports 2026 — online correction and adaptation

`Reinforcement drives within- not between-trial motor adaptation.`
Scientific Reports (2026).
https://www.nature.com/articles/s41598-026-45293-8

Within-trial online correction was associated with lower movement errors and higher adaptation rates than the matched condition without within-trial corrections in the reported paradigm.

Used to establish online correction as performance-relevant while retaining HF11 ownership.

---

### Wang et al. 2025 — sensory-specific online reaching correction

`Functional specialization of the human posterior parietal cortex in visually and proprioceptively driven reaching corrections.`
PMID: 41286340.
https://pubmed.ncbi.nlm.nih.gov/41286340/

Causal TMS evidence distinguished visual- versus proprioceptive-driven online reaching corrections in different posterior parietal regions.

Used to preserve:

```text
OnlineCorrection != one undifferentiated feedback channel.
```

---

### Franchak et al. review — person-plus-object affordances

`A systematic review of perception of affordances for the person-plus-object system.`
PMID: 37407795.
https://pubmed.ncbi.nlm.nih.gov/37407795/

Review of 71 experimental articles on attunement and (re)calibration for person-plus-object affordances.

Used for:

```text
Affordance is Human/object/environment relational.
Attunement and calibration improve with task-relevant experience.
No one intrinsic Human affordance score.
```

---

### Bertuccelli et al. 2025 — exoskeleton embodiment as one integration dimension

`Quantitative assessment of human-exoskeleton integration through a neurophysiological marker of embodiment.`
Scientific Reports (2025).
PMID: 41444771.
https://pubmed.ncbi.nlm.nih.gov/41444771/

Used to pressure dimension-specific Human-device integration:

```text
Embodiment/BodyRepresentationIntegration != ControlIntegration != CapabilityIntegration.
```

---

### Hou et al. 2025 — prosthetic control as cooperative adaptation

`Prosthetic Control by Learning: A Multi-Agent Cooperative Game Framework.`
IEEE ICORR 2025.
PMID: 40644202.
https://pubmed.ncbi.nlm.nih.gov/40644202/

Simulator-based framework models Human and powered prosthesis as reciprocally adapting controllers.

Used as an Agent-era conceptual pressure case:

```text
JointControllerAdaptation may occur on both Human and device sides;
one observed trajectory does not identify which side changed.
```


## HF23 / Language / Symbolic Practical — Round 4 additions

### Imai et al. 2025 — VLM common-ground metrics

`Measuring How (Not Just Whether) VLMs Build Common Ground.`
RANLP 2025.
ACL Anthology: https://aclanthology.org/2025.ranlp-1.53/

Interactive referential-game evaluation across 150 self-play sessions compared multiple VLMs with Human dyads using grounding efficiency, content alignment, lexical adaptation and Human-likeness metrics.

Used for:

```text
TaskSuccess != SuccessfulGrounding
ImageUtteranceAlignment != TaskSuccess
Fluency != HumanLikeCommonGroundProcess
```

Supports HOC6 common-ground ownership rather than a new language HOC.

---

### Zeng et al. 2026 — LVLMs and Humans ground differently

`LVLMs and Humans Ground Differently in Referential Communication.`
ACL 2026 Long Papers.
ACL Anthology: https://aclanthology.org/2026.acl-long.410/

Factorial director–matcher experiments included Human–Human, Human–AI, AI–Human and AI–AI pairs in repeated referential tasks.

Used for:

```text
ReferenceTaskSuccess != HumanLikeGrounding
CommonGroundDynamics are participant/configuration dependent.
```

---

### Wang et al. 2025 — overhearing does not guarantee common-ground adaptation

`LVLMs are Bad at Overhearing Human Referential Communication.`
EMNLP 2025.
ACL Anthology: https://aclanthology.org/2025.emnlp-main.849/

Seven LVLMs overheard repeated Human referential conversations; models did not consistently improve from accumulating those observations.

Used for:

```text
DialogueHistoryAccess != InteractiveGrounding
ObservedConvention != AcquiredPartnerSpecificReferencePolicy
```

---

### Shayegh et al. 2025 — adequacy/fluency translation tradeoff

`Feeding Two Birds or Favoring One? Adequacy–Fluency Tradeoffs in Evaluation and Meta-Evaluation of Machine Translation.`
WMT 2025.
ACL Anthology: https://aclanthology.org/2025.wmt-1.16/

Used for:

```text
TranslationQuality != OneObjectiveFreeScalar
Adequacy != Fluency
MetricRanking depends on evaluation emphasis.
```

---

### Choudhary et al. 2025 — discourse-aware translation context

`Exploring Context Strategies in LLMs for Discourse-Aware Machine Translation.`
Findings of EMNLP 2025.
ACL Anthology: https://aclanthology.org/2025.findings-emnlp.1324/

Context strategies changed translation and discourse-specific performance including formality, pronoun selection and lexical cohesion.

Used for:

```text
SentenceLocalAdequacy != DiscourseTranslationTotality
ContextFreeTranslation != ContextAppropriateTranslation
```

---

### Niklaus et al. 2025 — Swiss legal translation benchmark

`SwiLTra-Bench: The Swiss Legal Translation Benchmark.`
ACL 2025 Long Papers.
ACL Anthology: https://aclanthology.org/2025.acl-long.725/

Over 180K aligned multilingual legal translation pairs span laws, headnotes and press releases, with Human expert validation.

Used for:

```text
TranslationPerformance is document/domain dependent.
LegalTranslation requires domain-specific verification/force constraints.
```

---

### Ki & Carpuat 2025 — rewriting can improve translation while preserving meaning

`Automatic Input Rewriting Improves Translation with Large Language Models.`
NAACL 2025 Long Papers.
ACL Anthology: https://aclanthology.org/2025.naacl-long.542/

Input simplification improved translation in the studied settings; Human evaluation checked source/rewrite/translation meaning preservation.

Used as a transformation pressure case:

```text
RewriteForTranslatability
!= RewriteForHumanComprehensionByDefinition
TransformationObjective must be declared.
```

---

### Gaines & Vertanen 2025 — LLM prediction for AAC

`Adapting Large Language Models for Character-based Augmentative and Alternative Communication.`
Findings of EMNLP 2025.
ACL Anthology: https://aclanthology.org/2025.findings-emnlp.826/

Character prediction adapted subword LLMs for AAC input and improved prediction accuracy under the reported evaluation.

Used for:

```text
PredictionEfficiencyGain != HumanLanguageCapabilityGain
AACModelPerformance != HumanAuthorship
```

---

### Fried-Oken et al. 2025 — partner-suggested AAC vocabulary with Human selection

`Smart Predict: adding partner-suggested vocabulary to increase efficiency in a dual tablet AAC typing application.`
Augmentative and Alternative Communication.
PMID: 39164980.
https://pubmed.ncbi.nlm.nih.gov/39164980/

The dual-device design allows a partner to supplement vocabulary while the AAC user retains control to choose words.

Used for:

```text
PartnerSuggestion != HumanChoice
SupportCanImproveEfficiency without transferring message ownership.
```

---

### Choudhury, Kumar & Martin 2025 — Human–LLM representation alignment in AAC

`Evaluating Human-LLM Representation Alignment: A Case Study on Affective Sentence Generation for Augmentative and Alternative Communication.`
Findings of IJCNLP-AACL 2025.
ACL Anthology: https://aclanthology.org/2025.findings-ijcnlp.100/

Human judgments differed depending on how affective concepts were represented to the model.

Used for:

```text
MachineRepresentation != HumanExpectedMeaning
GeneratedSentence != HumanEndorsedExpression
```

---

### Holyfield et al. 2025 — context-aware just-in-time AAC response options

`Preliminary Investigation of Context-Aware Augmentative and Alternative Communication with Automated Just-in-Time Cloze Phrase Response Options for Social Participation from Children on the Autism Spectrum.`
PMID: 39467532.
https://pubmed.ncbi.nlm.nih.gov/39467532/

Used as a pressure case for adaptive symbolic support while preserving:

```text
AdaptiveInterfaceSupport != HumanInternalLanguageChange
```

---

### Kent-Walsh et al. 2025 — AAC language intervention RCT

`Generative Language Intervention for Young Children With Down Syndrome Using Augmentative and Alternative Communication: A Randomized Controlled Trial.`
PMID: 40587257.
https://pubmed.ncbi.nlm.nih.gov/40587257/

Used to preserve the distinction between:

```text
AAC as current communication support
and
AAC-supported language learning/change
```

with HOC3 owning learning/transfer claims.

---

### SALT-31 2026 — discourse/pragmatic multilingual translation pressure

`SALT-31: A Machine Translation Benchmark Dataset for 31 Ugandan Languages.`
AfricaNLP 2026.
ACL Anthology: https://aclanthology.org/2026.africanlp-main.21/

Scenario-driven mini-dialogues preserve discourse context, pragmatics and culturally grounded communication patterns across 31 Ugandan languages.

Used for:

```text
TranslationEvaluation must preserve discourse/pragmatic/cultural coordinates where relevant.
```
