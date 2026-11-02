"""Device route script for Currency route_23.

Method: CurrencyWidgetProvider.onReceive
Edge ids (in route order):
    E012ed474 Ee88066da Ef071a802 E4dd486ed E3b5308ec E2ea0fd55 E3b81bf90
    E1bc51235
Printed route file:
    graphs/Currency/scratch/route_print/CurrencyWidgetProvider.onReceive.txt
Permissions: (none)
Fixtures: (none)
Setup: network (ECB); cert issue on API<=27 images (handled by run_app.sh
    per-app setup, not by this script).

Note on the start of this route: the target is reached through a widget
broadcast, but the printed route reaches that broadcast through Main:
launch Main, then let Main lose the foreground, which makes Main.onPause
call updateWidgets, which sends the APPWIDGET_UPDATE broadcast. The
provider's onReceive runs on delivery regardless of the widget-id list
(CurrencyWidgetProvider.java:67-76 reads EXTRA_UPDATE_DONE and then
delegates to super.onReceive). This script follows that printed chain
exactly; it does not substitute a hand-made broadcast, because the app
itself sends the broadcast on pause.
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
    "E2ea0fd55", "E3b81bf90", "E1bc51235",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_23", edge_ids=EDGE_IDS,
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
    # HOME to KEYCODE_HOME.
    r.key("HOME", edge="E3b5308ec")

    # E2ea0fd55: Main.onPause -> Main.updateWidgets
    # Call edge: onPause calls updateWidgets() (Main.java:705-742, 838-851).
    # No user action beyond the HOME press above; the call is made by
    # Main itself while pausing.
    r.comment("Main.onPause calls updateWidgets; no user action",
              edge="E2ea0fd55")

    # E3b81bf90: Main.updateWidgets -> CurrencyWidgetProvider.<init>@UPDATE
    # Broadcast edge: updateWidgets sends an implicit
    # ACTION_APPWIDGET_UPDATE broadcast with EXTRA_UPDATE_DONE=true
    # (Main.java:847-851), resolved by action name to the manifest
    # receiver (AndroidManifest.xml: receiver CurrencyWidgetProvider,
    # exported, APPWIDGET_UPDATE intent filter). The system instantiates
    # the provider on delivery. No script broadcast is needed or added:
    # the app sends this broadcast itself on pause.
    r.comment("app sends APPWIDGET_UPDATE; system instantiates the provider",
              edge="E3b81bf90")

    # E1bc51235: CurrencyWidgetProvider.<init>@UPDATE
    #     -> CurrencyWidgetProvider.onReceive@UPDATE
    # Lifecycle edge: the system calls onReceive for the APPWIDGET_UPDATE
    # broadcast (CurrencyWidgetProvider.java:67-76). No user action
    # exists; delivery of the broadcast above is the trigger.
    r.comment("system delivers APPWIDGET_UPDATE to onReceive; no user action",
              edge="E1bc51235")

    r.done()


if __name__ == "__main__":
    main()
