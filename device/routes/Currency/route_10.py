#!/usr/bin/env python3
"""Device route script for Currency route_10.

Method: Singleton.setMap
Edge ids, in order: E012ed474 Ee88066da Ef071a802 E4dd486ed E1d534c40
    E7cc15d45 E32b68288 Ed734335b Efb5de184 E38d20523 E14071438
    Ed074f2c0 E007921cb E362e566f
Printed route file: graphs/Currency/scratch/route_print/Singleton.setMap.txt
Permissions: none
Fixtures: none
Setup: network (ECB); cert issue on API<=27 images

Pause note: edge E007921cb is "ChartActivity loses the foreground"
(ChartActivity.java:433). The trigger graph's own gui list for this
edge offers "Press Home" first, so the script presses HOME; onPause
then stores the (still null on a fresh launch) history map via
Singleton.setMap. No history download is needed for setMap itself:
ChartActivity.onPause calls instance.setMap(histMap) unconditionally
when the singleton instance exists (ChartActivity.java:441-446).
"""

import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from device.harness import Runner  # noqa: E402

EDGE_IDS = ["E012ed474", "Ee88066da", "Ef071a802", "E4dd486ed", "E1d534c40",
            "E7cc15d45", "E32b68288", "Ed734335b", "Efb5de184", "E38d20523",
            "E14071438", "Ed074f2c0", "E007921cb", "E362e566f"]
LAUNCHER = "org.billthefarmer.currency/.Main"


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    r = Runner(package=args.package, route="route_10", edge_ids=EDGE_IDS,
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

        # E4dd486ed: Main.onResume -> S_MAIN_DISPLAY. Main becomes
        # visible in DISPLAY_MODE (fresh pm clear leaves the select
        # list empty, Main.java:351-352). No user action exists.
        r.comment("automatic: Main visible in DISPLAY_MODE",
                  edge="E4dd486ed")

        # E1d534c40: S_MAIN_DISPLAY -> Main.onItemLongClick. Long-press
        # a currency row. The default list (CURRENCY_LIST) starts with
        # USD, so the first row's code text is "USD" (item.xml name
        # view); the header shows EUR, so "USD" matches only a list row.
        r.long_tap(text="USD", edge="E1d534c40")

        # E7cc15d45: Main.onItemLongClick -> S_MAIN_SELECT. Entering
        # SELECT_MODE is the automatic result of the long-press
        # (Main.java:1432-1437). No further user action exists.
        r.comment("automatic: long-press enters SELECT_MODE and "
                  "highlights the row", edge="E7cc15d45")

        # E32b68288: S_MAIN_SELECT -> Main.onOptionsItemSelected@SELECT.
        # Tap a menu item in the action bar (menu select.xml). The
        # chart item is shown as an icon (showAsAction="ifRoom") with
        # title "Chart" (strings.xml), so its action-bar button carries
        # content-desc "Chart".
        r.tap(desc="Chart", edge="E32b68288")

        # Ed734335b: Main.onOptionsItemSelected@SELECT -> Main.onChartClick.
        # Switch case R.id.action_chart (Main.java:805-806). Automatic
        # consequence of the Chart tap. No user action exists.
        r.comment("automatic: select-menu case action_chart calls "
                  "onChartClick", edge="Ed734335b")

        # Efb5de184: Main.onChartClick -> ChartActivity.<init>. Intent
        # edge: startActivity(ChartActivity) with CHART_LIST
        # (Main.java:955-973). Automatic consequence of onChartClick.
        r.comment("automatic: onChartClick starts ChartActivity",
                  edge="Efb5de184")

        # E38d20523: ChartActivity.<init> -> ChartActivity.onCreate.
        # Lifecycle edge: the system instantiates ChartActivity, then
        # onCreate. No user action exists.
        r.comment("lifecycle: system instantiates ChartActivity, then "
                  "onCreate", edge="E38d20523")

        # E14071438: ChartActivity.onCreate -> ChartActivity.onResume
        # (onStart -> onResume). Lifecycle edge: no user action exists.
        r.comment("lifecycle: onStart -> onResume", edge="E14071438")

        # Ed074f2c0: ChartActivity.onResume -> S_CHART_LOADING. No
        # history yet (histMap == null on a fresh launch), so the chart
        # shows "Updating" and Invert is disabled
        # (ChartActivity.java:305,479). The "Updating" text is drawn
        # on the chart canvas, not a UI node, so there is no wait_for
        # target; the state follows automatically from onResume.
        r.comment("automatic: histMap null, chart in loading state",
                  edge="Ed074f2c0")

        # E007921cb: S_CHART_LOADING -> ChartActivity.onPause.
        # ChartActivity loses the foreground. Press HOME, the first
        # gui option the trigger graph lists for this edge.
        r.key("HOME", edge="E007921cb")

        # E362e566f: ChartActivity.onPause -> Singleton.setMap.
        # Automatic: onPause stores the history map via
        # instance.setMap(histMap) (ChartActivity.java:445). No user
        # action exists.
        r.comment("automatic: onPause calls instance.setMap(histMap)",
                  edge="E362e566f")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
