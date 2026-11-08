# Stage 3 route check R3-G1 (Aegis schema 2, round 3, read-only)

Date: 2026-10-27
Sources: graph_def.py (read only); app source final_java_only/Aegis/app/Aegis-#v3.4.2/app/src/main/java/com/beemdevelopment/aegis/; framework fw_src/android-8.1.0_r1/core/java/android/ (cited lines printed with cat -n or sed).
Scope: routes 1-5 of group R3-G1 (all five routes checked; totals in the summary below).

Rules applied:
- OK: edge target, class, guard and needs_state confirmed on disk; library dispatch (AsyncTask, View.performClick, ActivityThread lifecycle) verified in fw_src.
- ERROR: a fix is listed (graph_def.py edit, or "no fix in graph" with reason).
- UNCLEAR: the next node is reached only through a library body not on disk (androidx ActivityResultLauncher, RecyclerView, fragments/preferences, Preference clicks, AppCompat and Material dialogs, AppCompat menu dispatch), or the step needs an earlier run or an input the route env does not name.
- Hilt: generated code is not UNCLEAR. It is read from the build class (app/build/intermediates/classes/debug/transformDebugClassesWithAsm), so Hilt_AegisApplication edges are OK.

## Summary

| Route | Target | Steps | ERROR | UNCLEAR | OK |
|---|---|---|---|---|---|
| 1 | NoAutofillEditText.getAutofillType | 76 | 14 | 17 | 45 |
| 2 | VaultBackupManager$FileInfo.throwBadFormat | 31 | 5 | 3 | 23 |
| 3 | EntryAdapter.setTempHighlightEntry | 27 | 9 | 2 | 16 |
| 4 | MOTP.<init> | 22 | 2 | 2 | 18 |
| 5 | Dialogs.lambda$showDetailedMultiErrorDialog$22 | 35 | 4 | 11 | 20 |
| Total | | 191 | 34 | 35 | 122 |

## Route 1: NoAutofillEditText.getAutofillType (76 steps)

