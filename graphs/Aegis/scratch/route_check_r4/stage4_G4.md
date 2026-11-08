# Stage 4 route check R4-G4 (Aegis schema 2, round 4, read-only)

Date: 2026-10-27. Sources: built graph out/aegis_trigger_graph.json (edges as printed by tools/show_route.py, and read directly where the tool failed), app source under final_java_only/Aegis/app/Aegis-#v3.4.2 (src/main/java), AOSP 8.1.0_r1 fw_src (Activity.java 7014-7019; ActivityThread.java 2729-2741, 5740; View.java 6289-6294).

Method notes (read before the verdicts):
- The shell expands `$` inside double quotes, so `"Dialogs.lambda$showDetailedMultiErrorDialog$22"` arrives as `Dialogs.lambda` ("no such method"). Single quotes were used for all method names.
- show_route.py prints "not found in the source tree" for every FW-SRC reference; those framework lines were printed with sed directly.
- Lambda numbers ($22, $23, ...) are compiler names from the build; the source cannot confirm the number, only the body, which is checked.
- Class `page` is used on ENTERS edges (20 of 21; the one other is E85a04dca, non_standard). It is not one of the three classes named in the brief; not counted as an error.
- All 18 INTENT edges in the graph are class standard (default). Step 13 follows that convention; not counted as an error.
- Library bodies (androidx, Material, AppCompat AlertDialog, FragmentFactory, dispatch of preference and dialog listeners) are not on disk: their steps are UNCLEAR per rule 7, with the app side checked.
- show_route.py main() reads the app name from argv[1], so the call needs a placeholder script name first (argv = [script, app, method, ...]). Run from cwd /Users/darshan/Desktop/yang/work (os.chdir inside the process, no shell cd).
- Guard standard used for all routes: a return is covered when the guard names it as not taken (for example "no early return at 947"). A guard that does not mention a return on the path is an omission (route 2 step 8).

## Summary

| Route | Target | Steps | ERROR steps | UNCLEAR steps | OK steps |
|---|---|---|---|---|---|
| 1 | Dialogs.lambda$showDetailedMultiErrorDialog$22 | 35 | 26 (wrong relay listener) | 2, 3, 8 (needs earlier run), 10, 13, 16, 18, 19, 20, 21, 24, 32, 34 | 21 (27 is OK in itself, but reached only through 26) |
| 2 | AuthActivity.lambda$onCreate$3 | 14 | 8 (text-only guard; route unaffected) | 2, 3, 8 (needs earlier run), 9, 13, 14 | 1, 4, 5, 6, 7, 10, 11, 12 |
| 3 | GoogleAuthImporter.readFromApp | 34 | 24 (wrong relay listener; prefix steps 21-22 is the pref_import row, isDirect false) | 2, 3, 8 (needs earlier run), 10, 13, 16, 18, 19, 20, 21, 23, 29 | 1, 4, 5, 6, 7, 9, 11, 12, 14, 15, 17, 22, 25, 26, 27, 28, 30, 31, 32, 33, 34 (25-34 OK in themselves, reached only through 24) |
| 4 | ImportExportPreferencesFragment.lambda$onImportSelectResult$11 | 30 | 26 (text-only guard; route unaffected) | 2, 3, 8 (needs earlier run), 10, 13, 16, 18, 19, 20, 21, 23 | 1, 4, 5, 6, 7, 9, 11, 12, 14, 15, 17, 22, 24, 25, 27, 28, 29, 30 |
| 5 | DaggerAegisApplication_HiltComponents_SingletonC$SingletonCImpl.injectVaultLockReceiver2 | 9 | none | 2, 3, 5, 6, 7, 8, 9 (generated code, not on disk; 5 and 6 also need the build or framework) | 1, 4 |

## Route 1: Dialogs.lambda$showDetailedMultiErrorDialog$22

Route verdict: ERROR. Step 26 hands the password-dialog OK click to the Authy listener, but this route's caller is the pin-keyboard path (steps 19-25), so steps 26-35 are not reachable from this prefix.

Step 2 (E5b266140, AegisApplication.<init> -> Hilt_AegisApplication.onCreate, LIFECYCLE standard): UNCLEAR. Printed: ActivityThread.java:5740 (`mInstrumentation.callApplicationOnCreate(app)`) and AegisApplication.java:6 (`public class AegisApplication extends AegisApplicationBase`, no onCreate). Source says the framework calls the application's onCreate at 5740; which onCreate runs is decided by the Hilt-generated superclass, not on disk. Fix: none (INFERRED generated body).

Step 3 (E1ef992ce, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate, CALL explicit): UNCLEAR. Generated Hilt code, not on disk. Fix: none.

