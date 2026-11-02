#!/usr/bin/env python3
"""AnkiDroid final-draw route_21: DiffEngine.diff_cleanupSemanticScore.

Target: DiffEngine.diff_cleanupSemanticScore.
Table verdict: CORRECT (combined-merge redraw, route_table.md
    row 23). Edges unchanged.
Route followed: the final BFS route (24 edges), never the first-draw
    route_20 UPDATE_FACT derivation. Prefix: IntentHandler -> DeckPicker
    -> study-options fragment (fragmented/tablet mode) -> Start button
    -> Reviewer -> onKeyUp -> displayCardAnswer -> typeAnsAnswerFilter
    -> diff chain. Tail from typeAnsAnswerFilter onward reuses the
    first-draw route_20 diff-chain edges (E858abb10 onward); the
    display->typeAns edge here is Ed006b7e1 (Reviewer display path),
    not old route_20's E23f3de26 (UPDATE_FACT path).
Preconditions/fixtures:
  - Tablet/large-screen config (mFragmented true) so the study-options
    fragment loads; collection open; deck with cards to study.
  - A type-answer card: mShowTypeAnswerField true and mTypeCorrect
    non-null, with a correct answer at least 100 chars after trim.
  - The typed answer below is at least 100 chars after trim, differs
    from the fixture correct answer, and (with that correct answer)
    yields non-empty diffs containing a single edit between
    equalities; run setup must set the fixture correct answer so
    this holds (see mapping notes). No file fixture is pushed.
Mapping notes:
  - The "Study" tap text is inherited from first-draw route_05
    (E518f89ef); verify it against a live uiautomator dump.
  - The answer field must be UNFOCUSED when Enter is pressed
    (AbstractFlashcardViewer.java:1016 guard). Typing focuses the
    field, so the live run must defocus it (tap outside the field)
    before the Enter key; no defocus selector could be verified
    statically, so that tap is a comment here, not a claimed tap.
    If the field stays focused, displayCardAnswer does not run.
  - Space/Enter: ENTER is used (judgement allows Space or Enter).
  - Diff steps after displayCardAnswer are automatic; the final
    diff_cleanupSemanticScore step is conditional on the diff
    pattern above, not on any further user action.
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
    "Eed14720a", "Ed7470ef3", "Ea375fff8", "E5e78b2d2", "E6d1d7be6",
    "E32795cf7", "Ed006b7e1", "E858abb10", "E2115c14e", "Eede34ab8",
    "E0e396506", "E74e7f2c0", "E6ad06c68", "E54d98842",
]

# Typed answer: >100 chars after trim. Run setup must make the
# fixture card's correct answer equal this string with exactly one
# single-character edit, so the diff pattern (single edit between
# equalities) holds; otherwise the final score step may not run.
TYPED_ANSWER = (
    "the quick brown fox jumps over the lazy dog and then runs "
    "back across the field again today while the sun shines "
    "brightly over the hills"
)


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_21")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_21", edge_ids=EDGE_IDS,
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
    # Ef3e13961 -> onFinishedStartup (nothing-special branch: enough
    # disc space, no first-run/version screens).
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
    # Ea375fff8 onCollectionLoaded -> S_REVIEWER.
    r.comment("reviewer page shown", edge="Ea375fff8")
    # Type the wrong long answer into the type-answer field. Typing
    # itself has no graph edge; it is logged against the next edge
    # in script order (E5e78b2d2, the key-up edge), as first-draw
    # route_20 logged typing against its next edge.
    r.type_text(TYPED_ANSWER, edge="E5e78b2d2")
    # DEFOCUS GAP (see header): the answer field must be unfocused
    # before Enter; no defocus selector was verifiable statically,
    # so no tap is claimed here. Live run must defocus first.
    r.comment("DEFOCUS GAP: tap outside the answer field to defocus "
              "it (selector unverified; see header) before Enter",
              edge="E5e78b2d2")
    # E5e78b2d2 S_REVIEWER -> Reviewer.onKeyUp: Enter key.
    r.key("ENTER", edge="E5e78b2d2")
    # E6d1d7be6 Reviewer.onKeyUp -> onKeyUp@Reviewer (super call).
    r.comment("super onKeyUp", edge="E6d1d7be6")
    # E32795cf7 onKeyUp@Reviewer -> displayCardAnswer@Reviewer
    # (answer field unfocused, answer not yet displayed).
    r.comment("displayCardAnswer", edge="E32795cf7")
    # Ed006b7e1 displayCardAnswer -> typeAnsAnswerFilter (card
    # non-null; typed answer non-empty and different from correct).
    r.comment("typeAnsAnswerFilter", edge="Ed006b7e1")
    # E858abb10 typeAnsAnswerFilter -> diffedHtmlStrings.
    r.comment("diffedHtmlStrings", edge="E858abb10")
    # E2115c14e diffedHtmlStrings -> diff_main(String,String).
    r.comment("diff_main", edge="E2115c14e")
    # Eede34ab8 diff_main(String,String) ->
    # diff_main(String,String,boolean).
    r.comment("diff_main with checklines", edge="Eede34ab8")
    # E0e396506 -> diff_compute.
    r.comment("diff_compute", edge="E0e396506")
    # E74e7f2c0 diff_compute -> diff_cleanupSemantic (checklines;
    # both trimmed texts >= 100 chars).
    r.comment("diff_cleanupSemantic", edge="E74e7f2c0")
    # E6ad06c68 diff_cleanupSemantic -> diff_cleanupSemanticLossless
    # (non-empty diffs).
    r.comment("diff_cleanupSemanticLossless", edge="E6ad06c68")
    # E54d98842 diff_cleanupSemanticLossless ->
    # diff_cleanupSemanticScore (single edit between equalities).
    r.comment("diff_cleanupSemanticScore (target)", edge="E54d98842")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
