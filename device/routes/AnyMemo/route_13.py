#!/usr/bin/env python3
"""AnyMemo route_13: AMDateUtil.<init>.

Method: AMDateUtil.<init>
Edge ids (in route order):
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E690f7694 E6da90567 E41662266
    Eb655c6eb E705abaec Eee3d301b E3ae14c6f Ea1b5c440 E22318784
    E2d07d42a E42afebab E539b41d9 E05e70ac4 Ede1d5ab9 E5cf2c281
    Ea4753c40 Ec558d914 Ec64df922 Eb6abfe4f E5b169a98 E1b4becc5
    E39d2913c E6c07c368 E337562df Ed1633779 E4950a6b8 E090eafdd
    Ecc2a0e76 Ee5c58ecf
Printed route source:
    graphs/AnyMemo/scratch/route_print/AMDateUtil.<init>.txt
    plus graphs/AnyMemo/out/anymemo_trigger_graph.json edges above.
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (granted by
    run_app.sh from ROUTES.csv; this script never grants it).
Fixtures: none listed for this route in ROUTES.csv.
Setup: fresh install (pm clear by run_app.sh). First launch
    auto-creates state: AnyMemo.loadUiComponents ->
    prepareFirstTimeRun copies the french-body-parts.db asset to
    AMEnv.DEFAULT_ROOT_PATH and registers it as recent path 0, so the
    Recent tab shows one deck and the file browser's default directory
    contains french-body-parts.db. A second, empty database is created
    through the Open tab's create-DB dialog (see the E6da90567 block):
    merging a database into itself throws IllegalArgumentException
    (utils/DatabaseUtil.java:48-50), so a successful merge needs two
    distinct .db files.

ROUTE SPLICES (read before judging the flow): the printed route
splices two DatabaseMerger producers and two QACardActivity
dispatches, and this script exercises each side honestly instead of
pretending one activity is another:
  * Misc entry vs PreviewEdit return: MiscTabFragment starts
    DatabaseMerger with plain startActivity (MiscTabFragment.java
    :346-349), so its RESULT_OK cannot reach PreviewEditActivity.
    The script runs the Misc merge for real (blocks E42afebab-
    E05e70ac4), then re-enters PreviewEdit on the same sample db via
    the Open tab (block Ede1d5ab9); the onActivityResult /
    restartActivity blocks are comments for that re-entry.
  * CardPlayer vs Study dispatch: CardPlayerActivity.onPostInit
    calls setupControlButtons (CardPlayerFragment), NOT
    setupGradeButtons; only StudyActivity.onPostInit calls
    setupGradeButtons (StudyActivity.java:296-300). The printed
    chain's QACardActivity$2.run -> StudyActivity.onPostInit edge is
    the StudyActivity instance's dispatch of the shared runnable, so
    the script reaches it by tapping the sample deck in Recent
    (block E6c07c368) after visiting CardPlayerActivity.
"""

import argparse
import os
import sys

_HERE = os.path.abspath(__file__)
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(_HERE))))
if not os.path.isfile(os.path.join(_ROOT, "device", "harness",
                                   "harness.py")):
    # Fallback for staging/helper layouts: walk up looking for a
    # device/harness dir, including the stage/device staging root.
    _d = os.path.dirname(_HERE)
    while True:
        if os.path.isfile(os.path.join(_d, "device", "harness",
                                       "harness.py")):
            _ROOT = _d
            break
        if os.path.isfile(os.path.join(_d, "device", "stage", "device",
                                       "harness", "harness.py")):
            _ROOT = os.path.join(_d, "device", "stage")
            break
        _parent = os.path.dirname(_d)
        if _parent == _d:
            break
        _d = _parent
sys.path.insert(0, _ROOT)

from device.harness import Runner

COMPONENT = ("org.liberty.android.fantastischmemopro/"
             "org.liberty.android.fantastischmemo.ui.AnyMemo")
SAMPLE_DB = "french-body-parts.db"
SECOND_DB = "second.db"

