#!/usr/bin/env python3
# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# New row 24: Hilt_AegisApplication.<init>. Verdict class: SCRIPTABLE (firm, pending drycheck and real run).
# TO-VERIFY (still open, never claimed): launch only; JaCoCo mapping for the generated Hilt class is a coverage question, not a scriptability blocker.
# Edge ids are EXACTLY the regenerated verification.csv path row (SHA 83c527cad5a03ec8c5e002e2b5177ceee79572e0ec8885133635139cb4074321).
# Action bodies carried from merger staging-D1 old row 24 with renumbering
# per ROUTES_NOTES.md. No real emulator/adb run, no CI request, no drycheck
# pass and no D9 pass is claimed by this staging file.
"""Aegis route_24: Hilt_AegisApplication.<init>.

Method: Hilt_AegisApplication.<init>
Edge ids (in route order):
    Eb9515d18 Ecaf88dff
Printed route source: graphs/Aegis/scratch/routes_postvault.txt,
    section "Hilt_AegisApplication.<init>" (2 steps, judged
    CORRECT), plus graphs/Aegis/out/methods.csv (same edge list)
    and graphs/Aegis/out/aegis_trigger_graph.json (edges above).
Permissions: none (ROUTES-g3.csv permissions cell empty; the route
    has no ENV permission gate and methods.csv env_kinds is empty).
Fixtures: none.
Setup: first-run vault creation (work-emulator ci/apps.csv Aegis
    row). No vault interaction is needed: this is a process-start
    route, scripted launch-only following the landed Currency
    route_15 precedent (a class-initialisation target reached by
    launching the app's MAIN/LAUNCHER activity). The target is
    reached at process start: launching MainActivity creates
    the process, the system instantiates AegisApplication, and
    its constructor runs the generated Hilt superclass
    constructor (AegisApplication extends Hilt_AegisApplication;
    source AegisApplication.java:6 has no onCreate of its own).
    The second edge is therefore a comment, not a tap: no user
    action exists for a superclass constructor.
Run (from the repo root, after the merger places this file at
    device/routes/Aegis/route_24.py):
    python3 -I device/routes/Aegis/route_24.py --package
    com.beemdevelopment.aegis.debug --log steps/route_24.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

PKG = "com.beemdevelopment.aegis.debug"
MAIN = PKG + "/com.beemdevelopment.aegis.ui.MainActivity"

EDGE_IDS = [
    "Eb9515d18", "Ecaf88dff"
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
        # Eb9515d18: Any outside trigger starts the app process;
        # the application class is created first. Launching the
        # MAIN/LAUNCHER activity is that trigger.
        r.launch(MAIN, edge="Eb9515d18")
        # Ecaf88dff: AegisApplication.<init> -> Hilt_AegisApplication
        # .<init> (direct call). Superclass constructor: runs as
        # part of process start, no user action. Target reached.
        r.comment("superclass constructor runs at process start: "
                  "target reached", edge="Ecaf88dff")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
