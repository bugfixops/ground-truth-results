#!/usr/bin/env python3
"""Device replay script for hash-checker route_35.

Method: DatabaseHelperModule.<init>
Printed route: graphs/hash-checker/scratch/route_print/DatabaseHelperModule.<init>.txt
Edge ids (in route order):
    E34de2c31 E7aab529b E4a4779ed
Permissions: none
Fixtures: none
Setup: any file as input (fixtures)
Status in ROUTES.csv: scripted

Route story: launching any activity creates the Application first.
App.onCreate() (App.java:71) builds the Dagger component with
new DatabaseHelperModule(localDataStorage), so the constructor runs
during launch with no further user action.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness.harness import Runner  # noqa: E402

EDGES = [
    "E34de2c31", "E7aab529b", "E4a4779ed",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    runner = Runner(package=args.package, route="route_35", edge_ids=EDGES,
                    log_path=args.log, dry_run=args.dry_run, adb=args.adb,
                    outdir=args.outdir)
    try:
        # E34de2c31 -- S_ENTRY -> App.<init>: launch the app. The
        # Application (AndroidManifest.xml:9, android:name=".App") is
        # created before the activity. Manifest package is
        # com.smlnskgmail.jaman.hashchecker and .MainActivity is the
        # launcher activity; args.package is the flavor applicationId,
        # so the component is built from it.
        runner.launch(args.package + "/com.smlnskgmail.jaman.hashchecker.MainActivity",
                      "E34de2c31")
        # E7aab529b -- App.<init> -> App.onCreate: Application
        # lifecycle, no user action.
        runner.comment("App.onCreate lifecycle", "E7aab529b")
        # E4a4779ed -- App.onCreate -> DatabaseHelperModule.<init>:
        # direct call in App.java:71 when building the Dagger
        # component; reached by launch alone, no user action.
        runner.comment("Dagger builder calls new DatabaseHelperModule()",
                       "E4a4779ed")
    finally:
        runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
