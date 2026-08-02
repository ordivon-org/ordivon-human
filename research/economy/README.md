# HUMAN-ECON-001 — Sustainable Personal Economic Autonomy

**Status: active. E0–E1 completed; E2 public phase completed 2026-08-02; authorized microdata execution pending.**

## Research question

> From the point at which a person can independently decide income, consumption, debt, saving, work, and investment, how can they accumulate more durable wealth without materially degrading present quality of life, while expanding security, refusal power, exit capacity, and future choices?

This is a household-finance and human-development question, not an investment-return contest.

## Current answer

A durable path is more likely to come from preserving a quality-of-life floor, building liquid resilience, limiting inflexible commitments and correlated failure modes, expanding transferable earning capability, maintaining a persistent whole-balance-sheet surplus, and only then converting long-horizon surplus into diversified productive assets.

E2 strengthens one part of that answer:

> Net worth is not enough. The timing, liquidity, debt structure, commitment burden, asset control, and recovery path determine whether wealth can actually protect choice.

This remains a conditional mechanism map, not individualized financial advice.

## Findings retained so far

1. **Income, consumption, wealth, debt, and liquidity are distinct.** None can represent economic autonomy alone.
2. **Liquidity has independent value.** A household can own substantial housing or business wealth while remaining unable to absorb a near-term shock.
3. **Net-worth-only fragility measures fail.** Historical CHFS research found that most benchmark hand-to-mouth households held positive illiquid wealth.
4. **Commitment timing matters.** The same annual balance sheet can imply different shock capacity depending on when income and fixed payments arrive.
5. **Gross saving is not net wealth creation.** Visible account accumulation can coexist with debt growth or reduced liquidity.
6. **Housing has opposing effects.** Shelter, collateral, leverage, payment burden, transaction cost, and location lock-in must be separated.
7. **Human capital is part of the risk system.** Age alone is not a sufficient risk rule; income volatility, labour flexibility, social insurance, and correlation with assets matter.
8. **Consumption totals conceal substitution.** Food, health, education, training, and other capability-supporting expenditure may be cut even when total spending appears stable.
9. **Autonomy is a distinct outcome.** It concerns feasible refusal, waiting, exit, relocation, retraining, reduced work, and recovery—not merely net worth.
10. **Current Chinese prevalence remains unresolved.** Historical estimates and public codebooks cannot replace an authorized recent microdata analysis.

## Research artefacts

### E0–E1

- [`E0E1-CLOSEOUT.md`](E0E1-CLOSEOUT.md) — first-round findings and rejected claims;
- [`E0-OUTCOME-FRAMEWORK.md`](E0-OUTCOME-FRAMEWORK.md) — plural outcomes and hard constraints;
- [`E1-STATE-MODEL.md`](E1-STATE-MODEL.md) — stocks, flows, commitments, risks, and transitions;
- [`EVIDENCE-REVIEW-001.md`](EVIDENCE-REVIEW-001.md) — liquidity, commitments, saving/debt, human capital, and wealth decomposition;
- [`CHINA-BASELINE-2025.md`](CHINA-BASELINE-2025.md) — reproducible official aggregate baseline.

### E2

- [`E2-PUBLIC-PHASE-CLOSEOUT.md`](E2-PUBLIC-PHASE-CLOSEOUT.md) — completed work, retained findings, limits, and next dependency;
- [`E2-RESEARCH-PROTOCOL.md`](E2-RESEARCH-PROTOCOL.md) — questions, definitions, panel design, analyses, identification, and exit criteria;
- [`CFPS-VARIABLE-MAP-2020-2022.md`](CFPS-VARIABLE-MAP-2020-2022.md) — official 2020–2022 household and person variables;
- [`EVIDENCE-REVIEW-002-CHINA-LIQUIDITY.md`](EVIDENCE-REVIEW-002-CHINA-LIQUIDITY.md) — China-specific liquidity, housing, debt, and adjustment evidence;
- [`E2-DATA-ACCESS.md`](E2-DATA-ACCESS.md) — lawful data access and private execution boundary;
- [`spec/e2-cfps-2020-2022.json`](spec/e2-cfps-2020-2022.json) — machine-readable variable and definition specification;
- [`e2_cfps_balance_sheet.py`](e2_cfps_balance_sheet.py) — aggregate-only CSV/Stata/Parquet analysis pipeline;
- [`test_e2_cfps_balance_sheet.py`](test_e2_cfps_balance_sheet.py) — standard-library acceptance suite;
- [`fixtures/`](fixtures/) — synthetic 2020–2022 panel fixtures;
- [`evidence/e2-synthetic-results.json`](evidence/e2-synthetic-results.json) — synthetic aggregate output, not an empirical estimate.

### Shared

- [`SOURCES.md`](SOURCES.md) — official frameworks, datasets, and primary research;
- [`china_2025_baseline.py`](china_2025_baseline.py) — official aggregate calculation;
- [`evidence/china-2025-baseline.json`](evidence/china-2025-baseline.json) — generated baseline result.

## E2 execution boundary

No CHFS or CFPS respondent-level data were found locally. Official data require registration or approval and may not be redistributed through this repository.

E2 is therefore separated into:

```text
E2A public evidence + official variable map + tested protocol   complete
E2B authorized respondent-level execution outside Git          pending
E2C reviewed aggregate findings returned to Git                pending
```

## Next empirical work

After lawful data access:

1. estimate cash-buffer and broad-net-liquidity constraint prevalence under several definitions;
2. distinguish poor and wealthy constrained households;
3. estimate 2020–2022 entry, persistence, and exit with attrition and household-split accounting;
4. compare renters, mortgage holders, and outright owners;
5. study category-level consumption adjustment after income and health shocks;
6. connect liquidity and commitments to employment, health, happiness, migration, and training recovery;
7. validate candidate proxies for refusal, exit, retraining, and relocation capacity.

Public Git will retain code, synthetic fixtures, aggregate outputs, and provenance—not respondent records.
