#!/usr/bin/env python3
"""AnyMemo route_23: SpeakWord.stripNonCardContent.

Method: SpeakWord.stripNonCardContent
Edge ids (in route order):
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E690f7694 E6da90567 E41662266
    Eb655c6eb E705abaec Eee3d301b E3ae14c6f Ea1b5c440 E22318784
    E2d07d42a E42afebab E539b41d9 E05e70ac4 Ede1d5ab9 E5cf2c281
    Ea4753c40 Eaa32ac34 Ed9fc0e2d E48e72fac Ee07c506d Ea4306967
    E4634e0cf E7392b1e1
Printed route file:
    graphs/AnyMemo/scratch/route_print/SpeakWord.stripNonCardContent.txt
    (32 edges, verdict REACHABLE).
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (ROUTES.csv;
    granted by run_app.sh before this script runs, so this script
    performs no permission grants itself).
Fixtures: none (ROUTES.csv fixtures cell is empty), so this script
    pushes no fixtures itself.
Setup: run_app.sh runs this script after pm clear (fresh install).
    First launch auto-creates deck state: AnyMemo.prepareFirstTimeRun
    (ui/AnyMemo.java:315-321) copies the bundled sample database
    french-body-parts.db (AMEnv.DEFAULT_DB_NAME) into the app root and
    records it as recent path 0, so the Recent tab lists a database
    with cards and no fixture or manual deck creation is needed.
    PreviewEditActivity.onPostInit falls back to the first-ordinal
    card when no card id is given, so a card is open in Preview/Edit
    once that activity is reached.

UI facts used (read from layout XML / strings.xml, never invented):
- Bottom-navigation menu (res/menu/main_tab_items.xml) item
  misc_tab_menu has title "Misc" (strings.xml misc_tab_text); the
  bottom-nav item is tapped by that exact text.
- Misc tab row res/layout/misc_tab.xml id misc_merge, text
  "Merge DB" (strings.xml merge_db_text); MiscTabFragment binds it
  as mergeButton and starts DatabaseMerger on tap.
- Database Merger layout res/layout/merge_layout.xml button
  merge_button, text "Merge DB"; DatabaseMerger binds it as
  mergeButton and runs the merge progress task on tap.
- Preview/Edit menu res/menu/preview_edit_activity_menu.xml item
  menuspeakquestion, title "Speak question" (strings.xml
  speak_question_menu_text); PreviewEditActivity.onOptionsItemSelected
  calls speakQuestion() for it when getCurrentCard() != null.

Real-run caveat (see REPORT.md): the printed chain splices two
DatabaseMerger launch sites. Steps up to the merger follow the
Misc-tab launch, but the return edge into
PreviewEditActivity.onActivityResult only fires when the merger was
started from PreviewEdit itself (menu_context_merge_db,
ACTIVITY_MERGE). A Misc-launched merger returns to AnyMemo, not to
PreviewEdit, and its target/source fields start empty, so a merge
that returns RESULT_OK needs two different existing databases.
In practice the speak segment is reached from a Preview/Edit
session: Recent tab -> MORE -> Edit on the sample database opens
PreviewEdit with a card, and its overflow menu holds
"Speak question". This script follows the printed edges in order;
the merger-return splice is flagged for the merger, not hidden.
"""

import argparse
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

try:
    from device.harness.harness import Runner
except ImportError:  # test-root fallback: load harness.py by path
    _HARNESS = None
    _here = os.path.abspath(__file__)
    _dir = os.path.dirname(_here)
    for _i in range(6):
        _cand = os.path.join(_dir, "device", "harness", "harness.py")
        if os.path.isfile(_cand):
            _HARNESS = _cand
            break
        _dir = os.path.dirname(_dir)
    if _HARNESS is None:
        raise
    _spec = importlib.util.spec_from_file_location("anymemo_harness",
                                                   _HARNESS)
    _mod = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)
    Runner = _mod.Runner

EDGE_IDS = [
    "Eddc920eb", "Ee33f0797", "E0b0115b9", "Ed9aa2280", "Efe6c7871",
    "E006becde", "E48c9d4a5", "Ef4267162", "E25e1518b", "E690f7694",
    "E6da90567", "E41662266", "Eb655c6eb", "E705abaec", "Eee3d301b",
    "E3ae14c6f", "Ea1b5c440", "E22318784", "E2d07d42a", "E42afebab",
    "E539b41d9", "E05e70ac4", "Ede1d5ab9", "E5cf2c281", "Ea4753c40",
    "Eaa32ac34", "Ed9fc0e2d", "E48e72fac", "Ee07c506d", "Ea4306967",
    "E4634e0cf", "E7392b1e1",
]

