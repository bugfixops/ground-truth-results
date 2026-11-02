#!/usr/bin/env python3
"""MMEX per-route setup for route_12 (IncomeVsExpensesListFragment$1.run).

Bootstrap + tablet emulation + transaction seed, in run_app.sh order
(after `pm clear`, before the route script), following the B3
bootstrap pattern of setup_route_23.py and the MMEX-B3-UIDRIVE
amendment (UI-driving setups are admitted; setup actions log under
edge "setup" in the separate setup log, never against a route edge).

1. Bootstrap (setup_route_23 pattern, same citations): an EMPTY file
   pushed to /sdcard/MoneyManagerEx/mmex.mmb, so the app's own
   MmxOpenHelper.onCreate runs the app's own schema script
   (R.raw.tables_v1) plus initDatabase -- database/MmxOpenHelper.
   java:96-103, 227-236. A hand-filled plaintext sqlite3 .mmb is
   deliberately NOT used: the app opens every database through the
   SQLCipher SupportFactory (MmxOpenHelper.java:132-154), so a
   plaintext file would be rejected as not-a-database, while a
   0-byte file is treated as a new database and initialised by the
   app itself. Default SharedPreferences written via `run-as`
   (debug build): prefshowtutorial = false (BehaviourSettings
   default true, settings/BehaviourSettings.java:86-88) and
   databasepath = /sdcard/MoneyManagerEx/mmex.mmb (pref key
   res/values/prefids.xml:34). Storage grants use option (a):
   READ+WRITE granted by setup itself before the run-as copy and
   the warm launch, because run_app.sh grants ROUTES permissions
   only AFTER setup. Warm launch of MainActivity follows, and
   setup waits until MainActivity is the resumed activity, so the
   schema creation has actually happened.
2. Tablet emulation (blocker (a)): `wm size 1920x1200` +
   `wm density 240`. Smallest-width arithmetic (see
   GROUNDING_12.md): 1200 px / (240 dpi / 160) = 800 dp, so the
   landscape smallest width is 800 dp >= 600 dp, selecting
   layout-sw600dp-land/report_chart_fragments_activity.xml, where
   fragmentChart exists (:38) and sets mIsDualPanel
   (reports/IncomeVsExpensesActivity.java:46) -- the exact guard
   on the final edge (reports/IncomeVsExpensesListFragment.
   java:188). The pair is the one proven in the retry pass
   (device-draft/retry/RETRY_REPORT.md section 12, audit
   b3-device/AUDIT.md section 4.6). The wm output is read back
   and must contain 1920x1200 / 240, else setup fails. After the
   size change MainActivity is recreated by the configuration
   change, so setup waits for MainActivity resumed again before
   driving UI. Seeding under the tablet size is safe on ids: the
   transaction-edit layout is NOT overridden in
   layout-sw600dp-land, and the calculator ids/texts are identical
   in layout-sw600dp-land/activity_calculator.xml and the default
   layout (see GROUNDING_12.md).
3. Seed (blocker (b)): one account "Retry12" through
   AccountEditActivity (same form as setup_route_23), then two
   transactions on that account through
   CheckingTransactionEditActivity, both dated today by default
   (EditTransactionCommonFunctions.initDateSelector:480-486: a
   null date becomes today), one Deposit of 100 and one
   Withdrawal of 50, sharing payee "RetryPayee" and category
   "RetryCat". Why this satisfies the route's data guards:
   - validateData (EditTransactionCommonFunctions.java:1146-1185)
     requires a positive amount (:1168-1171), a payee (:1174-1178)
     and a category (:1181-1185); all three are supplied, and
     the status defaults to "" (initStatusSelector:629-650 sets
     status_values[0], which is empty per res/values/arrays.xml:
     54-60), not "V", so the report query's
     `where not(mobiledata.status = 'V')`
     (res/raw/report_income_vs_expenses.sql) keeps both rows.
   - The YEARS loader needs a non-null cursor with a first row
     (IncomeVsExpensesListFragment.java:200) and the REPORT
     loader a non-null cursor (:171). The report query groups
     mobiledata by year (strftime('%Y', transdate) in
     res/raw/query_mobiledata.sql:60) into Deposit -> Income and
     Withdrawal -> Expenses (report_income_vs_expenses.sql).
     The list fragment pre-selects the current year
     (IncomeVsExpensesListFragment.java:95), and the seed date is
     today, so both rows fall in the selected year.
   - Account selection is driven, not assumed: the account
     spinner's listener is attached AFTER setSelection
     (EditTransactionCommonFunctions.java:374-381), so a fresh
     INSERT shows position 0 without setting the entity account
     id; setup taps spinnerAccount and taps "Retry12", and the
     listener then sets the account id (:319-330).
   Payee/category creation flows are cited per tap in
   GROUNDING_12.md. The second transaction reuses the existing
   payee/category rows (tap the row instead of re-creating).
4. Return to home (setup_route_03 pattern): relaunch MainActivity
   with NEW_TASK|CLEAR_TASK (-f 0x10008000) and wait for the
   seeded account row text "Retry12" before done(), so no setup
   UI state leaks into the route script. The route script itself
   then launches MainActivity fresh and taps the home card.

Failure mode: any step failing exits 1 (adb failures via _fail;
Runner lookup/timeout exceptions propagate nonzero), which
run_app.sh records as failed_at_step_0 (setup_failed). Nothing is
faked: if a seed row is not created, the route script's report
loaders fail honestly on the live run. This setup is NOT executed
by drycheck (only py_compiled); it is validated on the live run.

The wm size/density set here is NOT reset by this setup: the
route script owns the tablet configuration for its own edges
and resets it (wm size reset / wm density reset) before done(),
so the device is restored even if the route fails midway (see
route_12.py and GROUNDING_12.md section 3 for the decision and
its evidence). run_app.sh does pm clear between routes but does
NOT reset wm size, so leaving the reset to the route script's
finally block is deliberate, not an omission.

Usage (invoked by run_app.sh):
    setup_route_12.py --package <pkg> --log <log> --outdir <dir> \
        --gen-dir <dir>
"""

