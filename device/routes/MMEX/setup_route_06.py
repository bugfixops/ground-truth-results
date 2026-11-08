#!/usr/bin/env python3
"""MMEX per-route setup for route_06 (SplitRecurringCategoriesRepository.insert).

Bootstrap (same mechanism as setup_route_23, q.v. for citations):
empty .mmb pushed to /sdcard/MoneyManagerEx/mmex.mmb, default
SharedPreferences written via run-as (prefshowtutorial=false,
databasepath set), MainActivity warm-launched so the app's own
MmxOpenHelper.onCreate creates the schema (tables_v1 + initDatabase).

Seed (UI-driving, admitted by decision MMEX-B3-UIDRIVE; see the
run_app.sh per-route setup contract): one known non-investment
account "RetryRecur", created through the app's own
AccountEditActivity, launched with ACTION_INSERT. Form grounding
is the same as setup_route_23:
    - name field res_id editTextAccountName
      (res/layout/activity_account_edit.xml:53);
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

Why only an account is seeded, and nothing else (see GROUNDING_06.md
for the full split rationale):
    - Payee: the route script creates its payee inline. The edit
      form's payee field opens PayeeActivity with ACTION_PICK
      (EditTransactionCommonFunctions.java:570-584), and the payee
      list's FAB opens a new-payee dialog whose OK button creates
      the payee AND returns it to the form in one step when picking
      (PayeeListFragment.java:389-403, 431-433). Pre-seeding a
      payee would only add a list row to tap; it buys nothing.
    - Category: the route script uses categories the app itself
      seeds on first open (tables_v1.sql:108-131: "Bills" with
      "Telephone", "Food" with "Groceries"). No seeding needed.
    - Split entries: MUST NOT be pre-seeded. The target edge fires
      only for split items whose id is null or NOT_SET
      (RecurringTransactionEditActivity.java:571-580), and a
      pre-seeded split would be an existing database row (update
      branch, not insert). The two split entries are therefore
      created fresh inside the route script, in the split form.

Return-to-home rule (run_app.sh contract, setup_route_03 pattern):
after seeding, MainActivity is relaunched with NEW_TASK|CLEAR_TASK
(flags 0x10008000) and the script waits for the seeded account row
before done(), so no setup UI state (AccountEditActivity stack)
leaks into the route script, whose launch then brings the home
screen forward.

Failure mode: any step exits 1 -> run_app.sh failed_at_step_0.
This setup is NOT executed by drycheck (only py_compiled when it
backs a gen: fixture, and it backs none); it is validated on the
live run.

Usage (invoked by run_app.sh):
    setup_route_06.py --package <pkg> --log <log> --outdir <dir> \
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
ACCT_NAME = "RetryRecur"

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
        description="MMEX route_06 setup: bootstrap + known account")
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

    r = Runner(package=pkg, route="setup_route_06", edge_ids=None,
               log_path=args.log or os.path.join(gen_dir, "setup.log"),
               adb=adb, outdir=args.outdir or ".")
    try:
        create_account(r, ACCT_NAME)
        # Return to home: relaunch MainActivity with NEW_TASK |
        # CLEAR_TASK and wait for the seeded account row before
        # returning, so the route script starts from the home list
        # and never from the account editor's stack.
        _shell(adb, ["am", "start", "-W", "-n", MAIN, "-f", "0x10008000"])
        r.wait_for(edge="setup", text=ACCT_NAME, timeout=30)
    finally:
        r.done()
    log("seeded account %r on the home list" % ACCT_NAME)
    return 0


if __name__ == "__main__":
    sys.exit(main())