| # | Edge | Kind | Edge (src -> dst) | Verdict | Note |
|---|---|---|---|---|---|
| 1 | E14b4e906 | ENTRY | S_ENTRY -> AegisApplication.<init> | OK | AndroidManifest.xml:21-27 |
| 2 | E5b266140 | LIFECYCLE | AegisApplication.<init> -> Hilt_AegisApplication.onCreate | OK | Build class on disk: AegisApplication.class refers to Hilt_AegisApplication (transformDebugClassesWithAsm); source AegisApplication.java:6 extends AegisApplicationBase (Hilt rewrite) |
| 3 | E1ef992ce | CALL | Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate | OK | Build class on disk (transformDebugClassesWithAsm): Hilt_AegisApplication.onCreate runs hiltInternalInject(), then AegisApplicationBase.onCreate(), then returns (checked by bytecode order) |
| 4 | E88ed9829 | ENTERS | AegisApplicationBase.onCreate -> S_PROCESS | OK | AegisApplicationBase.java:45-67 |
| 5 | E28ffc58c | ENTRY | S_PROCESS -> MainActivity.<init> | OK | Manifest 44-51, LAUNCHER filter |
| 6 | Eb76444fd | LIFECYCLE | MainActivity.<init> -> onCreate | OK | ActivityThread 2729-2731, 2741; MainActivity 192-194 |
| 7 | E3a06baed | LIFECYCLE | MainActivity.onCreate -> onStart | OK | MainActivity 938-940 |
| 8 | E0602e719 | CALL | MainActivity.onStart -> startIntroActivity | OK | MainActivity 942-947. isVaultInitNeeded = !isVaultLoaded() && !fileExists (VaultManager 226-228); isVaultLoaded = _repo != null (VaultManager 222-224). Cold start: true |
| 9 | E4ce5043a | INTENT | MainActivity.startIntroActivity -> IntroActivity.<init> | UNCLEAR | Launch via introResultLauncher.launch (MainActivity 606); androidx body not on disk. Guard !_isDoingIntro (604) holds on cold start |
| 10 | E5e63fbe7 | LIFECYCLE | IntroActivity.<init> -> onCreate | OK | IntroActivity 35-41 |
| 11 | E93598a00 | CALL | IntroActivity.onCreate -> addSlide | OK | IntroActivity 38 |
| 12 | E1440feb8 | ENTERS | addSlide -> S_INTRO_WELCOME | UNCLEAR | Guard _slides.size()==1 (IntroBaseActivity 183-186) holds. But the hook it calls (IntroActivity.onAfterSlideChanged, IntroActivity 73-83) is a no-op (notification code commented out). The slide is shown by the ViewPager (library, not on disk) |
| 13 | Ee1d29ff8 | GUI | S_INTRO_WELCOME -> WelcomeSlide.lambda$onCreateView$1 | OK | WelcomeSlide 43-47; View.performClick (View 6286-6298) |
| 14 | E3870f4a6 | RESULT | WelcomeSlide.lambda$onCreateView$1 -> WelcomeSlide.lambda$new$0 | UNCLEAR | Launcher callback (WelcomeSlide 32-38) runs through androidx body not on disk |
| 15 | Ee4518b2e | CALL | WelcomeSlide.lambda$new$0 -> startImportVault | OK | Guard data != null && data.getData() != null (WelcomeSlide 35-36) |
| 16 | E4c857825 | ASYNC | startImportVault -> ImportFileTask.doInBackground | OK | WelcomeSlide 95; ProgressDialogTask 69-74; AsyncTask 632-650, 326-339 |
| 17 | E09458f31 | ASYNC | ImportFileTask.doInBackground -> onPostExecute | OK | AsyncTask 369-374, 691-697; ImportFileTask 53-56 |
| 18 | E87742878 | CALL | ImportFileTask.onPostExecute -> WelcomeSlide.lambda$startImportVault$2 | OK | _cb.onTaskFinished (ImportFileTask 55); callback at WelcomeSlide 59 |
| 19 | E32137f46 | CALL | WelcomeSlide.lambda$startImportVault$2 -> AegisImporter$EncryptedState.decrypt | OK | Guards: error null (WelcomeSlide 60-63); isEncrypted (68) |
| 20 | E71fa8be8 | CALL | EncryptedState.decrypt -> Dialogs.showPasswordInputDialog | OK | AegisImporter 90 |
| 21 | E62fef539 | CALL | Dialogs.showPasswordInputDialog -> Dialogs.showTextInputDialog | OK | Dialogs 271 |
| 22 | E5bb67188 | FRAMEWORK | Dialogs.showTextInputDialog -> Dialogs.lambda$showTextInputDialog$8 | UNCLEAR | AppCompat AlertDialog wrapper not on disk. android.app.Dialog show path is on disk (Dialog.java 333, 392-395, 1296) |
| 23 | Ec9266bec | FRAMEWORK | Dialogs.lambda$showTextInputDialog$8 -> Dialogs.lambda$showTextInputDialog$7 | OK | OK-button click listener is set in the OnShowListener (Dialogs 226-236); OK disabled until text non-empty (Dialogs 203, from earlier read) |
| 24 | E1ec716eb | CALL/non_standard | Dialogs.lambda$showTextInputDialog$7 -> SecurityPreferencesFragment.lambda$onCreatePreferences$7 | ERROR | Wrong listener. The dialog was opened by AegisImporter (step 20), but the shared node Dialogs.lambda$showTextInputDialog$7 fans out to every caller's listener (graph_def.py ~2040, ~2306, ~2757, ~2908). Fix: variant split of Dialogs.lambda$showTextInputDialog$7 per caller, so the AegisImporter caller reaches AegisImporter$EncryptedState.lambda$decrypt$1 (importers/AegisImporter.java:90-108). Also set cls explicit (app-to-app interface callback, as in steps 18 and 27) |
| 25 | Ec5219d4f | ASYNC | SecurityPreferencesFragment.lambda$onCreatePreferences$7 -> PasswordSlotDecryptTask.doInBackground | ERROR | Edge is right for the PIN path (digits-only guard, SecurityPreferencesFragment 158), but the importer password is not digits-only. Fix: replace steps 24-25 by AegisImporter$EncryptedState.lambda$decrypt$1 -> PasswordSlotDecryptTask.doInBackground (graph_def.py line 649, ASYNC) |
| 26 | E91f1f062 | ASYNC | PasswordSlotDecryptTask.doInBackground -> onPostExecute | OK | AsyncTask verified; PasswordSlotDecryptTask 87-90 |
| 27 | E59fcdb14 | CALL | PasswordSlotDecryptTask.onPostExecute -> AuthActivity$PasswordDerivationListener.onTaskFinished | ERROR | Instance mismatch. The task was built at SecurityPreferencesFragment.java:161 with PasswordConfirmationListener, so that instance runs, not AuthActivity's. Fix: target AegisImporter$EncryptedState.lambda$decrypt$0 (graph_def.py line 2790) on the importer path |
| 28 | Ef7f4f7c4 | CALL | AuthActivity$PasswordDerivationListener.onTaskFinished -> AuthActivity.finish | ERROR | Listener code is right (AuthActivity 345-356; result != null at 346), but it only runs for AuthActivity's own tasks, which this route never starts. Fix: reroute as in step 27; no edge change |
| 29 | E8a12fac2 | RESULT | AuthActivity.finish -> MainActivity.lambda$new$0 | ERROR | Result reaches the auth launcher only if MainActivity.startAuthActivity started AuthActivity (MainActivity 1146-1151). The route never starts it. No edge fix; insert MainActivity.startAuthActivity -> AuthActivity.<init> (graph_def.py lines 395, 619) before this step. Launcher body also UNCLEAR |
| 30 | E6b4310f7 | CALL | MainActivity.lambda$new$0 -> MainActivity.onDecryptResult | ERROR | Guard missing from edge text. Fix: add guard "activityResult.getResultCode() == RESULT_OK (MainActivity.java:137)" |
| 31 | E49a61ace | CALL | MainActivity.onDecryptResult -> loadEntries | OK | MainActivity 797-801 |
| 32 | E1ffae3d8 | ENTERS | MainActivity.loadEntries -> S_LIST | OK | Guard !_loaded (MainActivity 1134) |
| 33 | E887b87bf | GUI | S_LIST -> MainActivity.onOptionsItemSelected | UNCLEAR | AppCompat menu dispatch not on disk; onOptionsItemSelected 1086-1118 verified |
| 34 | Ef4e32054 | CALL | onOptionsItemSelected -> startPreferencesActivity() | OK | Guard action_settings (MainActivity 1088-1089) |
| 35 | Ef64f95ee | CALL | startPreferencesActivity() -> startPreferencesActivity(Class,String) | OK | MainActivity 827 |
| 36 | E640fb9eb | INTENT | startPreferencesActivity(Class,String) -> PreferencesActivity.<init> | UNCLEAR | preferenceResultLauncher.launch (MainActivity 834); androidx body not on disk |
| 37 | E94201299 | LIFECYCLE | PreferencesActivity.<init> -> onCreate | OK | PreferencesActivity 24; ActivityThread verified |
| 38 | Eea4c268e | CALL | PreferencesActivity.onCreate -> MainPreferencesFragment.<init> | OK | Guard savedInstanceState == null (PreferencesActivity 40). Early return at 26-28 not taken on a null bundle (AegisActivity 154-164) |
| 39 | E382bc001 | LIFECYCLE | MainPreferencesFragment.<init> -> onCreatePreferences | UNCLEAR | androidx fragment dispatch not on disk |
| 40 | Eccc3a740 | ENTERS | MainPreferencesFragment.onCreatePreferences -> S_SETTINGS_MAIN | OK | MainPreferencesFragment 9-11 (addPreferencesFromResource); PreferencesActivity 40-46 |
| 41 | E3452b602 | GUI | S_SETTINGS_MAIN -> PreferencesActivity.onPreferenceStartFragment | UNCLEAR | androidx Preference click dispatch not on disk; callback PreferencesActivity 80-84 verified |
| 42 | E63d9f2a4 | CALL/non_standard | PreferencesActivity.onPreferenceStartFragment -> ImportExportPreferencesFragment.<init> | UNCLEAR | FragmentFactory.instantiate (androidx) not on disk; target named by preferences.xml:38 |
| 43 | E245f8b40 | LIFECYCLE | ImportExportPreferencesFragment.<init> -> onCreatePreferences | UNCLEAR | androidx fragment dispatch not on disk |
| 44 | E91eeed07 | FRAMEWORK | ImportExportPreferencesFragment.onCreatePreferences -> lambda$onCreatePreferences$6 | UNCLEAR | Preference click dispatch (androidx) not on disk; listener set at ImportExportPreferencesFragment 105-106 |
| 45 | E5c464116 | CALL | lambda$onCreatePreferences$6 -> Dialogs.showImportersDialog | OK | ImportExportPreferencesFragment 107 (isDirect false) |
| 46 | Ebe22842e | FRAMEWORK | Dialogs.showImportersDialog -> Dialogs.lambda$showImportersDialog$27 | UNCLEAR | MaterialAlertDialogBuilder positive-button wiring not on disk; lambda at Dialogs 536-538 verified |
| 47 | E72c20578 | CALL | Dialogs.lambda$showImportersDialog$27 -> ImportExportPreferencesFragment.lambda$onCreatePreferences$7 | ERROR | Wrong listener and guard contradiction. Dialog opened from pref_import with isDirect false (ImportExportPreferencesFragment 107), but target is the isDirect true listener (lines 119-121). Fix: target ImportExportPreferencesFragment.lambda$onCreatePreferences$5 (edge exists at graph_def.py line 1642). Steps 48-49 then need the pref_import_app path (ImportExportPreferencesFragment 117-123) instead |
| 48 | Eca2b28fb | CALL | lambda$onCreatePreferences$7 -> startImportEntriesActivity | OK | Edge correct (ImportExportPreferencesFragment 120); unreachable from step 47 as written |
| 49 | E3156c24c | INTENT | startImportEntriesActivity -> ImportEntriesActivity.<init> | OK | Explicit startActivity (ImportExportPreferencesFragment 161-165) |
| 50 | Ef8499dba | LIFECYCLE | ImportEntriesActivity.<init> -> onCreate | OK | ImportEntriesActivity 62; ActivityThread verified |
| 51 | Eff12cb12 | FRAMEWORK | ImportEntriesActivity.onCreate -> lambda$onCreate$0 | OK | FAB click (ImportEntriesActivity 92-93); View.performClick verified |
| 52 | Eaa1a222c | CALL | lambda$onCreate$0 -> ImportEntriesActivity.saveAndFinish | OK | Guard: no entries or wipe off (ImportEntriesActivity 94-98) |
| 53 | E2b2da36a | FRAMEWORK | saveAndFinish -> lambda$saveAndFinish$10 | UNCLEAR | MaterialAlertDialogBuilder positive-button wiring not on disk (as step 46). Guards checked: saveAndBackupVault() true (ImportEntriesActivity 313) and hasIconPack (320) |
| 54 | Ea0f62157 | INTENT | lambda$saveAndFinish$10 -> AssignIconsActivity.<init> | OK | Explicit startActivity (ImportEntriesActivity 322-333) |
| 55 | E3ed34d26 | LIFECYCLE | AssignIconsActivity.<init> -> onCreate | OK | AssignIconsActivity 57 |
| 56 | E182263fc | FRAMEWORK | AssignIconsActivity.onCreate -> AssignIconAdapter.onBindViewHolder | UNCLEAR | RecyclerView bind not on disk (setAdapter 90; addEntries 113) |
| 57 | Ee848355c | FRAMEWORK | AssignIconAdapter.onBindViewHolder -> lambda$onBindViewHolder$0 | OK | Row click (AssignIconAdapter 40-42); View.performClick verified |
| 58 | E7cd59d3c | CALL | lambda$onBindViewHolder$0 -> AssignIconsActivity.onAssignIconEntryClick | OK | AssignIconAdapter 41 (interface call, explicit) |
| 59 | E42451aaa | CALL | AssignIconsActivity.onAssignIconEntryClick -> IconPickerDialog.create | OK | AssignIconsActivity 194 |
| 60 | Ec8d21670 | CALL | IconPickerDialog.create -> IconAdapter.loadIcons | OK | IconPickerDialog 127. Note: iconPacks.get(0) has no empty check; the page is reached only with an icon pack (ImportEntriesActivity 320) |
| 61 | E0ad50df8 | FRAMEWORK | IconAdapter.loadIcons -> IconAdapter.onBindViewHolder | UNCLEAR | RecyclerView bind not on disk |
| 62 | E9f3f0e20 | FRAMEWORK | IconAdapter.onBindViewHolder -> lambda$onBindViewHolder$2 | OK | Guard icon row (IconAdapter 168-169); View.performClick verified; click 173-179 |
| 63 | Efbf528db | CALL | IconAdapter.lambda$onBindViewHolder$2 -> EditEntryActivity$1.onCustomSelected | ERROR | Wrong listener. The picker was opened by AssignIconsActivity (step 59), whose onCustomSelected is empty (AssignIconsActivity.java:201). The shared node IconAdapter.lambda$onBindViewHolder$2 fans out to every picker (graph_def.py 3761). Fix: variant split of IconAdapter.lambda$onBindViewHolder$2 per picker. The suppression at graph_def.py 3765 only hides the AssignIcons target |
| 64 | E96dc91c6 | CALL | EditEntryActivity$1.onCustomSelected -> EditEntryActivity.startImageSelectionActivity | OK | EditEntryActivity 602; edge correct, but reachable only through step 63 |
| 65 | Edecf9fcc | CALL | startImageSelectionActivity -> VaultManager.fireIntentLauncher | OK | EditEntryActivity 577; startImageSelectionActivity 568-578 has no guard |
| 66 | E93aa99cf | RESULT | VaultManager.fireIntentLauncher -> MainActivity.lambda$new$7 | ERROR | Wrong launcher. The picker was started by EditEntryActivity (pickImageResultLauncher, EditEntryActivity 141-146, launched at 577), not MainActivity's codeScanResultLauncher (MainActivity 185-190, 812-824). Fix: target EditEntryActivity.lambda$new$1 (graph_def.py line 1318 already has this RESULT edge). Guard there: RESULT_OK (EditEntryActivity 144). Steps 67-73 are MainActivity's QR path and cannot follow from this picker |
| 67 | E909f3342 | CALL | MainActivity.lambda$new$7 -> MainActivity.onScanImageResult | ERROR | Guard missing. Fix: add "resultCode == RESULT_OK && data != null (MainActivity.java:187)". Depends on step 66 fix |
| 68 | Efe7a2f07 | CALL | MainActivity.onScanImageResult -> MainActivity.startDecodeQrCodeImages | ERROR | Guard missing. Fix: add "intent.getClipData() != null (MainActivity.java:645) and uris.size() > 0 (MainActivity.java:656)". Depends on step 66 fix |
| 69 | E5f504038 | ASYNC | MainActivity.startDecodeQrCodeImages -> QrDecodeTask.doInBackground | OK | MainActivity 669, 726; ProgressDialogTask 69-74; QrDecodeTask 24 |
| 70 | Ecc4391af | ASYNC | QrDecodeTask.doInBackground -> onPostExecute | OK | QrDecodeTask 51-53; AsyncTask verified |
| 71 | Ee5a5ce24 | CALL/non_standard | QrDecodeTask.onPostExecute -> MainActivity.lambda$startDecodeQrCodeImages$18 | ERROR | Class only. Target is correct (lambda at MainActivity 669). Fix: set cls explicit (as steps 18 and 27) |
| 72 | Eebe43dc6 | CALL | lambda$startDecodeQrCodeImages$18 -> MainActivity.importScannedEntries | ERROR | Guard missing. Runs only when the earlier error branches are not taken (MainActivity 705, 708, 713 not taken; errors.size()==0 at 718-723). Fix: add this guard text |
| 73 | Ef1d4cf7b | CALL | MainActivity.importScannedEntries -> startEditEntryActivityForNew | ERROR | Guard missing. Fix: add "entries.size() == 1 (MainActivity.java:730)" |
| 74 | E17c6e5f9 | INTENT | MainActivity.startEditEntryActivityForNew -> EditEntryActivity.<init> | UNCLEAR | addEntryResultLauncher.launch (MainActivity 506); androidx body not on disk |
| 75 | Ee228ce53 | LIFECYCLE | EditEntryActivity.<init> -> onCreate | OK | EditEntryActivity 165; ActivityThread verified |
| 76 | E0460ce8b | FRAMEWORK | EditEntryActivity.onCreate -> NoAutofillEditText.getAutofillType | UNCLEAR | ENV-gated. Framework paths on disk: focus 6966-6970 (notifyEnterOrExitForAutoFillIfNeeded), structure 7512-7535, isAutofillable 8013-8015. Env text is wrong for View.java:12196, which is onVisibilityAggregated (12178), not a focus path. Layout activity_edit_entry.xml contains NoAutofillEditText; setContentView at EditEntryActivity 170. The autofill request itself is not on disk; onCreate does not call getAutofillType directly |

