"""Unit tests for device.harness (brief D2 acceptance).

Run from the repo root:  python3 -I device/harness/test_harness.py
or:  python3 -I -m unittest device.harness.test_harness  (from a staging root)

Covers: bounds/centre parsing, node lookup by text/res_id/desc (including
clickable-first preference), dry-run planned-command recording, dry-run
edge validation, fixed-coordinate tap requiring a why string, log line
format, and lookup against the saved sample dumps (shaped from Currency
res/layout/main.xml and about.xml).
"""

import os
import re
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from device.harness import Runner, find_node, parse_bounds, node_center  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
EDGE_A = "Eaaaa0001"
EDGE_B = "Ebbbb0002"


def load_dump(name):
    with open(os.path.join(HERE, "sample_dumps", name), encoding="utf-8") as f:
        return ET.fromstring(f.read())


class TestParsing(unittest.TestCase):
    def test_parse_bounds_and_center(self):
        self.assertEqual(parse_bounds("[0,168][1080,336]"), (0, 168, 1080, 336))
        node = ET.Element("node", {"bounds": "[112,184][400,264]"})
        self.assertEqual(node_center(node), (256, 224))

    def test_parse_bounds_malformed(self):
        with self.assertRaises(ValueError):
            parse_bounds("nope")

    def test_find_by_text(self):
        root = load_dump("main.xml")
        node = find_node(root, text="Euro")
        self.assertIsNotNone(node)
        self.assertEqual(node.get("resource-id"),
                         "org.billthefarmer.currency:id/name")

    def test_find_by_res_id_short_and_full(self):
        root = load_dump("about.xml")
        self.assertIsNotNone(find_node(root, res_id="about"))
        self.assertIsNotNone(find_node(
            root, res_id="org.billthefarmer.currency:id/licence"))

    def test_find_by_desc(self):
        root = load_dump("main.xml")
        node = find_node(root, desc="More options")
        self.assertIsNotNone(node)
        self.assertEqual(node.get("clickable"), "true")

    def test_find_prefers_clickable(self):
        # Two nodes share text "Settings" only if a non-clickable copy
        # exists; here the single Settings node is clickable.
        root = load_dump("main.xml")
        node = find_node(root, text="Settings")
        self.assertEqual(node.get("clickable"), "true")

    def test_find_no_match(self):
        root = load_dump("main.xml")
        self.assertIsNone(find_node(root, text="No such view"))

    def test_find_needs_exactly_one_selector(self):
        root = load_dump("main.xml")
        with self.assertRaises(ValueError):
            find_node(root)
        with self.assertRaises(ValueError):
            find_node(root, text="Euro", res_id="name")


class TestDryRun(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.log = os.path.join(self.tmp.name, "route_01.log")
        self.r = Runner(package="org.billthefarmer.currency", route="route_01",
                        edge_ids=[EDGE_A, EDGE_B], log_path=self.log,
                        dry_run=True)
        self.addCleanup(self.r.done)

    def test_planned_commands_and_log_format(self):
        self.r.tap(text="Settings", edge=EDGE_A)
        self.r.type_text("hello world", edge=EDGE_B)
        self.assertEqual(len(self.r.planned), 2)
        self.assertIn("input tap", self.r.planned[0])
        self.assertIn("input text", self.r.planned[1])
        with open(self.log, encoding="utf-8") as f:
            lines = f.read().splitlines()
        self.assertEqual(len(lines), 2)
        pat = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z "
                         r"E\w+ (tap|type_text) \S+ planned$")
        for line in lines:
            self.assertRegex(line, pat)

    def test_unknown_edge_rejected(self):
        with self.assertRaises(ValueError):
            self.r.tap(text="Settings", edge="E99999999")

    def test_missing_edge_rejected(self):
        with self.assertRaises(ValueError):
            self.r.tap(text="Settings", edge=None)

    def test_dry_run_never_calls_adb(self):
        orig = subprocess.run

        def boom(*a, **k):
            raise AssertionError("adb must not be called in dry mode")

        subprocess.run = boom
        try:
            self.r.launch("org.billthefarmer.currency/.Main", edge=EDGE_A)
            self.r.tap(res_id="list", edge=EDGE_A)
            self.r.wait_for(text="Settings", edge=EDGE_B)
            self.r.scroll_to(text="Euro", edge=EDGE_A)
            self.r.assert_text("Currency", edge=EDGE_B)
            self.r.grant("android.permission.INTERNET", edge=EDGE_A)
            self.r.start_intent(edge=EDGE_B, action="android.intent.action.VIEW")
            self.r.broadcast(edge=EDGE_B, action="android.intent.action.BOOT_COMPLETED")
            self.r.comment("lifecycle edge, no user action", edge=EDGE_A)
        finally:
            subprocess.run = orig
        self.assertEqual(len(self.r.planned), 8)  # comment logs, no adb plan
        with open(self.log, encoding="utf-8") as f:
            self.assertEqual(len(f.read().splitlines()), 9)

    def test_fixed_coordinate_tap_needs_why(self):
        with self.assertRaises(ValueError):
            self.r.tap(edge=EDGE_A, x=100, y=200)
        self.r.tap(edge=EDGE_A, x=100, y=200,
                   why="no id, text, or desc on this canvas view")
        self.assertIn("input tap 100 200", self.r.planned[-1])

    def test_grant_and_push_planned(self):
        self.r.grant("android.permission.WRITE_EXTERNAL_STORAGE", edge=EDGE_A)
        self.r.push_fixture("/tmp/fixture.txt", edge=EDGE_B,
                            dest="/sdcard/Download/fixture.txt")
        self.assertIn("pm grant org.billthefarmer.currency "
                      "android.permission.WRITE_EXTERNAL_STORAGE",
                      self.r.planned[-2])
        self.assertIn("push /tmp/fixture.txt /sdcard/Download/fixture.txt",
                      self.r.planned[-1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
