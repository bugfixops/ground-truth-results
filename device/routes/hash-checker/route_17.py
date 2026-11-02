"""Device replay script for route_17: HashCalculatorFragment.folderNameFromUri.

Method: HashCalculatorFragment.folderNameFromUri
Printed route: graphs/hash-checker/scratch/route_print/HashCalculatorFragment.folderNameFromUri.txt
Edge ids (in route order): E372472a8, E3101d0cd, Edeb6bd90, E56501d6f, E9e141121, E3755babd, E9574aba4, E3ac2e1c9, E59c1e403, E79b435a7, Ee69c0c42, E2c58a33d, E4b06b3e0, Ed95ead38, E93d7aec9, E14efb922, E799c45d6, E1f654e2a, E4d8290b8, E3d90ec2f
Source (ROUTES.csv): HashCalculatorFragment.java:330,350-352
Permissions: none (ROUTES.csv permissions field is empty)
Fixtures: Pictures
Setup: any file as input (fixtures)
Notes: Pick the Pictures folder itself in the system folder picker; folderNameFromUri derives the folder name from the picked folder URI.
The script is delivered in the helper directory; its final location is
device/routes/hash-checker/route_17.py, and the sys.path bootstrap below
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
    parser = argparse.ArgumentParser(description="Replay route_17 for hash-checker.")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    runner = Runner(
        package=args.package,
        route="route_17",
        edge_ids=['E372472a8', 'E3101d0cd', 'Edeb6bd90', 'E56501d6f', 'E9e141121', 'E3755babd', 'E9574aba4', 'E3ac2e1c9', 'E59c1e403', 'E79b435a7', 'Ee69c0c42', 'E2c58a33d', 'E4b06b3e0', 'Ed95ead38', 'E93d7aec9', 'E14efb922', 'E799c45d6', 'E1f654e2a', 'E4d8290b8', 'E3d90ec2f'],
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
    # Ee69c0c42
    runner.tap('Ee69c0c42', res_id=args.package + ':id/btn_generate_from')
    # E2c58a33d
    runner.tap('E2c58a33d', text='Folder')
    # E4b06b3e0
    runner.comment('Row tap dispatches to ActionHolder.callItemClick; no separate action.', 'E4b06b3e0')
    # Ed95ead38
    runner.comment('callItemClick dispatches to userActionSelect; no separate action.', 'Ed95ead38')
    # E93d7aec9
    runner.comment('userActionSelect SEARCH_FOLDER case opens the system folder manager; no separate action.', 'E93d7aec9')
    # E14efb922
    runner.comment('System folder picker opens; the pick itself is the next edge.', 'E14efb922')
    # E799c45d6
    runner.scroll_to('E799c45d6', text="Pictures")
    runner.tap('E799c45d6', text="Pictures")
    runner.tap('E799c45d6', text="Use this folder")
    # E1f654e2a
    runner.comment('onActivityResult FOLDER_SELECT switch dispatches to selectFolderFromSystemFileManager; no separate action.', 'E1f654e2a')
    # E4d8290b8
    runner.comment('selectFolderFromSystemFileManager calls validateSelectedFolder; no separate action.', 'E4d8290b8')
    # E3d90ec2f
    runner.comment('validateSelectedFolder calls folderNameFromUri; target reached when the folder result returns.', 'E3d90ec2f')
    runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
