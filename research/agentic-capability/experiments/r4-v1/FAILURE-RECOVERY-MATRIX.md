# R4 v1 — Delegation / Failure Recovery Matrix

## Purpose

Test **intervention-capable substrate**, not full unaided craftsmanship. Each
scenario is derived from a real Ordivon failure class but is presented without
the hidden cause during Human testing.

| Scenario | Hidden perturbation | Useful retained substrate | Success criterion |
|---|---|---|---|
| R4-A effect uncertainty | client observation disappears during a durable external effect | operation identity, receipt/reconciliation, duplicate-effect risk | asks for authoritative effect evidence before retry; avoids new-id duplicate effect |
| R4-B environment/provider mismatch | caller emits a newer contract than the external provider actually implements | contract/version boundary, producer-vs-provider distinction, exact identity | localizes mismatch to cross-release/provider boundary rather than blaming domain semantics |
| R4-C browser substrate | browser runner fails inside isolated workspace; prior network-deadlock hypothesis exists | hypothesis falsification, OS path/resource boundary, minimal control-plane probe | tests old hypothesis, uses a short-temp/control-plane discriminator, avoids changing Web semantics |

## Human substrate probes

Do **not** ask the Human to reproduce implementation code. Before each recovery
attempt record whether they can:

1. reconstruct the relevant system boundary;
2. name one discriminating observation;
3. choose a reversible next action;
4. identify what would make retry unsafe;
5. switch to an alternative evidence path if the preferred tool is unavailable.

## Current real-system evidence

- Runtime P5 proves R4-A/R4-B are real classes: transport UNKNOWN required receipt
  reconciliation, and production graduation exposed a Linux Runtime ↔ Windows
  launcher contract discontinuity after source-level acceptance.
- Web Chromium recovery proves R4-C: the rev3 RTNL-deadlock hypothesis was later
  falsified; the actual reproducible cause was Unix socket path overflow from a
  long Runtime TMPDIR before Playwright import. A short temp root plus a minimal
  Playwright launch was the decisive discriminator; Web semantics and Runtime
  isolation did not need weakening.

## Current result

**System failure classes validated; Human substrate effect pending.** These cases
show that recovery needs boundary/evidence reasoning, but they do not prove how
much of that substrate the Human currently retains or how much practice is worth
maintaining.
