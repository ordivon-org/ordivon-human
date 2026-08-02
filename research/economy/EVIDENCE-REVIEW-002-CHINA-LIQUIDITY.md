# Evidence Review 002 — Liquidity, Housing, Debt, and Adjustment in China

## Scope

This review narrows E2 around a concrete claim:

> High net worth does not guarantee near-term economic autonomy when wealth is illiquid, debt and commitments are rigid, or income and assets fail together.

The review uses primary or official sources and distinguishes direct estimates from E2 inferences.

## 1. Wealthy hand-to-mouth households are not a marginal anomaly

Cui and Feng's CHFS study classifies households as hand-to-mouth when net liquid wealth is no greater than half of income in a pay period. Liquid wealth includes cash, transaction and saving accounts, stocks, bonds, and other financial products, net of credit-card debt. Illiquid wealth includes net housing and land, retirement and selected insurance accounts, housing funds, certificates of deposit, and productive physical assets.

Under its benchmark definition:

| State | Weighted share of households |
|---|---:|
| poor hand-to-mouth | 1.7% |
| wealthy hand-to-mouth | 15.3% |
| non-hand-to-mouth | 83.0% |
| all hand-to-mouth | 17.0% |
| hand-to-mouth using net worth only | 2.7% |

Thus about 90% of classified hand-to-mouth households were wealthy hand-to-mouth. A net-worth-only measure would miss most of them.

The study's 2011-era sample reported median net liquid wealth of 3,000 yuan and median net illiquid wealth of 111,400 yuan; 82.4% had positive housing wealth. These are historical figures, not current estimates, but the balance-sheet geometry remains important.

Source: <https://onlinelibrary.wiley.com/doi/10.1111/asej.12123>

Author-posted working-paper text: <https://www.researchgate.net/publication/311453321_The_Wealthy_Hand-to-Mouth_in_China>

### E2 judgment

**Retained:** liquidity and illiquid wealth must be represented separately.

**Not retained as current prevalence:** the 17% estimate comes from the first CHFS wave and cannot be applied to 2026 households.

## 2. Classification is sensitive to commitment timing

The same study explicitly treats rent, mortgage, school fees, utilities, phone, and internet as pre-committed spending with adjustment costs.

Its robustness table reports:

- 12.2% hand-to-mouth when committed spending is treated as occurring at the start of the period;
- 26.5% when it is treated as occurring at the end;
- 17.0% under the benchmark midpoint-equivalent definition.

This wide range is not merely statistical noise. It shows that the timing of obligations relative to income and liquid balances changes whether a household can smooth consumption.

### E2 judgment

A single annual balance-sheet snapshot is insufficient. Payment timing, income timing, and adjustment cost are part of liquidity.

## 3. Chinese household liquidity constraints worsened before the pandemic

Ning and Wang use CFPS 2010–2018 plus a pandemic-era internet survey. They report that the share of households classified as liquidity constrained rose from 24.37% in 2010 to 35.31% in 2018. Their results attribute middle-income constraints more strongly to a debt-overhang channel associated with the real-estate boom than to income stagnation alone. Liquidity-constrained households had consumption about 6.9% lower than unconstrained households in their specification.

They also report that mortgage homeowners and households without housing reduced consumption more and displayed greater precaution during the pandemic than homeowners without mortgages.

Source: <https://sysengi.cjoe.ac.cn/EN/10.12011/SETP2021-3017>

### E2 judgment

**Supported mechanism:** housing position is heterogeneous. Owning a home, owning with mortgage debt, and not owning are different states.

**Caution:** the 24.37%, 35.31%, and 6.9% figures depend on the paper's definition and model. E2 should replicate rather than import them as ground truth.

## 4. Housing can simultaneously expand collateral and increase fragility

A 2025 CHFS study of financially vulnerable households reports that house-purchasing behavior can reduce asset-based credit constraints while worsening vulnerability-based credit constraints and consumption pressure. The direction depends on the channel and household state.

