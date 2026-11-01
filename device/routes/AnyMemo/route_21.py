#!/usr/bin/env python3
"""AnyMemo route_21: Card.setCreationDate.

Method: Card.setCreationDate
Edge ids in order (from device/routes/AnyMemo/ROUTES.csv):
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E690f7694 E6da90567 E41662266
    Eb655c6eb E705abaec Eee3d301b E3ae14c6f Ea1b5c440 E22318784
    E2d07d42a E42afebab E539b41d9 E1f915012 E17765f04 E86d28cd3
    E99db9aec Ef139c57e Eca154fff Ec2fa9ffc Eac59faad
Printed route:
    graphs/AnyMemo/scratch/route_print/Card.setCreationDate.txt
Permissions (ROUTES.csv): android.permission.WRITE_EXTERNAL_STORAGE.
    Pre-granted by run_app.sh before this script runs; this script
    never grants permissions.
Fixtures (ROUTES.csv): none.
Setup: none beyond the standard configuration. run_app.sh starts
    from pm clear. First launch auto-creates the state this route
    needs: AnyMemo prepareFirstTimeRun copies the asset
    french-body-parts.db (28 cards) into the app root and copies
    empty.db (0 cards, valid schema) into the app files dir.

How the two distinct merge paths are obtained (through the Merge
UI itself, no fixture, no typed path):
  - Tap the target field: the FileBrowserActivity picker opens at
    the app root (no saved browser path exists on a fresh run).
    Tap ".." to go up to the app files dir, then tap "empty.db".
    Target = <files dir>/empty.db.
  - Tap the source field: the picker now opens at the app files
    dir, because openFile saved the target's parent as the browser
    path (FileBrowserFragment.openFile). Tap the "anymemo"
    directory row, then tap "french-body-parts.db".
    Source = <app root>/french-body-parts.db (28 cards).
  - Target != source, so mergeDatabases does not throw; it copies
    the 28 source cards into the target, and every copied card goes
    through CardDaoImpl.create -> AbstractHelperDaoImpl.create,
    which calls setCreationDate (Card is a VersionableDomainObject).
    An empty source would copy nothing, which is why the sample
    deck (not the empty db) must be the source.

Selector notes (all read from source, none invented):
  - Bottom-navigation items are tapped by content-desc (see
    route_20.py for why: unselected labels are hidden in AUTO
    label mode with four items). Titles come from
    res/menu/main_tab_items.xml and res/values/strings.xml ("Misc").
  - Misc rows are the LinearLayouts res/layout/misc_tab.xml
    (misc_merge, text "Merge DB").
  - Merge fields/buttons are merge_layout.xml: target_db_edit,
    source_db_edit, merge_button.
  - File-browser row display texts are the adapter's display
    names: the leading "/" is stripped, and directory rows lose
    their trailing "/", so the rows are "..", "empty.db",
    "anymemo", "french-body-parts.db".
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
    "E3ae14c6f", "Ea1b5c440", "E22318784", "E2d07d42a", "E42afebab",
    "E539b41d9", "E1f915012", "E17765f04", "E86d28cd3", "E99db9aec",
    "Ef139c57e", "Eca154fff", "Ec2fa9ffc", "Eac59faad",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnyMemo route_21")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_21", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # Eddc920eb S_ENTRY -> AnyMemo.<init>: MAIN / LAUNCHER intent.
    r.launch(args.package + "/org.liberty.android.fantastischmemopro.ui.AnyMemo",
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
    # "Merge DB" row (misc_merge).
    r.scroll_to("E3ae14c6f", res_id="misc_merge")
    r.tap("E3ae14c6f", res_id="misc_merge")
    # Ea1b5c440 onClick -> DatabaseMerger.<init>: v == mergeButton
    # starts DatabaseMerger.
    r.comment("merge button starts DatabaseMerger", "Ea1b5c440")
    # E22318784 DatabaseMerger.<init> -> onCreate: lifecycle.
    r.comment("DatabaseMerger onCreate", "E22318784")
    # E2d07d42a onCreate -> S_DB_MERGER: setContentView(merge_layout).
    r.comment("merger shows merge_layout", "E2d07d42a")
    # E42afebab S_DB_MERGER -> DatabaseMerger.onClick: pick the two
    # paths through the Merge UI pickers (see module docstring).
    # Target: tap the target field, go up one level from the app
    # root, and tap empty.db (app files dir).
    r.tap("E42afebab", res_id="target_db_edit")
    r.tap("E42afebab", text="..")
    r.tap("E42afebab", text="empty.db")
    # Source: tap the source field (picker reopens at the files
    # dir, the saved browser path), enter the anymemo directory,
    # and tap french-body-parts.db (28 cards).
    r.tap("E42afebab", res_id="source_db_edit")
    r.tap("E42afebab", text="anymemo")
    r.tap("E42afebab", text="french-body-parts.db")
    # E539b41d9 onClick -> DatabaseMerger$1.doHeavyTask: v ==
    # mergeButton runs the merge on a background task.
    r.tap("E539b41d9", res_id="merge_button")
    # E1f915012 $1.doHeavyTask -> DatabaseUtil.mergeDatabases:
    # direct call; target != source so no self-merge exception.
    r.comment("merge task calls mergeDatabases", "E1f915012")
    # E17765f04 mergeDatabases -> CardDaoImpl.createCards: the
    # destination dao creates the copied source cards.
    r.comment("mergeDatabases creates the copied cards", "E17765f04")
    # E86d28cd3 createCards -> AbstractHelperDaoImpl.callBatchTasks:
    # direct call.
    r.comment("createCards runs a batch task", "E86d28cd3")
    # E99db9aec callBatchTasks -> CardDaoImpl$2.call: the ORMLite
    # batch runner invokes call(), which runs createCardsNoBatch.
    r.comment("batch runner invokes CardDaoImpl$2.call", "E99db9aec")
    # Ef139c57e $2.call -> createCardsNoBatch: direct call.
    r.comment("batch call runs createCardsNoBatch", "Ef139c57e")
    # Eca154fff createCardsNoBatch -> create: one create per copied
    # card (28 source cards).
    r.comment("createCardsNoBatch creates each copied card",
              "Eca154fff")
    # Ec2fa9ffc create -> AbstractHelperDaoImpl.create@CARD:
    # super.create(c) inserts the card row.
    r.comment("card row inserted via super.create", "Ec2fa9ffc")
    # Eac59faad create@CARD -> Card.setCreationDate: the card is a
    # VersionableDomainObject, so create stamps it. Target edge.
    r.comment("create stamps setCreationDate on the card (target)",
              "Eac59faad")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
