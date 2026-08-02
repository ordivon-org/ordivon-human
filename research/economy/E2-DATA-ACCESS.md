# E2 Data Access and Compliance

## Current execution state

No CHFS or CFPS respondent-level data were found in the local environment on 2026-08-02.

E2 therefore does not claim to have executed respondent-level regressions or prevalence estimates.

## CFPS

Official public-data page:

<https://www.isss.pku.edu.cn/cfps/en/data/public/index.htm>

Official application guide:

<https://www.isss.pku.edu.cn/cfps/en/faq/data23/index.htm>

Official agreement:

<https://www.isss.pku.edu.cn/cfps/en/data/DataUserAgreement/index.htm>

The current process requires an approved account on the CFPS data platform or Peking University Open Data platform. Public datasets are provided in SAS and Stata formats.

The agreement requires privacy protection and source citation, restricts data to academic or policy research, and prohibits distribution of any part of the data—original or modified—on third-party platforms.

### Local placement after lawful download

```text
/root/private-data/ordivon-human/cfps/2020/
/root/private-data/ordivon-human/cfps/2022/
```

Suggested files:

```text
cfps2020famecon_*.dta
cfps2020person_*.dta
cfps2020famconf_*.dta
cfps2022famecon_*.dta
cfps2022person_*.dta
cfps2022famconf_*.dta
```

Exact release filenames and hashes must be recorded privately and summarized publicly without redistributing bytes.

## CHFS

Official 2021 release notice:

<https://chfs.swufe.edu.cn/info/1041/4051.htm>

Official application entry:

<http://chfser.swufe.edu.cn/datas/>

The official notice states that access requires real-name registration and approval. It prohibits unauthorized redistribution, sale, or other commercial or non-commercial reuse.

### Local placement after lawful download

```text
/root/private-data/ordivon-human/chfs/2021/
```

CHFS remains the preferred source for exact asset-component and liquid-debt replication.

## Public-repository rule

Never commit:

- `.dta`, `.sav`, `.sas7bdat`, or respondent-level `.csv` files;
- row-level extracts;
- recoded records that remain linkable;
- small-cell tables that enable reconstruction;
- direct identifiers or restricted geography;
- account credentials or approval documents.

May commit:

- code and variable specifications;
- synthetic fixtures;
- release metadata and hashes;
- reviewed aggregate statistics;
- model diagnostics without respondent records;
- disclosure-review notes.

## Reproducible execution

The E2 script uses CSV with the standard library and supports Stata/Parquet when optional mature readers are installed.

Recommended private execution:

```bash
uv run --with pandas --with pyreadstat \
  python research/economy/e2_cfps_balance_sheet.py \
  --wave-2020 /root/private-data/ordivon-human/cfps/2020/famecon.dta \
  --wave-2022 /root/private-data/ordivon-human/cfps/2022/famecon.dta \
  --output /root/private-data/ordivon-human/results/e2-cfps-results.json
```

Only reviewed aggregate results should be copied into `research/economy/evidence/`.

## Disclosure review

Before publication:

1. suppress or combine small cells;
2. remove extrema and exact rare combinations;
3. round estimates where exact precision adds no value;
4. verify that no output contains IDs;
5. document sample filters and denominator changes;
6. preserve weighted counts separately from raw row counts;
7. inspect transition cells for sparse household paths;
8. follow provider-specific publication and notification requirements.

## Why access is not automated

Registration requires user identity, agreement to terms, and approval. Ordivon does not fabricate consent, use another person's account, scrape protected downloads, or treat public documentation as permission to redistribute respondent data.
