#!/usr/bin/env python3
"""AnkiDroid final-draw route_25: BaseAsyncTask.onProgressUpdate.

Target: BaseAsyncTask.onProgressUpdate (via DeckTask.onProgressUpdate).
Table verdict: WRONG (final draw, route_table.md row 25; corrected
    route). The printed BFS route entered the LOAD_FAILED dialog but
    exited via the RESTORE_BACKUP dialog's onSelection, a
    wrong-dialog-id fiction. The corrected drive below keeps the
    LOAD_FAILED entry and walks the real dialog chain: LOAD_FAILED
    positive -> DIALOG_ERROR_HANDLING -> list selection "restore"
    -> DIALOG_RESTORE_BACKUP -> select a non-empty backup ->
    restoreFromBackup -> printed steps 7-11.
Route followed: corrected route, 11 edges in ROUTES_rows.csv. The
    graph collapses all DatabaseErrorDialog variants into the single
    page node S_DLG_DATABASE_ERROR, so the ROUTES edge chain is the
    page-collapsed chain (identical ids to the printed route); the
    intermediate dialog transitions have graph edges for their
    callbacks (E61571efb $1.onPositive, E1f36e8b7 $1 ->
    showDatabaseErrorDialog, Ea3ee3296 $3.onSelection,
    E49c947f6 $3 -> showDatabaseErrorDialog) but NO graph edge
    returns from showDatabaseErrorDialog to the page node, so the
    expanded chain cannot be made contiguous in graph terms. That
    gap is recorded in NOTES.md; no id is invented for it. In this
    script the three dialog taps share the page edge Ecfd88980
    (multi-tap-per-edge convention, as first-draw route_01 did for
    drawer taps), with comments naming the intermediate callbacks.
    This script is newly written; no first-draw script corresponds
    to this method.
Preconditions/fixtures:
  - Launch state in which the collection fails to load, so the
    LOAD_FAILED dialog is shown (DeckPicker.java:431-433), AND a
    usable collection context for doInBackgroundImportReplace,
    which dereferences col.getPath() (DeckTask.java:758-762). That
    tension is flagged in NOTES.md: if the live run shows
    importReplace cannot proceed from a failed load, the fallback
    is the collection-open menu prefix (action_restore_backup ->
    CONFIRM_RESTORE_BACKUP -> RESTORE_BACKUP, same tail).
  - At least one valid, non-empty backup apkg in the backups
    directory, so the RESTORE_BACKUP list is non-empty. No file
    fixture is pushed: a backup apkg is a binary zip and must not
    be committed; the backup must pre-exist from run setup.
Mapping notes:
  - Dialog texts verified from source/strings, not guessed:
    LOAD_FAILED positive is "Options" (error_handling_options);
    ERROR_HANDLING restore item is "Restore from backup"
    (backup_restore, value 3, offered unconditionally).
  - BACKUP-ITEM GAP: RESTORE_BACKUP list items are dates derived
    from backup filenames, formatted "YYYY-MM-DD (HH:MM h)"
    (DatabaseErrorDialog.java:251-270). The exact item text exists
    only at run time, so it cannot be written statically; the
    script marks the selection with a comment, not a fabricated
    tap. The live run must fill the exact item text from a
    uiautomator dump before this script can run end to end.
  - The import task runs asynchronously and publishes progress only
    after the backup zip opens, unzips, contains collection.anki2,
    and the temp collection validates; the script dwells on the
    onProgressUpdate edge while it runs.
  - No live run is claimed by this script.
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
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Ed414cece", "Ecfd88980",
    "E8606904f", "Edefdf964", "Edd5f59a3", "E19e47dc6", "Eb0fa26f7",
    "Eda96a2a1",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_25")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_25", edge_ids=EDGE_IDS,
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
    # Ed414cece onCreate -> S_DLG_DATABASE_ERROR (LOAD_FAILED
    # dialog; collection did not open).
    r.comment("LOAD_FAILED dialog shown", edge="Ed414cece")
    # Ecfd88980 S_DLG_DATABASE_ERROR -> DatabaseErrorDialog$6
    # .onSelection, via the real intermediate chain (page-collapsed;
    # see header): LOAD_FAILED positive ("Options", $1.onPositive
    # E61571efb -> showDatabaseErrorDialog E1f36e8b7) shows
    # ERROR_HANDLING; its "Restore from backup" item ($3.onSelection
    # Ea3ee3296 -> showDatabaseErrorDialog E49c947f6) shows
    # RESTORE_BACKUP; the return-to-page step has no graph edge.
    r.tap(edge="Ecfd88980", text="Options")
    r.tap(edge="Ecfd88980", text="Restore from backup")
    # BACKUP-ITEM GAP (see header): select a non-empty backup entry
    # from the RESTORE_BACKUP list. Item text is a run-time date
    # ("YYYY-MM-DD (HH:MM h)"); no tap text is fabricated here.
    r.comment("BACKUP-ITEM GAP: tap the non-empty backup entry "
              "(run-time date text; fill from a live uiautomator "
              "dump before a real run)", edge="Ecfd88980")
    # E8606904f $6.onSelection -> DeckPicker.restoreFromBackup
    # (guard: chosen backup file non-empty).
    r.comment("restoreFromBackup", edge="E8606904f")
    # Edefdf964 restoreFromBackup -> DeckPicker.importReplace.
    r.comment("importReplace", edge="Edefdf964")
    # Edd5f59a3 importReplace -> DeckTask.doInBackground
    # @IMPORT_REPLACE (launchDeckTask TASK_TYPE_IMPORT_REPLACE).
    r.comment("IMPORT_REPLACE task launched", edge="Edd5f59a3")
    # E19e47dc6 -> doInBackgroundImportReplace (task-type dispatch).
    r.comment("import-replace background work (valid backup apkg)",
              edge="E19e47dc6")
    # Eb0fa26f7 doInBackgroundImportReplace -> DeckTask
    # .onProgressUpdate (publishProgress after the backup validates).
    r.dwell(edge="Eb0fa26f7", seconds=10)
    # Eda96a2a1 DeckTask.onProgressUpdate ->
    # BaseAsyncTask.onProgressUpdate (target; super call).
    r.comment("BaseAsyncTask.onProgressUpdate (target)",
              edge="Eda96a2a1")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
