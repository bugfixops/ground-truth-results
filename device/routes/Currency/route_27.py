"""route_27: CurrencyWidgetUpdate.onDestroy (download-success branch).

Method: CurrencyWidgetUpdate.onDestroy
Edge ids (in route order):
    E1cfacc94 E1d8b2e92 Ef32416ec E50df3be1 Efb41e4e7 E09a1f5d6 E0ae51971
    E9ac79ef7 E38f6e26f E73c27e78 E85c5656c Ec8ea5917 E00d748b7 E8c73e084
    E3226d82d E279da83c
Printed route file:
    graphs/Currency/scratch/route_print/CurrencyWidgetUpdate.onDestroy.txt
Permissions: none (empty on the ROUTES.csv row; INTERNET and
    ACCESS_NETWORK_STATE are install-time only and need no grant).
Fixtures: none (empty on the ROUTES.csv row).
Setup: network (ECB); cert issue on API<=27 images.
    run_app.sh does pm clear, permission grants, fixture pushes, and
    per-app setup before running this script; this script performs only
    the route actions below.

Widget-route approximation (read before judging the first edges):
    The true first step is the launcher (another app) placing a Currency
    widget on the home screen, which starts the exported configure
    activity (res/xml/widget.xml android:configure; AndroidManifest
    lines 42-48). adb cannot place a widget through the launcher UI, so
    this script starts that same configure activity directly with the
    APPWIDGET_CONFIGURE action. Likewise the widget refresh icon does
    not exist on the home screen under this approximation, so the
    refresh step starts CurrencyWidgetRefresh directly -- it is the
    exact PendingIntent target the widget's refresh icon fires
    (CurrencyWidgetProvider.java:218-223,249). Everything after the
    refresh launch is app/framework code, not user action, and is
    comment()ed edge by edge.
"""

import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from device.harness import Runner

EDGE_IDS = [
    "E1cfacc94", "E1d8b2e92", "Ef32416ec", "E50df3be1", "Efb41e4e7",
    "E09a1f5d6", "E0ae51971", "E9ac79ef7", "E38f6e26f", "E73c27e78",
    "E85c5656c", "Ec8ea5917", "E00d748b7", "E8c73e084", "E3226d82d",
    "E279da83c",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_27", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, outdir=args.outdir,
               adb=args.adb)

    # E1cfacc94 -- ENTRY: launcher starts the configure activity after
    # the widget is dropped (android:configure). Approximation: start
    # the exported configure activity directly with the same action.
    # appWidgetId extra: the configure activity reads
    # AppWidgetManager.EXTRA_APPWIDGET_ID ("appWidgetId") from its
    # intent; 1 stands in for the id the launcher would have bound.
    r.start_intent(edge="E1cfacc94",
                   action="android.appwidget.action.APPWIDGET_CONFIGURE",
                   component="org.billthefarmer.currency/.CurrencyWidgetConfigure",
                   extras_args=["--ei", "appWidgetId", "1"])

    # E1d8b2e92 -- LIFECYCLE: system instantiates
    # CurrencyWidgetConfigure (dialog theme), then onCreate. No user
    # action exists for this edge.
    r.comment("system instantiates CurrencyWidgetConfigure, then onCreate",
              edge="E1d8b2e92")

    # Ef32416ec -- ENTERS: onCreate sets the config layout, showing the
    # dialog listing the Main list currencies. Page entry, no action.
    r.comment("config dialog appears, listing the Main list currencies",
              edge="Ef32416ec")

    # E50df3be1 -- GUI: tap a currency for the widget. The config list
    # falls back to Main.CURRENCY_LIST ("USD", "GBP", "CAD", "AUD") on a
    # fresh install, so its first row's name node reads "USD"
    # (choice.xml R.id.name). The tap stores the position, sends the
    # APPWIDGET_UPDATE broadcast, sets RESULT_OK, and finishes -- all
    # done by the app itself on the item click.
    r.tap(text="USD", edge="E50df3be1")

    # Efb41e4e7 -- ENTERS: setResult(RESULT_OK); finish() returns to
    # the home screen with the widget. App-driven, no script action.
    r.comment("configure finishes with RESULT_OK; home screen with widget",
              edge="Efb41e4e7")

    # E09a1f5d6 -- GUI: tap the refresh icon on the widget. The icon's
    # PendingIntent is getActivity(CurrencyWidgetRefresh), so this
    # script starts that exact activity directly: under the configure
    # approximation above no widget is actually placed, so no refresh
    # icon exists on the home screen to tap.
    r.start_intent(edge="E09a1f5d6",
                   component="org.billthefarmer.currency/.CurrencyWidgetRefresh")

    # E0ae51971 -- LIFECYCLE: system instantiates the invisible
    # (Theme.NoDisplay) refresh activity, then onCreate. No action.
    r.comment("system instantiates CurrencyWidgetRefresh, then onCreate",
              edge="E0ae51971")

    # E9ac79ef7 -- INTENT: CurrencyWidgetRefresh.onCreate itself calls
    # startService(CurrencyWidgetUpdate) once its network guard passes
    # (connected, and allowed by the Wi-Fi-only / Roaming prefs). The
    # refresh launch above is the action that causes it; there is no
    # separate script step. If the guard fails, the service never
    # starts and the later edges do not fire.
    r.comment("Refresh.onCreate starts CurrencyWidgetUpdate when its "
              "network guard passes; no separate script action",
              edge="E9ac79ef7")

    # E38f6e26f -- LIFECYCLE: system instantiates the service, then
    # onCreate (which registers the service as the Data listener).
    r.comment("system instantiates CurrencyWidgetUpdate, then onCreate",
              edge="E38f6e26f")

    # E73c27e78 -- LIFECYCLE: startService -> onStartCommand.
    r.comment("startService delivers onStartCommand", edge="E73c27e78")

    # E85c5656c -- CALL: onStartCommand calls startUpdate().
    r.comment("onStartCommand calls startUpdate()", edge="E85c5656c")

    # Ec8ea5917 -- CALL: startUpdate calls data.startParse(ECB_DAILY_URL).
    r.comment("startUpdate calls data.startParse(ECB_DAILY_URL)",
              edge="Ec8ea5917")

    # E00d748b7 -- ASYNC: executor worker thread; guard parsing == false
    # (no download already running). Framework threading, no action.
    r.comment("executor worker thread starts the ECB download",
              edge="E00d748b7")

    # E8c73e084 -- ASYNC (success branch): startParser returned true,
    # so the worker posts onDateResult(date) and onDataResult(map) back
    # to the main thread. This branch is environment-determined, not a
    # user action: it requires the ECB HTTPS download to succeed over
    # a trusted certificate chain. On API<=27 images the noted
    # certificate issue may instead take the failure branch (route_26).
    r.comment("download parsed: worker posts results to the main "
              "thread; environment-determined, no user action",
              edge="E8c73e084")

    # E3226d82d -- CALL: listener.onDataResult(parser.getMap()).
    # Callback on the main thread; no user action exists.
    r.comment("listener.onDataResult(map) runs on the main thread",
              edge="E3226d82d")

    # E279da83c -- LIFECYCLE: onDataResult calls stopSelf() (for a
    # non-empty map, after updating prefs) -> onDestroy, which removes
    # the Data listener. Service lifecycle, no user action. This is
    # the target method.
    r.comment("onDataResult calls stopSelf() -> onDestroy",
              edge="E279da83c")

    r.done()


if __name__ == "__main__":
    main()
