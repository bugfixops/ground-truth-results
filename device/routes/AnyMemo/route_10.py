#!/usr/bin/env python3
"""AnyMemo route_10: DatabaseOperationDialogUtil$4$1.onCancel.

Method: DatabaseOperationDialogUtil$4$1.onCancel
Edge ids (in route order):
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E690f7694 E6da90567 E526c5ca4
    E920eb93a Ec85bff66 E0f0f7b9b E32f0941a E15113078 Ee57bd8c9
    E14e26e11 Ef51283a6 E9ce1b9a0 E87b66810 E628b5323 E1424ae0a
    E55eb30b6 E75658ab7
Printed route file: graphs/AnyMemo/scratch/route_print/
    DatabaseOperationDialogUtil_4_1.onCancel.txt
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (granted by
    run_app.sh from ROUTES.csv; this script never grants it).
Fixtures: Download/sample_deck.apkg (pushed by run_app.sh to
    /sdcard/Download/sample_deck.apkg; this script never pushes it).
Setup: fresh install (pm clear). First launch installs the sample db
    (french-body-parts.db) into the default root, which is what the
    Open-tab file browser lists by default with its .db filter;
    long-pressing that row is the bound file row. The rename dialog
    has only a positive OK button plus a cancel listener, so the
    onCancel target is reached with the BACK key, not a button tap.
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

    r = Runner(package=args.package, route="route_10",
               edge_ids=["Eddc920eb", "Ee33f0797", "E0b0115b9",
                         "Ed9aa2280", "Efe6c7871", "E006becde",
                         "E48c9d4a5", "Ef4267162", "E25e1518b",
                         "E690f7694", "E6da90567", "E526c5ca4",
                         "E920eb93a", "Ec85bff66", "E0f0f7b9b",
                         "E32f0941a", "E15113078", "Ee57bd8c9",
                         "E14e26e11", "Ef51283a6", "E9ce1b9a0",
                         "E87b66810", "E628b5323", "E1424ae0a",
                         "E55eb30b6", "E75658ab7"],
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # Eddc920eb: MAIN / LAUNCHER intent starts AnyMemo.
        r.launch(args.package + "/org.liberty.android.fantastischmemo.ui.AnyMemo", edge="Eddc920eb")
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
        # E6da90567: tap a bottom-navigation item; Open tab title is
        # "Open" (strings.xml open_tab_text, menu main_tab_items.xml).
        r.tap(edge="E6da90567", desc="Open")
        # E526c5ca4: itemId == open_tab_menu: new OpenTabFragment.
        r.comment("itemId == open_tab_menu: new OpenTabFragment",
                  edge="E526c5ca4")
        # E920eb93a: OpenTabFragment onAttach sets the file-click listener.
        r.comment("OpenTabFragment onAttach sets the file-click listener",
                  edge="E920eb93a")
        # Ec85bff66: onAttach then onCreate of the Open-tab file browser.
        r.comment("Open-tab FileBrowserFragment lifecycle: onCreate",
                  edge="Ec85bff66")
        # E0f0f7b9b: onCreate then onCreateView (file_browser.xml).
        r.comment("FileBrowserFragment lifecycle: onCreateView",
                  edge="E0f0f7b9b")
        # E32f0941a: onCreateView then onResume.
        r.comment("FileBrowserFragment lifecycle: onResume",
                  edge="E32f0941a")
        # E15113078: onResume browses to the current/default directory.
        r.comment("onResume browses to the default root",
                  edge="E15113078")
        # Ee57bd8c9: browseTo lists the folder.
        r.comment("browseTo lists the folder", edge="Ee57bd8c9")
        # E14e26e11: fill passes the file list to the adapter.
        r.comment("fill passes the file list to the adapter",
                  edge="E14e26e11")
        # Ef51283a6: the recycler view binds the rows. Quiescence:
        # wait until the first-run sample db row is bound.
        r.wait_for(edge="Ef51283a6", text="french-body-parts.db")
        # E9ce1b9a0: long-press a file row: the first-run sample db
        # (AnyMemo.java first-run copy, .db filter match, default root).
        r.long_tap(edge="E9ce1b9a0", text="french-body-parts.db")
        # E87b66810: the row is a file (not "." or ".."), so the
        # long-press shows the edit dialog (title "Edit",
        # strings.xml fb_edit_dialog_title) with Delete/Clone/Rename.
        r.comment("file row long-press shows the edit dialog",
                  edge="E87b66810")
        # E628b5323: tap Delete / Clone / Rename; which == 2 is Rename
        # (array.xml fb_dialog_list, strings.xml rename_text).
        r.tap(edge="E628b5323", text="Rename")
        # E1424ae0a: which == 2 calls showRenameDbDialog(clickedFile).
        r.comment("which == 2 calls showRenameDbDialog(clickedFile)",
                  edge="E1424ae0a")
        # E55eb30b6: the Maybe subscribe shows the rename dialog.
        # Quiescence: wait for its message text (strings.xml
        # fb_rename_message) before cancelling it.
        r.wait_for(edge="E55eb30b6", text="Please enter the name below.")
        # E75658ab7: the rename dialog has no Cancel button (only a
        # positive OK button plus the cancel listener), so BACK
        # cancels it and the framework calls $4$1.onCancel (target).
        r.back(edge="E75658ab7")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
