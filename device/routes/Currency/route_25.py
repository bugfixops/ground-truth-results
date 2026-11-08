"""Device route script for Currency route_25.

Method: CurrencyWidgetProvider.onDeleted
Edge ids (in route order):
    E1cfacc94 E1d8b2e92 Ef32416ec E6b2b4384 Ee3672287 E0f9de2df Eaa043033
Printed route file:
    graphs/Currency/scratch/route_print/CurrencyWidgetProvider.onDeleted.txt
Permissions: (none)
Fixtures: (none)
Setup: network (ECB); cert issue on API<=27 images (handled by run_app.sh
    per-app setup, not by this script).

Launcher precondition, read before running: this route carries ENV
other_app and does NOT start from the app icon. Its printed chain
starts when the launcher, after a widget is dropped on the home screen,
starts the configure activity (android:configure in res/xml/widget.xml;
AndroidManifest.xml:42-48, CurrencyWidgetConfigure, exported, with an
APPWIDGET_CONFIGURE intent filter). Placing a widget is a launcher UI
action that adb cannot create, and the launcher's deletion of a widget
id whose configuration returned RESULT_CANCELED is likewise a launcher
action, not an app action. The script therefore reproduces both
launcher-mediated steps with the exact intents the launcher would use:
(1) start the configure activity directly with the APPWIDGET_CONFIGURE
action and an appWidgetId extra, and (2) after Cancel is tapped, send
the APPWIDGET_DELETED broadcast the AppWidgetService would deliver
for the deleted id, addressed to the manifest provider. The broadcast
substitution is recorded in the helper report for the merger to judge;
no route, label, or status file is changed here.
"""

import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from device.harness import Runner

EDGE_IDS = [
    "E1cfacc94", "E1d8b2e92", "Ef32416ec", "E6b2b4384", "Ee3672287",
    "E0f9de2df", "Eaa043033",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_25", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, outdir=args.outdir,
               adb=args.adb)

    # E1cfacc94: S_ENTRY -> CurrencyWidgetConfigure.<init>@ADD
    # Entry edge: after the widget is dropped, the launcher starts the
    # configure activity (android:configure, res/xml/widget.xml;
    # AndroidManifest.xml:42-48). This script starts that same activity
    # directly, because adb cannot place a widget through the launcher.
    # The configure activity reads EXTRA_APPWIDGET_ID ("appWidgetId")
    # from the intent (CurrencyWidgetConfigure.java:98-101), so the id
    # is supplied here; the Cancel path used below does not depend on
    # its value, but supplying it keeps the intent faithful to the
    # launcher's. Note this is deliberately NOT r.launch of Main: the
    # printed route does not start from the app icon.
    r.start_intent(action="android.appwidget.action.APPWIDGET_CONFIGURE",
                   component="org.billthefarmer.currency/.CurrencyWidgetConfigure",
                   extras_args=["--ei", "appWidgetId", "1"],
                   edge="E1cfacc94")

    # E1d8b2e92: CurrencyWidgetConfigure.<init>@ADD
    #     -> CurrencyWidgetConfigure.onCreate@ADD
    # Lifecycle edge: the system instantiates CurrencyWidgetConfigure
    # (dialog theme), then onCreate (CurrencyWidgetConfigure.java:51).
    # No user action exists for this edge.
    r.comment("system instantiates CurrencyWidgetConfigure then onCreate",
              edge="E1d8b2e92")

    # Ef32416ec: CurrencyWidgetConfigure.onCreate@ADD -> S_WIDGET_CONFIG@ADD
    # Enters-page edge: dialog listing the Main list currencies
    # (CurrencyWidgetConfigure.java:88-165; res/layout/config.xml, list
    # plus Cancel button). No user action beyond what follows.
    r.comment("widget configure dialog shown; no user action yet",
              edge="Ef32416ec")

    # E6b2b4384: S_WIDGET_CONFIG@ADD
    #     -> CurrencyWidgetConfigure.lambda$onCreate$1@ADD
    # Tap Cancel (CurrencyWidgetConfigure.java:121-125: setResult
    # (RESULT_CANCELED); finish()). The button text is "Cancel"
    # (res/values/strings.xml: cancel; res/layout/config.xml, id/cancel).
    r.tap(text="Cancel", edge="E6b2b4384")

    # Ee3672287: CurrencyWidgetConfigure.lambda$onCreate$1@ADD
    #     -> CurrencyWidgetProvider.<init>@DELETED
    # Intent/system edge: RESULT_CANCELED while placing means the
    # launcher deletes the new widget id and APPWIDGET_DELETED reaches
    # the provider (AppWidgetServiceImpl.java:1752-1767, per the printed
    # route). A bare start of the configure activity cannot produce
    # that launcher deletion on its own, so this call sends the same
    # APPWIDGET_DELETED broadcast, addressed to the manifest provider
    # (AndroidManifest.xml: receiver CurrencyWidgetProvider, exported,
    # APPWIDGET_UPDATE intent filter; the provider is the app's
    # AppWidgetProvider receiver), with the deleted id list
    # (appWidgetIds=[1], the id used at the configure step). See the
    # header note.
    r.broadcast(action="android.appwidget.action.APPWIDGET_DELETED",
                component="org.billthefarmer.currency/.CurrencyWidgetProvider",
                extras_args=["--eia", "appWidgetIds", "1"],
                edge="Ee3672287")

    # E0f9de2df: CurrencyWidgetProvider.<init>@DELETED
    #     -> CurrencyWidgetProvider.onReceive@DELETED
    # Lifecycle edge: the system instantiates the receiver and calls
    # onReceive for APPWIDGET_DELETED (CurrencyWidgetProvider.java:67-76).
    # No user action exists; delivery of the broadcast above is the
    # trigger.
    r.comment("system delivers APPWIDGET_DELETED to onReceive; no action",
              edge="E0f9de2df")

    # Eaa043033: CurrencyWidgetProvider.onReceive@DELETED
    #     -> CurrencyWidgetProvider.onDeleted
    # Framework edge: super.onReceive (AppWidgetProvider) dispatches
    # APPWIDGET_DELETED to onDeleted, which removes the per-widget
    # preference (CurrencyWidgetProvider.java: onDeleted). No user
    # action exists; the dispatch follows from the broadcast above.
    r.comment("super.onReceive dispatches APPWIDGET_DELETED to onDeleted",
              edge="Eaa043033")

    r.done()


if __name__ == "__main__":
    main()
