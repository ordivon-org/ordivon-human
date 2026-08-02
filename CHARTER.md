# Ordivon Human Charter

## 1. Mission

Ordivon Human studies the human being as a changing system embedded in biological, physical, social, economic, institutional, cultural, technological, and historical environments.

Its objective is not to produce a complete theory of humanity. Its objective is to build progressively better, falsifiable models that help answer:

- what a person can currently do;
- what constrains or expands that capability;
- how the person is changing;
- which observations are reliable;
- which causal claims are justified;
- which interventions improve an explicitly declared outcome;
- what trade-offs, uncertainty, and heterogeneity remain.

## 2. Unit of analysis

The default unit is not an isolated static individual. It is:

```text
person × time × context × history × action × event
```

A useful human model must preserve at least four distinctions:

1. **person** — biological and psychological organization, identity, capacities, preferences, and accumulated resources;
2. **context** — relationships, institutions, physical environment, economy, culture, technology, and current opportunity set;
3. **trajectory** — prior states, exposures, learning, shocks, path dependence, and developmental timing;
4. **observation** — how a claim was measured, by whom, with which instrument, error, selection process, and uncertainty.

## 3. Working dynamic model

Let:

- `S_t` be a person's latent and observed state at time `t`;
- `E_t` be the physical, social, economic, institutional, and technological environment;
- `A_t` be actions and behavioural patterns;
- `X_t` be exogenous events and shocks;
- `M_t` be measurement processes;
- `Y_t` be outcome variables selected for one explicit research question.

The project studies transitions of the form:

```text
S_(t+1) = F(S_t, E_t, A_t, X_t, history, development, uncertainty)
observed data = M_t(S_t, E_t, A_t, Y_t) + error
```

`F` is not assumed to be linear, stationary, universal, or fully identifiable. Feedback, thresholds, interactions, delays, adaptation, and path dependence are expected.

## 4. Research dimensions

Ordivon Human may study:

1. biological substrate and inheritance;
2. bodily functioning, health, energy, sleep, and recovery;
3. perception, cognition, memory, learning, emotion, motivation, and regulation;
4. personality, identity, values, preferences, and subjective experience;
5. behaviour, habits, decisions, and revealed trade-offs;
6. knowledge, skills, creativity, productivity, and capability formation;
7. income, wealth, consumption, time, risk capacity, and material security;
8. relationships, social networks, family, organizations, institutions, and culture;
9. physical, informational, digital, political, and technological environments;
10. development, ageing, shocks, transitions, and complete life-course trajectories.

These dimensions are analytical views, not independent compartments.

## 5. Outcome pluralism

No universal scalar objective is accepted by default.

Possible outcomes include survival, health, functioning, agency, autonomy, capability, learning, material security, relationships, participation, subjective well-being, creation, contribution, and meaning. A study must declare:

- whose outcome is being optimized;
- over what time horizon;
- under which value assumptions;
- which costs and displaced outcomes are counted;
- who bears the risk;
- whether the change is reversible.

## 6. Epistemic rules

1. **Population distributions do not determine individuals.** Group statistics update priors; they do not erase individual evidence.
2. **Correlation is not causation.** Prediction, explanation, intervention, and moral judgment are separate tasks.
3. **A proxy is not the construct.** Income is not freedom; test score is not intelligence; engagement is not well-being; body mass is not health.
4. **Self-report is evidence, not ground truth or noise.** Behavioural, physiological, administrative, digital, and reported measures each have distinct failure modes.
5. **Trait, state, context, event, and trajectory must not be conflated.** Stability is an empirical claim.
6. **Measurement changes behaviour.** Tracking, scoring, feedback, and model predictions can alter the person and the environment being studied.
7. **Missingness and selection are causal facts.** Who is measured, who remains, and who drops out can dominate conclusions.
8. **No precision theatre.** More variables, decimals, dashboards, or model parameters do not create more truth.
9. **No premature ontology.** A field or abstraction is retained only when it prevents a demonstrated analytical failure or enables a real study.
10. **Models remain contestable.** A person has the right to reject, correct, contextualize, or exit a model applied to them.

## 7. Human–AI boundary

Ordivon Human studies AI as part of the human environment and, increasingly, as a cognitive and action multiplier.

It asks whether AI:

- expands memory, learning, judgment, creativity, and execution;
- redistributes capability and access;
- creates dependence, deskilling, persuasion, surveillance, or concentration of control;
- changes identity, relationships, institutions, labour, and development;
- enables a durable human–machine composite without silently replacing the person's goals.

Human augmentation is not defined as maximizing time spent with AI or maximizing task output. The retained criterion is increased durable agency under explicit values and acceptable dependence.

## 8. Privacy and consequence boundary

The public repository contains frameworks, methods, synthetic examples, aggregate evidence, and legally reusable source material.

It does not contain identifiable personal health, financial, behavioural, relationship, location, biometric, genomic, or private conversational data. Any future private study must separate:

```text
public methods
private raw observations
controlled derived data
publishable aggregate evidence
```

Medical, legal, employment, insurance, credit, education-admission, policing, or other high-consequence decisions require domain-specific authority and evidence outside this repository.

## 9. Implementation admission

A new collector, schema, database, service, model, dashboard, benchmark, or governance process is admitted only when:

1. a named research question requires it;
2. mature tools cannot perform the work with acceptable cost and fidelity;
3. the minimum necessary data are identified;
4. measurement error and privacy consequences are explicit;
5. deletion or exit remains possible;
6. the expected information gain exceeds maintenance and governance cost.

The default H0 implementation is documents, analysis notebooks outside the public repository when needed, and small reproducible experiments. A permanent platform is not presumed.
