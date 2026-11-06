#!/usr/bin/env python3
# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# New row 19: SlotIntegrityException.<init>(Throwable). Verdict class: SCRIPTABLE (firm, pending drycheck and real run).
# TO-VERIFY (still open, never claimed): live-dump selector confirmation plus the wrong-PIN BadPadding throw trigger on device (source-derived, device-unproven).
# Edge ids are EXACTLY the regenerated verification.csv path row (SHA 83c527cad5a03ec8c5e002e2b5177ceee79572e0ec8885133635139cb4074321).
# Action bodies carried from merger staging-D1 old row 19 with renumbering
# per ROUTES_NOTES.md. No real emulator/adb run, no CI request, no drycheck
# pass and no D9 pass is claimed by this staging file.
"""Aegis route_19: SlotIntegrityException.<init>(Throwable).

Method: SlotIntegrityException.<init>(Throwable)
Edge ids (in route order):
    Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd
    E3a06baed E0602e719 E4ce5043a E5e63fbe7 E93598a00 E1440feb8
    E6830b6dc E32450899 E553f11f7 E251ac3f4 E7216511b E0ee134dc
    E3f8e1ae8 E0182bb68 Ed86a6d87 E0197aeab E743b6812 E5f44da38
    Ebdf8bea9 Ea76ae1a0 E887b87bf Ef4e32054 Ef64f95ee E640fb9eb
    E94201299 E50e3cfda E382bc001 Eccc3a740 E3452b602 Ed19f3b08
    E5c8f972e Ee4227c2d Ec2217fba Edd00aa28 Ec6728d2c Eb31da5f7
    Ecac24ac7 E566488b7 Efca19e89 E77f3fed6 E8ef49332 Ef33bc2ab
    E808d453d E6766e40e
Printed route source: graphs/Aegis/scratch/routes_postvault.txt,
    section "SlotIntegrityException.<init>(Throwable)" (50 steps,
    judged UNCLEAR only because the pin-keyboard preference is
    visible only when the vault is encrypted, while the drawn
    route's in-run vault is the NONE intro vault), plus
    graphs/Aegis/out/methods.csv (same edge list) and
    graphs/Aegis/out/aegis_trigger_graph.json (edges above).
Permissions: none (ROUTES-g3.csv permissions cell empty; the route
    has no ENV permission gate and methods.csv env_kinds is empty).
Fixtures: none.
Setup: first-run vault creation (work-emulator ci/apps.csv Aegis
    row), PLUS the unlisted in-run setup step the judged UNCLEAR
    ground names: enable encryption in settings first, so the
    pin-keyboard row is visible. The enable-encryption actions
    are logged inside the step-37 block (Security preferences
    built), i.e. on the same page as the pin-keyboard row and
    before the step-38 tap that needs the encrypted vault.
    The vault password set here is digits-only ("123456"), and
    the pin dialog is then given a DIFFERENT digits-only value
    ("654321"): the digits check passes, the decrypt runs, and
    the wrong password fails the padding check, so Slot.getKey
    throws SlotIntegrityException (Slot.java:57, BadPadding
    branch) -- that is the target edge, not a successful
    decrypt (a correct password would reach no target at all).
UI selectors (from the app sources, not a live dump): as
    route_22 for the intro and the overflow menu; settings rows
    by title text ("Settings", "Security" from
    pref_section_security_title, "Encryption" from
    pref_encryption_title, "Use PIN keyboard on lockscreen"
    from pref_pin_keyboard_title); set-password dialog fields:
    res_id text_password and text_password_confirm
    (Dialogs.showSetPasswordDialog, dialog_password layout)
    and its positive button text "OK" (android.R.string.ok);
    pin dialog positive button text "OK" (same android string).
    LIVE-DUMP GAPS (confirm on the real run, never silently
    rewritten): the overflow content-desc ("More options" is
    the framework default); the pin dialog's input field is
    typed without a tap because the dialog focuses its input
    on show -- if the live dump shows the input unfocused, tap
    its field first (id to confirm from the dump); whether
    enabling encryption leaves the Security page unlocked (if
    an AuthActivity lock screen appears, unlock with "123456"
    before the step-38 tap).
Run (from the repo root, after the merger places this file at
    device/routes/Aegis/route_19.py):
    python3 -I device/routes/Aegis/route_19.py --package
    com.beemdevelopment.aegis.debug --log steps/route_19.log
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
VAULT_PASSWORD = "123456"
WRONG_PIN = "654321"

EDGE_IDS = [
    "Eb9515d18", "E5b266140", "E1ef992ce", "E88ed9829", "E28ffc58c", "Eb76444fd",
    "E3a06baed", "E0602e719", "E4ce5043a", "E5e63fbe7", "E93598a00", "E1440feb8",
    "E6830b6dc", "E32450899", "E553f11f7", "E251ac3f4", "E7216511b", "E0ee134dc",
    "E3f8e1ae8", "E0182bb68", "Ed86a6d87", "E0197aeab", "E743b6812", "E5f44da38",
    "Ebdf8bea9", "Ea76ae1a0", "E887b87bf", "Ef4e32054", "Ef64f95ee", "E640fb9eb",
    "E94201299", "E50e3cfda", "E382bc001", "Eccc3a740", "E3452b602", "Ed19f3b08",
    "E5c8f972e", "Ee4227c2d", "Ec2217fba", "Edd00aa28", "Ec6728d2c", "Eb31da5f7",
    "Ecac24ac7", "E566488b7", "Efca19e89", "E77f3fed6", "E8ef49332", "Ef33bc2ab",
    "E808d453d", "E6766e40e"
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_19", edge_ids=EDGE_IDS,
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
        # Ea76ae1a0: The list is shown (vault loaded, list loaded
        # in this instance).
        r.comment("list shown", edge="Ea76ae1a0")
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
        # opens a sub-page (Security).
        r.scroll_to(text="Security", edge="E3452b602")
        r.tap(text="Security", edge="E3452b602")
        # Ed19f3b08: The framework creates the sub-page named by
        # the tapped row (SecurityPreferencesFragment).
        r.comment("SecurityPreferencesFragment created",
                  edge="Ed19f3b08")
        # E5c8f972e: The preference list is built after the
        # attach. UNLISTED SETUP (the judged UNCLEAR ground):
        # the NONE vault is unencrypted, so the pin-keyboard row
        # is hidden (preferences_security.xml:86 dependency on
        # pref_encryption). Enable encryption first: tap the
        # Encryption row, set a digits-only password, and wait
        # for key derivation. The pin-keyboard row then appears.
        r.comment("security preference list built; enabling "
                  "encryption first (unlisted setup for step 38)",
                  edge="E5c8f972e")
        r.tap(text="Encryption", edge="E5c8f972e")
        r.tap(res_id="text_password", edge="E5c8f972e")
        r.type_text(VAULT_PASSWORD, edge="E5c8f972e")
        r.tap(res_id="text_password_confirm", edge="E5c8f972e")
        r.type_text(VAULT_PASSWORD, edge="E5c8f972e")
        r.tap(text="OK", edge="E5c8f972e")
        r.dwell(edge="E5c8f972e", seconds=5)
        # Ee4227c2d: Turn Pin keyboard (pref_pin_keyboard) on:
        # asks for the password to confirm the digits-only pin.
        # Visible now because the vault is encrypted.
        r.tap(text="Use PIN keyboard on lockscreen", edge="Ee4227c2d")
        # Ec2217fba: The PIN keyboard password dialog opens.
        r.comment("pin keyboard password dialog opens",
                  edge="Ec2217fba")
        # Edd00aa28: showPasswordInputDialog -> showTextInputDialog.
        r.comment("password dialog delegates to text input dialog",
                  edge="Edd00aa28")
        # Ec6728d2c: The password dialog is shown: its show
        # listener disables OK until the input is not empty.
        r.comment("dialog shown; OK disabled until input non-empty",
                  edge="Ec6728d2c")
        # Eb31da5f7: Type in the input dialog (OK is enabled when
        # the text is not empty). A DIFFERENT digits-only value
        # from the vault password: the digits check passes, the
        # decrypt runs, and the wrong password fails it.
        # (The dialog input is focused on show; see the header
        # gap note if the live dump shows otherwise.)
        r.type_text(WRONG_PIN, edge="Eb31da5f7")
        # Ecac24ac7: Tap OK in the password dialog (the typed
        # text goes to the listener, then the dialog closes).
        r.tap(text="OK", edge="Ecac24ac7")
        # E566488b7: The typed password is passed to the
        # pin-keyboard listener: the digits-only check runs,
        # then the password is decrypted in a background task.
        r.comment("digits check passes; decrypt task starts",
                  edge="E566488b7")
        r.dwell(edge="E566488b7", seconds=5)
        # Efca19e89: AsyncTask runs doInBackground on the worker
        # thread (decrypt the password slot to confirm the PIN).
        r.comment("PasswordSlotDecryptTask doInBackground",
                  edge="Efca19e89")
        # E77f3fed6: PasswordSlotDecryptTask.decrypt (direct call).
        r.comment("decrypt entry point", edge="E77f3fed6")
        # E8ef49332: decrypt -> decryptPasswordSlot(PasswordSlot,
        # char[]) (direct call).
        r.comment("decryptPasswordSlot(slot, chars)", edge="E8ef49332")
        # Ef33bc2ab: decryptPasswordSlot(slot, chars) ->
        # decryptPasswordSlot(slot, SecretKey) (direct call).
        r.comment("decryptPasswordSlot(slot, key)", edge="Ef33bc2ab")
        # E808d453d: decryptPasswordSlot -> Slot.getKey (direct
        # call). The wrong password fails the padding check.
        r.comment("Slot.getKey: wrong password fails padding",
                  edge="E808d453d")
        # E6766e40e: Slot.getKey -> SlotIntegrityException.<init>
        # (Throwable): target reached (BadPadding branch).
        r.comment("BadPadding throws SlotIntegrityException: target "
                  "reached", edge="E6766e40e")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
