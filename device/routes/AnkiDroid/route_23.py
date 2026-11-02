#!/usr/bin/env python3
"""AnkiDroid final-draw route_23: Sched.getToday.

Target: Sched.getToday.
Table verdict: CORRECT (combined-merge redraw, row 21,
    18 steps; the printed route IS the judged route). This is the
    18-step is:due route: step 17 Ec9480f74 (_where ->
    _findCardState@due, guard: the rebuilt deck's first search
    term terms[0] contains is:due) and step 18 Ea2ff24e9 (@due ->
    getToday, val "due") replace old steps 17-18
    Efa260a34/E594578a7; steps 1-16 unchanged. The correction is
    a data condition (terms[0] contains is:due), not a tap change.
    Drive: overflow menu -> Rebuild.
Route followed: corrected route, 18 edges, derived from the graph
    JSON by src/dst pairs and verified contiguous (see NOTES.md).
    No old first-draw script corresponds to this method (old
    route_23 was CardTemplateEditor$3.onPositive); this script is
    newly written.
Preconditions/fixtures:
  - Tablet/large-screen config (mFragmented true) so the study-options
    fragment loads; collection open.
  - A filtered (dyn) deck exists and is selected, so the Rebuild
    menu item is visible (StudyOptionsFragment.java:346-348).
  - That dyn deck's first search term contains is:due (the corrected
    data condition). No file fixture is pushed; the dyn deck is
    collection state that run setup must establish.
Mapping notes:
  - The Rebuild item text "Rebuild" is the string value of
    rebuild_cram_label (study_options_fragment.xml action_rebuild).
    Whether it sits directly on the toolbar or under the overflow
    ("More options") could not be verified statically, so the script
    taps overflow then Rebuild under the single edge E57aebbea
    (two taps, one edge, as first-draw route_01 did for drawer taps);
    the live run must confirm this against a uiautomator dump.
  - _fillDyn calls findCards before its empty-result early return,
    so the target is reached even if no cards match.
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
    "Eae89b47b", "Ea73b74da", "E57aebbea", "E2e103f8f", "E40f4f2c5",
    "E2f5e0703", "Eb48c622f", "Ecd526a93", "E163cfb49", "Ed12e8336",
    "E76fba6ee", "Ec9480f74", "Ea2ff24e9",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_23")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_23", edge_ids=EDGE_IDS,
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
    r.comment("study options fragment shown (dyn deck selected)",
              edge="Ea73b74da")
    # E57aebbea S_STUDYOPTIONS_FRAG -> StudyOptionsFragment
    # .onMenuItemClick: Rebuild item (visible only for a dyn deck).
    # Two taps, one edge (see header): overflow, then Rebuild.
    r.tap(edge="E57aebbea", desc="More options")
    r.tap(edge="E57aebbea", text="Rebuild")
    # E2e103f8f onMenuItemClick -> DeckTask.doInBackground@REBUILD_CRAM
    # (launchDeckTask TASK_TYPE_REBUILD_CRAM, getDeckTaskListener).
    r.comment("REBUILD_CRAM task launched", edge="E2e103f8f")
    # E40f4f2c5 -> doInBackgroundRebuildCram (task-type dispatch).
    r.comment("rebuild-cram background work", edge="E40f4f2c5")
    # E2f5e0703 -> Sched.rebuildDyn(long).
    r.comment("rebuildDyn", edge="E2f5e0703")
    # Eb48c622f rebuildDyn -> Sched._fillDyn.
    r.comment("_fillDyn", edge="Eb48c622f")
    # Ecd526a93 _fillDyn -> Collection.findCards(String,String):
    # query is terms[0] (containing is:due, the corrected condition)
    # plus " -is:suspended -is:buried -deck:filtered".
    r.comment("findCards with is:due term", edge="Ecd526a93")
    # E163cfb49 -> Finder.findCards(String,String).
    r.comment("Finder.findCards", edge="E163cfb49")
    # Ed12e8336 -> Finder._findCards.
    r.comment("_findCards", edge="Ed12e8336")
    # E76fba6ee -> Finder._where.
    r.comment("_where tokenizes the query", edge="E76fba6ee")
    # Ec9480f74 _where -> _findCardState@due
    # (guard: terms[0] contains is:due).
    r.comment("_findCardState for is:due", edge="Ec9480f74")
    # Ea2ff24e9 _findCardState@due -> Sched.getToday (target; val "due",
    # Finder.java:466).
    # branch at Finder.java:465-467, reached only because terms[0]
    # contains is:due).
    r.comment("getToday (target, due branch)", edge="Ea2ff24e9")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
