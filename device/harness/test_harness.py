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

from device.harness import (Runner, find_node, find_row_action,  # noqa: E402
                            parse_bounds, node_center)

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

    def test_rotate_plans_two_settings_and_validates(self):
        self.r.rotate(edge=EDGE_A, orientation="landscape")
        self.assertEqual(len(self.r.planned), 2)
        self.assertIn("settings put system accelerometer_rotation 0",
                      self.r.planned[0])
        self.assertIn("settings put system user_rotation 1",
                      self.r.planned[1])
        with self.assertRaises(ValueError):
            self.r.rotate(edge=EDGE_A, orientation="upside_down")
        with self.assertRaises(ValueError):
            self.r.rotate(edge="E99999999", orientation="portrait")

    def test_grant_and_push_planned(self):
        self.r.grant("android.permission.WRITE_EXTERNAL_STORAGE", edge=EDGE_A)
        self.r.push_fixture("/tmp/fixture.txt", edge=EDGE_B,
                            dest="/sdcard/Download/fixture.txt")
        self.assertIn("pm grant org.billthefarmer.currency "
                      "android.permission.WRITE_EXTERNAL_STORAGE",
                      self.r.planned[-2])
        self.assertIn("push /tmp/fixture.txt /sdcard/Download/fixture.txt",
                      self.r.planned[-1])

    def test_dwell_plans_and_validates(self):
        self.r.dwell(edge=EDGE_A, seconds=60)
        self.assertIn("sleep 60s (dwell)", self.r.planned[-1])
        with open(self.log, encoding="utf-8") as f:
            self.assertIn("dwell seconds=60 planned", f.read())
        for bad in (0, -5, 601, "60", True):
            with self.assertRaises(ValueError):
                self.r.dwell(edge=EDGE_A, seconds=bad)

    def test_kill_app_plans_home_then_kill(self):
        self.r.kill_app(edge=EDGE_A)
        self.assertEqual(len(self.r.planned), 2)
        self.assertIn("input keyevent KEYCODE_HOME", self.r.planned[0])
        self.assertIn("am kill org.billthefarmer.currency",
                      self.r.planned[1])

    def test_relaunch_plans_start(self):
        self.r.relaunch(edge=EDGE_A,
                        component="org.billthefarmer.currency/.Main")
        self.assertIn("am start -W -n org.billthefarmer.currency/.Main",
                      self.r.planned[-1])
        with open(self.log, encoding="utf-8") as f:
            self.assertIn("relaunch component=org.billthefarmer.currency/.Main",
                          f.read())

    def test_restore_from_recents_plans_switch_and_tap(self):
        self.r.restore_from_recents(edge=EDGE_A, text="Currency")
        self.assertIn("input keyevent KEYCODE_APP_SWITCH",
                      self.r.planned[0])
        self.assertIn("input tap <text=Currency>", self.r.planned[1])

    def test_set_always_finish_plans_setting_and_validates(self):
        self.r.set_always_finish(edge=EDGE_A, enabled=True)
        self.assertIn("settings put global always_finish_activities 1",
                      self.r.planned[-1])
        self.r.set_always_finish(edge=EDGE_B, enabled=False)
        self.assertIn("settings put global always_finish_activities 0",
                      self.r.planned[-1])
        with self.assertRaises(ValueError):
            self.r.set_always_finish(edge=EDGE_A, enabled=1)

    def test_set_locale_plans_setting_and_validates(self):
        self.r.set_locale(edge=EDGE_A, locale="ja_JP")
        self.assertIn("settings put global system_locales ja-JP",
                      self.r.planned[-1])
        self.r.set_locale(edge=EDGE_B, locale="zh-TW")
        self.assertIn("settings put global system_locales zh-TW",
                      self.r.planned[-1])
        for bad in ("", "japanese", "ja_JP_extra", "JA-jp", 123):
            with self.assertRaises(ValueError):
                self.r.set_locale(edge=EDGE_A, locale=bad)

    def test_drag_plans_swipe_and_validates(self):
        self.r.drag(edge=EDGE_A, x1=100, y1=200, x2=400, y2=800,
                    duration_ms=1500, why="widget drop position has no node")
        self.assertIn("input swipe 100 200 400 800 1500", self.r.planned[-1])
        with self.assertRaises(ValueError):
            self.r.drag(edge=EDGE_A, x1=100, y1=200, x2=400, y2=800,
                        duration_ms=300, why="too fast for a drag")
        with self.assertRaises(ValueError):
            self.r.drag(edge=EDGE_A, x1=100, y1=200, x2=400, y2=800,
                        why=None)
        with self.assertRaises(ValueError):
            self.r.drag(edge=EDGE_A, x1=100.5, y1=200, x2=400, y2=800,
                        why="non-int coordinate")

    def test_drag_from_plans_one_drag_line(self):
        self.r.drag_from(edge=EDGE_A, x2=400, y2=800, text="Widget",
                         duration_ms=1500,
                         why="home-screen drop position has no node")
        self.assertEqual(len(self.r.planned), 1)
        self.assertIn("input swipe (drag from text=Widget to 400,800)",
                      self.r.planned[0])
        with self.assertRaises(ValueError):
            self.r.drag_from(edge=EDGE_A, x2=400, y2=800, text="Widget",
                             res_id="w", why="two selectors")

    def test_row_action_picks_same_row_button(self):
        xml = ("<hierarchy>"
               "<node text=\"Internal storage\" resource-id=\"\" "
               "bounds=\"[0,200][600,300]\" clickable=\"true\" />"
               "<node text=\"\" resource-id=\"com.example:id/imageButton\" "
               "bounds=\"[500,210][580,290]\" clickable=\"true\" />"
               "<node text=\"SCP/SFTP Connection\" resource-id=\"\" "
               "bounds=\"[0,400][600,500]\" clickable=\"true\" />"
               "<node text=\"\" resource-id=\"com.example:id/imageButton\" "
               "bounds=\"[500,410][580,490]\" clickable=\"true\" />"
               "</hierarchy>")
        root = ET.fromstring(xml)
        node = find_row_action(root, "SCP/SFTP Connection",
                               "com.example:id/imageButton")
        self.assertIsNotNone(node)
        self.assertEqual(node_center(node), (540, 450))
        # First row's button is NOT picked for the second row.
        node2 = find_row_action(root, "Internal storage",
                                "com.example:id/imageButton")
        self.assertEqual(node_center(node2), (540, 250))
        # Missing row, missing action, and action far from the row
        # all yield None (the Runner turns that into LookupError).
        self.assertIsNone(find_row_action(root, "No such row",
                                          "com.example:id/imageButton"))
        self.assertIsNone(find_row_action(root, "SCP/SFTP Connection",
                                          "com.example:id/other"))
        far = ET.fromstring(
            "<hierarchy>"
            "<node text=\"Lonely\" resource-id=\"\" bounds=\"[0,100][600,150]\" "
            "clickable=\"true\" />"
            "<node text=\"\" resource-id=\"com.example:id/imageButton\" "
            "bounds=\"[500,900][580,980]\" clickable=\"true\" />"
            "</hierarchy>")
        self.assertIsNone(find_row_action(far, "Lonely",
                                          "com.example:id/imageButton"))

    def test_tap_row_action_plans_one_line_and_validates(self):
        self.r.tap_row_action(edge=EDGE_A, row_text="SCP/SFTP Connection",
                              res_id="com.example:id/imageButton")
        self.assertEqual(len(self.r.planned), 1)
        self.assertIn("input tap", self.r.planned[0])
        self.assertIn("SCP/SFTP Connection", self.r.planned[0])
        with open(self.log, encoding="utf-8") as f:
            lines = f.read().splitlines()
        self.assertIn("tap_row_action", lines[-1])
        with self.assertRaises(ValueError):
            self.r.tap_row_action(edge=EDGE_A, row_text="",
                                  res_id="com.example:id/imageButton")
        with self.assertRaises(ValueError):
            self.r.tap_row_action(edge="E99999999",
                                  row_text="SCP/SFTP Connection",
                                  res_id="com.example:id/imageButton")

    def test_two_finger_swipe_exact_sequence_steps_1(self):
        self.r.two_finger_swipe(edge=EDGE_A, device="/dev/input/event0",
                                start1=(100, 200), start2=(300, 200),
                                end1=(100, 800), end2=(300, 800), steps=1)
        self.assertEqual(len(self.r.planned), 1)
        cmd = self.r.planned[0]
        # DOWN slot 0 (+BTN), DOWN slot 1, one MOVE step, UP.
        expected = [
            "sendevent /dev/input/event0 3 47 0",
            "sendevent /dev/input/event0 3 57 0",
            "sendevent /dev/input/event0 3 53 100",
            "sendevent /dev/input/event0 3 54 200",
            "sendevent /dev/input/event0 1 330 1",
            "sendevent /dev/input/event0 0 0 0",
            "sendevent /dev/input/event0 3 47 1",
            "sendevent /dev/input/event0 3 57 1",
            "sendevent /dev/input/event0 3 53 300",
            "sendevent /dev/input/event0 3 54 200",
            "sendevent /dev/input/event0 0 0 0",
            "sendevent /dev/input/event0 3 47 0",
            "sendevent /dev/input/event0 3 53 100",
            "sendevent /dev/input/event0 3 54 800",
            "sendevent /dev/input/event0 3 47 1",
            "sendevent /dev/input/event0 3 53 300",
            "sendevent /dev/input/event0 3 54 800",
            "sendevent /dev/input/event0 0 0 0",
            "sendevent /dev/input/event0 3 47 0",
            "sendevent /dev/input/event0 3 57 -1",
            "sendevent /dev/input/event0 3 47 1",
            "sendevent /dev/input/event0 3 57 -1",
            "sendevent /dev/input/event0 1 330 0",
            "sendevent /dev/input/event0 0 0 0",
        ]
        self.assertEqual(cmd, "adb shell " + "; ".join(expected))
        with open(self.log, encoding="utf-8") as f:
            # _log_line replaces spaces with underscores in targets.
            self.assertIn("two_finger_swipe device=/dev/input/event0_steps=1",
                          f.read())

    def test_two_finger_swipe_validates(self):
        kw = dict(edge=EDGE_A, device="/dev/input/event0",
                  start1=(100, 200), start2=(300, 200),
                  end1=(100, 800), end2=(300, 800))
        same = dict(kw, start2=(100, 200))
        with self.assertRaises(ValueError):
            self.r.two_finger_swipe(**same)
        baddev = dict(kw, device="/dev/input/mouse0")
        with self.assertRaises(ValueError):
            self.r.two_finger_swipe(**baddev)
        nosteps = dict(kw, steps=0)
        with self.assertRaises(ValueError):
            self.r.two_finger_swipe(**nosteps)

    def test_two_finger_tap_down_up_no_move(self):
        self.r.two_finger_tap(edge=EDGE_A, device="/dev/input/event2",
                              point1=(100, 200), point2=(300, 200))
        cmd = self.r.planned[0]
        self.assertIn("sendevent /dev/input/event2 3 53 100", cmd)
        self.assertIn("sendevent /dev/input/event2 3 53 300", cmd)
        self.assertNotIn("3 54 800", cmd)  # no move to an end point
        # 17 sendevent calls: 6 + 5 (down) + 6 (up).
        self.assertEqual(cmd.count("sendevent"), 17)
        with self.assertRaises(ValueError):
            self.r.two_finger_tap(edge=EDGE_A, device="/dev/input/event2",
                                  point1=(100, 200), point2=(100, 200))

    def test_key_app_switch_alias(self):
        self.r.key("APP_SWITCH", edge=EDGE_A)
        self.assertIn("input keyevent KEYCODE_APP_SWITCH", self.r.planned[-1])

    def test_wait_for_accepts_desc(self):
        self.r.wait_for(edge=EDGE_A, desc="Copy", timeout=30)
        self.assertIn("wait for desc=Copy", self.r.planned[-1])
        with self.assertRaises(ValueError):
            self.r.wait_for(edge=EDGE_A, text="Copy", desc="Copy")


if __name__ == "__main__":
    unittest.main(verbosity=2)
