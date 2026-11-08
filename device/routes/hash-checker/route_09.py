#!/usr/bin/env python3
"""Replay script for hash-checker route_09.

Method: HistoryFragment.refreshHistory
Edge ids (exact, from ROUTES.csv, in route order):
    E372472a8 E3101d0cd Edeb6bd90 E56501d6f E9e141121 E3755babd
    E9574aba4 E3ac2e1c9 E59c1e403 E79b435a7 E6c2f63a0 E7a1243ec
    E773e4c35 E1c5e958c Eaed75b00 Eb0aab7d5 E0a09ed58 E6dc05866
    E05ed2414 E2060174b E14d43b8a E4a52e049 Eef21d111 Ea16c95cd
    Ef6d9ada5 E0864fd57 E8fda859d E13cfe3ed
Printed route file:
    graphs/hash-checker/scratch/route_print/HistoryFragment.refreshHistory.txt
Permissions: (none)
Fixtures: (none)
Setup: any file as input (fixtures)

Flow: launch, then the STATE (data) gate, then the route proper: tap
the History action-bar item, and once history rows are shown tap the
trash item and confirm OK in the "Delete all history items?" dialog;
clearHistory calls refreshHistory.

STATE (data) gate, produced in-app with no fixture: the route needs at
least one history row (HistoryPresenterImpl.postLoad -> setLoaded@ROWS
and the trash item is hidden when the list is empty). run_app.sh clears the app before the script, so history starts empty. The gate is made
by generating one hash from text: From -> "Text" -> type "hash-checker"
-> Add -> Action -> Generate. Saving to history is on by default
(settings key_save_result_to_history, default true), and the first
generation on a cleared app does not pop the rate-app dialog (it only
shows when the generation count equals 5). No route edge covers this
preparation, so it is folded into the E79b435a7 block (the calculator
screen on which it happens, before the History item is tapped) and is
marked STATE there, not presented as the E79b435a7 trigger itself.

The History action-bar item is a trap worth noting: in menu_main.xml
its title reuses menu_title_feedback, so its visible title /
content-desc is literally "Feedback" even though MainActivity routes
that item id to HistoryFragment. It is tapped by desc "Feedback" with
a resource-id fallback. The trash item on the History screen
(menu_history.xml menu_item_clean_history) likewise reuses the
"Feedback" title; on that screen it is the only action item.

Every action carries one of this route's edge ids (the harness raises
for any other id). Lifecycle / call / async edges with no user action
are recorded with runner.comment.

Activity assumption: the manifest package is
com.smlnskgmail.jaman.hashchecker and .MainActivity is the activity
class under the flavor applicationId passed as --package.
"""

import argparse
import os
import sys

# Repo root is 3 levels up from this script's directory
# (device/routes/hash-checker/): hash-checker -> routes -> device -> root.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness.harness import Runner  # noqa: E402


