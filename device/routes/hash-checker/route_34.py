#!/usr/bin/env python3
"""Device replay script for hash-checker route_34.

Method: HashCalculatorFragment.selectFileFromSystemFileManager
Printed route: graphs/hash-checker/scratch/route_print/HashCalculatorFragment.selectFileFromSystemFileManager.txt
Edge ids (in route order):
    E372472a8 E3101d0cd Edeb6bd90 E56501d6f E9e141121 E3755babd
    E9574aba4 E3ac2e1c9 E59c1e403 E79b435a7 Ee69c0c42 Ed943ca35
    E8c979876 Eff786918 E12829a50 Ef6dc9320 Eb99504ff E1e4be207
Permissions: none
Fixtures: Download/todo.txt
Setup: any file as input (fixtures)
Status in ROUTES.csv: scripted

Route story: launch the calculator, open the "From" source sheet, pick
"File", and in the system file picker pick todo.txt (pushed by
run_app.sh to /sdcard/Download/todo.txt before this script runs).
The picker result (RESULT_OK) reaches onActivityResult, which calls
selectFileFromSystemFileManager(data.getData()); the method itself
only validates the returned URI.

Picker assumption: the picker view that opens shows (or scrolls to)
todo.txt by name. If the replay image's picker opens on a different
folder, the device lead must add a navigate-to-Download step before
the scroll below; no picker navigation label is invented here.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness.harness import Runner  # noqa: E402

EDGES = [
    "E372472a8", "E3101d0cd", "Edeb6bd90", "E56501d6f", "E9e141121",
    "E3755babd", "E9574aba4", "E3ac2e1c9", "E59c1e403", "E79b435a7",
    "Ee69c0c42", "Ed943ca35", "E8c979876", "Eff786918", "E12829a50",
    "Ef6dc9320", "Eb99504ff", "E1e4be207",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    runner = Runner(package=args.package, route="route_34", edge_ids=EDGES,
                    log_path=args.log, dry_run=args.dry_run, adb=args.adb,
                    outdir=args.outdir)
    try:
        # E372472a8 -- S_ENTRY -> MainActivity.<init>: launch the app.
        # Manifest package is com.smlnskgmail.jaman.hashchecker and
        # .MainActivity is the launcher activity; args.package is the
        # flavor applicationId, so the component is built from it.
        runner.launch(args.package + "/com.smlnskgmail.jaman.hashchecker.MainActivity",
                      "E372472a8")
        # E3101d0cd -- MainActivity.<init> -> MainActivity.onCreate:
        # lifecycle, no user action.
        runner.comment("MainActivity.onCreate lifecycle", "E3101d0cd")
        # Edeb6bd90 -- MainActivity.onCreate -> BaseActivity.onCreate@MainActivity:
        # super.onCreate, no user action.
        runner.comment("super.onCreate", "Edeb6bd90")
        # E56501d6f -- BaseActivity.onCreate@MainActivity -> MainActivity.create:
        # framework calls create(), no user action.
        runner.comment("BaseActivity calls MainActivity.create()", "E56501d6f")
        # E9e141121 -- MainActivity.create -> MainActivity.showFragment@CALC:
        # showFragment(mainFragment), no user action.
        runner.comment("showFragment(HashCalculatorFragment)", "E9e141121")
        # E3755babd -- MainActivity.showFragment@CALC -> HashCalculatorFragment.onAttach:
        # FragmentManager lifecycle, no user action.
        runner.comment("FragmentManager attaches HashCalculatorFragment",
                       "E3755babd")
        # E9574aba4 -- HashCalculatorFragment.onAttach -> BaseFragment.onCreateView@HashCalculatorFragment:
        # FragmentManager lifecycle, no user action.
        runner.comment("FragmentManager creates the fragment view", "E9574aba4")
        # E3ac2e1c9 -- BaseFragment.onCreateView@HashCalculatorFragment -> HashCalculatorFragment.onViewCreated:
        # FragmentManager lifecycle, no user action.
        runner.comment("HashCalculatorFragment.onViewCreated", "E3ac2e1c9")
        # E59c1e403 -- HashCalculatorFragment.onViewCreated -> BaseFragment.onResume@HashCalculatorFragment:
        # FragmentManager lifecycle, no user action.
        runner.comment("HashCalculatorFragment.onResume", "E59c1e403")
        # E79b435a7 -- BaseFragment.onResume@HashCalculatorFragment -> S_MAIN_EMPTY:
        # main screen entered; wait for the From button to prove it.
        runner.wait_for("E79b435a7",
                        res_id=args.package + ":id/btn_generate_from")
        # Ee69c0c42 -- S_MAIN_EMPTY -> S_SHEET_SOURCE@EMPTY:
        # tap "From" (btn_generate_from, fragment_hash_calculator.xml,
        # text @string/action_from = "From") to open the source sheet.
        runner.tap("Ee69c0c42",
                   res_id=args.package + ":id/btn_generate_from")
        # Ed943ca35 -- S_SHEET_SOURCE@EMPTY -> BaseListHolder.lambda$bind$0@SRC_FILE:
        # tap "File" (Action.FILE title R.string.common_file = "File").
        runner.tap("Ed943ca35", text="File")
        # E8c979876 -- BaseListHolder.lambda$bind$0@SRC_FILE -> ActionsListAdapter$ActionHolder.callItemClick@SRC_FILE:
        # item click handler, no user action beyond the tap above.
        runner.comment("ActionHolder.callItemClick for FILE", "E8c979876")
        # Eff786918 -- ActionsListAdapter$ActionHolder.callItemClick@SRC_FILE -> HashCalculatorFragment.userActionSelect@SRC_FILE:
        # userActionSelect(SEARCH_FILE), no user action beyond the tap.
        runner.comment("userActionSelect(SEARCH_FILE)", "Eff786918")
        # E12829a50 -- HashCalculatorFragment.userActionSelect@SRC_FILE -> HashCalculatorFragment.openSystemFileManager:
        # SEARCH_FILE case calls openSystemFileManager(), which fires
        # ACTION_OPEN_DOCUMENT via startActivityForResult.
        runner.comment("openSystemFileManager() fires ACTION_OPEN_DOCUMENT",
                       "E12829a50")
        # Ef6dc9320 -- HashCalculatorFragment.openSystemFileManager -> S_EXT_PICK_FILE:
        # system picker entered; scroll until the fixture file is
        # visible. The picker is outside the app package, so the file
        # is located by its displayed name, not by an app resource id.
        runner.scroll_to("Ef6dc9320", text="todo.txt")
        # Eb99504ff -- S_EXT_PICK_FILE -> HashCalculatorFragment.onActivityResult@PICK_FILE:
        # trigger: in the system dialog, choose a document and confirm.
        # Tap the fixture by name; the picker returns RESULT_OK and
        # onActivityResult(FILE_SELECT) runs.
        runner.tap("Eb99504ff", text="todo.txt")
        # E1e4be207 -- HashCalculatorFragment.onActivityResult@PICK_FILE -> HashCalculatorFragment.selectFileFromSystemFileManager:
        # onActivityResult switch on requestCode calls
        # selectFileFromSystemFileManager(data.getData()). The app
        # returns to the main screen; wait for the From button to
        # prove the result was delivered.
        runner.comment("onActivityResult calls selectFileFromSystemFileManager()",
                       "E1e4be207")
        runner.wait_for("E1e4be207",
                        res_id=args.package + ":id/btn_generate_from")
    finally:
        runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
