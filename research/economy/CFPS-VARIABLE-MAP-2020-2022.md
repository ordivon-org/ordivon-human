# CFPS 2020–2022 Variable Map for E2

## Provenance

This map was derived from the official English CFPS 2020 and 2022 codebooks published by the Institute of Social Science Survey, Peking University.

Official documentation pages:

- <https://www.isss.pku.edu.cn/cfps/en/documentation/data2/1201867cfps1295115.htm>
- <https://www.isss.pku.edu.cn/cfps/en/documentation/questionnaires/index.htm>
- <https://www.isss.pku.edu.cn/cfps/en/data/public/index.htm>

The codebooks report:

| Dataset | 2020 observations | 2022 observations |
|---|---:|---:|
| family economy | 11,620 | 10,726 |
| person | codebook release available | 27,001 |
| family configuration | codebook release available | 47,328 person-family rows |

Observation counts are release metadata, not a balanced-panel count.

## Household linkage

| Concept | 2020 | 2022 | Use |
|---|---|---|---|
| current family ID | `FID20` | `FID22` | wave-specific household key |
| prior 2020 family ID | — | `FID20` | primary 2020–2022 link |
| family size | `FAMILYSIZE20` | `FAMILYSIZE22` | composition and equivalence checks |

Household identity is not guaranteed to be substantively unchanged after splits, merges, deaths, migration, or respondent changes.

## Income and expenditure

| Concept | Variable | Codebook label | Cross-wave status |
|---|---|---|---|
| adjusted net family income | `FINCOME1` | Net family income (yuan) | stable |
| adjusted total family expenditure | `FEXP1` | Family's total expenditure adjusted (yuan) | stable |
| resident consumption expenditure | `PCE` | Residents' consumption expenditure: sum (yuan) | stable |
| food | `FOOD` | Expenditure on food: adjusted | stable |
| clothing | `DRESS` | Expenditure on clothing | stable |
| housing consumption | `HOUSE` | Expenditure on housing: adjusted | stable |
| household equipment/daily necessities | `DAILY` | Family equipment and daily necessities: adjusted | stable |
| medical and fitness | `MED` | Medical and fitness expenditure | stable |
| transport and communication | `TRCO` | Communication and transportation: adjusted | stable |
| education and entertainment | `EEC` | Education and entertainment expenditure | stable |
| other consumption | `OTHER` | Other consumption expenditure | stable |
| transfer expenditure | `EPTRAN` | Transfer expenditure | stable |
| welfare expenditure | `EPWELF` | Welfare expenditure | stable |

CFPS uses several recall periods and annualizes weekly or monthly responses. The official FAQ states that its income composite is not fully identical to the National Bureau of Statistics disposable-income definition.

## Assets and liabilities

| Concept | Variable | Codebook label | E2 role |
|---|---|---|---|
| cash and deposits | `SAVINGS` | Total amount of cash and deposits | narrow liquidity |
| financial assets | `FINANCE_ASSET` | Constructed financial asset | broad liquidity candidate |
| money lent to others | `DEBIT_OTHER` | Money lent out to others | receivable; liquidity uncertain |
| non-housing debt | `NONHOUSING_DEBTS` | Financial debt except house mortgage | broad debt sensitivity |
| housing debt | `HOUSE_DEBTS` | House mortgage | debt stock |
| mortgage constructed variable | `MORTAGE` | Mortgage on housing | reconcile before use |
| gross housing asset | `HOUSEASSET_GROSS` | Gross house asset, mortgage not deducted | concentration |
| net housing asset | `HOUSEASSET_NET` | House estate net | illiquid net wealth |
| business asset | `COMPANY` | Business asset | productive illiquid wealth |
| land asset | `LAND_ASSET` | Land asset | illiquid wealth |
| farm machinery | `AGRIMACHINE` | Value of farm machinery | productive illiquid wealth |
| productive fixed asset | `FIXED_ASSET` | Productive fixed asset | reconcile overlap before summing |
| net family asset | `TOTAL_ASSET` | Net family asset | whole-balance-sheet state |

