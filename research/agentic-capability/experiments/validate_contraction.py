#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
AC = ROOT / "research" / "agentic-capability"
EXP = AC / "experiments"
HISTORICAL_RECEIPT = EXP / "evidence" / "contraction-20260814.json"
HISTORICAL_RECEIPT_DIGEST = (
    "sha256:836bd5035e31c1a3ed38cb6940a4e5fb489223b7ff5a01bfa5df982c41da572b"
)
CURRENT_PROJECTION = EXP / "evidence" / "contraction-current.json"


def sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def require_text(path: Path, needle: str) -> None:
    text = path.read_text(encoding="utf-8")
    if needle not in text:
        raise AssertionError(f"missing marker in {path.relative_to(ROOT)}: {needle!r}")


def main() -> None:
    required = [
        AC / "EVIDENCE-TRANSPORT.md",
        AC / "CONTRACTION-20260814.md",
        AC / "README.md",
        AC / "EVIDENCE-BASE.md",
        AC / "HYPOTHESES.md",
        AC / "EXPERIMENTS.md",
        ROOT / "research" / "QUESTIONS.md",
        ROOT / "docs" / "RESEARCH-PROGRAM.md",
        ROOT / "README.md",
        EXP / "R1-R6-ROUND-1.md",
        EXP / "r1-v1" / "HUMAN-PACKETS.md",
        EXP / "r2-v1" / "CAPABILITY-SURFACES.md",
        EXP / "r3-v1" / "HUMAN-AUDIT-PACKETS.md",
        EXP / "r4-v1" / "FAILURE-RECOVERY-MATRIX.md",
        EXP / "r6-v1" / "HUMAN-PREDICTIONS-WAVE-1.md",
        ROOT / "methods" / "m0" / "POPULATION-TO-INDIVIDUAL.md",
        EXP / "validate_contraction.py",
    ]
    for path in required:
        if not path.is_file():
            raise AssertionError(f"missing required file: {path.relative_to(ROOT)}")

    markers = {
        AC / "EVIDENCE-TRANSPORT.md": "residual experiment only if still decision-relevant",
        AC / "CONTRACTION-20260814.md": "General Human science × Ordivon system",
        AC / "README.md": "Post-Round-1 contraction — evidence transport first",
        AC / "EVIDENCE-BASE.md": "Evidence transport rule added after Round 1",
        AC / "HYPOTHESES.md": "Post-Round-1 hypothesis contraction",
        AC / "EXPERIMENTS.md": "Current priority override",
        ROOT / "research" / "QUESTIONS.md": "HUMAN-AI-001 evidence-transport update",
        ROOT / "docs" / "RESEARCH-PROGRAM.md": "HUMAN-AI-001 evidence-transport contraction",
        ROOT / "README.md": "HUMAN-AI-001 evidence-transport update",
        EXP / "R1-R6-ROUND-1.md": "Post-round contraction disposition",
        EXP / "r1-v1" / "HUMAN-PACKETS.md": "dormant fixture",
        EXP / "r2-v1" / "CAPABILITY-SURFACES.md": "support-condition accounting model",
        EXP / "r3-v1" / "HUMAN-AUDIT-PACKETS.md": "dormant fixture",
        EXP / "r4-v1" / "FAILURE-RECOVERY-MATRIX.md": "natural recovery evidence",
        EXP / "r6-v1" / "HUMAN-PREDICTIONS-WAVE-1.md": "not an active prediction request",
        ROOT / "methods" / "m0" / "POPULATION-TO-INDIVIDUAL.md": "personal data without those conditions would not solve the causal problem",
    }
    for path, needle in markers.items():
        require_text(path, needle)

    disposition = {
        "R1": "external_evidence_and_ordivon_allocation_first; direct_fixture_dormant",
        "R2": "support_condition_accounting; no_standing_scorecard",
        "R3": "interface_historical_adversarial_first; direct_fixture_dormant",
        "R4": "natural_recovery_first",
        "R5": "active_ordivon_specific_timescale_experiment",
        "R6": "conditional_forecast_tool; standing_wave_dormant",
    }

    if not HISTORICAL_RECEIPT.is_file():
        raise AssertionError(
            f"missing immutable historical receipt: {HISTORICAL_RECEIPT.relative_to(ROOT)}"
        )
    historical_digest = sha256(HISTORICAL_RECEIPT)
    if historical_digest != HISTORICAL_RECEIPT_DIGEST:
        raise AssertionError(
            "immutable historical contraction receipt changed: "
            f"expected={HISTORICAL_RECEIPT_DIGEST} actual={historical_digest}"
        )

    projection = {
        "schemaVersion": 1,
        "kind": "human-ai-evidence-first-contraction-current-compatibility",
        "projectionRole": "CURRENT_COMPATIBILITY",
        "principle": "external evidence -> transport analysis -> Ordivon structural/system evidence -> natural dogfood -> residual experiment",
        "disposition": disposition,
        "historicalReceipt": {
            "file": str(HISTORICAL_RECEIPT.relative_to(ROOT)),
            "digest": historical_digest,
            "date": "2026-08-14",
            "role": "IMMUTABLE_HISTORICAL_EVIDENCE",
        },
        "files": {str(path.relative_to(ROOT)): sha256(path) for path in required},
        "nonClaims": [
            "Current compatibility does not rewrite the 2026-08-14 receipt.",
            "Marker compatibility does not prove intervention effectiveness or retained Human skill.",
            "This projection does not admit a Learning Harness or universal allocation policy.",
        ],
    }
    CURRENT_PROJECTION.write_text(
        json.dumps(projection, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(CURRENT_PROJECTION)
    print(json.dumps(disposition, sort_keys=True))


if __name__ == "__main__":
    main()
