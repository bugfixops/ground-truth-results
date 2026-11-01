#!/usr/bin/env python3
"""AmazeFileManager route_21: MainFragment.onDetach.

Method: MainFragment.onDetach
Edge ids in order:
    E380fe171 E45d73a86 E7708bb4d E858ed758 Ef643161a E3f533b40
    Ebd761bbf E9adbdc5d E411e6c12 E6b1dbdd0 E59c319e1 Eac844b0a
    E93059c3a
Printed route: graphs/AmazeFileManager/scratch/route_print/
    MainFragment.onDetach.txt, verdict REACHABLE, 13 edges.
    Edge list identical to methods.csv route_edge_ids for
    MainFragment.onDetach and to d1_routes_draft.csv route_21.
Permissions: android.permission.READ_EXTERNAL_STORAGE and
    android.permission.WRITE_EXTERNAL_STORAGE, pre-granted by
    run_app.sh (the app's standard set). No edge in this route
    requires a further permission; the first-run storage gate at
    MainActivity.java:436-484 refreshes the drawer only and does
    not block goToMain.
Fixtures: none. Setup: none beyond the standard config
    (run_app.sh starts from `pm clear`).
Standard configuration: run_app.sh starts from `pm clear` and grants
    only the ROUTES.csv permissions.

Mapping notes (printed source):
  - MainActivity is the MAIN/LAUNCHER activity
    (AndroidManifest.xml, .activities.MainActivity intent-filter
    MAIN/LAUNCHER). goToMain is called from the async callback
    (MainActivity.java:414,416,420); goToMain creates the
    TabFragment (MainActivity.java:784); TabFragment.onCreateView
    calls addTab (TabFragment.java:113-141) and addTab creates the
    MainFragment (TabFragment.java:351).
  - The detach driver is NOT a ViewPager tab switch: TabFragment
    holds exactly 2 fragments and sets an offscreen page limit of 4
    (TabFragment.java:366, getCurrentTabFragment/getFragmentAtIndex
    guard on size == 2), so switching tabs keeps both MainFragments
    attached and cannot drive onPause/onStop/onDestroy/onDetach.
    The driver used here is in-app navigation that finishes
    MainActivity: the drawer "Settings" row starts
    PreferencesActivity and calls mainActivity.finish()
    (Drawer.java:435-442). Finishing the activity drives the
    fragment through onPause -> onStop -> onDestroy -> onDetach
    (MainFragment.java:1433, 1446, 1544, 1698).
  - Drawer opening: the toolbar home indicator is an
    ActionBarDrawerToggle whose accessibility description is
    R.string.drawer_open = "Open navigation drawer"
    (Drawer.java:217-224, res/values/strings.xml:25), so the
    script taps that content description.
  - Drawer "Settings" row: Drawer.java:435-442 adds a row with
    R.string.setting = "Settings" (res/values/strings.xml:31).
    The row sits after the storage/bookmark rows, so the script
    scrolls to it before tapping; no fixed coordinates are used.
  - The final three edges (onStop, onDestroy, onDetach) are
    framework lifecycle steps after finish(); they get
    r.comment, not extra taps.
"""

import argparse
import os
import sys

# Locate the app root (the directory containing device/harness/)
# from wherever this script is checked out: the helper output dir
# or the merged device/routes/AmazeFileManager/ location. The
# template's fixed four-dirname climb assumes only the merged
# location, so this ancestor search replaces it.
_here = os.path.dirname(os.path.abspath(__file__))
_root = _here
while not os.path.exists(os.path.join(_root, "device", "harness",
                                      "harness.py")):
    _parent = os.path.dirname(_root)
    if _parent == _root:
        raise RuntimeError("device/harness/harness.py not found above %s"
                           % _here)
    _root = _parent
