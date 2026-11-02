#!/usr/bin/env python3
"""AnkiDroid route_08: SimpleMessageDialog$1.<init>.

Target: SimpleMessageDialog$1.<init> (MaterialDialog ButtonCallback
    in onCreateDialog, SimpleMessageDialog.java:40).
Table verdict: UNCLEAR (first-draw verdict, corrected from FIXED;
    this script drives the F2 derivation, the traversable form).
Route followed: F2 derivation (menu reroute) from
    helper/b6fix-r07-12/CORRECTED_ROUTES.md, with final-graph edge
    ids (14 edges). The printed route entered the LOAD_FAILED/CURSOR
    variant (not colOpen) but needed the CONFIRM_DATABASE_CHECK
    variant; this script enters the CONFIRM dialog from an
    open-collection DeckPicker through the options menu. No page
    split is needed: the menu entry already exists in the graph.
Mapping notes:
  - NO $16 edge is used anywhere. The step-6 rename $15 -> $16 was
    HELD: bytecode shows $15 = CHECK_DATABASE and $16 =
    CHECK_MEDIA, so renaming would create a false edge. The task
    listener here is DeckPicker$15 (CHECK_DATABASE).
  - The SimpleMessageDialog.<init> -> onCreateDialog step
    (Ea9d64477) is INFERRED: it rests on the support-v4
    DialogFragment lifecycle, whose source is not in the tree. The
    script drives the real showSimpleMessageDialog call; the
    lifecycle transition is its direct consequence. This is the step
    that keeps the route UNCLEAR as a graph route; it is marked
    scripted here because the dialog-show action is real and its
    consequence is the target's enclosing dialog creation.
  - Assumption flagged: the integrity check must complete with
    result non-null and true (DeckPicker.java:1160, 1170) for
    showSimpleMessageDialog to run. Whether a healthy collection
    yields that result must be confirmed on a live run; if a
    healthy check shows no message dialog, this script diverges at
    that step and the merger must re-rule the route.
  - Dialog buttons are "OK" / "Cancel" (dialog_ok / dialog_cancel).
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
    "E044ff236", "Ea13b2167", "E748990b0", "E3f20427c", "E32539324",
    "Eb4497af8", "E24224498", "Ea9d64477", "E79016988",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_08")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_08", edge_ids=EDGE_IDS,
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
    # E044ff236 onOptionsItemSelected -> S_DLG_DATABASE_ERROR
    # (action_check_database -> CONFIRM_DATABASE_CHECK dialog).
    r.tap(edge="E044ff236", text="Check database")
    # Ea13b2167 S_DLG_DATABASE_ERROR -> DeckPicker.integrityCheck
    # (guard: dialog variant is DIALOG_CONFIRM_DATABASE_CHECK;
    # positive button, DatabaseErrorDialog.java:294-302).
    r.tap(edge="Ea13b2167", text="OK")
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
    # SimpleMessageDialog.<init>.
    r.comment("dialog instance created", edge="E24224498")
    # Ea9d64477 <init> -> onCreateDialog (INFERRED support-v4
    # lifecycle step).
    r.comment("dialog onCreateDialog (INFERRED lifecycle)",
              edge="Ea9d64477")
    # E79016988 onCreateDialog -> SimpleMessageDialog$1.<init>
    # (target; ButtonCallback at SimpleMessageDialog.java:40).
    r.comment("onCreateDialog builds ButtonCallback $1 (target)",
              edge="E79016988")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
