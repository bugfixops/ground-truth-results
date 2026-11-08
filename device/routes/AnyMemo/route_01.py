#!/usr/bin/env python3
"""AnyMemo route_01: DefaultScheduler.randomNumber.

Method: DefaultScheduler.randomNumber
Edge ids in order:
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E690f7694 E6da90567 E41662266
    Eb655c6eb E705abaec Eee3d301b E3ae14c6f Ea1b5c440 E22318784
    E2d07d42a E42afebab E539b41d9 E05e70ac4 Ede1d5ab9 E5cf2c281
    E7318059a Ed6809c1a E381a1e56 E6ba0e8f5 E13ef4274 E8ac918d8
    E0f4e6d1d Ec1179877 Ee4fce072 Ee727ccc5 E21a4b76d E4dad0644
    E489d4cec E3207fdd2 E6fd729fa Efb283f3d E86a669f5 Ed571550a
    E85ceda98 Efb79e707 E1735427f E5b13cd61 E274afffc E38ccba43
Printed route: graphs/AnyMemo/scratch/route_print/DefaultScheduler.randomNumber.txt
Permissions (ROUTES.csv, granted by run_app.sh before this script runs):
    android.permission.WRITE_EXTERNAL_STORAGE
Fixtures: none.
Setup: none pushed by run_app.sh. First launch auto-creates state:
    AnyMemo.prepareFirstTimeRun copies the bundled sample database
    (french-body-parts.db) to the app's external files anymemo folder
    and registers it as recent path 0 (ui/AnyMemo.java:315-321), so the
    Recent tab is non-empty. A fresh install also shows the
    "New version installed" dialog (savedVersionCode default 1 differs
    from the app version code); the script taps OK to dismiss it.

Selector notes (all read from layout XML, strings.xml, or source):
  - Bottom navigation items are menu/main_tab_items.xml ids
    (misc_tab_menu); the harness matches resource ids by suffix.
  - Misc tab Merge button: layout/misc_tab.xml id misc_merge
    (MiscTabFragment.java:346-349 starts DatabaseMerger on it).
  - Database Merger Merge button: layout/merge_layout.xml id
    merge_button (DatabaseMerger.java:64,115).
  - Preview/Edit search: menu/preview_edit_activity_menu.xml id
    action_search with a SearchView; the query "#1" uses the
    search-by-id pattern (PreviewEditActivity.java SEARCH_BY_ID_PATTERN
    "#\\d+"), which finds card id 1 ("head") of the sample database
    regardless of card text.
  - Card body tap: layout/card_layout.xml root view id "root"
    (CardFragment.java:121-128 wires the card click listener to it).
  - Grade button tap on the final edge: layout/grade_buttons_quiz.xml
    id grade_button_5. In this source, setGradeButtonTitle calls
    scheduler.schedule(..., includeNoise=false), while grading a card
    calls schedule(..., includeNoise=true) (GradeButtonsFragment.java
    GradeTask), which is the call that can reach calculateIntervalNoise
    and randomNumber when noise is enabled (the default,
    SchedulingAlgorithmParameters defaultEnableNoise=true). The grade
    tap is therefore an extra driving action on the final edge, not a
    separate route step; see REPORT.md for the full caveat.
Caveat (see REPORT.md): the printed chain splices a Misc-tab
    DatabaseMerger entry onto a PreviewEditActivity result tail, but
    in this source a Misc-tab launch starts DatabaseMerger with no
    extras (empty target/source fields) and does not return a result
    to PreviewEditActivity; the result-returning entry is PreviewEdit's
    own merge-db menu item (menu_context_merge_db), which pre-fills
    the target field with the current database path. The script
    follows the printed edges as written; the merger tail may not be
    reachable in a real run from the Misc-tab entry point.
"""

import argparse
import importlib.util
import os
import sys


