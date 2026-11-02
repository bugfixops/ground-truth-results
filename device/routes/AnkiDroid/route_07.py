#!/usr/bin/env python3
"""AnkiDroid route_07: libanki.Utils$1.<init>.

Target: libanki.Utils$1.<init> (anonymous FileFilter in
    getImportableDecks, Utils.java:910).
Table verdict: WRONG (first-draw verdict; this script drives the
    CORRECTED derivation, never the printed BFS route).
Route followed: CORRECTED derivation (SELECT entry) from
    helper/b6fix-r07-12/CORRECTED_ROUTES.md, with final-graph edge
    ids (18 edges, second instance repeated). The printed route
    fixed the dialog id to DIALOG_IMPORT_ADD_CONFIRM, whose case
    never calls getImportableDecks; only the SELECT case does. This
    script enters through the HINT dialog: menu Import -> HINT ->
    positive -> SELECT.
Preconditions/fixtures:
  - Collection open; Import menu reachable.
  - The AnkiDroid directory exists and is a directory, so the
    getImportableDecks guard (dir.exists() and dir.isDirectory(),
    Utils.java:909-910) holds and the FileFilter is instantiated.
Mapping notes:
  - The ImportDialog.<init> -> onCreateDialog steps (E88404d0f,
    both instances) are INFERRED: they rest on the support-v4
    DialogFragment lifecycle, whose source is not in the tree. The
    script drives the real show calls; the lifecycle transition is
    their direct consequence.
  - ImportDialog.onCreateDialog -> S_DLG_IMPORT (the dialog being
    shown) has no dedicated graph edge; it is a page abstraction,
    noted in the E88404d0f comments, not given an invented id.
  - The HINT dialog's positive button is ImportDialog$1.onPositive
    (ImportDialog.java:75-77; the positive at :76 calls
    showImportDialog(DIALOG_IMPORT_SELECT)).
  - The "More options" content description is the standard AppCompat
    overflow description; verify it against a live uiautomator dump
    before a real run.
Launcher: com.ichi2.anki/.IntentHandler (AndroidManifest.xml:81-89).
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Eb3058057", "Ec0803f80",
    "Ed832b176", "E0ca886ae", "Eb7dfd04d", "E2da7107c", "E88404d0f",
    "E284aeafe", "E2821c117", "E0ca886ae", "Eb7dfd04d", "E2da7107c",
    "E88404d0f", "Ee61e1dd8", "Ecb463f10",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_07")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_07", edge_ids=EDGE_IDS,
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
    # Eb3058057 DeckPicker.onCreate -> S_DECKPICKER.
    r.comment("deck-picker page shown", edge="Eb3058057")
    # Ec0803f80 S_DECKPICKER -> DeckPicker.onOptionsItemSelected:
    # open the options menu.
    r.tap(edge="Ec0803f80", desc="More options")
    # Ed832b176 onOptionsItemSelected -> showImportDialog(int):
    # action_import shows the HINT dialog (DeckPicker.java:561-563).
    r.tap(edge="Ed832b176", text="Import")
    # E0ca886ae showImportDialog(int) -> showImportDialog(int,String).
    r.comment("showImportDialog delegates", edge="E0ca886ae")
    # Eb7dfd04d showImportDialog -> ImportDialog.newInstance.
    r.comment("HINT dialog newInstance", edge="Eb7dfd04d")
    # E2da7107c newInstance -> ImportDialog.<init>.
    r.comment("HINT dialog instance created", edge="E2da7107c")
    # E88404d0f <init> -> onCreateDialog (INFERRED support-v4
    # lifecycle; the dialog is then shown: S_DLG_IMPORT page
    # abstraction, no dedicated edge).
    r.comment("HINT dialog onCreateDialog (INFERRED lifecycle; "
              "dialog shown, page abstraction, no dedicated edge)",
              edge="E88404d0f")
    # E284aeafe S_DLG_IMPORT -> ImportDialog$1.onPositive: tap OK on
    # the HINT dialog (dialog_ok = "OK").
    r.tap(edge="E284aeafe", text="OK")
    # E2821c117 $1.onPositive -> showImportDialog(int): the HINT
    # positive calls showImportDialog(DIALOG_IMPORT_SELECT).
    r.comment("HINT positive enters SELECT", edge="E2821c117")
    # E0ca886ae showImportDialog(int) -> showImportDialog(int,String).
    r.comment("showImportDialog delegates", edge="E0ca886ae")
    # Eb7dfd04d showImportDialog -> ImportDialog.newInstance (SELECT).
    r.comment("SELECT dialog newInstance", edge="Eb7dfd04d")
    # E2da7107c newInstance -> ImportDialog.<init> (SELECT).
    r.comment("SELECT dialog instance created", edge="E2da7107c")
    # E88404d0f <init> -> onCreateDialog (SELECT; INFERRED).
    r.comment("SELECT dialog onCreateDialog (INFERRED lifecycle)",
              edge="E88404d0f")
    # Ee61e1dd8 onCreateDialog -> getImportableDecks (guard: mType
    # == DIALOG_IMPORT_SELECT, ImportDialog.java:86-88; the
    # ADD_CONFIRM case never calls it).
    r.comment("SELECT case calls getImportableDecks", edge="Ee61e1dd8")
    # Ecb463f10 getImportableDecks -> Utils$1.<init> (target; guard:
    # dir.exists() and dir.isDirectory(), Utils.java:909-910).
    r.comment("directory guard instantiates FileFilter $1 (target)",
              edge="Ecb463f10")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
