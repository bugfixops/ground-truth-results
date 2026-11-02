#!/usr/bin/env python3
"""Currency device route script: route_18.

Method: Main.onRefreshClick
Edge ids in order:
    E012ed474 Ee88066da Ef071a802 E4dd486ed Efc50320e Edfe4fcf5
Printed route file:
    graphs/Currency/scratch/route_print/Main.onRefreshClick.txt
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): network (ECB); cert issue on API<=27 images.

Route summary (from the printed route and the trigger graph): launch
Main, reach the main display in DISPLAY_MODE, tap the Refresh action
bar item, and onOptionsItemSelected dispatches case R.id.action_refresh
to onRefreshClick (Main.java:781-782).

Mapping notes:
- DISPLAY_MODE guard (edge E4dd486ed): on a fresh install (pm clear
  by run_app.sh) selectList is empty, so Main.java:351-352 sets mode
  = DISPLAY_MODE and onCreateOptionsMenu inflates res/menu/main.xml.
- Refresh target: main.xml declares action_refresh with
  showAsAction="ifRoom" and title "@string/refresh" = "Refresh"
  (res/values/strings.xml:6). An icon-only action item exposes its
  title as its content-desc, so the tap uses desc="Refresh". Both
  icon items (Add, Refresh) are ifRoom, so on a standard emulator
  width Refresh is shown in the bar rather than folded into overflow.
- The final CALL edge fires from the menu tap itself (switch case),
  so it is logged with r.comment, per the D3 rules; onRefreshClick
  runs on entry regardless of the later connectivity checks inside
  it, so no network state is needed to reach the method.
- Lifecycle edges with no user action are logged with r.comment.
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
ROUTE = "route_18"
EDGES = ["E012ed474", "Ee88066da", "Ef071a802", "E4dd486ed", "Efc50320e",
         "Edfe4fcf5"]
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
        # Efc50320e -- Tap a menu item in the action bar (menu
        # main.xml: action_add / action_refresh / action_update).
        # Refresh is the ifRoom icon item titled "Refresh".
        r.tap(edge="Efc50320e", desc="Refresh")
        # Edfe4fcf5 -- Main.onOptionsItemSelected@DISPLAY ->
        # Main.onRefreshClick: switch case R.id.action_refresh
        # (Main.java:781-782). No further user action; the menu tap
        # above dispatches directly here. This is the route target.
        r.comment("switch case R.id.action_refresh calls onRefreshClick",
                  edge="Edfe4fcf5")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