def tap_menu(runner, edge, desc, res_id):
    """Tap an icon-only action-bar item by content-desc, else by id."""
    try:
        runner.tap(edge, desc=desc)
    except LookupError:
        runner.tap(edge, res_id=res_id)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    pkg = args.package
    runner = Runner(
        package=args.package, route="route_09",
        edge_ids=["E372472a8", "E3101d0cd", "Edeb6bd90", "E56501d6f",
                  "E9e141121", "E3755babd", "E9574aba4", "E3ac2e1c9",
                  "E59c1e403", "E79b435a7", "E6c2f63a0", "E7a1243ec",
                  "E773e4c35", "E1c5e958c", "Eaed75b00", "Eb0aab7d5",
                  "E0a09ed58", "E6dc05866", "E05ed2414", "E2060174b",
                  "E14d43b8a", "E4a52e049", "Eef21d111", "Ea16c95cd",
                  "Ef6d9ada5", "E0864fd57", "E8fda859d", "E13cfe3ed"],
        log_path=args.log, dry_run=args.dry_run, adb=args.adb)
    try:
        # E372472a8: S_ENTRY -> MainActivity.<init>
        # Trigger: tap the launcher icon (MAIN + LAUNCHER intent filter).
        runner.launch(pkg + "/com.smlnskgmail.jaman.hashchecker.MainActivity",
                      "E372472a8")
        # E3101d0cd: MainActivity.<init> -> MainActivity.onCreate
        # Lifecycle: the system instantiates MainActivity, then onCreate.
        runner.comment("lifecycle: MainActivity.onCreate", "E3101d0cd")
        # Edeb6bd90: MainActivity.onCreate -> BaseActivity.onCreate@MainActivity
        # Call: super.onCreate(savedInstanceState) (MainActivity.java:52).
        runner.comment("call: super.onCreate", "Edeb6bd90")
        # E56501d6f: BaseActivity.onCreate@MainActivity -> MainActivity.create
        # Call: BaseActivity.onCreate calls create() (BaseActivity.java:19).
        runner.comment("call: MainActivity.create", "E56501d6f")
        # E9e141121: MainActivity.create -> MainActivity.showFragment@CALC
        # Call: showFragment(mainFragment) (MainActivity.java:93).
        runner.comment("call: showFragment HashCalculatorFragment", "E9e141121")
        # E3755babd: MainActivity.showFragment@CALC
        #   -> HashCalculatorFragment.onAttach
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: HashCalculatorFragment.onAttach", "E3755babd")
        # E9574aba4: HashCalculatorFragment.onAttach
        #   -> BaseFragment.onCreateView@HashCalculatorFragment
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: BaseFragment.onCreateView", "E9574aba4")
        # E3ac2e1c9: BaseFragment.onCreateView@HashCalculatorFragment
        #   -> HashCalculatorFragment.onViewCreated
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: HashCalculatorFragment.onViewCreated",
                       "E3ac2e1c9")
        # E59c1e403: HashCalculatorFragment.onViewCreated
        #   -> BaseFragment.onResume@HashCalculatorFragment
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: BaseFragment.onResume", "E59c1e403")
        # E79b435a7: BaseFragment.onResume@HashCalculatorFragment -> S_MAIN_EMPTY
        # The fragment is visible: the empty calculator screen.
        runner.comment("enters: calculator screen, no source yet", "E79b435a7")
        # STATE (data), folded here: generate one hash from text so that
        # at least one history row exists. From -> "Text"
        # (dialog_text_input.xml, title "Add text") -> type text -> "Add"
        # -> Action sheet -> "Generate". The hash task callback saves the
        # row because save-to-history defaults on.
        runner.tap("E79b435a7",
                   res_id=pkg + ":id/btn_generate_from")
        runner.tap("E79b435a7", text="Text")
        runner.tap("E79b435a7",
                   res_id=pkg + ":id/et_dialog_input_text")
        runner.type_text("hash-checker", "E79b435a7")
        runner.tap("E79b435a7",
                   res_id=pkg + ":id/btn_dialog_input_text_add")
        runner.tap("E79b435a7",
                   res_id=pkg + ":id/btn_hash_actions")
        runner.tap("E79b435a7", text="Generate")
        # E6c2f63a0: S_MAIN_EMPTY -> MainActivity.onOptionsItemSelected@HISTORY
        # Trigger: tap the History icon in the action bar
        # (menu_main.xml menu_main_section_history; its title reuses
        # menu_title_feedback, so the item's text/desc is "Feedback").
        tap_menu(runner, "E6c2f63a0", "Feedback",
                 pkg + ":id/menu_main_section_history")
        # E7a1243ec: MainActivity.onOptionsItemSelected@HISTORY
        #   -> MainActivity.showFragment@HISTORY
        # Call: MainActivity.java:133.
        runner.comment("call: showFragment HistoryFragment", "E7a1243ec")
        # E773e4c35: MainActivity.showFragment@HISTORY -> HistoryFragment.onAttach
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: HistoryFragment.onAttach", "E773e4c35")
        # E1c5e958c: HistoryFragment.onAttach
        #   -> BaseFragment.onCreateView@HistoryFragment
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: BaseFragment.onCreateView (History)",
                       "E1c5e958c")
        # Eaed75b00: BaseFragment.onCreateView@HistoryFragment
        #   -> HistoryFragment.onViewCreated
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: HistoryFragment.onViewCreated", "Eaed75b00")
        # Eb0aab7d5: HistoryFragment.onViewCreated -> HistoryPresenterImpl.init
        # Call: HistoryFragment.java:79 (bytecode).
        runner.comment("call: HistoryPresenterImpl.init", "Eb0aab7d5")
        # E0a09ed58: HistoryPresenterImpl.init -> HistoryPresenterImpl.load
        # Call: HistoryPresenterImpl.java:26 (bytecode).
        runner.comment("call: HistoryPresenterImpl.load", "E0a09ed58")
        # E6dc05866: HistoryPresenterImpl.load
        #   -> HistoryItemsLoaderTask.doInBackground
        # Async: guard "portion not complete" holds on first load.
        runner.comment("async: HistoryItemsLoaderTask.doInBackground",
                       "E6dc05866")
        # E05ed2414: HistoryItemsLoaderTask.doInBackground
        #   -> HistoryItemsLoaderTask.onPostExecute
        # Async: postResult on the main looper calls finish/onPostExecute.
        runner.comment("async: HistoryItemsLoaderTask.onPostExecute",
                       "E05ed2414")
        # E2060174b: HistoryItemsLoaderTask.onPostExecute
        #   -> HistoryItemsLoaderTask.completeLoad
        # Call: HistoryItemsLoaderTask.java:34 (bytecode).
        runner.comment("call: HistoryItemsLoaderTask.completeLoad", "E2060174b")
        # E14d43b8a: HistoryItemsLoaderTask.completeLoad
        #   -> HistoryPresenterImpl.postLoad
        # Call: HistoryItemsLoaderTask.java:41 (bytecode).
        runner.comment("call: HistoryPresenterImpl.postLoad", "E14d43b8a")
        # E4a52e049: HistoryPresenterImpl.postLoad -> HistoryFragment.setLoaded@ROWS
        # Call: HistoryPresenterImpl.java:50-53; guard "at least one
        # history row" holds because of the STATE text hash above.
        runner.comment("call: HistoryFragment.setLoaded with rows", "E4a52e049")
        # Eef21d111: HistoryFragment.setLoaded@ROWS -> S_HISTORY_LIST
        # Rows shown (HistoryFragment.java:117-126).
        runner.comment("enters: history list with rows", "Eef21d111")
        # Ea16c95cd: S_HISTORY_LIST -> HistoryFragment.onOptionsItemSelected@TRASH
        # Trigger: tap the trash icon in the action bar
        # (menu_history.xml menu_item_clean_history, icon ic_delete; its
        # title also reuses menu_title_feedback, i.e. "Feedback").
        tap_menu(runner, "Ea16c95cd", "Feedback",
                 pkg + ":id/menu_item_clean_history")
        # Ef6d9ada5: HistoryFragment.onOptionsItemSelected@TRASH
        #   -> S_DLG_CLEAR_HISTORY
        # Confirmation dialog (HistoryFragment.java:93-104).
        runner.wait_for("Ef6d9ada5", text="Delete all history items?")
        # E0864fd57: S_DLG_CLEAR_HISTORY
        #   -> HistoryFragment.lambda$onOptionsItemSelected$0
        # Trigger: tap "OK" (strings common_ok; HistoryFragment.java:98-101).
        runner.tap("E0864fd57", text="OK")
        # E8fda859d: HistoryFragment.lambda$onOptionsItemSelected$0
        #   -> HistoryPresenterImpl.clearHistory
        # Call: HistoryFragment.java:99 (bytecode).
        runner.comment("call: HistoryPresenterImpl.clearHistory", "E8fda859d")
        # E13cfe3ed: HistoryPresenterImpl.clearHistory
        #   -> HistoryFragment.refreshHistory  [TARGET]
        # Call: HistoryPresenterImpl.java:46 (bytecode).
        runner.comment("target: HistoryFragment.refreshHistory", "E13cfe3ed")
    finally:
        runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
