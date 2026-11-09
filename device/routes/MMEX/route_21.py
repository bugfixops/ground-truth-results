#!/usr/bin/env python3
# Re-scripted by Kiro, 2026-11-09, for the third and last real run (the 9 stale routes).
"""MMEX route_21: DefinedDateRange$1.<init>.

Method: DefinedDateRange$1.<init>
Edge ids (in route order, graphs/MMEX/out/methods.csv route_edge_ids of the final build):
    E71c76102 E2e074fc1 E5d5a9c2f Eff22f7d2 Ebbb78d0f Ee424c2e8
    Ebc409bd4 Ebb57ba7f E5e7583d5 E6cd10559 E994a6b75 E865a392e
    E7551131a E931a290d Ead211413 E0d84e708 Ea1f3a9f7
(17 steps; env=- state=-, class library: the account list fragment is shown through EventBus). The earlier device row
replayed the 20-step drawer -> Settings -> Look and feel route, which is no longer the best route.
Permissions: none. Fixtures: none.
Setup: setup_route_21.py (bootstrap + one account named "RetryCheck", type Cash; a copy of setup_route_04.py). The
    account's group is expanded by default (HomeFragment.java:747-759), so tap(text="RetryCheck") resolves the child row.
Run (from the repo root):
    python3 -I device/routes/MMEX/route_21.py --package com.money.manager.ex --log steps/route_21.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E5d5a9c2f", "Eff22f7d2", "Ebbb78d0f",
    "Ee424c2e8", "Ebc409bd4", "Ebb57ba7f", "E5e7583d5", "E6cd10559",
    "E994a6b75", "E865a392e", "E7551131a", "E931a290d", "Ead211413",
    "E0d84e708", "Ea1f3a9f7",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_21", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E71c76102: launch the MAIN/LAUNCHER activity.
        r.launch("com.money.manager.ex/.home.MainActivity", edge="E71c76102")
        r.comment("framework calls MainActivity.onCreate", edge="E2e074fc1")
        r.comment("MainActivity.onCreate calls initHomeFragment", edge="E5d5a9c2f")
        r.comment("home screen shown (HomeFragment committed)", edge="Eff22f7d2")
        # Ebbb78d0f: tap the seeded account child row (HomeFragment.java:686-706).
        r.wait_for(text="RetryCheck", edge="Ebbb78d0f", timeout=30)
        r.tap(text="RetryCheck", edge="Ebbb78d0f")
        r.comment("child click posts RequestAccountFragmentEvent", edge="Ee424c2e8")
        r.comment("onEvent shows the account fragment", edge="Ebc409bd4")
        r.comment("showAccountFragment creates the list fragment", edge="Ebb57ba7f")
        r.comment("newInstance creates the fragment", edge="E5e7583d5")
        r.comment("fragment attached", edge="E6cd10559")
        r.comment("fragment onCreate", edge="E994a6b75")
        r.dwell(edge="E994a6b75", seconds=3)
        r.comment("onCreate calls updateFilterDateRange", edge="E865a392e")
        r.comment("updateFilterDateRange builds DefinedDateRanges", edge="E7551131a")
        r.comment("DefinedDateRanges.initialize", edge="E931a290d")
        r.comment("DefinedDateRanges.create", edge="Ead211413")
        r.comment("DefinedDateRange class initialised", edge="E0d84e708")
        r.comment("DefinedDateRange$1 constant built: target reached", edge="Ea1f3a9f7")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