Step 8 (E20e76e09, MainActivity.onStart -> MainActivity.loadEntries, CALL explicit, STATE):
- Guard OK (corrected on re-check; the first pass wrongly called it an omission). The guard says no early return at 947, 960 or 971 and that the plain-text file is loaded at 963-965. Those cover isVaultInitNeeded() being false (MainActivity.java:942-947) and !vaultFile.isEncrypted() (963). This is the same wording as route 3 and route 4 step 8, so it is not counted as an error.
- UNCLEAR (needs earlier run). The state text names the earlier intro run that chose no security, and cites MainActivity.java:951-973 (the reader). It does not cite the writer. Writer found: IntroActivity.java:92-100 (no-security case: creds is null, `_vaultManager.initNew(creds)` at line 100), and VaultManager.java:59-64 (initNew saves the repository). Fix proposed (text only): add the writer cite to needs_state, "written by IntroActivity.java:100 via VaultManager.initNew when no security is chosen". Producer not added to this route.

Step 10 (E887b87bf, S_LIST -> MainActivity.onOptionsItemSelected, GUI standard): UNCLEAR. Printed MainActivity.java:1086-1089 (method start; `if (itemId == R.id.action_settings)`). Source says the toolbar tap is dispatched by androidx.appcompat, not on disk. App side OK. Fix: none.

Step 13 (E640fb9eb, MainActivity.startPreferencesActivity(Class,String) -> PreferencesActivity.<init>, INTENT standard): UNCLEAR. Printed MainActivity.java:826-835 (explicit `new Intent(this, PreferencesActivity.class)`, then `preferenceResultLauncher.launch(intent)`). The launch goes through androidx.activity.result, not on disk. Class note: standard is the graph default for all 18 INTENT edges; not an error. Fix: none.

Step 16 (E382bc001, MainPreferencesFragment.<init> -> MainPreferencesFragment.onCreatePreferences, LIFECYCLE standard): UNCLEAR. The attach/create order is androidx.fragment and androidx.preference (not on disk). App side: MainPreferencesFragment.java:9-11 defines onCreatePreferences. Fix: none.

Step 18 (E3452b602, S_SETTINGS_MAIN -> PreferencesActivity.onPreferenceStartFragment, GUI standard): UNCLEAR. Row tap dispatch is androidx.preference (not on disk). App side: PreferencesActivity.java:19 (implements the callback) and :80. Fix: none.

Step 19 (Ed19f3b08, PreferencesActivity.onPreferenceStartFragment -> SecurityPreferencesFragment.<init>, CALL non_standard, reflection): UNCLEAR. Guard OK: preferences.xml line 26 is the row with android:fragment=...SecurityPreferencesFragment. The constructor call goes through `getFragmentFactory().instantiate(...)` (PreferencesActivity.java:81), an androidx body, not on disk. Fix: none.

Step 20 (E5c8f972e, SecurityPreferencesFragment.<init> -> SecurityPreferencesFragment.onCreatePreferences, LIFECYCLE standard): UNCLEAR. androidx.preference builds the list (not on disk). App side: SecurityPreferencesFragment.java:57 (onCreatePreferences start). Fix: none.

Step 21 (Eb2d49c8f, SecurityPreferencesFragment.onCreatePreferences -> lambda$onCreatePreferences$9, FRAMEWORK standard): UNCLEAR. The change dispatch is androidx.preference (not on disk). Guard OK: SecurityPreferencesFragment.java:153-155 (`if (!(boolean) newValue) { return true; }`), so the body runs only when the switch is turned on. Fix: none.

Step 24 (E5bb67188, Dialogs.showTextInputDialog -> Dialogs.lambda$showTextInputDialog$8, FRAMEWORK standard): UNCLEAR. Printed Dialogs.java:226-229 (setOnShowListener). The dialog is androidx.appcompat.app.AlertDialog (Dialogs.java:30 import); show() running the listener is not on disk. Fix: none.

Step 26 (E02b5fa3e, Dialogs.lambda$showTextInputDialog$7 -> AuthyImporter$EncryptedState.lambda$decrypt$0, CALL non_standard, interface callback):
- ERROR (shared relay reaches the wrong listener for this route). Printed Dialogs.java:231-235: the OK click calls `listener.onTextInputResult(text)` at line 233. That listener is the parameter of showTextInputDialog (line 194), which the caller passes through showPasswordInputDialog (Dialogs.java:270-271). In this route the caller is SecurityPreferencesFragment.java:157, whose listener is the pin-keyboard lambda (SecurityPreferencesFragment.java:158-171). Source says the Authy lambda (AuthyImporter.java:207-214) is the listener only when AuthyImporter$EncryptedState.decrypt (AuthyImporter.java:206-207) opened the dialog. Steps 27-35 are reached only through this edge.
- Fix proposed: the route cannot be fixed by a guard. Replace the prefix (steps 19-25, the pin-keyboard password dialog) with the import path that already exists in the graph: ImportEntriesActivity.processImporterState -> AuthyImporter$EncryptedState.decrypt (edge Ef83e7094; source ImportEntriesActivity.java:179 `state.decrypt(this, ...)`), then AuthyImporter decrypt -> showPasswordInputDialog 4-argument overload (edge E74029e94; AuthyImporter.java:207). That import path needs an encrypted Authy file chosen in the import UI, which is a state the route does not yet name. Also, the edge E02b5fa3e is caller-independent; a variant split of Dialogs.lambda$showTextInputDialog$7 per caller would be needed before any route through the pin-keyboard path can use it.
- Class note: non_standard for TextInputListener calls matches the graph convention (58 CALL edges via an interface listener). Not counted as an error.

