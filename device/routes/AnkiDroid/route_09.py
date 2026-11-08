#!/usr/bin/env python3
"""AnkiDroid route_09 (final draw): Finder.findNotes.

Target: Finder.findNotes (Collection.findNotes ->
    new Finder(this).findNotes(query), Collection.java:1077).
Table verdict: CORRECT (combined-merge redraw, row 10, 34 steps;
    the judged route, with the Reviewer drawer dispatch
    Ebf481404/E09ef790a/E5285c072). Drive unchanged.
Route followed: final-draw BFS route from helper/judge-final/
    route_09.txt, edge ids verified against
    graphs/AnkiDroid/out/ankidroid_trigger_graph.json and
    methods.csv (route_edge_ids identical). Head changed vs the
    first-draw Finder script (old route_18): StudyOptionsFragment
    -> Reviewer -> drawer -> CardBrowser (steps 4-20), not the old
    deck-list drawer head. Tail changed vs the old script too: the
    final-draw route uses the for-result Previewer tail
    (Previewer.<init>@FORRESULT -> onCreate@FORRESULT ->
    onCollectionLoaded@FORRESULT -> S_PREVIEWER_FORRESULT ->
    onActivityResult -> deleteDummyCards -> findNotes), which the
    old script's plain-start Previewer tail did not have.
For-result split respected: Previewer is launched with
    startActivityForResult (CardTemplateEditor.java:503-504) and
    returns to the fragment's onActivityResult, which
    unconditionally calls deleteDummyCards (:557-560).
Preconditions (see ROUTES_rows.csv setup cell):
  - Collection open; deck with cards to study.
  - A note whose template editor is reachable from the CardBrowser
    add-card flow, and a real or dummy card id exists for Preview,
    so Previewer does not finish early (Previewer.java:35-38).
Mapping notes:
  - Selectors verified against the printed tree: "Study"
    (studyoptions_start string), "Card browser" (nav_browser
    title), "Add note" (menu_add_note string), "Preview"
    (card_editor_preview_card string).
  - The Cards button is tapped by resource id, not by text: its
    label is the formatted string "Cards: %1$s"
    (CardEditorCards), so an exact text match on "Cards" would
    fail; the button view id is CardEditorCardsText
    (NoteEditor.java:352, note_editor.xml:118). This corrects the
    old script's text="Cards" selector.
  - The Preview action is an ifRoom icon item (title "Preview");
    the script taps it by content description "Preview", which is
    the standard toolbar-item description; verify it against a live
    uiautomator dump before a real run, as with "Navigate up" and
    "More options".
  - The drawer-open tap and the "Card browser" tap share edge
    Ebf481404 (two log lines, one edge); the same applies to the
    "More options" tap and the "Add note" tap (E0281e707 /
    E37ba8c1f).
  - Leaving the Previewer so its for-result result returns to the
    fragment is a Back navigation, driven by r.back (proven by the
    shared harness copy and by Amaze route scripts using
    back(edge)).
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
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "E5906a191", "Ef3e13961",
    "Eae89b47b", "Ea73b74da", "E8972c27b", "E0b3abfeb", "Eb58e5599",
    "Eed14720a", "Ed7470ef3", "Ea375fff8", "Ebf481404", "E09ef790a",
    "E5285c072", "Eb06cba16", "E352d419a", "E0281e707", "E37ba8c1f",
    "E43fdf761", "E1daab677", "Ee8a3d32e", "E9d2d3b7f", "E731864d1",
    "Ef2bc6ed3", "E3112e0db", "E2b5d9886", "E9f7ec141", "Eb21e33e0",
    "E8d8741a0", "E2a61410a", "E94ef2a85", "E2d26f33d",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_09")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_09", edge_ids=EDGE_IDS,
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
    # E5906a191 DeckPicker.onCreate -> showStartupScreensAndDialogs.
    r.comment("showStartupScreensAndDialogs (collection open)",
              edge="E5906a191")
    # Ef3e13961 showStartupScreensAndDialogs -> onFinishedStartup.
    r.comment("onFinishedStartup", edge="Ef3e13961")
    # Eae89b47b onFinishedStartup -> loadStudyOptionsFragment.
    r.comment("loadStudyOptionsFragment", edge="Eae89b47b")
    # Ea73b74da loadStudyOptionsFragment -> S_STUDYOPTIONS_FRAG.
    r.comment("study options fragment shown", edge="Ea73b74da")
    # E8972c27b S_STUDYOPTIONS_FRAG -> StudyOptionsFragment$1.onClick:
    # tap Study; cards due, so openReviewer runs.
    r.tap(edge="E8972c27b", text="Study")
    # E0b3abfeb $1.onClick -> openReviewer.
    r.comment("openReviewer", edge="E0b3abfeb")
    # Eb58e5599 openReviewer -> Reviewer.<init> (Intent).
    r.comment("startActivity Reviewer", edge="Eb58e5599")
    # Eed14720a Reviewer.<init> -> AbstractFlashcardViewer.onCreate
    # @Reviewer.
    r.comment("Reviewer onCreate", edge="Eed14720a")
    # Ed7470ef3 onCreate -> Reviewer.onCollectionLoaded.
    r.dwell(edge="Ed7470ef3", seconds=5)
    # Ea375fff8 onCollectionLoaded -> S_REVIEWER.
    r.comment("Reviewer page shown", edge="Ea375fff8")
    # Ebf481404 S_REVIEWER -> NavigationDrawerActivity
    # .onNavigationItemSelected: open the drawer, then tap the
    # nav_browser item ("Card browser").
    r.tap(edge="Ebf481404", desc="Navigate up")
    r.tap(edge="Ebf481404", text="Card browser")
    # E09ef790a onNavigationItemSelected -> Reviewer.openCardBrowser
    # (nav_browser case).
    r.comment("drawer nav_browser opens CardBrowser",
              edge="E09ef790a")
    # E5285c072 Reviewer.openCardBrowser -> CardBrowser.<init> (Intent).
    r.comment("startActivityForResult CardBrowser", edge="E5285c072")
    # Eb06cba16 CardBrowser.<init> -> CardBrowser.onCreate.
    r.comment("system instantiates CardBrowser, then onCreate",
              edge="Eb06cba16")
    # E352d419a CardBrowser.onCreate -> S_CARDBROWSER.
    r.comment("CardBrowser page shown", edge="E352d419a")
    # E0281e707 S_CARDBROWSER -> CardBrowser.onOptionsItemSelected:
    # open the options menu.
    r.tap(edge="E0281e707", desc="More options")
    # E37ba8c1f onOptionsItemSelected -> S_NOTEEDITOR (Add note item,
    # CardBrowser.java:630-634).
    r.tap(edge="E37ba8c1f", text="Add note")
    # E43fdf761 S_NOTEEDITOR -> NoteEditor$2.onClick: tap the Cards
    # button by resource id (its text is "Cards: ..." formatted, so
    # an exact text match on "Cards" would fail).
    r.tap(edge="E43fdf761", res_id="CardEditorCardsText")
    # E1daab677 $2.onClick -> showCardTemplateEditor
    # (NoteEditor.java:357).
    r.comment("showCardTemplateEditor", edge="E1daab677")
    # Ee8a3d32e showCardTemplateEditor -> CardTemplateEditor.<init>
    # (NoteEditor.java:1001-1013, startActivityForResult).
    r.comment("template editor started", edge="Ee8a3d32e")
    # E9d2d3b7f CardTemplateEditor.<init> -> onCreate.
    r.comment("template editor onCreate", edge="E9d2d3b7f")
    # E731864d1 onCreate -> S_CARDTEMPLATEEDITOR (collection load +
    # fragment adapter, CardTemplateEditor.java:127, :157, :205).
    r.comment("template editor page shown", edge="E731864d1")
    # Ef2bc6ed3 S_CARDTEMPLATEEDITOR -> CardTemplateFragment
    # .onOptionsItemSelected (action_preview, CardTemplateEditor
    # .java:442-446, :449-521).
    r.tap(edge="Ef2bc6ed3", desc="Preview")
    # E3112e0db fragment onOptionsItemSelected -> Previewer.<init>
    # @FORRESULT (action_preview -> Previewer intent,
    # startActivityForResult(i, REQUEST_PREVIEWER),
    # CardTemplateEditor.java:478-504).
    r.comment("Previewer started for result", edge="E3112e0db")
    # E2b5d9886 Previewer.<init>@FORRESULT -> onCreate@FORRESULT
    # (valid card id required, else finish -- satisfiable).
    r.comment("Previewer onCreate", edge="E2b5d9886")
    # E9f7ec141 onCreate@FORRESULT -> onCollectionLoaded@FORRESULT
    # (Previewer.java:32-39, :46-51).
    r.comment("Previewer collection loaded", edge="E9f7ec141")
    # Eb21e33e0 onCollectionLoaded@FORRESULT -> S_PREVIEWER_FORRESULT
    # (card displayed, Previewer.java:45-51).
    r.comment("Previewer page shown", edge="Eb21e33e0")
    # E8d8741a0 S_PREVIEWER_FORRESULT -> CardTemplateFragment
    # .onActivityResult: press Back to leave the Previewer so its
    # for-result result returns to the fragment
    # (CardTemplateEditor.java:503-504, :557-560).
    r.back(edge="E8d8741a0")
    # E2a61410a fragment onActivityResult -> deleteDummyCards
    # (unconditional in onActivityResult, :559).
    r.comment("deleteDummyCards", edge="E2a61410a")
    # E94ef2a85 deleteDummyCards -> Collection.findNotes
    # (CardTemplateEditor.java:545 getCol().findNotes("tag:" +
    # DUMMY_TAG)).
    r.comment("findNotes called for dummy tag", edge="E94ef2a85")
    # E2d26f33d Collection.findNotes -> Finder.findNotes (target;
    # Collection.java:1077).
    r.comment("Finder.findNotes reached (target)", edge="E2d26f33d")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
