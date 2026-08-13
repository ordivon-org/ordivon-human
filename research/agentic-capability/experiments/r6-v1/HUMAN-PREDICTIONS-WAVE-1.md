# R6 v1 — Human Prediction Wave 1

> Freeze the claims and resolution rules before entering Human probabilities.
> The Human should provide only probabilities (0–100%) plus at most one decisive
> reason and one change-my-mind condition. Do not edit the claim after outcomes
> begin resolving.

## H6-01 — Active distillation earns a measurable learning advantage

**Exact claim:** after at least two additional condition-rotated R1 waves (minimum
six new case exposures in total), the active-distillation condition will exceed
the normal-summary condition by at least **0.5 points** on mean combined
`novel_transfer + seeded_error_detection` score (each component 0–2), while its
median Human attention time is no more than **1.5×** the normal-summary median.

**Resolution:** use only prospectively frozen R1 waves with condition rotation;
wave 1 alone cannot resolve this because case and treatment are confounded.

**Human probability:** ___ %

**One decisive reason:** ___

**One condition that would change the estimate:** ___

## H6-02 — Selective audit preserves most critical defect detection

**Exact claim:** after at least six new condition-rotated R3 cases, selective
audit will detect at least **80%** as many predeclared critical defects as bounded
full review while using no more than **70%** of its median Human review time.

**Resolution:** score only defects frozen before review; do not count generic
requests for more information as detection unless they target the decisive
uncertainty.

**Human probability:** ___ %

**One decisive reason:** ___

**One condition that would change the estimate:** ___

## H6-03 — Event-triggered synchronization is non-dominated

**Exact claim:** over the next five eligible prospectively observed Ordivon Tasks,
`eventTriggeredV1` will reduce preterminal Human interruptions by at least **40%**
relative to every-checkpoint review, will miss **zero** predeclared critical
escalations whose later correction cost is material, and will not be dominated by
the fixed-60-minute policy on both interruption load and critical detection.

**Resolution:** use the exact trigger set frozen in
`../r5-v1/PROSPECTIVE-POLICIES.json`; later edits create a new policy version and
cannot repair this prediction retrospectively.

**Human probability:** ___ %

**One decisive reason:** ___

**One condition that would change the estimate:** ___

## Scoring boundary

Three forecasts are not enough to infer stable Human calibration. They seed a
series. Use Brier-style scoring only after comparable binary events accumulate;
preserve causal reason quality and update behavior separately from the numeric
score.


## Contraction status

`H6-01..03` remain frozen historical apparatus but are **not an active prediction request**. Do not collect probabilities merely to populate a calibration series. Reopen a forecast only when the underlying decision independently earns a record under R6 admission rules.
