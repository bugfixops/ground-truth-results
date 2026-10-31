# Aegis route check, stage 5, group G3 (read-only)

Standard configuration: debug build, fresh install, API 27 emulator, no vault file and no icon pack at process start.
Sources: work/fw_src/android-8.1.0_r1 (framework), app source and compiled debug classes (bytecode read with a scratch classdump.py, since javap is unavailable).
Verdicts: OK = edge and guard confirmed; ERROR = edge or text wrong (FIX given); UNCLEAR = depends on androidx or another library not on disk (app side still checked).

| Route | Steps | OK | ERROR | UNCLEAR |
|---|---|---|---|---|
| 1. ImportExportPreferencesFragment$ExportResultListener.onTaskFinished | 55 | 38 | 8 | 9 |
| 2. GoogleAuthProtos$MigrationPayload$DigitCount$DigitCountVerifier.<init> | 32 | 20 | 3 | 9 |
| 3. IconPackExistsException.getIconPack | 30 | 21 | 3 | 6 |
| Total | 117 | 79 | 14 | 24 |

---

## Route 1: ImportExportPreferencesFragment$ExportResultListener.onTaskFinished (55 steps)

Totals: OK 38, ERROR 8, UNCLEAR 9.

The route starts with a fresh install, so the intro runs. The user imports an encrypted vault in the Welcome slide, then opens Settings, then Import/Export, then Export.

1. OK. Application class is `AegisApplication` (AndroidManifest.xml:22). FW ActivityThread.java:5713-5715 is the restricted-backup check that picks the base Application class, as the route says.
2. OK. `Hilt_AegisApplication.onCreate` runs first. AegisApplication.class names `Hilt_AegisApplication` as its superclass (constant pool). FW ActivityThread.java:5740 is `callApplicationOnCreate(app)`.
3. OK. Hilt_AegisApplication.class: onCreate L42 calls hiltInternalInject, L43 calls `AegisApplicationBase.onCreate`. The route's line 43 is correct.
4. OK. AegisApplicationBase.class onCreate L46-60 (super.onCreate, EarlyEntryPoints, receiver, lifecycle observer, cache clear, initAppShortcuts call at L60) matches source AegisApplicationBase.java:45-67.
5. OK. AndroidManifest.xml:44-51: MainActivity is exported, with the MAIN and LAUNCHER intent filter.
6. OK. FW ActivityThread.java:2729-2731 calls callActivityOnCreate. MainActivity.onCreate at source 193-194.
7. OK. FW ActivityThread.java:2741 is `activity.performStart()`. The route cites 2741, which is correct. An earlier note of a one-line drift (2742) was wrong. MainActivity.onStart at source 938-940.
8. OK. MainActivity bytecode: onStart L942 calls isVaultInitNeeded, L946 calls startIntroActivity, L947 returns. VaultManager.isVaultInitNeeded is `!isVaultLoaded() && !VaultRepository.fileExists()` (bytecode L227). A fresh install gives true.
9. OK. MainActivity.java:603-607 `startIntroActivity` launches IntroActivity through `introResultLauncher`, guarded by `!_isDoingIntro` (L604).
10. OK. IntroActivity.onCreate calls super.onCreate (bytecode L36) and adds the slides (source 35-41).
11. OK. IntroActivity.class onCreate L38 calls `addSlide(WelcomeSlide)`.
12. UNCLEAR. IntroBaseActivity.addSlide (bytecode L185-186) calls onBeforeSlideChanged and onAfterSlideChanged for the first slide, so the callback edge is confirmed. Whether the Welcome page is drawn depends on androidx ViewPager2, which is not on disk.
13. OK. WelcomeSlide.java:43-47 sets the click listener on btnImport (lambda$onCreateView$1, bytecode L44-46). FW View.java:6289-6296 `performClick` calls the listener.
14. UNCLEAR. ActivityResult callback dispatch belongs to androidx.activity.result, which is not on disk. App side: `vaultImportResultLauncher` is registered at WelcomeSlide.java:32-38 with callback lambda$new$0.
15. OK. lambda$new$0 calls `startImportVault(data.getData())` under the guard at WelcomeSlide.java:35-36 (bytecode L36).
16. OK. WelcomeSlide.startImportVault calls `ImportFileTask.execute(Lifecycle, ...)` at bytecode L95. ProgressDialogTask.java:69-74 calls `execute(params)`. FW AsyncTask.java:594-595 calls executeOnExecutor, which runs doInBackground.
17. OK. FW AsyncTask.java:691-697 `finish` calls onPostExecute when the task is not cancelled. ImportFileTask.java:53-56.
18. OK. ImportFileTask.onPostExecute calls the callback at L55. The callback is lambda$startImportVault$2 (WelcomeSlide.startImportVault bytecode L59 INDY).
19. OK. lambda$startImportVault$2: when `state.isEncrypted()` (WelcomeSlide.java:68-69), it calls `EncryptedState.decrypt(Context, DecryptListener)` (bytecode L69).
20. OK. AegisImporter.java:90 calls `Dialogs.showPasswordInputDialog` (bytecode L90).
21. OK. Dialogs.showPasswordInputDialog (5-arg) calls showTextInputDialog at Dialogs.java:271.
22. OK. Dialogs.java:226-229 OnShowListener disables OK and stores the button. `Dialogs.showSecureDialog` (Dialogs.java:66-69) calls `dialog.show()`, and FW Dialog.java:333 `sendShowMessage` runs the OnShowListener. The AppCompat AlertDialog subclass was not read; the FW Dialog base was used.
23. OK. OK click listener at Dialogs.java:231-235 (bytecode lambda$showTextInputDialog$7). FW View.java:6289-6296 `performClick` calls it. OK stays disabled until the text is non-empty (Dialogs.java:202-203).
24. ERROR. The listener at Dialogs.java:233 is `AegisImporter$EncryptedState.lambda$decrypt$1` (bytecode AegisImporter L90 INDY onTextInputResult), not `SecurityPreferencesFragment.lambda$onCreatePreferences$7`. The PIN keyboard at SecurityPreferencesFragment.java:157 is a different dialog and is not on the Welcome path.
   FIX: change the target to `AegisImporter$EncryptedState.lambda$decrypt$1`. New text: "the typed password goes to the import listener, which starts PasswordSlotDecryptTask". Justified by AegisImporter.java:90-93 and Dialogs.java:231-235.
