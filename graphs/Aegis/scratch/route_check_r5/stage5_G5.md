# Stage 5 route check, group G5 (Aegis, schema 2)

Read-only check of five routes from graphs/Aegis/graph_def.py. No files were changed outside this report.

Standard configuration: debug build, fresh install, API 27 emulator, no vault file at process start, no icon pack.

Paths used:
- SRC = final_java_only/Aegis/app/Aegis-#v3.4.2/app/src/main/java/com/beemdevelopment/aegis
- FW = fw_src/android-8.1.0_r1 (ActivityThread, Activity, View, com/android/internal/app/AlertController)
- BUILD = final_java_only/Aegis/app/Aegis-#v3.4.2/app/build/intermediates/classes/debug/transformDebugClassesWithAsm/dirs/com/beemdevelopment/aegis

Verdict rules used:
- OK: every link the edge claims is shown in SRC, BUILD or FW. An INTENT edge is OK when the target class is set explicitly in app code, even if the start call goes through an AndroidX launcher or Fragment.startActivity.
- UNCLEAR: the link depends on an AndroidX, Material, Glide or JDK body that is not on disk. The app side of the hop is still checked and cited. Also UNCLEAR for cross-run state whose edge text does not name the writing line.
- ERROR: the cited source contradicts the edge. Each ERROR has a FIX.

---

## Route 1: VaultGroup.equals (28 steps)

Route printout: `python3 -I tools/show_route.py Aegis 'VaultGroup.equals' --dedupe --max 60`. Verdicts: 16 OK, 0 ERROR, 12 UNCLEAR.

