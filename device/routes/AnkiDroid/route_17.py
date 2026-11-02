#!/usr/bin/env python3
"""AnkiDroid route_17: DeckPicker$5.onProgressUpdate.

Target: DeckPicker$5.onProgressUpdate.
Table verdict: CORRECT (final-draw verdict; this script drives the
    printed BFS route, 16 edges, unchanged).
Route followed: printed route: deck picker -> Import dialog ->
    importAdd -> IMPORT task -> AnkiPackageImporter.run ->
    publishProgress -> ProgressCallback -> doProgress ->
    onProgressUpdate@IMPORT -> TaskListener -> DeckPicker$5.
Preconditions: collection open; collection.anki2 exists;
    WRITE_EXTERNAL_STORAGE granted; an importable .apkg file (not
    named collection.apkg) present in the AnkiDroid folder, supplied
    by run setup (this script pushes no file); the import must run
    long enough for progress publication (the progress dialog shows
    values while importing).
Mapping notes:
  - No old first-draw script targets this method; the import-dialog
    walk is the same newly written walk as route_15 (hint OK ->
    select file -> Add), from ImportDialog.java:67-134 with
    res-verified texts.
  - "More options" is the standard AppCompat overflow description;
    verify it against a live uiautomator dump before a real run.
Launcher: com.ichi2.anki/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh already does pm clear, permission
    grants, fixture pushes, and per-app setup before this script, so
    the script performs only the route actions starting from launch.
Draft status: final-draw device draft for the merger; dry/static
    checks only. No live run has been performed with this script, and
    nothing in this file claims one.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Eb3058057", "Ec0803f80",
    "Ef124bec5", "Ef971cdc8", "E7207076d", "E3b62fa3a", "E1a9a3f49",
    "Ea7661a21", "E394ac0d1", "E88dc87aa", "E821efdb6", "E215233c1",
    "Eda073348",
]


FIXTURE_APKG_STEM = "import"


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_17")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_17", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate: launch MAIN/LAUNCHER.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init> (else branch).
    r.comment("IntentHandler else branch starts DeckPicker",
              edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # Eb3058057 DeckPicker.onCreate -> S_DECKPICKER (collection file
    # exists, WRITE_EXTERNAL_STORAGE granted).
    r.comment("deck-picker page shown", edge="Eb3058057")
    # Ec0803f80 S_DECKPICKER -> onOptionsItemSelected: open the
    # options menu (standard AppCompat overflow description).
    r.tap(edge="Ec0803f80", desc="More options")
    # Ef124bec5 onOptionsItemSelected -> S_DLG_IMPORT
    # (action_import). String verified in res: menu_import =
    # "Import".
    r.tap(edge="Ef124bec5", text="Import")
    # S_DLG_IMPORT page (ImportDialog): the graph collapses the
    # hint dialog, the select list, and the add-confirm dialog
    # into this one page. The taps below walk those stages in
    # order and are logged under the importAdd edge, following
    # the shared-page convention used for dialog stages in the
    # old scripts; only the final "Add" tap is the edge's own
    # action. The select list shows .apkg file names without
    # the extension, so the fixture stem is tapped, not the
    # full filename. The file itself is a run-setup
    # precondition (placed in the AnkiDroid folder before the
    # run); this script pushes no file.
    r.tap(edge="Ef971cdc8", text="OK")
    r.tap(edge="Ef971cdc8", text=FIXTURE_APKG_STEM)
    # Ef971cdc8 S_DLG_IMPORT -> DeckPicker.importAdd: tap "Add"
    # on the add-confirm dialog (string verified in res:
    # import_message_add = "Add"). Files named collection.apkg
    # would take the REPLACE confirm instead, so the fixture
    # must not carry that name.
    r.tap(edge="Ef971cdc8", text="Add")
    # E7207076d importAdd -> DeckTask.doInBackground@IMPORT.
    r.comment("IMPORT task launched", edge="E7207076d")
    # E3b62fa3a -> doInBackgroundImportAdd.
    r.comment("doInBackgroundImportAdd", edge="E3b62fa3a")
    # E1a9a3f49 -> AnkiPackageImporter.run.
    r.comment("AnkiPackageImporter.run", edge="E1a9a3f49")
    # E1a9a3f49 -> AnkiPackageImporter.run.
    r.comment("AnkiPackageImporter.run", edge="E1a9a3f49")
    # Ea7661a21 AnkiPackageImporter.run -> Anki2Importer.publishProgress
    # (also Anki2Importer.run calls publishProgress at :89 and
    # inside _import at :128, :131; the importer publishes on the
    # IMPORT path unconditionally once started).
    r.comment("importer publishes progress", edge="Ea7661a21")
    # E394ac0d1 Anki2Importer.publishProgress ->
    # DeckTask$ProgressCallback.publishProgress (callback installed
    # at DeckTask.java:751, so the null guard passes).
    r.comment("ProgressCallback.publishProgress", edge="E394ac0d1")
    # E88dc87aa -> DeckTask.doProgress.
    r.comment("doProgress", edge="E88dc87aa")
    # E821efdb6 doProgress -> onProgressUpdate@IMPORT (framework
    # delivery; wait for the progress dialog to update).
    r.dwell(edge="E821efdb6", seconds=5)
    # E215233c1 onProgressUpdate@IMPORT ->
    # TaskListener.onProgressUpdate@IMPORT.
    r.comment("listener onProgressUpdate", edge="E215233c1")
    # Eda073348 TaskListener -> DeckPicker$5.onProgressUpdate
    # (target; the mImportAddListener passed at DeckPicker.java:1580,
    # body at :260-262).
    r.comment("DeckPicker$5 onProgressUpdate (target)",
              edge="Eda073348")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