25. ERROR. Wrong source, because it is the PIN lambda. The digits-only check (SecurityPreferencesFragment.java:158) does not apply to the import password.
   FIX: source `AegisImporter$EncryptedState.lambda$decrypt$1`. ASYNC edge to `PasswordSlotDecryptTask.doInBackground` via `task.execute(lifecycle, params)` at AegisImporter.java:108 (ProgressDialogTask.java:69-74). Text: "decrypt the password slots in a background task".
26. OK. PasswordSlotDecryptTask.onPostExecute (source 87-90) runs after doInBackground through FW AsyncTask.finish. The edge is valid for any caller. Its successor (step 27) is the part that changes.
27. ERROR. The callback is AuthActivity's `PasswordDerivationListener` (AuthActivity.java:173-174, 343-364), which belongs to the unlock screen. On the Welcome path the callback is the one built at AegisImporter.java:93 (bytecode INDY onTaskFinished, L93).
   FIX: target `AegisImporter$EncryptedState.lambda$decrypt$0`. Text: "the result goes to the import callback: null means 'Password incorrect'; otherwise build the credentials and decrypt". Justified by AegisImporter.java:93-105.
28. ERROR. AuthActivity.finish (source 295-311) is not on the import path, because AuthActivity is not opened during the intro.
   FIX: `AegisImporter$EncryptedState.lambda$decrypt$0` -> `WelcomeSlide$1.onStateDecrypted` (AegisImporter.java:100-101; the listener is set at WelcomeSlide.java:69-70). Then `WelcomeSlide$1.onStateDecrypted` -> `WelcomeSlide.importVault(File)` (WelcomeSlide.java:71-74).
