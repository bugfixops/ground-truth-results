"""MMEX route_18: CurrencyRepositorySql_Factory.get -- CONVERTED (retry).

Method: CurrencyRepositorySql_Factory.get
Edge ids (in route order):
    E71c76102 E2e074fc1 E5d5a9c2f Eff22f7d2 E1644b6d5 E85eda8a2
    E8d5ee44f E72aafa5b Ec9797f96 Ec20e33bf E89a5da90 E059e6762
    E628ea28a Eae2ef743 Ed063c126 E611ff43a Ebd9daee6
Printed route source:
    graphs/MMEX/scratch/route_print_final2/CurrencyRepositorySql_Factory.get.txt
    (17 steps; header env=- state=-). These edge ids match, in order,
    the verification.csv path row for CurrencyRepositorySql_Factory.get
    exactly (checked by the g4 draft; no discrepancy).
Permissions: none (print header env=-; no ENV permission gate).
Fixtures: none (no STATE file gate).
Setup: setup_route_18.py (bootstrap + one account named "RetryAcct",
    created through AccountEditActivity). The previous unscriptable
    reasons (home unreachable after pm clear; no account row) are
    both removed: the bootstrap reaches home, and the known name
    makes the home child row tappable by text (see setup file for
    the res_id-collision analysis).
Run (from the repo root, after the merger drops this file into
    device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_18.py --package
    com.money.manager.ex --log steps/route_18.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E5d5a9c2f", "Eff22f7d2", "E1644b6d5",
    "E85eda8a2", "E8d5ee44f", "E72aafa5b", "Ec9797f96", "Ec20e33bf",
    "E89a5da90", "E059e6762", "E628ea28a", "Eae2ef743", "Ed063c126",
    "E611ff43a", "Ebd9daee6",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_18", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E71c76102: Launch the MAIN/LAUNCHER activity.
        r.launch("com.money.manager.ex/.home.MainActivity",
                 edge="E71c76102")
        # E2e074fc1: Framework calls MainActivity.onCreate.
        r.comment("framework calls MainActivity.onCreate",
                  edge="E2e074fc1")
        # E5d5a9c2f: onCreate calls initHomeFragment (:238).
        r.comment("MainActivity.onCreate calls initHomeFragment",
                  edge="E5d5a9c2f")
        # Eff22f7d2: HomeFragment committed; home screen shown.
        r.comment("home screen shown (HomeFragment committed)",
                  edge="Eff22f7d2")
        # E1644b6d5: Long-press the seeded account child row, then
        # tap "Edit" in its context menu. The child row's text is
        # the setup-known name "RetryAcct" (home/HomeFragment.java:
        # 450-469: EDIT check at 462; menu title R.string.edit =
        # "Edit", strings.xml:183). tap(text=...) resolves the child
        # row, not the group header, because the texts differ.
        r.long_tap(text="RetryAcct", edge="E1644b6d5")
        r.tap(text="Edit", edge="E1644b6d5")
        # E85eda8a2: onContextItemSelected starts AccountEditActivity
        # with ACTION_EDIT and the account id (:463-466).
        r.comment("context menu Edit starts AccountEditActivity",
                  edge="E85eda8a2")
        # E8d5ee44f: Framework calls AccountEditActivity.onCreate.
        r.comment("framework calls AccountEditActivity.onCreate",
                  edge="E8d5ee44f")
        # E72aafa5b: onCreate sets the account edit form
        # (AccountEditActivity.java:138). No user action.
        r.comment("account edit form shown", edge="E72aafa5b")
        # Ec9797f96: Tap the initial balance field, which opens the
        # calculator (AccountEditActivity.java:301-309; the field is
        # txtInitialBalance, bound to editTextInitialBalance in
        # AccountEditViewHolder.java:59).
        r.tap(res_id="editTextInitialBalance", edge="Ec9797f96")
        # Ec20e33bf: Calculator.show starts CalculatorActivity
        # (common/Calculator.java:70, 77-83). No user action.
        r.comment("Calculator.show starts CalculatorActivity",
                  edge="Ec20e33bf")
        # E89a5da90: Framework calls CalculatorActivity.onCreate.
        r.comment("framework calls CalculatorActivity.onCreate",
                  edge="E89a5da90")
        # E059e6762: Framework calls CalculatorActivity.onResume.
        r.comment("framework calls CalculatorActivity.onResume",
                  edge="E059e6762")
        # E628ea28a: onResume calls displayFormattedAmount (:133).
        r.comment("onResume calls displayFormattedAmount",
                  edge="E628ea28a")
        # Eae2ef743: displayFormattedAmount calls getFormattedAmount
        # (:161). No user action.
        r.comment("displayFormattedAmount calls getFormattedAmount",
                  edge="Eae2ef743")
        # Ed063c126: getFormattedAmount's Dagger Lazy<FormatUtilities>
        # .get() runs FormatUtilities_Factory.get (generated code,
        # INFERRED). No user action.
        r.comment("Dagger Lazy runs FormatUtilities_Factory.get",
                  edge="Ed063c126")
        # E611ff43a: FormatUtilities_Factory.get calls its currency
        # service Provider, whose runtime class is
        # CurrencyService_Factory (generated code, INFERRED).
        r.comment("factory provider runs CurrencyService_Factory.get",
                  edge="E611ff43a")
        # Ebd9daee6: CurrencyService_Factory.get calls its repository
        # Provider, whose runtime class is CurrencyRepositorySql_
        # Factory (generated code, INFERRED) -- target reached.
        # The calculator is left open; the coverage dump after this
        # script records the target regardless.
        r.comment("repository provider runs CurrencyRepositorySql_"
                  "Factory.get (target reached)", edge="Ebd9daee6")
    finally:
        r.done()


if __name__ == "__main__":
    main()