Step 27 (E15e02c9d, AuthyImporter$EncryptedState.lambda$decrypt$0 -> ImportEntriesActivity$2.onStateDecrypted, CALL explicit): OK in itself. Printed AuthyImporter.java:206-212: `decrypt(password)` at 209 in try, `listener.onStateDecrypted(state)` at 210, catch at 211-212 calls onError. The guard "decrypt does not throw" has the right sense. Reached only through step 26 (see above). ImportEntriesActivity.java:181-182 confirms the anonymous onStateDecrypted calls processDecryptedImporterState.

Step 32 (E5c7dbe16, Dialogs.showMultiErrorDialog -> Dialogs.lambda$showMultiErrorDialog$20, FRAMEWORK standard): UNCLEAR. Printed Dialogs.java:439-441 (`setNeutralButton(... details ..., (dialog, which) -> { showDetailedMultiErrorDialog(...); })`). The dialog is MaterialAlertDialogBuilder (Dialogs.java:44 import), so the DialogInterface listener is called by the dialog library, not on disk. The cited View.java:6289-6294 covers only the first hop (View click), not the DialogInterface call. Fix: none (library body).

Step 34 (E9e8ecab9, Dialogs.showDetailedMultiErrorDialog -> Dialogs.lambda$showDetailedMultiErrorDialog$23, FRAMEWORK standard): UNCLEAR. Printed Dialogs.java:476-479 (setOnShowListener). The dialog is androidx.appcompat.app.AlertDialog (Dialogs.java:30); show() running the listener is not on disk. Fix: none.

OK steps (21): 1, 4, 5, 6, 7, 9, 11, 12, 14, 15, 17, 22, 23, 25, 27 (in itself), 28, 29, 30, 31, 33, 35.
Checked facts behind them: ActivityThread.java 2729-2731 and 2741 (callActivityOnCreate, performStart); Activity.java 7019 (performStart calls callActivityOnStart); View.java 6289 and 6294 (performClick calls the OnClickListener); AegisApplicationBase.java 45-67; manifest 21-27 and 44-51; MainActivity.java 1133-1144 (loadEntries, `if (!_loaded)`); AegisActivity.java 154-158 (abortIfOrphan returns false on savedInstanceState null); PreferencesActivity.java 26-27 and 40-41; SecurityPreferencesFragment.java 153-177 (steps 21-22); ImportEntriesActivity.java 207-212, 220, 230-231, 245-248; Dialogs.java 440, 452, 477-483 region.

## Route 2: AuthActivity.lambda$onCreate$3

Route verdict: ERROR (text only). Step 8's guard omits two returns that come before the call (MainActivity.java:947 and 960). The route itself is unaffected, and every other step is OK or UNCLEAR as listed.

Steps 1, 4, 5, 6, 7: OK. Same edges and evidence as route 1 (manifest 21-27 and 44-51; AegisApplicationBase.java 45-67; MainActivity.java 193-194 and 938-940; ActivityThread 2729-2731, 2741).

Step 2 (E5b266140, AegisApplication.<init> -> Hilt_AegisApplication.onCreate, LIFECYCLE standard): UNCLEAR. Same as route 1 step 2 (Hilt-generated superclass, not on disk). Fix: none.

Step 3 (E1ef992ce, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate, CALL explicit): UNCLEAR. Same as route 1 step 3 (generated code, not on disk). Fix: none.

Step 8 (E57db524e, MainActivity.onStart -> MainActivity.startAuthActivity, CALL explicit*, STATE):
- ERROR (text-only guard omission; route unaffected). Printed MainActivity.java:942-947 (isVaultInitNeeded() returns at 947), 951-960 (readVaultFile(); the catch returns at 960), 963-973 (plain-text load only when `!vaultFile.isEncrypted()`), 976-977 (`if (!_vaultManager.isVaultLoaded()) startAuthActivity(false);`). The guard "a vault file exists and is encrypted (the plain-text branch at 951-973 did not load it)" has the right sense: an encrypted file is not loaded at 963, so the call at 977 runs. It does not name the return at 947 (no init-needed) or the return at 960 (readVaultFile does not throw), and both must hold before 977 runs. Fix proposed: add "readVaultFile does not throw (MainActivity.java:953-960) and isVaultInitNeeded() is false (MainActivity.java:942-947)" to the guard.
- UNCLEAR (needs earlier run). The STATE is written by an earlier run, so it is not checked here. Producers found: IntroActivity.java:100 (`_vaultManager.initNew(creds)` in onDonePressed, lines 84-106) and SecuritySetupSlide.java:101 (biometric slot initializer). Fix proposed (text only): add the producer cite to needs_state; not added to the route.

Step 9 (E06202b0e, MainActivity.startAuthActivity -> AuthActivity.<init>, INTENT standard*): UNCLEAR. Printed MainActivity.java:1146-1153: the guard `if (!_isAuthenticating)` at 1147 has the right sense (the launch happens only when no unlock screen is running; the flag is set at 1151). The launch goes through authResultLauncher (androidx.activity.result, not on disk). Class standard is the INTENT default (18 of 18 edges, see the method notes). Same pattern as route 1 step 13. Fix: none.

