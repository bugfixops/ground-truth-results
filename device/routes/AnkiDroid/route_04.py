#!/usr/bin/env python3
"""AnkiDroid route_04 (final draw): Sched._cntFnNew.

Target: Sched._cntFnNew (reflectively invoked via _walkingCount,
    Sched.java:337-353).
Table verdict: CORRECT (final draw, 15 steps; the BFS route IS the
    judged route, so this script drives the BFS route).
Route followed: final-draw BFS route from helper/judge-final/
    route_04.txt, edge ids verified against
    graphs/AnkiDroid/out/ankidroid_trigger_graph.json and
    methods.csv (route_edge_ids identical). No first-draw script
    exists for this method; this script is written fresh in the old
    scripts' style.
Route shape: launch-only. On resume DeckPicker takes the colIsOpen
    branch (not mSyncOnResume) to updateDeckList, which launches the
    LOAD_DECK_COUNTS DeckTask; deckDueTree -> deckDueList calls
    _checkDay, and with day rollover pending (Utils.now() >
    mDayCutoff, Sched.java:1882) reset() runs _resetNew ->
    _resetNewCount -> _walkingCount, which reflectively invokes the
    _cntFnNew method passed at Sched.java:564-565.
Preconditions (see ROUTES_rows.csv setup cell):
  - Collection open; not sync-on-resume.
  - Day rollover pending: the run collection's day cutoff must
    already have passed when the deck list loads, otherwise
    _checkDay does not call reset and the target is not reached.
    This is a collection-state precondition the live run must
    arrange and confirm; it is not statically verifiable here and
    no fixture is claimed for it (see NOTES.md).
Mapping notes:
  - No UI tap exists on this route after launch: every step after
    onResume is an automatic task/lifecycle consequence, logged with
    r.comment (and one dwell for the background task).
  - The final edge Ee3f8c63a (_walkingCount -> _cntFnNew) is a
    reflective invoke, not a UI action; the script drives the launch
    and waits for the deck-list load, and the invoke is the task's
    consequence.
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
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "E553ad2d8", "E0b111c68",
    "E9ce827b1", "E0b825f58", "E8425c0fa", "E9b11a75d", "E41f469b6",
    "E7da70881", "Ea3a16a29", "Ea457b3e5", "E91386df9", "Ee3f8c63a",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_04")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_04", edge_ids=EDGE_IDS,
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
    # E553ad2d8 DeckPicker.onCreate -> DeckPicker.onResume.
    r.comment("onStart -> onResume", edge="E553ad2d8")
    # E0b111c68 DeckPicker.onResume -> DeckPicker.updateDeckList
    # (guard: not mSyncOnResume and colIsOpen()).
    r.comment("resume takes updateDeckList (not sync)", edge="E0b111c68")
    # E9ce827b1 updateDeckList -> DeckTask.doInBackground
    # @LOAD_DECK_COUNTS (DeckPicker.java:1823; FW AsyncTask).
    r.comment("launchDeckTask TASK_TYPE_LOAD_DECK_COUNTS",
              edge="E9ce827b1")
    # E0b825f58 doInBackground@LOAD_DECK_COUNTS ->
    # doInBackgroundLoadDeckCounts (DeckTask.java:234-235).
    r.comment("dispatch takes LOAD_DECK_COUNTS case", edge="E0b825f58")
    # E8425c0fa doInBackgroundLoadDeckCounts -> Sched.deckDueTree
    # (DeckTask.java:485 col.getSched().deckDueTree()).
    r.comment("deckDueTree", edge="E8425c0fa")
    # E9b11a75d deckDueTree -> deckDueList (Sched.java:433).
    r.comment("deckDueList", edge="E9b11a75d")
    # E41f469b6 deckDueList -> _checkDay (Sched.java:380).
    r.comment("_checkDay", edge="E41f469b6")
    # E7da70881 _checkDay -> reset (guard: Utils.now() > mDayCutoff,
    # Sched.java:1882; day-rollover precondition, see header).
    r.dwell(edge="E7da70881", seconds=5)
    # Ea3a16a29 reset -> _resetNew (Sched.java:138).
    r.comment("reset -> _resetNew", edge="Ea3a16a29")
    # Ea457b3e5 _resetNew -> _resetNewCount (Sched.java:581).
    r.comment("_resetNew -> _resetNewCount", edge="Ea457b3e5")
    # E91386df9 _resetNewCount -> _walkingCount (Sched.java:564-565,
    # passing the _cntFnNew method by reflection).
    r.comment("_resetNewCount -> _walkingCount (_cntFnNew passed)",
              edge="E91386df9")
    # Ee3f8c63a _walkingCount -> _cntFnNew (target; reflective
    # invoke at Sched.java:337-353, no user action).
    r.comment("_walkingCount reflectively invokes _cntFnNew (target)",
              edge="Ee3f8c63a")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
