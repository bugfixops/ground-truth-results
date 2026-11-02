#!/usr/bin/env python3
"""AnkiDroid route_04: Stats$1.compare.

Target: Stats$1.compare (anonymous Comparator in
    Stats.calculateBreakdown).
Table verdict: WRONG (first-draw verdict; this script drives the
    CORRECTED route C04, never the printed BFS route).
Route followed: CORRECTED route C04 from
    helper/b6fix-r01-06/CORRECTED_ROUTES.md, with final-graph edge
    ids (24 edges). The printed route launched LOAD_DECK_COUNTS then
    took the RENDER_BROWSER_QA branch; this script follows the
    LOAD_DECK_COUNTS dispatch, the deck list it produces, and the
    navigation-drawer Statistics destination. No CardBrowser detour
    is needed: Statistics is a drawer destination of every
    NavigationDrawerActivity page.
Edge-id note: the helper file cites E47fbe466 for
    onResume -> updateDeckList, but that id is absent from the final
    graph build_F5.json; the final graph carries the same transition
    as E0b111c68 (guard: not mSyncOnResume and colIsOpen()), which
    this script uses instead. All other helper ids verified present.
Preconditions/fixtures:
  - Collection open; deck list loaded.
  - Review history giving at least 2 hourly-breakdown entries: the
    comparator is called only when the breakdown list has >= 2
    entries (the list is forced to >= 1 at Stats.java:838-840).
Mapping notes:
  - DeckPicker$22.onPostExecute -> S_DECKPICKER is a page
    abstraction with no dedicated graph edge; it is noted in the
    E10a14596 comment, not given an invented id.
  - The getItemPosition path applies to already-instantiated
    fragments (Statistics.java:296-298); the script dwells after
    onCollectionLoaded so fragments instantiate and the chart draws.
  - The JDK-sort link itself (Collections.sort calling compare) is
    INFERRED: java.util is not in the tree. The comparator's
    existence at Stats.java:852-859 is printed.
  - The drawer-open tap and the "Statistics" tap share edge
    E02986fa7 (two log lines, one edge).
  - The "Navigate up" content description is the standard framework
    description; verify it against a live uiautomator dump before a
    real run.
Launcher: com.ichi2.anki/.IntentHandler (AndroidManifest.xml:81-89).
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "E553ad2d8", "E0b111c68",
    "E8b5d2971", "E460971ee", "Ee1634710", "E3e610385", "Eee369b5f",
    "E10a14596", "E02986fa7", "E002cbed9", "E156e1693", "E267ed275",
    "Eaf3beafc", "E072f904d", "E5bf994da", "Efa80210f", "E9a6b7dfd",
    "E7974b03d", "Eb3bbd238", "E36391b1c", "Efcceb288",
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
    # E0b111c68 onResume -> updateDeckList (guard: not mSyncOnResume
    # and colIsOpen()).
    r.comment("resume takes updateDeckList (not sync)", edge="E0b111c68")
    # E8b5d2971 updateDeckList -> launchDeckTask (LOAD_DECK_COUNTS).
    r.comment("launchDeckTask TASK_TYPE_LOAD_DECK_COUNTS",
              edge="E8b5d2971")
    # E460971ee launchDeckTask -> doInBackground.
    r.comment("DeckTask execute -> doInBackground", edge="E460971ee")
    # Ee1634710 doInBackground -> doInBackgroundLoadDeckCounts
    # (DeckTask.java:234-235).
    r.comment("dispatch takes LOAD_DECK_COUNTS case", edge="Ee1634710")
    # E3e610385 doInBackground -> onPostExecute (framework delivery).
    r.dwell(edge="E3e610385", seconds=5)
    # Eee369b5f onPostExecute -> TaskListener.onPostExecute.
    r.comment("listener onPostExecute", edge="Eee369b5f")
    # E10a14596 TaskListener -> DeckPicker$22.onPostExecute; the deck
    # list is built, so the app is on the deck-picker page (page
    # abstraction: no dedicated graph edge for $22 -> S_DECKPICKER).
    r.comment("updateDeckList listener; deck list built, deck-picker "
              "page shown (page abstraction, no dedicated edge)",
              edge="E10a14596")
    # E02986fa7 S_DECKPICKER -> onNavigationItemSelected: open the
    # drawer, then tap the nav_stats item ("Statistics").
    r.tap(edge="E02986fa7", desc="Navigate up")
    r.tap(edge="E02986fa7", text="Statistics")
    # E002cbed9 onNavigationItemSelected -> Statistics.<init>
    # (nav_stats case).
    r.comment("drawer nav_stats starts Statistics", edge="E002cbed9")
    # E156e1693 Statistics.<init> -> Statistics.onCreate.
    r.comment("Statistics onCreate", edge="E156e1693")
    # E267ed275 Statistics.onCreate -> Statistics.onCollectionLoaded
    # (guard: col != null and colIsOpen()).
    r.comment("collection loaded", edge="E267ed275")
    # Eaf3beafc onCollectionLoaded -> getItemPosition
    # (notifyDataSetChanged; already-instantiated fragments).
    r.dwell(edge="Eaf3beafc", seconds=3)
    # E072f904d getItemPosition -> ChartFragment.checkAndUpdate.
    r.comment("fragment checkAndUpdate", edge="E072f904d")
    # E5bf994da checkAndUpdate -> createChart (guards: mIsCreated,
    # non-zero size, changed state).
    r.comment("createChart", edge="E5bf994da")
    # Efa80210f createChart -> AnkiStatsTaskHandler.createChart
    # (mChartType == HOURLY_BREAKDOWN).
    r.comment("handler createChart HOURLY_BREAKDOWN", edge="Efa80210f")
    # E9a6b7dfd handler createChart -> CreateChartTask.doInBackground
    # (guard: mIsRunning).
    r.comment("CreateChartTask doInBackground", edge="E9a6b7dfd")
    # E7974b03d doInBackground -> ChartBuilder.renderChart.
    r.comment("renderChart", edge="E7974b03d")
    # Eb3bbd238 renderChart -> calcStats.
    r.comment("calcStats", edge="Eb3bbd238")
    # E36391b1c calcStats -> Stats.calculateBreakdown
    # (HOURLY_BREAKDOWN case, ChartBuilder.java:84-85).
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