29. ERROR. AuthActivity.finish -> MainActivity.lambda$new$0 is the unlock launcher. The Welcome path returns through IntroActivity instead.
   FIX: replace with this chain. (a) `WelcomeSlide.importVault` (WelcomeSlide.java:99-108): VaultRepository.writeToFile, `_imported = true`, `goToNextSlide()`. (b) `IntroBaseActivity.goToNextSlide` (SlideFragment.java:59-60; IntroBaseActivity.java:80-91): isFinished() returns true (SlideFragment.java:38-40), so onSaveIntroState stores `imported` and `creds` (WelcomeSlide.java:52-55) and setPagerPosition runs. (c) `IntroActivity.onBeforeSlideChanged` (IntroActivity.java:52-57) calls `skipToSlide(DoneSlide)`, so the intro jumps to DoneSlide (IntroBaseActivity.java:134-147, 104-110). (d) The user taps Next on DoneSlide (IntroBaseActivity.java:47), which calls goToNextSlide; on the last slide it calls onDonePressed (IntroBaseActivity.java:91). (e) `IntroActivity.onDonePressed`, imported branch: readVaultFile, loadFrom(vaultFile, creds), setIntroDone, setResult(RESULT_OK), finish (IntroActivity.java:107-129; bytecode L109, L117, L126, L128, L129). (f) MainActivity.introResultLauncher -> `lambda$new$1` (MainActivity.java:142-147).
   Note: the route has no steps for the import itself, the skip to DoneSlide, or the Done tap. Those are the missing steps this FIX adds.
30. ERROR. `MainActivity.lambda$new$0` is `authResultLauncher` (MainActivity.java:134-140). The intro result is `lambda$new$1` (MainActivity.java:142-147; bytecode L142-146): it sets `_isDoingIntro = false`, and on RESULT_OK calls onIntroResult.
   FIX: `MainActivity.lambda$new$1` -> `MainActivity.onIntroResult` (MainActivity.java:142-147, 752-754).
31. ERROR. onDecryptResult (MainActivity.java:797-801) records the vault-unlocked audit event, and the intro path does not. onIntroResult only calls loadEntries (MainActivity.java:752-754).
   FIX: `MainActivity.onIntroResult` -> `MainActivity.loadEntries` (MainActivity.java:753 -> 1133-1144). Remove the unlock audit event from this path.
32. OK. loadEntries (MainActivity.java:1133-1144; guard `!_loaded` at L1134) matches. Its predecessor changes with the FIX for steps 29-31.
33. UNCLEAR. The toolbar tap reaches onOptionsItemSelected through AppCompat, which is not on disk. App side checked: MainActivity.java:1086-1118.
34. OK. MainActivity.java:1088-1089: action_settings calls startPreferencesActivity().
35. OK. MainActivity.java:827 calls startPreferencesActivity(null, null).
36. OK. MainActivity.java:831-834 builds the Intent for PreferencesActivity and launches preferenceResultLauncher.
37. OK. PreferencesActivity.onCreate calls super.onCreate (bytecode L25; source 24). Lifecycle per FW ActivityThread.java:2729-2731.
38. OK. PreferencesActivity.class: L26 abortIfOrphan, L41 `new MainPreferencesFragment` (guard savedInstanceState == null, source 40).
39. UNCLEAR. The Fragment order (attach, then onCreatePreferences) is androidx.fragment/preference, not on disk. App side: MainPreferencesFragment.java:9-11 calls addPreferencesFromResource.
40. UNCLEAR. The list is drawn by androidx (not on disk). The XML rows were checked in res/xml/preferences.xml.
41. UNCLEAR. The androidx.preference callback dispatch (OnPreferenceStartFragmentCallback) is not on disk. App side: PreferencesActivity.java:19, 80-84.
42. OK. PreferencesActivity.onPreferenceStartFragment bytecode L81 calls `FragmentFactory.instantiate(ClassLoader, pref.getFragment())`. preferences.xml:38 names ImportExportPreferencesFragment, and the class has an `<init>()V`.
43. UNCLEAR. Fragment lifecycle (androidx) is not on disk. App side: PreferencesActivity.java:84, 91-97 (showFragment commits the transaction).
44. UNCLEAR. Preference click dispatch (androidx.preference) is not on disk. App side verified: onCreatePreferences bytecode L125-126 calls setOnPreferenceClickListener, and the INDY at L126 targets lambda$onCreatePreferences$9.
45. OK. lambda$onCreatePreferences$9 (bytecode L127) calls startExport().
46. OK. startExport: bytecode L209 setOnShowListener -> lambda$startExport$20; L332 showSecureDialog -> dialog.show(), which runs FW Dialog.java:333 sendShowMessage.
47. OK. lambda$startExport$20: bytecode L252 setOnClickListener -> lambda$startExport$17. The guards at L255 (encrypt or accept ticked) and L259-262 (group chosen) match source 252-265.
48. OK. lambda$startExport$17 (bytecode L277) calls `VaultManager.fireIntentLauncher(Fragment, Intent, ActivityResultLauncher)`. The launcher comes from getExportRequestLauncher (L276).
49. UNCLEAR. The result callback comes from androidx.activity.result, which is not on disk. App side: fireIntentLauncher calls launch (VaultManager bytecode L267), and exportResultLauncher is registered at ImportExportPreferencesFragment.java:82-83 with callback lambda$new$1 (bytecode INDY at L81). The ENV condition in the route is fine.
50. OK. lambda$new$1 (bytecode L83) calls `onExportResult(int, int, Intent)`.
51. OK. onExportResult returns early on null data, a non-RESULT_OK result, or a null URI (source 506-512). Bytecode L514 calls `startExportVault(...)`.
52. OK. startExportVault: bytecode L445 calls isEncryptionEnabled(), which is `_creds != null` (VaultRepository.java:352-354). The import sets creds through loadFrom, so this is true. L446 calls `StartExportCallback.exportVault` through an interface, and that object is lambda$onExportResult$26 (INDY at L514).
53. ERROR. The step says the export runs on a background thread, and it skips a call. In lambda$onExportResult$26 (bytecode L518-520; source 514-535), the temp file is created and the vault is written first, on the calling UI thread: `cb.exportVault(outStream)` runs lambda$startExportVault$22, which calls exportFiltered (L448) or export (L450). Only after that does `ExportTask.execute` (L535) start the background copy. ExportTask.doInBackground (ExportTask.java:28-38) only copies the temp file to the destination URI.
   FIX: split into two steps. (a) CALL lambda$onExportResult$26 -> lambda$startExportVault$22 (FinishExportCallback.exportVault at ImportExportPreferencesFragment.java:520; bytecode L520), then VaultRepository.export or exportFiltered (main thread; bytecode L448/L450). (b) ASYNC lambda$onExportResult$26 -> ExportTask.doInBackground via ExportTask.execute at ImportExportPreferencesFragment.java:535 (bytecode L535). This step runs only if the try block did not return: the catch at source 521-524 returns, so the execute is skipped on error. The route's guard text is correct.
