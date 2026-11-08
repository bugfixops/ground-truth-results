#!/usr/bin/env python3
"""Replay script for hash-checker route_10.

Method: OrmLiteLocalDataStorage.getDatabaseFileName
Edge ids (exact, from ROUTES.csv, in route order):
    E372472a8 E3101d0cd Edeb6bd90 E56501d6f E9e141121 E3755babd
    E9574aba4 E3ac2e1c9 E59c1e403 E79b435a7 E98e98419 E30bb0ca3
    E58fc7a37 E0848626c Eed97dffc E329fd909 Eb87d737f Edcfc9c0b
    E86345c53 E55287499 E3ce12de4 Eeef8c2a2 E8654d3ef Ecb285e36
    Ef5b3d546
Printed route file:
    graphs/hash-checker/scratch/route_print/OrmLiteLocalDataStorage.getDatabaseFileName.txt
Permissions: (none)
Fixtures: (none; output-only ACTION_CREATE_DOCUMENT export)
Setup: any file as input (fixtures)

Flow: launch, then the STATE (data) gate, then the route proper: tap
the Settings action-bar item, tap "Export user data", and confirm the
output destination in the system save picker (ACTION_CREATE_DOCUMENT,
application/zip, suggested name hash_checker_user_data.zip). The
export copies the database through LocalDataExporter.exportDatabase,
which calls getDatabaseFileName.

STATE (data) gate, produced in-app with no fixture: the export only
reaches DONE when history has rows. Note the misnamed predicate:
OrmLiteLocalDataStorage.isHistoryItemsListIsEmpty() returns
getDao(HistoryItem.class).countOf() > 0, i.e. true exactly when rows
exist, and SettingsPresenterImpl.saveUserData takes the DONE branch
on that true value. run_app.sh clears the app before the script, so
history starts empty. The gate is made by generating one hash from
text: From -> "Text" -> type "hash-checker" -> Add -> Action ->
Generate. Saving to history is on by default, and the first
generation on a cleared app does not pop the rate-app dialog (it only
shows when the generation count equals 5). No route edge covers this
preparation, so it is folded into the E79b435a7 block (the calculator
screen on which it happens, before the Settings item is tapped) and is
marked STATE there, not presented as the E79b435a7 trigger itself.

The save picker is output-only: there is no input fixture to pick.
Its filename field is prefilled by the intent's EXTRA_TITLE, so the
script only confirms with "Save".

Every action carries one of this route's edge ids (the harness raises
for any other id). Lifecycle / call edges with no user action are
recorded with runner.comment.

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


def tap_menu(runner, edge, desc, res_id):
    """Tap an icon-only action-bar item by content-desc, else by id."""
    try:
        runner.tap(edge, desc=desc)
    except LookupError:
        runner.tap(edge, res_id=res_id)


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
        package=args.package, route="route_10",
        edge_ids=["E372472a8", "E3101d0cd", "Edeb6bd90", "E56501d6f",
                  "E9e141121", "E3755babd", "E9574aba4", "E3ac2e1c9",
                  "E59c1e403", "E79b435a7", "E98e98419", "E30bb0ca3",
                  "E58fc7a37", "E0848626c", "Eed97dffc", "E329fd909",
                  "Eb87d737f", "Edcfc9c0b", "E86345c53", "E55287499",
                  "E3ce12de4", "Eeef8c2a2", "E8654d3ef", "Ecb285e36",
                  "Ef5b3d546"],
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
        # STATE (data), folded here: generate one hash from text so that
        # history has at least one row (see header note on the misnamed
        # isHistoryItemsListIsEmpty predicate). From -> "Text"
        # (dialog_text_input.xml, title "Add text") -> type text -> "Add"
        # -> Action sheet -> "Generate". The hash task callback saves the
        # row because save-to-history defaults on.
        runner.tap("E79b435a7",
                   res_id=pkg + ":id/btn_generate_from")
        runner.tap("E79b435a7", text="Text")
        runner.tap("E79b435a7",
                   res_id=pkg + ":id/et_dialog_input_text")
        runner.type_text("hash-checker", "E79b435a7")
        runner.tap("E79b435a7",
                   res_id=pkg + ":id/btn_dialog_input_text_add")
        runner.tap("E79b435a7",
                   res_id=pkg + ":id/btn_hash_actions")
        runner.tap("E79b435a7", text="Generate")
        # E98e98419: S_MAIN_EMPTY -> MainActivity.onOptionsItemSelected@SETTINGS
        # Trigger: tap the Settings icon in the action bar
        # (menu_main.xml menu_main_section_settings, title "Settings").
        tap_menu(runner, "E98e98419", "Settings",
                 pkg + ":id/menu_main_section_settings")
        # E30bb0ca3: MainActivity.onOptionsItemSelected@SETTINGS
        #   -> MainActivity.showFragment@SETTINGS
        # Call: MainActivity.java:130.
        runner.comment("call: showFragment SettingsFragment", "E30bb0ca3")
        # E58fc7a37: MainActivity.showFragment@SETTINGS -> SettingsFragment.onAttach
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: SettingsFragment.onAttach", "E58fc7a37")
        # E0848626c: SettingsFragment.onAttach
        #   -> SettingsFragment.onCreatePreferences
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: SettingsFragment.onCreatePreferences",
                       "E0848626c")
        # Eed97dffc: SettingsFragment.onCreatePreferences
        #   -> SettingsFragment.onViewCreated
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: SettingsFragment.onViewCreated", "Eed97dffc")
        # E329fd909: SettingsFragment.onViewCreated -> SettingsFragment.onResume
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: SettingsFragment.onResume", "E329fd909")
        # Eb87d737f: SettingsFragment.onResume -> S_SETTINGS
        # The fragment is visible: the settings list.
        runner.wait_for("Eb87d737f", text="Export user data")
        # Edcfc9c0b: S_SETTINGS -> SettingsFragment.lambda$initUserDataExport$3
        # Trigger: tap the "Export user data" preference row
        # (settings.xml key_export_user_data, title
        # settings_title_export_user_data).
        runner.tap("Edcfc9c0b", text="Export user data")
        # E86345c53: SettingsFragment.lambda$initUserDataExport$3
        #   -> SettingsPresenterImpl.saveUserData
        # Call: SettingsFragment.java:198.
        runner.comment("call: SettingsPresenterImpl.saveUserData", "E86345c53")
        # E55287499: SettingsPresenterImpl.saveUserData
        #   -> SettingsFragment.saveUserDataResult@DONE
        # Call: SettingsPresenterImpl.java:44-50; guard countOf() > 0 holds
        # because of the STATE text hash above (see header note).
        runner.comment("call: saveUserDataResult DONE", "E55287499")
        # E3ce12de4: SettingsFragment.saveUserDataResult@DONE -> S_EXT_CREATE_ZIP
        # startActivityForResult(ACTION_CREATE_DOCUMENT, application/zip)
        # (SettingsFragment.java:293-295).
        runner.comment("enters: system save picker (zip export)", "E3ce12de4")
        # Eeef8c2a2: S_EXT_CREATE_ZIP -> SettingsFragment.onActivityResult@OK
        # Trigger: the user confirms the file name
        # (onActivityResult(FILE_CREATE, RESULT_OK, data)). The filename
        # is prefilled as hash_checker_user_data.zip by EXTRA_TITLE, so
        # confirming is a single "Save" tap; no fixture is picked.
        runner.wait_for("Eeef8c2a2", text="Save")
        runner.tap("Eeef8c2a2", text="Save")
        # E8654d3ef: SettingsFragment.onActivityResult@OK
        #   -> SettingsFragment.copyUserDataToUserFolder
        # Call: SettingsFragment.java:121-123.
        runner.comment("call: copyUserDataToUserFolder", "E8654d3ef")
        # Ecb285e36: SettingsFragment.copyUserDataToUserFolder
        #   -> LocalDataExporter.exportDatabase
        # Call: SettingsFragment.java:129.
        runner.comment("call: LocalDataExporter.exportDatabase", "Ecb285e36")
        # Ef5b3d546: LocalDataExporter.exportDatabase
        #   -> OrmLiteLocalDataStorage.getDatabaseFileName  [TARGET]
        # Call: LocalDataExporter.java:26 (bytecode); virtual/interface
        # dispatch to the ORMLite implementation.
        runner.comment("target: OrmLiteLocalDataStorage.getDatabaseFileName",
                       "Ef5b3d546")
    finally:
        runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
