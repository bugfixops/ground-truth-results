#!/usr/bin/env python3
"""Device route script for Currency route_14.

Method: Main.lambda$onUpdateClick$1
Edge ids, in order: E012ed474 Ee88066da Ef071a802 E4dd486ed Efc50320e
    Edca2fa28 Eba2f6640 E016892e6 E38895bf6
Printed route file: graphs/Currency/scratch/route_print/Main.lambda$onUpdateClick$1.txt
Permissions: none
Fixtures: none
Setup: network (ECB); cert issue on API<=27 images

State notes: run_app.sh runs pm clear before this script, so Main starts
in DISPLAY_MODE (selectList empty, Main.java:351-352) and the DISPLAY
menu (main.xml) applies. In main.xml, Update is showAsAction never, so
it is reached only through the overflow menu ("More options" on AOSP);
its title is "Update" (strings.xml). The dialog built by updateDialog
(Main.java:1098-1115) has OK / Cancel buttons (strings ok/cancel) and
an EditText prefilled with the formatted extra value, so tapping OK
fires the lambda's BUTTON_POSITIVE branch without typing anything.
"""

import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from device.harness import Runner  # noqa: E402

EDGE_IDS = ["E012ed474", "Ee88066da", "Ef071a802", "E4dd486ed",
            "Efc50320e", "Edca2fa28", "Eba2f6640", "E016892e6",
            "E38895bf6"]
LAUNCHER = "org.billthefarmer.currency/.Main"


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    r = Runner(package=args.package, route="route_14", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, outdir=args.outdir,
               adb=args.adb)
    try:
        # E012ed474: S_ENTRY -> Main.<init>. Tap the Currency icon in
        # the launcher (MAIN/LAUNCHER intent filter; Main is the
        # launcher activity in AndroidManifest.xml:19-24).
        r.launch(LAUNCHER, edge="E012ed474")

        # Ee88066da: Main.<init> -> Main.onCreate. Lifecycle edge: the
        # system instantiates Main, then calls onCreate. No user
        # action exists.
        r.comment("lifecycle: system instantiates Main, then onCreate",
                  edge="Ee88066da")

        # Ef071a802: Main.onCreate -> Main.onResume (onStart ->
        # onResume). Lifecycle edge: no user action exists.
        r.comment("lifecycle: onStart -> onResume", edge="Ef071a802")

        # E4dd486ed: Main.onResume -> S_MAIN_DISPLAY. Main becomes
        # visible in DISPLAY_MODE (no selection kept after pm clear).
        # No user action exists.
        r.comment("Main visible in DISPLAY_MODE after pm clear",
                  edge="E4dd486ed")

        # Efc50320e: S_MAIN_DISPLAY -> Main.onOptionsItemSelected@DISPLAY.
        # Open the overflow menu: Update is showAsAction never in
        # main.xml, so it is not an action-bar icon.
        r.tap(desc="More options", edge="Efc50320e")

        # Edca2fa28: Main.onOptionsItemSelected@DISPLAY ->
        # Main.onUpdateClick. switch case R.id.action_update
        # (Main.java:785-786): tap the "Update" overflow item.
        r.tap(text="Update", edge="Edca2fa28")

        # Eba2f6640: Main.onUpdateClick -> Main.updateDialog.
        # updateDialog(R.string.update_extra, extra, R.string.decimal,
        # listener) (Main.java:1045). Automatic after the tap; no user
        # action exists.
        r.comment("automatic: onUpdateClick opens updateDialog",
                  edge="Eba2f6640")

        # E016892e6: Main.updateDialog -> S_DLG_UPDATE. dialog.show():
        # AlertDialog with an EditText and OK / Cancel buttons
        # (Main.java:1098-1115). Automatic; no user action exists.
        r.comment("automatic: update dialog shown with OK / Cancel",
                  edge="E016892e6")

        # E38895bf6: S_DLG_UPDATE -> Main.lambda$onUpdateClick$1. Tap
        # a dialog button: OK fires the lambda's BUTTON_POSITIVE
        # branch (Main.java:1046,1102-1103). The EditText is prefilled
        # with the formatted extra value, so no typing is needed.
        # This is the target edge.
        r.tap(text="OK", edge="E38895bf6")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
