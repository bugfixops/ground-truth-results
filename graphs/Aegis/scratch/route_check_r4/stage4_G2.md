# Stage 4 route check R4-G2 (Aegis schema 2, round 4, read-only)

Date: 2026-10-27. Sources: current graph_def.py; tools/show_route.py output (with --dedupe --max 60, run from work/ in a child process); app source under final_java_only/Aegis/app/Aegis-#v3.4.2/app/src/main/java/com/beemdevelopment/aegis; FW-SRC android-8.1.0_r1 (ActivityThread.java, View.java); compiled classes in app/build/intermediates (FabMenuHelper, MainActivity, EditEntryActivity, Dialogs, SecurityPreferencesFragment, AuthenticatorPlusImporter$EncryptedState) read with a read-only parser for lambda names and call-site lines (javap cannot run: no Java runtime; build classes dated Sep 2, they agreed with the source wherever checked).

## Summary

| Route | Target | Steps | ERROR | UNCLEAR | OK |
|---|---|---|---|---|---|
| 1 | EntryAdapter.setTempHighlightEntry | 27 | 14, 18, 20, 23 | 2, 3, 8, 16, 19 | 18 |
| 2 | Slot.<init>(UUID,byte[],CryptParameters) | 36 | 26, 28, 29, 32, 33 | 2, 3, 8, 10, 13, 16, 18, 19, 20, 21, 24 | 20 |
| 3 | MainActivity.importScannedEntries | 21 | 12, 21 | 2, 3, 8, 14, 16, 19 | 13 |
| 4 | GoogleAuthProtos$MigrationPayload$DigitCount$DigitCountVerifier.<init> | 32 | 24, 25, 26 | 2, 3, 8, 10, 13, 16, 18, 19, 20, 21, 23, 28, 29, 30, 31, 32 | 13 |
| 5 | ScannerActivity.unbindPreview | 15 | 9, 13, 14 | 2, 3, 10, 12 | 8 |
| Total | | 131 | 17 | 42 | 72 |

## Route 1: EntryAdapter.setTempHighlightEntry

Route as built: app start, MainActivity onCreate/onStart (plain-text vault), list, + then enter item, then a manual entry. The route then takes the delete branch of the edit page (steps 20-23), which cannot happen for a new entry. The route is wrong as a whole, see step 20.

Step 2 (E5b266140, LIFECYCLE, AegisApplication.<init> -> Hilt_AegisApplication.onCreate): UNCLEAR. Printed: AegisApplication.java:6 (`public class AegisApplication extends AegisApplicationBase`); FW ActivityThread.java:5740 (mInstrumentation.callApplicationOnCreate). Source says: the framework call is verified; the Hilt superclass is generated code, not on disk (rule 7). Fix: none (INFERRED).

Step 3 (E1ef992ce, CALL, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate): UNCLEAR. Hilt generated body, not on disk. No guard. Fix: none.

Step 8 (E20e76e09, CALL, MainActivity.onStart -> loadEntries, STATE plain-text vault): UNCLEAR (needs earlier run). Printed MainActivity.java:936-997: guard text matches the code (947 return on isVaultInitNeeded, 951 read, 960 and 971 returns, 976-978, else branch 991-992). Writer of the plain file: IntroActivity.java:93 (CRYPT_TYPE_NONE means creds null) and IntroActivity.java:100 `_vaultManager.initNew(creds)`, which calls VaultManager.java:65 `repo.save()`. Source says: the state text names the earlier intro run but does not cite the writing line, which the convention asks for. Fix proposed: add the writer citation (IntroActivity.java:100, VaultManager.java:65) to the needs_state text. The route stays "needs earlier run".

Step 14 (E0979a03c, CALL/non_standard, FabMenuHelper.lambda$setupClickListeners$2 -> MainActivity.startEditEntryActivity): ERROR (text-only guard omission; route unaffected). Printed FabMenuHelper.java:59-64; line 60 `if (onClick != null)` guards `onClick.run()` at line 61. Build class: lambda$setupClickListeners$2 has an ifnull at L60 that skips the run at L61. The edge has no guard text. Route unaffected: the enter item always has its Runnable (MainActivity.java:256). Fix: add guard "onClick != null (FabMenuHelper.java:60); the enter item is registered at MainActivity.java:256".

Step 16 (E6597c1f8, INTENT, MainActivity.startEditEntryActivityForManual -> EditEntryActivity.<init>): UNCLEAR. Printed MainActivity.java:509-514 (isManual true at 512, launch at 513). The launch and its callback go through the androidx ActivityResultLauncher (not on disk, rule 7). Fix: none.