Source: <https://xbbjb.cufe.edu.cn/EN/Y2025/V0/I4/41>

### E2 judgment

The research should not classify housing as either universally productive wealth or universally harmful lock-in. It can provide shelter, collateral, appreciation exposure, leverage, fixed payments, transaction cost, and location constraint at the same time.

## 5. Liquidity constraints extend beyond consumption quantity

A 2026 CHFS study reports lower happiness among hand-to-mouth households, with worse outcomes for indebted households facing persistent rather than temporary constraints. The result is based on ordered-logit analysis and does not by itself establish causal effects.

Source: <https://doi.org/10.1080/00036846.2025.2453765>

### E2 judgment

Quality of life should be analyzed as an outcome alongside consumption, but cross-sectional happiness regression is not sufficient evidence for an intervention.

## 6. Shocks reallocate consumption, not merely reduce it

CFPS-based research on health shocks reports increased medical-expenditure shares alongside reductions in food and education expenditure, with stronger effects among low-income households. This demonstrates why total consumption alone can miss damage to future capability or present functioning.

Source: <https://pmc.ncbi.nlm.nih.gov/articles/PMC11260705/>

### E2 judgment

Category-level adjustment is required. A household that preserves total expenditure by borrowing, or cuts education and food to pay medical bills, has not necessarily preserved quality of life or future capability.

## 7. Measurement transport from CHFS to CFPS is imperfect

CHFS is designed for detailed household finance. CFPS is designed for longitudinal economic and non-economic well-being.

The Cui–Feng liquid-wealth definition subtracts credit-card debt specifically. CFPS's convenient constructed variable `NONHOUSING_DEBTS` is broader. Therefore:

```text
FINANCE_ASSET − NONHOUSING_DEBTS
```

is a sensitivity proxy, not an exact replication.

CFPS does, however, provide stable 2020–2022 variables for cash/deposits, financial assets, housing assets, mortgage and other debt, family income, consumption categories, family size, employment, health, happiness, migration, and training.

Official codebook page: <https://www.isss.pku.edu.cn/cfps/en/documentation/data2/1201867cfps1295115.htm>

## Findings retained after Review 002

1. **Net-worth-only fragility measures are rejected.**
2. **The wealthy-but-illiquid state is empirically material in China, at least historically.**
3. **Commitment timing and payment structure can approximately double measured constrained prevalence under plausible definitions.**
4. **Housing tenure and mortgage state must be separated.**
5. **Debt overhang may matter independently of income, especially for middle-income households.**
6. **Consumption totals are insufficient; category substitution and well-being outcomes matter.**
7. **CHFS and CFPS should be complementary rather than forced into one identical construct.**
8. **A current prevalence estimate requires authorized recent microdata; historical percentages are not current facts.**

## Hypothesis ledger

| Hypothesis | Status after Review 002 |
|---|---|
| High net worth can coexist with low shock capacity | strongly supported |
| Most liquidity-constrained Chinese households are currently wealthy hand-to-mouth | historical support only; current prevalence unresolved |
| Mortgage debt amplifies consumption adjustment after shocks | supported but heterogeneous |
| Housing always reduces autonomy | rejected |
| Housing always improves resilience | rejected |
| Total expenditure is enough to measure successful adjustment | rejected |
| A single liquidity threshold is sufficient | rejected |
| CFPS can exactly reproduce CHFS liquid-wealth definitions from constructed variables alone | rejected |

## Next empirical burden

The authorized-data phase must estimate:

- current and wave-specific prevalence under several definitions;
- persistence and entry/exit transitions;
- sensitivity to liquid-debt and illiquid-wealth construction;
- mortgage/renter/outright-owner heterogeneity;
- category-level consumption responses;
- recovery, health, happiness, employment, migration, and training outcomes;
- missingness, attrition, and weighting effects.
