#!/usr/bin/env python3
"""AnyMemo route_12: Category.setName.

Method: Category.setName
Edge ids (in route order):
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E690f7694 E6da90567 E41662266
    Eb655c6eb E705abaec Eee3d301b E3ae14c6f Ea1b5c440 E22318784
    E2d07d42a E42afebab E539b41d9 E05e70ac4 Ede1d5ab9 E5cf2c281
    Ea4753c40 E7419ac98 E5f166c81 E1139e2d6 Eea335e4d Efc5affc9
    E38d944b2 Efea12f21 E4372d4b5 E7fd4e338 E0079cf7f E433301e4
    E6ec64fc2 E61c173c6 E75a47095
Printed route file: graphs/AnyMemo/scratch/route_print/
    Category.setName.txt
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (granted by
    run_app.sh from ROUTES.csv; this script never grants it).
Fixtures: none.
Setup: fresh install (pm clear). The printed chain reaches
    Preview/Edit through DatabaseMerger: the Misc tab starts the
    merger, tapping Merge runs the merge task and finishes back to
    the Preview/Edit session, whose menu then opens the category
    editor. The editor pre-fills its text field with the current
    category name, so a new name must be typed first: createOrReturn
    only calls setName when the name does not already exist.
Caveat (see REPORT.md): a merger started from the Misc tab has
    empty target/source fields, and merging "" into "" raises
    IllegalArgumentException instead of finishing; the graph's
    Preview/Edit return assumes the merger was started from
    Preview/Edit with a db and card in session. A real run needs
    that session (or two distinct db paths set in the merger)
    before the category steps can run. The typed category name is
    chosen to be novel in the sample db; if it already existed,
    createOrReturn would return it without calling setName.
"""

import argparse
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
try:
    from device.harness import Runner
