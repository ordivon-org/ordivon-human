#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def assignment(seed: str, cases: list[str], conditions: list[str]) -> dict[str, str]:
    ordered = sorted(
        (int(hashlib.sha256(f"{seed}:{case}".encode()).hexdigest(), 16), case)
        for case in cases
    )
    return {case: conditions[i] for i, (_, case) in enumerate(ordered)}


def r5_replay() -> dict:
    samples = {
        "web-chromium": {
            "created": 1786619793898,
            "checkpoints": [1786619793921, 1786621704113, 1786624452465],
            "critical": None,
        },
        "runtime-p5": {
            "created": 1786407242208,
            "checkpoints": [
                1786407242240,
                1786408027861,
                1786410540025,
                1786411984643,
                1786413051562,
                1786415305831,
                1786417403958,
                1786418226493,
            ],
            "critical": 1786413051562,
        },
        "computing-rf1": {
            "created": 1786407514432,
            "checkpoints": [1786407514456, 1786408950816],
            "critical": None,
        },
    }

    rows = {}
    every_total = 0
    fixed_total = 0
    for name, sample in samples.items():
        created = sample["created"]
        end = sample["checkpoints"][-1]
        duration_min = (end - created) / 60000
        every_preterminal = len(sample["checkpoints"]) - 1
        # Reviews at 60, 120, ... minutes strictly before completion.
        fixed_preterminal = int(duration_min // 60)
        delay = None
        if sample["critical"] is not None:
            critical_min = (sample["critical"] - created) / 60000
            next_fixed = (int(critical_min // 60) + 1) * 60
            if next_fixed < duration_min:
                delay = next_fixed - critical_min
            else:
                delay = duration_min - critical_min
        rows[name] = {
            "durationMinutes": round(duration_min, 4),
            "everyCheckpointPreterminal": every_preterminal,
            "fixed60Preterminal": fixed_preterminal,
            "criticalDetectionDelayFixed60Minutes": None if delay is None else round(delay, 4),
        }
        every_total += every_preterminal
        fixed_total += fixed_preterminal

    return {
        "samples": rows,
        "aggregate": {
            "everyCheckpointPreterminal": every_total,
            "fixed60Preterminal": fixed_total,
            "hindsightEventTriggeredPreterminal": 1,
            "runtimeP5KnownCriticalDelayFixed60Minutes": rows["runtime-p5"]["criticalDetectionDelayFixed60Minutes"],
        },
        "boundary": "event-trigger count is hindsight-labeled hypothesis generation, not prospective evidence",
    }


def main() -> None:
    r1 = json.loads((ROOT / "r1-v1" / "manifest.json").read_text())
    r3 = json.loads((ROOT / "r3-v1" / "manifest.json").read_text())

    r1_expected = assignment(
        r1["seed"],
        [c["caseId"] for c in r1["cases"]],
        ["raw", "summary", "active_distillation"],
    )
    r1_actual = {c["caseId"]: c["condition"] for c in r1["cases"]}
    assert r1_actual == r1_expected, (r1_actual, r1_expected)

    r3_expected = assignment(
        r3["seed"],
        list(r3["assignments"]),
        ["full", "selective", "conclusion_only"],
    )
    assert r3["assignments"] == r3_expected, (r3["assignments"], r3_expected)

    required = [
        ROOT / "R1-R6-ROUND-1.md",
        ROOT / "r1-v1" / "manifest.json",
        ROOT / "r1-v1" / "HUMAN-PACKETS.md",
        ROOT / "r1-v1" / "SCORING-KEY.md",
        ROOT / "r2-v1" / "CAPABILITY-SURFACES.md",
        ROOT / "r3-v1" / "manifest.json",
        ROOT / "r3-v1" / "HUMAN-AUDIT-PACKETS.md",
        ROOT / "r3-v1" / "SCORING-KEY.md",
        ROOT / "r4-v1" / "FAILURE-RECOVERY-MATRIX.md",
        ROOT / "r5-v1" / "RETROSPECTIVE.md",
        ROOT / "r5-v1" / "PROSPECTIVE-POLICIES.json",
        ROOT / "r6-v1" / "PROTOCOL.json",
        ROOT / "r6-v1" / "FS0-PREFLIGHT.md",
        ROOT / "r6-v1" / "HUMAN-PREDICTIONS-WAVE-1.md",
    ]
    for path in required:
        assert path.is_file(), path

    receipt = {
        "schemaVersion": 1,
        "experiment": "HUMAN-AI-001/R1-R6-round1",
        "status": "apparatus_validated_human_endpoints_partial_or_pending",
        "r1Assignment": r1_actual,
        "r3Assignment": r3["assignments"],
        "r5": r5_replay(),
        "files": {str(p.relative_to(ROOT)): sha256(p) for p in required},
    }
    out = ROOT / "evidence" / "r1-r6-round1.json"
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(out)
    print(json.dumps(receipt["r5"]["aggregate"], sort_keys=True))


if __name__ == "__main__":
    main()
