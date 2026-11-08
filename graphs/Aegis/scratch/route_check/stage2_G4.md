# Stage 2 route check, G4 (Aegis schema 2)

Date: 2026-10-27
Scope: the five G4 routes in work/graphs/Aegis/graph_def.py. Read-only: graph_def.py was not edited.
Verdicts: OK = edge, class, guard and evidence check out. ERROR = wrong edge, class, guard, state or missing condition. UNCLEAR = the source on disk does not decide it.
Sources: Aegis source, Android framework (fw_src android-8.1.0_r1), and build-class bytecode (dump_calls.py). Hilt, Dagger, Glide, androidx, libsu and Material source are not on disk, so those steps are INFERRED.

| Route | Target | Steps | ERROR | UNCLEAR |
|---|---|---|---|---|
| 1 | ApkSignaturePin.getSignatures | 11 | none | 5, 8 |
| 2 | ImportExportPreferencesFragment.lambda$onImportSelectResult$11 | 28 | 8, 24 | none |
| 3 | DaggerAegisApplication_HiltComponents_SingletonC$ActivityRetainedCImpl$SwitchingProvider.<init> | 15 | 9 | 7 |
| 4 | GlideOptions.clone | 15 | 7, 10, 12, 14, 15 | none |
| 5 | SqlImporterHelper.lambda$findDatabaseFiles$0 | 36 | 8, 21, 22, 23, 24, 29, 32, 33 | 36 |

---

## Route 1: ApkSignaturePin.getSignatures

- Method: each edge checked against the cited Aegis source line, the framework source, and the build bytecode where listed. The route runs from the panic receiver to the pin comparison.
- Steps: 11
- ERROR: none
- UNCLEAR:
  - Step 5 (ENTRY, the panic app starts PanicResponderActivity). The panic app starts the activity through an implicit intent matched by the manifest intent-filter (AndroidManifest.xml:91-101). The class is undecided: standard as written, or FRAMEWORK/non_standard if the system's action resolution counts as framework dispatch. The ENV note cites the trust checks (PanicResponderActivity.java:29-37) instead of the sender. Fix: choose the class per the schema definition, and rewrite the ENV note to name the Guardian Project panic app as the sender, citing AndroidManifest.xml:91-101 and PanicResponderActivity.java:19-22. The trust checks belong to steps 7 and 8.
  - Step 8 (CALL, TrustedIntents.getIntentFromTrustedSender -> isPackageNameTrusted). The guard "calling package name is not empty (TrustedIntents.java:106-109)" depends on getCallingPackageName (131-142), which uses getCallingActivity (133). That returns a package only when PanicResponderActivity was started with startActivityForResult, and the singleInstance warning at TrustedIntents.java:120-124 applies. The framework getCallingActivity path is not fully read. Fix: add the startActivityForResult condition to the guard, cite lines 120-124 and 131-142, and read the framework path before setting OK.
- Steps 1-4, 6, 7, 9-11 OK.
  - Step 1 OK, but add the backup-exception citations: ActivityThread.java:5715 (makeApplication, restrictedBackupMode) and LoadedApk.java:959-970.
  - Step 10 OK, with a guard wording fix. "pm.getPackageInfo returns the package" should read "getPackageInfo does not throw NameNotFoundException (TrustedIntents.java:216; the catch is at 87-89)".

---

## Route 2: ImportExportPreferencesFragment.lambda$onImportSelectResult$11

