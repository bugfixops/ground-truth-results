#!/usr/bin/env python3
"""Device route script for Currency route_08.

Method: Parser.getMap
Edge ids, in order: E012ed474 Ee88066da Ef071a802 E576d70ee
Printed route file: graphs/Currency/scratch/route_print/Parser.getMap.txt
Permissions: none
Fixtures: none
Setup: network (ECB); cert issue on API<=27 images

State note: edge E576d70ee fires only on a first launch after install
or after clearing the data (Data.map == null and no saved pref_map).
That state is created by run_app.sh, which runs pm clear before this
script, so no fixture or setup step is needed inside the script. The
route is reached by launching Main alone: Main.onResume parses the
bundled rates and then reads parser.getMap(). There is no user action
past launch.
"""

import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from device.harness import Runner  # noqa: E402

EDGE_IDS = ["E012ed474", "Ee88066da", "Ef071a802", "E576d70ee"]
LAUNCHER = "org.billthefarmer.currency/.Main"


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    r = Runner(package=args.package, route="route_08", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, outdir=args.outdir,
               adb=args.adb)
    try:
        # E012ed474: Tap the Currency icon in the launcher
        # (MAIN/LAUNCHER intent filter; Main is the launcher activity
        # in AndroidManifest.xml).
        r.launch(LAUNCHER, edge="E012ed474")

        # Ee88066da: Main.<init> -> Main.onCreate. Lifecycle edge:
        # the system instantiates Main, then calls onCreate. No user
        # action exists.
        r.comment("lifecycle: system instantiates Main, then onCreate",
                  edge="Ee88066da")

        # Ef071a802: Main.onCreate -> Main.onResume (onStart -> onResume).
        # Lifecycle edge: no user action exists.
        r.comment("lifecycle: onStart -> onResume", edge="Ef071a802")

        # E576d70ee: Main.onResume -> Parser.getMap. Automatic on a
        # first launch after pm clear: after startParser, Main.onResume
        # reads valueMap = parser.getMap() (Main.java:529). No user
        # action exists.
        r.comment("automatic: first-launch onResume reads parser.getMap "
                  "after parsing bundled rates; no user action",
                  edge="E576d70ee")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
