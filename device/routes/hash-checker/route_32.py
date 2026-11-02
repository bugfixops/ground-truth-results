#!/usr/bin/env python3
"""Device replay script for hash-checker route_32.

Method: AppTextWatcher.<init>
Printed route: graphs/hash-checker/scratch/route_print/AppTextWatcher.<init>.txt
Edge ids (in route order):
    E372472a8 E3101d0cd Edeb6bd90 E56501d6f E9e141121 E3755babd
    E9574aba4 E3ac2e1c9 Ebfdc600d Ea7a75dfd Ee5897aea
Permissions: none
Fixtures: none
Setup: any file as input (fixtures)
Status in ROUTES.csv: scripted

Route story: launching the app is enough. HashCalculatorFragment.
onViewCreated() unconditionally attaches a watcher (an anonymous
AppTextWatcher subclass, HashCalculatorFragment.java:516) to each hash
EditText via watcherForInputField() (lines 457-468), so the constructor
runs during launch with no typing or other user action needed.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness.harness import Runner  # noqa: E402

EDGES = [
    "E372472a8", "E3101d0cd", "Edeb6bd90", "E56501d6f", "E9e141121",
    "E3755babd", "E9574aba4", "E3ac2e1c9", "Ebfdc600d", "Ea7a75dfd",
    "Ee5897aea",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    runner = Runner(package=args.package, route="route_32", edge_ids=EDGES,
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
        # onViewCreated builds the view and attaches the watchers; wait
        # for the From button to prove the view exists.
        runner.wait_for("E3ac2e1c9",
                        res_id=args.package + ":id/btn_generate_from")
        # Ebfdc600d -- HashCalculatorFragment.onViewCreated -> HashCalculatorFragment.watcherForInputField:
        # direct call for both hash EditTexts, no user action.
        runner.comment("watcherForInputField() for the hash fields",
                       "Ebfdc600d")
        # Ea7a75dfd -- HashCalculatorFragment.watcherForInputField -> HashCalculatorFragment$1.<init>:
        # anonymous AppTextWatcher subclass created at line 516.
        runner.comment("new AppTextWatcher() anonymous subclass",
                       "Ea7a75dfd")
        # Ee5897aea -- HashCalculatorFragment$1.<init> -> AppTextWatcher.<init>:
        # superclass constructor; reached by launch alone, no typing
        # is needed to construct the watcher (typing would only fire
        # its onTextChanged callback, a different method).
        runner.comment("AppTextWatcher.<init> superclass constructor",
                       "Ee5897aea")
    finally:
        runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
