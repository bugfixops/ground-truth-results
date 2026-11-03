#!/usr/bin/env python3
"""AnyMemo route_20: FileBrowserFragment.upOneLevel.

Method: FileBrowserFragment.upOneLevel
Edge ids in order (from device/routes/AnyMemo/ROUTES.csv):
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E690f7694 E6da90567 E526c5ca4
    E920eb93a Ec85bff66 E0ce63c74 E872f8d1d E871ded0d E1cfe984d
    E35cc7df1 E8f4762c2 E9f627f96 E3918323c E5cbe5d62
Printed route:
    graphs/AnyMemo/scratch/route_print/FileBrowserFragment.upOneLevel.txt
Permissions (ROUTES.csv): android.permission.WRITE_EXTERNAL_STORAGE.
    Pre-granted by run_app.sh before this script runs; this script
    never grants permissions.
Fixtures (ROUTES.csv): Download/sample_deck.apkg, pre-pushed by
    run_app.sh to /sdcard/Download/sample_deck.apkg. That fixture is
    NOT what this route's browser lists: the Open-tab browser
    filters ".db" (the default when no extension argument is given)
    in the app root, so the .apkg file can never appear as a row.
    The listing gate is satisfied without it: first launch
    auto-copies french-body-parts.db into the app root
    (AnyMemo.prepareFirstTimeRun), and the ".." row is always bound
    whenever the browsed folder has a parent.
Setup: none beyond the standard configuration. run_app.sh starts
    from pm clear.

Selector notes (all read from source, none invented):
  - Bottom-navigation items are tapped by content-desc: the item
    views carry the menu title as their description, while the
    label text of an unselected item is hidden in AUTO label mode
    with four items. Titles come from res/menu/main_tab_items.xml
    and res/values/strings.xml ("Open").
  - The file-browser menu items have no showAsAction, so they are
    overflow items: open the overflow ("More options", the AOSP
    overflow description) and tap "Go to home folder"
    (fb_go_home), the one item whose handler calls browseTo
    directly (FileBrowserFragment.onOptionsItemSelected).
  - The ".." row text is the literal UP_ONE_LEVEL_DIR constant
    ("..") in FileBrowserFragment; tapping it calls
    openFile(".."), which calls upOneLevel().
  - The "What's new" dialog on first launch (versionCode 241
    versus the saved default 1) is dismissed with its "OK"
    button (ok_text) before any navigation tap.
"""

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = None
_parent = _HERE
for _ in range(8):
    if os.path.isfile(os.path.join(_parent, "device", "harness",
                                   "harness.py")):
        _ROOT = _parent
        break
    _next = os.path.dirname(_parent)
    if _next == _parent:
        break
    _parent = _next
if _ROOT is None:
    raise RuntimeError(
        "could not locate device/harness under any ancestor of this "
        "script; copy the script to device/routes/AnyMemo/ first")
sys.path.insert(0, _ROOT)

