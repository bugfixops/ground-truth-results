#!/usr/bin/env python3
"""Device replay script for hash-checker route_11.

Method: HashCalculatorFragment.writeHashToFile
Edges: E372472a8 E3101d0cd Edeb6bd90 E56501d6f E9e141121 E3755babd
    E9574aba4 E3ac2e1c9 E59c1e403 E79b435a7 Ee69c0c42 E2728220f
    Ed083e7f5 Edcdc6e80 E9c8d2dc9 Ec7ee0bb2 E8bfb57b4 Ecb5a72cb
    E590080eb Ef8616cc0 Ef4c4488a Ea2bfc47e Ea4b92c06 E3d6c7981
    E79275963 E6fdfc92b Ed190d0ac Eb39f4a0e
Printed route: graphs/hash-checker/scratch/route_print/HashCalculatorFragment.writeHashToFile.txt
Permissions: none
Fixtures: none (output-only ACTION_CREATE_DOCUMENT .txt export)
Setup: any file as input (fixtures)

Flow: launch the calculator, pick Text as the source, enter text,
generate its hash (the Export gate: the generated field must be
non-empty), then export the generated hash as a .txt file through the
system CREATE_DOCUMENT picker and confirm the destination with Save.
The activity class is the manifest package
(com.smlnskgmail.jaman.hashchecker) plus .MainActivity, launched under
the flavor applicationId passed as --package.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner

EDGES = ["E372472a8", "E3101d0cd", "Edeb6bd90", "E56501d6f", "E9e141121",
         "E3755babd", "E9574aba4", "E3ac2e1c9", "E59c1e403", "E79b435a7",
         "Ee69c0c42", "E2728220f", "Ed083e7f5", "Edcdc6e80", "E9c8d2dc9",
         "Ec7ee0bb2", "E8bfb57b4", "Ecb5a72cb", "E590080eb", "Ef8616cc0",
         "Ef4c4488a", "Ea2bfc47e", "Ea4b92c06", "E3d6c7981", "E79275963",
         "E6fdfc92b", "Ed190d0ac", "Eb39f4a0e"]


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

    runner = Runner(package=args.package, route="route_11", edge_ids=EDGES,
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
        # Ee69c0c42 S_MAIN_EMPTY -> S_SHEET_SOURCE@EMPTY
        # Trigger: tap the From button, the source sheet opens.
        runner.tap("Ee69c0c42", res_id=rid("btn_generate_from"))
        # E2728220f S_SHEET_SOURCE@EMPTY -> BaseListHolder.lambda$bind$0@SRC_TEXT
        # Trigger: tap the "Text" row (Action.TEXT, strings common_text).
        runner.tap("E2728220f", text="Text")
        # Ed083e7f5 BaseListHolder.lambda$bind$0@SRC_TEXT -> callItemClick
        # Trigger: callItemClick() of the ActionHolder.
        runner.comment("call: ActionHolder.callItemClick", "Ed083e7f5")
        # Edcdc6e80 callItemClick -> HashCalculatorFragment.userActionSelect@SRC_TEXT
        # Trigger: userActionSelect(action.getUserActionType()).
        runner.comment("call: userActionSelect ENTER_TEXT", "Edcdc6e80")
        # E9c8d2dc9 userActionSelect@SRC_TEXT -> HashCalculatorFragment.enterText
        # Trigger: switch case for this action.
        runner.comment("call: enterText()", "E9c8d2dc9")
        # Ec7ee0bb2 HashCalculatorFragment.enterText -> S_DLG_TEXT_INPUT
        # Trigger: the action opens the text-input dialog.
        runner.comment("dialog: TextInputDialog opens", "Ec7ee0bb2")
        # E8bfb57b4 S_DLG_TEXT_INPUT -> TextInputDialog.lambda$initializeDialog$0
        # Trigger: type some text, tap "Add" (dialog_text_input.xml).
        runner.tap("E8bfb57b4", res_id=rid("et_dialog_input_text"))
        runner.type_text("hello", "E8bfb57b4")
        runner.tap("E8bfb57b4", res_id=rid("btn_dialog_input_text_add"))
        # Ecb5a72cb TextInputDialog.lambda$initializeDialog$0 -> textValueEntered
        # Trigger: textValueCallback.textValueEntered(text).
        runner.comment("call: textValueEntered", "Ecb5a72cb")
        # E590080eb HashCalculatorFragment.textValueEntered -> S_MAIN_TEXT
        # Trigger: text becomes the source; From button now reads "Text".
        runner.wait_for("E590080eb", text="Text")
        # Ef8616cc0 S_MAIN_TEXT -> S_SHEET_ACTIONS@TEXT
        # Trigger: tap the Actions button, the actions sheet opens.
        runner.tap("Ef8616cc0", res_id=rid("btn_hash_actions"))
        # Ef4c4488a S_SHEET_ACTIONS@TEXT -> BaseListHolder.lambda$bind$0@EXP_OK
        # Trigger: tap "Export .txt" -- but this edge needs a hash generated
        # first (Export needs a non-empty generated field), so generate
        # first from the already-open actions sheet, then reopen it and
        # tap the export row. Export row title is strings
        # action_export_to_txt: Export as ".txt".
        runner.tap("Ef4c4488a", text="Generate")
        # Generate runs an AsyncTask behind a progress dialog; the
        # generated field has no distinct text to assert, so confirm the
        # main screen is back before exporting.
        runner.wait_for("Ef4c4488a", text="Action", timeout=30)
        runner.tap("Ef4c4488a", res_id=rid("btn_hash_actions"))
        runner.tap("Ef4c4488a", text='Export as ".txt"')
        # Ea2bfc47e BaseListHolder.lambda$bind$0@EXP_OK -> callItemClick
        # Trigger: callItemClick() of the ActionHolder.
        runner.comment("call: ActionHolder.callItemClick", "Ea2bfc47e")
        # Ea4b92c06 callItemClick -> HashCalculatorFragment.userActionSelect@EXP_OK
        # Trigger: userActionSelect(action.getUserActionType()).
        runner.comment("call: userActionSelect EXPORT_AS_TXT", "Ea4b92c06")
        # E3d6c7981 userActionSelect@EXP_OK -> saveGeneratedHashAsTextFile@OK
        # Trigger: switch case for this action.
        runner.comment("call: saveGeneratedHashAsTextFile", "E3d6c7981")
        # E79275963 saveGeneratedHashAsTextFile@OK -> HashCalculatorFragment.saveTextFile
        # Trigger: saveTextFile(name); guard: source selected and the
        # generated field is not empty (satisfied by the Generate above).
        runner.comment("call: saveTextFile", "E79275963")
        # E6fdfc92b HashCalculatorFragment.saveTextFile -> S_EXT_CREATE_TXT
        # Trigger: startActivityForResult(ACTION_CREATE_DOCUMENT).
        runner.comment("intent: ACTION_CREATE_DOCUMENT text/plain fired",
                      "E6fdfc92b")
        # Ed190d0ac S_EXT_CREATE_TXT -> onActivityResult@CREATE_TXT
        # Trigger: the user picks/confirms in the system dialog;
        # onActivityResult(requestCode, RESULT_OK, data). System picker:
        # confirm the suggested destination with Save.
        runner.tap("Ed190d0ac", text="Save")
        # Eb39f4a0e onActivityResult@CREATE_TXT -> HashCalculatorFragment.writeHashToFile
        # Trigger: switch on requestCode; the target method writes the hash.
        runner.comment("call: writeHashToFile (target)", "Eb39f4a0e")
    finally:
        runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
