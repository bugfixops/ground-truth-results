#!/usr/bin/env python3
"""AnkiDroid route_19: AdvancedStatistics$Card.setIvl.

Method: AdvancedStatistics$Card.setIvl
Target verdict: WRONG (route_table.md route 19)
Route followed: the CORRECTED route, never the printed BFS route.
    Statistics/forecast prefix via runFilter("advancedStatistics");
    the mungeQA head is never used, because AdvancedStatistics
    registers only under "advancedStatistics" and its runFilter casts
    its argument to StatsMetaInfo, which an html String cannot satisfy.
Edge ids in order:
    E48de6d58 E26d20f74 E1ad4ef9b Eb3058057 E02986fa7 E002cbed9
    E156e1693 E267ed275 E13f0a521 E6ff1a41b E5bf994da Efa80210f
    E9a6b7dfd E7974b03d Eb3bbd238 E8e4a5c14 Ea34eba66 E70b0401a
    E66c764f8 Ed7f1b8da Ebc9c4330 E9f4ec50d E05d33c99 E9ec3d5bf
    Edf963b60 E97f65ff7
Sources: route_table.md route 19; helper/b6fix-r19-24/
    CORRECTED_ROUTES.md route 19.
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (graph env on
    Eb3058057; see route_16 for the full manifest list).
Fixtures: collection file exists; preference advanced_statistics_enabled
    true, so Hooks installs AdvancedStatistics on first getInstance;
    review history present; the deck-id list parses to at least one
    deck id and nIterations is at least one; the simulation yields at
    least one card with review time below tMax; the 2-arg
    simSingleReview takes the ELSE branch (not tElapsed >= computeNDays
    and not prob < computeMaxError).
Launcher: <package>/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh setup precedes this script; see
    route_16. At merge time this file lives under
    device/routes/AnkiDroid/, so the import matches Currency.

Mapping notes:
  - The drawer selector "Statistics" and the FORECAST chart-type
    selection are UI strings/state not fixed by the graph edges;
    verify them against a live uiautomator dump before a real run.
    The chart-type selection has no dedicated graph edge and is
    logged with r.comment, not invented as an edge id.
  - The old _renderQA head's guards do NOT carry over to this
    Statistics head.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Eb3058057", "E02986fa7",
    "E002cbed9", "E156e1693", "E267ed275", "E13f0a521", "E6ff1a41b",
    "E5bf994da", "Efa80210f", "E9a6b7dfd", "E7974b03d", "Eb3bbd238",
    "E8e4a5c14", "Ea34eba66", "E70b0401a", "E66c764f8", "Ed7f1b8da",
    "Ebc9c4330", "E9f4ec50d", "E05d33c99", "E9ec3d5bf", "Edf963b60",
    "E97f65ff7",
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
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init>.
    r.comment("launcher else branch starts DeckPicker", edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # Eb3058057 DeckPicker.onCreate -> S_DECKPICKER.
    r.comment("DeckPicker page shown, collection open", edge="Eb3058057")
    # E02986fa7 S_DECKPICKER ->
    # NavigationDrawerActivity.onNavigationItemSelected: open the
    # navigation drawer and choose Statistics.
    r.tap(edge="E02986fa7", text="Statistics")
    # E002cbed9 NavigationDrawerActivity.onNavigationItemSelected ->
    # Statistics.<init>. Automatic after the tap.
    r.comment("Statistics activity started", edge="E002cbed9")
    # E156e1693 Statistics.<init> -> Statistics.onCreate.
    r.comment("system instantiates Statistics, then onCreate",
              edge="E156e1693")
    # E267ed275 Statistics.onCreate -> Statistics.onCollectionLoaded.
    r.comment("Statistics collection loaded", edge="E267ed275")
    # E13f0a521 Statistics.onCollectionLoaded ->
    # Statistics$SectionsPagerAdapter.<init>. Automatic.
    r.comment("statistics pager adapter created", edge="E13f0a521")
    # CHART-TYPE STATE (no graph edge): select the FORECAST chart
    # type, so calcStats takes the FORECAST branch (ChartBuilder
    # .java:69-73). Verify the selector on a live dump.
    r.comment("CHART-TYPE STATE: select the FORECAST chart type", edge="E6ff1a41b")
    # E6ff1a41b Statistics$SectionsPagerAdapter.getItem ->
    # Statistics$ChartFragment.checkAndUpdate. Automatic.
    r.comment("chart fragment checked", edge="E6ff1a41b")
    # E5bf994da Statistics$ChartFragment.checkAndUpdate ->
    # Statistics$ChartFragment.createChart. Automatic.
    r.comment("chart creation requested", edge="E5bf994da")
    # Efa80210f Statistics$ChartFragment.createChart ->
    # AnkiStatsTaskHandler.createChart. Automatic.
    r.comment("chart task requested", edge="Efa80210f")
    # E9a6b7dfd AnkiStatsTaskHandler.createChart ->
    # AnkiStatsTaskHandler$CreateChartTask.doInBackground. Automatic.
    r.comment("chart task running", edge="E9a6b7dfd")
    # E7974b03d CreateChartTask.doInBackground ->
    # ChartBuilder.renderChart (ChartBuilder created at :108-110 of
    # AnkiStatsTaskHandler, renderChart called at :110). Automatic.
    r.comment("chart rendered", edge="E7974b03d")
    # Eb3bbd238 ChartBuilder.renderChart -> ChartBuilder.calcStats
    # (ChartBuilder.java:112-113). Automatic.
    r.comment("chart statistics calculated", edge="Eb3bbd238")
    # E8e4a5c14 ChartBuilder.calcStats ->
    # Stats.calculateDue(Context,AxisType) (FORECAST branch).
    # Automatic.
    r.comment("due statistics calculated", edge="E8e4a5c14")
    # Ea34eba66 Stats.calculateDue(Context,AxisType) ->
    # Hooks.runFilter (Stats.java:308-311, name
    # "advancedStatistics"). Automatic.
    r.comment("advancedStatistics filter run", edge="Ea34eba66")
    # E70b0401a Hooks.runFilter -> AdvancedStatistics.runFilter
    # (Hooks.java:144-150, name dispatch only). Automatic.
    r.comment("AdvancedStatistics filter dispatched",
              edge="E70b0401a")
    # E66c764f8 AdvancedStatistics.runFilter ->
    # AdvancedStatistics.calculateDueAsMetaInfo. Automatic.
    r.comment("due meta info calculated", edge="E66c764f8")
    # Ed7f1b8da calculateDueAsMetaInfo ->
    # calculateDueAsPlottableSimulationResult. Automatic.
    r.comment("simulation result calculated", edge="Ed7f1b8da")
    # Ebc9c4330 calculateDueAsPlottableSimulationResult ->
    # ReviewSimulator.simNreviews(int,Decks,String,TodayStats).
    r.comment("review simulation started", edge="Ebc9c4330")
    # E9f4ec50d simNreviews(int,Decks,String,TodayStats) ->
    # simNreviews(int,Deck). Automatic.
    r.comment("per-deck simulation", edge="E9f4ec50d")
    # E05d33c99 simNreviews(int,Deck) -> Review.simulateReview.
    r.comment("review simulated", edge="E05d33c99")
    # E9ec3d5bf Review.simulateReview ->
    # EaseClassifier.simSingleReview(Card,int) (ELSE branch).
    r.comment("single review simulated", edge="E9ec3d5bf")
    # Edf963b60 simSingleReview -> applyOutcomeToCard. Automatic.
    r.comment("review outcome applied", edge="Edf963b60")
    # E97f65ff7 applyOutcomeToCard -> AdvancedStatistics$Card.setIvl.
    # Automatic; this is the target edge.
    r.comment("card interval set", edge="E97f65ff7")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
