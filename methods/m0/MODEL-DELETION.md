# Methods M0 Model Deletion

## Problem with the initial model

The initial `L0–L9` table was useful for recall, but it was not a minimum model. It placed unlike objects on one axis:

- body and cognition were state domains;
- behaviour was a transition input;
- resources and institutions were situated conditions;
- time and development were axes;
- tools were environmental mechanisms;
- measurement and outcome were study definitions.

Treating all of them as levels encouraged field accumulation and hid causal structure.

## Level deletion results

| Initial element | H0 decision | Reason |
|---|---|---|
| L0 time and development | remove as a level; retain as a temporal axis | time conditions every domain and cannot be localized to one level |
| L1 biological substrate + L2 bodily functioning | merge into **body state** | the five H0 cases need bodily mechanisms and functioning but do not require two permanent top-level compartments |
| L3 cognition and affect + L4 identity and preferences | merge into **mind state** | cognition, affect, motivation, identity, values, and preferences interact and can remain typed subdomains when a study needs them |
| L5 behaviour | remove as a state level; retain as **action** | behaviour changes state and context; representing it as another static layer obscures the transition |
| L6 capability | retain as **capability state** | current performance, learned capacity, transfer, and retained ability must remain distinct from action and assisted output |
| L7 resources + L8 relationships and institutions | merge into **situated state** | assets, time, roles, rights, relationships, and access determine current options and are often relational rather than purely internal or external |
| L9 environment and tools | retain as **context** | physical, informational, technological, economic, and institutional conditions can change without changing the person's internal state |

The result is not six mandatory database sections. They are selectable domains in one dynamic model.

## Variable-role deletion results

| Initial role | H0 decision | Replacement |
|---|---|---|
| relatively stable attribute | delete as a role | a state with empirically estimated persistence |
| state | retain | current person or situated condition |
| behaviour | rename and retain | action |
| resource | delete as a generic role | a typed element of situated state or context |
| environment | delete as a generic role | context |
| event | retain | event or intervention |
| trajectory | delete as a primitive | a derived pattern over states, actions, contexts, and events |
| outcome | retain | a study-selected target with owner, horizon, and value assumptions |
| measurement | retain and strengthen | observation with instrument, source, timing, uncertainty, and missingness |
| latent construct | delete as a role | epistemic status: inferred rather than directly observed |
| confounder, mediator, moderator, collider | keep outside the ontology | roles assigned by a study-specific causal graph; moderation is an interaction claim |

## Retained minimum model

```text
StudySpec
  question
  scope: population or person
  outcome(s), owner, horizon, value assumptions
  estimand or prediction target

PersonState_t
  body
  mind
  capability
  situated state: resources, roles, rights, relationships, access

Context_t
  institutions and norms
  physical conditions
  information environment
  technologies and AI
  economy and historical conditions

Action_t
EventOrIntervention_t
History_(0:t)

Observation_t = Measurement(
  selected PersonState,
  Context,
  Action,
  Event,
  Outcome
) + error and selection
```

A transition hypothesis has the form:

```text
PersonState_(t+1), Context_(t+1)
  = F(PersonState_t, Context_t, Action_t, Event_t, History_(0:t), uncertainty)
```

This is a conceptual research model, not a requirement to persist every term.

## Case deletion matrix

| Component | Sleep and cognition | Skill and resources | Shock and recovery | AI assistance | Relationships and well-being | Retain? |
|---|---:|---:|---:|---:|---:|---|
| body state | required | conditional | required | conditional | conditional | yes, selectable |
| mind state | required | required | conditional | required | required | yes, selectable |
| capability state | conditional | required | conditional | required | conditional | yes, selectable |
| situated state | conditional | required | required | required | required | yes, selectable |
| context | required | required | required | required | required | yes |
| action | required | required | required | required | required | yes |
| event or intervention | conditional | conditional | required | required | conditional | yes |
| time and history | required | required | required | required | required | yes |
| observation process | required | required | required | required | required | yes |
| explicit outcomes and values | required | required | required | required | required | yes |

A component survives when removing it causes at least one concrete case to confuse the unit, mechanism, evidence, or objective. “Selectable” means the model can represent the domain; it does not mean every study collects it.

## Deletions that matter

H0 rejects the following tempting structures:

- a permanent ten-level hierarchy;
- a stable-trait table separate from time-series state;
- resources and environment as universal variable roles;
- trajectory as stored truth rather than a derived interpretation;
- latent constructs as if they were directly observed fields;
- causal roles embedded permanently in variable definitions;
- an aggregate human score;
- a requirement to instantiate every domain;
- a universal human database schema.

## Why the retained model is not empty abstraction

The model changes real analysis in four ways:

1. it prevents population differences from being used as claims about personal change;
2. it requires actions and interventions to be separated from state;
3. it binds claims to measurement and selection processes;
4. it prevents assisted output from being mistaken for retained human capability or agency.

Those failures appear in the H0 simulation and human–AI evidence contract. The retained distinctions therefore have current consumers.
