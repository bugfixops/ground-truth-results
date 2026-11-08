"""MMEX route_20: AboutFragment.getLogcat -- CONVERTED (retry).

Method: AboutFragment.getLogcat
Edge ids (in route order):
    E71c76102 E2e074fc1 E5d5a9c2f Eff22f7d2 Ed2488d54 E025b8cae
    E02874fba E64d9379e E5300011e Ee835bc9a E38752023 E45117f3d
    Ecef22362 E324d7c06 E9903f114 E4c9a9322 E1de73933
Printed route source:
    graphs/MMEX/scratch/route_print_final2/AboutFragment.getLogcat.txt
    (17 steps; header env=- state=-). These edge ids match, in order,
    the verification.csv path row for AboutFragment.getLogcat
    exactly (checked by the g4 draft; no discrepancy).
Permissions: none (print header env=-; no ENV permission gate).
Fixtures: none (no STATE file gate).
Setup: setup_route_20.py (bootstrap only -- see that file). The
    previous unscriptable reason (home unreachable after pm clear)
    is removed by the bootstrap: tutorial off + database path set +
    app-created schema, so MainActivity reaches the home screen.
Run (from the repo root, after the merger drops this file into
    device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_20.py --package
    com.money.manager.ex --log steps/route_20.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E5d5a9c2f", "Eff22f7d2", "Ed2488d54",
    "E025b8cae", "E02874fba", "E64d9379e", "E5300011e", "Ee835bc9a",
    "E38752023", "E45117f3d", "Ecef22362", "E324d7c06", "E9903f114",
    "E4c9a9322", "E1de73933",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_20", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E71c76102: Launch the MAIN/LAUNCHER activity.
        # AndroidManifest.xml:136-143: .home.MainActivity with MAIN +
        # LAUNCHER intent filter.
        r.launch("com.money.manager.ex/.home.MainActivity",
                 edge="E71c76102")
        # E2e074fc1: The framework calls MainActivity.onCreate after
        # creating the activity instance. No user action.
        r.comment("framework calls MainActivity.onCreate",
                  edge="E2e074fc1")
        # E5d5a9c2f: MainActivity.onCreate calls initHomeFragment
        # directly (MainActivity.java:238). No user action.
        r.comment("MainActivity.onCreate calls initHomeFragment",
                  edge="E5d5a9c2f")
        # Eff22f7d2: initHomeFragment commits HomeFragment into the
        # content container, showing the home screen
        # (MainActivity.java:1308-1324). No user action.
        r.comment("home screen shown (HomeFragment committed)",
                  edge="Eff22f7d2")
        # Ed2488d54: Open the drawer, then tap the About group.
        # Drawer toggle content description is R.string.open =
        # "Open" (MainActivity.java:1296; res/values/strings.xml:193).
        # Drawer group text is R.string.about = "About"
        # (MainActivity.java:1118-1120; res/values/strings.xml:177).
        r.tap(desc="Open", edge="Ed2488d54")
        r.tap(text="About", edge="Ed2488d54")
        # E025b8cae: The group-click tap posts a Runnable with a
        # 200 ms delay (MainActivity.java:948-962). No user action.
        r.comment("drawer group Runnable posted (200 ms delay)",
                  edge="E025b8cae")
        # E02874fba: The Runnable calls
        # onDrawerMenuAndOptionMenuSelected for the About group.
        # No user action.
        r.comment("drawer Runnable calls onDrawerMenuAndOptionMenuSelected",
                  edge="E02874fba")
        # E64d9379e: onDrawerMenuAndOptionMenuSelected starts
        # AboutActivity. No user action.
        r.comment("AboutActivity started from drawer selection",
                  edge="E64d9379e")
        # E5300011e: The framework calls AboutActivity.onCreate.
        # No user action.
        r.comment("framework calls AboutActivity.onCreate",
                  edge="E5300011e")
        # Ee835bc9a: AboutActivity.onCreate sets the tab adapter;
        # the framework shows the first tab's fragment. No action.
        r.comment("About tab adapter shows first tab fragment",
                  edge="Ee835bc9a")
        # E38752023: AboutTabAdapter.getItem creates the About
        # fragment. No user action.
        r.comment("AboutTabAdapter.getItem creates AboutFragment",
                  edge="E38752023")
        # E45117f3d: AboutFragment.newInstance creates the fragment.
        # No user action.
        r.comment("AboutFragment.newInstance creates fragment",
                  edge="E45117f3d")
        # Ecef22362: The framework calls AboutFragment.onCreateView.
        # No user action.
        r.comment("framework calls AboutFragment.onCreateView",
                  edge="Ecef22362")
        # E324d7c06: onCreateView inflates the About tab page.
        # No user action.
        r.comment("About tab page shown", edge="E324d7c06")
        # E9903f114: Tap the Logcat button. res/layout/
        # about_fragment.xml sendLogcatButton with text
        # @string/send_me_logcat = "Logcat" (strings.xml:483),
        # wired at AboutFragment.java:193-199.
        r.wait_for(text="Logcat", edge="E9903f114", timeout=30)
        r.tap(text="Logcat", edge="E9903f114")
        # E4c9a9322: The button click calls AboutFragment.sendLogcat
        # (AboutFragment.java:197). No user action.
        r.comment("Logcat button click calls sendLogcat",
                  edge="E4c9a9322")
        # E1de73933: sendLogcat calls getLogcat (AboutFragment.java:
        # 230-232), which runs `logcat -d` (AboutFragment.java:263).
        # The following email chooser is left open; the target
        # method has already executed, and the coverage dump after
        # this script records it.
        r.comment("sendLogcat calls getLogcat (target reached)",
                  edge="E1de73933")
    finally:
        r.done()


if __name__ == "__main__":
    main()
