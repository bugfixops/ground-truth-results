#!/usr/bin/env python3
"""AnkiDroid route_20: DiffEngine.diff_cleanupSemanticScore.

Method: DiffEngine.diff_cleanupSemanticScore
Target verdict: WRONG (route_table.md route 20)
Route followed: the CORRECTED route, never the printed BFS route.
    TASK_TYPE_UPDATE_FACT + mUpdateCardHandler prefix (AFV.java:1084,
    DeckTask.java:419,422), never RenderBrowserQA -> AFV$9: that task
    launches only from CardBrowser with mRenderQAHandler and a
    percent-int payload, so it cannot reach AFV$9. Tail is the
    printed steps 13-20 (displayCardAnswer onward).
Edge ids in order:
    E48de6d58 E26d20f74 E1ad4ef9b Eb3058057 E84e49f54 E251b66e4
    E8fb9dd46 E3662c8fc E460971ee Ec4842675 E33685aa4 Eb7581a2a
    E8c07d056 Ef3d27690 E23f3de26 E858abb10 E2115c14e Eede34ab8
    E0e396506 E74e7f2c0 E6ad06c68 E54d98842
Sources: route_table.md route 20; helper/b6fix-r19-24/
    CORRECTED_ROUTES.md route 20.
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (graph env on
    Eb3058057; see route_16 for the full manifest list).
Fixtures: collection file exists; deck has cards to study; a card
    with a type-answer field; answer display on (sDisplayAnswer true)
    and current card non-null; the typed answer is non-empty and
    differs from the correct answer, so the complex diff code runs
    (AFV.java:762-769); text1 != text2; checklines true; diffs contain
    a single edit surrounded by equalities.
Launcher: <package>/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh setup precedes this script; see
    route_16. At merge time this file lives under
    device/routes/AnkiDroid/, so the import matches Currency.

Mapping notes:
  - The deck-row selector ("Default") is a fixture value; verify it
    against a live uiautomator dump before a real run.
  - If tapping a deck row lands on a StudyOptions screen instead of
    opening the Reviewer directly, the merger must insert the
    StudyOptionsFragment openReviewer tap (E0b3abfeb ->
    Eb58e5599) in place of E84e49f54; both reach Reviewer.<init>.
  - UNRESOLVED STEP (no edge invented): there is no dedicated graph
    edge from Reviewer/AFV instantiation to AFV.onActivityResult.
    The editor round-trip (open editor, edit the note, return with
    RESULT_OK for EDIT_CURRENT_CARD) is logged with r.comment.
  - Text input uses r.type_text, proven by the shared harness copy
    (device/stage/device/harness/harness.py: type_text(s, edge))
    and by Amaze route scripts using type_text(s, edge) with the
    edge of the step the typing serves. The typed answer below is
    "wrong": non-empty, and different from the correct answer for
    any card whose correct answer is not literally "wrong" (the
    fixture card's correct answer must satisfy that; see Fixtures).
    The typing is logged against the next edge in script order
    (E3662c8fc, the UPDATE_FACT launch), since typing itself has
    no graph edge; it enables the later displayCardAnswer diff.
  - The reviewer-direct displayCardAnswer variant (no DeckTask) is
    equally genuine per the corrected derivation, but this script
    follows the UPDATE_FACT prefix because it preserves the
    task/listener structure.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Eb3058057", "E84e49f54",
    "E251b66e4", "E8fb9dd46", "E3662c8fc", "E460971ee", "Ec4842675",
    "E33685aa4", "Eb7581a2a", "E8c07d056", "Ef3d27690", "E23f3de26",
    "E858abb10", "E2115c14e", "Eede34ab8", "E0e396506", "E74e7f2c0",
    "E6ad06c68", "E54d98842",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_20")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_20", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init>.
    r.comment("launcher else branch starts DeckPicker", edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # Eb3058057 DeckPicker.onCreate -> S_DECKPICKER.
    r.comment("DeckPicker page shown, collection open", edge="Eb3058057")
    # E84e49f54 S_DECKPICKER -> DeckPicker.openReviewer: tap a deck
    # with cards to study.
    r.tap(edge="E84e49f54", text="Default")
    # E251b66e4 DeckPicker.openReviewer -> Reviewer.<init>.
    r.comment("Reviewer started", edge="E251b66e4")
    # E8fb9dd46 Reviewer.<init> -> AbstractFlashcardViewer.<init>.
    r.comment("flashcard viewer created", edge="E8fb9dd46")
    # Type a non-empty answer that differs from the correct answer
    # in the type-answer box, then show the answer. The typing
    # enables the later displayCardAnswer diff; it is logged
    # against the next edge in script order (see header).
    r.type_text("wrong", edge="E3662c8fc")
    # UNRESOLVED STEP (see header): open the note editor, edit the
    # note, and return with RESULT_OK for EDIT_CURRENT_CARD. No
    # graph edge covers Reviewer instantiation -> onActivityResult.
    r.comment("EDITOR ROUND-TRIP (no graph edge): edit the note in "
              "the editor and return with RESULT_OK", edge="E3662c8fc")
    # E3662c8fc AbstractFlashcardViewer.onActivityResult ->
    # DeckTask.launchDeckTask (TASK_TYPE_UPDATE_FACT,
    # mUpdateCardHandler, AFV.java:1082-1085). Automatic on return.
    r.comment("UPDATE_FACT task launched", edge="E3662c8fc")
    # E460971ee DeckTask.launchDeckTask -> DeckTask.doInBackground.
    r.comment("task running", edge="E460971ee")
    # Ec4842675 DeckTask.doInBackground ->
    # DeckTask.doInBackgroundUpdateNote (TASK_TYPE_UPDATE_FACT case).
    r.comment("note update running", edge="Ec4842675")
    # E33685aa4 DeckTask.doInBackgroundUpdateNote ->
    # DeckTask.onProgressUpdate (publishProgress with the new card).
    r.comment("progress published", edge="E33685aa4")
    # Eb7581a2a DeckTask.onProgressUpdate ->
    # DeckTask$TaskListener.onProgressUpdate. Automatic.
    r.comment("listener progress dispatch", edge="Eb7581a2a")
    # E8c07d056 DeckTask$TaskListener.onProgressUpdate ->
    # AbstractFlashcardViewer$9.onProgressUpdate (mUpdateCardHandler).
    r.comment("update-card handler progress", edge="E8c07d056")
    # Ef3d27690 AbstractFlashcardViewer$9.onProgressUpdate ->
    # AbstractFlashcardViewer.displayCardAnswer (sDisplayAnswer true,
    # card non-null, AFV.java:534-547). Automatic.
    r.comment("card answer displayed", edge="Ef3d27690")
    # E23f3de26 displayCardAnswer -> typeAnsAnswerFilter. Automatic.
    r.comment("typed answer filtered", edge="E23f3de26")
    # E858abb10 typeAnsAnswerFilter -> DiffEngine.diffedHtmlStrings
    # (complex diff branch, AFV.java:762-769). Automatic.
    r.comment("diffed html strings computed", edge="E858abb10")
    # E2115c14e diffedHtmlStrings -> diff_main(String,String).
    r.comment("diff main started", edge="E2115c14e")
    # Eede34ab8 diff_main(String,String) ->
    # diff_main(String,String,boolean). Automatic.
    r.comment("diff main with checklines", edge="Eede34ab8")
    # E0e396506 diff_main(String,String,boolean) -> diff_compute
    # (text1 != text2). Automatic.
    r.comment("diff computed", edge="E0e396506")
    # E74e7f2c0 diff_compute -> diff_cleanupSemantic (checklines).
    r.comment("semantic cleanup", edge="E74e7f2c0")
    # E6ad06c68 diff_cleanupSemantic -> diff_cleanupSemanticLossless.
    r.comment("lossless semantic cleanup", edge="E6ad06c68")
    # E54d98842 diff_cleanupSemanticLossless ->
    # diff_cleanupSemanticScore (single edit surrounded by
    # equalities). Automatic; this is the target edge.
    r.comment("semantic score cleanup reached", edge="E54d98842")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
