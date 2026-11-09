#!/usr/bin/env python3
"""Aegis per-route setup for route_21 (Salsa20Engine.salsaCore). Kiro, 2026-11-09 (third run, stale-route re-script).

The current best route of the target is the unlock of an existing password vault (MainActivity.onStart ->
startAuthActivity -> AuthActivity, unlock tap -> PasswordSlotDecryptTask -> SCrypt -> Salsa20Engine.salsaCore). After
`pm clear` the app has no vault, so this setup creates one through the first-run intro (Welcome -> Next, security
picker -> Password -> Next, setup slide -> both password fields -> Next, Done), the baseline state of the class rule
(onboarding passed, a password vault). It runs BEFORE the discard coverage dump, so its own key derivation is not counted
in the route's coverage; it ends on HOME and kills the app, so the route script starts a fresh process.

Selectors (app sources): btnNext (activity_intro.xml), rb_password (fragment_security_picker_slide.xml), text_password and
text_password_confirm (SecuritySetupSlide.java:56-57). The password is the one route_21.py types at the unlock screen.

Invoked by run_app.sh after `pm clear`, before the fixture phase and the route script:
    setup_route_21.py --package <pkg> --log <log> --outdir <dir> --gen-dir <dir> [--adb adb]
Any failure exits non-zero (failed_at_step_0, setup_failed: unclear, never wrong).
"""

import argparse
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(HERE))))

PASSWORD = "testpassword123"


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--package", default="com.beemdevelopment.aegis.debug")
    p.add_argument("--log", default=None)
    p.add_argument("--outdir", default=None)
    p.add_argument("--gen-dir", default=None)
    p.add_argument("--adb", default="adb")
    a = p.parse_args(argv)
    gen_dir = a.gen_dir or os.environ.get("GEN_DIR", "") or os.getcwd()
    os.makedirs(gen_dir, exist_ok=True)

    from device.harness import Runner
    r = Runner(package=a.package, route="route_21-setup", edge_ids=None,
               log_path=a.log or os.path.join(gen_dir, "setup.log"), adb=a.adb,
               outdir=a.outdir or gen_dir)
    main_component = a.package + "/com.beemdevelopment.aegis.ui.MainActivity"
    try:
        r.launch(main_component, edge="setup")
        r.tap(res_id="btnNext", edge="setup")            # Welcome -> security picker
        r.tap(res_id="rb_password", edge="setup")        # choose Password
        r.tap(res_id="btnNext", edge="setup")            # picker -> password setup slide
        r.tap(res_id="text_password", edge="setup")
        r.type_text(PASSWORD, edge="setup")
        r.tap(res_id="text_password_confirm", edge="setup")
        r.type_text(PASSWORD, edge="setup")
        r.tap(res_id="btnNext", edge="setup")            # key derivation, then the Done slide
        r.dwell(edge="setup", seconds=8)
        r.tap(res_id="btnNext", edge="setup")            # Done: the vault is written, the list opens
        r.dwell(edge="setup", seconds=3)
        r.kill_app(edge="setup")                         # HOME + am kill: the route starts a fresh process
        time.sleep(1)
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
