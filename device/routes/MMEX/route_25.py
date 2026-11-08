"""MMEX route_25: AccountRepository.first.

Method: AccountRepository.first
Edge ids (in route order):
    E2b98cbaa E3ffa36d3 E9eb5ff4d Ea4c507f5 Ebb29c7ff E64510675
    Ef7590543
Printed route source:
    graphs/MMEX/scratch/route_print_final2/AccountRepository.first.txt
    (7 steps; header env=- state=-). These edge ids match, in order,
    the verification.csv path row for AccountRepository.first exactly
    (checked by the helper; no discrepancy).
Permissions: none (print header env=-; no ENV permission gate, so no
    permission from the manifest is granted by this route).
Fixtures: none (no STATE file gate).
Setup: none (apps.csv MMEX setup is effectively none).
Caveat for the merger/device lead (not a script action): the display
    branch runs only when a default account id is configured
    (SingleAccountWidget.java:171-176: defaultAccountId is read from
    the database info table and displayAccountInfo is called only if
    it is non-null; NumericHelper.toInteger returns null for an empty
    value). The graph records no state gate for this route, so this
    script implements the printed route as written; a replay
    database with no default account configured would skip
    displayAccountInfo and never reach the target.
Run (from the repo root, after the merger drops this file into
    device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_25.py --package
    com.money.manager.ex --log steps/route_25.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E2b98cbaa", "E3ffa36d3", "E9eb5ff4d", "Ea4c507f5", "Ebb29c7ff",
    "E64510675", "Ef7590543",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_25", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E2b98cbaa: The framework creates the widget receiver by
        # class name because the manifest declares it exported with
        # the APPWIDGET_UPDATE intent filter
        # (AndroidManifest.xml:114-124, .widget.SingleAccountWidget).
        # A broadcast to that component with a non-empty widget-id
        # array drives the same entry; there is no launcher tap for a
        # widget receiver.
        r.broadcast(edge="E2b98cbaa",
                    action="android.appwidget.action.APPWIDGET_UPDATE",
                    extras_args=["--eia", "appWidgetIds", "1"],
                    component="com.money.manager.ex/.widget.SingleAccountWidget")
        # E3ffa36d3: AppWidgetProvider.onReceive calls onUpdate for
        # ACTION_APPWIDGET_UPDATE (FW-SRC AppWidgetProvider.java:61-66),
        # guarded on non-null extras and a non-empty id array; the
        # --eia extra above supplies both. No separate action.
        r.comment("onReceive calls onUpdate (APPWIDGET_UPDATE)",
                  edge="E3ffa36d3")
        # E9eb5ff4d: onUpdate calls updateAppWidget for each widget id
        # (SingleAccountWidget.java:74). No user action.
        r.comment("onUpdate calls updateAppWidget",
                  edge="E9eb5ff4d")
        # Ea4c507f5: updateAppWidget shows the account info for the
        # configured default account (SingleAccountWidget.java:171-176;
        # guard: defaultAccountId != null at :174). No user action.
        # See the docstring caveat.
        r.comment("updateAppWidget calls displayAccountInfo",
                  edge="Ea4c507f5")
        # Ebb29c7ff: displayAccountInfo calls loadAccount
        # (SingleAccountWidget.java:195). No user action.
        r.comment("displayAccountInfo calls loadAccount",
                  edge="Ebb29c7ff")
        # E64510675: loadAccount calls AccountRepository.load
        # (SingleAccountWidget.java:250). No user action.
        r.comment("loadAccount calls AccountRepository.load",
                  edge="E64510675")
        # Ef7590543: load returns the first account matching the where
        # clause for the given id (AccountRepository.java:51-57;
        # guard: id != Constants.NOT_SET at :52, first call at :57).
        # No user action.
        r.comment("load calls AccountRepository.first",
                  edge="Ef7590543")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