Step 10 (E0158aff6, AuthActivity.<init> -> AuthActivity.onCreate, LIFECYCLE standard*): OK. Same framework claim as route 1 step 6 (ActivityThread.java 2729-2731 and 2741). Source: AuthActivity.java:73-74 (onCreate with super.onCreate). No guard on this edge.

Step 11 (E911809ef, AuthActivity.onCreate -> AuthActivity.onResume, LIFECYCLE standard*): OK. ActivityThread.java:2741 (performStart after callActivityOnCreate), 3556 (`r.activity.performResume()`) and 3621 (`r = performResumeActivity(...)`) are on disk and match. AuthActivity.java:211-212 (onResume calls super.onResume). Note only: AuthActivity and AegisActivity define no onStart (grep: no match), but AegisActivity extends AppCompatActivity (AegisActivity.java:45), so a library onStart runs between the two steps. It is not app code and not on disk, and the edge does not claim otherwise.

Step 12 (E87843ac5, AuthActivity.onResume -> S_AUTH, ENTERS page*): OK. ENTERS page is the convention for these edges (20 of 21). Source: AuthActivity.java:211-224.

Step 13 (E700eadaa, S_AUTH -> AuthActivity.lambda$onCreate$4, GUI standard*, ENV, STATE): UNCLEAR (needs earlier run). Click dispatch on disk: View.java:6289-6294 (performClick calls the OnClickListener). The lambda body matches AuthActivity.java:180-194. Guard OK: readVaultFile must not throw, because the return at AuthActivity.java:127 skips the listener setup at 180; the button is shown at line 150 only when BiometricSlot is present (132), BiometricsHelper.isAvailable is true (132), and the keystore key is found and not null (140-146). ENV (fingerprint or face accepted) is a precondition; the prompt is at AuthActivity.java:270-293. STATE (biometric slot and keystore key from an earlier run): producer SecuritySetupSlide.java:101 (biometric slot initializer), not in this run. Fix: none (text is correct; the state is cross-run).

Step 14 (E552b9e69, AuthActivity.lambda$onCreate$4 -> AuthActivity.lambda$onCreate$3, FRAMEWORK standard*, STATE): UNCLEAR. Source AuthActivity.java:181-190: the dialog is built only when Preferences.isPasswordReminderNeeded() is true (181), and the OK lambda at 187-189 calls showBiometricPrompt(). The first hop (click) is View.java:6289-6294. The second hop (dialog OK click) is delivered by MaterialAlertDialogBuilder (library, not on disk), so it is UNCLEAR. The STATE (reminder due, saved by an earlier run) is checked against Preferences.java:138-146 (NEVER returns false; otherwise the timestamp age is compared with the frequency); its producer is not in this run. Fix: none.

OK steps (8): 1, 4, 5, 6, 7, 10, 11, 12.
Checked facts behind them: AuthActivity.java 73-74, 180-194, 211-224, 270-293; ActivityThread.java 2729-2731, 2741, 3556, 3621; View.java 6289-6294; AegisActivity.java 45 (extends AppCompatActivity), 89-91; MainActivity.java 938-977, 1146-1153; Preferences.java 138-146; IntroActivity.java 84-106; SecuritySetupSlide.java 101.

## Route 3: GoogleAuthImporter.readFromApp

Route verdict: ERROR. Step 24 gives the Import-from-app dialog OK click to the isDirect=true listener, but the route's prefix (steps 21-22) is the `pref_import` row, which calls the dialog with isDirect=false. Steps 25-34 are reached only through step 24.

Steps 1, 4, 5, 6, 7: OK (same as route 1). Steps 2, 3: UNCLEAR (same as route 1).

Step 8 (E20e76e09, MainActivity.onStart -> MainActivity.loadEntries, CALL explicit*, STATE): UNCLEAR (needs earlier run). The guard is complete: it names the returns at 947, 960 and 971, the isVaultLoaded() branch at 976-977, and the `_loaded` branch at 978 and 991-992; it matches MainActivity.java:942-992. The STATE is written by an earlier run that chose no security; producer IntroActivity.java:92-100 (creds null, `initNew(creds)` at 100). Fix (text only): add the producer cite; not added.

Step 9 (E1ffae3d8, MainActivity.loadEntries -> S_LIST, ENTERS page*): OK. Guard `if (!_loaded)` at MainActivity.java:1134 (loadEntries 1133-1144). ENTERS page is the convention.

Step 10 (E887b87bf, S_LIST -> MainActivity.onOptionsItemSelected, GUI standard*): UNCLEAR. The toolbar dispatch is androidx.appcompat (not on disk). App side: MainActivity.java:1086-1089. Same as route 1 step 10.

Step 11 (Ef4e32054, onOptionsItemSelected -> startPreferencesActivity(), CALL explicit*): OK. Guard is the action_settings branch at 1088-1089.

Step 12 (Ef64f95ee, startPreferencesActivity() -> startPreferencesActivity(Class,String), CALL explicit*): OK. MainActivity.java:827 has the call; the evidence label "(bytecode)" is not checked, the .java line is.

