#!/usr/bin/env python3
"""Replay script for hash-checker route_06.

Method: FNV1a.update256(byte[],int,int)
Edge ids (exact, from ROUTES.csv, in route order):
    E372472a8 E3101d0cd Edeb6bd90 E56501d6f E9e141121 E3755babd
    E9574aba4 E3ac2e1c9 E59c1e403 E79b435a7 Ee69c0c42 Ed943ca35
    E8c979876 Eff786918 E12829a50 Ef6dc9320 Eb99504ff E1e4be207
    Ef5562ab9 Ec8413c27 E0dbeffc7 E915e31df E84eade87 E00a75033
    Ed6d6a6fb E65a8dee6 E633a9408 Eb80710c7 E46ce41c2 E3eab88cf
    Eff811d30
Printed route file:
    graphs/hash-checker/scratch/route_print/FNV1a.update256(byte[],int,int).txt
Permissions: (none)
Fixtures: Download/todo.txt (pushed to /sdcard/Download/todo.txt by run_app.sh)
Setup: any file as input (fixtures)

Flow: launch, tap From, pick "File", pick todo.txt in the system file
picker, choose the FNV-1a 256-bit type in the hash-type sheet (STATE
settings: the choice is stored in preference last_type_value and makes
FNV1a.update dispatch to update256), tap Action, tap Generate. The
generated hash runs through HashCalculatorTask into JdkHashCalculator
and FNV1a.update256.

Every action carries one of this route's edge ids (the harness raises
for any other id). Lifecycle / call / async edges with no user action
are recorded with runner.comment. The hash-type choice has no edge of
its own in this route, so it is folded into the E0dbeffc7 block (the
screen on which it happens, immediately before the Action sheet is
opened) and is marked STATE there, not presented as the E0dbeffc7
trigger itself.

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
        package=args.package, route="route_06",
        edge_ids=["E372472a8", "E3101d0cd", "Edeb6bd90", "E56501d6f",
                  "E9e141121", "E3755babd", "E9574aba4", "E3ac2e1c9",
                  "E59c1e403", "E79b435a7", "Ee69c0c42", "Ed943ca35",
                  "E8c979876", "Eff786918", "E12829a50", "Ef6dc9320",
                  "Eb99504ff", "E1e4be207", "Ef5562ab9", "Ec8413c27",
                  "E0dbeffc7", "E915e31df", "E84eade87", "E00a75033",
                  "Ed6d6a6fb", "E65a8dee6", "E633a9408", "Eb80710c7",
                  "E46ce41c2", "E3eab88cf", "Eff811d30"],
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
        # Ee69c0c42: S_MAIN_EMPTY -> S_SHEET_SOURCE@EMPTY
        # Trigger: tap the "From" button; the source sheet opens.
        runner.tap("Ee69c0c42",
                   res_id=pkg + ":id/btn_generate_from")
        # Ed943ca35: S_SHEET_SOURCE@EMPTY -> BaseListHolder.lambda$bind$0@SRC_FILE
        # Trigger: tap the "File" row (Action.FILE, strings common_file).
        runner.tap("Ed943ca35", text="File")
        # E8c979876: BaseListHolder.lambda$bind$0@SRC_FILE
        #   -> ActionsListAdapter$ActionHolder.callItemClick@SRC_FILE
        # Call: the row tap invokes the holder click (BaseListHolder.java:44).
        runner.comment("call: ActionHolder.callItemClick (File row)", "E8c979876")
        # Eff786918: ActionsListAdapter$ActionHolder.callItemClick@SRC_FILE
        #   -> HashCalculatorFragment.userActionSelect@SRC_FILE
        # Call: ActionsListAdapter.java:55-58.
        runner.comment("call: userActionSelect SEARCH_FILE", "Eff786918")
        # E12829a50: HashCalculatorFragment.userActionSelect@SRC_FILE
        #   -> HashCalculatorFragment.openSystemFileManager
        # Call: SEARCH_FILE case (HashCalculatorFragment.java:166-189).
        runner.comment("call: openSystemFileManager", "E12829a50")
        # Ef6dc9320: HashCalculatorFragment.openSystemFileManager
        #   -> S_EXT_PICK_FILE
        # The action opens the system file picker (ACTION_OPEN_DOCUMENT).
        runner.comment("enters: system file picker", "Ef6dc9320")
        # Eb99504ff: S_EXT_PICK_FILE
        #   -> HashCalculatorFragment.onActivityResult@PICK_FILE
        # Trigger: in the system dialog, choose a document and confirm.
        # The pushed fixture is /sdcard/Download/todo.txt; pick it by name.
        runner.scroll_to("Eb99504ff", text="todo.txt")
        runner.tap("Eb99504ff", text="todo.txt")
        # E1e4be207: HashCalculatorFragment.onActivityResult@PICK_FILE
        #   -> HashCalculatorFragment.selectFileFromSystemFileManager
        # Call: FILE_SELECT + RESULT_OK (HashCalculatorFragment.java:587-604).
        runner.comment("call: selectFileFromSystemFileManager", "E1e4be207")
        # Ef5562ab9: HashCalculatorFragment.selectFileFromSystemFileManager
        #   -> HashCalculatorFragment.validateSelectedFile
        # Call: HashCalculatorFragment.java:609-612.
        runner.comment("call: validateSelectedFile", "Ef5562ab9")
        # Ec8413c27: HashCalculatorFragment.validateSelectedFile -> S_MAIN_FILE
        # File becomes the source; back on the calculator screen.
        runner.comment("enters: calculator screen with a file source",
                       "Ec8413c27")
        # E0dbeffc7: S_MAIN_FILE -> S_SHEET_ACTIONS@FILE
        # STATE (settings) first, folded here because no route edge covers
        # the hash-type sheet: tap the selected-hash-type view
        # (fragment_hash_calculator.xml tv_selected_hash_type), scroll to
        # and tap "FNV-1a-256" (HashConstants.FNV_1A_256). This stores the
        # choice in preference last_type_value, which the later edges need.
        runner.tap("E0dbeffc7",
                   res_id=pkg + ":id/tv_selected_hash_type")
        runner.scroll_to("E0dbeffc7", text="FNV-1a-256")
        runner.tap("E0dbeffc7", text="FNV-1a-256")
        # Trigger proper: tap the "Action" button; the actions sheet opens.
        runner.tap("E0dbeffc7",
                   res_id=pkg + ":id/btn_hash_actions")
        # E915e31df: S_SHEET_ACTIONS@FILE -> BaseListHolder.lambda$bind$0@GEN_FILE
        # Trigger: tap "Generate" (Action.GENERATE, strings action_generate).
        runner.tap("E915e31df", text="Generate")
        # E84eade87: BaseListHolder.lambda$bind$0@GEN_FILE
        #   -> ActionsListAdapter$ActionHolder.callItemClick@GEN_FILE
        # Call: the row tap invokes the holder click (BaseListHolder.java:44).
        runner.comment("call: ActionHolder.callItemClick (Generate row)",
                       "E84eade87")
        # E00a75033: ActionsListAdapter$ActionHolder.callItemClick@GEN_FILE
        #   -> HashCalculatorFragment.userActionSelect@GEN_FILE
        # Call: ActionsListAdapter.java:55-58.
        runner.comment("call: userActionSelect GENERATE_HASH", "E00a75033")
        # Ed6d6a6fb: HashCalculatorFragment.userActionSelect@GEN_FILE
        #   -> HashCalculatorFragment.generateHash@FILE
        # Call: GENERATE_HASH case (HashCalculatorFragment.java:166-189).
        runner.comment("call: generateHash with file source", "Ed6d6a6fb")
        # E65a8dee6: HashCalculatorFragment.generateHash@FILE
        #   -> HashCalculatorTask.doInBackground@FILE
        # Async: execute() runs doInBackground; guard fileUri != null holds
        # (todo.txt was picked).
        runner.comment("async: HashCalculatorTask.doInBackground", "E65a8dee6")
        # E633a9408: HashCalculatorTask.doInBackground@FILE
        #   -> JdkHashCalculator.fromFile(Context,Uri)
        # Call: HashCalculatorTask.java:70-76.
        runner.comment("call: JdkHashCalculator.fromFile(Context,Uri)",
                       "E633a9408")
        # Eb80710c7: JdkHashCalculator.fromFile(Context,Uri)
        #   -> JdkHashCalculator.fromFile(InputStream)
        # Call: JdkHashCalculator.java:54-55.
        runner.comment("call: JdkHashCalculator.fromFile(InputStream)",
                       "Eb80710c7")
        # E46ce41c2: JdkHashCalculator.fromFile(InputStream)
        #   -> JdkHashCalculatorDigest.update(byte[],int)@FNV
        # Call: JdkHashCalculator.java:46,72,106; needs the FNV-1a choice
        # made in the STATE step of the E0dbeffc7 block above.
        runner.comment("call: JdkHashCalculatorDigest.update @FNV", "E46ce41c2")
        # E3eab88cf: JdkHashCalculatorDigest.update(byte[],int)@FNV
        #   -> FNV1a.update(byte[],int,int)
        # Call: JdkHashCalculatorDigest.java:98-99.
        runner.comment("call: FNV1a.update", "E3eab88cf")
        # Eff811d30: FNV1a.update(byte[],int,int)
        #   -> FNV1a.update256(byte[],int,int)  [TARGET]
        # Call: FNV1a.java:107; guard this.type equals FNV_1A_256 holds
        # because the FNV-1a-256 type was chosen in the STATE step above.
        runner.comment("target: FNV1a.update256", "Eff811d30")
    finally:
        runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
