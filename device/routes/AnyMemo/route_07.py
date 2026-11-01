#!/usr/bin/env python3
"""AnyMemo route_07: SettingsScreen$11.onFileBrowserFileClick.

Method: SettingsScreen$11.onFileBrowserFileClick
Edge ids (in route order):
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E690f7694 E6da90567 E41662266
    Eb655c6eb E705abaec Eee3d301b E3ae14c6f E980e9e1b Ededb1a3c
    E7c955a83 E0fbe1f41 Eb0ac90c3 Efa212a15 Ee664f697 E1c4bf2cf
    E51ad15c7 Ebdbb14a1 E1720ff72 Ee6394bd1 E28f5e0b8 Eff833375
    Ed4203df0 E8a0390f4 Ee4451e74
Printed route file: graphs/AnyMemo/scratch/route_print/
    SettingsScreen_11.onFileBrowserFileClick.txt
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (granted by
    run_app.sh from ROUTES.csv; this script never grants it).
Fixtures: Download/sample_deck.apkg (pushed by run_app.sh to
    /sdcard/Download/sample_deck.apkg; this script never pushes it).
Setup: fresh install (pm clear). First launch installs the sample db
    (french-body-parts.db) into the default root and copies empty.db
    to the app files dir; the Misc tab opens SettingsScreen for that
    empty db. The Setting entity default question font is empty, so
    the question-typeface checkbox starts unchecked and its edit
    field starts hidden; tapping the checkbox shows the field.
Caveat (see REPORT.md): the question-typeface picker lists only
    .ttf files from the default root, and a fresh install has no
    .ttf file there; the listed fixture is neither in that root nor
    a .ttf file. The final row tap below records the bound file-row
    tap for dry-run purposes; a real run reaches the target only
    once a .ttf fixture in the picker root is listed in ROUTES.csv.
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

    r = Runner(package=args.package, route="route_07",
               edge_ids=["Eddc920eb", "Ee33f0797", "E0b0115b9",
                         "Ed9aa2280", "Efe6c7871", "E006becde",
                         "E48c9d4a5", "Ef4267162", "E25e1518b",
                         "E690f7694", "E6da90567", "E41662266",
                         "Eb655c6eb", "E705abaec", "Eee3d301b",
                         "E3ae14c6f", "E980e9e1b", "Ededb1a3c",
                         "E7c955a83", "E0fbe1f41", "Eb0ac90c3",
                         "Efa212a15", "Ee664f697", "E1c4bf2cf",
                         "E51ad15c7", "Ebdbb14a1", "E1720ff72",
                         "Ee6394bd1", "E28f5e0b8", "Eff833375",
                         "Ed4203df0", "E8a0390f4", "Ee4451e74"],
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
        # E3ae14c6f: tap any Misc-tab button; v == defaultSettingsButton
        # (misc_tab.xml misc_default_settings) starts SettingsScreen
        # for the empty db.
        r.tap(edge="E3ae14c6f", res_id="misc_default_settings")
        # E980e9e1b: onClick starts SettingsScreen for the empty db.
        r.comment("v == defaultSettingsButton: startActivity(SettingsScreen)",
                  edge="E980e9e1b")
        # Ededb1a3c: activity lifecycle: onCreate.
        r.comment("SettingsScreen lifecycle: onCreate", edge="Ededb1a3c")
        # E7c955a83: multipleLoaderManager registers the Setting loader.
        r.comment("Setting loader registered in onCreate",
                  edge="E7c955a83")
        # E0fbe1f41: the Setting loader delivers the Setting on the
        # main thread.
        r.comment("Setting loader delivers the Setting (async)",
                  edge="E0fbe1f41")
        # Eb0ac90c3: handler.post(stored runnable) after the loader.
        r.comment("handler.post of the post-init runnable",
                  edge="Eb0ac90c3")
        # Efa212a15: the runnable calls setContentView then updateViews.
        # Loader quiescence: wait until the typeface checkbox row
        # (settings_screen.xml checkbox_typeface_question) is present.
        r.wait_for(edge="Efa212a15", res_id="checkbox_typeface_question")
        # Ee664f697: tap a checkbox in Settings; the question-typeface
        # checkbox starts unchecked (default question font is empty),
        # so this tap checks it and makes the typeface edit visible.
        r.tap(edge="Ee664f697", res_id="checkbox_typeface_question")
        # E1c4bf2cf: v == qTypefaceEdit (settings_screen.xml
        # edit_typeface_question): show the question-typeface file
        # picker (extensions .ttf, default root DEFAULT_ROOT_PATH).
        r.tap(edge="E1c4bf2cf", res_id="edit_typeface_question")
        # E51ad15c7: dialog-fragment lifecycle: onCreate then onCreateView.
        r.comment("FileBrowserFragment lifecycle: onCreateView",
                  edge="E51ad15c7")
        # Ebdbb14a1: dialog-fragment lifecycle: onCreateView then onResume.
        r.comment("FileBrowserFragment lifecycle: onResume",
                  edge="Ebdbb14a1")
        # E1720ff72: onResume browses to the current/default directory.
        r.comment("onResume browses to the default root",
                  edge="E1720ff72")
        # Ee6394bd1: browseTo lists the folder.
        r.comment("browseTo lists the folder", edge="Ee6394bd1")
        # E28f5e0b8: fill passes the file list to the adapter.
        r.comment("fill passes the file list to the adapter",
                  edge="E28f5e0b8")
        # Eff833375: the recycler view binds the rows.
        r.comment("recycler view binds the rows", edge="Eff833375")
        # Ed4203df0: tap a file row (filebrowser_item.xml file_name
        # is the row TextView id). See the header caveat: the picker
        # lists only .ttf files, so a real run needs a .ttf fixture
        # in the picker root before this tap can reach the target.
        r.tap(edge="Ed4203df0", res_id="file_name")
        # E8a0390f4: row click calls fragment.openFile(selectedFileName).
        r.comment("row click calls openFile(selectedFileName)",
                  edge="E8a0390f4")
        # Ee4451e74: openFile calls the listener: target
        # SettingsScreen$11.onFileBrowserFileClick.
        r.comment("openFile calls onFileBrowserFileClick (target)",
                  edge="Ee4451e74")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
