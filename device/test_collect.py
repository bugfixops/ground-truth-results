"""Tests for device/collect.py (brief D5 acceptance).

Run: python3 -I device/test_collect.py
Builds a synthetic collected/ folder with a results artifact (including
a screenshot and a UI dump that must NOT be copied) and a dry-run
artifact, runs collect.py, and asserts only allowlisted text outputs
plus SUMMARY.md counts. TestCollectFlatFallback covers the flat
fallback: collected/ with no device-* directory but with
dryrun_report.txt and/or results.csv at its top level.
"""

import csv
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import collect  # noqa: E402


class TestCollect(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        col = os.path.join(self.tmp.name, "collected")
        cur = os.path.join(col, "device-Currency")
        os.makedirs(os.path.join(cur, "steps"))
        os.makedirs(os.path.join(cur, "screens", "route_01"))
        os.makedirs(os.path.join(cur, "dumps", "route_01"))
        with open(os.path.join(cur, "results.csv"), "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["app", "route", "method", "edges", "reached",
                        "script_status", "steps_done", "steps_total",
                        "error", "run_id"])
            w.writerow(["Currency", "route_01", "M.a", "E1 E2", "yes", "ok",
                        "3", "3", "", "r1"])
            w.writerow(["Currency", "route_02", "M.b", "E3", "no",
                        "failed_at_step_2", "1", "4", "", "r1"])
            w.writerow(["Currency", "route_03", "M.c", "E4", "not_run",
                        "unscriptable", "0", "0", "needs hardware", "r1"])
        with open(os.path.join(cur, "run.log"), "w") as f:
            f.write("run started\n")
        with open(os.path.join(cur, "steps", "route_01.log"), "w") as f:
            f.write("2026-01-01T00:00:00Z E1 tap ok\n")
        with open(os.path.join(cur, "steps", "route_02.log"), "w") as f:
            f.write("2026-01-01T00:00:00Z E3 tap ok\n")
        with open(os.path.join(cur, "screens", "route_01", "shot.png"),
                  "wb") as f:
            f.write(b"\x89PNG-not-a-real-image")
        with open(os.path.join(cur, "dumps", "route_01", "ui.xml"),
                  "w") as f:
            f.write("<hierarchy/>")
        dry = os.path.join(col, "device-Diary")
        os.makedirs(dry)
        with open(os.path.join(dry, "dryrun_report.txt"), "w") as f:
            f.write("route_01 PASS\nroute_02 PASS\nroute_03 FAIL no script\n"
                    "Diary: 2 PASS, 1 FAIL\n")
        with open(os.path.join(dry, "run.log"), "w") as f:
            f.write("dry run\n")
        self.collected = col
        self.dest = os.path.join(self.tmp.name, "dest")

    def test_collect(self):
        self.assertEqual(collect.main([self.collected, self.dest]), 0)
        # Allowlisted text copied verbatim.
        self.assertTrue(os.path.isfile(
            os.path.join(self.dest, "Currency", "results.csv")))
        self.assertTrue(os.path.isfile(
            os.path.join(self.dest, "Currency", "steps", "route_01.log")))
        self.assertTrue(os.path.isfile(
            os.path.join(self.dest, "Diary", "dryrun_report.txt")))
        # Screenshots and dumps never copied, anywhere under dest.
        for root, _dirs, files in os.walk(self.dest):
            for name in files:
                self.assertFalse(name.endswith(".png"), name)
                self.assertFalse(name.endswith(".xml"), name)
        # SUMMARY.md counts.
        with open(os.path.join(self.dest, "SUMMARY.md")) as f:
            summary = f.read()
        self.assertIn("| 3 | 1 | 1 | 1 | 1 |", summary)  # Currency row
        self.assertIn("| 2 | 1 |", summary)  # Diary PASS/FAIL row
        self.assertIn("Currency", summary)
        self.assertIn("Diary", summary)


