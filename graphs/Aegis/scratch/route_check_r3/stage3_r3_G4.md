# Stage 3 route check R3-G4 (Aegis schema 2, round 3, read-only)

Date: 2026-10-27. Sources: route print from `tools/show_route.py Aegis "<target>" --dedupe`; graph_def.py edge text; app source under `final_java_only/Aegis/app/Aegis-#v3.4.2/app/src/main/java/com/beemdevelopment/aegis/` and `res/`; AOSP 8.1.0_r1 under `fw_src/` (read directly with sed, because show_route printed "not found in the source tree" for every FW-SRC line).

Conventions used: a cross-run STATE is UNCLEAR ("needs earlier run") unless its text is wrong. A guard omitted from the text is an ERROR only when the omitted condition can be false on that route; when the route's own STATE makes it true, the omission is noted as a text addition. Androidx, Material, Hilt-generated and Glide-generated bodies are not on disk, so links that pass through them are UNCLEAR.

## Summary

| Route | Target | Steps | ERROR steps | UNCLEAR steps | OK steps |
|---|---|---|---|---|---|
| 1 | EditEntryActivity$CustomSvgIcon.<init> | 47 | 24, 40 | 8, 10, 13, 16, 18, 19, 20, 21, 23, 30, 33, 38, 43 | 32 |
| 2 | DaggerAegisApplication_HiltComponents_SingletonC$SingletonCImpl.injectVaultLockReceiver2 | 9 | none | none | 9 |
| 3 | OtpInfo.isAlgorithmValid | 17 | none | 8 | 16 |
| 4 | GlideOptions.clone | 15 | none | 7, 8, 9, 10, 12, 14, 15 | 8 |
| 5 | MainActivity.onIntroResult | 22 | none | 9, 14, 21 | 19 |

## Route 1: EditEntryActivity$CustomSvgIcon.<init> (47 steps)

Result: the route is not valid as written. Step 24 sends the Import (file) tap into the app-import listener. Step 40 sends the AssignIcons picker's custom tap into EditEntryActivity's listener, but the AssignIcons picker has no custom row. Steps 41-47 are correct edges on their own, but the route reaches them only through step 40.

Step 2 (E5b266140, AegisApplication.<init> -> Hilt_AegisApplication.onCreate): OK (bytecode). Printed: ActivityThread.java:5735-5740 (callApplicationOnCreate at 5740); AegisApplication.java:5-6 (extends AegisApplicationBase, no onCreate). Compiled work-emulator/classes/Aegis/0/com/beemdevelopment/aegis/Hilt_AegisApplication.class defines onCreate, and AegisApplication.class <init> calls Hilt_AegisApplication.<init>, so the framework's onCreate dispatch resolves to the Hilt class. Fix: none; the evidence should cite the class file, not "generated, not on disk".

