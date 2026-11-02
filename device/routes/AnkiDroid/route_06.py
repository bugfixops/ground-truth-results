#!/usr/bin/env python3
"""AnkiDroid route_06 (final draw): Sched.revDue.

Target: Sched.revDue (called as the `if (revDue())` test itself,
    Sched.java:1906, inside _nextDueMsg).
Table verdict: CORRECT (final draw, 16 steps; the BFS route IS the
    judged route, so this script drives the BFS route).
Route followed: final-draw BFS route from helper/judge-final/
    route_06.txt, edge ids verified against
    graphs/AnkiDroid/out/ankidroid_trigger_graph.json and
    methods.csv (route_edge_ids identical). No first-draw script
    exists for this method; this script is written fresh in the old
    scripts' style.
Route shape: launch-only. DeckPicker's startup loads the study
    options fragment (loadStudyOptionsFragment commits a replace
    transaction, DeckPicker.java:1651-1654); the framework then
    calls onAttach then onCreateView, whose end calls
    refreshInterface(true), which launches the
    UPDATE_VALUES_FROM_DECK task; its listener's onPostExecute takes
    the CONGRATS branch (finished deck) to finishedMsg, which
    appends _nextDueMsg unconditionally, and _nextDueMsg evaluates
    revDue() as its if test.
Preconditions (see ROUTES_rows.csv setup cell):
  - Collection open.
  - Finished deck: zero new, learning, and due cards, so the study
    options fragment takes the CONGRATS branch to finishedMsg
    (StudyOptionsFragment.java:570-579). This is a collection-state
    precondition the live run must arrange and confirm; it is not
    statically verifiable here and no fixture is claimed for it.
Mapping notes:
  - Steps E1672b7a2 (onAttach) and Ee3b9f7fe (onCreateView) are
    support-v4 fragment lifecycle steps, not androidx as the route
    evidence says (StudyOptionsFragment.java:22 imports
    android.support.v4.app.Fragment); substance is genuine and the
    steps are logged as INFERRED.
  - No UI tap exists on this route after launch: every step after
    the fragment transaction is an automatic lifecycle/task
    consequence, logged with r.comment (and one dwell for the
    background task).
  - The target edge Eb7092458 (_nextDueMsg -> revDue) is evaluated
    as the `if (revDue())` test itself, so revDue() is always called
    by _nextDueMsg once the CONGRATS branch is taken.
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
    "Eae89b47b", "E0cd51520", "E55ad6924", "E1672b7a2", "Ee3b9f7fe",
    "Eb2e9f322", "E2d232c7e", "E2a577bf0", "E5f452336", "Efe9bd917",
    "Eb7092458",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_06")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_06", edge_ids=EDGE_IDS,
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
    # E5906a191 DeckPicker.onCreate -> showStartupScreensAndDialogs.
    r.comment("showStartupScreensAndDialogs (collection open)",
              edge="E5906a191")
    # Ef3e13961 showStartupScreensAndDialogs -> onFinishedStartup.
    r.comment("onFinishedStartup", edge="Ef3e13961")
    # Eae89b47b onFinishedStartup -> loadStudyOptionsFragment.
    r.comment("loadStudyOptionsFragment", edge="Eae89b47b")
    # E0cd51520 loadStudyOptionsFragment ->
    # StudyOptionsFragment.newInstance (DeckPicker.java:1651).
    r.comment("StudyOptionsFragment.newInstance", edge="E0cd51520")
    # E55ad6924 newInstance -> StudyOptionsFragment.<init>
    # (StudyOptionsFragment.java:164).
    r.comment("StudyOptionsFragment instance created", edge="E55ad6924")
    # E1672b7a2 <init> -> onAttach (INFERRED support-v4 fragment
    # lifecycle; onAttach at StudyOptionsFragment.java:107).
    r.comment("fragment onAttach (INFERRED support-v4 lifecycle)",
              edge="E1672b7a2")
    # Ee3b9f7fe onAttach -> onCreateView (INFERRED support-v4
    # fragment lifecycle; onCreateView at StudyOptionsFragment
    # .java:173).
    r.comment("fragment onCreateView (INFERRED support-v4 lifecycle)",
              edge="Ee3b9f7fe")
    # Eb2e9f322 onCreateView -> refreshInterface(boolean)
    # (StudyOptionsFragment.java:190, end of onCreateView).
    r.comment("refreshInterface(true)", edge="Eb2e9f322")
    # E2d232c7e refreshInterface(boolean) ->
    # refreshInterface(boolean,boolean) (StudyOptionsFragment
    # .java:478).
    r.comment("refreshInterface(resetSched, false)", edge="E2d232c7e")
    # E2a577bf0 refreshInterface(boolean,boolean) ->
    # StudyOptionsFragment$3.onPostExecute (TASK_TYPE_
    # UPDATE_VALUES_FROM_DECK launch, StudyOptionsFragment
    # .java:489-494; listener onPostExecute at :511).
    r.dwell(edge="E2a577bf0", seconds=5)
    # E5f452336 $3.onPostExecute -> Sched.finishedMsg (CONGRATS
    # branch, StudyOptionsFragment.java:579; requires 0 due cards).
    r.comment("CONGRATS branch -> finishedMsg (finished deck)",
              edge="E5f452336")
    # Efe9bd917 finishedMsg -> _nextDueMsg (Sched.java:1897,
    # appended unconditionally).
    r.comment("finishedMsg appends _nextDueMsg", edge="Efe9bd917")
    # Eb7092458 _nextDueMsg -> revDue (target; Sched.java:1906
    # `if (revDue())` evaluates revDue() as the test itself).
    r.comment("revDue() evaluated as the if test (target)",
              edge="Eb7092458")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