Route 1 counts: 76 steps, OK 45, UNCLEAR 17, ERROR 14.

## Route 2: VaultBackupManager$FileInfo.throwBadFormat (31 steps)

env=- state=session (cold start: fresh install, no vault until the intro creates one)

| # | Edge | Kind | Edge (src -> dst) | Verdict | Note |
|---|---|---|---|---|---|
| 1 | E14b4e906 | ENTRY | S_ENTRY -> AegisApplication.<init> | OK | AndroidManifest.xml:21-27 |
| 2 | E5b266140 | LIFECYCLE | AegisApplication.<init> -> Hilt_AegisApplication.onCreate | OK | Build class on disk: AegisApplication.class refers to Hilt_AegisApplication; source AegisApplication.java:6 extends AegisApplicationBase (as route 1 step 2) |
| 3 | E1ef992ce | CALL | Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate | OK | Build class on disk: Hilt_AegisApplication.onCreate runs hiltInternalInject(), then AegisApplicationBase.onCreate(), then returns (as route 1 step 3) |
| 4 | E88ed9829 | ENTERS | AegisApplicationBase.onCreate -> S_PROCESS | OK | AegisApplicationBase.java:45-67 |
| 5 | E28ffc58c | ENTRY | S_PROCESS -> MainActivity.<init> | OK | Manifest 44-51, LAUNCHER filter |
| 6 | Eb76444fd | LIFECYCLE | MainActivity.<init> -> onCreate | OK | ActivityThread 2729-2731, 2741; MainActivity 192-194 |
| 7 | E3a06baed | LIFECYCLE | MainActivity.onCreate -> onStart | OK | MainActivity 938-940 |
| 8 | E0602e719 | CALL | MainActivity.onStart -> startIntroActivity | OK | MainActivity 942-947; isVaultInitNeeded true on a fresh install (VaultManager 222-228) |
| 9 | E4ce5043a | INTENT | MainActivity.startIntroActivity -> IntroActivity.<init> | UNCLEAR | introResultLauncher.launch (MainActivity 606); androidx body not on disk. Guard !_isDoingIntro (604) holds on cold start |
| 10 | E5e63fbe7 | LIFECYCLE | IntroActivity.<init> -> onCreate | OK | IntroActivity 35-41 |
| 11 | E93598a00 | CALL | IntroActivity.onCreate -> addSlide | OK | IntroActivity 38 |
| 12 | E1440feb8 | ENTERS | addSlide -> S_INTRO_WELCOME | UNCLEAR | Guard _slides.size()==1 holds (IntroBaseActivity 183-186). The hook is a no-op (IntroActivity 73-83); the ViewPager shows the slide (library, not on disk) |
| 13 | E6830b6dc | ENTERS | S_INTRO_WELCOME -> S_INTRO_PICKER | OK | Next on Welcome, not imported: IntroBaseActivity 80-93; IntroActivity 57-62; Welcome isFinished default true (SlideFragment 38-40) |
| 14 | E4fd4b49f | ENTERS | S_INTRO_PICKER -> S_INTRO_SETUP | OK | Guard: cryptType not NONE (IntroActivity 50-55); a picker choice made (SecurityPickerSlide 63-65) |
| 15 | Ead078030 | CALL | S_INTRO_SETUP -> SecuritySetupSlide.onNotFinishedError | OK | State: slide not finished (isFinished 117-135; passwords equal but no PasswordSlot yet). IntroBaseActivity 84-88; SecuritySetupSlide 138-146 |
| 16 | Ef86589e4 | CALL | SecuritySetupSlide.onNotFinishedError -> deriveKey | OK | Guard: passwords equal and type is password (SecuritySetupSlide 139, 141-142) |
| 17 | Ec6041c17 | ASYNC | SecuritySetupSlide.deriveKey -> KeyDerivationTask.doInBackground | OK | AsyncTask 594-595, 632-650, 326-339; SecuritySetupSlide 112-113; ProgressDialogTask 69-74 |
| 18 | E30d4c845 | ASYNC | KeyDerivationTask.doInBackground -> onPostExecute | OK | AsyncTask 369-374, 691-697; KeyDerivationTask 39-41 |
| 19 | E7f1310cf | CALL/non_standard | KeyDerivationTask.onPostExecute -> Dialogs.lambda$showSetPasswordDialog$2 | ERROR | Wrong listener. The task was built at SecuritySetupSlide.java:112 with new PasswordDerivationListener(), not the Dialogs.java:166 lambda. Fix: retarget to SecuritySetupSlide$PasswordDerivationListener.onTaskFinished (graph_def.py line 985 already has this edge), then S_INTRO_DONE (graph_def.py line 558). Steps 20-31 are the settings backup path, not the intro. They need a separate start: vault created, backups enabled, and the set-backup-password dialog opened from SecurityPreferencesFragment 235/253 |
| 20 | E193f27cd | CALL | Dialogs.lambda$showSetPasswordDialog$2 -> SecurityPreferencesFragment$SetBackupPasswordListener.onSlotResult | OK | Edge correct for the backup dialog (Dialogs.java:175). The shared node also fans out to callers at SecurityPreferencesFragment 84, 147 and ImportExport 454. Not reachable from step 19 as written (see step 19) |
| 21 | E58c507fc | CALL | SetBackupPasswordListener.onSlotResult -> PreferencesFragment.saveAndBackupVault | ERROR | Guard missing. The call at 387 runs only if the try at 370-386 completes; the catch at 381-384 returns first (SecurityPreferencesFragment.java). Fix: add "no exception in the try at 370-386 (catch 381-384 returns)" to the guard text |
| 22 | E4a0be42b | CALL | PreferencesFragment.saveAndBackupVault -> VaultManager.saveAndBackup | OK | PreferencesFragment 88-93; call at 90 inside a try with catch at 91 that handles the exception |
| 23 | E2cd88ac6 | CALL | VaultManager.saveAndBackup -> VaultManager.scheduleBackup | ERROR | Guards missing from edge text: getVault().isEncryptionEnabled() (VaultManager 143) and _prefs.isBackupsEnabled() (144). needs_state missing: backups default false (Preferences 400-401), and no step on this route enables them. Fix: add both guards and the needs_state "backups enabled", or add a step that enables backups |
| 24 | E5c9ce641 | CALL | VaultManager.scheduleBackup -> VaultBackupManager.scheduleBackup | ERROR | Guards missing. The call at 181 runs only if the cache dir exists or mkdir succeeds (VaultManager 169-171 throws IOException otherwise) and the temp-file export at 173-176 does not throw. It is inside try at 167; the catch at 182-183 rethrows VaultRepositoryException. Fix: add this guard text |
| 25 | E6de9a837 | ASYNC | VaultBackupManager.scheduleBackup -> lambda$scheduleBackup$0 | OK | _executor.execute (VaultBackupManager 58); newSingleThreadExecutor (53). JDK executor body not on disk; standard java.util.concurrent contract (INFERRED) |
| 26 | Eac29dfc9 | CALL | lambda$scheduleBackup$0 -> createBackup(File,BackupsVersioningStrategy,Uri,int) | OK | VaultBackupManager 59-60 inside try; catch 63-65 handles VaultRepositoryException and VaultBackupPermissionException |
| 27 | E983b61d4 | CALL | createBackup(File,BackupsVersioningStrategy,Uri,int) -> createBackup(File,Uri,int) | ERROR | Guards missing. Line 78 runs only when uri != null (VaultBackupManager 72-74 throws otherwise) and strategy == MULTIPLE_BACKUPS (77; SINGLE_BACKUPS at 75 takes the 2-arg call at 76). Fix: add "uri != null (72-74) and strategy == MULTIPLE_BACKUPS (77)" to the guard text |
| 28 | E832ab9cd | CALL | createBackup(File,Uri,int) -> enforceVersioning | OK | VaultBackupManager 150 after try/finally 143-148; the catch at 143-145 rethrows, so 150 runs only on success. enforceVersioning returns at once when versionsToKeep <= 0 (164-166) |
| 29 | Ec52c2d04 | CALL | enforceVersioning -> BackupFile.<init> | OK | State: versionsToKeep > 0 (default 5, Preferences 468-469). Guards isFile and !isVirtual (172); ParseException caught (175). Zero iterations if the backup folder is empty |
| 30 | E8ae9de66 | CALL | BackupFile.<init> -> FileInfo.parseFilename | OK | VaultBackupManager 274 |
| 31 | Eec05c5c1 | CALL | FileInfo.parseFilename -> FileInfo.throwBadFormat | UNCLEAR | Needs a backup-folder file whose name fails a format check (throwBadFormat at 222, 229, 234, 239). No step on this route creates one. ParseException caught and ignored (175) |

