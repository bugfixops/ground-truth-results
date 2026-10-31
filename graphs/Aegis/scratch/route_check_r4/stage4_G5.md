# Stage 4 route check R4-G5 (Aegis schema 2, round 4, read-only)

Date: 2026-10-27
Sources: graph_def.py via tools/show_route.py (Aegis, --dedupe --max 60); app source final_java_only/Aegis/app/Aegis-#v3.4.2/app/src/main/java/com/beemdevelopment/aegis; AOSP 8.1.0_r1 lines printed by sed (ActivityThread.java, Activity.java, LoadedApk.java, View.java, AlertController.java).

Conventions used: androidx, Material, Hilt-generated, Glide, Room, libsu, protobuf and JDK bodies are not on disk, so their dispatch hops are UNCLEAR; app call sites, guards and states are checked against the source. A framework citation that is AOSP platform code is not accepted for a path that the app runs through an androidx class.

## Summary

| Route | Target | Steps | ERROR | UNCLEAR | OK |
|---|---|---|---|---|---|
| 1 | VaultGroup.equals | 28 | 24, 28 | 2, 3, 8, 10, 13, 16, 18, 19, 20, 21, 25, 27 | 14 |
| 2 | OtpInfo.isAlgorithmValid | 17 | 8, 11 | 2, 3 | 13 |
| 3 | GlideOptions.clone | 15 | none | 2, 3, 7-15 | 4 |
| 4 | MainActivity.onIntroResult | 22 | 8, 17, 20 | 2, 3, 9, 14, 21 | 14 |
| 5 | EntryAdapter.lambda$doesAnyGroupMatchSearchFilter$1 | 15 | 12, 15 | 2, 3, 7, 13 | 9 |

Totals: 5 routes, 97 steps, ERROR 9, UNCLEAR 34, OK 54.

## Route 1: VaultGroup.equals

Step 2 (E5b266140, AegisApplication.<init> -> Hilt_AegisApplication.onCreate): UNCLEAR. Printed: AegisApplication.java:5-6 (@HiltAndroidApp, extends AegisApplicationBase); ActivityThread.java:5740 (callApplicationOnCreate). Source says: the Hilt superclass is generated and not on disk. Fix proposed: none (no source to justify a change).

Step 3 (E1ef992ce, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate): UNCLEAR. Generated code, not on disk. Fix proposed: none.

Step 8 (E20e76e09, MainActivity.onStart -> MainActivity.loadEntries): UNCLEAR, reason "needs earlier run". Guard checked and correct: MainActivity.java:942-947 (isVaultInitNeeded return at 947), 950-974 (readVaultFile; returns at 960 and 971 are in catch blocks), 963-965 (loadFrom), 976-977 (not loaded, not taken), 978 (_loaded), 991-992 (else, loadEntries). The needs_state names the earlier intro run and the reader lines (951-973) but not the writer. Writer: IntroActivity.java:100 (_vaultManager.initNew(creds)), which calls repo.save() at VaultManager.java:64-65. Fix proposed: text only, add the writer lines (IntroActivity.java:100; VaultManager.java:64-65) to the needs_state text. Route reachability is not changed.

Step 10 (E887b87bf, S_LIST -> MainActivity.onOptionsItemSelected): UNCLEAR. The AppCompat toolbar dispatch is androidx and not on disk. App side confirmed: MainActivity.java:1086-1093 (override and if chain). Fix proposed: none.

Step 13 (E640fb9eb, MainActivity.startPreferencesActivity(Class,String) -> PreferencesActivity.<init>): UNCLEAR. The intent target is correct (MainActivity.java:831). The launch is preferenceResultLauncher.launch(intent) at 834, registered at 166-167 with androidx StartActivityForResult; that library body is not on disk. Fix proposed: none.

Step 16 (E382bc001, MainPreferencesFragment.<init> -> onCreatePreferences): UNCLEAR. androidx.fragment attach and commit are not on disk. Fix proposed: none.

