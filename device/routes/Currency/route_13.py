#!/usr/bin/env python3
"""Device route script for Currency route_13.

Method: ChartParser$Handler.<init>
Edge ids, in order: E012ed474 Ee88066da Ef071a802 E4dd486ed E1d534c40
    E7cc15d45 E32b68288 Ed734335b Efb5de184 E38d20523 E14071438 E850a7523
    Ed3a105b0 Ed937b929 Ef3349d6d
Printed route file: graphs/Currency/scratch/route_print/ChartParser$Handler.<init>.txt
Permissions: none
Fixtures: none
Setup: network (ECB); cert issue on API<=27 images

State and timing notes: run_app.sh runs pm clear before this script, so
Main starts in DISPLAY_MODE (selectList empty, Main.java:351-352) and
ChartActivity starts with histMap == null. On resume, ChartActivity
calls Singleton.startParse(ECB_QUARTER_URL) only when network is
connected and allowed by the Wi-Fi-only / roaming preferences
(ChartActivity.java:427-428 and the connectivity checks above it);
the declared setup provides that network. Everything past the Chart
tap is automatic: the parse runs on a worker thread and
ChartParser.startParser opens the ECB HTTPS stream, after which it
constructs its Handler (ChartParser.java:68-70). There is no user
action past the Chart tap, and the harness offers no sleep step, so
the trailing edges are logged as automatic; on a real run the ECB
download must be allowed to complete (and the TLS chain must be
trusted, which the setup notes is an issue on API<=27 images) before
coverage/logcat is collected for this route.
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
            "Efb5de184", "E38d20523", "E14071438", "E850a7523",
            "Ed3a105b0", "Ed937b929", "Ef3349d6d"]
LAUNCHER = "org.billthefarmer.currency/.Main"


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    r = Runner(package=args.package, route="route_13", edge_ids=EDGE_IDS,
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

        # E850a7523: ChartActivity.onResume -> Singleton.startParse.
        # instance.startParse(ECB_QUARTER_URL)
        # (ChartActivity.java:427-428), automatic on resume when
        # histMap == null and network is connected and allowed by the
        # Wi-Fi-only / roaming preferences. No user action exists.
        r.comment("automatic: onResume starts ECB quarter parse when "
                  "network allowed", edge="E850a7523")

        # Ed3a105b0: Singleton.startParse ->
        # Singleton.lambda$startParse$1. executor.execute(...):
        # worker thread (Singleton.java:104-108), guard parsing ==
        # false. Automatic; no user action exists.
        r.comment("automatic: worker thread executes the parse task",
                  edge="Ed3a105b0")

        # Ed937b929: Singleton.lambda$startParse$1 ->
        # ChartParser.startParser(String). parser.startParser(url):
        # 90-day or full history XML (Singleton.java:114). Automatic;
        # no user action exists.
        r.comment("automatic: worker thread starts the ChartParser",
                  edge="Ed937b929")

        # Ef3349d6d: ChartParser.startParser(String) ->
        # ChartParser$Handler.<init>. new Handler() after the HTTPS
        # stream opened (ChartParser.java:68-70). This is the target
        # edge; it fires on the worker thread once the ECB download
        # stream opens. No user action exists.
        r.comment("automatic: Handler constructed after ECB HTTPS "
                  "stream opens", edge="Ef3349d6d")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