Step 13 (E640fb9eb, startPreferencesActivity(Class,String) -> PreferencesActivity.<init>, INTENT standard*): UNCLEAR. The launch is `preferenceResultLauncher.launch(intent)` (MainActivity.java:834), an androidx.activity.result dispatch (not on disk). Same as route 1 step 13.

Step 14 (E94201299, PreferencesActivity.<init> -> onCreate, LIFECYCLE standard*): OK. Same as route 1 step 14 (PreferencesActivity.java:24).

Step 15 (E50e3cfda, PreferencesActivity.onCreate -> MainPreferencesFragment.<init>, CALL explicit*): OK. Guard: abortIfOrphan false (PreferencesActivity.java:26-27) and savedInstanceState null (line 40); source matches.

Step 16 (E382bc001, MainPreferencesFragment.<init> -> onCreatePreferences, LIFECYCLE standard*): UNCLEAR. androidx.fragment and androidx.preference build the list (not on disk). App side: MainPreferencesFragment.java:9-11. Same as route 1 step 16.

Step 17 (Eccc3a740, onCreatePreferences -> S_SETTINGS_MAIN, ENTERS page*): OK. MainPreferencesFragment.java:10 (addPreferencesFromResource) and preferences.xml rows.

Step 18 (E3452b602, S_SETTINGS_MAIN -> PreferencesActivity.onPreferenceStartFragment, GUI standard*): UNCLEAR. Row tap dispatch is androidx.preference (not on disk). App side: PreferencesActivity.java:19, 80-84. Same as route 1 step 18.

Step 19 (E63d9f2a4, PreferencesActivity.onPreferenceStartFragment -> ImportExportPreferencesFragment.<init>, CALL non_standard, reflection): UNCLEAR. Guard OK: preferences.xml:38 is the row with android:fragment=ImportExportPreferencesFragment. The constructor is created by `getFragmentFactory().instantiate(...)` (PreferencesActivity.java:81), an androidx body (not on disk). Same as route 1 step 19.

Step 20 (E245f8b40, ImportExportPreferencesFragment.<init> -> onCreatePreferences, LIFECYCLE standard*): UNCLEAR. androidx.preference builds the list (not on disk). App side: ImportExportPreferencesFragment.java:98. Same as route 1 step 20.

Step 21 (E91eeed07, ImportExportPreferencesFragment.onCreatePreferences -> lambda$onCreatePreferences$6, FRAMEWORK standard*): UNCLEAR. The tap dispatch is androidx.preference (not on disk). App side: ImportExportPreferencesFragment.java:105-106 is the `pref_import` listener (isDirect=false path). The edge is right for "tap Import", but the route's later steps need the `pref_import_app` row (see step 24).

Step 22 (E5c464116, lambda$onCreatePreferences$6 -> Dialogs.showImportersDialog, CALL explicit*): OK in itself. ImportExportPreferencesFragment.java:107 calls `Dialogs.showImportersDialog(requireContext(), false, ...)`. Reached only through the isDirect=false caller; see step 24.

Step 23 (Ebe22842e, Dialogs.showImportersDialog -> Dialogs.lambda$showImportersDialog$27, FRAMEWORK standard*): UNCLEAR. The dialog is MaterialAlertDialogBuilder (Dialogs.java:533; library, not on disk), so the OK button dispatch is not on disk. The OK lambda source is Dialogs.java:536-538. Same pattern as route 1 step 32.

Step 24 (E72c20578, Dialogs.lambda$showImportersDialog$27 -> ImportExportPreferencesFragment.lambda$onCreatePreferences$7, CALL explicit*, guard isDirect true at ImportExportPreferencesFragment.java:119):
- ERROR (shared relay reaches the wrong listener for this route). Dialogs.java:537 calls `listener.onImporterSelectionResult(...)`, and `listener` is the parameter passed by the caller. In this route the caller is step 22 (ImportExportPreferencesFragment.java:107, isDirect=false), so the listener is the lambda at 107-113 (sets `_importerDef` and fires ACTION_GET_CONTENT), graph node lambda$onCreatePreferences$5 (edge E3fba437f). E72c20578 is the listener only for the caller at line 119 (isDirect=true). Its guard is correct for that caller and contradicts step 22.
- Fix from the graph: replace steps 21-22 with the `pref_import_app` row. Step 21 becomes Eda9f6e40 (onCreatePreferences -> lambda$onCreatePreferences$8, FRAMEWORK; UNCLEAR like step 21). Step 22 becomes E2a3becb9 (lambda$onCreatePreferences$8 -> Dialogs.showImportersDialog with `true`, ImportExportPreferencesFragment.java:119, CALL explicit; OK). With that prefix, step 24 is correct and the rest of the route is as printed. E3fba437f leads to fireIntentLauncher (file picker), not to readFromApp, so the pref_import prefix cannot reach GoogleAuthImporter.readFromApp.
- Class note: the importer relay calls are explicit (E72c20578, E3fba437f), while route 1 TextInputListener calls are non_standard. The brief gives no rule that separates them, so this is noted and not counted.

