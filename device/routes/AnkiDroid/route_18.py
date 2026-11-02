#!/usr/bin/env python3
"""AnkiDroid route_18: Finder.findNotes.

Method: Finder.findNotes
Target verdict: WRONG (route_table.md route 18)
Route followed: the CORRECTED route, never the printed BFS route.
    Rebuilt prefix R1-R7 (launcher -> DeckPicker page -> drawer
    openCardBrowser -> CardBrowser) + the merger-redraw bridge into
    the template editor (CardBrowser add-card steps, identical to
    route 23 steps 13-19) + audited tail T1-T9 from
    S_CARDTEMPLATEEDITOR. The printed CardBrowser-Previewer-result
    continuation is NOT scripted: that Previewer was launched with
    plain startActivity, so its result cannot return to the fragment.
Edge ids in order:
    E48de6d58 E26d20f74 E1ad4ef9b Eb3058057 Ed1dad133 E0e89f361
    Eb06cba16 E352d419a E0281e707 E37ba8c1f E43fdf761 E1daab677
    Ee8a3d32e E9d2d3b7f E731864d1 Ef2bc6ed3 E35d06ed2 E37519322
    Ecb6f2b21 E8a25b1c0 Eb9d6a916 E2a61410a E94ef2a85 E2d26f33d
Sources: route_table.md route 18; helper/b6fix-r13-18-rework/
    CORRECTED_ROUTES.md section 3 (R1-R7, T1-T9).
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (graph env on
    Eb3058057; see route_16 for the full manifest list).
Fixtures: collection file exists; at least one deck and one note; a
    valid model id, so showCardTemplateEditor starts the editor; a
    real or dummy card id exists, so the Previewer does not finish
    early (Previewer.java:35-38).
Launcher: <package>/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh setup precedes this script; see
    route_16. At merge time this file lives under
    device/routes/AnkiDroid/, so the import matches Currency.

Mapping notes:
  - Drawer and menu selectors ("Card browser", "Add", "Cards",
    "Preview") are UI strings not fixed by the graph edges; verify
    each against a live uiautomator dump before a real run.
  - R5 Ed1dad133 is the direct drawer edge; its expanded form is
    E02986fa7 (drawer item selected) + Ea0eba485 (navigation handler
    calls openCardBrowser), the same step expanded, not an extra tap.
  - Leaving the Previewer so its for-result result returns to the
    fragment is a Back navigation, driven by r.back, proven by the
    shared harness copy (device/stage/device/harness/harness.py:
    back(edge)) and by Amaze route scripts using back(edge).
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
    "Ef2bc6ed3", "E35d06ed2", "E37519322", "Ecb6f2b21", "E8a25b1c0",
    "Eb9d6a916", "E2a61410a", "E94ef2a85", "E2d26f33d",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_18")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_18", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate (R1).
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init> (R2).
    r.comment("launcher else branch starts DeckPicker", edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate (R3).
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # Eb3058057 DeckPicker.onCreate -> S_DECKPICKER (R4).
    r.comment("DeckPicker page shown, collection open", edge="Eb3058057")
    # Ed1dad133 S_DECKPICKER -> DeckPicker.openCardBrowser (R5):
    # drawer item nav_browser, not already checked.
    r.tap(edge="Ed1dad133", text="Card browser")
    # E0e89f361 DeckPicker.openCardBrowser -> CardBrowser.<init> (R6).
    r.comment("CardBrowser started for result", edge="E0e89f361")
    # Eb06cba16 CardBrowser.<init> -> CardBrowser.onCreate (R7).
    r.comment("system instantiates CardBrowser, then onCreate",
              edge="Eb06cba16")
    # E352d419a CardBrowser.onCreate -> S_CARDBROWSER.
    r.comment("card browser page shown", edge="E352d419a")
    # E0281e707 S_CARDBROWSER -> CardBrowser.onOptionsItemSelected:
    # open the options menu (bridge into the template editor).
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
    # CardTemplateEditor.<init>. Automatic.
    r.comment("template editor started", edge="Ee8a3d32e")
    # E9d2d3b7f CardTemplateEditor.<init> ->
    # CardTemplateEditor.onCreate.
    r.comment("system instantiates template editor, then onCreate",
              edge="E9d2d3b7f")
    # E731864d1 CardTemplateEditor.onCreate -> S_CARDTEMPLATEEDITOR.
    r.comment("template editor page shown", edge="E731864d1")
    # Ef2bc6ed3 S_CARDTEMPLATEEDITOR ->
    # CardTemplateEditor$CardTemplateFragment.onOptionsItemSelected
    # (T1): tap Preview (action_preview, card id exists).
    r.tap(edge="Ef2bc6ed3", text="Preview")
    # E35d06ed2 fragment onOptionsItemSelected -> Previewer.<init>
    # (T2): started for result (REQUEST_PREVIEWER). Automatic.
    r.comment("Previewer started for result", edge="E35d06ed2")
    # E37519322 Previewer.<init> -> Previewer.onCreate (T3).
    r.comment("system instantiates Previewer, then onCreate",
              edge="E37519322")
    # Ecb6f2b21 Previewer.onCreate -> Previewer.onCollectionLoaded
    # (T4): card id is not -1, so no early finish. Automatic.
    r.comment("Previewer collection loaded", edge="Ecb6f2b21")
    # E8a25b1c0 Previewer.onCollectionLoaded -> S_PREVIEWER (T5).
    r.comment("previewer page shown", edge="E8a25b1c0")
    # Eb9d6a916 S_PREVIEWER ->
    # CardTemplateEditor$CardTemplateFragment.onActivityResult (T6):
    # valid here ONLY because this Previewer was launched for result
    # by this fragment. Press Back to leave the Previewer.
    r.back(edge="Eb9d6a916")
    # E2a61410a fragment onActivityResult ->
    # fragment.deleteDummyCards (T7). Automatic.
    r.comment("dummy cards deleted", edge="E2a61410a")
    # E94ef2a85 fragment.deleteDummyCards -> Collection.findNotes
    # (T8). Automatic.
    r.comment("findNotes called for dummy tag", edge="E94ef2a85")
    # E2d26f33d Collection.findNotes -> Finder.findNotes (T9).
    # Automatic; this is the target edge.
    r.comment("Finder.findNotes reached", edge="E2d26f33d")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