import argparse
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner  # noqa: E402

PKG = "com.money.manager.ex"
MAIN = "com.money.manager.ex/.home.MainActivity"
DB_DEVICE_PATH = "/sdcard/MoneyManagerEx/mmex.mmb"
PREFS_NAME = "com.money.manager.ex_preferences.xml"
ACCT_NAME = "Retry12"
PAYEE_NAME = "RetryPayee"
CATEG_NAME = "RetryCat"
WM_SIZE = "1920x1200"
WM_DENSITY = "240"

PREFS_XML = """<?xml version='1.0' encoding='utf-8' standalone='yes' ?>
<map>
    <string name="databasepath">/sdcard/MoneyManagerEx/mmex.mmb</string>
    <boolean name="prefshowtutorial" value="false" />
</map>
"""


def _fail(msg):
    print("setup FAILED: " + msg, file=sys.stderr)
    sys.exit(1)


def _adb(adb, args, timeout=60):
    try:
        proc = subprocess.run([adb] + args, capture_output=True,
                              text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        _fail("adb %s timed out" % " ".join(args))
    if proc.returncode != 0:
        _fail("adb %s failed (%s): %s" % (
            " ".join(args), proc.returncode, proc.stderr.strip()[:300]))
    return proc.stdout


def _shell(adb, command, timeout=60):
    return _adb(adb, ["shell"] + command, timeout=timeout)


def _wait_main_resumed(adb, what):
    deadline = time.time() + 60
    while time.time() < deadline:
        dump = _shell(adb, ["dumpsys", "activity", "activities"])
        if "mResumedActivity" in dump and "MainActivity" in dump:
            return
        time.sleep(2)
    _fail("MainActivity did not become the resumed activity in 60s (%s)"
          % what)


def create_account(r, name):
    """Create one account through AccountEditActivity (INSERT)."""
    r.start_intent(edge="setup", action="android.intent.action.INSERT",
                   component=PKG + "/.account.AccountEditActivity")
    r.wait_for(edge="setup", res_id="editTextAccountName", timeout=30)
    r.tap(edge="setup", res_id="editTextAccountName")
    r.type_text(name, edge="setup")
    # Initial balance via the calculator (field tap opens it).
    r.tap(edge="setup", res_id="editTextInitialBalance")
    r.wait_for(edge="setup", res_id="buttonKeyEqual", timeout=30)
    r.tap(edge="setup", text="1")
    r.tap(edge="setup", text="0")
    r.tap(edge="setup", text="0")
    r.tap(edge="setup", res_id="buttonKeyEqual")
    r.wait_for(edge="setup", res_id="editTextAccountName", timeout=30)
    r.tap(edge="setup", text="Save")
    r.wait_for(edge="setup", text=name, timeout=30)


def _enter_amount(r, digits):
    """Amount via the calculator opened from textViewAmount."""
    r.tap(edge="setup", res_id="textViewAmount")
    r.wait_for(edge="setup", res_id="buttonKeyEqual", timeout=30)
    for d in digits:
        r.tap(edge="setup", text=d)
    r.tap(edge="setup", res_id="buttonKeyEqual")
    # CalculatorActivity finishes with RESULT_OK on "=" (its
    # :247 onClick equal -> :442-444 setResult + finish), so the
    # edit screen is foreground again.
    r.wait_for(edge="setup", res_id="textViewAmount", timeout=30)


def _pick_payee(r, name, create):
    """Payee for the open transaction: create once, pick after."""
    r.tap(edge="setup", res_id="textViewPayee")
    if create:
        # PayeeActivity picker; FAB creates (PayeeListFragment
        # :429-433 onFloatingActionButtonClicked -> INSERT dialog).
        r.wait_for(edge="setup", res_id="fab", timeout=30)
        r.tap(edge="setup", res_id="fab")
        r.wait_for(edge="setup", res_id="editTextPayeeName", timeout=30)
        r.tap(edge="setup", res_id="editTextPayeeName")
        r.type_text(name, edge="setup")
        # Positive button is android.R.string.ok (PayeeListFragment
        # :375); in PICK mode INSERT returns at once (:390-393).
        r.tap(edge="setup", text="OK")
    else:
        r.wait_for(edge="setup", text=name, timeout=30)
        r.tap(edge="setup", text=name)
    # showPayeeName writes the name into textViewPayee
    # (EditTransactionCommonFunctions.java:1031-1037).
    r.wait_for(edge="setup", text=name, timeout=30)


def _pick_category(r, name, create):
    """Category for the open transaction: create once, pick after."""
    r.tap(edge="setup", res_id="textViewCategory")
    if create:
        # CategoryListActivity picker; FAB opens the type selector
        # (CategoryListFragment :367-368 -> :707).
        r.wait_for(edge="setup", res_id="fab", timeout=30)
        r.tap(edge="setup", res_id="fab")
        r.wait_for(edge="setup", text="Choose a type", timeout=30)
        r.tap(edge="setup", text="Category")
        r.wait_for(edge="setup", res_id="editTextCategName", timeout=30)
        r.tap(edge="setup", res_id="editTextCategName")
        r.type_text(name, edge="setup")
        # INSERT only restarts the loader (CategoryListFragment
        # :536-560); the picker stays open, so pick the new group
        # row: 0 subcategories -> setResultAndFinish (:694-695).
        r.tap(edge="setup", text="OK")
        r.wait_for(edge="setup", text=name, timeout=30)
        r.tap(edge="setup", text=name)
    else:
        r.wait_for(edge="setup", text=name, timeout=30)
        r.tap(edge="setup", text=name)
    r.wait_for(edge="setup", res_id="textViewCategory", timeout=30)


def create_transaction(r, account, payee, category, digits, deposit,
                       create_payee, create_category):
    """One checking transaction through CheckingTransactionEditActivity.

    Type is set explicitly (default is Withdrawal when the entity
    type is null -- EditTransactionCommonFunctions.java:783-786),
    account via the spinner tap (see module docstring), amount via
    the calculator, payee/category via their pickers, date left at
    its today default, saved with the toolbar Save item.
    """
    r.start_intent(edge="setup", action="android.intent.action.INSERT",
                   component=PKG + "/.transactions.CheckingTransactionEditActivity")
    r.wait_for(edge="setup", res_id="spinnerAccount", timeout=30)
    if deposit:
        r.tap(edge="setup", res_id="depositButton")
    else:
        r.tap(edge="setup", res_id="withdrawalButton")
    r.tap(edge="setup", res_id="spinnerAccount")
    r.wait_for(edge="setup", text=account, timeout=30)
    r.tap(edge="setup", text=account)
    _enter_amount(r, digits)
    _pick_payee(r, payee, create_payee)
    _pick_category(r, category, create_category)
    # Save: toolbar item titled "Save" (MenuHelper.addSaveToolbarIcon,
    # core/MenuHelper.java:87-89; strings.xml:772) -> onActionDoneClick
    # (CheckingTransactionEditActivity.java:154-155, 195-196) ->
    # saveData -> finish; the home list is foreground again.
    r.tap(edge="setup", text="Save")
    r.wait_for(edge="setup", text=account, timeout=30)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="MMEX route_12 setup: bootstrap + tablet size + "
                    "account + income/expense transactions")
    parser.add_argument("--package", default=PKG)
    parser.add_argument("--log", default=None)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--gen-dir", default=None)
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    adb = args.adb
    pkg = args.package or PKG
    gen_dir = args.gen_dir or os.environ.get("GEN_DIR", "") or os.getcwd()
    os.makedirs(gen_dir, exist_ok=True)

    def log(msg):
        line = msg + "\n"
        if args.log:
            with open(args.log, "a", encoding="utf-8") as f:
                f.write(line)
        sys.stdout.write(line)

    # 1. Empty database file on shared storage (app-created schema).
    mmb_local = os.path.join(gen_dir, "mmex.mmb")
    with open(mmb_local, "wb") as f:
        pass  # 0 bytes, deliberately: the app initialises it itself.
    _shell(adb, ["mkdir", "-p", "/sdcard/MoneyManagerEx"])
    _adb(adb, ["push", mmb_local, DB_DEVICE_PATH])
    log("pushed empty %s (0 bytes) to %s" % (mmb_local, DB_DEVICE_PATH))

    # 2. SharedPreferences via run-as (debug build): tutorial off,
    # database path set. The app is not running (pm clear just ran),
    # so no in-memory preference cache can overwrite this file.
    prefs_local = os.path.join(gen_dir, "mmex_prefs.xml")
    with open(prefs_local, "w", encoding="utf-8") as f:
        f.write(PREFS_XML)
    _adb(adb, ["push", prefs_local, "/sdcard/mmex_prefs.xml"])
    # Storage grant (audit section 2.6, option (a)): run_app.sh grants
    # ROUTES permissions only AFTER setup, and the bootstrap DB lives
    # on shared /sdcard, so setup grants storage itself before the
    # run-as copy and the warm launch.
    _shell(adb, ["pm", "grant", pkg, "android.permission.READ_EXTERNAL_STORAGE"])
    _shell(adb, ["pm", "grant", pkg, "android.permission.WRITE_EXTERNAL_STORAGE"])
    _shell(adb, ["run-as", pkg, "mkdir", "-p",
                 "/data/data/%s/shared_prefs" % pkg])
    _shell(adb, ["run-as", pkg, "cp", "/sdcard/mmex_prefs.xml",
                 "/data/data/%s/shared_prefs/%s" % (pkg, PREFS_NAME)])
    back = _shell(adb, ["run-as", pkg, "cat",
                        "/data/data/%s/shared_prefs/%s" % (pkg, PREFS_NAME)])
    if "databasepath" not in back or "prefshowtutorial" not in back:
        _fail("preferences read-back does not contain the bootstrap keys")
    log("wrote shared prefs %s (tutorial off, databasepath set)" % PREFS_NAME)

    # 3. Warm launch: MainActivity onCreate opens the database, which
    # runs MmxOpenHelper.onCreate (tables_v1 + initDatabase).
    _shell(adb, ["am", "start", "-W", "-n", MAIN])
    _wait_main_resumed(adb, "warm launch")
    log("MainActivity resumed; app-created database schema is live")

    # 4. Tablet emulation, with read-back. This must precede seeding
    # only in the sense that the route's activity must launch under
    # it; seeding ids are identical under the tablet layout (see
    # module docstring), and MainActivity is re-awaited after the
    # configuration change recreates it.
    _shell(adb, ["wm", "size", WM_SIZE])
    _shell(adb, ["wm", "density", WM_DENSITY])
    size_out = _shell(adb, ["wm", "size"])
    density_out = _shell(adb, ["wm", "density"])
    if WM_SIZE not in size_out or WM_DENSITY not in density_out:
        _fail("wm read-back mismatch: size=%r density=%r"
              % (size_out.strip(), density_out.strip()))
    log("tablet emulation set: wm size %s, wm density %s (read back)"
        % (WM_SIZE, WM_DENSITY))
    _wait_main_resumed(adb, "after wm size/density")
    log("MainActivity resumed again after configuration change")

    r = Runner(package=pkg, route="setup_route_12", edge_ids=None,
               log_path=args.log or os.path.join(gen_dir, "setup.log"),
               adb=adb, outdir=args.outdir or ".")
    try:
        create_account(r, ACCT_NAME)
        log("seeded account %r" % ACCT_NAME)
        # Income first (Deposit 100, creates payee + category), then
        # expense (Withdrawal 50, reuses both rows).
        create_transaction(r, ACCT_NAME, PAYEE_NAME, CATEG_NAME,
                           "100", True, True, True)
        log("seeded Deposit 100 for %r" % ACCT_NAME)
        create_transaction(r, ACCT_NAME, PAYEE_NAME, CATEG_NAME,
                           "50", False, False, False)
        log("seeded Withdrawal 50 for %r" % ACCT_NAME)
        # Return to home (setup_route_03 pattern): the route
        # script's launch brings the existing task forward without
        # navigating, so relaunch MainActivity with
        # NEW_TASK|CLEAR_TASK and wait for the seeded account row
        # before returning; otherwise the route script's first real
        # action (home card tap) would run against the transaction
        # list screen.
        _shell(adb, ["am", "start", "-W", "-n", MAIN, "-f", "0x10008000"])
        r.wait_for(edge="setup", text=ACCT_NAME, timeout=30)
    finally:
        r.done()
    log("seeded account %r with Deposit 100 + Withdrawal 50; home "
        "restored; tablet size left set for route_12.py, which resets "
        "it before done()" % ACCT_NAME)
    return 0


if __name__ == "__main__":
    sys.exit(main())
