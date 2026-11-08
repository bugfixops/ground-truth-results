#!/usr/bin/env python3
# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# New row 21: Salsa20Engine.salsaCore. Verdict class: SCRIPTABLE (firm, pending drycheck and real run).
# TO-VERIFY (still open, never claimed): live-dump selector confirmation only; the setup-slide password is typed in-run.
# Edge ids are EXACTLY the regenerated verification.csv path row (SHA 83c527cad5a03ec8c5e002e2b5177ceee79572e0ec8885133635139cb4074321).
# Action bodies carried from merger staging-D1 old row 21 with renumbering
# per ROUTES_NOTES.md. No real emulator/adb run, no CI request, no drycheck
# pass and no D9 pass is claimed by this staging file.
"""Aegis route_21: Salsa20Engine.salsaCore.

Method: Salsa20Engine.salsaCore
Edge ids (in route order):
    Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd
    E3a06baed E0602e719 E4ce5043a E5e63fbe7 E93598a00 E1440feb8
    E6830b6dc E4fd4b49f Ead078030 Ef86589e4 Ec6041c17 E679fa2b8
    Eabd4923f E0205a921 E95462315 Ecc90cdf7 E19236baa Effe83609
    E89dde570
Printed route source: graphs/Aegis/scratch/routes_postvault.txt,
    section "Salsa20Engine.salsaCore" (25 steps, judged CORRECT),
    plus graphs/Aegis/out/methods.csv (same edge list) and
    graphs/Aegis/out/aegis_trigger_graph.json (edges above).
Permissions: none (ROUTES-g3.csv permissions cell empty; the route
    has no ENV permission gate and methods.csv env_kinds is empty).
Fixtures: none.
Setup: first-run vault creation (work-emulator ci/apps.csv Aegis
    row). The script drives the intro itself: Welcome -> security
    picker (Password) -> setup slide, where the Next tap on the
    unfinished slide starts key derivation, which reaches the
    target through SCrypt.
UI selectors (from the app sources, not a live dump):
    intro Next button: res_id btnNext (activity_intro.xml: it has
    an arrow icon and no text, so res_id is the only selector);
    security radio: res_id rb_password (fragment_security_picker_
    slide.xml); setup password fields: res_id text_password and
    text_password_confirm (SecuritySetupSlide.java:56-57).
    The password radio tap is an unlisted micro-action inside
    step 14's block: the dump has no separate edge for choosing
    the radio, only for the Next tap that moves picker -> setup.
Run (from the repo root, after the merger places this file at
    device/routes/Aegis/route_21.py):
    python3 -I device/routes/Aegis/route_21.py --package
    com.beemdevelopment.aegis.debug --log steps/route_21.log
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
PASSWORD = "testpassword123"

EDGE_IDS = [
    "Eb9515d18", "E5b266140", "E1ef992ce", "E88ed9829", "E28ffc58c", "Eb76444fd",
    "E3a06baed", "E0602e719", "E4ce5043a", "E5e63fbe7", "E93598a00", "E1440feb8",
    "E6830b6dc", "E4fd4b49f", "Ead078030", "Ef86589e4", "Ec6041c17", "E679fa2b8",
    "Eabd4923f", "E0205a921", "E95462315", "Ecc90cdf7", "E19236baa", "Effe83609",
    "E89dde570"
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
        # Eb9515d18: Any outside trigger starts the app process.
        # (Process start itself; the launch below is its action.)
        r.comment("process start: application class created first",
                  edge="Eb9515d18")
        # E5b266140: Application.onCreate: Hilt superclass onCreate
        # runs first, then AegisApplicationBase.onCreate.
        r.comment("Hilt superclass onCreate, then "
                  "AegisApplicationBase.onCreate", edge="E5b266140")
        # E1ef992ce: Hilt onCreate -> AegisApplicationBase.onCreate.
        r.comment("direct call into AegisApplicationBase.onCreate",
                  edge="E1ef992ce")
        # E88ed9829: The application is created; the process can
        # start a component.
        r.comment("application created; process can start a component",
                  edge="E88ed9829")
        # E28ffc58c: Tap the Aegis icon in the launcher
        # (MAIN / LAUNCHER).
        r.launch(MAIN, edge="E28ffc58c")
        # Eb76444fd: Activity.onCreate after the constructor.
        r.comment("MainActivity onCreate after constructor",
                  edge="Eb76444fd")
        # E3a06baed: Activity.onStart after onCreate.
        r.comment("MainActivity onStart after onCreate", edge="E3a06baed")
        # E0602e719: No vault file exists (fresh install): the
        # intro starts and onStart returns.
        r.comment("fresh install, no vault file: intro starts",
                  edge="E0602e719")
        # E4ce5043a: startActivityForResult(IntroActivity).
        r.comment("intro activity started", edge="E4ce5043a")
        # E5e63fbe7: Activity.onCreate of the intro.
        r.comment("IntroActivity onCreate", edge="E5e63fbe7")
        # E93598a00: addSlide: Direct call.
        r.comment("intro adds its slides", edge="E93598a00")
        # E1440feb8: The first slide (Welcome) is shown.
        r.comment("Welcome slide shown", edge="E1440feb8")
        # E6830b6dc: Next on Welcome (Welcome did not import):
        # the security picker is shown.
        r.tap(res_id="btnNext", edge="E6830b6dc")
        # E4fd4b49f: Next on the security picker: the password
        # setup slide is shown. The picker chose password: first
        # tap the Password radio (unlisted micro-action inside
        # this step; the dump has no separate radio edge here),
        # then tap Next.
        r.tap(res_id="rb_password", edge="E4fd4b49f")
        r.tap(res_id="btnNext", edge="E4fd4b49f")
        # Ead078030: Next on the setup slide when it is not
        # finished: goToNextSlide calls onNotFinishedError, which
        # starts key derivation. Fill both password fields with
        # matching passwords first (the slide is unfinished until
        # derivation produces the password slot).
        r.tap(res_id="text_password", edge="Ead078030")
        r.type_text(PASSWORD, edge="Ead078030")
        r.tap(res_id="text_password_confirm", edge="Ead078030")
        r.type_text(PASSWORD, edge="Ead078030")
        r.tap(res_id="btnNext", edge="Ead078030")
        # Ef86589e4: Next on the password setup with matching
        # passwords: key derivation starts (consequence of the
        # Next tap; the derivation runs async).
        r.comment("passwords match: key derivation starts",
                  edge="Ef86589e4")
        r.dwell(edge="Ef86589e4", seconds=5)
        # Ec6041c17: AsyncTask runs doInBackground on the worker
        # thread (derive the key from the password).
        r.comment("KeyDerivationTask doInBackground", edge="Ec6041c17")
        # E679fa2b8: PasswordSlot.deriveKey(char[], SCryptParameters).
        r.comment("PasswordSlot.deriveKey", edge="E679fa2b8")
        # Eabd4923f: CryptoUtils.deriveKey(char[], SCryptParameters).
        r.comment("CryptoUtils.deriveKey(char[])", edge="Eabd4923f")
        # E0205a921: CryptoUtils.deriveKey(byte[], SCryptParameters).
        r.comment("CryptoUtils.deriveKey(byte[])", edge="E0205a921")
        # E95462315: SCrypt.generate.
        r.comment("SCrypt.generate", edge="E95462315")
        # Ecc90cdf7: SCrypt.MFcrypt.
        r.comment("SCrypt.MFcrypt", edge="Ecc90cdf7")
        # E19236baa: SCrypt.SMix.
        r.comment("SCrypt.SMix", edge="E19236baa")
        # Effe83609: SCrypt.BlockMix.
        r.comment("SCrypt.BlockMix", edge="Effe83609")
        # E89dde570: SCrypt.BlockMix -> Salsa20Engine.salsaCore:
        # target reached.
        r.comment("BlockMix calls salsaCore: target reached",
                  edge="E89dde570")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
