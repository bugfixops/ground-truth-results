#!/usr/bin/env python3
"""AnkiDroid route_12: Sound.notifyConfigurationChanged.

Target: Sound.notifyConfigurationChanged (called from
    VideoPlayer.onConfigurationChanged).
Table verdict: WRONG (first-draw verdict; this script drives the
    REBUILT reviewer-flow route, never the printed route).
Route followed: rebuilt route from
    helper/b6fix-r07-12/CORRECTED_ROUTES.md route 12, with
    final-graph edge ids (29 edges). The printed route launched
    LOAD_DECK_COUNTS then took the RENDER_BROWSER_QA branch and its
    empty DeckPicker progress listener, so it never entered
    AbstractFlashcardViewer. This script grades a card (ANSWER_CARD
    task with mAnswerCardHandler), so the progress update drives
    displayCardQuestion for the next card, whose video sound opens
    VideoPlayer; rotating then fires onConfigurationChanged.
Preconditions/fixtures:
  - Collection open; deck "Default" with due cards (the
    openReviewer guard is "deck has cards to study").
  - The NEXT card's question side contains a video sound file:
    video extension whitelist or video MIME type, plus a non-null
    video thumbnail (Sound.java:283-289), and the calling activity
    non-null, so playVideo runs. The first card only needs to be
    gradeable; the video card must come second.
  - Device rotation allowed (the VideoPlayer manifest entry lists
    keyboardHidden|orientation|locale|screenSize).
Mapping notes:
  - S_REVIEWER -> AbstractFlashcardViewer$5.onClick has no graph
    edge: the Show-answer tap (reveals ease buttons) and the Good
    tap (grades) are both logged under E07fe57ce ($5.onClick ->
    answerCard), which is the grade tap's edge.
  - The reviewer-flow steps from displayCardQuestion onward reuse
    the printed steps 12-23 edges, which are real in isolation and
    are the tail of this rebuilt route.
  - notifyConfigurationChanged is a no-op unless mMediaPlayer is
    non-null (Sound.java:360-364); the video must actually be
    playing when the rotation happens, so the script rotates
    immediately after VideoPlayer opens.
Launcher: com.ichi2.anki/.IntentHandler (AndroidManifest.xml:81-89).
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Eb3058057", "E84e49f54",
    "E251b66e4", "E8fb9dd46", "E63fbdec5", "Ee2fb37d3", "Ea375fff8",
    "E07fe57ce", "E73158174", "E460971ee", "E96744bef", "E9f86ddb2",
    "Eb7581a2a", "E5b45a9a5", "Ebabd7196", "E96087c3c", "E7a69fc28",
    "E182b01ce", "E7729f801", "E92a6fecf", "Ef6c02372", "Edc5290aa",
    "E2277be29", "Ea8e5a419", "Eb66c3488", "Ed0faab27",
]

FIXTURE_DECK = "Default"


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
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init>.
    r.comment("IntentHandler else branch starts DeckPicker",
              edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # Eb3058057 DeckPicker.onCreate -> S_DECKPICKER.
    r.comment("deck-picker page shown", edge="Eb3058057")
    # E84e49f54 S_DECKPICKER -> DeckPicker.openReviewer: tap a due
    # deck (guard: deck has cards to study; non-fragmented layout
    # jumps straight to the Reviewer).
    r.tap(edge="E84e49f54", text=FIXTURE_DECK)
    # E251b66e4 openReviewer -> Reviewer.<init>.
    r.comment("openReviewer starts Reviewer", edge="E251b66e4")
    # E8fb9dd46 Reviewer.<init> -> AbstractFlashcardViewer.<init>.
    r.comment("Reviewer extends AbstractFlashcardViewer",
              edge="E8fb9dd46")
    # E63fbdec5 AFV.<init> -> AFV.onCreate.
    r.comment("AbstractFlashcardViewer onCreate", edge="E63fbdec5")
    # Ee2fb37d3 AFV.onCreate -> Reviewer.onCollectionLoaded.
    r.comment("collection loaded", edge="Ee2fb37d3")
    # Ea375fff8 Reviewer.onCollectionLoaded -> S_REVIEWER.
    r.comment("reviewer page shown", edge="Ea375fff8")
    # E07fe57ce $5.onClick -> answerCard: show the answer, then
    # grade Good. (No graph edge covers S_REVIEWER -> $5.onClick;
    # both taps are logged under the grade tap's edge.)
    r.tap(edge="E07fe57ce", text="Show answer")
    r.tap(edge="E07fe57ce", text="Good")
    # E73158174 answerCard -> launchDeckTask (TASK_TYPE_ANSWER_CARD,
    # mAnswerCardHandler).
    r.comment("answerCard launches ANSWER_CARD task", edge="E73158174")
    # E460971ee launchDeckTask -> doInBackground.
    r.comment("DeckTask execute -> doInBackground", edge="E460971ee")
    # E96744bef doInBackground -> doInBackgroundAnswerCard
    # (ANSWER_CARD dispatch, DeckTask.java:240-241).
    r.comment("dispatch takes ANSWER_CARD case", edge="E96744bef")
    # E9f86ddb2 doInBackgroundAnswerCard -> onProgressUpdate
    # (publishProgress with the next card).
    r.dwell(edge="E9f86ddb2", seconds=5)
    # Eb7581a2a onProgressUpdate -> TaskListener.onProgressUpdate.
    r.comment("progress update to listener", edge="Eb7581a2a")
    # E5b45a9a5 TaskListener -> $10.onProgressUpdate
    # (mAnswerCardHandler).
    r.comment("mAnswerCardHandler onProgressUpdate", edge="E5b45a9a5")
    # Ebabd7196 $10.onProgressUpdate -> displayCardQuestion
    # (guard: next card non-null and question side).
    r.comment("next card question displayed", edge="Ebabd7196")
    # E96087c3c displayCardQuestion -> updateCard.
    r.comment("updateCard", edge="E96087c3c")
    # E7a69fc28 updateCard -> playSounds (guard: not
    # mConfigurationChanged).
    r.comment("updateCard plays sounds", edge="E7a69fc28")
    # E182b01ce playSounds -> Sound.playSounds (question branch:
    # not useTTS, not sDisplayAnswer).
    r.comment("question-side sounds", edge="E182b01ce")
    # E7729f801 Sound.playSounds -> playSound(String,OnCompletion).
    r.comment("playSound question", edge="E7729f801")
    # E92a6fecf playSound -> playSound(String,OnCompletion,VideoView).
    r.comment("playSound with VideoView", edge="E92a6fecf")
    # Ef6c02372 playSound(VideoView) -> playVideo (guards: sound is
    # video, thumbnail non-null, videoView null, activity non-null).
    r.comment("video sound opens VideoPlayer", edge="Ef6c02372")
    # Edc5290aa playVideo -> VideoPlayer.<init> (Intent).
    r.comment("startActivity VideoPlayer", edge="Edc5290aa")
    # E2277be29 VideoPlayer.<init> -> VideoPlayer.onCreate.
    r.comment("VideoPlayer onCreate", edge="E2277be29")
    # Ea8e5a419 VideoPlayer.onCreate -> S_VIDEOPLAYER (its own Sound
    # instance is created here).
    r.comment("video player page shown", edge="Ea8e5a419")
    # Eb66c3488 S_VIDEOPLAYER -> VideoPlayer.onConfigurationChanged:
    # rotate to landscape now, while the video is playing.
    r.rotate(edge="Eb66c3488", orientation="landscape")
    # Ed0faab27 onConfigurationChanged -> notifyConfigurationChanged
    # (target; configures video only if mMediaPlayer != null).
    r.comment("configuration change notifies Sound (target)",
              edge="Ed0faab27")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
