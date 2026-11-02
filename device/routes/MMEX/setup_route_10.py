#!/usr/bin/env python3
"""MMEX per-route setup for route_10 (Core.resolveColorAttribute) -- bootstrap + seed.

Bootstrap (same mechanism as setup_route_23, q.v. for citations):
empty .mmb pushed to /sdcard/MoneyManagerEx/mmex.mmb, default
SharedPreferences written via run-as (prefshowtutorial=false,
databasepath set), MainActivity warm-launched so the app's own
MmxOpenHelper.onCreate creates the schema (tables_v1 + initDatabase).

Seed (drives UI through the harness Runner with edge_ids=None, as the
setup contract allows; setup actions log under edge "setup" in the
separate setup log, never against a route edge). The route's state
gate is that the payee report query returns at least one row, so the
setup creates, through the app's own UI and nothing else:

- One account named "RetryTxAcct", created through
  AccountEditActivity exactly as in setup_route_23, plus one extra
  tap: the default-account checkbox (res/layout/
  activity_account_edit.xml:76). Ticking it makes this account the
  app's default account (AccountEditActivity.saveDefaultAccount,
  account/AccountEditActivity.java:621-628), so the transaction
  editor's initAccountSelectors assigns it to a new transaction
  even though no account id is passed on the editor intent
  (transactions/EditTransactionCommonFunctions.java:293-305). This
  removes the spinner same-position uncertainty documented in
  GROUNDING_10.md; it is a belt-and-braces step, not a load-bearing
  one, because validateData does not check the account and the
  mobiledata view LEFT JOINs the account table (see GROUNDING_10.md).
- One transaction on that account, created through
  CheckingTransactionEditActivity (ACTION_INSERT), with:
    - amount 100 via the calculator (tap textViewAmount, keys
      "1" "0" "0", "="),
    - payee "RetryPayee", created from the payee picker via its FAB
      dialog (a fresh database has no payee to pick),
    - category "RetryCateg", created from the category picker via
      its FAB type-selector dialog (a fresh database has no
      category to pick),
    - type left at the default Withdrawal and status left at the
      default empty value, both of which pass the payee report
      query filter (Status <> 'V' AND TransactionType IN
      ('Withdrawal', 'Deposit'); reports/PayeeReportFragment.java:
      175-176).
  Save is the toolbar item titled "Save" (core/MenuHelper.java:
  87-89; res/values/strings.xml:772). A successful save finishes
  the editor back to the home list, where the seeded account row
  is waited for.

Return to home (run_app.sh return-to-home rule, decision
MMEX-B3-UIDRIVE): the route script's launch is a plain
`am start -W -n` with no task-clearing flags, so setup UI state
would leak into the route script's starting state. This setup
therefore ends with a CLEAR_TASK relaunch of MainActivity plus a
wait for the seeded account row (the setup_route_03 pattern)
before returning, so the route script starts on the home screen.

Failure mode: any step failing exits 1, which run_app.sh records
as failed_at_step_0 (setup_failed). Nothing is faked: if the
transaction does not save, the route script's report row wait
fails honestly on the live run. This setup is NOT executed by
drycheck (only py_compiled when it backs a gen: fixture, and it
backs none); it is validated on the live run.

Usage (invoked by run_app.sh):
    setup_route_10.py --package <pkg> --log <log> --outdir <dir> \
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
ACCT_NAME = "RetryTxAcct"
PAYEE_NAME = "RetryPayee"
CATEG_NAME = "RetryCateg"

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


def create_account(r, name):
    """Create one account through AccountEditActivity (INSERT).

    Same form as setup_route_23, plus the default-account checkbox
    tap (see module docstring): with this account as the default,
    the transaction editor assigns it to a new transaction.
    """
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
    # Default account: checkbox res_id defaultAccountCheckbox
    # (res/layout/activity_account_edit.xml:76); on save,
    # saveDefaultAccount stores this account's id as the default
    # (account/AccountEditActivity.java:621-628).
    r.tap(edge="setup", res_id="defaultAccountCheckbox")
    r.tap(edge="setup", text="Save")
    r.wait_for(edge="setup", text=name, timeout=30)


def create_transaction(r):
    """Create one Withdrawal transaction with a payee and a category.

    Launched with ACTION_INSERT (CheckingTransactionEditActivity
    is exported with EDIT/INSERT intent filters,
    AndroidManifest.xml:181-188). Field grounding is per-tap in
    GROUNDING_10.md; the short form:
      amount: textViewAmount -> CalculatorActivity keys -> "="
      payee: textViewPayee -> PayeeActivity (ACTION_PICK) -> FAB
        dialog (editTextPayeeName) -> OK returns the new payee
      category: textViewCategory -> CategoryListActivity
        (ACTION_PICK) -> FAB -> "Category" type item ->
        editTextCategName dialog -> OK, then tap the new group row
        (a category with no subcategories returns its result on
        the group tap itself)
      save: toolbar "Save" finishes the editor to the home list.
    """
    r.start_intent(edge="setup", action="android.intent.action.INSERT",
                   component=PKG + "/.transactions.CheckingTransactionEditActivity")
    r.wait_for(edge="setup", res_id="textViewPayee", timeout=30)
    # Amount 100 through the calculator (textViewAmount opens
    # CalculatorActivity; "=" returns the result to the editor).
    r.tap(edge="setup", res_id="textViewAmount")
    r.wait_for(edge="setup", res_id="buttonKeyEqual", timeout=30)
    r.tap(edge="setup", text="1")
    r.tap(edge="setup", text="0")
    r.tap(edge="setup", text="0")
    r.tap(edge="setup", res_id="buttonKeyEqual")
    r.wait_for(edge="setup", res_id="textViewPayee", timeout=30)
    # Payee: picker FAB dialog creates the payee; in ACTION_PICK
    # mode the dialog's OK sends the new payee back and finishes
    # the picker, and the editor shows the payee name.
    r.tap(edge="setup", res_id="textViewPayee")
    r.wait_for(edge="setup", res_id="fab", timeout=30)
    r.tap(edge="setup", res_id="fab")
    r.wait_for(edge="setup", res_id="editTextPayeeName", timeout=30)
    r.tap(edge="setup", res_id="editTextPayeeName")
    r.type_text(PAYEE_NAME, edge="setup")
    r.tap(edge="setup", text="OK")
    r.wait_for(edge="setup", text=PAYEE_NAME, timeout=30)
    # Category: picker FAB opens the type selector; "Category"
    # (arrays.xml category_type, first item) opens the new-category
    # dialog; OK creates it and the loader shows the group row,
    # whose tap returns it (no subcategories, so the group tap
    # itself finishes the picker).
    r.tap(edge="setup", res_id="textViewCategory")
    r.wait_for(edge="setup", res_id="fab", timeout=30)
    r.tap(edge="setup", res_id="fab")
    r.wait_for(edge="setup", text="Category", timeout=30)
    r.tap(edge="setup", text="Category")
    r.wait_for(edge="setup", res_id="editTextCategName", timeout=30)
    r.tap(edge="setup", res_id="editTextCategName")
    r.type_text(CATEG_NAME, edge="setup")
    r.tap(edge="setup", text="OK")
    r.wait_for(edge="setup", text=CATEG_NAME, timeout=30)
    r.tap(edge="setup", text=CATEG_NAME)
    r.wait_for(edge="setup", text=CATEG_NAME, timeout=30)
    # Save: toolbar item "Save"; a successful save finishes the
    # editor back to the home list (CheckingTransactionEditActivity
    # onActionDoneClick: saveData true -> setResult OK -> finish).
    r.tap(edge="setup", text="Save")
    r.wait_for(edge="setup", text=ACCT_NAME, timeout=30)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="MMEX route_10 setup: bootstrap + account + one "
                    "transaction with a payee")
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
    deadline = time.time() + 60
    while time.time() < deadline:
        dump = _shell(adb, ["dumpsys", "activity", "activities"])
        if "mResumedActivity" in dump and "MainActivity" in dump:
            break
        time.sleep(2)
    else:
        _fail("MainActivity did not become the resumed activity in 60s")
    log("MainActivity resumed; app-created database schema is live")

    r = Runner(package=pkg, route="setup_route_10", edge_ids=None,
               log_path=args.log or os.path.join(gen_dir, "setup.log"),
               adb=adb, outdir=args.outdir or ".")
    try:
        create_account(r, ACCT_NAME)
        create_transaction(r)
        # Return to home (run_app.sh return-to-home rule): the route
        # script's plain launch would otherwise bring the existing
        # task forward wherever setup left it, so relaunch
        # MainActivity with NEW_TASK|CLEAR_TASK and wait for the
        # seeded account row before returning (setup_route_03
        # pattern; flag value 0x10008000 as used there).
        _shell(adb, ["am", "start", "-W", "-n", MAIN, "-f", "0x10008000"])
        r.wait_for(edge="setup", text=ACCT_NAME, timeout=30)
    finally:
        r.done()
    log("seeded account %r with one transaction (payee %r, category %r)"
        % (ACCT_NAME, PAYEE_NAME, CATEG_NAME))
    return 0


if __name__ == "__main__":
    sys.exit(main())