- Method: as route 1. The route runs from the app start through Settings, Icon packs, the Import launcher, and the settings import task.
- Steps: 28
- ERROR: 8, 24
- OK conditional: 25 (valid only after the step 24 fix)
- Steps 1-7, 9-23, 26-28 OK. Steps 18-23 are valid edges, but they lead to the Icon packs page, which cannot reach this target (see step 24).
- Details:
  - Step 8 (ERROR): needs_state ST_VAULT_FILE has no producer on the route or in setup. A fresh install goes to the intro at MainActivity.onStart (942-948), and the fixtures have no vault file. Fix: add a setup producer (an intro run with no security choice, which writes the plain-text vault), or state the gate as a setup precondition with a fixture.
  - Step 19 (OK, text only): the evidence text is copied from step 16 (the androidx attach sentence) and does not describe FragmentFactory.instantiate. The cites (PreferencesActivity.java:80-84, preferences.xml:20) are correct. Replace the text.
  - Step 24 (ERROR): the launcher passed at IconPacksManagerFragment.java:175 is importResultLauncher, so the RESULT goes to IconPacksManagerFragment.lambda$new$0 (graph line 2049), not ImportExportPreferencesFragment.lambda$new$0. The ENV citation (WelcomeSlide.java:43-47) is the intro slide, not this route. Fix: replace steps 18-24 with the Import and export branch:
    PreferencesActivity.onPreferenceStartFragment -> ImportExportPreferencesFragment.<init> (reflection, non_standard, preferences.xml:38) -> onCreatePreferences (LIFECYCLE) -> tap pref_import: lambda$onCreatePreferences$6 (105-115) -> Dialogs.showImportersDialog(false) (107) -> Dialogs OK -> lambda$5 (107-113, non_standard) -> fireIntentLauncher with importSelectResultLauncher (112) -> RESULT -> ImportExportPreferencesFragment.lambda$new$0 (73-79; ENV other_app: the ACTION_GET_CONTENT picker, ImportExportPreferencesFragment.java:110-112) -> onImportSelectResult (77) -> ImportFileTask.doInBackground (ASYNC, 146-158) -> onPostExecute -> lambda$onImportSelectResult$11.
  - Step 25 (OK conditional): ImportExport.lambda$new$0 -> onImportSelectResult is correct only once step 24 uses the Import and export launcher.
  - Step 28 (OK, citation fix): the guard should cite ImportExportPreferencesFragment.java:152 (result.getError() == null; the error branch is at 154-156), not ImportFileTask.java:53-59.

---

## Route 3: SwitchingProvider.<init> (Dagger/Hilt)

- Method: app source lines checked directly. Hilt and Dagger generated classes checked in the build bytecode via dump_calls.py (Hilt_AegisActivity, DaggerAegisApplication_HiltComponents_SingletonC). Hilt and androidx source are not on disk, so those steps are INFERRED.
- Steps: 15
- ERROR: 9
- UNCLEAR: 7
- Steps 1-6, 8, 10-15 OK. Step 6 (implicit super() at MainActivity.java:99) is verified in bytecode. Step 12 class non_standard (Dagger/Hilt DI) is correct. Steps 10-15 bytecode lines verified: 99, 46, 77, 107, 487, 493.
- Details:
  - Step 7 (UNCLEAR): AegisActivity.<init> -> Hilt_AegisActivity.<init>. Source line AegisActivity.java:45 declares extends AppCompatActivity. The Hilt superclass exists only in the Hilt-rewritten build class. Fix: cite the bytecode of AegisActivity.<init> from the build dirs as the evidence, and keep the rewritten superclass as INFERRED. Then OK.
  - Step 9 (ERROR): Hilt_AegisActivity$1.onContextAvailable runs inside the super.onCreate call of the activity's onCreate, but the route has no onCreate step before it. Fix: insert between steps 8 and 9:
    MainActivity.<init> -> MainActivity.onCreate (ui/MainActivity.java:193-194, super.onCreate at 194) -> AegisActivity.onCreate (ui/AegisActivity.java:61-67, super.onCreate at 67) -> ComponentActivity.onCreate (androidx, INFERRED) -> Hilt listener. Keep the listener's own guard.

---

## Route 4: GlideOptions.clone

- Method: app classes checked against source and bytecode. Glide generated classes checked in the build bytecode (GeneratedRequestManagerFactory.build line 18; GlideRequests.setRequestOptions 173-178). Glide library source is not on disk. out/sanity_check.csv is coverage output, not a label source, so it does not count as evidence.
- Steps: 15
- ERROR: 7, 10, 12, 14, 15
- OK: 1-6, 8, 9 (INFERRED androidx lifecycle, standard), 11, 13
- Header: explicit_standard_route=yes. This will change once the classes are fixed, and the tool recomputes it.
- Details:
  - Step 7 (ERROR, class): the fragment is named in the layout XML (activity_main.xml:54-56, android:name) and created by androidx FragmentManager reflection. Class should be non_standard, not standard.
  - Step 10 (ERROR, class): Glide.with(this) reaches GeneratedRequestManagerFactory.build through library lookup of the generated module. Class should be non_standard.
  - Step 12 (ERROR, class): the RequestManager constructor calls setRequestOptions, which the generated GlideRequests overrides. This is virtual dispatch from library code, so class should be non_standard.
  - Step 14 (ERROR, class and evidence): RequestOptions.apply calls autoClone, which runs the generated override by virtual dispatch. Class should be non_standard. Evidence: replace the out/sanity_check.csv citation with the Glide library source or jar, or mark the step INFERRED.
  - Step 15 (ERROR, class and evidence): autoClone calls clone, which runs the generated override. Class should be non_standard. Same evidence fix as step 14.

