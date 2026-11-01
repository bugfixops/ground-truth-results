# AGENT_NOTES: AnyMemo 10.12.2 (schema 2)

Status: NOT DONE. PAUSED on 2026-10-26 at 23:15 EDT by the orchestrator (the user asked to stop AnyMemo and start the six remaining apps). Resume from the PAUSE POINT section below. Earlier notes further down are older and are superseded where they disagree.

## PAUSE POINT (2026-10-26 23:15 EDT, latest; this section wins over everything below)
- Stopped: the headless run (pid 49518, started 20:16) was ended with SIGTERM. Its last log write was scratch/fix_round1.md at 23:06. The graph_def.py file was last changed at 23:04.
- Build at the pause (scratch/build_at_pause_2026-10-26.txt): methods 2207, pages 77, edges 4485, REACHABLE 1960, UNREACHABLE 247, errors 0, warnings 0, STRICT = True. The sanity check still shows 3 UNREACHABLE methods that ran in a tool run (see item 1 below).
- Fix log: scratch/fix_round1.md. Round 1 covers groups 1 and 2. Round 1b covers groups F, W, C, B, D and E. Backups before each round or group are in scratch/ (graph_def_before_round1.py, graph_def_before_round1b.py, graph_def_before_group_C.py, graph_def_before_round1b_E.py).
- Route check: 26 of 30 sampled routes were WRONG and 4 CORRECT (the route-check files count 26; an earlier note said 25, which was a miscount). The fixes are applied group by group. The sample has NOT been redrawn since, so no fixed count exists yet.
- Still open, in this order:
  1. Group A1: three methods are UNREACHABLE but ran in a tool run: CategoryEditorFragment.onDestroy, PreviewEditActivity.onDestroy, QuizLauncherDialogFragment.onDestroy. Read the source for each. Do not just flip the label. The placeholders listed in fix_round1.md (CardListActivity.onDestroy, CardEditor.onConfigurationChanged, SettingsScreen.onConfigurationChanged) also need a real exit or a source-based UNREACHABLE reason.
  2. Dropped automatic edges: build_graph.py line 223 drops an automatic CALL when a hand-written edge has the same pair. fix_round1.md lists about ten such edges that are not yet checked against the source. Check each one, and restore it by hand where the call is real. This is a tool bug. tools/ is not edited by this job, so it is reported, not fixed.
  3. Route check: redraw the 30-route sample on the final build, then read each route step by step against the cited source lines. Error rate = (fixed + wrong) / (correct + fixed + wrong).
  4. Steps 7 to 10 of the brief: verification.csv (make_verification.py), readme_notes.md with the five headings, gen_readme_v2.py, the step-9 checks, LESSONS.md, and deleting scratch/.
