#!/usr/bin/env python3
"""AnkiDroid route_03 (final draw): Stats$1.compare.

Target: Stats$1.compare (anonymous Comparator in
    Stats.calculateBreakdown, Stats.java:852-859).
Table verdict: CORRECT (final draw, 26 steps; the BFS route IS the
    judged route, so this script drives the BFS route, not a
    corrected route).
Route followed: final-draw BFS route from helper/judge-final/
    route_03.txt, edge ids verified against
    graphs/AnkiDroid/out/ankidroid_trigger_graph.json and
    methods.csv (route_edge_ids identical). Head changed vs the
    first-draw Stats script (old route_04): StudyOptionsFragment
    -> Reviewer -> drawer -> Statistics (steps 4-15), not the old
    deck-list drawer head. The drawer dispatch edge is E0b2882d5
    (S_REVIEWER -> onNavigationItemSelected) followed by E002cbed9
    (nav_stats -> Statistics.<init>).
Preconditions (see ROUTES_rows.csv setup cell):
  - Collection open; deck with cards to study.
  - Review history giving at least 2 hourly-breakdown entries: the
    comparator is called only when the breakdown list has >= 2
    entries (the list is forced to >= 1 at Stats.java:847-849).
  - The HOURLY_BREAKDOWN ChartFragment is attached, created
    (mIsCreated), measured non-zero, and its size/type/deck changed
    since creation, so checkAndUpdate calls createChart
    (Statistics.java:522-545 guard).
Mapping notes:
  - Selectors verified against the printed tree: "Study"
    (studyoptions_start string), "Statistics" (nav_stats title).
  - The "Navigate up" content description is the standard framework
    description; verify it against a live uiautomator dump before a
    real run.
  - The drawer-open tap and the "Statistics" tap share edge
    E0b2882d5 (two log lines, one edge).
  - Step 21 citation correction (judge file): the HOURLY_BREAKDOWN
    case is Statistics.java:503, not :514 (the CARDS_TYPES case of
    the same call); the edge itself is genuine either way.
  - The getItemPosition path applies to already-instantiated
    fragments (Statistics.java:293-302); the script dwells after
    onCollectionLoaded so fragments instantiate and the chart draws.
  - The JDK-sort link itself (Collections.sort calling compare) is
    INFERRED: java.util is not in the tree. The comparator's
    existence at Stats.java:852-859 is printed.
  - Live-run check still open: which chart tab is shown by default
    when Statistics opens, and whether the HOURLY_BREAKDOWN fragment
    is the one created without an extra tab tap; verify against a
    live run (see NOTES.md).
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
    "Eed14720a", "Ed7470ef3", "Ea375fff8", "E0b2882d5", "E002cbed9",
    "E156e1693", "E267ed275", "Eaf3beafc", "E072f904d", "E5bf994da",
    "Efa80210f", "E9a6b7dfd", "E7974b03d", "Eb3bbd238", "E36391b1c",
    "Efcceb288",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_03")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_03", edge_ids=EDGE_IDS,
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
    # Ea73b74da loadStudyOptionsFragment -> S_STUDYOPTIONS_FRAG.
    r.comment("study options fragment shown", edge="Ea73b74da")
    # E518f89ef S_STUDYOPTIONS_FRAG -> StudyOptionsFragment$1.onClick:
    # tap Study; cards due, so openReviewer runs.
    r.tap(edge="E518f89ef", text="Study")
    # E0b3abfeb $1.onClick -> openReviewer.
    r.comment("openReviewer", edge="E0b3abfeb")
    # Eb58e5599 openReviewer -> Reviewer.<init> (Intent).
    r.comment("startActivity Reviewer", edge="Eb58e5599")
    # Eed14720a Reviewer.<init> -> AbstractFlashcardViewer.onCreate
    # @Reviewer.
    r.comment("Reviewer onCreate", edge="Eed14720a")
    # Ed7470ef3 onCreate -> Reviewer.onCollectionLoaded.
    r.dwell(edge="Ed7470ef3", seconds=5)
    # Ea375fff8 onCollectionLoaded -> S_REVIEWER.
    r.comment("Reviewer page shown", edge="Ea375fff8")
    # E0b2882d5 S_REVIEWER -> NavigationDrawerActivity
    # .onNavigationItemSelected: open the drawer, then tap the
    # nav_stats item ("Statistics").
    r.tap(edge="E0b2882d5", desc="Navigate up")
    r.tap(edge="E0b2882d5", text="Statistics")
    # E002cbed9 onNavigationItemSelected -> Statistics.<init>
    # (nav_stats case, NavigationDrawerActivity.java:265-268).
    r.comment("drawer nav_stats starts Statistics", edge="E002cbed9")
    # E156e1693 Statistics.<init> -> Statistics.onCreate.
    r.comment("Statistics onCreate", edge="E156e1693")
    # E267ed275 Statistics.onCreate -> Statistics.onCollectionLoaded
    # (startLoadingCollection; AnkiActivity delivery).
    r.dwell(edge="E267ed275", seconds=3)
    # Eaf3beafc onCollectionLoaded -> SectionsPagerAdapter
    # .getItemPosition (notifyDataSetChanged; support-v4 ViewPager
    # dispatch to attached fragments; INFERRED framework step).
    r.dwell(edge="Eaf3beafc", seconds=3)
    # E072f904d getItemPosition -> ChartFragment.checkAndUpdate.
    r.comment("fragment checkAndUpdate", edge="E072f904d")
    # E5bf994da checkAndUpdate -> createChart (guards: mIsCreated,
    # non-zero size, changed state, Statistics.java:522-545).
    r.comment("createChart", edge="E5bf994da")
    # Efa80210f createChart -> AnkiStatsTaskHandler.createChart
    # (mChartType == HOURLY_BREAKDOWN, Statistics.java:503).
    r.comment("handler createChart HOURLY_BREAKDOWN", edge="Efa80210f")
    # E9a6b7dfd handler createChart -> CreateChartTask.doInBackground
    # (AnkiStatsTaskHandler.java:65-69; FW AsyncTask).
    r.comment("CreateChartTask doInBackground", edge="E9a6b7dfd")
    # E7974b03d doInBackground -> ChartBuilder.renderChart.
    r.comment("renderChart", edge="E7974b03d")
    # Eb3bbd238 renderChart -> calcStats.
    r.comment("calcStats", edge="Eb3bbd238")
    # E36391b1c calcStats -> Stats.calculateBreakdown
    # (HOURLY_BREAKDOWN case, ChartBuilder.java:85).
    r.comment("calculateBreakdown HOURLY_BREAKDOWN", edge="E36391b1c")
    # Efcceb288 calculateBreakdown -> Stats$1.compare (target;
    # guard: breakdown list has >= 2 entries; JDK sort dispatch
    # itself is INFERRED).
    r.comment("sort calls Stats$1.compare (target; JDK dispatch "
              "INFERRED)", edge="Efcceb288")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
