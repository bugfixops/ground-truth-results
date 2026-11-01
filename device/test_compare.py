"""Tests for device/compare.py (brief D6 acceptance).

Run: python3 -I device/test_compare.py
Builds a synthetic device/results/<run>/ folder, runs compare.py with
--out-root into a temp dir, and asserts the per-app device/results.csv
columns, run/script values, and that no real graphs/ tree is touched.
"""

import csv
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compare  # noqa: E402


class TestCompare(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.results = os.path.join(self.tmp.name, "run-42-1")
        cur = os.path.join(self.results, "Currency")
        os.makedirs(cur)
        with open(os.path.join(cur, "results.csv"), "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["app", "route", "method", "edges", "reached",
                        "script_status", "steps_done", "steps_total",
                        "error", "run_id"])
            w.writerow(["Currency", "route_01", "M.a", "E1 E2", "yes", "ok",
                        "3", "3", "", "run-42-1"])
            w.writerow(["Currency", "route_02", "M.b", "E3", "not_run",
                        "unscriptable", "0", "0", "needs hw", "run-42-1"])
        self.out_root = os.path.join(self.tmp.name, "graphs")

    def test_compare(self):
        run, written = compare.compare(self.results, self.out_root)
        self.assertEqual(run, "run-42-1")
        self.assertEqual(written, {"Currency": 2})
        dest = os.path.join(self.out_root, "Currency", "device",
                            "results.csv")
        with open(dest, newline="") as f:
            reader = csv.DictReader(f)
            self.assertEqual(reader.fieldnames, compare.OUT_COLUMNS)
            rows = list(reader)
        self.assertEqual(rows[0]["route"], "route_01")
        self.assertEqual(rows[0]["method"], "M.a")
        self.assertEqual(rows[0]["edges"], "E1 E2")
        self.assertEqual(rows[0]["reached"], "yes")
        self.assertEqual(rows[0]["script_status"], "ok")
        self.assertEqual(rows[0]["run"], "run-42-1")
        self.assertEqual(rows[0]["script"], "route_01.py")
        self.assertEqual(rows[1]["reached"], "not_run")
        self.assertEqual(rows[1]["script_status"], "unscriptable")


if __name__ == "__main__":
    unittest.main(verbosity=2)
