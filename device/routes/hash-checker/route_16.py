"""Device replay script for route_16: HashCalculatorTask.<init>(Context,HashType,Uri,Uri,HashCalculatorTaskTarget).

Method: HashCalculatorTask.<init>(Context,HashType,Uri,Uri,HashCalculatorTaskTarget)
Printed route: graphs/hash-checker/scratch/route_print/HashCalculatorTask.<init>(Context,HashType,Uri,Uri,HashCalculatorTaskTarget).txt
Edge ids (in route order): E372472a8, E3101d0cd, Edeb6bd90, E56501d6f, E9e141121, E3755babd, E9574aba4, E3ac2e1c9, E59c1e403, E79b435a7, Ee69c0c42, Ed943ca35, E8c979876, Eff786918, E12829a50, Ef6dc9320, Eb99504ff, E1e4be207, Ef5562ab9, Ec8413c27, E0dbeffc7, E915e31df, E84eade87, E00a75033, Ed6d6a6fb, Edd386c8e
Source (ROUTES.csv): HashCalculatorFragment.java:227-234
Permissions: none (ROUTES.csv permissions field is empty)
Fixtures: Download/todo.txt
Setup: any file as input (fixtures)
Notes: Pick todo.txt in the system file picker, then tap Generate with the file as source (fileUri != null guard).
The script is delivered in the helper directory; its final location is
device/routes/hash-checker/route_16.py, and the sys.path bootstrap below
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
    parser = argparse.ArgumentParser(description="Replay route_16 for hash-checker.")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    runner = Runner(
        package=args.package,
        route="route_16",
        edge_ids=['E372472a8', 'E3101d0cd', 'Edeb6bd90', 'E56501d6f', 'E9e141121', 'E3755babd', 'E9574aba4', 'E3ac2e1c9', 'E59c1e403', 'E79b435a7', 'Ee69c0c42', 'Ed943ca35', 'E8c979876', 'Eff786918', 'E12829a50', 'Ef6dc9320', 'Eb99504ff', 'E1e4be207', 'Ef5562ab9', 'Ec8413c27', 'E0dbeffc7', 'E915e31df', 'E84eade87', 'E00a75033', 'Ed6d6a6fb', 'Edd386c8e'],
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
    # Ed943ca35
    runner.tap('Ed943ca35', text='File')
    # E8c979876
    runner.comment('Row tap dispatches to ActionHolder.callItemClick; no separate action.', 'E8c979876')
    # Eff786918
    runner.comment('callItemClick dispatches to userActionSelect; no separate action.', 'Eff786918')
    # E12829a50
    runner.comment('userActionSelect SEARCH_FILE case opens the system file manager; no separate action.', 'E12829a50')
    # Ef6dc9320
    runner.comment('System file picker opens; the pick itself is the next edge.', 'Ef6dc9320')
    # Eb99504ff
    runner.scroll_to('Eb99504ff', text="todo.txt")
    runner.tap('Eb99504ff', text="todo.txt")
    # E1e4be207
    runner.comment('onActivityResult FILE_SELECT switch dispatches to selectFileFromSystemFileManager; no separate action.', 'E1e4be207')
    # Ef5562ab9
    runner.comment('selectFileFromSystemFileManager calls validateSelectedFile; no separate action.', 'Ef5562ab9')
    # Ec8413c27
    runner.comment('File becomes the source; calculator screen now shows the picked file.', 'Ec8413c27')
    # E0dbeffc7
    runner.tap('E0dbeffc7', res_id=args.package + ':id/btn_hash_actions')
    # E915e31df
    runner.tap('E915e31df', text='Generate')
    # E84eade87
    runner.comment('Row tap dispatches to ActionHolder.callItemClick; no separate action.', 'E84eade87')
    # E00a75033
    runner.comment('callItemClick dispatches to userActionSelect; no separate action.', 'E00a75033')
    # Ed6d6a6fb
    runner.comment('userActionSelect GENERATE_HASH case calls generateHash; no separate action.', 'Ed6d6a6fb')
    # Edd386c8e
    runner.comment('generateHash with fileUri != null constructs HashCalculatorTask; target reached by the Generate tap above.', 'Edd386c8e')
    runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
