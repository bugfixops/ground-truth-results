# Stage 5 route check, group G4 (Aegis, schema 2)

Read-only check of 5 routes in graphs/Aegis/graph_def.py against final_java_only/Aegis/app/Aegis-#v3.4.2 (v3.4.2) and fw_src/android-8.1.0_r1. Standard configuration as in the brief (debug build, fresh install, API 27, no vault file at process start, no icon pack).

Verdicts: OK, ERROR, UNCLEAR. Where a route reaches a page only through an earlier broken step, the page step is marked ERROR, and the steps after it are judged on their own edges with a route note.

## Route 1: Dialogs.lambda$showPartialGoogleAuthImportWarningDialog$30

Route note: the route runs S_ENTRY, then MainActivity.onStart, then S_LIST, then the FAB menu, then the image picker, then QR decode, then the partial-import warning, then "Show error details". Step 8 is the root error: the route's only producer of a loaded vault is a plain-text vault file from an earlier run, which the standard configuration does not have. Steps 10 to 24 are judged on their own edges and are reachable only after the step 8 fix.

Step 1 (Eb9515d18, S_ENTRY -> AegisApplication.<init>, ENTRY/standard): OK. AndroidManifest.xml:21-22 names .AegisApplication, and the framework builds it unless restrictedBackupMode is set (ActivityThread.java:5713-5715), which a normal launch does not set.

Step 2 (E5b266140, AegisApplication.<init> -> Hilt_AegisApplication.onCreate, LIFECYCLE/standard): UNCLEAR. Hilt_AegisApplication is generated and not on disk. App side: AegisApplication.java:5-6 is @HiltAndroidApp, extends AegisApplicationBase and has no onCreate. The framework call to Application.onCreate is ActivityThread.java:5740 (checked).

Step 3 (E1ef992ce, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate, CALL/explicit): UNCLEAR. The generated body is not on disk, so it cannot be confirmed that it calls super.onCreate(). The target AegisApplicationBase.java:44-47 has the onCreate that the edge names.

Step 4 (E88ed9829, AegisApplicationBase.onCreate -> S_PROCESS, ENTERS/page): OK. AegisApplicationBase.java:45-67 has no early return. The EarlyEntryPoints lookup (line 47) reads the EntryPoint declared at lines 116-120 in the app source.

Step 5 (E28ffc58c, S_PROCESS -> MainActivity.<init>, ENTRY/standard): OK. AndroidManifest.xml:44-51 is the MAIN/LAUNCHER activity, and it is the only LAUNCHER entry in the manifest (line 50).

Step 6 (Eb76444fd, MainActivity.<init> -> MainActivity.onCreate, LIFECYCLE/standard): OK. MainActivity.java:192-194 is onCreate, and the framework calls it at ActivityThread.java:2728-2731. performStart is the call at ActivityThread.java:2741, and its !mFinished guard is at 2740.

Step 7 (E3a06baed, MainActivity.onCreate -> MainActivity.onStart, LIFECYCLE/standard): OK. onCreate (MainActivity.java:192-264) never calls finish(), so the framework runs performStart (ActivityThread.java:2740-2741: the !mFinished guard at 2740, performStart at 2741).

Step 8 (E20e76e09, MainActivity.onStart -> MainActivity.loadEntries, CALL/explicit): ERROR. In the standard configuration there is no vault file, so VaultManager.isVaultInitNeeded() is true (VaultManager.java:226-228). onStart then starts the intro and returns (MainActivity.java:942-947). The plain-text branch (950-974) and the else at 991-992 need a vault file, which the standard configuration does not have, and nothing on this route produces one. The needs_state is a file from an earlier run, which the standard configuration excludes.
FIX: Replace E20e76e09 with the intro path, which is the only standard-configuration path to loadEntries. The intro edges already exist in graph_def.py (MainActivity.onStart -> startIntroActivity at line 394; startIntroActivity -> IntroActivity through introResultLauncher at line 476). The route should be: (a) MainActivity.onStart -> MainActivity.startIntroActivity, CALL, guard "isVaultInitNeeded() is true and _isDoingIntro is false" (MainActivity.java:942-947, 603-604; VaultManager.java:226-228). (b) startIntroActivity -> IntroActivity, INTENT (MainActivity.java:605-606). (c) IntroActivity finishes with RESULT_OK after onDonePressed, which calls _vaultManager.initNew(creds) (IntroActivity.java:84-101, 128-129; VaultManager.java:59-68, which saves the file and sets _repo). The intro security choice does not change this; either choice loads the vault through initNew. (d) introResultLauncher with RESULT_OK -> MainActivity.onIntroResult -> MainActivity.loadEntries (MainActivity.java:142-148, 752-754). Remove the needs_state (a plain-text vault from an earlier run). The loaded-vault state is produced by the intro on this route.

Step 9 (E1ffae3d8, MainActivity.loadEntries -> S_LIST, ENTERS/page): ERROR. loadEntries needs a loaded vault (VaultManager.getVault() throws when none is loaded, VaultManager.java:231-233). The only loader on this route is step 8, which the standard configuration cannot reach, so S_LIST is reached without its precondition.
FIX: No change to this edge. It is valid once step 8 is replaced as above: loadEntries then runs after the intro has loaded the vault, and its guard "_loaded is false" holds (MainActivity.java:1134, set false in onCreate at line 198).

Step 10 (E2e3490fc, S_LIST -> FabMenuHelper.lambda$setupClickListeners$0, GUI/standard): OK on its own edge. The FAB listener is set in the FabMenuHelper constructor (MainActivity.java:258; FabMenuHelper.java:47, 55). It is reachable only after the step 8 fix, because S_LIST comes through step 9.

Step 11 (Eebad02db, FabMenuHelper.lambda$setupClickListeners$0 -> FabMenuHelper.toggle, CALL/explicit): OK. FabMenuHelper.java:55 calls toggle() (bytecode desc (View) matches).

Step 12 (E554aee35, FabMenuHelper.toggle -> FabMenuHelper.open, CALL/explicit): OK. toggle() (FabMenuHelper.java:68-74) calls open() in the else branch when _isOpen is false, which holds for a closed menu.

