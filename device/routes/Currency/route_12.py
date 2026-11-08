#!/usr/bin/env python3
"""Device route script for Currency route_12.

Method: ChartActivity.updateRange
Edge ids, in order: E012ed474 Ee88066da Ef071a802 E4dd486ed E1d534c40
    E7cc15d45 E32b68288 Ed734335b Efb5de184 E38d20523 E14071438 Ed074f2c0
    E1a13bbcc Eb738ef7e E8b4ae590
Printed route file: graphs/Currency/scratch/route_print/ChartActivity.updateRange.txt
Permissions: none
Fixtures: none
Setup: network (ECB); cert issue on API<=27 images

State notes: run_app.sh runs pm clear before this script, so Main starts
in DISPLAY_MODE (selectList empty, Main.java:351-352) and ChartActivity
starts with histMap == null, i.e. the S_CHART_LOADING state
(ChartActivity.java:305,479). The list rows come from the default list
after pm clear: CURRENCY_LIST is "USD", "GBP", "CAD", "AUD"
(Main.java:94-97), so the first row's name view reads "USD" (item.xml
name view). In the chart menu (chart.xml) Range is a submenu parent
with showAsAction never, so it is reached through the overflow menu;
Week is its first submenu item (title "Week", strings.xml).
"""

import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from device.harness import Runner  # noqa: E402

EDGE_IDS = ["E012ed474", "Ee88066da", "Ef071a802", "E4dd486ed",
            "E1d534c40", "E7cc15d45", "E32b68288", "Ed734335b",
            "Efb5de184", "E38d20523", "E14071438", "Ed074f2c0",
            "E1a13bbcc", "Eb738ef7e", "E8b4ae590"]
LAUNCHER = "org.billthefarmer.currency/.Main"


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    r = Runner(package=args.package, route="route_12", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, outdir=args.outdir,
               adb=args.adb)
    try:
        # E012ed474: S_ENTRY -> Main.<init>. Tap the Currency icon in
        # the launcher (MAIN/LAUNCHER intent filter; Main is the
        # launcher activity in AndroidManifest.xml:19-24).
        r.launch(LAUNCHER, edge="E012ed474")

        # Ee88066da: Main.<init> -> Main.onCreate. Lifecycle edge: the
        # system instantiates Main, then calls onCreate. No user
        # action exists.
        r.comment("lifecycle: system instantiates Main, then onCreate",
                  edge="Ee88066da")

        # Ef071a802: Main.onCreate -> Main.onResume (onStart ->
        # onResume). Lifecycle edge: no user action exists.
        r.comment("lifecycle: onStart -> onResume", edge="Ef071a802")

        # E4dd486ed: Main.onResume -> S_MAIN_DISPLAY. Main becomes
        # visible in DISPLAY_MODE (no selection kept after pm clear).
        # No user action exists.
        r.comment("Main visible in DISPLAY_MODE after pm clear",
                  edge="E4dd486ed")

        # E1d534c40: S_MAIN_DISPLAY -> Main.onItemLongClick. Long-press
        # a currency row: the first default row is "USD"
        # (CURRENCY_LIST, Main.java:94-97; item.xml name view).
        r.long_tap(text="USD", edge="E1d534c40")

        # E7cc15d45: Main.onItemLongClick -> S_MAIN_SELECT. mode =
        # SELECT_MODE, the row is highlighted (Main.java:1432-1437).
        # Automatic after the long-press; no further action exists.
        r.comment("automatic: long-press switches to SELECT_MODE",
                  edge="E7cc15d45")

        # E32b68288: S_MAIN_SELECT -> Main.onOptionsItemSelected@SELECT.
        # Tap the Chart action (select.xml action_chart, title "Chart",
        # showAsAction ifRoom, so it appears as an icon button whose
        # content-desc is its title). If the icon is folded into the
        # overflow on a narrow screen, the tap raises LookupError and
        # the fallback opens the overflow menu and taps the "Chart"
        # text item instead.
        try:
            r.tap(desc="Chart", edge="E32b68288")
        except LookupError:
            r.tap(desc="More options", edge="E32b68288")
            r.tap(text="Chart", edge="E32b68288")

        # Ed734335b: Main.onOptionsItemSelected@SELECT ->
        # Main.onChartClick. switch case R.id.action_chart
        # (Main.java:805-806). Automatic after the tap; no user
        # action exists.
        r.comment("automatic: switch case R.id.action_chart",
                  edge="Ed734335b")

        # Efb5de184: Main.onChartClick -> ChartActivity.<init>.
        # startActivity(ChartActivity, CHART_LIST) (Main.java:955-973).
        # Automatic after the tap; no user action exists.
        r.comment("automatic: startActivity ChartActivity with "
                  "CHART_LIST", edge="Efb5de184")

        # E38d20523: ChartActivity.<init> -> ChartActivity.onCreate.
        # Lifecycle edge: the system instantiates ChartActivity, then
        # onCreate. No user action exists.
        r.comment("lifecycle: system instantiates ChartActivity, then "
                  "onCreate", edge="E38d20523")

        # E14071438: ChartActivity.onCreate -> ChartActivity.onResume
        # (onStart -> onResume). Lifecycle edge: no user action
        # exists.
        r.comment("lifecycle: onStart -> onResume", edge="E14071438")

        # Ed074f2c0: ChartActivity.onResume -> S_CHART_LOADING. No
        # history yet ("Updating", Invert disabled) because histMap
        # is null after pm clear (ChartActivity.java:305,479). No user
        # action exists.
        r.comment("ChartActivity visible loading: histMap null after "
                  "pm clear", edge="Ed074f2c0")

        # E1a13bbcc: S_CHART_LOADING ->
        # ChartActivity.onOptionsItemSelected@LOADING. Open the
        # overflow menu (Range is showAsAction never in chart.xml),
        # then tap the Range submenu parent. Both taps are menu
        # navigation under this one GUI edge; tapping Range opens its
        # submenu (the action_range dispatch itself falls through to
        # the default branch, per the printed route note).
        r.tap(desc="More options", edge="E1a13bbcc")
        r.tap(text="Range", edge="E1a13bbcc")

        # Eb738ef7e: ChartActivity.onOptionsItemSelected@LOADING ->
        # ChartActivity.onWeekClick. switch case R.id.action_week
        # (ChartActivity.java:542-543): tap the Week submenu item.
        r.tap(text="Week", edge="Eb738ef7e")

        # E8b4ae590: ChartActivity.onWeekClick ->
        # ChartActivity.updateRange. range = WEEK;
        # item.setChecked(true); updateRange()
        # (ChartActivity.java:724-728). Automatic after the Week tap;
        # this is the target edge, no further user action exists.
        r.comment("automatic: onWeekClick sets range WEEK and calls "
                  "updateRange", edge="E8b4ae590")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
