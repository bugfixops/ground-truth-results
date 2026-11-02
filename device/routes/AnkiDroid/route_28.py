#!/usr/bin/env python3
"""AnkiDroid final-draw route_28: AbstractFlashcardViewer.typeAnswer.

Target: AbstractFlashcardViewer.typeAnswer (boolean predicate at
    AbstractFlashcardViewer.java:2326; evaluating it IS a call).
Table verdict: WRONG (final draw, route_table.md row 28; corrected
    route). The printed BFS route's step 9 was an interface fan-out
    fiction: DeckPicker's LOAD_DECK_COUNTS launch registers
    DeckPicker's own listener, never AbstractFlashcardViewer's
    mAnswerCardHandler, so DeckTask.onPreExecute on that prefix
    never reaches AFV$10.onPreExecute. The corrected route below
    uses the Reviewer prefix (final-draw route_21 steps 1-13) and
    the ANSWER_CARD launch that actually registers mAnswerCardHandler
    (Reviewer.java:96-98): onCollectionLoaded -> launchDeckTask ->
    onPreExecute -> mAnswerCardHandler.onPreExecute ($10) ->
    blockControls -> typeAnswer.
Route followed: corrected route, 18 edges, derived from the graph
    JSON by src/dst pairs and verified contiguous (see NOTES.md).
    Note the corrected chain skips the S_REVIEWER page edge
    (Ea375fff8): the ANSWER_CARD launch is inside onCollectionLoaded
    itself (graph edge Ebeafa06d Reviewer.onCollectionLoaded ->
    DeckTask.launchDeckTask), before the reviewer page is entered.
    The tail edges E749e5944, E0bb0a19c, Eed5b25c0, Eadf19602,
    E42fc2547 are the printed route's steps 7-11 with their producer
    corrected; no new tail edge was needed. This script is newly
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
    "Eed14720a", "Ed7470ef3", "Ebeafa06d", "E749e5944", "E0bb0a19c",
    "Eed5b25c0", "Eadf19602", "E42fc2547",
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
    # Ebeafa06d Reviewer.onCollectionLoaded -> DeckTask.launchDeckTask
    # (TASK_TYPE_ANSWER_CARD with mAnswerCardHandler, Reviewer
    # .java:96-98). This is the corrected producer: the listener
    # registered here IS the AFV listener, unlike the printed
    # route's LOAD_DECK_COUNTS launch.
    r.comment("ANSWER_CARD launch with mAnswerCardHandler",
              edge="Ebeafa06d")
    # E749e5944 launchDeckTask -> DeckTask.onPreExecute (AsyncTask
    # execute -> onPreExecute on the UI thread).
    r.comment("task onPreExecute", edge="E749e5944")
    # E0bb0a19c onPreExecute -> TaskListener.onPreExecute
    # (dispatch to this task's listener: mAnswerCardHandler).
    r.comment("listener onPreExecute", edge="E0bb0a19c")
    # Eed5b25c0 TaskListener.onPreExecute ->
    # AbstractFlashcardViewer$10.onPreExecute (mAnswerCardHandler).
    r.comment("mAnswerCardHandler onPreExecute", edge="Eed5b25c0")
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