1. Eb9515d18 ENTRY S_ENTRY -> AegisApplication.<init> : **OK**. SRC-manifest AndroidManifest.xml:22 (`android:name=".AegisApplication"`). Guard FW ActivityThread.java:5713-5715 (base class only in restricted backup mode).
2. E5b266140 LIFECYCLE AegisApplication.<init> -> Hilt_AegisApplication.onCreate : **OK**. FW ActivityThread.java:5740 (`mInstrumentation.callApplicationOnCreate(app)`). BUILD AegisApplication.class super = `com/beemdevelopment/aegis/Hilt_AegisApplication` (checked with tools/extract_calls.py parse_class). SRC AegisApplication.java:6 `extends AegisApplicationBase`, no onCreate in the file. The Hilt superclass is added by the build transform, so the edge is correct.
3. E1ef992ce CALL Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate : **OK**. BUILD Hilt_AegisApplication.class calls AegisApplicationBase.onCreate at line 43, after hiltInternalInject at line 42. The generated source is absent, but the class file is on disk, so the "INFERRED" label in the route evidence can be replaced with this BUILD citation.
4. E88ed9829 ENTERS AegisApplicationBase.onCreate -> S_PROCESS : **OK**. SRC AegisApplicationBase.java:45-67 (receiver, lifecycle observer, cache clear, shortcuts).
5. E28ffc58c ENTRY S_PROCESS -> MainActivity.<init> : **OK**. AndroidManifest.xml:44-51 (MainActivity, exported, MAIN and LAUNCHER filter).
6. Eb76444fd LIFECYCLE MainActivity.<init> -> MainActivity.onCreate : **OK**. FW ActivityThread.java:2729-2731 (`callActivityOnCreate`). SRC MainActivity.java:193-194.
7. E3a06baed LIFECYCLE MainActivity.onCreate -> MainActivity.onStart : **OK**. FW ActivityThread.java:2740-2741 (performStart runs only when `!r.activity.mFinished`; the route cites only 2741, which is a minor citation gap, not an error). SRC MainActivity.java:938-940. No finish() call in onCreate (lines 193-331).
8. E20e76e09 CALL MainActivity.onStart -> MainActivity.loadEntries, state: plain-text vault from an earlier intro run : **UNCLEAR**. In-run path checked: MainActivity.java:942-948 (isVaultInitNeeded false when the file exists), 951-974 (readVaultFile, then loadFrom for an unencrypted file), 976-977 (not taken, vault loaded), 978 (`else if (_loaded)`, false), 991-992 (`loadEntries()`). The writer exists in another run: IntroActivity.java:100 `_vaultManager.initNew(creds)` with creds null on the no-security path -> VaultManager.java:65 `repo.save()` -> VaultRepository.java:127 `writeToFile`. The edge text does not name these lines, so the strict cross-run rule gives UNCLEAR. Suggested note text: add "written by IntroActivity.java:100 -> VaultManager.java:65 -> VaultRepository.java:127 when creds is null" to the state.
9. E1ffae3d8 ENTERS loadEntries -> S_LIST : **OK**. SRC MainActivity.java:1133-1144 (guard `!_loaded` at 1134; `setEntries` at 1138; `_loaded = true` at 1142).
10. E887b87bf GUI S_LIST -> MainActivity.onOptionsItemSelected : **UNCLEAR**. The menu tap is dispatched by AndroidX AppCompat, which is not on disk. App side checked: MainActivity.java:1086-1118.
11. Ef4e32054 CALL onOptionsItemSelected -> startPreferencesActivity() : **OK**. SRC MainActivity.java:1088-1089.
12. Ef64f95ee CALL startPreferencesActivity() -> startPreferencesActivity(Class,String) : **OK**. SRC MainActivity.java:826-828 (line 827 is the call).
13. E640fb9eb INTENT startPreferencesActivity(Class,String) -> PreferencesActivity.<init> : **OK**. Explicit target at MainActivity.java:831; sent through `preferenceResultLauncher` (declared at 166-167, launched at 834). The AndroidX launcher body is not on disk, but the target is set in app code (INTENT rule).
14. E94201299 LIFECYCLE PreferencesActivity.<init> -> onCreate : **OK**. FW ActivityThread.java:2729-2731. SRC PreferencesActivity.java:24.
15. E50e3cfda CALL PreferencesActivity.onCreate -> MainPreferencesFragment.<init> : **OK**. SRC PreferencesActivity.java:26-27 (abortIfOrphan), 40-41 (`new MainPreferencesFragment()`). AegisActivity.java:154-156: abortIfOrphan returns false when savedInstanceState is null, so the guard holds on a fresh start.
16. E382bc001 LIFECYCLE MainPreferencesFragment.<init> -> onCreatePreferences : **UNCLEAR**. The attach and list build are AndroidX fragment and preference code, not on disk. App side: PreferencesActivity.java:41-46 (commit), MainPreferencesFragment.java:9-11.
17. Eccc3a740 ENTERS onCreatePreferences -> S_SETTINGS_MAIN : **UNCLEAR**. Rows appear only if AndroidX inflates R.xml.preferences (not on disk). App side: MainPreferencesFragment.java:9-11 (`addPreferencesFromResource(R.xml.preferences)`), preferences.xml:8-44.
18. E3452b602 GUI S_SETTINGS_MAIN -> PreferencesActivity.onPreferenceStartFragment : **UNCLEAR**. Row tap dispatch is AndroidX preference code, not on disk. App side: PreferencesActivity.java:19, 80-84.
19. Eba86fd82 CALL/non_standard onPreferenceStartFragment -> AppearancePreferencesFragment.<init> : **UNCLEAR**. The reflection is AndroidX `FragmentFactory.instantiate`, not on disk. App side: PreferencesActivity.java:81; preferences.xml:8 (`android:fragment=...AppearancePreferencesFragment`); the class exists at ui/fragments/preferences/AppearancePreferencesFragment.java.
20. Ef17c8ca0 LIFECYCLE AppearancePreferencesFragment.<init> -> onCreatePreferences : **UNCLEAR**. AndroidX fragment code, not on disk. App side: AppearancePreferencesFragment.java:29-37; PreferencesActivity.java:84, 91-97.
21. E37edc2e5 FRAMEWORK onCreatePreferences -> lambda$onCreatePreferences$0 : **UNCLEAR**. The registration is verified: AppearancePreferencesFragment.java:32-33 (`requirePreference("pref_groups")`, click listener lambda, the first lambda in this file so `$0` is the right name). res/xml/preferences_appearance.xml:78 has `android:key="pref_groups"`. The click dispatch is AndroidX Preference code, not on disk.
22. Ee5fe910f INTENT lambda$onCreatePreferences$0 -> GroupManagerActivity.<init> : **OK**. Explicit target at AppearancePreferencesFragment.java:34; sent at 35 through Fragment.startActivity (INTENT rule).
23. Ef4742d96 LIFECYCLE GroupManagerActivity.<init> -> onCreate : **OK**. FW ActivityThread.java:2729-2731. SRC GroupManagerActivity.java:36-40.
24. E76aeb3ee FRAMEWORK GroupManagerActivity.onCreate -> onCreateOptionsMenu : **UNCLEAR**. Menu creation is AppCompat code, not on disk. App side: GroupManagerActivity.java:42 (setSupportActionBar), 189-192 (inflates R.menu.menu_groups).
25. Ef7d7a2de FRAMEWORK onCreateOptionsMenu -> onOptionsItemSelected : **UNCLEAR**. AppCompat dispatch, not on disk. App side: GroupManagerActivity.java:195-208. res/menu/menu_groups.xml:7 has `@+id/action_delete_unused_groups`.
26. E28ea1e91 CALL onOptionsItemSelected -> onRemoveUnusedGroups : **OK**. SRC GroupManagerActivity.java:201-202.
27. E0a4ea7ca FRAMEWORK onRemoveUnusedGroups -> lambda$onRemoveUnusedGroups$2 : **UNCLEAR**. The name is correct: lambdas in GroupManagerActivity.java are at line 115 ($0, onEditGroup), 134 ($1, onRemoveGroup) and 149 ($2, onRemoveUnusedGroups). The dialog button is dispatched by the Material/AndroidX AlertController, which is not on disk. The route cites FW core/java/com/android/internal/app/AlertController.java:710,127-140,166. That is the platform AlertController, which MaterialAlertDialogBuilder does not use, so the citation is wrong. FIX (evidence only): replace the AlertController citation with "AndroidX/Material AlertDialog positive-button dispatch (library, not on disk)". Dialogs.java:66-69 (showSecureDialog calls show) is on disk and can stay as the app-side citation.
28. Ed2704c5a FRAMEWORK/non_standard lambda$onRemoveUnusedGroups$2 -> VaultGroup.equals : **UNCLEAR**. The compare happens inside java.util.AbstractSet.removeAll (JDK, not on disk). App side: GroupManagerActivity.java:150-151 (set of all groups, removeAll of used groups); VaultRepository.java:321-330 (getUsedGroups returns the same group instances as getGroups); VaultGroup.java:47-54 (equals: `super.equals(entry) && getName().equals(entry.getName())`). The guard is incomplete. With zero groups the set is empty and the loop never calls equals. FIX (guard text, pending the JDK check): "at least one group exists and every group is used by an entry (so the set is not larger than the used-group list and removeAll takes its contains branch)".

