#!/usr/bin/env python3
"""MMEX per-route setup for route_14
(RecurringTransactionListActivity.onActivityResult) -- UI-driving seed.

Bootstrap (identical mechanism to setup_route_23.py, q.v. for the
full citations): empty .mmb pushed to /sdcard/MoneyManagerEx/mmex.mmb,
default SharedPreferences written via run-as (prefshowtutorial=false,
databasepath set), MainActivity warm-launched so the app's own
MmxOpenHelper.onCreate creates the schema (tables_v1 + initDatabase).
This setup additionally sets the recurring-transaction notification
preference explicitly true (key string
"prefrepeatingtransactionnotifications", res/values/prefids.xml:83;
BehaviourSettings.getNotificationRecurringTransaction defaults to
true, settings/BehaviourSettings.java:41-43, and the preference XML
default is true, res/xml/preferences_behaviour.xml:23) so the route's
poster gate at home/MainActivity.java:1236-1237 cannot be off.

Seed, in order (see GROUNDING_14.md for per-tap citations):

1. One account "RetryDue", created through AccountEditActivity
   (setup_route_23 pattern: name field, calculator balance, Save).
2. One due recurring transaction ("RetryDue" account, "RetryPayee"
   payee, "RetryCat" category, amount 100, Monthly recurrence, next
   occurrence two days in the past), created through
   RecurringTransactionEditActivity with ACTION_INSERT (exported,
   AndroidManifest.xml ~240). The next-occurrence field is the
   payment date (NEXTOCCURRENCEDATE): RecurringTransactionEditActivity
   defaults it to today (initializeModel), and each tap of
   paymentPreviousDayButton moves it one day back
   (initializePaymentDateSelector). Two taps put it two days in the
   past, so the notification query's DAYSLEFT<=0 filter
   (notifications/RecurringTransactionNotifications.java:68-78)
   returns this row. Monthly (not the default Once) is chosen so
   populateScheduledTransactions' moveNextOccurrence advances the
   bill instead of deleting it (servicelayer/
   RecurringTransactionService.java: ONCE branch deletes).
3. A passcode "12345", set through Settings -> Security ->
   Activate Passcode, entered twice (route_05 precedent;
   settings/SecuritySettingsFragment.java:55-60, 103-118).

Ending state (read this before "fixing" it to the setup_route_03
pattern): this setup does NOT end with a CLEAR_TASK relaunch of
MainActivity. A MainActivity onCreate after step 2 would run
populateScheduledTransactions, which posts the notification AND
consumes the due bill (it inserts the account transaction and calls
moveNextOccurrence, home/MainActivity.java:1281-1285), so the route
script's own launch would find no due bill and post nothing fresh.
Instead the setup ends with kill_app (HOME + am kill, harness
kill_app): the device is left at the launcher home with no
MainActivity instance alive, so the route script's plain launch
creates the FIRST MainActivity instance after seeding and its
onCreate posts the fresh notification on the printed path. That
satisfies run_app.sh's return-to-home rule in substance (no setup
UI state leaks into the route script's starting state) while
preserving the due bill; see GROUNDING_14.md section 4.

Failure mode: any step failing exits 1 -> run_app.sh
failed_at_step_0 (setup_failed). Nothing is faked: if a seed row is
not created, the route script's notification wait fails honestly.
This setup is NOT executed by drycheck (only py_compiled when it
backs a gen: fixture, and it backs none, so it is entirely
dry-unvalidated -- run_app.sh MMEX-B3-UIDRIVE drycheck gap); it is
validated on the live run.

Usage (invoked by run_app.sh):
    setup_route_14.py --package <pkg> --log <log> --outdir <dir> \
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
ACCT_NAME = "RetryDue"
PAYEE_NAME = "RetryPayee"
CATEG_NAME = "RetryCat"
PASSCODE_DIGITS = ["1", "2", "3", "4", "5"]

PREFS_XML = """<?xml version='1.0' encoding='utf-8' standalone='yes' ?>
<map>
    <string name="databasepath">/sdcard/MoneyManagerEx/mmex.mmb</string>
    <boolean name="prefshowtutorial" value="false" />
    <boolean name="prefrepeatingtransactionnotifications" value="true" />
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


def enter_passcode(r):
    """Enter 12345 on a PasscodeActivity keypad (digit texts)."""
    r.wait_for(edge="setup", res_id="editTextPasscode1", timeout=30)
    for digit in PASSCODE_DIGITS:
        r.tap(edge="setup", text=digit)


