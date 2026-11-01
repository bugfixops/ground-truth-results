#!/usr/bin/env python3
"""AnyMemo route_22: CardDaoImpl$1.call.

Method: CardDaoImpl$1.call
Edge ids in order (from device/routes/AnyMemo/ROUTES.csv):
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E690f7694 E6da90567 E41662266
    Eb655c6eb E705abaec Eee3d301b E3ae14c6f Ea1b5c440 E22318784
    E2d07d42a E42afebab E539b41d9 E05e70ac4 Ede1d5ab9 E5cf2c281
    Ea4753c40 E0277b455 Eba96c17f E47cc197a E2842de5d E6cb11b56
    Ea82b0c59 E07a3fc1a
Printed route:
    graphs/AnyMemo/scratch/route_print/CardDaoImpl_1.call.txt
Permissions (ROUTES.csv): android.permission.WRITE_EXTERNAL_STORAGE.
    Pre-granted by run_app.sh before this script runs; this script
    never grants permissions.
Fixtures (ROUTES.csv): none.
Setup: none beyond the standard configuration. run_app.sh starts
    from pm clear. First launch auto-creates the state this route
    needs: AnyMemo prepareFirstTimeRun copies the asset
    french-body-parts.db (28 cards) into the app root and copies
    empty.db into the app files dir, and registers the sample deck
    as recent path 0.

Route-shape note (read this before a real run): the static route
runs the merger from the Misc tab and then continues into
PreviewEditActivity through its onActivityResult, but a
Misc-started DatabaseMerger returns its result to AnyMemo, not to
PreviewEditActivity. The PreviewEdit starter path is the
menu_context_merge_db item inside PreviewEditActivity itself.
So after the merge blocks, this script re-enters PreviewEdit
through the Recent list (row "more" button, then "Preview/edit"),
which is the screen the delete tail needs, and then performs the
delete tail for real. The merge itself is still performed exactly
as the route prescribes, with two distinct paths picked through
the Merge UI (see route_21.py for the same picker sequence):
target = <files dir>/empty.db, source = <app root>/
french-body-parts.db. Deleting a card mutates the sample deck,
but run_app.sh clears the app before every route, so each route
starts from the fresh first-run copy.

Selector notes (all read from source, none invented):
  - Bottom-navigation items are tapped by content-desc (see
    route_20.py for why). Titles come from
    res/menu/main_tab_items.xml and res/values/strings.xml.
  - Misc rows are res/layout/misc_tab.xml (misc_merge).
  - Merge fields/buttons are merge_layout.xml.
  - The Recent row "more" button is recent_item_more_button in
    res/layout/open_screen_recent_item.xml (text "MORE"); the
    OpenActions dialog item is edit in
    res/layout/open_actions_layout.xml (text "Preview/edit").
  - The PreviewEdit delete item is editmenu_delete_id in
    res/menu/preview_edit_activity_menu.xml (title "Delete",
    showAsAction ifRoom). It is tapped by content-desc: an
    action-bar icon carries the title as its description. If the
    emulator's toolbar room pushes it into the overflow instead,
    that tap must become an overflow tap on the text "Delete"
    (see REPORT.md); the script uses the icon form.
  - The delete confirm dialog buttons are "Yes" / "No"
    (yes_text / no_text).
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
    "E539b41d9", "E05e70ac4", "Ede1d5ab9", "E5cf2c281", "Ea4753c40",
    "E0277b455", "Eba96c17f", "E47cc197a", "E2842de5d", "E6cb11b56",
    "Ea82b0c59", "E07a3fc1a",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnyMemo route_22")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_22", EDGE_IDS, args.log,
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
    # paths through the Merge UI pickers (same sequence as
    # route_21.py: target empty.db in the files dir, source
    # french-body-parts.db in the app root).
    r.tap("E42afebab", res_id="target_db_edit")
    r.tap("E42afebab", text="..")
    r.tap("E42afebab", text="empty.db")
    r.tap("E42afebab", res_id="source_db_edit")
    r.tap("E42afebab", text="anymemo")
    r.tap("E42afebab", text="french-body-parts.db")
    # E539b41d9 onClick -> DatabaseMerger$1.doHeavyTask: v ==
    # mergeButton runs the merge on a background task.
    r.tap("E539b41d9", res_id="merge_button")
    # E05e70ac4 $1.doHeavyTask -> $1.doUITask: doProgressTask runs
    # doHeavyTask on a background thread, then posts doUITask.
    r.comment("merge task posts its UI task", "E05e70ac4")
    # Ede1d5ab9 $1.doUITask -> PreviewEditActivity.onActivityResult:
    # RESULT edge. In a real run a Misc-started merger returns to
    # AnyMemo, not to PreviewEditActivity, so this result edge does
    # not fire from this starter; see the re-entry in the next block.
    r.comment("merge UI task sets RESULT_OK and finishes (see note)",
              "Ede1d5ab9")
    # E5cf2c281 onActivityResult -> S_PREVIEW_EDIT: restart for
    # every non-CANCELED result. Real-run re-entry instead: the
    # merger finished back to AnyMemo, so open PreviewEdit through
    # the Recent list (more button, then Preview/edit) on the
    # sample deck. The deck has 28 cards, so the current card is
    # non-null and the delete tail below can run.
    r.comment("re-enter PreviewEdit through the Recent list",
              "E5cf2c281")
    r.tap("E5cf2c281", desc="Recent")
    r.wait_for("E5cf2c281", res_id="recent_item_more_button")
    r.tap("E5cf2c281", res_id="recent_item_more_button")
    r.tap("E5cf2c281", res_id="edit")
    # Ea4753c40 S_PREVIEW_EDIT -> PreviewEditActivity
    # .onOptionsItemSelected: tap the Delete menu item.
    r.tap("Ea4753c40", desc="Delete")
    # E0277b455 onOptionsItemSelected -> deleteCard:
    # editmenu_delete_id deletes the current card.
    r.comment("delete menu item deletes the current card", "E0277b455")
    # Eba96c17f deleteCard -> S_DLG_DELETE_CARD_PREVIEW: the
    # confirm dialog is shown.
    r.comment("delete confirm dialog shown", "Eba96c17f")
    # E47cc197a S_DLG_DELETE_CARD_PREVIEW -> PreviewEditActivity$6
    # .onClick: tap Yes (confirm delete).
    r.tap("E47cc197a", text="Yes")
    # E2842de5d $6.onClick -> DeleteCardTask.doInBackground: the
    # confirmed click executes the delete task.
    r.comment("confirmed delete executes DeleteCardTask", "E2842de5d")
    # E6cb11b56 doInBackground -> CardDaoImpl.queryNextCard: the
    # task queries the next card before deleting the current one.
    r.comment("delete task queries the next card", "E6cb11b56")
    # Ea82b0c59 queryNextCard -> queryFirstOrdinal: direct call.
    r.comment("queryNextCard calls queryFirstOrdinal", "Ea82b0c59")
    # E07a3fc1a queryFirstOrdinal -> CardDaoImpl$1.call: the
    # callable runs (it returns the first card, or null when the
    # deck is empty; the sample deck has 28 cards). Target edge.
    r.comment("queryFirstOrdinal runs CardDaoImpl$1.call (target)",
              "E07a3fc1a")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
