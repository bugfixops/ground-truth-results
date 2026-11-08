"""MMEX route_13: RecurringTransactionIntentService.onHandleWork --
CONVERTED (retry).

Method: RecurringTransactionIntentService.onHandleWork
Edge ids (in route order):
    Ef7b742ce E5e28ba39 E345a16d3 E8368c44e E9e535c7e Ef6aef24f
    Eef61d710
Printed route source:
    graphs/MMEX/scratch/route_print_final2/RecurringTransactionIntentService.onHandleWork.txt
    (7 steps; header env=time state=settings). These edge ids match,
    in order, the verification.csv path row for
    RecurringTransactionIntentService.onHandleWork exactly (checked
    by the g3 draft; no discrepancy).
Permissions: none (no ENV permission gate; RECEIVE_BOOT_COMPLETED
    is an install-time manifest permission, AndroidManifest.xml:26).
Fixtures: none (no STATE file gate).
Setup: setup_route_13.py (bootstrap + recurring-notification prefs:
    notifications on, check time = host UTC now + 3 minutes). The
    previous unscriptable reason (the daily alarm fires only at the
    configured time, up to 24 h after boot) is removed in two steps:
    (a) the alarm time itself is moved into the near future through
    the very preference setAlarm reads (BehaviourSettings.
    getNotificationTime, default "08:00", settings/BehaviourSettings.
    java:45-47; setAlarm calendar logic at core/RecurringTransaction-
    BootReceiver.java:59-84, which adds a day only if the time has
    already passed); (b) after the boot broadcast, this script
    advances the device clock past the alarm time (rooted emulator;
    run_app.sh roots the device), which makes AlarmManager deliver
    the pending RTC_WAKEUP alarm, then restores the clock. If the
    clock step fails (e.g. adbd not root on the CI image), the
    script falls back to a plain 480 s wait for natural delivery.
    LIVE-RUN RISKS, stated plainly: AlarmManager.setRepeating is
    inexact, so natural delivery may lag; the clock step depends on
    root adbd and on the emulator honouring `date`. Either failure
    makes this route not-reached (unclear), never wrong -- the
    JaCoCo result decides. No step is faked: the broadcast is the
    real BOOT_COMPLETED broadcast to the real exported receiver
    (AndroidManifest.xml:108-112), and the alarm that fires is the
    alarm setAlarm itself scheduled.
Run (from the repo root, after the merger drops this file into
    device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_13.py --package
    com.money.manager.ex --log steps/route_13.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import datetime
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "Ef7b742ce", "E5e28ba39", "E345a16d3", "E8368c44e", "E9e535c7e",
    "Ef6aef24f", "Eef61d710",
]

PKG = "com.money.manager.ex"
BOOT_RECEIVER = "com.money.manager.ex/.core.RecurringTransactionBootReceiver"


def _adb(adb, args, timeout=60):
    return subprocess.run([adb] + args, capture_output=True, text=True,
                          timeout=timeout)


def _device_clock(adb):
    """Current device clock as a datetime, or None if unreadable."""
    try:
        out = _adb(adb, ["shell", "date", "+%m%d%H%M%Y.%S"]).stdout.strip()
        return datetime.datetime.strptime(out, "%m%d%H%M%Y.%S")
    except Exception:
        return None


def _set_clock(adb, when):
    """Set the device clock; True on success, False otherwise."""
    try:
        proc = _adb(adb, ["shell", "date",
                          when.strftime("%m%d%H%M%Y.%S")])
        return proc.returncode == 0
    except Exception:
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_13", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # Ef7b742ce: Deliver BOOT_COMPLETED to the exported boot
        # receiver (AndroidManifest.xml:108-112). The harness
        # broadcast builds `am broadcast -a ... -n ...`.
        r.broadcast(edge="Ef7b742ce",
                    action="android.intent.action.BOOT_COMPLETED",
                    component=BOOT_RECEIVER)
        # E5e28ba39: The framework calls onReceive on the receiver
        # it created (RecurringTransactionBootReceiver.java:40-47).
        r.comment("framework calls BootReceiver.onReceive",
                  edge="E5e28ba39")
        # E345a16d3: onReceive calls setAlarm (:43). No user action.
        r.comment("onReceive calls setAlarm", edge="E345a16d3")
        # E8368c44e: setAlarm schedules the daily repeating
        # RTC_WAKEUP alarm (setRepeating at :83-84) for the
        # notification time armed by setup_route_13.py. The alarm
        # delivery itself is a framework edge; the wait below is
        # what lets it fire inside the run's 10-minute script
        # timeout. In dry mode no adb and no sleep happen at all:
        # this block only logs the plan.
        if not args.dry_run:
            advanced = False
            now = _device_clock(args.adb)
            if now is not None:
                advanced = _set_clock(
                    args.adb, now + datetime.timedelta(minutes=10))
            if advanced:
                # Clock now past the alarm time: AlarmManager
                # delivers the pending alarm, then we restore the
                # clock to host UTC time (best effort; the emulator
                # clock is host-derived, so drift is bounded).
                time.sleep(60)
                host_now = datetime.datetime.now(datetime.timezone.utc)
                _set_clock(args.adb, host_now.replace(tzinfo=None))
            else:
                # Fallback: wait for natural (inexact) delivery.
                time.sleep(480)
        r.comment("daily alarm fires (framework AlarmManager delivery)",
                  edge="E8368c44e")
        # E9e535c7e: The system creates RecurringTransactionReceiver
        # and calls onReceive; the notification setting is on by
        # setup (default true, notifications/RecurringTransaction-
        # Receiver.java:31-39). No user action.
        r.comment("alarm broadcast calls Receiver.onReceive",
                  edge="E9e535c7e")
        # Ef6aef24f: onReceive enqueues the job service (:38).
        r.comment("Receiver.onReceive enqueues IntentService",
                  edge="Ef6aef24f")
        # Eef61d710: JobIntentService delivers the queued intent to
        # onHandleWork (notifications/RecurringTransactionIntent-
        # Service.java:39-48) -- target reached. With the seeded
        # empty database, notifyRepeatingTransaction finds no due
        # bill and posts nothing, but onHandleWork itself executes.
        r.comment("JobIntentService delivers onHandleWork (target "
                  "reached)", edge="Eef61d710")
    finally:
        r.done()


if __name__ == "__main__":
    main()
