#!/usr/bin/env python3
"""Device replay script for hash-checker route_13.

Method: Clipboard.clear
Edges: E372472a8 E3101d0cd Edeb6bd90 E56501d6f E9e141121 E3755babd
    E9574aba4 E3ac2e1c9 E59c1e403 E79b435a7 E261a2c9b Ecb90c658
    Ebf668e28 E3d93fc17
Printed route: graphs/hash-checker/scratch/route_print/Clipboard.clear.txt
Permissions: none
Fixtures: none
Setup: any file as input (fixtures)

Flow: launch the calculator, type into the custom-hash field (the copy
icons are INVISIBLE while the field is empty, so the field must be
non-empty first), tap the custom-hash copy icon, and then allow the
60-second delayed clear to fire. Clipboard.copy posts its clear
runnable with handler.postDelayed(runnable, 60_000) (Clipboard.java
30-31), so the final step waits on a stable on-screen text with a
70-second timeout, giving the handler time to fire before the script
ends. The activity class is the manifest package
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
         "E261a2c9b", "Ecb90c658", "Ebf668e28", "E3d93fc17"]


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

    runner = Runner(package=args.package, route="route_13", edge_ids=EDGES,
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
        # E261a2c9b S_MAIN_EMPTY -> HashCalculatorFragment.lambda$onViewCreated$4
        # Trigger: tap the icon to copy the custom hash. The field must
        # be non-empty first (icons INVISIBLE while empty), so type
        # into the custom-hash field, then tap its copy icon
        # (iv_custom_hash_copy, fragment_hash_calculator.xml).
        runner.tap("E261a2c9b", res_id=rid("et_field_custom_hash"))
        runner.type_text("samplehash", "E261a2c9b")
        runner.tap("E261a2c9b", res_id=rid("iv_custom_hash_copy"))
        # Ecb90c658 lambda$onViewCreated$4 -> copyHashFromEditText
        # Trigger: copyHashFromEditText(etCustomHash).
        runner.comment("call: copyHashFromEditText(etCustomHash)", "Ecb90c658")
        # Ebf668e28 copyHashFromEditText -> Clipboard.copy
        # Trigger: direct call. The copy shows a LENGTH_SHORT snackbar
        # "Hash value copied to clipboard" (strings
        # history_item_click_text); it is transient, so no wait_for is
        # placed on it -- the next step is the timed clear.
        runner.comment("call: Clipboard.copy", "Ebf668e28")
        # E3d93fc17 Clipboard.copy -> Clipboard.clear
        # Trigger: handler.postDelayed(runnable, 60 s); the clipboard is
        # cleared. Wait on the stable main-screen "From" button with a
        # 70-second timeout so the 60-second handler fires before the
        # script ends. Note: the harness wait_for returns as soon as
        # the text is found, so on a real device this step alone does
        # not force a full 70-second dwell; the timeout is the window
        # allowed for the handler, and the clear itself has no UI
        # signal to assert on.
        runner.wait_for("E3d93fc17", text="From", timeout=70)
        runner.comment("async: Clipboard.clear fired by 60s handler",
                      "E3d93fc17")
    finally:
        runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
