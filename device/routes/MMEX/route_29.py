#!/usr/bin/env python3
# Re-scripted by Kiro, 2026-11-09, for the third and last real run (the 9 stale routes).
"""MMEX route_29: AppSettings.getPreferences.

Method: AppSettings.getPreferences
Edge ids (in route order, graphs/MMEX/out/methods.csv route_edge_ids of the final build):
    E71c76102 E2e074fc1 E5d5a9c2f Eff22f7d2 E36f6d77e Ea3f2e7b1
    E0b875140
(7 steps; env=- state=-). The earlier device row replayed the 8-step open-database intent route (handleIntent ->
changeDatabase), which is no longer the best route; the staged .mmb of the old setup is not needed.
Permissions: none. Fixtures: none.
Setup: setup_route_29.py (bootstrap + one account named "RetryCheck", type Cash; a copy of setup_route_04.py), so the
    home list has the "Cash Accounts" group (HomeFragment.java:840-841, R.string.cash_accounts), expanded by default
    (HomeFragment.java:747-759).
UI: tap the group header to collapse it (HomeFragment.java:710-719: onGroupCollapse writes the expanded flag through
    AppSettings, SettingsBase.set -> getPreferences).
Run (from the repo root):
    python3 -I device/routes/MMEX/route_29.py --package com.money.manager.ex --log steps/route_29.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E5d5a9c2f", "Eff22f7d2", "E36f6d77e",
    "Ea3f2e7b1", "E0b875140",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_29", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        r.launch("com.money.manager.ex/.home.MainActivity", edge="E71c76102")
        r.comment("framework calls MainActivity.onCreate", edge="E2e074fc1")
        r.comment("MainActivity.onCreate calls initHomeFragment", edge="E5d5a9c2f")
        r.comment("home screen shown (HomeFragment committed)", edge="Eff22f7d2")
        # E36f6d77e: tap the expanded group header to collapse it.
        r.wait_for(text="Cash Accounts", edge="E36f6d77e", timeout=30)
        r.tap(text="Cash Accounts", edge="E36f6d77e")
        r.comment("onGroupCollapse stores the collapsed flag", edge="Ea3f2e7b1")
        r.comment("SettingsBase.set reads AppSettings.getPreferences: target reached", edge="E0b875140")
        r.dwell(edge="E0b875140", seconds=2)
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
