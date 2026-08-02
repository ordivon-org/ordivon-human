# E2 — China Household Liquidity, Commitments, and Recovery Protocol

## Status

**Protocol and public-evidence phase completed 2026-08-02. Authorized microdata execution remains pending.**

No CHFS or CFPS respondent records were present locally. Both official providers require registration or approval, and their data terms prohibit redistribution. E2 therefore separates:

```text
E2A  public documentation + evidence + executable protocol
E2B  authorized microdata execution outside Git
E2C  reviewed aggregate findings returned to Git
```

## Research questions

### E2-Q1 — Wealthy but illiquid

How many households have positive or substantial illiquid net wealth but insufficient mobilizable resources for a short income interruption?

### E2-Q2 — Commitment amplification

Do housing and other infrequently adjustable obligations predict larger consumption cuts, debt accumulation, or slower recovery after an income shock, conditional on income and net worth?

### E2-Q3 — Transition and persistence

Which households enter, remain in, or exit liquidity-constrained states between waves, and what changes accompany those transitions?

### E2-Q4 — Quality-preserving adjustment

When households face shocks, which expenditures are protected and which are reduced—food, health, education, housing, transport, or discretionary consumption—and what later health, capability, or well-being changes follow?

### E2-Q5 — Autonomy proxies

Can observable events such as unemployment exit, job change, migration, retraining, reduced work, or recovery after a shock validate the claim that liquidity and low lock-in expand feasible choices?

## Data roles

### CHFS

Primary use:

- detailed household financial and non-financial assets;
- housing and business wealth;
- household liabilities and credit access;
- income, expenditure, social insurance, and insurance;
- close replication of wealthy-hand-to-mouth classifications.

The official 2021 release reports 22,027 households across 29 provincial-level regions and 269 districts/counties. Access requires real-name registration and approval. Redistribution is prohibited.

### CFPS

Primary use:

- longitudinal household income, expenditure, assets, debt, and family structure;
- individual employment, earnings, health, happiness, education, migration, and training;
- linkage of economic state to non-economic outcomes.

The public-use data require registration and approval. The official agreement prohibits distribution of original or modified respondent data on third-party platforms.

### National Bureau of Statistics

Use only for national and urban/rural calibration. Aggregate income minus aggregate consumption is not treated as a household saving rate.

## Core measurement design

### 1. Three liquidity surfaces

E2 will not force one definition.

#### L1 — cash-deposit buffer

```text
cash and deposits
```

CFPS proxy: `SAVINGS`.

This is the narrowest and most directly mobilizable surface.

#### L2 — broad financial assets

```text
cash + deposits + marketable financial assets
```

CFPS proxy: `FINANCE_ASSET`.

The composition and transaction time of each component must be checked before treating all components as equivalent cash.

#### L3 — broad net-liquidity sensitivity proxy

```text
FINANCE_ASSET − NONHOUSING_DEBTS
```

This is **not** the exact Kaplan–Violante–Weidner or Cui–Feng definition because CFPS non-housing debt is broader than credit-card debt. It is retained only as a sensitivity bound.

### 2. Constrained-state definitions

The literature benchmark classifies a household as hand-to-mouth when net liquid wealth is no greater than half of income received in one pay period. For monthly income:

```text
net liquid wealth ≤ 0.5 × annual income / 12
```

E2 reports at least two classifications:

- **cash-buffer constrained:** `SAVINGS ≤ 0.5 × FINCOME1 / 12`;
- **broad-net-liquidity constrained:** `(FINANCE_ASSET − NONHOUSING_DEBTS) ≤ 0.5 × FINCOME1 / 12`.

They are labelled CFPS proxies, not exact replications.

### 3. Wealthy versus poor constrained

Preferred CHFS definition:

- poor constrained: constrained and net illiquid wealth `≤ 0`;
- wealthy constrained: constrained and net illiquid wealth `> 0`.

CFPS residual proxy:

```text
illiquid net wealth proxy
= TOTAL_ASSET − (FINANCE_ASSET − NONHOUSING_DEBTS)
```

This proxy must be sensitivity-tested against explicit housing and productive-asset components.

### 4. Runway

```text
cash runway months = SAVINGS / (PCE / 12)
```

`PCE` is ordinary consumption expenditure, not unavoidable expenditure. Runway is therefore descriptive and must not be interpreted as a recommended emergency-fund duration.

### 5. Debt and concentration

Primary continuous measures:

```text
total debt / annual income
housing debt / annual income
non-housing debt / annual income
housing net wealth / total net wealth
financial assets / total net wealth
```

Ratios with zero, negative, or near-zero denominators are reported separately rather than winsorized silently.

### 6. Commitment proxies

Cross-wave CFPS candidates:

