"""MMEX route_12: IncomeVsExpensesListFragment$1.run.

Method: IncomeVsExpensesListFragment$1.run
Edge ids (in route order):
    E71c76102 E2e074fc1 E5d5a9c2f Eff22f7d2 Ef93f69de E6b63531e
    Eac39a25e E470440ef Ebfbf7e82 E6df1962a E428631c7 Ed2e1013e
    E645f3932 Ef27e0542
Printed route source:
    graphs/MMEX/scratch/route_print_final2/IncomeVsExpensesListFragment_1.run.txt
    (14 steps). These edge ids match, in order, the ROUTES.csv row
    for route_12 exactly.
Permissions: none (ROUTES.csv permissions cell empty; the print
    header env=hardware is the tablet-layout gate, not a manifest
    permission, and it is satisfied by the wm size/density set in
    setup_route_12.py, not by a grant).
Fixtures: none (no STATE file gate).
Setup: setup_route_12.py (B3 bootstrap + wm size 1920x1200 /
    wm density 240 + account "Retry12" + Deposit 100 + Withdrawal
    50, both dated today, sharing payee "RetryPayee" and category
    "RetryCat"; ends with the return-to-home rule, so this script
    starts on the home screen).
Tablet cleanup: setup_route_12.py sets the tablet size and this
    script resets it, because run_app.sh does pm clear between
    routes but does NOT reset wm size. The reset is cleanup, not
    an edge: it runs in the finally block before done() (so the
    device is restored even if a tap fails), via subprocess adb
    exactly as route_13.py uses subprocess adb for its clock step,
    and it is skipped in dry mode (drycheck runs this script with
    --dry-run and there is no device to reset). A reset failure
    fails the route loudly after the log is closed -- a leaked
    tablet size must never pass silently. The harness itself sets
    the same restore-before-done rule for its own global settings
    (set_locale, set_always_finish in device/harness/harness.py).
    Precedent for the reset itself: the retry pass
    (device-draft/retry/RETRY_REPORT.md section 12) and audit
    b3-device/AUDIT.md section 4.6 both require `wm size reset` /
    `wm density reset` at the script's end so later routes are not
    polluted; no landed route script yet performs a wm reset, so
    this is the first such cleanup and the auditor should confirm
    the contract point (see GROUNDING_12.md section 3).
Settle wait: the final edge's Runnable is posted with a 1000 ms
    delay (IncomeVsExpensesListFragment.java:195), after the
    REPORT loader delivers asynchronously. After the final comment
    this script sleeps 5 s in live mode only (not a Runner step,
    not an edge) so the Runnable fires before the reset and done().
    In dry mode no time passes.
Run (from the repo root, after the merger drops this file into
    device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_12.py --package
    com.money.manager.ex --log steps/route_12.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E5d5a9c2f", "Eff22f7d2", "Ef93f69de",
    "E6b63531e", "Eac39a25e", "E470440ef", "Ebfbf7e82", "E6df1962a",
    "E428631c7", "Ed2e1013e", "E645f3932", "Ef27e0542",
]


def _reset_tablet_size(adb):
    """Restore the phone wm configuration. Raises on failure."""
    for args in (["shell", "wm", "size", "reset"],
                 ["shell", "wm", "density", "reset"]):
        proc = subprocess.run([adb] + args, capture_output=True,
                              text=True, timeout=60)
        if proc.returncode != 0:
            raise RuntimeError("wm reset failed (%s): %s" % (
                " ".join(args), proc.stderr.strip()[:300]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_12", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    reset_error = None
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
        # Ef93f69de: Tap the Income vs Expenses card on the home
        # screen. The card carries android:onClick=
        # "onClickCardViewIncomesVsExpenses" at
        # res/layout/home_fragment.xml:127, and its header text is
        # "@string/income_vs_expenses_current_month" =
        # "Income vs Expenses: Current Month"
        # (res/values/strings.xml:293), inside the card's bounds.
        # Tapping the header text node therefore lands inside the
        # card and fires the card's onClick (see GROUNDING_12.md
        # section 1 for the dispatch caveat, carried as a live-run
        # risk). The handler starts IncomeVsExpensesActivity
        # (MainActivity.java:832-834).
        r.tap(text="Income vs Expenses: Current Month",
              edge="Ef93f69de")
        # E6b63531e: onClickCardViewIncomesVsExpenses starts
        # IncomeVsExpensesActivity (MainActivity.java:832-834).
        # No separate user action.
        r.comment("card tap starts IncomeVsExpensesActivity",
                  edge="E6b63531e")
        # Eac39a25e: The framework calls
        # IncomeVsExpensesActivity.onCreate right after the
        # constructor. No user action.
        r.comment("framework calls IncomeVsExpensesActivity.onCreate",
                  edge="Eac39a25e")
        # E470440ef: onCreate adds the list fragment when
        # fragmentMain is empty (IncomeVsExpensesActivity.java:
        # 50-53); the fragment manager then calls
        # onActivityCreated. No user action.
        r.comment("list fragment added, onActivityCreated follows",
                  edge="E470440ef")
        # Ebfbf7e82: onActivityCreated inits the YEARS loader
        # (IncomeVsExpensesListFragment.java:113). No user action.
        r.comment("onActivityCreated inits YEARS loader",
                  edge="Ebfbf7e82")
        # E6df1962a: The years loader (lines 142-146) delivers its
        # cursor and the LoaderManager calls onLoadFinished for
        # YEARS (lines 199-212). No user action.
        r.comment("YEARS loader delivers, onLoadFinished YEARS",
                  edge="E6df1962a")
        # E428631c7: The YEARS branch of onLoadFinished calls
        # startLoader (line 212) once the years cursor has a first
        # row (guard, line 200). No user action.
        r.comment("YEARS branch calls startLoader",
                  edge="E428631c7")
        # Ed2e1013e: startLoader restarts the REPORT loader
        # (lines 401-410). No user action.
        r.comment("startLoader restarts REPORT loader",
                  edge="Ed2e1013e")
        # E645f3932: The report loader (lines 135-140) delivers its
        # cursor and the LoaderManager calls onLoadFinished for
        # REPORT (lines 158-162). No user action.
        r.comment("REPORT loader delivers, onLoadFinished REPORT",
                  edge="E645f3932")
        # Ef27e0542: In the REPORT branch, when mIsDualPanel is true
        # (guard, line 188 -- true only under the tablet layout
        # set by setup_route_12.py, IncomeVsExpensesActivity.
        # java:46), a Handler posts the Runnable with a 1000 ms
        # delay (lines 189-195) and the Runnable's run() calls
        # showChart (line 193). No user action; the settle wait
        # below lets the delayed Runnable fire in live mode.
        r.comment("dual-panel REPORT branch posts $1 Runnable",
                  edge="Ef27e0542")
        if not args.dry_run:
            time.sleep(5)
    finally:
        # Tablet cleanup (not an edge): restore the phone wm
        # configuration before done(), even on failure, and fail
        # loudly if the restore itself fails -- never leak the
        # tablet size into later routes. Skipped in dry mode.
        if not args.dry_run:
            try:
                _reset_tablet_size(args.adb)
            except Exception as exc:  # noqa: BLE001 - reported below
                reset_error = exc
                print("route_12 WARNING: wm reset failed: %s" % exc,
                      file=sys.stderr)
        r.done()
    if reset_error is not None:
        raise RuntimeError("wm reset failed: %s" % reset_error)
    return 0


if __name__ == "__main__":
    sys.exit(main())
