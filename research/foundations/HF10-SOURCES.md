---
schema_version: 1
id: human.foundations.hf10.sources
title: HF10 External Evidence and Source Ledger
type: evidence
profile: research
lifecycle: active
source_role: supporting
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
updated: 2026-08-17
summary: Primary, review and replication-sensitive evidence used to reconstruct decision, choice, planning, strategy, exploration/exploitation, information search, stopping, commitment, sunk cost, uncertainty and Human×AI delegation boundaries.
evidence_status: verified
readiness: READY
applies_to:
  - HUMAN-FOUNDATIONS-001
  - HF10
related:
  - human.foundations.hf10
  - human.foundations.hf9.sources
---
# HF10 External Evidence and Source Ledger

## Evidence rule

HF10 studies how provisional judgments and candidate options become temporally
organized action policies. Every result is interpreted by separating:

```text
option generation / option set
representation / frame / reference
preference / current value estimate
information state and acquisition mode
choice / commitment / execution
planning model / horizon / subgoals
search / stopping / switching
risk / ambiguity / unknown structure
external aid / delegation / authority
normative objective and cost model
```

No observed choice is treated as direct access to a stable `true preference`.

---

# 1. Risky-choice framing and preference reversals

## Tversky & Kahneman (1981)

- PMID: 7455683
- DOI: 10.1126/science.7455683
- HF10 use: formally equivalent descriptions can produce systematic preference
  reversals; representation/reference framing is a causal part of choice.

## Kühberger (1998) meta-analysis

- PMID: 9719656
- DOI: 10.1006/obhd.1998.2781
- HF10 use: framing is reliable but effect size depends materially on design,
  response mode, reference-point versus salience manipulation and domain.

## Kühberger (2023) systematic review

- PMID: 37927347
- PMCID: PMC10620856
- DOI: 10.17179/excli2023-6169
- HF10 use: current synthesis rejecting the interpretation that framing effects are
  one simple irrationality marker; different theory families explain different
  variants.

## matched-description replication/extension (2026)

- PMID: 41979840
- PMCID: PMC13079499
- DOI: 10.3758/s13423-025-02771-w
- HF10 use: risky-choice framing persists under more carefully matched descriptions
  while valence/gist explains substantial variance.

### HF10 inference

```text
ObservedChoice != StablePreferenceReadout
FrameEffect != OneMechanismProof
DescriptionInvarianceFailure != UniqueIrrationalityDiagnosis
```

---

# 2. Description versus experience

## Hertwig et al. review — description-experience gap

- PMID: 19836292
- HF10 use: rare events often receive different behavioral weighting when outcomes
  are learned from experience rather than described.

## Madan et al. (2019) comparative program

- PMID: 30611852
- DOI: 10.1016/j.beproc.2018.12.009
- HF10 use: risky choices differ under description and experience, with memory and
  sampling processes contributing to the difference.

## Spicer et al. (2026)

- PMID: 42098277
- DOI: 10.1038/s44271-026-00467-y
- HF10 use: generated possible gamble outcomes show biased mental sampling and
  sequential dependencies that predict subsequent risky choice.

### HF10 inference

```text
NominalOutcomeDistribution
+ DifferentAcquisitionHistory
→ DifferentChoicePolicy

DescriptionChoice != ExperienceChoice
GeneratedPossibilities != ObjectiveDistribution
```

---

# 3. Risk and ambiguity

## ambiguity-effect experiments

- PMID: 10519925
- HF10 use: unknown probabilities can be avoided even when nominal alternatives
  otherwise match; ambiguity must not be collapsed into known risk.

## risk/ambiguity neuroimaging meta-analysis

- PMID: 33940147
- DOI: 10.1016/j.neuroimage.2021.118109
- HF10 use: overlapping and distinguishable processing across risky versus
  ambiguous decisions; supports typed uncertainty rather than one scalar.

## ambiguity × framing

- PMID: 25030206
- DOI: 10.3758/s13423-014-0688-0
- HF10 use: ambiguity and framing jointly alter choice; uncertainty type and frame
  are distinct variables.

