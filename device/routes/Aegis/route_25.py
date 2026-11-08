#!/usr/bin/env python3
# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# New row 25: AegisApplication.<init>. Verdict class: SCRIPTABLE (firm, pending drycheck and real run).
# TO-VERIFY (still open, never claimed): launch only; no fixture, picker, camera, or account dependency.
# Edge ids are EXACTLY the regenerated verification.csv path row (SHA 83c527cad5a03ec8c5e002e2b5177ceee79572e0ec8885133635139cb4074321).
# Action bodies carried from merger staging-D1 old row 25 with renumbering
# per ROUTES_NOTES.md. No real emulator/adb run, no CI request, no drycheck
# pass and no D9 pass is claimed by this staging file.
"""Aegis route_25: AegisApplication.<init>.

Method: AegisApplication.<init>
Edge ids (in route order):
    Eb9515d18
Printed route source: graphs/Aegis/scratch/routes_postvault.txt,
    section "AegisApplication.<init>" (1 step, judged CORRECT),
    plus graphs/Aegis/out/methods.csv (same edge list) and
    graphs/Aegis/out/aegis_trigger_graph.json (edge above).
Permissions: none (ROUTES-g3.csv permissions cell empty; the route
    has no ENV permission gate and methods.csv env_kinds is empty).
Fixtures: none.
Setup: first-run vault creation (work-emulator ci/apps.csv Aegis
    row). No vault interaction is needed: this is a process-start
    route, scripted launch-only following the landed Currency
    route_15 precedent. The single edge IS the target: launching
    the MAIN/LAUNCHER activity starts the process and the system
    instantiates the manifest application class
    (AndroidManifest.xml:21-27, android:name=".AegisApplication").
    The target is reached at process start, before any activity
    UI appears.
Run (from the repo root, after the merger places this file at
    device/routes/Aegis/route_25.py):
    python3 -I device/routes/Aegis/route_25.py --package
    com.beemdevelopment.aegis.debug --log steps/route_25.log
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
    "Eb9515d18"
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_25", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # Eb9515d18: Any outside trigger starts the app process;
        # the application class is created first. Launching the
        # MAIN/LAUNCHER activity is that trigger, and the created
        # class is the target itself.
        r.launch(MAIN, edge="Eb9515d18")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
