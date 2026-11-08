#!/usr/bin/env python3
"""AnyMemo route_18: SettingsScreen$12.onFileBrowserFileClick.

Method: SettingsScreen$12.onFileBrowserFileClick
Edge ids in order (from device/routes/AnyMemo/ROUTES.csv):
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E690f7694 E6da90567 E41662266
    Eb655c6eb E705abaec Eee3d301b E3ae14c6f E980e9e1b Ededb1a3c
    E7c955a83 E0fbe1f41 Eb0ac90c3 Efa212a15 Ee664f697 E27af0a92
    Ebcbee8f7 E4b710228 E883d7935 E1add7be1 E3004d681 E8b6dc7ad
    E786a4b47 E601dca0e E2ff07714
Printed route:
    graphs/AnyMemo/scratch/route_print/SettingsScreen_12.onFileBrowserFileClick.txt
Permissions (ROUTES.csv): android.permission.WRITE_EXTERNAL_STORAGE.
    Pre-granted by run_app.sh before this script runs; this script
    never grants permissions.
Fixtures (ROUTES.csv): Download/sample_deck.apkg (retained; it is
    NOT what this route's picker lists and does not satisfy this
    route) and
    Android/data/org.liberty.android.fantastischmemo/files/anymemo/DejaVuSans.ttf,
    which run_app.sh pushes to
    /sdcard/Android/data/org.liberty.android.fantastischmemo/files/anymemo/DejaVuSans.ttf
    — exactly the picker root (getExternalFilesDir(null) +
    "/anymemo/", AMEnv.java:49-50), where the answer-typeface picker
    filters ".ttf" (SettingsScreen.java:723-731). The .ttf row is the
    row this script taps; see the fixture note below.
Setup: none beyond the standard configuration. run_app.sh starts
    from pm clear. First launch auto-creates state: AnyMemo
    prepareFirstTimeRun copies the asset french-body-parts.db into
    the app root and copies empty.db into the app files dir, and
    registers the sample deck as recent path 0. This script opens
    SettingsScreen for the empty db through Misc / "DB default
    settings", exactly as the route prescribes.

Fixture note: TTF_ROW_TEXT below names the .ttf fixture ROUTES.csv
    lists at the picker-root path above (the adapter strips the
    leading "/" when it displays a row, so the row text is the bare
    filename "DejaVuSans.ttf"). PROVISIONING CONDITION (not a script
    defect): the .ttf file itself must be provisioned into the
    fixture store at that path before any real run; until it is,
    this script passes drycheck but cannot complete a real run past
    the picker (the tap then finds no row, and the DEVICE row reads
    unclear, never wrong). The fixture landing is a device-lead/D9
    provisioning item, not something this script creates.

Selector notes (all read from source, none invented):
  - Bottom-navigation items are tapped by content-desc: the item
    views carry the menu title as their description, while the
    label text of an unselected item is hidden in AUTO label mode
    with four items. Titles come from res/menu/main_tab_items.xml
    and res/values/strings.xml ("Misc").
  - Misc rows are the LinearLayouts res/layout/misc_tab.xml
    (misc_default_settings, text "DB default settings").
  - The answer-typeface checkbox/edit are
    checkbox_typeface_answer / edit_typeface_answer
    (SettingsScreen.java:324-331). The edit starts GONE for the
    empty db (its answerFont is empty), so the script taps the
    checkbox first to make it visible, then taps the edit.
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
    "E6da90567", "E41662266", "Eb655c6eb", "E705abaec", "Eee3d301b",
    "E3ae14c6f", "E980e9e1b", "Ededb1a3c", "E7c955a83", "E0fbe1f41",
    "Eb0ac90c3", "Efa212a15", "Ee664f697", "E27af0a92", "Ebcbee8f7",
    "E4b710228", "E883d7935", "E1add7be1", "E3004d681", "E8b6dc7ad",
    "E786a4b47", "E601dca0e", "E2ff07714",
]

# Bare filename of the provisioned .ttf fixture (ROUTES.csv lists it
# at the picker-root path; see module docstring). The picker shows
# this row once the fixture is provisioned into the fixture store.
TTF_ROW_TEXT = "DejaVuSans.ttf"


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnyMemo route_18")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_18", EDGE_IDS, args.log,
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
    # tap the Misc bottom-navigation item.
    r.tap("E6da90567", desc="Misc")
    # E41662266 onNavigationItemSelected -> MiscTabFragment.<init>:
    # itemId == misc_tab_menu.
    r.comment("Misc tab fragment created", "E41662266")
    # Eb655c6eb MiscTabFragment.<init> -> onAttach: lifecycle.
    r.comment("fragment onAttach", "Eb655c6eb")
    # E705abaec onAttach -> onCreate: lifecycle.
    r.comment("fragment onCreate", "E705abaec")
    # Eee3d301b onCreate -> onCreateView: lifecycle.
    r.comment("fragment onCreateView", "Eee3d301b")
    # E3ae14c6f onCreateView -> MiscTabFragment.onClick: tap the
    # "DB default settings" row (misc_default_settings).
    r.scroll_to("E3ae14c6f", res_id="misc_default_settings")
    r.tap("E3ae14c6f", res_id="misc_default_settings")
    # E980e9e1b onClick -> SettingsScreen.<init>: v ==
    # defaultSettingsButton starts SettingsScreen for the empty db.
    r.comment("default-settings button starts SettingsScreen (empty db)",
              "E980e9e1b")
    # Ededb1a3c SettingsScreen.<init> -> onCreate: lifecycle.
    r.comment("SettingsScreen onCreate", "Ededb1a3c")
    # E7c955a83 onCreate -> SettingLoaderCallbacks.onCreateLoader:
    # the Setting loader is registered in onCreate.
    r.comment("Setting loader registered", "E7c955a83")
    # E0fbe1f41 onCreateLoader -> onLoadFinished: loader delivers.
    r.comment("Setting loader delivers the Setting", "E0fbe1f41")
    # Eb0ac90c3 onLoadFinished -> SettingsScreen$6.run: posted
    # runnable runs after the loader reports.
    r.comment("posted runnable runs", "Eb0ac90c3")
    # Efa212a15 $6.run -> updateViews: setContentView + updateViews.
    r.comment("post-init runnable sets content view and updates views",
              "Efa212a15")
    # Ee664f697 updateViews -> SettingsScreen$10.onClick: tap the
    # answer-typeface checkbox (makes the edit visible; it starts
    # GONE because the empty db has no answer font), then tap the
    # answer-typeface edit itself.
    r.wait_for("Ee664f697", res_id="checkbox_typeface_answer")
    r.tap("Ee664f697", res_id="checkbox_typeface_answer")
    r.tap("Ee664f697", res_id="edit_typeface_answer")
    # E27af0a92 $10.onClick -> FileBrowserFragment.onCreate@SETTINGS_A:
    # v == aTypefaceEdit shows the ".ttf" picker dialog.
    r.comment("answer-typeface edit shows the ttf picker dialog",
              "E27af0a92")
    # Ebcbee8f7 picker onCreate@SETTINGS_A -> onCreateView: lifecycle.
    r.comment("picker onCreateView", "Ebcbee8f7")
    # E4b710228 onCreateView -> onResume: lifecycle.
    r.comment("picker onResume", "E4b710228")
    # E883d7935 onResume -> browseTo: onResume browses to the app
    # root directory.
    r.comment("picker onResume browses to the app root", "E883d7935")
    # E1add7be1 browseTo -> fill: browseTo lists the folder.
    r.comment("browseTo lists the folder", "E1add7be1")
    # E3004d681 fill -> FileBrowserAdapter.setItems: fill passes the
    # file list to the adapter.
    r.comment("fill passes the file list to the adapter", "E3004d681")
    # E8b6dc7ad setItems -> onBindViewHolder: recycler binds rows.
    r.comment("recycler view binds the rows", "E8b6dc7ad")
    # E786a4b47 onBindViewHolder -> FileBrowserAdapter$1.onClick:
    # tap the provisioned .ttf file row (TTF_ROW_TEXT, see module
    # docstring; the row appears once the fixture is provisioned).
    r.tap("E786a4b47", text=TTF_ROW_TEXT)
    # E601dca0e $1.onClick -> openFile: fragment.openFile(row).
    r.comment("row click calls openFile", "E601dca0e")
    # E2ff07714 openFile -> SettingsScreen$12.onFileBrowserFileClick:
    # the listener sets the answer-typeface text. Target edge.
    r.comment("file click reaches the answer-typeface listener (target)",
              "E2ff07714")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
