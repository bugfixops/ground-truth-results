# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# New row 13: ImportExportPreferencesFragment$ExportResultListener.onTaskFinished. Verdict class: DRAFT / TO-ASSESS.
# TO-VERIFY (still open, never claimed): system document-creator picker navigation and the export destination for the plain export.
# Edge ids are EXACTLY the regenerated verification.csv path row (SHA 83c527cad5a03ec8c5e002e2b5177ceee79572e0ec8885133635139cb4074321).
# Action bodies carried from merger staging-D1 old row 14 with renumbering
# per ROUTES_NOTES.md. No real emulator/adb run, no CI request, no drycheck
# pass and no D9 pass is claimed by this staging file.
"""Aegis route_13: ImportExportPreferencesFragment$ExportResultListener.onTaskFinished.

Method: ImportExportPreferencesFragment$ExportResultListener.onTaskFinished
Edge ids (in route order):
    Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed
    E0602e719 E4ce5043a E5e63fbe7 E93598a00 E1440feb8 E6830b6dc E32450899
    E553f11f7 E251ac3f4 E7216511b E0ee134dc E3f8e1ae8 E0182bb68 Ed86a6d87
    E0197aeab E743b6812 E5f44da38 Ebdf8bea9 Ea76ae1a0 E887b87bf Ef4e32054
    Ef64f95ee E640fb9eb E94201299 E50e3cfda E382bc001 Eccc3a740 E3452b602
    E63d9f2a4 E245f8b40 E629987fd Ed8c9ae46 E76172dad E847a2f41 Eae638791
    Ee3390dde E2733d9a8 Ec87ff415 E20d407ad Ebeaf464d Ec9295cb2 E546cc6f9
Printed route: merger/scratch/routes_postvault.txt (judged dump for this method),
graphs/Aegis/out/methods.csv shortest_path, and
graphs/Aegis/out/aegis_trigger_graph.json (edge trigger texts).
Source ref: ui/tasks/ExportTask.java:43-45
Permissions: none (ROUTES.csv permissions cell; run_app.sh grants
only these after pm clear).
Fixtures: none
Setup: first-run vault creation
Judged verdict (final sample, route 13): CORRECT. Plain-export path
end to end: Export row, export dialog, document creator, plain
result, export task, onTaskFinished. Plain (not encrypted) is the
point: the export dialog defaults to format Aegis (.JSON) with
Encrypt the vault CHECKED, so the script unchecks it and checks I
understand the risk (the accept checkbox only appears once
encryption is off, and OK stays disabled until encrypt or accept is
checked). The OK tap then fires ACTION_CREATE_DOCUMENT; the Save tap
in the system document creator is what returns the URI, so it is
logged against the creator-result edge. The creator UI is system UI
and varies by emulator image: the Save button text is the flagged
live-run gap (a missing Save button fails loudly at that tap, never
silently). No dumped step demands an encrypted vault.

Standard configuration for every route: start from pm clear com.beemdevelopment.aegis.debug,
grant only the permissions in ROUTES.csv, push only the listed fixtures,
and run the listed setup steps first (run_app.sh does the clear, grants
and pushes; this script drives the UI from the launcher).
Run (from the repo root):
    python3 -I device/routes/Aegis/route_13.py --package com.beemdevelopment.aegis.debug
    --log steps/route_13.log --outdir <outdir> [--dry-run] [--adb adb]
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
    "E94201299", "E50e3cfda", "E382bc001", "Eccc3a740", "E3452b602", "E63d9f2a4",
    "E245f8b40", "E629987fd", "Ed8c9ae46", "E76172dad", "E847a2f41", "Eae638791",
    "Ee3390dde", "E2733d9a8", "Ec87ff415", "E20d407ad", "Ebeaf464d", "Ec9295cb2",
    "E546cc6f9"
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_13", edge_ids=EDGE_IDS,
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
        r.tap(text="Import & Export", edge="E3452b602")
        # E63d9f2a4: PreferencesActivity.onPreferenceStartFragment -> ImportExportPreferencesFragment.<init> :: the framework creates the sub-page named by the tapped row (ImportExportPreferencesFragment)
        r.comment("fragment factory instantiates ImportExportPreferencesFragment", edge="E63d9f2a4")
        # E245f8b40: ImportExportPreferencesFragment.<init> -> ImportExportPreferencesFragment.onCreatePreferences :: the preference list is built after the attach (ImportExportPreferencesFragment)
        r.comment("preference list is built after the attach (ImportExport)", edge="E245f8b40")
        # E629987fd: ImportExportPreferencesFragment.onCreatePreferences -> ImportExportPreferencesFragment.lambda$onCreatePreferences$9 :: Tap Export (pref_export)
        r.tap(text="Export", edge="E629987fd")
        # Ed8c9ae46: ImportExportPreferencesFragment.lambda$onCreatePreferences$9 -> ImportExportPreferencesFragment.startExport :: Direct call
        r.comment("Export row calls startExport", edge="Ed8c9ae46")
        # E76172dad: ImportExportPreferencesFragment.startExport -> ImportExportPreferencesFragment.lambda$startExport$20 :: the export dialog is shown: its OnShowListener sets up the checkboxes and the OK and Share buttons
        r.tap(text="Encrypt the vault", edge="E76172dad")
        r.tap(text="I understand the risk", edge="E76172dad")
        # E847a2f41: ImportExportPreferencesFragment.lambda$startExport$20 -> ImportExportPreferencesFragment.lambda$startExport$17 :: Tap OK in the export dialog (the export goes to the document creator, ACTION_CREATE_DOCUMENT)
        r.tap(text="OK", edge="E847a2f41")
        # Eae638791: ImportExportPreferencesFragment.lambda$startExport$17 -> VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@EXPORT :: Tap OK: the export goes to the system document creator through the launcher of the chosen format
        r.comment("OK: export goes to the system document creator (ACTION_CREATE_DOCUMENT)", edge="Eae638791")
        # Ee3390dde: VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@EXPORT -> ImportExportPreferencesFragment.lambda$new$2 :: the export returns to Aegis: the launcher runs onExportResult with the result code and the file URI
        r.tap(text="Save", edge="Ee3390dde")
        # E2733d9a8: ImportExportPreferencesFragment.lambda$new$2 -> ImportExportPreferencesFragment.onExportResult@PLAIN :: Direct call
        r.comment("export file picked: onExportResult starts the plain export", edge="E2733d9a8")
        # Ec87ff415: ImportExportPreferencesFragment.onExportResult@PLAIN -> ImportExportPreferencesFragment.startExportVault@PLAIN_RESULT :: the export file was picked: onExportResult starts the export with the result callback
        r.comment("onExportResult starts the export with the result callback", edge="Ec87ff415")
        # E20d407ad: ImportExportPreferencesFragment.startExportVault@PLAIN_RESULT -> ImportExportPreferencesFragment.lambda$onExportResult$26@PLAIN :: startExportVault runs the result callback for the plain format
        r.comment("startExportVault runs the result callback for the plain format", edge="E20d407ad")
        # Ebeaf464d: ImportExportPreferencesFragment.lambda$onExportResult$26@PLAIN -> ExportTask.doInBackground :: the export runs on a background thread (the export task is started by the export callback)
        r.comment("export runs on a background thread", edge="Ebeaf464d")
        # Ec9295cb2: ExportTask.doInBackground -> ExportTask.onPostExecute :: the result is posted to the main thread
        r.comment("export result posted to the main thread", edge="Ec9295cb2")
        # E546cc6f9: ExportTask.onPostExecute -> ImportExportPreferencesFragment$ExportResultListener.onTaskFinished :: the export task is done: the listener shows the error dialog or the success toast
        r.comment("export task done: listener shows toast or error dialog: TARGET REACHED", edge="E546cc6f9")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
