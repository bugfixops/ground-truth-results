#!/usr/bin/env python3
"""AnkiDroid route_01 (final draw): Phrase.<init>.

Target: Phrase.<init> (Glosbe JSON Phrase, reflective Gson construction).
Table verdict: CORRECT (combined-merge redraw, row 01, 38 steps;
    the judged route, with the Reviewer drawer dispatch
    Ebf481404/E09ef790a/E5285c072 — see body notes). Drive
    unchanged.
Route followed: final-draw BFS route from helper/judge-final/
    route_01.txt, edge ids verified against
    graphs/AnkiDroid/out/ankidroid_trigger_graph.json and
    methods.csv (route_edge_ids identical). Head changed vs the
    first-draw script: StudyOptionsFragment -> Reviewer -> drawer
    -> CardBrowser (steps 4-16), not the old deck-list drawer head.
    Tail from CardBrowser onward matches the old script.
Preconditions (see ROUTES_rows.csv setup cell):
  - Collection open, deck with cards to study, a note whose first
    field has non-empty text (media button needs it, and the
    translate button needs non-empty source text).
  - Network on: glosbe.com reachable. The env is Glosbe, NOT the
    AnkiWeb sync server named in the methods.csv env prose.
  - Translation language spinners: if their defaults are empty, run
    setup must pre-set translatorLastLanguageFrom/To preferences to
    a valid pair; verify against a live run.
Mapping notes:
  - Selectors verified against the printed tree: "Study"
    (studyoptions_start string), "Card browser" (nav_browser title),
    "Add note" (menu_add_note string), media-button content
    description "Attach multimedia content to the note"
    (card_multimedia_editline.xml + multimedia_editor_attach_mm_content),
    "Translation" (multimedia_editor_text_field_editing_translate),
    "Glosbe.com" (BasicTextFieldController.java:169 source list),
    "Translate" (multimedia_editor_trans_translate).
  - The "Navigate up" and "More options" content descriptions are
    the standard framework/AppCompat descriptions; verify them
    against a live uiautomator dump before a real run.
  - The drawer-open tap and the "Card browser" tap share edge
    Ebf481404 (two log lines, one edge); the same applies to the
    "More options" tap and the "Add note" tap (E0281e707 /
    E37ba8c1f).
  - The final edge Edd1d361a (showPickTranslationDialog ->
    Phrase.<init>) is INFERRED: no printed Gson library source shows
    Gson reflectively invoking Phrase.<init>. The script drives
    every UI step up to the pick-translation dialog; the
    construction itself is a library consequence, logged with
    r.comment.
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
    "E94833ec9", "E44749e19", "Ed63b7964", "E7b61f827", "Eb7034235",
    "Ed31d10af", "Eabfa7572", "E92aeb8ec", "Ebb46b041", "E31bccb82",
    "Eaa5fd795", "E57ec0f8c", "Ece92d132", "E4591472f", "E2c3f2e9e",
    "Eb9c36e0c", "Ec32ee4bb", "Edd1d361a",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_01")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_01", edge_ids=EDGE_IDS,
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
    # E5906a191 DeckPicker.onCreate -> showStartupScreensAndDialogs
    # (colOpen branch, DeckPicker.java:417).
    r.comment("showStartupScreensAndDialogs (collection open)",
              edge="E5906a191")
    # Ef3e13961 showStartupScreensAndDialogs -> onFinishedStartup.
    r.comment("onFinishedStartup", edge="Ef3e13961")
    # Eae89b47b onFinishedStartup -> loadStudyOptionsFragment.
    r.comment("loadStudyOptionsFragment", edge="Eae89b47b")
    # Ea73b74da loadStudyOptionsFragment -> S_STUDYOPTIONS_FRAG
    # (fragment replace/commit, DeckPicker.java:1650-1655).
    r.comment("study options fragment shown", edge="Ea73b74da")
    # E8972c27b S_STUDYOPTIONS_FRAG -> StudyOptionsFragment$1.onClick:
    # tap Study; cards due, so content is not CONGRATS and the click
    # calls openReviewer (StudyOptionsFragment.java:120-136).
    r.tap(edge="E8972c27b", text="Study")
    # E0b3abfeb $1.onClick -> openReviewer.
    r.comment("openReviewer", edge="E0b3abfeb")
    # Eb58e5599 openReviewer -> Reviewer.<init> (Intent).
    r.comment("startActivity Reviewer", edge="Eb58e5599")
    # Eed14720a Reviewer.<init> -> AbstractFlashcardViewer.onCreate
    # @Reviewer.
    r.comment("Reviewer onCreate", edge="Eed14720a")
    # Ed7470ef3 onCreate -> Reviewer.onCollectionLoaded (collection
    # load via AnkiActivity).
    r.dwell(edge="Ed7470ef3", seconds=5)
    # Ea375fff8 onCollectionLoaded -> S_REVIEWER.
    r.comment("Reviewer page shown", edge="Ea375fff8")
    # Ebf481404 S_REVIEWER -> NavigationDrawerActivity
    # .onNavigationItemSelected: open the drawer, then tap the
    # nav_browser item ("Card browser").
    r.tap(edge="Ebf481404", desc="Navigate up")
    r.tap(edge="Ebf481404", text="Card browser")
    # E09ef790a onNavigationItemSelected -> Reviewer.openCardBrowser
    # (nav_browser case, NavigationDrawerActivity.java:262-264).
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
    # E94833ec9 S_NOTEEDITOR -> NoteEditor$11.onClick: tap the media
    # button of a field with non-empty text.
    r.tap(edge="E94833ec9",
          desc="Attach multimedia content to the note")
    # E44749e19 $11.onClick -> startMultimediaFieldEditor
    # (guard: field text non-empty, NoteEditor.java:1135-1141).
    r.comment("startMultimediaFieldEditor (field text non-empty)",
              edge="E44749e19")
    # Ed63b7964 -> MultimediaEditFieldActivity.<init>.
    r.comment("startActivityForResult MultimediaEditFieldActivity",
              edge="Ed63b7964")
    # E7b61f827 -> onCreate (fresh start).
    r.comment("MultimediaEditFieldActivity onCreate", edge="E7b61f827")
    # Eb7034235 onCreate -> S_MULTIMEDIA_EDIT_FIELD.
    r.comment("multimedia edit field page shown", edge="Eb7034235")
    # Ed31d10af S_MULTIMEDIA_EDIT_FIELD -> $3.onClick (Translation).
    r.tap(edge="Ed31d10af", text="Translation")
    # Eabfa7572 $3.onClick -> S_DLG_PICK_STRING (Glosbe.com offered).
    r.comment("PickString dialog shown", edge="Eabfa7572")
    # E92aeb8ec S_DLG_PICK_STRING -> $3$1.onClick: pick Glosbe.com.
    r.tap(edge="E92aeb8ec", text="Glosbe.com")
    # Ebb46b041 $3$1.onClick -> startTranslationWithGlosbe.
    r.comment("Glosbe.com branch starts translation", edge="Ebb46b041")
    # E31bccb82 -> TranslationActivity.<init>.
    r.comment("startActivityForResult TranslationActivity",
              edge="E31bccb82")
    # Eaa5fd795 TranslationActivity.<init> -> onCreate.
    r.comment("TranslationActivity onCreate", edge="Eaa5fd795")
    # E57ec0f8c onCreate -> S_TRANSLATION.
    r.comment("translation page shown", edge="E57ec0f8c")
    # Ece92d132 S_TRANSLATION -> TranslationActivity$1.onClick:
    # tap the Translate button.
    r.tap(edge="Ece92d132", text="Translate")
    # E4591472f $1.onClick -> translate.
    r.comment("translate()", edge="E4591472f")
    # E2c3f2e9e translate -> BackgroundPost.doInBackground
    # (guard: Connection.isOnline(); Glosbe address).
    r.dwell(edge="E2c3f2e9e", seconds=10)
    # Eb9c36e0c doInBackground -> onPostExecute.
    r.comment("BackgroundPost onPostExecute", edge="Eb9c36e0c")
    # Ec32ee4bb onPostExecute -> showPickTranslationDialog.
    r.comment("showPickTranslationDialog", edge="Ec32ee4bb")
    # Edd1d361a showPickTranslationDialog -> Phrase.<init>: Gson
    # parses the Glosbe response into Phrase. INFERRED (no printed
    # Gson source shows the reflective construction); no user action.
    r.comment("Gson parses response into Phrase (INFERRED step, "
              "library construction, no user action)", edge="Edd1d361a")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