Route 1 totals: 16 OK, 0 ERROR, 12 UNCLEAR.

---

## Route 2: OtpInfo.isAlgorithmValid (17 steps)

Route printout: `python3 -I tools/show_route.py Aegis 'OtpInfo.isAlgorithmValid' --dedupe --max 60`. Verdicts: 16 OK, 0 ERROR, 1 UNCLEAR.

1-7. Same edges as Route 1 steps 1-7 (Eb9515d18, E5b266140, E1ef992ce, E88ed9829, E28ffc58c, Eb76444fd, E3a06baed): **OK**. See Route 1 for the evidence.
8. Ef4d44119 CALL MainActivity.onStart -> VaultManager.loadFrom(VaultFile), state: plain-text vault from an earlier intro run : **UNCLEAR**. Same cross-run rule as Route 1 step 8. App side checked: MainActivity.java:951-965 (readVaultFile, unencrypted branch, `loadFrom` at 965). Writer: IntroActivity.java:100 -> VaultManager.java:65 -> VaultRepository.java:127. The edge text does not name the writer. Suggested note text is the same as Route 1 step 8.
9. Ea2c4bf33 CALL VaultManager.loadFrom(VaultFile) -> loadFrom(VaultFile,VaultFileCredentials) : **OK**. SRC VaultManager.java:96 (`return loadFrom(vaultFile, null);`).
10. E51f87b30 CALL loadFrom(VaultFile,creds) -> VaultRepository.fromFile : **OK**. SRC VaultManager.java:81-83 (guard: throws if already loaded), 85 (`_repo = VaultRepository.fromFile(...)`).
11. Ec427a608 CALL VaultRepository.fromFile -> Vault.fromJson : **OK**. SRC VaultRepository.java:93-95 (guard), 106 (`vault = Vault.fromJson(obj);`).
12. E68d38260 CALL Vault.fromJson -> VaultEntry.fromJson : **OK**. SRC Vault.java:60-63 (version check, throw at 62), 75-77 (entries loop; the edge fires only when the array has at least one element, which matches the guard).
13. E891d0646 CALL VaultEntry.fromJson -> OtpInfo.fromJson : **OK**. SRC VaultEntry.java:87 (`OtpInfo.fromJson(obj.getString("type"), obj.getJSONObject("info"))`).
14. E0e214f1e CALL OtpInfo.fromJson -> TotpInfo.<init>(byte[],String,int,int) : **OK**. SRC OtpInfo.java:121-123 (`case TotpInfo.ID` at 122; `new TotpInfo(secret, algo, digits, obj.getInt("period"))` at 123). TotpInfo.java:23 has the matching 4-argument constructor.
15. E127bdfc6 CALL TotpInfo.<init>(4-arg) -> OtpInfo.<init>(byte[],String,int) : **OK**. SRC TotpInfo.java:24 (`super(secret, algorithm, digits);`). OtpInfo.java:25 defines that constructor.
16. E7ae83abd CALL OtpInfo.<init>(byte[],String,int) -> OtpInfo.setAlgorithm : **OK**. SRC OtpInfo.java:27 (`setAlgorithm(algorithm);`); setAlgorithm is declared at OtpInfo.java:83.
17. Eb6b4b4b1 CALL OtpInfo.setAlgorithm -> OtpInfo.isAlgorithmValid : **OK**. SRC OtpInfo.java:89 (`if (!isAlgorithmValid(algorithm))`, inside setAlgorithm at 83-93). isAlgorithmValid is `public static` at OtpInfo.java:78, so the call is static and needs no receiver dispatch.

