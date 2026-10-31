# Stage 4 route check R4-G3 (Aegis schema 2, round 4, read-only)

Date: 2026-10-27. Sources: graph built at out/ 21:58:57 (newer than graph_def.py 21:57:47), routes printed with tools/show_route.py (its FW-SRC lines were printed by hand from fw_src/android-8.1.0_r1), app source final_java_only/Aegis/app/Aegis-#v3.4.2/app/src/main/java/com/beemdevelopment/aegis/ and manifest.

Policy used (conservative reading, as asked):
- UNCLEAR for any hop whose body is androidx, AppCompat, Material, Hilt or other generated code (not on disk), even when the app side of the hop was checked. Printed app lines are cited for that step.
- A guard omitted from the graph text is ERROR. When the route itself is unaffected, the step says so.
- Cross-run STATE: none on these routes.

## Summary

| Route | Target | Steps | ERROR steps | UNCLEAR steps | OK steps |
|---|---|---|---|---|---|
| 1 | ImportExportPreferencesFragment$ExportResultListener.onTaskFinished | 55 | 8, 17, 24, 25, 26, 27, 28 | 2, 3, 9, 14, 22, 29, 33, 36, 39, 41, 42, 43, 44, 46, 49 | 33 |
| 2 | IconPackExistsException.getIconPack | 30 | 26, 27 | 2, 3, 8, 10, 13, 16, 18, 19, 20, 24, 29 | 1, 4, 5, 6, 7, 9, 11, 12, 14, 15, 17, 21, 22, 23, 25, 28, 30 |
| 3 | Dialogs.lambda$showPartialGoogleAuthImportWarningDialog$30 | 24 | 14, 17, 18, 20 | 2, 3, 8, 16, 23 | 1, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15, 19, 21, 22, 24 |
| 4 | ApkSignaturePin.getSignatures | 11 | 8 | 2, 3, 7 | 1, 4, 5, 6, 9, 10, 11 |
| 5 | Hilt_AegisApplication.<init> | 2 | none | 2 | 1 |

Totals: 122 steps across the five routes: 14 ERROR, 35 UNCLEAR, 73 OK.

## Route 1: ImportExportPreferencesFragment$ExportResultListener.onTaskFinished

Route shape: cold start, intro, Welcome import of an encrypted file, unlock, settings, export. Steps 1 to 23 hold up. Steps 24 to 28 do not: the import password goes to the Settings PIN check and then to AuthActivity's listener, and AuthActivity is never started on this route. Steps 29 to 55 are a settings-and-export chain that is valid once the list is shown.

Step 2 (E5b266140, AegisApplication.<init> -> Hilt_AegisApplication.onCreate): UNCLEAR. Printed: ActivityThread.java:5740 (mInstrumentation.callApplicationOnCreate(app)); AegisApplication.java:6 (extends AegisApplicationBase, no onCreate). Source says: the system creates the application; the Hilt superclass onCreate is generated and not on disk. Fix proposed: none (generated code).

Step 3 (E1ef992ce, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate): UNCLEAR. Printed: AegisApplicationBase.java:45-47 (super.onCreate at 46 is in the base class, not the caller). Source says: the caller is the generated Hilt class (not on disk). Fix proposed: none (generated code).

Step 8 (E0602e719, MainActivity.onStart -> startIntroActivity): ERROR (text-only guard omission; route unaffected). Printed: VaultManager.java:226-227 (`return !isVaultLoaded() && !VaultRepository.fileExists(_context);`); MainActivity.java:942-947. Source says: the test has two clauses; the graph text has only the file clause. On a cold start the vault is not loaded, so the route holds. Fix proposed: guard text "vault init needed: no vault is loaded and no vault file exists (VaultManager.java:226-227; MainActivity.java:942)".

Step 9 (E4ce5043a, MainActivity.startIntroActivity -> IntroActivity.<init>): UNCLEAR. Printed: MainActivity.java:603-609 (guard `!_isDoingIntro` at 604 holds; launch at 606). Source says: the start goes through androidx ActivityResultLauncher.launch (not on disk). Fix proposed: none.

Step 14 (E3870f4a6, WelcomeSlide.lambda$onCreateView$1 -> WelcomeSlide.lambda$new$0): UNCLEAR. Printed: WelcomeSlide.java:32-38 (result callback registered with a guard at 35). Source says: the return to the callback is androidx ActivityResult code (not on disk). Fix proposed: none.

