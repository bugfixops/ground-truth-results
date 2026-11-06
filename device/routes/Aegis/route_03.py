# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# New row 03: StratumImporter$EncryptedState.decrypt(SecretKey). Verdict class: DRAFT / TO-ASSESS.
# TO-VERIFY (still open, never claimed): importer acceptance of the run-time generated Stratum backup, system-picker navigation to the pushed file, and the named-importer row tap.
# Edge ids are EXACTLY the regenerated verification.csv path row (SHA 83c527cad5a03ec8c5e002e2b5177ceee79572e0ec8885133635139cb4074321).
# Action bodies carried from merger staging-D1 old row 03 with renumbering
# per ROUTES_NOTES.md. No real emulator/adb run, no CI request, no drycheck
# pass and no D9 pass is claimed by this staging file.
"""Aegis route_03: StratumImporter$EncryptedState.decrypt(SecretKey).

Method: StratumImporter$EncryptedState.decrypt(SecretKey)
Edge ids (in route order):
    Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd
    E3a06baed E0602e719 E4ce5043a E5e63fbe7 E93598a00 E1440feb8
    E6830b6dc E32450899 E553f11f7 E251ac3f4 E7216511b E0ee134dc
    E3f8e1ae8 E0182bb68 Ed86a6d87 E0197aeab E743b6812 E5f44da38
    Ebdf8bea9 Ea76ae1a0 E887b87bf Ef4e32054 Ef64f95ee E640fb9eb
    E94201299 E50e3cfda E382bc001 Eccc3a740 E3452b602 E63d9f2a4
    E245f8b40 E91eeed07 Eb87e30cd E9edc8c99 E704f59ea E2b769c0f
    E16b26e12 E79701a94 E6715f6d3 Eaf9670a3 Eaf584e08 Edc9e31c0
    Efa07b0fb E4a84d5bd E743f9261 E062270d3 E06aeb459 E7067346f
    E631e6e57 E61c37f46 E88667145 E8aca2696 E9640aa8f E9f1f92f4
    Efedc0a7e Eff73a574 Ee2ded0b9 Ebf7b06fe E18666fda
Printed route source: graphs/Aegis/merger/scratch/routes_postvault.txt
    (judged dump, final-sample route 3) plus
    graphs/Aegis/out/methods.csv route_edge_ids for this method.
    Aegis has no scratch/route_print/<method>.txt files, so none is
    cited; the judged dump is the printed route source. Verdict in
    the final route table (route_table_postvault.md): CORRECT.
Permissions: none (ROUTES.csv permissions cell empty; methods.csv
    env_kinds is empty for this route and no dump step carries a
    permission gate; the manifest declares only CAMERA,
    USE_BIOMETRIC, VIBRATE, RECEIVE_BOOT_COMPLETED and
    POST_NOTIFICATIONS, none of which this route gates on).
Fixtures: gen:stratum_backup.bin -> /sdcard/Download/stratum_backup.bin (ROUTES.csv fixtures cell, drycheck gen form). RUN-TIME GENERATED, never committed: the setup script setup_route_03.py (device lead / merger to land with the final routes) must generate this file and the run pushes it to /sdcard/Download/ before the picker step. No $WEMU/fixtures file is used: work-emulator/fixtures/ holds no Aegis backup for this importer.
Setup: first-run vault creation (ci/apps.csv Aegis row); generate stratum_backup.bin (setup_route_03.py) and push it to /sdcard/Download/ before the picker step.
Status: scripted.
PICKER CAVEAT (read before judging the real run): the file pick happens in the system picker opened by ACTION_GET_CONTENT */* (ImportExportPreferencesFragment.java:110-112), whose screens Aegis sources do not describe. The script taps the generated file name in the picker (Diary route_06 / hash-checker route_07 pattern). If the picker first shows a folder list or an app chooser, the device lead inserts that navigation before the file tap; the tap itself is the file-pick step the edge describes (RESULT_OK with the URI).
Run (from the repo root, final location device/routes/Aegis/):
    python3 -I device/routes/Aegis/route_03.py --package
    com.beemdevelopment.aegis.debug --log steps/route_03.log
    --outdir <outdir> [--dry-run] [--adb adb]
    Standard configuration: pm clear, grant only ROUTES.csv
    permissions (none here), push only listed fixtures, listed
    setup first. No real emulator/adb run was made for this draft;
    dry-run evidence only (see REPORT-g1.md).
"""


