# Methods M0 Population-to-Individual Demonstration

## Purpose

This deterministic synthetic experiment tests three quantities that are often collapsed:

1. an observational difference between groups;
2. the population average causal effect;
3. the causal effect for a particular person.

It is a methodological demonstration, not a model of health, psychology, education, or any real person.

## Data-generating process

The synthetic population contains 5,000 people. Treatment selection depends on baseline capability and latent stress, so treated and untreated groups are not exchangeable.

Individual treatment effects are heterogeneous:

```text
effect = 0.4 + 0.5 × baseline capability − 0.3 × latent stress
```

Two target profiles then receive 400 simulated randomized N-of-1 trials, each with 96 periods. The regression accounts for a time trend, prior-period carryover, and a fixed external-event window.

## Results

| Quantity | Result |
|---|---:|
| naive treated-minus-untreated observational difference | −0.3480 |
| true population average effect | +0.3996 |
| population effect standard deviation | 0.5908 |
| fraction of people with a negative effect | 25.2% |
| target-benefit true individual effect | +1.0500 |
| target-benefit mean N-of-1 estimate | +1.0336 |
| target-harm true individual effect | −0.3100 |
| target-harm mean N-of-1 estimate | −0.3096 |

The naive observational association has the opposite sign from the true average effect. The average effect is itself insufficient for either target: one benefits substantially while the other is harmed.

The randomized repeated observations recover the target effects under the declared synthetic assumptions. This does not prove that N-of-1 designs are always valid. It shows what creates identification here:

- randomized assignment;
- repeated observations;
- an estimable and sufficiently rapid outcome response;
- declared carryover and event structure;
- a stable enough intervention and measurement process;
- a model whose assumptions match the data-generating process.

More personal data without those conditions would not solve the causal problem.

## H0 implications

The experiment forces the retained model to distinguish:

- population scope from individual scope;
- association from intervention effect;
- average effect from heterogeneous effect;
- person state from treatment assignment;
- external event from ordinary variation;
- observation from latent state;
- temporal trajectory from a one-time value.

It also sets a limit: personal intervention research should not begin merely because repeated data are available. The intervention must be repeatable, the outcome observable on the relevant timescale, carryover and trend manageable, and the consequences sufficiently reversible.

## Reproduction

```bash
python3 methods/m0/simulate_population_to_individual.py
```

The script uses only the Python standard library, writes [`evidence/population-to-individual.json`](evidence/population-to-individual.json), and contains assertions for the intended sign reversal, heterogeneity, and estimator accuracy.
