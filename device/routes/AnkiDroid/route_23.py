#!/usr/bin/env python3
"""AnkiDroid route_23: CardTemplateEditor$3.onPositive.

Method: CardTemplateEditor$3.onPositive
Target verdict: WRONG (route_table.md route 23)
Route followed: the CORRECTED route, never the printed BFS route.
    Corrected prefix via DeckPicker.openCardBrowser (:1708-1713);
    tail is the printed steps 12-23 with audited fixes. The printed
    head is wrong twice: LOAD_DECK_COUNTS cannot dispatch to
    RenderBrowserQA, and the static CardBrowser.updateSearchItemQA
    call is not a CardBrowser activity launch.
Edge ids in order:
    E48de6d58 E26d20f74 E1ad4ef9b Eb3058057 Ed1dad133 E0e89f361
    Eb06cba16 E352d419a E0281e707 E37ba8c1f E43fdf761 E1daab677
    Ee8a3d32e E9d2d3b7f E731864d1 E6269dbb1 E4e3c472c E90d84107
    E59ff013f
Sources: route_table.md route 23; helper/b6fix-r19-24/
    CORRECTED_ROUTES.md route 23.
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (graph env on
    Eb3058057; see route_16 for the full manifest list).
Fixtures: collection file exists; at least one note and one valid
    model id, so showCardTemplateEditor starts the editor (the
    JSONException at NoteEditor.java:1004-1008 is rethrown before
    the start, so a valid model id is required); template text is
    edited, so modelHasChanged is true.
Launcher: <package>/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh setup precedes this script; see
    route_16. At merge time this file lives under
    device/routes/AnkiDroid/, so the import matches Currency.

Mapping notes:
  - Drawer and menu selectors ("Card browser", "Add", "Cards") are
    UI strings not fixed by the graph edges; verify them against a
    live uiautomator dump before a real run.
  - Text input uses r.type_text, proven by the shared harness copy
    (device/stage/device/harness/harness.py: type_text(s, edge)).
    The template text is edited by appending " edited" to the
    focused template field, so modelHasChanged is true before Home
    is pressed. This assumes the template field is focused on entry;
    verify the focus target on a live dump, and tap the field first
    if it is not focused. The typing is logged against the next
    edge in script order (E6269dbb1, the Home press it enables).
  - No RenderBrowserQA step belongs in this head: that task runs
    only once CardBrowser is already open, the reverse of the
    printed route's order.
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
    "E43fdf761", "E1daab677", "Ee8a3d32e", "E9d2d3b7f", "E731864d1",
    "E6269dbb1", "E4e3c472c", "E90d84107", "E59ff013f",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_23")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_23", edge_ids=EDGE_IDS,
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
    # Ed1dad133 S_DECKPICKER -> DeckPicker.openCardBrowser:
    # DeckPicker.java:1708-1713, the corrected prefix.
    r.tap(edge="Ed1dad133", text="Card browser")
    # E0e89f361 DeckPicker.openCardBrowser -> CardBrowser.<init>.
    r.comment("CardBrowser started", edge="E0e89f361")
    # Eb06cba16 CardBrowser.<init> -> CardBrowser.onCreate.
    r.comment("system instantiates CardBrowser, then onCreate",
              edge="Eb06cba16")
    # E352d419a CardBrowser.onCreate -> S_CARDBROWSER.
    r.comment("card browser page shown", edge="E352d419a")
    # E0281e707 S_CARDBROWSER -> CardBrowser.onOptionsItemSelected.
    r.tap(edge="E0281e707", text="Add")
    # E37ba8c1f CardBrowser.onOptionsItemSelected -> S_NOTEEDITOR:
    # guard action_add_card_from_card_browser, drawer toggle does
    # not consume the item. Automatic after the tap.
    r.comment("note editor page shown (add-card flow)",
              edge="E37ba8c1f")
    # E43fdf761 S_NOTEEDITOR -> NoteEditor$2.onClick: tap the Cards
    # button (NoteEditor.java:352-353, 357).
    r.tap(edge="E43fdf761", text="Cards")
    # E1daab677 NoteEditor$2.onClick ->
    # NoteEditor.showCardTemplateEditor. Automatic.
    r.comment("template editor requested", edge="E1daab677")
    # Ee8a3d32e NoteEditor.showCardTemplateEditor ->
    # CardTemplateEditor.<init> (valid model id required). Automatic.
    r.comment("template editor started", edge="Ee8a3d32e")
    # E9d2d3b7f CardTemplateEditor.<init> ->
    # CardTemplateEditor.onCreate.
    r.comment("system instantiates template editor, then onCreate",
              edge="E9d2d3b7f")
    # E731864d1 CardTemplateEditor.onCreate -> S_CARDTEMPLATEEDITOR.
    r.comment("template editor page shown", edge="E731864d1")
    # Edit the template text so modelHasChanged is true (see
    # header for the focus assumption).
    r.type_text(" edited", edge="E6269dbb1")
    # E6269dbb1 S_CARDTEMPLATEEDITOR ->
    # CardTemplateEditor.onOptionsItemSelected: press Home with
    # modelHasChanged true (CardTemplateEditor.java:171-175).
    r.tap(edge="E6269dbb1", desc="Navigate up")
    # E4e3c472c CardTemplateEditor.onOptionsItemSelected ->
    # CardTemplateEditor.showDiscardChangesDialog. Automatic.
    r.comment("discard-changes dialog shown", edge="E4e3c472c")
    # E90d84107 CardTemplateEditor.showDiscardChangesDialog ->
    # CardTemplateEditor$3.<init> (callback built at :260).
    # Automatic.
    r.comment("discard dialog callback created", edge="E90d84107")
    # E59ff013f CardTemplateEditor$3.<init> ->
    # CardTemplateEditor$3.onPositive: tap the dialog positive
    # button (dialog shown at :270). Automatic; target edge.
    r.tap(edge="E59ff013f", text="Discard")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