54. OK. ExportTask.doInBackground -> onPostExecute through FW AsyncTask.finish (AsyncTask.java:691-697, calls onPostExecute when not cancelled). ExportTask.onPostExecute (bytecode L44-45).
55. OK. ExportTask.onPostExecute L45 calls Callback.onTaskFinished, which is ExportResultListener.onTaskFinished (bytecode L554-560: error dialog, or audit event and toast). ExportResultListener is created at ImportExportPreferencesFragment.java:535.

---

## Route 2: GoogleAuthProtos$MigrationPayload$DigitCount$DigitCountVerifier.<init> (32 steps)

Totals: OK 20, ERROR 3, UNCLEAR 9.

Plain summary: the route starts on a fresh install. The user opens Settings, then Import/Export, then the Google Authenticator style export. That export needs at least one TOTP or HOTP entry with SHA-1 and 6 digits (step 23). The last part of the route is the generated protobuf code that builds the export data (steps 27-32).

1. OK. AndroidManifest.xml:22 names AegisApplication as the app class. FW ActivityThread.java:5713-5715 picks the base Application class only for a backup or restore start, so a normal launch creates AegisApplication first.
2. OK. AegisApplication extends the Hilt-generated Hilt_AegisApplication (constant pool), and the system calls Application.onCreate at FW ActivityThread.java:5740.
3. OK. Hilt_AegisApplication.onCreate calls hiltInternalInject (L42), then AegisApplicationBase.onCreate (L43).
4. OK. AegisApplicationBase.onCreate runs super.onCreate, EarlyEntryPoints, the screen-off receiver, the lifecycle observer and the cache clear (bytecode L46-60; source AegisApplicationBase.java:45-67).
5. OK. AndroidManifest.xml:44-51 exports MainActivity with the MAIN and LAUNCHER filter, so a launcher tap starts it.
6. OK. The system calls Activity.onCreate after the constructor (FW ActivityThread.java:2729-2731). MainActivity.onCreate is at MainActivity.java:193-194.
7. OK. The system calls performStart after onCreate (FW ActivityThread.java:2741), which runs MainActivity.onStart (MainActivity.java:938-940).
8. ERROR. The edge needs a plain-text vault left by an earlier run. In the standard config there is no vault file, so isVaultInitNeeded() is true (VaultManager bytecode L227; MainActivity.java:942). onStart then starts the intro and returns (MainActivity.java:946-947), so the plain-text branch (MainActivity.java:951-974) and the call at line 992 never run.
   FIX: replace the edge with the standard path: CALL MainActivity.onStart -> MainActivity.startIntroActivity (MainActivity.java:942, 946; guard `!_isDoingIntro` at L604). The list is loaded when the intro returns: MainActivity.onIntroResult -> MainActivity.loadEntries (MainActivity.java:142-147, 752-754, 1133-1144), as route 1 steps 29-32 show. Keep the plain-text edge only as a second-launch path, outside the standard config. The intro itself is not traced in this route, and it leaves an empty vault, so step 23 still needs an entry.
