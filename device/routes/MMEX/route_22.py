"""MMEX route_22: QueryAccountBills.setReconciled.

Method: QueryAccountBills.setReconciled
Edge ids (in route order):
    E71c76102 E2e074fc1 E42f75996 Ed7c3255d E907a4a17 E4612a5e5
    Ef3db1a02 Eaf7907a9 Ea7478604 E0ef3fa39 E6cc59a43 E6c8e7c4e
Printed route source:
    graphs/MMEX/scratch/route_print_final2/QueryAccountBills.setReconciled.txt
    (12 steps; header env=- state=-). These edge ids match, in order,
    the verification.csv path row for QueryAccountBills.setReconciled
    exactly (checked by the helper; no discrepancy).
Permissions: none (print header env=-; no ENV permission gate, so no
    permission from the manifest is granted by this route).
Fixtures: none (no STATE file gate).
Setup: none (apps.csv MMEX setup is effectively none).
Caveat for the merger/device lead (not a script action): the final
    step runs inside a cursor loop, so the target is reached only
    when the account-bills cursor holds at least one row
    (HomeFragment.java:821-823: while (cursor.moveToNext()) { ...
    setValueFromCursor(cursor); }). The graph records no state gate
    for this route, so this script implements the printed route as
    written; a replay database with no accounts would deliver an
    empty cursor and never reach the target.
Run (from the repo root, after the merger drops this file into
    device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_22.py --package
    com.money.manager.ex --log steps/route_22.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E42f75996", "Ed7c3255d", "E907a4a17",
    "E4612a5e5", "Ef3db1a02", "Eaf7907a9", "Ea7478604", "E0ef3fa39",
    "E6cc59a43", "E6c8e7c4e",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_22", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E71c76102: Launch the MAIN/LAUNCHER activity.
        # AndroidManifest.xml:136-143: .home.MainActivity with MAIN +
        # LAUNCHER intent filter.
        r.launch("com.money.manager.ex/.home.MainActivity",
                 edge="E71c76102")
        # E2e074fc1: The framework calls MainActivity.onCreate after
        # creating the activity instance. No user action.
        r.comment("framework calls MainActivity.onCreate",
                  edge="E2e074fc1")
        # E42f75996: The framework starts the activity right after
        # onCreate. No user action.
        r.comment("framework calls MainActivity.onStart",
                  edge="E42f75996")
        # Ed7c3255d: The framework resumes the activity after onStart.
        # No user action.
        r.comment("framework calls MainActivity.onResume",
                  edge="Ed7c3255d")
        # E907a4a17: super.onResume dispatches onResume to the
        # fragments (MainActivity.java:271-276; HomeFragment.java:378-401).
        # No user action.
        r.comment("onResume dispatched to HomeFragment.onResume",
                  edge="E907a4a17")
        # E4612a5e5: HomeFragment.onResume calls startLoaders
        # (HomeFragment.java:400). No user action.
        r.comment("HomeFragment.onResume calls startLoaders",
                  edge="E4612a5e5")
        # Ef3db1a02: restartLoader(LOADER_ACCOUNT_BILLS) makes the
        # LoaderManager call onCreateLoader (HomeFragment.java:535-536).
        # No user action.
        r.comment("LoaderManager calls onCreateLoader",
                  edge="Ef3db1a02")
        # Eaf7907a9: The loader delivers its cursor to onLoadFinished
        # when the load completes (HomeFragment.java:222-273, 287-288).
        # Waiting for the account-bills list view confirms the home
        # fragment is displayed while the loaders run
        # (res/layout/home_fragment.xml:78, @+id/listViewAccountBills);
        # the delivery itself is framework work, not a tap.
        r.wait_for(res_id="listViewAccountBills", edge="Eaf7907a9",
                   timeout=60)
        # Ea7478604: onLoadFinished renders the account list for the
        # account-bills loader result (guard: loader id ==
        # LOADER_ACCOUNT_BILLS, HomeFragment.java:287-291).
        # No user action.
        r.comment("onLoadFinished renders accounts list",
                  edge="Ea7478604")
        # E0ef3fa39: renderAccountsList calls showAccountTotals
        # (HomeFragment.java:804). No user action.
        r.comment("renderAccountsList calls showAccountTotals",
                  edge="E0ef3fa39")
        # E6cc59a43: showAccountTotals calls setValueFromCursor for
        # each cursor row (HomeFragment.java:823). No user action.
        # See the docstring caveat: needs at least one cursor row.
        r.comment("showAccountTotals calls setValueFromCursor",
                  edge="E6cc59a43")
        # E6c8e7c4e: setValueFromCursor calls setReconciled
        # (QueryAccountBills.java:221). No user action.
        r.comment("setValueFromCursor calls setReconciled",
                  edge="E6c8e7c4e")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
