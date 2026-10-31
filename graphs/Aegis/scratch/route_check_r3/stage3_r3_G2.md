# Stage 3 route check R3-G2 (Aegis schema 2, round 3, read-only)

Date: 2026-10-27. Sources: graph_def.py (edge text, guard, needs_state, env, helper constants), show_route.py output (steps 1-18 of route 1), Aegis source under final_java_only/Aegis/app/Aegis-#v3.4.2/app/src/main/java/com/beemdevelopment/aegis/, AOSP fw_src/android-8.1.0_r1. Line numbers were confirmed with sed -n or grep -n.

Tool note: show_route.py crashed on a citation with a comma and a space ("SRC ui/ScannerActivity.java:217-219, 226-227", route 1 step 18). Steps after the crash were read from graph_def.py. Framework refs printed as "not found in the source tree" by the tool; the framework lines were checked with sed.

## Summary

| Route | Target | Steps | ERROR steps | UNCLEAR steps | OK steps (count) |
|---|---|---|---|---|---|
| 1 | MainActivity.onScanResult | 20 | 8, 12, 15 | 2, 3, 11, 14, 19 | 12 |
| 2 | ImportExportPreferencesFragment$ExportResultListener.onTaskFinished | 55 | 12, 24, 27, 30, 52, 55 | 2, 3, 9, 14, 22, 29, 33, 36, 39, 41, 43, 44, 46, 49 | 35 |
| 3 | GoogleAuthProtos$MigrationPayload$DigitCount$DigitCountVerifier.<init> | 32 | 8, 26, 28, 29, 30 | 2, 3, 10, 13, 16, 18, 20, 21, 23, 31, 32 | 16 |
| 4 | IconPackExistsException.getIconPack | 30 | 8, 15, 28 | 2, 3, 10, 13, 16, 18, 20, 24, 29 | 18 |
| 5 | VaultGroup.equals | 28 | 8, 15, 24, 28 | 2, 3, 10, 13, 16, 18, 20, 21, 25, 27 | 14 |

Totals: 5 routes, 165 steps; ERROR 21; UNCLEAR 49; OK 95.

## Route 1: MainActivity.onScanResult

Route chain: S_ENTRY -> AegisApplication.<init> -> Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate -> S_PROCESS -> MainActivity.<init> -> onCreate -> onStart -> Dialogs.showErrorDialog (vault read error) -> OK relay -> ScannerActivity listener -> bindPreview -> analyze -> onQrCodeDetected -> handleExportUri -> ScannerActivity.finish -> MainActivity.lambda$new$2 -> onScanResult.

Step 1 (E14b4e906, S_ENTRY -> AegisApplication.<init>): OK. AndroidManifest.xml:22 android:name=".AegisApplication".

Step 2 (E5b266140, AegisApplication.<init> -> Hilt_AegisApplication.onCreate): UNCLEAR. Printed: AegisApplication.java:6 `public class AegisApplication extends AegisApplicationBase {` (no onCreate); FW ActivityThread.java:5740 `mInstrumentation.callApplicationOnCreate(app);`. Source says: the framework call at 5740 holds. The Hilt_AegisApplication superclass is generated code not on disk (INFERRED), so its body is UNCLEAR. Fix proposed: none (the framework part is correct; the Hilt body is outside the source tree).

Step 3 (E1ef992ce, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate): UNCLEAR. The edge cites "the build class, line 43", which is not on disk and could not be printed. Hilt generated body. Fix proposed: none.

Step 4 (E88ed9829, AegisApplicationBase.onCreate -> S_PROCESS): OK. AegisApplicationBase.java:45-67 has no return before the state entry.

Step 5 (E28ffc58c, S_PROCESS -> MainActivity.<init>): OK. AndroidManifest.xml:44-51 (`.ui.MainActivity`, MAIN, LAUNCHER).

Step 6 (Eb76444fd, MainActivity.<init> -> MainActivity.onCreate): OK. FW ActivityThread.java:2729-2731 (callActivityOnCreate) and 2741 (activity.performStart(), checked with grep -n).

Step 7 (E3a06baed, MainActivity.onCreate -> MainActivity.onStart): OK. FW Activity.java:7014-7019 (performStart calls mInstrumentation.callActivityOnStart(this), line 7019).

Step 8 (E1fac164d, MainActivity.onStart -> Dialogs.showErrorDialog(Context,int,Exception,OnClickListener)): ERROR (guard incomplete). Printed: MainActivity.java:942-947 `if (_vaultManager.isVaultInitNeeded()) { ... startIntroActivity(); return; }`; 951 `if (!_vaultManager.isVaultLoaded()) {`; 954-955 try and readVaultFile; 957-960 showErrorDialog, then `return;`. Source says: the call is reached only when isVaultInitNeeded() is false (942) and isVaultLoaded() is false (951). The guard text lists only the catch. Fix proposed: add to the guard text "isVaultInitNeeded() is false (MainActivity.java:942-947) and isVaultLoaded() is false (MainActivity.java:951)". STATE (ST_VAULT_UNREADABLE): this is a cross-run state. Its text names the read line (954-955) but not the line that writes the vault file, so it is UNCLEAR, reason "needs earlier run" (not an invented producer).

Step 9 (Ec4596530, showErrorDialog(Context,int,Exception,...) -> showErrorDialog(Context,int,CharSequence,...)): OK. Dialogs.java:368 `showErrorDialog(context, message, e.toString(), listener);`.

