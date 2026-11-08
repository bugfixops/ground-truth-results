#!/usr/bin/env python3
"""Device replay script for openlauncher route_27.

Method: Init.<init>
Edge ids (ROUTES.csv order): E3a1527b1
Printed route: graphs/openlauncher/verification.csv path row for
    Init.<init> (1 step: the launcher entry instantiates Init), edge
    detail in graphs/openlauncher/out/openlauncher_trigger_graph.json,
    and step 1 of the shared launch prefix printed in
    graphs/openlauncher/scratch/overnight-20261101/scratch-outputs/routes_27_full.txt.
    (No per-method route_print file exists for openlauncher; the
    verification.csv path row plus the trigger graph are the printed route.)
Permissions: none (ROUTES.csv permissions cell is empty; no route edge
    names a permission gate).
Fixtures: none (ROUTES.csv fixtures cell is empty).
Setup: none (ROUTES.csv setup cell is empty; openlauncher has no setup).

Special case: Init is the MAIN + LAUNCHER entry activity
(AndroidManifest.xml:28-36). This route has a single edge whose
destination is Init.<init> itself, so launching the component IS the
route: there is no second, lifecycle edge to comment on (contrast
route_26, which adds E996c92b8 for onCreate). No pm clear,
permission grant, fixture push, or setup is done here:
device/run_app.sh does those before invoking this script.
"""

import argparse
import os
import sys

# Three levels up from the script's directory (device/routes/openlauncher
# -> device/routes -> device -> repo root). Counted from __file__ itself
# that is four dirname calls: the first gives the containing directory.
# A literal three dirname calls on __file__ lands on device/ itself,
# under which "device.harness" does not resolve (verified by a failed
# dry run before this fix); see REPORT.md.
_HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, REPO_ROOT)

from device.harness import Runner  # noqa: E402

COMPONENT = "com.benny.openlauncher/com.benny.openlauncher.activity.Init"


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    r = Runner(package=args.package, route="route_27",
               edge_ids=["E3a1527b1"],
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)

    # Edge E3a1527b1 (S_ENTRY -> Init.<init>): "Tap the OpenLauncher
    # icon in another launcher (MAIN + LAUNCHER filter), or adb monkey
    # / am start". The icon lives in another launcher's home screen,
    # whose layout is not this app's layout, so there is no app
    # resource-id/text/content-desc to tap; am start -n on the
    # MAIN + LAUNCHER component (AndroidManifest.xml:28-36) is the
    # adb equivalent the trigger text itself names, and instantiating
    # Init is exactly what this edge's destination requires.
    r.launch(COMPONENT, edge="E3a1527b1")

    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
