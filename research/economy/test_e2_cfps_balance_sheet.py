#!/usr/bin/env python3
"""Standard-library acceptance tests for the E2 aggregate pipeline."""

from __future__ import annotations

import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT / "e2_cfps_balance_sheet.py"
WAVE_2020 = ROOT / "fixtures" / "cfps-e2-2020-synthetic.csv"
WAVE_2022 = ROOT / "fixtures" / "cfps-e2-2022-synthetic.csv"


class E2PipelineTests(unittest.TestCase):
    def run_pipeline(
        self,
        wave_2022: Path = WAVE_2022,
        *,
        minimum: int = 1,
    ) -> dict:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "result.json"
            subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--wave-2020",
                    str(WAVE_2020),
                    "--wave-2022",
                    str(wave_2022),
                    "--weight-2020",
                    "FSWT_NATCS20N",
                    "--weight-2022",
                    "FSWT_NATCS22N",
                    "--min-cell-size",
                    str(minimum),
                    "--output",
                    str(output),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            return json.loads(output.read_text(encoding="utf-8"))

    def test_synthetic_panel_and_negative_net_assets(self) -> None:
        result = self.run_pipeline()
        self.assertEqual(result["waves"]["2020"]["rows"], 16)
        self.assertEqual(result["waves"]["2022"]["rows"], 16)
        self.assertEqual(result["panel2020to2022"]["matchedOneToOneHouseholds"], 16)
        self.assertEqual(result["waves"]["2020"]["missingness"]["cash"]["missing"], 1)
        self.assertEqual(result["waves"]["2020"]["cashStatus"]["unknown"]["count"], 1)
        self.assertEqual(result["waves"]["2020"]["cashStatus"]["poor_constrained"]["count"], 2)
        self.assertEqual(result["waves"]["2022"]["cashStatus"]["poor_constrained"]["count"], 2)

    def test_split_household_links_are_excluded_and_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            split_file = Path(directory) / "wave-2022-split.csv"
            with WAVE_2022.open("r", encoding="utf-8", newline="") as source:
                rows = list(csv.DictReader(source))
                fieldnames = list(rows[0])
            duplicate = dict(rows[0])
            duplicate["FID22"] = "2999"
            rows.append(duplicate)
            with split_file.open("w", encoding="utf-8", newline="") as target:
                writer = csv.DictWriter(target, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

            result = self.run_pipeline(split_file, minimum=5)
            panel = result["panel2020to2022"]
            self.assertEqual(panel["splitHouseholdLinks"], 1)
            self.assertEqual(panel["splitFollowupRows"], 2)
            self.assertEqual(panel["matchedOneToOneHouseholds"], 15)
            suppressed = [
                cell
                for cell in panel["cashStatusTransitions"]["cells"]
                if cell["display"] == "<5"
            ]
            self.assertTrue(suppressed)
            self.assertTrue(all(cell["count"] is None for cell in suppressed))

    def test_output_contains_no_household_ids(self) -> None:
        result = self.run_pipeline()
        serialized = json.dumps(result)
        for household_id in ("1001", "1016", "2001", "2016"):
            self.assertNotIn(f'"{household_id}"', serialized)


if __name__ == "__main__":
    unittest.main()
