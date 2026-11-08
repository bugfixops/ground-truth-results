#!/usr/bin/env python3
"""Currency device route script: route_19.

Method: Main.onCopyClick
Edge ids in order:
    E012ed474 Ee88066da Ef071a802 E4dd486ed E1d534c40 E7cc15d45
    E32b68288 Ea8d13ea1
Printed route file:
    graphs/Currency/scratch/route_print/Main.onCopyClick.txt
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): network (ECB); cert issue on API<=27 images.

Route summary (from the printed route and the trigger graph): launch
Main, reach the main display in DISPLAY_MODE, long-press a currency
row to enter SELECT_MODE (Main.java:1428-1442), then tap the Copy
action bar item, and onOptionsItemSelected dispatches case
R.id.action_copy to onCopyClick (Main.java:809-810).

Mapping notes:
- DISPLAY_MODE guard (edge E4dd486ed): on a fresh install (pm clear
  by run_app.sh) selectList is empty, so Main.java:351-352 sets mode
  = DISPLAY_MODE.
- Long-press target: on a fresh install onResume populates the list
  from the default CURRENCY_LIST = USD, GBP, CAD, AUD
  (Main.java:94-97, 558), so a "USD" row is present. Long-pressing
  it clears selectList and adds that row's position
  (Main.java:1436-1437), so onCopyClick has a non-empty selection
  to copy (Main.java:877-910).
- Copy target: on entering SELECT_MODE, onCreateOptionsMenu inflates
  res/menu/select.xml, whose action_copy item has
  showAsAction="ifRoom" and title "@string/copy" = "Copy"
  (res/values/strings.xml:33). An icon-only action item exposes its
  title as its content-desc, so the tap uses desc="Copy".
- The ENTERS edge into S_MAIN_SELECT and the final CALL edge fire
  from the long-press and the menu tap respectively, with no further
  user action, so they are logged with r.comment, per the D3 rules.
  (wait_for cannot express the select-menu state: it accepts only
  text/res_id, and the Copy item is an icon with a content-desc.)
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
ROUTE = "route_19"
EDGES = ["E012ed474", "Ee88066da", "Ef071a802", "E4dd486ed", "E1d534c40",
         "E7cc15d45", "E32b68288", "Ea8d13ea1"]
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
        # E1d534c40 -- Long-press a currency row (Main.java:1428-1442).
        # "USD" is the first row of the fresh-install default list;
        # the long-press switches to SELECT_MODE and selects it.
        r.long_tap(edge="E1d534c40", text="USD")
        # E7cc15d45 -- Main.onItemLongClick -> S_MAIN_SELECT: mode =
        # SELECT_MODE, the row is highlighted (Main.java:1432-1437)
        # and the menu is invalidated to select.xml. No separate user
        # action; this is the direct consequence of the long-press.
        r.comment("long-press sets SELECT_MODE and invalidates the menu",
                  edge="E7cc15d45")
        # E32b68288 -- Tap a menu item in the action bar (menu
        # select.xml). Copy is the ifRoom icon item titled "Copy".
        r.tap(edge="E32b68288", desc="Copy")
        # Ea8d13ea1 -- Main.onOptionsItemSelected@SELECT ->
        # Main.onCopyClick: switch case R.id.action_copy
        # (Main.java:809-810). No further user action; the menu tap
        # above dispatches directly here. This is the route target.
        r.comment("switch case R.id.action_copy calls onCopyClick",
                  edge="Ea8d13ea1")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
