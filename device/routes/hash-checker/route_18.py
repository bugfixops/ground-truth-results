"""Device replay script for route_18: FeedbackFragment.sendEmail.

Method: FeedbackFragment.sendEmail
Printed route: graphs/hash-checker/scratch/route_print/FeedbackFragment.sendEmail.txt
Edge ids (in route order): E372472a8, E3101d0cd, Edeb6bd90, E56501d6f, E9e141121, E3755babd, E9574aba4, E3ac2e1c9, E59c1e403, E79b435a7, E98e98419, E30bb0ca3, E58fc7a37, E0848626c, Eed97dffc, E329fd909, Eb87d737f, Ea2d6404c, E2829c319, E1f2a23a4, E0294f4af, E54b04060, E2a4171f8, E9197f285, E97f40c0a, Ebe2c70c8, Eb6930484, E76dc181f
Source (ROUTES.csv): FeedbackFragment.java:68-77,101-113
Permissions: none (ROUTES.csv permissions field is empty)
Fixtures: none
Setup: any file as input (fixtures)
Notes: Type a non-empty message in the feedback field, then tap Send; the presenter calls sendEmail. The email chooser that follows is outside this route.
The script is delivered in the helper directory; its final location is
device/routes/hash-checker/route_18.py, and the sys.path bootstrap below
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
    parser = argparse.ArgumentParser(description="Replay route_18 for hash-checker.")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    runner = Runner(
        package=args.package,
        route="route_18",
        edge_ids=['E372472a8', 'E3101d0cd', 'Edeb6bd90', 'E56501d6f', 'E9e141121', 'E3755babd', 'E9574aba4', 'E3ac2e1c9', 'E59c1e403', 'E79b435a7', 'E98e98419', 'E30bb0ca3', 'E58fc7a37', 'E0848626c', 'Eed97dffc', 'E329fd909', 'Eb87d737f', 'Ea2d6404c', 'E2829c319', 'E1f2a23a4', 'E0294f4af', 'E54b04060', 'E2a4171f8', 'E9197f285', 'E97f40c0a', 'Ebe2c70c8', 'Eb6930484', 'E76dc181f'],
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
    # Ea2d6404c
    runner.tap('Ea2d6404c', text='Feedback')
    # E2829c319
    runner.comment('Feedback preference click shows the feedback fragment; no separate action.', 'E2829c319')
    # E1f2a23a4
    runner.comment('FragmentManager attaches FeedbackFragment; no user action.', 'E1f2a23a4')
    # E0294f4af
    runner.comment('FragmentManager inflates the feedback layout; no user action.', 'E0294f4af')
    # E54b04060
    runner.comment('FeedbackFragment.onViewCreated runs; no user action.', 'E54b04060')
    # E2a4171f8
    runner.comment('onStart/onResume run; no user action.', 'E2a4171f8')
    # E9197f285
    runner.comment('Feedback screen visible; typing the message is the next edge.', 'E9197f285')
    # E97f40c0a
    runner.tap('E97f40c0a', res_id=args.package + ":id/et_feedback_message")
    runner.type_text("Replay test feedback", 'E97f40c0a')
    # Ebe2c70c8
    runner.tap('Ebe2c70c8', res_id=args.package + ':id/menu_action_send_feedback')
    # Eb6930484
    runner.comment('Send with a non-empty message calls presenter.sendFeedback; no separate action.', 'Eb6930484')
    # E76dc181f
    runner.comment('Presenter calls view.sendEmail; target reached by the Send tap above. The email chooser sendEmail then opens is outside this route, so the script ends here.', 'E76dc181f')
    runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
