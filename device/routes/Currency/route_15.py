#!/usr/bin/env python3
"""Device route script for Currency route_15.

Method: Main$Currency.<init>
Edge ids, in order: E4c32b395 Ea2843361
Printed route file: graphs/Currency/scratch/route_print/Main$Currency.<init>.txt
Permissions: none
Fixtures: none
Setup: network (ECB); cert issue on API<=27 images

State notes: this route has no Main.<init>/onCreate edges. Its first
edge is JVM class initialisation: the first use of class Main in a new
process builds the static CURRENCIES table (Main.java:115-151).
Launching Main is that first use, and run_app.sh runs pm clear before
this script, so the process is fresh and <clinit> runs exactly once.
The second edge is the table construction itself: new Currency(...)
for each of the 34 table entries (Main.java:117-150). No user action
past launch exists for either edge.
"""

import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from device.harness import Runner  # noqa: E402

EDGE_IDS = ["E4c32b395", "Ea2843361"]
LAUNCHER = "org.billthefarmer.currency/.Main"


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    r = Runner(package=args.package, route="route_15", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, outdir=args.outdir,
               adb=args.adb)
    try:
        # E4c32b395: S_ENTRY -> Main.<clinit>. First use of class Main
        # in a new process: launching the MAIN/LAUNCHER activity Main
        # (AndroidManifest.xml:19-24) triggers class initialisation
        # and builds the static CURRENCIES table.
        r.launch(LAUNCHER, edge="E4c32b395")

        # Ea2843361: Main.<clinit> -> Main$Currency.<init>.
        # new Currency(...) for each of the 34 table entries
        # (Main.java:117-150). This is the target edge; the
        # construction runs inside <clinit>, automatically, with no
        # user action.
        r.comment("automatic: <clinit> constructs all 34 Currency "
                  "table entries", edge="Ea2843361")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