### HF10 inference

```text
Risk != Ambiguity
KnownProbability != UnknownProbability
UncertaintyType_D != UncertaintyType_E
```

---

# 4. Regret and counterfactual outcome comparison

## Coricelli et al. (2005)

- PMID: 16116457
- DOI: 10.1038/nn1514
- HF10 use: feedback about unchosen outcomes induces regret and changes subsequent
  gamble choice; anticipated regret can become a policy input.

## risky-degree boundary (2021)

- PMID: 33719048
- HF10 use: experienced-regret effects on later risky choice reversed across low
  versus high risk conditions in the reported experiments.

## anticipated-regret experiments (2025)

- PMID: 41020099
- PMCID: PMC12460334
- DOI: 10.3389/fpsyg.2025.1667136
- HF10 use: anticipated regret altered risk-taking/satisfaction with effects
  moderated by time pressure in the reported tasks.

### HF10 inference

```text
Regret != RiskAversion
AnticipatedRegret != ExperiencedRegret
RegretEffect_D != RegretEffect_E
```

---

# 5. Information value is plural

## Pierson & Goodman (2014)

- PMID: 25426631
- PMCID: PMC4245129
- DOI: 10.1371/journal.pone.0113342
- HF10 use: people value information even when it has no obvious instrumental
  decision use; uncertainty resolution has subjective value.

## choice increases noninstrumental information value

- PMID: 33888764
- PMCID: PMC8062497
- DOI: 10.1038/s41598-021-88031-y
- HF10 use: self-choice increased preference for later outcome information beyond
  estimated win probability.

## neural information-seeking review (2024)

- PMID: 38703774
- DOI: 10.1016/j.neuron.2024.04.008
- HF10 use: current synthesis supports multiple drivers of information seeking,
  including instrumental and noninstrumental value.

### HF10 inference

```text
InformationValue
!= ExpectedActionImprovementOnly
```

Use a profile including instrumental, uncertainty-reduction and affective value.

---

# 6. Information avoidance

## Meese, Hua & Howell (2024)

- PMID: 39013284
- DOI: 10.1016/j.socscimed.2024.117065
- HF10 use: health-information avoidance can participate in a broader self-
  protective strategy and substitute for reactive derogation.

## daily-diary study (2025)

- PMID: 40445104
- DOI: 10.1111/aphw.70045
- HF10 use: information avoidance varied substantially within people across days
  and related to negative affect/self-efficacy.

### HF10 inference

```text
AvailableInformation != SoughtInformation
InformationAvoidance != IgnoranceByDefinition
MoreInformation != AlwaysPreferred
```

---

# 7. Metacognition and information search

## metacognitive sensitivity and search quality (2025)

- PMID: 41406863
- DOI: 10.1016/j.cognition.2025.106410
- HF10 use: more accurate uncertainty monitoring predicted better information
  search in value-based decision tasks.

## confidence and information seeking (2025)

- PMID: 40517523
- DOI: 10.1016/j.cognition.2025.106219
- HF10 use: causal manipulations show confidence and information-seeking relations
  are context/manipulation-sensitive rather than one monotonic law.

### HF10 inference

```text
Confidence != SearchPolicy
MetacognitiveSensitivity can support SearchPolicy
```

---

# 8. Exploration and exploitation

## Wilson et al. (2014)

- PMID: 25347535
- PMCID: PMC5635655
- DOI: 10.1037/a0038199
- HF10 use: horizon manipulation supports separable directed information-seeking
  and random-exploration components.

## information/randomization review

- PMID: 33184605
- HF10 use: synthesizes directed exploration, random exploration and computational
  distinctions in human bandit behavior.

## observational learning of explore/exploit policy (2025)

- PMID: 40117983
- DOI: 10.1016/j.cognition.2025.106124
- HF10 use: observed agents' behavior changes Human explore/exploit choices;
  exploration policy is socially learnable.

## selective maintenance and resource rationality

