#!/usr/bin/env python3
"""Currency device route script: route_17.

Method: Main.onItemClick
Edge ids in order:
    E012ed474 Ee88066da Ef071a802 E4dd486ed E0e9940ff
Printed route file:
    graphs/Currency/scratch/route_print/Main.onItemClick.txt
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): network (ECB); cert issue on API<=27 images.

Route summary (from the printed route and the trigger graph): launch
Main, reach the main display in DISPLAY_MODE, then tap a currency row;
the tap becomes the current currency (Main.java:1329-1402, DISPLAY_MODE
branch).

Mapping notes:
- DISPLAY_MODE guard (edge E4dd486ed): on a fresh install (pm clear
  by run_app.sh) selectList is empty, so Main.java:351-352 sets mode
  = DISPLAY_MODE, and the DISPLAY_MODE branch of onItemClick runs.
- Row target: on a fresh install onResume populates the list from the
  default CURRENCY_LIST = USD, GBP, CAD, AUD (Main.java:94-97, 558),
  with EUR as the current currency, so a "USD" row is present. The
  tap is by the row's name text ("USD", item.xml name TextView);
  tapping the centre of that text lands inside the row, which the
  ListView delivers as an item click to Main.onItemClick.
- Lifecycle edges with no user action are logged with r.comment,
  per the D3 rules.
- Launcher component: AndroidManifest.xml declares activity "Main"
  with the MAIN/LAUNCHER intent filter, in package
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
ROUTE = "route_17"
EDGES = ["E012ed474", "Ee88066da", "Ef071a802", "E4dd486ed", "E0e9940ff"]
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
        # adb equivalent.
        r.launch(LAUNCHER, edge="E012ed474")
        # Ee88066da -- The system instantiates Main, then calls
        # onCreate (Main.java:242). No user action; follows launch.
        r.comment("system instantiates Main, then calls onCreate",
                  edge="Ee88066da")
        # Ef071a802 -- onStart -> onResume (Main.java:369). No user
        # action; lifecycle step between onCreate and display.
        r.comment("onStart -> onResume", edge="Ef071a802")
        # E4dd486ed -- Main becomes visible (S_MAIN_DISPLAY), mode ==
        # DISPLAY_MODE because selectList is empty on a fresh install
        # (Main.java:351-352). The main ListView (main.xml, id list)
        # appearing is the observable for the display being up.
        r.wait_for(edge="E4dd486ed", res_id="list")
        # E0e9940ff -- Tap a currency row: it becomes the current
        # currency (Main.java:1329-1402). "USD" is the first row of
        # the fresh-install default list; this is the route target.
        r.tap(edge="E0e9940ff", text="USD")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
