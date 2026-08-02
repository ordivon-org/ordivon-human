# HUMAN-ECON-001 E2 Public Phase Closeout

## Decision

E2's public-evidence and executable-protocol phase is complete. The authorized respondent-level phase is ready but has not been executed because no approved CHFS or CFPS microdata were present locally.

The project does not infer current household prevalence from historical papers or public codebooks.

## Completed work

### E2A-1 — Chinese liquidity evidence review

The review established that:

- net worth can conceal severe near-term liquidity constraints;
- wealthy hand-to-mouth households were empirically material in the first CHFS wave;
- commitment timing changes classification substantially;
- housing, mortgage debt, and outright ownership are different states;
- debt overhang can constrain consumption independently of current income;
- health and other shocks change consumption composition, not only total spending;
- happiness and other quality outcomes may deteriorate alongside liquidity constraints, but current evidence is not sufficient for personalized causal advice.

### E2A-2 — official CFPS variable map

Official 2020 and 2022 codebooks were parsed to establish stable variables for:

- household linkage and family size;
- income and consumption categories;
- cash and deposits;
- financial assets;
- housing and non-housing debt;
- housing and total net assets;
- employment, earnings, health, happiness, migration, and training;
- expenditure decision authority and selected ownership surfaces.

### E2A-3 — executable aggregate pipeline

The pipeline now:

- reads CSV and JSON with the standard library;
- reads Stata and Parquet when optional mature readers are available;
- creates cash-buffer and broad-net-liquidity classifications;
- distinguishes poor and wealthy constrained states;
- produces liquid-runway, debt, concentration, and missingness diagnostics;
- links 2020 and 2022 one-to-one households;
- detects family splits rather than silently selecting a successor;
- suppresses small transition cells;
- writes aggregate output only;
- records input hashes and definitions;
- never writes respondent rows.

### E2A-4 — synthetic acceptance suite

Synthetic fixtures cover:

- non-constrained households;
- wealthy constrained households;
- poor constrained households with legitimate negative net assets;
- missing cash values;
- entry and exit from constrained states;
- household split links;
- small-cell suppression;
- absence of household IDs from aggregate output.

The same fixtures were validated through CSV and temporary Stata inputs.

## Findings retained

### F9 — net-worth-only fragility measures fail

Historical CHFS evidence found about 17% of households classified as hand-to-mouth under the benchmark liquid-wealth definition, with about 90% of those households holding positive illiquid wealth. A net-worth-only definition identified only about 2.7%.

These are historical first-wave estimates, not current prevalence.

### F10 — commitment timing is part of liquidity

The historical CHFS classification varied from 12.2% to 26.5% depending on whether pre-committed expenditures were placed at the start or end of the period, compared with 17.0% under the benchmark convention.

Therefore annual assets and annual income do not fully represent shock capacity.

### F11 — housing is a bundle of opposing mechanisms

Housing may provide shelter, collateral, wealth, and inflation exposure while also creating leverage, fixed payments, transaction costs, location lock-in, and correlated labour-market risk.

Housing ownership cannot be given one universal sign.

### F12 — consumption totals conceal harmful substitution

After a health or income shock, households may preserve total expenditure by borrowing or by cutting food, education, training, or other capability-supporting expenditure.

Total consumption is therefore not a sufficient quality-of-life or recovery outcome.

### F13 — measurement definitions materially change results

CFPS's convenient non-housing-debt composite is broader than the credit-card-debt term used in the historical CHFS hand-to-mouth definition. The broad CFPS classifier is therefore a sensitivity proxy, not an exact replication.

### F14 — family identity is dynamic

A 2020 household can correspond to more than one 2022 household after splits or reorganization. Primary transitions must restrict to validated one-to-one links or explicitly model family transformation.

### F15 — legitimate negative net assets must survive cleaning

Treating every negative monetary value as a missing code deletes genuinely negative net-worth households and biases poor-constrained prevalence downward. Constructed net-asset variables require variable-specific cleaning.

## Claims rejected or narrowed

- Historical hand-to-mouth percentages are not current Chinese estimates.
- `TOTAL_ASSET` alone cannot identify liquidity, authority, or resilience.
- `FINANCE_ASSET - NONHOUSING_DEBTS` is not an exact liquid-wealth measure.
- All mortgage holders do not have the same commitment burden.
- All household links are not one-to-one across waves.
- All negative values are not missing codes.
- Total expenditure does not measure preserved quality of life.
- Codebook availability does not authorize respondent-data download or redistribution.

## What remains unresolved

- current weighted prevalence under recent CHFS and CFPS releases;
- persistence and transition rates after attrition and household splits;
- exact household and longitudinal weight selection;
- the role of mortgage payment flows versus mortgage stocks;
- which consumption categories are protected or cut after shocks;
- recovery in employment, health, happiness, migration, and training;
- whether autonomy proxies predict actual refusal and exit events;
- how conditional family support changes effective liquidity and control.

## Infrastructure judgment

Retained:

- one variable specification;
- one aggregate-only analysis script;
- two small synthetic CSV fixtures;
- one standard-library acceptance test;
- one synthetic aggregate result.

Rejected:

- a database;
- a survey-data mirror;
- a dashboard;
- a scoring service;
- a personal finance profile;
- automated protected-data acquisition;
- a bespoke statistics framework.

## Next admitted work — E2B

1. Obtain CFPS and/or CHFS access through the official user process.
2. Store source files in a private, non-Git directory.
3. Validate release filenames, hashes, variables, missing codes, weights, and panel links.
4. Execute the aggregate pipeline privately.
5. Review disclosure risk and measurement sensitivity.
6. Commit only aggregate findings, code changes, and provenance.

## Final status

```text
E2 public evidence review: complete
CFPS 2020–2022 variable map: complete
aggregate analysis protocol: complete
synthetic CSV path: validated
synthetic Stata path: validated
split-household handling: validated
small-cell suppression: validated
real CHFS/CFPS microdata run: not executed
current prevalence estimate: not claimed
next dependency: lawful approved data access
```