Route 2 totals: 16 OK, 0 ERROR, 1 UNCLEAR.

---

## Route 3: GlideOptions.clone (15 steps)

Route printout: `python3 -I tools/show_route.py Aegis 'GlideOptions.clone' --dedupe --max 60`. Verdicts: 8 OK, 0 ERROR, 7 UNCLEAR.

1-6. Same edges as Route 1 steps 1-6 (Eb9515d18, E5b266140, E1ef992ce, E88ed9829, E28ffc58c, Eb76444fd): **OK**. See Route 1. MainActivity.onCreate (193-331) has no finish() call, so the route does not stop in onCreate.
7. E3e74e870 FRAMEWORK/non_standard MainActivity.onCreate -> EntryListView.<init> : **UNCLEAR**. The fragment is created by AndroidX FragmentManager from the layout (not on disk). App side: MainActivity.java:195 (`setContentView(R.layout.activity_main)`); res/layout/activity_main.xml:54-56 (`<fragment android:name="com.beemdevelopment.aegis.ui.views.EntryListView">`).
8. E89bce4c8 LIFECYCLE EntryListView.<init> -> EntryListView.onCreate : **UNCLEAR**. Fragment.onCreate is called by AndroidX FragmentManager (not on disk). App side: EntryListView.java:66 (`extends Fragment`), 84 (`public void onCreate`).
9. Eda7e9bd0 LIFECYCLE EntryListView.onCreate -> EntryListView.onCreateView : **UNCLEAR**. AndroidX Fragment lifecycle (not on disk). App side: EntryListView.java:97-144 (inflate, recycler setup, Glide preloader, adapter).
10. Eaaf7ec29 FRAMEWORK/non_standard EntryListView.onCreateView -> GeneratedRequestManagerFactory.build : **UNCLEAR**. Glide.with lookup is library code (not on disk). App side: EntryListView.java:124 (`Glide.with(this)`). The generated factory is on disk, so the route's note "dataset, not source tree" should cite BUILD com/bumptech/glide/GeneratedRequestManagerFactory.class instead.
11. Eab5f3cfb CALL GeneratedRequestManagerFactory.build -> GlideRequests.<init> : **OK**. BUILD GeneratedRequestManagerFactory.class, build() calls `invokespecial GlideRequests.<init>` at line 18 (checked with tools/extract_calls.py parse_class).
12. E265bbd0b FRAMEWORK/non_standard GlideRequests.<init> -> GlideRequests.setRequestOptions : **UNCLEAR**. The edge needs Glide's RequestManager constructor to call setRequestOptions, which is library code (not on disk). BUILD GlideRequests.class: `<init>` (lines 32-33) calls only RequestManager.<init>; `setRequestOptions(RequestOptions)V` is overridden in GlideRequests, so the virtual target exists.
13. Edb1d9299 CALL GlideRequests.setRequestOptions -> GlideOptions.apply : **OK**. BUILD GlideRequests.class, setRequestOptions, bytecode checked: line 173 `instanceof GlideOptions` then `ifeq` (offsets 1-4); line 174 invokespecial RequestManager.setRequestOptions, then goto (offsets 9-12); line 176 `new GlideOptions`, `invokespecial <init>`, `invokevirtual GlideOptions.apply` (offsets 16-24), then invokespecial RequestManager.setRequestOptions (offset 27). The guard (else branch at 176 when the options are not a GlideOptions) holds.
14. Ec449db03 FRAMEWORK/non_standard GlideOptions.apply -> GlideOptions.autoClone : **UNCLEAR**. The step relies on Glide's RequestOptions.apply calling autoClone() virtually (library, not on disk). BUILD GlideOptions.class: apply (line 610) calls `invokespecial RequestOptions.apply`; the generated bridge at line 27 and `autoClone()GlideOptions` at line 622 exist. The route's own note says this step is not verified.
15. E9d286870 FRAMEWORK/non_standard GlideOptions.autoClone -> GlideOptions.clone : **UNCLEAR**. The step relies on Glide's RequestOptions.autoClone calling clone() virtually (library, not on disk). BUILD GlideOptions.class: `autoClone()GlideOptions` (line 622) calls `invokespecial RequestOptions.autoClone`; `clone()GlideOptions` (line 421) calls `invokespecial RequestOptions.clone`; the bridge `clone()BaseRequestOptions` at line 27 exists, so the virtual target exists.

