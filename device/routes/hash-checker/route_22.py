#!/usr/bin/env python3
"""Device replay script for hash-checker route_22.

Method: Language.getPrimaryIconResId
Printed route: graphs/hash-checker/scratch/route_print/Language.getPrimaryIconResId.txt
Edge ids (in route order, from ROUTES.csv):
    E372472a8 E3101d0cd Edeb6bd90 E56501d6f E9e141121 E3755babd E9574aba4
    E3ac2e1c9 E59c1e403 E79b435a7 E98e98419 E30bb0ca3 E58fc7a37 E0848626c
    Eed97dffc E329fd909 Eb87d737f E336266fc E9b38055b E4f82c39c Ed43133ac
    E19e1a777 E3f50838e Ee8d2d2bd
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
    "E98e98419", "E30bb0ca3", "E58fc7a37", "E0848626c", "Eed97dffc",
    "E329fd909", "Eb87d737f", "E336266fc", "E9b38055b", "E4f82c39c",
    "Ed43133ac", "E19e1a777", "E3f50838e", "Ee8d2d2bd",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    args = ap.parse_args()
    runner = Runner(package=args.package, route="route_22",
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
        # E98e98419: S_MAIN_EMPTY ->
        # MainActivity.onOptionsItemSelected@SETTINGS
        # Trigger: "Tap the Settings icon in the action bar
        # (R.id.menu_main_section_settings)" (menu_main.xml, shown always).
        runner.tap("E98e98419",
                   res_id=args.package + ":id/menu_main_section_settings")
        # E30bb0ca3: MainActivity.onOptionsItemSelected@SETTINGS ->
        # MainActivity.showFragment@SETTINGS
        # Trigger: "showFragment(...)" (MainActivity.java:130).
        runner.comment("call: showFragment settings fragment", "E30bb0ca3")
        # E58fc7a37: MainActivity.showFragment@SETTINGS ->
        # SettingsFragment.onAttach
        # Trigger: "FragmentTransaction.commit(): the fragment is attached".
        runner.comment("lifecycle: SettingsFragment attached", "E58fc7a37")
        # E0848626c: SettingsFragment.onAttach ->
        # SettingsFragment.onCreatePreferences
        # Trigger: "onCreate (PreferenceFragmentCompat: onCreatePreferences)".
        runner.comment("lifecycle: settings preferences created", "E0848626c")
        # Eed97dffc: SettingsFragment.onCreatePreferences ->
        # SettingsFragment.onViewCreated
        # Trigger: "onViewCreated".
        runner.comment("lifecycle: settings fragment onViewCreated", "Eed97dffc")
        # E329fd909: SettingsFragment.onViewCreated -> SettingsFragment.onResume
        # Trigger: "onStart -> onResume".
        runner.comment("lifecycle: settings fragment resumed", "E329fd909")
        # Eb87d737f: SettingsFragment.onResume -> S_SETTINGS
        # Trigger: "The fragment is visible". Observable: the Language
        # preference title (res/xml/settings.xml key_language, title
        # strings.xml settings_title_language = "Language").
        runner.wait_for("Eb87d737f", text="Language")
        # E336266fc: S_SETTINGS ->
        # SettingsFragment.lambda$initLanguageSettings$0
        # Trigger: "Tap the Language row" (SettingsFragment.java:161-165:
        # the language preference click listener shows LanguagesBottomSheet).
        runner.tap("E336266fc", text="Language")
        # E9b38055b: SettingsFragment.lambda$initLanguageSettings$0 ->
        # LanguagesBottomSheet.onAttach
        # Trigger: "show(): the bottom-sheet fragment is attached".
        runner.comment("lifecycle: LanguagesBottomSheet attached", "E9b38055b")
        # E4f82c39c: LanguagesBottomSheet.onAttach ->
        # BaseListBottomSheet.onViewCreated@LanguagesBottomSheet
        # Trigger: "onViewCreated (after onCreateView)".
        runner.comment("lifecycle: languages bottom sheet view created", "E4f82c39c")
        # Ed43133ac: BaseListBottomSheet.onViewCreated@LanguagesBottomSheet
        # -> BaseListAdapter.onBindViewHolder@LANG_AD
        # Trigger: "RecyclerView binds the rows". Observable: the bottom
        # sheet list (bottom_sheet_list_items.xml, rv_bottom_sheet_list_items).
        runner.wait_for("Ed43133ac",
                        res_id=args.package + ":id/rv_bottom_sheet_list_items")
        # E19e1a777: BaseListAdapter.onBindViewHolder@LANG_AD ->
        # LanguagesListAdapter$LanguagesListHolder.bind
        # Trigger: "holder.bind(items.get(position))" (BaseListAdapter.java:44).
        # Observable: a bound row title (item_list.xml, tv_item_list_title).
        runner.wait_for("E19e1a777",
                        res_id=args.package + ":id/tv_item_list_title")
        # E3f50838e: LanguagesListAdapter$LanguagesListHolder.bind ->
        # BaseListHolder.bind@LanguagesListAdapter$LanguagesListHolder
        # Trigger: "Direct call" (super.bind, LanguagesListAdapter.java:76).
        runner.comment("call: BaseListHolder.bind", "E3f50838e")
        # Ee8d2d2bd: BaseListHolder.bind@LanguagesListAdapter$LanguagesListHolder
        # -> Language.getPrimaryIconResId
        # Trigger: "Virtual/interface call that can dispatch to this
        # implementation". No separate wait target: getPrimaryIconResId is
        # called unconditionally at BaseListHolder.java:47 inside the bind
        # already evidenced by the rendered row above, and the primary
        # icon view (iv_item_list_icon) is GONE by default
        # (getConditionToPrimaryIconVisibleState is false), so it cannot
        # be waited on even though the method ran.
        runner.comment("call: Language.getPrimaryIconResId in BaseListHolder.bind",
                       "Ee8d2d2bd")
    finally:
        runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
