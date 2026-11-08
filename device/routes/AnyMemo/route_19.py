#!/usr/bin/env python3
"""AnyMemo route_19: Option$DictApp.parse.

Method: Option$DictApp.parse
Edge ids in order (from device/routes/AnyMemo/ROUTES.csv):
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E690f7694 E6da90567 E41662266
    Eb655c6eb E705abaec Eee3d301b E3ae14c6f Ea1b5c440 E22318784
    E2d07d42a E42afebab E539b41d9 E05e70ac4 Ede1d5ab9 E5cf2c281
    Ea4753c40 Ec558d914 Ec64df922 Eb6abfe4f E5dadaabd E50b7563c
    Ee9403ef8 E84637f23 Eceee02ee E85d7e389 Ea85c6e81 Eb92c9568
    E4e9cad12
Printed route:
    graphs/AnyMemo/scratch/route_print/Option_DictApp.parse.txt
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

Dictionary-app question (answered from source, not assumed): the
lookup list does NOT require an installed third-party dictionary
app. DictionaryUtil.showLookupListDialog lists WORDS from the
current card (full question, full answer, then each word), not
dictionary apps. Tapping a word calls lookupDictionary(word),
which calls option.getDictApp() -- and getDictApp is exactly where
DictApp.parse runs (Option.java:61-62, default "COLORDICT"). Only
after parse returns does lookupDictionary fire the ColorDict
intent, which fails on an AOSP emulator with no ColorDict
installed and shows an error dialog. Parse has already executed
by then, so no dictionary app is needed for this route's target.
getDictApp has no other caller in the app, so the lookup chain is
the only way to reach parse.

Route-shape notes (read before a real run):
  1. Starter mismatch, same as route_22: a Misc-started
     DatabaseMerger returns to AnyMemo, not to PreviewEditActivity,
     so the route's PreviewEdit result/restart edges cannot fire
     from this starter. After the merge blocks, this script
     re-enters the study flow through the Recent list instead.
  2. Card-player mismatch: the route continues into
     CardPlayerActivity and then into StudyActivity
     .onGestureDetected, but CardPlayerActivity extends
     QACardActivity directly and does not override
     onGestureDetected, so a gesture in CardPlayerActivity would
     hit QACardActivity's no-op default, never StudyActivity's
     override. StudyActivity is the QACardActivity subclass that
     actually maps O_SHAPE to lookupDictionary, and it shares
     QACardActivity.startInit / loadGestures / the $8 listener
     with CardPlayerActivity. The script therefore enters
     StudyActivity directly from the Recent row (row tap starts
     StudyActivity) and performs the gesture tail there.
  3. Gestures default OFF (Option.getGestureEnabled defaults to
     false), so the gesture overlay ignores touches until gestures
     are enabled. The script enables them through StudyActivity's
     overflow "Gestures" dialog (enable_gestures checkbox) before
     the gesture step; dismissing that dialog restarts the
     activity with gestures enabled.
  4. The harness has no stroke API, so a real O-shape stroke
     (recognized with score > 3.0 by the gesture library) cannot
     be drawn by this script. The gesture step uses a long press
     on the gesture overlay as the closest available action; a
     press without movement is unlikely to score as an O-shape,
     so real-run reachability of the gesture tail is UNCERTAIN
     even with gestures enabled. Reliable fallback (not used
     here, because the route's edge is the gesture): StudyActivity
     menu_context_lookup ("Look up in a dictionary", ifRoom)
     calls the same lookupDictionary() directly. See REPORT.md.

Word tap: the script taps "head", the question of card 1
(ordinal 1) in the sample deck asset. This assumes StudyActivity
shows card 1 first (new cards in ordinal order); if it shows
another card, the word row differs but the chain is identical.

Selector notes (all read from source, none invented):
  - Bottom-navigation items are tapped by content-desc (see
    route_20.py for why). Titles come from
    res/menu/main_tab_items.xml and res/values/strings.xml.
  - Misc rows are res/layout/misc_tab.xml (misc_merge).
  - Merge fields/buttons are merge_layout.xml.
  - The StudyActivity "Gestures" item has no showAsAction, so it
    is an overflow item (text "Gestures", gestures_text); the
    dialog checkbox is enable_gestures (text "Enable gestures").
  - The gesture overlay view is gesture_overlay
    (QACardActivity.loadGestures).
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
    "Ec558d914", "Ec64df922", "Eb6abfe4f", "E5dadaabd", "E50b7563c",
    "Ee9403ef8", "E84637f23", "Eceee02ee", "E85d7e389", "Ea85c6e81",
    "Eb92c9568", "E4e9cad12",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnyMemo route_19")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_19", EDGE_IDS, args.log,
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
    # merger finished back to AnyMemo, so open the study flow
    # through the Recent list. A Recent row tap starts
    # StudyActivity directly (RecentListFragment item click), which
    # is the QACardActivity subclass whose onGestureDetected maps
    # O_SHAPE to lookupDictionary (see module docstring, note 2).
    r.comment("re-enter the study flow through the Recent list",
              "E5cf2c281")
    r.tap("E5cf2c281", desc="Recent")
    r.wait_for("E5cf2c281", text="french-body-parts.db")
    r.tap("E5cf2c281", text="french-body-parts.db")
    # Ea4753c40 S_PREVIEW_EDIT -> PreviewEditActivity
    # .onOptionsItemSelected: NO menu tap is performed here. The
    # route's PreviewEdit -> Card player step is substituted by
    # the StudyActivity entry above, because CardPlayerActivity
    # has no onGestureDetected override (see module docstring,
    # note 2). The menu tap is therefore logged as a comment, not
    # executed, so the script does not tap a menu that cannot lead
    # to the target.
    r.comment("PreviewEdit card-player menu step substituted by the "
              "StudyActivity entry above (see module docstring)",
              "Ea4753c40")
    # Ec558d914 onOptionsItemSelected -> CardPlayerActivity.<init>:
    # menu_card_player starts CardPlayerActivity in the static
    # route; in this script the equivalent QACardActivity entry is
    # the StudyActivity started from the Recent row.
    r.comment("card-player entry substituted by StudyActivity entry",
              "Ec558d914")
    # Ec64df922 CardPlayerActivity.<init> -> onCreate: lifecycle
    # (StudyActivity onCreate runs the same QACardActivity start).
    r.comment("study activity onCreate", "Ec64df922")
    # Eb6abfe4f onCreate -> QACardActivity.startInit: direct call.
    r.comment("QACardActivity.startInit", "Eb6abfe4f")
    # E5dadaabd startInit -> loadGestures: loadGestures() loads the
    # gesture library and attaches the $8 listener; the overlay
    # starts disabled (gestures default off), so enabling happens
    # in the next block before the gesture step.
    r.comment("loadGestures attaches the gesture listener (disabled "
              "by default)", "E5dadaabd")
    # E50b7563c loadGestures -> QACardActivity$8.onGesturePerformed:
    # first enable gestures (overflow "Gestures" dialog, check
    # "Enable gestures", back to dismiss; the dialog restart
    # re-runs startInit with the overlay enabled), then perform
    # the closest harness action to a gesture: a long press on
    # the gesture overlay. The harness has no stroke API, so a
    # real O-shape stroke scoring over 3.0 cannot be drawn here;
    # see module docstring, note 4.
    r.tap("E50b7563c", desc="More options")
    r.tap("E50b7563c", text="Gestures")
    r.tap("E50b7563c", res_id="enable_gestures")
    r.back("E50b7563c")
    r.long_tap("E50b7563c", res_id="gesture_overlay", duration_ms=1000)
    # Ee9403ef8 $8.onGesturePerformed -> StudyActivity
    # .onGestureDetected: virtual dispatch to the StudyActivity
    # override, reached only if a gesture scores over 3.0.
    r.comment("gesture listener dispatches to StudyActivity "
              "onGestureDetected", "Ee9403ef8")
    # E84637f23 onGestureDetected -> lookupDictionary: the O_SHAPE
    # branch calls lookupDictionary().
    r.comment("O_SHAPE branch calls lookupDictionary", "E84637f23")
    # Eceee02ee lookupDictionary -> showLookupListDialog: direct
    # call; the dialog lists words from the current card.
    r.comment("lookupDictionary shows the word list dialog",
              "Eceee02ee")
    # E85d7e389 showLookupListDialog -> DictionaryUtil$1.onItemClick:
    # tap a word row. "head" is card 1's question (and a listed
    # word); see the module docstring for the first-card
    # assumption.
    r.tap("E85d7e389", text="head")
    # Ea85c6e81 $1.onItemClick -> lookupDictionary: the dialog
    # dismisses and lookupDictionary(word) runs.
    r.comment("word click calls lookupDictionary(word)", "Ea85c6e81")
    # Eb92c9568 lookupDictionary -> Option.getDictApp: direct call.
    r.comment("lookupDictionary consults getDictApp", "Eb92c9568")
    # E4e9cad12 getDictApp -> Option$DictApp.parse: getDictApp
    # parses the stored preference (default COLORDICT). Target
    # edge. No dictionary app needs to be installed: parse runs
    # before the ColorDict intent, which then fails on AOSP with
    # an error dialog; the script stops here.
    r.comment("getDictApp parses the stored dict-app value (target)",
              "E4e9cad12")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