Step 18 (E3452b602, S_SETTINGS_MAIN -> PreferencesActivity.onPreferenceStartFragment): UNCLEAR. The callback is implemented at PreferencesActivity.java:19 and 80-84; the androidx dispatch that calls it is not on disk. Relay note: this method serves every row with android:fragment; the row is selected by the guard at step 19. Fix proposed: none.

Step 19 (Eba86fd82, PreferencesActivity.onPreferenceStartFragment -> AppearancePreferencesFragment.<init>, non_standard): UNCLEAR. App side confirmed: PreferencesActivity.java:81 calls getFragmentFactory().instantiate(getClassLoader(), pref.getFragment()); res/xml/preferences.xml:8 names AppearancePreferencesFragment. The body of androidx FragmentFactory.instantiate is not on disk. The guard states a precondition from the XML row; that is accurate. Fix proposed: none.

Step 20 (Ef17c8ca0, AppearancePreferencesFragment.<init> -> onCreatePreferences): UNCLEAR. androidx.fragment body, not on disk. Fix proposed: none.

Step 21 (E37edc2e5, AppearancePreferencesFragment.onCreatePreferences -> lambda$onCreatePreferences$0): UNCLEAR. Lambda name checked: AppearancePreferencesFragment.java:33 is the first lambda in the class (index 0). The androidx click dispatch that calls it is not on disk. Fix proposed: none.

Step 24 (E76aeb3ee, GroupManagerActivity.onCreate -> GroupManagerActivity.onCreateOptionsMenu): ERROR (text-only guard omission). Printed: GroupManagerActivity.java:38-39 (if (abortIfOrphan(savedInstanceState)) { return; }) ends onCreate early; the edge carries no guard text. abortIfOrphan returns false when savedInstanceState is null (AegisActivity.java:155-156), so on a fresh start the edge is reached; the route is unaffected. Framework: ActivityThread.java:2740-2741 runs performStart only if !r.activity.mFinished. The menu creation itself is androidx (UNCLEAR). Fix proposed: add guard text "onCreate did not return early at GroupManagerActivity.java:38-39 (abortIfOrphan false; false on a fresh start since savedInstanceState is null, AegisActivity.java:155-156)".

Step 25 (Ef7d7a2de, GroupManagerActivity.onCreateOptionsMenu -> onOptionsItemSelected): UNCLEAR. AppCompat dispatch not on disk. App side confirmed: GroupManagerActivity.java:195-208. Fix proposed: none.

Step 27 (E0a4ea7ca, GroupManagerActivity.onRemoveUnusedGroups -> lambda$onRemoveUnusedGroups$2): UNCLEAR. App side confirmed: the method starts at GroupManagerActivity.java:144 with no enclosing if; the lambda is the third lambda in source order (lines 115, 134, 149, 184-185), so index 2 matches; Dialogs.java:66-69 calls dialog.show(). The cited AOSP lines do not decide this path: the dialog is built by MaterialAlertDialogBuilder, which yields an androidx.appcompat AlertDialog (AppearancePreferencesFragment.java:7, and the cast at line 59 of a Material builder dialog), so the button handler is androidx's AlertController, not on disk. Fix proposed: none in graph; the cited platform lines AlertController.java:127-140, 166, 710 and View.java:6289-6296 describe a different class. The step is standard behaviour but the source on disk does not decide it.

Step 28 (Ed2704c5a, GroupManagerActivity.lambda$onRemoveUnusedGroups$2 -> VaultGroup.equals): ERROR (guard text omits a necessary condition); the JDK part is INFERRED. Printed: GroupManagerActivity.java:150-151 (new HashSet of getGroups; removeAll(getUsedGroups())); VaultRepository.java:317-319 (getGroups returns the collection) and 321-330 (getUsedGroups). UUIDMap.java:163-172 is the UUID equals that VaultGroup.java:54 reaches through super.equals. The JDK AbstractSet.removeAll (not on disk, INFERRED) calls c.contains for each set element when set size is not greater than c.size(), and ArrayList.indexOf calls equals on the element. The printed guard "every group is used by an entry" is the right trigger, since the used list is a subset of the groups. But with zero groups the set is empty, nothing is compared, and VaultGroup.equals is never called, while "every group is used" holds vacuously. Fix proposed: add "and at least one group exists (VaultRepository.java:317-319)" to the guard text. The route to a real vault with groups is unaffected. Also note: the guard depends on vault data (at least one group, every group used), which is not in needs_state (blank for this step); the route header says state=file only.