- PMID: 30502584
- HF10 use: selective compression of value information can outperform more
  resource-intensive uncertainty-directed strategies in some learnable environments.

### HF10 inference

```text
Exploration != RandomChoice
DirectedExploration != RandomExploration
Exploitation != OptimalityByDefinition
MoreExploration != BetterLearningByDefinition
```

---

# 9. Stopping information search

## O'Bryan et al. (2018)

- PMID: 29410293
- DOI: 10.1016/j.neuroimage.2018.01.084
- HF10 use: self-paced category learning explicitly separates continued sampling
  from stopping to commit a rule; stopping relates to rule activation/confidence.

## current information-search metacognition evidence

- PMID: 41406863
- HF10 use: uncertainty monitoring predicts search quality before final choice.

### HF10 inference

```text
SearchPolicy != StoppingRule
Stopping != Failure
Stopping is a decision under remaining uncertainty and cost
```

---

# 10. Satisficing / bounded search

## Gigerenzer et al. précis (2001)

- PMID: 11301545
- HF10 use: fast-and-frugal heuristics can explicitly contain search, stopping and
  decision rules; satisficing is a bounded strategy rather than synonymous with
  defective optimization.

### HF10 inference

```text
Satisficing != IrrationalityByDefinition
StoppingAtThreshold != FailureByDefinition
```

---

# 11. Option generation is a distinct decision stage

## Kalis, Kaiser & Mojzisch (2013)

- PMID: 23986737
- PMCID: PMC3750205
- DOI: 10.3389/fpsyg.2013.00555
- HF10 use: decision research usually assumes options are externally given, but
  real decisions often require generating the option set first.

## Del Missier et al. (2015)

- PMID: 25657628
- PMCID: PMC4302792
- DOI: 10.3389/fpsyg.2014.01584
- HF10 use: ideation contributes to option generation beyond memory retrieval;
  generating more options can raise maximum quality while reducing average quality.

## latent-variable option-generation study

- PMID: 30264544
- HF10 use: everyday option generation has partly distinct cognitive predictors.

## task-design boundary (2025)

- PMID: 40166816
- DOI: 10.1111/sjop.13112
- HF10 use: quantity-breeds-quality, less-is-more and Take-The-First patterns depend
  on task design; no one option-generation heuristic is universal.

### HF10 inference

```text
OptionGeneration != OptionEvaluation
OptionGeneration != MemoryRetrievalOnly
MoreGeneratedOptions != MonotonicChoiceQuality
```

---

# 12. Choice overload is conditional

## Iyengar & Lepper (2000)

- PMID: 11138768
- DOI: 10.1037//0022-3514.79.6.995
- HF10 use: classic demonstrations that larger choice sets can reduce uptake and
  satisfaction under some contexts.

## motivational choice-overload study

- PMID: 30951804
- DOI: 10.1016/j.biopsycho.2019.03.010
- HF10 use: many options can increase engagement/value while also increasing threat
  relative to perceived decision resources.

## 2024 qualitative review

- PMID: 38784631
- PMCID: PMC11111947
- DOI: 10.3389/fpsyg.2024.1290359
- HF10 use: overload is moderated by decision task, context and chooser
  characteristics.

### HF10 inference

```text
MoreOptions != AlwaysBetter
MoreOptions != AlwaysWorse
ChoiceOverload != UniversalOptionCountLaw
```

---

# 13. Sunk cost and escalation of commitment

## Garland & Conlon (1998/2001 record)

- PMID: 11302222
- DOI: 10.1037/0021-9010.86.1.104
- HF10 use: sunk cost and proximity/completion exert separable and interacting
  pressures on continued commitment.

## escalation with transparent future outcomes

- PMID: 15779532
- HF10 use: escalation can persist even when future returns and alternatives are
  explicitly presented, challenging purely informational explanations.

## spent and remaining cost (2022)

- PMID: 36474069
- HF10 use: change-of-mind sunk-cost sensitivity reflects both time already spent
  and time remaining; information presented about these dimensions matters.