Step 18 (Ef6ab7dd8, FRAMEWORK, EditEntryActivity.onCreate -> onCreateOptionsMenu): ERROR (text-only guard omission; route unaffected). Printed EditEntryActivity.java:165-170: `if (abortIfOrphan(savedInstanceState)) { return; }` (167-168) hides the rest of onCreate, including setContentView and the toolbar. AegisActivity.java:155-163: abortIfOrphan returns true only when savedInstanceState != null and isOrphan(); a fresh launch passes null, so it returns false. The androidx dispatch of onCreateOptionsMenu is UNCLEAR (not on disk). Fix: add guard "abortIfOrphan(savedInstanceState) is false (EditEntryActivity.java:167-168; fresh launch has null state, AegisActivity.java:155)".

Step 19 (E69bb265a, FRAMEWORK, EditEntryActivity.onCreateOptionsMenu -> onOptionsItemSelected): UNCLEAR. Printed EditEntryActivity.java:535-552; build class L539-540 (save -> onSave), L541-542 (delete). The toolbar dispatch is androidx (not on disk). The edge text is generic ("save, delete, discard, reset"), so the edge itself holds; the wrong item is chosen at step 20. Fix: none on this edge.

Step 20 (E624f9135, FRAMEWORK, EditEntryActivity.onOptionsItemSelected -> lambda$onOptionsItemSelected$18, "Tap Yes in the delete dialog"): ERROR (missing guard; route impossible for a new entry). EditEntryActivity.java:658-659 (onCreateOptionsMenu): `if (_isNew) menu.findItem(R.id.action_delete).setVisible(false);`. This route is a new manual entry (EditEntryActivity.java:193-195 sets _isNew = true for the newEntry branch), so the delete item is hidden and the dialog cannot be reached. The evidence cites View.performClick (FW 6289-6296), which is not the mechanism for a menu item. Fix: replace steps 20-22 for this route with the add path: EditEntryActivity.onOptionsItemSelected -> EditEntryActivity.onSave (EditEntryActivity.java:539-540; build L540 invoke onSave), then onSave -> addAndFinish (EditEntryActivity.java:867) with guards parseEntry succeeds (850-856) and no same name and issuer entry when _isNew (858-865), then addAndFinish -> saveAndFinish(entry, false) (680). graph_def.py has no onSave or addAndFinish edge, so these must be added.

Step 23 (E58ce4492, RESULT, EditEntryActivity.saveAndFinish -> MainActivity.lambda$new$6): ERROR (guard contradicted by the chain). The guard says "delete is false (saveAndFinish from addAndFinish, EditEntryActivity.java:680)". Printed EditEntryActivity.java:698-706: `delete` is only written to the intent (701); it is not a branch. Steps 20-22 call saveAndFinish(entry, true) (695), so the chain taken has delete=true. Build class lambda$new$6 (L179-182) does not read "delete". Fix: route through addAndFinish (see step 20), so delete=false holds from line 680. Keep the guard text; the saveAndBackupVault() guard holds (EditEntryActivity.java:703; AegisActivity.java:139-147 returns true on success). FW part (ActivityThread.java:4253-4265) printed; the androidx dispatch to the callback is UNCLEAR.

## Route 2: Slot.<init>(UUID,byte[],CryptParameters)

Route as built: app start, MainActivity list (plain-text vault), Settings, the Security page, the pin-keyboard switch and its password dialog, then the Authenticator Plus importer, VaultFile, SlotList and Slot. The route cannot reach the target as built: step 26 gives the typed password to the wrong listener, and step 29 dispatches to GoogleAuthUriImporter, not AegisImporter. Steps 1-8 are the same edges as route 1 (same verdicts). Steps 27, 30 and 31 are correct as single edges but are reached only through steps 26 and 29.

Step 2 (E5b266140, LIFECYCLE): UNCLEAR. Same as route 1 step 2 (Hilt superclass, generated code, rule 7). Fix: none.

Step 3 (E1ef992ce, CALL): UNCLEAR. Same as route 1 step 3 (Hilt generated body). Fix: none.

Step 8 (E20e76e09, CALL, STATE plain-text vault): UNCLEAR (needs earlier run). Printed MainActivity.java:950-974 and 976-995: `if (!isVaultLoaded()) startAuthActivity ... else if (_loaded) {...} else { loadEntries(); ... }` (976-992). The guard holds, including `_loaded` false at 978. Writer not cited: the state text names the earlier intro run but not the writing line (IntroActivity.java:100 initNew(creds); VaultManager.java:65 repo.save()), as in route 1 step 8. Fix: add the writer citation to needs_state. The route stays "needs earlier run".

Step 10 (E887b87bf, GUI, S_LIST -> MainActivity.onOptionsItemSelected): UNCLEAR. Printed MainActivity.java:1086-1118 (1088 action_settings, 1090 action_about, 1093 action_lock, 1096 sort group); the body matches the edge text. The toolbar dispatch to onOptionsItemSelected is androidx.appcompat (not on disk), as in route 1 step 19. Fix: none on this edge.

Step 13 (E640fb9eb, INTENT, MainActivity.startPreferencesActivity(Class,String) -> PreferencesActivity.<init>): UNCLEAR. Printed MainActivity.java:830-834 (Intent to PreferencesActivity at 831; preferenceResultLauncher.launch at 834). The target class is correct; the launch goes through the androidx ActivityResultLauncher (not on disk), as in route 1 step 16. Fix: none.