from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "Eddc920eb", "Ee33f0797", "E0b0115b9", "Ed9aa2280", "Efe6c7871",
    "E006becde", "E48c9d4a5", "Ef4267162", "E25e1518b", "E690f7694",
    "E6da90567", "E526c5ca4", "E920eb93a", "Ec85bff66", "E0ce63c74",
    "E872f8d1d", "E871ded0d", "E1cfe984d", "E35cc7df1", "E8f4762c2",
    "E9f627f96", "E3918323c", "E5cbe5d62",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnyMemo route_20")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_20", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # Eddc920eb S_ENTRY -> AnyMemo.<init>: MAIN / LAUNCHER intent.
    r.launch(args.package + "/org.liberty.android.fantastischmemo.ui.AnyMemo",
             "Eddc920eb")
    # Ee33f0797 AnyMemo.<init> -> AnyMemo.onCreate: lifecycle.
    r.comment("system instantiates AnyMemo, then onCreate", "Ee33f0797")
    # E0b0115b9 AnyMemo.onCreate -> AnyMemo.loadUiComponents: the
    # first-launch "What's new" dialog (prepareFirstTimeRun) covers
    # the screen; dismiss it with OK before navigating.
    r.wait_for("E0b0115b9", text="OK", timeout=30)
    r.tap("E0b0115b9", text="OK")
    # Ed9aa2280 loadUiComponents -> initDrawer: direct call.
    r.comment("loadUiComponents calls initDrawer", "Ed9aa2280")
    # Efe6c7871 initDrawer -> AnyMemo$2.onNavigationItemSelected@INIT:
    # setSelectedItemId(recent_tab_menu) selects Recent by default.
    r.comment("bottom nav selects Recent by default", "Efe6c7871")
    # E006becde @INIT -> RecentListFragment.<init>: direct call.
    r.comment("Recent tab fragment created", "E006becde")
    # E48c9d4a5 RecentListFragment.<init> -> onAttach: lifecycle.
    r.comment("fragment onAttach", "E48c9d4a5")
    # Ef4267162 onAttach -> onCreate: lifecycle.
    r.comment("fragment onCreate", "Ef4267162")
    # E25e1518b onCreate -> onCreateView: lifecycle.
    r.comment("fragment onCreateView", "E25e1518b")
    # E690f7694 onCreateView -> S_MAIN_RECENT: Recent tab shown.
    r.comment("Recent tab shown", "E690f7694")
    # E6da90567 S_MAIN_RECENT -> AnyMemo$2.onNavigationItemSelected:
    # tap the Open bottom-navigation item.
    r.tap("E6da90567", desc="Open")
    # E526c5ca4 onNavigationItemSelected -> OpenTabFragment.<init>:
    # itemId == open_tab_menu.
    r.comment("Open tab fragment created", "E526c5ca4")
    # E920eb93a OpenTabFragment.<init> -> onAttach: constructor then
    # onAttach (sets the file-click listener).
    r.comment("Open tab onAttach sets the file-click listener",
              "E920eb93a")
    # Ec85bff66 onAttach -> FileBrowserFragment.onCreate@OPEN:
    # onAttach then onCreate of the Open-tab file browser.
    r.comment("Open-tab file browser onCreate", "Ec85bff66")
    # E0ce63c74 onCreate -> onCreateOptionsMenu: the options menu,
    # reached from this host after its onCreate.
    r.comment("file browser options menu created", "E0ce63c74")
    # E872f8d1d onCreateOptionsMenu -> onOptionsItemSelected: open
    # the overflow menu and tap "Go to home folder".
    r.tap("E872f8d1d", desc="More options")
    r.tap("E872f8d1d", text="Go to home folder")
    # E871ded0d onOptionsItemSelected -> browseTo: the go-home item
    # browses to the app root directory.
    r.comment("go-home item browses to the app root", "E871ded0d")
    # E1cfe984d browseTo -> fill: browseTo lists the folder.
    r.comment("browseTo lists the folder", "E1cfe984d")
    # E35cc7df1 fill -> FileBrowserAdapter.setItems: fill passes the
    # file list to the adapter.
    r.comment("fill passes the file list to the adapter", "E35cc7df1")
    # E8f4762c2 setItems -> onBindViewHolder: setItems calls
    # notifyDataSetChanged and the recycler binds the rows. The
    # rows are ".." plus french-body-parts.db (first-run sample).
    r.comment("recycler view binds the rows", "E8f4762c2")
    # E9f627f96 onBindViewHolder -> FileBrowserAdapter$1.onClick:
    # tap the ".." row.
    r.tap("E9f627f96", text="..")
    # E3918323c $1.onClick -> openFile: fragment.openFile("..").
    r.comment('row click calls openFile("..")', "E3918323c")
    # E5cbe5d62 openFile -> upOneLevel: the ".." row calls
    # upOneLevel(). Target edge.
    r.comment('openFile("..") calls upOneLevel (target)', "E5cbe5d62")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
