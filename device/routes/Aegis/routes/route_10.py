# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# New row 10: EntryAdapter.setTempHighlightEntry. Verdict class: SCRIPTABLE (firm, pending drycheck and real run).
# TO-VERIFY (still open, never claimed): live-dump selector confirmation only; no fixture, picker, camera, or account dependency.
# Edge ids are EXACTLY the regenerated verification.csv path row (SHA 83c527cad5a03ec8c5e002e2b5177ceee79572e0ec8885133635139cb4074321).
# Action bodies carried from merger staging-D1 old row 10 with renumbering
# per ROUTES_NOTES.md. No real emulator/adb run, no CI request, no drycheck
# pass and no D9 pass is claimed by this staging file.
"""Aegis route_10: EntryAdapter.setTempHighlightEntry.

Method: EntryAdapter.setTempHighlightEntry
Edge ids (in route order):
    Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed
    E0602e719 E4ce5043a E5e63fbe7 E93598a00 E1440feb8 E6830b6dc E32450899
    E553f11f7 E251ac3f4 E7216511b E8da5177a E3f8e1ae8 E0182bb68 Ef2e59617
    E0197aeab E743b6812 E5f44da38 Ebdf8bea9 Ea76ae1a0 E2e3490fc Eebad02db
    E554aee35 E75d0fba5 E0979a03c Ec66f5e2c E6597c1f8 Ee228ce53 Ef6ab7dd8
    E69bb265a E1436e4f3 E7c838ae7 E563cb84a Ea80bb15d E16eb2dbc E3d6ab8a1
    E59ee7c4c Eb404a7df
Printed route: merger/scratch/routes_postvault.txt (judged dump for this method),
graphs/Aegis/out/methods.csv shortest_path, and
graphs/Aegis/out/aegis_trigger_graph.json (edge trigger texts).
Source ref: EntryListView.java:496
Permissions: none (ROUTES.csv permissions cell; run_app.sh grants
only these after pm clear).
Fixtures: none
Setup: first-run vault creation
Judged verdict (final sample, route 10): CORRECT. The suffix creates
its own entry in-run (FAB, manual entry, save, result, highlight),
so no pre-existing entry is needed. Field entry before the save tap
is logged against the save edge (E69bb265a): the graph has no edge
for typing into the entry fields, and the save parses what was
typed. Name, issuer and a base32 secret are typed so the new entry
parses and saves instead of erroring on empty fields. Selectors:
entry fields by res_id (text_name, text_issuer, text_secret from
activity_edit_entry.xml); Save is the toolbar item titled Save
(menu_edit.xml, no icon, shown as text).

Standard configuration for every route: start from pm clear com.beemdevelopment.aegis.debug,
grant only the permissions in ROUTES.csv, push only the listed fixtures,
and run the listed setup steps first (run_app.sh does the clear, grants
and pushes; this script drives the UI from the launcher).
Run (from the repo root):
    python3 -I device/routes/Aegis/route_10.py --package com.beemdevelopment.aegis.debug
    --log steps/route_10.log --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import sys

import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "Eb9515d18", "E5b266140", "E1ef992ce", "E88ed9829", "E28ffc58c", "Eb76444fd",
    "E3a06baed", "E0602e719", "E4ce5043a", "E5e63fbe7", "E93598a00", "E1440feb8",
    "E6830b6dc", "E32450899", "E553f11f7", "E251ac3f4", "E7216511b", "E8da5177a",
    "E3f8e1ae8", "E0182bb68", "Ef2e59617", "E0197aeab", "E743b6812", "E5f44da38",
    "Ebdf8bea9", "Ea76ae1a0", "E2e3490fc", "Eebad02db", "E554aee35", "E75d0fba5",
    "E0979a03c", "Ec66f5e2c", "E6597c1f8", "Ee228ce53", "Ef6ab7dd8", "E69bb265a",
    "E1436e4f3", "E7c838ae7", "E563cb84a", "Ea80bb15d", "E16eb2dbc", "E3d6ab8a1",
    "E59ee7c4c", "Eb404a7df"
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_10", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # Eb9515d18: S_ENTRY -> AegisApplication.<init> :: Any outside trigger starts the app process; the application class is created first, except in a backup or restore start, which uses the base Application class
        r.comment("process starts; application class created first", edge="Eb9515d18")
        # E5b266140: AegisApplication.<init> -> Hilt_AegisApplication.onCreate :: Application.onCreate: the Hilt-generated superclass onCreate runs first (Hilt injection), then AegisApplicationBase.onCreate
        r.comment("system instantiates application, then onCreate", edge="E5b266140")
        # E1ef992ce: Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate :: Direct call
        r.comment("Hilt superclass onCreate calls AegisApplicationBase.onCreate", edge="E1ef992ce")
        # E88ed9829: AegisApplicationBase.onCreate -> S_PROCESS :: the application is created: the process can start a component
        r.comment("application created; process can start a component", edge="E88ed9829")
        # E28ffc58c: S_PROCESS -> MainActivity.<init> :: Tap the Aegis icon in the launcher (MAIN / LAUNCHER)
        r.launch("com.beemdevelopment.aegis.debug/com.beemdevelopment.aegis.ui.MainActivity", edge="E28ffc58c")
        # Eb76444fd: MainActivity.<init> -> MainActivity.onCreate :: Activity.onCreate after the constructor
        r.comment("MainActivity onCreate after the constructor", edge="Eb76444fd")
        # E3a06baed: MainActivity.onCreate -> MainActivity.onStart :: Activity.onStart after onCreate
        r.comment("MainActivity onStart after onCreate", edge="E3a06baed")
        # E0602e719: MainActivity.onStart -> MainActivity.startIntroActivity :: no vault file exists (fresh install): the intro starts and onStart returns
        r.comment("fresh install, no vault file: the intro starts", edge="E0602e719")
        # E4ce5043a: MainActivity.startIntroActivity -> IntroActivity.<init> :: startActivityForResult(IntroActivity) through introResultLauncher
        r.comment("startActivityForResult(IntroActivity) via intro launcher", edge="E4ce5043a")
        # E5e63fbe7: IntroActivity.<init> -> IntroActivity.onCreate :: Activity.onCreate of the intro
        r.comment("Activity.onCreate of the intro", edge="E5e63fbe7")
        # E93598a00: IntroActivity.onCreate -> IntroBaseActivity.addSlide@IntroActivity :: Direct call
        r.comment("IntroActivity.onCreate adds the slides", edge="E93598a00")
        # E1440feb8: IntroBaseActivity.addSlide@IntroActivity -> S_INTRO_WELCOME :: the first slide (Welcome) is shown
        r.comment("first slide (Welcome) is shown", edge="E1440feb8")
        # E6830b6dc: S_INTRO_WELCOME -> S_INTRO_PICKER :: Next on Welcome (Welcome did not import): the security picker is shown
        r.tap(res_id="btnNext", edge="E6830b6dc")
        # E32450899: S_INTRO_PICKER -> S_INTRO_PICKER@NONE :: the user taps the None radio button on the security picker
        r.tap(res_id="rb_none", edge="E32450899")
        # E553f11f7: S_INTRO_PICKER@NONE -> IntroBaseActivity.lambda$onCreate$1@NONE :: Tap Next on the security picker with None checked
        r.tap(res_id="btnNext", edge="E553f11f7")
        # E251ac3f4: IntroBaseActivity.lambda$onCreate$1@NONE -> IntroBaseActivity.goToNextSlide@NONE :: the Next button calls goToNextSlide
        r.comment("Next button calls goToNextSlide", edge="E251ac3f4")
        # E7216511b: IntroBaseActivity.goToNextSlide@NONE -> IntroActivity.onBeforeSlideChanged@NONE :: the pager moves on: setPagerPosition calls onBeforeSlideChanged, which IntroActivity overrides
        r.comment("pager moves on; onBeforeSlideChanged runs", edge="E7216511b")
        # E8da5177a: IntroActivity.onBeforeSlideChanged@NONE -> IntroBaseActivity.skipToSlide :: security "none" skips the setup slide
        r.comment("security none skips the setup slide", edge="E8da5177a")
        # E3f8e1ae8: IntroBaseActivity.skipToSlide -> S_INTRO_DONE :: the Done slide is shown after the skip
        r.comment("Done slide is shown after the skip", edge="E3f8e1ae8")
        # E0182bb68: S_INTRO_DONE -> IntroActivity.onDonePressed :: Tap Next on the Done slide: goToNextSlide calls onDonePressed (the tap path is lambda -> goToNextSlide -> onDonePressed)
        r.tap(res_id="btnNext", edge="E0182bb68")
        # Ef2e59617: IntroActivity.onDonePressed -> VaultManager.initNew :: a new vault is created (no import)
        r.comment("new vault is created (Welcome did not import)", edge="Ef2e59617")
        # E0197aeab: VaultManager.initNew -> IntroActivity.onDonePressed@SAVED :: initNew returns: the new vault exists and onDonePressed goes on to set the intro-done flag and return
        r.comment("initNew returns; intro-done flag is set", edge="E0197aeab")
        # E743b6812: IntroActivity.onDonePressed@SAVED -> MainActivity.lambda$new$1 :: setResult(RESULT_OK) and finish() return the result to the caller's launcher
        r.comment("setResult(RESULT_OK) and finish return to MainActivity", edge="E743b6812")
        # E5f44da38: MainActivity.lambda$new$1 -> MainActivity.onIntroResult :: RESULT_OK from the intro: the list is loaded
        r.comment("RESULT_OK from the intro: the list is loaded", edge="E5f44da38")
        # Ebdf8bea9: MainActivity.onIntroResult -> MainActivity.loadEntries :: the entries are loaded after the intro
        r.comment("entries are loaded after the intro", edge="Ebdf8bea9")
        # Ea76ae1a0: MainActivity.loadEntries -> S_LIST :: the list is shown (vault loaded, list loaded in this instance)
        r.comment("list is shown (vault loaded in this instance)", edge="Ea76ae1a0")
        # E2e3490fc: S_LIST -> FabMenuHelper.lambda$setupClickListeners$0 :: Tap the + floating button (opens the menu)
        r.tap(res_id="fab", edge="E2e3490fc")
        # Eebad02db: FabMenuHelper.lambda$setupClickListeners$0 -> FabMenuHelper.toggle :: Direct call
        r.comment("FAB tap calls toggle", edge="Eebad02db")
        # E554aee35: FabMenuHelper.toggle -> FabMenuHelper.open :: the closed floating menu is opened by toggle
        r.comment("closed floating menu is opened by toggle", edge="E554aee35")
        # E75d0fba5: FabMenuHelper.open -> FabMenuHelper.lambda$setupClickListeners$2 :: Tap a menu item (scan, scan image or enter) while the menu is open
        r.tap(text="Enter manually", edge="E75d0fba5")
        # E0979a03c: FabMenuHelper.lambda$setupClickListeners$2 -> MainActivity.startEditEntryActivity() :: the enter item runs its Runnable: startEditEntryActivity
        r.comment("enter item runs startEditEntryActivity", edge="E0979a03c")
        # Ec66f5e2c: MainActivity.startEditEntryActivity() -> MainActivity.startEditEntryActivityForManual :: no usable clipboard URI: the manual entry page opens
        r.comment("no usable clipboard URI: manual entry page opens", edge="Ec66f5e2c")
        # E6597c1f8: MainActivity.startEditEntryActivityForManual -> EditEntryActivity.<init> :: the add-entry page opens for a manual entry (isManual true)
        r.comment("add-entry page opens for a manual entry", edge="E6597c1f8")
        # Ee228ce53: EditEntryActivity.<init> -> EditEntryActivity.onCreate :: Activity.onCreate of the add or edit page
        r.comment("Activity.onCreate of the add page", edge="Ee228ce53")
        # Ef6ab7dd8: EditEntryActivity.onCreate -> EditEntryActivity.onCreateOptionsMenu :: the toolbar menu is created after onCreate
        r.comment("toolbar menu is created after onCreate", edge="Ef6ab7dd8")
        # E69bb265a: EditEntryActivity.onCreateOptionsMenu -> EditEntryActivity.onOptionsItemSelected :: Tap a toolbar item: save, delete, discard, or reset the usage count (a menu tap)
        r.tap(res_id="text_name", edge="E69bb265a")
        r.type_text("Device Test", edge="E69bb265a")
        r.tap(res_id="text_issuer", edge="E69bb265a")
        r.type_text("Device Issuer", edge="E69bb265a")
        r.tap(res_id="text_secret", edge="E69bb265a")
        r.type_text("JBSWY3DPEHPK3PXP", edge="E69bb265a")
        r.tap(text="Save", edge="E69bb265a")
        # E1436e4f3: EditEntryActivity.onOptionsItemSelected -> EditEntryActivity.onSave :: the save toolbar item is tapped (not delete, which is hidden for a new entry, EditEntryActivity.java:658-659)
        r.comment("save toolbar item tapped (delete is hidden for a new entry)", edge="E1436e4f3")
        # E7c838ae7: EditEntryActivity.onSave -> EditEntryActivity.addAndFinish :: the entry parses and, for a new entry, has no duplicate name and issuer, so the save finishes
        r.comment("entry parses, no duplicate name/issuer: save finishes", edge="E7c838ae7")
        # E563cb84a: EditEntryActivity.addAndFinish -> EditEntryActivity.saveAndFinish@ADD :: addAndFinish saves the entry with delete=false (EditEntryActivity.java:680)
        r.comment("addAndFinish saves the entry with delete=false", edge="E563cb84a")
        # Ea80bb15d: EditEntryActivity.saveAndFinish@ADD -> MainActivity.lambda$new$6 :: setResult(RESULT_OK) and finish after a new entry is saved: the add launcher runs
        r.comment("RESULT_OK after a new entry is saved: add launcher runs", edge="Ea80bb15d")
        # E16eb2dbc: MainActivity.lambda$new$6 -> MainActivity.onAddEntryResult :: the add-entry result is handled: the new entry is added to the list
        r.comment("add-entry result handled: new entry added to the list", edge="E16eb2dbc")
        # E3d6ab8a1: MainActivity.onAddEntryResult -> EntryListView.onEntryAdded :: the new entry is shown in the list at once
        r.comment("new entry shown in the list at once", edge="E3d6ab8a1")
        # E59ee7c4c: EntryListView.onEntryAdded -> EntryListView.tempHighlightEntry :: the entry is on screen: the highlight starts at once
        r.comment("entry on screen: highlight starts at once", edge="E59ee7c4c")
        # Eb404a7df: EntryListView.tempHighlightEntry -> EntryAdapter.setTempHighlightEntry :: Direct call
        r.comment("tempHighlightEntry calls setTempHighlightEntry: TARGET REACHED", edge="Eb404a7df")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