Step 3 (E1ef992ce, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate): OK (bytecode). Hilt_AegisApplication.class onCreate invokes AegisApplicationBase.onCreate (checked by parsing the class file's constant pool and method code with a Python script; javap cannot run because no Java runtime is installed). AegisApplicationBase.java:45-46 has onCreate with super.onCreate. Fix: none; evidence text should cite the class file.

Step 8 (Ed6230165, MainActivity.onStart -> MainActivity.loadEntries): UNCLEAR (needs earlier run). Printed: MainActivity.java:936-997. The writer exists: IntroActivity.java:88-100 (no-security choice gives creds null) -> VaultManager.java:59-67 initNew(null) calls save(), so the plain file is written. The state text does not name the writer's source line; add IntroActivity.java:100. The guard text omits two enclosing conditions: the early return at MainActivity.java:942-947 (isVaultInitNeeded, VaultManager.java:226-228) and the vault-loaded branch at 976-977. Both hold under this STATE (the file exists, and the plain file is loaded at 965), so this is a text addition, not a route change. Fix: add both conditions to the guard text.

Step 10 (E887b87bf, S_LIST -> MainActivity.onOptionsItemSelected): UNCLEAR. The toolbar-to-onOptionsItemSelected dispatch is androidx.appcompat, not on disk. App side checked: MainActivity.java:1086-1094; action_settings is in res/menu/menu_main.xml. Fix: none.

Step 13 (E640fb9eb, startPreferencesActivity(Class,String) -> PreferencesActivity.<init>): UNCLEAR. The launch goes through androidx ActivityResultLauncher (not on disk). App side checked: MainActivity.java:830-834 (explicit Intent to PreferencesActivity). Fix: none.

Step 16 (E382bc001, MainPreferencesFragment.<init> -> onCreatePreferences): UNCLEAR. The attach/onCreatePreferences order is androidx.fragment (not on disk). App side: PreferencesActivity.java:40-46; MainPreferencesFragment.java:7-12. Fix: none.

Step 18 (E3452b602, S_SETTINGS_MAIN -> PreferencesActivity.onPreferenceStartFragment): UNCLEAR. The row-tap dispatch to the activity callback is androidx.preference (not on disk). App side: PreferencesActivity.java:18-19 (implements the callback), 80-84; preferences.xml:38 is the Import/Export row. Fix: none.

Step 19 (E63d9f2a4, onPreferenceStartFragment -> ImportExportPreferencesFragment.<init>, non_standard): UNCLEAR. The class (non_standard, reflection) is right: PreferencesActivity.java:81 calls FragmentFactory.instantiate with pref.getFragment(). The class name matches preferences.xml:38. The instantiate body is androidx (not on disk). Fix: none.

Step 20 (E245f8b40, ImportExportPreferencesFragment.<init> -> onCreatePreferences): UNCLEAR. androidx.fragment lifecycle (not on disk). App side: ImportExportPreferencesFragment.java:98-99 inflates preferences_import_export.xml. Fix: none.

Step 21 (E91eeed07, onCreatePreferences -> lambda$onCreatePreferences$6, Import tap): UNCLEAR. The preference click dispatch is androidx.preference (not on disk). App side: ImportExportPreferencesFragment.java:105-115; pref_import key at preferences_import_export.xml:6. The lambda id is taken from the route tool and was not checked against bytecode. Fix: none for this step (see step 24).

Step 23 (Ebe22842e, Dialogs.showImportersDialog -> Dialogs.lambda$showImportersDialog$27): UNCLEAR. The OK button of a Material MaterialAlertDialogBuilder is dispatched by Material (not on disk). The cited View.performClick is not the path for a dialog button. App side: Dialogs.java:515-541 (OK calls the listener passed in; no isDirect branch on that call). Fix: none in this step (see step 24).

Step 24 (E72c20578, Dialogs.lambda$showImportersDialog$27 -> ImportExportPreferencesFragment.lambda$onCreatePreferences$7): ERROR. Printed: ImportExportPreferencesFragment.java:105-115 (pref_import listener, which calls showImportersDialog with false at 107) and 117-121 (pref_import_app listener, which calls showImportersDialog with true at 119 and startImportEntriesActivity(def, null) at 120). Dialogs.java:515-538: the OK button calls the listener passed in. Step 22's dialog was opened with isDirect false, so its listener is the pref_import listener (lines 107-112), not lambda 7. The guard "isDirect true" is therefore wrong for this step, and the route has no file, which the Import (file) path needs. Fix proposed (variant split, not a one-line edit): retarget to the pref_import listener (107-112; build id to confirm), guard "dialog opened by Import (isDirect false)", and insert the file-pick path: fireIntentLauncher at ImportExportPreferencesFragment.java:112 (ENV other_app, the user picks a file) -> importSelectResultLauncher 73-78 -> onImportSelectResult 144-148 (RESULT_OK and a URI) -> ImportFileTask.doInBackground (ImportFileTask.java:27-50, openInputStream on the content URI) -> callback at 152-153 -> startImportEntriesActivity(_importerDef, file) at 161-165. Steps 25-26 stay only as the app-import variant (pref_import_app, no file).

Step 25 (Eca2b28fb, lambda$onCreatePreferences$7 -> startImportEntriesActivity): OK as an edge (ImportExportPreferencesFragment.java:119-121). It is reachable only from the app-import dialog (isDirect true), so it does not follow step 23 as routed; see step 24.

Step 26 (E3156c24c, startImportEntriesActivity -> ImportEntriesActivity.<init>): OK as an edge (161-165; ImportEntriesActivity is declared in the manifest). The "no file" note holds for the app-import variant only.

Step 27 (Ef8499dba, ImportEntriesActivity.<init> -> onCreate): OK (ImportEntriesActivity.java:62-64; abortIfOrphan returns false on a fresh start, AegisActivity.java:155).

Step 28 (Eff12cb12, ImportEntriesActivity.onCreate -> lambda$onCreate$0, save button): OK. ImportEntriesActivity.java:92-100; View.java:6289-6296 (performClick calls onClick at 6294).

Step 29 (Eaa1a222c, lambda$onCreate$0 -> saveAndFinish): OK. Guard at ImportEntriesActivity.java:94-98 is correct in sense. menu_import_entries.xml:8-10: toggle_wipe_vault has no android:checked, so it is unchecked by default, and no code sets it on this path (only line 410 toggles it). The else branch is the default.

Step 30 (E2b2da36a, saveAndFinish -> lambda$saveAndFinish$10, Yes in assign dialog): UNCLEAR. The positive button is dispatched by Material (not on disk); the cited View.performClick is not that path. App guard holds: ImportEntriesActivity.java:262-269 (no early return), 313 (saveAndBackupVault), 320 (hasIconPack), 329-335 (dialog). Fix: evidence text should cite the Material dialog, not View.performClick.

Step 31 (Ea0f62157, lambda$saveAndFinish$10 -> AssignIconsActivity.<init>): OK (ImportEntriesActivity.java:322-333; AssignIconsActivity is in the manifest at line 87).

Step 32 (E3ed34d26, AssignIconsActivity.<init> -> onCreate): OK (AssignIconsActivity.java:57; abortIfOrphan false on a fresh start).

Step 33 (E182263fc, AssignIconsActivity.onCreate -> AssignIconAdapter.onBindViewHolder): UNCLEAR. The row binding is androidx.recyclerview (not on disk). App side: AssignIconsActivity.java:90 (setAdapter), 113 (addEntries), both inside onCreate (57-115). The guard text omits the enclosing throw at AssignIconsActivity.java:101-102 (no icon pack). It holds on this route because step 31 requires an icon pack. Fix: add that check to the guard text.

Step 34 (Ee848355c, AssignIconAdapter.onBindViewHolder -> lambda$onBindViewHolder$0): OK (View.java:6289-6296; AssignIconAdapter.java:40-42).

Step 35 (E7cd59d3c, lambda$onBindViewHolder$0 -> AssignIconsActivity.onAssignIconEntryClick): OK (AssignIconAdapter.java:41; AssignIconsActivity implements AssignIconAdapter.Listener at line 48; the adapter is built with `this` at line 86).

Step 36 (E42451aaa, onAssignIconEntryClick -> IconPickerDialog.create): OK (AssignIconsActivity.java:194; no early return above it in 189-194). This call passes showAddCustom=false (see step 40).

Step 37 (Ec8d21670, IconPickerDialog.create -> IconAdapter.loadIcons): OK (IconPickerDialog.java:127, adapter.loadIcons(iconPacks.get(0), showAddCustom)).

Step 38 (E0ad50df8, IconAdapter.loadIcons -> IconAdapter.onBindViewHolder): UNCLEAR. RecyclerView binding is androidx (not on disk). App side: IconAdapter.java:60-100 (ends with notifyDataSetChanged), 166-168. Fix: none.

Step 39 (E9f3f0e20, onBindViewHolder -> lambda$onBindViewHolder$2, icon tap): OK (guard at IconAdapter.java:168; View.java:6289-6296; 173-179).

Step 40 (Efbf528db, IconAdapter.lambda$onBindViewHolder$2 -> EditEntryActivity$1.onCustomSelected): ERROR. Printed: AssignIconsActivity.java:194 (IconPickerDialog.create with showAddCustom false); AssignIconsActivity.java:199-201 (the listener here is an anonymous class in AssignIconsActivity whose onCustomSelected is empty); IconAdapter.java:63-64 (the DummyIcon custom row is added only when showAddCustom is true), 174-175; EditEntryActivity.java:594-602 (a different picker, showAddCustom true, whose onCustomSelected calls startImageSelectionActivity). Source says: the custom row does not exist in the AssignIcons picker, and the listener is not EditEntryActivity$1, so the guard (DummyIcon) cannot hold on this route. Fix proposed: no guard or text change fixes this. Variant split: a route that opens EditEntryActivity for an existing entry (entry path not traced here), then taps the icon view (EditEntryActivity.java:364-366) or the edit-icon menu item (545-546), which calls startIconSelection (585-607) with showAddCustom true; then custom row -> onCustomSelected (601-603) -> startImageSelectionActivity. Steps 31-40 would be replaced by that variant. The name EditEntryActivity$1 was not checked against the build.

Step 41 (E96dc91c6, EditEntryActivity$1.onCustomSelected -> startImageSelectionActivity): OK as an edge (EditEntryActivity.java:601-602). Reachable only after the step 40 fix.

Step 42 (Edecf9fcc, startImageSelectionActivity -> VaultManager.fireIntentLauncher): OK (EditEntryActivity.java:577; fireIntentLauncher launches inside try, VaultManager.java:243-248).

Step 43 (E319304e5, fireIntentLauncher -> EditEntryActivity.lambda$new$1, RESULT): UNCLEAR. The result delivery to the registered callback is androidx ActivityResult (not on disk). The framework hop is printed: ActivityThread.java:4253-4265 (deliverResults -> dispatchActivityResult). App guard holds: EditEntryActivity.java:141-146 (RESULT_OK and data). The lambda id was not checked against the build. Fix: none (reachable only after the step 40 fix).

Step 44 (E5d0f8d55, lambda$new$1 -> ImportFileTask.doInBackground, ASYNC): OK. Guard at EditEntryActivity.java:148 (SVG mime). IconType.java:43-44 maps SVG to "image/svg+xml". ProgressDialogTask.java:69-74 and AsyncTask.java:594-595, 632-651, 326-333 (doInBackground at 333). ImportFileTask reads the content URI with the content resolver (ImportFileTask.java:32), so no file:// issue.

Step 45 (E02aa5ba2, doInBackground -> onPostExecute, ASYNC): OK. AsyncTask.java:369-374, 691-695 (finish calls onPostExecute when not cancelled; the isCancelled check at 692 is not in the guard text, but the route never cancels the task), 705-713. ImportFileTask.java:53-56.

Step 46 (E82a3bc77, ImportFileTask.onPostExecute -> lambda$new$0, STATE): OK. ImportFileTask.java:55 (_cb.onTaskFinished). The STATE (SVG picked, import started) is produced inside this route by steps 43-44.

Step 47 (E1f02485b, lambda$new$0 -> CustomSvgIcon.<init>): OK (EditEntryActivity.java:151-152; constructor at 1009-1011). Reachable only after the step 40 fix.

## Route 2: DaggerAegisApplication_HiltComponents_SingletonC$SingletonCImpl.injectVaultLockReceiver2 (9 steps)

Result: the route is valid. All 9 steps are OK. The Hilt and Dagger bodies are not in source, so each generated link was checked against the compiled classes in work-emulator/classes/Aegis/0/com/beemdevelopment/aegis/ (constant pool and method code parsed with a Python script; javap cannot run because no Java runtime is installed). The build copy under final_java_only/Aegis/app/Aegis-#v3.4.2/app/build/intermediates matched the VaultLockReceiver method references.

Step 1 (E14b4e906, S_ENTRY -> AegisApplication.<init>, ENTRY): OK. AndroidManifest.xml:21-27 (android:name=".AegisApplication", backupAgent). The base-class note for backup and restore starts matches ActivityThread.java:5712-5715 and LoadedApk.java:959-970.

Step 2 (E5b266140, AegisApplication.<init> -> Hilt_AegisApplication.onCreate, LIFECYCLE): OK (bytecode). AegisApplication.class <init> invokes Hilt_AegisApplication.<init>, Hilt_AegisApplication.class defines onCreate, and the framework calls Application.onCreate at ActivityThread.java:5740. Fix: none to the route. The evidence label "INFERRED" can be upgraded to BYTECODE.

Step 3 (E1ef992ce, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate, CALL): OK (bytecode). Hilt_AegisApplication.class onCreate invokes AegisApplicationBase.onCreate. AegisApplicationBase.java:45-46 has the matching super.onCreate. Fix: none; evidence can cite the class file.

Step 4 (E88ed9829, AegisApplicationBase.onCreate -> S_PROCESS, ENTERS/page): OK. AegisApplicationBase.java:45-67, no early return. S_PROCESS is reached when Application.onCreate returns (ActivityThread.java:5740). Fix: none.

Step 5 (E313f4f87, S_PROCESS -> VaultLockReceiver.onReceive, SYSTEM, ENV screen off): OK. Framework delivery: LoadedApk.java:1313 (receiver.onReceive(mContext, intent) in the dispatcher). The receiver is registered at AegisApplicationBase.java:49-51 with an ACTION_SCREEN_OFF filter. The registration call is ContextCompat.registerReceiver (androidx, not on disk), but the registration is not an edge in this route; the STATE comes from the in-source line 51. VaultLockReceiver.java:25-27 lets ACTION_SCREEN_OFF through. Fix: none.

Step 6 (E47521e87, VaultLockReceiver.onReceive -> Hilt_VaultLockReceiver.onReceive, CALL/explicit): OK (bytecode, not source). The source has no super.onReceive call (VaultLockReceiver.java:24-34; the class extends BroadcastReceiver at line 16). The compiled VaultLockReceiver.class onReceive contains invokespecial Hilt_VaultLockReceiver.onReceive, so the superclass in the compiled code is the Hilt class. This call is most likely added by the Hilt build transform (not read). Fix (evidence text only): the label "SRC VaultLockReceiver.java:None (bytecode)" should read "BYTECODE VaultLockReceiver.class onReceive (invokespecial); not in the source". The route itself is unchanged.

Step 7 (Ef238aaad, Hilt_VaultLockReceiver.onReceive -> Hilt_VaultLockReceiver.inject, CALL/explicit): OK (bytecode). Hilt_VaultLockReceiver.class onReceive invokes inject. Fix: none; the evidence can cite the class file, not "build class, line 27".

Step 8 (E4e6415e1, Hilt_VaultLockReceiver.inject -> SingletonCImpl.injectVaultLockReceiver, CALL, interface dispatch): OK (bytecode). Hilt_VaultLockReceiver.class inject invokes the interface VaultLockReceiver_GeneratedInjector.injectVaultLockReceiver. The component superclass AegisApplication_HiltComponents$SingletonC lists VaultLockReceiver_GeneratedInjector among its interfaces, and SingletonCImpl.class defines injectVaultLockReceiver, so the virtual dispatch lands there. Fix: none.

Step 9 (E421cdc72, SingletonCImpl.injectVaultLockReceiver -> SingletonCImpl.injectVaultLockReceiver2, CALL/explicit): OK (bytecode). SingletonCImpl.class injectVaultLockReceiver invokes injectVaultLockReceiver2. The target method exists in the class, and it calls Provider.get and VaultLockReceiver_MembersInjector.inject_vaultManager, so the route ends at the field injection. Fix: none.

Route 2 counts: 9 steps, ERROR 0, UNCLEAR 0, OK 9.

## Route 3: OtpInfo.isAlgorithmValid (17 steps)

Result: the route is valid. No ERROR. Step 8 is UNCLEAR only because of its cross-run STATE. Its code path is correct.

Step 1 (E14b4e906, ENTRY): OK. AndroidManifest.xml:21-27.

Step 2 (E5b266140, LIFECYCLE): OK (bytecode). Same check as route 2, step 2.

Step 3 (E1ef992ce, CALL): OK (bytecode). Same check as route 2, step 3.

Step 4 (E88ed9829, ENTERS/page): OK. AegisApplicationBase.java:45-67.

Step 5 (E28ffc58c, S_PROCESS -> MainActivity.<init>, ENTRY): OK. AndroidManifest.xml:44-51 (MAIN and LAUNCHER filter on .ui.MainActivity).

Step 6 (Eb76444fd, MainActivity.<init> -> onCreate, LIFECYCLE): OK. MainActivity.java:192-194 (super.onCreate at 194); the order is ActivityThread.java:2729-2731 and 2741.

Step 7 (E3a06baed, onCreate -> onStart, LIFECYCLE): OK. MainActivity.java:938-940; ActivityThread.java:2741 (performStart after onCreate).

Step 8 (Ef4d44119, MainActivity.onStart -> VaultManager.loadFrom(VaultFile), CALL, STATE: plain-text vault file exists): UNCLEAR (needs earlier run). The edge is correct: MainActivity.java:951 (not loaded), 954 (readVaultFile), 963 (not encrypted), 965 (loadFrom). The STATE is cross-run. Its writer is the intro no-security path: IntroActivity.java:91-100 (creds null) -> VaultManager.initNew(null) (VaultManager.java:59-67), which calls save(). Fix: none to the edge. The STATE text should cite IntroActivity.java:91-100 and VaultManager.java:59-67. The guard text also omits the early return at MainActivity.java:942-947 (isVaultInitNeeded); the file-exists STATE makes that return false, so this is a text addition, not a route change.

Step 9 (Ea2c4bf33, loadFrom(VaultFile) -> loadFrom(VaultFile, creds), CALL): OK. VaultManager.java:95-96 (`return loadFrom(vaultFile, null);` at 96).

Step 10 (E51f87b30, loadFrom(VaultFile, creds) -> VaultRepository.fromFile, CALL): OK. VaultManager.java:80 (signature), 81-83 (throws if already loaded; step 8's guard makes this false), 85 (fromFile).

Step 11 (E567fe5c3, VaultRepository.fromFile -> Vault.fromJson, CALL): OK. VaultRepository.java:100-101 (plain path, file.getContent()), 106 (Vault.fromJson). The creds-null check at 93-95 does not throw for a plain file.

Step 12 (E68d38260, Vault.fromJson -> VaultEntry.fromJson, CALL): OK. Vault.java:61-62 (version check), 75-77 (entries loop). The guard text matches.

Step 13 (E891d0646, VaultEntry.fromJson -> OtpInfo.fromJson, CALL): OK. VaultEntry.java:87.

Step 14 (E0e214f1e, OtpInfo.fromJson -> TotpInfo.<init>, CALL): OK. OtpInfo.java:121-123 (switch; case TotpInfo.ID at 122, which is "totp" per TotpInfo.java:13).

Step 15 (E127bdfc6, TotpInfo.<init>(4 args) -> OtpInfo.<init>(3 args), CALL): OK. TotpInfo.java:23-24 (super call at 24); OtpInfo.java:25.

Step 16 (E7ae83abd, OtpInfo.<init>(3 args) -> setAlgorithm, CALL): OK. OtpInfo.java:25-27 (setAlgorithm at 27).

Step 17 (Eb6b4b4b1, setAlgorithm -> isAlgorithmValid, CALL): OK. OtpInfo.java:83 (setAlgorithm), 89 (isAlgorithmValid call); the target is defined at OtpInfo.java:78-81 and checks SHA1, SHA256, SHA512 and MD5.

Route 3 counts: 17 steps, ERROR 0, UNCLEAR 1 (step 8), OK 16.

## Route 4: GlideOptions.clone (15 steps)

Result: no ERROR. Steps 1-6 are the application and launch chain, already checked in routes 1-3. Steps 7-10, 12, 14 and 15 pass through androidx.fragment or Glide library bodies, which are not on disk, so they are UNCLEAR. Steps 11 and 13 are the Glide-generated code, which is in the compiled Aegis classes and was checked there.

Step 1 (E14b4e906, ENTRY): OK. AndroidManifest.xml:21-27.

Step 2 (E5b266140, LIFECYCLE): OK (bytecode). Same as route 2, step 2.

Step 3 (E1ef992ce, CALL): OK (bytecode). Same as route 2, step 3.

Step 4 (E88ed9829, ENTERS/page): OK. AegisApplicationBase.java:45-67.

Step 5 (E28ffc58c, ENTRY): OK. AndroidManifest.xml:44-51.

Step 6 (Eb76444fd, LIFECYCLE): OK. MainActivity.java:192-194; ActivityThread.java:2729-2731, 2741.

Step 7 (E3e74e870, MainActivity.onCreate -> EntryListView.<init>, FRAMEWORK, reflection): UNCLEAR. The FragmentManager (androidx.fragment) creates the class from the layout, and that body is not on disk. App side checked: MainActivity.java:195 (setContentView(R.layout.activity_main)); activity_main.xml:54-56 (the fragment with android:name="com.beemdevelopment.aegis.ui.views.EntryListView"). Fix: none.

Step 8 (E89bce4c8, EntryListView.<init> -> onCreate, LIFECYCLE): UNCLEAR. The Fragment lifecycle call is androidx (not on disk). App side: EntryListView.java:66 (extends Fragment), 84-85 (onCreate, super.onCreate). Fix: none.

Step 9 (Eda7e9bd0, onCreate -> onCreateView, LIFECYCLE): UNCLEAR. androidx lifecycle (not on disk). App side: EntryListView.java:97-144 (onCreateView inflates fragment_entry_list_view at 98; setAdapter at 144, matching the route text). Fix: none.

Step 10 (Eaaf7ec29, onCreateView -> GeneratedRequestManagerFactory.build, FRAMEWORK, library lookup): UNCLEAR. The Glide.with(this) call is at EntryListView.java:124, but the lookup through Glide's library is not on disk (no Glide library classes in work-emulator, final_java_only, or the Gradle cache). The generated factory exists in work-emulator/classes/Aegis/0/com/bumptech/glide/GeneratedRequestManagerFactory.class. Fix: none.

Step 11 (Eab5f3cfb, GeneratedRequestManagerFactory.build -> GlideRequests.<init>, CALL): OK (bytecode). GeneratedRequestManagerFactory.class build invokes GlideRequests.<init> (work-emulator/classes/Aegis/0/com/bumptech/glide/). The route text says "the build class, line 18", which cannot be checked; the invoke is confirmed.

Step 12 (E265bbd0b, GlideRequests.<init> -> setRequestOptions, FRAMEWORK, library virtual dispatch): UNCLEAR. GlideRequests.class <init> (work-emulator/classes/Aegis/0/com/beemdevelopment/aegis/ui/glide/) invokes only RequestManager.<init>. The step that RequestManager's constructor calls setRequestOptions is inside the Glide library, which is not on disk. The generated override of setRequestOptions does exist (see step 13). Fix: none.

Step 13 (Edb1d9299, setRequestOptions -> GlideOptions.apply, CALL, guard: options not already a GlideOptions): OK (bytecode). The generated setRequestOptions (GlideRequests.class) has instanceof GlideOptions at offset 9 and ifeq at 12, which jumps to 23. From 23 it runs new GlideOptions (24), GlideOptions.<init> (28), GlideOptions.apply (32), and then RequestManager.setRequestOptions (35). The fall-through (instanceof true) calls super.setRequestOptions directly. The guard is therefore correct. The route text cites "GlideRequests.java:176", which cannot be checked because the generated source is not on disk; the bytecode branch is what was verified.

Step 14 (Ec449db03, GlideOptions.apply -> GlideOptions.autoClone, FRAMEWORK, library virtual dispatch): UNCLEAR. GlideOptions.class apply invokes RequestOptions.apply (invokespecial), and GlideOptions.class defines autoClone (invokes RequestOptions.autoClone). The claim that the library's RequestOptions.apply calls autoClone() is inside the Glide library, which is not on disk, so it cannot be verified. Risk: if the library's apply calls clone() directly, this edge is wrong. Fix: none on disk; it needs the Glide library source.

Step 15 (E9d286870, GlideOptions.autoClone -> GlideOptions.clone, FRAMEWORK, library virtual dispatch): UNCLEAR. GlideOptions.class defines clone (invokes RequestOptions.clone), and autoClone invokes RequestOptions.autoClone. The library's autoClone -> clone() call is inside the Glide library, which is not on disk. Fix: none on disk.

Route 4 counts: 15 steps, ERROR 0, UNCLEAR 7 (7, 8, 9, 10, 12, 14, 15), OK 8 (1-6, 11, 13).

## Route 5: MainActivity.onIntroResult (22 steps)

Result: no ERROR. The route is valid as a chain. Steps 9, 14 and 21 are UNCLEAR because each passes through a body that is not on disk (androidx ActivityResult or launcher, and android.widget.RadioGroup). Steps 8, 13, 17, 20 and 21 have text fixes (guard text or compression) that do not change the route. Steps 1-7 are the launch chain already checked in routes 1-4.

Step 1 (E14b4e906, ENTRY): OK. AndroidManifest.xml:21-27.

Step 2 (E5b266140, LIFECYCLE): OK (bytecode). Same as route 2, step 2. Evidence label "INFERRED" can be upgraded to BYTECODE: AegisApplication.class <init> invokes Hilt_AegisApplication.<init>, and Hilt_AegisApplication.class defines onCreate.

Step 3 (E1ef992ce, CALL): OK (bytecode). Same as route 2, step 3.

Step 4 (E88ed9829, ENTERS/page): OK. AegisApplicationBase.java:45-67.

Step 5 (E28ffc58c, ENTRY): OK. AndroidManifest.xml:44-51.

Step 6 (Eb76444fd, LIFECYCLE): OK. MainActivity.java:192-194; ActivityThread.java:2729-2731, 2741.

Step 7 (E3a06baed, LIFECYCLE): OK. MainActivity.java:938-940; ActivityThread.java:2741.

Step 8 (E0602e719, CALL, guard: vault init needed): OK. MainActivity.java:942-948: when isVaultInitNeeded() is true, startIntroActivity() runs and onStart returns. Text addition: VaultManager.isVaultInitNeeded (VaultManager.java:226-228) is !isVaultLoaded && !fileExists, but the guard names only "no vault file exists". The omitted !isVaultLoaded holds on a fresh install, because nothing is loaded before the first onStart. Fix (text only): add "and the vault is not loaded in memory" to the guard.

Step 9 (E4ce5043a, INTENT, MainActivity.startIntroActivity -> IntroActivity.<init>): UNCLEAR. The launch goes through introResultLauncher.launch, which is androidx ActivityResultLauncher (not on disk). App side checked: MainActivity.java:603-607 (the `!_isDoingIntro` guard at 604; the Intent to IntroActivity at 605). Fix: none.

Step 10 (E5e63fbe7, LIFECYCLE): OK. ActivityThread.java:2729-2731, 2741 (onCreate after the constructor); IntroActivity.java:35-36 (onCreate with super.onCreate).

Step 11 (E93598a00, CALL): OK. IntroActivity.java:38 is the addSlide(WelcomeSlide) call that the route uses (lines 38-41 hold four addSlide calls). Evidence text: the note "bytecode line was 41" is unclear; cite line 38 only.

Step 12 (E1440feb8, ENTERS/page): OK. IntroBaseActivity.java:175-186: the first slide added (_slides.size() == 1) fires onBeforeSlideChanged(null, slide) and onAfterSlideChanged(null, slide). IntroActivity.java:38 is the first addSlide. The guard matches.

Step 13 (E6830b6dc, ENTERS/page, S_INTRO_WELCOME -> S_INTRO_PICKER): OK, with a structure note. The transition is correct. goToNextSlide (IntroBaseActivity.java:80-93) calls WelcomeSlide.isFinished, which is not overridden (WelcomeSlide.java:28 extends SlideFragment), so SlideFragment.isFinished returns true (SlideFragment.java:38-39). setPagerPosition(pos, 1) then calls onBeforeSlideChanged, and IntroActivity.java:57-62 returns true (skip to Done) only when imported is true, so the "not imported" guard is the one that lets the transition reach the picker. Structure note: the route has no GUI edge for the Next tap on Welcome. Fix: add the tap edge before this step, S_INTRO_WELCOME -> IntroBaseActivity.lambda$onCreate$1 (IntroBaseActivity.java:47), as steps 15-16 do for the picker's Next.

Step 14 (E32450899, ENTERS/page, S_INTRO_PICKER -> S_INTRO_PICKER@NONE): UNCLEAR. The layout id is right (fragment_security_picker_slide.xml:41, rb_none). The radio check is done by android.widget.RadioGroup, which is not on disk: fw_src/android-8.1.0_r1 has no RadioGroup.java, and its core/java/android/widget directory has no radio file. The cryptType itself is saved only when Next is pressed (SecurityPickerSlide.java:73-88, through IntroBaseActivity.java:85), so "@NONE" describes the checked radio, not a saved value. Fix: none on disk.

Step 15 (E553f11f7, GUI, S_INTRO_PICKER@NONE -> lambda$onCreate$1@NONE): OK. IntroBaseActivity.java:47 (`_btnNext.setOnClickListener(v -> goToNextSlide())`); View.java:6289-6296 (performClick calls onClick at 6294). The name lambda$onCreate$1 was checked in the class file: IntroBaseActivity.class lambda$onCreate$1 invokes goToNextSlide.

Step 16 (E251ac3f4, CALL): OK. IntroBaseActivity.java:47, 80-93; bytecode confirms lambda$onCreate$1 -> goToNextSlide.

Step 17 (E7216511b, CALL, goToNextSlide@NONE -> IntroActivity.onBeforeSlideChanged@NONE): OK, compressed. The edge skips the intermediate calls that carry the call into the override: goToNextSlide -> setPagerPosition(pos, 1) (IntroBaseActivity.java:86, 149-151) -> setPagerPosition(int) -> onBeforeSlideChanged (138). The guard (82: not last slide; 84: isFinished) holds for the picker (position 1 of 4, and the picker radio is checked, so isFinished is true). Fix (optional): name the 149-151 and 138 hops in the edge text. No route change.

Step 18 (E8da5177a, CALL, STATE: picker chose none): OK. IntroActivity.java:50-55: oldSlide == SecurityPickerSlide, newSlide == SecuritySetupSlide (the pager's next slide, position 2), and cryptType == CRYPT_TYPE_NONE, so skipToSlide(DoneSlide) runs and returns true. The STATE is produced inside this route (steps 14-16; SecurityPickerSlide.java:85 saves cryptType before setPagerPosition at IntroBaseActivity.java:86), so it is not cross-run.

Step 19 (E3f8e1ae8, ENTERS/page): OK. IntroBaseActivity.java:104-111 (skipToSlide finds DoneSlide, then setPagerPosition(i)); IntroActivity.java:50-55 (the none skip). The guard is a disjunction (imported skip or none skip); the none branch holds on this route.

Step 20 (E0182bb68, GUI, S_INTRO_DONE -> IntroActivity.onDonePressed): OK, compressed. The Next tap on Done runs lambda$onCreate$1 (IntroBaseActivity.java:47) -> goToNextSlide (80-93). On the last slide (pos == size-1, so line 82 is false), goToNextSlide calls onDonePressed (line 91). The edge skips the lambda and goToNextSlide hops, which are in its evidence. Fix (optional): split the edge as in steps 15-17. No route change.

Step 21 (Ee73dcba1, RESULT, IntroActivity.onDonePressed -> MainActivity.lambda$new$1): UNCLEAR. The route inside onDonePressed is correct: IntroActivity.java:126 (setIntroDone), 128 (setResult(RESULT_OK)), 129 (finish); Activity.java:5526-5527 (finish). The framework hop is printed: ActivityThread.java:4253-4265 (deliverResults -> dispatchActivityResult). The hop from there to the registered callback is androidx ComponentActivity / ActivityResultRegistry, which is not on disk, so the link into MainActivity.lambda$new$1 is UNCLEAR. The target side is correct: the class file's MainActivity.lambda$new$1 invokes getResultCode and onIntroResult (source MainActivity.java:142-148). Guard text fix: the guard says "the error branches return at 104 and 121", but this route takes the non-imported branch (initNew at line 100; its error return is 104). Line 113 (readVaultFile failure, imported branch) is missing from the text, and line 121 (loadFrom failure, imported branch) is not on this route. Fix: rewrite the guard as "non-imported branch: initNew succeeded (no return at 104); cryptType none needs creds null (92-96)".

Step 22 (E5f44da38, CALL, MainActivity.lambda$new$1 -> MainActivity.onIntroResult): OK. MainActivity.java:142-148 (`getResultCode() == RESULT_OK` at 145 guards the call at 146). Bytecode confirms lambda$new$1 invokes ActivityResult.getResultCode and MainActivity.onIntroResult.

Route 5 counts: 22 steps, ERROR 0, UNCLEAR 3 (9, 14, 21), OK 19 (1-8, 10-13, 15-20, 22).

<!-- END -->
