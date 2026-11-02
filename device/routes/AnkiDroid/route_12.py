#!/usr/bin/env python3
"""AnkiDroid route_12: HttpFetcher.downloadFileToSdCardMethod.

Target: HttpFetcher.downloadFileToSdCardMethod.
Table verdict: WRONG (final-draw verdict; this script drives the
    CORRECTED route, never the printed BFS route). The printed step
    15 named DeckPicker.openCardBrowser for a Reviewer receiver; the
    corrected step 15 is Reviewer.openCardBrowser, per
    helper/judge-final/judge-11-20/JUDGEMENTS.md route 12. All other
    steps are unchanged (37 edges).
Route followed: corrected route, identical to the printed route
    except steps 15-16 relabelled to the Reviewer override.
Preconditions: collection open; deck with cards to study; a note
    whose field has non-empty text; TEXT field controller, so the
    pronounce button exists; network on with the Beolingus page
    (dict.tu-chemnitz.de) reachable. No AnkiWeb account is needed.
Mapping notes:
  - This script reuses the old first-draw route_13 script's tail
    (CardBrowser onward, including its strings-grounded button
    texts) but replaces its rebuilt drawer prefix with the final
    route's Reviewer prefix and the corrected step 15.
  - "Navigate up" and "More options" are the standard
    framework/AppCompat descriptions; verify them against a live
    uiautomator dump before a real run.
Launcher: com.ichi2.anki/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh already does pm clear, permission
    grants, fixture pushes, and per-app setup before this script, so
    the script performs only the route actions starting from launch.
Draft status: final-draw device draft for the merger; dry/static
    checks only. No live run has been performed with this script, and
    nothing in this file claims one.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "E5906a191", "Ef3e13961",
    "Eae89b47b", "Ea73b74da", "E518f89ef", "E0b3abfeb", "Eb58e5599",
    "Eed14720a", "Ed7470ef3", "Ea375fff8", "E0b2882d5", "E1e676c95",
    "E5285c072", "Eb06cba16", "E352d419a", "E0281e707", "E37ba8c1f",
    "E94833ec9", "E44749e19", "Ed63b7964", "E7b61f827", "Eb7034235",
    "E1e29f3f5", "Ea9606e5d", "E1ae02f15", "Ed9c9d15a", "E34e471f3",
    "E70e68337", "Ece5d578d", "Ea4a2a47a", "E22a358c4", "E19aee917",
    "Ea27383e7", "Ef9fac826",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_12")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_12", edge_ids=EDGE_IDS,
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
    # E5906a191 DeckPicker.onCreate -> showStartupScreensAndDialogs.
    r.comment("showStartupScreensAndDialogs", edge="E5906a191")
    # Ef3e13961 -> onFinishedStartup.
    r.comment("onFinishedStartup", edge="Ef3e13961")
    # Eae89b47b -> loadStudyOptionsFragment.
    r.comment("loadStudyOptionsFragment", edge="Eae89b47b")
    # Ea73b74da -> S_STUDYOPTIONS_FRAG.
    r.comment("study-options fragment page shown", edge="Ea73b74da")
    # E518f89ef S_STUDYOPTIONS_FRAG -> StudyOptionsFragment$1.onClick:
    # the start-study button. Guard: deck has cards to study.
    # String verified in res: studyoptions_start = "Study".
    r.tap(edge="E518f89ef", text="Study")
    # E0b3abfeb $1.onClick -> openReviewer.
    r.comment("openReviewer", edge="E0b3abfeb")
    # Eb58e5599 openReviewer -> Reviewer.<init>.
    r.comment("startActivity Reviewer", edge="Eb58e5599")
    # Eed14720a Reviewer.<init> -> onCreate@Reviewer.
    r.comment("Reviewer onCreate", edge="Eed14720a")
    # Ed7470ef3 onCreate@Reviewer -> Reviewer.onCollectionLoaded.
    r.comment("Reviewer collection loaded", edge="Ed7470ef3")
    # Ea375fff8 -> S_REVIEWER.
    r.comment("reviewer page shown", edge="Ea375fff8")
    # E0b2882d5 S_REVIEWER -> onNavigationItemSelected: open the
    # drawer, then tap the nav_browser item. String verified in
    # res: card_browser = "Card browser".
    r.tap(edge="E0b2882d5", desc="Navigate up")
    r.tap(edge="E0b2882d5", text="Card browser")
    # E1e676c95 onNavigationItemSelected -> Reviewer.openCardBrowser
    # (CORRECTED step 15: the receiver is Reviewer, so virtual
    # dispatch runs Reviewer.openCardBrowser, Reviewer.java:508-518,
    # not DeckPicker.openCardBrowser. The @Reviewer variant edge
    # E367a70a5 exists but would break chain contiguity here, since
    # the previous edge ends at the unvariant node; the unvariant
    # edge is therefore carried and the choice recorded in NOTES).
    r.comment("Reviewer.openCardBrowser (corrected receiver)",
              edge="E1e676c95")
    # E5285c072 Reviewer.openCardBrowser -> CardBrowser.<init>.
    r.comment("startActivity CardBrowser", edge="E5285c072")
    # Eb06cba16 CardBrowser.<init> -> onCreate.
    r.comment("CardBrowser onCreate", edge="Eb06cba16")
    # E352d419a -> S_CARDBROWSER.
    r.comment("card browser page shown", edge="E352d419a")
    # E0281e707 S_CARDBROWSER -> onOptionsItemSelected: open the
    # options menu (standard AppCompat overflow description).
    r.tap(edge="E0281e707", desc="More options")
    # E37ba8c1f onOptionsItemSelected -> S_NOTEEDITOR (Add note
    # item; string verified: card_editor_add_card = "Add note").
    r.tap(edge="E37ba8c1f", text="Add note")
    # E94833ec9 S_NOTEEDITOR -> NoteEditor$11.onClick: tap the media
    # button of a field with non-empty text. Guard: !editModelMode.
    # Description from the old route_13 script (strings-grounded).
    r.tap(edge="E94833ec9",
          desc="Attach multimedia content to the note")
    # E44749e19 $11.onClick -> startMultimediaFieldEditor.
    r.comment("startMultimediaFieldEditor (field text non-empty)",
              edge="E44749e19")
    # Ed63b7964 -> MultimediaEditFieldActivity.<init>.
    r.comment("startActivity MultimediaEditFieldActivity",
              edge="Ed63b7964")
    # E7b61f827 -> onCreate.
    r.comment("MultimediaEditFieldActivity onCreate", edge="E7b61f827")
    # Eb7034235 -> S_MULTIMEDIA_EDIT_FIELD.
    r.comment("multimedia edit field page shown", edge="Eb7034235")
    # E1e29f3f5 S_MULTIMEDIA_EDIT_FIELD -> $2.onClick (Pronunciation
    # button; needs TEXT field controller, source text non-empty).
    # Text from the old route_13 script (strings-grounded).
    r.tap(edge="E1e29f3f5", text="Pronunciation")
    # Ea9606e5d $2.onClick -> LoadPronounciationActivity.<init>.
    r.comment("startActivity LoadPronounciationActivity",
              edge="Ea9606e5d")
    # E1ae02f15 -> onCreate.
    r.comment("LoadPronounciationActivity onCreate", edge="E1ae02f15")
    # Ed9c9d15a -> S_LOAD_PRONOUNCIATION.
    r.comment("load pronunciation page shown", edge="Ed9c9d15a")
    # E34e471f3 S_LOAD_PRONOUNCIATION -> $1.onClick: tap Load.
    # Text from the old route_13 script (strings-grounded).
    r.tap(edge="E34e471f3", text="Load")
    # E70e68337 $1.onClick -> onLoadPronunciation.
    r.comment("onLoadPronunciation", edge="E70e68337")
    # Ece5d578d onLoadPronunciation -> BackgroundPost.doInBackground
    # (guard: Connection.isOnline(); env: Beolingus page reachable).
    r.comment("BackgroundPost fetches translation page",
              edge="Ece5d578d")
    # Ea4a2a47a doInBackground -> onPostExecute (first cycle:
    # translation post). Wait for the fetch.
    r.dwell(edge="Ea4a2a47a", seconds=10)
    # E22a358c4 onPostExecute -> processPostFinished (translation
    # post; launches the second BackgroundPost for the
    # pronunciation page, same edges firing again).
    r.comment("translation post finished; second BackgroundPost "
              "cycle fetches pronunciation page", edge="E22a358c4")
    r.dwell(edge="Ea4a2a47a", seconds=10)
    # E19aee917 processPostFinished (pronunciation post) ->
    # DownloadFileTask.doInBackground (guard: !mStopped, mp3 address
    # not "no").
    r.comment("pronunciation post launches download task",
              edge="E19aee917")
    # Ea27383e7 DownloadFileTask.doInBackground ->
    # HttpFetcher.downloadFileToSdCard.
    r.comment("download task calls downloadFileToSdCard",
              edge="Ea27383e7")
    # Ef9fac826 downloadFileToSdCard -> downloadFileToSdCardMethod
    # (target; :125 unconditional GET).
    r.comment("unconditional GET calls target method (target)",
              edge="Ef9fac826")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
