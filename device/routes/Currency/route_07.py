#!/usr/bin/env python3
"""Device route script for Currency route_07.

Method: ChartActivity.showToast(String)
Edge ids, in order: E012ed474 Ee88066da Ef071a802 E4dd486ed E1d534c40
    E7cc15d45 E32b68288 Ed734335b Efb5de184 E38d20523 E14071438
    E4c809227 E8fefbfc4 Ea1dbc7bc
Printed route file: graphs/Currency/scratch/route_print/ChartActivity.showToast(String).txt
Permissions: none
Fixtures: none
Setup: network (ECB); cert issue on API<=27 images

Network-failure note (edge E4c809227): this route is the FAILURE branch
of ChartActivity.onResume. It fires only when histMap == null and the
network check fails: no connection, or (with the default pref_wifi=true)
a connection that is not Wi-Fi, or roaming with pref_roaming=false
(ChartActivity.java:401-424). No in-app preference combination produces
the toast while the emulator is connected on Wi-Fi and not roaming, and
the Runner contract provides no network-toggle action, so this script
cannot itself switch the network off: it drives the chart navigation
and the toast then follows automatically IF the emulator/CI setup
presents no connection or a non-Wi-Fi connection at ChartActivity
resume. See REPORT.md (conditional assessment on E4c809227); the
merger decides whether a network-off setup step is added outside this
script. The toast text itself ("No connection" / "No WiFi" /
"Roaming", strings.xml) is a transient Toast, not a UI node, so it is
not asserted with assert_text.
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
            "E14071438", "E4c809227", "E8fefbfc4", "Ea1dbc7bc"]
LAUNCHER = "org.billthefarmer.currency/.Main"


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    r = Runner(package=args.package, route="route_07", edge_ids=EDGE_IDS,
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

        # E4dd486ed: Main.onResume -> S_MAIN_DISPLAY. Main is visible
        # in DISPLAY_MODE (fresh pm clear leaves the select list empty,
        # Main.java:351-352). Wait for the header currency code, which
        # is "EUR" by default (DEFAULT_CURRENCY), before touching the
        # list.
        r.wait_for(text="EUR", edge="E4dd486ed")

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

        # E4c809227: ChartActivity.onResume ->
        # ChartActivity.showToast(int,Object[]). Network check failed
        # (ChartActivity.java:401-424): histMap == null on a fresh
        # launch, and the connection is absent, non-Wi-Fi with the
        # default Wi-Fi-only preference, or roaming. This is an
        # automatic branch of onResume, not a tap; the network
        # precondition itself is supplied by the emulator/CI setup
        # (see the header note), not by any Runner action.
        r.comment("automatic branch of onResume: network check fails, "
                  "showToast(no_connection/no_wifi/roaming); network "
                  "precondition comes from emulator setup, not a tap",
                  edge="E4c809227")

        # E8fefbfc4: ChartActivity.showToast(int,Object[]) ->
        # ChartActivity.showToast(String,Object[]). Automatic call
        # showToast(getString(id), args) (ChartActivity.java:1026-1027).
        r.comment("automatic: showToast(int) delegates to "
                  "showToast(String,Object[])", edge="E8fefbfc4")

        # Ea1dbc7bc: ChartActivity.showToast(String,Object[]) ->
        # ChartActivity.showToast(String). Automatic call
        # showToast(String.format(format, args))
        # (ChartActivity.java:1033-1034).
        r.comment("automatic: showToast(String,Object[]) delegates to "
                  "showToast(String)", edge="Ea1dbc7bc")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
