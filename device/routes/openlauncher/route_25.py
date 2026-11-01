"""Device replay script for openlauncher route_25.

Method: FiveSecsDelayContentProvider.<init>
Edge ids, in ROUTES.csv order:
    Edb156ef1
Printed route file: graphs/openlauncher/scratch/overnight-20261101/
    scratch-outputs/routes_27_full.txt (FiveSecsDelayContentProvider
    section), cross-checked against
    graphs/openlauncher/out/openlauncher_trigger_graph.json and the
    verification.csv path row for this method.
Permissions: none (ROUTES.csv permissions cell empty).
Fixtures: none (ROUTES.csv fixtures cell empty).
Setup: none (ROUTES.csv setup cell empty).

Package: com.benny.openlauncher (AndroidManifest.xml package attribute).

PROVIDER NOTE (stated plainly): this route has no GUI steps and a single
edge. The provider is declared in AndroidManifest.xml:56-61
(com.benny.openlauncher.util.FiveSecsDelayContentProvider, enabled,
exported), and Android installs an app's manifest providers when its
process starts, before any component runs. Launching the app therefore
covers this route: the launch action below implements the process-start
edge, which is the provider's instantiation. The same launch also covers
route_24 (onCreate follows from attachInfo). No content call,
permission, or fixture is involved.
"""

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
# The script lives at device/routes/openlauncher/route_25.py, so the repo
# root is three directories up from the script's containing directory:
# openlauncher/ -> routes/ -> device/ -> repo root. (Four dirname calls
# in total counting _HERE: _HERE is already one level below routes/.)
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, REPO_ROOT)

from device.harness import Runner

EDGE_IDS = [
    "Edb156ef1",
]

INIT_COMPONENT = "com.benny.openlauncher/com.benny.openlauncher.activity.Init"


def main(argv=None):
    parser = argparse.ArgumentParser(description="openlauncher route_25")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    r = Runner(package=args.package, route="route_25", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)

    # Edb156ef1 -- The process installs the providers of its manifest
    # when it starts, before any component.
    # Launching any app component starts the process, which instantiates
    # the provider; the MAIN/LAUNCHER activity Init is launched. This
    # single launch is the whole route (see header note).
    r.launch(component=INIT_COMPONENT, edge="Edb156ef1")

    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