Do not sum every constructed asset variable blindly. `FIXED_ASSET`, `COMPANY`, `LAND_ASSET`, and `AGRIMACHINE` may overlap depending on the provider's construction rules. The preferred first pass uses `TOTAL_ASSET` and tests explicit component alternatives.

## Commitments and authority

| Concept | Variable | Wave | Use |
|---|---|---|---|
| expenditure decision maker | `FF201` | 2022 confirmed | asset/expenditure authority surface |
| monthly rent | `FP407` | 2020 and 2022 | annualized rent burden |
| current-house monthly mortgage payment | `FQ54` | 2022 | payment burden after questionnaire validation |
| mortgage expenditure | `FT302` | 2020 and 2022 | ambiguous stock/flow wording; do not use until validated |
| housing ownership certificate members | `FQ3PID_A_*` | 2022 | legal-name ownership surface |
| current-house ownership type | `FQ2` | 2022 | tenure |
| loan rejection experience | `FT8` | 2020 and 2022 | credit constraint surface |

Authority is not inferred from household membership alone. `FF201` and ownership-name fields may reveal who decides or legally owns, but they do not completely measure veto power or access.

## Person outcomes and capability

| Concept | Variable | 2020–2022 status |
|---|---|---|
| person ID | `PID` | stable |
| current employment | `EMPLOY` | stable |
| total employment income | `EMP_INCOME` | wave-specific constructed value |
| job-income satisfaction | `QG401` | stable |
| job-security satisfaction | `QG402` | stable |
| unemployment reason | `QGB6` | stable where applicable |
| on-the-job training | `QGB2` | stable |
| online education/training use | `QU5` | observed in 2022 |
| happiness | `QM2016` | stable |
| self-rated health | `QP201` | stable |
| health change from prior year | `QP202` | stable |
| moved since prior interview | `EAR103` | stable |
| moved or changed hukou | `QR7` | stable |
| education years | `CFPS2020EDUY`, `CFPS2022EDUY` | wave-specific name |

Person outcomes can be joined through family IDs and `PID`. Repeating household exposure across members requires household-clustered inference.

## Social protection and support

Candidate person variables include:

- employer pension, health, unemployment, injury, and maternity insurance: `QG9_A_*`;
- pension registration and receipt: `QI1011`, `QI200`, `QI2001`, `QI202`;
- medical-insurance type: `QP605_A_*`;
- economic support to parents: `QF601_A_1`, `QF601_A_2`.

Candidate family-economy variables include:

- commercial-insurance expenditure: `FP514`;
- support to relatives and others: `FP515`, `FP516`;
- gifts and cash received: `FU102`;
- transfer income: `FTRANSFER_1`;
- transfer expenditure: `EPTRAN`.

Support can increase resilience while reducing autonomy when access is revocable or conditional. Existing variables do not fully identify those conditions.

## Weight status

The 2020 and 2022 family-economy codebooks contain variables labelled as standardized cross-sectional weights, including `FSWT_NATCS20N` and `FSWT_NATCS22N`. The English label refers to individual-level weight even though the file is household economic data.

E2 therefore does **not** select a weight automatically. The microdata run must validate the appropriate household and longitudinal weights against the official manual before weighted estimation.

## Special missing values

The codebooks use negative values for states such as:

- not applicable;
- refusal;
- do not know;
- unable to estimate;
- no valid prior-wave value.

The public pipeline converts negative monetary values to missing and reports missingness. It does not convert every negative value to zero.

## Variables intentionally not treated as complete measures

- `FINANCE_ASSET` is not automatically equivalent to same-day cash.
- `NONHOUSING_DEBTS` is not equivalent to credit-card debt.
- `HOUSE` is housing consumption, not mortgage payment or adjustment cost.
- `TOTAL_ASSET` does not reveal who can mobilize the asset.
- `QM2016` does not exhaust quality of life.
- `EMP_INCOME` does not measure transferable earning capability.
- `FF201` does not fully identify financial control.

These limits are part of the model, not documentation footnotes.