Mistakes check (route 1): no first-resume shortcut; no static flag; no file:// or content:// issue; early returns checked (step 8 and step 15 guards carry them, step 24 omitted); shared relay onPreferenceStartFragment handled by step 19 guard; step 12 evidence label says "(bytecode)" but cites source line 827, which is the call (no effect).

Counts (route 1): 28 steps, ERROR 2 (24, 28), UNCLEAR 12, OK 14.

## Route 2: OtpInfo.isAlgorithmValid

Steps 1 to 7 have the same edge ids and text as route 1 steps 1 to 7, so the verdicts are the same (1, 4, 5, 6, 7 OK; 2, 3 UNCLEAR, see route 1).

Step 2 (E5b266140, AegisApplication.<init> -> Hilt_AegisApplication.onCreate): UNCLEAR. Hilt generated superclass, not on disk. Fix proposed: none.

Step 3 (E1ef992ce, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate): UNCLEAR. Generated code, not on disk. Fix proposed: none.

Step 8 (Ef4d44119, MainActivity.onStart -> VaultManager.loadFrom(VaultFile)): ERROR (text-only guard omission). Printed: MainActivity.java:942-947 (if isVaultInitNeeded() { ... startIntroActivity(); return; }, return at 947); 951-965 (if !isVaultLoaded(); readVaultFile; return at 960 in its catch; if !isEncrypted() at 963; loadFrom at 965). Source says the call at 965 is reached only when the return at 947 is not taken and the return at 960 is not taken. The edge guard lists only "not loaded yet" and "not encrypted". Fix proposed: add to the guard "isVaultInitNeeded() false (no return at MainActivity.java:947) and readVaultFile did not throw (no return at 960)". Route unaffected on a cold start with a vault file. The needs_state (earlier intro run) is UNCLEAR, reason "needs earlier run", with the writer not named (see route 1 step 8: IntroActivity.java:100, VaultManager.java:64-65).

Step 11 (E567fe5c3, VaultRepository.fromFile -> Vault.fromJson): ERROR (text-only guard omission). Printed: VaultRepository.java:92-95 (fromFile; if (file.isEncrypted() && creds == null) { throw new IllegalArgumentException(...); }); 98-106 (try; obj from getContent; vault = Vault.fromJson(obj) at 106); 107-109 (catch converts to VaultRepositoryException, not a guard for reaching the call). Source says the call at 106 is reached only when the throw at 93-95 is not taken. The edge has an empty guard. Fix proposed: add guard "the file is not encrypted or creds is not null (VaultRepository.java:93-95 throws otherwise)". Route unaffected: the route's file is plain text and creds are null, so the throw is not taken.

Step 14, 9, 10, 12, 13, 15, 16, 17 and steps 1, 4 to 7: OK (edges, classes and guards match the printed lines; no setAlgorithm override in the otp package, grep). Step 12 guard: Vault.java:61-63 (throw when ver > VERSION) and the loop at 76-77 (at least one entry) match. Step 14 guard: OtpInfo.java:121-122 (switch on type, case TotpInfo.ID "totp", TotpInfo.java:13). The entry data (TOTP type, entries) comes from the plain-text vault file of step 8 (route header state=file); no separate needs_state.

Counts (route 2): 17 steps, ERROR 2 (8, 11), UNCLEAR 2 (2, 3), OK 13.

## Route 3: GlideOptions.clone

Steps 1, 4, 5, 6: OK (same edges, text and evidence as route 2 steps 1, 4, 5, 6; manifest lines 21-27 and 44-51, AegisApplicationBase.java:45-67 with no guard on the ENTERS edge, MainActivity.java:192-194 with ActivityThread 2729-2731, 2741).

