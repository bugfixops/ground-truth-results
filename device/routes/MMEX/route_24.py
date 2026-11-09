#!/usr/bin/env python3
# Re-scripted by Kiro, 2026-11-09, for the third and last real run (the 9 stale routes).
"""MMEX route_24: NumericHelper.getNumberOfDecimals.

Method: NumericHelper.getNumberOfDecimals
Edge ids (in route order, graphs/MMEX/out/methods.csv route_edge_ids of the final build):
    E71c76102 E2e074fc1 E5d5a9c2f Eff22f7d2 E1644b6d5 Ed53fefe5
    Effcbf1e0 Ebdf66967 Ed01ff055 Eddab3db0
(10 steps; env=- state=-). The earlier device row replayed the 8-step home-screen widget route
(AccountBillsWidgetProvider.onUpdate), which is no longer the best route.
Permissions: none. Fixtures: none.
Setup: setup_route_24.py (bootstrap + one account named "RetryCheck", type Cash; a copy of setup_route_04.py).
UI: long press the account row; the context menu item "Balance account" (R.string.balance_account,
    HomeFragment.java:470-471) opens AmountInputDialog (HomeFragment.java:545-548).
Run (from the repo root):
    python3 -I device/routes/MMEX/route_24.py --package com.money.manager.ex --log steps/route_24.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E5d5a9c2f", "Eff22f7d2", "E1644b6d5",
    "Ed53fefe5", "Effcbf1e0", "Ebdf66967", "Ed01ff055", "Eddab3db0",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_24", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        r.launch("com.money.manager.ex/.home.MainActivity", edge="E71c76102")
        r.comment("framework calls MainActivity.onCreate", edge="E2e074fc1")
        r.comment("MainActivity.onCreate calls initHomeFragment", edge="E5d5a9c2f")
        r.comment("home screen shown (HomeFragment committed)", edge="Eff22f7d2")
        # E1644b6d5: long press the account row, then "Balance account" in its context menu.
        r.wait_for(text="RetryCheck", edge="E1644b6d5", timeout=30)
        r.long_tap(text="RetryCheck", edge="E1644b6d5")
        r.tap(text="Balance account", edge="E1644b6d5")
        r.comment("onContextItemSelected calls startBalanceAccount", edge="Ed53fefe5")
        r.comment("AmountInputDialog shown (onCreate)", edge="Effcbf1e0")
        r.dwell(edge="Effcbf1e0", seconds=2)
        r.comment("initializeNewDialog", edge="Ebdf66967")
        r.comment("truncateToCurrency", edge="Ed01ff055")
        r.comment("getNumberOfDecimals: target reached", edge="Eddab3db0")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