def _load_runner():
    """Find harness.py: walk up from this file, else the stage copy."""
    node = os.path.dirname(os.path.abspath(__file__))
    candidates = []
    while True:
        candidates.append(os.path.join(node, "harness", "harness.py"))
        parent = os.path.dirname(node)
        if parent == node:
            break
        node = parent
    for path in candidates:
        if os.path.isfile(path):
            spec = importlib.util.spec_from_file_location("device_harness", path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module.Runner
    raise ImportError("harness.py not found in any candidate location")


Runner = _load_runner()

EDGE_IDS = [
    "Eddc920eb", "Ee33f0797", "E0b0115b9", "Ed9aa2280", "Efe6c7871",
    "E006becde", "E48c9d4a5", "Ef4267162", "E25e1518b", "E690f7694",
    "E6da90567", "E41662266", "Eb655c6eb", "E705abaec", "Eee3d301b",
    "E3ae14c6f", "Ea1b5c440", "E22318784", "E2d07d42a", "E42afebab",
    "E539b41d9", "E05e70ac4", "Ede1d5ab9", "E5cf2c281", "E7318059a",
    "Ed6809c1a", "E381a1e56", "E6ba0e8f5", "E13ef4274", "E8ac918d8",
    "E0f4e6d1d", "Ec1179877", "Ee4fce072", "Ee727ccc5", "E21a4b76d",
    "E4dad0644", "E489d4cec", "E3207fdd2", "E6fd729fa", "Efb283f3d",
    "E86a669f5", "Ed571550a", "E85ceda98", "Efb79e707", "E1735427f",
    "E5b13cd61", "E274afffc", "E38ccba43",
]

PKG_COMPONENT = ("org.liberty.android.fantastischmemopro/"
                 "org.liberty.android.fantastischmemo.ui.AnyMemo")


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnyMemo route_01 replay")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_01", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # Eddc920eb S_ENTRY -> AnyMemo.<init>: launch the MAIN/LAUNCHER
    # activity. A fresh install shows the "New version installed"
    # dialog on top of it; tap OK (strings.xml ok_text) to dismiss.
    r.launch(PKG_COMPONENT, "Eddc920eb")
    r.tap("Eddc920eb", text="OK")
    # Ee33f0797 AnyMemo.<init> -> AnyMemo.onCreate: framework.
    r.comment("system instantiates AnyMemo, then onCreate", "Ee33f0797")
    # E0b0115b9 AnyMemo.onCreate -> AnyMemo.loadUiComponents: granted
    # WRITE_EXTERNAL_STORAGE by run_app.sh; framework/call, no action.
    r.comment("loadUiComponents runs (permission pre-granted)", "E0b0115b9")
    # Ed9aa2280 AnyMemo.loadUiComponents -> AnyMemo.initDrawer: call.
    r.comment("initDrawer runs", "Ed9aa2280")
    # Efe6c7871 AnyMemo.initDrawer -> AnyMemo$2.onNavigationItemSelected@INIT:
    # cold-start selection of the Recent tab (AnyMemo.java:263).
    r.comment("cold-start selects the Recent tab", "Efe6c7871")
    # E006becde AnyMemo$2.onNavigationItemSelected@INIT -> RecentListFragment.<init>.
    r.comment("RecentListFragment created for the Recent tab", "E006becde")
    # E48c9d4a5 RecentListFragment.<init> -> RecentListFragment.onAttach.
    r.comment("fragment onAttach", "E48c9d4a5")
    # Ef4267162 RecentListFragment.onAttach -> RecentListFragment.onCreate.
    r.comment("fragment onCreate", "Ef4267162")
    # E25e1518b RecentListFragment.onCreate -> RecentListFragment.onCreateView.
    r.comment("fragment onCreateView", "E25e1518b")
    # E690f7694 RecentListFragment.onCreateView -> S_MAIN_RECENT.
    r.comment("Recent tab page entered", "E690f7694")
    # E6da90567 S_MAIN_RECENT -> AnyMemo$2.onNavigationItemSelected:
    # tap the Misc bottom-navigation item.
    r.tap("E6da90567", res_id="misc_tab_menu")
    # E41662266 AnyMemo$2.onNavigationItemSelected -> MiscTabFragment.<init>:
    # itemId == misc_tab_menu branch (AnyMemo.java:249-250).
    r.comment("MiscTabFragment created for the Misc tab", "E41662266")
    # Eb655c6eb MiscTabFragment.<init> -> MiscTabFragment.onAttach.
    r.comment("fragment onAttach", "Eb655c6eb")
    # E705abaec MiscTabFragment.onAttach -> MiscTabFragment.onCreate.
    r.comment("fragment onCreate", "E705abaec")
    # Eee3d301b MiscTabFragment.onCreate -> MiscTabFragment.onCreateView.
    r.comment("fragment onCreateView (misc_tab layout)", "Eee3d301b")
    # E3ae14c6f MiscTabFragment.onCreateView -> MiscTabFragment.onClick:
    # tap the Merge DB button on the Misc tab.
    r.tap("E3ae14c6f", res_id="misc_merge")
    # Ea1b5c440 MiscTabFragment.onClick -> DatabaseMerger.<init>:
    # v == mergeButton branch starts DatabaseMerger.
    r.comment("mergeButton branch starts DatabaseMerger", "Ea1b5c440")
    # E22318784 DatabaseMerger.<init> -> DatabaseMerger.onCreate.
    r.comment("DatabaseMerger onCreate", "E22318784")
    # E2d07d42a DatabaseMerger.onCreate -> S_DB_MERGER.
    r.comment("Database Merger page entered", "E2d07d42a")
    # E42afebab S_DB_MERGER -> DatabaseMerger.onClick: tap Merge.
    r.tap("E42afebab", res_id="merge_button")
    # E539b41d9 DatabaseMerger.onClick -> DatabaseMerger$1.doHeavyTask:
    # v == mergeButton branch runs the merge progress task.
    r.comment("merge progress task runs (doHeavyTask)", "E539b41d9")
    # E05e70ac4 DatabaseMerger$1.doHeavyTask -> DatabaseMerger$1.doUITask.
    r.comment("merge task finishes, doUITask runs", "E05e70ac4")
    # Ede1d5ab9 DatabaseMerger$1.doUITask -> PreviewEditActivity.onActivityResult.
    r.comment("merge result returns to PreviewEditActivity", "Ede1d5ab9")
    # E5cf2c281 PreviewEditActivity.onActivityResult -> S_PREVIEW_EDIT.
    r.comment("Preview/Edit page entered (restartActivity)", "E5cf2c281")
    # E7318059a S_PREVIEW_EDIT -> PreviewEditActivity.onCreateOptionsMenu:
    # framework inflates preview_edit_activity_menu.
    r.comment("options menu inflated by the framework", "E7318059a")
    # Ed6809c1a PreviewEditActivity.onCreateOptionsMenu ->
    # PreviewEditActivity$12.onQueryTextSubmit: open SearchView, type
    # the search-by-id query, submit with ENTER.
    r.tap("Ed6809c1a", res_id="action_search")
    r.type_text("#1", "Ed6809c1a")
    r.key("ENTER", "Ed6809c1a")
    # E381a1e56 PreviewEditActivity$12.onQueryTextSubmit ->
    # PreviewEditActivity.searchCard: automatic after submit.
    r.comment("query submitted, searchCard runs", "E381a1e56")
    # E6ba0e8f5 PreviewEditActivity.searchCard ->
    # PreviewEditActivity$SearchCardTask.doInBackground: AsyncTask.
    r.comment("SearchCardTask runs in the background", "E6ba0e8f5")
    # E13ef4274 PreviewEditActivity$SearchCardTask.doInBackground ->
    # PreviewEditActivity$SearchCardTask.onPostExecute: AsyncTask.
    r.comment("SearchCardTask finishes, onPostExecute runs", "E13ef4274")
    # E8ac918d8 PreviewEditActivity$SearchCardTask.onPostExecute ->
    # PreviewEditActivity.updateCardFrontSide: automatic.
    r.comment("found card shown, updateCardFrontSide runs", "E8ac918d8")
    # E0f4e6d1d PreviewEditActivity.updateCardFrontSide ->
    # QACardActivity.displayCard@PreviewEditActivity: call.
    r.comment("displayCard shows the card", "E0f4e6d1d")
    # Ec1179877 QACardActivity.displayCard@PreviewEditActivity ->
    # FlipableCardFragment.<init>: card style DOUBLE_SIDED.
    r.comment("double-sided card fragment created", "Ec1179877")
    # Ee4fce072 FlipableCardFragment.<init> -> FlipableCardFragment.onCreate.
    r.comment("fragment onCreate", "Ee4fce072")
    # Ee727ccc5 FlipableCardFragment.onCreate -> FlipableCardFragment.onCreateView.
    r.comment("fragment onCreateView", "Ee727ccc5")
    # E21a4b76d FlipableCardFragment.onCreateView -> FlipableCardFragment$1.getItem.
    r.comment("pager adapter supplies the card fragment", "E21a4b76d")
    # E4dad0644 FlipableCardFragment$1.getItem -> CardFragment$Builder.build.
    r.comment("card fragment built", "E4dad0644")
    # E489d4cec CardFragment$Builder.build -> CardFragment.<init>.
    r.comment("CardFragment created", "E489d4cec")
    # E3207fdd2 CardFragment.<init> -> CardFragment.onCreateView.
    r.comment("card view created", "E3207fdd2")
    # E6fd729fa CardFragment.onCreateView -> QACardActivity$6.onClick:
    # tap the card body (question-view click listener, set at
    # QACardActivity.java:742 via CardFragment root view).
    r.tap("E6fd729fa", res_id="root")
    # Efb283f3d QACardActivity$6.onClick -> QuizActivity.onClickQuestionView.
    r.comment("question-view click reveals the answer", "Efb283f3d")
    # E86a669f5 QuizActivity.onClickQuestionView ->
    # QACardActivity.displayCard@QuizActivity: call.
    r.comment("displayCard with the answer shown", "E86a669f5")
    # Ed571550a QACardActivity.displayCard@QuizActivity ->
    # QuizActivity.onPostDisplayCard: call.
    r.comment("onPostDisplayCard runs", "Ed571550a")
    # E85ceda98 QuizActivity.onPostDisplayCard ->
    # GradeButtonsFragment.setVisibility: call.
    r.comment("grade buttons made visible", "E85ceda98")
    # Efb79e707 GradeButtonsFragment.setVisibility ->
    # GradeButtonsFragment$6.run: handler-posted runnable.
    r.comment("posted runnable runs, grade titles computed", "Efb79e707")
    # E1735427f GradeButtonsFragment$6.run ->
    # GradeButtonsFragment.setGradeButtonTitle: call.
    r.comment("setGradeButtonTitle runs", "E1735427f")
    # E5b13cd61 GradeButtonsFragment.setGradeButtonTitle ->
    # DefaultScheduler.schedule: call.
    r.comment("scheduler computes grade intervals", "E5b13cd61")
    # E274afffc DefaultScheduler.schedule ->
    # DefaultScheduler.calculateIntervalNoise: noise enabled and the
    # interval is above the minimal interval.
    r.comment("interval noise computed", "E274afffc")
    # E38ccba43 DefaultScheduler.calculateIntervalNoise ->
    # DefaultScheduler.randomNumber: target edge. The grade tap below
    # is an extra driving action on this edge: grading a card calls
    # scheduler.schedule(..., includeNoise=true), the call shape that
    # reaches calculateIntervalNoise in this source (see header).
    r.tap("E38ccba43", res_id="grade_button_5")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
