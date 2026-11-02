#!/usr/bin/env python3
"""Replay script for hash-checker route_08.

Method: JdkHashCalculator.inputStreamsFormFolder
Edge ids (exact, from ROUTES.csv, in route order):
    E372472a8 E3101d0cd Edeb6bd90 E56501d6f E9e141121 E3755babd
    E9574aba4 E3ac2e1c9 E59c1e403 E79b435a7 Ee69c0c42 E2c58a33d
    E4b06b3e0 Ed95ead38 E93d7aec9 E14efb922 E799c45d6 E1f654e2a
    E4d8290b8 E5c1d025b Ed4256db3 E7a8b44b5 E87941bc5 E248aefe7
    E2dfb21aa E6cdff816 Ed3b616aa Eb0b91e7b
Printed route file:
    graphs/hash-checker/scratch/route_print/JdkHashCalculator.inputStreamsFormFolder.txt
Permissions: (none)
Fixtures: Pictures (a directory, pushed to /sdcard/Pictures by run_app.sh;
    it contains photo_1.jpg .. photo_6.jpg)
Setup: any file as input (fixtures)

Flow: launch, tap From, pick "Folder", pick the Pictures folder itself
in the system folder picker (ACTION_OPEN_DOCUMENT_TREE), tap Action,
tap Generate. The folder hash runs through HashCalculatorTask into
JdkHashCalculator.fromFolder and inputStreamsFormFolder.

Folder-picker sequence: tapping the "Pictures" row enters that folder,
and "Use this folder" then confirms Pictures itself as the tree root
returned to the app. The "Allow" tap is conditional: some picker builds
show a permission-grant dialog after "Use this folder" and some do
not, so it is wrapped so a missing dialog does not fail the script
(in dry-run mode the tap is planned, never raised).

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
        package=args.package, route="route_08",
        edge_ids=["E372472a8", "E3101d0cd", "Edeb6bd90", "E56501d6f",
                  "E9e141121", "E3755babd", "E9574aba4", "E3ac2e1c9",
                  "E59c1e403", "E79b435a7", "Ee69c0c42", "E2c58a33d",
                  "E4b06b3e0", "Ed95ead38", "E93d7aec9", "E14efb922",
                  "E799c45d6", "E1f654e2a", "E4d8290b8", "E5c1d025b",
                  "Ed4256db3", "E7a8b44b5", "E87941bc5", "E248aefe7",
                  "E2dfb21aa", "E6cdff816", "Ed3b616aa", "Eb0b91e7b"],
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
        # E2c58a33d: S_SHEET_SOURCE@EMPTY -> BaseListHolder.lambda$bind$0@SRC_FOLDER
        # Trigger: tap the "Folder" row (Action.FOLDER, strings common_folder).
        runner.tap("E2c58a33d", text="Folder")
        # E4b06b3e0: BaseListHolder.lambda$bind$0@SRC_FOLDER
        #   -> ActionsListAdapter$ActionHolder.callItemClick@SRC_FOLDER
        # Call: the row tap invokes the holder click (BaseListHolder.java:44).
        runner.comment("call: ActionHolder.callItemClick (Folder row)",
                       "E4b06b3e0")
        # Ed95ead38: ActionsListAdapter$ActionHolder.callItemClick@SRC_FOLDER
        #   -> HashCalculatorFragment.userActionSelect@SRC_FOLDER
        # Call: ActionsListAdapter.java:55-58.
        runner.comment("call: userActionSelect SEARCH_FOLDER", "Ed95ead38")
        # E93d7aec9: HashCalculatorFragment.userActionSelect@SRC_FOLDER
        #   -> HashCalculatorFragment.openSystemFolderManager
        # Call: SEARCH_FOLDER case (HashCalculatorFragment.java:166-189).
        runner.comment("call: openSystemFolderManager", "E93d7aec9")
        # E14efb922: HashCalculatorFragment.openSystemFolderManager
        #   -> S_EXT_PICK_FOLDER
        # The action opens the system folder picker (ACTION_OPEN_DOCUMENT_TREE).
        runner.comment("enters: system folder picker", "E14efb922")
        # E799c45d6: S_EXT_PICK_FOLDER
        #   -> HashCalculatorFragment.onActivityResult@PICK_FOLDER
        # Trigger: in the system dialog, choose a document and confirm.
        # Pick the Pictures folder itself: scroll to it, tap its row to
        # enter it, then "Use this folder" confirms Pictures as the tree
        # root. A following "Allow" grant dialog, when shown, is confirmed.
        runner.scroll_to("E799c45d6", text="Pictures")
        runner.tap("E799c45d6", text="Pictures")
        runner.wait_for("E799c45d6", text="Use this folder")
        runner.tap("E799c45d6", text="Use this folder")
        try:
            runner.tap("E799c45d6", text="Allow")
        except LookupError:
            # No grant dialog on this picker build; nothing to confirm.
            pass
        # E1f654e2a: HashCalculatorFragment.onActivityResult@PICK_FOLDER
        #   -> HashCalculatorFragment.selectFolderFromSystemFileManager
        # Call: FOLDER_SELECT + RESULT_OK (HashCalculatorFragment.java:587-604).
        runner.comment("call: selectFolderFromSystemFileManager", "E1f654e2a")
        # E4d8290b8: HashCalculatorFragment.selectFolderFromSystemFileManager
        #   -> HashCalculatorFragment.validateSelectedFolder
        # Call: HashCalculatorFragment.java:614-617.
        runner.comment("call: validateSelectedFolder", "E4d8290b8")
        # E5c1d025b: HashCalculatorFragment.validateSelectedFolder
        #   -> S_MAIN_FOLDER
        # Folder becomes the source; back on the calculator screen.
        runner.wait_for("E5c1d025b",
                        res_id=pkg + ":id/btn_hash_actions")
        # Ed4256db3: S_MAIN_FOLDER -> S_SHEET_ACTIONS@FOLDER
        # Trigger: tap the "Action" button; the actions sheet opens.
        runner.tap("Ed4256db3",
                   res_id=pkg + ":id/btn_hash_actions")
        # E7a8b44b5: S_SHEET_ACTIONS@FOLDER
        #   -> BaseListHolder.lambda$bind$0@GEN_FOLDER
        # Trigger: tap "Generate" (Action.GENERATE, strings action_generate).
        runner.tap("E7a8b44b5", text="Generate")
        # E87941bc5: BaseListHolder.lambda$bind$0@GEN_FOLDER
        #   -> ActionsListAdapter$ActionHolder.callItemClick@GEN_FOLDER
        # Call: the row tap invokes the holder click (BaseListHolder.java:44).
        runner.comment("call: ActionHolder.callItemClick (Generate row)",
                       "E87941bc5")
        # E248aefe7: ActionsListAdapter$ActionHolder.callItemClick@GEN_FOLDER
        #   -> HashCalculatorFragment.userActionSelect@GEN_FOLDER
        # Call: ActionsListAdapter.java:55-58.
        runner.comment("call: userActionSelect GENERATE_HASH", "E248aefe7")
        # E2dfb21aa: HashCalculatorFragment.userActionSelect@GEN_FOLDER
        #   -> HashCalculatorFragment.generateHash@FOLDER
        # Call: GENERATE_HASH case (HashCalculatorFragment.java:166-189).
        runner.comment("call: generateHash with folder source", "E2dfb21aa")
        # E6cdff816: HashCalculatorFragment.generateHash@FOLDER
        #   -> HashCalculatorTask.doInBackground@FOLDER
        # Async: execute() runs doInBackground; guard folderUri != null
        # (else branch) holds (Pictures was picked).
        runner.comment("async: HashCalculatorTask.doInBackground", "E6cdff816")
        # Ed3b616aa: HashCalculatorTask.doInBackground@FOLDER
        #   -> JdkHashCalculator.fromFolder(Context,Uri)
        # Call: HashCalculatorTask.java:70-76.
        runner.comment("call: JdkHashCalculator.fromFolder", "Ed3b616aa")
        # Eb0b91e7b: JdkHashCalculator.fromFolder(Context,Uri)
        #   -> JdkHashCalculator.inputStreamsFormFolder  [TARGET]
        # Call: JdkHashCalculator.java:87.
        runner.comment("target: JdkHashCalculator.inputStreamsFormFolder",
                       "Eb0b91e7b")
    finally:
        runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
