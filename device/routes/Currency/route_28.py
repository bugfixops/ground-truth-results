"""route_28: Main.onEditorAction (value field, Done / Enter).

Method: Main.onEditorAction
Edge ids (in route order):
    E012ed474 Ee88066da Ef071a802 E4dd486ed E9c7fb26f Ec7a6bf31
Printed route file:
    graphs/Currency/scratch/route_print/Main.onEditorAction.txt
Permissions: none (empty on the ROUTES.csv row; INTERNET and
    ACCESS_NETWORK_STATE are install-time only and need no grant).
Fixtures: none (empty on the ROUTES.csv row).
Setup: network (ECB); cert issue on API<=27 images.
    run_app.sh does pm clear, permission grants, fixture pushes, and
    per-app setup before running this script; this script performs only
    the route actions below.

Keyboard note: the value field is an EditText with
imeOptions="actionDone" and inputType="numberDecimal" (res/layout/
main.xml, R.id.edit), and Main registers itself as its
OnEditorActionListener (Main.java:320-324). The soft keyboard's Done
action is what the printed route names; per the route notes, sending
keyevent 66 (ENTER) with the field focused is the accepted scripted
equivalent. The IME itself is not scripted -- only the resulting
input: tap the field, type a value, press Enter.
"""

import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from device.harness import Runner

EDGE_IDS = [
    "E012ed474", "Ee88066da", "Ef071a802", "E4dd486ed", "E9c7fb26f",
    "Ec7a6bf31",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_28", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, outdir=args.outdir,
               adb=args.adb)

    # E012ed474 -- ENTRY: tap the Currency icon in the launcher
    # (MAIN/LAUNCHER intent filter, AndroidManifest lines 19-24).
    # Scripted as a direct launch of the launcher activity.
    r.launch("org.billthefarmer.currency/.Main", edge="E012ed474")

    # Ee88066da -- LIFECYCLE: system instantiates Main, then onCreate.
    # No user action exists for this edge.
    r.comment("system instantiates Main, then onCreate", edge="Ee88066da")

    # Ef071a802 -- LIFECYCLE: onStart -> onResume. No user action.
    r.comment("onStart -> onResume", edge="Ef071a802")

    # E4dd486ed -- ENTERS: Main becomes visible in DISPLAY_MODE.
    # run_app.sh clears app data before this script, so the selection
    # list is empty and Main.java:351-352 selects DISPLAY_MODE. Page
    # entry, no script action.
    r.comment("Main visible in DISPLAY_MODE (fresh data, no selection)",
              edge="E4dd486ed")

    # E9c7fb26f -- ENTERS: tap the value field (number box at the top
    # of the main screen, R.id.edit). The tap takes focus -- the first
    # tap may only take focus -- and the soft keyboard opens (the
    # manifest's stateHidden only hides the keyboard at start).
    r.tap(res_id="edit", edge="E9c7fb26f")

    # Ec7a6bf31 -- GUI: Done on the soft keyboard (IME_ACTION_DONE).
    # The field selects all on focus (selectAllOnFocus), so the typed
    # text replaces the initial value, and onEditorAction parses it.
    # Pressing Enter is the scripted Done-equivalent: the IME itself
    # is not scripted, only the resulting input.
    r.type_text("2", edge="Ec7a6bf31")
    r.key("ENTER", edge="Ec7a6bf31")

    r.done()


if __name__ == "__main__":
    main()