9. OK. loadEntries fills the list when `_loaded` is false (MainActivity.java:1134; method at 1133-1144). The edge is right; its predecessor is fixed under step 8.
10. UNCLEAR. A toolbar tap reaches onOptionsItemSelected through AppCompat, which is not on disk. App side checked: MainActivity.java:1086-1118.
11. OK. action_settings calls startPreferencesActivity() (MainActivity.java:1088-1089).
12. OK. startPreferencesActivity() calls the two-argument version with nulls (MainActivity.java:827).
13. OK. The Intent for PreferencesActivity is built and launched through preferenceResultLauncher (MainActivity.java:831-834). The launcher's dispatch is androidx, but the app-side launch is confirmed (as route 1 step 36).
14. OK. PreferencesActivity.onCreate calls super.onCreate (bytecode L25; source 24), on the same system path as step 6.
15. OK. abortIfOrphan returns false (PreferencesActivity.java:26-27) and savedInstanceState is null (line 40), so `new MainPreferencesFragment()` runs (line 41).
16. UNCLEAR. The attach-then-build order (onCreatePreferences) is androidx.fragment and androidx.preference, not on disk. App side: MainPreferencesFragment.java:9-11 calls addPreferencesFromResource.
17. UNCLEAR. The list is drawn by androidx, not on disk. The rows are checked in res/xml/preferences.xml:8-44.
18. UNCLEAR. The tap dispatch to OnPreferenceStartFragmentCallback is androidx.preference, not on disk. App side: PreferencesActivity.java:19, 80-84.
19. OK. FragmentFactory.instantiate loads the class named in android:fragment (PreferencesActivity.java:81, bytecode L81; preferences.xml:38) and calls its constructor. ImportExportPreferencesFragment has `<init>()V`.
20. UNCLEAR. The list is built after the fragment attaches (androidx.fragment, not on disk). App side: showFragment commits the transaction (PreferencesActivity.java:91-97).
21. UNCLEAR. The row click goes through androidx.preference (not on disk). App side verified: the click listener at ImportExportPreferencesFragment.java:131-135 (bytecode L133) calls startGoogleAuthenticatorStyleExport and returns true.
22. OK. lambda$onCreatePreferences$10 calls startGoogleAuthenticatorStyleExport() directly (bytecode L133; source 133).
23. ERROR. The edge needs a non-empty export list, which needs at least one TOTP or HOTP entry with SHA-1 and 6 digits (ImportExportPreferencesFragment.java:357-363). In the standard config the vault is empty, so the list has zero entries. The code then shows a Toast and does not start TransferEntriesActivity (ImportExportPreferencesFragment.java:384-385). No step on this route creates an entry.
   FIX: add an in-route producer before step 23 (an entry must be added to the vault; the add-entry path is not traced in this stage), or mark this state as outside the standard config. Justified by ImportExportPreferencesFragment.java:384-390.
24. OK. TransferEntriesActivity.onCreate runs after construction (FW ActivityThread.java:2729-2731). The app's onCreate calls super.onCreate (bytecode L56) and abortIfOrphan (L57) (TransferEntriesActivity.java:55-57).
25. OK. The Next click listener is set at TransferEntriesActivity.java:84 (bytecode INDY, lambda$onCreate$0). The button shows when `_authInfos.size() != 1` (lines 81-82), so Next shows with two or more entries. The route's text "more than one entry" holds for every size that reaches this page (size 0 never gets here, see step 23).
26. ERROR. The edge omits a guard. In lambda$onCreate$0, generateQR() (line 88) runs only when `_currentEntryCount < _authInfos.size()` (line 85). The else branch calls finish() (line 94). Bytecode: L85 List.size, L88 generateQR, L94 finish.
   FIX: add the guard `_currentEntryCount < _authInfos.size()` (TransferEntriesActivity.java:85) to the edge TransferEntriesActivity.lambda$onCreate$0 -> TransferEntriesActivity.generateQR. The else branch to finish (line 94) is a separate edge and is not on this route.
