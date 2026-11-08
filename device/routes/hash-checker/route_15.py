#!/usr/bin/env python3
"""Device replay script for hash-checker route_15.

Method: SettingsFragment.copyFile
Edges: E372472a8 E3101d0cd Edeb6bd90 E56501d6f E9e141121 E3755babd
    E9574aba4 E3ac2e1c9 E59c1e403 E79b435a7 E98e98419 E30bb0ca3
    E58fc7a37 E0848626c Eed97dffc E329fd909 Eb87d737f Edcfc9c0b
    E86345c53 E55287499 E3ce12de4 Eeef8c2a2 E8654d3ef E8dd93771
Printed route: graphs/hash-checker/scratch/route_print/SettingsFragment.copyFile.txt
Permissions: none
Fixtures: none (output-only ACTION_CREATE_DOCUMENT zip export)
Setup: any file as input (fixtures)

Flow: launch the calculator, generate a hash first (the STATE gate on
the export: at least one hash generated with "Save result to History"
on, which is the default in settings.xml), then open Settings from
the action bar, tap "Export user data", and confirm the suggested
zip destination in the system CREATE_DOCUMENT picker with Save; the
result callback copies the user-data zip through copyFile. The
generate-first steps are executed after the calculator is visible
and are attributed to gate edge E55287499; that edge is commented
again at its in-order position. The activity class is the manifest
package (com.smlnskgmail.jaman.hashchecker) plus .MainActivity,
launched under the flavor applicationId passed as --package.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner

EDGES = ["E372472a8", "E3101d0cd", "Edeb6bd90", "E56501d6f", "E9e141121",
         "E3755babd", "E9574aba4", "E3ac2e1c9", "E59c1e403", "E79b435a7",
         "E98e98419", "E30bb0ca3", "E58fc7a37", "E0848626c", "Eed97dffc",
         "E329fd909", "Eb87d737f", "Edcfc9c0b", "E86345c53", "E55287499",
         "E3ce12de4", "Eeef8c2a2", "E8654d3ef", "E8dd93771"]


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

    runner = Runner(package=args.package, route="route_15", edge_ids=EDGES,
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
        # STATE setup for gate edge E55287499 (history must be
        # non-empty for saveUserData to return DONE): generate one
        # hash from text on the calculator. "Save result to History"
        # defaults to on (settings.xml), so generating saves a row.
        runner.tap("E55287499", res_id=rid("btn_generate_from"))
        runner.tap("E55287499", text="Text")
        runner.tap("E55287499", res_id=rid("et_dialog_input_text"))
        runner.type_text("hello", "E55287499")
        runner.tap("E55287499", res_id=rid("btn_dialog_input_text_add"))
        runner.tap("E55287499", res_id=rid("btn_hash_actions"))
        runner.tap("E55287499", text="Generate")
        # Generate runs an AsyncTask behind a progress dialog; the
        # generated field has no distinct text to assert, so confirm
        # the main screen is back before leaving for Settings.
        runner.wait_for("E55287499", text="Action", timeout=30)
        # E98e98419 S_MAIN_EMPTY -> MainActivity.onOptionsItemSelected@SETTINGS
        # Trigger: tap the Settings icon in the action bar
        # (menu_main.xml, menu_main_section_settings).
        runner.tap("E98e98419", res_id=rid("menu_main_section_settings"))
        # E30bb0ca3 onOptionsItemSelected@SETTINGS -> showFragment@SETTINGS
        # Trigger: showFragment(...).
        runner.comment("call: showFragment settings fragment", "E30bb0ca3")
        # E58fc7a37 showFragment@SETTINGS -> SettingsFragment.onAttach
        # Trigger: FragmentTransaction.commit(), the fragment is attached.
        runner.comment("lifecycle: settings fragment attached", "E58fc7a37")
        # E0848626c SettingsFragment.onAttach -> onCreatePreferences
        # Trigger: onCreate (PreferenceFragmentCompat: onCreatePreferences).
        runner.comment("lifecycle: settings onCreatePreferences", "E0848626c")
        # Eed97dffc onCreatePreferences -> SettingsFragment.onViewCreated
        # Trigger: onViewCreated.
        runner.comment("lifecycle: settings onViewCreated", "Eed97dffc")
        # E329fd909 SettingsFragment.onViewCreated -> SettingsFragment.onResume
        # Trigger: onStart -> onResume.
        runner.comment("lifecycle: settings onResume", "E329fd909")
        # Eb87d737f SettingsFragment.onResume -> S_SETTINGS
        # Trigger: the fragment is visible. Confirm the settings list.
        runner.wait_for("Eb87d737f", text="Export user data")
        # Edcfc9c0b S_SETTINGS -> SettingsFragment.lambda$initUserDataExport$3
        # Trigger: tap "Export user data" (settings.xml preference,
        # strings settings_title_export_user_data).
        runner.tap("Edcfc9c0b", text="Export user data")
        # E86345c53 lambda$initUserDataExport$3 -> SettingsPresenterImpl.saveUserData
        # Trigger: settingsPresenter.saveUserData().
        runner.comment("call: SettingsPresenterImpl.saveUserData", "E86345c53")
        # E55287499 saveUserData -> saveUserDataResult@DONE
        # Trigger: history has rows, result DONE with an
        # ACTION_CREATE_DOCUMENT intent. Gate satisfied by the
        # generate-first steps above.
        runner.comment("call: saveUserDataResult DONE (gate set above)",
                      "E55287499")
        # E3ce12de4 saveUserDataResult@DONE -> S_EXT_CREATE_ZIP
        # Trigger: startActivityForResult(ACTION_CREATE_DOCUMENT
        # application/zip).
        runner.comment("intent: ACTION_CREATE_DOCUMENT application/zip fired",
                      "E3ce12de4")
        # Eeef8c2a2 S_EXT_CREATE_ZIP -> onActivityResult@OK
        # Trigger: the user confirms the file name;
        # onActivityResult(FILE_CREATE, RESULT_OK, data). System
        # picker: confirm the suggested zip destination with Save.
        runner.tap("Eeef8c2a2", text="Save")
        # E8654d3ef onActivityResult@OK -> copyUserDataToUserFolder
        # Trigger: copyUserDataToUserFolder(data.getData()).
        runner.comment("call: copyUserDataToUserFolder", "E8654d3ef")
        # E8dd93771 copyUserDataToUserFolder -> SettingsFragment.copyFile
        # Trigger: direct call; the target method copies the zip.
        runner.comment("call: copyFile (target)", "E8dd93771")
    finally:
        runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
