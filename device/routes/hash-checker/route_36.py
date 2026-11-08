#!/usr/bin/env python3
"""Replay script for hash-checker route_36.

Method: SettingsHelperModule.<init>
Edge ids (exact, in route order, from ROUTES.csv):
    E34de2c31, E7aab529b, E13bfb3f1
Printed route file:
    graphs/hash-checker/scratch/route_print/SettingsHelperModule.<init>.txt
Permissions: (none)
Fixtures: (none)
Setup: any file as input (fixtures)
Status in ROUTES.csv: scripted

Route shape: the constructor is reached from App.onCreate by a plain
``new`` call (explicit edge), not by any UI step. Launching the app
creates the Application object and runs App.onCreate, so the whole
route is exercised by a single launch on fresh / cleared data (which
run_app.sh guarantees with pm clear before invoking this script).
No fixture push, permission grant, or pm clear happens in this script:
run_app.sh owns all of those.
"""

import argparse
import os
import sys

# Repo root is 3 directory levels up from this script's FINAL location
# (device/routes/hash-checker/): four dirname() calls on __file__,
# because the first call yields the script's own directory and each
# further call climbs one level (hash-checker -> routes -> device ->
# repo root).
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ["E34de2c31", "E7aab529b", "E13bfb3f1"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    args = ap.parse_args()
    runner = Runner(package=args.package, route="route_36",
                    edge_ids=EDGE_IDS, log_path=args.log,
                    dry_run=args.dry_run, adb=args.adb)
    try:
        # Edge E34de2c31: S_ENTRY -> App.<init> (ENTRY).
        # Trigger: "Android starts the app process; the Application
        # object is created before any component" (manifest
        # AndroidManifest.xml:9, android:name=".App"). Launching
        # MainActivity starts the app process, which constructs App.
        # Component assumption: the manifest package
        # com.smlnskgmail.jaman.hashchecker plus .MainActivity is the
        # activity class under the flavor applicationId (args.package).
        runner.launch(args.package + "/com.smlnskgmail.jaman.hashchecker.MainActivity",
                      "E34de2c31")
        # Edge E7aab529b: App.<init> -> App.onCreate (LIFECYCLE).
        # Trigger: "Application.onCreate runs right after
        # construction" (App.java:53). Framework lifecycle edge: no
        # user action exists or is needed.
        runner.comment("App.onCreate runs right after App construction "
                       "(framework lifecycle, no user action)",
                       "E7aab529b")
        # Edge E13bfb3f1: App.onCreate -> SettingsHelperModule.<init>
        # (CALL, explicit). Trigger: "Direct call" (App.java:72:
        # .settingsHelperModule(new SettingsHelperModule(settings))).
        # Plain ``new`` inside App.onCreate: runs during the launch
        # above, before any UI is shown. No user action.
        runner.comment("App.onCreate constructs SettingsHelperModule "
                       "directly (App.java:72, plain new call, "
                       "no user action)",
                       "E13bfb3f1")
    finally:
        runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