---

## Route 5: SqlImporterHelper.lambda$findDatabaseFiles$0

- Method: app classes checked against source and build bytecode (ImportEntriesActivity, GoogleAuthImporter, SqlImporterHelper). libsu (SuFile) and Material/androidx source are not on disk, so those steps are INFERRED.
- Steps: 36
- ERROR: 8, 21, 22, 23, 24, 29, 32, 33
- UNCLEAR: 36
- OK: 1-7, 9-20, 25-28, 30, 31, 34, 35
- Header: env=- is incomplete. It needs other_app (the installed Google Authenticator, step 29) and other (the root shell, step 33).
- Details:
  - Step 8 (ERROR): the same vault-file state problem as route 2 step 8. Fix as there.
  - Step 19 (OK, text only): the evidence text is copied from step 16 (the androidx attach sentence). The cites (PreferencesActivity.java:80-84, preferences.xml:38) are correct.
  - Step 21 (ERROR): pref_import (lambda$onCreatePreferences$6, isDirect false) is the wrong row for an app import. Fix: use pref_import_app (lambda$onCreatePreferences$8, lines 117-123), which calls showImportersDialog(true) at line 119.
  - Step 22 (ERROR): showImportersDialog(false) at line 107 conflicts with step 24's guard (isDirect true). Fix: the call comes from lambda$8 at line 119 with isDirect true.
  - Step 23 (ERROR): cites the framework AlertController (fw_src 127-140, 166, 710). Dialogs.java:533 uses com.google.android.material.dialog.MaterialAlertDialogBuilder (and androidx AlertDialog), which is not on disk. Fix: mark the OK-button step INFERRED for Material/androidx. View.java:6289-6296 (performClick) is a valid cite.
  - Step 24 (ERROR): the target lambda$onCreatePreferences$7 (119-121) is correct once steps 21-22 use isDirect true. The class is wrong: Dialogs calls the app's ImporterListener interface, which app code implements, so the class is explicit, not non_standard. Fix: change the class and make the guard isDirect true at line 119.
  - Step 25 (OK once fixed): lambda$7 -> startImportEntriesActivity (line 120).
  - Step 29 (ERROR): missing ENV other_app. The route depends on the installed Google Authenticator with versionCode <= 5000100 (GoogleAuthImporter.java:40-49). Fix: add the ENV tag to step 29 and to the header.
  - Step 30 (OK): ImportEntriesActivity.java:173 calls task.execute(this), which binds to AsyncTask.execute(Params...), not ProgressDialogTask.execute(Lifecycle, Params...) (ProgressDialogTask.java:69-74). The step text is correct.
  - Step 32 (ERROR, class): RootShellTask.Callback.onTaskFinished is an app interface called from app code (RootShellTask.java:25). Class should be explicit, not non_standard.
  - Step 33 (ERROR): the guard "chosen importer is GoogleAuthImporter (line 108)" is wrong. Line 108 is DatabaseImporter.create. The dispatch to GoogleAuthImporter.readFromApp is a virtual call on the chosen importer. Fix: reword the guard. Also add ENV other (root shell granted, ImportEntriesActivity.java:149-153).
  - Step 36 (UNCLEAR): SuFile.listFiles(FilenameFilter) is a libsu method, not framework API, so the FRAMEWORK/standard class is not supported. Recommended class: non_standard (library callback via libsu, INFERRED). The guard "the SQL import reads a database from a folder (SqlImporterHelper.java:68)" should be the filter itself: name.startsWith(path.getName()) at SqlImporterHelper.java:67-68. Fix the class and guard, then OK.
