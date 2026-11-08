#!/usr/bin/env python3
"""Device route script for Currency route_06.

Method: Parser$Handler.startElement
Edge ids, in order: E012ed474 Ee88066da Ef071a802 E1f5a81d0 E19c2a4c6
Printed route file: graphs/Currency/scratch/route_print/Parser$Handler.startElement.txt
Permissions: none
Fixtures: none
Setup: network (ECB); cert issue on API<=27 images

State note: edge E1f5a81d0 fires only on a first launch after install or
after clearing the data (Data.map == null and no saved pref_map). That
state is created by run_app.sh, which runs pm clear before this script,
so no fixture or setup step is needed inside the script. The route is
reached by launching Main alone: Main.onResume parses the bundled
R.raw.eurofxref_daily resource, and the SAX parser calls startElement
once per XML element. There is no user action past launch.
"""

import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from device.harness import Runner  # noqa: E402

EDGE_IDS = ["E012ed474", "Ee88066da", "Ef071a802", "E1f5a81d0", "E19c2a4c6"]
LAUNCHER = "org.billthefarmer.currency/.Main"


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    r = Runner(package=args.package, route="route_06", edge_ids=EDGE_IDS,
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

        # E1f5a81d0: Main.onResume -> Parser.startParser(Context,int).
        # Automatic on a first launch after pm clear: Main.onResume
        # calls parser.startParser(this, R.raw.eurofxref_daily) when no
        # exchange rates are saved yet (Main.java:497). No user action.
        r.comment("automatic: first-launch onResume parses bundled "
                  "eurofxref_daily; no user action", edge="E1f5a81d0")

        # E19c2a4c6: Parser.startParser -> Parser$Handler.startElement.
        # Framework edge: Xml.parse SAX callback, once per XML element
        # (Parser.java:94). No user action exists.
        r.comment("framework: Xml.parse SAX callback startElement; "
                  "no user action", edge="E19c2a4c6")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