Step 25 (Eca2b28fb, lambda$onCreatePreferences$7 -> startImportEntriesActivity, CALL explicit*): OK in itself. ImportExportPreferencesFragment.java:119-120 calls `startImportEntriesActivity(definition, null)`. Reached only through step 24.

Step 26 (E3156c24c, startImportEntriesActivity -> ImportEntriesActivity.<init>, INTENT standard*): OK. ImportExportPreferencesFragment.java:161-165 builds the intent with the importerDef and file extras and calls `startActivity` directly (not a launcher). ImportEntriesActivity.java:103-104 reads the extras. The framework launch is standard, unlike step 13.

Step 27 (Ef8499dba, ImportEntriesActivity.<init> -> onCreate, LIFECYCLE standard*): OK. Same claim as route 1 step 6; ImportEntriesActivity.java:62-63.

Step 28 (E411f08d7, ImportEntriesActivity.onCreate -> startImport, CALL explicit*): OK. Guard: abortIfOrphan false (ImportEntriesActivity.java:64-66; AegisActivity.java:154-157). The method returns false when savedInstanceState is null, so the cold start passes. The call at line 104 is inside onCreate (closed at 105).

Step 29 (E7faea19a, ImportEntriesActivity.startImport -> lambda$startImport$1, FRAMEWORK standard*): UNCLEAR. Guard OK: the warning is the else branch of `importer.isInstalledAppVersionSupported()` (ImportEntriesActivity.java:110-113). The Yes click is dispatched by MaterialAlertDialogBuilder (library, not on disk), same as route 1 step 32. The route covers only this warning branch; the supported branch (line 111) calls startImportApp directly and is not part of this route.

Step 30 (Ee1e1ad6c, lambda$startImport$1 -> startImportApp, CALL explicit*): OK. ImportEntriesActivity.java:119.

Step 31 (Ecf27001f, ImportEntriesActivity.startImportApp -> RootShellTask.doInBackground, ASYNC standard*): OK. ImportEntriesActivity.java:173 `task.execute(this)` resolves to AsyncTask.execute(Params...): RootShellTask extends ProgressDialogTask (RootShellTask.java:8), whose execute takes a Lifecycle first (ProgressDialogTask.java:69), and `this` is an Activity, not a Lifecycle. Framework source (read directly, fw_src AsyncTask.java): execute 594-595; executeOnExecutor 632-650; worker call with doInBackground at 333; postResult in finally at 339, postResult body 369-374. Cited lines match.

Step 32 (E1de399e4, RootShellTask.doInBackground -> RootShellTask.onPostExecute, ASYNC standard*): OK. Framework path: postResult -> handleMessage (705-713) -> finish (691-697) -> onPostExecute at 695. RootShellTask.java:23-25 (super call, then `_cb.onTaskFinished(shell)`).

Step 33 (Efb3b152a, RootShellTask.onPostExecute -> ImportEntriesActivity.lambda$startImportApp$5, CALL explicit*): OK. `_cb` (RootShellTask.java:25) is the lambda passed at ImportEntriesActivity.java:144 in startImportApp; the per-instance callback is correct for this route. The lambda number is a build name.

