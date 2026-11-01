#!/usr/bin/env python3
"""AnyMemo route_14: Card.setId.

Method: Card.setId
Edge ids (in route order):
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E690f7694 E6da90567 E41662266
    Eb655c6eb E705abaec Eee3d301b E3ae14c6f Ea1b5c440 E22318784
    E2d07d42a E42afebab E539b41d9 E05e70ac4 Ede1d5ab9 E5cf2c281
    Ea4753c40 E29551d36 Ea9547810 E3e3dde07 E4c188ddd Ef35c2821
    Ec4ea1a32 E84049e2b E466c974a E40ae8328 Ee6ff2df1 Ee3b0092c
    E5e476aa4 E56061cd8
Printed route source:
    graphs/AnyMemo/scratch/route_print/Card.setId.txt
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

ROUTE SPLICE (read before judging the flow): the printed route
splices two DatabaseMerger producers. MiscTabFragment starts
DatabaseMerger with plain startActivity (MiscTabFragment.java
:346-349), so its RESULT_OK cannot reach PreviewEditActivity. The
script runs the Misc merge for real (blocks E42afebab-E05e70ac4),
then re-enters PreviewEdit on the same sample db via the Open tab
(block Ede1d5ab9); the onActivityResult / restartActivity blocks are
comments for that re-entry. The rest of the chain (PreviewEdit ->
Detail -> save -> Card.setId) is one coherent flow: PreviewEdit is
entered with the sample db's first card (OpenActions passes start id
1 by default), and DetailScreen.saveEntries -> refreshEntries sets
the card id from the shown id field (DetailScreen.java:173).
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
             "org.liberty.android.fantastischmemopro.ui.AnyMemo")
SAMPLE_DB = "french-body-parts.db"
SECOND_DB = "second.db"

EDGE_IDS = [
    "Eddc920eb", "Ee33f0797", "E0b0115b9", "Ed9aa2280", "Efe6c7871",
    "E006becde", "E48c9d4a5", "Ef4267162", "E25e1518b", "E690f7694",
    "E6da90567", "E41662266", "Eb655c6eb", "E705abaec", "Eee3d301b",
    "E3ae14c6f", "Ea1b5c440", "E22318784", "E2d07d42a", "E42afebab",
    "E539b41d9", "E05e70ac4", "Ede1d5ab9", "E5cf2c281", "Ea4753c40",
    "E29551d36", "Ea9547810", "E3e3dde07", "E4c188ddd", "Ef35c2821",
    "Ec4ea1a32", "E84049e2b", "E466c974a", "E40ae8328", "Ee6ff2df1",
    "Ee3b0092c", "E5e476aa4", "E56061cd8",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_14", edge_ids=EDGE_IDS,
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
        # Ea4753c40: Tap a menu item in Preview/Edit. "Detail"
        # (editmenu_detail_id, title detail_menu_text) lives in the
        # overflow menu; the overflow button's standard AppCompat
        # content description is "More options".
        r.tap(edge="Ea4753c40", desc="More options")
        r.tap(edge="Ea4753c40", text="Detail")
        # E29551d36: editmenu_detail_id: startActivityForResult
        # (DetailScreen) with the current card id.
        r.comment("Detail menu item starts DetailScreen for the "
                  "current card", edge="E29551d36")
        # Ea9547810: Activity lifecycle / framework callback.
        r.comment("system instantiates DetailScreen, then onCreate",
                  edge="Ea9547810")
        # E3e3dde07: new InitTask().execute(): onPreExecute runs on
        # the calling (main) thread first.
        r.comment("DetailScreen.onCreate executes InitTask",
                  edge="E3e3dde07")
        # E4c188ddd: AsyncTask runs doInBackground after onPreExecute.
        r.comment("InitTask loads the card from the db on a worker "
                  "thread", edge="E4c188ddd")
        # Ef35c2821: the card is delivered on the main thread.
        r.comment("InitTask.onPostExecute populates the fields",
                  edge="Ef35c2821")
        # Ec4ea1a32: the raw fields are populated and shown.
        r.comment("Detail screen shows the card fields",
                  edge="Ec4ea1a32")
        # E84049e2b: Tap a menu item in Detail. "Save" (detail menu
        # id save, title settings_save) is shown as an action with
        # an icon, so its content description is its title.
        r.tap(edge="E84049e2b", desc="Save")
        # E466c974a: save: the confirm-save dialog is shown.
        r.comment("Save menu item shows the update-warning dialog",
                  edge="E466c974a")
        # E40ae8328: Tap OK (confirm save).
        r.tap(edge="E40ae8328", text="OK")
        # Ee6ff2df1: new SaveCardTask().execute().
        r.comment("OK click executes SaveCardTask", edge="Ee6ff2df1")
        # Ee3b0092c: Direct call to saveEntries().
        r.comment("SaveCardTask.doInBackground calls saveEntries",
                  edge="Ee3b0092c")
        # E5e476aa4: Direct call to refreshEntries().
        r.comment("saveEntries calls refreshEntries", edge="E5e476aa4")
        # E56061cd8: Direct call to Card.setId: refreshEntries
        # parses the shown id field and sets it on the card
        # (DetailScreen.java:173), before cardDao.update runs.
        r.comment("refreshEntries sets the card id from the id field",
                  edge="E56061cd8")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
