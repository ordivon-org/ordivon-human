# R5 v1 — Retrospective Timescale Replay

## Boundary

This is **hindsight-labeled hypothesis generation**, not prospective evidence.
Host exposes checkpoint times/digests but not arbitrary prior semantic payloads.
Only changes reconstructible from current final checkpoints and independent
continuity evidence are labeled.

A fixed-cadence rival is frozen at **60 minutes** for this v1 replay. Task
completion is treated as a natural final handoff, separate from preterminal
interruptions.

## Reconstructible sample

### Web Chromium recovery

- created: `1786619793898` ms
- rev2: `1786619793921`
- rev3: `1786621704113`
- rev4/final: `1786624452465`
- total duration: ~77.64 min
- final checkpoint explicitly states rev3's RTNL-deadlock diagnosis was
  superseded by direct falsifiers; actual cause was Unix-socket path overflow.

Policy consequences:

- every-checkpoint: 2 preterminal interruptions;
- fixed 60m: 1 preterminal review, occurring after rev3 and before rev4 — exactly
  while the wrong working hypothesis was current;
- hindsight event-trigger: 0 preterminal interruptions; final corrected state is
  the first clearly decision-changing Human handoff in the reconstructible data.

### Runtime P5

- created: `1786407242208` ms
- checkpoint revisions 2–9 at:
  `1786407242240, 1786408027861, 1786410540025, 1786411984643,
   1786413051562, 1786415305831, 1786417403958, 1786418226493`
- total duration: ~183.07 min
- independent FS0 continuity identifies rev6 as the point where production
  graduation exposed the hidden Windows launcher/release-provider coupling.

Policy consequences:

- every-checkpoint: 7 preterminal interruptions;
- fixed 60m: scheduled preterminal reviews at ~60, 120, and 180 min;
- critical rev6 falsifier occurred ~96.82 min after creation, so fixed 60m would
  next surface it at ~120 min: ~23.18 min detection delay;
- hindsight event-trigger can mark rev6 immediately and otherwise allow
  provider/release reconciliation to proceed until final handoff.

### Computing RF1

- created: `1786407514432` ms
- rev2: `1786407514456`
- rev3/final: `1786408950816`
- total duration: ~23.94 min
- final evidence falsified serial Agent stopping; no earlier reconstructible
  decision-changing semantic checkpoint is exposed.

Policy consequences:

- every-checkpoint: 1 preterminal interruption;
- fixed 60m: 0 preterminal interruptions;
- hindsight event-trigger: 0 preterminal interruptions.

## Aggregate exploratory counts

| Policy | Preterminal Human interruptions across 3 tasks | Known critical-delay issue |
|---|---:|---|
| every checkpoint | 10 | none by construction, highest interruption load |
| fixed 60m | 4 | Runtime critical falsifier ~23.18 min delayed; Web review lands on a later-rejected hypothesis |
| hindsight event trigger | 1 | zero in this hindsight-coded sample |

## Interpretation

The replay gives a **reason to test** event/evidence triggering prospectively,
not a reason to promote it. The event policy was labeled with knowledge of later
outcomes, while fixed cadence was frozen without such knowledge. The next round
must freeze trigger predicates before evaluated tasks start.
