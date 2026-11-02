#!/usr/bin/env python3
"""AnkiDroid route_13: Sound.notifyConfigurationChanged.

Target: Sound.notifyConfigurationChanged.
Table verdict: CORRECT (final-draw verdict; this script drives the
    printed BFS route, 24 edges, unchanged).
Route followed: printed route: fragment -> Study -> Reviewer ->
    options menu -> action_replay -> playSounds -> Sound chain ->
    VideoPlayer -> rotate -> notifyConfigurationChanged.
Preconditions: collection open; deck with cards to study; TTS off
    (non-TTS replay branch); the current card's question side
    contains a video sound (video extension/MIME) with a non-null
    video thumbnail; device rotation allowed.
Mapping notes:
  - This route is NOT the old first-draw route_12 script: that
    script drove a rebuilt grade-the-card flow to reach the video
    card second. The final BFS route replays audio directly from
    the reviewer menu, so no grading is needed and no second card
    is required; the old script's video/thumbnail guards are kept.
  - "More options" is the standard AppCompat overflow description;
    verify it against a live uiautomator dump before a real run.
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
    "Eed14720a", "Ed7470ef3", "Ea375fff8", "E875f2b99", "E53189d7a",
    "E182b01ce", "E7729f801", "E92a6fecf", "Ef6c02372", "Edc5290aa",
    "E2277be29", "Ea8e5a419", "Eb66c3488", "Ed0faab27",
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
    # the start-study button (guard: deck has cards to study).
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
    # E875f2b99 S_REVIEWER -> Reviewer.onOptionsItemSelected: open
    # the options menu (standard AppCompat overflow description).
    r.tap(edge="E875f2b99", desc="More options")
    # E53189d7a onOptionsItemSelected -> playSounds: action_replay
    # case (Reviewer.java:150-153). String verified in res:
    # replay_audio = "Replay audio".
    r.tap(edge="E53189d7a", text="Replay audio")
    # E182b01ce playSounds -> Sound.playSounds (guard: !useTTS,
    # non-TTS replay branch).
    r.comment("question-side sounds, non-TTS branch", edge="E182b01ce")
    # E7729f801 Sound.playSounds -> playSound(String,Listener).
    r.comment("playSound question", edge="E7729f801")
    # E92a6fecf -> playSound(String,Listener,VideoView).
    r.comment("playSound with VideoView", edge="E92a6fecf")
    # Ef6c02372 playSound -> playVideo (guards: sound is video,
    # thumbnail non-null, videoView null, activity non-null).
    r.comment("video sound opens VideoPlayer", edge="Ef6c02372")
    # Edc5290aa playVideo -> VideoPlayer.<init> (Intent).
    r.comment("startActivity VideoPlayer", edge="Edc5290aa")
    # E2277be29 VideoPlayer.<init> -> onCreate.
    r.comment("VideoPlayer onCreate", edge="E2277be29")
    # Ea8e5a419 -> S_VIDEOPLAYER.
    r.comment("video player page shown", edge="Ea8e5a419")
    # Eb66c3488 S_VIDEOPLAYER -> onConfigurationChanged: rotate to
    # landscape now, while the video is playing. VideoPlayer
    # declares configChanges keyboardHidden|orientation|locale|
    # screenSize (AndroidManifest.xml:184), so rotation dispatches
    # here instead of recreating.
    r.rotate(edge="Eb66c3488", orientation="landscape")
    # Ed0faab27 onConfigurationChanged -> notifyConfigurationChanged
    # (target; configures video only if mMediaPlayer != null, so
    # the rotation must happen while the video plays).
    r.comment("configuration change notifies Sound (target)",
              edge="Ed0faab27")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
