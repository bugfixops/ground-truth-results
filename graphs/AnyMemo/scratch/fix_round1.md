# Round 1 fix log: AnyMemo schema 2 trigger graph

Status: IN PROGRESS (this file is updated as each group is done).
Editor: round-1 fixer. Only graph_def.py was edited. Backup: scratch/graph_def_before_round1.py.
Read-only inputs: scratch/route_check/*.md, source under final_java_only/, fw_src/ (AOSP 8.1.0_r1).

## Counts

| build | file | methods | pages | edges | REACHABLE | UNREACHABLE | errors | warnings |
|---|---|---|---|---|---|---|---|---|
| before | scratch/build_round1_0.txt | 2207 | 77 | 4356 | 1966 | 241 | 0 | 0 |
| step 1 (placeholders added) | build_round1_1.txt | | | | | | 17 | 0 |
| step 2 (hand edges off, sup added) | build_round1_2.txt | | | | | | 0 | 4 |
| step 3 (lc chain + AnyMemo exits) | build_round1_3.txt | 2207 | 77 | 4344 | 1949 | 258 | 0 | 0 |
| step 4 (real exits added; 3 CardPlayer edges wrong) | build_round1_4.txt | 2207 | 77 | 4356 | 1957 | 247 | 3 | 0 |
| step 5 | build_round1_5.txt | 2207 | 77 | 4359 | 1960 | 247 | 0 | 0 |
| step 6 (group 1, S3 and S3b) | build_round1_6.txt | 2207 | 77 | 4358 | 1960 | 247 | 0 | 0 |
| step 7 (group 2 first pass; comparator UNRESOLVED) | build_round1_7.txt | | | | | | 1 | 0 |
| step 8 (Dagger text in Ec37fd169 matched NONSTD_HINT) | build_round1_8.txt | | | | | | 0 | 1 |
| step 9 (base CALL edges restored by hand; build_graph.py:223 tools bug) | build_round1_9.txt | 2207 | 77 | 4461 | 1960 | 247 | 0 | 0 |
| step 10 (export and converter super calls suppressed; G3-5 s18-19) | build_round1_10.txt (overwritten by the last run of step 10) | 2207 | 77 | 4459 | 1960 | 247 | 0 | 0 |
| CURRENT (step 11: G2-1 s13 duplicate removed; G2-1 s20 GATE) | build_round1_11.txt | 2207 | 77 | 4459 | 1960 | 247 | 0 | 0 |

Build command (from work/): `python3 -I tools/build_graph.py graphs/AnyMemo anymemo > graphs/AnyMemo/scratch/build_round1_N.txt 2>&1` (the prefix argument `anymemo` is required, per AGENT_NOTES.md:95).

STRICT = True in build_graph.py. The build verdict counts: branch_never_taken 7, framework_never_calls 18, no_trigger_in_app 222.

## Checker verdicts (counted from the 30 files, not from the orchestrator note)

- route_check files with `Verdict: WRONG`: 26. With `Verdict: CORRECT`: 4 (G2_3, G2_5, G2_6, G5_4).
- The orchestrator note said 25 WRONG. This is a discrepancy. This log uses the files: 26 WRONG.

## Systemic fixes

- S1 (DONE): lifecycle chain. lc_chain (graph_def.py ~63-90) now follows AOSP order: onAttach then onCreate from <init>; ranked callbacks reached from the nearest earlier ranked callback. onDestroy, onDetach and onConfigurationChanged have no automatic trigger (LC_NO_TRIGGER). FW-SRC: Activity.java:6989-6999 (performCreate), 7203-7208 (performDestroy: dispatchDestroy 7207, onDestroy 7208), 3001-3010 (onBackPressed -> finishAfterTransition), 5580-5584 (finish when no transition), 5526-5528 (finish delegates); Fragment.java:940-946 (setHasOptionsMenu), 2626-2629 (performCreateOptionsMenu).
- S1a (DONE): permission env split. ENV_PERM_ANSWER_STORAGE (Allow or Deny) for the gate; ENV_PERM_DENY_STORAGE for the Deny path (AnyMemo.java:169-178, finish() at 178).
- S1b (DONE): AnyMemo exits from main tabs. SYSTEM edge 'Press Back on a main tab' (no onBackPressed override in AnyMemo or BaseActivity; FW-SRC 3001-3010, 5580-5584, 7203-7208; SRC AnyMemo.java:399-411). LIFECYCLE from AnyMemo$3.onClick (AnyMemo.java:273-277) and onRequestPermissionsResult denied path (AnyMemo.java:169-178).
- S1c (DONE): real exits for other destroys (graph_def.py ~1586-1612). Each cites a finish() site checked against source (see the table below). Anonymous-class names checked against the compiled LineNumberTable (javap is not installed; read with a small parser under build/intermediates/javac/.../classes):
  - CardEditor$1 = Neutral (Cancel) listener (table 143-146); CardEditor$2 = Yes listener.
  - SettingsScreen$2 = Neutral listener (208-211); SettingsScreen$3 = Yes listener.
  - StudyActivity$1 = OnCancelListener (418-419); StudyActivity$2 = positive button.
  - DetailScreen$SaveCardTask.onPostExecute table 226-235.
- S1d (DONE, corrected in step 5): CardPlayer chain. CardPlayerActivity.onBackPressed (CardPlayerActivity.java:179-185, finish at 184) -> CardPlayerActivity.onDestroy (89-92, unbindCardPlayerService at 91). unbindCardPlayerService -> CardPlayerService.onUnbind is ENABLED (ActivityThread.java:3388-3394 calls s.onUnbind, checked). CardPlayerService.onUnbind -> onDestroy ENABLED (onUnbind returns false at CardPlayerService.java:130; the stop itself is INFERRED, FW_TEARDOWN).
  - The old hand edge CardPlayerActivity.onDestroy -> CardPlayerActivity$3.onServiceDisconnected was WRONG (round 1 claimed it fired on unbind). LoadedApk.java:1644-1646 and 1668 show onServiceDisconnected is called only when an old connection is replaced (doConnected) or the binder dies (doDeath). unbindService does not call it. Replaced by an env edge from S_CARD_PLAYER with ENV_CARD_SVC_DIES (system event: process death).

## Placeholders still pending (honest, not final verdicts)

These are UNREACHABLE with a PENDING text and must get a real exit in a later round.
- CardListActivity.onDestroy (finish sites not modelled)
- PreviewEditActivity.onDestroy (finish sites not modelled; build reports CONTRADICTION: it ran in a tool run)
- CategoryEditorFragment.onDestroy (host or dialog dismiss not modelled; CONTRADICTION, ran in a tool run)
- QuizLauncherDialogFragment.onDestroy (dismiss or host destroy not modelled; CONTRADICTION, ran in a tool run)
- CardEditor.onConfigurationChanged (rotation; system event not modelled)
- SettingsScreen.onConfigurationChanged (rotation; system event not modelled)

## Tools bug (not fixed here; tools/ is read-only for this round)

- DropboxApiHelper.java:164 (first page call of parseListFolderResponse) is lost: auto_calls.json keeps one call site per caller/callee pair, and :186 (continuation inside while(hasMore) at :167) wins. Workaround: hand edges that suppress the auto edge (build_graph.py:223-224). Planned under S4.

## Per-finding log

Verdict rules used in this log:
- CONFIRMED: the reported edge is wrong, and the fix the report suggests is applied.
- ALTERNATIVE: the reported edge is wrong and is fixed, but what is kept or removed differs from the report's suggested fix. The difference is stated.
- REJECTED: the reported step is right by source, so nothing is changed.

### Group 1: RecentListFragment rows (S3 and S3b)

Source (read in this round): RecentListFragment.java:179-182 (onCreateView sets an empty adapter), 268-272 (loader guard at 269, setItems at 270), 298-304 (detail guard at 301, setItems at 302), 416-422 (row tap: getSelectedItemCount() == 0 at 416, startActivity at 417-422, toggle at 423-424), 464-468 (setItems: clear, addAll, notifyDataSetChanged).

Changes in graph_def.py:
- S3: the onCreateView loop (line 2376-2386) keeps getItemCount, DividerItemDecoration.onDraw and getItemOffsets. It no longer has onCreateViewHolder or onBindViewHolder.
- S3: new FRAMEWORK edges setItems -> onCreateViewHolder and setItems -> onBindViewHolder (lines 2388-2398, needs_state NEED_RECENT).
- S3: the two loader callbacks already have bytecode CALL edges to setItems (auto_calls.json lines 270 and 302). Their guards are added in the GATE dict (line 2888-2890), so the same edges are guarded. No new hand edge was needed.
- S3b: the ENTERS RecentListAdapter$1.onClick -> S_STUDY was deleted (old lines 484-485; comment at line 484). The INTENT at line 618 gets guard 'getSelectedItemCount() == 0 (RecentListFragment.java:416)'.

| Report | Step | Verdict | Source evidence | What changed in graph_def.py and why |
|---|---|---|---|---|
| G1-2 injectCardFragment | 10 | ALTERNATIVE | RecentListFragment.java:179-182, 268-272, 464-468 | Edge onCreateView -> onBindViewHolder removed (the error is CONFIRMED). The report keeps onCreateViewHolder on onCreateView. Removed here too: with no items, the recycler view creates no holders at layout (INFERRED androidx). |
| G1-2 injectCardFragment | 12 | CONFIRMED | RecentListFragment.java:416 (guard), 417-422 (startActivity) | The INTENT at line 618 had no guard=. Guard added. |
| G1-3 onPostDisplayCard | 10 | ALTERNATIVE | as above | Same as G1-2 step 10. The report says "fix as in G1-2", so the onCreateViewHolder difference applies. |
| G1-5 CategoryAdapter.hasItem | 10 | ALTERNATIVE | as above | The report removes only onBindViewHolder. Also removed onCreateViewHolder (same reason as G1-2). |
| G1-5 CategoryAdapter.hasItem | 12 | CONFIRMED | RecentListFragment.java:416-422 | ENTERS RecentListAdapter$1.onClick -> S_STUDY deleted. The report says its guard was correct. The error is the shortcut: the Study page is shown by StudyActivity.onPostInit (ui/StudyActivity.java:296-300), after onCreate. |
| G3-1 DetailScreen.refreshEntries | 10 | ALTERNATIVE | as above | The report says remove getItemCount too. Kept it: RecyclerView asks the adapter for its item count on every layout pass, even when empty (INFERRED androidx). onCreateViewHolder and onBindViewHolder removed. |
| G3-1 DetailScreen.refreshEntries | 12 | CONFIRMED | as G1-5 step 12 | ENTERS deleted; INTENT at line 618 guarded (the report's suggested fix). |
| G3-2 CardPlayerService.LocalBinder.getService | 10 | ALTERNATIVE | as above | Same as G3-1 step 10. The report keeps only onDraw and getItemOffsets on onCreateView; getItemCount also kept here. |
| G3-3 DefaultScheduler.randomNumber | 10 | ALTERNATIVE | as above | "Fix as in G3-2": same as G3-2 step 10. |
| G3-4 DetailScreen.loadEntries | 10 | ALTERNATIVE | as above | "Fix as in G3-2": same as G3-2 step 10. |
| G3-6 CardDaoImpl.getCardsByCategory | 10 | ALTERNATIVE | as above | "Fix as in G3-1": same as G3-1 step 10. |
| G4-2 CardEditor.onReceiveCategory | 10 | CONFIRMED | as above | The report says take onBindViewHolder and onCreateViewHolder off onCreateView, and add loader -> setItems and setItems -> row callbacks. This matches the change. |

Group 1 totals (12 WRONG steps): CONFIRMED 4 (G1-2 s12, G1-5 s12, G3-1 s12, G4-2 s10); ALTERNATIVE 8 (G1-2 s10, G1-3 s10, G1-5 s10, G3-1 s10, G3-2 s10, G3-3 s10, G3-4 s10, G3-6 s10); REJECTED 0.

Extra findings outside the WRONG lists:
- G2-3 AMDateUtil.<init> has verdict CORRECT, but its step 10 ("onCreateView -> RecentListAdapter.onBindViewHolder via setAdapter") is the same wrong edge. Fixed by this group. The checker missed it.
- G4-2 step 11 and the step-11 OK notes in G3-1..G3-6: the row click (onBindViewHolder -> $1.onClick) needed a producer for NEED_RECENT. setItems -> onBindViewHolder now provides it. No verdict change.

Build 6 (build_round1_6.txt): errors 0, warnings 0, STRICT True. Edges 4358 (4359 - 1 ENTERS - 2 onCreateView edges + 2 setItems edges). REACHABLE and UNREACHABLE unchanged (1960 / 247).

Not in group 1 (same S3 pattern, handled in the FileBrowser group): G3-5 steps 13 and 12, G4-1 steps 9, 10 and 12, FileBrowserFragment.onCreateView -> row click edges (graph_def.py ~550-551).

### Group 2: FileBrowserFragment hosts, Misc-tab export and converter, result branches, Dropbox upload, Download and Settings

Changes in graph_def.py (all lines are current line numbers):
- Host variants (about 560-626): openFile@X clones (FB_ROW_IS_FILE guard at 572 on every host except UPLOADDROPBOX; the UPLOADDROPBOX variant reaches notifyFileClick instead). Per-host chain: onCreate@X, onCreateView@X, onResume@X, browseTo@X, fill@X, setItems@X, onBindViewHolder@X, $1.onClick@X (NEED_FB_ROW), openFile@X.
- Base chain (593-609): host-neutral. The long-press edge moved to base onBindViewHolder (593). The base openFile -> notifyFileClick auto edge is suppressed (sup at 546), so no base node reaches a host listener.
- Base CALL restore (599-609): 11 bytecode CALL edges that build_graph.py:223 drops (see Systemic fixes below).
- Page entries: OPEN from FB.onResume@OPEN (634); EXPORT and CONVERTER from FB.onResume@EXPORT and @CONVERTER (635-636) with NEED_EXPORT_SECTION.
- Page-sourced lifecycle (637-638): only onDestroy is kept from each page. The page-sourced onCreateView edges are removed.
- New state text NEED_EXPORT_SECTION (graph_def.py:171-172): "The Export section of the Misc tab is expanded" (export_items is GONE in misc_tab.xml:256-257; header toggle MiscTabFragment.java:240-241). Used on 635, 636, 1139, 1485.
- Export and converter result branches: sup at 546-553 suppresses the super-call auto edges ExportAnyMemoDbFragment.onActivityResult -> FileBrowserFragment.onActivityResult and ConverterFragment.onActivityResult -> FileBrowserFragment.onActivityResult. The GATE entry at (old) 2999 is deleted. The GATE at 3000 (base import branch -> $3.<init>) is kept.
- GATE entry added for DropboxApiHelper$5.call -> DropboxApiHelper.getResponseErrorString (graph_def.py ~3001): guard !response.isSuccessful() (DropboxApiHelper.java:249-250), after the file-exists check (:236-238).
- Duplicate hand edge notifyFileClick -> UploadDropboxActivity.onFileBrowserFileClick (old graph_def.py:1288, no guard) removed; the guarded edge at 579 is the only one.

| Report | Step | Verdict | Source evidence | What changed in graph_def.py and why |
|---|---|---|---|---|
| G3-5 FileBrowserFragment.<init> | 6 | ALTERNATIVE | AnyMemo.java:240-241, 253-257; RecentListFragment.onCreateView | The ENTERS from AnyMemo$2 to S_MAIN_RECENT is removed. S_MAIN_RECENT is entered from RecentListFragment.onCreateView (line 364), as the report asks. OPEN is entered from FB.onResume@OPEN (634), not onCreateView, because the Open tab shows the file list, and the list is filled in onResume (FileBrowserFragment.java:208-212). DOWNLOAD is entered from DownloadTabFragment.onCreateView (365). |
| G3-5 | 8 | CONFIRMED | AnyMemo.java:249-250 | The ENTERS from AnyMemo$2 to S_MAIN_MISC is removed. S_MAIN_MISC is entered from MiscTabFragment.onCreateView (366), reached through the CALL to MiscTabFragment.<init> (347). |
| G3-5 | 9 | CONFIRMED | MiscTabFragment.java:129-131 (onAttach sets mActivity), 143-146 (onCreate), per the report's citations | The page-sourced onCreateView edge is removed. Lifecycle is now MiscTab.<init> -> onAttach -> onCreate -> onCreateView (1470-1472). The page-sourced onDestroy and onSaveInstanceState edges (1468) are kept: they run when the page is left, so they are not backwards. |
| G3-5 | 11 | ALTERNATIVE | misc_tab.xml:256-257; MiscTabFragment.java:240-241, 253-256 | The ENTERS from MiscTab.onClick to S_DLG_EXPORT_ANYMEMO is already gone (the picker is now entered from FB.onResume@EXPORT, 635). The report's state "the folder listing has at least one file" is replaced by "the Export section is expanded" (NEED_EXPORT_SECTION). The picker list shows the folder whether or not it has files. The export button is a row of export_items, which is GONE until the header is tapped. Extra: converter NEED_DECK at 636 and 1485 had the same error and got the same fix. |
| G3-5 | 12 | ALTERNATIVE | ExportAnyMemoDbFragment.java:33-41 (onCreate), :34 (super.onCreate) | Kept the super chain ExportAnyMemo.onCreate -> FB.onCreate@EXPORT (629; super at :34) -> onCreateView@EXPORT, instead of the report's ExportAnyMemo.onCreate -> FB.onCreateView. The report's version drops FB.onCreate, which sets the menu flag (FileBrowserFragment.java:173). The page-sourced onCreateView edge is removed (see step 9 for the pattern). |
| G3-5 | 13 | CONFIRMED | FileBrowserFragment.java:480, 514-519, 594 (setItems), 216-232 | The onCreateView -> row-click edges (old 550-551 loop) are removed. The chain is browseTo@X -> fill@X -> setItems@X -> onBindViewHolder@X -> $1.onClick@X, with NEED_FB_ROW ("the current folder has at least one file or sub-folder to list, so a row is bound"), as the report asks. |
| G3-5 | 18 | ALTERNATIVE | ExportAnyMemoDbFragment.java:64, 96-97; FileBrowserFragment.java:326 | The report's claim is right: the else branch runs when the export save condition at line 64 is false, and it forwards requestCode 1002, not 1001. The fix went further: the super-call edge is suppressed (sup at 546-553), because the forwarded call reaches no app code. A guarded edge would still reach the base import branch in the graph, and the tool cannot check the guard. The negated condition is recorded in the comment at 1146-1150. |
| G3-5 | 19 | ALTERNATIVE | FileBrowserFragment.java:311-316, 326, 338, 354 | The route is infeasible for the reason given (the listener needs requestCode 1001). The origin of the import path is the RESULT at graph_def.py:657 (FB.onOptionsItemSelected -> FB.onActivityResult), not the old line 571. The GATE for the export -> base edge (old 2999) is deleted. The GATE for FB.onActivityResult -> $3.<init> (3000) is kept. A dead-end variant (FB.onActivityResult@EXPORT) was tried and rejected: build_graph.py:228 copies every base auto CALL onto each @variant, so it picked up $3.<init> and getFileNameFromUri. |
| G4-1 FileBrowserFragment (ShareUtil) | 9 | ALTERNATIVE | FileBrowserFragment.java:208-212 (onResume browses), AnyMemo.java:242-246, 253-257 | The page-sourced edge S_MAIN_OPEN -> FB.onCreateView@OPEN is removed. OPEN is entered from FB.onResume@OPEN (634), after the list is filled, instead of onCreateView. The OpenTabFragment.onAttach -> FB.onCreate@OPEN edge (627) is kept. |
| G4-1 | 10 | ALTERNATIVE | FileBrowserFragment.java:272, 480, 594 | The report wanted onCreateView@OPEN -> row click (550). The row click is now reached through the chain browseTo@OPEN -> fill@OPEN -> setItems@OPEN -> onBindViewHolder@OPEN -> $1.onClick@OPEN, not directly from browseTo. Also checked: the old onCreateView -> onBindViewHolder edge (report: graph_def.py:2579) is gone. The row loop at 2731 has only getItemCount. |
| G4-1 | 12 | CONFIRMED | FileBrowserFragment.java:407, 412 | The FB_TARGET edges (572) carry FB_ROW_IS_FILE (folder rows browse, they do not reach OpenTabFragment$1.onFileBrowserFileClick). |
| G4-3 AMPrefUtil.removePrefKeys | 9 | CONFIRMED | Fragment.java:940-946, 2626-2629; FileBrowserFragment.java:173 | onCreateOptionsMenu is removed from the FB_PAGES loop. onCreate@X -> onCreateOptionsMenu (588, 615) carries FB_MENU_GUARD: the menu is built only after setHasOptionsMenu(true) ran in onCreate. This is the report's fix. |
| G2-1 DropboxApiHelper.getResponseErrorString | 12 | CONFIRMED | FileBrowserFragment.java:412-415; OpenTabFragment.java:38 | notifyFileClick is in the clone's exclude set (568), so openFile@OPEN no longer reaches notifyFileClick. The UPLOADDROPBOX hand edge at 570 stays. |
| G2-1 | 13 | REJECTED (edge) | FileBrowserFragment.java:435-438 | The edge notifyFileClick -> UploadDropboxActivity.onFileBrowserFileClick is right by source: the activity branch (437) runs when getParentFragment() is not a listener (435; null on the activity host). The report's optional guard text was added (graph_def.py:579-580). The duplicate hand edge at old 1288 was removed (see Changes). |
| G2-1 | 20 | CONFIRMED | DropboxApiHelper.java:236-238, 248-251 | The auto record is DropboxApiHelper$5.call -> getResponseErrorString at DropboxApiHelper.java:250 (checked in auto_calls.json). A GATE entry adds the guard !response.isSuccessful() (249-250), after the file-exists check (236-238). |
| G2-4 SettingsScreen$11 | 21 | CONFIRMED | FileBrowserFragment.java:407-414 | The SETTINGS_Q edge (FB_TARGET, 572) now carries FB_ROW_IS_FILE. |
| G1-6 DownloaderUtils.downloadFile | 12 | CONFIRMED | DownloadTabFragment.java:64-66 | Guard v == amButton on DownloadTabFragment.onClick -> AnyMemoDownloaderActivity.<init> (1473). The report's line 1372 is stale. |

Group 2 totals (17 WRONG steps): CONFIRMED 9 (G3-5 s8, s9, s13; G4-1 s12; G4-3 s9; G2-1 s12, s20; G2-4 s21; G1-6 s12); ALTERNATIVE 7 (G3-5 s6, s11, s12, s18, s19; G4-1 s9, s10); REJECTED 1 (G2-1 s13, the edge only; its guard text was refined).

Extra findings outside the WRONG lists:
- Converter super call (ConverterFragment.onActivityResult -> base FB.onActivityResult, an auto edge): the same error as export step 18. Converter's own request code is 1003 (ConverterFragment.java:47). Suppressed at 546-553.
- Converter picker NEED_DECK (636, 1485): same fix as export step 11.
- Long-press edge moved from the per-host row to base onBindViewHolder (593, 609) so that the base chain holds it.
- Download ENTERS (G1-6 step 8, checker marked OK): the tab-switch edge into S_MAIN_DOWNLOAD was moved to DownloadTabFragment.onCreateView (367), so the page is entered after its view exists. Same pattern as G3-5 step 6.

Systemic fixes from group 2:
- Base CALL edges restored (graph_def.py:599-609): FB.onCreate -> AMEnv.<clinit> (164), onCreate -> DaggerAppComponents inject (133), onCreate -> BaseDialogFragment.fragmentComponents (133), browseTo -> fill (228), fill -> DISPLAYMODE.<clinit> (243), fill -> setItems (272), upOneLevel -> browseTo (278), openFile -> DISPLAYMODE.<clinit> (394), openFile -> upOneLevel (391), openFile -> browseTo (428), $1.onClick -> openFile (517). The line numbers are from auto_calls.json.
- Cause (tools bug, not fixed here): build_graph.py:223 skips an auto edge when ANY hand edge has the same base-name pair. The per-host @X edges therefore silently removed the base auto CALLs. Build 7 failed as UNRESOLVED (FileBrowserFragment$FileBrowserAdapter$3.compare) because browseTo -> fill was missing. Restored by hand (above).
- Second tools finding: build_graph.py:228 copies every base auto CALL onto each hand-written @variant of that base (variants[base]). Any @X node of a base with auto CALLs inherits them. That is why the dead-end variant was dropped (G3-5 s19).
- Still-dropped auto edges from the line-223 rule (not yet checked against round 0): AbstractDownloaderFragment$DownloadListAdapter$1.onClick -> showFetchDatabaseDialog (434), $1$1.call -> openCategory (422), $1.call -> initialRetrieve (185), FetchDatabaseTask.doInBackground -> fetchDatabase (319), onViewCreated -> refreshList (173), RetrieveTask.onPostExecute -> hasMore (231), $1$2.call -> goBack (430), $2.onClick -> startFetchDatabaseTask (287), DropboxListActivity.refreshList -> AbstractDownloaderFragment.refreshList (DropboxListActivity.java:95), DropboxOauth2AccountActivity.onCreate -> Oauth2AccountActivity.onCreate (DropboxOauth2AccountActivity.java:21). To be handled in the group (d) and (e) work.

Build history for group 2: build 7 UNRESOLVED (comparator, errors 1); build 8 Dagger hint warning (Ec37fd169, fixed by rewording); build 9 clean; build 10 clean (4459 edges after the export and converter super calls were suppressed); build 11 clean (G2-1 guard added; the duplicate notifyFileClick edge was removed after build 11, so the final rebuild is the one to cite).


## Round 1b (2026-10-26, single writer; graph_def.py is the only edited file)

Backup before round 1b: scratch/graph_def_before_round1b.py. Baseline build (21:53 numbers): scratch/build_r1b_0.txt = methods 2207, pages 77, edges 4458, REACHABLE 1960, UNREACHABLE 247 (no_trigger_in_app 222, framework_never_calls 18, branch_never_taken 7), errors 0, warnings 0, STRICT True (graph_def.py line 39).
Helper scripts: scratch/r1b_tool.py (exact-text replace, one match required, nothing written on failure), scratch/r1b_F.py (group F).

### Group F

| Item | Outcome | Grep / source confirmation |
|---|---|---|
| F1 | applied | Three new GATE keys (createConversationNotificationChannel, createCardPlayerNotificationChannel, createReviewReminderNotificationChannel) for createNotificationChannels, placed at the end of the GATE dict. No prior key (grep). Auto edges present in auto_calls.json (lines 41-43, dispatch exact). Source: utils/NotificationChannelUtil.java:36 is the SDK_INT >= O check. |
| F2 | applied | Edge at graph_def.py ~1044 (FRAMEWORK, multipleLoaderManager registers the Setting loader in onCreate) and edge ~2744 (onLoaderReset) now start at SettingsScreen.onCreate. GATE key for onLoaderReset moved to SettingsScreen.onCreate. Source: ui/SettingsScreen.java:137-139 (registerLoaderCallbacks at 137). Other callers of SettingsScreen.<init> (OpenActionsFragment$1.onClick, MiscTabFragment.onClick) unchanged. |
| F3 | applied | NEED_FULLSCREEN state_text added after NEED_PREF_SAVED. GATE ('BaseActivity.onCreate', 'BaseActivity.enableImmersiveMode') gets needs_state NEED_FULLSCREEN. Sources: common/BaseActivity.java:36-37; res/xml/option_screen.xml:66-69 (CheckBoxPreference fullscreen_mode, defaultValue false); common/AMPrefKeys.java:126. |
| F4 | applied | GATE key ('BaseActivity.activityComponents', 'AMApplication.activityComponents'). Auto edge exists (auto_calls.json line 79, no hand edge on the pair). Source: common/BaseActivity.java:78. |
| F5 | applied | GATE key ('AnyMemo.onDestroy', 'MultipleLoaderManager.destroy'). Auto edge exists (auto_calls.json line 409). Source: ui/AnyMemo.java:408. |

Build after group F: scratch/build_r1b_F.txt. methods 2207, pages 77, edges 4458, REACHABLE 1960, UNREACHABLE 247 (no_trigger_in_app 222, framework_never_calls 18, branch_never_taken 7), errors 0, warnings 0, STRICT True.

### Group W (W1, W2)

| Item | Outcome | Grep / source confirmation |
|---|---|---|
| W1 | applied | Hand edge 'S_DLG_CATEGORY_CARD' -> 'CardEditor$8.onReceiveCategory' (CALL) now has the guard and evidence from the brief. Note: the brief quotes the trigger as "tap OK in the category dialog", but the file text is "a category is picked". I kept the file text (no change to the trigger). Sources: ui/CategoryEditorFragment.java:94-109 (OK button at 96; category null when no row is checked at 100-101); ui/CardEditor.java:567 (resultListener set), 572 (show), 634-639 (onReceiveCategory). No sup() added. |
| W2 | applied | New constant NEED_DB_NAME_TAKEN (graph_def.py line 180, state_text kind 'file') placed after NEED_FILE_ZIP. GATE ('FileBrowserFragment.onActivityResult', 'FileBrowserFragment$3.<init>') now has needs_state NEED_DB_NAME_TAKEN; its existing guard is kept. Source: ui/FileBrowserFragment.java:336-338 (newFile at 336, exists check at 338). The sup() for ExportAnyMemoDbFragment.onActivityResult and ConverterFragment.onActivityResult -> FileBrowserFragment.onActivityResult is already present at graph_def.py 554-555, so nothing was added. |

Tally Group W: applied 2, already applied 0, skipped 0.
Build after group W: scratch/build_r1b_W.txt. methods 2207, pages 77, edges 4458, REACHABLE 1960, UNREACHABLE 247 (no_trigger_in_app 222, framework_never_calls 18, branch_never_taken 7), errors 0, warnings 0, STRICT True.

### Group C (C1 to C13)

| Item | Outcome | Grep / source confirmation |
|---|---|---|
| C1 | applied, no fallback | The four gui edges QACardActivity$4..$7.onClick now start at CardFragment.onCreateView (was QACardActivity.<init>). Source: ui/CardFragment.java:114-201 (onCreateView); card view listener set at 127-128 ($6, $7); text listener set at 135-140 ($4, $5). Listener definitions: ui/QACardActivity.java:726-755; builder: 255-261. Evidence strings now also cite the CardFragment lines. Built: 4 FRAMEWORK edges from CardFragment.onCreateView. |
| C2 | applied, 5 of 5 variants existed | GATE keys (QACardActivity.onClickQuestionView + v, QACardActivity.displayCard + v) for v = '', @CardPlayerActivity, @PreviewEditActivity, @QuizActivity, @StudyActivity. Guard from ui/QACardActivity.java:547-549. Built: all 5 CALL edges guard True. |
| C3 | applied, 5 of 5 variants existed | GATE keys (displayCard + v, FlipableCardFragment.<init>) with DOUBLE_SIDED (QACardActivity.java:371-372) and (displayCard + v, TwoFieldsCardFragment.<init>) with SINGLE_SIDED (QACardActivity.java:321-322). Built: all 10 CALL edges guard True. |
| C4 | applied | Hand edge CardPlayerFragment.onDestroyView -> CardPlayerService.stopPlaying: guard added. Source: ui/CardPlayerFragment.java:201-207 (stopPlaying), 204-205 (activity and service null check). Built: guard True. |
| C5 | applied | GATE for CardPlayerState$1.transition -> CardPlayerService$1.onPlayCard. The pair is an automatic edge (built JSON E759be6b5, bytecode line 60, the GO_TO_PREV branch); it is not a hand edge. The GO_TO_NEXT call at service/cardplayer/CardPlayerState.java:52 is on the same pair, so the one GATE guard covers both call sites. Source: CardPlayerState.java:43-61; service/CardPlayerService.java:229-235. Built: guard True. |
| C6 | applied | Guard on CardPlayerFragment$2.onReceive -> CardPlayerActivity.gotoCardId replaced (was only activity.isActivityForeground()). Evidence changed from 238-239 to 234-239 so it covers the new null check. Source: ui/CardPlayerFragment.java:233-239 (null check at 234, foreground and card id check at 238). Built: guard True. |
| C7 | applied, no fallback | The automatic edge (CardPlayerActivity.java:205) is replaced by two hand edges to QACardActivity.displayCard@CardPlayerActivity: DOUBLE_SIDED (guard 199-202, displayCard(false)) and otherwise (guard 199-205, displayCard(true)). The builder kept both (no merge). Source: ui/CardPlayerActivity.java:198-208. Built: E82b481db and E8d8bd783 with guard True; the automatic edge is gone. |
| C8 | applied | GATE keys ('QACardActivity$2.run', X.onPostInit) for X = CardPlayerActivity, StudyActivity, QuizActivity, PreviewEditActivity. Not a no-op: all four were automatic edges with no hand edge on the pair (built JSON, bytecode line 660). Source: ui/QACardActivity.java:167 (setOnAllLoaderCompletedRunnable), 658-662 (onPostInitRunnable). Built: all 4 guard True. |
| C9 | applied | needs_state=NEED_CARD added to the ENTRY CardPlayerActivity.onPostInit -> CardPlayerService.onCreate. Source: ui/CardPlayerActivity.java:111 (bindCardPlayerService), 112-113 (empty-deck check). Built: state True. Hazard recorded below. |
| C10 | applied | GATE ('StudyActivity.onClickQuestionView', 'QACardActivity.displayCard@StudyActivity'): guard 'answer not yet shown' and needs_state NEED_CARD. Source: ui/StudyActivity.java:363-369 (the check is at 365; the call at 366). Built: guard True and state True. |
| C11 | applied, no fallback | The automatic edge (StudyActivity.java:313, INVISIBLE) is replaced by three CALL hand edges to GradeButtonsFragment.setVisibility: VISIBLE (guard 306-307), GONE (guard 310-311), INVISIBLE (guard 312-313). The builder kept all three. Source: ui/StudyActivity.java:303-315 (onPostDisplayCard). Built: 3 edges, guard True. |
| C12 | applied | GATE ('DefaultScheduler.schedule', 'DefaultScheduler.calculateIntervalNoise'). Source: scheduler/DefaultScheduler.java:128-129. Built: guard True. |
| C13 | applied | GATE ('DefaultScheduler.calculateIntervalNoise', 'DefaultScheduler.randomNumber'). Source: scheduler/DefaultScheduler.java:199-200 (the minimal-interval branch sets noise to 0, so the randomNumber calls at 202-208 need interval above the minimum). The 60-day guard was not added, as the brief says. Built: guard True. |

Tally Group C: applied 13, already applied 0, skipped 0, fallbacks used 0.

Hazard candidate (recorded, not a graph change): ui/CardPlayerActivity.java:213 reads getCurrentCard().getId() inside bindCardPlayerService(), which is called at line 111. The empty-deck check (showNoItemDialog) comes after, at lines 112-113. If the deck is empty, getCurrentCard() can be null here, which would throw before the dialog. INFERRED: the crash itself is not checked at runtime.

Build after group C: scratch/build_r1b_C.txt. methods 2207, pages 77, edges 4461 (up 3: C7 gives +1, C11 gives +2), REACHABLE 1960, UNREACHABLE 247 (no_trigger_in_app 222, framework_never_calls 18, branch_never_taken 7), errors 0, warnings 0, STRICT True. needs_state edges 137 -> 139 (C9, C10).
Pre-existing sanity-check contradictions (same in the W build, not caused by group C): CategoryEditorFragment.onDestroy, PreviewEditActivity.onDestroy, QuizLauncherDialogFragment.onDestroy are UNREACHABLE but ran in a tool run. These are for item A1.
Backup before group C: scratch/graph_def_before_group_C.py. Script: scratch/r1b_C.py.

### Group B (B1 to B11)

Backup before group B: scratch/graph_def_before_group_B.py. Script: scratch/r1b_B.py (line-prefix edits; each anchor must match exactly once). Edge counts in the build: ENTERS -6, ENTRY +3, GUI +4, FRAMEWORK +1, LIFECYCLE -1, CALL -1 (net 0, 4461 -> 4461). The CALL -1 is build_graph.py:223 at work: the new hand CALL on CategoryEditorFragment$1.onClick -> QuizLauncherDialogFragment$10.onReceiveCategory suppressed the automatic CALL on the same pair.

| Item | Outcome | Grep / source confirmation |
|---|---|---|
| B1 | applied, FALLBACK | The brief says OpenActionsFragment.onCreateView calls df.show. Source: the show call is in RecentListFragment.java:450 inside RecentListAdapter$3.onClick (the existing CALL to OpenActionsFragment.<init> at 446-451 is kept). Fallback: the ENTERS was moved to OpenActionsFragment.onCreateView (ui/OpenActionsFragment.java:85-117), which builds the sheet view. Trigger text and evidence name the df.show caller. Built: OpenActionsFragment.onCreateView -> S_DLG_OPEN_ACTIONS ENTERS (E7be5a455), the only incoming ENTERS. |
| B2 | applied | Deleted OpenActionsFragment$1.onClick -> S_CARD_LIST ENTERS (OpenActionsFragment.java:139-145). The ENTRY to CardListActivity.<init> from the same click stays (E14fa2d40). NEED_CARD removed from CardListActivity$11.run -> S_CARD_LIST (the onPostInitRunnable at CardListActivity.java:640-655 sets the adapter, selection, listeners and sort; it needs no card). The brief's line 835 does not exist (the file has 665 lines). The long-press edge at CardListActivity.java:437-446 keeps NEED_CARD. |
| B3 | applied, FALLBACK | Same premise as B1: df.show is at OpenActionsFragment.java:152, inside the click at 147-154. Deleted OpenActionsFragment$1.onClick -> S_DLG_QUIZ_LAUNCHER ENTERS. Added QuizLauncherDialogFragment.onCreateDialog -> S_DLG_QUIZ_LAUNCHER ENTERS (Ec49d569c, source QuizLauncherDialogFragment.java:145-205). The CALL from the click to QuizLauncherDialogFragment.<init> (Eef9e1b13) is kept. |
| B4 | applied, FALLBACK (ENTERS part) | (a) Already applied: the construction CALL showCategoriesDialog -> CategoryEditorFragment.<init> and the lifecycle chain to onCreateView (Efc5affc9) already existed as automatic edges. (b) ENTERS moved from showCategoriesDialog to CategoryEditorFragment.onCreateView (E6341e794, state NEED_CATEGORY kept). Fallback: the df.show is still at QuizLauncherDialogFragment.java:508-516. (c) Result CALL moved from S_DLG_CATEGORY_QUIZ to CategoryEditorFragment$1.onClick (the OK handler), guard v == okButton (CategoryEditorFragment.java:96), state NEED_CATEGORY (Efafd611e). Source: CategoryEditorFragment.java:105-107 calls resultListener.onReceiveCategory when OK is tapped. |
| B5 | applied | GATE ('QuizQueueManager$Builder.build', 'QuizQueueManager.refill(Category)'): guard filterCategory != null (QuizQueueManager.java:199-202); state: the category id from EXTRA_CATEGORY_ID exists in the category table (QuizActivity.java:264-268). The graph node is named refill(Category), as in the brief's intent. Built: E29ea0011, guard True, state True. |
| B6 | applied | Deleted OpenActionsFragment$1.onClick -> S_CARD_PLAYER ENTERS (the same click reaches CardPlayerActivity.<init> through the ENTRY, Ebd3f9223). Guard v == cardPlayerItem (OpenActionsFragment.java:192-197) added to the ENTRY (1351). S_CARD_PLAYER still has four other incoming ENTERS. |
| B7 | applied, FALLBACK (settings CALL source) | Star loop from CardPlayerFragment.onCreate replaced by the chain onCreate -> onCreateView -> onResume -> onPause -> onDestroyView (LIFECYCLE) plus onCreate -> onCreateOptionsMenu (LIFECYCLE). onOptionsItemSelected is now a FRAMEWORK edge from S_CARD_PLAYER (FW_MENU; SRC CardPlayerFragment.java:137-146). The settings CALL moved from CardPlayerFragment$1.onClick to CardPlayerFragment.onOptionsItemSelected: the `itemId == card_player_settings` branch calls displaySettingsDialog() at lines 140-141 (built: E6f73d55d). Note: onPause -> onDestroyView skips the framework onStop, which is not a node in this graph. |
| B8 | applied | Deleted StudyActivity.onOptionsItemSelected -> S_PREVIEW_EDIT ENTERS (line 721). Added ENTRY StudyActivity.onOptionsItemSelected -> PreviewEditActivity.<init>, guard itemId == menu_context_gotoprev (StudyActivity.java:175-177) via gotoPreviewEdit() (701-710). |
| B9 | applied | PreviewEditActivity.onOptionsItemSelected -> S_DETAIL ENTERS (line 993) replaced by ENTRY -> DetailScreen.<init>, guard getCurrentCard() != null (PreviewEditActivity.java:278). StudyActivity menudetail ENTERS (line 708) replaced by ENTRY -> DetailScreen.<init>, guard itemId == menudetail (StudyActivity.java:157-159), needs_state NEED_CARD kept. S_DETAIL still has DetailScreen.onOptionsItemSelected and DetailScreen$InitTask.onPostExecute as incoming ENTERS. |
| B10 | applied, FALLBACK | Deleted SettingsScreen$10.onClick -> S_DLG_TYPEFACE_Q and _A ENTERS (the guards stay in the text). Added FileBrowserFragment.onResume@SETTINGS_Q/A -> S_DLG_TYPEFACE_Q/A ENTERS (E97310e47, Ee7db3358). Fallback: the df.show calls are at SettingsScreen.java:720 and :731; the ENTERS is placed on onResume (picker on screen after the list is filled). Added four GUI edges from S_SETTINGS to SettingsScreen$10.onClick (the one listener that handles all the row taps, FRAMEWORK from updateViews): Q checkbox (658-665), Q field (712-721, needs VISIBLE), A checkbox (667-674), A field (723-732, needs VISIBLE). VISIBLE = the checkbox is ticked, which is set when a font is saved (SettingsScreen.java:467-472 and 475-480) or by the tap (659-660 and 669-670). |
| B11 | applied, FALLBACK | Deleted OpenTabFragment$1.onFileBrowserFileClick -> S_DLG_OPEN_ACTIONS ENTERS (NEED_DECK; line 683). The sheet is now entered from OpenActionsFragment.onCreateView (B1), and the CALL at line 682 still reaches it. GATE ('FileBrowserFragment$FileBrowserAdapter$1.onClick@OPEN', 'FileBrowserFragment.openFile@OPEN'): needs_state 'the Open tab folder holds at least one .db file'. Source for the state is the brief; the Open tab's .db file filter was not re-read this round (INFERRED). |

Tally Group B: 11 items. Applied with no fallback: B2, B5, B6, B8, B9. Applied with fallback: B1, B3, B4 (ENTERS part), B7 (settings CALL source), B10, B11. Already applied (part of B4): construction CALL and lifecycle chain. Skipped: 0.

Build after group B: scratch/build_r1b_B.txt. methods 2207, pages 77, edges 4461 (net 0), REACHABLE 1960, UNREACHABLE 247 (no_trigger_in_app 222, framework_never_calls 18, branch_never_taken 7), errors 0, warnings 0, STRICT True. Routes checked by scratch/r1b_q.py: S_DLG_OPEN_ACTIONS, S_DLG_QUIZ_LAUNCHER, S_DLG_CATEGORY_QUIZ, S_DLG_TYPEFACE_Q/A, S_CARD_PLAYER, S_PREVIEW_EDIT, S_DETAIL, S_CARD_LIST all have incoming edges. QuizActivity.<init> is entered by QuizLauncherDialogFragment$2.onClick at three ENTRY edges (E1d6bc99a, E113cd89b, E6a473753). The no-state route E6a473753 (QuizLauncherDialogFragment.java:255-265) is the one the builder prefers, so the category route is not what the route search shows (builder limit, see the report).


## Round 1b, Group D (Dropbox and downloader): applied

Script: scratch/r1b_D.py (all 13 apply() calls printed OK). Backup of graph_def.py before the group: scratch/graph_def_before_round1b_D.py. Build: scratch/build_round1b_D.txt (exit 1, 1 error, see the end of this section).

- D1 applied. Locator correction: the brief names "the DropboxApiHelper$4.call route", but the edge is DownloadTabFragment.onClick -> DropboxOauth2AccountActivity.<init> (ENTRY). Guard added: 'v == dropboxButton (DownloadTabFragment.java:67-69)'. Built JSON: E447f2cb3 guard True.
- D2 applied. The old loop (LIFECYCLE onCreate, onDestroy, onNewIntent from DropboxOauth2AccountActivity.onCreate) is removed. Replaced by CALL DropboxOauth2AccountActivity.onCreate -> Oauth2AccountActivity.onCreate (super, :21) and ENTRY S_DROPBOX_LOGIN -> Oauth2AccountActivity.onNewIntent (needs_state, env ENV_OAUTH_CALLBACK; trigger text says the framework redirect delivery is INFERRED). The onCreate LIFECYCLE had to go, otherwise it would duplicate the CALL on the same pair. onDestroy removal is intentional and is re-added in A1. Built JSON: Eba2af780, E0f39672d.
- D3 applied. Deleted the wrong fetch edge fetchTokenAndOnAuthenticate -> Oauth2AccountActivity$2.onComplete. The fetch path now goes only to $1.onSuccess and $1.onError (built JSON: E969bac98, E3fc0a812).
- D4 applied, with deviations (logged):
  (a) $1.onSuccess -> DropboxOauth2AccountActivity.onAuthenticated: needs_state removed, env ENV_OAUTH_CALLBACK (built: Ebc85a6b7, state False, env True). GATE entries for fetch -> $1.onError and fetch -> $1.onSuccess changed from ENV_DROPBOX to ENV_OAUTH_CALLBACK.
  (b) $2.onComplete -> onAuthenticated: evidence :114, needs_state NEED_SAVED_TOKEN (built: E6fe4b6d1). Env is ENV_DROPBOX, not the brief's ENV_NET (DEVIATION): the verify step calls the Dropbox API (dropboxApiHelper.getUserInfo, DropboxOauth2AccountActivity.java:33-35) and the ENV_NET text names anymemo.org. The GATE verify entries stay ENV_DROPBOX for the same reason.
  (c) verify -> $1.onSuccess retargeted to Oauth2AccountActivity$2.onComplete (needs_state, env ENV_DROPBOX; built E5cf638d0). The duplicate verify -> $2.onComplete at the old line 1626 is deleted; only one edge remains.
  (d) $1.onError -> requestAuth renamed to Oauth2AccountActivity$2.onError (verify error path, Oauth2AccountActivity.java:118-121). Env changed from ENV_NET to ENV_DROPBOX (DEVIATION, same reason as (b)). Built: E39984c4f, state True, env True.
  The automatic Oauth2AccountActivity$1.onError -> requestAuth (bytecode line 100) comes back, as the brief expected (built: Ef42f178b).
- D5 covered by D4(b): evidence :114 is in the built JSON.
- D6 applied. Interpretation: the brief's "source becomes RT.onPostExecute@X" was applied to the row-click edge only. The per-host edge onCreateView@X -> getView is removed, because rows reach getView only through addList. Changes: RT.onPostExecute@X -> DL_LN.onClick@X (FRAMEWORK, env=h_env; built E32fc9ed1 and Ebebb15f3); RT.onPostExecute@X -> DownloadListAdapter.addList (CALL, per host, SRC :229-230; built Ef1011b90 and E81e3fc1d); shared addList -> getView (FRAMEWORK, drawn once outside the host loop, layout timing INFERRED; built Ecf6270aa). No shared getView -> row-click edge was added. The comment at about line 1216 was rewritten to match.
- D7 applied. startFetchDatabaseTask@X -> FetchDatabaseTask.onPreExecute@X (per host; built E86dd5c3a, Eb99ef3ad), then ASYNC onPreExecute@X -> doInBackground@X (Eb150dbd7, Ef9fd3634), and the direct startFetchDatabaseTask -> doInBackground edge is deleted. The same shape for RetrieveTask: refreshList@X -> RetrieveTask.onPreExecute@X (E9827b63c, E6bf92af2), onPreExecute@X -> doInBackground@X (Ec5d30f7f, Ec136ea15), direct edge deleted. Kept on purpose: the row-click edge DL_LN.onClick@X -> shared RetrieveTask.onPreExecute (built Ec780d310, Ea01634b0). The shared FetchDatabaseTask.onPreExecute now has no incoming and no outgoing edge. The builder accepts it (base-name reachability, no error).
- D8 applied. Guard 'row is neither Category nor Back (AbstractDownloaderFragment.java:417, 425)' on DL_LN.onClick@X -> showFetchDatabaseDialog@X (built E30961aed and E72ef4f0f, guard True). Locator note: the brief says "near 1228"; the edge is in the same DL_HOSTS loop, matched by text.
- D9 applied. Two hand CALL edges: fetchDatabase -> DownloaderUtils.downloadFile with guard .db (evidence :81, built E4dfe850b) and guard .zip (evidence :85, built Ee8a0cf5a). Only these two remain for the pair. Trigger text names filePath (AMEnv.DEFAULT_ROOT_PATH + fileName) and zipFilePath (AMEnv.DEFAULT_TMP_PATH + fileName), from AnyMemoDownloaderFragment.java:79-85.
- D10 applied. Four hand CALL edges on DropboxApiHelper$3.subscribe: parseListFolderResponse at :164 (guard first response successful, Ebf21d808) and at :186 (guard hasMore and continuation successful, E47b1de4b); getResponseErrorString at :156 (guard first response failed, Eb9295a38) and at :178 (guard continuation failed, E12dc9191). The brief said the :186 call was already in the graph. It was, but the new :164 hand edge would suppress it (same pair), so :186 was written by hand as well.
- D11 FALLBACK. Fragment.onCreate cannot be a node: build_graph.py:350 rejects endpoints that are not app methods or screens. Kept onAttach -> onCreateView (LIFECYCLE, evidence ui/DownloadTabFragment.java:52-61) and added to its trigger text that the inherited Fragment.onCreate runs in between (built E2455ca30).
- D12 applied. S_DROPBOX_LIST -> DropboxListFragment.onCreate (LIFECYCLE, needs_state from DropboxListActivity.java:42-43 token extras, evidence DropboxListFragment.java:49-55; built E098d6234, state True). DBX only.
- D13 applied. Locator correction: the brief says the refreshList -> Callable edge is near 1241, but refreshList edges are ASYNC and carry no Callable. The guard went on RetrieveTask.doInBackground@X -> $1.call@X (CALL, SRC :208-212; for-loop at :210 confirmed; built E24b4ee5c, guard True).

Build after Group D (scratch/build_round1b_D.txt): methods 2207, pages 77, edges 4460; verdicts REACHABLE 1959, UNREACHABLE 247, UNRESOLVED 1; errors 1, warnings 0. The one error is expected: ERROR method has no path and no UNREACHABLE entry: Oauth2AccountActivity.onDestroy. D2 removed the old LIFECYCLE onDestroy edge on purpose, and A1 adds it back from DropboxOauth2AccountActivity.onAuthenticated. The build is not at 0 errors until A1 is applied. Expected final state: 0 errors.


## Round 1b, Group E (database helpers, AsyncTask, state texts): applied

Scripts: scratch/r1b_E.py (13 edit replacements and one GATE block of 9 keys, applied once) and scratch/r1b_E_fix.py (one follow-up, see E17 (e)). Backup before the group: scratch/graph_def_before_round1b_E.py. Builds: scratch/build_round1b_E.txt is the final build of this group (after the follow-up). The first Group E build reported 3 errors (Oauth2AccountActivity.onDestroy, which A1 fixes, plus two ConvertIntentService notification errors, which the follow-up fixed).

- E1 applied. GATE MiscTabFragment.onClick -> DatabaseMerger.<init> (guard v == mergeButton, MiscTabFragment.java:346-349). Both duplicate edges carry the guard (built Ea1b5c440, Eb2d613a1).
- E2 applied. GATE DatabaseMerger.onClick -> DatabaseMerger$1.doHeavyTask (guard, DatabaseMerger.java:115). Kind stays CALL (built E539b41d9).
- E3 applied. GATE DatabaseUtil.mergeDatabases -> CardDaoImpl.createCards (guard destPath is not equal to srcPath, DatabaseUtil.java:47-48). Built E17765f04, guard True.
- E4 applied. The FRAMEWORK edge now starts at AbstractHelperDaoImpl.callBatchTasks -> CardDaoImpl$2.call. Evidence is FW_ORMLITE (INFERRED, SRC AbstractHelperDaoImpl.java:149-151; CardDaoImpl.java:491-496). The text has no RxJava. Located by text anchor at graph_def.py ~1580 (the brief said near 1543). Built E99db9aec. The old CardDaoImpl.createCards -> CardDaoImpl$2.call edge is gone. The new text says the call runs createCardsNoBatch at CardDaoImpl.java:493 (the call site; the Callable is at 491).
- E5 applied. Variant split for AbstractHelperDaoImpl.create. Hand edges: CategoryDaoImpl.createOrReturn -> create@CATEGORY (E2254ea7f, CategoryDaoImpl.java:37); CardDaoImpl.createCardsNoBatch -> create@CATEGORY (E3ab53e8b, guard from CardDaoImpl.java:846-851); CardDaoImpl.create -> create@CARD (Ec2fa9ffc, CardDaoImpl.java:228); create@CATEGORY -> Category.setCreationDate (E63deb88f); create@CARD -> Card.setCreationDate (Eac59faad). sup() added for the base pairs. The base edge is absent from the build. Both setCreationDate targets are REACHABLE in the build.
  Builder notes for E5: sup() acts only on automatic CALLs (build_graph.py:218), so it cannot remove hand edges. A hand edge of any kind on a base pair already suppresses automatic CALLs on that pair (build_graph.py:223), so the sup() call is redundant but harmless.
- E6 applied. GATE StudyActivity.onOptionsItemSelected -> StudyActivity.showCategoriesDialog (guard itemId == R.id.menu_memo_category, StudyActivity.java:163-164). The pending check from the previous window is resolved: the automatic edge exists (built E6d8bfe6e, guard True).
- E7 applied. The direct CategoryEditorFragment.onCreateView -> InitTask.doInBackground edge is deleted. ASYNC InitTask.onPreExecute -> doInBackground added (Efea12f21; SRC ui/CategoryEditorFragment.java:135-150). Open question resolved: no automatic onCreateView -> InitTask.doInBackground edge is generated after the delete (query returns none), so onPreExecute is no longer skipped.
- E8 applied. The direct NewCategoryTask.doInBackground edge is deleted. ASYNC NewCategoryTask.onPreExecute -> doInBackground added (E6ec64fc2; SRC ui/CategoryEditorFragment.java:241-250). GATE CategoryEditorFragment$1.onClick -> NewCategoryTask.onPreExecute (guard v == newButton, CategoryEditorFragment.java:111; built E433301e4, guard True). Checked: the if at line 111 matches.
- E9 applied, with a locator correction. The brief names "DetailScreen loadEntries" as the source of the direct edge. The actual direct edge is DetailScreen.onCreate -> DetailScreen$InitTask.doInBackground (SRC ui/DetailScreen.java:103-104, graph_def.py ~950). It is deleted. ASYNC InitTask.onPreExecute -> doInBackground added (E4c188ddd; SRC ui/DetailScreen.java:242-269).
- E10 applied, with a location change. The removePrefKeys path is DatabaseOperationDialogUtil$1$3.onClick -> AMFileUtil.deleteFileWithBackup -> deleteDbSafe -> AMPrefUtil.removePrefKeys. needs_state NEED_TYPED_DB_FILE is added to the GATE entry for DatabaseOperationDialogUtil$1$3.onClick -> AMFileUtil.deleteFileWithBackup (built E9bb8cb31, state True). NEED_TYPED_DB_FILE is defined beside NEED_AUDIO_FILE. Existence check: DatabaseOperationDialogUtil.java:57-58.
- E11 applied. GATE AMFileUtil.deleteFileWithBackup -> deleteDbSafe, guard "the file exists" (AMFileUtil.java:72-73). Checked. Built Eb84a8e8f, guard True.
- E12 applied. GATE AMFileUtil.deleteDbSafe -> AMPrefUtil.removePrefKeys, guard "the file exists" (AMFileUtil.java:59-60). Checked. Built Ed0859dd6, guard True.
- E13 applied. GATE RecentListFragment.loadRecentItemsWithDetails -> AnyMemoDBOpenHelper.getCardDao, guard (context and entry, RecentListFragment.java:337, 339-341) plus needs_state NEED_RECENT. Checked. Built E98d514af, guard and state True.
- E14 applied. DB_VERSION_ZERO (new state text) is on the onCreate edge (SQLiteOpenHelper.java:332-333; built E8ed15433, state True). DB_NEW_OR_CHANGED is reworded to "the stored schema version is newer or older than the app's" and is used only by onDowngrade and onUpgrade (graph_def.py:2442, 2446).
- E15 applied, with a note. Hand LIFECYCLE edge Setting.<init> -> Setting$CardStyle.<clinit> (cls non_standard, via C4_CLINIT_VIA, evidence SRC entity/Setting.java:46; built E07e9ee19). The automatic "Direct call" edge on that pair is suppressed (build_graph.py:223), and the build has only this one edge on the pair. The bytecode line was NOT checked: the automatic edge cites Setting.java:45, the source field initialiser is at Setting.java:46.
- E16 applied. GATE ConverterFragment.startConversion -> ConverterFragment.invokeConverterService, guard "destination extension is db and the output file does not exist" (ConverterFragment.java:93-94, 123-125). The automatic pair exists at ConverterFragment.java:125 (built Ebda5998a, guard True).
- E17 applied, with deviations:
  (a) Wording deviation. The brief's guard phrase "EXTRA_CONVERTER_CLASS is a chained importer" does not appear in the source. The guard now cites pendingImportConverterClass (MiscTabFragment.java:408-409, 469-477) (built E835f2200).
  (b) Retargeted entries. MiscTabFragment.invokeImportConversion -> ConvertIntentService.onCreate@IMPORT (E835f2200). ConverterFragment.invokeConverterService -> ConvertIntentService.onCreate@EXPORT (E00705c31, no guard; ConverterFragment is opened from the Misc tab export items, MiscTabFragment.java:291-333). The base-node entries are removed.
  (c) LIFECYCLE onCreate@X -> onHandleIntent@X added (E94b69705 for IMPORT, E2e1b4d56 for EXPORT).
  (d) The 12 automatic onHandleIntent -> converter pairs are suppressed with sup(). Hand CALLs from onHandleIntent@IMPORT to the 7 importer convert methods and from onHandleIntent@EXPORT to the 5 exporter convert methods are all in the build (ConverterFragment and MiscTabFragment sources cited; ConvertIntentService.java:125).
  (e) Follow-up fix. The two notification CALLs (onHandleIntent -> showSuccessNotification and -> showFailureNotification) started at the base node. After the split no route reaches the base node, so the first build reported "method has no path" for both. scratch/r1b_E_fix.py re-points each to both variants (built Ef988cded, E88100cd5, Ebe5a560f, E0a144de9). The build error count then fell to 1.
  (f) TabTxt. TabTxtImporter extends CSVImporter (TabTxtImporter.java:27) and TabTxtExporter extends CSVExporter (TabTxtExporter.java:23). They inherit convert(), so the CSV convert edges cover them. No TabTxt edge is needed (no change made).

Build after Group E (scratch/build_round1b_E.txt): methods 2207, pages 77, edges 4478; verdicts REACHABLE 1959, UNREACHABLE 247, UNRESOLVED 1; errors 1, warnings 0. The one error is expected and is fixed by A1: ERROR method has no path and no UNREACHABLE entry: Oauth2AccountActivity.onDestroy.

## Round 1b, Group A (onDestroy exits and AnyMemo rotation): applied

Scripts: scratch/r1b_A.py (seven replacements, applied once in one atomic apply() call) and scratch/r1b_A_fix.py (one follow-up for Oauth2AccountActivity.onDestroy, see A3). Backup before the group: scratch/graph_def_before_round1b_A.py (the file before r1b_A.py). Builds: scratch/build_round1b_A.txt is the Group A build (after the follow-up): methods 2207, pages 77, edges 4485, REACHABLE 1960, UNREACHABLE 247, errors 0, warnings 0.

Plain explanation: an onDestroy edge means the screen is destroyed. A screen is destroyed only by a real exit (finish(), the Back press, a dialog dismiss) or by the system (a rotation). The graph had direct edges from onCreate straight to onDestroy, and loops that did the same. Each one was replaced by the real exit.

- A1a QACardActivity: applied. The direct onCreate -> onDestroy edge is removed. QACardActivity.java has no finish(). Its onDestroy runs only as super.onDestroy() of its subclasses. CardPlayerActivity (exit: onBackPressed, graph_def.py ~1777) and StudyActivity (exit: dialog cancel, graph_def.py ~1775) reach it through three automatic CALL edges (CardPlayerActivity.java:90, StudyActivity.java:248, PreviewEditActivity.java:183; auto_calls.json). Verdict REACHABLE through the first two. The PreviewEditActivity route stays UNREACHABLE. No UNREACHABLE entry was added, because the class is reached through its subclasses.
- A1b StatisticsScreen: applied. The direct edge is removed. New SYSTEM edge S_STATISTICS -> StatisticsScreen.onDestroy (E353312c7, env ENV_HW_KEY). StatisticsScreen.java has no finish() and no onBackPressed. Its Up/home item only opens the drawer (StatisticsScreen.java:110-112). BaseActivity has no onBackPressed. The default Back press finishes the activity (Activity.java:3001-3010, 5580-5584, 7203-7208). Verdict REACHABLE. Not modelled: with the drawer open, Back closes the drawer first (INFERRED; the drawer library was not read).
- A1c ExportAnyMemoDbFragment: applied. The unguarded onCreate -> onDestroy loop is removed. It is replaced by one LIFECYCLE edge per dismiss() in the source: ExportAnyMemoDbFragment$2.accept (Eafaf9a6d, success, dismiss at :86), ExportAnyMemoDbFragment$3.accept (Ee94fe051, error, dismiss at :93), and ExportAnyMemoDbFragment.onActivityResult (E555c24fc, guarded: request code is the export code and the result is not RESULT_OK with data; dismiss at :99). All REACHABLE. Not modelled: Back or cancel on the picker dialog (the framework cancel path calls dismiss; no app line for it; INFERRED).
- A1d UploadDropboxActivity: applied. onDestroy is removed from the onCreate loop (onStart and onStop stay). New SYSTEM edge S_DROPBOX_UPLOAD -> UploadDropboxActivity.onDestroy (Ee581940c, env ENV_HW_KEY). The source has no finish(): the upload success and cancel paths only dismiss the progress dialog (:106, :116). The default Back press is the exit. Neither the class nor BaseActivity overrides onBackPressed. REACHABLE.
- A1e MiscTabFragment: applied. onDestroy is removed from the S_MAIN_MISC loop; onSaveInstanceState stays. Two real routes are added: FRAMEWORK S_MAIN_MISC -> MiscTabFragment.onDestroy for the Back press on the Misc tab (Ec95fc2fe, same model as RecentListFragment), and LIFECYCLE MiscTabFragment$1.onClick -> MiscTabFragment.onDestroy for OK on the reset dialog, which calls mActivity.finish() at MiscTabFragment.java:361 (Ecbb181b7). REACHABLE.
- A1f Brief lines 1286 and 1477: the current file has no onDestroy loop at those lines. The quoted 'onDestroy' loops were only at the three sites above (1168, 1353, 1551 before this group). The other lc_chain calls make no onDestroy edge (LC_NO_TRIGGER, graph_def.py:75). Nothing changed for them.
- A3 Oauth2AccountActivity.onDestroy (not in the brief's list; this was the one error left after Group E): applied through scratch/r1b_A_fix.py. The real exit is DropboxOauth2AccountActivity.onAuthenticated, which calls finish() (DropboxOauth2AccountActivity.java:29). onDestroy is declared in Oauth2AccountActivity (lines 53-55) and inherited. Added LIFECYCLE DropboxOauth2AccountActivity.onAuthenticated -> Oauth2AccountActivity.onDestroy (E41a7ad8e). REACHABLE. The build error is gone.
- A2 rotation of AnyMemo: applied.
  - Check: AndroidManifest.xml lines 23-46 (the AnyMemo element) have no android:configChanges. The first configChanges in the file is on line 54 (GoogleAccountActivity). A rotation therefore destroys and recreates AnyMemo.
  - Framework: ActivityThread.handleRelaunchActivity (fw_src line 4553) calls handleDestroyActivity (line 4675) and then handleLaunchActivity (line 4699). That is the destroy-and-recreate sequence. Which event the system server sends is INFERRED (its source was not read).
  - New ENV text ENV_RECREATE_ROTATE: 'the device is rotated: AnyMemo is destroyed and recreated because its manifest entry lists no configChanges'. Kind 'hardware' (rotation is a physical movement read by the sensors). Not ENV_ROTATE.
  - Four new SYSTEM edges, one from each main tab: S_MAIN_RECENT, S_MAIN_OPEN, S_MAIN_DOWNLOAD and S_MAIN_MISC -> AnyMemo.onDestroy. Each tab now has a Back edge and a rotation edge to AnyMemo.onDestroy. All REACHABLE.
  - Not modelled: a rotation on the other screens (for example S_STATISTICS). The same rule applies there, but the brief limits A2 to the main tabs.
  - Observation (not changed): graph_def.py:405 (BaseActivity.onConfigurationChanged, ENV_ROTATE) describes a rotation that runs onConfigurationChanged. That is right only for activities that declare configChanges. AnyMemo does not, so onConfigurationChanged does not run for it.

Group A counts: applied 7 (A1a, A1b, A1c, A1d, A1e, A2 with 4 edges and 1 ENV text, and the A3 follow-up). Already applied: none. Skipped: none. Left open: the four round-1 PENDING onDestroy entries (see the final section).

## Round 1b, final: clean build and corrections to the brief's notes

Final build: scratch/build_round1b_final.txt. methods 2207, pages 77, edges 4485, REACHABLE 1960, UNREACHABLE 247, UNRESOLVED 0, errors 0, warnings 0. STRICT True (graph_def.py:39). Before Group A (scratch/build_round1b_E.txt): edges 4478, REACHABLE 1959, UNRESOLVED 1, errors 1. Edge change in Group A: +7 (QACardActivity -1; StatisticsScreen 0; ExportAnyMemoDbFragment +2; UploadDropboxActivity 0; MiscTabFragment +1; Oauth2 +1; rotation +4).

Corrections to the brief's Group B notes (these were wrong or garbled and are corrected here):
(a) The note that "e() does not take gui=" is wrong. build_graph.py:304 accepts gui=, and the Group B edits use it.
(b) The B10 note "(the guards stay in the text)" is wrong. The two SettingsScreen$10.onClick -> S_DLG_TYPEFACE_Q and _A ENTERS edges were deleted, so the guards went with them; no removed edge keeps them.
(c) The line "The CALL -1 is build_graph.py:223 at work" was garbled. The intended reading: the CALL -1 comes from build_graph.py:223 (any hand edge on a base pair suppresses the automatic CALLs on that pair). The new hand CALL CategoryEditorFragment$1.onClick -> QuizLauncherDialogFragment$10.onReceiveCategory suppressed the automatic CALL on the same pair.

Still open (not changed; for the orchestrator):
- The four round-1 PENDING UNREACHABLE onDestroy entries at graph_def.py:1786-1790 (PreviewEditActivity, CardListActivity, CategoryEditorFragment, QuizLauncherDialogFragment) are still labelled PENDING, not final verdicts. They are outside the Group A list, so their finish() and dismiss() sites were not modelled.
- Not modelled in A1 and A2: Back on the export picker dialog; rotation on screens other than the four main tabs.

Builder limits (reported, not fixed; tools/ is read-only in this round):
- build_graph.py:223: any hand edge on a base pair, of any kind, suppresses the automatic CALLs on that pair. sup() (line 218) acts only on automatic CALLs.
- build_graph.py:228: automatic CALLs are copied to every hand-written @variant of the source.
- build_graph.py:350: the endpoint check rejects inherited framework methods (for example Fragment.onCreate), which is why D11 used a fallback.
- "method has no path" errors appear when every route goes through @variants and a base-node edge is left behind (the E17 notification case).

Backups kept in scratch/: graph_def_before_round1b_D.py, graph_def_before_round1b_E.py, graph_def_before_round1b_A.py. Each is the file as it was before its group (the _A backup is before r1b_A.py and r1b_A_fix.py).

Hazard candidates recorded (not graph changes): ui/CardPlayerActivity.java:213 (see the hazard note above). Rotation observation at graph_def.py:405 (see Group A).

Scope check: edits only to graph_def.py and files under scratch/. Every bash command in this window began with the lock touch.