Route 3 totals: 8 OK, 0 ERROR, 7 UNCLEAR.

---

## Route 4: MainActivity.onIntroResult (22 steps)

Route printout: `python3 -I tools/show_route.py Aegis 'MainActivity.onIntroResult' --dedupe --max 60` (run from /Users/darshan/Desktop/yang/work). Verdicts: 20 OK, 0 ERROR, 2 UNCLEAR.

Note on the printout: it says core/java/android/app/ActivityThread.java, core/java/android/app/Activity.java and core/java/android/view/View.java are "not found in the source tree". All three exist under FW (fw_src/android-8.1.0_r1/core/java/android/...). The citations below use the FW path.

1-7. Same edges as Route 1 steps 1-7 (Eb9515d18, E5b266140, E1ef992ce, E88ed9829, E28ffc58c, Eb76444fd, E3a06baed): **OK**. See Route 1.

8. E0602e719 CALL MainActivity.onStart -> MainActivity.startIntroActivity, guard isVaultInitNeeded : **OK**. SRC MainActivity.java:942-948 (`isVaultInitNeeded()` branch; `startIntroActivity()` at 946).
9. E4ce5043a INTENT MainActivity.startIntroActivity -> IntroActivity.<init> : **OK**. SRC MainActivity.java:603-606 (`new Intent(this, IntroActivity.class)` at 605; `introResultLauncher.launch` at 606); guard `!_isDoingIntro` at 604. The launch goes through the AndroidX launcher, but the target is explicit in app code (INTENT rule).
10. E5e63fbe7 LIFECYCLE IntroActivity.<init> -> IntroActivity.onCreate : **OK**. FW fw_src/.../android/app/ActivityThread.java:2729-2731. SRC IntroActivity.java:35-36.
11. E93598a00 CALL IntroActivity.onCreate -> IntroBaseActivity.addSlide : **OK**. SRC IntroActivity.java:38-41 (addSlide for Welcome, SecurityPicker, SecuritySetup, Done).
12. E1440feb8 ENTERS IntroBaseActivity.addSlide -> S_INTRO_WELCOME : **OK**. SRC IntroBaseActivity.java:183-186 (the first slide triggers onBeforeSlideChanged at 185 and onAfterSlideChanged at 186); IntroActivity.java:38.
13. E6830b6dc ENTERS S_INTRO_WELCOME -> S_INTRO_PICKER : **OK**. SRC IntroBaseActivity.java:80-93 (Next: isFinished at 84, onSaveIntroState at 85, setPagerPosition at 86); IntroActivity.java:57-62 (the imported skip is not taken when the state has imported = false).
14. E32450899 ENTERS S_INTRO_PICKER -> S_INTRO_PICKER@NONE : **UNCLEAR**. The check is made by the platform `android.widget.RadioGroup` (the layout uses the bare `<RadioGroup` tag at res/layout/fragment_security_picker_slide.xml:34). fw_src/android-8.1.0_r1/core/java/android/widget has no RadioGroup.java, so the radio check is not on disk. App side: rb_none at fragment_security_picker_slide.xml:41; SecurityPickerSlide.java:31 (`rg_authenticationMethod`), 72-88 (`onSaveIntroState`: rb_none -> CRYPT_TYPE_NONE at 77-78; `putInt("cryptType")` at 87). The state is written when Next is pressed (IntroBaseActivity.java:85), not at the tap; the edge text says "taps", so the note is only partly accurate.
15. E553f11f7 GUI S_INTRO_PICKER@NONE -> IntroBaseActivity.lambda$onCreate$1@NONE : **OK**. SRC IntroBaseActivity.java:45 (`_btnPrevious` lambda, index $0) and 47 (`_btnNext.setOnClickListener(v -> goToNextSlide())`, index $1). The file has no other `->` or `::` in it, so the javac index is $1. FW fw_src/.../android/view/View.java:6289-6296 (`performClick` calls `li.mOnClickListener.onClick(this)`).
16. E251ac3f4 CALL lambda$onCreate$1 -> IntroBaseActivity.goToNextSlide : **OK**. SRC IntroBaseActivity.java:47, 80-93.
17. E7216511b CALL goToNextSlide -> IntroActivity.onBeforeSlideChanged : **OK**. SRC IntroBaseActivity.java:86 (`setPagerPosition(pos, 1)`), 149-151 (delta overload), 138 (`onBeforeSlideChanged` call); IntroActivity.java:45 (override). Guard at 82-86 (not the last slide, slide finished).
18. E8da5177a CALL IntroActivity.onBeforeSlideChanged -> IntroBaseActivity.skipToSlide : **OK**. SRC IntroActivity.java:50-55 (picker -> setup with cryptType NONE calls `skipToSlide(DoneSlide.class)` at 53). The cryptType NONE value is written at SecurityPickerSlide.java:77-78, 87 and saved to state at IntroBaseActivity.java:85, before the read at IntroActivity.java:52.
19. E3f8e1ae8 ENTERS IntroBaseActivity.skipToSlide -> S_INTRO_DONE : **OK**. SRC IntroBaseActivity.java:104-110 (indexOf at 105, `setPagerPosition(i)` at 110); IntroActivity.java:50-62 (the none skip and the imported skip).
20. E0182bb68 GUI S_INTRO_DONE -> IntroActivity.onDonePressed : **OK**. SRC IntroBaseActivity.java:47 and 80-93. On the last slide (pos == size-1, Done is the 4th slide) the else branch at 90-91 calls `onDonePressed()`. FW View.java:6289-6296 (performClick), on disk.
21. E6073bb9b RESULT IntroActivity.onDonePressed -> MainActivity.lambda$new$1 : **UNCLEAR**. App side checked: IntroActivity.java:86-129. The none path throws at 93-96 when creds is non-null, so the guard "creds null on the none path" holds. Error returns at 104, 113 and 121. `setResult(RESULT_OK)` at 128, `finish()` at 129. MainActivity.java:142-148 registers the launcher at 143, and the lambda is `lambda$new$1` (the first `->` in the class is at 135, which is `$0`; 143 is `$1`). FW: fw_src/.../android/app/Activity.java:5526-5527 (`finish()` calls `finish(DONT_FINISH_TASK_WITH_ACTIVITY)`); fw_src/.../android/app/ActivityThread.java:4253-4265 (`deliverResults` calls `r.activity.dispatchActivityResult`). The hop from `dispatchActivityResult` into the AndroidX ActivityResultRegistry callback that runs the lambda is library code, not on disk, so UNCLEAR. Wording: the edge note "setResult(RESULT_OK) and finish: the list starts" does not describe this hop. Suggested note text: "setResult(RESULT_OK) and finish() return the result to the caller's launcher". The verdict does not change.
22. E5f44da38 CALL MainActivity.lambda$new$1 -> MainActivity.onIntroResult : **OK**. SRC MainActivity.java:142-148 (`_isDoingIntro = false` at 144, RESULT_OK check at 145, `onIntroResult()` at 146).

