# R1 v1 — Scoring Key

> Keep hidden from the Human until all R1 responses for this wave are frozen.

Each question is scored 0/1/2. Do not award points for matching vocabulary alone;
score the causal distinction.

## runtime-p5

1. **2:** identifies release/provider version discontinuity: new Runtime protocol/flags
   were paired with an old production Windows launcher, so source success did not
   imply provider-release continuity. **1:** says version mismatch/provider drift
   without the release-boundary mechanism. **0:** blames Windows immutable input
   generally.
2. **2:** transport loss/UNKNOWN is not effect truth; reconcile using the durable
   structured release receipt / `release.get` and exact replay semantics. **1:**
   says check server state/logs but not the receipt boundary. **0:** retry as new
   effect immediately.
3. **2:** treat response loss as uncertain delivery, query idempotent/durable
   transaction identity/receipt, replay same request only under declared semantics,
   avoid duplicate effect. **1:** verify before retry. **0:** new retry blindly.
4. **2:** rejects: unrelated reservations are real capacity constraints; release
   must wait/fail closed, and cancellation changes unrelated user effects. **1:**
   rejects without authority/capacity reasoning. **0:** accepts.
5. **2:** enough to recognize operation identity, provider/version binding,
   authoritative receipt/reconciliation, and when to avoid duplicate external
   effects; full launcher implementation memory is unnecessary. **1:** generic
   debugging only. **0:** either memorize all code or know nothing.

## computing-rf1

1. **2:** falsified serial per-observation Agent STOP as default on a small cheap
   finite universe; did not falsify stopping/selective observation when the full
   universe is expensive. **1:** only first half. **0:** says all stopping fails.
2. **2:** there were zero autonomous early-stop opportunities because every trial
   consumed all windows; denominator/event never occurred. **1:** notes metric is
   uninformative. **0:** treats zero as success.
3. **2:** default to one-shot full bounded synthesis; reconsider when full evidence
   is materially expensive/large and selection overhead can amortize. **1:** full
   inspect without reconsideration condition. **0:** serial STOP by default.
4. **2:** rejects; progressive used all evidence and cost ~2.3× tokens/~2.8× time.
   **1:** rejects without cost mechanism. **0:** accepts.
5. **2:** semantic/dialogue path dependence from sequential acquisition; same
   eventual evidence set can be interpreted differently because prior turns alter
   model state/context. **1:** vague ordering effect. **0:** random noise only.

## harness-p0

1. **2:** hidden-but-correct composition forced repeated source reconstruction;
   generated catalog/explain exposed existing owner truth; specialized shared seam
   was admitted only after repeated consumer evidence, while authority stayed in
   existing layers. **1:** captures projection but not admission/authority. **0:**
   says new global registry solved it.
2. **2:** catalog is derived read-only projection from source owners and grants no
   new authority; registry would become another canonical owner/grant plane. **1:**
   says catalog is read-only. **0:** no distinction.
3. **2:** first test owner-derived capability discovery/explain projection; do not
   add global registry/new persistent owner/shared abstraction without repeated
   demand. **1:** only projection. **0:** build registry.
4. **2:** rejects; stable API expansion was deliberately shrunk and specialized seam
   remained advanced/conditional until evidence. **1:** rejects vaguely. **0:** accepts.
5. **2:** examples include repeated real consumers needing composition that projection
   cannot express, inability to make a required Run/effective boundary legible, or
   evidence that source reconstruction remains materially costly after projection.
   **1:** plausible but weak falsifier. **0:** aesthetic preference.

## Interpretation

Do not compare raw totals causally across conditions in wave 1. Case difficulty is
confounded with condition. Use the wave to validate burden, scoring sensitivity,
and identify gross failures. Rotate conditions across new cases in later waves.
