#!/usr/bin/env python3
"""Replay script for hash-checker route_01.

Method: HistoryItem.<init>()
Edge ids (exact, in order, from ROUTES.csv):
    E372472a8 E3101d0cd Edeb6bd90 E56501d6f E9e141121 E3755babd
    E9574aba4 E3ac2e1c9 E59c1e403 E79b435a7 E6c2f63a0 E7a1243ec
    E773e4c35 E1c5e958c Eaed75b00 Eb0aab7d5 E0a09ed58 E6dc05866
    E1523e6d2 E3ef2bf11
Printed route:
    graphs/hash-checker/scratch/route_print/HistoryItem.<init>().txt
Permissions: none (ROUTES.csv permissions cell is empty).
Fixtures: none (ROUTES.csv fixtures cell is empty).
Setup: any file as input (fixtures).

STATE note (data): HistoryItem.<init>() fires only when the history
database holds at least one row, because ORMLite constructs one
HistoryItem per stored row (final edge E3ef2bf11). run_app.sh clears
the app before this script, so the script first generates a hash from
text on the calculator screen: saving the result to history is the
default (SharedPreferencesSettings.canSaveResultToHistory defaults to
true), so that generation inserts exactly the row the History screen
then loads. All preamble taps are logged under E79b435a7, the edge
that enters the calculator's main-empty state where they happen.
The preamble waits for the generated MD5 of the text "hash-checker"
(4807007b03b99a1332b94ddabb08f57f, lowercase hex as produced by
JdkHashUtils) so the script does not open History before the row
exists. No pm clear, fixture push, or permission grant happens here;
run_app.sh owns those steps.
"""

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, _ROOT)

from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E372472a8", "E3101d0cd", "Edeb6bd90", "E56501d6f", "E9e141121",
    "E3755babd", "E9574aba4", "E3ac2e1c9", "E59c1e403", "E79b435a7",
    "E6c2f63a0", "E7a1243ec", "E773e4c35", "E1c5e958c", "Eaed75b00",
    "Eb0aab7d5", "E0a09ed58", "E6dc05866", "E1523e6d2", "E3ef2bf11",
]

