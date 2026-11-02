#!/usr/bin/env python3
"""Device replay script for hash-checker route_25.

Method: App.getShortcut
Printed route: graphs/hash-checker/scratch/route_print/App.getShortcut.txt
Edge ids (in route order, from ROUTES.csv):
    E34de2c31 E7aab529b Ecff74424 E2f51b4e7 E97f48490
Permissions: (none)
Fixtures: (none)
Setup: any file as input (fixtures)
Status in ROUTES.csv: scripted

FIRST-LAUNCH ASSUMPTION (read before running): edge Ecff74424 carries
the guard "shortcuts not created yet: first launch after install (if
!settings.isShortcutsIsCreated(), App.java:76)". This script is
therefore scriptable ONLY on a fresh install / cleared app data.
run_app.sh guarantees that with pm clear before each script; this
script itself performs NO clearing, fixture push, or permission grant.

One script block per route edge, in route order. This whole route runs
inside Application.onCreate, before any activity is visible, so every
edge except the launch is a comment(); the final block waits for the
main screen only to prove App.onCreate completed and the app reached
the calculator screen. Launching MainActivity is what creates the App
object: Android instantiates the Application before any component.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from device.harness.harness import Runner

EDGE_IDS = [
    "E34de2c31", "E7aab529b", "Ecff74424", "E2f51b4e7", "E97f48490",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    args = ap.parse_args()
    runner = Runner(package=args.package, route="route_25",
                    edge_ids=EDGE_IDS, log_path=args.log,
                    dry_run=args.dry_run, adb=args.adb,
                    outdir=args.outdir)
    try:
        # E34de2c31: S_ENTRY -> App.<init>
        # Trigger: "Android starts the app process; the Application object
        # is created before any component". Launching the launcher
        # activity is the way to start the process; the manifest package
        # is com.smlnskgmail.jaman.hashchecker, so .MainActivity resolves
        # under the flavor applicationId given by --package. App is the
        # android:name=".App" application in AndroidManifest.xml:9.
        runner.launch(args.package + "/com.smlnskgmail.jaman.hashchecker.MainActivity",
                      "E34de2c31")
        # E7aab529b: App.<init> -> App.onCreate
        # Trigger: "Application.onCreate runs right after construction"
        # (App.java:53). Lifecycle edge, no user action.
        runner.comment("lifecycle: App.onCreate", "E7aab529b")
        # Ecff74424: App.onCreate -> App.createShortcuts
        # Trigger: "Direct call" (App.java:77). Guard: first launch only
        # (shortcuts not yet created); guaranteed by run_app.sh pm clear
        # before this script, NOT by any step here.
        runner.comment("call: App.createShortcuts (first-launch guard)",
                       "Ecff74424")
        # E2f51b4e7: App.createShortcuts -> App.getShortcutForFolderType
        # Trigger: "Direct call" (App.java:91). Guard: SDK_INT >= 26 and
        # a ShortcutManager exists (App.java:84-86); true on API 27.
        runner.comment("call: App.getShortcutForFolderType (SDK>=26 guard)",
                       "E2f51b4e7")
        # E97f48490: App.getShortcutForFolderType -> App.getShortcut
        # Trigger: "Direct call" (App.java:126). getShortcut builds the
        # ShortcutInfo: no UI of its own. Observable used: the calculator
        # screen appears once App.onCreate (which contains this whole
        # chain) has finished (fragment_hash_calculator.xml,
        # tv_selected_hash_type).
        runner.wait_for("E97f48490",
                        res_id=args.package + ":id/tv_selected_hash_type")
    finally:
        runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
