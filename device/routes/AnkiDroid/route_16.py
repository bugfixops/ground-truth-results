#!/usr/bin/env python3
"""AnkiDroid route_16: Sched.haveBuried(long).

Method: Sched.haveBuried(long)
Target verdict: CORRECT (route_table.md route 16)
Route followed: the final BFS route (10 steps, all correct as printed).
Edge ids in order:
    E48de6d58 E26d20f74 E1ad4ef9b Eb3058057 E53ebd7d4 E3da9d804
    E5d3708ba E55d4b4d0 E5f50a6f6 E22471726
Printed route: graphs/AnkiDroid/scratch/route_print/Sched.haveBuried(long).txt
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (graph env on
    Eb3058057; manifest also declares VIBRATE, INTERNET,
    ACCESS_NETWORK_STATE, RECORD_AUDIO, WAKE_LOCK, none of which this
    route exercises).
Fixtures: collection file collection.anki2 exists; at least one deck
    exists; the deck row tapped is named Default.
Launcher: <package>/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh already does pm clear, permission
    grants, fixture pushes, and per-app setup before this script, so
    the script performs only the route actions starting from launch.
    At merge time this file lives under device/routes/AnkiDroid/, so
    the import below matches the Currency layout exactly.

Mapping notes:
  - The deck row is long-pressed by its deck-name text "Default".
    That text is a fixture value, not an app-source string; verify it
    against a live uiautomator dump before a real run.
  - getListIds and haveBuried run while the context menu is built;
    no further tap is needed after the long-press.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Eb3058057", "E53ebd7d4",
    "E3da9d804", "E5d3708ba", "E55d4b4d0", "E5f50a6f6", "E22471726",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_16")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_16", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate: launch the
    # MAIN/LAUNCHER activity (AndroidManifest.xml:81-89).
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init>: the else
    # branch at IntentHandler.java:132-138 runs (neither ACTION_VIEW
    # nor DO_SYNC). No user action.
    r.comment("launcher else branch starts DeckPicker", edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate: the system
    # instantiates DeckPicker, then onCreate (DeckPicker.java:353).
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # Eb3058057 DeckPicker.onCreate -> S_DECKPICKER: DeckPicker page
    # shown; needs a collection file and WRITE_EXTERNAL_STORAGE.
    r.comment("DeckPicker page shown, collection open", edge="Eb3058057")
    # E53ebd7d4 S_DECKPICKER -> DeckPicker$4.onLongClick: long-press
    # a deck row (DeckPicker.java:229-235, 387).
    r.long_tap(edge="E53ebd7d4", text="Default")
    # E3da9d804 DeckPicker$4.onLongClick ->
    # DeckPickerContextMenu.newInstance: the long-press handler builds
    # the context menu (DeckPicker.java:233). Automatic.
    r.comment("context menu fragment created", edge="E3da9d804")
    # E5d3708ba DeckPickerContextMenu.newInstance ->
    # DeckPickerContextMenu.<init>. Automatic.
    r.comment("context menu fragment instantiated", edge="E5d3708ba")
    # E55d4b4d0 DeckPickerContextMenu.<init> ->
    # DeckPickerContextMenu.onCreateDialog. Automatic.
    r.comment("context menu dialog created", edge="E55d4b4d0")
    # E5f50a6f6 DeckPickerContextMenu.onCreateDialog ->
    # DeckPickerContextMenu.getListIds (DeckPickerContextMenu.java:65).
    # Automatic.
    r.comment("menu item ids computed", edge="E5f50a6f6")
    # E22471726 DeckPickerContextMenu.getListIds ->
    # Sched.haveBuried(long) (DeckPickerContextMenu.java:110).
    # Automatic; this is the target edge.
    r.comment("haveBuried evaluated for the deck", edge="E22471726")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