sys.path.insert(0, _root)
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E380fe171", "E45d73a86", "E7708bb4d", "E858ed758", "Ef643161a",
    "E3f533b40", "Ebd761bbf", "E9adbdc5d", "E411e6c12", "E6b1dbdd0",
    "E59c319e1", "Eac844b0a", "E93059c3a",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AmazeFileManager route_21")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_21", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # E380fe171 S_ENTRY -> MainActivity.onCreate: launch MainActivity
    # (MAIN/LAUNCHER).
    r.launch(args.package + "/.activities.MainActivity", "E380fe171")
    # E45d73a86 MainActivity.onCreate -> MainActivity.goToMain:
    # goToMain runs from the async callback (MainActivity.java:414,
    # 416, 420). No user action.
    r.comment("async callback calls goToMain", "E45d73a86")
    # E7708bb4d MainActivity.goToMain -> TabFragment.<init>:
    # goToMain creates the TabFragment (MainActivity.java:784).
    # No user action.
    r.comment("goToMain creates TabFragment", "E7708bb4d")
    # E858ed758 TabFragment.<init> -> TabFragment.onCreateView:
    # framework fragment lifecycle. No user action.
    r.comment("framework runs TabFragment.onCreateView", "E858ed758")
    # Ef643161a TabFragment.onCreateView -> MainFragment.<init>:
    # onCreateView calls addTab (TabFragment.java:113-141) and
    # addTab creates the MainFragment (TabFragment.java:351).
    # No user action.
    r.comment("addTab creates MainFragment", "Ef643161a")
    # E3f533b40 MainFragment.<init> -> MainFragment.onCreate:
    # framework fragment lifecycle. No user action.
    r.comment("framework runs MainFragment.onCreate", "E3f533b40")
    # Ebd761bbf MainFragment.onCreate -> MainFragment.onCreateView:
    # framework fragment lifecycle. No user action.
    r.comment("framework runs MainFragment.onCreateView", "Ebd761bbf")
    # E9adbdc5d MainFragment.onCreateView ->
    # MainFragment.onActivityCreated: framework fragment lifecycle.
    # No user action.
    r.comment("framework runs MainFragment.onActivityCreated",
              "E9adbdc5d")
    # E411e6c12 MainFragment.onActivityCreated -> MainFragment.onResume:
    # framework fragment lifecycle (MainFragment.java:1419).
    # No user action.
    r.comment("framework runs MainFragment.onResume", "E411e6c12")
    # E6b1dbdd0 MainFragment.onResume -> MainFragment.onPause:
    # driven by navigation that finishes MainActivity. Open the
    # drawer (content-desc "Open navigation drawer",
    # Drawer.java:217-224) and tap the "Settings" row
    # (Drawer.java:435-442, R.string.setting). That row starts
    # PreferencesActivity and calls mainActivity.finish(), so the
    # activity (and its MainFragment) starts tearing down: this
    # is the onPause step. A tab switch is deliberately NOT used:
    # with 2 fragments and offscreen limit 4 (TabFragment.java:366)
    # it would keep both MainFragments attached.
    r.tap("E6b1dbdd0", desc="Open navigation drawer")
    r.scroll_to("E6b1dbdd0", text="Settings")
    r.tap("E6b1dbdd0", text="Settings")
    # E59c319e1 MainFragment.onPause -> MainFragment.onStop:
    # finish() continues the teardown (MainFragment.java:1446).
    # No further action.
    r.comment("finish() drives MainFragment.onStop", "E59c319e1")
    # Eac844b0a MainFragment.onStop -> MainFragment.onDestroy:
    # finish() continues the teardown (MainFragment.java:1544).
    # No further action.
    r.comment("finish() drives MainFragment.onDestroy", "Eac844b0a")
    # E93059c3a MainFragment.onDestroy -> MainFragment.onDetach:
    # finish() completes the teardown (MainFragment.java:1698).
    # This is the target edge. No further action.
    r.comment("finish() drives MainFragment.onDetach", "E93059c3a")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
