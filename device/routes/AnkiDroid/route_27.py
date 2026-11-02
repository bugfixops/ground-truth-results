#!/usr/bin/env python3
"""AnkiDroid final-draw route_27: Collection.close().

Target: Collection.close() (via BackupManager.repairCollection).
Table verdict: WRONG (final draw, route_table.md row 27; corrected
    route). The printed BFS route entered the LOAD_FAILED dialog but
    exited via the REPAIR_COLLECTION dialog's onPositive, a
    wrong-dialog-id fiction. The corrected drive below keeps the
    LOAD_FAILED entry and walks the real dialog chain: LOAD_FAILED
    positive -> DIALOG_ERROR_HANDLING -> list selection "repair"
    -> DIALOG_REPAIR_COLLECTION -> onPositive -> repairDeck ->
    printed steps 7-10.
Route followed: corrected route, 10 edges in ROUTES_rows.csv. The
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
    script the three dialog taps share the page edge Ee8da2b4f
    (multi-tap-per-edge convention, as first-draw route_01 did for
    drawer taps), with comments naming the intermediate callbacks.
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
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Ed414cece", "Ee8da2b4f",
    "E599359e9", "Eaae76619", "Eee65a7b8", "E002ceda8", "E5eaacfc5",
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
    # Ed414cece onCreate -> S_DLG_DATABASE_ERROR (LOAD_FAILED
    # dialog; collection did not open).
    r.comment("LOAD_FAILED dialog shown", edge="Ed414cece")
    # Ee8da2b4f S_DLG_DATABASE_ERROR -> DatabaseErrorDialog$4
    # .onPositive, via the real intermediate chain (page-collapsed;
    # see header): LOAD_FAILED positive ("Options", $1.onPositive
    # E61571efb -> showDatabaseErrorDialog E1f36e8b7) shows
    # ERROR_HANDLING; its "Repair database" item ($3.onSelection
    # Ea3ee3296 -> showDatabaseErrorDialog E49c947f6) shows
    # REPAIR_COLLECTION; the return-to-page step has no graph edge.
    r.tap(edge="Ee8da2b4f", text="Options")
    r.tap(edge="Ee8da2b4f", text="Repair database")
    # Ee8da2b4f (same page edge): REPAIR dialog positive "Repair"
    # -> repairDeck (DatabaseErrorDialog.java:207-212).
    r.tap(edge="Ee8da2b4f", text="Repair")
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
