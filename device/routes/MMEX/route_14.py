"""MMEX route_14: RecurringTransactionListActivity.onActivityResult.

Method: RecurringTransactionListActivity.onActivityResult
Edge ids (in route order):
    E71c76102 E2e074fc1 E00ecbc65 E44a6cda6 E18f2d60d Ec7b6275e
    E0d135dde E5947e9db Ea5a84992
Printed route source:
    graphs/MMEX/scratch/route_print_final2/RecurringTransactionListActivity.onActivityResult.txt
    (9 steps; header env=system_event state=data;settings).
Permissions: none (no ENV permission gate in the print header, so
    no permission from the manifest is granted by this route).
Fixtures: none (no STATE file gate).
Setup: setup_route_14.py (bootstrap + account "RetryDue" + due
    Monthly recurring transaction with next occurrence 2 days in
    the past + passcode 12345; ends with the app killed to the
    launcher home so this script's launch is the first MainActivity
    onCreate after seeding -- see GROUNDING_14.md section 4).
Harness note: the landed harness (device/harness/harness.py) has NO
    notification-shade primitive -- no shade, notification, or
    status-bar method exists in its Runner (method list: launch,
    key, back, rotate, kill_app, relaunch, restore_from_recents,
    set_always_finish, set_locale, tap, long_tap, drag, drag_from,
    tap_row_action, two_finger_swipe, two_finger_tap, type_text,
    scroll_to, wait_for, dwell, start_intent, broadcast, grant,
    deny, push_fixture, screenshot, dump_ui, assert_text, comment,
    done). The shade is therefore expanded with a live-only adb
    subprocess (`adb shell cmd statusbar expand-notifications`),
    guarded by `if not args.dry_run` exactly as route_13.py guards
    its raw adb clock calls, and the notification row is then tapped
    with the ordinary Runner tap (the harness dump has no package
    filter, so tap/wait_for operate on system UI too). Drycheck
    cannot validate the shade step: it only dry-loads this script,
    and the subprocess never runs in dry mode, so a drycheck PASS
    says nothing about the live shade expansion -- that is a
    live-run risk carried in GROUNDING_14.md, not a drycheck PASS.
Starting-state note: because the setup set a passcode,
    MainActivity.onStart prompts for it on this fresh launch
    (home/MainActivity.java:252-260). Entering it here is a
    starting-state consequence, not a route edge; it sits between
    the Ec7b6275e comment and the E0d135dde shade tap.
Run (from the repo root, after the merger drops this file into
    device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_14.py --package
    com.money.manager.ex --log steps/route_14.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E00ecbc65", "E44a6cda6", "E18f2d60d",
    "Ec7b6275e", "E0d135dde", "E5947e9db", "Ea5a84992",
]

PASSCODE_DIGITS = ["1", "2", "3", "4", "5"]
# Notification content text (setContentText, R.string.
# notification_repeating_transaction_expired, res/values/
# strings.xml:269): the row text tapped in the shade.
NOTIFICATION_TEXT = "There are expired scheduled transactions"
PASSCODE_PROMPT = "Enter your passcode"


def _expand_notifications(adb):
    """Expand the notification shade; raise loudly on failure."""
    proc = subprocess.run(
        [adb, "shell", "cmd", "statusbar", "expand-notifications"],
        capture_output=True, text=True, timeout=30)
    if proc.returncode != 0:
        raise RuntimeError(
            "cmd statusbar expand-notifications failed (%s): %s"
            % (proc.returncode, proc.stderr.strip()[:300]))


def _enter_passcode(r, edge):
    """Enter passcode 12345 on the PasscodeActivity keypad."""
    r.wait_for(edge=edge, text=PASSCODE_PROMPT, timeout=30)
    for digit in PASSCODE_DIGITS:
        r.tap(edge=edge, text=digit)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_14", edge_ids=EDGE_IDS,
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
        # E00ecbc65: MainActivity.onCreate calls
        # populateScheduledTransactions directly
        # (MainActivity.java:244). Guard !showPrerequisite()
        # (MainActivity.java:184-187): tutorial off and a database
        # available, both set by setup_route_14.py. No user action.
        r.comment("MainActivity.onCreate calls "
                  "populateScheduledTransactions", edge="E00ecbc65")
        # E44a6cda6: populateScheduledTransactions calls
        # notifyRepeatingTransaction when the notification setting
        # is on (MainActivity.java:1236-1239; setting default true,
        # explicitly true in the setup prefs). No user action.
        r.comment("populateScheduledTransactions calls "
                  "notifyRepeatingTransaction", edge="E44a6cda6")
        # E18f2d60d: notifyRepeatingTransaction calls
        # notifyRepeatingTransaction_Internal directly
        # (RecurringTransactionNotifications.java:54).
        # No user action.
        r.comment("notifyRepeatingTransaction calls "
                  "notifyRepeatingTransaction_Internal",
                  edge="E18f2d60d")
        # Ec7b6275e: _Internal calls showNotification when the
        # DAYSLEFT<=0 query returns a row
        # (RecurringTransactionNotifications.java:68-78: query,
        # count > 0, showNotification). The setup's due bill is
        # that row. No user action.
        r.comment("due row found, _Internal calls showNotification",
                  edge="Ec7b6275e")
        # Starting-state consequence (not a route edge): this fresh
        # MainActivity instance prompts for the passcode in onStart
        # (MainActivity.java:252-260) because the setup set one.
        # Enter it so the home screen, not the passcode screen, is
        # foreground when the shade is pulled.
        _enter_passcode(r, edge="E0d135dde")
        # E0d135dde: The user taps the recurring transaction
        # notification. showNotification built it with a
        # PendingIntent for RecurringTransactionListActivity
        # carrying INTENT_EXTRA_LAUNCH_NOTIFICATION=true
        # (RecurringTransactionNotifications.java:90-94), so the
        # tap starts that activity. In dry mode only the plan is
        # logged: the shade expansion is a live-only adb call
        # (see module docstring) and drycheck cannot validate it.
        if args.dry_run:
            r.comment("tap notification in shade (dry: shade "
                      "expansion is live-only)", edge="E0d135dde")
        else:
            _expand_notifications(args.adb)
            r.wait_for(edge="E0d135dde", text=NOTIFICATION_TEXT,
                       timeout=30)
            r.tap(edge="E0d135dde", text=NOTIFICATION_TEXT)
        # E5947e9db: The framework calls
        # RecurringTransactionListActivity.onCreate after the
        # constructor. No user action.
        r.comment("framework calls RecurringTransactionListActivity"
                  ".onCreate", edge="E5947e9db")
        # Ea5a84992: onCreate starts PasscodeActivity for result
        # when launched from the notification and a passcode is set
        # (RecurringTransactionListActivity.java:48-56). Enter the
        # setup passcode; the fifth digit makes PasscodeActivity
        # set RESULT_OK and finish (PasscodeActivity.java:101-131),
        # and the framework delivers the result to
        # RecurringTransactionListActivity.onActivityResult (the
        # target). TARGET REACHED on the framework delivery.
        _enter_passcode(r, edge="Ea5a84992")
        r.comment("PasscodeActivity returns RESULT_OK; framework "
                  "delivers onActivityResult (target)",
                  edge="Ea5a84992")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