COMPONENT = "org.liberty.android.fantastischmemopro.ui.AnyMemo"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_23", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # Eddc920eb: MAIN / LAUNCHER intent starts AnyMemo.
        r.launch(args.package + "/" + COMPONENT, edge="Eddc920eb")
        # Ee33f0797: Activity lifecycle / framework callback.
        r.comment("system instantiates AnyMemo, then calls onCreate",
                  edge="Ee33f0797")
        # E0b0115b9: onCreate: API <= 29 and WRITE_EXTERNAL_STORAGE
        # already granted (granted by run_app.sh).
        r.comment("onCreate loads UI components (permission granted)",
                  edge="E0b0115b9")
        # Ed9aa2280: initDrawer().
        r.comment("loadUiComponents calls initDrawer", edge="Ed9aa2280")
        # Efe6c7871: bottomNavigation.setSelectedItemId(recent_tab_menu):
        # the library calls the bottom-nav listener for the Recent item,
        # so the Recent tab is selected by default on a cold start.
        r.comment("cold start selects the Recent tab",
                  edge="Efe6c7871")
        # E006becde: Direct call, itemId == recent_tab_menu.
        r.comment("navigation listener creates RecentListFragment",
                  edge="E006becde")
        # E48c9d4a5: Fragment lifecycle callback.
        r.comment("RecentListFragment onAttach", edge="E48c9d4a5")
        # Ef4267162: Fragment lifecycle callback.
        r.comment("RecentListFragment onCreate", edge="Ef4267162")
        # E25e1518b: Fragment lifecycle callback.
        r.comment("RecentListFragment onCreateView", edge="E25e1518b")
        # E690f7694: the Recent tab is shown once its view exists
        # (cold start selects it). The first-run sample database is
        # listed here.
        r.comment("Recent tab shown with the sample database",
                  edge="E690f7694")
        # E6da90567: Tap a bottom-navigation item (Recent / Open /
        # Download / Misc) -- here the Misc item, title "Misc".
        r.tap(edge="E6da90567", text="Misc")
        # E41662266: itemId == misc_tab_menu: new MiscTabFragment().
        r.comment("navigation listener creates MiscTabFragment",
                  edge="E41662266")
        # Eb655c6eb: constructor then onAttach.
        r.comment("MiscTabFragment onAttach", edge="Eb655c6eb")
        # E705abaec: onAttach then onCreate.
        r.comment("MiscTabFragment onCreate", edge="E705abaec")
        # Eee3d301b: onCreate then onCreateView.
        r.comment("MiscTabFragment onCreateView", edge="Eee3d301b")
        # E3ae14c6f: Tap a button on the Misc tab -- the Merge DB row
        # (misc_tab.xml id misc_merge, text "Merge DB").
        r.tap(edge="E3ae14c6f", res_id="misc_merge")
        # Ea1b5c440: v == mergeButton: starts DatabaseMerger.
        r.comment("MiscTabFragment onClick starts DatabaseMerger",
                  edge="Ea1b5c440")
        # E22318784: Activity lifecycle callback.
        r.comment("DatabaseMerger onCreate", edge="E22318784")
        # E2d07d42a: setContentView(merge_layout).
        r.comment("DatabaseMerger shows merge_layout",
                  edge="E2d07d42a")
        # E42afebab: Tap a field or button in Database Merger -- the
        # Merge button (merge_layout.xml id merge_button).
        r.tap(edge="E42afebab", res_id="merge_button")
        # E539b41d9: v == mergeButton: AMGUIUtility.doProgressTask,
        # its task.doHeavyTask() call.
        r.comment("merge button runs doProgressTask doHeavyTask",
                  edge="E539b41d9")
        # E05e70ac4: doProgressTask runs doHeavyTask() on a background
        # Thread, then posts doUITask() to the main thread.
        r.comment("doHeavyTask finishes, doUITask posted to main thread",
                  edge="E05e70ac4")
        # Ede1d5ab9: setResult(RESULT_OK); finish(): the Preview/Edit
        # starter gets its result (menu_context_merge_db). See the
        # header caveat: this return only reaches Preview/Edit when
        # the merger was started from Preview/Edit.
        r.comment("merger sets RESULT_OK and finishes",
                  edge="Ede1d5ab9")
        # E5cf2c281: restartActivity() for every request code except
        # RESULT_CANCELED -- Preview/Edit is shown with a card open.
        r.comment("Preview/Edit restarts with a card open",
                  edge="E5cf2c281")
        # Ea4753c40: Tap a menu item in Preview/Edit -- "Speak
        # question" (menu id menuspeakquestion).
        r.tap(edge="Ea4753c40", text="Speak question")
        # Eaa32ac34: menuspeakquestion, getCurrentCard() != null.
        r.comment("Preview/Edit menu calls QACardActivity.speakQuestion",
                  edge="Eaa32ac34")
        # Ed9fc0e2d: Direct call.
        r.comment("speakQuestion calls CardTTSUtil.speakCardQuestion",
                  edge="Ed9fc0e2d")
        # E48e72fac: Direct call.
        r.comment("speakCardQuestion(Card) calls the 2-arg overload",
                  edge="E48e72fac")
        # Ee07c506d: Virtual/interface call dispatching to this
        # implementation.
        r.comment("speakCardQuestion calls AnyMemoTTSImpl.sayText",
                  edge="Ee07c506d")
        # Ea4306967: speakWord.speakWord(s) is tried first (a stored
        # audio tag in the text).
        r.comment("sayText calls SpeakWord.speakWord", edge="Ea4306967")
        # E4634e0cf: Direct call.
        r.comment("speakWord calls SpeakWord.searchAlternatives",
                  edge="E4634e0cf")
        # E7392b1e1: Direct call -- TARGET
        # SpeakWord.stripNonCardContent reached.
        r.comment("searchAlternatives calls SpeakWord.stripNonCardContent "
                  "(target edge)", edge="E7392b1e1")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
