#!/usr/bin/env python3
"""Device replay script for hash-checker route_14.

Method: Blake2B.update(byte[],int,int)
Edges: E372472a8 E3101d0cd Edeb6bd90 E56501d6f E9e141121 E3755babd
    E9574aba4 E3ac2e1c9 E59c1e403 E79b435a7 Ee69c0c42 Ed943ca35
    E8c979876 Eff786918 E12829a50 Ef6dc9320 Eb99504ff E1e4be207
    Ef5562ab9 Ec8413c27 E0dbeffc7 E915e31df E84eade87 E00a75033
    Ed6d6a6fb E65a8dee6 E633a9408 Eb80710c7 Ed7d0e9b9 E7be8a23b
Printed route: graphs/hash-checker/scratch/route_print/Blake2B.update(byte[],int,int).txt
Permissions: none
Fixtures: Download/todo.txt (pushed to /sdcard/Download/todo.txt by run_app.sh)
Setup: any file as input (fixtures)

Flow: launch the calculator, choose BLAKE2b in the hash-type sheet
(the STATE gate on the digest edges: the choice is stored in
preference last_type_value), pick todo.txt in the system file picker,
then generate the file hash, which runs through
JdkHashCalculatorDigest.update to Blake2B.update. The BLAKE2b choice
is executed early as STATE setup for gate edge Ed7d0e9b9 and is
commented again at that edge in route order. The activity class is
the manifest package (com.smlnskgmail.jaman.hashchecker) plus
.MainActivity, launched under the flavor applicationId passed as
--package.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner

EDGES = ["E372472a8", "E3101d0cd", "Edeb6bd90", "E56501d6f", "E9e141121",
         "E3755babd", "E9574aba4", "E3ac2e1c9", "E59c1e403", "E79b435a7",
         "Ee69c0c42", "Ed943ca35", "E8c979876", "Eff786918", "E12829a50",
         "Ef6dc9320", "Eb99504ff", "E1e4be207", "Ef5562ab9", "Ec8413c27",
         "E0dbeffc7", "E915e31df", "E84eade87", "E00a75033", "Ed6d6a6fb",
         "E65a8dee6", "E633a9408", "Eb80710c7", "Ed7d0e9b9", "E7be8a23b"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    args = ap.parse_args()
    pkg = args.package

    def rid(name):
        return pkg + ":id/" + name

    runner = Runner(package=args.package, route="route_14", edge_ids=EDGES,
                    log_path=args.log, dry_run=args.dry_run, adb=args.adb,
                    outdir=args.outdir)
    try:
        # E372472a8 S_ENTRY -> MainActivity.<init>
        # Trigger: tap the launcher icon (MAIN + LAUNCHER intent filter).
        runner.launch(pkg + "/com.smlnskgmail.jaman.hashchecker.MainActivity",
                      "E372472a8")
        # E3101d0cd MainActivity.<init> -> MainActivity.onCreate
        # Trigger: the system instantiates MainActivity, then calls onCreate.
        runner.comment("lifecycle: MainActivity.onCreate", "E3101d0cd")
        # Edeb6bd90 MainActivity.onCreate -> BaseActivity.onCreate@MainActivity
        # Trigger: direct call (super.onCreate).
        runner.comment("call: super.onCreate", "Edeb6bd90")
        # E56501d6f BaseActivity.onCreate@MainActivity -> MainActivity.create
        # Trigger: direct call (create()).
        runner.comment("call: create()", "E56501d6f")
        # E9e141121 MainActivity.create -> MainActivity.showFragment@CALC
        # Trigger: showFragment(mainFragment) adds the calculator.
        runner.comment("call: showFragment calculator fragment", "E9e141121")
        # E3755babd MainActivity.showFragment@CALC -> HashCalculatorFragment.onAttach
        # Trigger: FragmentTransaction.commit(), the fragment is attached.
        runner.comment("lifecycle: fragment attached", "E3755babd")
        # E9574aba4 HashCalculatorFragment.onAttach -> BaseFragment.onCreateView
        # Trigger: onCreateView inflates the layout.
        runner.comment("lifecycle: fragment view created", "E9574aba4")
        # E3ac2e1c9 BaseFragment.onCreateView -> HashCalculatorFragment.onViewCreated
        # Trigger: onViewCreated.
        runner.comment("lifecycle: fragment onViewCreated", "E3ac2e1c9")
        # E59c1e403 HashCalculatorFragment.onViewCreated -> BaseFragment.onResume
        # Trigger: onStart -> onResume.
        runner.comment("lifecycle: fragment resumed", "E59c1e403")
        # E79b435a7 BaseFragment.onResume -> S_MAIN_EMPTY
        # Trigger: the fragment is visible. Confirm the main screen.
        runner.wait_for("E79b435a7", text="From")
        # STATE setup for gate edge Ed7d0e9b9 (executed early, before
        # any Generate): tap the hash-type field to open the hash-type
        # sheet, scroll to BLAKE2b (HashType.BLAKE_2B title, 12th of 18
        # rows, so it may be off-screen), and tap it. The choice is
        # stored in preference last_type_value.
        runner.tap("Ed7d0e9b9", res_id=rid("tv_selected_hash_type"))
        runner.scroll_to("Ed7d0e9b9", text="BLAKE2b")
        runner.tap("Ed7d0e9b9", text="BLAKE2b")
        # Ee69c0c42 S_MAIN_EMPTY -> S_SHEET_SOURCE@EMPTY
        # Trigger: tap the From button, the source sheet opens.
        runner.tap("Ee69c0c42", res_id=rid("btn_generate_from"))
        # Ed943ca35 S_SHEET_SOURCE@EMPTY -> BaseListHolder.lambda$bind$0@SRC_FILE
        # Trigger: tap the "File" row (Action.FILE, strings common_file).
        runner.tap("Ed943ca35", text="File")
        # E8c979876 BaseListHolder.lambda$bind$0@SRC_FILE -> callItemClick
        # Trigger: callItemClick() of the ActionHolder.
        runner.comment("call: ActionHolder.callItemClick", "E8c979876")
        # Eff786918 callItemClick -> HashCalculatorFragment.userActionSelect@SRC_FILE
        # Trigger: userActionSelect(action.getUserActionType()).
        runner.comment("call: userActionSelect SEARCH_FILE", "Eff786918")
        # E12829a50 userActionSelect@SRC_FILE -> openSystemFileManager
        # Trigger: switch case for this action.
        runner.comment("call: openSystemFileManager", "E12829a50")
        # Ef6dc9320 openSystemFileManager -> S_EXT_PICK_FILE
        # Trigger: the action opens the system file picker
        # (ACTION_OPEN_DOCUMENT, type */*).
        runner.comment("intent: ACTION_OPEN_DOCUMENT fired", "Ef6dc9320")
        # Eb99504ff S_EXT_PICK_FILE -> onActivityResult@PICK_FILE
        # Trigger: the user picks/confirms in the system dialog;
        # onActivityResult(requestCode, RESULT_OK, data). The fixture
        # was pushed to /sdcard/Download/todo.txt by run_app.sh; pick
        # it by name in the system picker.
        runner.scroll_to("Eb99504ff", text="todo.txt")
        runner.tap("Eb99504ff", text="todo.txt")
        # E1e4be207 onActivityResult@PICK_FILE -> selectFileFromSystemFileManager
        # Trigger: switch on requestCode.
        runner.comment("call: selectFileFromSystemFileManager", "E1e4be207")
        # Ef5562ab9 selectFileFromSystemFileManager -> validateSelectedFile
        # Trigger: validateSelectedFile(uri).
        runner.comment("call: validateSelectedFile", "Ef5562ab9")
        # Ec8413c27 validateSelectedFile -> S_MAIN_FILE
        # Trigger: file becomes the source; From button now reads "File".
        runner.wait_for("Ec8413c27", text="File")
        # E0dbeffc7 S_MAIN_FILE -> S_SHEET_ACTIONS@FILE
        # Trigger: tap the Actions button, the actions sheet opens.
        runner.tap("E0dbeffc7", res_id=rid("btn_hash_actions"))
        # E915e31df S_SHEET_ACTIONS@FILE -> BaseListHolder.lambda$bind$0@GEN_FILE
        # Trigger: tap "Generate" (Action.GENERATE, strings action_generate).
        runner.tap("E915e31df", text="Generate")
        # E84eade87 BaseListHolder.lambda$bind$0@GEN_FILE -> callItemClick
        # Trigger: callItemClick() of the ActionHolder.
        runner.comment("call: ActionHolder.callItemClick", "E84eade87")
        # E00a75033 callItemClick -> HashCalculatorFragment.userActionSelect@GEN_FILE
        # Trigger: userActionSelect(action.getUserActionType()).
        runner.comment("call: userActionSelect GENERATE_HASH", "E00a75033")
        # Ed6d6a6fb userActionSelect@GEN_FILE -> generateHash@FILE
        # Trigger: switch case for this action.
        runner.comment("call: generateHash (file)", "Ed6d6a6fb")
        # E65a8dee6 generateHash@FILE -> HashCalculatorTask.doInBackground@FILE
        # Trigger: AsyncTask.execute(); doInBackground runs on a worker
        # thread. Guard: fileUri != null (satisfied by the picker step).
        runner.comment("async: HashCalculatorTask.doInBackground", "E65a8dee6")
        # E633a9408 doInBackground@FILE -> JdkHashCalculator.fromFile(Context,Uri)
        # Trigger: source kind file.
        runner.comment("call: JdkHashCalculator.fromFile(Context,Uri)",
                      "E633a9408")
        # Eb80710c7 JdkHashCalculator.fromFile(Context,Uri) -> fromFile(InputStream)
        # Trigger: fromFile(stream).
        runner.comment("call: JdkHashCalculator.fromFile(InputStream)",
                      "Eb80710c7")
        # Ed7d0e9b9 fromFile(InputStream) -> JdkHashCalculatorDigest.update@BLAKE
        # Trigger: update(...) for BLAKE2b. Gate satisfied by the early
        # BLAKE2b selection above (preference last_type_value).
        runner.comment("call: digest update BLAKE2b (gate set early)",
                      "Ed7d0e9b9")
        # E7be8a23b JdkHashCalculatorDigest.update@BLAKE -> Blake2B.update(byte[],int,int)
        # Trigger: blake2B.update(input, 0, length); the target method.
        runner.comment("call: Blake2B.update (target)", "E7be8a23b")
    finally:
        runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
