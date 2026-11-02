#!/usr/bin/env python3
"""AnkiDroid final-draw route_30: SimpleMessageDialog.<init>.

Target: SimpleMessageDialog.<init> (the fragment's constructor,
    SimpleMessageDialog.java:23: new SimpleMessageDialog()).
Drive verdict: combined-merge device drive KEPT (13 edges,
    MENU @CONFIRM drive, NOT the new-sample print). The new-sample
    row 29 print is CORRECT on its own 10-step showStartup route
    and is NOT this drive. This drive: steps 1-8 shared with
    route_24 through integrityCheck via $9@CONFIRM
    (Ed463497a/Efb51fa08/Efa8d93c4); tail after integrityCheck is
    the success branch E748990b0 -> E3f20427c (guard: result !=
    null && result.getBoolean()) -> showSimpleMessageDialog ->
    newInstance -> <init>. Old generic menu ENTERS
    Ea13b2167/E044ff236 are dropped. Taps unchanged (options
    menu -> Check database -> OK on the CONFIRM dialog -> wait
    for success).
Route followed: corrected route, 12 edges, derived from the graph
    JSON by src/dst pairs and verified contiguous (see NOTES.md).
    This script is adapted from first-draw route_08, but the target
    is DIFFERENT and the adaptation is not blind: first-draw
    route_08 targeted SimpleMessageDialog$1.<init> (a dialog-button
    callback, reached via two further edges Ea9d64477 and
    E79016988 after <init>); this script STOPS at <init>
    (E24224498) and does not use those two edges at all. The menu
    prefix and the integrity-check tail through newInstance are
    shared with route_08 and are reused.
Preconditions/fixtures:
  - Collection open; SD card available so the Check database menu
    item is enabled (DeckPicker.java:528).
  - The integrity check completes with result non-null and true
    (DeckPicker.java:1170), so showSimpleMessageDialog runs instead
    of handleDbError. Whether a healthy collection yields that
    result is flagged in NOTES.md (inherited from route_08's
    assumption flag); if a healthy check shows no message dialog,
    this script diverges at that step. No file fixture is pushed.
Mapping notes:
  - Menu texts: "Check database" (check_db string; also used by
    first-draw route_08) and "OK" (dialog_ok string) for the
    CONFIRM dialog's positive button. The "More options" content
    description is the standard AppCompat overflow description;
    verify it against a live uiautomator dump.
  - NO $16 edge is used anywhere: bytecode shows $15 =
    CHECK_DATABASE and $16 = CHECK_MEDIA, so the task listener here
    is DeckPicker$15 (CHECK_DATABASE), as in first-draw route_08.
  - The <init> step itself is automatic (newInstance allocates the
    fragment); no onCreateDialog step is claimed, unlike route_08.
  - No live run is claimed by this script.
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
    "Ed463497a", "Efb51fa08", "Efa8d93c4", "E748990b0", "E3f20427c",
    "E32539324", "Eb4497af8", "E24224498",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_30")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_30", edge_ids=EDGE_IDS,
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
    # Eb3058057 DeckPicker.onCreate -> S_DECKPICKER (collection open;
    # this open-collection state is required, unlike the printed
    # route's not-colOpen entry).
    r.comment("deck-picker page shown, collection open",
              edge="Eb3058057")
    # Ec0803f80 S_DECKPICKER -> DeckPicker.onOptionsItemSelected:
    # open the options menu.
    r.tap(edge="Ec0803f80", desc="More options")
    # Ed463497a onOptionsItemSelected -> S_DLG_DATABASE_ERROR@CONFIRM
    # (guard: action_check_database).
    # (action_check_database -> CONFIRM_DATABASE_CHECK dialog).
    r.tap(edge="Ed463497a", text="Check database")
    # Efb51fa08 S_DLG_DATABASE_ERROR@CONFIRM ->
    # DatabaseErrorDialog$9.onPositive@CONFIRM (@CONFIRM sole
    # outgoing edge).
    # (guard: dialog variant is DIALOG_CONFIRM_DATABASE_CHECK;
    # positive button, DatabaseErrorDialog.java:294-302).
    r.tap(edge="Efb51fa08", text="OK")
    # Efa8d93c4 DatabaseErrorDialog$9.onPositive@CONFIRM ->
    # DeckPicker.integrityCheck.
    r.comment("integrityCheck", edge="Efa8d93c4")
    # E748990b0 integrityCheck -> DeckPicker$15.onPostExecute
    # (CHECK_DATABASE task listener; $15, NOT $16).
    r.dwell(edge="E748990b0", seconds=10)
    # E3f20427c $15.onPostExecute -> showSimpleMessageDialog
    # (guard: result != null and result.getBoolean(); else
    # handleDbError runs instead -- see header assumption).
    r.comment("check result shows message dialog", edge="E3f20427c")
    # E32539324 showSimpleMessageDialog -> newInstance(String,boolean).
    r.comment("showSimpleMessageDialog builds dialog",
              edge="E32539324")
    # Eb4497af8 newInstance(String,boolean) ->
    # newInstance(String,String,boolean).
    r.comment("newInstance delegates to 3-arg form", edge="Eb4497af8")
    # E24224498 newInstance(String,String,boolean) ->
    # SimpleMessageDialog.<init> (target; fragment constructor,
    # NOT the $1 button callback of first-draw route_08).
    r.comment("dialog instance created (target)", edge="E24224498")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