Step 34 (Ee74cd64a, lambda$startImportApp$5 -> GoogleAuthImporter.readFromApp, CALL explicit*, ENV root): OK. ImportEntriesActivity.java:156 is a virtual call on `importer`, which is GoogleAuthImporter only when the chosen definition is Google (the route's guard says so). GoogleAuthImporter.java:60-68 is the readFromApp body (getAppPath, helper read of "accounts"). Guard lines 145-153 match; ENV is the root check at 149-153 and RootShellTask.java:17-20.

Notes: the evidence labels "SRC ... (bytecode)" on the CALL edges (steps 12, 22, 25, 30) cite .java lines, and those lines were checked. Steps 24-34 use the same source.

OK steps (21): 1, 4, 5, 6, 7, 9, 11, 12, 14, 15, 17, 22, 25, 26, 27, 28, 30, 31, 32, 33, 34.
UNCLEAR steps (12, including step 8's state): 2, 3, 8, 10, 13, 16, 18, 19, 20, 21, 23, 29.
ERROR: 24.

## Route 4: ImportExportPreferencesFragment.lambda$onImportSelectResult$11

Route verdict: ERROR (text only). Step 26's guard says the picker must return RESULT_OK with a URI, but the launcher callback (ImportExportPreferencesFragment.java:74-79) checks only data != null (line 76) and calls onImportSelectResult for any result code. The RESULT_OK and URI check is at line 146, which step 28 covers. The route is unaffected.

Steps 1, 4, 5, 6, 7, 9, 11, 12, 14, 15, 17: OK. Same edges and evidence as route 3 (manifest 21-27; AegisApplicationBase.java 45-67; ActivityThread 2729-2731, 2741; MainActivity 938-940 and 991-992; PreferencesActivity 19, 24, 26-27, 40-41, 80-84).

Steps 2, 3: UNCLEAR (Hilt-generated superclass and wrapper, not on disk; same as route 1).

Step 8 (E20e76e09, MainActivity.onStart -> MainActivity.loadEntries, STATE): UNCLEAR (needs earlier run). Guard OK, same text as route 1 step 8 (see the correction there). The plain-text file is written by IntroActivity.java:92-100 (no-security case, initNew(creds) at 100). Producer cite not added to the graph.

Steps 10, 13, 16: UNCLEAR (androidx.appcompat toolbar dispatch, androidx.activity.result launch, androidx.fragment and androidx.preference list build; same as route 3).

Step 18 (E3452b602, S_SETTINGS_MAIN -> PreferencesActivity.onPreferenceStartFragment, GUI): UNCLEAR. Row tap dispatch is androidx.preference (not on disk). App side: PreferencesActivity.java:19, 80-84; preferences.xml:8-44.

Step 19 (E63d9f2a4, PreferencesActivity.onPreferenceStartFragment -> ImportExportPreferencesFragment.<init>, CALL non_standard, reflection): UNCLEAR. Guard OK: preferences.xml:38 is the row with android:fragment=ImportExportPreferencesFragment. The instance is made by getFragmentFactory().instantiate (PreferencesActivity.java:81), an androidx body (not on disk).

Step 20 (E245f8b40, ImportExportPreferencesFragment.<init> -> onCreatePreferences, LIFECYCLE): UNCLEAR. androidx.fragment and androidx.preference build the list (not on disk). App side: ImportExportPreferencesFragment.java:98; PreferencesActivity.java:84, 91-97 (showFragment commit).

Step 21 (E91eeed07, onCreatePreferences -> lambda$onCreatePreferences$6, FRAMEWORK): UNCLEAR. The tap dispatch is androidx.preference (not on disk). App side: ImportExportPreferencesFragment.java:105-106 (pref_import listener). The edge is right for "tap Import".

Step 22 (E5c464116, lambda$onCreatePreferences$6 -> Dialogs.showImportersDialog, CALL explicit): OK. ImportExportPreferencesFragment.java:107 calls showImportersDialog(requireContext(), false, ...).

Step 23 (Ebe22842e, Dialogs.showImportersDialog -> Dialogs.lambda$showImportersDialog$27, FRAMEWORK): UNCLEAR. The OK click is delivered by MaterialAlertDialogBuilder (library, not on disk). Source lambda: Dialogs.java:536-538. View.java:6289-6294 covers only the view click, not the dialog button delivery.

Step 24 (E3fba437f, Dialogs.lambda$showImportersDialog$27 -> ImportExportPreferencesFragment.lambda$onCreatePreferences$5, CALL explicit): OK. Dialogs.java:537 calls listener.onImporterSelectionResult, and the listener passed by this route's caller (step 22, isDirect false, ImportExportPreferencesFragment.java:107) is the lambda at 107-113, which is graph node lambda$onCreatePreferences$5. The edge is correct for this prefix. The relay is shared: the same relay reaches other listeners for other callers (route 3 step 24 is the mirror error). Not counted.

Step 25 (E63f82c4b, lambda$onCreatePreferences$5 -> VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@SETTINGS_IMPORT, CALL explicit): OK. ImportExportPreferencesFragment.java:112 passes `this` (a Fragment), so the Fragment overload at VaultManager.java:263 is called; it runs resultLauncher.launch(intent).

Step 26 (Ebe3b8b81, VaultManager.fireIntentLauncher(Fragment)@SETTINGS_IMPORT -> ImportExportPreferencesFragment.lambda$new$0, RESULT, ENV):
- ERROR (text-only guard; route unaffected). The guard reads "the picker returned RESULT_OK with a URI (onImportSelectResult returns early otherwise, ImportExportPreferencesFragment.java:146-148)". The callback at lines 74-79 checks only data != null (line 76) and runs for any result code. The RESULT_OK and URI check is on step 28's path (146-148). Fix: replace the guard with "none on this edge (the callback runs for any result code; data != null is checked at ImportExportPreferencesFragment.java:76, step 27; RESULT_OK and URI are checked at 146, step 28)". The delivery to the callback is androidx.activity.result (not on disk), so the verdict rests on the guard text only.

Step 27 (E36289880, lambda$new$0 -> onImportSelectResult, CALL explicit): OK. ImportExportPreferencesFragment.java:76-77 has the right guard (data != null); onImportSelectResult(int, Intent) is at 144.

Step 28 (E4770a1db, onImportSelectResult -> ImportFileTask.doInBackground, ASYNC): OK. Guard lines 146-148 (return when resultCode != RESULT_OK or uri == null) match. Line 158 task.execute(getLifecycle(), params) -> ProgressDialogTask.execute(Lifecycle, Params...) (ProgressDialogTask.java:69-74) -> AsyncTask.execute (fw_src AsyncTask.java 594-595) -> executeOnExecutor (632-650) -> doInBackground on the worker thread (333). ImportFileTask.java:27 is the doInBackground.

Step 29 (Ead311677, ImportFileTask.doInBackground -> ImportFileTask.onPostExecute, ASYNC): OK. doInBackground returns a Result on every path (ImportFileTask.java:45 and 48). The framework posts the result (AsyncTask.java 369-374), handles it on the main thread (705-713), and calls onPostExecute from finish (691-697, call at 695). ImportFileTask.java:53-56 calls super, then _cb.onTaskFinished. ProgressDialogTask's lifecycle observer only dismisses the dialog on ON_PAUSE (ProgressDialogTask.java:80-100) and does not cancel the task. Same framework path as route 3 step 32 (OK there).

Step 30 (Ed10f6640, ImportFileTask.onPostExecute -> lambda$onImportSelectResult$11, CALL explicit, STATE set inside the route): OK. ImportFileTask.java:55 is unconditional. The callback (ImportExportPreferencesFragment.java:151-157) opens the import page when result.getError() == null (152-153) and shows the read error otherwise (155). The STATE (an import task started by steps 26-28) is produced inside this route, so it is not cross-run.

Route 4 counts: OK 18 (1, 4, 5, 6, 7, 9, 11, 12, 14, 15, 17, 22, 24, 25, 27, 28, 29, 30); UNCLEAR 11 (2, 3, 8, 10, 13, 16, 18, 19, 20, 21, 23); ERROR 1 (26).

## Route 5: DaggerAegisApplication_HiltComponents_SingletonC$SingletonCImpl.injectVaultLockReceiver2

Route verdict: no ERROR. Steps 1 and 4 are OK. Steps 2, 3, 5, 6, 7, 8, 9 are UNCLEAR. The route ends in generated Hilt and Dagger code (steps 2-3 and 7-9), and step 6 depends on a build-time superclass that is not in the source.

Step 1 (E14b4e906, S_ENTRY -> AegisApplication.<init>, ENTRY): OK. Manifest 21-27 (android:name=".AegisApplication", backupAgent=".AegisBackupAgent"). Same as route 1 step 1.

Step 2 (E5b266140, AegisApplication.<init> -> Hilt_AegisApplication.onCreate, LIFECYCLE): UNCLEAR. Same as route 1 step 2 (Hilt-generated superclass, not on disk).

Step 3 (E1ef992ce, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate, CALL explicit): UNCLEAR. Generated code, not on disk.

Step 4 (E88ed9829, AegisApplicationBase.onCreate -> S_PROCESS, ENTERS page): OK. AegisApplicationBase.java:45-51 creates `new VaultLockReceiver()` (49) and registers it for ACTION_SCREEN_OFF (50-51).

Step 5 (E313f4f87, S_PROCESS -> VaultLockReceiver.onReceive, SYSTEM, ENV screen off): UNCLEAR. The registration goes through ContextCompat.registerReceiver (AegisApplicationBase.java:51), an androidx.core body not on disk. The ACTION_SCREEN_OFF broadcast is delivered by the system (not on disk). App side: VaultLockReceiver.java:24-34 (filter at 25-29; lock at 31-32 when auto-lock on device lock is set). Fix: none.

Step 6 (E47521e87, VaultLockReceiver.onReceive -> Hilt_VaultLockReceiver.onReceive, CALL explicit, evidence "bytecode"): UNCLEAR. The source does not decide it. VaultLockReceiver.java:16 says `extends BroadcastReceiver`, and onReceive (lines 24-34) has no super.onReceive call. The Hilt_VaultLockReceiver superclass exists only in the build (generated, not on disk), and grep found no javap dump of the class in the work tree. Check needed before this can be OK: javap -c on the built VaultLockReceiver.class, method onReceive, for an invokespecial of Hilt_VaultLockReceiver.onReceive. If the build has no such call, the route does not reach steps 7-9 from the framework call to VaultLockReceiver.onReceive. Fix: none from source.

Step 7 (Ef238aaad, Hilt_VaultLockReceiver.onReceive -> Hilt_VaultLockReceiver.inject, CALL explicit): UNCLEAR. Generated code, not on disk (build class line 27 per the graph's evidence).

Step 8 (E4e6415e1, Hilt_VaultLockReceiver.inject -> DaggerAegisApplication_HiltComponents_SingletonC$SingletonCImpl.injectVaultLockReceiver, CALL explicit): UNCLEAR. Generated code, not on disk. The dispatch to the component implementation is Hilt-generated. The field being filled is VaultLockReceiver.java:20-21 (`@Inject protected VaultManager _vaultManager;`).

Step 9 (E421cdc72, injectVaultLockReceiver -> injectVaultLockReceiver2, CALL explicit): UNCLEAR. Dagger-generated component code (DaggerAegisApplication_HiltComponents_SingletonC.java, build line 583) is not on disk. The field injection of _vaultManager is inside it. Fix: none.

Route 5 counts: OK 2 (1, 4); UNCLEAR 7 (2, 3, 5, 6, 7, 8, 9); ERROR 0.

## Totals

Primary verdict per step (route 2 step 8 is ERROR and also needs an earlier run, so it counts once, as ERROR).

| Route | Steps | ERROR | UNCLEAR | OK |
|---|---|---|---|---|
| 1 | 35 | 1 (26) | 13 | 21 |
| 2 | 14 | 1 (8) | 5 (2, 3, 9, 13, 14) | 8 |
| 3 | 34 | 1 (24) | 12 | 21 |
| 4 | 30 | 1 (26) | 11 | 18 |
| 5 | 9 | 0 | 7 | 2 |
| Total | 122 | 4 | 48 | 70 |
