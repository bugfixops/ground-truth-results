"""Device route script for Currency route_24.

Method: CurrencyWidgetProvider.onUpdate
Edge ids (in route order):
    E012ed474 Ee88066da Ef071a802 E4dd486ed E3b5308ec E2ea0fd55 E3b81bf90
    E1bc51235 E2d9123e2
Printed route file:
    graphs/Currency/scratch/route_print/CurrencyWidgetProvider.onUpdate.txt
Permissions: (none)
Fixtures: (none)
Setup: network (ECB); cert issue on API<=27 images (handled by run_app.sh
    per-app setup, not by this script).

Launcher precondition, read before running: this route carries ENV
other_app -- the printed guard for the final edge is "at least one
Currency widget placed" through the launcher (another app). Placing a
widget on the home screen is a launcher UI action that adb cannot
create: there is no adb command that binds a widget id to the home
screen for this app. The script therefore follows the printed Main
chain up to the app's own broadcast, and then sends the identical
system broadcast the AppWidgetService would deliver for a placed
widget -- ACTION_APPWIDGET_UPDATE with a non-empty id list, addressed
to the manifest provider -- so that super.onReceive dispatches to
onUpdate (AppWidgetProvider dispatch requires a non-empty id list;
the app's own broadcast on a fresh install carries the empty list
returned by getAppWidgetIds, which would stop at onReceive). The
broadcast substitution is recorded in the helper report for the
merger to judge; no route, label, or status file is changed here.
"""

import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from device.harness import Runner

EDGE_IDS = [
    "E012ed474", "Ee88066da", "Ef071a802", "E4dd486ed", "E3b5308ec",
    "E2ea0fd55", "E3b81bf90", "E1bc51235", "E2d9123e2",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_24", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, outdir=args.outdir,
               adb=args.adb)

    # E012ed474: S_ENTRY -> Main.<init>
    # Tap the Currency icon in the launcher (MAIN/LAUNCHER intent filter,
    # AndroidManifest.xml:19-24). Launcher component is Main, declared
    # without a package prefix, so ".Main" under the app package.
    r.launch("org.billthefarmer.currency/.Main", edge="E012ed474")

    # Ee88066da: Main.<init> -> Main.onCreate
    # Lifecycle edge: the system instantiates Main, then calls onCreate
    # (Main.java:242). No user action exists for this edge.
    r.comment("system instantiates Main then calls onCreate; no user action",
              edge="Ee88066da")

    # Ef071a802: Main.onCreate -> Main.onResume
    # Lifecycle edge: onStart -> onResume (Main.java:369). No user action.
    r.comment("onStart -> onResume; no user action", edge="Ef071a802")

    # E4dd486ed: Main.onResume -> S_MAIN_DISPLAY
    # Enters-page edge: Main becomes visible in DISPLAY_MODE (no selection
    # kept, Main.java:351-352). No user action.
    r.comment("Main visible in DISPLAY_MODE; no user action", edge="E4dd486ed")

    # E3b5308ec: S_MAIN_DISPLAY -> Main.onPause
    # System edge: Main loses the foreground (Main.java:700). Pressing
    # HOME is the user/system step that pauses Main; the harness maps
    # HOME to KEYCODE_HOME. Main.onPause then calls updateWidgets and
    # sends its own APPWIDGET_UPDATE broadcast, as in the printed route.
    r.key("HOME", edge="E3b5308ec")

    # E2ea0fd55: Main.onPause -> Main.updateWidgets
    # Call edge: onPause calls updateWidgets() (Main.java:705-742, 838-851).
    # No user action beyond the HOME press above; the call is made by
    # Main itself while pausing.
    r.comment("Main.onPause calls updateWidgets; no user action",
              edge="E2ea0fd55")

    # E3b81bf90: Main.updateWidgets -> CurrencyWidgetProvider.<init>@UPDATE
    # Broadcast edge: updateWidgets sends ACTION_APPWIDGET_UPDATE with
    # EXTRA_UPDATE_DONE=true (Main.java:847-851). On a fresh install
    # with no widget placed, that broadcast carries an empty id list,
    # which AppWidgetProvider dispatch would not forward to onUpdate.
    # This call therefore sends the same action, addressed to the
    # manifest provider (AndroidManifest.xml: receiver
    # CurrencyWidgetProvider, exported, APPWIDGET_UPDATE intent filter),
    # with a non-empty id list (appWidgetIds=[1]) and the same
    # EXTRA_UPDATE_DONE=true extra, standing in for the launcher-placed
    # widget the printed route's ENV requires. See the header note.
    r.broadcast(action="android.appwidget.action.APPWIDGET_UPDATE",
                component="org.billthefarmer.currency/.CurrencyWidgetProvider",
                extras_args=["--eia", "appWidgetIds", "1",
                             "--ez",
                             "org.billthefarmer.currency.EXTRA_UPDATE_DONE",
                             "true"],
                edge="E3b81bf90")

    # E1bc51235: CurrencyWidgetProvider.<init>@UPDATE
    #     -> CurrencyWidgetProvider.onReceive@UPDATE
    # Lifecycle edge: the system calls onReceive for the APPWIDGET_UPDATE
    # broadcast (CurrencyWidgetProvider.java:67-76: reads
    # EXTRA_UPDATE_DONE, then super.onReceive). No user action exists;
    # delivery of the broadcast above is the trigger. The broadcast
    # above sets that extra with --ez to the exact key
    # CurrencyWidgetUpdate.EXTRA_UPDATE_DONE
    # ("org.billthefarmer.currency.EXTRA_UPDATE_DONE",
    # CurrencyWidgetUpdate.java:61-62), matching the app's own
    # updateWidgets broadcast.
    r.comment("system delivers APPWIDGET_UPDATE to onReceive; no user action",
              edge="E1bc51235")

    # E2d9123e2: CurrencyWidgetProvider.onReceive@UPDATE
    #     -> CurrencyWidgetProvider.onUpdate
    # Framework edge: super.onReceive (AppWidgetProvider) dispatches
    # APPWIDGET_UPDATE with a non-empty id list to onUpdate. No user
    # action exists; the dispatch follows from the broadcast above.
    r.comment("super.onReceive dispatches APPWIDGET_UPDATE to onUpdate",
              edge="E2d9123e2")

    r.done()


if __name__ == "__main__":
    main()
