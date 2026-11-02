#!/usr/bin/env python3
"""Replay script for hash-checker route_05.

Method: Blake2B.littleEndianToInt
Edge ids (exact, in order, from ROUTES.csv):
    E372472a8 E3101d0cd Edeb6bd90 E56501d6f E9e141121 E3755babd
    E9574aba4 E3ac2e1c9 E59c1e403 E79b435a7 Ee69c0c42 E2728220f
    Ed083e7f5 Edcdc6e80 E9c8d2dc9 Ec7ee0bb2 E8bfb57b4 Ecb5a72cb
    E590080eb Ef8616cc0 E05e0bcb7 E64f91a49 Efc4c965d E3918c21f
    E1c1f54d8 E90973e55 E78eefda0 E74445007 E907e4915 E6fef809b
    Ef23378ee E1402c60d
Printed route:
    graphs/hash-checker/scratch/route_print/Blake2B.littleEndianToInt.txt
Permissions: none (ROUTES.csv permissions cell is empty).
Fixtures: none (ROUTES.csv fixtures cell is empty).
Setup: any file as input (fixtures).

STATE note (settings): the printed route reaches
JdkHashCalculatorDigest.result@BLAKE, which only happens when the
selected hash type is BLAKE2b (result() returns blake2B.getValue()
only for BLAKE_2B). The fresh-app default hash type is MD5
(SharedPreferencesSettings.getLastHashType defaults to MD5), so the
script first taps the hash-type field (tv_selected_hash_type) and
picks "BLAKE2b" (HashConstants.BLAKE_2B) from the hash-type sheet.
Those taps are logged under E79b435a7, the edge that enters the
main-empty state where they happen, before the source sheet opens.
The final wait checks the generated BLAKE2b-512 value of the text
"hash-checker" (lowercase hex, as produced by Blake2B.bytesToHex),
which proves the whole chain ran to the result field. No pm clear,
fixture push, or permission grant happens here; run_app.sh owns
those steps.
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
    "Ee69c0c42", "E2728220f", "Ed083e7f5", "Edcdc6e80", "E9c8d2dc9",
    "Ec7ee0bb2", "E8bfb57b4", "Ecb5a72cb", "E590080eb", "Ef8616cc0",
    "E05e0bcb7", "E64f91a49", "Efc4c965d", "E3918c21f", "E1c1f54d8",
    "E90973e55", "E78eefda0", "E74445007", "E907e4915", "E6fef809b",
    "Ef23378ee", "E1402c60d",
]

# BLAKE2b-512 (lowercase hex) of the text "hash-checker", the value the
# generated-hash field shows once generation with BLAKE2b completes.
TEXT_BLAKE2B = (
    "de171b9d16e3855dc2e98348955b7bcc02e480cc86bf240d6e1203fa8c09d33"
    "bc89bd46c2485d6b68c2b5abf40fd4a313821108287cceee9330c7cd3e0bd5854"
)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    pkg = args.package
    runner = Runner(package=args.package, route="route_05",
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
    # Settings step under E79b435a7 (still on the main-empty screen):
    # the fresh-app default hash type is MD5, but this route needs
    # BLAKE2b. Tap the hash-type field (fragment_hash_calculator.xml
    # tv_selected_hash_type) to open the hash-type sheet, scroll to
    # and tap the "BLAKE2b" row (HashType list item title), which calls
    # hashTypeSelect and saves BLAKE2b as the last hash type.
    runner.tap("E79b435a7", res_id=pkg + ":id/tv_selected_hash_type")
    runner.scroll_to("E79b435a7", text="BLAKE2b")
    runner.tap("E79b435a7", text="BLAKE2b")
    runner.wait_for("E79b435a7", text="BLAKE2b")
    # Ee69c0c42: S_MAIN_EMPTY -> S_SHEET_SOURCE@EMPTY
    # Trigger: tap the From button; the sheet opens over this page.
    runner.tap("Ee69c0c42", res_id=pkg + ":id/btn_generate_from")
    # E2728220f: S_SHEET_SOURCE@EMPTY -> BaseListHolder.lambda$bind$0@SRC_TEXT
    # Trigger: tap the "Text" row (Action.TEXT, common_text).
    runner.tap("E2728220f", text="Text")
    # Ed083e7f5: BaseListHolder.lambda$bind$0@SRC_TEXT ->
    # ActionsListAdapter$ActionHolder.callItemClick@SRC_TEXT
    # Trigger: callItemClick() of the ActionHolder.
    runner.comment("sheet row click dispatches callItemClick", "Ed083e7f5")
    # Edcdc6e80: ActionsListAdapter$ActionHolder.callItemClick@SRC_TEXT ->
    # HashCalculatorFragment.userActionSelect@SRC_TEXT
    # Trigger: userActionSelect(action.getUserActionType()).
    runner.comment("holder calls userActionSelect(ENTER_TEXT)", "Edcdc6e80")
    # E9c8d2dc9: HashCalculatorFragment.userActionSelect@SRC_TEXT ->
    # HashCalculatorFragment.enterText
    # Trigger: switch case for this action.
    runner.comment("userActionSelect switch case calls enterText",
                   "E9c8d2dc9")
    # Ec7ee0bb2: HashCalculatorFragment.enterText -> S_DLG_TEXT_INPUT
    # Trigger: the action opens this window. The dialog's input field
    # (dialog_text_input.xml et_dialog_input_text) is the anchor.
    runner.wait_for("Ec7ee0bb2",
                    res_id=pkg + ":id/et_dialog_input_text")
    # E8bfb57b4: S_DLG_TEXT_INPUT -> TextInputDialog.lambda$initializeDialog$0
    # Trigger: tap Add. The text is typed first, then Add
    # (btn_dialog_input_text_add, common_add) submits it.
    runner.tap("E8bfb57b4", res_id=pkg + ":id/et_dialog_input_text")
    runner.type_text("hash-checker", "E8bfb57b4")
    runner.tap("E8bfb57b4", res_id=pkg + ":id/btn_dialog_input_text_add")
    # Ecb5a72cb: TextInputDialog.lambda$initializeDialog$0 ->
    # HashCalculatorFragment.textValueEntered
    # Trigger: textValueCallback.textValueEntered(text).
    runner.comment("dialog Add callback calls textValueEntered", "Ecb5a72cb")
    # E590080eb: HashCalculatorFragment.textValueEntered -> S_MAIN_TEXT
    # Trigger: text becomes the source. The selected-object label now
    # shows the typed text.
    runner.wait_for("E590080eb", text="hash-checker")
    # Ef8616cc0: S_MAIN_TEXT -> S_SHEET_ACTIONS@TEXT
    # Trigger: tap the Actions button; the sheet opens over this page.
    runner.tap("Ef8616cc0", res_id=pkg + ":id/btn_hash_actions")
    # E05e0bcb7: S_SHEET_ACTIONS@TEXT -> BaseListHolder.lambda$bind$0@GEN_TEXT
    # Trigger: tap "Generate" (Action.GENERATE, action_generate).
    runner.tap("E05e0bcb7", text="Generate")
    # E64f91a49: BaseListHolder.lambda$bind$0@GEN_TEXT ->
    # ActionsListAdapter$ActionHolder.callItemClick@GEN_TEXT
    # Trigger: callItemClick() of the ActionHolder.
    runner.comment("sheet row click dispatches callItemClick", "E64f91a49")
    # Efc4c965d: ActionsListAdapter$ActionHolder.callItemClick@GEN_TEXT ->
    # HashCalculatorFragment.userActionSelect@GEN_TEXT
    # Trigger: userActionSelect(action.getUserActionType()).
    runner.comment("holder calls userActionSelect(GENERATE_HASH)",
                   "Efc4c965d")
    # E3918c21f: HashCalculatorFragment.userActionSelect@GEN_TEXT ->
    # HashCalculatorFragment.generateHash@TEXT
    # Trigger: switch case for this action.
    runner.comment("userActionSelect switch case calls generateHash",
                   "E3918c21f")
    # E1c1f54d8: HashCalculatorFragment.generateHash@TEXT ->
    # HashCalculatorTask.doInBackground@TEXT
    # Trigger: AsyncTask.execute(); doInBackground runs on a worker thread.
    runner.comment("generateHash executes HashCalculatorTask", "E1c1f54d8")
    # E90973e55: HashCalculatorTask.doInBackground@TEXT ->
    # JdkHashCalculator.fromString
    # Trigger: source kind: text.
    runner.comment("task hashes the text source", "E90973e55")
    # E78eefda0: JdkHashCalculator.fromString ->
    # JdkHashCalculatorDigest.result@BLAKE
    # Trigger: result() for BLAKE2b.
    runner.comment("digest result() takes the BLAKE2b branch", "E78eefda0")
    # E74445007: JdkHashCalculatorDigest.result@BLAKE -> Blake2B.getValue
    # Trigger: blake2B.getValue().
    runner.comment("direct call: blake2B.getValue()", "E74445007")
    # E907e4915: Blake2B.getValue -> Blake2B.doFinal
    # Trigger: direct call.
    runner.comment("direct call: getValue calls doFinal", "E907e4915")
    # E6fef809b: Blake2B.doFinal -> Blake2B.compress
    # Trigger: direct call.
    runner.comment("direct call: doFinal calls compress", "E6fef809b")
    # Ef23378ee: Blake2B.compress -> Blake2B.littleEndianToLong
    # Trigger: direct call.
    runner.comment("direct call: compress calls littleEndianToLong",
                   "Ef23378ee")
    # E1402c60d: Blake2B.littleEndianToLong -> Blake2B.littleEndianToInt
    # Trigger: direct call. The generated-hash field showing the
    # BLAKE2b-512 value of "hash-checker" proves the task completed
    # through this chain; coverage comparison is the final proof.
    runner.wait_for("E1402c60d", text=TEXT_BLAKE2B, timeout=30)
    runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
