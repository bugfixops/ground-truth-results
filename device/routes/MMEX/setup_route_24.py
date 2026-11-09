#!/usr/bin/env python3
"""MMEX per-route setup for route_24 (NumericHelper.getNumberOfDecimals). Kiro, 2026-11-09: a copy of setup_route_04.py (bootstrap + the
account "RetryCheck") for the re-scripted current best route of the third real run: long press the RetryCheck row, Balance account: the amount dialog truncates to the currency.
The text below is setup_route_04's, whose account facts hold unchanged here.

Bootstrap (same mechanism as setup_route_20, q.v. for citations):
empty .mmb pushed to /sdcard/MoneyManagerEx/mmex.mmb, default
SharedPreferences written via run-as (prefshowtutorial=false,
databasepath set), MainActivity warm-launched so the app's own
MmxOpenHelper.onCreate creates the schema (tables_v1 + initDatabase).

Seed (drives UI through the harness Runner with edge_ids=None, as the
retry contract allows; setup actions log under edge "setup" in the
separate setup log, never against a route edge):

- One account named "RetryCheck", created through the app's own
  AccountEditActivity, launched with ACTION_INSERT (the activity is
  exported with EDIT/INSERT intent filters, AndroidManifest.xml
  ~232). Form grounding:
    - name field res_id editTextAccountName
      (res/layout/activity_account_edit.xml:53);
    - type spinner left at its default position 0 = "Cash"
      (res/values/arrays.xml:76-84 accounttype_items; default
      position 0, AccountEditActivity.java:285-290) -- Cash is
      non-investment, satisfying route_04's guard that the tapped
      row's account type is not INVESTMENT (HomeFragment.java:
      699, 701-702: investment rows post RequestWatchlistFragment-
      Event instead of RequestAccountFragmentEvent);
    - currency defaults to the base currency (USD, seeded by
      tables_v1.sql:219), so validateData's currency check
      (AccountEditActivity.java:643-646) passes;
    - initial balance entered through the calculator (tap
      editTextInitialBalance, keys "1" "0" "0", "=") so
      validateData's balance check (:647-650) passes;
    - status defaults to the first status item "Open"
      (arrays.xml:91-94), date defaults to today (:361-367);
    - save is the toolbar item titled "Save"
      (MenuHelper.addSaveToolbarIcon, core/MenuHelper.java:87-89;
      res/values/strings.xml:772).
  No transaction rows are needed: route_04's tail is
  AccountTransactionListFragment.onEvent -> displayRunningBalances
  (AccountTransactionListFragment.java:409-413), which forwards
  whatever balances the task computed, with no non-empty guard, so
  an empty account still reaches the target through the status-menu
  reload path.
  The route script then taps this known name on the
  home list: tap(text="RetryCheck") resolves the CHILD row, because
  its text differs from every group header ("Bank Accounts",
  "Cash Accounts", ...). The original collision was res_id-only:
  group and child rows share layout item_account_bills and id
  textViewItemAccountName (HomeAccountsExpandableAdapter.java:115
  and 201), so a res_id lookup returns the first match, the group
  header. A text lookup with a setup-known name has no such
  collision. Groups expand by default on fresh preferences
  (HomeFragment.setVisibilityOfAccountGroups reads each group key
  with default true, HomeFragment.java:747-759), so no expansion
  tap is needed.

Failure mode: any step exits 1 -> run_app.sh failed_at_step_0.
This setup is NOT executed by drycheck (only py_compiled for gen:
fixtures); it is validated on the live run.

Usage (invoked by run_app.sh):
    setup_route_24.py --package <pkg> --log <log> --outdir <dir> \
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
ACCT_NAME = "RetryCheck"

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


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="MMEX route_24 setup: bootstrap + one known account")
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

    mmb_local = os.path.join(gen_dir, "mmex.mmb")
    with open(mmb_local, "wb") as f:
        pass
    _shell(adb, ["mkdir", "-p", "/sdcard/MoneyManagerEx"])
    _adb(adb, ["push", mmb_local, DB_DEVICE_PATH])
    prefs_local = os.path.join(gen_dir, "mmex_prefs.xml")
    with open(prefs_local, "w", encoding="utf-8") as f:
        f.write(PREFS_XML)
    _adb(adb, ["push", prefs_local, "/sdcard/mmex_prefs.xml"])
    # Storage grant (audit §2.6, option (a)): run_app.sh grants ROUTES
    # permissions only AFTER setup, and the bootstrap DB lives on shared
    # /sdcard, so setup grants storage itself before the run-as copy
    # and the warm launch.
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
    log("bootstrap prefs written (tutorial off, databasepath set)")

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

    r = Runner(package=pkg, route="setup_route_24", edge_ids=None,
               log_path=args.log or os.path.join(gen_dir, "setup.log"),
               adb=adb, outdir=args.outdir or ".")
    try:
        create_account(r, ACCT_NAME)
    finally:
        r.done()
    log("seeded account %r on the home list" % ACCT_NAME)
    return 0


if __name__ == "__main__":
    sys.exit(main())
