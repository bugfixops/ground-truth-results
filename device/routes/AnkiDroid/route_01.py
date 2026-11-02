#!/usr/bin/env python3
"""AnkiDroid route_01: Phrase.<init>.

Target: Phrase.<init> (glosbe json Phrase, implicit default constructor).
Table verdict: WRONG (first-draw verdict; this script drives the
    CORRECTED route C01, never the printed BFS route).
Route followed: CORRECTED route C01 from
    helper/b6fix-r01-06/CORRECTED_ROUTES.md, with the final-graph edge
    ids from route_table.md row 01 (35 edges). The printed BFS route
    launched LOAD_DECK_COUNTS then took the RENDER_BROWSER_QA branch;
    this script follows the LOAD_DECK_COUNTS dispatch, the deck-list
    page, and the drawer CardBrowser launch instead.
Preconditions/fixtures:
  - Collection open, with a deck and a note whose first field has
    non-empty text (the media button needs it, and the translate
    button needs non-empty source text).
  - Network on: glosbe.com reachable. The corrected env is Glosbe,
    NOT the AnkiWeb sync server named in the printed route.
  - Translation language spinners: if their defaults are empty, run
    setup must pre-set translatorLastLanguageFrom/To preferences to a
    valid pair; verify against a live run (see mapping notes).
Mapping notes:
  - The drawer-open tap and the "Card browser" tap share edge
    Ed1dad133 (two log lines, one edge; same convention as the
    harness rotate, which logs two lines for one edge). The same
    applies to the "More options" tap and the "Add note" tap
    (E0281e707 / E37ba8c1f).
  - DeckPicker$22.onPostExecute -> S_DECKPICKER is a page
    abstraction with no dedicated graph edge; it is noted in the
    E10a14596 comment, not given an invented id.
  - The final edge Edd1d361a (showPickTranslationDialog ->
    Phrase.<init>) is INFERRED: no printed Gson library source shows
    Gson reflectively invoking Phrase.<init>. The script drives every
    UI step up to the pick-translation dialog; the construction
    itself is a library consequence, logged with r.comment.
  - The "Navigate up" and "More options" content descriptions are
    the standard framework/AppCompat descriptions; verify them
    against a live uiautomator dump before a real run, as the
    Currency route_01 script does for its one unverified selector.
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
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "E553ad2d8", "E0b111c68",
    "E8b5d2971", "E460971ee", "Ee1634710", "E3e610385", "Eee369b5f",
    "E10a14596", "Ed1dad133", "E0e89f361", "Eb06cba16", "E352d419a",
    "E0281e707", "E37ba8c1f", "E94833ec9", "E44749e19", "Ed63b7964",
    "E7b61f827", "Eb7034235", "Ed31d10af", "Eabfa7572", "E92aeb8ec",
    "Ebb46b041", "E31bccb82", "Eaa5fd795", "E57ec0f8c", "Ece92d132",
    "E4591472f", "E2c3f2e9e", "Eb9c36e0c", "Ec32ee4bb", "Edd1d361a",
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
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init> (else branch).
    r.comment("IntentHandler else branch starts DeckPicker",
              edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # E553ad2d8 DeckPicker.onCreate -> DeckPicker.onResume.
    r.comment("onStart -> onResume", edge="E553ad2d8")
    # E0b111c68 DeckPicker.onResume -> DeckPicker.updateDeckList
    # (guard: not mSyncOnResume and colIsOpen()).
    r.comment("resume takes updateDeckList (not sync)", edge="E0b111c68")
    # E8b5d2971 updateDeckList -> launchDeckTask (LOAD_DECK_COUNTS).
    r.comment("launchDeckTask TASK_TYPE_LOAD_DECK_COUNTS",
              edge="E8b5d2971")
    # E460971ee launchDeckTask -> doInBackground.
    r.comment("DeckTask execute -> doInBackground", edge="E460971ee")
    # Ee1634710 doInBackground -> doInBackgroundLoadDeckCounts
    # (DeckTask.java:234-235; the RENDER_BROWSER_QA case is not taken).
    r.comment("dispatch takes LOAD_DECK_COUNTS case", edge="Ee1634710")
    # E3e610385 doInBackground -> onPostExecute (framework delivery).
    r.dwell(edge="E3e610385", seconds=5)
    # Eee369b5f onPostExecute -> TaskListener.onPostExecute.
    r.comment("listener onPostExecute", edge="Eee369b5f")
    # E10a14596 TaskListener -> DeckPicker$22.onPostExecute; the deck
    # list is built, so the app is on the deck-picker page (page
    # abstraction: no dedicated graph edge for $22 -> S_DECKPICKER).
    r.comment("updateDeckList listener; deck list built, deck-picker "
              "page shown (page abstraction, no dedicated edge)",
              edge="E10a14596")
    # Ed1dad133 S_DECKPICKER -> DeckPicker.openCardBrowser: open the
    # drawer, then tap the nav_browser item ("Card browser").
    r.tap(edge="Ed1dad133", desc="Navigate up")
    r.tap(edge="Ed1dad133", text="Card browser")
    # E0e89f361 openCardBrowser -> CardBrowser.<init> (Intent).
    r.comment("startActivityForResult CardBrowser", edge="E0e89f361")
    # Eb06cba16 CardBrowser.<init> -> CardBrowser.onCreate.
    r.comment("system instantiates CardBrowser, then onCreate",
              edge="Eb06cba16")
    # E352d419a CardBrowser.onCreate -> S_CARDBROWSER.
    r.comment("CardBrowser page shown", edge="E352d419a")
    # E0281e707 S_CARDBROWSER -> CardBrowser.onOptionsItemSelected:
    # open the options menu.
    r.tap(edge="E0281e707", desc="More options")
    # E37ba8c1f onOptionsItemSelected -> S_NOTEEDITOR (Add note item,
    # drawer toggle does not consume the item; guard !editModelMode
    # is satisfied by the next tap's target, see below).
    r.tap(edge="E37ba8c1f", text="Add note")
    # E94833ec9 S_NOTEEDITOR -> NoteEditor$11.onClick: tap the media
    # button of a field with non-empty text.
    r.tap(edge="E94833ec9",
          desc="Attach multimedia content to the note")
    # E44749e19 $11.onClick -> startMultimediaFieldEditor
    # (guard: field text non-empty).
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