Step 13 (E75d0fba5, FabMenuHelper.open -> FabMenuHelper.lambda$setupClickListeners$2, FRAMEWORK/standard): OK. The item listener is set once in the constructor (FabMenuHelper.java:58-64). The items are GONE until open() makes the container and the items VISIBLE (FabMenuHelper.java:40-45, 89, 163-164), so a tap on an item happens only while the menu is open.

Step 14 (E4fb13bc8, lambda$setupClickListeners$2 -> MainActivity.startScanImageActivity, CALL/non_standard): OK. FabMenuHelper.java:60-63 runs the Runnable for the tapped view. The map value for fab_menu_item_scan_image is this::startScanImageActivity (MainActivity.java:255), which is non-null (bytecode desc (Runnable, View)).

Step 15 (Ef0ebbe1d, MainActivity.startScanImageActivity -> VaultManager.fireIntentLauncher@QR_SCAN, CALL/explicit): OK. MainActivity.java:812-823 builds the chooser and calls fireIntentLauncher with codeScanResultLauncher; fireIntentLauncher calls resultLauncher.launch (VaultManager.java:243-247).

Step 16 (E6d7a279a, fireIntentLauncher@QR_SCAN -> MainActivity.lambda$new$7, RESULT/standard): OK. The picker's result goes to the registered launcher callback (MainActivity.java:185-186; the framework delivers results at ActivityThread.java:4253-4265). The env text is incomplete for steps 18 and 24; see those fixes.

Step 17 (E909f3342, MainActivity.lambda$new$7 -> MainActivity.onScanImageResult, CALL/explicit): OK. The call sits in an if (MainActivity.java:187-188: RESULT_OK and data non-null). A picker result satisfies both. The edge text does not record this guard; adding it is optional.

Step 18 (Efe7a2f07, MainActivity.onScanImageResult -> MainActivity.startDecodeQrCodeImages, CALL/explicit): ERROR. The cited call (line 657) is in the ClipData branch. onScanImageResult returns early when intent.getData() is non-null (MainActivity.java:640-643), and line 657 runs only when getData() is null and the ClipData holds URIs (lines 645-658). The edge has no guard, so the route is wrong for a single pick, which uses line 641 instead.
FIX: On Efe7a2f07, add guard "intent.getData() is null and intent.getClipData() holds at least one URI" (MainActivity.java:640, 645-657). On E6d7a279a (the step 16 env text), change it to "the user multi-selects several images in the chooser; the picker returns them as ClipData with no single data URI" (MainActivity.java:640-659). Whether a picker returns ClipData with a null data URI is picker behaviour that is not on disk, so the route depends on it.

Step 19 (E5f504038, MainActivity.startDecodeQrCodeImages -> QrDecodeTask.doInBackground, ASYNC/standard): OK. startDecodeQrCodeImages has no early return before task.execute(getLifecycle(), uris) (MainActivity.java:726). ProgressDialogTask.execute (ProgressDialogTask.java:69-74) calls AsyncTask.execute, which runs doInBackground on the worker thread (framework AsyncTask.java:594-595, 632-634).

Step 20 (Ee9441d1b, QrDecodeTask.doInBackground -> QrDecodeTask.onPostExecute, ASYNC/standard): OK. The framework finish() calls onPostExecute unless isCancelled() (AsyncTask.java:691-697). Nothing on this route cancels the task; the ProgressDialogTask lifecycle observer only dismisses the dialog on pause (ProgressDialogTask.java:84-90).

Step 21 (Ee5a5ce24, QrDecodeTask.onPostExecute -> MainActivity.lambda$startDecodeQrCodeImages$18, CALL/non_standard): OK. QrDecodeTask.java:53 calls _cb.onTaskFinished, and the callback is the lambda at MainActivity.java:669 (bytecode desc (List uris, List results) matches).

Step 22 (E01df91ec, MainActivity.lambda$startDecodeQrCodeImages$18 -> Dialogs.showPartialGoogleAuthImportWarningDialog, CALL/explicit): OK. The guard holds on a route whose picked files form a single-batch partial Google Auth export: googleAuthExports non-empty, single batch, missing indices non-empty (MainActivity.java:700-712). The input requirement belongs in the step 16 env text (see the step 24 fix).

Step 23 (Ebe1d9340, Dialogs.showPartialGoogleAuthImportWarningDialog -> Dialogs.lambda$showPartialGoogleAuthImportWarningDialog$31, FRAMEWORK/standard): OK. Dialogs.java:570 sets the OnShowListener, then showSecureDialog calls dialog.show() (Dialogs.java:580, 66-69). The framework Dialog.show() sends the show message (fw_src Dialog.java:288-333, 392-395), so the listener runs. This is settled from framework source, not inferred.

Step 24 (Eec40a496, Dialogs.lambda$showPartialGoogleAuthImportWarningDialog$31 -> Dialogs.lambda$showPartialGoogleAuthImportWarningDialog$30, FRAMEWORK/standard): ERROR. The neutral button exists only when scanningErrors is non-empty (Dialogs.java:565-567), and this edge taps that button. On this route the errors list is filled only from the picked files (MainActivity.java:675-677, 694-695). A single pick cannot yield both errors and a Google Auth export, because each result goes to one list (MainActivity.java:674-697). So the dialog at line 712 can show errors only when at least two files are picked, one of which is unreadable or not a Google Auth QR. The route's env text does not say so.
FIX: On E6d7a279a (step 16 env), change it to "the user multi-selects at least two images: one single-batch Google Auth export QR with missing batch indices, and at least one image that cannot be decoded or is not an otpauth or migration QR, so that errors is non-empty" (MainActivity.java:674-697, 700-712). The guard text on Eec40a496 is correct as written (Dialogs.java:565-567).

Route 1 table: 24 steps. OK 18, ERROR 4 (steps 8, 9, 18, 24), UNCLEAR 2 (steps 2, 3).

## Route 2: Dialogs.lambda$showDetailedMultiErrorDialog$22

