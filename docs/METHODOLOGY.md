# Methodology

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
