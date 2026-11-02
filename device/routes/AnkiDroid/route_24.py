#!/usr/bin/env python3
"""AnkiDroid final-draw route_24: DB.insert.

Target: DB.insert (Collection._logRem -> mDb.insert("graves", ...)).
Table verdict: WRONG (final draw, route_table.md row 24; corrected
    route). The printed BFS route entered the LOAD_FAILED dialog but
    exited via the CONFIRM_DATABASE_CHECK dialog's onPositive, a
    wrong-dialog-id fiction. The corrected route below replaces the
    prefix with the collection-open prefix: DeckPicker menu
    action_check_database -> CONFIRM dialog -> onPositive ->
    integrityCheck, then printed steps 6-11 unchanged.
Route followed: corrected route, 13 edges, derived from the graph
    JSON by src/dst pairs and verified contiguous (see NOTES.md).
    The menu prefix (Eb3058057, Ec0803f80, E044ff236, Ea13b2167)
    is reused from first-draw route_08 (SimpleMessageDialog$1),
    which drove the same CONFIRM dialog; the tail from
    integrityCheck onward is new (route_08's tail went to the
    message dialog instead).
Preconditions/fixtures:
  - Collection open; SD card available so the Check database menu
    item is enabled (DeckPicker.java:528).
  - A corrupt collection with orphan notes (missing note type,
    wrong field count, or notes with no cards) so fixIntegrity's
    _remNotes branch runs with a non-empty id set and _logRem is
    reached. No file fixture is pushed.
Mapping notes:
  - Menu texts: "Check database" (check_db string; also used by
    first-draw route_08) and "OK" (dialog_ok string) for the
    CONFIRM dialog's positive button. The "More options" content
    description is the standard AppCompat overflow description;
    verify it against a live uiautomator dump.
  - The integrity-check task runs asynchronously; the script dwells
    on the doInBackground@CHECK_DATABASE edge while it runs.
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
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Eb3058057", "Ec0803f80",
    "E044ff236", "Ea13b2167", "Ed79280db", "E0e270167", "E02689004",
    "Ee4200db9", "E441361aa", "E91887e80",
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
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate: launch MAIN/LAUNCHER.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init>.
    r.comment("IntentHandler else branch starts DeckPicker",
              edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # Eb3058057 onCreate -> S_DECKPICKER (collection open).
    r.comment("deck-picker page shown, collection open",
              edge="Eb3058057")
    # Ec0803f80 S_DECKPICKER -> DeckPicker.onOptionsItemSelected:
    # open the options menu.
    r.tap(edge="Ec0803f80", desc="More options")
    # E044ff236 onOptionsItemSelected -> S_DLG_DATABASE_ERROR
    # (action_check_database -> CONFIRM_DATABASE_CHECK dialog).
    r.tap(edge="E044ff236", text="Check database")
    # Ea13b2167 S_DLG_DATABASE_ERROR -> DeckPicker.integrityCheck
    # (CONFIRM dialog positive button, DatabaseErrorDialog
    # .java:294-302). This is the corrected dialog variant, not the
    # printed route's LOAD_FAILED entry.
    r.tap(edge="Ea13b2167", text="OK")
    # Ed79280db integrityCheck -> DeckTask.doInBackground
    # @CHECK_DATABASE (launchDeckTask TASK_TYPE_CHECK_DATABASE).
    r.dwell(edge="Ed79280db", seconds=10)
    # E0e270167 -> doInBackgroundCheckDatabase (task-type dispatch).
    r.comment("check-database background work", edge="E0e270167")
    # E02689004 -> Collection.fixIntegrity (after null check).
    r.comment("fixIntegrity", edge="E02689004")
    # Ee4200db9 fixIntegrity -> Collection._remNotes (orphan-note
    # branches; requires a corrupt collection with orphan notes).
    r.comment("_remNotes (orphan notes)", edge="Ee4200db9")
    # E441361aa _remNotes -> Collection._logRem (ids non-empty).
    r.comment("_logRem", edge="E441361aa")
    # E91887e80 _logRem -> DB.insert (target; insert into "graves").
    r.comment("DB.insert into graves (target)", edge="E91887e80")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