Step 2 (E5b266140, AegisApplication.<init> -> Hilt_AegisApplication.onCreate): UNCLEAR. Hilt-generated superclass, not on disk. Fix proposed: none.

Step 3 (E1ef992ce, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate): UNCLEAR. Generated code, not on disk. Fix proposed: none.

Step 7 (E3e74e870, MainActivity.onCreate -> EntryListView.<init>, non_standard): UNCLEAR. Printed: MainActivity.java:192-195 (onCreate; super.onCreate at 194; setContentView(R.layout.activity_main) at 195, with no return above it); res/layout/activity_main.xml:54-56 (the fragment tag with android:name EntryListView). Source says the fragment is created while setContentView inflates the layout, by the androidx FragmentManager, which is not on disk. The app side of the edge is right: nothing returns early before setContentView. Fix proposed: none (androidx body).

Step 8 (E89bce4c8, EntryListView.<init> -> EntryListView.onCreate): UNCLEAR. Printed: EntryListView.java:84-88 (onCreate: super.onCreate, _adapter = new EntryAdapter(this), _showProgress = false; no return). Source confirms the target method and that it has no guard. The Fragment.onCreate dispatch is androidx, not on disk, as in route 1 step 20. Fix proposed: none.

Step 9 (Eda7e9bd0, EntryListView.onCreate -> EntryListView.onCreateView): UNCLEAR. Printed: EntryListView.java:97 (onCreateView starts), and onCreate (84-88) has no return before the edge. The androidx dispatch is not on disk. Fix proposed: none.

Step 10 (Eaaf7ec29, EntryListView.onCreateView -> GeneratedRequestManagerFactory.build, non_standard): UNCLEAR. Printed: EntryListView.java:124 (`RecyclerViewPreloader<VaultEntry> preloader = new RecyclerViewPreloader<>(Glide.with(this), modelProvider, _preloadSizeProvider, 10);`). The line is not under any if or return in onCreateView (lines 97-124 printed: the only ifs, at 108 and 115, are inside listener bodies). Source says Glide.with(this) reaches the generated factory inside the Glide library, which is not on disk. Fix proposed: none.

Step 11 (Eab5f3cfb, GeneratedRequestManagerFactory.build -> GlideRequests.<init>): UNCLEAR. Generated class, not on disk (show_route evidence: the call is in the build class, line 18). Fix proposed: none.

Step 12 (E265bbd0b, GlideRequests.<init> -> GlideRequests.setRequestOptions): UNCLEAR. The Glide RequestManager constructor is library code, not on disk. Fix proposed: none.

Step 13 (Edb1d9299, GlideRequests.setRequestOptions -> GlideOptions.apply): UNCLEAR. Guard text: "the options passed in are not already a GlideOptions (GlideRequests.java:176 is the else branch of the instanceof check)". GlideRequests.java is generated and not on disk, so neither the else branch nor line 176 can be checked. No guard invented. Fix proposed: none (cannot be verified on disk).

Step 14 (Ec449db03, GlideOptions.apply -> GlideOptions.autoClone): UNCLEAR. Glide RequestOptions.apply is library code, not on disk; the generated GlideOptions is not on disk either. Fix proposed: none.

Step 15 (E9d286870, GlideOptions.autoClone -> GlideOptions.clone): UNCLEAR. Glide RequestOptions.autoClone is library code, not on disk. This is the route's target edge, so the route's end is not verified. Fix proposed: none.

Mistakes check (route 3): no first-resume shortcut; no static flag; no file:// or content:// issue; early returns checked (none between MainActivity.onCreate entry and setContentView, none in EntryListView.onCreate, none above Glide.with at line 124); step 13 bytecode line (GlideRequests.java:176) is generated and unverified; no shared relay node in this route.

Counts (route 3): 15 steps, ERROR 0, UNCLEAR 11 (2, 3, 7-15), OK 4 (1, 4, 5, 6).

## Route 4: MainActivity.onIntroResult

Steps 1 to 7: OK (same edges and text as route 2 steps 1 to 7; MainActivity.java:938-948 for the onStart lines, no return at 941).

