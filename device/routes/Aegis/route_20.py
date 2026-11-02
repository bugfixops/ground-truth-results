#!/usr/bin/env python3
# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# New row 20: IconPack$Icon.<init>. Verdict class: DRAFT / TO-ASSESS.
# TO-VERIFY (still open, never claimed): generated icon-pack install acceptance, picker navigation, and the kill plus relaunch rescan.
# Edge ids are EXACTLY the regenerated verification.csv path row (SHA 83c527cad5a03ec8c5e002e2b5177ceee79572e0ec8885133635139cb4074321).
# Action bodies carried from merger staging-D1 old row 20 with renumbering
# per ROUTES_NOTES.md. No real emulator/adb run, no CI request, no drycheck
# pass and no D9 pass is claimed by this staging file.
"""Aegis route_20: IconPack$Icon.<init>.

Method: IconPack$Icon.<init>
Edge ids (in route order):
    Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd
    Efe5ce260 E1e4b62ae E7d4e454a E262cce3d Eada96a15 E67272644
    E9f3e06cc E375694d7 E75a5e491 Ebac005d0 Eecb7add2 Eaf319356
    Ecc690490
Printed route source: graphs/Aegis/scratch/routes_postvault.txt,
    section "IconPack$Icon.<init>" (19 steps, judged UNCLEAR on
    two grounds: the Hilt/Dagger injection chain rests on
    generated code, and the icon pack is cross-run state with no
    in-run producer), plus graphs/Aegis/out/methods.csv (same
    edge list) and graphs/Aegis/out/aegis_trigger_graph.json.
Permissions: none (ROUTES-g3.csv permissions cell empty; the route
    has no ENV permission gate and methods.csv env_kinds is empty).
Fixtures: run-time generated aegis_icon_pack.zip only (never
    committed): setup_route_20.py builds it from text (pack.json
    + one SVG icon file) into the run's gen dir, and run_app.sh
    pushes it to /sdcard/aegis_icon_pack.zip before this script
    runs. No file under $WEMU/fixtures is used (none exists for
    Aegis); the script itself pushes nothing.
Setup: first-run vault creation (work-emulator ci/apps.csv Aegis
    row), PLUS the unlisted in-run setup the judged UNCLEAR
    ground names: install an icon pack first, so the startup
    rescan finds one. The script is two-phase, and the phases
    are labelled in the log:
    Phase A (install, logged under the process-start edge
    Eb9515d18 because it precedes the route's own launch and
    has no route edges of its own): NONE intro -> Settings ->
    Icon packs -> FAB import -> system file picker -> pick the
    generated zip. IconPackManager.importPack then writes the
    pack to filesDir/icons/<uuid>/<version>/.
    Phase B (the route): kill the app and relaunch MainActivity.
    The relaunch IS the route's process start (edges 1-7), the
    Hilt injection chain (edges 8-14) runs as part of activity
    creation, IconPackManager.<init> rescans the icons folder
    (edge 15-16), and the installed pack's pack.json parses
    (edges 17-19) to the target. The generated-code edges have
    no UI trigger and are comment only; they fire as a
    consequence of the relaunch.
UI selectors (from the app sources, not a live dump): as
    route_22 for the intro and the overflow menu; "Icon packs"
    from pref_section_icon_packs; the import FAB: res_id fab
    (fragment_icon_packs layout, IconPacksManagerFragment.java
    onViewCreated); the picker file: text "aegis_icon_pack.zip".
    LIVE-DUMP GAPS (confirm on the real run, never silently
    rewritten): the overflow content-desc ("More options" is
    the framework default); the system picker's navigation to
    the pushed zip -- ACTION_GET_CONTENT with type */* opens
    the picker, but the taps that reach /sdcard/aegis_icon_pack
    .zip vary by picker (Downloads view, hamburger, search);
    the script waits for and taps the file name directly, which
    only works if the picker already shows it; if the picker
    lands elsewhere, the import tap must be re-aimed from the
    live dump. Also confirm the import task completed (the
    pack row appears in the Icon packs list) before the kill;
    the dwell covers the task, not a proof.
Run (from the repo root, after the merger places this file at
    device/routes/Aegis/route_20.py and setup_route_20.py
    alongside it):
    python3 -I device/routes/Aegis/route_20.py --package
    com.beemdevelopment.aegis.debug --log steps/route_20.log
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
PACK_ZIP = "aegis_icon_pack.zip"

EDGE_IDS = [
    "Eb9515d18", "E5b266140", "E1ef992ce", "E88ed9829", "E28ffc58c", "Eb76444fd",
    "Efe5ce260", "E1e4b62ae", "E7d4e454a", "E262cce3d", "Eada96a15", "E67272644",
    "E9f3e06cc", "E375694d7", "E75a5e491", "Ebac005d0", "Eecb7add2", "Eaf319356",
    "Ecc690490"
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_20", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # ---- Phase A: install an icon pack (unlisted setup) ----
        # Eb9515d18 (setup use): process start for the install
        # run. The NONE intro below is setup, not route edges.
        r.launch(MAIN, edge="Eb9515d18")
        r.comment("SETUP: NONE intro for the install run",
                  edge="Eb9515d18")
        r.tap(res_id="btnNext", edge="Eb9515d18")
        r.tap(res_id="rb_none", edge="Eb9515d18")
        r.tap(res_id="btnNext", edge="Eb9515d18")
        r.tap(res_id="btnNext", edge="Eb9515d18")
        r.comment("SETUP: vault created; open Settings -> Icon packs",
                  edge="Eb9515d18")
        r.tap(desc="More options", edge="Eb9515d18")
        r.tap(text="Settings", edge="Eb9515d18")
        r.scroll_to(text="Icon packs", edge="Eb9515d18")
        r.tap(text="Icon packs", edge="Eb9515d18")
        r.comment("SETUP: FAB import opens the system picker "
                  "(ACTION_GET_CONTENT */*)", edge="Eb9515d18")
        r.tap(res_id="fab", edge="Eb9515d18")
        r.wait_for(text=PACK_ZIP, edge="Eb9515d18")
        r.tap(text=PACK_ZIP, edge="Eb9515d18")
        r.comment("SETUP: import task extracts the pack to "
                  "filesDir/icons/<uuid>/<version>/", edge="Eb9515d18")
        r.dwell(edge="Eb9515d18", seconds=5)
        # ---- Phase B: the route (relaunch with pack installed) ----
        # Eb9515d18: Any outside trigger starts the app process
        # (here: the relaunch after the kill below).
        r.comment("route process start: relaunch with pack installed",
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
        # E28ffc58c: Tap the Aegis icon in the launcher. Driven
        # as kill + relaunch: the first launch above was the
        # install run, so this process start needs a fresh
        # process with the pack on disk.
        r.kill_app(edge="E28ffc58c")
        r.relaunch(edge="E28ffc58c", component=MAIN)
        # Eb76444fd: Activity.onCreate after the constructor.
        r.comment("MainActivity onCreate after constructor",
                  edge="Eb76444fd")
        # Efe5ce260: MainActivity.onCreate -> AegisActivity.onCreate.
        r.comment("MainActivity.onCreate calls AegisActivity.onCreate",
                  edge="Efe5ce260")
        # E1e4b62ae: The framework calls the OnContextAvailable
        # Listener registered in _initHiltInternal, inside the
        # super.onCreate call (generated Hilt code; comment only).
        r.comment("Hilt OnContextAvailableListener runs inside "
                  "super.onCreate (generated)", edge="E1e4b62ae")
        # E7d4e454a: Hilt listener -> Hilt_AegisActivity.inject.
        r.comment("Hilt inject entry (generated)", edge="E7d4e454a")
        # E262cce3d: inject -> Dagger ActivityCImpl
        # .injectAegisActivity (generated; comment only).
        r.comment("Dagger injectAegisActivity (generated)",
                  edge="E262cce3d")
        # Eada96a15: injectAegisActivity -> injectAegisActivity2
        # (generated; comment only).
        r.comment("Dagger injectAegisActivity2 (generated)",
                  edge="Eada96a15")
        # E67272644: The activity injection fills the @Inject
        # IconPackManager field from its provider (generated;
        # comment only).
        r.comment("Dagger provider fills IconPackManager field "
                  "(generated)", edge="E67272644")
        # E9f3e06cc: The IconPackManager case builds it through
        # the module provide method (generated dispatch; comment
        # only).
        r.comment("provider dispatches to provideIconPackManager",
                  edge="E9f3e06cc")
        # E375694d7: AegisModule.provideIconPackManager ->
        # IconPackManager.<init> (direct call).
        r.comment("provide method constructs IconPackManager",
                  edge="E375694d7")
        # E75a5e491: IconPackManager.<init> -> rescanIconPacks.
        r.comment("IconPackManager constructor rescans packs",
                  edge="E75a5e491")
        # Ebac005d0: Each pack folder with a UUID name and a
        # readable definition file is parsed at startup: the
        # installed pack's pack.json opens.
        r.comment("rescan opens the installed pack's pack.json",
                  edge="Ebac005d0")
        # Eecb7add2: IconPack.fromBytes (direct call).
        r.comment("pack.json bytes parsed", edge="Eecb7add2")
        # Eaf319356: IconPack.fromJson -> IconPack$Icon.fromJson:
        # each icon of the pack is parsed from its JSON entry.
        r.comment("pack JSON parsed; its icon entry parsed",
                  edge="Eaf319356")
        # Ecc690490: IconPack$Icon.fromJson -> IconPack$Icon.<init>:
        # target reached.
        r.comment("Icon.fromJson constructs the Icon: target reached",
                  edge="Ecc690490")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