## responsibility / preference / framing (2023)

- PMID: 36710742
- HF10 use: personal responsibility, initial preference and loss framing jointly
  alter reinvestment/escalation and premature abandonment.

## social signaling (2021)

- PMID: 34472961
- PMCID: PMC9354500
- DOI: 10.1037/xge0001101
- HF10 use: escalating commitment can signal trustworthiness to others in some
  social contexts, making persistence potentially socially instrumental.

## self/other sunk cost (2024)

- PMID: 39504839
- DOI: 10.1016/j.actpsy.2024.104557
- HF10 use: sunk-cost effects vary with whose resources are at stake and whether
  the participant decides, predicts or advises.

### HF10 inference

```text
SunkResource != RemainingCost
SunkCostEffect != OneBiasMechanism
PersistenceAfterSunkCost != IrrationalByDefinition
Completion / responsibility / signaling / switching may matter
```

---

# 14. Precommitment changes future option architecture

## Studer et al. (2019)

- PMID: 30966912
- HF10 use: removing an easy smaller reward in advance increased attainment of an
  effortful larger reward; computational comparison favored a motivation-
  maximization account over the tested willpower account.

## subjective cost of self-control

- PMID: 34446546
- PMCID: PMC8536396
- DOI: 10.1073/pnas.2018726118
- HF10 use: Humans will pay to avoid future self-control demands, supporting the
  value of changing future choice architecture.

## revocable precommitment (2024)

- PMID: 39657992
- PMCID: PMC11642602
- DOI: 10.1093/scan/nsae093
- HF10 use: revocable commitment can still reduce impulsive smaller-sooner choices;
  commitment need not equal absolute irreversibility.

## soft/uncommitted commitment pilot

- PMID: 32440646
- PMCID: PMC7198673
- DOI: 10.1007/s40614-019-00229-8
- HF10 use: repeated soft commitment was explored as a way to reduce temporal
  preference reversal.

### HF10 inference

```text
Precommitment != MoreWillpower
Commitment != Irreversibility
OptionRestriction can increase long-horizon goal control
```

---

# 15. Model-based and model-free sequential choice

## Daw et al. (2011)

- PMID: 21435563
- HF10 use: multistep task distinguished model-based transition-sensitive and
  model-free reward-history influences; both contributed to Human choices.

## reliability boundary

- PMID: 30759077
- HF10 use: common two-step measures have limited reliability under conventional
  designs; model-based/model-free labels require measurement caution.

## task complexity/state uncertainty

- PMID: 31844060
- HF10 use: environmental uncertainty and complexity change relative advantages and
  Human use of model-based versus model-free control.

## environmental-demand arbitration (2026)

- PMID: 41083652
- DOI: 10.3758/s13415-025-01350-9
- HF10 use: Humans can learn to alter model-based/model-free reliance in response
  to environmental demands rather than possessing one fixed balance.

### HF10 inference

```text
Planning != ModelBasedScalar
ModelBased != PurelyGood
ModelFree != PurelyBad
PlanningPolicy is resource/environment sensitive
```

---

# 16. Depth-limited and hierarchical planning

## Keramati et al. / plan-until-habit (2016)

- PMID: 27791110
- HF10 use: Human planning can simulate only to limited depth and integrate cached
  values thereafter; time pressure reduces planning depth.

## hierarchical action sequences

- PMID: 24339762
- DOI: 10.1371/journal.pcbi.1003364
- HF10 use: goal-directed control can select learned action sequences; flat
  model-free versus model-based decomposition is not the only viable architecture.

## hierarchical planning fMRI (2022)

- PMID: 35709949
- HF10 use: virtual navigation supports hierarchical planning with higher/lower
  level organization.

## subgoal representation in model-based hierarchy (2026)

- PMID: 41690311
- DOI: 10.1016/j.neuron.2025.12.023
- HF10 use: sequential subgoals are represented/valued during hierarchical,
  model-based behavior; planning depends on latent subgoal structure.

## planning algorithms review (2025)