Step 17 (E09458f31, ImportFileTask.doInBackground -> ImportFileTask.onPostExecute): ERROR (text-only guard omission; route unaffected). Printed: AsyncTask.java:691-697 (finish calls onCancelled when cancelled, onPostExecute otherwise); ImportFileTask.java:53-56. Source says: onPostExecute runs only when the task is not cancelled; the graph has no guard. The cold path never cancels this task. Fix proposed: guard "the task was not cancelled (a cancelled task calls onCancelled instead, AsyncTask.java:691-697)", the same as step 54.

Step 22 (E5bb67188, Dialogs.showTextInputDialog -> Dialogs.lambda$showTextInputDialog$8): UNCLEAR. Printed: Dialogs.java:226-229 (OnShowListener disables OK), 239 (showSecureDialog(dialog)). Source says: the listener runs inside AlertDialog.show() (AppCompat, not on disk). Fix proposed: none.

Step 24 (E1ec716eb, Dialogs.lambda$showTextInputDialog$7 -> SecurityPreferencesFragment.lambda$onCreatePreferences$7): ERROR (wrong listener for this route). Printed: Dialogs.java:231-235 (OK click calls the listener passed by the caller, at 233); AegisImporter.java:90-109 (the import passes its own password lambda); SecurityPreferencesFragment.java:157 (the Settings PIN dialog). Source says: on this route the listener is AegisImporter's password lambda (AegisImporter.java:90-109), not the Settings one. Dialogs.lambda$showTextInputDialog$7 is a shared relay that serves every caller. Fix proposed: point the dst at AegisImporter$EncryptedState.lambda$decrypt$1, the password TextInputListener (AegisImporter.java:90-108; name mapping from graph_def.py:2803). Steps 25 to 28 must be rewritten as well.

Step 25 (Ec5219d4f, SecurityPreferencesFragment.lambda$onCreatePreferences$7 -> PasswordSlotDecryptTask.doInBackground): ERROR (wrong branch). Printed: SecurityPreferencesFragment.java:158-162 (digits-only check, then a task with PasswordConfirmationListener at 161). Source says: this is the Settings PIN check. The import path starts its own task in AegisImporter.java:92-108 with a result callback, and it has no digits check. Fix proposed: source the step at AegisImporter$EncryptedState.lambda$decrypt$1 (AegisImporter.java:90-108). The ASYNC edge from that lambda to PasswordSlotDecryptTask.doInBackground already exists (graph_def.py:649-650, SRC importers/AegisImporter.java:93,108); use it in place of the Settings edge, which carries the digits-only check.

Step 26 (E91f1f062, PasswordSlotDecryptTask.doInBackground -> PasswordSlotDecryptTask.onPostExecute): ERROR (text-only guard omission; route unaffected). Printed: PasswordSlotDecryptTask.java:87-90; AsyncTask.java:691-697 (onPostExecute only when not cancelled). Source says: the not-cancelled guard is missing from the graph text. Fix proposed: add guard "the task was not cancelled (a cancelled task calls onCancelled instead, AsyncTask.java:691-697)".

