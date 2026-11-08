#!/usr/bin/env python3
"""Currency route_05: ChoiceDialog.onRestoreInstanceState.

Method: ChoiceDialog.onRestoreInstanceState
Edge ids in order:
    E012ed474 Ee88066da Ef071a802 E4dd486ed Efc50320e E81249289
    Ea8c3b3b7 E66b0b6ad Ea6de7fcb Ed26a607d Eb43116bb
Printed route: graphs/Currency/scratch/route_print/ChoiceDialog.onRestoreInstanceState.txt
    (REACHABLE, SOURCE_OK, ref ChoiceDialog.java:134).
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none.
Setup: network (ECB); cert issue on API<=27 images (ROUTES.csv setup
    column; no network step is needed on this route).
Launcher: org.billthefarmer.currency/.Main (AndroidManifest.xml:18-25,
    MAIN/LAUNCHER). run_app.sh already does pm clear, permission
    grants, fixture pushes, and per-app setup before this script, so
    the script performs only the route actions starting from launch.

Mapping notes:
  - The DISPLAY menu (res/menu/main.xml) shows Add as an icon
    (showAsAction="ifRoom"); its title is "Add"
    (res/values/strings.xml:5), so it is tapped by content
    description, not text. That drives Main.onOptionsItemSelected
    case R.id.action_add (Main.java:777-778) -> onAddClick ->
    startActivityForResult(ChoiceDialog) (Main.java:857-858).
  - The picker is opened with nothing selected (choose.xml: Clear /
    Select start disabled; ChoiceDialog.java:96-129), exactly the
    S_CHOICE_DISPLAY@MAIN state the printed route rotates from, so
    no row is tapped before rotating: tapping a row would move the
    picker out of the printed state.
  - Rotation: the harness has no public rotate() or
    configuration-change action (only launch, key, tap, long_tap,
    type_text, scroll_to, wait_for, start_intent, broadcast, and
    evidence calls). Rotation is therefore driven through the
    harness's own adb shell helper, Runner._shell, which every public
    action funnels through: first disable auto-rotate
    (accelerometer_rotation 0), then set user_rotation 1
    (landscape). ChoiceDialog declares no configChanges in
    AndroidManifest.xml, so the rotation recreates it and the
    framework calls onSaveInstanceState before onStop and then
    onRestoreInstanceState on the new instance
    (ChoiceDialog.java:134-179, 176-182). If the merger requires
    public-API-only scripts, this is the one edge pair that needs a
    public rotate() added to the harness instead.
  - After the target, the script deliberately does NOT rotate back:
    rotating back would recreate the picker again after the target
    edge, and a restore step needs a route edge id, which the route
    does not provide. The device is left in landscape; the
    device lead should reset orientation in setup before the next
    route (accelerometer_rotation back to 1).
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E012ed474", "Ee88066da", "Ef071a802", "E4dd486ed", "Efc50320e",
    "E81249289", "Ea8c3b3b7", "E66b0b6ad", "Ea6de7fcb", "Ed26a607d",
    "Eb43116bb",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Currency route_05")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_05", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E012ed474 S_ENTRY -> Main.<init>: launch the MAIN/LAUNCHER
    # activity (AndroidManifest.xml:18-25).
    r.launch(args.package + "/.Main", edge="E012ed474")
    # Ee88066da Main.<init> -> Main.onCreate: the system instantiates
    # Main, then calls onCreate (Main.java:242). No user action.
    r.comment("system instantiates Main, then onCreate",
              edge="Ee88066da")
    # Ef071a802 Main.onCreate -> Main.onResume: onStart -> onResume
    # (Main.java:369). No user action.
    r.comment("onStart -> onResume", edge="Ef071a802")
    # E4dd486ed Main.onResume -> S_MAIN_DISPLAY: Main becomes visible
    # in DISPLAY_MODE (Main.java:351-352; pm clear leaves no
    # selection). No user action.
    r.comment("Main visible in DISPLAY_MODE", edge="E4dd486ed")
    # Efc50320e S_MAIN_DISPLAY -> Main.onOptionsItemSelected@DISPLAY:
    # tap a menu item in the action bar (res/menu/main.xml). Add is
    # an ifRoom icon item, tapped by its title description.
    r.tap(edge="Efc50320e", desc="Add")
    # E81249289 Main.onOptionsItemSelected@DISPLAY -> Main.onAddClick:
    # switch case R.id.action_add (Main.java:777-778). Automatic
    # after the tap. No further action.
    r.comment("switch case R.id.action_add", edge="E81249289")
    # Ea8c3b3b7 Main.onAddClick -> ChoiceDialog.<init>@MAIN:
    # startActivityForResult(new Intent(this, ChoiceDialog.class), 0)
    # (Main.java:857-858). Automatic after the tap. No further action.
    r.comment("startActivityForResult(ChoiceDialog)", edge="Ea8c3b3b7")
    # E66b0b6ad ChoiceDialog.<init>@MAIN -> ChoiceDialog.onCreate@MAIN:
    # the system instantiates ChoiceDialog (dialog-themed activity),
    # then onCreate (ChoiceDialog.java:59). No user action.
    r.comment("system instantiates ChoiceDialog, then onCreate",
              edge="E66b0b6ad")
    # Ea6de7fcb ChoiceDialog.onCreate@MAIN -> S_CHOICE_DISPLAY@MAIN:
    # picker shown, nothing selected (ChoiceDialog.java:96-129;
    # res/layout/choose.xml Clear/Select disabled). No user action.
    r.comment("picker shown, nothing selected", edge="Ea6de7fcb")
    # Ed26a607d S_CHOICE_DISPLAY@MAIN ->
    # ChoiceDialog.onSaveInstanceState@MAIN: rotate the device while
    # the picker is open. The harness has no public rotate(), so
    # this uses its own adb shell helper (see header): disable
    # auto-rotate, then force landscape. State is saved before
    # onStop on recreation.
    r._shell(["settings", "put", "system", "accelerometer_rotation",
              "0"], edge="Ed26a607d", action="rotate_setup",
              target="accelerometer_rotation=0")
    r._shell(["settings", "put", "system", "user_rotation", "1"],
             edge="Ed26a607d", action="rotate",
             target="user_rotation=1")
    # Eb43116bb ChoiceDialog.onSaveInstanceState@MAIN ->
    # ChoiceDialog.onRestoreInstanceState@MAIN: rotation recreates
    # the picker (new instance: onCreate, then onRestoreInstanceState
    # with the saved selection, ChoiceDialog.java:134-179). Wait for
    # the recreated picker (its Cancel button, res/layout/choose.xml)
    # to be visible, then log the target edge.
    r.wait_for(edge="Eb43116bb", text="Cancel", timeout=30)
    r.comment("rotation recreated picker; onRestoreInstanceState ran "
              "with the saved selection", edge="Eb43116bb")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
