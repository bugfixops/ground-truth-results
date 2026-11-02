"""Device replay script for route_20: AppSnackbar.lambda$show$0.

Method: AppSnackbar.lambda$show$0
Printed route: graphs/hash-checker/scratch/route_print/AppSnackbar.lambda_show_0.txt
Edge ids (in route order): E372472a8, E3101d0cd, Edeb6bd90, E56501d6f, E9e141121, E3755babd, E9574aba4, E3ac2e1c9, E59c1e403, E79b435a7, Ef56672b6, Ef7f7e606, Ef7b0cfbc, E222f5cf5, E0f3fef6d, E33503f59, E937eadef, Ed873a5de, E8cb7fbf2
Source (ROUTES.csv): AppSnackbar.java:62-71
Permissions: none (ROUTES.csv permissions field is empty)
Fixtures: none
Setup: any file as input (fixtures)
Notes: On a fresh calculator screen (no source selected: fileUri == null, folderUri == null, text not selected), tap Generate, then tap OK on the info snackbar.
The script is delivered in the helper directory; its final location is
device/routes/hash-checker/route_20.py, and the sys.path bootstrap below
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
    parser = argparse.ArgumentParser(description="Replay route_20 for hash-checker.")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    runner = Runner(
        package=args.package,
        route="route_20",
        edge_ids=['E372472a8', 'E3101d0cd', 'Edeb6bd90', 'E56501d6f', 'E9e141121', 'E3755babd', 'E9574aba4', 'E3ac2e1c9', 'E59c1e403', 'E79b435a7', 'Ef56672b6', 'Ef7f7e606', 'Ef7b0cfbc', 'E222f5cf5', 'E0f3fef6d', 'E33503f59', 'E937eadef', 'Ed873a5de', 'E8cb7fbf2'],
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
    # Ef56672b6
    runner.tap('Ef56672b6', res_id=args.package + ':id/btn_hash_actions')
    # Ef7f7e606
    runner.tap('Ef7f7e606', text='Generate')
    # Ef7b0cfbc
    runner.comment('Row tap dispatches to ActionHolder.callItemClick; no separate action.', 'Ef7b0cfbc')
    # E222f5cf5
    runner.comment('callItemClick dispatches to userActionSelect; no separate action.', 'E222f5cf5')
    # E0f3fef6d
    runner.comment('userActionSelect GENERATE_HASH case calls generateHash; no separate action.', 'E0f3fef6d')
    # E33503f59
    runner.comment('Fresh screen: fileUri and folderUri are null and no text is selected, so generateHash shows the select-object snackbar; no separate action.', 'E33503f59')
    # E937eadef
    runner.comment('showSnackbarWithoutAction creates an AppSnackbar and shows it; no separate action.', 'E937eadef')
    # Ed873a5de
    runner.comment('Info snackbar shown with the OK action (no custom action); the OK tap is the next edge.', 'Ed873a5de')
    # E8cb7fbf2
    runner.tap('E8cb7fbf2', text='OK')
    runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
