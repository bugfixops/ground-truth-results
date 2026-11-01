"""Tests for device/collect.py (brief D5 acceptance).

Run: python3 -I device/test_collect.py
Builds a synthetic collected/ folder with a results artifact (including
a screenshot and a UI dump that must NOT be copied) and a dry-run
artifact, runs collect.py, and asserts only allowlisted text outputs
plus SUMMARY.md counts.
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