Step 10 (Eff284e41, showErrorDialog(Context,int,CharSequence,...) -> showErrorDialog(Context,String,CharSequence,...)): OK. Dialogs.java:376 `showErrorDialog(context, context.getString(message), error, listener);`.

Step 11 (Ef2c4b2cc, showErrorDialog(Context,String,CharSequence,...) -> Dialogs.lambda$showErrorDialog$15): UNCLEAR. Printed: Dialogs.java:391-395 `.setPositiveButton(android.R.string.ok, (dialog1, which) -> { if (listener != null) { listener.onClick(dialog1, which); } })`; FW View.java:6289-6296 performClick calls li.mOnClickListener.onClick(this). Source says: the OK button is wired inside the AppCompat/Material AlertDialog (not on disk). The cited View.performClick shows only the generic click path. Fix proposed: none (INFERRED library link; keep as UNCLEAR).

Step 12 (Ec9aba117, Dialogs.lambda$showErrorDialog$15 -> ScannerActivity.lambda$onQrCodeDetected$1; STATE ST_CAMERA_READY): ERROR (wrong route join). Printed: Dialogs.java:391-395 (the relay calls whatever listener the caller passed); MainActivity.java:957-959 (step 8's dialog passes `(dialog, which) -> { finish(); }`); ScannerActivity.java:194-196 (the scanner's listener is `bindPreview(_cameraProvider)`). Source says: the OK relay is shared, and this route reaches it from the vault-read dialog, whose OK calls MainActivity's finish(). The scanner listener cannot run after step 8. Also: (a) no step on this route opens ScannerActivity (no edge into ScannerActivity.<init>/onCreate), so ST_CAMERA_READY (ScannerActivity.java:70, 79-88, set only by the scanner's camera listener) is never produced here; (b) the guard text omits the `listener != null` check (Dialogs.java:392). Fix proposed: a variant split of the shared OK relay per opener. The vault-read dialog's OK must go to the MainActivity lambda at MainActivity.java:957-959 (finish), and the scanner listener edge must come only from the scanner's error dialog, which needs a ScannerActivity start on the route.

Step 13 (E268ab4ba, ScannerActivity.lambda$onQrCodeDetected$1 -> ScannerActivity.bindPreview): OK as an edge (ScannerActivity.java:196 calls bindPreview). Reachable only through step 12, which fails.

Step 14 (Ed8457530, ScannerActivity.bindPreview -> QrCodeAnalyzer.analyze): UNCLEAR. Printed: ScannerActivity.java:164 `_analysis.setAnalyzer(_executor, new QrCodeAnalyzer(this));`; QrCodeAnalyzer.java:29 `public void analyze(@NonNull ImageProxy image)`. Source says: setAnalyzer stores the analyzer; the call from CameraX into analyze is an androidx.camera body (not on disk). Fix proposed: none (INFERRED per rule).

Step 15 (Ece1825c9, QrCodeAnalyzer.analyze -> ScannerActivity.onQrCodeDetected; non_standard): ERROR (class). QrCodeAnalyzer.java:31-34 (format check returns), 55-58 (decode, then `if (_listener != null)` and the listener call), 59 (catch NotFoundException). Guard text matches. Class: the listener is an app-defined interface (QrCodeAnalyzer.Listener) called by app code, which is explicit by the class rule, not non_standard. Fix: relabel the edge to explicit.

Step 16 (Ede72ed30, ScannerActivity.onQrCodeDetected -> lambda$onQrCodeDetected$2): OK. ScannerActivity.java:176 `new Handler(getMainLooper()).post(...)`; FW Handler.java:355-357 `post(Runnable r) { return sendMessageDelayed(getPostMessage(r), 0); }`.

Step 17 (Ec386f776, lambda$onQrCodeDetected$2 -> ScannerActivity.handleExportUri): OK. ScannerActivity.java:177-179 (`if (isFinishing()) return;`), 181 (`if (_analysis != null)`), 184-185 (export scheme check, call). Guard text matches.

Step 18 (E146f71d1, ScannerActivity.handleExportUri -> ScannerActivity.finish): OK. ScannerActivity.java:212-213 (batch id set, _batchId starts at 0, line 48), 217 (`if (_batchId != export.getBatchId())`, else branch), 219 (`_batchIndex == -1 || _batchIndex == batchIndex - 1`; _batchIndex starts at -1, line 49), 226-227 (`if (_batchIndex + 1 == export.getBatchSize()) finish(_entries);`). Guard text matches. Read manually (tool crashed on this cite).

