#!/usr/bin/env python3
"""AnkiDroid final-draw route_27: Collection.close().

Target: Collection.close() (via BackupManager.repairCollection).
Drive verdict: combined-merge device drive KEPT (14 edges,
    underscore-page REPAIR drive, gate judge section 3c, NOT the
    new-sample print and NOT the 15-edge @-page variant — its $3
    edge guard says 'route 25 takes the restore branch', which
    contradicts a repair drive). Chain: @LOAD_FAILED -> $1 ->
    legacy ERROR_HANDLING page -> $3.onSelection (guard: value
    2, repair, sqlite3 installed) -> REPAIR page -> $4.onPositive
    (guard: collection non-null so repairCollection reaches
    col.close()) -> repairDeck -> REPAIR_DECK task ->
    repairCollection -> close(). Gate-verified as a route; not
    in the new sample.
Route followed: driven route, 14 edges in ROUTES.csv (REPAIR chain,
    gate judge section 3c). The new graph carries distinct
    @/underscore dialog pages, so the chain below is contiguous
    edge-by-edge (verified in the new JSON); the old page-collapsed
    explanation and the old intermediate callback ids
    (E61571efb/E1f36e8b7/Ea3ee3296/E49c947f6) are OBSOLETE — those
    four ids are ABSENT from the new JSON and must not remain cited
    as live. The three dialog taps now map to distinct edges (see
    body notes).
    This script is newly written; no first-draw script corresponds
    to this method (old route_27 was Decks.id).
Preconditions/fixtures:
  - Launch state in which the collection fails to load, so the
    LOAD_FAILED dialog is shown (DeckPicker.java:431-433), AND a
    non-null collection, because repairCollection dereferences
    col.getPath() (BackupManager.java:243) before reaching
    col.close() at :245. That tension is flagged in NOTES.md.
  - sqlite3 installed on the device, so the ERROR_HANDLING "repair"
    option (value 2) is offered (DatabaseErrorDialog.java:144-148).
    No file fixture is pushed.
Mapping notes:
  - Dialog texts verified from source/strings, not guessed:
    LOAD_FAILED positive is "Options" (error_handling_options);
    ERROR_HANDLING repair item is "Repair database"
    (backup_error_menu_repair, value 2, iff sqlite3 installed);
    REPAIR dialog positive is "Repair" (dialog_positive_repair).
  - REPAIR_DECK is exempt from the collection-null abort
    (DeckTask.java:228), but repairCollection still needs a
    non-null collection to reach close(); see header.
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
    "Eb92c13df", "E7232c65a", "Ef5b276a2", "Eea3ff2de", "E599359e9",
    "Eaae76619", "Eee65a7b8", "E002ceda8", "E5eaacfc5",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_27")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_27", edge_ids=EDGE_IDS,
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
    # dialog; collection did not open).
    r.comment("LOAD_FAILED dialog shown", edge="E76f091e5")
    # Efe87b1dc S_DLG_DATABASE_ERROR@LOAD_FAILED ->
    # DatabaseErrorDialog$1.onPositive (LOAD_FAILED positive,
    # "Options", error_handling_options).
    r.tap(edge="Efe87b1dc", text="Options")
    # Eb92c13df $1.onPositive ->
    # S_DLG_DATABASE_ERROR_ERROR_HANDLING (legacy underscore
    # ERROR_HANDLING page).
    r.comment("error-handling page shown", edge="Eb92c13df")
    # E7232c65a S_DLG_DATABASE_ERROR_ERROR_HANDLING ->
    # DatabaseErrorDialog$3.onSelection (guard: value 2, repair,
    # sqlite3 installed; "Repair database", backup_error_menu_repair).
    r.tap(edge="E7232c65a", text="Repair database")
    # Ef5b276a2 $3.onSelection -> S_DLG_DATABASE_ERROR_REPAIR.
    r.comment("repair page shown", edge="Ef5b276a2")
    # Eea3ff2de S_DLG_DATABASE_ERROR_REPAIR ->
    # DatabaseErrorDialog$4.onPositive (REPAIR dialog positive
    # "Repair", dialog_positive_repair; guard: collection non-null).
    r.tap(edge="Eea3ff2de", text="Repair")
    # E599359e9 $4.onPositive -> DeckPicker.repairDeck.
    r.comment("repairDeck", edge="E599359e9")
    # Eaae76619 repairDeck -> DeckTask.doInBackground@REPAIR_DECK
    # (launchDeckTask TASK_TYPE_REPAIR_DECK).
    r.dwell(edge="Eaae76619", seconds=10)
    # Eee65a7b8 -> doInBackgroundRepairDeck (task-type dispatch).
    r.comment("repair-deck background work", edge="Eee65a7b8")
    # E002ceda8 -> BackupManager.repairCollection (col.close(false)
    # first if col != null, then repair).
    r.comment("repairCollection", edge="E002ceda8")
    # E5eaacfc5 repairCollection -> Collection.close() (target;
    # requires col != null, BackupManager.java:243-245).
    r.comment("Collection.close (target)", edge="E5eaacfc5")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