import argparse
import os
import sys

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
    "E245f8b40", "E91eeed07", "Eb87e30cd", "E9edc8c99", "E704f59ea", "E2b769c0f",
    "E16b26e12", "E79701a94", "E6715f6d3", "Eaf9670a3", "Eaf584e08", "Edc9e31c0",
    "Efa07b0fb", "E4a84d5bd", "E743f9261", "E062270d3", "E06aeb459", "E7067346f",
    "E631e6e57", "E61c37f46", "E88667145", "E8aca2696", "E9640aa8f", "E9f1f92f4",
    "Efedc0a7e", "Eff73a574", "Ee2ded0b9", "Ebf7b06fe", "E18666fda"
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_03", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # 1. Eb9515d18: S_ENTRY -> AegisApplication.<init>: Any outside trigger starts the app process; the application class is created first, except in a backup or restore start, which uses the base Application class
        r.comment("Any outside trigger starts the app process; the application class is created first, except in a backup or restore start, which uses the base Application class", edge="Eb9515d18")
        # 2. E5b266140: AegisApplication.<init> -> Hilt_AegisApplication.onCreate: Application.onCreate: the Hilt-generated superclass onCreate runs first (Hilt injection), then AegisApplicationBase.onCreate
        r.comment("Application.onCreate: the Hilt-generated superclass onCreate runs first (Hilt injection), then AegisApplicationBase.onCreate", edge="E5b266140")
        # 3. E1ef992ce: Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate: Direct call
        r.comment("Direct call", edge="E1ef992ce")
        # 4. E88ed9829: AegisApplicationBase.onCreate -> S_PROCESS: the application is created: the process can start a component
        r.comment("the application is created: the process can start a component", edge="E88ed9829")
        # 5. E28ffc58c: S_PROCESS -> MainActivity.<init>: Tap the Aegis icon in the launcher (MAIN / LAUNCHER)
        r.launch("com.beemdevelopment.aegis.debug/com.beemdevelopment.aegis.ui.MainActivity", edge="E28ffc58c")
        # 6. Eb76444fd: MainActivity.<init> -> MainActivity.onCreate: Activity.onCreate after the constructor
        r.comment("Activity.onCreate after the constructor", edge="Eb76444fd")
        # 7. E3a06baed: MainActivity.onCreate -> MainActivity.onStart: Activity.onStart after onCreate
        r.comment("Activity.onStart after onCreate", edge="E3a06baed")
        # 8. E0602e719: MainActivity.onStart -> MainActivity.startIntroActivity: no vault file exists (fresh install): the intro starts and onStart returns
        r.comment("no vault file exists (fresh install): the intro starts and onStart returns", edge="E0602e719")
        # 9. E4ce5043a: MainActivity.startIntroActivity -> IntroActivity.<init>: startActivityForResult(IntroActivity) through introResultLauncher
        r.comment("startActivityForResult(IntroActivity) through introResultLauncher", edge="E4ce5043a")
        # 10. E5e63fbe7: IntroActivity.<init> -> IntroActivity.onCreate: Activity.onCreate of the intro
        r.comment("Activity.onCreate of the intro", edge="E5e63fbe7")
        # 11. E93598a00: IntroActivity.onCreate -> IntroBaseActivity.addSlide@IntroActivity: Direct call
        r.comment("Direct call", edge="E93598a00")
        # 12. E1440feb8: IntroBaseActivity.addSlide@IntroActivity -> S_INTRO_WELCOME: the first slide (Welcome) is shown
        r.comment("the first slide (Welcome) is shown", edge="E1440feb8")
        # 13. E6830b6dc: S_INTRO_WELCOME -> S_INTRO_PICKER: Next on Welcome (Welcome did not import): the security picker is shown
        r.tap(res_id="btnNext", edge="E6830b6dc")  # intro Next (icon-only button, activity_intro.xml btnNext)
        # 14. E32450899: S_INTRO_PICKER -> S_INTRO_PICKER@NONE: the user taps the None radio button on the security picker
        r.tap(res_id="rb_none", edge="E32450899")  # "None" (fragment_security_picker_slide.xml rb_none, strings.xml authentication_method_none)
        # 15. E553f11f7: S_INTRO_PICKER@NONE -> IntroBaseActivity.lambda$onCreate$1@NONE: Tap Next on the security picker with None checked
        r.tap(res_id="btnNext", edge="E553f11f7")
        # 16. E251ac3f4: IntroBaseActivity.lambda$onCreate$1@NONE -> IntroBaseActivity.goToNextSlide@NONE: the Next button calls goToNextSlide
        r.comment("the Next button calls goToNextSlide", edge="E251ac3f4")
        # 17. E7216511b: IntroBaseActivity.goToNextSlide@NONE -> IntroActivity.onBeforeSlideChanged@NONE: the pager moves on: setPagerPosition calls onBeforeSlideChanged, which IntroActivity overrides
        r.comment("the pager moves on: setPagerPosition calls onBeforeSlideChanged, which IntroActivity overrides", edge="E7216511b")
        # 18. E0ee134dc: IntroActivity.onBeforeSlideChanged@NONE -> IntroBaseActivity.skipToSlide: security "none" skips the setup slide
        r.comment("security \"none\" skips the setup slide", edge="E0ee134dc")
        # 19. E3f8e1ae8: IntroBaseActivity.skipToSlide -> S_INTRO_DONE: the Done slide is shown after the skip
        r.comment("the Done slide is shown after the skip", edge="E3f8e1ae8")
        # 20. E0182bb68: S_INTRO_DONE -> IntroActivity.onDonePressed: Tap Next on the Done slide: goToNextSlide calls onDonePressed (the tap path is lambda -> goToNextSlide -> onDonePressed)
        r.tap(res_id="btnNext", edge="E0182bb68")  # last slide: btnNext shows the check icon (IntroBaseActivity.java:161)
        # 21. Ed86a6d87: IntroActivity.onDonePressed -> VaultManager.initNew: a new vault is created (no import)
        r.comment("a new vault is created (no import)", edge="Ed86a6d87")
        # 22. E0197aeab: VaultManager.initNew -> IntroActivity.onDonePressed@SAVED: initNew returns: the new vault exists and onDonePressed goes on to set the intro-done flag and return
        r.comment("initNew returns: the new vault exists and onDonePressed goes on to set the intro-done flag and return", edge="E0197aeab")
        # 23. E743b6812: IntroActivity.onDonePressed@SAVED -> MainActivity.lambda$new$1: setResult(RESULT_OK) and finish() return the result to the caller's launcher
        r.comment("setResult(RESULT_OK) and finish() return the result to the caller's launcher", edge="E743b6812")
        # 24. E5f44da38: MainActivity.lambda$new$1 -> MainActivity.onIntroResult: RESULT_OK from the intro: the list is loaded
        r.comment("RESULT_OK from the intro: the list is loaded", edge="E5f44da38")
        # 25. Ebdf8bea9: MainActivity.onIntroResult -> MainActivity.loadEntries: the entries are loaded after the intro
        r.comment("the entries are loaded after the intro", edge="Ebdf8bea9")
        # 26. Ea76ae1a0: MainActivity.loadEntries -> S_LIST: the list is shown (vault loaded, list loaded in this instance)
        r.comment("the list is shown (vault loaded, list loaded in this instance)", edge="Ea76ae1a0")
        # 27. E887b87bf: S_LIST -> MainActivity.onOptionsItemSelected: Tap an item in the list toolbar or overflow menu: the lock icon, Settings, About or a sort option
        r.tap(desc="More options", edge="E887b87bf")  # overflow button (Diary precedent)
        # 28. Ef4e32054: MainActivity.onOptionsItemSelected -> MainActivity.startPreferencesActivity(): the Settings item opens the settings page
        r.tap(text="Settings", edge="Ef4e32054")  # menu_main.xml action_settings, strings.xml action_settings
        # 29. Ef64f95ee: MainActivity.startPreferencesActivity() -> MainActivity.startPreferencesActivity(Class,String): Direct call
        r.comment("Direct call", edge="Ef64f95ee")
        # 30. E640fb9eb: MainActivity.startPreferencesActivity(Class,String) -> PreferencesActivity.<init>: the settings page opens (fragment and preference extras)
        r.comment("the settings page opens (fragment and preference extras)", edge="E640fb9eb")
        # 31. E94201299: PreferencesActivity.<init> -> PreferencesActivity.onCreate: Activity.onCreate of the settings page
        r.comment("Activity.onCreate of the settings page", edge="E94201299")
        # 32. E50e3cfda: PreferencesActivity.onCreate -> MainPreferencesFragment.<init>: the settings page creates its main fragment on a fresh start
        r.comment("the settings page creates its main fragment on a fresh start", edge="E50e3cfda")
        # 33. E382bc001: MainPreferencesFragment.<init> -> MainPreferencesFragment.onCreatePreferences: the preference list is built after the attach (MainPreferencesFragment)
        r.comment("the preference list is built after the attach (MainPreferencesFragment)", edge="E382bc001")
        # 34. Eccc3a740: MainPreferencesFragment.onCreatePreferences -> S_SETTINGS_MAIN: the settings main list is shown (the preferences.xml rows)
        r.comment("the settings main list is shown (the preferences.xml rows)", edge="Eccc3a740")
        # 35. E3452b602: S_SETTINGS_MAIN -> PreferencesActivity.onPreferenceStartFragment: Tap a row of the main settings list that opens a sub-page (android:fragment in preferences.xml)
        r.tap(text="Import & Export", edge="E3452b602")  # preferences.xml row, strings.xml pref_section_import_export_title
        # 36. E63d9f2a4: PreferencesActivity.onPreferenceStartFragment -> ImportExportPreferencesFragment.<init>: the framework creates the sub-page named by the tapped row (ImportExportPreferencesFragment)
        r.comment("the framework creates the sub-page named by the tapped row (ImportExportPreferencesFragment)", edge="E63d9f2a4")
        # 37. E245f8b40: ImportExportPreferencesFragment.<init> -> ImportExportPreferencesFragment.onCreatePreferences: the preference list is built after the attach (ImportExportPreferencesFragment)
        r.comment("the preference list is built after the attach (ImportExportPreferencesFragment)", edge="E245f8b40")
        # 38. E91eeed07: ImportExportPreferencesFragment.onCreatePreferences -> ImportExportPreferencesFragment.lambda$onCreatePreferences$6: Tap Import in the import and export settings (pref_import)
        r.tap(text="Import from file", edge="E91eeed07")  # preferences_import_export.xml pref_import, strings.xml pref_import_file_title
        # 39. Eb87e30cd: ImportExportPreferencesFragment.lambda$onCreatePreferences$6 -> Dialogs.showImportersDialog@FILE: the file import row opens the importer dialog (isDirect false)
        r.comment("the file import row opens the importer dialog (isDirect false)", edge="Eb87e30cd")
        # 40. E9edc8c99: Dialogs.showImportersDialog@FILE -> Dialogs.lambda$showImportersDialog$26@FILE_STRATUM: Tap the `Stratum` row in the importer list (its help text is shown)
        r.tap(text="Stratum (Authenticator Pro)", edge="E9edc8c99")  # Dialogs.java:526-527 list_importers row = DatabaseImporter.Definition name (DatabaseImporter.java)
        # 41. E704f59ea: Dialogs.lambda$showImportersDialog$26@FILE_STRATUM -> Dialogs.lambda$showImportersDialog$27@FILE_STRATUM: Tap OK after the `Stratum` row was tapped (gives the chosen importer to the listener)
        r.tap(text="OK", edge="E704f59ea")  # importer dialog positive button android.R.string.ok (Dialogs.java:536)
        # 42. E2b769c0f: Dialogs.lambda$showImportersDialog$27@FILE_STRATUM -> ImportExportPreferencesFragment.lambda$onCreatePreferences$5@FILE_STRATUM: the OK button gives the chosen `Stratum` importer to the import listener: the file picker opens
        r.comment("the OK button gives the chosen `Stratum` importer to the import listener: the file picker opens", edge="E2b769c0f")
        # 43. E16b26e12: ImportExportPreferencesFragment.lambda$onCreatePreferences$5@FILE_STRATUM -> VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@FILE_STRATUM: the file picker opens (ACTION_GET_CONTENT) through the import launcher, after the `Stratum` importer is chosen
        r.comment("the file picker opens (ACTION_GET_CONTENT) through the import launcher, after the `Stratum` importer is chosen", edge="E16b26e12")
        # 44. E79701a94: VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@FILE_STRATUM -> ImportExportPreferencesFragment.lambda$new$0@FILE_STRATUM: the file picker returns a file: the import launcher runs onImportSelectResult
        r.tap(text="stratum_backup.bin", edge="E79701a94")  # PICKER PATTERN (Diary route_06 / hash-checker route_07 precedent): the pick happens in the system picker (ACTION_GET_CONTENT */*, ImportExportPreferencesFragment.java:110-112); if the picker first shows a folder list or a chooser, the device lead inserts that navigation before this tap; this tap is the file-pick step (RESULT_OK with the URI)
        # 45. E6715f6d3: ImportExportPreferencesFragment.lambda$new$0@FILE_STRATUM -> ImportExportPreferencesFragment.onImportSelectResult@FILE_STRATUM: the picker result carries data: onImportSelectResult runs
        r.comment("the picker result carries data: onImportSelectResult runs", edge="E6715f6d3")
        # 46. Eaf9670a3: ImportExportPreferencesFragment.onImportSelectResult@FILE_STRATUM -> ImportFileTask.doInBackground@FILE_STRATUM: AsyncTask runs doInBackground on the worker thread (read the picked file)
        r.comment("AsyncTask runs doInBackground on the worker thread (read the picked file)", edge="Eaf9670a3")
        # 47. Eaf584e08: ImportFileTask.doInBackground@FILE_STRATUM -> ImportFileTask.onPostExecute@FILE_STRATUM: the result is posted to the main thread (the `Stratum` file-import task)
        r.comment("the result is posted to the main thread (the `Stratum` file-import task)", edge="Eaf584e08")
        # 48. Edc9e31c0: ImportFileTask.onPostExecute@FILE_STRATUM -> ImportExportPreferencesFragment.lambda$onImportSelectResult$11@FILE_STRATUM: the file is read: the callback opens the import page, or shows the read error
        r.comment("the file is read: the callback opens the import page, or shows the read error", edge="Edc9e31c0")
        # 49. Efa07b0fb: ImportExportPreferencesFragment.lambda$onImportSelectResult$11@FILE_STRATUM -> ImportExportPreferencesFragment.startImportEntriesActivity@FILE_STRATUM: Direct call
        r.comment("Direct call", edge="Efa07b0fb")
        # 50. E4a84d5bd: ImportExportPreferencesFragment.startImportEntriesActivity@FILE_STRATUM -> ImportEntriesActivity.<init>@FILE_STRATUM: the import page opens with the chosen `Stratum` importer and the file (file import)
        r.comment("the import page opens with the chosen `Stratum` importer and the file (file import)", edge="E4a84d5bd")
        # 51. E743f9261: ImportEntriesActivity.<init>@FILE_STRATUM -> ImportEntriesActivity.onCreate@FILE_STRATUM: Activity.onCreate of the import page
        r.comment("Activity.onCreate of the import page", edge="E743f9261")
        # 52. E062270d3: ImportEntriesActivity.onCreate@FILE_STRATUM -> ImportEntriesActivity.startImport@FILE_STRATUM: the import page starts the import from its intent extras
        r.comment("the import page starts the import from its intent extras", edge="E062270d3")
        # 53. E06aeb459: ImportEntriesActivity.startImport@FILE_STRATUM -> ImportEntriesActivity.startImportFile@FILE_STRATUM: Direct call
        r.comment("Direct call", edge="E06aeb459")
        # 54. E7067346f: ImportEntriesActivity.startImportFile@FILE_STRATUM -> ImportEntriesActivity.processImporterState@FILE_STRATUM: the file just read is processed on the `Stratum` file-import path
        r.comment("the file just read is processed on the `Stratum` file-import path", edge="E7067346f")
        # 55. E631e6e57: ImportEntriesActivity.processImporterState@FILE_STRATUM -> StratumImporter$EncryptedState.decrypt(Context,DecryptListener): the picked file import is an encrypted Stratum backup: the importer asks for the password and decrypts it
        r.comment("the picked file import is an encrypted Stratum backup: the importer asks for the password and decrypts it", edge="E631e6e57")
        # 56. E61c37f46: StratumImporter$EncryptedState.decrypt(Context,DecryptListener) -> Dialogs.showPasswordInputDialog(Context,int,int,TextInputListener,OnCancelListener)@STRATUM: Direct call
        r.comment("Direct call", edge="E61c37f46")
        # 57. E88667145: Dialogs.showPasswordInputDialog(Context,int,int,TextInputListener,OnCancelListener)@STRATUM -> Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@STRATUM: Direct call
        r.comment("Direct call", edge="E88667145")
        # 58. E8aca2696: Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@STRATUM -> Dialogs.lambda$showTextInputDialog$8@STRATUM: the input dialog is shown: its OnShowListener disables OK and sets the OK click listener
        r.comment("the input dialog is shown: its OnShowListener disables OK and sets the OK click listener", edge="E8aca2696")
        # 59. E9640aa8f: Dialogs.lambda$showTextInputDialog$8@STRATUM -> Dialogs.lambda$showTextInputDialog$6@STRATUM: Type in the input dialog (OK is enabled when the text is not empty)
        r.tap(res_id="text_input", edge="E9640aa8f")  # dialog_text_input layout (Dialogs.java showTextInputDialog)
        r.type_text("aegis-test-password", edge="E9640aa8f")
        # 60. E9f1f92f4: Dialogs.lambda$showTextInputDialog$6@STRATUM -> Dialogs.lambda$showTextInputDialog$7@STRATUM: Tap OK in the password dialog (the typed text goes to the listener, then the dialog closes)
        r.tap(text="OK", edge="E9f1f92f4")  # password dialog positive button android.R.string.ok; OK is disabled until the input is non-empty (Dialogs.java:203)
        # 61. Efedc0a7e: Dialogs.lambda$showTextInputDialog$7@STRATUM -> StratumImporter$EncryptedState.lambda$decrypt$1: the typed password goes to the importer, which starts the key derivation or the decryption
        r.comment("the typed password goes to the importer, which starts the key derivation or the decryption", edge="Efedc0a7e")
        # 62. Eff73a574: StratumImporter$EncryptedState.lambda$decrypt$1 -> Argon2Task.doInBackground: AsyncTask runs doInBackground on the worker thread (Argon2 key derivation)
        r.comment("AsyncTask runs doInBackground on the worker thread (Argon2 key derivation)", edge="Eff73a574")
        # 63. Ee2ded0b9: Argon2Task.doInBackground -> Argon2Task.onPostExecute: the derived key is posted to the main thread
        r.comment("the derived key is posted to the main thread", edge="Ee2ded0b9")
        # 64. Ebf7b06fe: Argon2Task.onPostExecute -> StratumImporter$EncryptedState.lambda$decrypt$0: the Argon2 key goes back to the Stratum importer, which decrypts
        r.comment("the Argon2 key goes back to the Stratum importer, which decrypts", edge="Ebf7b06fe")
        # 65. E18666fda: StratumImporter$EncryptedState.lambda$decrypt$0 -> StratumImporter$EncryptedState.decrypt(SecretKey): Direct call
        r.comment("Direct call", edge="E18666fda")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