Step 2 (E5b266140, AegisApplication.<init> -> Hilt_AegisApplication.onCreate): UNCLEAR. Hilt-generated superclass, not on disk. Fix proposed: none.

Step 3 (E1ef992ce, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate): UNCLEAR. Generated code, not on disk. Fix proposed: none.

Step 8 (E0602e719, MainActivity.onStart -> MainActivity.startIntroActivity): ERROR (text-only, guard incomplete). Printed: MainActivity.java:942-948 (if (_vaultManager.isVaultInitNeeded()) { ... startIntroActivity(); return; }); VaultManager.java:226-228 (isVaultInitNeeded returns !isVaultLoaded() && !VaultRepository.fileExists(_context)). Source says the branch needs two conditions: no vault loaded and no vault file. The guard text gives only "no vault file exists". Fix proposed: change the guard text to "isVaultInitNeeded() true: no vault loaded and no vault file exists (VaultManager.java:226-228)". Route unaffected: on a cold start the manager is not loaded yet.

Step 9 (E4ce5043a, MainActivity.startIntroActivity -> IntroActivity.<init>, INTENT): UNCLEAR. Printed: MainActivity.java:603-607 (if (!_isDoingIntro) { new Intent(this, IntroActivity.class); introResultLauncher.launch(intro); _isDoingIntro = true; }). The guard sense is right, and _isDoingIntro is an instance field (MainActivity.java:106, private boolean). The launch goes through the androidx ActivityResultLauncher, which is not on disk, so the hop to IntroActivity.<init> is not verified. Fix proposed: none.

Step 10 (E5e63fbe7, IntroActivity.<init> -> IntroActivity.onCreate): OK (see OK count).

Step 14 (E32450899, S_INTRO_PICKER -> S_INTRO_PICKER@NONE, ENTERS): UNCLEAR. Printed: res/layout/fragment_security_picker_slide.xml:41 (android:id="@+id/rb_none"); ui/slides/SecurityPickerSlide.java:63-88 (isFinished reads getCheckedRadioButtonId; onSaveIntroState maps rb_none to CRYPT_TYPE_NONE and writes cryptType). Source says the checked radio is set by platform RadioGroup/RadioButton (not read), and the value is saved only on Next (IntroBaseActivity.java:85), not on the tap. The @NONE uses in steps 15 and 18 happen after Next, so the route is not broken. Fix proposed: none in graph; optional text change to "the user checks the None radio (cryptType is stored on Next, IntroBaseActivity.java:85)".

Step 17 (E7216511b, IntroBaseActivity.goToNextSlide@NONE -> IntroActivity.onBeforeSlideChanged@NONE, CALL): ERROR (wrong source). Printed: IntroBaseActivity.java:86 (setPagerPosition(pos, 1) in goToNextSlide); 138 (if (!onBeforeSlideChanged(oldSlide, newSlide)) inside private setPagerPosition(int)); 149-151 (private setPagerPosition(int pos, int delta) { pos += delta; setPagerPosition(pos); }). IntroActivity.java:45 (the override). Source says goToNextSlide never calls onBeforeSlideChanged directly; the call is in setPagerPosition(int), reached through setPagerPosition(int,int). The guard (IntroBaseActivity.java:82-86) is right. Fix proposed: change the source to IntroBaseActivity.setPagerPosition(int) (the call at line 138), or add the hops goToNextSlide -> setPagerPosition(int,int) (line 149-151) -> setPagerPosition(int) before the edge, keeping the guard on the goToNextSlide hop. Route reachability is unaffected because the same chain runs.

Step 20 (E0182bb68, S_INTRO_DONE -> IntroActivity.onDonePressed, GUI): ERROR (text-only, guard omitted). Printed: IntroBaseActivity.java:47 (Next listener); 80-93 (goToNextSlide: if (pos != _slides.size() - 1) {...} else { onDonePressed(); } at 82 and 90-91). Source says onDonePressed has one caller (IntroBaseActivity.java:91, the else branch, which runs when the pager is on the last slide). The edge's guard is empty. The state S_INTRO_DONE already implies the last slide, so the route is unaffected. Fix proposed: add guard text "the pager is on the last slide (IntroBaseActivity.java:82 false; else branch 90-91 calls onDonePressed)".