# MD5 (lowercase hex) of the preamble text "hash-checker", the value the
# generated-hash field shows once the preamble generation completes.
PREAMBLE_MD5 = "4807007b03b99a1332b94ddabb08f57f"


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    pkg = args.package
    runner = Runner(package=args.package, route="route_01",
                    edge_ids=EDGE_IDS, log_path=args.log,
                    dry_run=args.dry_run, adb=args.adb)

    # E372472a8: S_ENTRY -> MainActivity.<init>
    # Trigger: tap the launcher icon (MAIN + LAUNCHER intent filter).
    runner.launch(pkg + "/com.smlnskgmail.jaman.hashchecker.MainActivity",
                  "E372472a8")
    # E3101d0cd: MainActivity.<init> -> MainActivity.onCreate
    # Trigger: the system instantiates MainActivity, then calls onCreate.
    runner.comment("lifecycle: system calls MainActivity.onCreate",
                   "E3101d0cd")
    # Edeb6bd90: MainActivity.onCreate -> BaseActivity.onCreate@MainActivity
    # Trigger: direct call (super.onCreate).
    runner.comment("direct call: super.onCreate", "Edeb6bd90")
    # E56501d6f: BaseActivity.onCreate@MainActivity -> MainActivity.create
    # Trigger: direct call (BaseActivity calls create()).
    runner.comment("direct call: BaseActivity calls create()", "E56501d6f")
    # E9e141121: MainActivity.create -> MainActivity.showFragment@CALC
    # Trigger: showFragment(mainFragment) adds the calculator.
    runner.comment("showFragment(mainFragment) adds the calculator",
                   "E9e141121")
    # E3755babd: MainActivity.showFragment@CALC -> HashCalculatorFragment.onAttach
    # Trigger: FragmentTransaction.commit(); the fragment is attached.
    runner.comment("fragment transaction attaches HashCalculatorFragment",
                   "E3755babd")
    # E9574aba4: HashCalculatorFragment.onAttach -> BaseFragment.onCreateView
    # Trigger: onCreateView inflates the layout.
    runner.comment("lifecycle: onCreateView inflates the calculator layout",
                   "E9574aba4")
    # E3ac2e1c9: BaseFragment.onCreateView -> HashCalculatorFragment.onViewCreated
    # Trigger: onViewCreated.
    runner.comment("lifecycle: onViewCreated", "E3ac2e1c9")
    # E59c1e403: HashCalculatorFragment.onViewCreated -> BaseFragment.onResume
    # Trigger: onStart -> onResume.
    runner.comment("lifecycle: onStart -> onResume", "E59c1e403")
    # E79b435a7: BaseFragment.onResume -> S_MAIN_EMPTY
    # Trigger: the fragment is visible. Calculator "From" button is the
    # anchor that the main-empty screen is shown.
    runner.wait_for("E79b435a7",
                    res_id=pkg + ":id/btn_generate_from")
    # Preamble under E79b435a7 (still on the main-empty screen):
    # generate a hash from text so one history row exists. From button
    # (fragment_hash_calculator.xml btn_generate_from, text "From")
    # opens the source sheet; "Text" (Action.TEXT, common_text) opens
    # the text-input dialog; "Add" (dialog_text_input.xml
    # btn_dialog_input_text_add, common_add) submits the text; Action
    # button (btn_hash_actions, text "Action") opens the actions sheet;
    # "Generate" (Action.GENERATE, action_generate) runs the hash.
    runner.tap("E79b435a7", res_id=pkg + ":id/btn_generate_from")
    runner.tap("E79b435a7", text="Text")
    runner.tap("E79b435a7", res_id=pkg + ":id/et_dialog_input_text")
    runner.type_text("hash-checker", "E79b435a7")
    runner.tap("E79b435a7", res_id=pkg + ":id/btn_dialog_input_text_add")
    runner.tap("E79b435a7", res_id=pkg + ":id/btn_hash_actions")
    runner.tap("E79b435a7", text="Generate")
    runner.wait_for("E79b435a7", text=PREAMBLE_MD5, timeout=30)
    # E6c2f63a0: S_MAIN_EMPTY -> MainActivity.onOptionsItemSelected@HISTORY
    # Trigger: tap the History icon in the action bar
    # (R.id.menu_main_section_history). Note: that menu item's title
    # string is menu_title_feedback ("Feedback"); the res_id, not the
    # title, identifies it, so tap by res_id.
    runner.tap("E6c2f63a0", res_id=pkg + ":id/menu_main_section_history")
    # E7a1243ec: MainActivity.onOptionsItemSelected@HISTORY ->
    # MainActivity.showFragment@HISTORY. Trigger: showFragment(...).
    runner.comment("showFragment(new HistoryFragment())", "E7a1243ec")
    # E773e4c35: MainActivity.showFragment@HISTORY -> HistoryFragment.onAttach
    # Trigger: FragmentTransaction.commit(); the fragment is attached.
    runner.comment("fragment transaction attaches HistoryFragment",
                   "E773e4c35")
    # E1c5e958c: HistoryFragment.onAttach -> BaseFragment.onCreateView
    # Trigger: onCreateView inflates the layout.
    runner.comment("lifecycle: onCreateView inflates the history layout",
                   "E1c5e958c")
    # Eaed75b00: BaseFragment.onCreateView -> HistoryFragment.onViewCreated
    # Trigger: onViewCreated.
    runner.comment("lifecycle: onViewCreated", "Eaed75b00")
    # Eb0aab7d5: HistoryFragment.onViewCreated -> HistoryPresenterImpl.init
    # Trigger: virtual/interface call to this implementation.
    runner.comment("presenter init via interface dispatch", "Eb0aab7d5")
    # E0a09ed58: HistoryPresenterImpl.init -> HistoryPresenterImpl.load
    # Trigger: direct call.
    runner.comment("direct call: init calls load", "E0a09ed58")
    # E6dc05866: HistoryPresenterImpl.load -> HistoryItemsLoaderTask.doInBackground
    # Trigger: HistoryItemsLoaderTask.execute(); worker thread.
    runner.comment("async task execute: loader runs on a worker thread",
                   "E6dc05866")
    # E1523e6d2: HistoryItemsLoaderTask.doInBackground ->
    # OrmLiteLocalDataStorage.historyItems. Trigger: localDataStorage.historyItems(portion).
    runner.comment("loader reads stored history rows", "E1523e6d2")
    # E3ef2bf11: OrmLiteLocalDataStorage.historyItems -> HistoryItem.<init>()
    # Trigger: ORMLite builds each row object by reflection (no-arg
    # constructor). The history list (fragmant_history.xml
    # rv_history_items) is the completion anchor; row presence itself
    # is proven by the run's coverage comparison, not by this wait.
    runner.wait_for("E3ef2bf11", res_id=pkg + ":id/rv_history_items")
    runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