Route note: the route is Settings, then Security, then the pin keyboard switch, then a password dialog, then the Authy decrypt listener, then the import result, then the multi-error dialog, then Details, then Copy. Steps 1-9 use the same edges as route 1, so their verdicts and the step 8 fix match route 1. Step 21 needs an encrypted vault, so the step 8 fix must choose a password at intro for this route. Step 26 is the root of the second error. Steps 27-35 are judged on their own edges.

Step 1 (Eb9515d18, S_ENTRY -> AegisApplication.<init>, ENTRY/standard): OK. Same as route 1 step 1 (AndroidManifest.xml:21-22).

Step 2 (E5b266140, AegisApplication.<init> -> Hilt_AegisApplication.onCreate, LIFECYCLE/standard): UNCLEAR. Same as route 1 step 2. The Hilt-generated class is not on disk.

Step 3 (E1ef992ce, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate, CALL/explicit): UNCLEAR. Same as route 1 step 3. The generated body is not on disk.

Step 4 (E88ed9829, AegisApplicationBase.onCreate -> S_PROCESS, ENTERS/page): OK. AegisApplicationBase.java:45-67 has no early return.

Step 5 (E28ffc58c, S_PROCESS -> MainActivity.<init>, ENTRY/standard): OK. AndroidManifest.xml:44-51; the only LAUNCHER entry is line 50.

Step 6 (Eb76444fd, MainActivity.<init> -> MainActivity.onCreate, LIFECYCLE/standard): OK. MainActivity.java:192-194; framework ActivityThread.java:2728-2731.

Step 7 (E3a06baed, MainActivity.onCreate -> MainActivity.onStart, LIFECYCLE/standard): OK. onCreate does not call finish(); framework ActivityThread.java:2740-2741 (the !mFinished guard at 2740, performStart at 2741).

Step 8 (E20e76e09, MainActivity.onStart -> MainActivity.loadEntries, CALL/explicit): ERROR. Same root as route 1 step 8. In a standard run there is no vault file, so onStart starts the intro and returns (MainActivity.java:942-947; VaultManager.java:226-228). The plain-text branch (950-974) needs a file from an earlier run.
FIX: Same as route 1 step 8: replace E20e76e09 with the intro path (graph_def.py:394 startIntroActivity; graph_def.py:476 INTENT to IntroActivity; MainActivity.java:142-148 and 752-754; IntroActivity.java:84-101 and 128-129; VaultManager.java:59-68). For this route the intro must choose a password (see step 21). Remove the needs_state.

Step 9 (E1ffae3d8, MainActivity.loadEntries -> S_LIST, ENTERS/page): ERROR. Dependent on step 8. VaultManager.getVault() throws when no vault is loaded (VaultManager.java:231-233).
FIX: No change on this edge beyond the step 8 fix. It is valid after that fix.

Step 10 (E887b87bf, S_LIST -> MainActivity.onOptionsItemSelected, GUI/standard): OK. menu_main.xml:50-52 has action_settings; onCreateOptionsMenu (MainActivity.java:1011-1013) inflates menu_main; the handler is at 1086-1089. Reached only after the step 8 fix.

Step 11 (Ef4e32054, MainActivity.onOptionsItemSelected -> MainActivity.startPreferencesActivity(), CALL/explicit): OK. MainActivity.java:1088-1089.

Step 12 (Ef64f95ee, startPreferencesActivity() -> startPreferencesActivity(Class,String), CALL/explicit): OK. MainActivity.java:827.

Step 13 (E640fb9eb, startPreferencesActivity(Class,String) -> PreferencesActivity.<init>, INTENT/standard): OK. MainActivity.java:831-834 builds the Intent and calls preferenceResultLauncher.launch; the launcher is registered at 166-167.

Step 14 (E94201299, PreferencesActivity.<init> -> PreferencesActivity.onCreate, LIFECYCLE/standard): OK. PreferencesActivity.java:24; the framework calls onCreate.

Step 15 (E50e3cfda, PreferencesActivity.onCreate -> MainPreferencesFragment.<init>, CALL/explicit): OK. PreferencesActivity.java:26-27 and 40-41. abortIfOrphan returns false when savedInstanceState is null (AegisActivity.java:154-156).

Step 16 (E382bc001, MainPreferencesFragment.<init> -> MainPreferencesFragment.onCreatePreferences, LIFECYCLE/standard): OK. This is the PreferenceFragmentCompat callback. The androidx source is not on disk. App side: MainPreferencesFragment.java:9-10.

Step 17 (Eccc3a740, MainPreferencesFragment.onCreatePreferences -> S_SETTINGS_MAIN, ENTERS/page): OK. MainPreferencesFragment.java:9-10; res/xml/preferences.xml:8-44.

Step 18 (E3452b602, S_SETTINGS_MAIN -> PreferencesActivity.onPreferenceStartFragment, GUI/standard): OK. PreferencesActivity.java:19 and 80-84; the Security row with android:fragment is res/xml/preferences.xml:25-29.

Step 19 (Ed19f3b08, PreferencesActivity.onPreferenceStartFragment -> SecurityPreferencesFragment.<init>, CALL/non_standard reflection): OK. PreferencesActivity.java:81 instantiates the class named in res/xml/preferences.xml:26, which is SecurityPreferencesFragment.

Step 20 (E5c8f972e, SecurityPreferencesFragment.<init> -> SecurityPreferencesFragment.onCreatePreferences, LIFECYCLE/standard): OK. PreferencesActivity.java:84 and 91-97; androidx callback.

Step 21 (Eb2d49c8f, SecurityPreferencesFragment.onCreatePreferences -> SecurityPreferencesFragment.lambda$onCreatePreferences$9, FRAMEWORK/standard): ERROR. The change listener is lambda$onCreatePreferences$9 (method_list desc (Preference,Object)Z; SecurityPreferencesFragment.java:152-177). The switch is visible only when the vault is encrypted: SecurityPreferencesFragment.java:259 (encrypted = vault.isEncryptionEnabled()) and 265 (_pinKeyboardPreference.setVisible(encrypted)); preferences_security.xml:86 (android:dependency="pref_encryption"). A standard run that chose no security never shows the switch, so this change cannot happen. The guard names only "switch on".
FIX: On Eb2d49c8f, add to the guard: "the vault is encrypted (vault.isEncryptionEnabled() is true), so the pin switch is visible (SecurityPreferencesFragment.java:259, 265; preferences_security.xml:86)". For this route, the step 8 fix must choose a password at intro (not the no-security choice).

