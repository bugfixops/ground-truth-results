#!/usr/bin/env python3
"""Currency route_04: ChartActivity.onInvertClick.

Method: ChartActivity.onInvertClick
Edge ids in order:
    E012ed474 Ee88066da Ef071a802 E4dd486ed E1d534c40 E7cc15d45
    E32b68288 Ed734335b Efb5de184 E38d20523 E14071438 E850a7523
    Ed3a105b0 Eb5402ee6 E040559a4 E91d95a61 E39a24f33 E47225cfb
Printed route: graphs/Currency/scratch/route_print/ChartActivity.onInvertClick.txt
    (REACHABLE, SOURCE_OK, ref ChartActivity.java:526-527).
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none.
Setup: network (ECB); cert issue on API<=27 images (ROUTES.csv setup
    column). This route needs the ECB history download to succeed:
    ChartActivity.onResume starts the parse only when network is
    connected and allowed by the Wi-Fi only / Roaming settings
    (ChartActivity.java:427-428), and Invert is enabled only once
    histMap != null (ChartActivity.java:479). On API<=27 images the
    dataset notes a certificate issue with the ECB chain, so a real
    run needs an image where that chain is trusted.
Launcher: org.billthefarmer.currency/.Main (AndroidManifest.xml:18-25,
    MAIN/LAUNCHER). run_app.sh already does pm clear, permission
    grants, fixture pushes, and per-app setup before this script, so
    the script performs only the route actions starting from launch.

Mapping notes:
  - Fresh-install list rows are the default CURRENCY_LIST
    (Main.java:94-97): USD, GBP, CAD, AUD. The header shows the
    current currency EUR (Main.java:393, DEFAULT_CURRENCY), so the
    row text "USD" is unambiguous. Long-pressing it enters
    SELECT_MODE (Main.java:1428-1442).
  - The SELECT menu (res/menu/select.xml) shows its items as icons
    (showAsAction="ifRoom"); the Chart item's title is "Chart"
    (res/values/strings.xml:36), so it is tapped by content
    description, not text.
  - The chart menu (res/menu/chart.xml) likewise shows Invert as an
    icon (showAsAction="ifRoom"); its title is "Invert"
    (res/values/strings.xml:48), so it is tapped by content
    description once the chart is loaded.
  - Chart load wait: while the ECB history is downloading, the chart
    title shows "Updating" (res/values/strings.xml:58;
    ChartActivity.java:265-271); onDataResult restores the pair
    label secondName + "/" + firstName (ChartActivity.java:900-902).
    With current currency EUR and the long-pressed USD row, the
    CHART_LIST is [EUR, USD] (Main.java:955-973), so the loaded
    label is "USD/EUR". The script waits for that text on the loaded
    edge before tapping Invert; a tap before the load would hit a
    disabled Invert item and reach nothing.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E012ed474", "Ee88066da", "Ef071a802", "E4dd486ed", "E1d534c40",
    "E7cc15d45", "E32b68288", "Ed734335b", "Efb5de184", "E38d20523",
    "E14071438", "E850a7523", "Ed3a105b0", "Eb5402ee6", "E040559a4",
    "E91d95a61", "E39a24f33", "E47225cfb",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Currency route_04")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_04", edge_ids=EDGE_IDS,
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
    # E4dd486ed Main.onResume -> S_MAIN_DISPLAY: Main becomes visible
    # in DISPLAY_MODE (Main.java:351-352; pm clear leaves no
    # selection). No user action.
    r.comment("Main visible in DISPLAY_MODE", edge="E4dd486ed")
    # E1d534c40 S_MAIN_DISPLAY -> Main.onItemLongClick: long-press a
    # currency row (Main.java:1428-1442). Fresh-install first default
    # row is USD (Main.java:94-97).
    r.long_tap(edge="E1d534c40", text="USD")
    # E7cc15d45 Main.onItemLongClick -> S_MAIN_SELECT: mode =
    # SELECT_MODE, the row is highlighted (Main.java:1432-1437).
    # Automatic after the long-press. No further action.
    r.comment("SELECT_MODE entered, row highlighted", edge="E7cc15d45")
    # E32b68288 S_MAIN_SELECT -> Main.onOptionsItemSelected@SELECT:
    # tap a menu item in the action bar (res/menu/select.xml).
    # Chart is an ifRoom icon item, tapped by its title description.
    r.tap(edge="E32b68288", desc="Chart")
    # Ed734335b Main.onOptionsItemSelected@SELECT -> Main.onChartClick:
    # switch case R.id.action_chart (Main.java:805-806). Automatic
    # after the tap. No further action.
    r.comment("switch case R.id.action_chart", edge="Ed734335b")
    # Efb5de184 Main.onChartClick -> ChartActivity.<init>:
    # startActivity(ChartActivity, CHART_LIST = [EUR, USD])
    # (Main.java:955-973). Automatic after the tap. No further action.
    r.comment("startActivity(ChartActivity)", edge="Efb5de184")
    # E38d20523 ChartActivity.<init> -> ChartActivity.onCreate: the
    # system instantiates ChartActivity, then onCreate
    # (ChartActivity.java:116). No user action.
    r.comment("system instantiates ChartActivity, then onCreate",
              edge="E38d20523")
    # E14071438 ChartActivity.onCreate -> ChartActivity.onResume:
    # onStart -> onResume (ChartActivity.java:285). No user action.
    r.comment("onStart -> onResume", edge="E14071438")
    # E850a7523 ChartActivity.onResume -> Singleton.startParse:
    # instance.startParse(ECB_QUARTER_URL) (ChartActivity.java:427-
    # 428), when histMap == null and network is connected and allowed
    # by the Wi-Fi only / Roaming settings. Automatic on resume; no
    # user action. Network/ECB setup is run_app.sh's setup step.
    r.comment("onResume starts the ECB history parse",
              edge="E850a7523")
    # Ed3a105b0 Singleton.startParse -> Singleton.lambda$startParse$1:
    # executor.execute(...), worker thread (Singleton.java:104-108).
    # No user action.
    r.comment("worker thread started", edge="Ed3a105b0")
    # Eb5402ee6 Singleton.lambda$startParse$1 ->
    # Singleton.lambda$startParse$0: download parsed, handler.post to
    # the main thread (Singleton.java:114-128); nothing is posted on
    # failure, so this edge needs a successful ECB download over a
    # trusted chain. No user action.
    r.comment("ECB download parsed, posted to main thread",
              edge="Eb5402ee6")
    # E040559a4 Singleton.lambda$startParse$0 ->
    # ChartActivity.onDataResult: listener.onDataResult(parser.getMap())
    # (Singleton.java:126). No user action.
    r.comment("listener.onDataResult(map)", edge="E040559a4")
    # E91d95a61 ChartActivity.onDataResult -> S_CHART_LOADED: chart
    # drawn; invalidateOptionsMenu enables Invert
    # (ChartActivity.java:915-1007, 479). Wait for the loaded pair
    # label "USD/EUR" (title shows "Updating" while downloading).
    r.wait_for(edge="E91d95a61", text="USD/EUR", timeout=60)
    # E39a24f33 S_CHART_LOADED -> ChartActivity.onOptionsItemSelected
    # @LOADED: tap a menu item (res/menu/chart.xml). Invert is an
    # ifRoom icon item, tapped by its title description; it is
    # enabled only now that histMap != null.
    r.tap(edge="E39a24f33", desc="Invert")
    # E47225cfb ChartActivity.onOptionsItemSelected@LOADED ->
    # ChartActivity.onInvertClick: switch case R.id.action_invert
    # (ChartActivity.java:526-527). Automatic after the tap; this is
    # the target edge. No further action.
    r.comment("switch case R.id.action_invert", edge="E47225cfb")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
