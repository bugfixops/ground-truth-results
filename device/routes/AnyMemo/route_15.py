#!/usr/bin/env python3
"""AnyMemo route_15: FileBrowserActivity.fileClickAction.

Method: FileBrowserActivity.fileClickAction
Edge ids (in route order):
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E690f7694 E6da90567 E41662266
    Eb655c6eb E705abaec Eee3d301b E3ae14c6f Ea1b5c440 E22318784
    E2d07d42a E42afebab Ec535ad41 E4821628a E06545007 E462b202a
    E2f87d376 E8e949ae4 E1cc2efc2 Ed6ca9a86 E33a7b439 E6ac84fa0
    Ece6ab928 E0b4fdb95 E61fb79e7
Printed route source:
    graphs/AnyMemo/scratch/route_print/FileBrowserActivity.fileClickAction.txt
    plus graphs/AnyMemo/out/anymemo_trigger_graph.json edges above.
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (granted by
    run_app.sh from ROUTES.csv; this script never grants it).
Fixtures: ROUTES.csv lists Download/sample_deck.apkg for this route,
    but this script does NOT use it, and no new fixture is needed:
    run_app.sh pushes it to /sdcard/Download, while the file browser
    opened here filters to ".db" (DatabaseMerger passes
    EXTRA_FILE_EXTENSIONS ".db") and starts in the app's anymemo
    directory, which on first launch already contains the sample
    database (see Setup). Tapping that .db row is what reaches
    fileClickAction. If the merger wants the .apkg tapped instead,
    ROUTES.csv and/or the browser filter would need amending first;
    that change belongs to the merger, not to this script.
Setup: fresh install (pm clear by run_app.sh). First launch
    auto-creates state: AnyMemo.loadUiComponents ->
    prepareFirstTimeRun copies the french-body-parts.db asset to
    AMEnv.DEFAULT_ROOT_PATH and registers it as recent path 0, so the
    file browser's default directory (DEFAULT_ROOT_PATH, used when no
    saved browser path exists) lists french-body-parts.db.
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

EDGE_IDS = [
    "Eddc920eb", "Ee33f0797", "E0b0115b9", "Ed9aa2280", "Efe6c7871",
    "E006becde", "E48c9d4a5", "Ef4267162", "E25e1518b", "E690f7694",
    "E6da90567", "E41662266", "Eb655c6eb", "E705abaec", "Eee3d301b",
    "E3ae14c6f", "Ea1b5c440", "E22318784", "E2d07d42a", "E42afebab",
    "Ec535ad41", "E4821628a", "E06545007", "E462b202a", "E2f87d376",
    "E8e949ae4", "E1cc2efc2", "Ed6ca9a86", "E33a7b439", "E6ac84fa0",
    "Ece6ab928", "E0b4fdb95", "E61fb79e7",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_15", edge_ids=EDGE_IDS,
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
        r.comment("Recent tab shown", edge="E690f7694")
        # E6da90567: Tap a bottom-navigation item (Recent / Open /
        # Download / Misc). Misc tab button titles come from
        # menu/main_tab_items.xml (misc_tab_text = "Misc").
        r.tap(edge="E6da90567", text="Misc")
        # E41662266: itemId == misc_tab_menu: new MiscTabFragment().
        r.comment("bottom-nav listener creates MiscTabFragment",
                  edge="E41662266")
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
        # target field opens the file browser (next edge).
        r.tap(edge="E42afebab", res_id="target_db_edit")
        # Ec535ad41: v == targetEdit: startActivityForResult
        # (FileBrowserActivity, ".db").
        r.comment("target field starts FileBrowserActivity (.db "
                  "filter)", edge="Ec535ad41")
        # E4821628a: Activity lifecycle callback.
        r.comment("system instantiates FileBrowserActivity, then "
                  "onCreate", edge="E4821628a")
        # E06545007: the activity commits the file browser fragment
        # in onCreate (listener at FileBrowserActivity.java:52).
        r.comment("FileBrowserActivity commits FileBrowserFragment",
                  edge="E06545007")
        # E462b202a: onCreate then onCreateView (this host).
        r.comment("FragmentManager calls FileBrowserFragment."
                  "onCreateView", edge="E462b202a")
        # E2f87d376: onCreateView then onResume (this host).
        r.comment("FragmentManager calls FileBrowserFragment.onResume",
                  edge="E2f87d376")
        # E8e949ae4: onResume() browses to the current/default
        # directory (this host). Fresh install: no saved browser
        # path, so the default is AMEnv.DEFAULT_ROOT_PATH, which
        # holds the first-run sample db.
        r.comment("onResume browses to the default anymemo directory",
                  edge="E8e949ae4")
        # E1cc2efc2: browseTo lists the folder (this host).
        r.comment("browseTo lists the directory", edge="E1cc2efc2")
        # Ed6ca9a86: fill passes the file list to the adapter of
        # this host.
        r.comment("fill passes the file list to the adapter",
                  edge="Ed6ca9a86")
        # E33a7b439: the recycler view binds the rows (this host).
        r.comment("RecyclerView binds the file rows", edge="E33a7b439")
        # E6ac84fa0: Tap a file or folder row (this host). Rows show
        # the file name (layout/filebrowser_item.xml file_name);
        # the sample db row reads "french-body-parts.db".
        r.tap(edge="E6ac84fa0", text=SAMPLE_DB)
        # Ece6ab928: fragment.openFile(selectedFileName) (this host).
        r.comment("row click calls fragment.openFile", edge="Ece6ab928")
        # E0b4fdb95: onFileClickListener.onFileBrowserFileClick
        # (clickedFile).
        r.comment("openFile notifies the activity listener",
                  edge="E0b4fdb95")
        # E61fb79e7: fileClickAction(file): puts the path in the
        # result intent and finishes (FileBrowserActivity.java
        # :68-71). DatabaseMerger.onActivityResult then fills the
        # target field with the picked path.
        r.comment("listener calls fileClickAction; result returns "
                  "the picked db path", edge="E61fb79e7")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
