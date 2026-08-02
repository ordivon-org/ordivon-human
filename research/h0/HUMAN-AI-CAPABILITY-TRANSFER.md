# H0 Human–AI Capability Transfer

## Problem

“AI improves performance” and “AI harms learning” are both underspecified claims.

Recent randomized evidence points in different directions under different tasks and assistance structures:

- AI-supported cover-letter practice improved later unassisted writing in two preregistered experiments, though exposure to a high-quality AI example explained much of the gain;
- answer-oriented AI assistance in mathematical and reading tasks improved immediate performance but reduced later unassisted performance and persistence in the studied experiments.

The correct H0 conclusion is not that the studies cancel each other. It is that **AI assistance is not one intervention** and immediate output is not human capability.

## Four distinct objects

### 1. Model-performed output

What the model produced or directly supplied.

Examples:

- generated code, answer, explanation, plan, or text;
- errors corrected by the model;
- actions executed without requiring the human to possess the underlying skill.

This is model capability used on the person's behalf.

### 2. Human-plus-model system capability

What the coupled system can reliably achieve while the model, interface, context, tools, and access remain available.

This includes coordination costs, verification, latency, model failures, context quality, and the person's ability to direct the system.

A strong composite system is valuable even when the capability is not internalized by the person. It should be named accurately.

### 3. Retained human capability

What the person can do after assistance is removed or materially changed.

Minimum evidence can include:

- immediate unassisted performance;
- delayed retention;
- transfer to novel tasks;
- error detection and explanation;
- strategy generation;
- relearning rate after interruption.

Retained capability can increase, remain unchanged, or decline while assisted output improves.

### 4. Human agency over the system

Whether the person can:

- choose and revise the goal;
- understand when help is needed;
- direct and constrain the model;
- verify uncertain or consequential output;
- reject persuasive but unwanted recommendations;
- replace the provider or interaction mode;
- continue acceptably after loss of access;
- recognize dependence and decide whether it is acceptable.

Agency is not identical to independent task skill. A person may rationally depend on tools while retaining authorship, verification, replacement, and exit. Conversely, high output with no practical refusal or recovery may reduce agency.

## Minimum intervention description

A human–AI study must record the assistance mechanism, not only the model name:

```text
answer giving | examples | hints | critique | questions | decomposition
execution | retrieval | simulation | feedback | memory | social support
```

It should also record:

- whether assistance is optional or automatic;
- how quickly complete answers are available;
- whether the system adapts to learner state;
- whether the person must attempt before receiving help;
- whether explanations are inspectable;
- whether the model acts externally;
- whether the task and provider change at evaluation time.

## Minimum comparison design

A credible capability-transfer experiment should include, when the question permits:

1. baseline unassisted performance;
2. one or more precisely described assistance conditions;
3. an equivalent no-assistance or mature alternative baseline;
4. assisted task performance;
5. immediate unassisted performance after assistance;
6. delayed unassisted retention;
7. transfer to materially different tasks;
8. persistence, effort, help-seeking, and giving-up behaviour;
9. verification and confidence calibration;
10. ability to replace, refuse, and recover from the assistant.

Not every study needs all ten measures. A study cannot claim durable human augmentation when it measures only assisted output.

## Outcome vector

H0 rejects a single augmentation score. Report at least the relevant parts of this vector:

```text
assisted_output
joint_system_reliability
retained_capability
transfer
persistence_and_effort
verification_and_calibration
goal_authorship
replaceability_and_exit
dependence_cost
health_relationship_or_time_displacement
```

Trade-offs remain visible. For example, a system may increase joint output, preserve agency, and rationally reduce independent memorization. Another may increase output while degrading transfer and exit. These are different outcomes, not one scalar ranking.

## Retained Ordivon implication

Ordivon Human owns evidence about human change and agency. It may feed findings into:

- Harness interaction design;
- Host decision and interruption design;
- Ordivon Game behavioural experiments;
- Ordivon organization and adaptation research.

It does not gain authority to force “educational” friction into every workflow. Whether the user wants learning, delegation, speed, resilience, or another objective belongs in the StudySpec or Goal. The same complete answer can be harmful in a learning task and rational in an urgent execution task.
