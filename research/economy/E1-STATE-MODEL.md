# E1 — Personal Economic State and Transition Model

## 1. Unit of analysis

The preferred unit is:

```text
person or decision household
× time
× jurisdiction
× control and obligation structure
```

A household is not automatically a unified actor. Assets, income, debt, decision authority, and exit rights may belong to different members.

## 2. Stocks

### Financial stocks

- transaction cash;
- emergency liquid assets;
- long-horizon marketable assets;
- restricted retirement or benefit accounts;
- receivables;
- unsecured debt;
- secured debt;
- contingent liabilities.

### Non-financial stocks

- owner-occupied housing;
- other real estate;
- business equity and productive equipment;
- durable goods with resale or service value;
- intellectual property and reusable digital assets.

### Human and social stocks

- transferable earning capability;
- health and functional capacity;
- reputation and demonstrated work;
- labour flexibility;
- reliable formal insurance;
- public benefits and legal entitlements;
- family and network support, including its conditions and uncertainty.

Human and social stocks are not added mechanically to accounting net worth. They enter earning, shock, and option models separately.

## 3. Flows

### Inflows

- wages and salaries;
- business and self-employment income;
- property and investment income;
- transfers, benefits, and family support;
- borrowing;
- asset sales;
- one-time windfalls.

### Outflows

- essential consumption;
- quality-of-life consumption;
- capability-building expenditure;
- taxes and social contributions;
- debt service;
- insurance;
- maintenance and transaction cost;
- transfers to others;
- asset purchase and active saving;
- losses, fraud, penalties, and avoidable error.

Borrowing and asset sales are financing flows, not income. Asset purchases are not ordinary consumption, but they may still reduce liquidity.

## 4. Commitment structure

Each recurring outflow receives four properties:

| Property | Meaning |
|---|---|
| necessity | consequence of stopping payment |
| adjustability | time and cost required to reduce it |
| authority | who can change or veto it |
| duration | expected remaining obligation |

This avoids treating all spending as equally compressible.

A useful distinction is:

```text
flexible expenditure
versus
infrequently adjustable commitment
```

The research does not presume that flexible expenditure is low value or that commitments are wasteful. It asks how adjustment costs alter shock response and choice.

## 5. Risk exposures

- labour-income volatility and unemployment;
- business and client concentration;
- asset-price and interest-rate risk;
- inflation and currency mismatch;
- housing and location concentration;
- health, disability, and care shocks;
- family or relationship change;
- legal and policy change;
- fraud, cyber, and provider failure;
- skill obsolescence and technology substitution;
- correlation among income, assets, obligations, and support systems.

The last item is critical. A person employed in an industry, holding employer equity, living in an industry-dependent city, and relying on colleagues for opportunity may have several assets that fail together.

## 6. Derived indicators

These indicators are descriptive surfaces, not universal targets.

### 6.1 Liquid runway

```text
mobilizable low-loss resources
÷
monthly unavoidable net outflow during the selected shock
```

The denominator may change during unemployment, illness, relocation, or study leave.

### 6.2 Commitment ratio

```text
infrequently adjustable recurring obligations
÷
reliable after-tax recurring income
```

This is not a conventional debt-service ratio; it includes other lock-in where the study requires it.

### 6.3 Active saving

```text
income and transfers
− consumption
− taxes and costs
```

Asset valuation gains are reported separately. Change in net worth must reconcile active saving, valuation change, transfers, and measurement error.

### 6.4 Whole-balance-sheet gain

```text
change in assets
− change in liabilities
− external capital transfers
```

A retirement-account increase accompanied by unsecured debt is not counted as the full asset increase.

### 6.5 Income concentration

Shares of reliable income attributable to:

- largest employer or client;
- largest industry;
- largest platform;
- largest household contributor;
- transfers controlled by another party.

### 6.6 Asset concentration and liquidity composition

- largest-asset share;
- housing share;
- business-equity share;
- risky financial share;
- liquid share;
- restricted share;
- liabilities linked to each asset.

### 6.7 Quality-preserving surplus

```text
reliable net income
− unavoidable commitments
− spending required to maintain the declared quality floor
```

This is the candidate flow available for resilience, capability investment, and long-horizon assets.

### 6.8 Option coverage

For each named option—leave work, relocate, retrain, start a project, provide care—estimate:

- cash requirement;
- minimum time;
- income lost;
- obligations that continue;
- support required;
- probability of recovery if the option fails.

There is no single option-coverage score.

## 7. Transition model

At time `t`, define:

- `L_t`: liquid resources;
- `A_t`: long-horizon financial and productive assets;
- `D_t`: liabilities;
- `H_t`: earning and functional capability;
- `C_t`: commitment structure;
- `Q_t`: quality-of-life state;
- `R_t`: risk and correlation structure;
- `O_t`: feasible option set;
- `X_t`: external shocks and institutional conditions;
- `U_t`: chosen actions.

The next state is represented as:

```text
(L, A, D, H, C, Q, R, O)_(t+1)
=
F((L, A, D, H, C, Q, R, O)_t, U_t, X_t, history)
```

`F` is not assumed linear or stationary.

## 8. Recurrent mechanisms

### Liquidity trap

```text
illiquid wealth + low cash
→ expensive borrowing or forced sale after shock
→ consumption/capability cuts
→ slower recovery
```

### Commitment amplification

```text
high fixed obligations
→ moderate income shock cannot be absorbed through low-value cuts
→ increased labour and portfolio risk sensitivity
→ reduced refusal and exit power
```

### Capability compounding

```text
quality floor + time + tools + practice
→ greater transferable capability
→ higher or more diversified income
→ larger quality-preserving surplus
→ further capability and assets
```

### Lifestyle lock-in

```text
income growth
→ inflexible expenditure growth
→ unchanged runway and autonomy
→ continued dependence on peak income
```

### Correlated concentration

```text
same sector drives wage, equity, housing demand, and network support
→ one shock damages several buffers simultaneously
```

### Gross-saving illusion

```text
automatic or visible asset accumulation
+ hidden borrowing or reduced liquid balances
→ smaller-than-reported net improvement
```

## 9. Stage dependence

The model does not impose one universal sequence, but it expects the binding constraint to change:

| State | Likely binding constraint |
|---|---|
| no independent income | authority and capability formation |
| low liquid wealth | shock absorption and expensive debt |
| early stable income | earning growth and persistent surplus |
| growing commitments | lock-in, insurance, and correlated risk |
| substantial assets | concentration, tax, control, and capital preservation |
| reduced labour dependence | longevity, health, care, and withdrawal sustainability |

These are hypotheses for empirical testing, not age bands.

## 10. Model deletion test

A field is removed if it does not change:

- shock survival;
- expected whole-balance-sheet change;
- quality-of-life trajectory;
- capability trajectory;
- commitment or concentration risk;
- a named feasible option;
- strategy ranking for at least one complete case.

This keeps E1 as a decision model rather than a complete financial profile.