Step 22 (Eafa4c4f5, lambda$onCreatePreferences$9 -> Dialogs.showPasswordInputDialog, CALL/explicit): OK on its own edge. The call at SecurityPreferencesFragment.java:157 is in the body of lambda$onCreatePreferences$9 and matches the 5-argument overload (Dialogs.java:270-271). Reached only after the step 21 fix.

Step 23 (E62fef539, Dialogs.showPasswordInputDialog -> Dialogs.showTextInputDialog, CALL/explicit): OK. Dialogs.java:271.

Step 24 (E5bb67188, Dialogs.showTextInputDialog -> Dialogs.lambda$showTextInputDialog$8, FRAMEWORK/standard): OK. The OnShowListener at Dialogs.java:226-229 runs when the dialog is shown (framework Dialog.java:288-333 and 392-395; same mechanism as route 1 step 23).

Step 25 (Ec9266bec, Dialogs.lambda$showTextInputDialog$8 -> Dialogs.lambda$showTextInputDialog$7, FRAMEWORK/standard): OK. The click listener is at Dialogs.java:231-235. The OK button starts disabled (Dialogs.java:228) and the text watcher enables it only for non-empty text (Dialogs.java:203), so the guard holds.

Step 26 (E02b5fa3e, Dialogs.lambda$showTextInputDialog$7 -> AuthyImporter$EncryptedState.lambda$decrypt$0, CALL/non_standard): ERROR. Wrong listener. Dialogs.java:233 calls the listener that the caller passed in. On this route that caller is step 22, whose listener is SecurityPreferencesFragment.lambda$onCreatePreferences$7 (method_list desc ([C)V; SecurityPreferencesFragment.java:157-172), not the Authy listener. The Authy decrypt dialog is opened only by AuthyImporter$EncryptedState.decrypt (AuthyImporter.java:206-207), which runs only from ImportEntriesActivity.processImporterState (ImportEntriesActivity.java:176-179, state.decrypt). The pin switch never reaches it.
FIX (choose one): (a) If this route keeps the pin branch, change E02b5fa3e's target to SecurityPreferencesFragment.lambda$onCreatePreferences$7 (SecurityPreferencesFragment.java:157-172). The branch then ends at the password check (PasswordSlotDecryptTask) and cannot reach steps 27-35. (b) For this route's goal (multi-error Details and Copy), replace steps 10-26 with the import entry: ImportExportPreferencesFragment.onImportSelectResult (ImportExportPreferencesFragment.java:144-153; startImportEntriesActivity at 153) -> ImportEntriesActivity.processImporterState (ImportEntriesActivity.java:176-179) -> AuthyImporter$EncryptedState.decrypt (AuthyImporter.java:206-207) -> Dialogs.showPasswordInputDialog -> Dialogs.lambda$showTextInputDialog$7 -> E02b5fa3e, keeping the target AuthyImporter$EncryptedState.lambda$decrypt$0 (method_list desc (DecryptListener,[C)V). Option (b) matches the route's goal.

Step 27 (E15e02c9d, AuthyImporter$EncryptedState.lambda$decrypt$0 -> ImportEntriesActivity$2.onStateDecrypted, CALL/explicit): OK on its own edge. AuthyImporter.java:209-210 calls listener.onStateDecrypted, and ImportEntriesActivity$2 is the DecryptListener at ImportEntriesActivity.java:179-195. Guard: decrypt(password) does not throw (AuthyImporter.java:211-212 calls onError instead). Reached only after the step 26 fix.

Step 28 (Efdf9842a, ImportEntriesActivity$2.onStateDecrypted -> ImportEntriesActivity.processDecryptedImporterState, CALL/explicit): OK. ImportEntriesActivity.java:181-182.

Step 29 (Ece6b33ed, ImportEntriesActivity.processDecryptedImporterState -> ImportEntriesActivity.processImporterResult, CALL/explicit): OK. The guard holds: state.convert() errors return early (ImportEntriesActivity.java:207-213), and an empty icon map goes to the else branch at 230-231. A non-empty map uses the IconOptimizationTask callback (221-227), which is a separate path.

Step 30 (Eb9310dac, ImportEntriesActivity.processImporterResult -> Dialogs.showMultiExceptionDialog, CALL/explicit): OK. ImportEntriesActivity.java:245-248; the guard is errors.size() > 0 at 246.

Step 31 (Efbfd355a, Dialogs.showMultiExceptionDialog -> Dialogs.showMultiErrorDialog, CALL/explicit): OK. Dialogs.java:452 calls it. The signature at Dialogs.java:427-428 is (Context, int, String, List<CharSequence>, OnClickListener), which matches the call.

Step 32 (E5c7dbe16, Dialogs.showMultiErrorDialog -> Dialogs.lambda$showMultiErrorDialog$20, FRAMEWORK/standard): OK. The Details neutral button is always set (Dialogs.java:439-441) and the dialog goes through showSecureDialog (Dialogs.java:429-442). method_list desc (Context,int,List,OnClickListener,...) matches the captures.

Step 33 (E25822db8, Dialogs.lambda$showMultiErrorDialog$20 -> Dialogs.showDetailedMultiErrorDialog, CALL/explicit): OK. Dialogs.java:440; the method at 455-456 takes (Context, int, List<CharSequence>, OnClickListener), which matches.

Step 34 (E9e8ecab9, Dialogs.showDetailedMultiErrorDialog -> Dialogs.lambda$showDetailedMultiErrorDialog$23, FRAMEWORK/standard): OK. The OnShowListener is at Dialogs.java:476-484. The dialog is shown through showSecureDialog (Dialogs.java:486) and dialog.show() (Dialogs.java:66-69), and the framework runs the listener (Dialog.java:288-333, 392-395).

Step 35 (E47462230, Dialogs.lambda$showDetailedMultiErrorDialog$23 -> Dialogs.lambda$showDetailedMultiErrorDialog$22, FRAMEWORK/standard): OK. The Copy click is at Dialogs.java:478-483. method_list desc (Context, SpannableStringBuilder, View)V matches the captures.

Route 2 table: 35 steps. OK 29, ERROR 4 (steps 8, 9, 21, 26), UNCLEAR 2 (steps 2, 3).

## Route 3: AuthActivity.lambda$onCreate$3

Route note: the route runs S_ENTRY, then MainActivity.onStart, then the auth screen (AuthActivity), then the biometrics button, then the password-reminder dialog, whose OK button is the target. Step 8 is the root error: a standard fresh run has no encrypted vault file, so onStart takes the intro branch. Step 13 needs a biometric slot, and step 14 needs a password reminder that is due. Both depend on state that an earlier run produces, so the standard configuration does not reach the target. Steps 9-12 are judged on their own edges.

Step 1 (Eb9515d18, S_ENTRY -> AegisApplication.<init>, ENTRY/standard): OK. Same as route 1 step 1 (AndroidManifest.xml:21-22).

Step 2 (E5b266140, AegisApplication.<init> -> Hilt_AegisApplication.onCreate, LIFECYCLE/standard): UNCLEAR. Same as route 1 step 2. The Hilt-generated class is not on disk.

Step 3 (E1ef992ce, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate, CALL/explicit): UNCLEAR. Same as route 1 step 3. The generated body is not on disk.

Step 4 (E88ed9829, AegisApplicationBase.onCreate -> S_PROCESS, ENTERS/page): OK. AegisApplicationBase.java:45-67 has no early return.

Step 5 (E28ffc58c, S_PROCESS -> MainActivity.<init>, ENTRY/standard): OK. AndroidManifest.xml:44-51, the LAUNCHER entry.

Step 6 (Eb76444fd, MainActivity.<init> -> MainActivity.onCreate, LIFECYCLE/standard): OK. MainActivity.java:192-194; the framework calls onCreate at ActivityThread.java:2728-2731.

Step 7 (E3a06baed, MainActivity.onCreate -> MainActivity.onStart, LIFECYCLE/standard): OK. onCreate does not call finish(), so performStart runs (ActivityThread.java:2740-2741).

Step 8 (E57db524e, MainActivity.onStart -> MainActivity.startAuthActivity, CALL/explicit): ERROR. In a standard fresh run there is no vault file, so VaultManager.isVaultInitNeeded() is true (VaultManager.java:226-228). onStart takes the intro branch and returns (MainActivity.java:942-947). The only call to startAuthActivity from onStart is at 976-977, which needs an encrypted vault file from an earlier run, and the standard configuration has none. The STATE note on this edge is cross-run only.
FIX: Replace the cross-run STATE with a same-run path through the Lock action. In one standard run: intro (MainActivity.onStart -> startIntroActivity, MainActivity.java:942-947 and 603-609; onIntroResult at 752-754; VaultManager.initNew at VaultManager.java:59-68 creates the vault), then the list loads, then the Lock action (MainActivity.onOptionsItemSelected, action_lock at MainActivity.java:1093-1094) -> VaultManager.lock(true) (VaultManager.java:103-111; it calls each LockListener at 106-107) -> MainActivity.onLocked(true) (MainActivity.java:1348-1367; registered by AegisActivity.java:77) -> MainActivity.startAuthActivity(true) (MainActivity.java:1146-1153). Change E57db524e's source to MainActivity.onLocked with guard "userInitiated is true" (MainActivity.java:1362-1363). The lock-action edges (onOptionsItemSelected -> VaultManager.lock, VaultManager.lock -> onLocked) are not in this route's graph and must be added.

Step 9 (E06202b0e, MainActivity.startAuthActivity -> AuthActivity.<init>, INTENT/standard): OK. MainActivity.java:1146-1153 is guarded by !_isAuthenticating (line 1147) and launches the auth activity at 1150.

Step 10 (E0158aff6, AuthActivity.<init> -> AuthActivity.onCreate, LIFECYCLE/standard): OK. AuthActivity.java:73-195, called by the framework on creation (ActivityThread.java:2728-2731).

Step 11 (E911809ef, AuthActivity.onCreate -> AuthActivity.onResume, LIFECYCLE/standard): OK. The framework calls performResume (ActivityThread.java:3556 and 3621).

Step 12 (E87843ac5, AuthActivity.onResume -> S_AUTH, ENTERS/page): OK. AuthActivity.java:210-224 focuses the password field, so the auth page is shown.

Step 13 (E700eadaa, S_AUTH -> AuthActivity.lambda$onCreate$4, GUI/standard [ENV fingerprint enrolled][STATE biometric slot]): ERROR. The biometrics button is visible only when the vault has a BiometricSlot whose key is in the keystore (AuthActivity.java:132-150). A standard run uses a password intro, which creates no biometric slot. The STATE note says the slot was saved by an earlier intro run, which is cross-run state with no producer in this run.
FIX: Replace the STATE on E700eadaa with a same-run producer: the intro creates the biometric slot. SecuritySetupSlide.java:101 starts BiometricSlotInitializer, which creates the BiometricSlot (BiometricSlotInitializer.java:61). Keep the ENV: a fingerprint is enrolled and accepted by the sensor (BiometricsHelper.isAvailable, AuthActivity.java:132). The ENV is not part of the standard configuration, so this step stays ENV-dependent after the fix.

Step 14 (E552b9e69, AuthActivity.lambda$onCreate$4 -> AuthActivity.lambda$onCreate$3, FRAMEWORK/standard [STATE reminder due]): ERROR. The reminder dialog is shown from the biometrics click only when _prefs.isPasswordReminderNeeded() is true (AuthActivity.java:181). That check needs the time since the stored timestamp to be at least the interval (Preferences.java:138-145). The timestamp is set on the first Preferences construction (Preferences.java:64-65), and the default interval is BIWEEKLY, 14 days (Preferences.java:120-124; PassReminderFreq.getDurationMillis). In a fresh run the timestamp is now, so the reminder is not due and the else branch (AuthActivity.java:191-192) calls showBiometricPrompt directly. The dialog's OK click is the FRAMEWORK dispatch and is OK on its own. The positive button calls showBiometricPrompt at AuthActivity.java:187-189, which is lambda$onCreate$3.
FIX: Replace the STATE on E552b9e69 with an ENV: the device clock is moved forward by at least 14 days after the first run, so that isPasswordReminderNeeded() is true (Preferences.java:138-145). Resetting the timestamp after a password unlock (AuthActivity.java:353) does not change this, because the reset time is also "now".

Route 3 table: 14 steps. OK 9 (steps 1, 4, 5, 6, 7, 9, 10, 11, 12), ERROR 3 (steps 8, 13, 14), UNCLEAR 2 (steps 2, 3).

## Route 4: GoogleAuthImporter.readFromApp

Route note: the route runs S_ENTRY, then MainActivity, then Settings (PreferencesActivity), then the Import and export sub-page (ImportExportPreferencesFragment), then the "Import from another app" row, then the importer dialog, then ImportEntriesActivity (app import), then the root shell, then GoogleAuthImporter.readFromApp. Step 8 is the same root error as routes 1-3. Steps 21-22 open the wrong row: the route taps pref_import (the file import, isDirect false) where it needs pref_import_app (isDirect true). Step 24 depends on that fix. Steps 9 and 29-34 are described below.

Step 1 (Eb9515d18, S_ENTRY -> AegisApplication.<init>, ENTRY/standard): OK. AndroidManifest.xml:21-27.

Step 2 (E5b266140, AegisApplication.<init> -> Hilt_AegisApplication.onCreate, LIFECYCLE/standard): UNCLEAR. Same as route 1 step 2.

Step 3 (E1ef992ce, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate, CALL/explicit): UNCLEAR. Same as route 1 step 3.

Step 4 (E88ed9829, AegisApplicationBase.onCreate -> S_PROCESS, ENTERS/page): OK. AegisApplicationBase.java:45-67.

Step 5 (E28ffc58c, S_PROCESS -> MainActivity.<init>, ENTRY/standard): OK. AndroidManifest.xml:44-51.

Step 6 (Eb76444fd, MainActivity.<init> -> MainActivity.onCreate, LIFECYCLE/standard): OK. MainActivity.java:192-194; ActivityThread.java:2728-2731, 2741.

Step 7 (E3a06baed, MainActivity.onCreate -> MainActivity.onStart, LIFECYCLE/standard): OK. ActivityThread.java:2740-2741.

Step 8 (E20e76e09, MainActivity.onStart -> MainActivity.loadEntries, CALL/explicit): ERROR. Same root as route 1 step 8. The plain-text vault needs a file from an earlier run, and a standard fresh run takes the intro branch (MainActivity.java:942-947; VaultManager.java:226-228).
FIX: Same as route 1 step 8. Replace E20e76e09 with the intro path (graph_def.py:394 startIntroActivity; graph_def.py:476 INTENT to IntroActivity; MainActivity.java:142-148 and 752-754; IntroActivity.java:84-101 and 128-129; VaultManager.java:59-68). Remove the cross-run needs_state.

Step 9 (E1ffae3d8, MainActivity.loadEntries -> S_LIST, ENTERS/page): ERROR. Dependent on step 8. VaultManager.getVault() throws when no vault is loaded (VaultManager.java:231-233).
FIX: No change to this edge. It is valid once step 8 is fixed (MainActivity.java:1133-1144).

Step 10 (E887b87bf, S_LIST -> MainActivity.onOptionsItemSelected, GUI/standard): OK. MainActivity.java:1086-1089; reachable after the step 8 fix.

Step 11 (Ef4e32054, MainActivity.onOptionsItemSelected -> MainActivity.startPreferencesActivity(), CALL/explicit): OK. MainActivity.java:1088-1089.

Step 12 (Ef64f95ee, MainActivity.startPreferencesActivity() -> startPreferencesActivity(Class,String), CALL/explicit): OK. MainActivity.java:827.

Step 13 (E640fb9eb, startPreferencesActivity(Class,String) -> PreferencesActivity.<init>, INTENT/standard): OK. MainActivity.java:830-834.

Step 14 (E94201299, PreferencesActivity.<init> -> PreferencesActivity.onCreate, LIFECYCLE/standard): OK. PreferencesActivity.java:24.

Step 15 (E50e3cfda, PreferencesActivity.onCreate -> MainPreferencesFragment.<init>, CALL/explicit): OK. PreferencesActivity.java:26-27 and 40-41.

Step 16 (E382bc001, MainPreferencesFragment.<init> -> MainPreferencesFragment.onCreatePreferences, LIFECYCLE/standard): OK. PreferenceFragmentCompat callback; app side MainPreferencesFragment.java:9-10.

Step 17 (Eccc3a740, MainPreferencesFragment.onCreatePreferences -> S_SETTINGS_MAIN, ENTERS/page): OK. res/xml/preferences.xml:8-44.

Step 18 (E3452b602, S_SETTINGS_MAIN -> PreferencesActivity.onPreferenceStartFragment, GUI/standard): OK. The row tapped must be the Import and export row (preferences.xml:37-41); PreferencesActivity.java:80-84.

Step 19 (E63d9f2a4, PreferencesActivity.onPreferenceStartFragment -> ImportExportPreferencesFragment.<init>, CALL/non_standard reflection): OK. PreferencesActivity.java:81 creates the class named by preferences.xml:38. ImportExportPreferencesFragment.java:68 is a public class, and grep finds no explicit constructor in that file, so the framework uses the default public no-arg constructor.

Step 20 (E245f8b40, ImportExportPreferencesFragment.<init> -> ImportExportPreferencesFragment.onCreatePreferences, LIFECYCLE/standard): OK. PreferencesActivity.java:84 and 91-97.

Step 21 (E91eeed07, ImportExportPreferencesFragment.onCreatePreferences -> ImportExportPreferencesFragment.lambda$onCreatePreferences$6, FRAMEWORK/standard): ERROR. lambda$onCreatePreferences$6 is the click listener of pref_import (ImportExportPreferencesFragment.java:105-115), which is the file import and opens the dialog with isDirect false (line 107). The app import this route needs is the pref_import_app row, whose listener holds the isDirect true call at lines 119-121.
FIX: On E91eeed07, change the target to ImportExportPreferencesFragment.lambda$onCreatePreferences$8 and the label to "Tap Import from another app (pref_import_app)". The $8 name is INFERRED from post-order numbering (inner listener $7 at lines 119-121; outer listener $8), and method_list.json lists lambda$onCreatePreferences$8.

Step 22 (E5c464116, ImportExportPreferencesFragment.lambda$onCreatePreferences$6 -> Dialogs.showImportersDialog, CALL/explicit): ERROR. The call at ImportExportPreferencesFragment.java:107 passes isDirect false, which opens the file-import dialog, not the app-import dialog.
FIX: On E5c464116, change the source to ImportExportPreferencesFragment.lambda$onCreatePreferences$8 and add the guard "the call passes isDirect true (ImportExportPreferencesFragment.java:119)". The target Dialogs.showImportersDialog is unchanged.

Step 23 (Ebe22842e, Dialogs.showImportersDialog -> Dialogs.lambda$showImportersDialog$27, FRAMEWORK/standard): OK. Dialogs.java:536-538 is the positive button; the Material dispatch is INFERRED, as for the other routes.

Step 24 (E72c20578, Dialogs.lambda$showImportersDialog$27 -> ImportExportPreferencesFragment.lambda$onCreatePreferences$7, CALL/explicit): ERROR. Dependent on step 22. The guard "the dialog was opened by Import from another app (isDirect true)" is not met by the dialog the route opens at step 22 (isDirect false).
FIX: No change to E72c20578. It is correct once step 22 opens the dialog with isDirect true (listener at ImportExportPreferencesFragment.java:119-121).

Step 25 (Eca2b28fb, lambda$onCreatePreferences$7 -> ImportExportPreferencesFragment.startImportEntriesActivity, CALL/explicit): OK. ImportExportPreferencesFragment.java:120, with file null.

Step 26 (E3156c24c, startImportEntriesActivity -> ImportEntriesActivity.<init>, INTENT/standard): OK. ImportExportPreferencesFragment.java:161-165.

Step 27 (Ef8499dba, ImportEntriesActivity.<init> -> ImportEntriesActivity.onCreate, LIFECYCLE/standard): OK. ImportEntriesActivity.java:62.

Step 28 (E411f08d7, ImportEntriesActivity.onCreate -> ImportEntriesActivity.startImport, CALL/explicit): OK. ImportEntriesActivity.java:62-66 and 103-104; abortIfOrphan returns false when savedInstanceState is null (AegisActivity.java:154-157).

Step 29 (E7faea19a, ImportEntriesActivity.startImport -> ImportEntriesActivity.lambda$startImport$1, FRAMEWORK/standard): UNCLEAR. The warning opens only when importer.isInstalledAppVersionSupported() is false (ImportEntriesActivity.java:110-112). GoogleAuthImporter.isInstalledAppVersionSupported returns false when the package is missing (GoogleAuthImporter.java:44-45) and is true only for versionCode <= 5000100 (line 48). So this warning branch needs Google Authenticator to be absent or newer than 5000100. A supported version calls startImportApp directly (ImportEntriesActivity.java:111), an edge the graph does not have. The standard configuration does not say whether Google Authenticator is installed, so the verdict is UNCLEAR.
FIX (to resolve): state the ENV for this route, or add the missing edge ImportEntriesActivity.startImport -> startImportApp (ImportEntriesActivity.java:111) for a supported version.

Step 30 (Ee1e1ad6c, lambda$startImport$1 -> ImportEntriesActivity.startImportApp, CALL/explicit): OK. ImportEntriesActivity.java:119.

Step 31 (Ecf27001f, ImportEntriesActivity.startImportApp -> RootShellTask.doInBackground, ASYNC/standard): OK. task.execute(this) at ImportEntriesActivity.java:173 binds to AsyncTask.execute, because the activity is not a Lifecycle, so the ProgressDialogTask overload does not apply. RootShellTask extends ProgressDialogTask (RootShellTask.java:8), which extends AsyncTask (ProgressDialogTask.java:22). doInBackground is at RootShellTask.java:17-20.

Step 32 (E1de399e4, RootShellTask.doInBackground -> RootShellTask.onPostExecute, ASYNC/standard): OK. RootShellTask.java:23-25.

Step 33 (Efb3b152a, RootShellTask.onPostExecute -> ImportEntriesActivity.lambda$startImportApp$5, CALL/explicit): OK. RootShellTask.java:25 calls _cb.onTaskFinished; the callback is ImportEntriesActivity.java:144-172.

Step 34 (Ee74cd64a, ImportEntriesActivity.lambda$startImportApp$5 -> GoogleAuthImporter.readFromApp, CALL/explicit [ENV root]): UNCLEAR. The shell is a libsu root shell (RootShellTask.java:19). Without root, shell.isRoot() is false, so the code toasts and finishes (ImportEntriesActivity.java:149-153), and readFromApp is not reached. Root on the emulator is not part of the standard configuration. readFromApp also needs the package installed, because getAppPath throws NameNotFoundException (GoogleAuthImporter.java:34-37, 61), which is caught at ImportEntriesActivity.java:158-161.

Route 4 table: 34 steps. OK 25, ERROR 5 (steps 8, 9, 21, 22, 24), UNCLEAR 4 (steps 2, 3, 29, 34).

## Route 5: ImportExportPreferencesFragment.lambda$onImportSelectResult$11

Route note: the route runs S_ENTRY, then MainActivity, then Settings, then the Import and export sub-page, then the "Import" row (pref_import, the file import, isDirect false), then the system document picker, then onImportSelectResult, then the import task, then the task callback (the target). Step 8 is the same root error as routes 1-4, and step 9 depends on it. Steps 10-30 are judged on their own edges, and the file-import path (steps 21-25) is correct.

Step 1 (Eb9515d18): OK. Same as route 4 step 1.
Step 2 (E5b266140): UNCLEAR. Same as route 1 step 2.
Step 3 (E1ef992ce): UNCLEAR. Same as route 1 step 3.
Step 4 (E88ed9829): OK. AegisApplicationBase.java:45-67.
Step 5 (E28ffc58c): OK. AndroidManifest.xml:44-51.
Step 6 (Eb76444fd): OK. MainActivity.java:192-194.
Step 7 (E3a06baed): OK. ActivityThread.java:2740-2741.

Step 8 (E20e76e09, MainActivity.onStart -> MainActivity.loadEntries, CALL/explicit): ERROR. Same root as route 1 step 8 (cross-run plain-text vault; the standard fresh run takes the intro branch, MainActivity.java:942-947).
FIX: Same as route 1 step 8: replace E20e76e09 with the intro path (graph_def.py:394 and 476; MainActivity.java:142-148, 752-754; IntroActivity.java:84-101, 128-129; VaultManager.java:59-68). Remove the cross-run needs_state.

Step 9 (E1ffae3d8, MainActivity.loadEntries -> S_LIST, ENTERS/page): ERROR. Dependent on step 8 (VaultManager.java:231-233).
FIX: No change to this edge. It is valid once step 8 is fixed.

Steps 10-20 (E887b87bf, Ef4e32054, Ef64f95ee, E640fb9eb, E94201299, E50e3cfda, E382bc001, Eccc3a740, E3452b602, E63d9f2a4, E245f8b40): OK. Each edge matches the route 4 verdicts for the same steps (MainActivity.java:1086-1089, 827, 830-834; PreferencesActivity.java:24, 26-27, 40-41, 80-84; preferences.xml:38; ImportExportPreferencesFragment.java:68 default constructor). The reflection edge E63d9f2a4 is OK as in route 4 step 19.

Step 21 (E91eeed07, ImportExportPreferencesFragment.onCreatePreferences -> lambda$onCreatePreferences$6, FRAMEWORK/standard): OK. The pref_import listener (ImportExportPreferencesFragment.java:105-115) is the file import this route needs. The preference click dispatch is INFERRED (androidx source is not on disk).

Step 22 (E5c464116, lambda$onCreatePreferences$6 -> Dialogs.showImportersDialog, CALL/explicit): OK. ImportExportPreferencesFragment.java:107 passes isDirect false.

Step 23 (Ebe22842e, Dialogs.showImportersDialog -> Dialogs.lambda$showImportersDialog$27, FRAMEWORK/standard): OK. Dialogs.java:536-538.

Step 24 (E3fba437f, Dialogs.lambda$showImportersDialog$27 -> ImportExportPreferencesFragment.lambda$onCreatePreferences$5, CALL/explicit): OK. The listener at ImportExportPreferencesFragment.java:107-113 (body 108-112) sets _importerDef and starts the picker. The target is the isDirect false listener, which matches the dialog opened at step 22.

Step 25 (E63f82c4b, lambda$onCreatePreferences$5 -> VaultManager.fireIntentLauncher@SETTINGS_IMPORT, CALL/explicit): OK. ImportExportPreferencesFragment.java:112. VaultManager.java:243-252 blocks auto lock, then calls resultLauncher.launch.

Step 26 (Ebe3b8b81, fireIntentLauncher@SETTINGS_IMPORT -> ImportExportPreferencesFragment.lambda$new$0, RESULT/standard [ENV the user picks a file in the system document picker]): OK. The picker is ACTION_GET_CONTENT with type */* (ImportExportPreferencesFragment.java:110-111). The result goes to the importSelectResultLauncher callback, which is the first registration, lambda$new$0 (ImportExportPreferencesFragment.java:74-79). The ENV is a user choice in the picker, which the standard configuration allows.

Step 27 (E36289880, lambda$new$0 -> ImportExportPreferencesFragment.onImportSelectResult, CALL/explicit): OK. ImportExportPreferencesFragment.java:76-77, guarded by data != null.

Step 28 (E4770a1db, onImportSelectResult -> ImportFileTask.doInBackground@SETTINGS_IMPORT, ASYNC/standard): OK. ImportExportPreferencesFragment.java:144-158: the RESULT_OK and uri checks at 146-148, and task.execute(getLifecycle(), params) at 158, which reaches AsyncTask.execute through ProgressDialogTask.java:69-74.

Step 29 (E810536ac, ImportFileTask.doInBackground@SETTINGS_IMPORT -> ImportFileTask.onPostExecute@SETTINGS_IMPORT, ASYNC/standard): OK. ImportFileTask.java:27 and 53-55. The ProgressDialogTask pause observer only dismisses the dialog (ProgressDialogTask.java:84-90), so the result still arrives in the standard run.

Step 30 (Ed10f6640, ImportFileTask.onPostExecute@SETTINGS_IMPORT -> ImportExportPreferencesFragment.lambda$onImportSelectResult$11, CALL/explicit [STATE the import task was started in this run]): OK. ImportFileTask.java:55 calls _cb.onTaskFinished(result). The callback is the lambda at ImportExportPreferencesFragment.java:151-157 (method_list.json lists lambda$onImportSelectResult$11), and the state comes from steps 26-29 in the same run, not from an earlier run.

Route 5 table: 30 steps. OK 26, ERROR 2 (steps 8, 9), UNCLEAR 2 (steps 2, 3).

## Final table

| Route | Steps | OK | ERROR | UNCLEAR |
|---|---|---|---|---|
| 1. Dialogs.lambda$showPartialGoogleAuthImportWarningDialog$30 | 24 | 18 | 4 | 2 |
| 2. Dialogs.lambda$showDetailedMultiErrorDialog$22 | 35 | 29 | 4 | 2 |
| 3. AuthActivity.lambda$onCreate$3 | 14 | 9 | 3 | 2 |
| 4. GoogleAuthImporter.readFromApp | 34 | 25 | 5 | 4 |
| 5. ImportExportPreferencesFragment.lambda$onImportSelectResult$11 | 30 | 26 | 2 | 2 |
| Total | 137 | 107 | 18 | 12 |

<!-- END OF ROUTES -->