class TestCollectFlatFallback(unittest.TestCase):
    """collected/ with no device-* dir but flat report/results files."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.collected = os.path.join(self.tmp.name, "collected")
        os.makedirs(self.collected)
        self.dest = os.path.join(self.tmp.name, "dest")

    def _summary(self):
        with open(os.path.join(self.dest, "SUMMARY.md")) as f:
            return f.read()

    def _write_results(self, app="MMEX"):
        with open(os.path.join(self.collected, "results.csv"),
                  "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["app", "route", "method", "edges", "reached",
                        "script_status", "steps_done", "steps_total",
                        "error", "run_id"])
            w.writerow([app, "route_01", "M.a", "E1", "yes", "ok",
                        "3", "3", "", "r1"])
            w.writerow([app, "route_02", "M.b", "E2", "no",
                        "failed_at_step_1", "0", "2", "", "r1"])
            w.writerow([app, "route_03", "M.c", "E3", "not_run",
                        "unscriptable", "0", "0", "needs account", "r1"])

    def test_flat_dryrun_report_only(self):
        with open(os.path.join(self.collected, "dryrun_report.txt"),
                  "w") as f:
            f.write("route_01 PASS\nroute_02 FAIL no script\n"
                    "MMEX: 1 PASS, 1 FAIL\n")
        with open(os.path.join(self.collected, "run.log"), "w") as f:
            f.write("dry run\n")
        os.makedirs(os.path.join(self.collected, "steps"))
        with open(os.path.join(self.collected, "steps", "route_01.log"),
                  "w") as f:
            f.write("tap ok\n")
        self.assertEqual(collect.main([self.collected, self.dest]), 0)
        self.assertTrue(os.path.isfile(
            os.path.join(self.dest, "MMEX", "dryrun_report.txt")))
        self.assertTrue(os.path.isfile(
            os.path.join(self.dest, "MMEX", "steps", "route_01.log")))
        summary = self._summary()
        self.assertIn("## MMEX", summary)
        self.assertIn("| 1 | 1 |", summary)
        self.assertNotIn("No device-* artifacts found.", summary)

    def test_flat_results_csv_only(self):
        self._write_results()
        self.assertEqual(collect.main([self.collected, self.dest]), 0)
        self.assertTrue(os.path.isfile(
            os.path.join(self.dest, "MMEX", "results.csv")))
        summary = self._summary()
        self.assertIn("## MMEX", summary)
        self.assertIn("| 3 | 1 | 1 | 1 | 1 |", summary)
        self.assertNotIn("No device-* artifacts found.", summary)

    def test_flat_both_prefers_dryrun_report(self):
        with open(os.path.join(self.collected, "dryrun_report.txt"),
                  "w") as f:
            f.write("route_01 PASS\nMMEX: 1 PASS, 0 FAIL\n")
        self._write_results(app="Diary")
        self.assertEqual(collect.main([self.collected, self.dest]), 0)
        self.assertTrue(os.path.isdir(os.path.join(self.dest, "MMEX")))
        self.assertFalse(os.path.isdir(os.path.join(self.dest, "Diary")))
        self.assertIn("## MMEX", self._summary())

    def test_flat_report_without_summary_line_falls_back_to_results(self):
        with open(os.path.join(self.collected, "dryrun_report.txt"),
                  "w") as f:
            f.write("route_01 PASS\nroute_02 PASS\n")
        self._write_results(app="Diary")
        self.assertEqual(collect.main([self.collected, self.dest]), 0)
        self.assertTrue(os.path.isdir(os.path.join(self.dest, "Diary")))
        self.assertIn("## Diary", self._summary())

    def test_flat_report_without_summary_line_and_no_results(self):
        # No name can be derived: no section is invented.
        with open(os.path.join(self.collected, "dryrun_report.txt"),
                  "w") as f:
            f.write("route_01 PASS\nroute_02 PASS\n")
        self.assertEqual(collect.main([self.collected, self.dest]), 0)
        self.assertIn("No device-* artifacts found.", self._summary())

    def test_empty_collected_still_no_artifacts(self):
        self.assertEqual(collect.main([self.collected, self.dest]), 0)
        self.assertIn("No device-* artifacts found.", self._summary())

    def test_device_dirs_win_over_flat_files(self):
        dry = os.path.join(self.collected, "device-MMEX")
        os.makedirs(dry)
        with open(os.path.join(dry, "dryrun_report.txt"), "w") as f:
            f.write("route_01 PASS\nMMEX: 1 PASS, 0 FAIL\n")
        with open(os.path.join(self.collected, "dryrun_report.txt"),
                  "w") as f:
            f.write("route_01 PASS\nDiary: 1 PASS, 0 FAIL\n")
        self._write_results(app="Currency")
        self.assertEqual(collect.main([self.collected, self.dest]), 0)
        self.assertTrue(os.path.isdir(os.path.join(self.dest, "MMEX")))
        self.assertFalse(os.path.isdir(os.path.join(self.dest, "Diary")))
        self.assertFalse(os.path.isdir(
            os.path.join(self.dest, "Currency")))
        summary = self._summary()
        self.assertIn("## MMEX", summary)
        self.assertNotIn("## Diary", summary)
        self.assertNotIn("## Currency", summary)


if __name__ == "__main__":
    unittest.main(verbosity=2)
