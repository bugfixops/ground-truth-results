#!/usr/bin/env python3
"""AnyMemo route_03: CardDaoImpl.getCardsByCategory.

Method: CardDaoImpl.getCardsByCategory
Edge ids in order:
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E0336067c E3cdfa763 E0195fc37
    Ebf2205c3 E367b72be Ed19034c7 E0642b349 E7fde7d29 E8d639cb8
    E868fed7f Eed088f4e E7be5a455 Ef81b9220 Eef9e1b13 E5f5613c5
    Ea8f16838 E77427312 Ec49d569c E2966827d E6a473753 E8ca92427
    E3bd0f0ac E9fb575e4 Ef3621a87 E29ea0011 E3caa50fb
Printed route: graphs/AnyMemo/scratch/route_print/CardDaoImpl.getCardsByCategory.txt
Permissions (ROUTES.csv, granted by run_app.sh before this script runs):
    android.permission.WRITE_EXTERNAL_STORAGE
Fixtures: none.
Setup: none pushed by run_app.sh. First launch auto-creates state:
    AnyMemo.prepareFirstTimeRun copies the bundled sample database
    (french-body-parts.db) to the app's external files anymemo folder
    and registers it as recent path 0 (ui/AnyMemo.java:315-321), so the
    Recent tab shows the sample deck. A fresh install also shows the
    "New version installed" dialog; the script taps OK to dismiss it.

Selector notes (all read from layout XML, strings.xml, or source):
  - Recent row "more" button: layout/open_screen_recent_item.xml id
    recent_item_more_button (RecentListFragment.java:381,442-452).
  - Open-actions sheet: layout/open_actions_layout.xml ids; the quiz
    item is id "quiz" (OpenActionsFragment.java:99-101,148-152 branch
    creates QuizLauncherDialogFragment). Note: the trigger graph's gui
    text for this edge says "study", but the study item starts
    StudyActivity, while the quiz item is the one that creates
    QuizLauncherDialogFragment, so the script taps "quiz"; see
    REPORT.md.
  - Quiz launcher: layout/quiz_launcher_dialog.xml ids
    quiz_by_category_radio, category_button, start_quiz_button
    (QuizLauncherDialogFragment.java:148-190).
  - Category picked: "French (Body parts)", category id 2 of the
    sample database (checked in the bundled french-body-parts.db
    asset), so the quiz runs with a non-null filter category and
    QuizQueueManager.Builder.build takes the refill(Category) branch
    (QuizQueueManager.java:199-202) that calls getCardsByCategory.
    The printed route's guard for the launcher edge ("both radios not
    checked") describes the group-quiz branch, which instead takes
    refill(startOrd, quizSize) and never calls getCardsByCategory;
    the script therefore checks the category radio and picks a
    category, which is the only path in this source that reaches the
    target; see REPORT.md.
  - Category confirmation: layout/category_dialog.xml id button_ok
    (CategoryEditorFragment.java:80); the row tap only fills the edit
    field, OK confirms the selection to the launcher dialog.
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
    "E006becde", "E48c9d4a5", "Ef4267162", "E25e1518b", "E0336067c",
    "E3cdfa763", "E0195fc37", "Ebf2205c3", "E367b72be", "Ed19034c7",
    "E0642b349", "E7fde7d29", "E8d639cb8", "E868fed7f", "Eed088f4e",
    "E7be5a455", "Ef81b9220", "Eef9e1b13", "E5f5613c5", "Ea8f16838",
    "E77427312", "Ec49d569c", "E2966827d", "E6a473753", "E8ca92427",
    "E3bd0f0ac", "E9fb575e4", "Ef3621a87", "E29ea0011", "E3caa50fb",
]

PKG_COMPONENT = ("org.liberty.android.fantastischmemopro/"
                 "org.liberty.android.fantastischmemo.ui.AnyMemo")


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnyMemo route_03 replay")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_03", EDGE_IDS, args.log,
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
    # E0336067c RecentListFragment.onCreateView -> RecentListFragment.onResume.
    r.comment("fragment onResume, recent-deck loaders restart", "E0336067c")
    # E3cdfa763 RecentListFragment.onResume ->
    # RecentListFragment$RecentListLoaderCallbacks.onCreateLoader: framework.
    r.comment("loader callbacks run", "E3cdfa763")
    # E0195fc37 RecentListFragment$RecentListLoaderCallbacks.onCreateLoader ->
    # RecentListFragment$RecentListLoaderCallbacks$1.loadInBackground: async.
    r.comment("recent items load in the background", "E0195fc37")
    # Ebf2205c3 RecentListFragment$RecentListLoaderCallbacks$1.loadInBackground ->
    # RecentListFragment$RecentListLoaderCallbacks.onLoadFinished: async.
    r.comment("recent items loaded", "Ebf2205c3")
    # E367b72be RecentListFragment$RecentListLoaderCallbacks.onLoadFinished ->
    # RecentListFragment$RecentListAdapter.setItems: call.
    r.comment("adapter receives the recent items", "E367b72be")
    # Ed19034c7 RecentListFragment$RecentListAdapter.setItems ->
    # RecentListFragment$RecentListAdapter.onBindViewHolder: RecyclerView
    # binds the sample-deck row (recent list non-empty, see header).
    r.comment("recent row bound", "Ed19034c7")
    # E0642b349 RecentListFragment$RecentListAdapter.onBindViewHolder ->
    # RecentListFragment$RecentListAdapter$3.onClick: tap the "more"
    # button on the sample-deck row.
    r.tap("E0642b349", res_id="recent_item_more_button")
    # E7fde7d29 RecentListFragment$RecentListAdapter$3.onClick ->
    # OpenActionsFragment.<init>: call.
    r.comment("OpenActionsFragment created", "E7fde7d29")
    # E8d639cb8 OpenActionsFragment.<init> -> OpenActionsFragment.onAttach.
    r.comment("fragment onAttach", "E8d639cb8")
    # E868fed7f OpenActionsFragment.onAttach -> OpenActionsFragment.onCreate.
    r.comment("fragment onCreate", "E868fed7f")
    # Eed088f4e OpenActionsFragment.onCreate -> OpenActionsFragment.onCreateView.
    r.comment("fragment onCreateView", "Eed088f4e")
    # E7be5a455 OpenActionsFragment.onCreateView -> S_DLG_OPEN_ACTIONS.
    r.comment("open-actions sheet entered", "E7be5a455")
    # Ef81b9220 S_DLG_OPEN_ACTIONS -> OpenActionsFragment$1.onClick:
    # tap the quiz item, which creates QuizLauncherDialogFragment
    # (see header note on the trigger graph's "study" text).
    r.tap("Ef81b9220", res_id="quiz")
    # Eef9e1b13 OpenActionsFragment$1.onClick ->
    # QuizLauncherDialogFragment.<init>: call.
    r.comment("QuizLauncherDialogFragment created", "Eef9e1b13")
    # E5f5613c5 QuizLauncherDialogFragment.<init> ->
    # QuizLauncherDialogFragment.onAttach.
    r.comment("fragment onAttach", "E5f5613c5")
    # Ea8f16838 QuizLauncherDialogFragment.onAttach ->
    # QuizLauncherDialogFragment.onCreate.
    r.comment("fragment onCreate", "Ea8f16838")
    # E77427312 QuizLauncherDialogFragment.onCreate ->
    # QuizLauncherDialogFragment.onCreateDialog.
    r.comment("launcher dialog created", "E77427312")
    # Ec49d569c QuizLauncherDialogFragment.onCreateDialog -> S_DLG_QUIZ_LAUNCHER.
    r.comment("quiz launcher dialog entered", "Ec49d569c")
    # E2966827d S_DLG_QUIZ_LAUNCHER -> QuizLauncherDialogFragment$2.onClick:
    # check "quiz by category", pick the sample database's category,
    # confirm it, then tap Start quiz (the $2.onClick action).
    r.tap("E2966827d", res_id="quiz_by_category_radio")
    r.tap("E2966827d", res_id="category_button")
    r.tap("E2966827d", text="French (Body parts)")
    r.tap("E2966827d", res_id="button_ok")
    r.tap("E2966827d", res_id="start_quiz_button")
    # E6a473753 QuizLauncherDialogFragment$2.onClick -> QuizActivity.<init>:
    # startActivity with the category extra.
    r.comment("QuizActivity started for the chosen category", "E6a473753")
    # E8ca92427 QuizActivity.<init> -> QuizActivity.onCreate.
    r.comment("QuizActivity onCreate", "E8ca92427")
    # E3bd0f0ac QuizActivity.onCreate ->
    # QuizActivity$QuizQueueManagerLoaderCallbacks.onCreateLoader: framework.
    r.comment("queue-manager loader callbacks run", "E3bd0f0ac")
    # E9fb575e4 QuizActivity$QuizQueueManagerLoaderCallbacks.onCreateLoader ->
    # QuizActivity$QuizQueueManagerLoader.dbLoadInBackground: async.
    r.comment("queue loads in the background", "E9fb575e4")
    # Ef3621a87 QuizActivity$QuizQueueManagerLoader.dbLoadInBackground ->
    # QuizQueueManager$Builder.build: call.
    r.comment("queue manager built", "Ef3621a87")
    # E29ea0011 QuizQueueManager$Builder.build ->
    # QuizQueueManager.refill(Category): filterCategory non-null, so
    # the category branch is taken.
    r.comment("queue refilled for the category", "E29ea0011")
    # E3caa50fb QuizQueueManager.refill(Category) ->
    # CardDaoImpl.getCardsByCategory: target edge, automatic call.
    r.comment("target: cards loaded by category", "E3caa50fb")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
