#!/usr/bin/env python3
"""AnkiDroid route_28: NoteEditor.closeNoteEditor(int,Intent).

Method: NoteEditor.closeNoteEditor(int,Intent)
Target verdict: WRONG (route_table.md route 28)
Route followed: the CORRECTED route from the note-editor page (10
    steps), never the BFS dispatch route via the generic page through
    ModelBrowser deleteModelDialog. Prefix: CardBrowser card-row tap
    edits an existing note (edit mode, not add mode). changeNoteType
    appears twice because the first call throws and the confirm
    re-calls it, not because of a duplicated graph edge.
Edge ids in order (prefix 10 + note-editor steps 10):
    E48de6d58 E26d20f74 E1ad4ef9b Eb3058057 Ed1dad133 E0e89f361
    Eb06cba16 E352d419a Ed736a06a E79c27e7e Ec7b4ddbb Ee8811021
    E927dc587 Ed22fab27 E30f7c51d E3cc3b1c8 Ea1cb2a50 Ecbf73392
    E8da0bfba E4b3e5a5a
Sources: route_table.md route 28; helper/b6fix-r25-30/
    CORRECTED_ROUTES.md route 28.
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (graph env on
    Eb3058057; see route_16 for the full manifest list).
Fixtures: collection file exists; deck has cards to study; an
    existing note is opened for editing (edit mode, not mAddNote);
    the note type is changed to a different model
    (!newModel.equals(oldModel)); the card mapping does NOT lose
    cards, so the direct call at NoteEditor.java:701 is taken (not
    the $5 lose-cards dialog at :688-698); schema not yet marked
    changed, so changeNoteType throws ConfirmModSchemaException.
Launcher: <package>/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh setup precedes this script; see
    route_16. At merge time this file lives under
    device/routes/AnkiDroid/, so the import matches Currency.

Mapping notes:
  - Drawer and card-row selectors ("Card browser", the card row)
    are UI values not fixed by the graph edges; verify them against
    a live uiautomator dump before a real run. The card row tapped
    must be a card whose note can change type without losing cards.
  - UNRESOLVED STEP (no edge invented): there is no dedicated graph
    edge from NoteEditor.<init> to S_NOTEEDITOR on this edit path
    (the addNote path carries E70e741c7 instead). The system
    instantiation and editor page are logged with r.comment.
  - PRECONDITION ACTION (no graph edge): changing the note type in
    the editor (note-type selector, choose a different model) must
    happen before Save is tapped; it is logged with r.comment, not
    invented as an edge id.
  - The 16 confirm + 8 cancel virtual-dispatch edges from the
    generic page are deliberately left unsuppressed in the graph;
    this script uses only the variant-page confirm E3cc3b1c8.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Eb3058057", "Ed1dad133",
    "E0e89f361", "Eb06cba16", "E352d419a", "Ed736a06a", "E79c27e7e",
    "Ec7b4ddbb", "Ee8811021", "E927dc587", "Ed22fab27", "E30f7c51d",
    "E3cc3b1c8", "Ea1cb2a50", "Ecbf73392", "E8da0bfba", "E4b3e5a5a",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_28")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_28", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init>.
    r.comment("launcher else branch starts DeckPicker", edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # Eb3058057 DeckPicker.onCreate -> S_DECKPICKER.
    r.comment("DeckPicker page shown, collection open", edge="Eb3058057")
    # Ed1dad133 S_DECKPICKER -> DeckPicker.openCardBrowser: drawer
    # item nav_browser.
    r.tap(edge="Ed1dad133", text="Card browser")
    # E0e89f361 DeckPicker.openCardBrowser -> CardBrowser.<init>.
    r.comment("CardBrowser started", edge="E0e89f361")
    # Eb06cba16 CardBrowser.<init> -> CardBrowser.onCreate.
    r.comment("system instantiates CardBrowser, then onCreate",
              edge="Eb06cba16")
    # E352d419a CardBrowser.onCreate -> S_CARDBROWSER.
    r.comment("card browser page shown", edge="E352d419a")
    # Ed736a06a S_CARDBROWSER -> CardBrowser$7.onItemClick: tap an
    # existing card row to edit its note.
    r.tap(edge="Ed736a06a", text="Default")
    # E79c27e7e CardBrowser$7.onItemClick -> NoteEditor.<init>:
    # edit mode (existing note). Automatic after the tap.
    r.comment("note editor started in edit mode", edge="E79c27e7e")
    # UNRESOLVED STEP (see header): system instantiates NoteEditor
    # and shows the editor page. No NoteEditor.<init> ->
    # S_NOTEEDITOR edge is carried here.
    r.comment("SYSTEM: NoteEditor instantiated, editor page shown", edge="Ec7b4ddbb")
    # PRECONDITION ACTION (see header): change the note type to a
    # different model, with a mapping that does not lose cards.
    r.comment("PRECONDITION: change the note type to a different "
              "model (mapping must not lose cards)", edge="Ec7b4ddbb")
    # Ec7b4ddbb S_NOTEEDITOR -> NoteEditor.onOptionsItemSelected:
    # tap the Save action-bar item (R.id.action_save, :834).
    r.tap(edge="Ec7b4ddbb", desc="Save")
    # Ee8811021 NoteEditor.onOptionsItemSelected ->
    # NoteEditor.saveNote (action_save case, :836). Automatic.
    r.comment("note saved", edge="Ee8811021")
    # E927dc587 NoteEditor.saveNote ->
    # NoteEditor.changeNoteTypeWithErrorHandling (edit mode, model
    # changed, mapping does not lose cards, :684-701). Automatic.
    r.comment("note-type change with error handling",
              edge="E927dc587")
    # Ed22fab27 NoteEditor.changeNoteTypeWithErrorHandling ->
    # NoteEditor.changeNoteType: first, throwing attempt (try at
    # :747-748). Automatic.
    r.comment("note-type change attempted, throws",
              edge="Ed22fab27")
    # E30f7c51d NoteEditor.changeNoteTypeWithErrorHandling ->
    # S_DLG_CONFIRMATION_NOTEEDITOR_CHANGETYPE: guard changeNoteType
    # throws ConfirmModSchemaException (catch block :749-765).
    r.comment("change-type confirmation dialog shown",
              edge="E30f7c51d")
    # E3cc3b1c8 S_DLG_CONFIRMATION_NOTEEDITOR_CHANGETYPE ->
    # NoteEditor$6.confirm: tap Confirm (NoteEditor.java:753-757).
    r.tap(edge="E3cc3b1c8", text="OK")
    # Ea1cb2a50 NoteEditor$6.confirm -> NoteEditor.changeNoteType:
    # second, successful call, after modSchemaNoCheck at :755.
    r.comment("note-type change retried", edge="Ea1cb2a50")
    # Ecbf73392 NoteEditor.changeNoteType ->
    # NoteEditor.closeNoteEditor() (end of changeNoteType, :781).
    r.comment("editor closing, no-arg variant", edge="Ecbf73392")
    # E8da0bfba NoteEditor.closeNoteEditor() ->
    # NoteEditor.closeNoteEditor(Intent) (:932-933). Automatic.
    r.comment("editor closing, intent variant", edge="E8da0bfba")
    # E4b3e5a5a NoteEditor.closeNoteEditor(Intent) ->
    # NoteEditor.closeNoteEditor(int,Intent) (:937-951, target at
    # :960). Automatic; this is the target edge.
    r.comment("editor closed with result", edge="E4b3e5a5a")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
