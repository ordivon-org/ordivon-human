# Initial Human Model

## 1. Why a dynamic model

A static table of age, height, weight, education, and income describes only one observation surface. Human outcomes emerge from interactions among current state, prior history, environment, behaviour, opportunity, and random events.

The initial model therefore uses three axes:

```text
levels of organization × variable type × time
```

## 2. Levels of organization

| Level | Research content | Typical observations |
|---|---|---|
| L0 — time and development | age, developmental stage, cohort, historical period, timing and duration | dates, age, exposure windows, transition history |
| L1 — biological substrate | genetics, anatomy, physiology, metabolism, immune and endocrine processes | biospecimens, clinical measures, family history |
| L2 — bodily functioning | mobility, sensory function, sleep, energy, pain, fitness, illness, recovery | physical measures, wearables, functional assessments |
| L3 — cognition and affect | attention, memory, reasoning, language, learning, emotion, motivation, regulation | tasks, behaviour, self-report, performance traces |
| L4 — identity and preferences | self-model, values, goals, personality, risk and time preferences, meaning | repeated reports, choices, narratives, behavioural consistency |
| L5 — behaviour | habits, routines, decisions, effort, avoidance, exploration, consumption, communication | logs, observation, transactions, repeated actions |
| L6 — capability | knowledge, skills, creativity, coordination, tool use, execution, adaptation | real tasks, portfolios, tests, transfer and learning curves |
| L7 — resources | money, assets, debt, time, housing, equipment, access, legal status, risk buffer | administrative and financial records, time budgets |
| L8 — relationships and institutions | family, peers, networks, organizations, norms, trust, authority, culture | network structure, roles, interaction and institutional data |
| L9 — environment and tools | physical environment, information exposure, technology, AI, economy, policy, historical shocks | environmental sensors, platform records, macro and policy data |

No level is the privileged explanation for every question. Reduction to biology can miss institutions; reduction to society can miss physiology; reduction to traits can miss changing opportunity and state.

## 3. Variable types

Every variable should be classified by its role in the study:

- **relatively stable attribute** — changes slowly within the observation window;
- **state** — current condition that may change rapidly;
- **behaviour** — an action or repeated action pattern;
- **resource** — something the person can draw upon or is constrained by;
- **environment** — conditions outside the person that shape opportunities and exposure;
- **event** — a discrete transition, shock, intervention, or encounter;
- **trajectory** — a sequence, trend, volatility pattern, or developmental path;
- **outcome** — the declared target of one analysis;
- **measurement** — the instrument and process producing an observation;
- **latent construct** — an inferred concept not directly observed;
- **confounder, mediator, moderator, or collider** — a causal role, not an intrinsic property of the variable.

The same quantity can occupy different roles in different studies. Sleep may be an outcome, exposure, mediator, or confounder depending on the question.

## 4. Time properties

For each observed variable, retain when relevant:

- level;
- direction and rate of change;
- volatility;
- persistence and half-life;
- lag before effects appear;
- recovery time;
- sensitivity to developmental timing;
- reversibility;
- minimum meaningful change;
- measurement frequency and missingness.

A trajectory often carries more information than a single value. Stable income and equally valued but highly volatile income imply different risk and autonomy. A one-time high performance and a sustained learning curve imply different capability.

## 5. Interactions and feedback

Expected structures include:

```text
sleep ↔ emotion regulation ↔ work quality ↔ stress
skills → income → time and tool access → further learning
social support → recovery → participation → stronger relationships
AI use → capability → task selection → learning or deskilling
health shock → income loss → treatment access → health trajectory
```

The project should search for thresholds, loops, bottlenecks, substitution, complementarity, and delayed effects rather than assuming independent additive variables.

## 6. Outcome families

No family is universally primary:

- survival and health;
- bodily and cognitive functioning;
- agency and autonomy;
- capability and learning;
- material security and option value;
- relationships and social participation;
- subjective well-being and suffering;
- creation, contribution, and meaning;
- resilience, recoverability, and adaptability.

Studies must also record adverse displacement: an intervention can improve productivity while worsening sleep, relationships, autonomy, or long-term learning.

## 7. Observation model

A recorded value should be treated as:

```text
observation = target phenomenon
            + instrument behaviour
            + respondent or observer behaviour
            + context
            + sampling and selection
            + random and systematic error
```

Agreement across methods raises confidence only when the methods do not share the same bias. A wearable, self-report, and platform log can all be wrong in correlated ways.

## 8. Minimum useful representation

H0 does not define a universal database schema. The minimum record for one study is:

```text
research question
population or person scope
construct and operational measure
observation time and context
source and instrument
uncertainty and missingness
causal role assumed
declared outcome and horizon
privacy class
```

Additional fields require a demonstrated analytical use.
