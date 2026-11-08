#!/usr/bin/env python3
"""AnkiDroid route_11: StudyOptionsActivity.closeStudyOptions(int).

Target: StudyOptionsActivity.closeStudyOptions(int).
Drive verdict: combined-merge device drive KEPT (24 edges,
    corrected custom-study drive, NOT the new-sample print).
    The new-sample row 09 print is WRONG (33-step fiction,
    step-23 E10ee7f20 plus the mFragmented guard tension) and is
    NOT this drive. This drive's producer chain is the genuine
    variant chain below (E9dee210a/E886e6770/E78bbf014/E8cc2ed4f).
    The mFragmented guard tension (fragment prefix needs true,
    StudyOptionsActivity tail needs false) is UNRESOLVED — see
    NOTES_NEW.md, OPEN flag.
Route followed: steps 1-12 as before (launch -> fragment ->
    toolbar menu -> Custom study -> Review ahead -> OK ->
    createCustomStudySession), then the producer-variant chain:
    createCustomStudySession -> doInBackground@REBUILD_CRAM@
    CustomStudyDialog -> onPostExecute@REBUILD_CRAM@CustomStudyDialog
    -> TaskListener.onPostExecute@REBUILD_CRAM@CustomStudyDialog ->
    CustomStudyDialog$4.onPostExecute (CALL edge, genuine producer
    created inside createCustomStudySession) ->
    onCreateCustomStudySession -> openStudyOptions ->
    StudyOptionsActivity -> Back -> closeStudyOptions(int).
Preconditions: collection open with a non-dyn deck and cards to
    study, so the study-options fragment shows (not the congrats
    view); phone layout for the StudyOptionsActivity tail.
Mapping notes:
  - The layout precondition is flagged, not verified: the prefix
    loads the fragment in DeckPicker while the tail needs the
    non-fragmented openStudyOptions branch. The judge calls this
    consistent; the live run must confirm the activity actually
    launches from the fragment layout, or the tail fails at
    Eec5d8f89. See NOTES.md.
  - "More options" is the standard AppCompat overflow description;
    verify it against a live uiautomator dump before a real run.
  - The S_DLG_CUSTOM_STUDY page covers two dialog stages (context
    menu, then input dialog); both taps share edge E0ee30d62.
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
    "Eae89b47b", "Ea73b74da", "E3e2454e8", "E3fa695ec", "E638ffef5",
    "E0ee30d62", "E479c4204", "E9dee210a", "E886e6770", "E78bbf014",
    "E8cc2ed4f", "Ec59f2073", "Eeed3792f", "Eec5d8f89", "Ef09158d9",
    "E51a47dcb", "Ef8e134b9", "Eec10eebd", "E45f54dfb",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_11")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_11", edge_ids=EDGE_IDS,
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
    # E3e2454e8 S_STUDYOPTIONS_FRAG -> onMenuItemClick: open the
    # fragment toolbar menu (overflow description is the standard
    # AppCompat description; verify against a live dump).
    r.tap(edge="E3e2454e8", desc="More options")
    # E3fa695ec onMenuItemClick -> showCustomStudyContextMenu:
    # action_custom_study case (StudyOptionsFragment.java:306-309).
    # Guard: custom-study item visible only for a non-dyn deck and
    # when the congrats view is not shown (:350-356, 360-362).
    # String verified in res: custom_study = "Custom study".
    r.tap(edge="E3fa695ec", text="Custom study")
    # E638ffef5 showCustomStudyContextMenu -> S_DLG_CUSTOM_STUDY.
    r.comment("custom-study dialog page shown", edge="E638ffef5")
    # E0ee30d62 S_DLG_CUSTOM_STUDY -> CustomStudyDialog$2.onPositive.
    # The S_DLG_CUSTOM_STUDY page covers both dialog stages: first
    # pick a custom-study option in the context menu (here "Review
    # ahead", res custom_study_review_ahead), which opens the input
    # dialog, then tap its positive button ("OK", res dialog_ok).
    # Both taps are logged under this edge, the page-abstraction
    # convention used for shared-edge taps in the old scripts.
    r.tap(edge="E0ee30d62", text="Review ahead")
    r.tap(edge="E0ee30d62", text="OK")
    # E479c4204 $2.onPositive -> createCustomStudySession.
    r.comment("createCustomStudySession", edge="E479c4204")
    # E9dee210a createCustomStudySession ->
    # DeckTask.doInBackground@REBUILD_CRAM@CustomStudyDialog
    # (genuine producer-variant task node; guard: REBUILD_CRAM,
    # launch site CustomStudyDialog.createCustomStudySession).
    # DeckTask.doInBackground@REBUILD_CRAM (the launchDeckTask call
    # at CustomStudyDialog.java:454-455 is collapsed into this ASYNC
    # edge; no separate launchDeckTask edge is carried).
    r.comment("REBUILD_CRAM task launched", edge="E9dee210a")
    # E886e6770 -> onPostExecute@REBUILD_CRAM@CustomStudyDialog.
    r.dwell(edge="E886e6770", seconds=5)
    # E78bbf014 -> TaskListener.onPostExecute@
    # REBUILD_CRAM@CustomStudyDialog.
    r.comment("listener onPostExecute", edge="E78bbf014")
    # E8cc2ed4f -> CustomStudyDialog$4.onPostExecute (CALL
    # edge — the genuine producer step; the old E46c212fb id is
    # DEAD in the new JSON and the generic-listener REGISTER edge
    # is not used as a traversal step).
    # that calls onCreateCustomStudySession, :467).
    r.comment("CustomStudyDialog$4 onPostExecute", edge="E8cc2ed4f")
    # Ec59f2073 -> DeckPicker.onCreateCustomStudySession.
    r.comment("onCreateCustomStudySession", edge="Ec59f2073")
    # Eeed3792f -> openStudyOptions.
    r.comment("openStudyOptions", edge="Eeed3792f")
    # Eec5d8f89 openStudyOptions -> StudyOptionsActivity.<init>:
    # non-fragmented (phone) branch only (DeckPicker.java:1695-1703).
    r.comment("startActivity StudyOptionsActivity (phone branch)",
              edge="Eec5d8f89")
    # Ef09158d9 -> onCreate.
    r.comment("StudyOptionsActivity onCreate", edge="Ef09158d9")
    # E51a47dcb -> S_STUDYOPTIONS.
    r.comment("study-options page shown", edge="E51a47dcb")
    # Ef8e134b9 S_STUDYOPTIONS -> onBackPressed: press Back with
    # the navigation drawer closed (else branch, :113).
    r.back(edge="Ef8e134b9")
    # Eec10eebd onBackPressed -> closeStudyOptions().
    r.comment("closeStudyOptions()", edge="Eec10eebd")
    # E45f54dfb closeStudyOptions() -> closeStudyOptions(int)
    # (target; RESULT_OK at StudyOptionsActivity.java:96).
    r.comment("closeStudyOptions(int) reached (target)",
              edge="E45f54dfb")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
