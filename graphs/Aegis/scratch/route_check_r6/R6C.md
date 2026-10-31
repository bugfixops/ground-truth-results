# Round 6 route check C (Aegis 3.4.2, schema-2 trigger graph)

Basis: standard configuration (debug build, fresh install, API 27 emulator, no vault at start, default settings, CAMERA granted only for G3_3). A vault file or biometric slot that exists only because an earlier process ran the intro is cross-run state, so steps that need it are UNCLEAR. The intro of this run leaves the vault loaded in-process (IntroActivity.java:99-100; MainActivity.java:752-754). The onStart vault-file branches (MainActivity.java:951-977) run only in a later process, so they are not treated as same-run producers. Framework lines were read with sed -n from work/fw_src/android-8.1.0_r1/core/java/...; the Hilt superclass and lambda names were checked against the build classes under app/build/intermediates.

## ImportExportPreferencesFragment.lambda$onImportSelectResult$11 (steps: 30)

| step | edge | result | reason |
|---|---|---|---|
| 1 | Eb9515d18 S_ENTRY -> AegisApplication.<init> | OK | ActivityThread.java:5713-5715 full application class unless restricted backup |
| 2 | E5b266140 AegisApplication.<init> -> Hilt_AegisApplication.onCreate | OK | ActivityThread.java:5740 calls Application.onCreate; AegisApplication.java has no onCreate |
| 3 | E1ef992ce Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate | OK | Hilt build class calls the base onCreate (generated code, line 43) |
| 4 | E88ed9829 AegisApplicationBase.onCreate -> S_PROCESS | OK | AegisApplicationBase.java:45-47 (super.onCreate at 46) |
| 5 | E28ffc58c S_PROCESS -> MainActivity.<init> | OK | AndroidManifest.xml:44-51 MAIN/LAUNCHER entry |
| 6 | Eb76444fd MainActivity.<init> -> MainActivity.onCreate | OK | ActivityThread.java:2729-2731; MainActivity.java:193-194 |
| 7 | E3a06baed MainActivity.onCreate -> MainActivity.onStart | OK | ActivityThread.java:2739-2741 performStart when not finished; onCreate has no finish (MainActivity.java:193-264); MainActivity.java:938-940 |
| 8 | E20e76e09 MainActivity.onStart -> MainActivity.loadEntries | UNCLEAR | needs a plain-text vault file from an earlier run (cross-run); fresh install returns at MainActivity.java:942-947 into the intro |
| 9 | Ea76ae1a0 MainActivity.loadEntries -> S_LIST | UNCLEAR | needs the vault loaded by step 8 (MainActivity.java:1134-1138; VaultManager.java:231-233) |
| 10 | E887b87bf S_LIST -> MainActivity.onOptionsItemSelected | OK | overflow item action_settings (menu_main.xml:50 showAsAction never); MainActivity.java:1086-1089; edge guard holds from S_LIST |
| 11 | Ef4e32054 onOptionsItemSelected -> startPreferencesActivity() | OK | MainActivity.java:1088-1089 |
| 12 | Ef64f95ee startPreferencesActivity() -> startPreferencesActivity(Class,String) | OK | MainActivity.java:827 |
| 13 | E640fb9eb startPreferencesActivity(Class,String) -> PreferencesActivity.<init> | OK | MainActivity.java:830-834 preferenceResultLauncher.launch (declared at 166); PreferencesActivity is in the manifest (AndroidManifest.xml:82) |
| 14 | E94201299 PreferencesActivity.<init> -> PreferencesActivity.onCreate | OK | ActivityThread.java:2729-2741; PreferencesActivity.java:24 |
| 15 | E50e3cfda PreferencesActivity.onCreate -> MainPreferencesFragment.<init> | OK | abortIfOrphan false on fresh start (AegisActivity.java:155); PreferencesActivity.java:40-46 |
| 16 | E382bc001 MainPreferencesFragment.<init> -> onCreatePreferences | OK | PreferencesActivity.java:41-46 committed transaction (androidx, INFERRED) |
| 17 | Eccc3a740 MainPreferencesFragment.onCreatePreferences -> S_SETTINGS_MAIN | OK | MainPreferencesFragment.java:9-10; res/xml/preferences.xml |
| 18 | E3452b602 S_SETTINGS_MAIN -> PreferencesActivity.onPreferenceStartFragment | OK | PreferencesActivity.java:80 callback for a row with android:fragment |
| 19 | E63d9f2a4 onPreferenceStartFragment -> ImportExportPreferencesFragment.<init> | OK | PreferencesActivity.java:81 instantiate; preferences.xml:38 names the class; no explicit constructor in ImportExportPreferencesFragment.java |
| 20 | E245f8b40 ImportExportPreferencesFragment.<init> -> onCreatePreferences | OK | PreferencesActivity.java:84, 91-97 (androidx, INFERRED) |
| 21 | E91eeed07 onCreatePreferences -> lambda$onCreatePreferences$6 | OK | ImportExportPreferencesFragment.java:105-106 pref_import listener; build name confirmed |
| 22 | Eb87e30cd lambda$onCreatePreferences$6 -> Dialogs.showImportersDialog | OK | ImportExportPreferencesFragment.java:107 isDirect false |
| 23 | Ebb77585c Dialogs.showImportersDialog -> lambda$showImportersDialog$27 | OK | Dialogs.java:536-538 OK button; name present in Dialogs.class (also $26 at the row click, $27 is the later one); pre-checked row is Aegis (Dialogs.java:521, 528; strings.xml app_name; DatabaseImporter.java:34) |
| 24 | E8f0c9a56 lambda$showImportersDialog$27 -> lambda$onCreatePreferences$5 | OK | Dialogs.java:537; ImportExportPreferencesFragment.java:107-113 |
| 25 | E63f82c4b lambda$onCreatePreferences$5 -> VaultManager.fireIntentLauncher(Fragment) | OK | ImportExportPreferencesFragment.java:110-112; VaultManager.java:263-267; ActivityNotFound for GET_CONTENT shows an error (VaultManager.java:295-300) |
| 26 | Ebe3b8b81 fireIntentLauncher -> lambda$new$0 | UNCLEAR | another app's picker must return a file (env); standard config has no file to pick (ImportExportPreferencesFragment.java:73-79) |
| 27 | E36289880 lambda$new$0 -> onImportSelectResult | OK | ImportExportPreferencesFragment.java:75-77 data non-null |
| 28 | E4770a1db onImportSelectResult -> ImportFileTask.doInBackground | OK | ImportExportPreferencesFragment.java:146-148, 158; ProgressDialogTask.java:69-75; AsyncTask.java:594-595, 326-339 |
| 29 | E810536ac ImportFileTask.doInBackground -> onPostExecute | OK | AsyncTask.java:369-374, 691-697 (onPostExecute unless cancelled); ImportFileTask.java:53-56 |
| 30 | Ed10f6640 ImportFileTask.onPostExecute -> lambda$onImportSelectResult$11 | OK | ImportFileTask.java:55 unconditional; ImportExportPreferencesFragment.java:151-157 |