Route 2 counts: 31 steps, OK 23, UNCLEAR 3, ERROR 5 (ERROR: 19, 21, 23, 24, 27).

## Route 3: EntryAdapter.setTempHighlightEntry (27 steps)

env=- state=file;session (cross-run plain-text vault file, ST_PLAIN_VAULT_FILE; new manual entry; clipboard empty or not an otpauth link; the list entry visible after add)

| # | Edge | Kind | Edge (src -> dst) | Verdict | Note |
|---|---|---|---|---|---|
| 1 | E14b4e906 | ENTRY | S_ENTRY -> AegisApplication.<init> | OK | AndroidManifest.xml:21-27 |
| 2 | E5b266140 | LIFECYCLE | AegisApplication.<init> -> Hilt_AegisApplication.onCreate | OK | Build class on disk: AegisApplication.class refers to Hilt_AegisApplication; source AegisApplication.java:6 extends AegisApplicationBase (as route 1 step 2) |
| 3 | E1ef992ce | CALL | Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate | OK | Build class on disk: Hilt_AegisApplication.onCreate runs hiltInternalInject(), then AegisApplicationBase.onCreate(), then returns (as route 1 step 3) |
| 4 | E88ed9829 | ENTERS | AegisApplicationBase.onCreate -> S_PROCESS | OK | AegisApplicationBase.java:45-67 |
| 5 | E28ffc58c | ENTRY | S_PROCESS -> MainActivity.<init> | OK | Manifest 44-51, LAUNCHER filter |
| 6 | Eb76444fd | LIFECYCLE | MainActivity.<init> -> onCreate | OK | ActivityThread 2729-2731, 2741; MainActivity 192-194 |
| 7 | E3a06baed | LIFECYCLE | MainActivity.onCreate -> onStart | OK | MainActivity 938-940 |
| 8 | Ed6230165 | CALL | MainActivity.onStart -> MainActivity.loadEntries | ERROR | Guard incomplete. The call at 992 runs only when isVaultLoaded() is true (976-977 start auth otherwise) and _loaded is false (978). The edge text (graph_def.py 421-423) lists the plain-text load and the else branch but not the 976 check. Fix: add "isVaultLoaded() true (MainActivity.java:976-977 not taken)" to the guard. Cross-run dependency: the plain-text vault file must come from an earlier intro run (ST_PLAIN_VAULT_FILE, no producer in this run) |
| 9 | E1ffae3d8 | ENTERS | MainActivity.loadEntries -> S_LIST | OK | Guard !_loaded (MainActivity 1134); loadEntries 1133-1144 verified |
| 10 | E2e3490fc | GUI | S_LIST -> FabMenuHelper.lambda$setupClickListeners$0 | OK | FAB click listener FabMenuHelper 55; View.performClick 6289-6296 (onClick at 6294) verified |
| 11 | Eebad02db | CALL | FabMenuHelper.lambda$setupClickListeners$0 -> FabMenuHelper.toggle | OK | FabMenuHelper 55 (direct); class file confirms lambda$setupClickListeners$0 calls toggle |
| 12 | E0c457d96 | CALL | FabMenuHelper.toggle -> FabMenuHelper.open | ERROR | Guard missing. The call at 72 is the else branch of if (_isOpen) at 69 (close() otherwise). Fix: add "!_isOpen (FabMenuHelper.java:69-73, else branch)". The edge is bytecode-derived, not a literal in graph_def.py; add it with sup() plus an explicit e() (pattern at graph_def.py 378-381) |
| 13 | E75d0fba5 | FRAMEWORK | FabMenuHelper.open -> FabMenuHelper.lambda$setupClickListeners$2 | OK | State: menu open (ST_FAB_OPEN). Source open() is the graph's convention for menu-tap edges (graph_def.py 737). Handler name verified in class file: lambda$setupClickListeners$2 (descriptor (Runnable, View); calls Runnable.run and close). Dispatch is View.performClick |
| 14 | E0979a03c | CALL/non_standard | FabMenuHelper.lambda$setupClickListeners$2 -> MainActivity.startEditEntryActivity() | OK | Edge at graph_def.py 745-746. Enter item: MainActivity 256 maps fab_menu_item_enter to this::startEditEntryActivity. Note: the handler is shared by the scan and scan-image items (graph fan-out, not on this route) |
| 15 | E1b8fd9e8 | CALL | MainActivity.startEditEntryActivity() -> MainActivity.startEditEntryActivityForManual | ERROR | Guard missing. The call at 499 runs only when the clipboard is null (476) or does not parse as an otpauth URI (parseUri throws; catch at 494-496). A valid clipboard returns at 493 after its dialog (ST_CLIPBOARD_DIALOG). Fix: add "clipboard null or parseUri throws (MainActivity.java:476, 494-496)" to the guard. Bytecode-derived edge: add via sup() plus explicit e() |
| 16 | E6597c1f8 | INTENT | MainActivity.startEditEntryActivityForManual -> EditEntryActivity.<init> | UNCLEAR | addEntryResultLauncher.launch (MainActivity 513); androidx body not on disk (as route 1 step 74). Guard text (new manual entry, isManual true) matches 509-513 |
| 17 | Ee228ce53 | LIFECYCLE | EditEntryActivity.<init> -> EditEntryActivity.onCreate | OK | EditEntryActivity 165; Activity.onCreate verified (ActivityThread 2729-2731, 2741) |
| 18 | Ef6ab7dd8 | FRAMEWORK | EditEntryActivity.onCreate -> EditEntryActivity.onCreateOptionsMenu | UNCLEAR | AppCompat calls onCreateOptionsMenu; androidx body not on disk. Method body 656-666 verified |
| 19 | E69bb265a | FRAMEWORK | EditEntryActivity.onCreateOptionsMenu -> EditEntryActivity.onOptionsItemSelected | ERROR | Route picks delete, but action_delete is hidden for a new entry (EditEntryActivity 658-659 when _isNew), and this route's step 16 opens a new entry. Fix: route the menu tap to action_save (539-540): onOptionsItemSelected -> onSave (declared 845; calls addAndFinish at 867; guards parseEntry ok at 854 and no duplicate at 857-862) -> addAndFinish (668-681) -> saveAndFinish(entry,false) (680). graph_def.py has no onSave or addAndFinish edges (grep); add them near the gui edges at 1384-1390. Menu dispatch is AppCompat (not on disk) |
| 20 | E624f9135 | FRAMEWORK | EditEntryActivity.onOptionsItemSelected -> EditEntryActivity.lambda$onOptionsItemSelected$18 | ERROR | Unreachable for a new entry: the delete item is hidden (step 19). The lambda name is confirmed (class file: calls deleteAndFinish). Reroute only; no edge change. Dialog positive wiring (Dialogs.showDeleteEntriesDialog, MaterialAlertDialogBuilder) not on disk |
| 21 | E94c17e0d | CALL | EditEntryActivity.lambda$onOptionsItemSelected$18 -> EditEntryActivity.deleteAndFinish | ERROR | Edge valid (EditEntryActivity 542-544; class file confirms). Not on this route after the step 19 reroute. Reroute only; no edge change |
| 22 | E92b148c8 | CALL | EditEntryActivity.deleteAndFinish -> EditEntryActivity.saveAndFinish | ERROR | Valid code (695: saveAndFinish(entry, true)). Sets delete true, which contradicts step 23's guard. Reroute (step 19 fix); no edge change |
| 23 | E58ce4492 | RESULT | EditEntryActivity.saveAndFinish -> MainActivity.lambda$new$6 | ERROR | Edge guard (delete is false, from addAndFinish at 680; graph_def.py 1140) is right for the add path, but this route reaches it through deleteAndFinish (delete true). Fix: reroute steps 19-22 through onSave -> addAndFinish -> saveAndFinish(false) (step 19 fix). No edge change to step 23 |
| 24 | E16eb2dbc | CALL | MainActivity.lambda$new$6 -> MainActivity.onAddEntryResult | OK | Constructor launcher lambda 178-183; RESULT_OK and data check at 179-180 (graph_def.py 1152-1153). Class file has lambda$new$6 |
| 25 | Eaf3d5381 | CALL | MainActivity.onAddEntryResult -> EntryListView.onEntryAdded | ERROR | Guard missing. The body is inside if (_loaded) at MainActivity 619 (618-625). Edge is bytecode-derived (no literal in graph_def.py; grep finds only the step 24 edge). Fix: add "_loaded true (MainActivity.java:619)" via sup() plus explicit e(). The route has _loaded true from step 9 |
| 26 | E59ee7c4c | CALL | EntryListView.onEntryAdded -> EntryListView.tempHighlightEntry | OK | Guards at graph_def.py 2669-2670 match 444-446 (position >= 0), 449-450 (no scroll), else at 490-491. State: the entry is on screen (no scroll) |
| 27 | Eb404a7df | CALL | EntryListView.tempHighlightEntry -> EntryAdapter.setTempHighlightEntry | OK | Direct call at 496; tempHighlightEntry 495-500 has no guard |

