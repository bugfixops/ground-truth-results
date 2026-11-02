#!/usr/bin/env python3
"""AnkiDroid final-draw route_25: BaseAsyncTask.onProgressUpdate.

Target: BaseAsyncTask.onProgressUpdate (via DeckTask.onProgressUpdate).
Drive verdict: combined-merge device drive KEPT (17 edges, @
    RESTORE chain, gate judge section 2b, NOT the new-sample
    print and NOT the 13-step sync route). Chain:
    @LOAD_FAILED -> $1.onPositive -> helper@ERROR_HANDLING ->
    @ERROR_HANDLING -> $3.onSelection (restore branch,
    mRepairValues == 3) -> helper@RESTORE_BACKUP ->
    @RESTORE_BACKUP -> $6.onSelection (backup list non-empty,
    chosen backup length > 0) -> restoreFromBackup ->
    importReplace -> IMPORT_REPLACE task -> onProgressUpdate ->
    BaseAsyncTask.onProgressUpdate. The 16-edge
    legacy-underscore variant is NOT used (its $3 guard says
    repair while its onward edge requires restore).
    Gate-verified as a route; not in the new sample.
Route followed: driven route, 17 edges in ROUTES.csv (@ RESTORE
    chain, gate judge section 2b). The new graph carries distinct
    @ dialog pages, so the chain below is contiguous edge-by-edge
    (verified in the new JSON); the old page-collapsed explanation
    and the old intermediate callback ids
    (E61571efb/E1f36e8b7/Ea3ee3296/E49c947f6) are OBSOLETE — those
    four ids are ABSENT from the new JSON and must not remain cited
    as live. The three dialog taps now map to distinct edges (see
    body notes); the old multi-tap-per-edge note ('the three dialog
    taps share the page edge Ecfd88980') is STALE and must be
    deleted wherever it appears.
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
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "E76f091e5", "Efe87b1dc",
    "E096587df", "E832f6db8", "E41b7fcb0", "E041e4962", "Ed4572b17",
    "E28a894d2", "E8606904f", "Edefdf964", "Edd5f59a3", "E19e47dc6",
    "Eb0fa26f7", "Eda96a2a1",
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
    # E76f091e5 DeckPicker.onCreate ->
    # S_DLG_DATABASE_ERROR@LOAD_FAILED (dialog id 0; collection
    # did not open).
    r.comment("LOAD_FAILED dialog shown", edge="E76f091e5")
    # Efe87b1dc S_DLG_DATABASE_ERROR@LOAD_FAILED ->
    # DatabaseErrorDialog$1.onPositive (LOAD_FAILED positive,
    # "Options", error_handling_options).
    r.tap(edge="Efe87b1dc", text="Options")
    # E096587df $1.onPositive ->
    # DeckPicker.showDatabaseErrorDialog@ERROR_HANDLING.
    r.comment("error-handling dialog shown", edge="E096587df")
    # E832f6db8 showDatabaseErrorDialog@ERROR_HANDLING ->
    # S_DLG_DATABASE_ERROR@ERROR_HANDLING.
    r.comment("error-handling page shown", edge="E832f6db8")
    # E41b7fcb0 S_DLG_DATABASE_ERROR@ERROR_HANDLING ->
    # DatabaseErrorDialog$3.onSelection (guard: restore branch,
    # mRepairValues == 3; "Restore from backup", backup_restore).
    r.tap(edge="E41b7fcb0", text="Restore from backup")
    # E041e4962 $3.onSelection ->
    # DeckPicker.showDatabaseErrorDialog@RESTORE_BACKUP.
    r.comment("restore-backup dialog shown", edge="E041e4962")
    # Ed4572b17 showDatabaseErrorDialog@RESTORE_BACKUP ->
    # S_DLG_DATABASE_ERROR@RESTORE_BACKUP.
    r.comment("restore-backup page shown", edge="Ed4572b17")
    # Backup entry (D9): the entry text is a run-time date
    # supplied by setup_route_25.py via GEN_DIR/backup_entry.txt
    # (format "YYYY-MM-DD (HH:MM h)", see NOTES_NEW.md). No date
    # is hard-coded here; if the file is absent, fail loudly
    # rather than tapping a fabricated date.
    _gen = os.environ.get("GEN_DIR", "")
    _entry_path = os.path.join(_gen, "backup_entry.txt") if _gen \
        else os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "backup_entry.txt")
    with open(_entry_path, encoding="utf-8") as _f:
        _backup_entry = _f.read().strip()
    r.tap(edge="E28a894d2", text=_backup_entry)
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
