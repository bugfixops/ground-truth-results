"""MMEX route_10: Core.resolveColorAttribute.

Method: Core.resolveColorAttribute
Edge ids (in route order):
    E71c76102 E2e074fc1 E5d5a9c2f Eff22f7d2 E25d552ed E7a1586a1
    E0c84ecce E3e34477a Eefc61514 Eee1d77ae E6f2749ed Eeb0bdb17
    Ee5898424 E0fd899cd Ea3736990 Ef80f78d8 E2c7bb2a3 E297859cc
Printed route source:
    graphs/MMEX/scratch/route_print_final2/Core.resolveColorAttribute.txt
    (18 steps; header env=- state=data). These edge ids match, in
    order, the route_10 row of device-fix/routes/ROUTES.csv exactly
    (checked by the helper against that row; the ROUTES.csv reason
    cell for route_10 is the old unscriptable reason this draft
    removes, see GROUNDING_10.md).
Permissions: none (print header env=-; no ENV permission gate, and
    the ROUTES.csv permissions cell for route_10 is empty).
Fixtures: none (no STATE file gate; the seeded row is created by
    the setup through the app UI, not pushed as a file).
Setup: setup_route_10.py (bootstrap + account "RetryTxAcct" + one
    Withdrawal transaction with payee "RetryPayee" and category
    "RetryCateg"). The route script's only data-dependent tap is
    the report row wait on the setup-known payee name; the drawer
    taps use static strings from source (see below).
Drawer note (the E25d552ed collision, GROUNDING_10.md section 3):
    the drawer has TWO children with text "Payees": Entities >
    Payees (PayeeListFragment) and Reports > Payees
    (PayeesReportActivity). The script taps the "Reports" group
    first; drawer groups start collapsed (no expandGroup call for
    the drawer exists in source), so only the Reports children are
    visible when tap(text="Payees") runs, and it resolves the
    report child. The script must never tap "Payees" before
    expanding "Reports", and must never tap the options-menu
    title "Payee" (singular, menu_main.xml:107-108), which is a
    different item. The setup never opens the drawer, so the
    Entities group is never expanded before this script runs.
State gate (E2c7bb2a3): the payee report query returns at least
    one row only because the setup saved a transaction; the row
    wait below is the observable for "the list lays out a row":
    bindView writes the payee name into the row's textViewColumn1
    (reports/PayeeReportAdapter.java:59-61), and the header's
    textViewColumn1 is the static word "Payee", so the seeded name
    cannot match the header. If the setup transaction did not
    save, this wait times out honestly and the route fails.
Run (from the repo root, after the merger drops this file into
    device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_10.py --package
    com.money.manager.ex --log steps/route_10.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E5d5a9c2f", "Eff22f7d2", "E25d552ed",
    "E7a1586a1", "E0c84ecce", "E3e34477a", "Eefc61514", "Eee1d77ae",
    "E6f2749ed", "Eeb0bdb17", "Ee5898424", "E0fd899cd", "Ea3736990",
    "Ef80f78d8", "E2c7bb2a3", "E297859cc",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_10", edge_ids=EDGE_IDS,
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
        # E5d5a9c2f: MainActivity.onCreate calls initHomeFragment
        # directly (MainActivity.java:238). No user action.
        r.comment("MainActivity.onCreate calls initHomeFragment",
                  edge="E5d5a9c2f")
        # Eff22f7d2: initHomeFragment commits HomeFragment into the
        # content container, showing the home screen
        # (MainActivity.java:1308-1324). No user action.
        r.comment("home screen shown (HomeFragment committed)",
                  edge="Eff22f7d2")
        # E25d552ed: Open the drawer, expand the Reports group, tap
        # its Payees child. Drawer toggle content description is
        # R.string.open = "Open" (MainActivity.java:1296;
        # res/values/strings.xml:193; same tap as route_20). Group
        # text is R.string.menu_reports = "Reports"
        # (MainActivity.java:1103-1106; strings.xml:301). Child
        # text is R.string.payees = "Payees"
        # (MainActivity.java:898-901; strings.xml:398). Groups
        # start collapsed and only Reports is expanded here, so
        # this "Payees" is the report child, not the Entities
        # child (see docstring drawer note). The child tap closes
        # the drawer and posts the 200 ms Runnable (onChildClick,
        # MainActivity.java:965-980).
        r.tap(desc="Open", edge="E25d552ed")
        r.tap(text="Reports", edge="E25d552ed")
        r.wait_for(text="Payees", edge="E25d552ed", timeout=30)
        r.tap(text="Payees", edge="E25d552ed")
        # E7a1586a1: The child tap posted a Runnable with a 200 ms
        # delay; the framework runs run() when the delay ends.
        # No user action.
        r.comment("drawer Runnable runs after 200 ms delay",
                  edge="E7a1586a1")
        # E0c84ecce: run() calls onDrawerMenuAndOptionMenuSelected
        # (MainActivity.java:978). No user action.
        r.comment("run() calls onDrawerMenuAndOptionMenuSelected",
                  edge="E0c84ecce")
        # E3e34477a: case R.id.menu_report_payees starts
        # PayeesReportActivity (MainActivity.java:667-669).
        # No user action.
        r.comment("case menu_report_payees starts PayeesReportActivity",
                  edge="E3e34477a")
        # Eefc61514: The framework calls PayeesReportActivity.onCreate
        # (PayeesReportActivity.java:32-34). No user action.
        r.comment("framework calls PayeesReportActivity.onCreate",
                  edge="Eefc61514")
        # Eee1d77ae: onCreate constructs PayeeReportFragment
        # (PayeesReportActivity.java:46). No user action.
        r.comment("onCreate constructs PayeeReportFragment",
                  edge="Eee1d77ae")
        # E6f2749ed: The framework calls onCreate on the committed
        # fragment; the body is the inherited BaseReportFragment.
        # onCreate (BaseReportFragment.java:67-72). No user action.
        r.comment("framework calls fragment onCreate (base body)",
                  edge="E6f2749ed")
        # Eeb0bdb17: The fragment manager calls onActivityCreated;
        # the override sets the PayeeReportAdapter before calling
        # super (PayeeReportFragment.java:63-96). No user action.
        r.comment("fragment onActivityCreated sets PayeeReportAdapter",
                  edge="Eeb0bdb17")
        # Ee5898424: onActivityCreated calls super, i.e.
        # BaseReportFragment.onActivityCreated
        # (PayeeReportFragment.java:95). No user action.
        r.comment("onActivityCreated calls super (base)",
                  edge="Ee5898424")
        # E0fd899cd: BaseReportFragment.onActivityCreated starts the
        # loader (BaseReportFragment.java:97). No user action.
        r.comment("base onActivityCreated starts loader",
                  edge="E0fd899cd")
        # Ea3736990: restartLoader creates the loader through
        # onCreateLoader (BaseReportFragment.java:261-263, 115-132).
        # No user action.
        r.comment("restartLoader creates loader via onCreateLoader",
                  edge="Ea3736990")
        # Ef80f78d8: The loader delivers its cursor and the
        # LoaderManager calls PayeeReportFragment.onLoadFinished,
        # which calls super (PayeeReportFragment.java:129-130;
        # BaseReportFragment.java:142-144 changeCursor). No user
        # action; the cursor swap is what lets the list lay out
        # rows on the next edge.
        r.comment("loader delivers cursor; onLoadFinished swaps it in",
                  edge="Ef80f78d8")
        # E2c7bb2a3: STATE GATE. CursorAdapter.getView calls
        # bindView for each row it lays out, and bindView writes
        # the payee name into the row (PayeeReportAdapter.java:
        # 59-61). Waiting for the setup-seeded payee name is
        # therefore the observable that a row was laid out; the
        # loader runs asynchronously, so this wait (not a fixed
        # sleep) is the synchronisation. Timeout here means the
        # setup transaction did not save, and the route fails
        # honestly rather than claiming the target.
        r.wait_for(text="RetryPayee", edge="E2c7bb2a3", timeout=30)
        # E297859cc: bindView calls Core.resolveColorAttribute
        # (PayeeReportAdapter.java:75) for the laid-out row --
        # target reached. No further user action; the row wait
        # above already proves bindView ran for this row.
        r.comment("bindView calls Core.resolveColorAttribute (target "
                  "reached)", edge="E297859cc")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
