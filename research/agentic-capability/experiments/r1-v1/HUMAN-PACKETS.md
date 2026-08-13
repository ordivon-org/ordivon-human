# R1 v1 — Frozen Human Learning Packets

> Do not read `SCORING-KEY.md` before the Human response is frozen. The three
> cases are intentionally assigned different treatments. Wave 1 is exploratory
> because case difficulty and treatment are confounded within one Human.

## Case runtime-p5 — RAW bounded evidence condition

### Source identity

- Host Task: `task:runtime:rsi-p5-foundation-closeout-20260811`
- frozen checkpoint: revision 9
- checkpoint digest: `sha256:e283d718daa44b571d63d7347f392251e9f1699d11df50b8d4da67f287dfc529`

### Bounded evidence record

P5 began as a Runtime foundation closeout. Stable trusted-local Cargo
presentation and Windows immutable-input semantics were already source/acceptance
complete. Production graduation then falsified a release/provider assumption:
the Linux Runtime release emitted new Windows launcher input flags while
production still referenced the older launcher binary, so a production
`windows_native execBound` became LOST before start evidence.

The repair remained target-specific rather than creating a generic provider
framework. Windows provider contract V2 was introduced for new admission while
V1 remained historical replay compatibility. The release candidate bound exact
content-addressed launcher bytes, an atomic `ORDIVON_WINDOWS_LAUNCHER_PATH`
transition, and receipt-bound rollback/reconciliation. A first release attempt
from the same Workspace was rejected with `CONCURRENCY_LIMIT` because the bridge
Job itself occupied the Workspace's slot; `commitState=not_started` and
`retryClass=safe_same_request` showed that structured release did not bypass
capacity. A dedicated clean release Workspace then admitted the release effect.

During Runtime self-replacement, one `task.observe` transport was interrupted
and entered an UNKNOWN/ExceptionGroup window. The task did **not** classify this
as release failure. `release.get` reconciled from deterministic receipt truth and
established `effectDisposition=deployed`; the generic release Job later
converged to succeeded/committed. Exact replay of the same `release.apply`
request returned `replayed=true` with the same effect, Job and receipt, proving
there was no duplicate physical replacement.

A subsequent production `windows_native workspace.execBound` read the committed
immutable input and had overwrite and sibling creation denied under the limited
token. Terminal evidence bound the source revision, execution target, provider
V2 digest, limited token and exact input set. A final audit confirmed deployed
commit, release artifacts, Registry schema 4, 22 Tools, no recovery-required
cases, active service, and canonical/source/deployment convergence.

Important rejected paths included: inferring failure from transport loss during
self-replacement; cancelling unrelated Jobs to make release pass; reusing V1 for
new admission; abstracting a generic provider framework from one target-specific
coupling; and reopening P0–P5 merely because the architecture looked imperfect.

### Human response — answer without external help

1. In your own words, what was the **causal defect**, not merely the visible
   failure?
2. Why was the interrupted `task.observe` not sufficient evidence that the
   release failed? Name the stronger evidence boundary.
3. Novel transfer: suppose a future database migration command loses its client
   connection after the server commits a transaction and writes a durable
   receipt. What principle from this case should govern retry/reconciliation?
4. Seeded-error check: evaluate this claim — “The right fix was to cancel other
   Runtime Jobs and immediately re-run the release until the Windows Job starts.”
   State whether it is supported and why.
5. What minimum Human understanding would be useful if the same class of failure
   recurred with a different external provider?

Record approximate reading + response time before consulting any answer key.

---

## Case computing-rf1 — NORMAL SUMMARY condition

### Source identity

- Host Task: `task:computing:rf0-rf1-research-stopping-20260811`
- frozen checkpoint: revision 3
- checkpoint digest: `sha256:6a5ad817a5293ca384adcdbd85d4b228fb057e967901fded57663e6bc0577895`

### Summary

