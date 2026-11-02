"""Device replay script for route_19: SharedPreferencesSettings.saveTheme.

Method: SharedPreferencesSettings.saveTheme
Printed route: graphs/hash-checker/scratch/route_print/SharedPreferencesSettings.saveTheme.txt
Edge ids (in route order): E372472a8, E3101d0cd, Edeb6bd90, E56501d6f, E9e141121, E3755babd, E9574aba4, E3ac2e1c9, E59c1e403, E79b435a7, E98e98419, E30bb0ca3, E58fc7a37, E0848626c, Eed97dffc, E329fd909, Eb87d737f, E1db6de16, Ecad76f66, E72b166f1, E24b40c53, E8269f4a6, Ea0ac28a2, Edcd0fa85, Ebb7bdd23, Eeb86f308, Edfdf2f07
Source (ROUTES.csv): SharedPreferencesSettings.java:128-147; ThemeConfigImpl.java:30
Permissions: none (ROUTES.csv permissions field is empty)
Fixtures: none
Setup: any file as input (fixtures)
Notes: Tap the Theme preference, tap the other theme, then tap OK on the restart-warning dialog. On a cleared install the default theme is DARK (SharedPreferencesSettings.getTheme default), so the other theme is Light.
The script is delivered in the helper directory; its final location is
device/routes/hash-checker/route_19.py, and the sys.path bootstrap below
is written for that final location (three levels up from
device/routes/hash-checker/ is the repo root). No data clearing, fixture push, or permission grant happens here:
run_app.sh does those before invoking this script. First action is launch of MainActivity; the
manifest package is com.smlnskgmail.jaman.hashchecker and .MainActivity
is its activity class, launched under the flavor applicationId passed
as --package.
"""

import argparse
import os
import sys

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_SCRIPT_DIR)))
sys.path.insert(0, _REPO_ROOT)

from device.harness.harness import Runner


def main(argv=None):
    parser = argparse.ArgumentParser(description="Replay route_19 for hash-checker.")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    runner = Runner(
        package=args.package,
        route="route_19",
        edge_ids=['E372472a8', 'E3101d0cd', 'Edeb6bd90', 'E56501d6f', 'E9e141121', 'E3755babd', 'E9574aba4', 'E3ac2e1c9', 'E59c1e403', 'E79b435a7', 'E98e98419', 'E30bb0ca3', 'E58fc7a37', 'E0848626c', 'Eed97dffc', 'E329fd909', 'Eb87d737f', 'E1db6de16', 'Ecad76f66', 'E72b166f1', 'E24b40c53', 'E8269f4a6', 'Ea0ac28a2', 'Edcd0fa85', 'Ebb7bdd23', 'Eeb86f308', 'Edfdf2f07'],
        log_path=args.log,
        dry_run=args.dry_run,
        adb=args.adb,
    )
    # E372472a8
    runner.launch(args.package + "/com.smlnskgmail.jaman.hashchecker.MainActivity", 'E372472a8')
    # E3101d0cd
    runner.comment('System instantiates MainActivity, then calls onCreate.', 'E3101d0cd')
    # Edeb6bd90
    runner.comment('super.onCreate runs (BaseActivity.onCreate); no user action.', 'Edeb6bd90')
    # E56501d6f
    runner.comment('BaseActivity.onCreate calls MainActivity.create; no user action.', 'E56501d6f')
    # E9e141121
    runner.comment('create() adds the calculator fragment; no user action.', 'E9e141121')
    # E3755babd
    runner.comment('FragmentManager attaches HashCalculatorFragment; no user action.', 'E3755babd')
    # E9574aba4
    runner.comment('FragmentManager inflates the calculator layout; no user action.', 'E9574aba4')
    # E3ac2e1c9
    runner.comment('onViewCreated runs; no user action.', 'E3ac2e1c9')
    # E59c1e403
    runner.comment('onStart/onResume run; no user action.', 'E59c1e403')
    # E79b435a7
    runner.wait_for('E79b435a7', res_id=args.package + ':id/btn_generate_from')
    # E98e98419
    runner.tap('E98e98419', res_id=args.package + ':id/menu_main_section_settings')
    # E30bb0ca3
    runner.comment('onOptionsItemSelected SETTINGS case shows the settings fragment; no separate action.', 'E30bb0ca3')
    # E58fc7a37
    runner.comment('FragmentManager attaches SettingsFragment; no user action.', 'E58fc7a37')
    # E0848626c
    runner.comment('PreferenceFragmentCompat onCreatePreferences runs; no user action.', 'E0848626c')
    # Eed97dffc
    runner.comment('SettingsFragment.onViewCreated runs; no user action.', 'Eed97dffc')
    # E329fd909
    runner.comment('SettingsFragment.onResume runs; no user action.', 'E329fd909')
    # Eb87d737f
    runner.wait_for('Eb87d737f', text='Theme')
    # E1db6de16
    runner.tap('E1db6de16', text='Theme')
    # Ecad76f66
    runner.comment('Theme preference click opens the themes bottom sheet; no separate action.', 'Ecad76f66')
    # E72b166f1
    runner.tap('E72b166f1', text='Light')
    # E24b40c53
    runner.comment('Row tap dispatches to ThemesListHolder.callItemClick; no separate action.', 'E24b40c53')
    # E8269f4a6
    runner.comment('A different theme was tapped, so showThemeApplyDialog runs; no separate action.', 'E8269f4a6')
    # Ea0ac28a2
    runner.comment('Restart-warning dialog shown; the OK tap is the next edge.', 'Ea0ac28a2')
    # Edcd0fa85
    runner.tap('Edcd0fa85', text='OK')
    # Ebb7bdd23
    runner.comment('Dialog positive click calls configureNewTheme; no separate action.', 'Ebb7bdd23')
    # Eeb86f308
    runner.comment('configureNewTheme calls themeConfig.setCurrentTheme; no separate action.', 'Eeb86f308')
    # Edfdf2f07
    runner.comment('setCurrentTheme calls saveTheme; target reached by the OK tap above. The app restart that follows the dialog dismiss is outside this route.', 'Edfdf2f07')
    runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
