#!/usr/bin/env python3
"""Device replay script for hash-checker route_23.

Method: Action.getAdditionalIconResId
Printed route: graphs/hash-checker/scratch/route_print/Action.getAdditionalIconResId.txt
Edge ids (in route order, from ROUTES.csv):
    E372472a8 E3101d0cd Edeb6bd90 E56501d6f E9e141121 E3755babd E9574aba4
    E3ac2e1c9 E59c1e403 E79b435a7 E9f3e3d7b Eb36900a4 E762718bd E4cb47141
    E69e5b24a E633c76e6 E6474ddfb
Permissions: (none)
Fixtures: (none)
Setup: any file as input (fixtures)
Status in ROUTES.csv: scripted

One script block per route edge, in route order. Lifecycle/framework
edges with no user action are logged with comment(); GUI edges are real
taps/waits. No pm clear, fixture push, or permission grant happens here:
run_app.sh does pm clear, fixture push, and grants before invoking this
script.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from device.harness.harness import Runner

EDGE_IDS = [
    "E372472a8", "E3101d0cd", "Edeb6bd90", "E56501d6f", "E9e141121",
    "E3755babd", "E9574aba4", "E3ac2e1c9", "E59c1e403", "E79b435a7",
    "E9f3e3d7b", "Eb36900a4", "E762718bd", "E4cb47141", "E69e5b24a",
    "E633c76e6", "E6474ddfb",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    args = ap.parse_args()
    runner = Runner(package=args.package, route="route_23",
                    edge_ids=EDGE_IDS, log_path=args.log,
                    dry_run=args.dry_run, adb=args.adb,
                    outdir=args.outdir)
    try:
        # E372472a8: S_ENTRY -> MainActivity.<init>
        # Trigger: "Tap the launcher icon (MAIN + LAUNCHER intent filter);
        # the only activity". Manifest package is
        # com.smlnskgmail.jaman.hashchecker, so .MainActivity resolves
        # under the flavor applicationId given by --package.
        runner.launch(args.package + "/com.smlnskgmail.jaman.hashchecker.MainActivity",
                      "E372472a8")
        # E3101d0cd: MainActivity.<init> -> MainActivity.onCreate
        # Trigger: "The system instantiates MainActivity, then calls
        # onCreate". Lifecycle edge, no user action.
        runner.comment("lifecycle: MainActivity.onCreate", "E3101d0cd")
        # Edeb6bd90: MainActivity.onCreate -> BaseActivity.onCreate@MainActivity
        # Trigger: "Direct call" (super.onCreate).
        runner.comment("call: super.onCreate", "Edeb6bd90")
        # E56501d6f: BaseActivity.onCreate@MainActivity -> MainActivity.create
        # Trigger: "Direct call" (create()).
        runner.comment("call: MainActivity.create", "E56501d6f")
        # E9e141121: MainActivity.create -> MainActivity.showFragment@CALC
        # Trigger: "showFragment(mainFragment): adds the calculator".
        runner.comment("call: showFragment calculator fragment", "E9e141121")
        # E3755babd: MainActivity.showFragment@CALC ->
        # HashCalculatorFragment.onAttach
        # Trigger: "FragmentTransaction.commit(): the fragment is attached".
        runner.comment("lifecycle: HashCalculatorFragment attached", "E3755babd")
        # E9574aba4: HashCalculatorFragment.onAttach ->
        # BaseFragment.onCreateView@HashCalculatorFragment
        # Trigger: "onCreateView inflates the layout".
        runner.comment("lifecycle: calculator fragment view created", "E9574aba4")
        # E3ac2e1c9: BaseFragment.onCreateView@HashCalculatorFragment ->
        # HashCalculatorFragment.onViewCreated
        # Trigger: "onViewCreated".
        runner.comment("lifecycle: calculator fragment onViewCreated", "E3ac2e1c9")
        # E59c1e403: HashCalculatorFragment.onViewCreated ->
        # BaseFragment.onResume@HashCalculatorFragment
        # Trigger: "onStart -> onResume".
        runner.comment("lifecycle: calculator fragment resumed", "E59c1e403")
        # E79b435a7: BaseFragment.onResume@HashCalculatorFragment ->
        # S_MAIN_EMPTY
        # Trigger: "The fragment is visible". Observable: the hash-type
        # TextView (fragment_hash_calculator.xml, tv_selected_hash_type).
        runner.wait_for("E79b435a7",
                        res_id=args.package + ":id/tv_selected_hash_type")
        # E9f3e3d7b: S_MAIN_EMPTY ->
        # HashCalculatorFragment.lambda$onViewCreated$9
        # Trigger: "Tap the From button" (HashCalculatorFragment.java:476:
        # btnGenerateFrom.setOnClickListener shows
        # SourceSelectActionsBottomSheet).
        runner.tap("E9f3e3d7b",
                   res_id=args.package + ":id/btn_generate_from")
        # Eb36900a4: HashCalculatorFragment.lambda$onViewCreated$9 ->
        # SourceSelectActionsBottomSheet.onAttach
        # Trigger: "show(): the bottom-sheet fragment is attached".
        runner.comment("lifecycle: SourceSelectActionsBottomSheet attached",
                       "Eb36900a4")
        # E762718bd: SourceSelectActionsBottomSheet.onAttach ->
        # BaseListBottomSheet.onViewCreated@SourceSelectActionsBottomSheet
        # Trigger: "onViewCreated (after onCreateView)".
        runner.comment("lifecycle: actions bottom sheet view created", "E762718bd")
        # E4cb47141: BaseListBottomSheet.onViewCreated@SourceSelectActionsBottomSheet
        # -> BaseListAdapter.onBindViewHolder@ACTIONS_AD
        # Trigger: "RecyclerView binds the rows". Observable: the bottom
        # sheet list (bottom_sheet_list_items.xml, rv_bottom_sheet_list_items).
        runner.wait_for("E4cb47141",
                        res_id=args.package + ":id/rv_bottom_sheet_list_items")
        # E69e5b24a: BaseListAdapter.onBindViewHolder@ACTIONS_AD ->
        # ActionsListAdapter$ActionHolder.bind
        # Trigger: "holder.bind(items.get(position))" (BaseListAdapter.java:44).
        # Observable: a bound row title (item_list.xml, tv_item_list_title).
        runner.wait_for("E69e5b24a",
                        res_id=args.package + ":id/tv_item_list_title")
        # E633c76e6: ActionsListAdapter$ActionHolder.bind ->
        # BaseListHolder.bind@ActionsListAdapter$ActionHolder
        # Trigger: "Direct call" (super.bind, ActionsListAdapter.java:51).
        runner.comment("call: BaseListHolder.bind", "E633c76e6")
        # E6474ddfb: BaseListHolder.bind@ActionsListAdapter$ActionHolder
        # -> Action.getAdditionalIconResId
        # Trigger: "Virtual/interface call that can dispatch to this
        # implementation". No separate wait target: getAdditionalIconResId
        # is called unconditionally at BaseListHolder.java:56 inside the
        # bind already evidenced by the rendered row above, and the
        # additional icon view (iv_item_list_additional_icon) is INVISIBLE
        # by default (getConditionToAdditionalIconVisibleState is false),
        # so it is not a reliable wait target even though the method ran.
        runner.comment("call: Action.getAdditionalIconResId in BaseListHolder.bind",
                       "E6474ddfb")
    finally:
        runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
