#!/usr/bin/env python3
"""AnyMemo route_09: ExportAnyMemoDbFragment$3.accept.

Method: ExportAnyMemoDbFragment$3.accept
Edge ids (in route order):
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E690f7694 E6da90567 E41662266
    Eb655c6eb E705abaec Eee3d301b E3ae14c6f E32666868 E5de38108
    E371cde50 E80feb1d6 E4c9c6696 E819c4c37 E25db057c E0d920d05
    E11a193de Ea1290c7c E2cd531af E0a423d55 Efc94cdcf Edb4ae0e1
    Eb4314df5
Printed route file: graphs/AnyMemo/scratch/route_print/
    ExportAnyMemoDbFragment_3.accept.txt
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (granted by
    run_app.sh from ROUTES.csv; this script never grants it).
Fixtures: Download/sample_deck.apkg (pushed by run_app.sh to
    /sdcard/Download/sample_deck.apkg; this script never pushes it).
Setup: fresh install (pm clear). First launch installs the sample db
    (french-body-parts.db) into the default root (the app external
    files anymemo/ dir), which is what the export file browser lists
    by default with its .db filter; tapping that row is the bound
    file row. The Misc-tab Export section starts collapsed
    (misc_tab.xml export_items is gone), so the section header must
    be tapped first.
Caveat (see REPORT.md): tapping the row starts the system
    ACTION_CREATE_DOCUMENT picker; the accept target fires only
    after that picker is completed with a save location (an
    out-of-app step with no route edge).
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

    r = Runner(package=args.package, route="route_09",
               edge_ids=["Eddc920eb", "Ee33f0797", "E0b0115b9",
                         "Ed9aa2280", "Efe6c7871", "E006becde",
                         "E48c9d4a5", "Ef4267162", "E25e1518b",
                         "E690f7694", "E6da90567", "E41662266",
                         "Eb655c6eb", "E705abaec", "Eee3d301b",
                         "E3ae14c6f", "E32666868", "E5de38108",
                         "E371cde50", "E80feb1d6", "E4c9c6696",
                         "E819c4c37", "E25db057c", "E0d920d05",
                         "E11a193de", "Ea1290c7c", "E2cd531af",
                         "E0a423d55", "Efc94cdcf", "Edb4ae0e1",
                         "Eb4314df5"],
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
        # E3ae14c6f: tap any Misc-tab button; the Export section
        # header (misc_tab.xml misc_export) toggles the export_items
        # group from gone to visible, exposing the export rows.
        r.tap(edge="E3ae14c6f", res_id="misc_export")
        r.scroll_to(edge="E3ae14c6f", res_id="export_anymemo_db")
        # E32666868: v == exportAnyMemoButton (misc_tab.xml
        # export_anymemo_db): new ExportAnyMemoDbFragment, then show.
        r.tap(edge="E32666868", res_id="export_anymemo_db")
        # E5de38108: df.show then the DialogFragment lifecycle onCreate.
        r.comment("ExportAnyMemoDbFragment lifecycle: onCreate",
                  edge="E5de38108")
        # E371cde50: super.onCreate of the export picker (a
        # FileBrowserFragment subclass); it registers the file-click
        # listener that calls exportDatabase.
        r.comment("super.onCreate of the export file browser",
                  edge="E371cde50")
        # E80feb1d6: dialog-fragment lifecycle: onCreate then onCreateView.
        r.comment("FileBrowserFragment lifecycle: onCreateView",
                  edge="E80feb1d6")
        # E4c9c6696: dialog-fragment lifecycle: onCreateView then onResume.
        r.comment("FileBrowserFragment lifecycle: onResume",
                  edge="E4c9c6696")
        # E819c4c37: onResume browses to the current/default directory.
        r.comment("onResume browses to the default root",
                  edge="E819c4c37")
        # E25db057c: browseTo lists the folder.
        r.comment("browseTo lists the folder", edge="E25db057c")
        # E0d920d05: fill passes the file list to the adapter.
        r.comment("fill passes the file list to the adapter",
                  edge="E0d920d05")
        # E11a193de: the recycler view binds the rows. Quiescence:
        # wait until the first-run sample db row is bound.
        r.wait_for(edge="E11a193de", text="french-body-parts.db")
        # Ea1290c7c: tap a file row: the first-run sample db
        # (AnyMemo.java first-run copy, .db filter match, default root).
        r.tap(edge="Ea1290c7c", text="french-body-parts.db")
        # E2cd531af: row click calls fragment.openFile(selectedFileName).
        r.comment("row click calls openFile(selectedFileName)",
                  edge="E2cd531af")
        # E0a423d55: openFile calls the listener:
        # ExportAnyMemoDbFragment$1.onFileBrowserFileClick.
        r.comment("openFile calls $1.onFileBrowserFileClick",
                  edge="E0a423d55")
        # Efc94cdcf: the listener calls exportDatabase(file), which
        # starts the system ACTION_CREATE_DOCUMENT picker.
        r.comment("listener calls exportDatabase(file); system "
                  "create-document picker opens", edge="Efc94cdcf")
        # Edb4ae0e1: the picker finishes and returns its result to
        # the caller (onActivityResult). In a real run this needs the
        # picker to be completed with a save location; see REPORT.md.
        r.comment("picker returns RESULT_OK to onActivityResult",
                  edge="Edb4ae0e1")
        # Eb4314df5: the copy completes and the framework calls
        # accept (target ExportAnyMemoDbFragment$3.accept).
        r.comment("copy completes; framework calls $3.accept (target)",
                  edge="Eb4314df5")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