Step 16 (E382bc001, LIFECYCLE, MainPreferencesFragment.<init> -> onCreatePreferences): UNCLEAR. Printed PreferencesActivity.java:40-46 and MainPreferencesFragment.java:7-12 (onCreatePreferences at 9-11). The fragment attach and list build are androidx.fragment/preference (not on disk). Fix: none.

Step 18 (E3452b602, GUI, S_SETTINGS_MAIN -> PreferencesActivity.onPreferenceStartFragment): UNCLEAR. Printed PreferencesActivity.java:19 and 80-84 (match). The tap-to-callback dispatch is androidx.preference (not on disk). Fix: none on this edge.

Step 19 (Ed19f3b08, CALL/non_standard, reflection -> SecurityPreferencesFragment.<init>): UNCLEAR. Printed PreferencesActivity.java:81 (`getSupportFragmentManager().getFragmentFactory().instantiate(getClassLoader(), pref.getFragment())`) and preferences.xml:26 (the row's android:fragment is SecurityPreferencesFragment, matching the guard). The constructor call is inside androidx FragmentFactory.instantiate (not on disk). Fix: none on this edge; the route fix is at step 26.

Step 20 (E5c8f972e, LIFECYCLE, SecurityPreferencesFragment.<init> -> onCreatePreferences): UNCLEAR. Printed PreferencesActivity.java:84 and 91-97 (showFragment commit). The fragment attach and list build are androidx (not on disk). Fix: none.

Step 21 (Eb2d49c8f, FRAMEWORK, onCreatePreferences -> SecurityPreferencesFragment.lambda$onCreatePreferences$9): UNCLEAR. Name verified in SecurityPreferencesFragment.class: lambda$onCreatePreferences$9 lines 153-176; registered at SecurityPreferencesFragment.java:152; guard 153-155 holds. The change dispatch is androidx.preference (not on disk). Fix: none.

Step 24 (E5bb67188, FRAMEWORK, Dialogs.showTextInputDialog -> Dialogs.lambda$showTextInputDialog$8): UNCLEAR. Name verified in Dialogs.class: lambda$showTextInputDialog$8 lines 227-236 (the OnShowListener at Dialogs.java:226-236). The OnShowListener runs from AlertDialog.show, which is MaterialAlertDialogBuilder/androidx (not on disk). Fix: none.

Step 26 (E41c33149, CALL/non_standard, Dialogs.lambda$showTextInputDialog$7 -> AuthenticatorPlusImporter$EncryptedState.lambda$decrypt$0): ERROR (route-breaking, wrong listener). Printed Dialogs.java:231-235 (listener.onTextInputResult(text) at 233), SecurityPreferencesFragment.java:157-172 (the password lambda that the pin switch passes to the dialog), AuthenticatorPlusImporter.java:67-74. Source says: the listener that Dialogs.java:233 calls is the one passed down from step 22's call at SecurityPreferencesFragment.java:157, which is SecurityPreferencesFragment.lambda$onCreatePreferences$7 (build lines 158-173: isDigitsOnly, then PasswordSlotDecryptTask at 159-162). The route's dst AuthenticatorPlusImporter$EncryptedState.lambda$decrypt$0 is the listener of a different dialog (AuthenticatorPlusImporter.java:67, opened by decrypt(Context, DecryptListener)). Fix: the edge itself can be corrected to dst SecurityPreferencesFragment.lambda$onCreatePreferences$7, but that path ends at PasswordSlotDecryptTask, so the pin switch cannot reach Slot.<init>. Route-level fix: replace steps 19-26 with the Aegis import path: step 19 targets the ImportExport row (preferences.xml:37-41, android:fragment ImportExportPreferencesFragment) instead of the Security row, then ImportExportPreferencesFragment.startImportEntriesActivity (graph_def.py:1687) -> ImportEntriesActivity.<init> -> onCreate -> startImport (ImportEntriesActivity.java:103-104) -> startImportFile when file != null (109-127) -> the read at step 29's fix.

Step 28 (E9a12d4df, CALL, decrypt(char[]) -> DatabaseImporter.read): ERROR (text-only guard omission; route unaffected). Printed AuthenticatorPlusImporter.java:53-55: `if (file.getName().equals(FILENAME)) { GoogleAuthUriImporter importer = new GoogleAuthUriImporter(null); return importer.read(zipStream); }`. Source says: the call at 55 runs only when a zip entry named FILENAME is found (line 53), and the edge has no guard text. The receiver is GoogleAuthUriImporter (line 54); its read(InputStream) is inherited (GoogleAuthUriImporter.java declares only the 2-arg read at line 27), so the resolved target is DatabaseImporter.read(InputStream). The route is unaffected, because the file has that entry. Fix: add guard "a zip entry named FILENAME is found (AuthenticatorPlusImporter.java:53-55)". Note: the receiver type is what breaks step 29.

Step 29 (Ec82b48e4, CALL, DatabaseImporter.read -> AegisImporter.read): ERROR (route-breaking, impossible receiver). Printed DatabaseImporter.java:75-77 (read(stream) -> read(stream, false) at 76), GoogleAuthUriImporter.java:16 and 27 (extends DatabaseImporter; overrides read(InputStream, boolean) at 27), AegisImporter.java:33 (extends DatabaseImporter). Source says: the virtual call at 76 dispatches on the receiver's class, which at AuthenticatorPlusImporter.java:54 is GoogleAuthUriImporter, so the target is GoogleAuthUriImporter.read (27). AegisImporter is not a subclass of GoogleAuthUriImporter, so AegisImporter.read cannot be reached from this receiver. The edge text ("can dispatch to this implementation") does not check the receiver type. Fix: none on this edge (the target is impossible for this receiver). The route-level fix is the Aegis receiver: DatabaseImporter.create builds the importer for the Aegis Definition by reflection (DatabaseImporter.java:34 and 92; graph_def.py:2796-2799), and ImportEntriesActivity.java:133 calls importer.read(stream), which reaches AegisImporter.read (AegisImporter.java:45) and then steps 30-36. Check before editing: graph_def.py has no literal 'DatabaseImporter.read' node string (grep), so confirm the node name used by step 28, and the edges ImportEntriesActivity.startImportFile -> that read and the dispatch to AegisImporter.read.

Step 32 (E50406d09, CALL, VaultFile.fromJson -> VaultFile$Header.fromJson): ERROR (text-only guard omission; route unaffected). Printed VaultFile.java:62-68: `if (obj.getInt("version") > VERSION) { throw new VaultFileException(...); }` (64-66) gates the call at 68. The edge has no guard text. Route unaffected (a supported version). Fix: add guard "obj.getInt(\"version\") <= VERSION (VaultFile.java:64-66)".

Step 33 (Ed2faa897, CALL, VaultFile$Header.fromJson -> SlotList.fromJson): ERROR (text-only guard omission; route unaffected). Printed VaultFile.java:144-150: `if (obj.isNull("slots") && obj.isNull("params")) { return new Header(null, null); }` (145-147) gates the call at 150. The edge has no guard text. Route unaffected (slots present). Fix: add guard "not (obj.isNull(\"slots\") and obj.isNull(\"params\")) (VaultFile.java:145-147)".

OK as edges and counted only: steps 1, 4-7, 9, 11, 12, 14, 15, 17, 22, 23, 25, 27, 30, 31, 34, 35, 36 (20 OK in total with steps 27, 30, 31 reached only through 26 and 29).

## Route 3: MainActivity.importScannedEntries

Route as built: app start, MainActivity onCreate/onStart, the unreadable-vault error dialog (steps 8-11), a jump from that dialog's OK to the scanner's listener (step 12), the camera bind and QR decode (13-17), the export batch end (18), the result to MainActivity (19-20) and the import (21). The route never opens the scanner: no edge from MainActivity to ScannerActivity.<init> is on it. Step 12 is the break, so steps 13-21 are reachable only through it.

Tool note: show_route.py stopped with ValueError on the step 18 evidence `SRC ui/ScannerActivity.java:217-219, 226-227` (the regex keeps the trailing comma, and int('') fails). The trace was rerun with the comma stripped in memory (tools/show_route.py not modified). The second range (226-227) was read from the source directly.

Step 1 (E14b4e906, ENTRY): OK. AndroidManifest.xml:21-27 (android:name=".AegisApplication").

Step 2 (E5b266140, LIFECYCLE): UNCLEAR. Same as route 1 step 2 (Hilt superclass, generated code, rule 7). Fix: none.

Step 3 (E1ef992ce, CALL): UNCLEAR. Same as route 1 step 3 (Hilt generated body). Fix: none.

Step 4 (E88ed9829, ENTERS/page): OK. AegisApplicationBase.java:45-67; FW ActivityThread.java:5740.

Step 5 (E28ffc58c, ENTRY): OK. AndroidManifest.xml:44-51 (MAIN and LAUNCHER filter at 47-50).

Step 6 (Eb76444fd, LIFECYCLE): OK. MainActivity.java:192-194; FW ActivityThread.java:2729-2731, 2741.

Step 7 (E3a06baed, LIFECYCLE): OK. MainActivity.java:938-940; FW ActivityThread.java:2741.

Step 8 (E7400a38d, CALL, STATE: vault file unreadable): UNCLEAR (needs earlier run; and this branch is not on the scanner route). Printed MainActivity.java:946-960: the intro return at 946-947 (isVaultInitNeeded), the readVaultFile catch at 954-960 (showErrorDialog at 957, OK listener `finish()` at 958, return at 960). The edge text matches these lines. But the state text names no writer ("an earlier run left it unreadable"), and the branch returns from onStart without starting the scanner. Fix: for this route use E20e76e09 (MainActivity.onStart -> loadEntries, the plain-text vault branch used by routes 1 and 2; MainActivity.java:976-992) and cite its writer as in route 1 step 8 (IntroActivity.java:100, VaultManager.java:65).

Step 9 (Ec4596530, CALL): OK. Dialogs.java:368 (`showErrorDialog(context, message, e.toString(), listener)`).

Step 10 (Eff284e41, CALL): OK. Dialogs.java:376 (`showErrorDialog(context, context.getString(message), error, listener)`).

Step 11 (Ef2c4b2cc, FRAMEWORK): OK. FW View.java:6289-6296 (performClick calls onClick); Dialogs.java:391-395 (OK relay at 392-393). Build class: lambda$showErrorDialog$15 at 392-395 (name verified).

Step 12 (Ec9aba117, CALL/non_standard, STATE: camera ready): ERROR (route-breaking, wrong listener). The edge's guard says the dialog was opened by the scanner error branch (ScannerActivity.java:189-196). In this route the dialog is the one from step 8, and its OK listener is MainActivity's `finish()` (MainActivity.java:957-959), not the ScannerActivity lambda at line 196. Step 11 calls whatever OnClickListener the dialog holds, so the target is decided at runtime (same as route 2 step 29), and for this dialog it is not ScannerActivity.lambda$onQrCodeDetected$1 (build 196-196, name verified). Fix: remove steps 8-13 from this route and start the scanner: FabMenuHelper.lambda$setupClickListeners$2 -> MainActivity.startScanActivity (graph_def.py:745; the scan item is registered at MainActivity.java:254), then MainActivity.startScanActivity -> ScannerActivity.<init> (graph_def.py:771; MainActivity.java:803-809), ScannerActivity.<init> -> ScannerActivity.onCreate (graph_def.py:1132), then ScannerActivity.lambda$onCreate$0 -> ScannerActivity.bindPreview (graph_def.py:3204; ScannerActivity.java:87), then step 14. The edges that open the FAB before line 745 were not re-checked here. Alternative start: MainActivity.onStart -> doShortcutActions (MainActivity.java:1006) -> startScanActivity with the scan shortcut intent (MainActivity.java:837-846).

Step 13 (E268ab4ba, CALL): OK as an edge (ScannerActivity.java:196 calls bindPreview). It is reached only through step 12, so it is not on any valid route as built.

Step 14 (Ed8457530, FRAMEWORK, ENV: QR code in front of the camera): UNCLEAR. The per-frame dispatch is INFERRED androidx.camera (CameraX source not read; rule 7). Printed ScannerActivity.java:164 (setAnalyzer) and QrCodeAnalyzer.java:29 (analyze). Fix: none.

Step 15 (Ece1825c9, CALL): OK. QrCodeAnalyzer.java:31-34 (YUV check, return), 55-58 (decode, then listener call at 56-57), 59 (NotFoundException skips the call); ScannerActivity.java:36 (implements Listener), 175.

Step 16 (Ede72ed30, FRAMEWORK): UNCLEAR. Handler.post is platform code, and the framework Handler source is not in the tree (a depth-6 search found no os/Handler.java), so main-looper delivery is not verified. Fix: none on this edge.

Step 17 (Ec386f776, CALL): OK. ScannerActivity.java:177-181 (isFinishing at 177-179; _analysis check at 181), 183-185 (export scheme check at 184, handleExportUri at 185). Build class: lambda$onQrCodeDetected$2 at 177-199 (name verified).

Step 18 (E146f71d1, CALL): OK. ScannerActivity.java:217-219 (batch id match, next index), 226-227 (last one: `finish(_entries)` at 227). The dst "ScannerActivity.finish" is the list overload at line 236; the edge's name does not show the overload, which is worth adding.

Step 19 (E8ec348dd, RESULT): UNCLEAR. Verified: ScannerActivity.java:236-241 (setResult(RESULT_OK) with the entries, then finish()) and FW ActivityThread.java:4253-4265. The step into MainActivity.lambda$new$2 goes through the androidx ActivityResultLauncher callback (rule 7, not on disk), as in route 1 step 16. Fix: none.

Step 20 (E528f4565, CALL): OK. MainActivity.java:150-156; build lambda$new$2 at 152-156 (name verified); the guard matches 152-154.

Step 21 (Ec60d3cdc, CALL): ERROR (text-only guard omission; route unaffected). MainActivity.java:613 `if (entries != null)` gates the call at 614 (`importScannedEntries(entries)`). The edge has no guard text. Route unaffected: the export path always puts the entries list in the result (ScannerActivity.java:238). Fix: add guard "entries != null (MainActivity.java:611-614)".

Route-level result: steps 8-13 need the scanner-start fix above; steps 14-21 are valid edges but are reached only through the broken step 12.

## Route 4: GoogleAuthProtos$MigrationPayload$DigitCount$DigitCountVerifier.<init>

Route as built: app start, MainActivity onStart (plain-text vault), the list, Settings, the Import/Export page, the Google Authenticator style export (TransferEntriesActivity, one Next tap), the export URI build (GoogleAuthInfo.Export.getUri), then protobuf serialization down to the DigitCountVerifier constructor. Steps 1-27 are checked against the source. Steps 28-32 are protobuf runtime or generated code (INFERRED, rule 7), so they stay UNCLEAR. The route is consistent with the source up to step 27. Steps 24-26 have guard-text gaps, but the route is unaffected.

Tool note: the unpatched show_route.py has the same trailing-comma crash as in route 3. Routes 4 and 5 were generated with the same in-memory fix (tools/show_route.py not modified).

Step 1 (E14b4e906, ENTRY): OK. AndroidManifest.xml:21-27.

Step 2 (E5b266140, LIFECYCLE): UNCLEAR. Hilt superclass (generated, rule 7). Fix: none.

Step 3 (E1ef992ce, CALL): UNCLEAR. Hilt generated body (rule 7). Fix: none.

Step 4 (E88ed9829, ENTERS/page): OK. AegisApplicationBase.java:45-67; FW ActivityThread.java:5740.

Step 5 (E28ffc58c, ENTRY): OK. AndroidManifest.xml:44-51.

Step 6 (Eb76444fd, LIFECYCLE): OK. MainActivity.java:192-194; FW ActivityThread.java:2729-2731, 2741.

Step 7 (E3a06baed, LIFECYCLE): OK. MainActivity.java:938-940; FW ActivityThread.java:2741.

Step 8 (E20e76e09, CALL, STATE: plain-text vault from an earlier intro run): UNCLEAR (needs earlier run). The guard matches the code: MainActivity.java:950-974 (loadFrom at 965; early returns at 947, 960, 971), and 991-992 (loadEntries). The state text names the intro run but not the line that writes the file. Fix: cite IntroActivity.java:100 (`_vaultManager.initNew(creds)`) and VaultManager.java:65 (`repo.save()`), as in route 1 step 8.

Step 9 (E1ffae3d8, ENTERS/page): OK. MainActivity.java:1133-1144 (guard `_loaded` at 1134, set at 1142).

Step 10 (E887b87bf, GUI): UNCLEAR. The tap-to-onOptionsItemSelected dispatch is androidx.appcompat (rule 7). The body is verified at MainActivity.java:1086-1118. Fix: none.

Step 11 (Ef4e32054, CALL): OK. MainActivity.java:1088-1089.

Step 12 (Ef64f95ee, CALL): OK. MainActivity.java:827 (bytecode).

Step 13 (E640fb9eb, INTENT): UNCLEAR. The intent is verified (MainActivity.java:830-834), but the launch goes through preferenceResultLauncher (androidx.activity.result, not on disk), as in route 2 step 13. Fix: none.

Step 14 (E94201299, LIFECYCLE): OK. PreferencesActivity.java:24; FW ActivityThread.java:2729-2731, 2741.

Step 15 (E50e3cfda, CALL): OK. PreferencesActivity.java:26-27 (abortIfOrphan false for a null state), 40-41 (new MainPreferencesFragment).

Step 16 (E382bc001, LIFECYCLE): UNCLEAR. Fragment attach and onCreatePreferences are androidx.fragment/preference (rule 7), as in route 2 step 16. Fix: none.

Step 17 (Eccc3a740, ENTERS/page): OK. MainPreferencesFragment.java:9-11 (addPreferencesFromResource at 10); preferences.xml:8-44 (rows).

Step 18 (E3452b602, GUI): UNCLEAR. The tap dispatch to onPreferenceStartFragment is androidx.preference (rule 7). PreferencesActivity.java:80-84 verified. Fix: none.

Step 19 (E63d9f2a4, CALL/non_standard reflection): UNCLEAR. The reflective instantiate is at PreferencesActivity.java:81 and the row is preferences.xml:38 (both verified), but the constructor runs inside androidx FragmentFactory.instantiate (not on disk). The evidence text is wrong: it repeats the attach/onCreatePreferences sentence from step 16. Fix (evidence text): cite PreferencesActivity.java:80-84 and preferences.xml:38 only.

Step 20 (E245f8b40, LIFECYCLE): UNCLEAR. androidx.fragment lifecycle (rule 7). PreferencesActivity.java:84, 91-97 verified. Fix: none.

Step 21 (E8e4d066b, FRAMEWORK): UNCLEAR. Name verified: ImportExportPreferencesFragment.lambda$onCreatePreferences$10 at build 133-134; source 131-135 (click listener at 132). The tap dispatch is androidx.preference (rule 7). Fix: none.

Step 22 (E1f7435e7, CALL): OK. ImportExportPreferencesFragment.java:133 (bytecode); the lambda is at build 133-134.

Step 23 (Eba2c5bb9, INTENT, STATE: vault holds a TOTP or HOTP entry with SHA-1 and 6 digits): UNCLEAR (needs earlier run). The guard matches: ImportExportPreferencesFragment.java:352-363 (type, DEFAULT_DIGITS and DEFAULT_ALGORITHM filter), 384-390 (empty-list check at 384; intent at 387-389). The state text names the reader (352-363) but no writer. Fix: cite the step that writes such an entry (an add or import path, e.g. EditEntryActivity.java:867 onSave -> addAndFinish), or keep it as needs earlier run.

Step 24 (E72e1a8df, LIFECYCLE): ERROR (text-only guard omission; route unaffected). TransferEntriesActivity.java:57-58 `if (abortIfOrphan(savedInstanceState)) return;` gates the rest of onCreate (the Next wiring at 84-96 included). The edge has no guard. Route unaffected: a fresh launch passes a null state (AegisActivity.java:155-163). Fix: add guard "abortIfOrphan(savedInstanceState) is false (TransferEntriesActivity.java:57-58)".

Step 25 (Ec5f95bb3, FRAMEWORK): ERROR (guard text does not match the code; route unaffected). Name verified: TransferEntriesActivity.lambda$onCreate$0 at build 85-96 (source 84-96). The edge says the Next button is shown only when the list has more than one entry. The code at 81-82 is `_authInfos.size() != 1 ? VISIBLE : INVISIBLE`, which also shows it for an empty list. Route unaffected, because step 23 requires a non-empty list. Fix: change the guard text to "Next is visible when the list size is not 1 (TransferEntriesActivity.java:81-82)". The performClick dispatch (View.java:6289-6296) is verified.

Step 26 (E930ed9ef, CALL): ERROR (text-only guard omission; route unaffected). TransferEntriesActivity.java:85 `if (_currentEntryCount < _authInfos.size())` gates generateQR() at 88. The edge has no guard. Route unaffected: the route's Next tap has a count below the size. Fix: add guard "_currentEntryCount < _authInfos.size() (TransferEntriesActivity.java:85)".

Step 27 (Ee0ce6c02, CALL): OK. TransferEntriesActivity.java:213 (`selectedEntry.getUri()`). The receiver's static type is the Transferable interface (instanceof checks at 198 and 201). The dispatch reaches GoogleAuthInfo$Export.getUri only when the selected entry is an Export, which this route needs; build getUri 400-462 and source 400-463 match.

Step 28 (Ea8a623d5, FRAMEWORK): UNCLEAR. The getUri part is verified (GoogleAuthInfo.java:459-460: builder.build().toByteArray() and the data parameter). The step into MigrationPayload.dynamicMethod is protobuf-lite runtime (INFERRED, source not read; rule 7). Fix: none.

Step 29 (E75a4904b, FRAMEWORK): UNCLEAR. protobuf-lite runtime (rule 7). Fix: none.

Step 30 (E00b93575, FRAMEWORK): UNCLEAR. protobuf-lite runtime and generated DigitCount (dataset, rule 7). Fix: none.

Step 31 (E6c7b88cc, LIFECYCLE): UNCLEAR. JVM class initialization of a generated class; the generated body is not in the source tree (rule 7). Fix: none.

Step 32 (Ec45d78f1, CALL): UNCLEAR. Generated DigitCountVerifier body (dataset, rule 7); the <init> endpoint cannot be checked from source. Fix: none.

Route-level result: steps 1-27 match the source; steps 24-26 need guard text (the route is unaffected); steps 28-32 are outside what can be checked here.

## Route 5: ScannerActivity.unbindPreview

Route as built: launcher tap (step 5), MainActivity onCreate/onStart (plain-text vault), the scan action (doShortcutActions), the camera permission, the scanner onCreate and camera bind, the camera switch tap, then unbindPreview. The route cannot reach the scan action as built: step 9 needs the intent extra action = "scan", and a launcher tap carries no extras. Steps 10-15 are reached only through step 9, and step 14 also needs a device with two lenses.

Tool note: the trace (r4g2_r5_route.txt, 15 steps, complete) was generated with the same in-memory trailing-comma fix as route 4. tools/show_route.py was not modified.

Step 1 (E14b4e906, ENTRY): OK. AndroidManifest.xml:21-27 (android:name=".AegisApplication"), as route 1 step 1.

Step 2 (E5b266140, LIFECYCLE): UNCLEAR. Hilt superclass, generated code not on disk (rule 7). Fix: none.

Step 3 (E1ef992ce, CALL): UNCLEAR. Hilt generated body (rule 7). Fix: none.

Step 4 (E88ed9829, ENTERS/page): OK. AegisApplicationBase.java:45-67; FW ActivityThread.java:5740.

Step 5 (E28ffc58c, ENTRY): OK as an edge. AndroidManifest.xml:44-51 (MAIN and LAUNCHER filter). A launcher tap carries no extras, so this entry cannot satisfy step 9's guard. See step 9.

Step 6 (Eb76444fd, LIFECYCLE): OK. MainActivity.java:192-194; FW ActivityThread.java:2729-2731, 2741.

Step 7 (E3a06baed, LIFECYCLE): OK. MainActivity.java:938-940; FW ActivityThread.java:2741.

Step 8 (E779a1da2, CALL): OK. The guard holds: the early returns are at 947 (intro, only when the vault is not initialised), 960 and 971 (read or load errors). Each is inside a branch this route does not take. The call at 1006 is reached after the block (999-1005 have no return). The encrypted-vault branch (963) falls through to startAuthActivity (976-977) and still reaches 1006, but doShortcutActions returns at 840-841 because the vault is not loaded. The cross-run need (a readable plain-text vault from an earlier run) is carried by step 9. Fix: none on this edge.

Step 9 (E01ce0942, CALL, STATE: vault loaded in this process and not locked since): ERROR (route-breaking; the route's entry does not meet the guard). Printed MainActivity.java:837-846: 840-841 return when action is null or the vault is not loaded; 845-846 "scan" calls startScanActivity. The guard text matches the code. But the step 5 launcher intent has no "action" extra, so getStringExtra returns null and doShortcutActions returns at 840-841. The state also needs an earlier run: a plain-text vault file must exist, written by IntroActivity.java:100 (initNew) and VaultManager.java:65 (repo.save()). The state text cites no writer, as in route 1 step 8. Fix: replace step 5 with the scanner tile entry: S_PROCESS -> LaunchScannerTileService.onClick (graph_def.py:317-318, ENV_QS), then LaunchScannerTileService.onClick -> MainActivity.<init> (graph_def.py:319-320). The tile intent sets action = scan (services/LaunchScannerTileService.java:33; ACTION_MAIN at 35). Keep steps 6-8. Add the writer citation to the STATE text. Note: the app shortcut (AegisApplicationBase.java:76-79, action = scan) also sets the extra, but graph_def.py has no ENTRY edge for it (grep for "shortcut" finds only the doShortcutActions edges), so it would need a new edge.

Step 10 (E4c53d66d, INTENT, ENV: camera permission granted): UNCLEAR. Guard verified: MainActivity.java:804-806 returns when PermissionHelper.request is false, and PermissionHelper.java:22-36 returns true only when nothing is denied (35). The launch at 809 goes through scanResultLauncher (androidx.activity.result, rule 7), so the dispatch to ScannerActivity.<init> is UNCLEAR, as in route 1 step 16. Fix: none on this edge.

Step 11 (Edd5d8048, LIFECYCLE): OK. ScannerActivity.java:53; FW ActivityThread.java:2729-2731, 2741.

Step 12 (Eea6435c6, FRAMEWORK): UNCLEAR. The guard holds: abortIfOrphan at ScannerActivity.java:55-57 returns false for a fresh launch (AegisActivity.java:155, null savedInstanceState), and the listener is registered at line 68, after that guard. The listener dispatch is INFERRED Guava ListenableFuture (rule 7; body not on disk). The build class lambda$onCreate$0 spans 70-88 (name verified). Fix: none.

Step 13 (E314fd012, ENTERS/page): ERROR (text-only claim; affects only a device with one lens). The guard matches: ScannerActivity.java:79-83 finish the page when no lens exists, and 84-87 set the lens and bind. But the edge text "the camera switch icon can be tapped" is not guaranteed. updateCameraIcon sets the icon visible only when dual (ScannerActivity.java:137-148; item.setVisible(dual) at 148), and dual needs two lenses. Fix: change the edge text to "the camera provider is ready and a lens exists", and move the two-lens condition to step 14.

Step 14 (Ef5aafb40, GUI, STATE: camera ready): ERROR (STATE text does not match its guard). The STATE says the camera provider is ready, a lens exists, and "the camera switch icon is set", and cites lines 70 and 79-88. Those lines do not show the icon is set. The icon is visible only with two lenses (ScannerActivity.java:137-148), and the guard text itself says "two lenses", but the STATE does not require them. Route affected: the switch can be tapped only on a device with two lenses (ENV). The toolbar tap dispatch to onOptionsItemSelected is androidx.appcompat (rule 7, not on disk); the body at 107-118 matches the edge text. Fix: change the STATE to "the camera provider is set and two lenses exist (ScannerActivity.java:137-148; the icon is visible only with two lenses)". Add ENV: a device with a front and a back camera.

Step 15 (Eb5012061, CALL): OK as an edge. ScannerActivity.java:108-110 (return when the provider is null), 112-113 (action_camera check, then unbindPreview(_cameraProvider)). The target ScannerActivity.unbindPreview is declared at ScannerActivity.java:169. The edge is reached only through step 14, so it is not on a valid route until step 14 is fixed.

Route-level result: step 9 is the break, and steps 10-15 are unreachable as built. With the tile entry (step 9 fix) and the two-lens STATE (step 14 fix), they become reachable. Step 10 needs the camera permission ENV, and steps 13-14 need a two-lens device. Steps 2-3 stay UNCLEAR (Hilt).

Counts for this route: OK 8 (1, 4, 5, 6, 7, 8, 11, 15), ERROR 3 (9, 13, 14), UNCLEAR 4 (2, 3, 10, 12).