except ModuleNotFoundError:
    # Fallback for layouts where the repo root is not four levels up:
    # load harness.py from the nearest ancestor device/harness dir.
    _dir = os.path.dirname(os.path.abspath(__file__))
    _spec = None
    while True:
        for _cand in (os.path.join(_dir, "device", "harness", "harness.py"),
                      os.path.join(_dir, "harness", "harness.py")):
            if os.path.isfile(_cand):
                _spec = importlib.util.spec_from_file_location(
                    "device_harness", _cand)
                break
        if _spec is not None:
            break
        _parent = os.path.dirname(_dir)
        if _parent == _dir:
            raise
        _dir = _parent
    _mod = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)
    Runner = _mod.Runner


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_12",
               edge_ids=["Eddc920eb", "Ee33f0797", "E0b0115b9",
                         "Ed9aa2280", "Efe6c7871", "E006becde",
                         "E48c9d4a5", "Ef4267162", "E25e1518b",
                         "E690f7694", "E6da90567", "E41662266",
                         "Eb655c6eb", "E705abaec", "Eee3d301b",
                         "E3ae14c6f", "Ea1b5c440", "E22318784",
                         "E2d07d42a", "E42afebab", "E539b41d9",
                         "E05e70ac4", "Ede1d5ab9", "E5cf2c281",
                         "Ea4753c40", "E7419ac98", "E5f166c81",
                         "E1139e2d6", "Eea335e4d", "Efc5affc9",
                         "E38d944b2", "Efea12f21", "E4372d4b5",
                         "E7fd4e338", "E0079cf7f", "E433301e4",
                         "E6ec64fc2", "E61c173c6", "E75a47095"],
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # Eddc920eb: MAIN / LAUNCHER intent starts AnyMemo.
        r.launch(args.package + "/.ui.AnyMemo", edge="Eddc920eb")
        # Ee33f0797: system instantiates AnyMemo, then onCreate.
        r.comment("system instantiates AnyMemo, then calls onCreate",
                  edge="Ee33f0797")
        # E0b0115b9: onCreate, permission already granted, loadUiComponents.
        r.comment("WRITE_EXTERNAL_STORAGE granted by run_app.sh; "
                  "onCreate calls loadUiComponents", edge="E0b0115b9")
        # Ed9aa2280: loadUiComponents calls initDrawer.
        r.comment("loadUiComponents calls initDrawer", edge="Ed9aa2280")
        # Efe6c7871: bottomNavigation.setSelectedItemId(recent_tab_menu)
        # dispatches the listener, so the Recent tab is selected cold.
        r.comment("setSelectedItemId(recent_tab_menu) dispatches the "
                  "bottom-nav listener", edge="Efe6c7871")
        # E006becde: itemId == recent_tab_menu: new RecentListFragment.
        r.comment("itemId == recent_tab_menu: new RecentListFragment",
                  edge="E006becde")
        # E48c9d4a5: fragment lifecycle: onAttach.
        r.comment("RecentListFragment lifecycle: onAttach",
                  edge="E48c9d4a5")
        # Ef4267162: fragment lifecycle: onCreate.
        r.comment("RecentListFragment lifecycle: onCreate",
                  edge="Ef4267162")
        # E25e1518b: fragment lifecycle: onCreateView.
        r.comment("RecentListFragment lifecycle: onCreateView",
                  edge="E25e1518b")
        # E690f7694: the Recent tab is shown once its view exists.
        r.comment("Recent tab shown (S_MAIN_RECENT)", edge="E690f7694")
        # E6da90567: tap a bottom-navigation item; Misc tab title is
        # "Misc" (strings.xml misc_tab_text, menu main_tab_items.xml).
        r.tap(edge="E6da90567", desc="Misc")
        # E41662266: itemId == misc_tab_menu: new MiscTabFragment.
        r.comment("itemId == misc_tab_menu: new MiscTabFragment",
                  edge="E41662266")
        # Eb655c6eb: fragment lifecycle: onAttach.
        r.comment("MiscTabFragment lifecycle: onAttach", edge="Eb655c6eb")
        # E705abaec: fragment lifecycle: onCreate.
        r.comment("MiscTabFragment lifecycle: onCreate", edge="E705abaec")
        # Eee3d301b: fragment lifecycle: onCreateView (misc_tab.xml).
        r.comment("MiscTabFragment lifecycle: onCreateView",
                  edge="Eee3d301b")
        # E3ae14c6f: tap any Misc-tab button; v == mergeButton
        # (misc_tab.xml misc_merge) starts DatabaseMerger.
        r.tap(edge="E3ae14c6f", res_id="misc_merge")
        # Ea1b5c440: onClick starts DatabaseMerger.
        r.comment("v == mergeButton: startActivity(DatabaseMerger)",
                  edge="Ea1b5c440")
        # E22318784: activity lifecycle: onCreate.
        r.comment("DatabaseMerger lifecycle: onCreate", edge="E22318784")
        # E2d07d42a: setContentView(merge_layout) shows the merger.
        r.comment("setContentView(merge_layout) shows the merger",
                  edge="E2d07d42a")
        # E42afebab: tap a field or button in Database Merger;
        # v == mergeButton (merge_layout.xml merge_button) runs the
        # merge progress task.
        r.tap(edge="E42afebab", res_id="merge_button")
        # E539b41d9: v == mergeButton: doProgressTask, whose task
        # doHeavyTask merges target into source.
        r.comment("mergeButton: doProgressTask runs doHeavyTask",
                  edge="E539b41d9")
        # E05e70ac4: doProgressTask runs doHeavyTask on a background
        # thread, then posts doUITask to the main thread.
        r.comment("doHeavyTask finishes; doUITask posted to main",
                  edge="E05e70ac4")
        # Ede1d5ab9: doUITask sets RESULT_OK and finishes, so the
        # Preview/Edit starter gets its result (menu_context_merge_db).
        r.comment("doUITask sets RESULT_OK and finishes",
                  edge="Ede1d5ab9")
        # E5cf2c281: PreviewEdit onActivityResult restarts the
        # activity, showing Preview/Edit (S_PREVIEW_EDIT).
        r.comment("PreviewEdit onActivityResult restarts Preview/Edit",
                  edge="E5cf2c281")
        # Ea4753c40: tap a Preview/Edit toolbar/overflow menu item.
        # menu_edit_categories has no showAsAction, so it lives in
        # the overflow menu ("More options" is the framework overflow
        # affordance); its title is "Filter category" (strings.xml
        # filter_category_text, menu preview_edit_activity_menu.xml).
        r.tap(edge="Ea4753c40", desc="More options")
        r.tap(edge="Ea4753c40", text="Filter category")
        # E7419ac98: menu_edit_categories (current card non-null)
        # calls showCategoriesDialog.
        r.comment("menu_edit_categories calls showCategoriesDialog",
                  edge="E7419ac98")
        # E5f166c81: showCategoriesDialog creates CategoryEditorFragment.
        r.comment("showCategoriesDialog creates CategoryEditorFragment",
                  edge="E5f166c81")
        # E1139e2d6: DialogFragment lifecycle: onAttach.
        r.comment("CategoryEditorFragment lifecycle: onAttach",
                  edge="E1139e2d6")
        # Eea335e4d: DialogFragment lifecycle: onCreate.
        r.comment("CategoryEditorFragment lifecycle: onCreate",
                  edge="Eea335e4d")
        # Efc5affc9: DialogFragment lifecycle: onCreateView
        # (category_dialog.xml); it starts InitTask.
        r.comment("CategoryEditorFragment lifecycle: onCreateView",
                  edge="Efc5affc9")
        # E38d944b2: onCreateView runs new InitTask().execute().
        r.comment("onCreateView starts InitTask", edge="E38d944b2")
        # Efea12f21: AsyncTask onPreExecute runs on the main thread.
        r.comment("InitTask onPreExecute on the main thread",
                  edge="Efea12f21")
        # E4372d4b5: AsyncTask doInBackground loads the categories.
        r.comment("InitTask doInBackground loads the categories",
                  edge="E4372d4b5")
        # E7fd4e338: onPostExecute fills the list and calls
        # enableListeners. Quiescence: wait for the dialog title
        # (strings.xml category_dialog_title) before tapping New.
        r.wait_for(edge="E7fd4e338",
                   text="Please select a category or enter a new one")
        # E0079cf7f: tap OK / New / Edit in the category dialog.
        # NewCategoryTask reads the edit field, and createOrReturn
        # only creates (and calls setName) for a name that does not
        # already exist, so first focus the field and type a novel
        # name, then tap New (category_dialog.xml button_new).
        r.tap(edge="E0079cf7f", res_id="category_dialog_edit")
        r.type_text("DeviceRouteCategory", edge="E0079cf7f")
        r.tap(edge="E0079cf7f", res_id="button_new")
        # E433301e4: new NewCategoryTask().execute(); onPreExecute
        # runs on the main thread first.
        r.comment("New button starts NewCategoryTask (onPreExecute)",
                  edge="E433301e4")
        # E6ec64fc2: AsyncTask doInBackground calls createOrReturn.
        r.comment("NewCategoryTask doInBackground calls createOrReturn",
                  edge="E6ec64fc2")
        # E61c173c6: createOrReturn (new name) calls create on the
        # new Category via CategoryDaoImpl.createOrReturn.
        r.comment("createOrReturn creates the new Category",
                  edge="E61c173c6")
        # E75a47095: the new Category gets its name: target
        # Category.setName.
        r.comment("new Category gets its name (target)",
                  edge="E75a47095")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
