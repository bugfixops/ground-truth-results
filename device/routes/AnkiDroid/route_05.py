#!/usr/bin/env python3
"""AnkiDroid route_05 (final draw): libanki.Utils$1.<init>.

Target: libanki.Utils$1.<init> (anonymous FileFilter in
    Utils.getImportableDecks, Utils.java:910).
Table verdict: CORRECT (final draw, 14 steps; the BFS route IS the
    judged route, so this script drives the BFS route).
Route followed: final-draw BFS route from helper/judge-final/
    route_05.txt, edge ids verified against
    graphs/AnkiDroid/out/ankidroid_trigger_graph.json and
    methods.csv (route_edge_ids identical). Reused from the
    first-draw Utils$1 script (old route_07) with a new edge list:
    the final BFS route enters through the HINT dialog's positive
    button and takes the @SELECT dialog-id chain directly
    (S_DLG_IMPORT -> ImportDialog$1.onPositive -> showImportDialog
    @SELECT -> ... -> onCreateDialog@SELECT -> getImportableDecks
    -> $1.<init>). The old script's repeated HINT/SELECT instance
    steps are NOT reused: this BFS route abstracts the HINT dialog
    show into the S_DLG_IMPORT page, so the script taps Import and
    then the HINT dialog's OK button, and comments the remaining
    @SELECT steps.
Dialog-id split respected throughout: the HINT dialog's positive
    button yields SELECT, and SELECT propagates unchanged through
    the showImportDialog overloads and newInstance, so the
    onCreateDialog SELECT branch (which calls getImportableDecks)
    is the one taken.
Preconditions (see ROUTES_rows.csv setup cell):
  - Collection open; WRITE_EXTERNAL_STORAGE granted;
    collection.anki2 exists in the AnkiDroid folder.
  - The AnkiDroid directory exists and is a directory, so the
    getImportableDecks guard (dir.exists() and dir.isDirectory(),
    Utils.java:909-910) holds and the FileFilter is instantiated.
Mapping notes:
  - Selectors verified against the printed tree: "Import"
    (menu_import string), "OK" carried from the old script for the
    HINT dialog's positive button (flagged unverified in NOTES.md;
    confirm the HINT dialog's positive label against a live dump).
  - The "More options" content description is the standard AppCompat
    overflow description; verify it against a live uiautomator dump
    before a real run.
  - The ImportDialog.<init> -> onCreateDialog step (E3ad99a6a) is
    INFERRED: it rests on the support-v4 DialogFragment lifecycle,
    whose source is not in the tree. The script drives the real show
    call; the lifecycle transition is its direct consequence.
    (The route evidence says support-v4 here; routes 06/07/08 of
    this batch are the ones whose evidence wrongly says androidx.)
Launcher: com.ichi2.anki/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh already does pm clear, permission
    grants, fixture pushes, and per-app setup before this script, so
    the script performs only the route actions starting from launch.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Eb3058057", "Ec0803f80",
    "Ef124bec5", "E284aeafe", "Ecce72970", "Eaee0b2f0", "Edf68a935",
    "Ec6e3c8ef", "E3ad99a6a", "E2538c512", "Ecb463f10",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_05")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_05", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate: launch MAIN/LAUNCHER.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init>.
    r.comment("IntentHandler else branch starts DeckPicker",
              edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # Eb3058057 DeckPicker.onCreate -> S_DECKPICKER (collection file
    # exists, WRITE_EXTERNAL_STORAGE granted).
    r.comment("deck-picker page shown", edge="Eb3058057")
    # Ec0803f80 S_DECKPICKER -> DeckPicker.onOptionsItemSelected:
    # open the options menu.
    r.tap(edge="Ec0803f80", desc="More options")
    # Ef124bec5 onOptionsItemSelected -> S_DLG_IMPORT
    # (action_import -> showImportDialog(DIALOG_IMPORT_HINT),
    # DeckPicker.java:561-563).
    r.tap(edge="Ef124bec5", text="Import")
    # E284aeafe S_DLG_IMPORT -> ImportDialog$1.onPositive: tap the
    # HINT dialog's positive button (ImportDialog.java:75-77; the
    # positive at :76 calls showImportDialog(DIALOG_IMPORT_SELECT)).
    r.tap(edge="E284aeafe", text="OK")
    # Ecce72970 $1.onPositive -> DeckPicker.showImportDialog(int)
    # @SELECT.
    r.comment("HINT positive enters SELECT", edge="Ecce72970")
    # Eaee0b2f0 showImportDialog(int)@SELECT ->
    # showImportDialog(int,String)@SELECT (DeckPicker.java:1089).
    r.comment("showImportDialog delegates (id still SELECT)",
              edge="Eaee0b2f0")
    # Edf68a935 showImportDialog(int,String)@SELECT ->
    # ImportDialog.newInstance@SELECT (DeckPicker.java:1095).
    r.comment("SELECT dialog newInstance", edge="Edf68a935")
    # Ec6e3c8ef newInstance@SELECT -> ImportDialog.<init>@SELECT
    # (ImportDialog.java:49).
    r.comment("SELECT dialog instance created", edge="Ec6e3c8ef")
    # E3ad99a6a <init>@SELECT -> onCreateDialog@SELECT (INFERRED
    # support-v4 DialogFragment lifecycle; the shown fragment's
    # onCreateDialog at ImportDialog.java:59 is called by the
    # framework once shown).
    r.comment("SELECT dialog onCreateDialog (INFERRED lifecycle)",
              edge="E3ad99a6a")
    # E2538c512 onCreateDialog@SELECT -> Utils.getImportableDecks
    # (SELECT branch, ImportDialog.java:88).
    r.comment("SELECT case calls getImportableDecks", edge="E2538c512")
    # Ecb463f10 getImportableDecks -> Utils$1.<init> (target;
    # Utils.java:910 dir.listFiles(new FileFilter(){...}); the
    # anonymous FileFilter IS Utils$1, instantiated at the listFiles
    # call under the directory guard).
    r.comment("directory guard instantiates FileFilter $1 (target)",
              edge="Ecb463f10")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
