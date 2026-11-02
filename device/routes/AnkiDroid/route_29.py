#!/usr/bin/env python3
"""AnkiDroid route_29: DB.executeScript.

Method: DB.executeScript
Target verdict: FIXED (route_table.md route 29)
Route followed: the final BFS route (11 steps). The fix guards are
    in the graph; the script must satisfy them: else-chain
    conditions; !colIsOpen + directory initialisation; server false;
    server false + media .ad.db2 absent.
Edge ids in order:
    E48de6d58 E26d20f74 E1ad4ef9b E45d63a96 E37e55142 E4c7e034e
    E689ba35d E760abd53 E707b4d42 E298eb4b1 E3acef312
Printed route: graphs/AnkiDroid/scratch/route_print/
    DB.executeScript.txt
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (guard at
    DeckPicker.java:420; see route_16 for the full manifest list).
Fixtures: cold start (pm clear, so the collection is not open and
    the media database file does not exist); storage permission
    granted; SD card mounted; AnkiDroid directory accessible; media
    server false.
Launcher: <package>/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh setup precedes this script; see
    route_16. At merge time this file lives under
    device/routes/AnkiDroid/, so the import matches Currency.

Mapping notes:
  - No user action is needed after launch: every step is automatic
    on a cold start with a fresh install state.
  - The combined-build duplicate hand edges (E45d63a96 F4 and
    E18aeeb0c F5; E4c7e034e F4 and Ea49432e0 F5) are compatible guard
    variants; this script carries the F4 ids from the printed route.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "E45d63a96", "E37e55142",
    "E4c7e034e", "E689ba35d", "E760abd53", "E707b4d42", "E298eb4b1",
    "E3acef312",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_29")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_29", edge_ids=EDGE_IDS,
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
    # E689ba35d Storage.Collection ->
    # Collection.<init>(Context,DB,String,boolean,boolean).
    r.comment("collection constructed", edge="E689ba35d")
    # E760abd53 Collection.<init> -> Media.<init>. Automatic.
    r.comment("media constructed", edge="E760abd53")
    # E707b4d42 Media.<init> -> Media.connect: guard server false.
    r.comment("media connected, no server", edge="E707b4d42")
    # E298eb4b1 Media.connect -> Media._initDB: guard server false
    # and media .ad.db2 file absent (create true). Automatic.
    r.comment("media database initialised", edge="E298eb4b1")
    # E3acef312 Media._initDB -> DB.executeScript. Automatic; this
    # is the target edge.
    r.comment("media database script executed", edge="E3acef312")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