- PMID: 40617759
- DOI: 10.1016/j.tics.2025.06.006
- HF10 use: contemporary synthesis of tree-search and resource-rational methods for
  long-horizon Human planning; retained as theory map rather than ontology.

### HF10 inference

```text
Plan != SingleAction
Planning != FullHorizonExhaustiveSearch
PlanningDepth != PlanningExistence
Subgoal != FinalGoal
PlanStructure can be hierarchical
```

---

# 17. Strategy, plan and policy are distinct

HF10 uses the above planning/search evidence to motivate a structural distinction:

```text
Policy = mapping from represented states/information to action distribution
Plan = represented prospective sequence/partial tree/subgoal structure
Strategy = higher-level rule for allocating search/planning/action across contexts
Tactic = local method within a strategy/plan
```

These are working research definitions, not claims that one neural module
instantiates each object.

---

# 18. AI deference and delegation

## Landes, Francis & Everett (2026)

- PMID: 41795476
- DOI: 10.1016/j.cognition.2026.106504
- HF10 use: participants were influenced by AI moral advice but were not uniformly
  blindly deferential; reasons versus source deference matter.

## delegation and dishonest behavior (2025)

- PMID: 40963011
- PMCID: PMC12488497
- DOI: 10.1038/s41586-025-09505-x
- HF10 use: delegating goals to machine agents can increase unethical requests/
  execution under some designs, showing that delegation changes action architecture
  without automatically transferring moral responsibility.

## expert correction of AI scoring errors (2026)

- PMID: 42273403
- HF10 use: expert correction/deference to AI-labeled recommendations depends on
  error direction and attributed AI ability/responsibility.

### HF10 inference

```text
Delegation != AuthorityTransferByDefinition
Delegation != ResponsibilityElimination
Deference != BlindCompliance
AIRecommendation != HumanChoice
```

---

# 19. AI option generation / comparison is upstream framing

## automated comparison-table study (2026)

- PMID: 40987186
- DOI: 10.1016/j.pec.2025.109356
- HF10 use: LLMs/search can generate treatment option comparison surfaces, making
  completeness/framing of option sets an upstream Human-decision variable.

### HF10 inference

```text
AIGeneratedOptionSet != CompleteOptionSetByDefinition
OptionPresentation is a DecisionIntervention
```

---

# 20. Source-level synthesis

The strongest cross-source separations are:

```text
Judgment != Decision
Decision != Choice != Action
OptionGeneration != OptionEvaluation != Selection
ObservedChoice != StablePreference
Frame != Preference
DescriptionChoice != ExperienceChoice
Risk != Ambiguity
AnticipatedRegret != ExperiencedRegret

InformationValue != InstrumentalValueOnly
AvailableInformation != SoughtInformation
MoreInformation != AlwaysPreferred
Confidence != SearchPolicy
SearchPolicy != StoppingRule

Exploration != RandomChoice
DirectedExploration != RandomExploration
Exploitation != Optimality
MoreExploration != BetterLearning

MoreOptions != AlwaysBetter
MoreOptions != AlwaysWorse
OptionCount != ChoiceQuality

SunkResource != RemainingCost
SunkCostEffect != OneMechanism
Persistence != IrrationalityByDefinition
Precommitment != MoreWillpower
Commitment != Irreversibility

Plan != Policy != Strategy != Tactic
Planning != FullExhaustiveSearch
PlanningDepth != PlanningExistence
Subgoal != FinalGoal
ModelBased != PlanningTotality

AIRecommendation != HumanDecision
Delegation != Authority/ResponsibilityTransfer
AIGeneratedOptions != NeutralCompleteChoiceSet
```

The repeated residual across choice, planning, precommitment and delegation is
**realized action and control**. A Human can choose/commit/plan but still fail to
execute; actions must be selected, initiated, coordinated, corrected online and
coupled to environmental affordances/tools. Plans can be delegated to other humans
or AI while authority/responsibility remain separately assigned. HF10 therefore
points toward action/execution/control rather than another decision taxonomy.
