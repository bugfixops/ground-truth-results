#!/usr/bin/env python3
"""AnkiDroid route_19: AdvancedStatistics$Card.setIvl.

Target: AdvancedStatistics$Card.setIvl.
Table verdict: CORRECT (combined-merge redraw, row 22, 35 steps;
    the printed route IS the judged route, with the Statistics
    drawer dispatch Ebf481404/Ebd71b23a). Edges unchanged.
Route followed: printed route: fragment -> Study -> Reviewer ->
    drawer Statistics -> Statistics lifecycle -> pager
    getItemPosition -> chart fragment -> chart task -> renderChart
    -> calcStats -> calculateDue -> runFilter advancedStatistics ->
    simulation chain -> setIvl.
Preconditions: collection open; deck with cards to study; review
    history present so the simulation has cards to simulate;
    preference advanced_statistics_enabled ON, set by run setup
    before launch (Hooks installs AdvancedStatistics only then).
Mapping notes:
  - Rewritten from the old first-draw route_19 script: that script
    drove a different prefix (deck-picker drawer directly to
    Statistics, getItem edge) and a different tail edge set. The
    final BFS prefix goes through the Reviewer, and the pager edge
    is getItemPosition, not getItem; the old script's drawer
    "Statistics" text and FORECAST chart-type state note are kept.
  - "Navigate up" is the standard drawer-toggle description;
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
    "Eae89b47b", "Ea73b74da", "E8972c27b", "E0b3abfeb", "Eb58e5599",
    "Eed14720a", "Ed7470ef3", "Ea375fff8", "Ebf481404", "Ebd71b23a",
    "E156e1693", "E267ed275", "Eaf3beafc", "E072f904d", "E5bf994da",
    "Efa80210f", "E9a6b7dfd", "E7974b03d", "Eb3bbd238", "E8e4a5c14",
    "Edbd9c947", "E776e20c8", "E66c764f8", "Ed7f1b8da", "Ebc9c4330",
    "E9f4ec50d", "E05d33c99", "E9ec3d5bf", "Edf963b60", "E97f65ff7",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_19")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_19", edge_ids=EDGE_IDS,
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
    # E8972c27b S_STUDYOPTIONS_FRAG -> StudyOptionsFragment$1.onClick:
    # the start-study button (guard: deck has cards to study).
    r.tap(edge="E8972c27b", text="Study")
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
    # Ebf481404 S_REVIEWER -> onNavigationItemSelected: open the
    # drawer, then tap the nav_stats item. String verified in res:
    # statistics = "Statistics".
    r.tap(edge="Ebf481404", desc="Navigate up")
    r.tap(edge="Ebf481404", text="Statistics")
    # Ebd71b23a onNavigationItemSelected -> Statistics.<init>.
    r.comment("startActivity Statistics", edge="Ebd71b23a")
    # E156e1693 Statistics.<init> -> onCreate.
    r.comment("Statistics onCreate", edge="E156e1693")
    # E267ed275 onCreate -> onCollectionLoaded.
    r.comment("Statistics collection loaded", edge="E267ed275")
    # Eaf3beafc onCollectionLoaded ->
    # SectionsPagerAdapter.getItemPosition (framework delivery after
    # notifyDataSetChanged). CHART-TYPE STATE (no dedicated graph
    # edge): select the FORECAST tab (Statistics.java:485-488
    # passes ChartType.FORECAST; tab title verified in res:
    # stats_forecast = "Forecast"), so calcStats takes the FORECAST
    # branch. The tab tap is logged under this edge, the same
    # convention the old route_19 script used for chart-type state.
    r.tap(edge="Eaf3beafc", text="Forecast")
    # E072f904d getItemPosition -> ChartFragment.checkAndUpdate.
    r.comment("chart fragment checkAndUpdate", edge="E072f904d")
    # E5bf994da checkAndUpdate -> createChart.
    r.comment("createChart", edge="E5bf994da")
    # Efa80210f createChart -> AnkiStatsTaskHandler.createChart.
    r.comment("AnkiStatsTaskHandler.createChart", edge="Efa80210f")
    # E9a6b7dfd -> CreateChartTask.doInBackground.
    r.comment("chart task running", edge="E9a6b7dfd")
    # E7974b03d -> ChartBuilder.renderChart.
    r.comment("renderChart", edge="E7974b03d")
    # Eb3bbd238 renderChart -> calcStats.
    r.comment("calcStats", edge="Eb3bbd238")
    # E8e4a5c14 calcStats -> Stats.calculateDue (FORECAST branch).
    # Wait for the chart computation.
    r.dwell(edge="E8e4a5c14", seconds=10)
    # Edbd9c947 calculateDue -> Hooks.runFilter@advancedStatistics.
    r.comment("runFilter advancedStatistics", edge="Edbd9c947")
    # E776e20c8 runFilter -> AdvancedStatistics.runFilter. Guard:
    # the hook is installed only when pref
    # advanced_statistics_enabled is true (run setup must set it);
    # without it the chain stops here.
    r.comment("AdvancedStatistics.runFilter", edge="E776e20c8")
    # E66c764f8 -> calculateDueAsMetaInfo.
    r.comment("calculateDueAsMetaInfo", edge="E66c764f8")
    # Ed7f1b8da -> calculateDueAsPlottableSimulationResult.
    r.comment("calculateDueAsPlottableSimulationResult",
              edge="Ed7f1b8da")
    # Ebc9c4330 -> simNreviews(int,Decks,String,TodayStats).
    r.comment("simNreviews 4-arg", edge="Ebc9c4330")
    # E9f4ec50d simNreviews(4-arg) -> simNreviews(int,Deck).
    r.comment("simNreviews per deck", edge="E9f4ec50d")
    # E05d33c99 simNreviews(int,Deck) -> simulateReview.
    r.comment("simulateReview", edge="E05d33c99")
    # E9ec3d5bf simulateReview -> simSingleReview(Card,int).
    r.comment("simSingleReview", edge="E9ec3d5bf")
    # Edf963b60 simSingleReview -> applyOutcomeToCard.
    r.comment("applyOutcomeToCard", edge="Edf963b60")
    # E97f65ff7 applyOutcomeToCard -> Card.setIvl (target;
    # AdvancedStatistics.java:832).
    r.comment("Card.setIvl reached (target)", edge="E97f65ff7")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