- `HOUSE / FINCOME1` — annual housing expenditure share;
- `HOUSE_DEBTS / FINCOME1` — mortgage stock relative to income;
- `FP407 × 12 / FINCOME1` — annualized rent share where available;
- 2022 `FQ54 × 12 / FINCOME1` — current-house mortgage payment share, pending questionnaire validation;
- household size and dependent-member structure;
- transfers and welfare expenditure where obligations are observed.

These are not interchangeable. Debt stock, payment flow, essential housing services, and adjustment cost must remain distinct.

## Panel construction

### Household linkage

- 2020 key: `FID20`;
- 2022 current key: `FID22`;
- 2022 link to 2020 household: `FID20`.

The primary balanced panel joins 2020 `FID20` to the 2022 carried-forward `FID20`.

Household composition can change. Analyses must record:

- family-size change;
- split and merged households where identifiable;
- changes in financial respondent or expenditure decision maker;
- attrition and re-entry;
- whether the same economic decision unit still exists.

### Person linkage

Use `PID` for individual outcomes and family IDs for time-varying household membership.

Household economic variables may be repeated across adults only when:

- standard errors are clustered at household level;
- the outcome belongs to the individual;
- the interpretation is household exposure, not an independent observation.

## Primary analyses

### A1 — cross-sectional state distribution

For each wave:

- cash-buffer-constrained share;
- broad-net-liquidity-constrained share;
- wealthy and poor constrained shares;
- liquid-runway distribution;
- joint distribution by income, net wealth, housing, debt, family size, urban/rural status, and employment structure.

Report weighted and unweighted results separately after validating official weights.

### A2 — transition matrix

Between 2020 and 2022:

```text
not constrained
poor constrained
wealthy constrained
unknown
```

Estimate entry, persistence, exit, and state-switching rates under each liquidity definition.

### A3 — shock and adjustment event study

Candidate shocks:

- loss of employment or transition to unemployment;
- large negative household-income change;
- major medical expenditure or health deterioration;
- household split, death, divorce, or care burden;
- migration or forced housing change.

Outcomes:

- total and category consumption;
- new debt and debt service;
- liquid assets;
- training and education expenditure;
- health and happiness;
- employment recovery;
- migration and job change.

A two-wave result is descriptive. Stronger causal claims require more waves, policy discontinuities, or explicit quasi-experimental designs.

### A4 — decomposition of wealth change

Where measurement supports it:

```text
Δ net wealth
= active saving
+ transfers
+ asset revaluation
+ business/housing acquisition
− borrowing costs and losses
+ residual measurement error
```

CFPS alone may not identify all components. Unexplained residuals must remain visible.

### A5 — commitment heterogeneity

Test whether liquidity has different associations with shock response across:

- renters, mortgage holders, and owners without mortgage;
- low and high housing-expenditure shares;
- single versus multiple earners;
- households with children, older adults, or care responsibilities;
- households with and without social insurance;
- stable versus volatile labour income.

## Missingness and data quality

### Special codes

Negative survey codes—such as not applicable, refusal, do not know, and unable to estimate—are missing states, not money values.

Every analysis must report:

- original code frequencies;
- constructed-variable imputation flags where available;
- complete-case loss;
- interval and estimated responses;
- whether missing values were set to zero by the data provider or researcher.

### Recall periods

CFPS expenditure combines weekly, monthly, and annual recall periods into annual composites. Category comparisons must account for different recall error and seasonality.

### Income concept

CFPS warns that its household net-income composite is not fully equivalent to the National Bureau of Statistics disposable-income definition; property and transfer components differ. Cross-source comparisons must therefore be directional, not identity checks.

### Asset valuation

Housing and business values are respondent estimates with uncertain liquidation values. Report gross, net, and liquid measures separately.

## Identification hierarchy

1. weighted descriptive distributions;
2. within-household changes;
3. matched event studies with pre-trend checks where enough waves exist;
4. fixed-effects or correlated-random-effects models;
5. quasi-experiments tied to policies or plausibly exogenous shocks;
6. structural simulation only after descriptive and causal moments are established.

Machine-learning prediction does not establish mechanism or intervention value.

## Privacy and execution boundary

Authorized source files remain outside Git, for example:

```text
/root/private-data/ordivon-human/cfps/
/root/private-data/ordivon-human/chfs/
```

Public Git may retain only:

- variable specifications;
- analysis code;
- synthetic fixtures;
- aggregate tables reviewed for disclosure risk;
- provenance and exact data-release identifiers.

No row-level, transformed row-level, or reconstructable microdata are committed.

## E2 exit criteria

E2 closes only when:

1. official data access is obtained lawfully;
2. variable and weight definitions are validated against released documentation;
3. at least two liquidity definitions and two illiquid-wealth definitions are compared;
4. 2020–2022 transitions are estimated with attrition accounting;
5. commitment and shock-response analyses are run;
6. quality-of-life and capability outcomes are connected without treating expenditure as welfare;
7. aggregate outputs pass disclosure review;
8. claims are narrowed to what the design actually identifies.
