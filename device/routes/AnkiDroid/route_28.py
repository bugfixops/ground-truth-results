#!/usr/bin/env python3
"""AnkiDroid final-draw route_28: AbstractFlashcardViewer.typeAnswer.

Target: AbstractFlashcardViewer.typeAnswer (boolean predicate at
    AbstractFlashcardViewer.java:2326; evaluating it IS a call).
Table verdict: CORRECT as a route (combined merge,
    gate-verified 16-step print; not in the new sample). The new
    tail is the ANSWER_CARD launch with mAnswerCardHandler
    (Eba52c92a) -> $10.onPreExecute via the hand edge E3a9489a8
    (not the receiver-variant auto edge) -> blockControls ->
    typeAnswer. The old 18-edge route's extra LOAD_DECK_COUNTS /
    updateDeckList steps are gone. Taps unchanged (Study -> wait
    for Reviewer collection load); the target runs automatically.
    The old drive's 'tablet/large-screen' wording is a
    precondition note, NOT a tap, left for merger confirmation —
    see NOTES_NEW.md flag.
Route followed: driven route, 16 edges, gate-verified print (ANSWER_CARD launch with mAnswerCardHandler)
    JSON by src/dst pairs and verified contiguous (see NOTES.md).
    The new chain also skips the S_REVIEWER page edge (Ea375fff8):
    the ANSWER_CARD launch sits inside onCollectionLoaded itself
    (Eba52c92a), before the reviewer page is entered. The tail
    is Eba52c92a -> E3a9489a8 (hand edge to $10.onPreExecute) ->
    Eadf19602 (blockControls) -> E42fc2547 (typeAnswer). The
    old tail ids Ebeafa06d/E749e5944/E0bb0a19c/Eed5b25c0 are
    superseded by Eba52c92a/E3a9489a8 (Eadf19602/E42fc2547
    unchanged).
    written; no first-draw script corresponds to this method.
Preconditions/fixtures:
  - Tablet/large-screen config (mFragmented true); collection open;
    deck with cards to study, so the Start button opens Reviewer.
    No file fixture is pushed.
Mapping notes:
  - The "Study" tap text is inherited from first-draw route_05
    (E518f89ef); verify it against a live uiautomator dump.
  - blockControls -> typeAnswer is automatic: blockControls
    evaluates typeAnswer() at AbstractFlashcardViewer.java:2449
    regardless of the predicate's value, so no card interaction is
    needed after Reviewer loads; the script dwells while the
    ANSWER_CARD task's onPreExecute runs.
  - No live run is claimed by this script.
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
    "Eae89b47b", "Ea73b74da", "E518f89ef", "E0b3abfeb", "Eb58e5599",
    "Eed14720a", "Ed7470ef3", "Eba52c92a", "E3a9489a8", "Eadf19602",
    "E42fc2547",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_28")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_28", edge_ids=EDGE_IDS,
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
    # E5906a191 onCreate -> showStartupScreensAndDialogs (colOpen).
    r.comment("startup screens (collection open)", edge="E5906a191")
    # Ef3e13961 -> onFinishedStartup (nothing-special branch).
    r.comment("finished startup", edge="Ef3e13961")
    # Eae89b47b -> loadStudyOptionsFragment (fragmented mode).
    r.comment("fragmented mode loads study options", edge="Eae89b47b")
    # Ea73b74da -> S_STUDYOPTIONS_FRAG.
    r.comment("study options fragment shown", edge="Ea73b74da")
    # E518f89ef S_STUDYOPTIONS_FRAG -> StudyOptionsFragment$1.onClick:
    # Start button; guard deck has cards to study.
    r.tap(edge="E518f89ef", text="Study")
    # E0b3abfeb onClick -> openReviewer.
    r.comment("openReviewer", edge="E0b3abfeb")
    # Eb58e5599 openReviewer -> Reviewer.<init>.
    r.comment("Reviewer started", edge="Eb58e5599")
    # Eed14720a Reviewer.<init> -> onCreate@Reviewer.
    r.comment("Reviewer onCreate, collection loading starts",
              edge="Eed14720a")
    # Ed7470ef3 -> Reviewer.onCollectionLoaded (loader dispatch).
    r.dwell(edge="Ed7470ef3", seconds=5)
    # Eba52c92a Reviewer.onCollectionLoaded -> ANSWER_CARD
    # launch with mAnswerCardHandler (Reviewer.java:110-111).
    # This is the genuine producer: the listener registered here
    # IS the AFV listener.
    r.comment("ANSWER_CARD launch with mAnswerCardHandler",
              edge="Eba52c92a")
    # E3a9489a8 ANSWER_CARD launch -> $10.onPreExecute (hand
    # edge, not the receiver-variant auto edge).
    r.comment("mAnswerCardHandler onPreExecute",
              edge="E3a9489a8")
    # Eadf19602 $10.onPreExecute -> blockControls.
    r.comment("blockControls", edge="Eadf19602")
    # E42fc2547 blockControls -> typeAnswer (target; predicate
    # evaluated at AbstractFlashcardViewer.java:2449).
    r.comment("typeAnswer predicate evaluated (target)",
              edge="E42fc2547")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