def create_due_recurring(r):
    """Create the due recurring transaction through its edit form."""
    r.start_intent(edge="setup", action="android.intent.action.INSERT",
                   component=PKG + "/.recurring.transactions"
                   ".RecurringTransactionEditActivity")
    r.wait_for(edge="setup", res_id="paymentDateTextView", timeout=30)
    # Account: spinner backed by the account-name list
    # (EditTransactionCommonFunctions.initAccountSelectors); the
    # dropdown item text is the account name.
    r.tap(edge="setup", res_id="spinnerAccount")
    r.wait_for(edge="setup", text=ACCT_NAME, timeout=30)
    r.tap(edge="setup", text=ACCT_NAME)
    # Recurrence: spinnerFrequencies entries are
    # res/values/arrays.xml frequencies_items; "Monthly" is the
    # Monthly entry (res/values/strings.xml:239), index 3, which
    # the edit activity's listener stores as recurrence 3.
    r.tap(edge="setup", res_id="spinnerFrequencies")
    r.wait_for(edge="setup", text="Monthly", timeout=30)
    r.tap(edge="setup", text="Monthly")
    # Next occurrence: payment date defaults to today; each
    # paymentPreviousDayButton tap moves it one day back, so two
    # taps put it two days in the past (DAYSLEFT <= 0).
    r.tap(edge="setup", res_id="paymentPreviousDayButton")
    r.tap(edge="setup", res_id="paymentPreviousDayButton")
    # Payee: picker FAB opens the new-payee dialog; in PICK mode
    # confirming auto-selects the new payee and returns
    # (PayeeListFragment FAB + dialog + sendResultToActivity).
    r.tap(edge="setup", res_id="textViewPayee")
    r.wait_for(edge="setup", res_id="fab", timeout=30)
    r.tap(edge="setup", res_id="fab")
    r.wait_for(edge="setup", res_id="editTextPayeeName", timeout=30)
    r.tap(edge="setup", res_id="editTextPayeeName")
    r.type_text(PAYEE_NAME, edge="setup")
    r.tap(edge="setup", text="OK")
    r.wait_for(edge="setup", text=PAYEE_NAME, timeout=30)
    # Category: picker FAB opens the type selector; "Category" is
    # the first category_type item (res/values/strings.xml:128).
    # The category dialog only inserts + reloads, so the new group
    # row must then be tapped to pick it (group click with zero
    # subcategories returns the result).
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
    # Amount via the calculator (same keys as the account form).
    r.tap(edge="setup", res_id="textViewAmount")
    r.wait_for(edge="setup", res_id="buttonKeyEqual", timeout=30)
    r.tap(edge="setup", text="1")
    r.tap(edge="setup", text="0")
    r.tap(edge="setup", text="0")
    r.tap(edge="setup", res_id="buttonKeyEqual")
    r.wait_for(edge="setup", res_id="textViewAmount", timeout=30)
    # Save (toolbar item titled "Save") returns to the home list.
    r.tap(edge="setup", text="Save")
    r.wait_for(edge="setup", text=ACCT_NAME, timeout=30)


def set_passcode(r):
    """Set passcode 12345 via Settings -> Security (route_05 flow)."""
    r.key("MENU", edge="setup")
    r.tap(edge="setup", text="Settings")
    r.wait_for(edge="setup", text="Security", timeout=30)
    r.tap(edge="setup", text="Security")
    r.wait_for(edge="setup", text="Activate Passcode", timeout=30)
    r.tap(edge="setup", text="Activate Passcode")
    # First entry, then the re-entry screen, then the second entry.
    enter_passcode(r)
    enter_passcode(r)
    r.wait_for(edge="setup", text="Activate Passcode", timeout=30)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="MMEX route_14 setup: bootstrap + account + due "
                    "recurring transaction + passcode")
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
    # database path set, recurring notifications explicitly on.
    # The app is not running (pm clear just ran), so no in-memory
    # preference cache can overwrite this file.
    prefs_local = os.path.join(gen_dir, "mmex_prefs.xml")
    with open(prefs_local, "w", encoding="utf-8") as f:
        f.write(PREFS_XML)
    _adb(adb, ["push", prefs_local, "/sdcard/mmex_prefs.xml"])
    # Storage grant (audit section 2.6, option (a)): run_app.sh
    # grants ROUTES permissions only AFTER setup, and the bootstrap
    # DB lives on shared /sdcard, so setup grants storage itself
    # before the run-as copy and the warm launch.
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
    log("wrote shared prefs %s (tutorial off, databasepath set, "
        "recurring notifications on)" % PREFS_NAME)

    # 3. Warm launch: MainActivity onCreate opens the database, which
    # runs MmxOpenHelper.onCreate (tables_v1 + initDatabase). No due
    # bill exists yet, so this launch posts no notification and
    # consumes nothing.
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

    r = Runner(package=pkg, route="setup_route_14", edge_ids=None,
               log_path=args.log or os.path.join(gen_dir, "setup.log"),
               adb=adb, outdir=args.outdir or ".")
    try:
        create_account(r, ACCT_NAME)
        log("seeded account %r" % ACCT_NAME)
        create_due_recurring(r)
        log("seeded due recurring transaction (account %r, payee %r, "
            "category %r, Monthly, next occurrence 2 days past)"
            % (ACCT_NAME, PAYEE_NAME, CATEG_NAME))
        set_passcode(r)
        log("set passcode 12345 via Settings -> Security")
        # Ending state: kill the app to the launcher home. Do NOT
        # CLEAR_TASK-relaunch MainActivity here: that relaunch's
        # onCreate would consume the due bill (see module
        # docstring). The route script's launch is then the first
        # MainActivity onCreate after seeding.
        r.kill_app(edge="setup")
    finally:
        r.done()
    log("setup done: app killed to launcher home; due bill unconsumed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