27. OK. generateQR calls `selectedEntry.getUri()` through the Transferable interface (TransferEntriesActivity.java:213; bytecode invokeinterface otp.Transferable.getUri). The list is typed ArrayList<GoogleAuthInfo.Export>, and Export implements Transferable (GoogleAuthInfo.java:331), so the call dispatches to Export.getUri.
28. UNCLEAR. The edge starts at the toByteArray call at GoogleAuthInfo.java:459 (after the Export class start at L331), which builds the payload. The step into MigrationPayload.dynamicMethod is made by the protobuf-lite runtime, which is not on disk. The generated class is on disk; the runtime that calls it is not. App side confirmed: builder.build().toByteArray().
29. UNCLEAR. MigrationPayload.dynamicMethod (MigrationPayload.class L1744-1792; newMessageInfo at L1764) gives the protobuf-lite runtime a message description. The runtime, not on disk, decides when it reads each OtpParameters message. The generated code has no direct invoke of OtpParameters (checked: its invokes are ordinal, the constructors, newMessageInfo, DefaultInstanceBasedParser, Byte.valueOf and UnsupportedOperationException).
30. UNCLEAR. OtpParameters.dynamicMethod (L1137-1185; newMessageInfo at L1157) builds an Object[] of field names (secret_, name_, issuer_, algorithm_, digits_, type_, counter_) plus the info string and default-instance references (constant scan of the bytecode). It has no invoke or class constant of DigitCount, and no call to DigitCount.internalGetVerifier appears in the five GoogleAuthProtos classes checked. The link to the DigitCount verifier is made inside the protobuf-lite runtime (not on disk), so it cannot be confirmed statically. The edge text ("the runtime gets the DigitCount verifier") is consistent with that, so no FIX is needed for the text.
31. OK. DigitCount.internalGetVerifier returns the static INSTANCE of DigitCountVerifier (getstatic, bytecode check). Reading a static field triggers class initialization (JLS 12.4.1), so DigitCountVerifier.<clinit> runs at the first read.
32. OK. DigitCountVerifier.<clinit> creates the singleton with `new` and invokespecial <init> (bytecode L268), and <init> calls Object.<init> (L266). The chain ends at the constructor, as the route states.

---

## Route 3: IconPackExistsException.getIconPack (30 steps)

Totals: OK 21, ERROR 3, UNCLEAR 6.

Plain summary: fresh install, then Settings, then Icon packs, then the add button and the file picker. getIconPack is reached only when an icon pack with the same name already exists (steps 29-30). Steps 1-7 and 9-18 match route 2 steps 1-7 and 9-18 (same edges and evidence).

1. OK. Same as route 2 step 1 (AndroidManifest.xml:22; FW ActivityThread.java:5713-5715).
2. OK. Same as route 2 step 2 (FW ActivityThread.java:5740).
3. OK. Same as route 2 step 3 (Hilt_AegisApplication.onCreate, L42-43).
4. OK. Same as route 2 step 4 (AegisApplicationBase.onCreate, bytecode L46-60).
5. OK. Same as route 2 step 5 (AndroidManifest.xml:44-51).
6. OK. Same as route 2 step 6 (FW ActivityThread.java:2729-2731).
7. OK. Same as route 2 step 7 (FW ActivityThread.java:2741; MainActivity.onStart).
8. ERROR. The edge needs a plain-text vault from an earlier run. It is not in the standard config (see route 2 step 8: isVaultInitNeeded() is true, and onStart returns at MainActivity.java:947).
   FIX: replace the edge with CALL MainActivity.onStart -> MainActivity.startIntroActivity (MainActivity.java:942, 946), and load the list through MainActivity.onIntroResult -> MainActivity.loadEntries (MainActivity.java:752-754, 1133-1144), as in route 1 steps 29-32. The plain-text edge stays a second-launch path, outside the standard config.