EDGE_IDS = [
    "Eddc920eb", "Ee33f0797", "E0b0115b9", "Ed9aa2280", "Efe6c7871",
    "E006becde", "E48c9d4a5", "Ef4267162", "E25e1518b", "E690f7694",
    "E6da90567", "E41662266", "Eb655c6eb", "E705abaec", "Eee3d301b",
    "E3ae14c6f", "Ea1b5c440", "E22318784", "E2d07d42a", "E42afebab",
    "E539b41d9", "E05e70ac4", "Ede1d5ab9", "E5cf2c281", "Ea4753c40",
    "Ec558d914", "Ec64df922", "Eb6abfe4f", "E5b169a98", "E1b4becc5",
    "E39d2913c", "E6c07c368", "E337562df", "Ed1633779", "E4950a6b8",
    "E090eafdd", "Ecc2a0e76", "Ee5c58ecf",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_13", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # Eddc920eb: MAIN / LAUNCHER intent starts AnyMemo.
        r.launch(COMPONENT, edge="Eddc920eb")
        # Ee33f0797: Activity lifecycle / framework callback.
        r.comment("system instantiates AnyMemo, then calls onCreate",
                  edge="Ee33f0797")
        # E0b0115b9: onCreate: API <= 29 and WRITE_EXTERNAL_STORAGE
        # already granted, so loadUiComponents() runs.
        r.comment("permission pre-granted by run_app.sh; "
                  "loadUiComponents() runs", edge="E0b0115b9")
        # Ed9aa2280: initDrawer().
        r.comment("loadUiComponents calls initDrawer()", edge="Ed9aa2280")
        # Efe6c7871: bottomNavigation.setSelectedItemId(recent_tab_menu)
        # selects the Recent tab by default on a cold start.
        r.comment("bottom nav selects the Recent tab by default",
                  edge="Efe6c7871")
        # E006becde: Direct call to RecentListFragment.
        r.comment("bottom-nav listener creates RecentListFragment",
                  edge="E006becde")
        # E48c9d4a5: Fragment lifecycle callback.
        r.comment("FragmentManager calls onAttach", edge="E48c9d4a5")
        # Ef4267162: Fragment lifecycle callback.
        r.comment("FragmentManager calls onCreate", edge="Ef4267162")
        # E25e1518b: Fragment lifecycle callback.
        r.comment("FragmentManager calls onCreateView", edge="E25e1518b")
        # E690f7694: The Recent tab is shown once its view exists.
        # First launch already copied french-body-parts.db and
        # registered it as recent path 0, so the list is non-empty.
        r.comment("Recent tab shown; first-run sample deck present",
                  edge="E690f7694")
        # E6da90567: Tap a bottom-navigation item. This block taps
        # Open first: the Open tab's create-DB button (add_db_fab,
        # shown because AnyMemo passes EXTRA_SHOW_CREATE_DB_BUTTON)
        # creates the second, empty database that a successful merge
        # needs (merging a db into itself throws).
        r.tap(edge="E6da90567", text="Open")
        r.tap(edge="E6da90567", res_id="add_db_fab")
        r.type_text(SECOND_DB, edge="E6da90567")
        r.tap(edge="E6da90567", text="OK")
        # E41662266: itemId == misc_tab_menu: new MiscTabFragment().
        r.tap(edge="E41662266", text="Misc")
        # Eb655c6eb: constructor then onAttach.
        r.comment("FragmentManager calls MiscTabFragment.onAttach",
                  edge="Eb655c6eb")
        # E705abaec: onAttach then onCreate.
        r.comment("FragmentManager calls MiscTabFragment.onCreate",
                  edge="E705abaec")
        # Eee3d301b: onCreate then onCreateView.
        r.comment("FragmentManager calls MiscTabFragment.onCreateView",
                  edge="Eee3d301b")
        # E3ae14c6f: Tap a button on the Misc tab (every button
        # shares one OnClickListener, dispatched by v == field).
        # Misc tab button text "Merge DB" (merge_db_text); prefer
        # its layout id misc_merge (layout/misc_tab.xml).
        r.tap(edge="E3ae14c6f", res_id="misc_merge")
        # Ea1b5c440: v == mergeButton: startActivity(DatabaseMerger).
        r.comment("mergeButton starts DatabaseMerger", edge="Ea1b5c440")
        # E22318784: Activity lifecycle callback.
        r.comment("system instantiates DatabaseMerger, then onCreate",
                  edge="E22318784")
        # E2d07d42a: setContentView(merge_layout).
        r.comment("DatabaseMerger shows merge_layout", edge="E2d07d42a")
        # E42afebab: Tap a field or button in Database Merger. The
        # target field opens the .db-filtered file browser; tapping
        # a file row fills the field and returns. Fill target with
        # the sample db and source with the empty second db, so the
        # merge below succeeds.
        r.tap(edge="E42afebab", res_id="target_db_edit")
        r.tap(edge="E42afebab", text=SAMPLE_DB)
        r.tap(edge="E42afebab", res_id="source_db_edit")
        r.tap(edge="E42afebab", text=SECOND_DB)
        # E539b41d9: v == mergeButton: AMGUIUtility.doProgressTask,
        # whose task.doHeavyTask() merges target <- source.
        r.tap(edge="E539b41d9", res_id="merge_button")
        # E05e70ac4: doProgressTask runs doHeavyTask() on a
        # background thread, then posts doUITask() to the main
        # thread (toast + setResult(RESULT_OK) + finish()). The
        # Misc-started merger returns to the main screen, since
        # MiscTabFragment used plain startActivity, not
        # startActivityForResult.
        r.comment("merge succeeds (empty source into sample db); "
                  "doUITask sets RESULT_OK and finishes",
                  edge="E05e70ac4")
        # Ede1d5ab9: setResult(RESULT_OK); finish(): the Preview/Edit
        # starter gets its result (menu_context_merge_db). SPLICE
        # NOTE: the Misc-started merger above has no result
        # receiver, so this delivery cannot literally fire from it;
        # the printed route's merger-return belongs to the
        # PreviewEdit merge-menu flow. The script re-enters
        # PreviewEdit on the same sample db via the Open tab: tap
        # the sample db row, then Preview/edit (res/layout
        # open_actions_layout.xml id edit, text "Preview/edit").
        r.comment("merger result delivery (PreviewEdit merge-menu "
                  "flow); re-entering PreviewEdit via the Open tab",
                  edge="Ede1d5ab9")
        r.tap(edge="Ede1d5ab9", text="Open")
        r.tap(edge="Ede1d5ab9", text=SAMPLE_DB)
        r.tap(edge="Ede1d5ab9", res_id="edit")
        # E5cf2c281: restartActivity() for every request code except
        # RESULT_CANCELED. PreviewEdit is now showing the sample
        # db's first card, the same state a restart produces.
        r.comment("PreviewEdit showing after result/restart",
                  edge="E5cf2c281")
        # Ea4753c40: Tap a menu item in Preview/Edit. "Card player"
        # (menu_card_player, title card_player_text) lives in the
        # overflow menu; the overflow button's standard AppCompat
        # content description is "More options".
        r.tap(edge="Ea4753c40", desc="More options")
        r.tap(edge="Ea4753c40", text="Card player")
        # Ec558d914: menu_card_player: startActivityForResult
        # (CardPlayerActivity).
        r.comment("menu_card_player starts CardPlayerActivity",
                  edge="Ec558d914")
        # Ec64df922: Activity lifecycle callback.
        r.comment("system instantiates CardPlayerActivity, then "
                  "onCreate", edge="Ec64df922")
        # Eb6abfe4f: Direct call to QACardActivity.startInit.
        r.comment("CardPlayerActivity.onCreate calls startInit",
                  edge="Eb6abfe4f")
        # E5b169a98: multipleLoaderManager registers the Setting
        # loader.
        r.comment("startInit registers the Setting loader",
                  edge="E5b169a98")
        # E1b4becc5: The Setting loader delivers the Setting to its
        # callbacks object on the main thread.
        r.comment("Setting loader delivers on the main thread",
                  edge="E1b4becc5")
        # E39d2913c: handler.post(stored runnable) after the Setting
        # loader reports.
        r.comment("MultipleLoaderManager posts onPostInitRunnable",
                  edge="E39d2913c")
        # E6c07c368: Virtual/interface call that can dispatch to
        # this implementation. SPLICE NOTE: the runnable's
        # onPostInit() dispatches on the runtime activity;
        # CardPlayerActivity.onPostInit calls setupControlButtons,
        # not setupGradeButtons, so only a StudyActivity instance
        # reaches the next edge. The script backs out to the main
        # screen and taps the sample deck in Recent, which starts
        # StudyActivity and drives the same runnable to
        # StudyActivity.onPostInit.
        r.comment("CardPlayer dispatch cannot reach GradeButtons; "
                  "backing out to start StudyActivity instead",
                  edge="E6c07c368")
        r.back(edge="E6c07c368")
        r.back(edge="E6c07c368")
        r.tap(edge="E6c07c368", text="Recent")
        r.tap(edge="E6c07c368", text=SAMPLE_DB)
        # E337562df: the deck has at least one card.
        r.comment("StudyActivity.onPostInit: deck has cards, so "
                  "setupGradeButtons() runs", edge="E337562df")
        # Ed1633779: a new GradeButtonsFragment is added to
        # buttons_root.
        r.comment("setupGradeButtons adds GradeButtonsFragment",
                  edge="Ed1633779")
        # E4950a6b8: Fragment lifecycle callback.
        r.comment("FragmentManager calls GradeButtonsFragment.onCreate",
                  edge="E4950a6b8")
        # E090eafdd: Virtual/interface call that can dispatch to
        # this implementation (Dagger fragment injection).
        r.comment("onCreate calls fragmentComponents().inject(this)",
                  edge="E090eafdd")
        # Ecc2a0e76: Direct call to injectGradeButtonsFragment.
        r.comment("Dagger injects GradeButtonsFragment fields",
                  edge="Ecc2a0e76")
        # Ee5c58ecf: Dagger creates the @Inject field amDateUtil of
        # GradeButtonsFragment (GradeButtonsFragment.java:83).
        r.comment("Dagger creates @Inject AMDateUtil amDateUtil",
                  edge="Ee5c58ecf")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
