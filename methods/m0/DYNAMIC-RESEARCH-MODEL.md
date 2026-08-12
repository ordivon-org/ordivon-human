# Dynamic Research Model

> **Naming note:** this document was produced before the original method-first H0 work was reclassified as [Methods M0](README.md). “H0” below is historical wording and does not refer to the current [Human System Atlas](../../research/h0/README.md).

**Methods M0 retained model — 2026-08-02.**

The initial ten-level hierarchy has been superseded by a smaller dynamic model. H0 showed that the hierarchy mixed state domains, actions, context, time, measurement, and study-specific causal roles on one axis.

See [`MODEL-DELETION.md`](MODEL-DELETION.md) for the deletion evidence.

## 1. Unit of analysis

The default unit remains:

```text
person × time × context × history × action × event
```

The model is question-specific. It describes only the domains needed by one study; it is not a complete record of a person.

## 2. Study specification

Every analysis begins with a `StudySpec`:

```text
question
scope: population, subgroup, or person
prediction target or causal estimand
outcome owner
outcome vector and time horizon
value assumptions and displaced outcomes
population and selection process
privacy and consequence class
```

Without this specification, there is no context-independent meaning of “important human variable” or “improvement.”

## 3. Person state

`PersonState_t` may select from four domains.

### Body

Biological organization and bodily functioning relevant to the question:

- anatomy, physiology, metabolism, immune and endocrine processes;
- sleep, energy, pain, sensory function, mobility, fitness, illness, and recovery.

H0 merged biological substrate and bodily functioning at the top level. Mechanistic studies may retain finer subdomains locally.

### Mind

Psychological organization relevant to the question:

- perception, attention, memory, reasoning, language, and learning;
- emotion, motivation, regulation, identity, values, preferences, and subjective experience.

H0 merged cognition/affect and identity/preferences at the top level because their separation is question-dependent rather than universally structural.

### Capability

What the person can reliably do across declared conditions:

- knowledge and skill;
- creation and problem solving;
- coordination and tool use;
- transfer, adaptation, verification, and relearning.

Capability is not identical to one observed action, one test score, model-provided output, or joint human–tool performance.

### Situated state

Current options and constraints that are attached to the person but relational or institutional in nature:

- money, assets, debt, time, housing, equipment, and risk buffer;
- roles, rights, legal status, credentials, access, and obligations;
- relationships, trust, support, network position, and organizational membership.

These are not purely internal traits or an undifferentiated external environment.

## 4. Context

`Context_t` describes conditions not adequately represented as the person's current state:

- institutions, norms, culture, and policy;
- physical and ecological conditions;
- information exposure and media systems;
- technologies, AI systems, interfaces, and available tools;
- economic conditions and historical period.

A tool can be a context, intervention, or component of a joint system depending on the question.

## 5. Transition inputs

### Action

What the person or another participant does. Behaviour is represented as action rather than a static human level.

### Event or intervention

A discrete occurrence or deliberately assigned change, including shocks, transitions, treatments, policy changes, encounters, and changes in access.

Actions and events may change both person state and context.

## 6. Time and history

Time is an axis across all domains, not a peer level.

Relevant properties include:

- age, development, cohort, and historical period;
- prior states, exposures, actions, and events;
- direction and rate of change;
- persistence and volatility;
- lag, carryover, and recovery time;
- sensitive periods and cumulative effects;
- reversibility and path dependence.

A “trait” is a state with empirically estimated persistence over a declared window. A trajectory is a derived interpretation of observations across time, not primitive truth.

## 7. Observation and measurement

Observed data are not the state itself:

```text
Observation_t = Measurement(
  selected PersonState_t,
  Context_t,
  Action_t,
  Event_t,
  Outcome_t
) + error + selection effects
```

Each observation should preserve when relevant:

- construct and operational measure;
- source, instrument, observer, and version;
- time, frequency, and context;
- uncertainty, reliability, and missingness;
- participant or platform reactivity;
- privacy class and transformation provenance.

A latent construct is marked as inferred. Confounder, mediator, moderator, and collider are roles in a study-specific causal graph, not permanent properties of a variable.

## 8. Dynamic transition hypothesis

A study may propose:

```text
PersonState_(t+1), Context_(t+1)
  = F(
      PersonState_t,
      Context_t,
      Action_t,
      Event_t,
      History_(0:t),
      uncertainty
    )
```

`F` is not assumed to be linear, universal, stationary, identifiable, or the same across people. Feedback, thresholds, delayed effects, adaptation, and heterogeneous responses are expected.

## 9. Outcome pluralism

Possible outcome families include:

- survival, health, and functioning;
- agency and autonomy;
- capability, learning, and adaptability;
- material security and option value;
- relationships and participation;
- subjective well-being and suffering;
- creation, contribution, and meaning;
- resilience and recoverability.

No universal scalar objective is retained. A study records trade-offs and adverse displacement rather than hiding them in one score.

## 10. Population and individual inference

The model distinguishes:

- population distribution;
- observational association;
- predictive estimate;
- population average causal effect;
- subgroup heterogeneity;
- individual prior;
- individual longitudinal or experimental evidence.

Population statistics can update a prior for one person. They do not determine personal causal response. H0's synthetic demonstration produced an observational association opposite in sign to the true population effect, while two individual effects had opposite signs.

See [`POPULATION-TO-INDIVIDUAL.md`](POPULATION-TO-INDIVIDUAL.md).

## 11. Human–AI distinction

Human–AI studies must separate:

```text
model-performed output
human-plus-model system capability
retained human capability
human agency, replacement, refusal, and exit
```

Immediate assisted task success is evidence only for the first two. Durable human augmentation requires measurements appropriate to the declared objective.

See [`HUMAN-AI-CAPABILITY-TRANSFER.md`](HUMAN-AI-CAPABILITY-TRANSFER.md).

## 12. Minimum useful study record

H0 retains this compact record:

```text
StudySpec
selected state and context domains
actions and events
observation provenance and uncertainty
time and history assumptions
causal graph or prediction assumptions
outcomes, horizon, values, and trade-offs
privacy, consequence, stopping, and deletion conditions
```

Additional structure requires a demonstrated analytical use. No universal database schema follows from this conceptual model.