Step 21 (E6073bb9b, IntroActivity.onDonePressed -> MainActivity.lambda$new$1, RESULT): UNCLEAR. Printed: IntroActivity.java:86-129 (onDonePressed: 92-96 cryptType check, throw at 96; 100 initNew; 104, 113, 121 returns in the catch blocks; 126 setIntroDone; 128-129 setResult(RESULT_OK), finish()); ActivityThread.java:4253-4264 (deliverResults calls r.activity.dispatchActivityResult; verified); Activity.java:5526-5527 (finish delegates; verified); MainActivity.java:143-148 (launcher lambda, the second field-initializer lambda after the one at 135, so lambda$new$1 is the right name). The guard is checked and right: the vault was created or imported, with no error return, and the none path needs creds null (line 93). The last hop from dispatchActivityResult to the launcher callback is androidx ActivityResultRegistry, which is not on disk, so UNCLEAR. Fix proposed: none.

Step 22 (E5f44da38, MainActivity.lambda$new$1 -> MainActivity.onIntroResult): OK (see OK count). Guard at MainActivity.java:145 is right and onIntroResult is defined at line 752.

Mistakes check (route 4): no first-resume shortcut (cold start from ENTRY). No static flag: _isDoingIntro is an instance field (MainActivity.java:106). No file:// or content:// issue. Early returns: step 8 guard includes the return at 947, but its text is incomplete (ERROR above); step 21 guard includes the returns at 104, 113, 121. Lambda names checked: MainActivity lambda$new$1 (field lambdas at 135 = index 0, 143 = index 1); IntroBaseActivity lambda$onCreate$1 (lines 45 = index 0, 47 = index 1). Shared relay: setPagerPosition(int) (IntroBaseActivity.java:138) is shared by goToNextSlide, goToPreviousSlide and skipToSlide. Step 19 (skipToSlide -> S_INTRO_DONE) is OK because its relay guard is the union of both callers (IntroActivity.java:50-55, 57-62), and the pager gate at 138 returns false for Picker to Done. Bytecode line: step 11 cites 38-41; dedupe merges the four addSlide calls into one edge; the Welcome call is line 38 (used by step 12); the earlier bytecode note of line 41 is the DoneSlide call, so no error.

Counts (route 4): 22 steps, ERROR 3 (8, 17, 20), UNCLEAR 5 (2, 3, 9, 14, 21), OK 14 (1, 4, 5, 6, 7, 10, 11, 12, 13, 15, 16, 18, 19, 22).

## Route 5: EntryAdapter.lambda$doesAnyGroupMatchSearchFilter$1

Steps 1, 4, 5, 6: OK (same edges, text and evidence as route 3 steps 1, 4, 5, 6).

Step 2 (E5b266140, AegisApplication.<init> -> Hilt_AegisApplication.onCreate): UNCLEAR. Hilt-generated superclass, not on disk. Fix proposed: none.

Step 3 (E1ef992ce, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate): UNCLEAR. Generated code, not on disk. Fix proposed: none.

Step 7 (E8e6d6f10, MainActivity.onCreate -> MainActivity.onCreateOptionsMenu): UNCLEAR. The AppCompat dispatch that calls onCreateOptionsMenu is androidx, not on disk. App side: MainActivity.onCreate (MainActivity.java:192-264) has no return, and onCreateOptionsMenu starts at MainActivity.java:1011 as cited. Fix proposed: none.

Step 8 (Ed60e6cbd, MainActivity.onCreateOptionsMenu -> EntryListView.setSearchFilter): OK. Guard checked: MainActivity.java:1066-1073 (if _pendingSearchQuery != null {...} else if _submittedSearchQuery != null { ... setSearchFilter at 1073 }). The guard is false on a plain cold start: savedInstanceState is null, so the restore at MainActivity.java:202-205 does not run and the field (line 109) stays null. The guard is true only after a search was submitted (set at MainActivity.java:1040) or restored on a recreate (line 205). The guard states that precondition correctly, so no fix.

