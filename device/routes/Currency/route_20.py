#!/usr/bin/env python3
"""Currency device route script: route_20.

Method: Main.onActivityResult
Edge ids in order:
    E012ed474 Ee88066da Ef071a802 E4dd486ed Efc50320e E81249289
    Ea8c3b3b7 E66b0b6ad Ea6de7fcb Eb4cf7f67
Printed route file:
    graphs/Currency/scratch/route_print/Main.onActivityResult.txt
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): network (ECB); cert issue on API<=27 images.

Route summary (from the printed route and the trigger graph): launch
Main, reach the main display in DISPLAY_MODE, tap the Add action bar
item, which starts ChoiceDialog for result (Main.java:857-858); then
press Back, which closes the picker with the default RESULT_CANCELED,
and Main.onActivityResult runs to its early return
(Main.java:1446-1449, resultCode != RESULT_OK).

Mapping notes:
- DISPLAY_MODE guard (edge E4dd486ed): on a fresh install (pm clear
  by run_app.sh) selectList is empty, so Main.java:351-352 sets mode
  = DISPLAY_MODE and onCreateOptionsMenu inflates res/menu/main.xml.
- Add target: main.xml declares action_add with
  showAsAction="ifRoom" and title "@string/add" = "Add"
  (res/values/strings.xml:5). An icon-only action item exposes its
  title as its content-desc, so the tap uses desc="Add".
- The INTENT edge (Ea8c3b3b7) is deliberately NOT sent as a separate
  r.start_intent call: onAddClick itself starts ChoiceDialog with
  startActivityForResult(intent, 0), and only that for-result launch
  delivers a result to Main.onActivityResult. A plain am start from
  the script would open a second picker instance whose Back would
  merely resume Main without calling onActivityResult. The edge is
  therefore logged with r.comment as the direct consequence of the
  Add tap, and the Back step below exercises the real result path.
- Picker-shown observable (edge Ea6de7fcb): choose.xml has a Cancel
  button (id cancel, "@string/cancel" = "Cancel",
  res/values/strings.xml:35), so wait_for text="Cancel" proves the
  dialog-themed picker is up before Back is pressed.
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
ROUTE = "route_20"
EDGES = ["E012ed474", "Ee88066da", "Ef071a802", "E4dd486ed", "Efc50320e",
         "E81249289", "Ea8c3b3b7", "E66b0b6ad", "Ea6de7fcb", "Eb4cf7f67"]
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
        # Add is the ifRoom icon item titled "Add".
        r.tap(edge="Efc50320e", desc="Add")
        # E81249289 -- Main.onOptionsItemSelected@DISPLAY ->
        # Main.onAddClick: switch case R.id.action_add
        # (Main.java:777-778). No further user action; the menu tap
        # above dispatches directly here.
        r.comment("switch case R.id.action_add calls onAddClick",
                  edge="E81249289")
        # Ea8c3b3b7 -- Main.onAddClick -> ChoiceDialog.<init>@MAIN:
        # startActivityForResult(new Intent(this, ChoiceDialog.class),
        # 0) (Main.java:857-858). No separate script intent: only
        # this for-result launch delivers a result to Main, so the
        # edge is the direct consequence of the Add tap above.
        r.comment("onAddClick starts ChoiceDialog for result (request 0)",
                  edge="Ea8c3b3b7")
        # E66b0b6ad -- The system instantiates ChoiceDialog
        # (dialog-themed activity, AndroidManifest.xml:31-33), then
        # onCreate (ChoiceDialog.java:59). No user action.
        r.comment("system instantiates ChoiceDialog, then onCreate",
                  edge="E66b0b6ad")
        # Ea6de7fcb -- ChoiceDialog.onCreate@MAIN ->
        # S_CHOICE_DISPLAY@MAIN: picker shown, nothing selected
        # (ChoiceDialog.java:96-129; choose.xml). The Cancel button
        # proves the picker is up.
        r.wait_for(edge="Ea6de7fcb", text="Cancel")
        # Eb4cf7f67 -- Back closes the picker with the default
        # RESULT_CANCELED, delivering to Main.onActivityResult, which
        # returns early (Main.java:1446-1449). This is the route
        # target: the method is entered even on the cancel path.
        r.back(edge="Eb4cf7f67")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
