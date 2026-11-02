#!/usr/bin/env python3
"""AnkiDroid route_13: HttpFetcher.downloadFileToSdCardMethod.

Target: HttpFetcher.downloadFileToSdCardMethod (unconditional GET
    at HttpFetcher.java:125).
Table verdict: WRONG (first-draw verdict; this script drives the
    REBUILT route, never the printed BFS route).
Route followed: rebuilt route from
    helper/b6fix-r13-18-rework/CORRECTED_ROUTES.md section 1:
    rebuilt prefix R1-R7 (launcher -> deck-picker page -> drawer
    CardBrowser -> CardBrowser launch) plus surviving printed steps
    12-31 with the EDITS.md corrections (27 edges). The printed
    steps 5-10 (LOAD_DECK_COUNTS into RenderBrowserQA, then
    CardBrowser via class init) are discarded, and step 9
    (E3f1b0491, <clinit> -> <init>) is NOT carried: it is UNCLEAR
    per the Finder convention and unreachable on a route that never
    enters RenderBrowserQA. The BFS best route is unchanged in
    structure (guards do not change BFS cost), so the table must
    not be copied from the redraw.
Preconditions/fixtures:
  - Collection open; note with non-empty text field; TEXT field
    controller, so the pronounce button exists
    (BasicTextFieldController.java:93).
  - Network on: the Beolingus translation page
    (dict.tu-chemnitz.de) reachable. The env is Beolingus, NOT the
    AnkiWeb sync server. No account is needed.
Mapping notes:
  - The drawer openCardBrowser edge Ed1dad133 is the direct GUI
    edge; its expansion (E02986fa7 drawer dispatch + Ea0eba485
    dispatch to openCardBrowser) is the same step expanded, noted
    here rather than double-listed.
  - The second BackgroundPost cycle is compressed in the edge list:
    the printed step 28 invocation is the translation post, whose
    processPostFinished launches a second BackgroundPost for the
    pronunciation page (LoadPronounciationActivity.java:288-306),
    and only the second invocation's processPostFinished reaches
    the pronunciation-post branch that launches DownloadFileTask.
    The script dwells for both cycles; the same three edges fire
    twice.
  - Step 14 guard is !editModelMode (audit Correction C1); step 20
    needs field type TEXT; step 26 guard is Connection.isOnline()
    with Beolingus env; step 29 guard is !mStopped, pronunciation
    post, mp3 address not "no".
  - Button texts are grounded in strings.xml: "Pronunciation"
    (multimedia_editor_text_field_editing_say), "Load"
    (multimedia_editor_pron_load), media-button description
    "Attach multimedia content to the note".
  - The "Navigate up" and "More options" descriptions are the
    standard framework/AppCompat descriptions; verify them against
    a live uiautomator dump before a real run.
Launcher: com.ichi2.anki/.IntentHandler (AndroidManifest.xml:81-89).
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
    "E94833ec9", "E44749e19", "Ed63b7964", "E7b61f827", "Eb7034235",
    "E1e29f3f5", "Ea9606e5d", "E1ae02f15", "Ed9c9d15a", "E34e471f3",
    "E70e68337", "Ece5d578d", "Ea4a2a47a", "E22a358c4", "E19aee917",
    "Ea27383e7", "Ef9fac826",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_13")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_13", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # R1 E48de6d58 S_ENTRY -> IntentHandler.onCreate: launch.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # R2 E26d20f74 IntentHandler.onCreate -> DeckPicker.<init>.
    r.comment("IntentHandler else branch starts DeckPicker",
              edge="E26d20f74")
    # R3 E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # R4 Eb3058057 DeckPicker.onCreate -> S_DECKPICKER (collection
    # file exists, WRITE_EXTERNAL_STORAGE granted).
    r.comment("deck-picker page shown", edge="Eb3058057")
    # R5 Ed1dad133 S_DECKPICKER -> DeckPicker.openCardBrowser: open
    # the drawer, then tap nav_browser ("Card browser").
    r.tap(edge="Ed1dad133", desc="Navigate up")
    r.tap(edge="Ed1dad133", text="Card browser")
    # R6 E0e89f361 openCardBrowser -> CardBrowser.<init> (genuine
    # Intent launch, not a static call).
    r.comment("startActivityForResult CardBrowser", edge="E0e89f361")
    # R7 Eb06cba16 CardBrowser.<init> -> CardBrowser.onCreate.
    r.comment("system instantiates CardBrowser, then onCreate",
              edge="Eb06cba16")
    # Step 12 E352d419a CardBrowser.onCreate -> S_CARDBROWSER.
    r.comment("CardBrowser page shown", edge="E352d419a")
    # Step 13 E0281e707 S_CARDBROWSER -> onOptionsItemSelected:
    # open the options menu.
    r.tap(edge="E0281e707", desc="More options")
    # Step 14 E37ba8c1f onOptionsItemSelected -> S_NOTEEDITOR
    # (Add note item; drawer toggle does not consume it).
    r.tap(edge="E37ba8c1f", text="Add note")
    # Step 15 E94833ec9 S_NOTEEDITOR -> NoteEditor$11.onClick
    # (guard: !editModelMode): tap the media button of a field with
    # non-empty text.
    r.tap(edge="E94833ec9",
          desc="Attach multimedia content to the note")
    # Step 16 E44749e19 $11.onClick -> startMultimediaFieldEditor
    # (guard: field text non-empty).
    r.comment("startMultimediaFieldEditor (field text non-empty)",
              edge="E44749e19")
    # Step 17 Ed63b7964 -> MultimediaEditFieldActivity.<init>.
    r.comment("startActivityForResult MultimediaEditFieldActivity",
              edge="Ed63b7964")
    # Step 18 E7b61f827 -> onCreate (cold start).
    r.comment("MultimediaEditFieldActivity onCreate", edge="E7b61f827")
    # Step 19 Eb7034235 onCreate -> S_MULTIMEDIA_EDIT_FIELD.
    r.comment("multimedia edit field page shown", edge="Eb7034235")
    # Step 20 E1e29f3f5 S_MULTIMEDIA_EDIT_FIELD -> $2.onClick
    # (Pronunciation button; needs TEXT field controller).
    r.tap(edge="E1e29f3f5", text="Pronunciation")
    # Step 21 Ea9606e5d $2.onClick -> LoadPronounciationActivity.<init>
    # (guard: source text non-empty).
    r.comment("startActivity LoadPronounciationActivity",
              edge="Ea9606e5d")
    # Step 22 E1ae02f15 -> onCreate (cold start).
    r.comment("LoadPronounciationActivity onCreate", edge="E1ae02f15")
    # Step 23 Ed9c9d15a onCreate -> S_LOAD_PRONOUNCIATION.
    r.comment("load pronunciation page shown", edge="Ed9c9d15a")
    # Step 24 E34e471f3 S_LOAD_PRONOUNCIATION -> $1.onClick:
    # tap Load.
    r.tap(edge="E34e471f3", text="Load")
    # Step 25 E70e68337 $1.onClick -> onLoadPronunciation.
    r.comment("onLoadPronunciation", edge="E70e68337")
    # Step 26 Ece5d578d onLoadPronunciation ->
    # BackgroundPost.doInBackground (guard: Connection.isOnline();
    # env: Beolingus page reachable).
    r.comment("BackgroundPost fetches translation page",
              edge="Ece5d578d")
    # Step 27 Ea4a2a47a doInBackground -> onPostExecute (first
    # cycle: translation post). Wait for the fetch.
    r.dwell(edge="Ea4a2a47a", seconds=10)
    # Step 28 E22a358c4 onPostExecute -> processPostFinished
    # (translation post; launches the second BackgroundPost for the
    # pronunciation page, same edges firing again).
    r.comment("translation post finished; second BackgroundPost "
              "cycle fetches pronunciation page", edge="E22a358c4")
    r.dwell(edge="Ea4a2a47a", seconds=10)
    # Step 29 E19aee917 processPostFinished (pronunciation post) ->
    # DownloadFileTask.doInBackground (guard: !mStopped,
    # pronunciation post, mp3 address not "no").
    r.comment("pronunciation post launches download task",
              edge="E19aee917")
    # Step 30 Ea27383e7 DownloadFileTask.doInBackground ->
    # HttpFetcher.downloadFileToSdCard.
    r.comment("download task calls downloadFileToSdCard",
              edge="Ea27383e7")
    # Step 31 Ef9fac826 downloadFileToSdCard ->
    # downloadFileToSdCardMethod (target; :125 unconditional GET).
    r.comment("unconditional GET calls target method (target)",
              edge="Ef9fac826")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