Step 27 (E59fcdb14, PasswordSlotDecryptTask.onPostExecute -> AuthActivity$PasswordDerivationListener.onTaskFinished): ERROR (wrong listener). Printed: PasswordSlotDecryptTask.java:87-90 (calls _cb); AuthActivity.java:343-364 (the listener); AuthActivity.java:174 (the only place it is created, for the unlock screen); SecurityPreferencesFragment.java:161 (its own PasswordConfirmationListener); AegisImporter.java:93-105 (the import's result callback). Source says: the callback for this route is the AegisImporter result callback, not AuthActivity's. Fix proposed: point the dst at AegisImporter$EncryptedState.lambda$decrypt$0, the result callback (AegisImporter.java:93-105; name mapping from graph_def.py:2803 and the existing edge at graph_def.py:2848-2851).

Step 28 (Ef7f4f7c4, AuthActivity$PasswordDerivationListener.onTaskFinished -> AuthActivity.finish): ERROR (order impossible on this route). Printed: AuthActivity.java:345-356 (guard `result != null` at 346 is correct); AuthActivity.java:295-311 (finish); MainActivity.java:1146-1151 (the only AuthActivity start, not on this route). Source says: AuthActivity is never shown on this route, so its listener and fields do not exist at this point. Fix proposed: replace steps 25 to 28 with the import continuation that the source supports: the AegisImporter result callback (AegisImporter.java:93-105) calls listener.onStateDecrypted, which is WelcomeSlide$1.onStateDecrypted (WelcomeSlide.java:71-74) and then importVault (WelcomeSlide.java:98-109: writes the vault file, then goToNextSlide). The intro's remaining slides and IntroActivity finish with loadFrom and RESULT_OK (IntroActivity.java:110-129) then return to MainActivity.introResultLauncher (MainActivity.java:141-147), onIntroResult, and loadEntries (MainActivity.java:752-754, 1133-1144).

Step 29 (E8a12fac2, AuthActivity.finish -> MainActivity.lambda$new$0): UNCLEAR. Printed: AuthActivity.java:295-311; ActivityThread.java:4253-4265 (deliverResults -> dispatchActivityResult); Activity.java:5526-5527 (finish). Source says: the last hop into the MainActivity launcher callback is androidx (not on disk). The route is also wrong here because AuthActivity is not started (see step 28). Fix proposed: none in this step; step 28 fix applies.

Step 33 (E887b87bf, S_LIST -> MainActivity.onOptionsItemSelected): UNCLEAR. Printed: MainActivity.java:1086-1093. Source says: a toolbar tap reaches onOptionsItemSelected through AppCompat (not on disk). Fix proposed: none.

Step 36 (E640fb9eb, MainActivity.startPreferencesActivity(Class,String) -> PreferencesActivity.<init>): UNCLEAR. Printed: MainActivity.java:830-834 (launch through preferenceResultLauncher). Source says: the launch goes through androidx ActivityResultLauncher (not on disk). Fix proposed: none.

Step 39 (E382bc001, MainPreferencesFragment.<init> -> MainPreferencesFragment.onCreatePreferences): UNCLEAR. Printed: PreferencesActivity.java:40-46 (commit). Source says: the attach then onCreatePreferences order is androidx.fragment and preference code (not on disk). Fix proposed: none.

Step 41 (E3452b602, S_SETTINGS_MAIN -> PreferencesActivity.onPreferenceStartFragment): UNCLEAR. Printed: PreferencesActivity.java:19, 80-84; preferences.xml:8-44. Source says: the row tap reaches the activity callback through androidx Preference (not on disk). Fix proposed: none.

Step 42 (E63d9f2a4, PreferencesActivity.onPreferenceStartFragment -> ImportExportPreferencesFragment.<init>): UNCLEAR. Printed: PreferencesActivity.java:80-84 (instantiate with pref.getFragment() at 81); preferences.xml:38 (ImportExport row). Source says: the reflection is in androidx FragmentFactory (not on disk). The non_standard class and the row are right. Fix proposed: none.

Step 43 (E245f8b40, ImportExportPreferencesFragment.<init> -> ImportExportPreferencesFragment.onCreatePreferences): UNCLEAR. Printed: PreferencesActivity.java:84, 91-97. Source says: the attach then onCreatePreferences order is androidx (not on disk). Fix proposed: none.

Step 44 (E629987fd, ImportExportPreferencesFragment.onCreatePreferences -> lambda$onCreatePreferences$9): UNCLEAR. Printed: ImportExportPreferencesFragment.java:125-129 (click listener registered for pref_export). Source says: the tap reaches the listener through androidx Preference (not on disk). Fix proposed: none.

Step 46 (E76172dad, ImportExportPreferencesFragment.startExport -> lambda$startExport$20): UNCLEAR. Printed: ImportExportPreferencesFragment.java:201-209 (OnShowListener), 332 (showSecureDialog). Source says: the listener runs inside AppCompat AlertDialog.show() (not on disk). Fix proposed: none.

Step 49 (Eedce6158, VaultManager.fireIntentLauncher@EXPORT -> ImportExportPreferencesFragment.lambda$new$1): UNCLEAR. Printed: ImportExportPreferencesFragment.java:81-83 (exportResultLauncher callback calls onExportResult with CODE_EXPORT); 403-411 (encrypt picks exportResultLauncher at 405); VaultManager.java:263-266 (Fragment overload). Source says: the return to the callback goes through androidx ActivityResultLauncher (not on disk). The guard (encrypted Aegis format) and the ENV text match the code. Fix proposed: none.

Steps that are OK (33): 1, 4, 5, 6, 7, 10, 11, 12, 13, 15, 16, 18, 19, 20, 21, 23, 30, 31, 32, 34, 35, 37, 38, 40, 45, 47, 48, 50, 51, 52, 53, 54, 55.
Notes on the OK steps: step 1 checked the backup-start class claim (ActivityThread.java:5715-5716, LoadedApk.java:970-971). Step 18 is a shared relay (ImportFileTask.onPostExecute) but reaches the WelcomeSlide callback that this route actually created (WelcomeSlide.java:59). Steps 30 to 32 hold on their own, but they depend on the broken auth segment at 24 to 29. Step 40 depends on the androidx step 39.

## Route 2: IconPackExistsException.getIconPack

Route shape: cold start, the plain-text vault from an earlier run loads in onStart, then Settings, Icon packs, import, the "already exists" dialog, Yes, getIconPack. Steps 1 to 7 and 9 to 25 are sound. Step 8 needs an earlier run (cross-run STATE). Steps 26 and 27 are the problem: the printed route has no exception source between the background import and the result.

1. OK: S_ENTRY to AegisApplication.<init>. Manifest 21-27.
2. UNCLEAR: AegisApplication.<init> to Hilt_AegisApplication.onCreate. Hilt-generated base class, not on disk. The system call is ActivityThread.java:5740 (FW).
3. UNCLEAR: Hilt_AegisApplication.onCreate to AegisApplicationBase.onCreate. Generated code.
4. OK: AegisApplicationBase.onCreate to S_PROCESS. AegisApplicationBase.java:45-67.
5. OK: S_PROCESS to MainActivity.<init> (launcher). AndroidManifest.xml:44-51.
6. OK: MainActivity.<init> to onCreate. FW ActivityThread.java:2729-2731; MainActivity.java:192-194.
7. OK: onCreate to onStart. FW ActivityThread.java:2741; MainActivity.java:938-940.
8. UNCLEAR: MainActivity.onStart to loadEntries. The guard text checks out: the early return at 947 is the intro branch (MainActivity.java:942-947), the plain-text load is at 951-973 (loadFrom at 965), isVaultLoaded at 976, _loaded at 978, loadEntries at 991-992. The STATE is a plain-text vault written by an earlier intro run (cross-run), so it needs an earlier run and is UNCLEAR under the policy.
9. OK: loadEntries to S_LIST. Guard _loaded at MainActivity.java:1134.
10. UNCLEAR: S_LIST to MainActivity.onOptionsItemSelected. The toolbar tap goes through AppCompat (not on disk). Printed MainActivity.java:1086-1093.
11. OK: onOptionsItemSelected to startPreferencesActivity(). Guard action_settings at 1088-1089.
12. OK: startPreferencesActivity() to startPreferencesActivity(Class,String). MainActivity.java:827.
13. UNCLEAR: startPreferencesActivity(Class,String) to PreferencesActivity.<init>. The launch at MainActivity.java:834 goes through the androidx ActivityResultLauncher (not on disk).
14. OK: PreferencesActivity.<init> to onCreate. PreferencesActivity.java:24; FW ActivityThread.java:2729-2731.
15. OK: PreferencesActivity.onCreate to MainPreferencesFragment.<init>. Guards at PreferencesActivity.java:26-27 and 40-41 (savedInstanceState null).
16. UNCLEAR: MainPreferencesFragment.<init> to onCreatePreferences. Committed fragment transaction, androidx (not on disk). PreferencesActivity.java:41-46.
17. OK: onCreatePreferences to S_SETTINGS_MAIN. MainPreferencesFragment.java:7-12; preferences.xml:8-44.
18. UNCLEAR: S_SETTINGS_MAIN to PreferencesActivity.onPreferenceStartFragment. The row tap goes through androidx Preference (not on disk). PreferencesActivity.java:80-84.
19. UNCLEAR: onPreferenceStartFragment to IconPacksManagerFragment.<init>. The reflection is androidx FragmentFactory.instantiate (not on disk); the call site is PreferencesActivity.java:81 and the row at preferences.xml:19-21 names the class at line 20.
20. UNCLEAR: IconPacksManagerFragment.<init> to onViewCreated. androidx fragment (not on disk). IconPacksManagerFragment.java:65,69.
21. OK: onViewCreated to lambda$onViewCreated$1. FAB tap via FW View.performClick (View.java:6289-6296); IconPacksManagerFragment.java:70-71.
22. OK: lambda$onViewCreated$1 to startImportIconPack. Line 71.
23. OK: startImportIconPack to VaultManager.fireIntentLauncher(Fragment,...). Line 175.
24. UNCLEAR: fireIntentLauncher to lambda$new$0 (the import result callback). The return goes through androidx ActivityResultLauncher (not on disk). The ENV text matches: ACTION_GET_CONTENT at IconPacksManagerFragment.java:173-174 (printed). VaultManager.java:263-269 checked.
25. OK: lambda$new$0 to importIconPack. Guard RESULT_OK && data != null && data.getData() != null at IconPacksManagerFragment.java:59.
26. ERROR (text-only; route unaffected): importIconPack to ImportIconPackTask.doInBackground (ASYNC). The edge note at graph_def.py:2155 says ProgressDialogTask.execute (IconPacksManagerFragment.java:155) is "skipped on purpose". Line 155 is `task.execute(getLifecycle(), new ImportIconPackTask.Params(...))`, which calls ProgressDialogTask.execute(Lifecycle, Params...) (ProgressDialogTask.java:69-74). The note is wrong; the path does go through that wrapper. Fix: replace the note with "task.execute(lifecycle, params) at IconPacksManagerFragment.java:155 goes through ProgressDialogTask.execute (ProgressDialogTask.java:69-74), then AsyncTask.execute, then doInBackground (ImportIconPackTask.java:26)".
27. ERROR (route gap): ImportIconPackTask.doInBackground to onPostExecute (ASYNC). The stored route has no edge that puts the exception into the result. The exception is raised in importPack: ImportIconPackTask.java:41 calls importPack; IconPackManager.java:84-90 throws IconPackExistsException when packDir exists or the UUID is already installed; the catch at ImportIconPackTask.java:43-45 returns Result(null, e). graph_def.py already has these edges (2157 doInBackground to importPack; 2159 importPack to IconPackExistsException.<init>; 2206-2209 <init> back to doInBackground), but the printed route skips them. Fix: insert these three steps before this one: doInBackground to IconPackManager.importPack (CALL, ImportIconPackTask.java:41); IconPackManager.importPack to IconPackExistsException.<init> (CALL, guard IconPackManager.java:84 or 87-89); IconPackExistsException.<init> to doInBackground (CALL, catch at ImportIconPackTask.java:43-45).
28. OK: ImportIconPackTask.onPostExecute to lambda$importIconPack$5 (the callback). ImportIconPackTask.java:54-57; callback at IconPacksManagerFragment.java:134-154. Label note: the edge is CALL/explicit, but it is an interface callback (_cb.onTaskFinished, ImportIconPackTask.java:56). Route 1 labels its equivalent callback non_standard, so the label is inconsistent across the two routes.
29. UNCLEAR: lambda$importIconPack$5 to lambda$importIconPack$4 (the Yes button). The AlertDialog button dispatch goes through AppCompat/Material (not on disk). The FW View.performClick hop only covers the view tap. STATE text is too narrow: the source fires the exists error after an earlier import in the same run too (IconPackManager.java:84 checks the folder that the same run wrote). The text "from an earlier run" should also say "or an earlier import in this run".
30. OK: lambda$importIconPack$4 to IconPackExistsException.getIconPack. IconPacksManagerFragment.java:142; IconPackExistsException.java:3 (extends IconPackException, so the catch at ImportIconPackTask.java:43 applies) and 11-13.

Route 2 counts: OK 17, UNCLEAR 11, ERROR 2 (26, 27).

## Route 5: Hilt_AegisApplication.<init>

Header says confirmed_by=SOURCE, but step 2 rests on build output for Hilt-generated code, so that label overstates it.

1. OK: S_ENTRY to AegisApplication.<init>. AndroidManifest.xml:21-27.
2. UNCLEAR: AegisApplication.<init> to Hilt_AegisApplication.<init> (CALL). AegisApplication.java:6 says `extends AegisApplicationBase`; the rewrite to Hilt_AegisApplication happens at build time and the generated class is not on disk. The printed evidence cites the bytecode, which cannot be checked from source. Fix: none; relabel the header as confirmed_by=BUILD or INFERRED.

Route 5 counts: OK 1, UNCLEAR 1, ERROR 0.

## Route 3: Dialogs.lambda$showPartialGoogleAuthImportWarningDialog$30

Route shape: cold start, the main list, the + menu, scan image, QR decode on a background thread, the partial Google Auth warning, then Show error details. The route holds from start to finish. The four ERRORs are guard or note omissions in the edge text; the route is unaffected by each.

1. OK: S_ENTRY to AegisApplication.<init>. AndroidManifest.xml:21-27.
2. UNCLEAR: AegisApplication.<init> to Hilt onCreate. Generated code, not on disk.
3. UNCLEAR: Hilt onCreate to AegisApplicationBase.onCreate. Generated code.
4. OK: AegisApplicationBase.onCreate to S_PROCESS. AegisApplicationBase.java:45-67.
5. OK: S_PROCESS to MainActivity.<init> (launcher). AndroidManifest.xml:44-51.
6. OK: MainActivity.<init> to onCreate. FW ActivityThread.java:2729-2731; MainActivity.java:192-194.
7. OK: onCreate to onStart. FW ActivityThread.java:2741; MainActivity.java:938-940.
8. UNCLEAR: onStart to loadEntries. Guard text checks out (MainActivity.java:947 is the intro-branch return; 951-973 plain-text load; 976-992 branches). The STATE is a plain-text vault from an earlier intro run (cross-run), so UNCLEAR under the policy.
9. OK: loadEntries to S_LIST. Guard _loaded at MainActivity.java:1134.
10. OK: S_LIST to FabMenuHelper.lambda$setupClickListeners$0 (+ FAB tap). FW View.java:6289-6296 (performClick); FabMenuHelper.java:55.
11. OK: lambda$setupClickListeners$0 to toggle. Direct call, FabMenuHelper.java:55.
12. OK: toggle to open. Guard _isOpen false is the else branch (FabMenuHelper.java:68-74); open() checks _isOpen at 77.
13. OK: open to lambda$setupClickListeners$2 (menu item tap). FW performClick; FabMenuHelper.java:59-64. The STATE (menu open) is set at 81 and shown at 89 (checked).
14. ERROR (text-only; route unaffected): lambda$setupClickListeners$2 to MainActivity.startScanImageActivity (Runnable.run). The guard onClick != null (FabMenuHelper.java:60) is missing from the edge text. The scan-image item always has a Runnable (MainActivity.java:255), so the route holds. Fix: add guard "onClick != null (FabMenuHelper.java:60); true for the scan-image item (MainActivity.java:255)".
15. OK: startScanImageActivity to fireIntentLauncher(Activity,...)@QR_SCAN. MainActivity.java:823; VaultManager.java:243-247.
16. UNCLEAR: fireIntentLauncher to MainActivity.lambda$new$7 (launcher callback). The return goes through androidx ActivityResult (not on disk). ENV matches the chooser at MainActivity.java:813-823. The FW deliverResults hop (ActivityThread.java:4253-4265) was checked only up to dispatch.
17. ERROR (text-only; route unaffected): lambda$new$7 to onScanImageResult. The guard RESULT_OK && getData() != null (MainActivity.java:186-187) is missing from the edge text. Fix: add that guard.
18. ERROR (text-only; route unaffected): onScanImageResult to startDecodeQrCodeImages. The call at MainActivity.java:657 sits inside if (getClipData() != null) (645) and if (uris.size() > 0) (656). Neither is in the edge text. Fix: add guard "clip data present (MainActivity.java:645) and at least one URI (656)".
19. OK: startDecodeQrCodeImages to QrDecodeTask.doInBackground (ASYNC). task.execute(getLifecycle(), uris) at MainActivity.java:726 goes through ProgressDialogTask.execute (ProgressDialogTask.java:69-74). No false note on this edge.
20. ERROR (text-only; route unaffected): QrDecodeTask.doInBackground to QrDecodeTask.onPostExecute (ASYNC). The not-cancelled guard is missing (AsyncTask.java:691-697), the same omission as route 1 steps 17 and 26. Fix: add guard "the task was not cancelled (a cancelled task calls onCancelled instead, AsyncTask.java:691-697)".
21. OK: QrDecodeTask.onPostExecute to lambda$startDecodeQrCodeImages$18. _cb.onTaskFinished(results) at QrDecodeTask.java:53; callback opened at MainActivity.java:669. Label non_standard is right for an interface callback.
22. OK: callback to Dialogs.showPartialGoogleAuthImportWarningDialog. Guard at MainActivity.java:700-712 is correct: the call at 712 is reached only when googleAuthExports is non-empty, the batch is single (the non-single branches return at 705 and 708), and missingIndices is non-empty. The call is inside the lambda (669-725).
23. UNCLEAR: showPartialGoogleAuthImportWarningDialog to lambda$showPartialGoogleAuthImportWarningDialog$31 (OnShowListener). AppCompat AlertDialog show() runs the listener (not on disk). Dialogs.java:570-580 (setOnShowListener at 570; showSecureDialog at 580).
24. OK: lambda$...$31 to lambda$...$30 (Show error details tap). FW View.java:6289-6296 (performClick); Dialogs.java:571-576. Guard "the scan had errors" holds: the neutral button is added only then (Dialogs.java:565-567).

Route 3 counts: OK 15, UNCLEAR 5 (2, 3, 8, 16, 23), ERROR 4 (14, 17, 18, 20).

## Route 4: ApkSignaturePin.getSignatures

Route shape: the Guardian Project panic app sends the TRIGGER action, PanicResponderActivity checks the caller's signature (TrustedIntents), then compares it with the pinned signer. Step 8 cannot hold with the manifest and the library as written, so steps 9 to 11 cannot be reached from this entry. This is a route-level block, not only a text issue.

1. OK: S_ENTRY to AegisApplication.<init>. AndroidManifest.xml:21-27.
2. UNCLEAR: AegisApplication.<init> to Hilt onCreate. Generated code (as route 2 step 2).
3. UNCLEAR: Hilt onCreate to AegisApplicationBase.onCreate. Generated code.
4. OK: AegisApplicationBase.onCreate to S_PROCESS. AegisApplicationBase.java:45-67.
5. OK: S_PROCESS to PanicResponderActivity.<init> (intent resolved by action). AndroidManifest.xml:91-101 (launchMode="singleInstance" at line 94); PanicResponderActivity.java:16.
6. OK: PanicResponderActivity.<init> to onCreate. PanicResponderActivity extends AegisActivity (PanicResponderActivity.java:15), so super.onCreate runs AegisActivity.onCreate, which sets _prefs at AegisActivity.java:63.
7. UNCLEAR: onCreate to TrustedIntents.getIntentFromTrustedSender. Guards are correct: PanicResponderActivity.java:22-26 (trigger enabled), 29 and 35-36 (test build branch). The STATE is the pref_panic_trigger preference (default false; Preferences.java:107-108). The process starts cold at step 5, so the preference must come from an earlier process: cross-run, UNCLEAR.
8. ERROR (guard cannot hold; route blocked here): getIntentFromTrustedSender to isPackageNameTrusted. The guard "calling package name not empty" (TrustedIntents.java:106-109) needs getCallingPackageName to return a package, which needs getCallingActivity() non-null. Activity.java:5384-5390 (FW, on disk) says the calling package is null unless the caller used startActivityForResult with a request code. Step 5 does not say the panic app does this. The manifest sets launchMode="singleInstance" (AndroidManifest.xml:94), and TrustedIntents.java:120-124 warns that a singleInstance activity cannot get the calling activity. So packageName is null, getIntentFromTrustedSender returns null (TrustedIntents.java:107-108), and PanicResponderActivity falls through to finish() (PanicResponderActivity.java:46) without the trigger. The enforcing framework code (ActivityManager service) is not in fw_src, so the conclusion rests on the library warning and the FW doc note. Fix: the owner must either mark the target unreachable from the panic trigger, or correct the edge text to name the startActivityForResult requirement and the launch-mode restriction.
9. OK (downstream of step 8): isPackageNameTrusted to checkTrustedSigner(String). Direct call at TrustedIntents.java:85-86; the catches at 87-92 return false. The edge is mechanically right but cannot be reached while step 8 is blocked.
10. OK (downstream): checkTrustedSigner(String) to checkTrustedSigner(Signature[]). getPackageInfo at TrustedIntents.java:216 and the call at 217. The guard text (getPackageInfo returns the package) matches.
11. OK (downstream): checkTrustedSigner(Signature[]) to ApkSignaturePin.getSignatures. Throws at TrustedIntents.java:227-231; loop over pinList at 234-235 (the call pin.getSignatures() at 235). Pins are added at PanicResponderActivity.java:31-32. ApkSignaturePin.java:17 is the target.

Route 4 counts: OK 7 (1, 4, 5, 6, 9, 10, 11), UNCLEAR 3 (2, 3, 7), ERROR 1 (8).
