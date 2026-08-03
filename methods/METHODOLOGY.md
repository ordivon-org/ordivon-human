---
schema_version: 1
id: human.methodology
title: Methodology
type: protocol
profile: research
lifecycle: active
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - builder
  - agent
updated: 2026-08-03
summary: Canonical methodological protocol for matching Human claims to measurement, statistical, causal, longitudinal, qualitative, and model-validation evidence.
evidence_status: not_applicable
readiness: READY
applies_to:
  - ordivon-human
related:
  - human.charter
  - human.program
  - human.privacy-ethics
  - human.authority
---
# Methodology

## Question

What minimum methodological discipline is required for Human research to distinguish observation, prediction, causal explanation, and normative choice without overstating population, individual, or intervention claims?

## Method

Match the design to the claim; state target population, measurement validity, uncertainty, missingness, heterogeneity, time structure, identification assumptions, transport limits, privacy risk, and simpler alternatives; preserve null results and delete models that add no explanatory or decision value.

## Inputs

Inputs may include primary studies, official statistical documentation, validated instruments, longitudinal and experimental designs, qualitative evidence, administrative or behavioral records, systematic reviews, project-specific hypotheses, and reproducible code or transformations.

## Procedure

Classify the claim, define constructs and outcomes, select an appropriate design, document data provenance and selection, analyze uncertainty and heterogeneity, test assumptions and simpler baselines, separate empirical findings from value judgments, and record limitations and deletion conditions.

## Evidence

Evidence is sufficient only when its design, measurement, population, timing, and uncertainty support the stated claim. Prestige, sample size, predictive accuracy, statistical significance, or model complexity alone do not establish causal or normative authority.

## Failure conditions

Fail or narrow the claim when constructs lack validity, missingness or selection changes interpretation, within-person and between-person effects are conflated, causal assumptions are unsupported, subgroup harm is hidden by averages, transport is unjustified, privacy cost is disproportionate, or a simpler explanation performs equivalently. [`../docs/PRIVACY-AND-ETHICS.md`](../docs/PRIVACY-AND-ETHICS.md) governs data and consequence limits; [`../docs/authority.md`](../docs/authority.md) governs how method relates to current findings.

## 1. Separate four tasks

Ordivon Human distinguishes:

1. **description** — what is observed and how it is distributed;
2. **prediction** — what is likely to occur under the observed data-generating process;
3. **causal explanation** — what mechanisms or interventions change an outcome;
4. **normative decision** — what should be optimized, for whom, and under which values.

A predictive model can be accurate without identifying causes. A causal estimate can be valid for one intervention and population without defining what is desirable.

## 2. Study hierarchy

No single design dominates every question. Evidence may come from:

- measurement and validation studies;
- cross-sectional observational studies;
- longitudinal cohorts;
- natural experiments and quasi-experiments;
- randomized interventions;
- within-person and N-of-1 designs;
- qualitative studies and process tracing;
- mechanistic biological or cognitive experiments;
- administrative, behavioural, wearable, and environmental data;
- systematic reviews and meta-analyses.

The design must match the claim.

## 3. Minimum statistical discipline

Each quantitative analysis should report where applicable:

- target population and sampling process;
- sample size and effective sample size;
- missing-data mechanism and attrition;
- distribution, central tendency, dispersion, and outliers;
- uncertainty intervals, not only point estimates;
- effect size and practical significance;
- model assumptions and diagnostics;
- preregistered versus exploratory status;
- multiple-comparison and researcher-degree-of-freedom risks;
- subgroup heterogeneity and distributional effects;
- external-validity limits;
- code, transformations, and data provenance sufficient for reproduction.

Statistical significance is not a retention criterion for a theory or intervention.

## 4. Causal discipline

Before estimating an intervention effect, state:

```text
exposure or intervention
outcome
time order and horizon
target population
causal estimand
assumed causal graph
confounders and mediators
selection and measurement processes
interference or spillovers
identification assumptions
```

Do not mechanically “control for all available variables.” Conditioning on mediators, colliders, or post-treatment variables can increase bias.

## 5. Within-person and between-person effects

A relation across people may not describe change within one person.

Examples:

- people who sleep more may differ from people who sleep less, while adding sleep for one individual may have a different effect;
- higher-income groups may report different well-being, while a short-term income increase has heterogeneous effects;
- high performers may use a tool frequently, while assigning that tool to a novice may initially reduce learning.

Models should separate within-person, between-person, cohort, and period variation when the question requires it.

## 6. Heterogeneity

Average effects may hide:

- responders and non-responders;
- benefit and harm subgroups;
- thresholds and diminishing returns;
- interactions with baseline state;
- developmental timing;
- environmental constraints;
- implementation differences.

Subgroup analysis must not become unbounded pattern mining. Hypotheses, shrinkage, validation, and replication are preferred.

## 7. Measurement quality

A construct requires an operational definition and evidence for:

- reliability;
- content and construct validity;
- criterion or predictive validity where appropriate;
- sensitivity to meaningful change;
- invariance across relevant groups and time;
- acceptable burden and reactivity;
- known floor, ceiling, and context effects.

A famous scale is not automatically valid for a new population, language, age, context, or repeated-measure use.

## 8. Source policy

Priority order:

1. primary research, official statistical or scientific documentation, and validated instruments;
2. systematic reviews, meta-analyses, and major consensus reports;
3. high-quality secondary synthesis;
4. clearly marked hypotheses, interpretations, and project-specific models.

Source prestige does not override study design, measurement quality, relevance, or contradictory evidence.

## 9. Model evaluation

Human models should be evaluated for:

- calibration and discrimination when predictive;
- temporal and external validation;
- subgroup error and distribution shift;
- robustness to measurement choices;
- causal identification when intervention claims are made;
- interpretability appropriate to consequence;
- privacy leakage and misuse potential;
- whether the model changes the behaviour it predicts;
- whether a simpler model performs equivalently.

## 10. Negative results and deletion

A study should preserve:

- failed hypotheses;
- null or heterogeneous effects;
- invalid instruments;
- non-replicating findings;
- data that proved unnecessary;
- abstractions deleted after comparison.

The project optimizes information gain, not the number of retained frameworks, measures, datasets, or positive findings.
