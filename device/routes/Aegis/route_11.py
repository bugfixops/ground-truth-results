# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# New row 11: GroupAdapter.getGroupByUUID. Verdict class: SCRIPTABLE (firm, pending drycheck and real run).
# TO-VERIFY (still open, never claimed): live-dump selector confirmation only; the group is created in-run via the group-manager UI.
# Edge ids are EXACTLY the regenerated verification.csv path row (SHA 83c527cad5a03ec8c5e002e2b5177ceee79572e0ec8885133635139cb4074321).
# Action bodies carried from merger staging-D1 old row 11 with renumbering
# per ROUTES_NOTES.md. No real emulator/adb run, no CI request, no drycheck
# pass and no D9 pass is claimed by this staging file.
"""Aegis route_11: GroupAdapter.getGroupByUUID.

Method: GroupAdapter.getGroupByUUID
Edge ids (in route order):
    Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed
    E0602e719 E4ce5043a E5e63fbe7 E93598a00 E1440feb8 E6830b6dc E32450899
    E553f11f7 E251ac3f4 E7216511b E0ee134dc E3f8e1ae8 E0182bb68 Ed86a6d87
    E0197aeab E743b6812 E5f44da38 Ebdf8bea9 Ea76ae1a0 E887b87bf Ef4e32054
    Ef64f95ee E640fb9eb E94201299 E50e3cfda E382bc001 Eccc3a740 E3452b602
    Eba86fd82 Ef17c8ca0 E37edc2e5 Ee5fe910f Ef4742d96 Eb43a1733 Ed82877e6
    E60b69331 E1fe7fa89 E05744b28 Ea558e9b6 E7d8dd4ed Ee0d2237f E862dcf74
    E02b181bd E77b81f18 E2d25c3ba
Printed route: merger/scratch/routes_postvault.txt (judged dump for this method),
graphs/Aegis/out/methods.csv shortest_path, and
graphs/Aegis/out/aegis_trigger_graph.json (edge trigger texts).
Source ref: GroupAdapter.java:42
Permissions: none (ROUTES.csv permissions cell; run_app.sh grants
only these after pm clear).
Fixtures: none
Setup: first-run vault creation
Judged verdict (final sample, route 11): UNCLEAR, on exactly one
ground: the addGroup loop body in GroupManagerActivity.onCreate runs
only if the vault already has a group (GroupManagerActivity.java:90-95)
and a fresh vault has none (Vault.java:16-17, initNew bare Vault).
That ground is satisfiable by an unlisted in-run action, so it is
SCRIPTED here, not left unscriptable: the SETUP block below creates
a group first, through the entry editor (the Groups page itself has
no add button: activity_groups.xml has only the list, and groups are
created from EditEntryActivity showGroupSelectionDialog,
EditEntryActivity.java:384-420, or not at all). Setup taps are logged
against Eb43a1733, the addGroup edge they produce, and run right
after the list appears, before the settings navigation; the
Eb43a1733 block itself is then comment-only (onCreate's loop runs
addGroup for the setup group when the Groups page opens). Setup
entry fields are typed so the entry saves; the group is created
from the group's bottom sheet (tap the group field, tap the add
row, type the name, OK, Save sheet, Save entry). Rename: the edit
button is tapped with tap_row_action on the setup group's row
(card_group.xml button_edit, content-desc Rename Group), so a
different row's button can never be hit. Rename text is typed
against the graph's type edge and confirmed with OK.

Standard configuration for every route: start from pm clear com.beemdevelopment.aegis.debug,
grant only the permissions in ROUTES.csv, push only the listed fixtures,
and run the listed setup steps first (run_app.sh does the clear, grants
and pushes; this script drives the UI from the launcher).
Run (from the repo root):
    python3 -I device/routes/Aegis/route_11.py --package com.beemdevelopment.aegis.debug
    --log steps/route_11.log --outdir <outdir> [--dry-run] [--adb adb]
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
    "E6830b6dc", "E32450899", "E553f11f7", "E251ac3f4", "E7216511b", "E0ee134dc",
    "E3f8e1ae8", "E0182bb68", "Ed86a6d87", "E0197aeab", "E743b6812", "E5f44da38",
    "Ebdf8bea9", "Ea76ae1a0", "E887b87bf", "Ef4e32054", "Ef64f95ee", "E640fb9eb",
    "E94201299", "E50e3cfda", "E382bc001", "Eccc3a740", "E3452b602", "Eba86fd82",
    "Ef17c8ca0", "E37edc2e5", "Ee5fe910f", "Ef4742d96", "Eb43a1733", "Ed82877e6",
    "E60b69331", "E1fe7fa89", "E05744b28", "Ea558e9b6", "E7d8dd4ed", "Ee0d2237f",
    "E862dcf74", "E02b181bd", "E77b81f18", "E2d25c3ba"
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_11", edge_ids=EDGE_IDS,
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
        # E0ee134dc: IntroActivity.onBeforeSlideChanged@NONE -> IntroBaseActivity.skipToSlide :: security "none" skips the setup slide
        r.comment("security none skips the setup slide", edge="E0ee134dc")
        # E3f8e1ae8: IntroBaseActivity.skipToSlide -> S_INTRO_DONE :: the Done slide is shown after the skip
        r.comment("Done slide is shown after the skip", edge="E3f8e1ae8")
        # E0182bb68: S_INTRO_DONE -> IntroActivity.onDonePressed :: Tap Next on the Done slide: goToNextSlide calls onDonePressed (the tap path is lambda -> goToNextSlide -> onDonePressed)
        r.tap(res_id="btnNext", edge="E0182bb68")
        # Ed86a6d87: IntroActivity.onDonePressed -> VaultManager.initNew :: a new vault is created (no import)
        r.comment("new vault is created (Welcome did not import)", edge="Ed86a6d87")
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
        # SETUP BLOCK logged against Eb43a1733, running before E887b87bf:
        # SETUP STEP (unlisted in-run action satisfying the route's
        # UNCLEAR ground): create a group first, via a new manual entry.
        # Logged against Eb43a1733 because these taps are what make
        # that addGroup edge fire when the Groups page opens below.
        r.tap(res_id="fab", edge="Eb43a1733")
        r.tap(text="Enter manually", edge="Eb43a1733")
        r.tap(res_id="text_name", edge="Eb43a1733")
        r.type_text("Device Test", edge="Eb43a1733")
        r.tap(res_id="text_issuer", edge="Eb43a1733")
        r.type_text("Device Issuer", edge="Eb43a1733")
        r.tap(res_id="text_secret", edge="Eb43a1733")
        r.type_text("JBSWY3DPEHPK3PXP", edge="Eb43a1733")
        r.tap(res_id="text_group", edge="Eb43a1733")
        r.tap(res_id="addGroup", edge="Eb43a1733")
        r.tap(res_id="text_input", edge="Eb43a1733")
        r.type_text("Device Group", edge="Eb43a1733")
        r.tap(text="OK", edge="Eb43a1733")
        r.tap(res_id="btnSave", edge="Eb43a1733")
        r.tap(text="Save", edge="Eb43a1733")
        # E887b87bf: S_LIST -> MainActivity.onOptionsItemSelected :: Tap an item in the list toolbar or overflow menu: the lock icon, Settings, About or a sort option
        r.tap(desc="More options", edge="E887b87bf")
        r.tap(text="Settings", edge="E887b87bf")
        # Ef4e32054: MainActivity.onOptionsItemSelected -> MainActivity.startPreferencesActivity() :: the Settings item opens the settings page
        r.comment("Settings item opens the settings page", edge="Ef4e32054")
        # Ef64f95ee: MainActivity.startPreferencesActivity() -> MainActivity.startPreferencesActivity(Class,String) :: Direct call
        r.comment("direct call into startPreferencesActivity(Class, String)", edge="Ef64f95ee")
        # E640fb9eb: MainActivity.startPreferencesActivity(Class,String) -> PreferencesActivity.<init> :: the settings page opens (fragment and preference extras)
        r.comment("settings page opens with fragment and preference extras", edge="E640fb9eb")
        # E94201299: PreferencesActivity.<init> -> PreferencesActivity.onCreate :: Activity.onCreate of the settings page
        r.comment("Activity.onCreate of the settings page", edge="E94201299")
        # E50e3cfda: PreferencesActivity.onCreate -> MainPreferencesFragment.<init> :: the settings page creates its main fragment on a fresh start
        r.comment("settings page creates its main fragment on a fresh start", edge="E50e3cfda")
        # E382bc001: MainPreferencesFragment.<init> -> MainPreferencesFragment.onCreatePreferences :: the preference list is built after the attach (MainPreferencesFragment)
        r.comment("preference list is built after the attach", edge="E382bc001")
        # Eccc3a740: MainPreferencesFragment.onCreatePreferences -> S_SETTINGS_MAIN :: the settings main list is shown (the preferences.xml rows)
        r.comment("settings main list is shown (preferences.xml rows)", edge="Eccc3a740")
        # E3452b602: S_SETTINGS_MAIN -> PreferencesActivity.onPreferenceStartFragment :: Tap a row of the main settings list that opens a sub-page (android:fragment in preferences.xml)
        r.tap(text="Appearance", edge="E3452b602")
        # Eba86fd82: PreferencesActivity.onPreferenceStartFragment -> AppearancePreferencesFragment.<init> :: the framework creates the sub-page named by the tapped row (AppearancePreferencesFragment)
        r.comment("fragment factory instantiates AppearancePreferencesFragment", edge="Eba86fd82")
        # Ef17c8ca0: AppearancePreferencesFragment.<init> -> AppearancePreferencesFragment.onCreatePreferences :: the preference list is built after the attach (AppearancePreferencesFragment)
        r.comment("preference list is built after the attach (Appearance)", edge="Ef17c8ca0")
        # E37edc2e5: AppearancePreferencesFragment.onCreatePreferences -> AppearancePreferencesFragment.lambda$onCreatePreferences$0 :: Tap Groups in the appearance settings (pref_groups)
        r.tap(text="Edit groups", edge="E37edc2e5")
        # Ee5fe910f: AppearancePreferencesFragment.lambda$onCreatePreferences$0 -> GroupManagerActivity.<init> :: the groups page opens
        r.comment("groups page opens", edge="Ee5fe910f")
        # Ef4742d96: GroupManagerActivity.<init> -> GroupManagerActivity.onCreate :: Activity.onCreate of the groups page
        r.comment("Activity.onCreate of the groups page", edge="Ef4742d96")
        # Eb43a1733: GroupManagerActivity.onCreate -> GroupAdapter.addGroup :: Direct call
        r.comment("onCreate loops over vault groups; setup group above makes addGroup run here", edge="Eb43a1733")
        # Ed82877e6: GroupAdapter.addGroup -> GroupAdapter.onBindViewHolder :: RecyclerView binds the new row to its group after the notify call
        r.comment("RecyclerView binds the new row to its group", edge="Ed82877e6")
        # E60b69331: GroupAdapter.onBindViewHolder -> GroupAdapter.lambda$onBindViewHolder$0 :: Tap the edit button of a group row (the rename dialog opens)
        r.tap_row_action(edge="E60b69331", row_text="Device Group", res_id="button_edit")
        # E1fe7fa89: GroupAdapter.lambda$onBindViewHolder$0 -> GroupManagerActivity.onEditGroup :: Virtual/interface call that can dispatch to this implementation
        r.comment("edit button dispatches to onEditGroup", edge="E1fe7fa89")
        # E05744b28: GroupManagerActivity.onEditGroup -> Dialogs.showTextInputDialog(Context,int,int,TextInputListener,String)@GROUP :: Direct call
        r.comment("onEditGroup opens the rename input dialog", edge="E05744b28")
        # Ea558e9b6: Dialogs.showTextInputDialog(Context,int,int,TextInputListener,String)@GROUP -> Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@GROUP :: Direct call
        r.comment("direct call into the full text-input dialog", edge="Ea558e9b6")
        # E7d8dd4ed: Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@GROUP -> Dialogs.lambda$showTextInputDialog$8@GROUP :: the input dialog is shown: its OnShowListener disables OK and sets the OK click listener
        r.comment("input dialog is shown: its OnShowListener", edge="E7d8dd4ed")
        # Ee0d2237f: Dialogs.lambda$showTextInputDialog$8@GROUP -> Dialogs.lambda$showTextInputDialog$6@GROUP :: Type in the input dialog (OK is enabled when the text is not empty)
        r.tap(res_id="text_input", edge="Ee0d2237f")
        r.type_text("Device Group Renamed", edge="Ee0d2237f")
        # E862dcf74: Dialogs.lambda$showTextInputDialog$6@GROUP -> Dialogs.lambda$showTextInputDialog$7@GROUP :: Tap OK in the input dialog (gives the text to the listener)
        r.tap(text="OK", edge="E862dcf74")
        # E02b181bd: Dialogs.lambda$showTextInputDialog$7@GROUP -> GroupManagerActivity.lambda$onEditGroup$0 :: the typed name is passed to the rename listener: the name is trimmed, the group is cloned and replaced in the list
        r.comment("OK gives the text to the onEditGroup listener", edge="E02b181bd")
        # E77b81f18: GroupManagerActivity.lambda$onEditGroup$0 -> GroupAdapter.replaceGroup :: Direct call
        r.comment("listener calls replaceGroup", edge="E77b81f18")
        # E2d25c3ba: GroupAdapter.replaceGroup -> GroupAdapter.getGroupByUUID :: Direct call
        r.comment("replaceGroup calls getGroupByUUID: TARGET REACHED", edge="E2d25c3ba")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
