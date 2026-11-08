#!/usr/bin/env python3
"""Currency device route script: route_16.

Method: Data.<init>
Edge ids in order:
    E012ed474 Ee88066da E2c242327 E2f8ae154
Printed route file:
    graphs/Currency/scratch/route_print/Data.<init>.txt
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): network (ECB); cert issue on API<=27 images.

Route summary (from the printed route and the trigger graph): launching
Main runs Main.onCreate, which calls Data.getInstance(this)
(Main.java:282); on the first call in the process the singleton is null,
so getInstance constructs a new Data (Data.java:56-57). The target
method therefore fires during launch itself, before any user gesture.

Mapping notes:
- run_app.sh does pm clear before running this script, so the launch
  starts a fresh process and the instance == null guard on edge
  E2f8ae154 holds. No fixture or setup step is needed in this script.
- Lifecycle and CALL edges with no user action are logged with
  r.comment, per the D3 rules. The launch call itself carries the
  first edge id; the remaining edges fire automatically inside
  onCreate, in order, with no further UI step between them.
- Launcher component: AndroidManifest.xml declares activity "Main"
  (no leading dot) with the MAIN/LAUNCHER intent filter, in package
  org.billthefarmer.currency, so the full component is
  org.billthefarmer.currency/org.billthefarmer.currency.Main.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner

PKG = "org.billthefarmer.currency"
ROUTE = "route_16"
EDGES = ["E012ed474", "Ee88066da", "E2c242327", "E2f8ae154"]
LAUNCHER = "org.billthefarmer.currency/org.billthefarmer.currency.Main"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    a = ap.parse_args()
    r = Runner(package=a.package, route=ROUTE, edge_ids=EDGES,
               log_path=a.log, dry_run=a.dry_run, adb=a.adb,
               outdir=a.outdir)
    try:
        # E012ed474 -- Tap the Currency icon in the launcher
        # (MAIN/LAUNCHER intent filter). The harness launch is the
        # adb equivalent; run_app.sh already cleared app data, so
        # this starts a fresh process.
        r.launch(LAUNCHER, edge="E012ed474")
        # Ee88066da -- The system instantiates Main, then calls
        # onCreate (Main.java:242). No user action; follows launch.
        r.comment("system instantiates Main, then calls onCreate",
                  edge="Ee88066da")
        # E2c242327 -- Main.onCreate -> Data.getInstance:
        # data = Data.getInstance(this) (Main.java:282). No user
        # action; runs inside onCreate.
        r.comment("onCreate calls Data.getInstance(this)",
                  edge="E2c242327")
        # E2f8ae154 -- Data.getInstance -> Data.<init>: instance ==
        # null -> new Data() (Data.java:56-57). No user action; the
        # fresh process (pm clear by run_app.sh) makes this the first
        # call, so the constructor runs. This is the route target.
        r.comment("first call in process: instance is null, new Data()",
                  edge="E2f8ae154")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