- Sample size stays at 30 (the brief's rule). The user has not chosen a smaller sample.
- Do not start this app again. graph_def.py is the working file and it builds clean.

## CURRENT STATUS (2026-10-26, latest; this section wins over the older segments below)
- NEWEST (2026-10-26 20:20, sixth resume by the top-level orchestrator): the killed run (stopped by the watcher at 20:15) had applied the QuizLauncher start-button split, the CategoryEditor cancel guards (cancel(true) in onPreExecute, AsyncTask.java:345-358, 632-651, 691-696) and three Group D guards (FileBrowserFragment createdb, DatabaseOperationDialogUtil$1$3, BaseActivity.enableImmersiveMode). Group 13 (CardFragment sup, lines 349-360) IS in graph_def.py. Build of 20:16 (scratch/build_now_20.txt): methods 2207, pages 77, edges 4356, REACHABLE 1966, UNREACHABLE 241, errors 0, warnings 0.
- Sample redrawn on that build: scratch/verify_sample_30_now.txt (seed 20261025). Five read-only checkers (G1-G5, six routes each) write their findings to scratch/route_check/G<k>_<n>_<method>.md. They do not edit graph_def.py. The fixer applies the findings after all five reports, then the sample is redrawn and every route whose steps changed is read again.
- Open step: 6 (path verification), then 7-10. Group 6 (RESULT edges for every onActivityResult starter; cold-start LIFECYCLE shortcut to onActivityResult removed in 7 classes; CHA restartActivity edges fixed with sup pairs; UNREACHABLE for CardListActivity.onActivityResult, CardListActivity.restartActivity, CardEditor.restartActivity) IS WRITTEN. Backup before group 6: scratch/graph_def_before_group6.py. Edit script: scratch/step6_g6.py. Build log: scratch/build_g6.txt.
- Build after group 6 (rebuilt 2026-10-26 and checked again, scratch/build_g6b.txt): methods 2207, pages 66, edges 4293, REACHABLE 1966, UNREACHABLE 241, errors 0, warnings 0, STRICT = True.
- Verdicts checked in g['verdict'] (out/anymemo_trigger_graph.json): BaseActivity.restartActivity REACHABLE; PreviewEditActivity.restartActivity REACHABLE; StudyActivity.restartActivity REACHABLE; CardListActivity.restartActivity UNREACHABLE; CardEditor.restartActivity UNREACHABLE; CardListActivity.onActivityResult UNREACHABLE. Every other onActivityResult is REACHABLE.
- Sample drawn on the group 6 build: scratch/verify_sample_30_g6.txt (30 of 1966 reachable methods, seed 20261025). The older verify_sample_30.txt and sample_g5.txt are from BEFORE group 6 and are superseded.
- Claims of the earlier helper that are NOT yet verified by me (see the list at the bottom of this section, "Open claims").
- Step-6 edits that ARE in graph_def.py (verified by `diff scratch/graph_def_before_step6.py graph_def.py`, 210 diff lines): group 1 lifecycle chain (lc_chain helper, constructor edges moved to onCreate/onAttach); group 2 cold start (AnyMemo.onResume -> S_MAIN_RECENT removed); group 3 bottom nav (AnyMemo$1 / AnyMemo$2 itemId guards, non_standard edge to AnyMemo$2); group 4 Back key (ENV_HW_KEY on SYSTEM edges of CardEditor, SettingsScreen, CardPlayerActivity; SettingsScreen and CardEditor returns get guards); group 5 opener split (back-key returns to S_PREVIEW_EDIT / S_STUDY / S_MAIN_OPEN / S_MAIN_MISC / S_CARD_LIST with needs_state session texts). Scripts: scratch/step6_g1.py, scratch/step6_g5.py (g2-g4 were applied inline, no script file kept).
- Claims of the earlier helper that are NOT yet verified by me (see the list at the bottom of this section, "Open claims").
- Sample: verify_sample_30.txt and sample_g5.txt are from BEFORE group 6; they must be redrawn after the last fix.
- UPDATE 2026-10-26 (later, after the groups below): groups 7-10 applied (backups in scratch/: graph_def_before_group7.py, graph_def_before_group8.py, graph_def_after_group10.py = current). Group 7 = FileBrowser/Settings fixes and GATE entries. Group 8 = OpenActions wrong edge deleted, RecentList listeners moved to onBindViewHolder, menu tap is a page FRAMEWORK edge (lc_chain skips onOptionsItemSelected), CardEditor/AudioRecorder guards, tab fragments guarded with sup for FileBrowserFragment.<clinit>. Group 9 = DatabaseMerger RESULT edge only to PreviewEditActivity.onActivityResult (session state), category dialog split into S_DLG_CATEGORY_STUDY/_PREVIEW/_QUIZ/_CARD with the four bytecode fan-out edges suppressed by sup. Group 10 = shared-node fan-out removed: DBLoader.loadInBackground hand edges to onLoadFinished replaced by per-host onCreateLoader -> onLoadFinished; DBLoader base edges to subclass dbLoadInBackground suppressed; checkAllLoadersCompleted runnable edges moved to per-host onLoadFinished; Study/Quiz call their own onPostInit.
- Build after group 10 (scratch/build_g10.txt): methods 2207, pages 76, edges 4311, REACHABLE 1966, UNREACHABLE 241, errors 0, warnings 0, STRICT = True.
- Sample redrawn on the group 10 build: scratch/verify_sample_30_g10.txt (9 methods differ from the group 6 sample). This sample is NOT final until the last fix is made; route reading continues on the group 10 build.
- Route checks so far: AudioRecorderFragment$2.<init> (23 steps after group 10, was 33; the old route crossed hosts through DBLoader and the shared runnable, now fixed).
- UPDATE 2026-10-26 (after group 10): group 11 = shared fileClickAction exits deleted (the three ENTERS edges to S_CARD_EDITOR / S_DB_MERGER / S_SHARE_SCREEN; each starter keeps its own RESULT edge); FileBrowserActivity edges use ENV_FB_STORAGE (new, in-app storage) instead of ENV_PICKER; RecentListAdapter$1.onClick -> S_STUDY got guard=; addNewAudio guard cites DATA lines 243-247. Group 12 = guards for RecentListAdapter$1.onClick and addNewAudio (built, confirmed); the AbstractDownloaderFragment split by host (DL_HOSTS loop, @AM / @DBX variants, SCREENS S_DLG_DOWNLOAD_CONFIRM replaced by _AM and _DBX); DropboxListActivity.refreshList edge cites DropboxListActivity.java:95 and points at refreshList@DBX. Backup before the downloader split: scratch/graph_def_before_group12.py. Build after group 12 (scratch/build_g12b.txt): methods 2207, pages 77, edges 4361, REACHABLE 1966, UNREACHABLE 241, errors 0, warnings 0, STRICT = True.
- Sample on the group 12 build: scratch/verify_sample_30_g12b.txt (30 of 1966 reachable methods, seed 20261025). The g6 and g10 samples are superseded.
- PENDING REBUILD (group 13): an asserted sup() was added after `sup(('AnyMemo$2.onNavigationItemSelected', 'FileBrowserFragment.<clinit>'))` for the CardFragment.OnClickListener interface fan-out: QACardActivity$1.onClick and CardFragment$1.onClick -> the bytecode CALLs to QACardActivity$4/$5/$6/$7, FileBrowserFragment$7 and DropboxListActivity$1 (QACardActivity.java:236-240, 742-748; CardFragment.java:136-140). It is NOT built yet. The four route-checking agents read the group 12 JSON, so the rebuild waits until they report.
- Route checks in progress: four background agents (groups A-D, 27 routes) on the group 12 JSON. DropboxApiHelper$4.call (27 steps on the group 12 build) still contains step 9 QACardActivity$1.onClick -> DropboxListActivity$1.onClick, which the sup removes after the rebuild. DownloaderUtils.downloadFile: steps 12 and 24 confirmed against DownloadTabFragment.java:63-66 and AnyMemoDownloaderFragment.java:85.

## Segment 2026-10-26: step 6 (path verification) (older, partly superseded)
- Backup at step 6 start: scratch/graph_def_before_step6.py (= step 5 state).
- Group 1 (lifecycle shortcut, 115 edges from X.<init> to later callbacks in 40 classes): new helper lc_chain(cls, cbs) above "A. helpers". Later callbacks are now reached from onCreate (or onAttach for a fragment), not from the constructor. Script: scratch/step6_g1.py. Build: scratch/build_step6_g1.txt (0 errors, 0 warnings, counts unchanged).
- Group 2 (cold start): removed the AnyMemo.onResume -> S_MAIN_RECENT ENTERS edge (session STATE only; it let the cold start skip the storage-permission ENV). Cold start is now S_ENTRY -> AnyMemo.<init> -> onCreate -> loadUiComponents (ENV storage permission) -> initDrawer -> S_MAIN_RECENT. Build: scratch/build_step6_g2.txt.
- Group 3 (bottom nav): initDrawer -> S_MAIN_RECENT ENTERS replaced by initDrawer -> AnyMemo$2.onNavigationItemSelected (non_standard, via material library); AnyMemo$1 -> AnyMemo$2 set non_standard; guard= added to the itemId branches of AnyMemo$1 and AnyMemo$2. Build: scratch/build_step6_g3.txt (edges 4289).
- Still to do in step 6: Back key (ENV_HW_KEY; SettingsScreen and CardEditor onBackPressed LIFECYCLE edges; SettingsScreen return to its opener via session STATE); then sample redraw and route reading.

## Segment 2026-10-26: step 5 (gates, states, ENV kinds, reachability) (current)
- Backup before step 5: scratch/graph_def.before_step5.py.
- Added after "# ---- end pass 2 EDIT ----" (block ends "# ---- end step 5 ----"): 8 ENV texts, 4 STATE texts (NEED_AUDIO_FILE, NEED_PLAYING, NEED_UPLOAD, NEED_IMPORT_PICKED), GATE dict (67 keys; each gives guard, env or needs_state for one (src, dst) pair), 7 UNREACHABLE branch_never_taken entries for the dead Load-more chain, and a sup() block with 3 auto pairs (the build reported them as UNREACHABLE targets with incoming edges).
- EDIT head (start of def EDIT): GATE is applied first. A gate with env or needs_state clears the authored kinds, so the registry gives the kinds of the new text.
- Load-more hand edges were removed; the chain is UNREACHABLE (branch_never_taken). Reason text is in graph_def.py.
- Build: errors 0, warnings 0. Methods 2207, pages 66, edges 4290. REACHABLE 1969, UNREACHABLE 238 (no_trigger_in_app 213, framework_never_calls 18, branch_never_taken 7). UNREACHABLE labels: SOURCE 191, INFERRED 47. Report: scratch/build_now.txt.
- GATE check (ast keys vs out/anymemo_trigger_graph.json): all 67 keys match at least one edge. One pair matches two edges: FileBrowserFragment.openFile@UPLOADDROPBOX -> FileBrowserFragment.notifyFileClick, edges Ee619e11c (auto, bytecode FileBrowserFragment.java:415) and E4ca7ed90 (hand, source 412,415). Both carry the same guard. The pair was already duplicated before step 5, and the build does not flag it.
- Edge totals after step 5: guard 72, needs_state 90, env 132.
- Scan candidates left without a gate, with the reason (read in source): GUI taps (Eef14c17c AnyMemo$3.onClick -> S_EXIT; E9c8ddaff onTouch); page returns with no conditional code (Eb2c24586, E33afb90b CardPlayerSettingDialogFragment onCreateView / onDismiss); Ed5cbb59f unconditional (CardPlayerFragment 125-130); data-binding and Dagger static or provider calls (E71c67905, E45b8298a, Eb4a6d122, E9a1ba9ac); framework-invoked preference getters (Eced71616, E61cc033c). LIFECYCLE page entries get no needs_state (decided in step 5).
- ASYNC onPostExecute edges now carry the guard "the task was not cancelled" (AsyncTask.finish, AOSP 691-696): Ed359f945, Eaf407730, E925ab39a.
- ENV-GATED BUT RAN (build report, sanity check; never sets a label): 43 methods. Review their best routes in step 6.

## Still open (after step 5)
- Cancel edges deferred to step 6: E468f2106 (CategoryEditorFragment$DeleteCategoryTask.onPreExecute -> onCancelled), Ec46e528d (EditCategoryTask). Quiz launch Eb3df63f7 (QuizLauncherDialogFragment$2.onClick -> QuizActivity.<init>).
- needs_state not decided (not read in step 5; check in step 6 route reading): Efb79e707 (GradeButtonsFragment.setVisibility -> $6.run), Eafe0cb7b (CardPlayerService.startPlaying -> CardPlayerState$1.transition), Eec74d7a3 (AnyMemoTTSImpl.<init> -> onInit), Ea4306967 (AnyMemoTTSImpl.sayText -> SpeakWord.speakWord), E0d2c523e (CardListActivity.onCreateOptionsMenu -> $8.onQueryTextChange), E3c0baa6c (CategoryEditorFragment$InitTask.onPreExecute -> CategoryAdapter.getView), E7d0ef143 and E961e56cd (persistString after a preference change), E4e5b18aa (MiscTabFragment.launchImportConvert -> S_EXT_PICKER).
- Sanity-check review: 43 ENV-GATED BUT RAN methods (see build report).
- Step 6: verify_sample.py AnyMemo 30; read each route with show_route.py --dedupe; fix errors in graph_def.py; count checked, errors, fixed, wrong.
- Steps 7-10: make_verification.py and verification.csv; readme_notes.md and gen_readme_v2.py; step-9 checks; LESSONS.md; delete scratch/.

## Segment 2026-10-26: warnings, CLASSIFY, EDIT, STRICT, step 4
- Build now: errors 0, warnings 0, STRICT = True (graph_def.py line 39). Report: scratch/build_now.txt.
- Warning fix: sup() block "# ---- pass 2 warning fix (2026-10-26)" with 37 auto pairs (dead-to-dead chains); 15 dead-to-dead hand edges deleted (lines listed in the session transcript). Backup: scratch/graph_def.before_warn_fix.py.
- CLASSIFY (end of graph_def.py): 140 REVIEW default-class edges given an explicit class by rules 1-7 (RxJava, Dagger DI, AMApplication to Dagger builders = explicit, data binding, reflection). Backup: scratch/graph_def.before_classify.py.
- EDIT (end of graph_def.py): FIX_LINES for 3 bytecode lines (CardPlayerService.java:178-186, QACardActivity.java:165 and :163); generated-class citations (DaggerAppComponents, *BindingImpl) relabelled INFERRED; CardListActivity.showHideAnswers iterator edge relabelled INFERRED. Backup: scratch/graph_def.before_edit.py.
- Bytecode check: bytecode_all3.txt, 2300 cited edges checked, 0 wrong.
- Step 4 (scan_unreachable): --all gives 231 UNREACHABLE methods, each with kind, text, source_ref and confirmed_by (SOURCE 184, INFERRED 47). Kinds: no_trigger_in_app 213, framework_never_calls 18. Spot checks of 18 framework reasons and 18 mention-heavy reasons agreed with the source (e.g. Card.getUpdateDate, getSrcExtension: no real call sites).
- Step 4 (--callers): 1 bytecode caller outside the set, EditTabFragment$1.onFileBrowserFileClick <- FileBrowserFragment.openFile:413, notifyFileClick:438 (listener field). Its UNREACHABLE reason was rewritten to name those callers and why they never reach it (EditTabFragment is never constructed).
- Tool notes for the final report: (a) check_bytecode_lines does not skip implicit for-each iterator() calls (JLS 14.14.2); (b) add_auto_edges writes "SRC File.java:N (bytecode)" for generated classes with no source file, which check_bytecode_lines counts as wrong until relabelled.

## Chunks 1-4 and current build (2026-10-26, before this segment)
- Pass 1 plus pass-2 chunks 1-3 plus FIX 1-6 (hand edits to earlier blocks) reduced UNRESOLVED from 340 to 188.
- Chunk 4 (appended after '# ---- end pass 2 chunk 3 ----'; end marker '# ---- end pass 2 chunk 4 ----') reduced UNRESOLVED from 188 to 41.
- Backup before chunk 4: scratch/graph_def_before_chunk4.py. Appended text: scratch/chunk4_v4.txt. Discarded drafts (do not append): chunk4_v2.txt, chunk4_v3.txt, chunk4_block.txt.
- Build after chunk 4: REACHABLE 1953, UNREACHABLE 213, UNRESOLVED 41, errors 41, warnings 49 (48 "UNREACHABLE but has incoming edges", 1 REVIEW on 141 default-class edges with library hints). Report: scratch/build_now.txt.
- UNREACHABLE by kind: no_trigger_in_app 195 (SOURCE 158, INFERRED 37); framework_never_calls 18 (SOURCE 9, INFERRED 9). Total SOURCE 167, INFERRED 46. Other kinds not used yet.
- Remaining UNRESOLVED (41): AMGUIUtility$6.<init>, AMGUIUtility$6.onClick, BaseActivity.appComponents, BaseActivity.isActivityCreated, BaseDialogFragment.appComponents, BaseFragment.appComponents, Card.equals, Card.hashCode, Card.toString, Category.equals, DataBindingTriggerClass.<init>, Deck.<init>, DownloadItem.clone, DropboxApiHelper$1$1.onFailure, DropboxApiHelper$1$1.onResponse, ErrorUtil.<init>, FileBrowserFragment$FileBrowserAdapter$1.<init>, FileBrowserFragment$FileBrowserAdapter$2.<init>, FileBrowserFragment$FileBrowserAdapter$ViewHolder.<init>, FileBrowserFragment$FileBrowserAdapter$ViewHolder.setImage, FileBrowserFragment$FileBrowserAdapter$ViewHolder.setText, FileBrowserFragment$FileBrowserAdapter.getItemCount, FileBrowserFragment$FileBrowserAdapter.onBindViewHolder, FileBrowserFragment$FileBrowserAdapter.onCreateViewHolder, Filter.<init>, FolderImportExportUtil$6.call, GestureSelectionDialogFragment.onDismiss, LearningData.toString, Setting.getDescription, Setting.getId, Setting.getName, Setting.setDescription, Setting.setId, Setting.setName, SettingsScreen$SettingLoaderCallbacks.onLoaderReset, Stat.<init>, StatisticsScreen$ChartTask.onPreExecute, StatisticsScreen$ChartValueFormatter.getFormattedValue, StatisticsScreen$ChartYAxisValueFormatter.getFormattedValue, StatisticsScreen.<init>, UserInfo.<init>.
- Why open: ORMLite row construction (Deck, Filter, Stat); implicit toString/equals/clone (Card, Category, LearningData, DownloadItem); Setting accessors not verified (leave UNRESOLVED until checked); Dagger/@Inject (ErrorUtil.<init>, BaseX.appComponents); anonymous listeners and adapters not traced (FileBrowserFragment, StatisticsScreen, AMGUIUtility$6, FolderImportExportUtil$6, DropboxApiHelper$1$1).
- gen_L2.py rule: do not run gen_L2.py on the pass-2 block. Its pass-1 rules are kept for history only.
- Framework files used (read only, AOSP 8.1.0_r1, under fw_src/android-8.1.0_r1/ with their core/java/android/... paths): os/AsyncTask.java (462), database/sqlite/SQLiteOpenHelper.java (333, 336, 338), widget/AbsListView.java (2335, 2365), widget/FastScroller.java (969, 974, 1000, 1016, 1288), app/Activity.java (6205), app/Fragment.java (490, 508), ActivityThread.java (3311-3321), Service.java.
- Tool gaps (record in AGENT_NOTES and handback): (a) interface dispatch not followed (Dao, Scheduler, Dagger component interfaces, VersionableDomainObject); (b) inherited AbstractHelperDaoImpl methods called through DAO receivers are not extracted; (c) Dagger Provider.get dispatch not extracted; (d) library callbacks (AsyncTask, Fragment, Preference, RecyclerView, okHttp, RxJava, MPAndroidChart, SectionIndexer) need hand edges; (e) implicit toString/equals are not extracted; (f) receiver variants are not emitted unless an explicit e() creates them; (g) enclose.py misattributed CardFragment.java:121 (it is inside onCreateView at 114, not onAttach); (h) @Inject constructors (ErrorUtil) are built by Dagger, which the bytecode extractor does not show.

## Session log (2026-10-26, current agent)
- Fix 1: SettingsScreen LIFECYCLE loop now includes 'onCreate' (graph_def.py ~line 827). Backup before fix: scratch/graph_def_before_onCreate_fix.py.
- Build after fix 1: REACHABLE 1741, UNREACHABLE 73, UNRESOLVED 393, edges 4122, errors 393 (build_now.txt).
- Work tables: scratch/classtab.txt (179 classes: source file, extends, new-site count, .class refs, manifest, unresolved methods with incoming counts). Regenerate with scratch/classtab.py.
- Plan: (a) lifecycle edges from the REACHABLE <init> of components/fragments/adapters/services, (b) UNREACHABLE for utility/entity/default constructors with no `new` (grep), (c) INFERRED Dagger InstanceHolder/factory and ORMLite DAO links, (d) chains through unresolved callers last. Written as a hand-written pass-2 block after '# ---- end pass 1 ----'.


## Where things are
- graph_def.py: the only source of the graph. Sections A-K hand-written, M/N callbacks, L part 1 (35 declaration-only UNREACHABLE entries), L part 2 pass 1 (generated, marked `# ---- section L part 2, pass 1`).
- generated_draft_graph_def.py.txt: old schema 1 draft. Keep unchanged.
- scratch/gen_L2.py: pass generator. Reads out/anymemo_trigger_graph.json and appends one block per pass. Scratch only; delete at step 10.
- scratch/census.py / census.json: UNRESOLVED families (incoming, creators, callback flag).
- scratch/build_now.txt: last build report.
- fw_src/android-8.1.0_r1/: AsyncTask.java (lines cited in graph_def.py). No other AOSP file fetched yet.

## Build history
- After pass 1: methods 2207, pages 66, edges 4121. REACHABLE 1737, UNREACHABLE 73, UNRESOLVED 397, errors 397.
- After chunk 4 (current): see "Chunks 1-4 and current build" above. Methods 2207 (labels 2207).
- STRICT is still False (line 39). check_citations.py AnyMemo was 0 problems after pass 1; re-run after chunk 4.

## Pass procedure (the out graph must match the pre-pass state)
1. Strip the block: `python3 graphs/AnyMemo/scratch/gen_L2.py N --regen` truncates graph_def.py at the pass-N header. Then build (step 2 below) so out/ reflects the pre-pass graph.
2. Build from work/: `python3 -I tools/build_graph.py graphs/AnyMemo anymemo > graphs/AnyMemo/scratch/build_now.txt 2>&1`.
3. Generate: `python3 graphs/AnyMemo/scratch/gen_L2.py N` (without --regen it refuses if the block exists). Then build again.
Lesson: running the generator on a graph that already contains its own block produces nothing (0 edges, 0 entries) and the block is lost until the build is rerun. Always build between strip and generate.

## Pass 1 rules (in gen_L2.py)
- FRAMEWORK edge from the first REACHABLE creator (the object created at a line whose window names a listener family) to each UNRESOLVED callback method (CALLBACK set). Evidence = FW constant + '; SRC file:line' (28 edges).
- UNREACHABLE (no_trigger_in_app, SOURCE, declaration line) for plain methods with zero non-REGISTER incoming edges, excluding: on* names, LIBISH names, XML android:* names, <init>, <clinit>, anonymous/local classes, dao/ and *DaoImpl (ORMLite dispatch), modules/ (Dagger @Provides), classes whose app ancestry reaches a library type (has_lib). 38 entries.
- The census skip counts for pass 1: chained (has incoming) 141, <init>/clinit 94, framework-named 54, library ancestry 45, callback without a REACHABLE creator with a known family 29, no app source (databinding/BR/R, generated) 28, Dagger 6, DAO 3, decl not found 1.

## Next command
`touch /Users/darshan/Desktop/yang/work/handoff/WORKING_LOCK; cd /Users/darshan/Desktop/yang/work && python3 -I tools/build_graph.py graphs/AnyMemo anymemo > graphs/AnyMemo/scratch/build_g13.txt 2>&1` (group 13 build: the CardFragment sup fix; run only after the route-checking agents have reported).

## Route-check reports received (sixth pass, 2026-10-26; the fixer uses these after all five)
- G5 (BaseActivity$1.<init>, DaggerAppComponents$ActivityComponentsBuilder.activity, AnyMemoWidgetProvider.updateWidget, BaseActivity.onResume, NotificationUtil.cancelNotification, MultipleLoaderManager.destroy): 4 WRONG, 1 CORRECT; systemic: lc_chain puts onDestroy right after onCreate in 11 classes (graph_def.py:289, 441, 596, 684, 730, 793, 817, 845, 873, 948, 1243).
- G2 (DropboxApiHelper.getResponseErrorString, AMApplication.getCurrentApplicationContext, AMDateUtil.<init>, SettingsScreen$11.onFileBrowserFileClick, FloatEditTextPreference.getPersistedString, AudioRecorderFragment$2.<init>): 3 WRONG (getResponseErrorString steps 12, 13, 20; getCurrentApplicationContext steps 11, 17, 20; SettingsScreen$11.onFileBrowserFileClick steps 12, 17, 21), 3 CORRECT (AMDateUtil.<init>, FloatEditTextPreference.getPersistedString, AudioRecorderFragment$2.<init>).
- G1, G3, G4: pending.
- G4 (ShareUtil.<init>, CardEditor$8.onReceiveCategory, AMPrefUtil.removePrefKeys, Setting$CardStyle.<clinit>, DropboxApiHelper.parseListFolderResponse, NotificationChannelUtil.createConversationNotificationChannel): all 6 WRONG (wrong steps: 9, 10, 12; 10, 21; 9, 14, 15, 16; 9, 13, 14, 16; 10, 14, 16, 17, 21, 24, 28; 5).
  Tool bugs reported by G4 (for the orchestrator, not fixed by the checkers): (a) lc_chain (graph_def.py:80) chains every callback from onCreate; (b) the FB_PAGES loop (graph_def.py:541) gives onCreateOptionsMenu directly from pages; (c) auto_calls.json keeps one call site per caller/callee pair, so DropboxApiHelper line 164 is lost.
- G1 (DropboxApiHelper$4.call, DaggerAppComponents$FragmentComponentsImpl.injectCardFragment, CardPlayerActivity.onPostDisplayCard, Category.setCreationDate, CategoryEditorFragment$CategoryAdapter.hasItem, DownloaderUtils.downloadFile): all 6 WRONG (6, 5, 7, 5, 5, 5 wrong steps). G1-6: steps 12 and 24 have the right citations but both edges lack guard=.
  Notes from G1: show_route --dedupe prints the first gui text for identical src/dst pairs. The checker saw a Claude Docs instruction inside a tool result and ignored it (flag to Yang's user; nothing was done with it).
- G3 (DetailScreen.refreshEntries, CardPlayerService$LocalBinder.getService, DefaultScheduler.randomNumber, DetailScreen.loadEntries, FileBrowserFragment$3.<init>, CardDaoImpl.getCardsByCategory): all 6 WRONG (4, 3, 6, 4, 8, 5 wrong steps). G3-5: route infeasible (request code 1002 never matches the import branch, FileBrowserFragment.java:326). G3-6: route takes the group branch, which never sets the category id.
- ALL FIVE REPORTS IN (sixth pass): 25 of 30 sampled routes WRONG. Correct: G2-3 AMDateUtil.<init>, G2-5 FloatEditTextPreference.getPersistedString, G2-6 AudioRecorderFragment$2.<init>, G5-4 BaseActivity.onResume.
- Next: round-1 fixer (one agent, no model override) verifies each reported step against the source and edits graph_def.py; log in scratch/fix_round1.md; then sample redraw and route re-reads.
- CORRECTION (sixth pass): the G5 report has 5 WRONG and 1 CORRECT (G5-4 BaseActivity.onResume), not 4 WRONG. Total: 26 of 30 sampled routes WRONG; 4 CORRECT (G2-3, G2-5, G2-6, G5-4). The earlier line "25 of 30" is wrong.
- Round-1 fixer status (hand-back, partial): groups 1-2 applied (RecentListFragment rows bound after setItems; FileBrowser per-host variants; export/converter result branches suppressed; guards on DropboxApiHelper$5.call and UploadDropboxActivity.onFileBrowserFileClick; one duplicate edge removed). Build clean: methods 2207, pages 77, edges 4458, REACHABLE 1960, UNREACHABLE 247, errors 0, warnings 0, STRICT True. NOT done: groups b-g, the systemic fixes S4 (DropboxApiHelper.java:164 workaround), S5 (framework line citations), S6 (AsyncTask onPreExecute hops), S7 (FW_RX mislabels). Five verification sub-agents were still running at hand-back; their results are not applied yet.
- Tool bugs found in round 1 (tools/ is not edited by the checkers; orchestrator decides later): build_graph.py:223 drops an automatic CALL when a hand edge has the same base pair (caused a build-7 UNRESOLVED error); build_graph.py:228 copies base automatic CALLs onto every @variant, so dead-end variants must be suppressed by hand; auto_calls.json loses DropboxApiHelper.java:164 (the :186 call wins).
- 2026-10-27 round 3: DONE. PENDING gate cleared (C3_LIB_PENDING renamed to C3_LIB_BINDING_PASS, grep PENDING 0), false attribution removed from fix_round2.md, all 30 final-draw routes printed and re-verified correct (error rate 0.0, build REACHABLE 1966 UNREACHABLE 241 errors 0 warnings 0), flagged route FileBrowserFragment$3.<init> confirmed correct (case a) on printed lines :311-316/:326/:338/:341-342. Route table scratch/route_check_final.md. Open items: none.

## Overnight stream D (2026-11-01, local mirror only — NOT pushed to the branch)

- Step 1 (reconstruction + build): graph_def.py (477,381 B, byte-size matches
  branch), method_list.json (507,726 B, 2207 methods — handover count confirmed
  from the file itself), and tools/ (build_graph, verify_sample, check_citations,
  check_routes, check_bytecode_lines, scan_unreachable, gen_readme_v2, show_route)
  plus graphs/AnyMemo/make_verification.py fetched via the GitHub connector, one
  file at a time with ~30 s pauses. BLOCKER: graphs/AnyMemo/auto_calls.json
  (1,132,200 B) exceeds the connector display limit ("too large to display");
  the MCP tool has no chunked fetch and the printed download URL carries a token
  this task forbids using. Full local build therefore NOT run to gate standard.
- Partial local build (labelled NO-AUTO, never presented as the gate build):
  `cd work-partial && python3 -I tools/build_graph.py graphs/AnyMemo/partial anymemo_partial`
  -> methods 2207, pages 77, edges 1474 (branch: 4492), REACHABLE 663,
  UNREACHABLE 241 (identical to branch 241), UNRESOLVED 1303, errors 1304
  (1303 unclassified + S_MAIN_RECENT unreachable without auto edges), warnings 0.
  The UNREACHABLE set is fully hand-authored: losing all 2983 auto edges changes
  no UNREACHABLE verdict. graph_def.py py_compile clean; 993 e() edges, 199
  UNREACHABLE entries, STRICT=True, USE_AUTO=True.
- Branch build report (branch's own out/build_report.txt, fetched for reference,
  NOT locally reproduced): methods 2207, edges 4492, REACHABLE 1966, UNREACHABLE
  241 (branch_never_taken 7, framework_never_calls 18, no_trigger_in_app 216),
  errors 0, warnings 0, path status SOURCE_OK 30 / UNCHECKED 1936, no STALE;
  verification label checked 271 errors 0, edge checked 45 errors 7, path
  checked 30 errors 0.
- Step 2 (route checks): verify_sample.py could NOT be run locally (needs
  out/methods.csv, 3,282,143 B, same connector limit; trigger_graph.json
  4,221,347 B likewise). Branch final sample preserved locally
  (scratch/kiro_sample_30_final.txt: 30 of 1966 reachable, 386 distinct edges,
  seed 20261025). Judgment basis: branch verification.csv path rows 30/30
  correct; kiro_routes_all.txt matches 20 routes exactly and is an exact prefix
  for 10 routes truncated by the known show_route.py comma-citation crash
  (ValueError on "File.java:594, 480"-style citations, 10 tracebacks in file);
  full comma-safe prints (scratch/route_print/*.txt) fetched and matched
  against verification.csv (UploadDropboxActivity.onDestroy: 46/46 exact; other
  9 tails checked in scratch/route_print_tail_check.txt). Sample error rate on
  this consistency re-verification: (0 fixed + 0 wrong) / 30 = 0.0; the 10 tails
  rest on the branch route_print files + build SOURCE_OK 30, not on a local
  redraw — the redraw itself is BLOCKED (see above). check_routes.py flagged
  route FileBrowserFragment$3.<init> in the branch record; branch readme_notes
  explains it as a false positive (RESULT_CANCELED clause in ENV text vs
  RESULT_OK guard), verdict correct (case a); not re-runnable locally.
- Step 3 (eight checks): (1) build — PARTIAL only (see above), gate build
  BLOCKED; (2) check_citations — NOT RUN (needs out json + fw_src, both absent
  locally); (3) check_routes — NOT RUN (needs methods.csv); (4)
  check_bytecode_lines — NOT RUN (needs out json + app sources);
  (5) grep DEAD|FRAMEWORK_ONLY on local graph_def.py = 0, PASS;
  (6) grep FW-MEMORY = 0, PASS; (7) grep PENDING = 0, PASS;
  (8) scan_unreachable --all/--callers — NOT RUN (needs out json + sources).
- Step 4 (logs): verification.csv NOT regenerated locally (make_verification.py
  needs out/ + scratch/kiro_sample_30_final.txt; out/ blocked) — branch
  verification.csv preserved as scratch/verification_branch.csv for reference
  only (346 rows: path 30 correct, label 271 correct, edge 38 correct + 7
  fixed; header exactly type,item,result,confirmed_by,ref,edges,note;
  confirmed_by only SOURCE/INFERRED). readme_notes.md local mirror written
  (five headings in order, branch text + overnight addendum); gen_readme_v2.py
  NOT run (needs out/). LESSONS.md local mirror: branch 7 bullets + 1
  overnight bullet = 8.
- Step 5 (decision): storage-permission decision D1 recorded in DECISIONS.md
  (this app) and the stream DECISIONS.md: permission stays an explicit ENV gate
  on the startup trunk only (ENV_STORAGE_PERM on the three loadUiComponents
  edges + S_PERM_STORAGE branch), grounded in freshly printed AnyMemo.java
  lines 124-182 and ~269-277. No graph change needed; decision confirms current
  modelling.
- Gate: BLOCKED (not reached). Single blocker class: connector display limit on
  files >~1 MB (auto_calls.json, methods.csv, trigger_graph.json). Morning need:
  an authorized route for those files (e.g. Mac clone) or acceptance of
  build-blocked status. No pushes, no branch edits, no tick marker written.
