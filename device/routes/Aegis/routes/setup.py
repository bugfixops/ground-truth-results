#!/usr/bin/env python3
# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# Shared per-app setup for Aegis: INTENTIONALLY A NO-OP (logs only, drives no UI,
# provisions no vault, grants nothing, pushes nothing).
#
# Why a no-op, as a proposal for the merger to confirm (see
# D1D3D7_REPORT.md, row-14 decision): the current runner invokes this file
# once per route, after pm clear and before the route script, with only
# --package --log --outdir — it receives NO route argument, so it cannot
# know which route it is setting up. A shared setup that drove the intro
# vault creation would corrupt every route whose own prefix creates or
# imports its vault (new rows 01, 03-08, 10-17, 19, 21-23 drive intro or
# Welcome-import edges themselves) and would fight the two-phase scripts
# (rows 18, 20) that prepare their own state in-script. Vault and seed
# provisioning therefore lives per route: in the route script itself
# (intro prefix, in-script seeding, two-phase preparation) and in the
# per-route setup_route_NN.py generators (run-time fixture files into the
# gen dir, pushed by the runner for gen: entries). If the merger instead
# wants a shared setup, it must be one that is safe for ALL 25 rows
# (for example, truly nothing, as here) — a UI-driving shared setup cannot
# be correct under the current no-route-argument contract.
#
# Interface (runner contract): --package PKG --log LOG --outdir DIR.
# Exits 0. No real emulator/adb run, no CI request, no drycheck pass claimed.
"""Aegis shared setup.py (staging): no-op by design. See header comment."""

import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", default="")
    parser.add_argument("--log", default="")
    parser.add_argument("--outdir", default="")
    args = parser.parse_args()
    msg = ("Aegis setup.py: no-op by design (staging proposal); "
           "vault provisioning is per-route, see D1D3D7_REPORT.md\n")
    if args.log:
        try:
            with open(args.log, "a", encoding="utf-8") as f:
                f.write(msg)
        except OSError:
            pass
    sys.stdout.write(msg)
    sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
