#!/usr/bin/env python3
"""AnkiDroid route_22: libanki.Utils.base62.

Method: libanki.Utils.base62
Target verdict: WRONG (route_table.md route 22)
Route followed: the CORRECTED route, never the printed BFS route.
    New-note construction (NoteEditor.setNote -> Note(col,model,null)
    -> guid64 -> base91 -> base62). DISMISS alone cannot save the
    tail: a correct DISMISS launch still ends at card.note() with a
    non-null id, and the Note-constructor id==null branch conflicts
    with the non-null id supplied by getNote.
Edge ids in order:
    E48de6d58 E26d20f74 E1ad4ef9b Eb3058057 Ed1dad133 E0e89f361
    Eb06cba16 E352d419a E0281e707 E37ba8c1f E34bd403a Ef9f80682
    E80e8ad56 E62a24da3 Ed4aa2957 E4a0aec25
Sources: route_table.md route 22; helper/b6fix-r19-24/
    CORRECTED_ROUTES.md route 22.
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (graph env on
    Eb3058057; see route_16 for the full manifest list).
Fixtures: collection file exists; a current model exists; the editor
    is opened for ADDING a note, so setNote sees a null note and
    builds a new Note (NoteEditor.java:1366-1370). No field text is
    needed: guid64 runs in the constructor before any editing.
Launcher: <package>/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh setup precedes this script; see
    route_16. At merge time this file lives under
    device/routes/AnkiDroid/, so the import matches Currency.

Mapping notes:
  - Drawer and menu selectors ("Card browser", "Add") are UI strings
    not fixed by the graph edges; verify them against a live
    uiautomator dump before a real run.
  - The parallel launch edge E83452f16 (CardBrowser
    .onOptionsItemSelected -> NoteEditor.<init>) is the same Add tap
    as the page edge E37ba8c1f; the edge list carries the page edge
    and the editor instantiation is a system step.
  - UNRESOLVED STEP (no edge invented): there is no dedicated graph
    edge from S_NOTEEDITOR to NoteEditor.onCollectionLoaded. The
    system instantiation, onCreate, and collection load are logged
    with r.comment.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Eb3058057", "Ed1dad133",
    "E0e89f361", "Eb06cba16", "E352d419a", "E0281e707", "E37ba8c1f",
    "E34bd403a", "Ef9f80682", "E80e8ad56", "E62a24da3", "Ed4aa2957",
    "E4a0aec25",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_22")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_22", edge_ids=EDGE_IDS,
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
    # E0281e707 S_CARDBROWSER -> CardBrowser.onOptionsItemSelected:
    # open the options menu.
    r.tap(edge="E0281e707", text="Add")
    # E37ba8c1f CardBrowser.onOptionsItemSelected -> S_NOTEEDITOR:
    # guard action_add_card_from_card_browser, drawer toggle does
    # not consume the item. Automatic after the tap.
    r.comment("note editor page shown (add-card flow)",
              edge="E37ba8c1f")
    # UNRESOLVED STEP (see header): system instantiates NoteEditor,
    # onCreate runs, the collection loads. No S_NOTEEDITOR ->
    # onCollectionLoaded edge exists in the final graph.
    r.comment("SYSTEM: NoteEditor instantiated, collection loaded", edge="E34bd403a")
    # E34bd403a NoteEditor.onCollectionLoaded ->
    # NoteEditor.setNote(Note): adding a note, so setNote builds a
    # new Note with the current model (NoteEditor.java:1366-1370).
    r.comment("new note construction started", edge="E34bd403a")
    # Ef9f80682 NoteEditor.setNote(Note) ->
    # Note.<init>(Collection,JSONObject). Automatic.
    r.comment("two-arg Note constructor", edge="Ef9f80682")
    # E80e8ad56 Note.<init>(Collection,JSONObject) ->
    # Note.<init>(Collection,JSONObject,Long) with id null
    # (Note.java:58-59). Automatic.
    r.comment("three-arg Note constructor, id null", edge="E80e8ad56")
    # E62a24da3 Note.<init>(Collection,JSONObject,Long) ->
    # libanki.Utils.guid64: the id==null else branch runs
    # (Note.java:66-72). Automatic.
    r.comment("guid64 generated", edge="E62a24da3")
    # Ed4aa2957 libanki.Utils.guid64 -> libanki.Utils.base91
    # (Utils.java:426-427). Automatic.
    r.comment("base91 encoding", edge="Ed4aa2957")
    # E4a0aec25 libanki.Utils.base91 -> libanki.Utils.base62
    # (Utils.java:420-421). Automatic; this is the target edge.
    r.comment("base62 encoding reached", edge="E4a0aec25")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
