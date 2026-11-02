"""MMEX route_02: SplitCategoriesActivity$1.<init>.

Method: SplitCategoriesActivity$1.<init>
Edge ids (in route order):
    Eaf2975b8 E4fa3f67a E475b68ad E157bdc5f Ecd641bb4 E3759dc47
    Ee44c0eab Ee02d36ba E95765797 E17773f39 E08346eb9 E188a464f
    E07f0f6e5 Ec69fa8c2 Ef33e8876 Eebcaa84a Ec14d436f Ec97f118b
    E8d321a82 Eae208bbe E2a5a7095 E01801377 E4c09ea2d E0548d81e
Printed route source:
    graphs/MMEX/scratch/route_print_final2/SplitCategoriesActivity_1.<init>.txt
    (24 steps; edge list verified identical to the verification.csv
    path row for SplitCategoriesActivity$1.<init>, result fixed).
Launch component: the route does NOT start from the launcher. Its
    entry is the add-transaction widget (see the widget CAVEAT
    below); the MAIN/LAUNCHER activity is still
    com.money.manager.ex/.home.MainActivity
    (AndroidManifest.xml:136-143).
Permissions: none. The print header has env=-, so no ENV permission
    gate applies.
Fixtures: none (no STATE file gate in the print header).
Setup: none (apps.csv MMEX setup cell is effectively none).
State preconditions (read before judging the real run): a valid
    database must be present and the first-run tutorial already
    dismissed (home/MainActivity.java:184, 1478-1490); the printed
    route assumes both. The split form is guaranteed at least one
    row by showSplitCategoriesForm, which creates a split record
    from the transaction when the list is empty
    (transactions/EditTransactionCommonFunctions.java:1512-1517).
WIDGET CAVEAT (edges Eaf2975b8 and E475b68ad, read before judging
    the real run): the harness has no widget-placement action, so
    this script does NOT drive launcher UI to place the MMEX
    add-transaction widget and tap it. Following the Diary
    route_01 precedent for widget entries, it instead reproduces
    the two framework dispatches exactly: (1) an APPWIDGET_UPDATE
    broadcast to the manifest receiver
    (AndroidManifest.xml:67-77, .widget.ButtonAddTransactionWidgetProvider),
    which makes the system instantiate the receiver and call
    onReceive -> onUpdate; (2) a start of the very intent the
    widget button's PendingIntent carries -- ACTION_INSERT to
    CheckingTransactionEditActivity with the
    KEY_TRANS_SOURCE extra (widget/ButtonAddTransactionWidgetProvider.java:38-42;
    the extra key string is
    "AllDataActivity:TransSource",
    transactions/EditTransactionActivityConstants.java:47). If the
    run's launcher can place a real widget first, that placement
    plus a real button tap should replace these two stand-in
    steps; as scripted, the broadcast plus the PendingIntent's own
    intent are what drive the editor open.
Run (from the repo root, once merged to device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_02.py --package
    com.money.manager.ex --log steps/route_02.log
    --outdir <outdir> [--dry-run] [--adb adb]
Draft location: finish/work/MMEX/device-draft/g1/route_02.py; the
    import below resolves once the file sits under device/routes/MMEX/
    as in the Currency template scripts.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "Eaf2975b8", "E4fa3f67a", "E475b68ad", "E157bdc5f", "Ecd641bb4",
    "E3759dc47", "Ee44c0eab", "Ee02d36ba", "E95765797", "E17773f39",
    "E08346eb9", "E188a464f", "E07f0f6e5", "Ec69fa8c2", "Ef33e8876",
    "Eebcaa84a", "Ec14d436f", "Ec97f118b", "E8d321a82", "Eae208bbe",
    "E2a5a7095", "E01801377", "E4c09ea2d", "E0548d81e",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_02", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # Eaf2975b8: WIDGET STAND-IN (see docstring caveat). The
        # framework creates the widget receiver because the manifest
        # declares it exported with the APPWIDGET_UPDATE filter
        # (AndroidManifest.xml:67-77). The broadcast below is the
        # framework dispatch that creates it; it is not a launcher
        # widget tap.
        r.broadcast(edge="Eaf2975b8",
                    action="android.appwidget.action.APPWIDGET_UPDATE",
                    component="com.money.manager.ex/com.money.manager.ex"
                              ".widget.ButtonAddTransactionWidgetProvider",
                    extras_args=["--eia", "appWidgetIds", "1"])
        # E4fa3f67a: AppWidgetProvider.onReceive calls onUpdate for
        # ACTION_APPWIDGET_UPDATE (widget/ButtonAddTransactionWidgetProvider.java:31-32).
        r.comment("onReceive dispatches APPWIDGET_UPDATE to onUpdate",
                  edge="E4fa3f67a")
        # E475b68ad: WIDGET STAND-IN (see docstring caveat). The
        # widget button's PendingIntent is getActivity for an
        # ACTION_INSERT intent to CheckingTransactionEditActivity
        # with the KEY_TRANS_SOURCE extra
        # (widget/ButtonAddTransactionWidgetProvider.java:38-42).
        # Starting that exact intent reproduces the tap's effect;
        # a real placed-widget tap should replace this step.
        r.start_intent(edge="E475b68ad",
                       action="android.intent.action.INSERT",
                       component="com.money.manager.ex/com.money.manager.ex"
                                 ".transactions.CheckingTransactionEditActivity",
                       extras={"AllDataActivity:TransSource":
                               "ButtonAddTransactionWidgetProvider.java"})
        # E157bdc5f: The system instantiates the editor, then
        # onCreate.
        r.comment("system instantiates CheckingTransactionEditActivity, "
                  "then onCreate", edge="E157bdc5f")
        # Ecd641bb4: onCreate calls initializeInputControls
        # (transactions/CheckingTransactionEditActivity.java:122).
        r.comment("onCreate calls initializeInputControls",
                  edge="Ecd641bb4")
        # E3759dc47: initializeInputControls calls
        # mCommon.initSplitCategories
        # (transactions/CheckingTransactionEditActivity.java:370).
        r.comment("initializeInputControls calls initSplitCategories",
                  edge="E3759dc47")
        # Ee44c0eab: Tap the split button. It is a FontIconView with
        # id splitButton (transactions/EditTransactionViewHolder.java:72;
        # res/layout/activity_edit_checking_account_transaction.xml:440,
        # the Checking editor layout set at
        # CheckingTransactionEditActivity.java:95). Its text is a
        # font-icon glyph (@string/ic_split), so the tap uses the
        # resource id, not text.
        r.tap(res_id="splitButton", edge="Ee44c0eab")
        # Ee02d36ba: The split button takes the splitting branch
        # (splitting = !isSplitSelected(),
        # transactions/EditTransactionCommonFunctions.java:602-605)
        # and calls showSplitCategoriesForm.
        r.comment("splitting branch calls showSplitCategoriesForm",
                  edge="Ee02d36ba")
        # E95765797: showSplitCategoriesForm starts
        # SplitCategoriesActivity for result
        # (transactions/EditTransactionCommonFunctions.java:1519-1528).
        r.comment("showSplitCategoriesForm starts SplitCategoriesActivity",
                  edge="E95765797")
        # E17773f39: The system instantiates SplitCategoriesActivity,
        # then onCreate.
        r.comment("system instantiates SplitCategoriesActivity, then "
                  "onCreate", edge="E17773f39")
        # E08346eb9: onCreate calls initRecyclerView
        # (transactions/SplitCategoriesActivity.java:105).
        r.comment("onCreate calls initRecyclerView",
                  edge="E08346eb9")
        # E188a464f: After setAdapter the RecyclerView asks the
        # adapter to create each row holder
        # (transactions/SplitCategoriesActivity.java:259).
        r.comment("RecyclerView creates row holders via the adapter",
                  edge="E188a464f")
        # E07f0f6e5: onCreateViewHolder calls initAmountControl
        # (transactions/SplitCategoriesAdapter.java:79).
        r.comment("onCreateViewHolder calls initAmountControl",
                  edge="E07f0f6e5")
        # Ec69fa8c2: Tap the amount view of a split row. The amount
        # TextView is R.id.editTextTotAmount
        # (transactions/SplitItemViewHolder.java:38;
        # res/layout/item_splittransaction.xml:90), whose listener
        # is set at transactions/SplitCategoriesAdapter.java:161.
        # The first matching node is the first split row; at least
        # one row exists by showSplitCategoriesForm (see docstring).
        r.tap(res_id="editTextTotAmount", edge="Ec69fa8c2")
        # Ef33e8876: The amount listener posts
        # AmountEntryRequestedEvent on EventBus
        # (transactions/SplitCategoriesAdapter.java:174).
        r.comment("amount tap posts AmountEntryRequestedEvent",
                  edge="Ef33e8876")
        # Eebcaa84a: SplitCategoriesActivity.onEvent opens the
        # calculator via Calculator.show
        # (transactions/SplitCategoriesActivity.java:205-211).
        r.comment("onEvent opens the calculator (Calculator.show)",
                  edge="Eebcaa84a")
        # Ec14d436f: The system instantiates CalculatorActivity,
        # then onCreate.
        r.comment("system instantiates CalculatorActivity, then "
                  "onCreate", edge="Ec14d436f")
        # Ec97f118b: onCreate sets the calculator layout
        # (common/CalculatorActivity.java:115) and wires the keys;
        # the calculator screen is shown.
        r.comment("CalculatorActivity shows the calculator screen",
                  edge="Ec97f118b")
        # E8d321a82: Tap the equals key. The calculator keys are
        # RobotoButtons with literal texts
        # (res/layout/activity_calculator.xml:87-166: "C", digits,
        # "-", "="). The four taps before "=" enter the expression
        # 0-5, so the returned amount is -5, which is exactly what
        # the next edge's negative-amount guard needs
        # (transactions/SplitCategoriesActivity.java:277); the "="
        # tap itself is this edge's GUI action
        # (@OnClick(R.id.buttonKeyEqual),
        # common/CalculatorActivity.java:247-250).
        r.tap(text="C", edge="E8d321a82")
        r.tap(text="0", edge="E8d321a82")
        r.tap(text="-", edge="E8d321a82")
        r.tap(text="5", edge="E8d321a82")
        r.tap(text="=", edge="E8d321a82")
        # Eae208bbe: onEqualsClicked calls returnResult
        # (common/CalculatorActivity.java:249).
        r.comment("onEqualsClicked calls returnResult",
                  edge="Eae208bbe")
        # E2a5a7095: returnResult sets RESULT_OK and finishes
        # (common/CalculatorActivity.java:443-444); the framework
        # delivers the result to SplitCategoriesActivity.
        r.comment("calculator returns RESULT_OK; framework delivers "
                  "the result", edge="E2a5a7095")
        # E01801377: The amount branch of onActivityResult calls
        # onAmountEntered (transactions/SplitCategoriesActivity.java:142-145).
        r.comment("amount branch calls onAmountEntered",
                  edge="E01801377")
        # E4c09ea2d: The returned amount is negative, so
        # onAmountEntered calls showInvalidAmountDialog
        # (transactions/SplitCategoriesActivity.java:276-278).
        r.comment("negative amount calls showInvalidAmountDialog",
                  edge="E4c09ea2d")
        # E0548d81e: showInvalidAmountDialog builds the dialog; its
        # positive-button listener is the anonymous class whose
        # constructor is the target (SplitCategoriesActivity$1),
        # created at transactions/SplitCategoriesActivity.java:320.
        # The dialog message text is @string/error_amount_must_be_positive
        # (res/values/strings.xml:115), so waiting for it confirms
        # the dialog -- and the target constructor -- exists.
        # TARGET REACHED (construction, no dialog tap needed).
        r.wait_for(text="Amount must be positive. The sign is "
                        "determined by Transaction Type.",
                  edge="E0548d81e", timeout=30)
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