Step 19 (ScannerActivity.finish -> MainActivity.lambda$new$2, RESULT; graph_def.py:1128, edge id not printed): UNCLEAR. Printed: ScannerActivity.java:239-240 `setResult(RESULT_OK, intent); finish();`; FW ActivityThread.java:4253-4265 deliverResults -> r.activity.dispatchActivityResult(...); MainActivity.java:151-155 (registerForActivityResult callback). Source says: the framework part holds, but the step from dispatchActivityResult to the launcher callback runs in androidx.activity.result (not on disk; the graph's own FW_LAUNCHER note is INFERRED). Fix proposed: none. Note: the edge has no guard field; the RESULT_OK check is on edge step 20 (see below).

Step 20 (MainActivity.lambda$new$2 -> MainActivity.onScanResult, graph_def.py:1162, edge id not printed): OK. MainActivity.java:152-155 (`if (getResultCode() != RESULT_OK || getData() == null) return;`, then `onScanResult(...)`). Guard text matches.

Route 1 result: FAIL at step 12. Steps 13-20 are edge-correct but cannot follow a cold start on this route, because the route never starts ScannerActivity and step 8's dialog cannot reach the scanner listener.

Route 1 counts: 20 steps; ERROR 3 (8, 12, 15); UNCLEAR 5 (2, 3, 11, 14, 19); OK 12.

## Route 2: ImportExportPreferencesFragment$ExportResultListener.onTaskFinished

Route chain: S_ENTRY -> AegisApplication -> MainActivity.onStart (vault init needed) -> IntroActivity -> WelcomeSlide import (picker, ImportFileTask) -> AegisImporter password dialog -> [wrong join at step 24] -> SecurityPreferencesFragment listener -> PasswordSlotDecryptTask -> [wrong target at step 27] -> AuthActivity.finish -> MainActivity.onDecryptResult -> loadEntries -> MainActivity settings -> PreferencesActivity -> ImportExportPreferencesFragment -> export dialog -> document creator -> onExportResult -> ExportTask -> ExportResultListener.onTaskFinished.

Steps 1-55 (verdict, then reason):

1. OK. AndroidManifest.xml:21-27.
2. UNCLEAR. Hilt-generated superclass not on disk; FW ActivityThread.java:5740 holds.
3. UNCLEAR. Hilt-generated body, not on disk.
4. OK. AegisApplicationBase.java:45-67.
5. OK. AndroidManifest.xml:44-51.
6. OK. FW ActivityThread.java:2729-2731, 2741; MainActivity.java:192-194.
7. OK. FW Activity.java:7014-7019; MainActivity.java:938-940.
8. OK. MainActivity.java:942-948 (guard matches). Note: VaultManager.java:226-227 isVaultInitNeeded also requires !isVaultLoaded(); the guard text says only "no vault file exists", which is a description gap, not a missing if.
9. UNCLEAR. introResultLauncher.launch (MainActivity.java:606) runs through androidx.activity.result (body not on disk); the framework start is not cited.
10. OK. IntroActivity.java:35-41; FW 2729-2731, 2741.
11. OK. IntroActivity.java:38-41.
12. ERROR (guard incomplete). IntroBaseActivity.java:175-176 throws if the slide type is already in _slides; the step runs only when that throw is not taken. Fix: add to the guard "WelcomeSlide not already in _slides (IntroBaseActivity.java:175-176 throws otherwise)". No ENV change proposed; the fresh-install condition is carried by step 8.
13. OK. ENV tag present. View.java:6289-6296 (performClick); WelcomeSlide.java:43-47.
14. UNCLEAR. The result is delivered by the androidx launcher (WelcomeSlide.java:32-38); body not on disk. Same as route 1 step 19.
15. OK. WelcomeSlide.java:35-37 (guard `data != null && data.getData() != null` matches; the if is inside the callback body).
16. OK. AsyncTask.java:594-595 (execute), 632-650 (executeOnExecutor), 326-339 (doInBackground call at 333); ProgressDialogTask.java:69-74; ImportFileTask.java:27.
17. OK. AsyncTask.java:691-697 (finish calls onPostExecute at 695), 705-713 (handleMessage calls finish at 712); ImportFileTask.java:53-56.
18. OK. Explicit: ImportFileTask.java:53-56 calls _cb.onTaskFinished; WelcomeSlide.java:59-69 is the lambda.
19. OK. Guard lines WelcomeSlide.java:60-63 (error return) and 68 (isEncrypted); AegisImporter.java:88-90.
20. OK. AegisImporter.java:88-90 (decrypt(Context, DecryptListener) calls showPasswordInputDialog at 90).
21. OK. Dialogs.java:271 (bytecode) calls showTextInputDialog.
22. UNCLEAR. The OnShowListener is run by AppCompat AlertDialog.show() (body not on disk); show call at Dialogs.java:239 is not cited. Dialogs.java:226-229 is verified.
23. OK. Dialogs.java:231-235 (OK click) via FW View.java:6289-6296; guard "text not empty" matches Dialogs.java:203 (watcher enables OK when text is non-empty).
24. ERROR (wrong join, and class). Dialogs.java:233 calls whatever TextInputListener the caller passed. Step 20's caller passed the lambda at AegisImporter.java:90, not the SecurityPreferencesFragment lambda at SecurityPreferencesFragment.java:157, so this edge joins two different dialogs. Also labelled non_standard but Dialogs.TextInputListener (Dialogs.java:647) is app-defined and called by app code, so class should be explicit. Fix: the edge source must be AegisImporter.java:90 lambda (its body creates PasswordSlotDecryptTask at line 93 with its own callback), labelled explicit.
25. OK as an edge. SecurityPreferencesFragment.java:157-162 (guard `isDigitsOnly` at 158), PasswordSlotDecryptTask.java:27. Reached on this route only through the step-24 wrong join.
26. OK. AsyncTask.java:691-697; PasswordSlotDecryptTask.java:27, 87-90.
27. ERROR (wrong target). PasswordSlotDecryptTask is constructed at SecurityPreferencesFragment.java:161 with `new PasswordConfirmationListener()`, so onPostExecute (PasswordSlotDecryptTask.java:87-90) calls SecurityPreferencesFragment.PasswordConfirmationListener (SecurityPreferencesFragment.java:450), not AuthActivity$PasswordDerivationListener (AuthActivity.java:343). Fix: target SecurityPreferencesFragment$PasswordConfirmationListener.onTaskFinished, explicit.
28. OK as an edge (AuthActivity.java:345-356, guard `result != null` at 346). Not reached on this route: its caller is the wrong target at step 27.
29. UNCLEAR. androidx.activity.result hop not on disk (same as route 1 step 19). Framework verified: ActivityThread.java:4253-4265 (deliverResults), Activity.java:5526-5527 (finish). AuthActivity is never started on this route; the only start is startAuthActivity at MainActivity.java:1148-1150, which the route does not reach.
30. ERROR (guard missing). MainActivity.java:137 `if (activityResult.getResultCode() == RESULT_OK)` encloses the call at 138, but the edge has no guard. Fix: guard "activityResult.getResultCode() == RESULT_OK (MainActivity.java:137)".
31. OK. MainActivity.java:797-801.
32. OK. Guard `!_loaded` at MainActivity.java:1134 matches; ENTERS at 1135-1142.
33. UNCLEAR. AppCompat/Toolbar dispatches the menu tap to onOptionsItemSelected (AppCompat body not on disk). MainActivity.java:1086-1099 verified.
34. OK. MainActivity.java:1088-1089 (guard matches).
35. OK. MainActivity.java:827 (bytecode).
36. UNCLEAR. preferenceResultLauncher.launch (MainActivity.java:834) runs through androidx.activity.result (body not on disk); the framework start is not cited. Same as step 9.
37. OK. FW ActivityThread.java:2729-2731, 2741; PreferencesActivity.java:24.
38. OK. Guard `savedInstanceState == null` at PreferencesActivity.java:40 matches; 41 creates the fragment.
39. UNCLEAR. The list is built by the androidx PreferenceFragmentCompat (body not on disk).
40. OK. The state is entered by the app's call addPreferencesFromResource(R.xml.preferences) at MainPreferencesFragment.java:10. The on-screen render is androidx (see step 39).
41. UNCLEAR. A row tap is dispatched by androidx Preference/PreferenceFragmentCompat (body not on disk); PreferencesActivity.java:80-84 verified.
42. OK. Non_standard is correct: reflection through FragmentFactory.instantiate (PreferencesActivity.java:81); preferences.xml:38 names ImportExportPreferencesFragment.
43. UNCLEAR. Fragment commit and attach run in androidx.fragment (body not on disk). PreferencesActivity.java:84, 91-97 verified.
44. UNCLEAR. The export row tap is dispatched by androidx Preference (body not on disk); ImportExportPreferencesFragment.java:125-129 verified.
45. OK. ImportExportPreferencesFragment.java:127.
46. UNCLEAR. AppCompat AlertDialog.show() runs the OnShowListener (body not on disk); ImportExportPreferencesFragment.java:201-209, 332 verified.
47. OK. The OK click is a View click (FW View.java:6289-6296). The guard text (Encrypt or accept ticked; all groups or a group chosen) is the set of returns at lines 255-257 and 259-264. It is placed on the entry edge, but the handler entry itself is unconditional; the guard covers the path to step 48, so no ERROR.
48. OK. ImportExportPreferencesFragment.java:276-277 (launcher chosen by getExportRequestLauncher at 276, then fireIntentLauncher call at 277). The path conditions are the step-47 guard.
49. UNCLEAR. The result is delivered by androidx.activity.result to the launcher callback (ImportExportPreferencesFragment.java:81-83); body not on disk. The guard (Aegis format with encryption, :403-405) is on the launcher choice at 275, which is correct.
50. OK. ImportExportPreferencesFragment.java:83 (bytecode).
51. OK. Guard: data null (506-508) and resultCode != RESULT_OK or uri null (510-512). Both returns match.
52. ERROR (class). StartExportCallback (ImportExportPreferencesFragment.java:569) is app-defined and called by app code (startExportVault at 446). That is explicit by the class rule, but it is labelled non_standard. Fix: relabel to explicit. Guard (444-445) matches.
53. OK. ImportExportPreferencesFragment.java:535 (execute after the catch at 521-524 returns, so the path is skipped on error); ExportTask.java:24; ProgressDialogTask.java:69-74; AsyncTask.java:326-339, 594-595, 632-650 (verified).
54. OK. AsyncTask.java:691-697 (finish; cancelled path calls onCancelled instead); ExportTask.java:43-45.
55. ERROR (class). ExportTask.Callback (ExportTask.java:66) is app-defined and called by app code (ExportTask.java:45). That is explicit by the class rule, but it is labelled non_standard. Fix: relabel to explicit. Target and guard match ImportExportPreferencesFragment.java:550-563.

Route 2 result: FAIL at step 12 (early-throw guard), then the wrong joins at steps 24 and 27. Steps 28-31 belong to AuthActivity, which the route does not start, so they cannot run on this path. Steps 32-55 are edge-correct after the vault is loaded, except steps 30 and 52, 55.

Route 2 counts: 55 steps; ERROR 6 (12, 24, 27, 30, 52, 55); UNCLEAR 14 (2, 3, 9, 14, 22, 29, 33, 36, 39, 41, 43, 44, 46, 49); OK 35.

Tool notes for route 2: the FW-SRC lookup reported "core/java/... not found in the source tree" for AsyncTask.java, Activity.java and View.java, although the files exist under fw_src/android-8.1.0_r1/core/java/...; the tool's framework root is wrong. I read those lines with sed (AsyncTask 326-339, 369-374, 594-595, 632-650, 691-697, 705-713; Activity 5520-5530; View 6289-6296). The tool printed no "guard:" line for step 30, so its guard was checked from source.

## Route 3: GoogleAuthProtos$MigrationPayload$DigitCount$DigitCountVerifier.<init>

Route chain: S_ENTRY -> AegisApplication -> MainActivity.onStart (plain-text vault) -> loadEntries -> S_LIST -> Settings -> PreferencesActivity -> ImportExportPreferencesFragment -> Google Authenticator export -> TransferEntriesActivity -> generateQR -> GoogleAuthInfo$Export.getUri -> protobuf payload -> DigitCountVerifier.<clinit> -> <init>.

Steps 1-32 (verdict, then reason):

1. OK. AndroidManifest.xml:21-27.
2. UNCLEAR. Hilt-generated superclass not on disk; FW ActivityThread.java:5740 holds. Same as route 2 step 2.
3. UNCLEAR. Hilt-generated body, not on disk.
4. OK. AegisApplicationBase.java:45-67.
5. OK. AndroidManifest.xml:44-51.
6. OK. FW ActivityThread.java:2729-2731, 2741; MainActivity.java:192-194.
7. OK. FW Activity.java:7014-7019; MainActivity.java:938-940.
8. ERROR (guard incomplete). The edge's source calls loadEntries() at MainActivity.java:992, which is the else branch of `if (!_vaultManager.isVaultLoaded())` at 976-977 (else of 976), and the `_loaded` check at 978 (`else if (_loaded)`). The guard names the plain-text load (963-965) and `_loaded` but not the 976 branch, and it does not cover the case where the vault was already loaded (951 skipped). Fix: add "vault loaded: MainActivity.java:976-977 else branch (!isVaultLoaded() false), by the plain-text load at 963-965 or already loaded (951 skipped); and _loaded false (978)". STATE note: the plain-text vault file from an earlier intro run is cross-run, so the state itself needs an earlier run (UNCLEAR-level), but the guard defect is the ERROR.
9. OK. ENTERS S_LIST; guard `!_loaded` at MainActivity.java:1134 matches (1133-1144).
10. UNCLEAR. The toolbar menu tap reaches onOptionsItemSelected through AppCompat (body not on disk). MainActivity.java:1086-1099 verified.
11. OK. MainActivity.java:1088-1089.
12. OK. MainActivity.java:827 (bytecode).
13. UNCLEAR. preferenceResultLauncher.launch (MainActivity.java:834) runs through androidx.activity.result (body not on disk). Same as route 2 step 36.
14. OK. FW ActivityThread.java:2729-2731, 2741; PreferencesActivity.java:24.
15. OK. Guard `savedInstanceState == null` at PreferencesActivity.java:40 matches; 41 creates the fragment.
16. UNCLEAR. The fragment attach and onCreatePreferences run in androidx.fragment (body not on disk). PreferencesActivity.java:41-46 verified.
17. OK. The state is entered by the app call addPreferencesFromResource(R.xml.preferences) at MainPreferencesFragment.java:10. The render is androidx (see step 16).
18. UNCLEAR. A row tap is dispatched by androidx Preference/PreferenceFragmentCompat (body not on disk). PreferencesActivity.java:80-84 verified.
19. OK. Non_standard is correct: reflection through FragmentFactory.instantiate (PreferencesActivity.java:81); preferences.xml:38 names ImportExportPreferencesFragment.
20. UNCLEAR. The commit and attach run in androidx.fragment (body not on disk). PreferencesActivity.java:84, 91-97 verified.
21. UNCLEAR. The row tap is dispatched by androidx Preference (body not on disk). ImportExportPreferencesFragment.java:131-135 verified. Same as route 2 step 44.
22. OK. ImportExportPreferencesFragment.java:133 (bytecode); explicit, app calls app.
23. UNCLEAR (needs earlier run). The STATE requires the vault to already hold a SHA-1, 6-digit TOTP or HOTP entry, which this route cannot create. The guard matches the code: the filter at ImportExportPreferencesFragment.java:357-363 and the else branch (exports non-empty) at 384-390 with startActivity at 389.
24. OK. FW ActivityThread.java:2729-2731, 2741; TransferEntriesActivity.java:55.
25. OK. Visibility guard at TransferEntriesActivity.java:81-82 (`size() != 1` sets VISIBLE); click handler 84-96; FW View.java:6289-6296 (performClick).
26. ERROR (guard missing). generateQR() at TransferEntriesActivity.java:88 is inside `if (_currentEntryCount < _authInfos.size())` at line 85; the edge has no guard. Fix: guard "_currentEntryCount < _authInfos.size() (TransferEntriesActivity.java:85)". The else branch at 93-94 is finish() and is not on this route.
27. OK. generateQR (TransferEntriesActivity.java:197-203 chain) does not gate the call at 213, which is `selectedEntry.getUri()`. The route only builds GoogleAuthInfo.Export entries (ImportExportPreferencesFragment.java:388), so the virtual dispatch lands on GoogleAuthInfo$Export.getUri. Explicit: app calls app.
28. ERROR (class). The call is `builder.build().toByteArray()` at GoogleAuthInfo.java:459, which is a protobuf library call, not a framework registered callback. It is labelled FRAMEWORK/standard. By the class rule (library = non_standard), fix: relabel to non_standard. Body: GoogleAuthProtos is not in the source tree (the find under final_java_only found only monkey/report HTML), so the body is UNCLEAR.
29. ERROR (class). The protobuf runtime reads or writes OtpParameters through the generated dynamicMethod. Library-driven, labelled FRAMEWORK/standard; fix: relabel to non_standard. Generated body not on disk.
30. ERROR (class). The runtime gets the DigitCount verifier through the generated internalGetVerifier. Library-driven, labelled FRAMEWORK/standard; fix: relabel to non_standard. Generated body not on disk.
31. UNCLEAR. JVM class initialization (JLS 12.4.1) runs the static initializer on first read of the singleton. The class label (standard, runtime-run) is accepted. The generated body (GoogleAuthProtos$MigrationPayload$DigitCount) is not on disk.
32. UNCLEAR. The <clinit> to <init> edge is explicit generated code (protoc output), but the generated static initializer is not on disk; cannot check that the singleton field creates DigitCountVerifier.

Route 3 result: FAIL at step 8 (guard) and step 26 (guard). Steps 28-30 are wrong class labels (protobuf library). Steps 31-32 are generated-body UNCLEAR.

Route 3 counts: 32 steps; ERROR 5 (8, 26, 28, 29, 30); UNCLEAR 11 (2, 3, 10, 13, 16, 18, 20, 21, 23, 31, 32); OK 16 (1, 4, 5, 6, 7, 9, 11, 12, 14, 15, 17, 19, 22, 24, 25, 27).

## Route 4: IconPackExistsException.getIconPack

Route chain: S_ENTRY -> AegisApplication -> AegisApplicationBase.onCreate -> S_PROCESS -> MainActivity.onStart (plain-text vault, cross-run) -> loadEntries -> S_LIST -> Settings -> PreferencesActivity -> IconPacksManagerFragment -> add button -> file picker -> ImportIconPackTask (background) -> IconPackExistsException dialog -> Yes -> getIconPack.

Steps 1-30 (verdict, then reason):

1. OK. AndroidManifest.xml:21-27 (android:name=".AegisApplication").
2. UNCLEAR. AegisApplication.java:5-6 uses @HiltAndroidApp and extends AegisApplicationBase; the generated Hilt_AegisApplication is not on disk. FW ActivityThread.java:5740 holds.
3. UNCLEAR. Hilt-generated body (build class, line 43), not on disk.
4. OK. AegisApplicationBase.java:45-67; super.onCreate at 46, and no return before the state entry.
5. OK. AndroidManifest.xml:44-51 (`.ui.MainActivity`, MAIN, LAUNCHER).
6. OK. FW ActivityThread.java:2729-2731, 2741; MainActivity.java:192-194.
7. OK. FW ActivityThread.java:2740 (performStart only when !mFinished) and 2741; MainActivity.java:192-240 has no finish() or early return (the only `if` is at 202); MainActivity.java:938-940.
8. ERROR (guard incomplete). The call at MainActivity.java:992 is reached only when: isVaultInitNeeded() is false (942-948, return at 947 not taken); readVaultFile does not throw (catch 955-960, return at 960 not taken); loadFrom does not throw (catch 966-971, return at 971 not taken); the vault is plain text (963); isVaultLoaded() is true (976 else); and _loaded is false (978). The guard text names the plain-text load, the else at 991-992 and _loaded, but not the 942-948 return or the two catch-returns. Fix: add "isVaultInitNeeded() false (MainActivity.java:942-948); no exception from readVaultFile (955-960) or loadFrom (966-971)". STATE: the plain-text vault file from an earlier intro run is cross-run, so it also needs an earlier run.
9. OK. ENTERS S_LIST; guard `!_loaded` at MainActivity.java:1134 matches (1133-1144).
10. UNCLEAR. The toolbar or overflow tap reaches onOptionsItemSelected through AppCompat (body not on disk). MainActivity.java:1086-1089 verified.
11. OK. MainActivity.java:1088-1089 (guard matches).
12. OK. MainActivity.java:826-828; the call at 827 `startPreferencesActivity(null, null);`.
13. UNCLEAR. The intent is explicit (MainActivity.java:831 `new Intent(this, PreferencesActivity.class)`), but the start runs through preferenceResultLauncher.launch (834) in androidx.activity.result (body not on disk). Same as route 2 step 36.
14. OK. PreferencesActivity.java:23-24 (@Override, onCreate); FW ActivityThread.java:2729-2731, 2741.
15. ERROR (guard incomplete). The fragment is created only if the early return is not taken: PreferencesActivity.java:26-28 `if (abortIfOrphan(savedInstanceState)) { return; }`. The guard names only savedInstanceState == null (line 40). Fix: add "abortIfOrphan(savedInstanceState) is false (PreferencesActivity.java:26-28, return not taken)".
16. UNCLEAR. The fragment attach and onCreatePreferences run in androidx.fragment (body not on disk). PreferencesActivity.java:41-46 verified. Same as route 2 step 43.
17. OK. The state is entered by the app call addPreferencesFromResource(R.xml.preferences) at MainPreferencesFragment.java:9-10; the render is androidx (see step 16).
18. UNCLEAR. The row tap is dispatched by androidx Preference/PreferenceFragmentCompat (body not on disk). PreferencesActivity.java:19, 80-84 and preferences.xml:19-20 verified.
19. OK. Reflection is the correct non_standard class: PreferencesActivity.java:81 `getFragmentFactory().instantiate(getClassLoader(), pref.getFragment())`, with the class name at res/xml/preferences.xml:20. IconPacksManagerFragment.java:64 has a public no-arg constructor. The factory body is androidx and not read; the target and class are correct.
20. UNCLEAR. The attach and view creation run in androidx.fragment (body not on disk). IconPacksManagerFragment.java:64-65, 69 verified. Same as step 16.
21. OK. IconPacksManagerFragment.java:70-71 (`fab.setOnClickListener(v -> startImportIconPack())`); FW View.java:6289-6296 (performClick calls onClick at 6294).
22. OK. IconPacksManagerFragment.java:71 (bytecode).
23. OK. IconPacksManagerFragment.java:172-175 (startImportIconPack; ACTION_GET_CONTENT at 173; fireIntentLauncher at 175).
24. UNCLEAR. VaultManager.java:267 calls resultLauncher.launch(intent), and the result returns through androidx.activity.result to the lambda at IconPacksManagerFragment.java:57-62 (body not on disk). Same as route 2 step 49. The ENV (another app's picker returns a file) is a stated precondition.
25. OK. IconPacksManagerFragment.java:59 guard (RESULT_OK && data != null && data.getData() != null), then 60 importIconPack(data.getData()).
26. OK as an edge. importIconPack calls task.execute(getLifecycle(), ...) at IconPacksManagerFragment.java:155, which is ProgressDialogTask.execute (ProgressDialogTask.java:69-74) and then AsyncTask.execute. The route skips those two hops, as the printer marks on purpose. The framework runs doInBackground on a worker: FW AsyncTask.java:333 (doInBackground call), 369-374 (postResult). ImportIconPackTask.java:26.
27. OK. FW AsyncTask.java:691-695 (finish calls onPostExecute at 695), 705-713 (handleMessage calls finish); ImportIconPackTask.java:54-56.
28. ERROR (class). ImportIconPackTask.Callback (ImportIconPackTask.java:59-61) is an app-defined interface called by app code (ImportIconPackTask.java:56, `_cb.onTaskFinished(result)`), so it is explicit by the class rule, not non_standard. Fix: relabel to CALL/explicit. The target lambda$importIconPack$5 (IconPacksManagerFragment.java:134) matches.
29. UNCLEAR (needs earlier run). The IconPackExistsException path needs an icon pack already installed: IconPackManager.java:85 (dir exists) and 87-89 (UUID match) throw it, and installed packs come from the startup rescan (IconPackManager.java:33, rescanIconPacks at 132). This route imports nothing before step 26, so the state comes from an earlier run. The button dispatch is also inside MaterialAlertDialogBuilder/AppCompat (IconPacksManagerFragment.java:137), not on disk. The guard at 136 matches.
30. OK. IconPacksManagerFragment.java:142 `removeIconPack(((IconPackExistsException) e).getIconPack())`, inside the instanceof guard at 136 (the cast is safe). IconPackExistsException.java:11 `public IconPack getIconPack()` exists.

Route 4 result: FAIL at step 8 (guard), step 15 (guard), and step 28 (class). Steps 2-3 (Hilt), 10, 13, 16, 18, 20 and 24 (androidx) and 29 (needs an earlier-run icon pack) stay UNCLEAR. Steps 19, 21-23, 25-27 and 30 are edge-correct.

Route 4 counts: 30 steps; ERROR 3 (8, 15, 28); UNCLEAR 9 (2, 3, 10, 13, 16, 18, 20, 24, 29); OK 18 (1, 4, 5, 6, 7, 9, 11, 12, 14, 17, 19, 21, 22, 23, 25, 26, 27, 30).

Tool notes for route 4: my first show_route.py print was cut at 300 lines by my own `sed -n '1,300p'`, which stopped at step 25. Steps 23-30 were read from a saved copy (the full output is 386 lines). The tool again printed "core/java/... not found in the source tree" for ActivityThread.java, AsyncTask.java and View.java; those lines were checked with sed. The tool header said confirmed_by=INFERRED path=UNCHECKED; it was not used as a verdict.

## Route 5: VaultGroup.equals

Route chain: S_ENTRY -> AegisApplication -> AegisApplicationBase.onCreate -> S_PROCESS -> MainActivity.onStart (plain-text vault, cross-run) -> loadEntries -> S_LIST -> Settings -> PreferencesActivity -> AppearancePreferencesFragment -> Groups row -> GroupManagerActivity -> onOptionsItemSelected (delete unused groups) -> dialog Yes -> HashSet.removeAll -> ArrayList.contains -> VaultGroup.equals.

Steps 1-28 (verdict, then reason). Steps 1-18 are the same edges as route 4 (same edge IDs), so their verdicts match route 4:

1. OK. AndroidManifest.xml:21-27.
2. UNCLEAR. Hilt-generated superclass not on disk; FW ActivityThread.java:5740 holds. Same as route 4 step 2.
3. UNCLEAR. Hilt-generated body, not on disk.
4. OK. AegisApplicationBase.java:45-67.
5. OK. AndroidManifest.xml:44-51.
6. OK. FW ActivityThread.java:2729-2731, 2741; MainActivity.java:192-194.
7. OK. FW ActivityThread.java:2740-2741; MainActivity.java:192-240 has no finish() or early return (only the savedInstanceState check at 202); MainActivity.java:938-940.
8. ERROR (guard incomplete). Same edge as route 4 step 8. The guard omits isVaultInitNeeded() false (MainActivity.java:942-948) and the two catch-returns (955-960, 966-971). Fix: add "isVaultInitNeeded() false (MainActivity.java:942-948); no exception from readVaultFile (955-960) or loadFrom (966-971)". STATE: the plain-text vault file is cross-run, so it also needs an earlier run.
9. OK. ENTERS S_LIST; guard `!_loaded` at MainActivity.java:1134 matches (1133-1144).
10. UNCLEAR. The toolbar tap reaches onOptionsItemSelected through AppCompat (body not on disk). MainActivity.java:1086-1089 verified.
11. OK. MainActivity.java:1088-1089.
12. OK. MainActivity.java:827.
13. UNCLEAR. preferenceResultLauncher.launch (MainActivity.java:834) runs through androidx.activity.result (body not on disk). Same as route 2 step 36.
14. OK. PreferencesActivity.java:23-24; FW ActivityThread.java:2729-2731, 2741.
15. ERROR (guard incomplete). Same edge as route 4 step 15. The fragment is created only when the early return at PreferencesActivity.java:26-28 (`if (abortIfOrphan(savedInstanceState)) { return; }`) is not taken. Fix: add "abortIfOrphan(savedInstanceState) false (PreferencesActivity.java:26-28)". AegisActivity.java:154-156 returns false when savedInstanceState is null, so the route passes, but the guard must say so.
16. UNCLEAR. The fragment attach and onCreatePreferences run in androidx.fragment (body not on disk). Same as route 4 step 16.
17. OK. The state is entered by the app call addPreferencesFromResource(R.xml.preferences) at MainPreferencesFragment.java:9-10; the render is androidx (see step 16).
18. UNCLEAR. The row tap is dispatched by androidx Preference/PreferenceFragmentCompat (body not on disk). PreferencesActivity.java:19, 80-84 verified.
19. OK. Reflection is the correct non_standard class: PreferencesActivity.java:81 `getFragmentFactory().instantiate(getClassLoader(), pref.getFragment())`, with the class name at res/xml/preferences.xml:8. AppearancePreferencesFragment.java:23 declares no constructor, so the implicit public no-arg constructor is used. The factory body is androidx and not read.
20. UNCLEAR. The attach and onCreatePreferences run in androidx.fragment (body not on disk). AppearancePreferencesFragment.java:29 verified. Same as route 4 step 16.
21. UNCLEAR. The Groups row tap is dispatched by androidx Preference (OnPreferenceClickListener, body not on disk). The class (standard) and target are correct: AppearancePreferencesFragment.java:32-37 (listener set in onCreatePreferences, line 29). Same as route 2 step 44.
22. OK. AppearancePreferencesFragment.java:34-35 (`new Intent(requireContext(), GroupManagerActivity.class)`, then startActivity); AndroidManifest.xml:85 declares .ui.GroupManagerActivity.
23. OK. Entry into GroupManagerActivity.onCreate: FW ActivityThread.java:2729-2731, 2741; GroupManagerActivity.java:36-37. The entry edge needs no guard; the continuation guard is step 24.
24. ERROR (guard incomplete). The rest of GroupManagerActivity.onCreate (setContentView at 41, setSupportActionBar at 42) runs only when abortIfOrphan(savedInstanceState) returns false: GroupManagerActivity.java:38-40 `if (abortIfOrphan(savedInstanceState)) { return; }`. The guard text omits this. AegisActivity.java:154-156 returns false when savedInstanceState is null, so the fresh-start route passes. Fix: add "abortIfOrphan(savedInstanceState) false (GroupManagerActivity.java:38-40; AegisActivity.java:154-156 returns false when savedInstanceState is null)". The menu-creation claim itself is AppCompat (androidx, not on disk).
25. UNCLEAR. The toolbar tap is dispatched to onOptionsItemSelected by AppCompat (body not on disk). GroupManagerActivity.java:195-207 verified (branch at 201-202).
26. OK. GroupManagerActivity.java:201-202 (the else-if chain; the home and save branches above are false on this path, so the guard text is complete).
27. UNCLEAR. The Yes button is wired by MaterialAlertDialogBuilder (AppCompat/Material body, not on disk). The cited framework AlertController is not the class this dialog uses. GroupManagerActivity.java:145-149 verified (showSecureDialog at 145, setPositiveButton at 149, Yes lambda 149-158). Same as route 4 step 29.
28. ERROR (class). The call chain is `unusedGroups.removeAll(...)` (GroupManagerActivity.java:151) -> HashSet/AbstractSet.removeAll -> ArrayList.contains (VaultRepository.java:327-329 returns Collectors.toList(), an ArrayList) -> `o.equals(elementData[i])` -> VaultGroup.equals (VaultGroup.java:48, body 47-55). This is library code (java.util) calling an app override, so it is non_standard by the class rule, not FRAMEWORK/standard. It is the same category as the protobuf calls in route 3 steps 28-30. Fix: relabel to non_standard. The guard (set not larger than the used list; since used is a subset of all groups, that means every group is used) matches the contains branch. The JDK source is not on disk, so the removeAll and indexOf behaviour is not checked against source; the class verdict does not depend on it.

Route 5 result: FAIL at step 8 and step 15 (shared prefix guards with route 4), step 24 (guard), and step 28 (class). Steps 21, 25 and 27 are AppCompat/Material dispatch (UNCLEAR). Steps 19, 22, 23 and 26 are edge-correct.

Route 5 counts: 28 steps; ERROR 4 (8, 15, 24, 28); UNCLEAR 10 (2, 3, 10, 13, 16, 18, 20, 21, 25, 27); OK 14 (1, 4, 5, 6, 7, 9, 11, 12, 14, 17, 19, 22, 23, 26).

Tool notes for route 5: the full printout was saved and read without truncation (366 lines). The framework lookup again printed "not found in the source tree" for View.java and AlertController.java, although fw_src/android-8.1.0_r1/core/java/... exists. The JDK collections source (java.util AbstractSet, ArrayList) is not in the source tree, so step 28's body claim is not checked against source.
