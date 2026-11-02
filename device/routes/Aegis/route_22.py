#!/usr/bin/env python3
# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# New row 22: EditEntryActivity.deleteAndFinish. Verdict class: SCRIPTABLE (firm, pending drycheck and real run).
# TO-VERIFY (still open, never claimed): live-dump selector confirmation only; the entry is added via FAB first so the long-press has a row.
# Edge ids are EXACTLY the regenerated verification.csv path row (SHA 83c527cad5a03ec8c5e002e2b5177ceee79572e0ec8885133635139cb4074321).
# Action bodies carried from merger staging-D1 old row 22 with renumbering
# per ROUTES_NOTES.md. No real emulator/adb run, no CI request, no drycheck
# pass and no D9 pass is claimed by this staging file.
"""Aegis route_22: EditEntryActivity.deleteAndFinish.

Method: EditEntryActivity.deleteAndFinish
Edge ids (in route order):
    Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd
    E3a06baed E0602e719 E4ce5043a E5e63fbe7 E93598a00 E1440feb8
    E6830b6dc E32450899 E553f11f7 E251ac3f4 E7216511b E8da5177a
    E3f8e1ae8 E0182bb68 Ef2e59617 E0197aeab E743b6812 E5f44da38
    Ebdf8bea9 Ea76ae1a0 E925839a0 E614708b9 Eec2cee41 Eecd32631
    E61a741b2 Ee1fbd7db Edcca50e0 Ed53a4891 Ed78bc83b E117654d4
    Ed46b4aa9 E94c17e0d
Printed route source: graphs/Aegis/scratch/routes_postvault.txt,
    section "EditEntryActivity.deleteAndFinish" (38 steps, judged
    UNCLEAR only because the fresh in-run vault is empty, so no
    row exists to long-press at step 27), plus
    graphs/Aegis/out/methods.csv (same edge list) and
    graphs/Aegis/out/aegis_trigger_graph.json (edges above).
Permissions: none (ROUTES-g3.csv permissions cell empty; the route
    has no ENV permission gate and methods.csv env_kinds is empty).
Fixtures: none.
Setup: first-run vault creation (work-emulator ci/apps.csv Aegis
    row), PLUS the unlisted in-run setup step the judged UNCLEAR
    ground names: create one entry first via the FAB, so the
    step-27 long-press has a row. The entry creation is logged
    inside the step-26 block (list shown), i.e. after the list
    exists and before the long-press that needs it.
UI selectors (from the app sources, not a live dump):
    intro Next: res_id btnNext (icon-only button,
    activity_intro.xml); None radio: res_id rb_none
    (fragment_security_picker_slide.xml); main FAB: res_id fab;
    manual-entry menu item: res_id fab_menu_item_enter
    (fab_menu.xml, text "Enter manually"); new-entry fields:
    res_id text_name, text_issuer, text_secret
    (activity_edit_entry.xml); save: text "Save" (menu_edit.xml
    action_save, no icon, so its title shows); list row: the
    issuer text (EntryHolder binds profile_issuer); action-mode
    Edit item: desc "Edit" (menu_action_mode.xml action_edit,
    icon-only in the action bar, so its content-desc carries the
    title); edit-page overflow: desc "More options", then text
    "Delete" (menu_edit.xml action_delete, showAsAction never);
    delete dialog: text "Yes" (android.R.string.yes in
    Dialogs.showDeleteEntriesDialog).
    LIVE-DUMP GAPS (confirm on the real run, never silently
    rewritten): the overflow content-desc ("More options" is the
    framework default, not read from Aegis sources); the
    action-mode Edit item's desc (if the dump shows no desc,
    tap text "Edit" instead); the long-press landing on the row
    when its centre is the issuer text node.
Run (from the repo root, after the merger places this file at
    device/routes/Aegis/route_22.py):
    python3 -I device/routes/Aegis/route_22.py --package
    com.beemdevelopment.aegis.debug --log steps/route_22.log
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
ISSUER = "ZzTestIssuer"
NAME = "ZzTestAccount"
SECRET = "JBSWY3DPEHPK3PXP"

EDGE_IDS = [
    "Eb9515d18", "E5b266140", "E1ef992ce", "E88ed9829", "E28ffc58c", "Eb76444fd",
    "E3a06baed", "E0602e719", "E4ce5043a", "E5e63fbe7", "E93598a00", "E1440feb8",
    "E6830b6dc", "E32450899", "E553f11f7", "E251ac3f4", "E7216511b", "E8da5177a",
    "E3f8e1ae8", "E0182bb68", "Ef2e59617", "E0197aeab", "E743b6812", "E5f44da38",
    "Ebdf8bea9", "Ea76ae1a0", "E925839a0", "E614708b9", "Eec2cee41", "Eecd32631",
    "E61a741b2", "Ee1fbd7db", "Edcca50e0", "Ed53a4891", "Ed78bc83b", "E117654d4",
    "Ed46b4aa9", "E94c17e0d"
]


def create_entry(r, edge):
    """FAB -> Enter manually -> fill -> Save. One entry in the
    list, so the step-27 long-press has a row. Logged under the
    caller's edge (the list-shown edge): this is the unlisted
    in-run setup step, not a route edge of its own."""
    r.tap(res_id="fab", edge=edge)
    r.tap(res_id="fab_menu_item_enter", edge=edge)
    r.tap(res_id="text_name", edge=edge)
    r.type_text(NAME, edge=edge)
    r.tap(res_id="text_issuer", edge=edge)
    r.type_text(ISSUER, edge=edge)
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
    r = Runner(package=args.package, route="route_22", edge_ids=EDGE_IDS,
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
        # E8da5177a: Security "none" skips the setup slide.
        r.comment("security none skips the setup slide",
                  edge="E8da5177a")
        # E3f8e1ae8: The Done slide is shown after the skip.
        r.comment("Done slide shown after the skip", edge="E3f8e1ae8")
        # E0182bb68: Tap Next (check icon) on the Done slide:
        # goToNextSlide calls onDonePressed.
        r.tap(res_id="btnNext", edge="E0182bb68")
        # Ef2e59617: A new vault is created (no import).
        r.comment("new vault created, no import", edge="Ef2e59617")
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
        # in this instance). UNLISTED SETUP (the judged UNCLEAR
        # ground): the fresh vault is empty, so create one entry
        # via the FAB now, so step 27 has a row to long-press.
        r.comment("list shown; creating one entry first (unlisted "
                  "setup for the step-27 long-press)", edge="Ea76ae1a0")
        create_entry(r, "Ea76ae1a0")
        # E925839a0: Long press an entry in the list (the row
        # long-click listener). The row shows the issuer text.
        r.long_tap(text=ISSUER, edge="E925839a0")
        # E614708b9: EntryAdapter long-click -> EntryListView
        # onLongEntryClick (direct call).
        r.comment("long-click reaches EntryListView", edge="E614708b9")
        # Eec2cee41: EntryListView -> MainActivity.onLongEntryClick.
        r.comment("MainActivity.onLongEntryClick", edge="Eec2cee41")
        # Eecd32631: MainActivity.onLongEntryClick ->
        # MainActivity.startActionMode (direct call).
        r.comment("selection action mode starts", edge="Eecd32631")
        # E61a741b2: Tap an item of the selection action bar.
        # (The Edit tap itself is the next edge; this edge is
        # the action-mode callback entry.)
        r.comment("action-mode callback entered", edge="E61a741b2")
        # Ee1fbd7db: Tap Edit with the selection: the edit page
        # opens for the selected entry.
        r.tap(desc="Edit", edge="Ee1fbd7db")
        # Edcca50e0: The edit page opens for the selected entry
        # (entryUUID).
        r.comment("edit page opens for the selected entry",
                  edge="Edcca50e0")
        # Ed53a4891: Activity.onCreate of the edit page for an
        # existing entry.
        r.comment("EditEntryActivity onCreate (existing entry)",
                  edge="Ed53a4891")
        # Ed78bc83b: The toolbar menu is created after onCreate
        # (existing entry: the delete item stays visible).
        r.comment("edit toolbar menu created; delete stays visible",
                  edge="Ed78bc83b")
        # E117654d4: Tap a toolbar item on an existing-entry page.
        # Delete is showAsAction never, so it is under the
        # overflow menu.
        r.tap(desc="More options", edge="E117654d4")
        r.tap(text="Delete", edge="E117654d4")
        # Ed46b4aa9: Tap Yes in the delete dialog (the entry is
        # deleted).
        r.tap(text="Yes", edge="Ed46b4aa9")
        # E94c17e0d: The delete-dialog listener calls
        # deleteAndFinish: target reached.
        r.comment("delete dialog confirms: deleteAndFinish reached",
                  edge="E94c17e0d")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