Route 4 totals: 20 OK, 0 ERROR, 2 UNCLEAR.

---

## Route 5: EntryAdapter.lambda$doesAnyGroupMatchSearchFilter$1 (15 steps)

Route printout: `python3 -I tools/show_route.py Aegis 'EntryAdapter.lambda$doesAnyGroupMatchSearchFilter$1' --dedupe --max 60` (run from /Users/darshan/Desktop/yang/work). Verdicts: 10 OK, 1 ERROR, 4 UNCLEAR.

Lambda names used for checks: graphs/Aegis/auto_calls.json (built from the BUILD classes by tools/extract_calls.py) lists `EntryAdapter.isEntryFiltered -> lambda$isEntryFiltered$0` (line 204), `doesAnyGroupMatchSearchFilter -> lambda$doesAnyGroupMatchSearchFilter$1` (line 226) and `-> lambda$doesAnyGroupMatchSearchFilter$2` (line 228). The source has no other `->` before line 205, so the index order matches the source order.

1-6. Same edges as Route 1 steps 1-6 (Eb9515d18, E5b266140, E1ef992ce, E88ed9829, E28ffc58c, Eb76444fd): **OK**. See Route 1.

7. E8e6d6f10 FRAMEWORK/standard MainActivity.onCreate -> MainActivity.onCreateOptionsMenu : **UNCLEAR**. The call comes from the AndroidX AppCompat menu dispatch, which is not on disk. App side: SRC ui/MainActivity.java:1011-1016 (`onCreateOptionsMenu` body: inflate at 1013, updateLockIcon at 1015).
8. Ed60e6cbd CALL/explicit MainActivity.onCreateOptionsMenu -> EntryListView.setSearchFilter, guard `_pendingSearchQuery == null and _submittedSearchQuery != null` : **UNCLEAR**. The code path is correct: the restore block at MainActivity.java:1066-1073 sits inside onCreateOptionsMenu (1011-1083), and line 1073 calls `_entryListView.setSearchFilter(_submittedSearchQuery)`. The state is the problem. `_submittedSearchQuery` is written only by onQueryTextSubmit at MainActivity.java:1040 (same activity instance) or restored from savedInstanceState at 204-205 (saved at 419-420). In the standard configuration (fresh launch, savedInstanceState null) it stays null, so this edge fires only after a recreate or an earlier submit in the same instance. The edge text does not name either writer, so the cross-run rule gives UNCLEAR. Suggested note text for the STATE label: "a search was submitted in this activity instance (MainActivity.java:1040) or the activity is recreated with savedInstanceState (MainActivity.java:204-205, saved at 419-420)".
9. Ececfe4d5 CALL/explicit EntryListView.setSearchFilter -> EntryAdapter.setSearchFilter : **OK**. SRC ui/views/EntryListView.java:279-280 (`_adapter.setSearchFilter(search)` at 280).
10. Ef330c979 CALL/explicit EntryAdapter.setSearchFilter -> EntryAdapter.refreshEntryList, guard new text differs : **OK**. SRC ui/views/EntryAdapter.java:267 (method), 271 (`if (!Objects.equals(_searchFilter, newSearchFilter))`), 272-273 (assignment, refreshEntryList call).
11. Ed33e097b CALL/explicit EntryAdapter.refreshEntryList -> EntryAdapter.calculateShownEntries : **OK**. SRC EntryAdapter.java:280 (`calculateShownEntries(_entryList.getEntries())`).
12. Efa06baf0 CALL/explicit calculateShownEntries -> EntryAdapter.isEntryFiltered, [STATE: "The vault holds at least one entry (the loop in Vault.toJson(EntryFilter) runs, Vault.java:9-12)"] : **ERROR**. The edge's real mechanism is the for loop in calculateShownEntries (EntryAdapter.java:299-302: `for (VaultEntry entry : entries)` at 301, `if (!isEntryFiltered(entry))` at 302). The STATE cite does not support the edge. Vault.java:9-12 are import lines, not a loop. The method named in the note, Vault.toJson(EntryFilter), is at Vault.java:27 and is not on this route. The state itself is real: in the standard configuration (no vault file, fresh install) the entry list is empty, so isEntryFiltered is never called, and the STATE label is needed.
   FIX: edge Efa06baf0 (calculateShownEntries -> isEntryFiltered), field STATE, new text: "the entry list passed in is not empty: the for loop at EntryAdapter.java:301 runs once per entry". Justifying source lines: EntryAdapter.java:280 (the list is `_entryList.getEntries()`), 299-302 (the loop and the call). Remove the Vault.java:9-12 and Vault.toJson(EntryFilter) reference from the note and the evidence.
