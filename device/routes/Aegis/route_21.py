#!/usr/bin/env python3
# Re-scripted by Kiro, 2026-11-09, for the third and last real run (the 9 stale routes): the current best route of
# Salsa20Engine.salsaCore is the unlock of an existing password vault, not the first-run intro of the earlier script.
"""Aegis route_21: Salsa20Engine.salsaCore.

Method: Salsa20Engine.salsaCore
Edge ids (in route order, graphs/Aegis/out/methods.csv route_edge_ids of the final build):
    Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd
    E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5
    E4520b83d Ec2a7b2f4 E45df5be5 E8ef49332 E7545a097 E996ea32b
    E0205a921 E95462315 Ecc90cdf7 E19236baa Effe83609 E89dde570
(24 steps; env=- state=-). The earlier device row replayed the 25-step intro route (MainActivity.onStart ->
startIntroActivity -> ... -> SecuritySetupSlide.deriveKey), which is no longer the best route: the baseline has a vault.
Permissions: none. Fixtures: none.
Setup: setup_route_21.py: creates the password vault through the first-run intro (baseline: onboarding passed, a password
    vault), before the discard coverage dump, then kills the app.
UI selectors (app sources): text_password (res/layout/activity_auth.xml:55; the standard field, since the PIN keyboard
    setting is off by default, AuthActivity.java:82-89) and button_decrypt (activity_auth.xml:87, "Unlock").
Run (from the repo root):
    python3 -I device/routes/Aegis/route_21.py --package com.beemdevelopment.aegis.debug
    --log steps/route_21.log --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

PKG = "com.beemdevelopment.aegis.debug"
MAIN = PKG + "/com.beemdevelopment.aegis.ui.MainActivity"
PASSWORD = "testpassword123"

EDGE_IDS = [
    "Eb9515d18",
    "E5b266140",
    "E1ef992ce",
    "E88ed9829",
    "E28ffc58c",
    "Eb76444fd",
    "E3a06baed",
    "Eef600725",
    "E06202b0e",
    "E0158aff6",
    "E911809ef",
    "E87843ac5",
    "E4520b83d",
    "Ec2a7b2f4",
    "E45df5be5",
    "E8ef49332",
    "E7545a097",
    "E996ea32b",
    "E0205a921",
    "E95462315",
    "Ecc90cdf7",
    "E19236baa",
    "Effe83609",
    "E89dde570",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    main_component = args.package + "/com.beemdevelopment.aegis.ui.MainActivity"
    r = Runner(package=args.package, route="route_21", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # Eb9515d18: the process starts (application class created first).
        r.comment("process start: application class created first", edge="Eb9515d18")
        # E5b266140: Hilt superclass onCreate, then AegisApplicationBase.onCreate.
        r.comment("Hilt superclass onCreate, then AegisApplicationBase.onCreate", edge="E5b266140")
        # E1ef992ce: direct call into AegisApplicationBase.onCreate.
        r.comment("direct call into AegisApplicationBase.onCreate", edge="E1ef992ce")
        # E88ed9829: the application is created; the process can start a component.
        r.comment("application created; process can start a component", edge="E88ed9829")
        # E28ffc58c: tap the Aegis icon in the launcher (MAIN / LAUNCHER).
        r.launch(main_component, edge="E28ffc58c")
        # Eb76444fd, E3a06baed: MainActivity onCreate, onStart.
        r.comment("MainActivity onCreate after constructor", edge="Eb76444fd")
        r.comment("MainActivity onStart after onCreate", edge="E3a06baed")
        # Eef600725: the vault exists and is encrypted, not loaded: onStart starts the unlock screen.
        r.comment("vault exists, encrypted, not loaded: startAuthActivity", edge="Eef600725")
        # E06202b0e .. E87843ac5: AuthActivity is started, created and resumed; the unlock page is shown.
        r.comment("AuthActivity started", edge="E06202b0e")
        r.comment("AuthActivity onCreate", edge="E0158aff6")
        r.comment("AuthActivity onResume", edge="E911809ef")
        r.wait_for(res_id="button_decrypt", edge="E87843ac5", timeout=30)
        # E4520b83d: type the password and tap Unlock.
        r.tap(res_id="text_password", edge="E4520b83d")
        r.type_text(PASSWORD, edge="E4520b83d")
        r.tap(res_id="button_decrypt", edge="E4520b83d")
        # Ec2a7b2f4 .. E89dde570: the decrypt task derives the key from the password through SCrypt.
        r.comment("PasswordSlotDecryptTask doInBackground", edge="Ec2a7b2f4")
        r.dwell(edge="Ec2a7b2f4", seconds=8)
        r.comment("PasswordSlotDecryptTask.decrypt", edge="E45df5be5")
        r.comment("decryptPasswordSlot", edge="E8ef49332")
        r.comment("PasswordSlot.deriveKey(char[])", edge="E7545a097")
        r.comment("CryptoUtils.deriveKey(char[])", edge="E996ea32b")
        r.comment("CryptoUtils.deriveKey(byte[])", edge="E0205a921")
        r.comment("SCrypt.generate", edge="E95462315")
        r.comment("SCrypt.MFcrypt", edge="Ecc90cdf7")
        r.comment("SCrypt.SMix", edge="E19236baa")
        r.comment("SCrypt.BlockMix", edge="Effe83609")
        r.comment("BlockMix calls salsaCore: target reached", edge="E89dde570")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
