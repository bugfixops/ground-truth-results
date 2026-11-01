"""Device replay script for openlauncher route_24.

Method: FiveSecsDelayContentProvider.onCreate
Edge ids, in ROUTES.csv order:
    Edb156ef1 Ea9707b85
Printed route file: graphs/openlauncher/scratch/overnight-20261101/
    scratch-outputs/routes_27_full.txt (FiveSecsDelayContentProvider
    section), cross-checked against
    graphs/openlauncher/out/openlauncher_trigger_graph.json and the
    verification.csv path row for this method.
Permissions: none (ROUTES.csv permissions cell empty).
Fixtures: none (ROUTES.csv fixtures cell empty).
Setup: none (ROUTES.csv setup cell empty).

Package: com.benny.openlauncher (AndroidManifest.xml package attribute).

PROVIDER NOTE (stated plainly): this route has no GUI steps. The provider
is declared in AndroidManifest.xml:56-61
(com.benny.openlauncher.util.FiveSecsDelayContentProvider, enabled,
exported), and Android installs an app's manifest providers when its
process starts, before any component runs. Launching the app therefore
covers both this route and route_25: the launch action below implements
the process-start edge, and onCreate follows from attachInfo with no
further step. No content call, permission, or fixture is involved.
"""

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
# The script lives at device/routes/openlauncher/route_24.py, so the repo
# root is three directories up from the script's containing directory:
# openlauncher/ -> routes/ -> device/ -> repo root. (Four dirname calls
# in total counting _HERE: _HERE is already one level below routes/.)
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, REPO_ROOT)

from device.harness import Runner

EDGE_IDS = [
    "Edb156ef1", "Ea9707b85",
]

INIT_COMPONENT = "com.benny.openlauncher/com.benny.openlauncher.activity.Init"


def main(argv=None):
    parser = argparse.ArgumentParser(description="openlauncher route_24")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    r = Runner(package=args.package, route="route_24", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)

    # Edb156ef1 -- The process installs the providers of its manifest
    # when it starts, before any component.
    # Launching any app component starts the process, which installs the
    # provider; the MAIN/LAUNCHER activity Init is launched. This single
    # launch covers both route_24 and route_25 (see header note).
    r.launch(component=INIT_COMPONENT, edge="Edb156ef1")

    # Ea9707b85 -- ContentProvider.attachInfo calls onCreate
    # (util/FiveSecsDelayContentProvider.java:19-22, returns true).
    # Lifecycle edge driven by the framework at process start; no user
    # action and no GUI step.
    r.comment("attachInfo calls provider onCreate at process start; "
              "no user action", "Ea9707b85")

    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
