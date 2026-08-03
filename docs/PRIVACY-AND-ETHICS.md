---
schema_version: 1
id: human.privacy-ethics
title: Privacy and Ethics
type: decision
profile: organization
lifecycle: active
source_role: canonical
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - maintainer
  - builder
  - participant
  - agent
updated: 2026-08-03
summary: Canonical decision for public-data prohibition, minimization, participation, high-consequence use, anti-reductionism, Human–AI studies, and private-study separation.
evidence_status: not_applicable
readiness: READY
applies_to:
  - ordivon-human
related:
  - human.charter
  - human.methodology
  - human.authority
---
# Privacy and Ethics

## Context

Human research may involve intimate, linkable, consequential, or behavior-changing information. Technical access, storage cost, model capability, or participant consent alone do not justify collection, publication, inference, or automated use.

## Decision

Keep the public repository free of identifiable human research data. Minimize every observation to a named question, match consent and review to actual risk and jurisdiction, prohibit automated high-consequence authority, reject essentialist or moral ranking from limited measurements, and separate private raw data, controlled analysis, and reviewed aggregate publication.

## Consequences

Public Git may contain questions, methods, code, synthetic fixtures, aggregate evidence, and lawful reusable sources. It may not contain raw or linkable personal health, financial, relationship, behavioral, location, biometric, genetic, conversational, credential, education, employment, legal, or identity records. A private study must remain deletable and the public repository must function without its raw data.

## Status

Accepted and active. [`../CHARTER.md`](../CHARTER.md) defines project admission, [`../methods/METHODOLOGY.md`](../methods/METHODOLOGY.md) defines evidence discipline, and [`authority.md`](authority.md) records content authority. Any proposed exception requires an explicit study-specific review outside this document and does not modify the default public-data prohibition.

## 1. Default data posture

The public repository stores no identifiable human research data.

Prohibited public content includes raw or linkable:

- health and medical records;
- biometrics, genetics, images, voice, or physiological streams;
- precise location or movement;
- financial transactions and account information;
- private messages, relationships, and social graphs;
- education, employment, legal, or identity records;
- detailed behavioural traces;
- credentials or platform exports;
- data about another person collected without an appropriate basis.

Synthetic examples must not be lightly transformed copies of real people.

## 2. Data minimization

Collect only variables needed for a named question. “May be useful later” is not sufficient.

For every proposed observation, document:

- purpose;
- necessity;
- sensitivity;
- retention period;
- access scope;
- expected information gain;
- deletion path;
- consequences of disclosure or misuse.

## 3. Consent and participation

Future studies involving people must match consent and review requirements to jurisdiction, institution, risk, and intended publication or deployment.

Consent is not a blanket transfer of authority. Participants should know:

- what is observed;
- why it is observed;
- who can access it;
- how long it remains;
- what inferences may be made;
- what decisions may use the result;
- how to correct, withdraw, or exit where applicable.

## 4. High-consequence use

Ordivon Human does not authorize automated decisions in medicine, employment, education, insurance, credit, housing, law enforcement, migration, benefits, or other high-consequence domains.

A model that predicts a group-level outcome is not sufficient evidence for an adverse decision about a person.

## 5. Anti-reductionism

The project rejects:

- permanent essentialist labels from limited observations;
- moral worth inferred from ability, productivity, health, wealth, personality, or model score;
- opaque composite scores presented as objective truth;
- optimization that hides who selected the objective;
- surveillance justified solely by potential personalization;
- collecting intimate data because storage and analysis are technically cheap.

## 6. Human–AI research

Human–AI studies should measure both benefits and displaced capacities:

- output and learning;
- convenience and dependence;
- personalization and manipulation;
- memory extension and privacy loss;
- delegation and retained judgment;
- access expansion and concentration of control;
- immediate performance and long-term adaptability.

## 7. Private research layout

If a private study is later justified, the preferred separation is:

```text
ordivon-human public repository: questions, methods, synthetic fixtures, aggregate findings
private encrypted source: identifiable raw observations
controlled workspace: derived and pseudonymized analysis data
publishable artifacts: reviewed aggregate outputs with disclosure checks
```

The public repository must remain functional without access to private data.
