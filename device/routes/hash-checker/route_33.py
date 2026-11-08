#!/usr/bin/env python3
"""Device replay script for hash-checker route_33.

Method: ThemeConfigImpl.setCurrentTheme
Printed route: graphs/hash-checker/scratch/route_print/ThemeConfigImpl.setCurrentTheme.txt
Edge ids (in route order):
    E372472a8 E3101d0cd Edeb6bd90 E56501d6f E9e141121 E3755babd
    E9574aba4 E3ac2e1c9 E59c1e403 E79b435a7 E98e98419 E30bb0ca3
    E58fc7a37 E0848626c Eed97dffc E329fd909 Eb87d737f E1db6de16
    Ecad76f66 E72b166f1 E24b40c53 E8269f4a6 Ea0ac28a2 Edcd0fa85
    Ebb7bdd23 Eeb86f308
Permissions: none
Fixtures: none
Setup: any file as input (fixtures)
Status in ROUTES.csv: scripted

Route story: launch, open Settings from the action bar, tap the Theme
preference, tap the OTHER theme in the sheet, and confirm the restart
dialog with OK; configureNewTheme() then calls setCurrentTheme().

Fresh-state assumption (run_app.sh clears the app before each route):
SharedPreferencesSettings.getSelectedTheme() defaults to Theme.DARK,
so the "other theme" tapped below is "Light"
(R.string.title_theme_light). If the current theme were already Light,
tapping Light would just dismiss the sheet and this route would not
reach setCurrentTheme.
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
    "E98e98419", "E30bb0ca3", "E58fc7a37", "E0848626c", "Eed97dffc",
    "E329fd909", "Eb87d737f", "E1db6de16", "Ecad76f66", "E72b166f1",
    "E24b40c53", "E8269f4a6", "Ea0ac28a2", "Edcd0fa85", "Ebb7bdd23",
    "Eeb86f308",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    runner = Runner(package=args.package, route="route_33", edge_ids=EDGES,
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
        # E98e98419 -- S_MAIN_EMPTY -> MainActivity.onOptionsItemSelected@SETTINGS:
        # menu_main.xml item menu_main_section_settings is
        # showAsAction="always", i.e. an icon-only action-bar button
        # whose title ("Settings", R.string.menu_title_settings) is
        # exposed as its content description, so tap by desc.
        runner.tap("E98e98419", desc="Settings")
        # E30bb0ca3 -- MainActivity.onOptionsItemSelected@SETTINGS -> MainActivity.showFragment@SETTINGS:
        # showFragment(new SettingsFragment()), no user action beyond
        # the menu tap above.
        runner.comment("showFragment(SettingsFragment)", "E30bb0ca3")
        # E58fc7a37 -- MainActivity.showFragment@SETTINGS -> SettingsFragment.onAttach:
        # FragmentManager lifecycle, no user action.
        runner.comment("FragmentManager attaches SettingsFragment",
                       "E58fc7a37")
        # E0848626c -- SettingsFragment.onAttach -> SettingsFragment.onCreatePreferences:
        # FragmentManager lifecycle, no user action.
        runner.comment("SettingsFragment.onCreatePreferences", "E0848626c")
        # Eed97dffc -- SettingsFragment.onCreatePreferences -> SettingsFragment.onViewCreated:
        # FragmentManager lifecycle, no user action.
        runner.comment("SettingsFragment.onViewCreated", "Eed97dffc")
        # E329fd909 -- SettingsFragment.onViewCreated -> SettingsFragment.onResume:
        # FragmentManager lifecycle, no user action.
        runner.comment("SettingsFragment.onResume", "E329fd909")
        # Eb87d737f -- SettingsFragment.onResume -> S_SETTINGS:
        # settings screen entered; wait for the Theme preference row
        # (res/xml/settings.xml, title R.string.settings_title_theme).
        runner.wait_for("Eb87d737f", text="Theme")
        # E1db6de16 -- S_SETTINGS -> SettingsFragment.lambda$initThemeSettings$1:
        # tap the Theme preference (trigger text: Tap "Theme").
        runner.tap("E1db6de16", text="Theme")
        # Ecad76f66 -- SettingsFragment.lambda$initThemeSettings$1 -> S_SHEET_THEMES:
        # ThemesBottomSheet entered; wait for the Light row to prove
        # the sheet (Theme.values() = Light, Dark) is showing.
        runner.wait_for("Ecad76f66", text="Light")
        # E72b166f1 -- S_SHEET_THEMES -> BaseListHolder.lambda$bind$0@THEME_OTHER:
        # tap the other theme. Fresh state current theme is DARK, so
        # the other theme is "Light" (see module docstring).
        runner.tap("E72b166f1", text="Light")
        # E24b40c53 -- BaseListHolder.lambda$bind$0@THEME_OTHER -> ThemesListAdapter$ThemesListHolder.callItemClick@OTHER:
        # item click handler; not the current theme, so it shows the
        # apply dialog instead of dismissing the sheet.
        runner.comment("callItemClick for the non-current theme",
                       "E24b40c53")
        # E8269f4a6 -- ThemesListAdapter$ThemesListHolder.callItemClick@OTHER -> ThemesListAdapter$ThemesListHolder.showThemeApplyDialog:
        # AppAlertDialog with title Warning, message
        # R.string.message_change_theme, positive button OK.
        runner.comment("showThemeApplyDialog()", "E8269f4a6")
        # Ea0ac28a2 -- ThemesListAdapter$ThemesListHolder.showThemeApplyDialog -> S_DLG_CHANGE_THEME:
        # change-theme dialog entered; wait for its OK button.
        runner.wait_for("Ea0ac28a2", text="OK")
        # Edcd0fa85 -- S_DLG_CHANGE_THEME -> ThemesListAdapter$ThemesListHolder.lambda$showThemeApplyDialog$0:
        # tap OK (trigger text: Tap "OK").
        runner.tap("Edcd0fa85", text="OK")
        # Ebb7bdd23 -- ThemesListAdapter$ThemesListHolder.lambda$showThemeApplyDialog$0 -> ThemesListAdapter$ThemesListHolder.configureNewTheme:
        # dialog positive-button handler calls configureNewTheme().
        runner.comment("dialog handler calls configureNewTheme()",
                       "Ebb7bdd23")
        # Eeb86f308 -- ThemesListAdapter$ThemesListHolder.configureNewTheme -> ThemeConfigImpl.setCurrentTheme:
        # configureNewTheme() calls themeConfig.setCurrentTheme().
        # The handler then restarts the app, so wait for the main
        # screen to come back (longer timeout for the restart).
        runner.comment("configureNewTheme() calls setCurrentTheme()",
                       "Eeb86f308")
        runner.wait_for("Eeb86f308",
                        res_id=args.package + ":id/btn_generate_from",
                        timeout=30)
    finally:
        runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
