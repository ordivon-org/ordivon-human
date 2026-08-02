# Privacy and Ethics

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