Verdict: ERROR 0, UNCLEAR 3, OK 27.

Fixes:
- None (no ERROR steps). UNCLEAR steps 8, 9 and 26 need a vault file from an earlier run or a picked file.

## ScannerActivity.unbindPreview (steps: 15)

| step | edge | result | reason |
|---|---|---|---|
| 1 | Eb9515d18 S_ENTRY -> AegisApplication.<init> | OK | ActivityThread.java:5713-5715 |
| 2 | E5b266140 AegisApplication.<init> -> Hilt_AegisApplication.onCreate | OK | ActivityThread.java:5740; AegisApplication.java has no onCreate |
| 3 | E1ef992ce Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate | OK | Hilt build class (generated, line 43) |
| 4 | E88ed9829 AegisApplicationBase.onCreate -> S_PROCESS | OK | AegisApplicationBase.java:45-47 |
| 5 | E28ffc58c S_PROCESS -> MainActivity.<init> | OK | AndroidManifest.xml:44-51; the launcher intent has no action extra (see step 9) |
| 6 | Eb76444fd MainActivity.<init> -> MainActivity.onCreate | OK | ActivityThread.java:2729-2731; MainActivity.java:193-194 |
| 7 | E3a06baed MainActivity.onCreate -> MainActivity.onStart | OK | ActivityThread.java:2739-2741; onCreate has no finish (MainActivity.java:193-264); MainActivity.java:938-940 |
| 8 | E1ff98fce MainActivity.onStart -> MainActivity.doShortcutActions | UNCLEAR | line 1006 is reached only when isVaultInitNeeded() is false (MainActivity.java:942-948); a fresh install returns at 947, so this needs an existing vault from an earlier run (cross-run) |
| 9 | E01ce0942 MainActivity.doShortcutActions -> MainActivity.startScanActivity | ERROR | the launcher intent from step 5 has no action extra, so doShortcutActions returns at MainActivity.java:839-841; only action=scan producers reach 846 (see Fixes) |
| 10 | E4c53d66d startScanActivity -> ScannerActivity.<init> | OK | MainActivity.java:803-809; PermissionHelper.java:22-36 returns true when CAMERA is granted (standard config for this route) |
| 11 | Edd5d8048 ScannerActivity.<init> -> ScannerActivity.onCreate | OK | ActivityThread.java:2729-2741; ScannerActivity.java:53 |
| 12 | Eea6435c6 ScannerActivity.onCreate -> lambda$onCreate$0 | OK | ScannerActivity.java:67-68, 88 listener runs on the main executor; abortIfOrphan false on fresh start (AegisActivity.java:155) |
| 13 | E314fd012 lambda$onCreate$0 -> S_SCANNER@CAMERA_READY | UNCLEAR | needs at least one lens exposed to CameraX (ScannerActivity.java:77-83 finishes the page when none); camera hardware is not in the standard configuration |
| 14 | Ef5aafb40 S_SCANNER@CAMERA_READY -> ScannerActivity.onOptionsItemSelected | UNCLEAR | the camera switch icon is shown only with two lenses (ScannerActivity.java:137-148, setVisible(dual) at 148); needs two cameras (hardware) |
| 15 | Eb5012061 ScannerActivity.onOptionsItemSelected -> ScannerActivity.unbindPreview | OK | ScannerActivity.java:108-113 (provider set; action_camera); unbindPreview at 169-172 |