Route 3 counts: 27 steps, OK 16, UNCLEAR 2, ERROR 9 (ERROR: 8, 12, 15, 19, 20, 21, 22, 23, 25).

## Route 4: MOTP.<init> (22 steps)

env=- state=data;session (cold start after an earlier run: the vault holds a MOTP entry with a PIN, step 20; the route env does not yet name the error-card state for step 11 or the second TOTP entry for step 13)

| # | Edge | Kind | Edge (src -> dst) | Verdict | Note |
|---|---|---|---|---|---|
| 1 | E14b4e906 | ENTRY | S_ENTRY -> AegisApplication.<init> | OK | AndroidManifest.xml:21-27. Backup or restore start uses the default Application class (ActivityThread 5715; LoadedApk 970), not on a launcher start |
| 2 | E5b266140 | LIFECYCLE | AegisApplication.<init> -> Hilt_AegisApplication.onCreate | OK | Build class on disk: AegisApplication.class refers to Hilt_AegisApplication; source AegisApplication.java:6 extends AegisApplicationBase. ActivityThread 5740 calls Application.onCreate |
| 3 | E1ef992ce | CALL | Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate | OK | Build class: onCreate runs hiltInternalInject(), then AegisApplicationBase.onCreate(), then returns (bytecode order) |
| 4 | E88ed9829 | ENTERS | AegisApplicationBase.onCreate -> S_PROCESS | OK | AegisApplicationBase.java:45-67; ActivityThread 5740 |
| 5 | E28ffc58c | ENTRY | S_PROCESS -> MainActivity.<init> | OK | Manifest 44-51: MAIN and LAUNCHER filter, exported |
| 6 | Eb76444fd | LIFECYCLE | MainActivity.<init> -> MainActivity.onCreate | OK | ActivityThread 2729-2731 (callActivityOnCreate); MainActivity 192-194 |
| 7 | E3a06baed | LIFECYCLE | MainActivity.onCreate -> MainActivity.onStart | OK | ActivityThread 2741 (performStart, calls onStart); MainActivity 938-940 |
| 8 | Ec7af65b2 | CALL | MainActivity.onStart -> MainActivity.updateErrorCard | OK | updateErrorCard is the last call in onStart (MainActivity 1003-1007). Returns at 947 (vault init needed), 960 and 971 (load errors) are not taken. Needs a vault present (state data) |
| 9 | E0c98179f | CALL | MainActivity.updateErrorCard -> EntryListView.setErrorCardInfo | OK | MainActivity 1196 (bytecode line matches source) |
| 10 | E440f596e | CALL | EntryListView.setErrorCardInfo -> EntryAdapter.setErrorCardInfo | OK | EntryListView 437-439 (direct wrapper, no guard) |
| 11 | E98d747f0 | CALL | EntryAdapter.setErrorCardInfo -> EntryAdapter.replaceEntryList | UNCLEAR | Guard (info differs from the shown one, EntryAdapter 153-155) is right. But updateErrorCard builds a non-null card only for an errored backup result, a needed and enabled backup reminder, or a needed plaintext warning (MainActivity 1163-1194; Preferences 495-505, 542-543, 550-552). All default to none, and the list starts with a null card (EntryAdapter 88), so the guard returns. Needs an earlier run that sets one of these. Fix: add it to the route env |
| 12 | Efafb0d56 | CALL | EntryAdapter.replaceEntryList -> EntryAdapter.updatePeriodUniformity | OK | EntryAdapter 285-288: the call is unconditional (bytecode 288 matches). Bytecode-derived, no literal in graph_def.py |
| 13 | Ea0594e14 | CALL | EntryAdapter.updatePeriodUniformity -> EntryHolder.setShowProgress | UNCLEAR | Guards are right (early return 578-580 not taken; TOTP holder 586; period differs from the most frequent one 587). But the loop runs only over bound holders (_holders, added at EntryAdapter 569). On the first onStart call, rows are not bound yet. Also, with the MOTP entry as the only TOTP entry, getMostFrequentPeriod (594-609) returns 10, the MOTP period, so setShowProgress(false). Needs an earlier run with a second TOTP entry of a different period (or no majority period, 630) and bound rows. Fix: add to the route env. Second caller on other routes: EntryHolder.setData 150 |
| 14 | E4eb59eb8 | CALL | EntryHolder.setShowProgress -> EntryHolder.startRefreshLoop | ERROR | Guard missing. The call at EntryHolder 252 runs only when showProgress is true after the HOTP override (245-247; progress set at 250). Bytecode-derived edge, no literal in graph_def.py. Fix: add an explicit e() via sup() (pattern at graph_def.py 378-381) with guard "showProgress true and entry not HOTP (EntryHolder.java:245-252)" |
| 15 | E0d080ed7 | CALL/non_standard | EntryHolder.startRefreshLoop -> EntryHolder$1.onRefresh | ERROR | Guard misplaced. graph_def.py 2637 holds the progress-bar guard, which belongs to step 14. The guard for this edge is UiRefresher not already running (UiRefresher.java:23-25, _running). The callback is posted with a delay (UiRefresher.java:28-34). The edge also skips UiRefresher.start and UiRefresher$1.run (app code, named in via only). Fix: change the guard at graph_def.py 2637 to the _running guard; move the progress-bar guard to the step 14 edge |
| 16 | E9119e58d | CALL | EntryHolder$1.onRefresh -> EntryHolder.refreshCode | OK | EntryHolder 109-111; bytecode 110 matches. EntryHolder$1 is the anonymous UiRefresher.Listener (EntryHolder 107; class file refers to UiRefresher$Listener) |
| 17 | E15dcda7a | CALL | EntryHolder.refreshCode -> EntryHolder.updateCodes | OK | EntryHolder 297-302; guard !_hidden && !_paused (298-299). Both flags are set in setData (130-131) and setPaused (507-515). Route state: row visible and not paused (defaults are false) |
| 18 | E19d9d207 | CALL | EntryHolder.updateCodes -> EntryHolder.getOtp() | OK | EntryHolder 304-305 (first statement; bytecode 305 matches) |
| 19 | Ec20b1d81 | CALL | EntryHolder.getOtp() -> EntryHolder.getOtp(int) | OK | EntryHolder 312-313 (return getOtp(0)) |
| 20 | E4db374dd | CALL | EntryHolder.getOtp(int) -> MotpInfo.getOtp | OK | EntryHolder 325-326: guard info instanceof TotpInfo; virtual dispatch to MotpInfo.getOtp (MotpInfo extends TotpInfo, MotpInfo.java:14). The MOTP entry with PIN comes from an earlier run, as declared in STATE (OtpInfo.java:134-136; MotpInfo.java:56) |
| 21 | Efcea8b94 | CALL | MotpInfo.getOtp -> MOTP.generateOTP(6-arg) | OK | MotpInfo 35-37 guard (_pin not null, else IllegalStateException); call at 40 inside try (39) |
| 22 | E730a31f1 | CALL | MOTP.generateOTP(6-arg) -> MOTP.<init> | OK | MOTP.java:37 (return new MOTP(code, digits)); no guard before it in the method (29-38). The constructor is private (16) and called from the same class |

