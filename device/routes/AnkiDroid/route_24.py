#!/usr/bin/env python3
"""AnkiDroid route_24: Hook.<init>.

Method: Hook.<init>
Target verdict: FIXED (route_table.md route 24)
Route followed: the final BFS route (11 steps), cold-start
    satisfiable. The fix guards are in the graph; the script must
    satisfy them, notably firstCollectionOpen false at DeckPicker
    .java:357 with storage permission granted, SD card mounted, and
    the AnkiDroid directory accessible, so the else-if at :430 runs.
Edge ids in order:
    E48de6d58 E26d20f74 E1ad4ef9b E45d63a96 E37e55142 E4c7e034e
    Eb9dd04e0 E98cbc59f Eeb9f51d0 E483048de Ef693ef80
Printed route: graphs/AnkiDroid/scratch/route_print/Hook.<init>.txt
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (guard at
    DeckPicker.java:420; see route_16 for the full manifest list).
Fixtures: cold start (pm clear, so sInstance is null and the
    collection is not open); preference advanced_statistics_enabled
    true, set by run_app.sh setup before launch.
Launcher: <package>/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh setup precedes this script; see
    route_16. At merge time this file lives under
    device/routes/AnkiDroid/, so the import matches Currency.

Mapping notes:
  - No user action is needed after launch: every step is automatic
    on a cold start. The combined-build duplicate hand edges
    (E45d63a96 F4 and E18aeeb0c F5 for the same call, and E4c7e034e
    F4 and Ea49432e0 F5) are compatible guard variants; this script
    carries the F4 ids from the printed route.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "E45d63a96", "E37e55142",
    "E4c7e034e", "Eb9dd04e0", "E98cbc59f", "Eeb9f51d0", "E483048de",
    "Ef693ef80",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_24")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_24", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init>.
    r.comment("launcher else branch starts DeckPicker", edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # E45d63a96 DeckPicker.onCreate ->
    # CollectionHelper.exceededCursorSizeLimit: cold start, colOpen
    # false, storage permission granted, SD mounted, directory
    # accessible (DeckPicker.java:357, 415-418 else branch, 420-430).
    r.comment("cold-start collection check", edge="E45d63a96")
    # E37e55142 CollectionHelper.exceededCursorSizeLimit ->
    # CollectionHelper.getCol. Automatic.
    r.comment("collection helper requested", edge="E37e55142")
    # E4c7e034e CollectionHelper.getCol ->
    # Storage.Collection(Context,String,boolean,boolean): guard
    # collection not open (CollectionHelper.java:88). Automatic.
    r.comment("storage collection opened", edge="E4c7e034e")
    # Eb9dd04e0 Storage.Collection -> Hooks.getInstance. Automatic.
    r.comment("hooks instance requested", edge="Eb9dd04e0")
    # E98cbc59f Hooks.getInstance -> Hooks.<init>: guard sInstance
    # null, first getInstance call on a cold start (Hooks.java:38-40).
    r.comment("hooks instance created", edge="E98cbc59f")
    # Eeb9f51d0 Hooks.<init> -> AdvancedStatistics.install: guard
    # preference advanced_statistics_enabled true (Hooks.java:61-62).
    r.comment("advanced statistics installed", edge="Eeb9f51d0")
    # E483048de AdvancedStatistics.install ->
    # AdvancedStatistics.<init>. Automatic.
    r.comment("advanced statistics created", edge="E483048de")
    # Ef693ef80 AdvancedStatistics.<init> -> Hook.<init>:
    # AdvancedStatistics extends Hook and neither class declares an
    # explicit constructor, so the default constructor calls super().
    # Automatic; this is the target edge.
    r.comment("Hook constructor reached", edge="Ef693ef80")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