Verdict: ERROR 1, UNCLEAR 3, OK 11.

Fixes:
- Step 9: the launcher tap (step 5) sends no "action" extra, so doShortcutActions returns at MainActivity.java:840-841 before startScanActivity. Re-point step 5 to an entry that carries action=scan: the Quick Settings tile (LaunchScannerTileService.java:32-33; already in the graph at graph_def.py:325-328), or the dynamic app shortcut "shortcut_new" (AegisApplicationBase.java:76-77; not in the graph, add it as a producer if that entry is wanted).

## AuthActivity.lambda$onCreate$3 (steps: 14)

| step | edge | result | reason |
|---|---|---|---|
| 1 | Eb9515d18 S_ENTRY -> AegisApplication.<init> | OK | ActivityThread.java:5713-5715 |
| 2 | E5b266140 AegisApplication.<init> -> Hilt_AegisApplication.onCreate | OK | ActivityThread.java:5740; AegisApplication.java has no onCreate |
| 3 | E1ef992ce Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate | OK | Hilt build class (generated, line 43) |
| 4 | E88ed9829 AegisApplicationBase.onCreate -> S_PROCESS | OK | AegisApplicationBase.java:45-47 |
| 5 | E28ffc58c S_PROCESS -> MainActivity.<init> | OK | AndroidManifest.xml:44-51 |
| 6 | Eb76444fd MainActivity.<init> -> MainActivity.onCreate | OK | ActivityThread.java:2729-2731; MainActivity.java:193-194 |
| 7 | E3a06baed MainActivity.onCreate -> MainActivity.onStart | OK | ActivityThread.java:2739-2741; onCreate has no finish (MainActivity.java:193-264) |
| 8 | E57db524e MainActivity.onStart -> MainActivity.startAuthActivity | UNCLEAR | needs an encrypted vault file from an earlier run (cross-run); fresh install takes the intro branch (MainActivity.java:942-948) |
| 9 | E06202b0e MainActivity.startAuthActivity -> AuthActivity.<init> | OK | MainActivity.java:1147-1150; _isAuthenticating false from onCreate (MainActivity.java:201) |
| 10 | E0158aff6 AuthActivity.<init> -> AuthActivity.onCreate | OK | AuthActivity.java:73-128; readVaultFile failure path at 121-128 is not taken for a valid file |
| 11 | E911809ef AuthActivity.onCreate -> AuthActivity.onResume | OK | AuthActivity.java:211-224; AegisActivity.java:89-92; neither AuthActivity nor AegisActivity defines onStart (grep), so the performStart step runs framework code only (ActivityThread.java:2741) |
| 12 | E87843ac5 AuthActivity.onResume -> S_AUTH | OK | AuthActivity.java:211-224 unlock screen in front |
| 13 | E26725a4d S_AUTH -> AuthActivity.lambda$onCreate$4 | UNCLEAR | needs an accepted fingerprint or face (hardware, not in standard config) and a BiometricSlot with a keystore key from an earlier run (AuthActivity.java:132-150); prompt at 270-293 |
| 14 | Ec640bc11 lambda$onCreate$4 -> lambda$onCreate$3 | UNCLEAR | the reminder dialog replaces the prompt only when isPasswordReminderNeeded() (AuthActivity.java:181-190); BIWEEKLY default (Preferences.java:120-124) fires 14 days after first construction (Preferences.java:64-65, 138-145; PassReminderFreq.java:20-21, 34); not due on a fresh install at standard clock |

