# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# New row 06: TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$0. Verdict class: DRAFT / TO-ASSESS.
# TO-VERIFY (still open, never claimed): importer acceptance of the run-time generated TOTP Authenticator backup, system-picker navigation to the pushed file, and the named-importer row tap.
# Edge ids are EXACTLY the regenerated verification.csv path row (SHA 83c527cad5a03ec8c5e002e2b5177ceee79572e0ec8885133635139cb4074321).
# Action bodies carried from merger staging-D1 old row 05 with renumbering
# per ROUTES_NOTES.md. No real emulator/adb run, no CI request, no drycheck
# pass and no D9 pass is claimed by this staging file.
"""Aegis route_06: TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$0.

Method: TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$0
Edge ids (in route order):
    Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd
    E3a06baed E0602e719 E4ce5043a E5e63fbe7 E93598a00 E1440feb8
    E6830b6dc E32450899 E553f11f7 E251ac3f4 E7216511b E8da5177a
    E3f8e1ae8 E0182bb68 Ef2e59617 E0197aeab E743b6812 E5f44da38
    Ebdf8bea9 Ea76ae1a0 E887b87bf Ef4e32054 Ef64f95ee E640fb9eb
    E94201299 E50e3cfda E382bc001 Eccc3a740 E3452b602 E63d9f2a4
    E245f8b40 E91eeed07 Eb87e30cd Eb51c0932 E5eb44505 E3a5ccc62
    E7c4a2b7c Ede870e08 E4d29f6bd E4b289f60 Ec7144448 Ea0b76b96
    Eeb0293da E59b644b8 E030d215b Ee3bc9dfc Ef64041ea E559996bd
    E94c0e46e E709bf655 E9f3a18cb Ef8e931ed Eff775ca3 Ecade69e6
    E10ae2e57 Efdb318dc
Printed route source: graphs/Aegis/merger/scratch/routes_postvault.txt
    (judged dump, final-sample route 6) plus
    graphs/Aegis/out/methods.csv route_edge_ids for this method.
    Aegis has no scratch/route_print/<method>.txt files, so none is
    cited; the judged dump is the printed route source. Verdict in
    the final route table (route_table_postvault.md): CORRECT.
Permissions: none (ROUTES.csv permissions cell empty; methods.csv
    env_kinds is empty for this route and no dump step carries a
    permission gate; the manifest declares only CAMERA,
    USE_BIOMETRIC, VIBRATE, RECEIVE_BOOT_COMPLETED and
    POST_NOTIFICATIONS, none of which this route gates on).
Fixtures: gen:totpauth_backup.txt -> /sdcard/Download/totpauth_backup.txt (ROUTES.csv fixtures cell, drycheck gen form). RUN-TIME GENERATED, never committed: the setup script setup_route_06.py (device lead / merger to land with the final routes) must generate this file and the run pushes it to /sdcard/Download/ before the picker step. No $WEMU/fixtures file is used: work-emulator/fixtures/ holds no Aegis backup for this importer.
Setup: first-run vault creation (ci/apps.csv Aegis row); generate totpauth_backup.txt (setup_route_06.py) and push it to /sdcard/Download/ before the picker step.
Status: scripted.
PICKER CAVEAT (read before judging the real run): the file pick happens in the system picker opened by ACTION_GET_CONTENT */* (ImportExportPreferencesFragment.java:110-112), whose screens Aegis sources do not describe. The script taps the generated file name in the picker (Diary route_06 / hash-checker route_07 pattern). If the picker first shows a folder list or an app chooser, the device lead inserts that navigation before the file tap; the tap itself is the file-pick step the edge describes (RESULT_OK with the URI).
Run (from the repo root, final location device/routes/Aegis/):
    python3 -I device/routes/Aegis/route_06.py --package
    com.beemdevelopment.aegis.debug --log steps/route_06.log
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
    "E6830b6dc", "E32450899", "E553f11f7", "E251ac3f4", "E7216511b", "E8da5177a",
    "E3f8e1ae8", "E0182bb68", "Ef2e59617", "E0197aeab", "E743b6812", "E5f44da38",
    "Ebdf8bea9", "Ea76ae1a0", "E887b87bf", "Ef4e32054", "Ef64f95ee", "E640fb9eb",
    "E94201299", "E50e3cfda", "E382bc001", "Eccc3a740", "E3452b602", "E63d9f2a4",
    "E245f8b40", "E91eeed07", "Eb87e30cd", "Eb51c0932", "E5eb44505", "E3a5ccc62",
    "E7c4a2b7c", "Ede870e08", "E4d29f6bd", "E4b289f60", "Ec7144448", "Ea0b76b96",
    "Eeb0293da", "E59b644b8", "E030d215b", "Ee3bc9dfc", "Ef64041ea", "E559996bd",
    "E94c0e46e", "E709bf655", "E9f3a18cb", "Ef8e931ed", "Eff775ca3", "Ecade69e6",
    "E10ae2e57", "Efdb318dc"
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_06", edge_ids=EDGE_IDS,
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
        # 18. E8da5177a: IntroActivity.onBeforeSlideChanged@NONE -> IntroBaseActivity.skipToSlide: security "none" skips the setup slide
        r.comment("security \"none\" skips the setup slide", edge="E8da5177a")
        # 19. E3f8e1ae8: IntroBaseActivity.skipToSlide -> S_INTRO_DONE: the Done slide is shown after the skip
        r.comment("the Done slide is shown after the skip", edge="E3f8e1ae8")
        # 20. E0182bb68: S_INTRO_DONE -> IntroActivity.onDonePressed: Tap Next on the Done slide: goToNextSlide calls onDonePressed (the tap path is lambda -> goToNextSlide -> onDonePressed)
        r.tap(res_id="btnNext", edge="E0182bb68")  # last slide: btnNext shows the check icon (IntroBaseActivity.java:161)
        # 21. Ef2e59617: IntroActivity.onDonePressed -> VaultManager.initNew: a new vault is created (no import)
        r.comment("a new vault is created (no import)", edge="Ef2e59617")
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
        # 40. Eb51c0932: Dialogs.showImportersDialog@FILE -> Dialogs.lambda$showImportersDialog$26@FILE_TOTP: Tap the `TOTP Authenticator` row in the importer list (its help text is shown)
        r.tap(text="TOTP Authenticator", edge="Eb51c0932")  # Dialogs.java:526-527 list_importers row = DatabaseImporter.Definition name (DatabaseImporter.java)
        # 41. E5eb44505: Dialogs.lambda$showImportersDialog$26@FILE_TOTP -> Dialogs.lambda$showImportersDialog$27@FILE_TOTP: Tap OK after the `TOTP Authenticator` row was tapped (gives the chosen importer to the listener)
        r.tap(text="OK", edge="E5eb44505")  # importer dialog positive button android.R.string.ok (Dialogs.java:536)
        # 42. E3a5ccc62: Dialogs.lambda$showImportersDialog$27@FILE_TOTP -> ImportExportPreferencesFragment.lambda$onCreatePreferences$5@FILE_TOTP: the OK button gives the chosen `TOTP Authenticator` importer to the import listener: the file picker opens
        r.comment("the OK button gives the chosen `TOTP Authenticator` importer to the import listener: the file picker opens", edge="E3a5ccc62")
        # 43. E7c4a2b7c: ImportExportPreferencesFragment.lambda$onCreatePreferences$5@FILE_TOTP -> VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@FILE_TOTP: the file picker opens (ACTION_GET_CONTENT) through the import launcher, after the `TOTP Authenticator` importer is chosen
        r.comment("the file picker opens (ACTION_GET_CONTENT) through the import launcher, after the `TOTP Authenticator` importer is chosen", edge="E7c4a2b7c")
        # 44. Ede870e08: VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@FILE_TOTP -> ImportExportPreferencesFragment.lambda$new$0@FILE_TOTP: the file picker returns a file: the import launcher runs onImportSelectResult
        r.tap(text="totpauth_backup.txt", edge="Ede870e08")  # PICKER PATTERN (Diary route_06 / hash-checker route_07 precedent): the pick happens in the system picker (ACTION_GET_CONTENT */*, ImportExportPreferencesFragment.java:110-112); if the picker first shows a folder list or a chooser, the device lead inserts that navigation before this tap; this tap is the file-pick step (RESULT_OK with the URI)
        # 45. E4d29f6bd: ImportExportPreferencesFragment.lambda$new$0@FILE_TOTP -> ImportExportPreferencesFragment.onImportSelectResult@FILE_TOTP: the picker result carries data: onImportSelectResult runs
        r.comment("the picker result carries data: onImportSelectResult runs", edge="E4d29f6bd")
        # 46. E4b289f60: ImportExportPreferencesFragment.onImportSelectResult@FILE_TOTP -> ImportFileTask.doInBackground@FILE_TOTP: AsyncTask runs doInBackground on the worker thread (read the picked file)
        r.comment("AsyncTask runs doInBackground on the worker thread (read the picked file)", edge="E4b289f60")
        # 47. Ec7144448: ImportFileTask.doInBackground@FILE_TOTP -> ImportFileTask.onPostExecute@FILE_TOTP: the result is posted to the main thread (the `TOTP Authenticator` file-import task)
        r.comment("the result is posted to the main thread (the `TOTP Authenticator` file-import task)", edge="Ec7144448")
        # 48. Ea0b76b96: ImportFileTask.onPostExecute@FILE_TOTP -> ImportExportPreferencesFragment.lambda$onImportSelectResult$11@FILE_TOTP: the file is read: the callback opens the import page, or shows the read error
        r.comment("the file is read: the callback opens the import page, or shows the read error", edge="Ea0b76b96")
        # 49. Eeb0293da: ImportExportPreferencesFragment.lambda$onImportSelectResult$11@FILE_TOTP -> ImportExportPreferencesFragment.startImportEntriesActivity@FILE_TOTP: Direct call
        r.comment("Direct call", edge="Eeb0293da")
        # 50. E59b644b8: ImportExportPreferencesFragment.startImportEntriesActivity@FILE_TOTP -> ImportEntriesActivity.<init>@FILE_TOTP: the import page opens with the chosen `TOTP Authenticator` importer and the file (file import)
        r.comment("the import page opens with the chosen `TOTP Authenticator` importer and the file (file import)", edge="E59b644b8")
        # 51. E030d215b: ImportEntriesActivity.<init>@FILE_TOTP -> ImportEntriesActivity.onCreate@FILE_TOTP: Activity.onCreate of the import page
        r.comment("Activity.onCreate of the import page", edge="E030d215b")
        # 52. Ee3bc9dfc: ImportEntriesActivity.onCreate@FILE_TOTP -> ImportEntriesActivity.startImport@FILE_TOTP: the import page starts the import from its intent extras
        r.comment("the import page starts the import from its intent extras", edge="Ee3bc9dfc")
        # 53. Ef64041ea: ImportEntriesActivity.startImport@FILE_TOTP -> ImportEntriesActivity.startImportFile@FILE_TOTP: Direct call
        r.comment("Direct call", edge="Ef64041ea")
        # 54. E559996bd: ImportEntriesActivity.startImportFile@FILE_TOTP -> ImportEntriesActivity.processImporterState@FILE_TOTP: the file just read is processed on the `TOTP Authenticator` file-import path
        r.comment("the file just read is processed on the `TOTP Authenticator` file-import path", edge="E559996bd")
        # 55. E94c0e46e: ImportEntriesActivity.processImporterState@FILE_TOTP -> TotpAuthenticatorImporter$EncryptedState.decrypt(Context,DecryptListener): the picked file import is an encrypted TOTP Authenticator backup: the importer asks for the password and decrypts it
        r.comment("the picked file import is an encrypted TOTP Authenticator backup: the importer asks for the password and decrypts it", edge="E94c0e46e")
        # 56. E709bf655: TotpAuthenticatorImporter$EncryptedState.decrypt(Context,DecryptListener) -> TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$2: Tap Yes in the TOTP Authenticator question: the password dialog opens
        r.tap(text="Yes", edge="E709bf655")  # TotpAuthenticatorImporter.java question dialog, strings.xml yes
        # 57. E9f3a18cb: TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$2 -> Dialogs.showPasswordInputDialog(Context,TextInputListener,OnCancelListener)@TOTP: Direct call
        r.comment("Direct call", edge="E9f3a18cb")
        # 58. Ef8e931ed: Dialogs.showPasswordInputDialog(Context,TextInputListener,OnCancelListener)@TOTP -> Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@TOTP: Direct call
        r.comment("Direct call", edge="Ef8e931ed")
        # 59. Eff775ca3: Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@TOTP -> Dialogs.lambda$showTextInputDialog$8@TOTP: the input dialog is shown: its OnShowListener disables OK and sets the OK click listener
        r.comment("the input dialog is shown: its OnShowListener disables OK and sets the OK click listener", edge="Eff775ca3")
        # 60. Ecade69e6: Dialogs.lambda$showTextInputDialog$8@TOTP -> Dialogs.lambda$showTextInputDialog$6@TOTP: Type in the input dialog (OK is enabled when the text is not empty)
        r.tap(res_id="text_input", edge="Ecade69e6")  # dialog_text_input layout (Dialogs.java showTextInputDialog)
        r.type_text("aegis-test-password", edge="Ecade69e6")
        # 61. E10ae2e57: Dialogs.lambda$showTextInputDialog$6@TOTP -> Dialogs.lambda$showTextInputDialog$7@TOTP: Tap OK in the password dialog (the typed text goes to the listener, then the dialog closes)
        r.tap(text="OK", edge="E10ae2e57")  # password dialog positive button android.R.string.ok; OK is disabled until the input is non-empty (Dialogs.java:203)
        # 62. Efdb318dc: Dialogs.lambda$showTextInputDialog$7@TOTP -> TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$0: the typed password goes to the importer, which starts the key derivation or the decryption
        r.comment("the typed password goes to the importer, which starts the key derivation or the decryption", edge="Efdb318dc")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