9. OK. Same as route 2 step 9 (loadEntries, `_loaded` guard at MainActivity.java:1134).
10. UNCLEAR. Same as route 2 step 10 (AppCompat not on disk; MainActivity.java:1086-1118).
11. OK. Same as route 2 step 11 (MainActivity.java:1088-1089).
12. OK. Same as route 2 step 12 (MainActivity.java:827).
13. OK. Same as route 2 step 13 (MainActivity.java:831-834).
14. OK. Same as route 2 step 14 (PreferencesActivity.onCreate, source 24).
15. OK. Same as route 2 step 15 (PreferencesActivity.java:26-27, 40-41).
16. UNCLEAR. Same as route 2 step 16 (androidx.fragment not on disk; MainPreferencesFragment.java:9-11).
17. UNCLEAR. Same as route 2 step 17 (rows drawn by androidx; preferences.xml:8-44).
18. UNCLEAR. Same as route 2 step 18 (androidx.preference callback; PreferencesActivity.java:19, 80-84).
19. OK. FragmentFactory.instantiate loads IconPacksManagerFragment (PreferencesActivity.java:81, bytecode L81; preferences.xml:20 names it). The class constructor calls super(R.layout.fragment_icon_packs) at IconPacksManagerFragment.java:65.
20. UNCLEAR. The view is built from the layout and onViewCreated runs (androidx.fragment, not on disk). App side: IconPacksManagerFragment.java:65, 69.
21. OK. The add button's click listener is set at IconPacksManagerFragment.java:70-71 (bytecode INDY, lambda$onViewCreated$1). performClick (FW View.java:6289-6296) calls it.
22. OK. lambda$onViewCreated$1 calls startImportIconPack() directly (bytecode L71; source 71).
23. OK. startImportIconPack calls _vaultManager.fireIntentLauncher(this, intent, importResultLauncher) (IconPacksManagerFragment.java:175; bytecode L175). That sets setBlockAutoLock and launches the picker (VaultManager.java:263-269; launch at L267).
24. UNCLEAR. The file picker's result callback is androidx.activity.result, not on disk. App side: importResultLauncher is registered at IconPacksManagerFragment.java:56-62 with callback lambda$new$0 (bytecode INDY at L57).
25. OK. lambda$new$0 calls importIconPack(data.getData()) only when RESULT_OK, data is non-null and getData() is non-null (IconPacksManagerFragment.java:59-60).
26. ERROR (note text only). The edge is correct: importIconPack calls task.execute(getLifecycle(), Params) at IconPacksManagerFragment.java:155, which runs ProgressDialogTask.execute (ProgressDialogTask.java:69-74) and then AsyncTask.execute to doInBackground. But the note "ProgressDialogTask.execute (IconPacksManagerFragment.java:155) is skipped on purpose" is false. Bytecode L155 is an unconditional invokevirtual ImportIconPackTask.execute(Lifecycle,Object[]), and no guard surrounds line 155 (source 133-155).
   FIX: delete the note. Replace it with: "ProgressDialogTask.execute at IconPacksManagerFragment.java:155 runs unconditionally, so doInBackground runs for every import."
27. OK. ImportIconPackTask.onPostExecute runs after doInBackground through AsyncTask.finish (AsyncTask.java:691-697, which calls onPostExecute when not cancelled; ImportIconPackTask.java:54).
28. OK. onPostExecute calls _cb.onTaskFinished(result) (ImportIconPackTask.java:56). The callback is the lambda created at IconPacksManagerFragment.java:134 (bytecode INDY, lambda$importIconPack$5).
29. ERROR. The edge is correct: the Yes click at IconPacksManagerFragment.java:141 is wired in lambda$importIconPack$5 to lambda$importIconPack$4. But its STATE is not reachable in the standard config. The exists result is only produced when a pack is already installed (IconPackManager.java:85 packDir exists; :89 UUID exists). The standard config has no icon pack at process start, and IconPackManager rescans the folder only in its constructor (IconPackManager.java:30-33). No step on this route installs a pack first, so the exists dialog never shows.
   FIX: add in-run producer steps before step 29: a first successful import (IconPacksManagerFragment.java:151, `_adapter.addIconPack`), then a second import of the same pack that throws IconPackExistsException (IconPackManager.java:85 or :89). Otherwise mark the state as outside the standard config.
30. OK. The Yes lambda calls ((IconPackExistsException) e).getIconPack() directly (IconPacksManagerFragment.java:142; bytecode L142). IconPackExistsException.getIconPack returns the stored pack (`return _pack;`).

---

---

