#!/usr/bin/env python3
"""Replay script for hash-checker route_04.

Method: ThemeHelperModule.themeHelper
Edge ids (exact, in order, from ROUTES.csv):
    E372472a8 E3101d0cd E2211fe22
Printed route:
    graphs/hash-checker/scratch/route_print/ThemeHelperModule.themeHelper.txt
Permissions: none (ROUTES.csv permissions cell is empty).
Fixtures: none (ROUTES.csv fixtures cell is empty).
Setup: any file as input (fixtures).

Every edge after launch is a lifecycle or Dagger-injection call with
no user action of its own: the provider fires while MainActivity is
created, during App.appComponent.inject in MainActivity.onCreate.
The final wait is only a steady-state anchor proving the calculator
screen came up after the injection; it is not itself the edge's
trigger. No pm clear, fixture push, or permission grant happens here;
run_app.sh owns those steps.
"""

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, _ROOT)

from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E372472a8", "E3101d0cd", "E2211fe22",
]


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    runner = Runner(package=args.package, route="route_04",
                    edge_ids=EDGE_IDS, log_path=args.log,
                    dry_run=args.dry_run, adb=args.adb)

    # E372472a8: S_ENTRY -> MainActivity.<init>
    # Trigger: tap the launcher icon (MAIN + LAUNCHER intent filter).
    runner.launch(args.package + "/com.smlnskgmail.jaman.hashchecker.MainActivity",
                  "E372472a8")
    # E3101d0cd: MainActivity.<init> -> MainActivity.onCreate
    # Trigger: the system instantiates MainActivity, then calls onCreate.
    runner.comment("lifecycle: system calls MainActivity.onCreate",
                   "E3101d0cd")
    # E2211fe22: MainActivity.onCreate -> ThemeHelperModule.themeHelper
    # Trigger: virtual/interface call that can dispatch to this
    # implementation (through DaggerAppComponent.inject,
    # DaggerAppComponent.injectMainActivity,
    # ThemeHelperModule_ThemeHelperFactory.themeHelper). The injection
    # runs inside onCreate, before the calculator view exists, so the
    # "From" button wait below only proves the app reached its steady
    # state afterwards.
    runner.comment("Dagger inject in onCreate provides themeHelper",
                   "E2211fe22")
    runner.wait_for("E2211fe22",
                    res_id=args.package + ":id/btn_generate_from")
    runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
