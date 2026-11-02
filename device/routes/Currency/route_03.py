#!/usr/bin/env python3
"""Currency route_03: Parser.startParser(Context,int).

Method: Parser.startParser(Context,int)
Edge ids in order:
    E012ed474 Ee88066da Ef071a802 E1f5a81d0
Printed route: graphs/Currency/scratch/route_print/Parser.startParser(Context,int).txt
    (REACHABLE, SOURCE_OK, ref Main.java:497).
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none.
Setup: network (ECB); cert issue on API<=27 images (ROUTES.csv setup
    column; this route parses the bundled raw resource, so no network
    step is needed on this route).
Launcher: org.billthefarmer.currency/.Main (AndroidManifest.xml:18-25,
    MAIN/LAUNCHER). run_app.sh already does pm clear, permission
    grants, fixture pushes, and per-app setup before this script, so
    the script performs only the route actions starting from launch.

Mapping notes:
  - No GUI action is needed past launch. Main.onResume parses the
    bundled rates when no rates are saved yet: the edge guard is
    Data.map == null and pref_map not saved yet (first launch after
    install or after clearing the data, Main.java:497:
    parser.startParser(this, R.raw.eurofxref_daily)). run_app.sh
    runs pm clear before this script, so that guard holds and the
    target runs on launch. The final edge is therefore logged with
    r.comment, not driven by a tap.
  - This route must run before any route that saves rates; it does
    not depend on the ECB network download.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E012ed474", "Ee88066da", "Ef071a802", "E1f5a81d0",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Currency route_03")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_03", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E012ed474 S_ENTRY -> Main.<init>: launch the MAIN/LAUNCHER
    # activity (AndroidManifest.xml:18-25).
    r.launch(args.package + "/.Main", edge="E012ed474")
    # Ee88066da Main.<init> -> Main.onCreate: the system instantiates
    # Main, then calls onCreate (Main.java:242). No user action.
    r.comment("system instantiates Main, then onCreate",
              edge="Ee88066da")
    # Ef071a802 Main.onCreate -> Main.onResume: onStart -> onResume
    # (Main.java:369). No user action.
    r.comment("onStart -> onResume", edge="Ef071a802")
    # E1f5a81d0 Main.onResume -> Parser.startParser(Context,int):
    # parser.startParser(this, R.raw.eurofxref_daily) (Main.java:497)
    # fires on a fresh install / after pm clear, when no rates are
    # saved yet. Automatic on resume; no user action. This is the
    # target edge.
    r.comment("fresh install: onResume starts the bundled-rates parser",
              edge="E1f5a81d0")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