Step 12 (Efa06baf0, EntryAdapter.calculateShownEntries -> EntryAdapter.isEntryFiltered): ERROR (wrong STATE citation, text-only). The STATE says "the loop in Vault.toJson(EntryFilter) runs, Vault.java:9-12". Vault.java:9-12 are import lines (imports at 3-12, class at 14). The Vault.toJson(EntryFilter) loop is at Vault.java:30, and that loop is not the one on this route. The loop that runs here is the for loop over the entries list at EntryAdapter.java:301-302, which the edge's own guard already cites. The edge guard is correct. Fix proposed: change the STATE text to "[STATE: the entry list holds at least one entry, so the for loop at EntryAdapter.java:301 runs]". Route reachability is not changed.

Step 13 (E9b4d2bef, EntryAdapter.isEntryFiltered -> EntryAdapter.lambda$isEntryFiltered$0): UNCLEAR. The guard "_searchFilter is not null (EntryAdapter.java:200)" is right: no return sits between the field reads at 195-198 and the if at 200. The hop from the terminal allMatch (EntryAdapter.java:205) to the lambda is java.util.stream, not on disk (INFERRED). Fix proposed: none.

Step 15 (E4bf8b9e0, EntryAdapter.doesAnyGroupMatchSearchFilter -> EntryAdapter.lambda$doesAnyGroupMatchSearchFilter$1): ERROR (text-only guard omission). Printed: EntryAdapter.java:225-229 (the method reads _groups.stream() at 226; the filter lambda at 227 is lambda$doesAnyGroupMatchSearchFilter$1, index 1 after lambda$isEntryFiltered$0 at 205, and lambda$doesAnyGroupMatchSearchFilter$2 is at 229). The filter lambda runs once per element of _groups, so this edge is reached only when _groups holds at least one group. The edge has no guard text. _groups is declared at EntryAdapter.java:57 with no initializer, and setGroups (EntryAdapter.java:339) is the only assignment in that file. If setGroups never ran, _groups is null and line 226 throws before the lambda runs. With an empty _groups the lambda never runs. Fix proposed: add guard text "_groups is set (setGroups, EntryAdapter.java:339) and holds at least one group; the filter lambda runs once per group (EntryAdapter.java:226-227)". The route is reachable only on a vault with at least one group, which the route header (state=data) does not say.

Steps 9, 10, 11, 14: OK (edges, guards and lines match: EntryListView.java:280 is unconditional; EntryAdapter.java:271-273 has the !Objects.equals guard; EntryAdapter.java:280 is the call in refreshEntryList; EntryAdapter.java:206-209 has the || chain, and the group check at 209 runs only when the three earlier checks are false).

Mistakes check (route 5): no first-resume shortcut (cold start from ENTRY). No static flag: _searchFilter (EntryAdapter.java:77), _searchBehaviorMask (EntryAdapter.java:73) and _submittedSearchQuery (MainActivity.java:109) are instance fields. No file:// or content:// issue. Early returns: MainActivity.onCreate has none (192-264), and isEntryFiltered has none before the token block (195-200). Lambda names: lambda$isEntryFiltered$0 at 205, lambda$doesAnyGroupMatchSearchFilter$1 at 227, lambda$doesAnyGroupMatchSearchFilter$2 at 229 (grep -n "->" lists no earlier lambda in the file). Shared relay: calculateShownEntries (EntryAdapter.java:299) has three callers (181, 280, 388); the route uses the call at 280, and its edge to isEntryFiltered is the same for every caller, so the shared node adds no route-specific guard. doesAnyGroupMatchSearchFilter has one caller (line 209). Guard-less edge: step 15 (above).

Counts (route 5): 15 steps, ERROR 2 (12, 15), UNCLEAR 4 (2, 3, 7, 13), OK 9 (1, 4, 5, 6, 8, 9, 10, 11, 14).