Route 4 counts: 22 steps, OK 18, UNCLEAR 2, ERROR 2 (ERROR: 14, 15).

## Route 5: Dialogs.lambda$showDetailedMultiErrorDialog$22 (35 steps)

env=- state=file (cross-run: plain-text vault file from an earlier intro run, see step 8; an Authy export chosen by the user in the import dialog, not named in the route; the typed password decrypts it)

| # | Edge | Kind | Edge (src -> dst) | Verdict | Note |
|---|---|---|---|---|---|
| 1 | E14b4e906 | ENTRY | S_ENTRY -> AegisApplication.<init> | OK | AndroidManifest.xml:21-27 (as route 1 step 1) |
| 2 | E5b266140 | LIFECYCLE | AegisApplication.<init> -> Hilt_AegisApplication.onCreate | OK | Build class on disk (as route 1 step 2) |
| 3 | E1ef992ce | CALL | Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate | OK | Build class: hiltInternalInject(), then AegisApplicationBase.onCreate() (as route 1 step 3) |
| 4 | E88ed9829 | ENTERS | AegisApplicationBase.onCreate -> S_PROCESS | OK | AegisApplicationBase.java:45-67 |
| 5 | E28ffc58c | ENTRY | S_PROCESS -> MainActivity.<init> | OK | Manifest 44-51, LAUNCHER filter |
| 6 | Eb76444fd | LIFECYCLE | MainActivity.<init> -> onCreate | OK | ActivityThread 2729-2731; MainActivity 192-194 |
| 7 | E3a06baed | LIFECYCLE | MainActivity.onCreate -> onStart | OK | ActivityThread 2741; MainActivity 938-940 |
| 8 | Ed6230165 | CALL | MainActivity.onStart -> MainActivity.loadEntries | ERROR | Guard incomplete. loadEntries (MainActivity 992) is the else of if (!isVaultLoaded()) at 976-977 (startAuthActivity otherwise) and of else if (_loaded) at 978. The edge text has the plain-text load and _loaded but not isVaultLoaded() true. Fix: add "isVaultLoaded() true (MainActivity.java:976-977 not taken)" to the guard (as route 3 step 8). Cross-run state: plain-text vault file from an earlier intro run (no producer in this run) |
| 9 | E1ffae3d8 | ENTERS | MainActivity.loadEntries -> S_LIST | OK | Guard !_loaded (MainActivity 1134); loadEntries 1133-1144. Depends on step 8 fix |
| 10 | E887b87bf | GUI | S_LIST -> MainActivity.onOptionsItemSelected | UNCLEAR | AppCompat menu dispatch not on disk (as route 1 step 33); onOptionsItemSelected 1086-1118 verified |
| 11 | Ef4e32054 | CALL | MainActivity.onOptionsItemSelected -> MainActivity.startPreferencesActivity() | OK | Guard action_settings (MainActivity 1088-1089) |
| 12 | Ef64f95ee | CALL | MainActivity.startPreferencesActivity() -> startPreferencesActivity(Class,String) | OK | MainActivity 827 (no-arg overload 826-828) |
| 13 | E640fb9eb | INTENT | startPreferencesActivity(Class,String) -> PreferencesActivity.<init> | UNCLEAR | preferenceResultLauncher.launch (MainActivity 834); androidx body not on disk (as route 1 step 36) |
| 14 | E94201299 | LIFECYCLE | PreferencesActivity.<init> -> onCreate | OK | PreferencesActivity 24; ActivityThread verified |
| 15 | Eea4c268e | CALL | PreferencesActivity.onCreate -> MainPreferencesFragment.<init> | OK | Guard savedInstanceState == null (PreferencesActivity 40-41), as route 1 step 38 |
| 16 | E382bc001 | LIFECYCLE | MainPreferencesFragment.<init> -> onCreatePreferences | UNCLEAR | androidx fragment dispatch not on disk (as route 1 step 39) |
| 17 | Eccc3a740 | ENTERS | MainPreferencesFragment.onCreatePreferences -> S_SETTINGS_MAIN | OK | MainPreferencesFragment 9-11; PreferencesActivity 40-46 |
| 18 | E3452b602 | GUI | S_SETTINGS_MAIN -> PreferencesActivity.onPreferenceStartFragment | UNCLEAR | androidx Preference click dispatch not on disk; callback PreferencesActivity 80-84 verified (as route 1 step 41). The tapped row must be the Import/Export row (preferences.xml:38), not Security; see step 19 |
| 19 | Ed19f3b08 | CALL/non_standard | PreferencesActivity.onPreferenceStartFragment -> SecurityPreferencesFragment.<init> | ERROR | Wrong branch for the target. The edge is right for the row it names (reflection at PreferencesActivity 81; preferences.xml:26), but the Authy import is reached from the Import/Export row (preferences.xml:38; route 1 step 42, E63d9f2a4 -> ImportExportPreferencesFragment.<init>). Fix: no edge change. Reroute steps 18-19 to that row and drop steps 20-26 (the pin path). Also add the missing import entry: the Import/Export file import (ImportExportPreferencesFragment 105-107; the file pick is a launcher, not on disk), then ImportEntriesActivity.onCreate -> startImportFile (ImportEntriesActivity 127) -> processImporterState (134) -> DecryptListener (176-183), then AuthyImporter$EncryptedState.decrypt (AuthyImporter 206-207) |
| 20 | E5c8f972e | LIFECYCLE | SecurityPreferencesFragment.<init> -> onCreatePreferences | UNCLEAR | androidx fragment dispatch not on disk (as route 1 step 39). Not reached as written (step 19) |
| 21 | Eb2d49c8f | FRAMEWORK | SecurityPreferencesFragment.onCreatePreferences -> SecurityPreferencesFragment.lambda$onCreatePreferences$9 | UNCLEAR | Preference change dispatch (androidx) not on disk. Listener name confirmed by probe (Preference, Object; calls Dialogs.showPasswordInputDialog). Guard 153-155 (switch turned on) verified. Not reached as written (step 19) |
| 22 | Eafa4c4f5 | CALL | SecurityPreferencesFragment.lambda$onCreatePreferences$9 -> Dialogs.showPasswordInputDialog | OK | SecurityPreferencesFragment.java:157 direct call (probe confirms). Not reached as written (step 19) |
| 23 | E62fef539 | CALL | Dialogs.showPasswordInputDialog -> Dialogs.showTextInputDialog | OK | Dialogs 271 (as route 1 step 21) |
| 24 | E5bb67188 | FRAMEWORK | Dialogs.showTextInputDialog -> Dialogs.lambda$showTextInputDialog$8 | UNCLEAR | AppCompat AlertDialog wrapper not on disk (as route 1 step 22). Probe confirms lambda$showTextInputDialog$8 is the OnShowListener body (getButton, setEnabled, setOnClickListener) |
| 25 | Ec9266bec | FRAMEWORK | Dialogs.lambda$showTextInputDialog$8 -> Dialogs.lambda$showTextInputDialog$7 | OK | OK button click set directly on the button (Dialogs 231); View.performClick calls onClick at View.java 6294. OK disabled until text (Dialogs 203, as route 1 step 23) |
| 26 | E02b5fa3e | CALL/non_standard | Dialogs.lambda$showTextInputDialog$7 -> AuthyImporter$EncryptedState.lambda$decrypt$0 | ERROR | Wrong listener on this route. Step 22 opened the pin dialog (SecurityPreferencesFragment.java:157), so its OK click reaches SecurityPreferencesFragment.lambda$onCreatePreferences$7 (probe: takes char[], calls PasswordSlotDecryptTask), not AuthyImporter. The target name lambda$decrypt$0 is correct for the Authy caller (AuthyImporter.java:207-210; probe confirms it calls decrypt, onStateDecrypted, onError). Shared-node fan-out (as route 1 step 24). Fix: variant split of Dialogs.lambda$showTextInputDialog$7 per caller; keep this edge on the Authy-caller variant and set cls explicit (app-to-app interface callback). Needs the step 19 reroute so the Authy dialog is open at the OK click |
| 27 | E26208cc0 | CALL/explicit | AuthyImporter$EncryptedState.lambda$decrypt$0 -> ImportEntriesActivity$2.onStateDecrypted | ERROR | Guard missing. The call at AuthyImporter.java:210 is inside try (209); the catch at 211-212 calls listener.onError instead, so it runs only when decrypt(password) does not throw. Fix: add "decrypt(password) does not throw (AuthyImporter.java:209; catch 211-212 calls onError)" to the guard. Target confirmed: ImportEntriesActivity$2 is the DecryptListener (onError and onCanceled match 186-194; onStateDecrypted calls processDecryptedImporterState, bytecode @5) |
| 28 | Efdf9842a | CALL/explicit | ImportEntriesActivity$2.onStateDecrypted -> ImportEntriesActivity.processDecryptedImporterState | OK | ImportEntriesActivity 181-182 direct call (bytecode @5) |
| 29 | Ece6b33ed | CALL/explicit | ImportEntriesActivity.processDecryptedImporterState -> ImportEntriesActivity.processImporterResult | UNCLEAR | Edge is the else branch at ImportEntriesActivity 230-231 (bytecode @120). Guards are right in code: convert does not throw (207-212) and icons empty (220). Both depend on the input file, which the route env does not name. The icon path (221-229) calls processImporterResult from a lambda instead. Fix: add a parseable Authy file with no icons needing optimisation to the route env |
| 30 | Eb9310dac | CALL/explicit | ImportEntriesActivity.processImporterResult -> Dialogs.showMultiExceptionDialog | UNCLEAR | Guard errors.size() > 0 (ImportEntriesActivity 245-248) is right. It needs an input file with at least one entry error, or the dialog never opens. The route env does not name it. Fix: add to env |
| 31 | Efbfd355a | CALL/explicit | Dialogs.showMultiExceptionDialog -> Dialogs.showMultiErrorDialog | OK | Dialogs 452 direct call (bytecode matches) |
| 32 | E5c7dbe16 | FRAMEWORK | Dialogs.showMultiErrorDialog -> Dialogs.lambda$showMultiErrorDialog$20 | UNCLEAR | Details listener (Dialogs 439-441) is passed to MaterialAlertDialogBuilder. The first hop (View.performClick, View.java 6289-6296) is on disk, but the dialog button handler that calls the listener is AppCompat/Material, not on disk (as route 1 step 46). Probe confirms lambda$showMultiErrorDialog$20 calls showDetailedMultiErrorDialog |
| 33 | E25822db8 | CALL/explicit | Dialogs.lambda$showMultiErrorDialog$20 -> Dialogs.showDetailedMultiErrorDialog | OK | Dialogs 440 direct call (bytecode and probe agree) |
| 34 | E9e8ecab9 | FRAMEWORK | Dialogs.showDetailedMultiErrorDialog -> Dialogs.lambda$showDetailedMultiErrorDialog$23 | UNCLEAR | OnShowListener set at Dialogs 476-477. It runs on AlertDialog.show: the android.app.Dialog show path is on disk, but the AppCompat AlertDialog wrapper is not (as route 1 step 22 and step 24 here). Probe confirms lambda$showDetailedMultiErrorDialog$23 is the OnShowListener body (getButton, setOnClickListener) |
| 35 | E47462230 | FRAMEWORK | Dialogs.lambda$showDetailedMultiErrorDialog$23 -> Dialogs.lambda$showDetailedMultiErrorDialog$22 | OK | Copy listener set directly on the neutral button (Dialogs 477-478); View.performClick calls onClick (View.java 6294). Probe confirms lambda$showDetailedMultiErrorDialog$22 is the Copy body (ClipboardManager, Toast; Dialogs 479-482). Depends on step 34 (dialog shown) |

Route 5 counts: 35 steps, OK 20, UNCLEAR 11, ERROR 4 (ERROR: 8, 19, 26, 27).