13. E9b4d2bef FRAMEWORK/standard EntryAdapter.isEntryFiltered -> EntryAdapter.lambda$isEntryFiltered$0 : **UNCLEAR**. The predicate is run by `java.util.stream` allMatch, which is JDK code and not on disk. App side: SRC EntryAdapter.java:200 (guard `_searchFilter != null`), 204-210 (`Arrays.stream(tokens).allMatch(token -> ...)`, lambda at 205). The lambda name is confirmed as $0 by auto_calls.json (line 204), the first lambda in the file.
14. E399cebc2 CALL/explicit lambda$isEntryFiltered$0 -> EntryAdapter.doesAnyGroupMatchSearchFilter, guard SEARCH_IN_GROUPS and the token did not match issuer, name or note : **OK**. SRC EntryAdapter.java:206-209 (the `||` chain: the groups term runs only when the earlier terms are false, and the mask check is at 209). The method is declared at 225 (`private boolean doesAnyGroupMatchSearchFilter`).
15. E4bf8b9e0 FRAMEWORK/standard EntryAdapter.doesAnyGroupMatchSearchFilter -> EntryAdapter.lambda$doesAnyGroupMatchSearchFilter$1 : **UNCLEAR**. The filter runs inside `java.util.stream`, which is JDK code and not on disk. App side: SRC EntryAdapter.java:226-227 (`_groups.stream().filter(group -> entryGroupUUIDs.contains(group.getUUID()))`). $1 is this filter lambda, which is the second lambda in the file (auto_calls.json line 226). The `anyMatch` at 229 drives the pipeline, so it is a correct citation for the run, but the name test itself is lambda$doesAnyGroupMatchSearchFilter$2 (source 229, auto_calls.json line 228), which is not on this route. The edge text ("keeps the groups that the entry belongs to") matches $1. Suggested note text: add "the group-name test is in lambda$doesAnyGroupMatchSearchFilter$2 (EntryAdapter.java:229), which this route does not reach".

Route 5 totals: 10 OK, 1 ERROR, 4 UNCLEAR.

---

## Final table (G5 routes)

| Route | Target | Steps | OK | ERROR | UNCLEAR |
|---|---|---|---|---|---|
| 1 | VaultGroup.equals | 28 | 16 | 0 | 12 |
| 2 | OtpInfo.isAlgorithmValid | 17 | 16 | 0 | 1 |
| 3 | GlideOptions.clone | 15 | 8 | 0 | 7 |
| 4 | MainActivity.onIntroResult | 22 | 20 | 0 | 2 |
| 5 | EntryAdapter.lambda$doesAnyGroupMatchSearchFilter$1 | 15 | 10 | 1 | 4 |
| **Total** | | **97** | **70** | **1** | **26** |

ERROR count: 1 (Route 5 step 12, FIX above). All other ERRORs: none.

<!-- END -->
