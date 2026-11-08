#!/usr/bin/env python3
# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# New row 23: GoogleAuthProtos$MigrationPayload$DigitCount$DigitCountVerifier.<init>. Verdict class: SCRIPTABLE (firm, pending drycheck and real run).
# TO-VERIFY (still open, never claimed): live-dump selector confirmation plus manual-entry defaults (SHA-1, 6 digits) for the 11 qualifying entries and the 2-batch rule.
# Edge ids are EXACTLY the regenerated verification.csv path row (SHA 83c527cad5a03ec8c5e002e2b5177ceee79572e0ec8885133635139cb4074321).
# Action bodies carried from merger staging-D1 old row 23 with renumbering
# per ROUTES_NOTES.md. No real emulator/adb run, no CI request, no drycheck
# pass and no D9 pass is claimed by this staging file.
"""Aegis route_23: GoogleAuthProtos$MigrationPayload$DigitCount$DigitCountVerifier.<init>.

Method: GoogleAuthProtos$MigrationPayload$DigitCount$DigitCountVerifier.<init>
Edge ids (in route order):
    Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd
    E3a06baed E0602e719 E4ce5043a E5e63fbe7 E93598a00 E1440feb8
    E6830b6dc E32450899 E553f11f7 E251ac3f4 E7216511b E0ee134dc
    E3f8e1ae8 E0182bb68 Ed86a6d87 E0197aeab E743b6812 E5f44da38
    Ebdf8bea9 Ea76ae1a0 E887b87bf Ef4e32054 Ef64f95ee E640fb9eb
    E94201299 E50e3cfda E382bc001 Eccc3a740 E3452b602 E63d9f2a4
    E245f8b40 E8e4d066b E1f7435e7 Eff96a909 E72e1a8df Ec5f95bb3
    E6817ac19 Ee0ce6c02 Ea8a623d5 E75a4904b E00b93575 E6c7b88cc
    Ec45d78f1
Printed route source: graphs/Aegis/scratch/routes_postvault.txt,
    section "GoogleAuthProtos$MigrationPayload$DigitCount$DigitCountVerifier.<init>"
    (49 steps, judged UNCLEAR on two grounds: the in-run vault
    holds 0 entries, and the tail rests on the generated
    protobuf class), plus graphs/Aegis/out/methods.csv (same
    edge list) and graphs/Aegis/out/aegis_trigger_graph.json.
Permissions: none (ROUTES-g3.csv permissions cell empty; the route
    has no ENV permission gate and methods.csv env_kinds is empty).
Fixtures: none.
Setup: first-run vault creation (work-emulator ci/apps.csv Aegis
    row), PLUS the unlisted in-run setup step the judged UNCLEAR
    ground names: create qualifying entries first via the FAB.
    The count ground is satisfiable in-run, and this script
    satisfies it: the Next button on the transfer page is shown
    only when the batch list has more than one entry, and
    batches hold 10 entries (TransferEntriesActivity / the
    export code in ImportExportPreferencesFragment.java:375-384),
    so 2 batches need 11 qualifying entries. The script creates
    11 TOTP entries with the defaults the export filter needs
    (TOTP type, SHA-1, 6 digits: ImportExportPreferencesFragment
    .java:352-363) and then needs only ONE Next tap: from batch
    0, Next generates batch 1 (count 1 < list size 2), which
    runs the protobuf tail. The generated-protobuf tail itself
    (steps 45-49) has no UI trigger: those edges are comment
    only, and the target fires when the runtime serializes the
    batch (GoogleAuthInfo.java:459 toByteArray).
UI selectors (from the app sources, not a live dump): as
    route_22 for the intro, FAB, manual-entry fields and Save;
    settings rows by title text ("Settings" from
    action_settings, "Import & Export" from
    pref_section_import_export_title, "Export for Google
    Authenticator" from pref_google_auth_export_title);
    transfer Next button: res_id btnNext
    (TransferEntriesActivity.java:69, text "Next" on batch 0).
    LIVE-DUMP GAPS (confirm on the real run, never silently
    rewritten): the overflow content-desc ("More options" is
    the framework default); each of the 11 saves returning to
    the list (if a save leaves the edit page open, the loop's
    next FAB tap lands on the wrong screen); the batch count
    on the transfer page being 2 (if the export filter drops
    an entry, Next shows "Done" instead and the tail never
    runs -- the live log must show the Next tap, not Done).
Run (from the repo root, after the merger places this file at
    device/routes/Aegis/route_23.py):
    python3 -I device/routes/Aegis/route_23.py --package
    com.beemdevelopment.aegis.debug --log steps/route_23.log
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
SECRET = "JBSWY3DPEHPK3PXP"
ENTRY_COUNT = 11

EDGE_IDS = [
    "Eb9515d18", "E5b266140", "E1ef992ce", "E88ed9829", "E28ffc58c", "Eb76444fd",
    "E3a06baed", "E0602e719", "E4ce5043a", "E5e63fbe7", "E93598a00", "E1440feb8",
    "E6830b6dc", "E32450899", "E553f11f7", "E251ac3f4", "E7216511b", "E0ee134dc",
    "E3f8e1ae8", "E0182bb68", "Ed86a6d87", "E0197aeab", "E743b6812", "E5f44da38",
    "Ebdf8bea9", "Ea76ae1a0", "E887b87bf", "Ef4e32054", "Ef64f95ee", "E640fb9eb",
    "E94201299", "E50e3cfda", "E382bc001", "Eccc3a740", "E3452b602", "E63d9f2a4",
    "E245f8b40", "E8e4d066b", "E1f7435e7", "Eff96a909", "E72e1a8df", "Ec5f95bb3",
    "E6817ac19", "Ee0ce6c02", "Ea8a623d5", "E75a4904b", "E00b93575", "E6c7b88cc",
    "Ec45d78f1"
]


def create_entry(r, edge, index):
    """FAB -> Enter manually -> fill -> Save, for one
    qualifying TOTP entry (defaults: TOTP, SHA-1, 6 digits).
    Logged under the caller's edge: unlisted in-run setup."""
    issuer = "ExportTest%02d" % index
    name = "Account%02d" % index
    r.tap(res_id="fab", edge=edge)
    r.tap(res_id="fab_menu_item_enter", edge=edge)
    r.tap(res_id="text_name", edge=edge)
    r.type_text(name, edge=edge)
    r.tap(res_id="text_issuer", edge=edge)
    r.type_text(issuer, edge=edge)
    r.tap(res_id="text_secret", edge=edge)
    r.type_text(SECRET, edge=edge)
    r.tap(text="Save", edge=edge)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_23", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # Eb9515d18: Any outside trigger starts the app process.
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
        # E28ffc58c: Tap the Aegis icon in the launcher.
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
        # E32450899: The user taps the None radio button on the
        # security picker.
        r.tap(res_id="rb_none", edge="E32450899")
        # E553f11f7: Tap Next on the security picker with None
        # checked.
        r.tap(res_id="btnNext", edge="E553f11f7")
        # E251ac3f4: The Next button calls goToNextSlide.
        r.comment("Next button calls goToNextSlide", edge="E251ac3f4")
        # E7216511b: The pager moves on: setPagerPosition calls
        # onBeforeSlideChanged.
        r.comment("pager moves on via onBeforeSlideChanged",
                  edge="E7216511b")
        # E0ee134dc: Security "none" skips the setup slide.
        r.comment("security none skips the setup slide",
                  edge="E0ee134dc")
        # E3f8e1ae8: The Done slide is shown after the skip.
        r.comment("Done slide shown after the skip", edge="E3f8e1ae8")
        # E0182bb68: Tap Next (check icon) on the Done slide:
        # goToNextSlide calls onDonePressed.
        r.tap(res_id="btnNext", edge="E0182bb68")
        # Ed86a6d87: A new vault is created (no import).
        r.comment("new vault created, no import", edge="Ed86a6d87")
        # E0197aeab: initNew returns: the new vault exists and
        # onDonePressed sets the intro-done flag and returns.
        r.comment("initNew returns; intro-done flag set",
                  edge="E0197aeab")
        # E743b6812: setResult(RESULT_OK) and finish() return the
        # result to the caller's launcher.
        r.comment("intro returns RESULT_OK", edge="E743b6812")
        # E5f44da38: RESULT_OK from the intro: the list is loaded.
        r.comment("intro RESULT_OK: list loads", edge="E5f44da38")
        # Ebdf8bea9: The entries are loaded after the intro.
        r.comment("entries loaded after the intro", edge="Ebdf8bea9")
        # Ea76ae1a0: The list is shown. UNLISTED SETUP (the
        # judged count ground): create 11 qualifying entries,
        # so the export has 2 batches of 10 and the transfer
        # page shows Next (not Done) on batch 0.
        r.comment("list shown; creating 11 qualifying entries "
                  "(unlisted setup for the 2-batch ground)",
                  edge="Ea76ae1a0")
        for i in range(1, ENTRY_COUNT + 1):
            create_entry(r, "Ea76ae1a0", i)
        # E887b87bf: Tap an item in the list toolbar or overflow
        # menu: the Settings item.
        r.tap(desc="More options", edge="E887b87bf")
        # Ef4e32054: The Settings item opens the settings page.
        r.tap(text="Settings", edge="Ef4e32054")
        # Ef64f95ee: startPreferencesActivity() -> the
        # (Class, String) overload (direct call).
        r.comment("settings page overload entered", edge="Ef64f95ee")
        # E640fb9eb: The settings page opens.
        r.comment("PreferencesActivity opens", edge="E640fb9eb")
        # E94201299: Activity.onCreate of the settings page.
        r.comment("PreferencesActivity onCreate", edge="E94201299")
        # E50e3cfda: The settings page creates its main fragment
        # on a fresh start.
        r.comment("main preferences fragment created", edge="E50e3cfda")
        # E382bc001: The preference list is built after the attach.
        r.comment("main preference list built", edge="E382bc001")
        # Eccc3a740: The settings main list is shown.
        r.comment("settings main list shown", edge="Eccc3a740")
        # E3452b602: Tap a row of the main settings list that
        # opens a sub-page (Import & Export).
        r.scroll_to(text="Import & Export", edge="E3452b602")
        r.tap(text="Import & Export", edge="E3452b602")
        # E63d9f2a4: The framework creates the sub-page named by
        # the tapped row (ImportExportPreferencesFragment).
        r.comment("ImportExportPreferencesFragment created",
                  edge="E63d9f2a4")
        # E245f8b40: The preference list is built after the attach.
        r.comment("import/export preference list built",
                  edge="E245f8b40")
        # E8e4d066b: Tap Google Authenticator style export
        # (pref_google_auth_style_export).
        r.tap(text="Export for Google Authenticator", edge="E8e4d066b")
        # E1f7435e7: Tap handler -> startGoogleAuthenticatorStyle
        # Export (direct call).
        r.comment("Google Authenticator style export starts",
                  edge="E1f7435e7")
        # Eff96a909: The export page opens with the QR batches:
        # at least one qualifying entry, so the export list is
        # not empty (here: 11 entries, 2 batches).
        r.comment("transfer page opens with 2 QR batches",
                  edge="Eff96a909")
        # E72e1a8df: Activity.onCreate of the transfer page.
        r.comment("TransferEntriesActivity onCreate", edge="E72e1a8df")
        # Ec5f95bb3: Tap Next (shown only when the list has more
        # than one entry; the Done label on the last entry
        # closes the page). Batch 0 of 2, so Next is shown.
        r.tap(res_id="btnNext", edge="Ec5f95bb3")
        # E6817ac19: Tap Next while entries remain: the next QR
        # code is generated (count 1 < list size 2).
        r.comment("Next while batches remain: next QR generated",
                  edge="E6817ac19")
        r.dwell(edge="E6817ac19", seconds=5)
        # Ee0ce6c02: generateQR -> GoogleAuthInfo$Export.getUri.
        r.comment("Export.getUri builds the payload", edge="Ee0ce6c02")
        # Ea8a623d5: The built payload is finished and serialized
        # (toByteArray, GoogleAuthInfo.java:459). Generated
        # protobuf code: no UI trigger; comment only.
        r.comment("payload serialized via generated protobuf code",
                  edge="Ea8a623d5")
        # E75a4904b: The runtime reads/writes each OtpParameters
        # message of the payload (generated code; comment only).
        r.comment("protobuf runtime walks OtpParameters",
                  edge="E75a4904b")
        # E00b93575: The runtime gets the DigitCount verifier of
        # an OtpParameters field (generated code; comment only).
        r.comment("protobuf runtime gets DigitCount verifier",
                  edge="E00b93575")
        # E6c7b88cc: The DigitCountVerifier singleton is created
        # on first use (generated code; comment only).
        r.comment("DigitCountVerifier singleton created on first use",
                  edge="E6c7b88cc")
        # Ec45d78f1: The singleton constructor runs during class
        # initialization: target reached.
        r.comment("DigitCountVerifier constructor: target reached",
                  edge="Ec45d78f1")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
