"""MMEX route_28: SyncPreferences.getUploadImmediately.

Method: SyncPreferences.getUploadImmediately
Edge ids (in route order):
    E71c76102 E2e074fc1 E1975beaa Ece87d249 E2409594a Ef6bd6929
    Ef8378602 Ee260f9b8
Printed route source:
    graphs/MMEX/scratch/route_print_final2/SyncPreferences.getUploadImmediately.txt
    (8 steps; edges above verified identical to the verification.csv
    path row for SyncPreferences.getUploadImmediately).
Permissions: none (print header env=-, so no ENV permission gate;
    no permission is granted by this script).
Fixtures: none (print header state=-; no STATE file gate; no
    $WEMU/fixtures file is needed).
Setup: none (apps.csv MMEX setup is "none (minSdk 22)").
State precondition NOT created by this script (read before replay):
    MainActivity.onCreate reaches the UID block only after
    showPrerequisite() returns false (home/MainActivity.java:184-187;
    tutorial already dismissed and a valid database already
    configured). The UID block then calls setInfoValue only when no
    UID is stored (home/MainActivity.java:228-233), but the route
    continues through the UPDATE path only when the UID info row
    already exists (servicelayer/InfoService.java:139, :144-145) --
    i.e. in practice a second launch after a first run stored the
    row, not a fresh pm-clear launch. The tail then requires sync
    configured: isSyncEnabled(), a non-empty remote path, automatic
    upload not disabled, and canSync() (network available)
    (sync/SyncManager.java:131-149). Configuring a remote path is a
    sync setup step outside this route's edges; if that setup needs
    a real online account, the merger/auditor must reclassify this
    route -- on the printed evidence alone the tail is a local
    preference read (settings/SyncPreferences.java:71) with no
    credential named. No tap is invented for any of this.
    The remaining edges are internal calls with no user action, so
    they are comment-only below.
Run (from the repo root, once placed in device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_28.py --package
    com.money.manager.ex --log steps/route_28.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E1975beaa", "Ece87d249", "E2409594a",
    "Ef6bd6929", "Ef8378602", "Ee260f9b8",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_28", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E71c76102: Launch the MAIN/LAUNCHER activity.
        # AndroidManifest.xml:136-143 (.home.MainActivity, MAIN +
        # LAUNCHER intent filter).
        r.launch("com.money.manager.ex/.home.MainActivity",
                 edge="E71c76102")
        # E2e074fc1: Lifecycle edge, no user action: the framework
        # creates MainActivity, then calls onCreate.
        r.comment("framework creates MainActivity, then calls onCreate",
                  edge="E2e074fc1")
        # E1975beaa: Internal call, no user action: onCreate stores
        # a UID for this install when none is set
        # (home/MainActivity.java:233; prerequisite gate :184-187).
        r.comment("MainActivity.onCreate calls InfoService.setInfoValue "
                  "(MainActivity.java:233)",
                  edge="E1975beaa")
        # Ece87d249: Internal call, no user action: setInfoValue
        # updates the existing info row for the key
        # (servicelayer/InfoService.java:144-145; exists check :139).
        r.comment("InfoService.setInfoValue calls "
                  "InfoRepositorySql.update (InfoService.java:144-145)",
                  edge="Ece87d249")
        # E2409594a: Internal call, no user action: update forwards
        # to SqlRepositoryBase.update (InfoRepositorySql.java:76).
        r.comment("InfoRepositorySql.update calls "
                  "SqlRepositoryBase.update (InfoRepositorySql.java:76)",
                  edge="E2409594a")
        # Ef6bd6929: Internal call, no user action: update notifies
        # sync listeners when a row was actually changed
        # (datalayer/SqlRepositoryBase.java:118; guard :117).
        r.comment("SqlRepositoryBase.update calls notifySync "
                  "(SqlRepositoryBase.java:118)",
                  edge="Ef6bd6929")
        # Ef8378602: Internal call, no user action: notifySync calls
        # SyncManager.dataChanged (SqlRepositoryBase.java:132).
        r.comment("SqlRepositoryBase.notifySync calls "
                  "SyncManager.dataChanged (SqlRepositoryBase.java:132)",
                  edge="Ef8378602")
        # Ee260f9b8: Internal call, no user action: dataChanged
        # checks whether an immediate upload is configured
        # (sync/SyncManager.java:149; guards :131, :134-135, :141,
        # :142-145).
        r.comment("SyncManager.dataChanged calls "
                  "SyncPreferences.getUploadImmediately "
                  "(SyncManager.java:149)",
                  edge="Ee260f9b8")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