Verdict: ERROR 0, UNCLEAR 3, OK 11.

Fixes:
- None (no ERROR steps). UNCLEAR steps 8, 13 and 14 need an earlier-run encrypted vault, biometric hardware, and a clock moved 14 days forward.

## GoogleAuthImporter.readFromApp (steps: 34)

| step | edge | result | reason |
|---|---|---|---|
| 1 | Eb9515d18 S_ENTRY -> AegisApplication.<init> | OK | ActivityThread.java:5713-5715 |
| 2 | E5b266140 AegisApplication.<init> -> Hilt_AegisApplication.onCreate | OK | ActivityThread.java:5740; AegisApplication.java has no onCreate |
| 3 | E1ef992ce Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate | OK | Hilt build class (generated, line 43) |
| 4 | E88ed9829 AegisApplicationBase.onCreate -> S_PROCESS | OK | AegisApplicationBase.java:45-47 |
| 5 | E28ffc58c S_PROCESS -> MainActivity.<init> | OK | AndroidManifest.xml:44-51 |
| 6 | Eb76444fd MainActivity.<init> -> MainActivity.onCreate | OK | ActivityThread.java:2729-2731; MainActivity.java:193-194 |
| 7 | E3a06baed MainActivity.onCreate -> MainActivity.onStart | OK | ActivityThread.java:2739-2741; onCreate has no finish (MainActivity.java:193-264) |
| 8 | E20e76e09 MainActivity.onStart -> MainActivity.loadEntries | UNCLEAR | needs a plain-text vault from an earlier run (cross-run); fresh install returns at MainActivity.java:942-947 |
| 9 | Ea76ae1a0 MainActivity.loadEntries -> S_LIST | UNCLEAR | needs the vault loaded by step 8 (MainActivity.java:1134-1138; VaultManager.java:231-233) |
| 10 | E887b87bf S_LIST -> MainActivity.onOptionsItemSelected | OK | MainActivity.java:1086-1089; menu_main.xml:50 |
| 11 | Ef4e32054 onOptionsItemSelected -> startPreferencesActivity() | OK | MainActivity.java:1088-1089 |
| 12 | Ef64f95ee startPreferencesActivity() -> startPreferencesActivity(Class,String) | OK | MainActivity.java:827 |
| 13 | E640fb9eb startPreferencesActivity(Class,String) -> PreferencesActivity.<init> | OK | MainActivity.java:830-834 |
| 14 | E94201299 PreferencesActivity.<init> -> PreferencesActivity.onCreate | OK | ActivityThread.java:2729-2741; PreferencesActivity.java:24 |
| 15 | E50e3cfda PreferencesActivity.onCreate -> MainPreferencesFragment.<init> | OK | PreferencesActivity.java:26-27, 40-46 |
| 16 | E382bc001 MainPreferencesFragment.<init> -> onCreatePreferences | OK | PreferencesActivity.java:41-46 (androidx, INFERRED) |
| 17 | Eccc3a740 MainPreferencesFragment.onCreatePreferences -> S_SETTINGS_MAIN | OK | MainPreferencesFragment.java:9-10; preferences.xml |
| 18 | E3452b602 S_SETTINGS_MAIN -> PreferencesActivity.onPreferenceStartFragment | OK | PreferencesActivity.java:80 |
| 19 | E63d9f2a4 onPreferenceStartFragment -> ImportExportPreferencesFragment.<init> | OK | PreferencesActivity.java:81; preferences.xml:38 |
| 20 | E245f8b40 ImportExportPreferencesFragment.<init> -> onCreatePreferences | OK | PreferencesActivity.java:84, 91-97 (androidx, INFERRED) |
| 21 | Eda9f6e40 onCreatePreferences -> lambda$onCreatePreferences$8 | OK | ImportExportPreferencesFragment.java:117-123 pref_import_app listener |
| 22 | Ec00da88f lambda$onCreatePreferences$8 -> Dialogs.showImportersDialog | OK | ImportExportPreferencesFragment.java:119 isDirect true |
| 23 | E02b6c676 Dialogs.showImportersDialog -> lambda$showImportersDialog$27 | OK | Dialogs.java:536-538 OK button; the click sets the checked row, but the pre-checked row here is index 0, Authy (Dialogs.java:519-528; dialog_importers.xml:17 singleChoice); see step 34 |
| 24 | Ec769f085 lambda$showImportersDialog$27 -> lambda$onCreatePreferences$7 | OK | Dialogs.java:537; ImportExportPreferencesFragment.java:119-121 |
| 25 | Eca2b28fb lambda$onCreatePreferences$7 -> startImportEntriesActivity | OK | ImportExportPreferencesFragment.java:120 |
| 26 | Ec53371da startImportEntriesActivity -> ImportEntriesActivity.<init> | OK | ImportExportPreferencesFragment.java:161-165; file extra is null on the app path (line 120); manifest ImportEntriesActivity.java:40-42 |
| 27 | Ef8499dba ImportEntriesActivity.<init> -> onCreate | OK | ImportEntriesActivity.java:62 |
| 28 | E411f08d7 ImportEntriesActivity.onCreate -> startImport | OK | ImportEntriesActivity.java:63-66 (abortIfOrphan false on fresh start), 103-104 |
| 29 | E7faea19a startImport -> lambda$startImport$1 | OK | ImportEntriesActivity.java:109-113 warning shown when isInstalledAppVersionSupported() is false; GoogleAuthImporter.java:43-45 returns false when the app is absent, so the warning shows in standard config; Yes at 118-119 |
| 30 | Ee1e1ad6c lambda$startImport$1 -> startImportApp | OK | ImportEntriesActivity.java:119 |
| 31 | Ecf27001f startImportApp -> RootShellTask.doInBackground | OK | ImportEntriesActivity.java:173; RootShellTask.java:17-20; AsyncTask.java:594-595, 326-339 |
| 32 | E1de399e4 RootShellTask.doInBackground -> onPostExecute | OK | AsyncTask.java:369-374; RootShellTask.java:23-25 |
| 33 | Efb3b152a RootShellTask.onPostExecute -> lambda$startImportApp$5 | OK | RootShellTask.java:25; ImportEntriesActivity.java:145-147 (isFinishing check) |
| 34 | Ee74cd64a lambda$startImportApp$5 -> GoogleAuthImporter.readFromApp | ERROR | guard fails in the default dialog state: the checked row is AuthyImporter (Dialogs.java:519-528; dialog_importers.xml:17), so ImportEntriesActivity.java:156 calls AuthyImporter.readFromApp; also needs root (ImportEntriesActivity.java:149-153) and the app installed (GoogleAuthImporter.java:61; NameNotFound caught at ImportEntriesActivity.java:158) |

Verdict: ERROR 1, UNCLEAR 2, OK 31.

Fixes:
- Step 34: the direct-import dialog pre-checks row 0, which is Authy (Dialogs.java:519-528, singleChoice at dialog_importers.xml:17). Add a step that taps the "Google Authenticator" row (listed in the direct list, DatabaseImporter.java:44) before OK at step 23; otherwise the route ends at AuthyImporter. The route also needs the Google Authenticator app installed and root granted, which are outside the standard configuration.
