# Route check G1 (Aegis, schema 2 ground truth, round 5)

Read-only check of the seven routes in graphs/Aegis/graph_def.py. Only this file was written.

Basis:
- Standard configuration: debug build, BuildConfig.TEST false, fresh install, API 27 emulator, default preferences, no vault file, no icon pack at process start.
- Sources: final_java_only Aegis app source, method_list.json, fw_src android-8.1.0_r1.
- Route listings were regenerated for this run (scratchpad g1_route*.txt). The shared scratchpad files r3.txt and r5.txt held other routes and were not used.
- Hilt and Dagger generated code is not on disk, so those edges are INFERRED and accepted on the generated naming. Lambda numbers follow post-order numbering, consistent with method_list.json (no class files on disk to confirm).
- Verdicts: OK = edge matches source or framework and its guard and state hold in the standard configuration. ERROR = a FIX is given. UNCLEAR = a reason is given.

---

## Route 1: GlideRequests.asBitmap (68 steps): OK 55, ERROR 13, UNCLEAR 0

1. Eb9515d18 ENTRY/standard: S_ENTRY -> AegisApplication.<init> [OK]
2. E5b266140 LIFECYCLE: AegisApplication.<init> -> Hilt_AegisApplication.onCreate [OK]
3. E1ef992ce CALL: Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate [OK]
4. E88ed9829 ENTERS: AegisApplicationBase.onCreate -> S_PROCESS [OK]
5. E28ffc58c ENTRY: S_PROCESS -> MainActivity.<init> (launcher) [OK]
6. Eb76444fd LIFECYCLE: MainActivity.<init> -> MainActivity.onCreate [OK]
7. E3a06baed LIFECYCLE: MainActivity.onCreate -> MainActivity.onStart [OK]
8. E0602e719 CALL: MainActivity.onStart -> MainActivity.startIntroActivity [OK]
9. E4ce5043a INTENT: MainActivity.startIntroActivity -> IntroActivity.<init> [OK]
10. E5e63fbe7 LIFECYCLE: IntroActivity.<init> -> IntroActivity.onCreate [OK]
11. E93598a00 CALL: IntroActivity.onCreate -> IntroBaseActivity.addSlide@IntroActivity [OK]
12. E1440feb8 ENTERS: IntroBaseActivity.addSlide@IntroActivity -> S_INTRO_WELCOME [OK]
13. Ee1d29ff8 GUI: S_INTRO_WELCOME -> WelcomeSlide.lambda$onCreateView$1 [OK] (env: other app's document picker returns a file, WelcomeSlide.java:43-47)
14. E3870f4a6 RESULT: WelcomeSlide.lambda$onCreateView$1 -> WelcomeSlide.lambda$new$0 [OK] (same env)
15. Ee4518b2e CALL: WelcomeSlide.lambda$new$0 -> WelcomeSlide.startImportVault [OK]
16. E4c857825 ASYNC: WelcomeSlide.startImportVault -> ImportFileTask.doInBackground@WELCOME [OK]
17. E3810e168 ASYNC: ImportFileTask.doInBackground@WELCOME -> ImportFileTask.onPostExecute@WELCOME [OK]
18. E87742878 CALL: ImportFileTask.onPostExecute@WELCOME -> WelcomeSlide.lambda$startImportVault$2 [OK]
19. E32137f46 CALL: WelcomeSlide.lambda$startImportVault$2 -> AegisImporter$EncryptedState.decrypt(Context,DecryptListener) [OK]
20. E71fa8be8 CALL: AegisImporter$EncryptedState.decrypt -> Dialogs.showPasswordInputDialog(...) [OK]
21. E62fef539 CALL: Dialogs.showPasswordInputDialog -> Dialogs.showTextInputDialog(...) [OK]
22. E5bb67188 FRAMEWORK: Dialogs.showTextInputDialog -> Dialogs.lambda$showTextInputDialog$8 [OK]
23. Ec9266bec FRAMEWORK: Dialogs.lambda$showTextInputDialog$8 -> Dialogs.lambda$showTextInputDialog$7 [OK]
24. E23a01370 CALL/non_standard: Dialogs.lambda$showTextInputDialog$7 -> SecurityPreferencesFragment.lambda$onCreatePreferences$7 [ERROR]
    FIX: edge E23a01370, dst: change SecurityPreferencesFragment.lambda$onCreatePreferences$7 to AegisImporter$EncryptedState.lambda$decrypt$1 (the TextInputListener). Guard: "password not empty" (Dialogs.java:203). Source: AegisImporter.java:90-109; Dialogs.java:231-233 (OK click calls listener.onTextInputResult at 233).
25. Ec5219d4f ASYNC: SecurityPreferencesFragment.lambda$onCreatePreferences$7 -> PasswordSlotDecryptTask.doInBackground [ERROR]
    FIX: edge Ec5219d4f, src: AegisImporter$EncryptedState.lambda$decrypt$1 -> PasswordSlotDecryptTask.doInBackground (task created in the lambda; task.execute at AegisImporter.java:108). The route follows the PIN path here, which is wrong; see the step 24 reroute. Source: AegisImporter.java:90-108.
26. Eba701841 ASYNC: PasswordSlotDecryptTask.doInBackground -> PasswordSlotDecryptTask.onPostExecute [OK]
27. E9f4b7d7f CALL: PasswordSlotDecryptTask.onPostExecute -> AuthActivity$PasswordDerivationListener.onTaskFinished [ERROR]
    FIX: edge E9f4b7d7f, dst: AuthActivity$PasswordDerivationListener.onTaskFinished -> AegisImporter$EncryptedState.lambda$decrypt$0 (PasswordSlotDecryptTask callback). Source: AegisImporter.java:93-105. AuthActivity never starts on this route.
28. Ef7f4f7c4 CALL: AuthActivity$PasswordDerivationListener.onTaskFinished -> AuthActivity.finish [ERROR]
    FIX: edge Ef7f4f7c4, replace with AegisImporter$EncryptedState.lambda$decrypt$0 -> WelcomeSlide DecryptListener.onStateDecrypted (listener.onStateDecrypted at AegisImporter.java:101; WelcomeSlide.java:71-74).
29. E8a12fac2 RESULT: AuthActivity.finish -> MainActivity.lambda$new$0 [ERROR]
    FIX: remove edge E8a12fac2 from the route. The import continues in WelcomeSlide.importVault (WelcomeSlide.java:73, 98-109). Source: WelcomeSlide.java:71-74, 98-109.
30. Ec3137a3c CALL: MainActivity.lambda$new$0 -> MainActivity.onDecryptResult [ERROR]
    FIX: remove edge Ec3137a3c (no AuthActivity result on this path). Source: MainActivity.java:134-140 (authResultLauncher).
31. E49a61ace CALL: MainActivity.onDecryptResult -> MainActivity.loadEntries [ERROR]
    FIX: remove edge E49a61ace (onDecryptResult is not reached on this path). Source: MainActivity.java:797-801.
32. E1ffae3d8 ENTERS: MainActivity.loadEntries -> S_LIST [ERROR]
    FIX: add precondition "vault loaded" to the route state, or add a producing step before this edge. loadEntries needs the loaded vault (MainActivity.java:1133-1144), which the route does not load before this point.
33. E887b87bf GUI: S_LIST -> MainActivity.onOptionsItemSelected [OK]
34. Ef4e32054 CALL: MainActivity.onOptionsItemSelected -> MainActivity.startPreferencesActivity() [OK]
35. Ef64f95ee CALL: MainActivity.startPreferencesActivity() -> MainActivity.startPreferencesActivity(Class,String) [OK]
36. E640fb9eb INTENT: MainActivity.startPreferencesActivity(Class,String) -> PreferencesActivity.<init> [OK]
37. E94201299 LIFECYCLE: PreferencesActivity.<init> -> PreferencesActivity.onCreate [OK]
38. E50e3cfda CALL: PreferencesActivity.onCreate -> MainPreferencesFragment.<init> [OK]
39. E382bc001 LIFECYCLE: MainPreferencesFragment.<init> -> MainPreferencesFragment.onCreatePreferences [OK]
40. Eccc3a740 ENTERS: MainPreferencesFragment.onCreatePreferences -> S_SETTINGS_MAIN [OK]
41. E3452b602 GUI: S_SETTINGS_MAIN -> PreferencesActivity.onPreferenceStartFragment [OK]
42. E63d9f2a4 CALL/non_standard (reflection, PreferencesActivity.java:81; res/xml/preferences.xml:38): PreferencesActivity.onPreferenceStartFragment -> ImportExportPreferencesFragment.<init> [OK]
43. E245f8b40 LIFECYCLE: ImportExportPreferencesFragment.<init> -> ImportExportPreferencesFragment.onCreatePreferences [OK]
44. E91eeed07 FRAMEWORK: ImportExportPreferencesFragment.onCreatePreferences -> ImportExportPreferencesFragment.lambda$onCreatePreferences$6 [OK]
45. E5c464116 CALL: ImportExportPreferencesFragment.lambda$onCreatePreferences$6 -> Dialogs.showImportersDialog [OK]
46. Ebe22842e FRAMEWORK: Dialogs.showImportersDialog -> Dialogs.lambda$showImportersDialog$27 [OK]
47. E72c20578 CALL: Dialogs.lambda$showImportersDialog$27 -> ImportExportPreferencesFragment.lambda$onCreatePreferences$7 [ERROR]
    FIX: edge E72c20578, dst: change ImportExportPreferencesFragment.lambda$onCreatePreferences$7 to ImportExportPreferencesFragment.lambda$onCreatePreferences$5 (showImportersDialog(false), listener at ImportExportPreferencesFragment.java:107-113). Guard: "isDirect = false" (ImportExportPreferencesFragment.java:107). Source: ImportExportPreferencesFragment.java:105-123. ($7 at lines 119-121 is the app-import listener with isDirect = true.)
48. Eca2b28fb CALL: ImportExportPreferencesFragment.lambda$onCreatePreferences$7 -> ImportExportPreferencesFragment.startImportEntriesActivity [ERROR]
    FIX: edge Eca2b28fb, replace with the file-import branch: lambda$onCreatePreferences$5 -> VaultManager.fireIntentLauncher (ImportExportPreferencesFragment.java:112) -> importSelectResultLauncher lambda$new$0 (ImportExportPreferencesFragment.java:74-78) -> onImportSelectResult (144-159) -> ImportFileTask callback lambda$onImportSelectResult$11 (151-157) -> startImportEntriesActivity (153).
49. E3156c24c INTENT: ImportExportPreferencesFragment.startImportEntriesActivity -> ImportEntriesActivity.<init> [ERROR]
    FIX: edge E3156c24c, field state: the file argument must come from the ImportFileTask result (ImportExportPreferencesFragment.java:153). The app-import call passes null (ImportExportPreferencesFragment.java:120). Source: ImportExportPreferencesFragment.java:120, 153.
50. Ef8499dba LIFECYCLE: ImportEntriesActivity.<init> -> ImportEntriesActivity.onCreate [OK]
51. Eff12cb12 FRAMEWORK: ImportEntriesActivity.onCreate -> ImportEntriesActivity.lambda$onCreate$0 [OK]
52. Eaa1a222c CALL: ImportEntriesActivity.lambda$onCreate$0 -> ImportEntriesActivity.saveAndFinish [OK]
53. E2b2da36a FRAMEWORK: ImportEntriesActivity.saveAndFinish -> ImportEntriesActivity.lambda$saveAndFinish$10 [ERROR]
    FIX: add precondition "an icon pack is installed" (ImportEntriesActivity.java:320, hasIconPack() true), or add a producing step. Without it the else branch calls finish() (ImportEntriesActivity.java:321-322). No producer exists on the route.
54. Ea0f62157 INTENT: ImportEntriesActivity.lambda$saveAndFinish$10 -> AssignIconsActivity.<init> [OK]
55. E3ed34d26 LIFECYCLE: AssignIconsActivity.<init> -> AssignIconsActivity.onCreate [OK]
56. E182263fc FRAMEWORK: AssignIconsActivity.onCreate -> AssignIconAdapter.onBindViewHolder [OK]
57. Ee848355c FRAMEWORK: AssignIconAdapter.onBindViewHolder -> AssignIconAdapter.lambda$onBindViewHolder$0 [OK]
58. E7cd59d3c CALL: AssignIconAdapter.lambda$onBindViewHolder$0 -> AssignIconsActivity.onAssignIconEntryClick [OK]
59. E42451aaa CALL: AssignIconsActivity.onAssignIconEntryClick -> IconPickerDialog.create [OK]
60. Ec8d21670 CALL: IconPickerDialog.create -> IconAdapter.loadIcons [OK] (note: iconPacks.get(0) at IconPickerDialog.java:127 throws on an empty list; unreachable without the step 53 precondition)
61. E0ad50df8 FRAMEWORK: IconAdapter.loadIcons -> IconAdapter.onBindViewHolder [OK]
62. E9f3f0e20 FRAMEWORK: IconAdapter.onBindViewHolder -> IconAdapter.lambda$onBindViewHolder$2 [OK]
63. Efbf528db CALL: IconAdapter.lambda$onBindViewHolder$2 -> EditEntryActivity$1.onCustomSelected [ERROR]
    FIX: edge Efbf528db, dst: change EditEntryActivity$1.onCustomSelected to AssignIconsActivity$1.onCustomSelected (AssignIconsActivity.java:201, empty body). Note: the DummyIcon is never created on this path (showAddCustom = false, AssignIconsActivity.java:194; IconAdapter.java:63-64). Alternative: reroute through the EditEntryActivity picker (EditEntryActivity.java:594, showAddCustom = true).
64. E96dc91c6 CALL: EditEntryActivity$1.onCustomSelected -> EditEntryActivity.startImageSelectionActivity [OK]
65. E9a4fbaa2 CALL: EditEntryActivity.startImageSelectionActivity -> VaultManager.fireIntentLauncher@EDIT_PICK [OK]
66. E5832fe9e RESULT: VaultManager.fireIntentLauncher@EDIT_PICK -> EditEntryActivity.lambda$new$1 [OK] (env: the user picks an image or file in another app's chooser)
67. E824b6a53 CALL: EditEntryActivity.lambda$new$1 -> EditEntryActivity.startEditingIcon [OK]
68. E3dff3f05 FRAMEWORK: EditEntryActivity.startEditingIcon -> GlideRequests.asBitmap [OK]

Route 1 total: OK 55, ERROR 13, UNCLEAR 0.

---

## Route 2: ApkSignaturePin.getSignatures (11 steps): OK 9, ERROR 1, UNCLEAR 1

1. Eb9515d18 ENTRY/standard: S_ENTRY -> AegisApplication.<init> [OK]
2. E5b266140 LIFECYCLE: AegisApplication.<init> -> Hilt_AegisApplication.onCreate [OK]
3. E1ef992ce CALL: Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate [OK]
4. E88ed9829 ENTERS: AegisApplicationBase.onCreate -> S_PROCESS [OK] (AegisApplicationBase.java:45-67)
5. E598bf619 ENTRY/non_standard: S_PROCESS -> PanicResponderActivity.<init> [OK] (env: panic app sends info.guardianproject.panic.action.TRIGGER; AndroidManifest.xml:91-101)
6. E2d62949a LIFECYCLE: PanicResponderActivity.<init> -> PanicResponderActivity.onCreate [OK] (PanicResponderActivity.java:19-20; AegisActivity.java:61-67, _prefs set at 63)
7. E59d710ae CALL/explicit: PanicResponderActivity.onCreate -> TrustedIntents.getIntentFromTrustedSender [ERROR]
    FIX: add a producer for pref_panic_trigger = true before this step, namely a SecurityPreferencesFragment toggle (res/xml/preferences_security.xml:93; the only writer), or add the precondition "pref_panic_trigger = true" to the route state. The default is false (Preferences.java:107-108); setIsPanicTriggerEnabled has no Java callers (Preferences.java:111-113).
8. E4c5cd131 CALL: TrustedIntents.getIntentFromTrustedSender -> TrustedIntents.isPackageNameTrusted [UNCLEAR]
    Reason: TrustedIntents.java:120-124 says a singleInstance activity cannot get its caller, so getCallingPackageName returns null (TrustedIntents.java:131-142). But ActivityStarter.java:329-337 sets resultRecord for startActivityForResult (requestCode >= 0) with no launch-mode check, and ActivityStarter.java:502 and 1496-1512 change behavior when an existing singleInstance activity is reused. The sender app is outside the tree, so whether getCallingActivity() is non-null here is not settled.
9. E3192ea22 CALL: TrustedIntents.isPackageNameTrusted -> TrustedIntents.checkTrustedSigner(String) [OK] (TrustedIntents.java:86)
10. E548d37eb CALL: TrustedIntents.checkTrustedSigner(String) -> TrustedIntents.checkTrustedSigner(Signature[]) [OK] (TrustedIntents.java:214-217)
11. E28b753fb CALL: TrustedIntents.checkTrustedSigner(Signature[]) -> ApkSignaturePin.getSignatures [OK] (TrustedIntents.java:225-235; PanicResponderActivity.java:31-32)

Route 2 total: OK 9, ERROR 1, UNCLEAR 1.

---

## Route 3: ScannerActivity.unbindPreview (15 steps): OK 11, ERROR 2, UNCLEAR 2

1. Eb9515d18 ENTRY/standard: S_ENTRY -> AegisApplication.<init> [OK]
2. E5b266140 LIFECYCLE: AegisApplication.<init> -> Hilt_AegisApplication.onCreate [OK]
3. E1ef992ce CALL: Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate [OK]
4. E88ed9829 ENTERS: AegisApplicationBase.onCreate -> S_PROCESS [OK] (AegisApplicationBase.java:45-67)
5. E28ffc58c ENTRY: S_PROCESS -> MainActivity.<init> (launcher intent) [OK] (manifest 44-51). Note: this intent carries no action extra; see step 9.
6. Eb76444fd LIFECYCLE: MainActivity.<init> -> MainActivity.onCreate [OK] (MainActivity.java:193-194)
7. E3a06baed LIFECYCLE: MainActivity.onCreate -> MainActivity.onStart [OK] (MainActivity.java:939-940)
8. E779a1da2 CALL: MainActivity.onStart -> MainActivity.doShortcutActions [ERROR]
    FIX: edge E779a1da2, field guard: replace "onStart does not return before the call: no early return at MainActivity.java:947, 960 or 971" with "vault init not needed: isVaultInitNeeded() is false, so the return at MainActivity.java:947 (inside the vault-init branch, lines 942-948) is not taken; the error returns at 960 and 971 are not taken". On a fresh install onStart returns at 947 after startIntroActivity (946), so doShortcutActions is never reached. Source: MainActivity.java:942-948, 1006.
9. E01ce0942 CALL: MainActivity.doShortcutActions -> MainActivity.startScanActivity [ERROR]
    FIX: edge E28ffc58c (step 5) must carry the "scan" extra. Replace the launcher trigger with the scan shortcut intent (AegisApplicationBase.java:76-79, putExtra("action","scan") at 77) or the scan tile intent (LaunchScannerTileService.java:32-35, putExtra at 33). Also add the precondition "vault is plain text" (MainActivity.java:951-973 loads it in onStart; otherwise startAuthActivity at 976-977 leaves the vault unloaded and doShortcutActions returns at MainActivity.java:840).
10. E4c53d66d INTENT: MainActivity.startScanActivity -> ScannerActivity.<init> [OK] (env: camera permission granted; PermissionHelper.java:22-35; MainActivity.java:804-809)
11. Edd5d8048 LIFECYCLE: ScannerActivity.<init> -> ScannerActivity.onCreate [OK] (ScannerActivity.java:53)
12. Eea6435c6 FRAMEWORK: ScannerActivity.onCreate -> ScannerActivity.lambda$onCreate$0 [OK] (ScannerActivity.java:55-57, 67-68, 88; method_list.json lists ScannerActivity.lambda$onCreate$0)
13. E314fd012 ENTERS: ScannerActivity.lambda$onCreate$0 -> S_SCANNER@CAMERA_READY [UNCLEAR]
    Reason: needs a camera lens (ScannerActivity.java:77-83 finishes the page when there is none). Camera hardware is not part of the standard configuration.
14. Ef5aafb40 GUI: S_SCANNER@CAMERA_READY -> ScannerActivity.onOptionsItemSelected [UNCLEAR]
    Reason: the camera switch icon is shown only with two lenses (ScannerActivity.java:137-148). That needs both back and front cameras, which the standard configuration does not fix.
15. Eb5012061 CALL: ScannerActivity.onOptionsItemSelected -> ScannerActivity.unbindPreview [OK] (ScannerActivity.java:112-113)

Route 3 total: OK 11, ERROR 2, UNCLEAR 2.

---

## Route 4: IconPack$Icon.<init> (12 steps): OK 10, ERROR 2, UNCLEAR 0

1. Eb9515d18 ENTRY/standard: S_ENTRY -> AegisApplication.<init> [OK]
2. E5b266140 LIFECYCLE: AegisApplication.<init> -> Hilt_AegisApplication.onCreate [OK]
3. E1ef992ce CALL: Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate [OK]
4. Ef539c17b CALL: AegisApplicationBase.onCreate -> SingletonCImpl.getVaultManager [OK] (AegisApplicationBase.java:47; interface call dispatched to the generated component, INFERRED)
5. Ebdc15ea3 FRAMEWORK: SingletonCImpl.getVaultManager -> SwitchingProvider.get [OK] (generated Dagger code, INFERRED)
6. E29463d22 CALL: SwitchingProvider.get -> AegisModule.provideIconPackManager [ERROR]
    FIX: getVaultManager reaches the provideVaultManager case (case 627 in the earlier extraction), not the provideIconPackManager case (case 636). Replace steps 4-6 with a route that injects IconPackManager: AegisActivity.java:55-56 (@Inject IconPackManager) or IconPacksManagerFragment.java:45-46 (@Inject IconPackManager). Those start the getter path that reaches case 636. Source: AegisModule.java:26-28 (provideIconPackManager); AegisModule.java:37-41 (provideVaultManager).
7. E375694d7 CALL: AegisModule.provideIconPackManager -> IconPackManager.<init> [OK] (AegisModule.java:27)
8. E75a5e491 CALL: IconPackManager.<init> -> IconPackManager.rescanIconPacks [OK] (IconPackManager.java:30-34; line 33)
9. Ebac005d0 CALL: IconPackManager.rescanIconPacks -> IconPack.fromBytes [ERROR]
    FIX: the route header says explicit_standard_route=yes, but this step's state needs an icon pack left over from an earlier run (IconPackManager.java:136-158). The standard configuration has no icon pack at start. Either set explicit_standard_route=no (reclassify as non_standard) in the route header, or add the precondition "icon pack folder from an earlier run exists" to the route state.
10. Eecb7add2 CALL: IconPack.fromBytes -> IconPack.fromJson [OK] (IconPack.java:128-131; line 130)
11. Eaf319356 CALL: IconPack.fromJson -> IconPack$Icon.fromJson [OK] (IconPack.java:117, 120-121)
12. Ecc690490 CALL: IconPack$Icon.fromJson -> IconPack$Icon.<init> [OK] (IconPack.java:196-208; line 208)

Route 4 total: OK 10, ERROR 2, UNCLEAR 0.

---

## Route 5: injectVaultLockReceiver2 (9 steps): OK 8, ERROR 0, UNCLEAR 1

1. Eb9515d18 ENTRY/standard: S_ENTRY -> AegisApplication.<init> [OK]
2. E5b266140 LIFECYCLE: AegisApplication.<init> -> Hilt_AegisApplication.onCreate [OK]
3. E1ef992ce CALL: Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate [OK]
4. E88ed9829 ENTERS: AegisApplicationBase.onCreate -> S_PROCESS [OK] (AegisApplicationBase.java:45-67)
5. E313f4f87 SYSTEM: S_PROCESS -> VaultLockReceiver.onReceive [OK] (env: screen off; AegisApplicationBase.java:49-51 registers ACTION_SCREEN_OFF; VaultLockReceiver.java:24-34)
6. E47521e87 CALL: VaultLockReceiver.onReceive -> Hilt_VaultLockReceiver.onReceive [UNCLEAR]
    Reason: VaultLockReceiver.java:24-34 has no super.onReceive call, and the bytecode "Direct call" cannot be checked because no class files are on disk. Whether the generated base onReceive runs at all is not settled. Steps 7-9 depend on this edge.
7. Ef238aaad CALL: Hilt_VaultLockReceiver.onReceive -> Hilt_VaultLockReceiver.inject [OK] (generated Hilt code, INFERRED)
8. E4e6415e1 CALL: Hilt_VaultLockReceiver.inject -> SingletonCImpl.injectVaultLockReceiver [OK] (generated code, INFERRED)
9. E421cdc72 CALL: SingletonCImpl.injectVaultLockReceiver -> SingletonCImpl.injectVaultLockReceiver2 [OK] (generated code, INFERRED)

Route 5 total: OK 8, ERROR 0, UNCLEAR 1.

---

## Route 6: Hilt_AegisApplication.<init> (2 steps): OK 2, ERROR 0, UNCLEAR 0

1. Eb9515d18 ENTRY/standard: S_ENTRY -> AegisApplication.<init> [OK] (FW ActivityThread.java:5713-5715 backup or restore guard)
2. Ecaf88dff CALL: AegisApplication.<init> -> Hilt_AegisApplication.<init> [OK] (AegisApplication.java:6 declares extends AegisApplicationBase; the Hilt Gradle plugin rewrites the superclass to Hilt_AegisApplication. The rewritten bytecode is not on disk, so this is INFERRED)

Route 6 total: OK 2, ERROR 0, UNCLEAR 0.

---

## Route 7: AegisApplication.<init> (1 step): OK 1, ERROR 0, UNCLEAR 0

1. Eb9515d18 ENTRY/standard: S_ENTRY -> AegisApplication.<init> [OK] (AndroidManifest.xml:21-27; FW ActivityThread.java:5713-5715 backup or restore guard)

Route 7 total: OK 1, ERROR 0, UNCLEAR 0.

---

## Final table

| Route | Steps | OK | ERROR | UNCLEAR |
|---|---|---|---|---|
| GlideRequests.asBitmap | 68 | 55 | 13 | 0 |
| ApkSignaturePin.getSignatures | 11 | 9 | 1 | 1 |
| ScannerActivity.unbindPreview | 15 | 11 | 2 | 2 |
| IconPack$Icon.<init> | 12 | 10 | 2 | 0 |
| injectVaultLockReceiver2 | 9 | 8 | 0 | 1 |
| Hilt_AegisApplication.<init> | 2 | 2 | 0 | 0 |
| AegisApplication.<init> | 1 | 1 | 0 | 0 |
| **Total** | **118** | **96** | **18** | **4** |