Computing tested whether an Agent could save research cost by inspecting a
six-window Game trajectory progressively and deciding when to STOP. The
prediction was that useful marginal-evidence stopping would often use less than
75% of the available windows. A full-evidence baseline and matched one-shot
comparison were frozen.

The result went the other way. Across eight accepted trajectories, the
progressive policy never stopped early: all 8/8 used all six windows. Even after
seeing the same complete evidence, progressive serial acquisition agreed with
unanimous full-evidence references only 6/8; both disagreements occurred on the
hard Hive-hunt cases. Progressive also used about 2.3× the Provider tokens and
about 2.8× the elapsed Provider time of the matched one-shot full-evidence
condition.

The retained conclusion was narrow: on a small finite evidence universe that is
cheap enough to inspect in one bounded synthesis, serial Agent-controlled
observe/STOP loops can be worse than full inspection because selection overhead
and semantic path dependence dominate the savings they are supposed to create.
The experiment did **not** conclude that stopping is useless in general; it left
open evidence spaces where full inspection is genuinely expensive.

### Human response — answer without external help

1. What hypothesis did RF1 falsify, and what broader hypothesis did it **not**
   falsify?
2. Why is “the progressive policy had zero false early stops” not positive
   evidence here?
3. Novel transfer: if you have only five short log segments and one model call can
   inspect all five cheaply, what default does this result suggest? What fact
   would make you reconsider?
4. Seeded-error check: evaluate — “Adaptive evidence acquisition was cheaper
   because it was selective by design.”
5. What is the main mechanism by which equal eventual evidence can still produce
   different conclusions in this experiment?

Record approximate reading + response time before consulting any answer key.

---

## Case harness-p0 — ACTIVE DISTILLATION condition

### Source identity

- Host Task: `task:harness:p0-composition-friction-ablation-20260813`
- frozen checkpoint: revision 3
- checkpoint digest: `sha256:6db838a0a45d24159a11b53f88cb805bd6e49fd6e395973165e80f463fda58cb`

### Problem

Harness had real composition capability, but Agents often had to reconstruct
installed Tool surfaces and Run composition from source. The risk was to solve
that friction by adding a new global registry/composer that would duplicate
existing authority.

### Mechanism candidate

Expose **generated discovery and read-only explanation** derived from existing
source-owned Tool definitions and current Run state. Keep installed → Run
admitted → turn admitted authority stages separate. Add a specialized explicit
Tool-surface seam only if real distinct consumers demonstrate the need.

### Decisive evidence

- Baseline focused tests passed but exposed only one CLI profile and hard-coded
  two ordinary Tool surfaces.
- Catalog treatment exposed four source-owned installed surfaces without adding
  grant authority.
- Catalog + explain/workbench made composition and durable proof boundaries
  inspectable without source-code reconstruction or liveness guessing.
- A specialized seam was retained only after a third real consumer existed.
- Final acceptance passed 357 tests / 3 skips plus static and contract gates.

### Rivals / deletions

Rejected or shrunk: global registry/plugin tree, second `CompositionSpec`, new
workbench persistence, stable public API expansion merely because it looked
cleaner, and any UX improvement that weakened authority/recovery/privacy.

### Boundary

The retained result is **not** “make everything globally discoverable.” It is:
make effective capability legible by projection from existing owners, and add
new shared composition authority only when repeated real consumers force it.

### Active reconstruction — do this before looking back

Without rereading the sections above, answer:

1. Reconstruct the causal chain from hidden composition friction to the retained
   solution in 3–5 sentences.
2. Why does a generated catalog differ from a second authority registry?
3. Novel transfer: another Ordivon project has correct capabilities but Agents
   repeatedly read five source files to discover them. What is the first class of
   solution this case suggests testing? What should *not* be added by default?
4. Seeded-error check: evaluate — “P0 proved that all specialized Tool surfaces
   should be promoted to stable package-root APIs.”
5. Name one falsifier that would make the retained projection insufficient.

Record approximate reading + response time before consulting any answer key.
