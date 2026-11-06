# AnkiDroid: convert run notes (schema 2)

Started: 2026-10-27 (overnight convert run, handoff/RESUME_PROMPT_CONVERT.md).

## Setup facts
- final_java_only/AnkiDroid/app/DATASET.txt: app AnkiDroid, package com.ichi2.anki, apk AnkiDroid-debug-2.6beta6-#4200-rebuilt.apk, sha256 e21f15cb108dd7344d39904d0a0b0e05a3e4a9abfa9aba3a1a6ff4740690e91a, min_sdk 10, target_sdk 23. Source commit 58725f6db609b85c01c2a6e026f55c6c357447e1.
- App source root: final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java (package com.ichi2.anki; the api folder next to it is a separate library, not part of this app's source root).
- Flavor: the flavor is not stated in DATASET.txt. Using src/main only.
- method_list.json: 4186 entries (app classes plus library classes packaged in the APK).
- Old schema-1 draft moved to graphs/AnkiDroid/generated_draft_graph_def.py.txt (never built, inventory only).

## Current step
- 2026-11-06 04:30 UTC: Kiro (takeover from Muse), re-audit W3 done for AnkiDroid (no in-app start for any env-gated exported entry; no graph change); next W4 (RTA). Earlier status below.
Status as of 2026-11-02 (Stream A, user order 2026-11-02 ~09:32 EST). Graph after the A1 fixes: methods 4186, pages 49, edges 9608, REACHABLE 3275, UNREACHABLE 911, errors 0, warnings 0. Final-draw route table (seed 20261025, 30 routes, 325 distinct edges): CORRECT 20, WRONG 10, UNCLEAR 0, rate 0.3333; verification.csv regenerated from the final draw (path 30, label 941, edge 232), writer runs with no arguments and reproduces it byte-identically over 2 runs; checks 2 = 274 distinct / 0 problems, 4 = 7033 checked / 0 bad lines, 3 = 0 flagged. Device: ROUTES.csv 30 rows, 28 scripted / 2 unscriptable (routes 02 AnkiWeb account, 26) = 6.7%; drycheck 30 PASS / 0 FAIL in both plain and --load-scripts modes (layout with branch-current harness files); route_info.py find_manifest prefers the LAUNCHER manifest (AnkiDroid/src/main, not api/src/main). Next: fix round on the 10 WRONG routes (a variant fix for each, or a recorded reason a variant cannot express it), then rebuild, redraw, re-judge every changed route, rerun the writer, and update ROUTES.csv and scripts for changed routes. Open, not in the gate: routes 15/17 live-D9 .apkg provisioning; route 25 backup-item tap and backup .apkg (same class); CI SUMMARY + D9 dry-run remain coordinator gates; 5 stale branch files await deletion via the deletion-capable path once the coordinator confirms the run-log listing has landed (route_26.py, route_26b.py, ROUTE_UNSCRIPTABLE_02.md, ROUTE_UNSCRIPTABLE_15.md, ROUTE_UNSCRIPTABLE_25.md).
Superseded 2026-11-02 — previous Current step:
Status as of 2026-10-30 16:20 EDT (overnight labelling run, labelling only). Labelled: build 205 (scratch/build_205.txt), methods 4186, edges 9178, REACHABLE 3275, UNREACHABLE 911, UNRESOLVED 0, errors 0, warnings 0. Build 204 had the same verdict counts. Parts 134 to 150 merged as builds 189 to 204. Route checks not started (out of scope for this run).
Checks on 2026-10-30: all 747 sup pairs in graph_def.py match a bytecode CALL record in auto_calls.json (23 use the receiver-variant form "src@receiver"). Reasons for sup are recorded per block (the "# ---- suppressed" and "# ---- sup for part NNN" headers) and in the build log rows, not per pair.
Open, not in the gate: the build 205 sanity check (never used to set a label) reports 1 contradiction: Card.toString (libanki) is UNREACHABLE (no_trigger_in_app) but ran in a tool run. Read on 2026-10-30: AdvancedStatistics.java:1499 concatenates its own inner class Card (declared at AdvancedStatistics.java:399), not libanki Card. Grep of the source root for "+ card", "valueOf(card)" and "%s, card" found no other implicit conversion, so the origin of the tool hit is not known. Label kept; settle it in the route-check phase. Build 205 also prints 180 "ENV-GATED BUT RAN" lines: sanity output only, not counted as warnings.

## Status at 2026-10-29 03:46 (superseded)
Status as of 2026-10-29 03:46 EDT. Parts 121-129 are merged as builds 170-179, each after C1 (problems 0) and a citation spot-check; premerge warnings were cleared by sup blocks justified in the build log. Build 179: edges 9116, REACHABLE 2606, UNREACHABLE 908, UNRESOLVED 672, errors 694, warnings 0.
Batches 130-133 merged as builds 180-183 (C1 problems 0; citations spot-checked; build 183: REACHABLE 2606, UNRESOLVED 672, warnings 0). Batches 134-139 not launched: they do not reduce UNRESOLVED.

UNRESOLVED diagnosis (2026-10-29 04:10, from out/ankidroid_trigger_graph.json at build 182): 672 methods are UNRESOLVED in 212 classes. The batch labels for 2-125 were not the cause: those methods were labelled REACHABLE, but the graph has no route to them. 654 of the 672 have no REACHABLE caller, and 22 have no caller at all (framework dispatch with no edge: AnkiActivity.onLoadFinished and onLoaderReset, CollectionLoader.onStartLoading and onReset, comparators Sched$1.compare, Template$1.compare, DeckTask$1.compare, Sched$DeckDueTreeNode.compareTo, ServiceConnection callbacks, DB$MyDbErrorHandler.onCorruption, WidgetStatus$UpdateDeckStatusAsyncTask doInBackground and onPostExecute, LinesPoints.<init>, StudyOptionsFragment.onDestroy). Reviewer chain: Reviewer.<init> is REACHABLE (INTENT edges), but AbstractFlashcardViewer.onCreate@Reviewer has no LIFECYCLE edge into it, and S_REVIEWER has no incoming edges, so Reviewer.getContentViewAttr, initControls, onCollectionLoaded and onCreateOptionsMenu have no path. The builder supports hand-written @Context variants (tools/build_graph.py add_auto_edges), so these gaps are missing graph_def.py edges, not a builder limit. Batches 133-139 contain none of the 672 (checked against scratch/batches). Their labels will not reduce UNRESOLVED. Decision 2026-10-29: AnkiDroid is blocked (see "## Blocked"); the run stopped without starting MMEX.
Open: EasySSLSocketFactory.equals and hashCode (INFERRED, OPEN in scratch/conflicts.md); Card.toString contradiction (OPEN); Hooks.runFilter to AdvancedStatistics.runFilter is a suspect automatic pair, not suppressed, to revisit with batches 135-137.

## Status at 02:53 (superseded)
Status as of 2026-10-29 02:53 EDT, 2026-10-29 (overnight convert run, model claude-haiku-5-5, run started 02:50). Merged part 120 as build 169 (premerge build_169_premerge.txt; sup block for part 120 = 23 automatic CALL pairs into the never-constructed XAxisBarGraph and XAxisHistoGram; warnings 0; REACHABLE 2295, UNREACHABLE 813, UNRESOLVED 1078, errors 1100, edges 9195). Batch 122 (helper of 00:09) had written label_122.py and no label_122.md: stuck; partial moved to scratch/stuck/label_122_partial_0015.py. Batch 121 had no output. Relaunched 121, 122, 123, 124 as four LABEL helpers (foreground, one message). Next: C1 check (scratch/c1_check.py), spot-check one citation in five, then scratch/orch_merge.py PART BUILD in plan order: 121 (build 170), 122 (171), 123 (172), 124 (173), then 125 onward. Pending sup: check each build's WARN lines and add one sup block per part (backup graph_def first; build as the same number).

Earlier current step (kept for the record)
Status as of 22:01 EDT, 2026-10-28 (overnight convert run, model claude-haiku-5-5). The runner had hit the session limit at 21:17 and 21:38; this run started after the 9:50pm reset.
- Merged in this run: parts 081 (build 128), 082 (129), 083 (130), 086 (131). Build 131: REACHABLE 2296, UNREACHABLE 403, UNRESOLVED 1487, errors 1508, warnings 0. Merge tool: scratch/orch_merge.py PART BUILD (backup, append, compile(), build, summary).
- Stuck, no output (no helper alive in the session): 084 and 085 (last rows 17:57 and 17:58; partial files moved to scratch/stuck/), 087 (no output). Relaunched at 22:01 with the same batch and MG ranges: 084, 085, 087, 088. Each helper's own STATUS lines are the record.
- 22:22: merged 084 to 089 (builds 132-136), sup block 137, parts 090 and 091 (builds 138-139), sup block 140. Build 140: warnings 0, errors 1459, UNRESOLVED 1438, edges 9568. Running: 092 (Media, MG862-871, started about 22:14; no part file yet at 22:19). Next: merge 092 as build 141 after its DONE line.
- 22:27: 092 DONE, C1 problems 0, citations spot-checked (MediaTest.java:108-110, Media.java:358-363, MediaSyncer.java:235, NoteService.java:175, Media.java:489), merged as build 141 (row 141 in the build log). Running: 093 (Models, MG872-881), 094 (Note, MG882-891), 095 (Sched part 1, MG892-901), 096 (Sched part 2, MG902-911). Next: merge in plan order, 093 as build 142, then 094, 095, 096, then 097 onward.
- 22:42: 095 DONE 22:40 merged as build 144 and 096 DONE 22:41 merged as build 145, both after fixes (see the build-log rows). Lesson for later helpers: reflective edges need cls='non_standard' with a via reflection entry, and evidence strings need the SRC/FW-SRC/INFERRED prefix. Running: 097 (MG912-921), 098 (MG922-931). Next: 097 as build 146, then 098 as build 147.
- 22:40: 093 DONE 22:39 (C1 problems 0, citations spot-checked) merged as build 142; 094 DONE 22:34 (C1 problems 0) merged as build 143 after its Note.contains reason was corrected (the helper said the body was empty; Note.java:222 returns containsKey). Helper 097 (Sched part 3, MG912-921) launched; 095 (MG892-901) and 096 (MG902-911) still running. Next: 095 as build 144, 096 as build 145, 097 as build 146.
- 22:47: 097 DONE 22:44 (C1 problems 0 after one citation fix in newDue, CustomStudyDialog 338/341) merged as build 146 after fixes (see the build-log row). Lesson: a helper's "only caller" claim must be checked against auto_calls.json (removeLrn(long[]) has three callers). Monitor b0oso2unc finished for 097. Running: 098 (MG922-931), 099 (MG932-941), 100 (MG942-951), 101 (Tags, MG952-961, launched 22:48). Next: 098 as build 147, then 099 as 148, 100 as 149, 101 as 150, then 102 onward.
- 22:52: 098 DONE 22:51 (C1 problems 0; setToday and DeckDueTreeNode.toString UNREACHABLE claims checked by grep; citations spot-checked at Sched 2155-2157, 2520-2525, 2554-2557, 774-779, 793) merged as build 147. Running: 099 (Sound, MG932-941), 100 (Stats Storage, MG942-951), 101 (Tags, MG952-961). Next: 099 as build 148, 100 as 149, 101 as 150, then 102 onward.
- 22:54: 100 DONE 22:53 (C1 problems 0; Storage.<init> UNREACHABLE checked: no new Storage, no subclass, no auto CALL record into it; DeckTask.java:790, Storage.java:35-41, Stats.java:852-858 printed). Held until 099 merges as build 148, because plan order puts 100 after 099 (it will be build 149). Lead for readme_notes Hazard candidates: Storage.java:357 holds malformed SQL (not executed by the helper). Launched 101 (Tags, MG952-961, running), 102 (Utils part 1, MG962-971, launched 22:53), 103 (Utils part 2, 4 methods, MG972-981, launched 22:54).
- 23:01: 099 DONE 22:58 (C1 problems 0; three citations spot-checked: Sound.java:319-328, MediaPlayer.java:3235-3240, MediaPlayer.java:3191 and 3203-3205) merged as build 148. 100 DONE 22:53 merged as build 149 (warnings 0). Running: 101 (Tags, MG952-961), 102 (Utils part 1, MG962-971), 103 (Utils part 2, MG972-981). Launched 104 (ZipFile, AdvancedStatistics, ChessFilter, ExternalHookLoader, HebrewFixFilter, Hook, Hooks, Leech; 32 methods, MG982-991). Next: 101 as build 150, 102 as 151, 103 as 152, 104 as 153, then 105 onward.
- 23:04: 101 DONE 23:03 (C1 problems 0; grep confirms the four UNREACHABLE claims) merged as build 150 after three sup pairs (warnings 0). 103 DONE 23:02 (C1 problems 0; citations and the fw_src File.java 404 stub checked) waits for 102 to merge as 151 (plan order). Running: 102 (Utils part 1, MG962-971), 104 (MG982-991). Next: 102 as build 151, then 103 as 152, 104 as 153, then 105 onward. 102 must write the FRAMEWORK edge libanki.Utils.getImportableDecks -> libanki.Utils$1.accept (batch 103 hand-back).
- About 23:06: launched 105 (Importers, MG992-1001) and 106 (TextImporter, FullSyncer, HttpSyncer, MG1002-1011). Helpers running: 102, 104, 105, 106. Merge order is unchanged: 102 (151), 103 (152), 104 (153), 105 (154), 106 (155).
- 104 DONE 23:10 (C1 problems 0; Hooks.runHook dispatch, Hook.runHook empty body, Sched.java:1721-1723, Leech.java:33-38, 46-51 checked; the 18 no_trigger_in_app claims checked against auto_calls.json, which has no caller from a live source). Needs one sup pair at merge: ('Hooks.runHook', 'Hook.runHook') (exact auto CALL, Hooks.java:121). Waits for 102 and 103 to merge as 151 and 152, then 104 as build 153.
- 23:21: 102 merged as build 151 (after the libanki.Utils name fix and sup151), 103 as build 152, 104 as build 153 (after sup153), 105 as build 154 (after sup154; 105 DONE 23:14, C1 problems 0, five citations spot-checked). Build 154: REACHABLE 2301, UNREACHABLE 516, UNRESOLVED 1369, errors 1390, warnings 1 (NoteImporter.<init>, waits for batch 106). Running: 106 (TextImporter, FullSyncer, HttpSyncer, MG1002-1011). Next: 106 as build 155, then 107-139 in plan.tsv order.
- 23:45: 106 DONE 23:25 (C1 problems 0; citations spot-checked at TextImporter.java:14-25, HttpSyncer.java:114-124 and 239, FullSyncer.java:159, Connection.java:199-202, 318-322, 337, DeckPicker.java:1452) merged as build 155 after sup155. Batches 107 (MediaSyncer, RemoteMediaServer, RemoteServer, MG1012-1021), 108 (Syncer, Template, MG1022-1031), 109 (Atom classes, MG1032-1041) and 110 (Expression and Term classes, MG1042-1051) launched in background. Next: merge in plan order, 107 as build 156.
- 23:40: 110 DONE 23:37 (C1 problems 0; citations spot-checked at Pow.java:45, 61, 85, Factor.java:77 and TopLevelParser.java:165) merged as build 159. Its 74 warnings were all automatic CALL pairs inside the parser tree, fixed by sup159 (214 pairs; warnings 0). Running: 111 (MG1052-1061), 112 (MG1062-1071), 113 (MG1072-1081), 114 (MG1082-1091). Next: 115-139 in plan order.
- 23:58: 112 merged as build 163 (C1 problems 0). Before its sup it had 35 warnings; sup163 (19 pairs) leaves 23, all with PlotSheet or ReliefDrawer sources. 117 DONE 23:55 (C1 problems 0; grep finds no new PointDrawer2D, RelativeColorGradient or ReliefDrawer in the java root) merged as build 164 after sup164 (3 pairs; 29 warnings). Running: 115, 116, 118 (ReliefDrawer, MG1122-1131) and 119 (XAxis, MG1132-1141). Next: merge 115 and 116 (builds 165, 166), then 118 and 119 in plan.tsv order. Pending sup: (makeGradient, delta) and the ReliefDrawer constructor pairs, after 118 merges.
- 00:01: 116 DONE 00:01 (C1 problems 0; citations spot-checked at PlotSheet.java:40, 43, 172-175, 313, 692-697, XAxis.java:192-193, YAxis.java:179-180) merged as build 165 (warnings 35).
- 00:05: 118 DONE 00:01 (C1 problems 0; grep: no new ReliefDrawer(, no subclass, no new RelativeColorGradient; ReliefDrawer.java:132 and 179 call makeGradient, 474 builds ReliefLegend) merged as build 166 (warnings 57).
- 00:05: 119 DONE 00:03 (C1 problems 0; XAxis.markOnDownside is true by default (XAxis.java:120), but ChartBuilder.java:280 calls setOnFrame before paint and unsetOnFrame has no caller) merged as build 167 (warnings 60).
- 00:09: sup167 applied (31 pairs; build 167 rebuilt; warnings 60 to 39, all PlotSheet-sourced). 120 (XAxisBarGraph, XAxisHistoGram), 121 (XGrid), 122 (YAxis) launched. 115 still running (label_115.md RUNNING 00:00, no label_115.py yet).
- 00:13: 115 DONE 00:08 merged as build 168. Guard check for ticsCalcX and ticsCalcY: XAxis.java:143 and 155 (double and float constructors), XAxis.java:160 sets isAutoTic in the float constructor only; YAxis.java:131 and 144, set at 149; XGrid.java:92 and 105 (double), 117 and 130 (int), set at 122 and 136; YGrid.java:91 and 105 (double), 118 and 132 (int), set at 123 and 138; ChartBuilder.java:279, 315, 317, 342, 343 all pass double tick values, so they use the double constructors, which do not set isAutoTic. Builds: 168 had 49 warnings (new ones from batch 115 targets); sup168 leaves 0. Batches 120 (RUNNING 00:07), 121 and 122 (launched 00:09) still running.
- Next: when a helper ends with STATUS DONE: c1_check, spot-check one citation in five with sed -n, then orch_merge.py with the next build number (132 onward). Then batches 089 to 139 in plan.tsv order, at most 4 helpers at a time, 30-minute stuck rule.
- Hazard lead (part 090): Finder._findDupes (Finder.java:762-767) calls split(",", 1), which returns one element, so the length check always returns null and lines 768-786 never run. The row stays REACHABLE (the method is entered). Record it under "Hazard candidates" in readme_notes.md at the readme step.
- Syncer.start(int,boolean,JSONObject) (Syncer.java:622): part 084 reports no caller in the source root. The Syncer batch must label it (UNREACHABLE if no caller is found there).
- Card.<clinit> open item (part 081) settled at 22:15: the row cites the automatic CALL edges in auto_calls.json (see Open items).

## Earlier current step
Status as of 17:54 EDT (date): merged 076 (builds 120-121), 077 (122-123), 079 (124-125) and 080 (126-127); build 127 has UNRESOLVED 1495, errors 1516, warnings 0. Checked and waiting in plan order: 082 (behind 081), 083 (behind 081). Helpers running: 081 (a46733e77c1647290, MG752-761), 084 (a1c4924a718e4d18b, MG782-791), 085 (aebdaa063a26d47c0, MG792-801), 086 (MG802-811). Merge each part only after its DONE line and c1_check problems 0. Next: 081, then 082, 083, then 084 onward per scratch/batches/plan.tsv. Checked and waiting: 086 (Consts DB, 4 UNREACHABLE/REACHABLE rows, C1 problems 0). Helper 087 (a3f6d723e88e327b0, MG812-821) running. Pending for batch 131 (DB.<init> is in it, not yet labelled): write e('DB.<init>', 'DB$MyDbErrorHandler.onCorruption', 'FRAMEWORK', ...) with MISSING GATE MG802 (collection file damaged, SQLite calls DatabaseErrorHandler.onCorruption); the 086 part writes no edge for it.

Run 10 (2026-10-28 17:00 EDT, overnight convert run). At 16:59 there were no output files for batches 068-071 and no helper process, so they are relaunched with the same MG ranges (068 MG622-631, 069 MG632-641, 070 MG642-651, 071 MG652-661). Each helper writes parts/label_0NN.md and .py; each part is merged only after its C1 check (c1_check.py prints problems 0) and a spot-check. Part 071 merged as build 108 (C1 problems 0, spot-checks on DeckTask.java:1493-1495, 1538-1540; DeckPicker.java:704-709; IntentHandler.java:158-160; FW AsyncTask.java:594-596 matched). Parts 068 (builds 110 and 111, with three sup pairs) and 069 (build 109) are merged. Part 070 merged as build 112 (DeckTask part 2; C1 problems 0; warnings 0; errors 1642). Part 072 merged as build 113 (CompatHelper and CompatV10..V17; 15 warnings from 25 automatic CALL edges into UNREACHABLE CompatV10 base bodies), then the sup block for part 072 as build 114 (25 pairs; warnings 0; errors 1629; UNRESOLVED 1608). The sup pairs are justified by CompatHelper.java:35-36 (API 27 selects CompatV21) and the overrides in CompatV11..V21, which were checked by grep; supportAddContentMenu is closed by the DeckPicker fallback (DeckPicker.java:391-404). Part 074 merged as build 115 (C1 problems 0; warnings 0; errors 1616; UNRESOLVED 1595). Part 075 merged as build 116 (C1 problems 0; warnings 0; errors 1602; UNRESOLVED 1581). Open lead from 075 (not a label error): methods.csv gives SeekBarPreference.getValue the route SettingsFragment.onResume, which is wrong (onResume at Preferences.java:799-801 passes only three other keys). The real route is initAllPreferences (374) -> initPreference (398, ends with updateSummary at 445) -> updateSummary (588) -> getValue (614-615). The label stands; the methods.csv route is not used to decide labels. Part 073 merged as build 117 (17 e() calls, 4 UNREACHABLE; warnings 0). Part 078 merged as build 118 (3 UNREACHABLE; one warning on Base64$OutputStream.write(int)), with the sup pair as build 119 (warnings 0; errors 1581; UNRESOLVED 1560). Running at 17:38: batches 076 (MG702-711), 077 (MG712-721, Base64 and 39 more), 079 (MG732-741, BitmapUtil and 36 more) and 080 (MG742-751, MethodLogger and 32 more). Next: merge 076, 077, 079 and 080 in order, each after its C1 check, spot-check, backup, append and build (builds 115 onward), then batches 076-139 in plan.tsv order. Pending cross-batch edges from 072: ReadText.java:195 to CompatV15.setTtsOnUtteranceProgressListener (ReadText batch); DiffEngine.java:1100-1108 to CompatV16.detagged (DiffEngine batch). Decisions are in HANDOFF_V2 "Convert run decisions" (run 10 entries).

Run 9 (2026-10-28 about 14:15 EDT). Merged: 001-067 (060 with three sup pairs for FieldBase.getThisModified; 061 with 25 sup pairs; 062 with a four-edge Gson addendum; the two invalid edges from build 098 fixed in build 099; 063 with two sup pairs and one e() edge removed, build 103; 067 with the FabBehavior constructor edge cls non_standard). Build 107: 0 warnings, REACHABLE 2121, UNREACHABLE 268, UNRESOLVED 1797, edges 9610. Exit 1 is expected: UNRESOLVED and the unentered-page errors remain.
Running: batches 068-071 (helpers launched about 14:20 as background agents; 068 = MG622-631 BaseAsyncTask, CollectionLoader, Connection; 069 = MG632-641 DeckTask part 1; 070 = MG642-651 DeckTask part 2; 071 = MG652-661 DeckTask part 3). Merge each only after its C1 check and its STATUS: DONE line. Done and merged: 054-067.
Not started: batches 067-126 in plan order, then gap batches 127-139. MG range rule: batch N uses MG (132 + 10*(N-19)) to +9.
Open lead (page entries, updated 13:58): the 12 REACHABLE rows of batch 062 and the startTranslationWithGlosbe chain are UNRESOLVED because S_MULTIMEDIA_EDIT_FIELD has no ENTERS edge. NoteEditor.startMultimediaFieldEditor is REACHABLE and starts MultimediaEditFieldActivity.<init> through an INTENT (graph_def.py ~2140); S_TRANSLATION likewise has no ENTERS owner, though its INTENT (BasicTextFieldController.startTranslationWithGlosbe -> TranslationActivity.<init>) is written. The ENTERS convention was used once: S_DLG_CUSTOM_STUDY from StudyOptionsFragment.showCustomStudyContextMenu (build 099). The other unentered pages need a decision at the route check. Convention: e(<starter method>, S_PAGE, ENTERS, ...), as with DeckPicker.addNote -> S_NOTEEDITOR.
Open leads: FieldBase.getThisModified is closed (batch 060, build 101). S_STUDYOPTIONS_FRAG -> Reviewer.<init> and AbstractFlashcardViewer.playVideo -> VideoPlayer.<init> were added as method-level addenda (end of graph_def.py) in build 061. The rename lead is closed: DeckPicker.renameDeckDialog(long) has a path through the automatic CALL at StudyOptionsFragment.java:329; the no-arg renameDeckDialog() waits for batch 042. Still no path: playVideo and VideoPlayer.<init> (waiting for batch 099, Sound.playSound -> playVideo). Batch 050 lead, not changed: the auto_calls record for Utils.java:881 names AnkiFont.<clinit>, not createAnkiFont; createAnkiFont is still reached through the automatic CALL at Utils.java:892.

## Last command
python3 -I tools/build_graph.py graphs/AnkiDroid ankidroid > graphs/AnkiDroid/scratch/build_107.txt 2>&1 (after merging part 067; warnings 0; exit 1 expected while UNRESOLVED and the unentered-page errors remain). Before that: build_106 (part 066, warnings 0), build_105 (part 065, warnings 0), build_104 (part 064, warnings 0), build_103 (after removing the e() edge LanguagesLister.getLanguages -> LanguagesLister$1.compare and the sup for part 063, 2 pairs; warnings 0). Before that: build_102 (part 063 merged, 3 warnings), build_101 (sup for part 060, 3 pairs; warnings 0). Before that: build_100 (part 060 merged, 1 warning on FieldBase.getThisModified incoming CALLs), build_099 (fixes for E27a0753e and E6e7e03cd, warnings 0), build_098 (part 062 with the Gson addendum, warnings 0), build_097 (sup for part 061, 25 pairs, warnings 0), build_096 (part 061 merged, 12 warnings). graph_def.py backups at scratch/graph_def_before_part060.py, _before_part062.py, and earlier ones.
Before that: build_087 (sup for part 055, five pairs, warnings 0), build_086 (part 055 merged, 4 warnings), build_085 (part 057, warnings 0), build_084 (sup for part 051, seven pairs, warnings 0), build_082 (part 051 merge, 7 warnings), build_081 (part 050, warnings 0), build_080 (sup for part 052, warnings 0), build_079 (part 052, 2 warnings, resolved as recorded in HANDOFF_V2); graph_def.py backups at scratch/graph_def_before_part050.py, _before_part051.py, _before_sup051.py, _before_part053.py, _before_sup052.py, _before_part052.py.

## Next command
Wait for each helper completion notice. For each: python3 -I graphs/AnkiDroid/scratch/c1_check.py graphs/AnkiDroid/parts/label_0NN.py graphs/AnkiDroid/parts/label_0NN.md (must print problems 0; if not, fix the rows and re-run, and record the fix in HANDOFF_V2); compile() check on the .py (no py_compile); spot-check one citation in five with sed -n; back up graph_def.py to scratch/graph_def_before_part0NN.py; append "# ---- part 0NN (date)" and the .py text to graph_def.py; build with python3 -I tools/build_graph.py graphs/AnkiDroid ankidroid > graphs/AnkiDroid/scratch/build_0NN.txt 2>&1; add sup() only if a warning names an UNREACHABLE method with an automatic CALL edge.

## Build log

| Build | Edges | REACHABLE | UNREACHABLE | UNRESOLVED | Warnings |
|---|---|---|---|---|---|
| 001 | 8982 | 422 | 0 | 3764 | 0 |
| 002 | 8986 | 426 | 8 | 3752 | 2 |
| 003 | 8992 | 426 | 15 | 3745 | 9 |
| 004 | 8982 | 426 | 15 | 3745 | 2 |
| 005 | 8997 | 426 | 15 | 3745 | 2 |
| 006 | 9000 | 647 | 15 | 3524 | 2 |
| 007 | 8999 | 646 | 20 | 3520 | 2 |
| 008 | 9010 | 646 | 29 | 3511 | 11 |
| 009 | 8998 | 646 | 29 | 3511 | 2 |
| 010 | 9001 | 646 | 29 | 3511 | 2 |
| 011 | 9061 | 838 | 30 | 3318 | 3 |
| 012 | 9050 | 838 | 30 | 3318 | 0 |
| 013 | 9059 | 840 | 32 | 3314 | 1 |
| 014 | 9058 | 840 | 32 | 3314 | 0 |
| 015 | 9068 | 986 | 32 | 3168 | 0 |
| 016 | 9092 | 1012 | 32 | 3142 | 0 |
| 017 | 9112 | 1084 | 32 | 3070 | 0 |
| 018 | 9130 | 1095 | 37 | 3054 | 3 |
| 019 | 9127 | 1095 | 37 | 3054 | 0 |
| 020 | 9135 | 1155 | 39 | 2992 | 0 |
| 021 | 9162 | 1208 | 41 | 2937 | 0 |
| 022 | 9166 | 1212 | 41 | 2933 | 0 |
| 023 | 9182 | 1315 | 41 | 2830 | 0 |
| 024 | 9212 | 1403 | 43 | 2740 | 1 |
| 025 | 9211 | 1403 | 43 | 2740 | 0 |
| 026 | 9220 | 1410 | 43 | 2733 | 0 |
| 027 | 9228 | 1415 | 44 | 2727 | 0 |
| 028 | 9244 | 1423 | 48 | 2715 | 1 |
| 029 | 9243 | 1423 | 48 | 2715 | 0 |
| 030 | 9254 | 1622 | 49 | 2515 | 1 |
| 031 | 9252 | 1622 | 49 | 2515 | 0 |
| 032 | 9257 | 1621 | 51 | 2514 | 2 |
| 033 | 9251 | 1621 | 51 | 2514 | 0 |
| 034 | 9283 | 1621 | 52 | 2513 | 1 |
| 035 | 9282 | 1621 | 52 | 2513 | 0 |
| 036 | 9293 | 1621 | 54 | 2511 | 2 |
| 037 | 9291 | 1621 | 54 | 2511 | 0 |
| 038 | 9302 | 1624 | 54 | 2508 | 0 |
| 039 | 9302 | 1624 | 54 | 2508 | 0 |
| 040 | 9310 | 1624 | 56 | 2506 | 2 |
| 041 | 9307 | 1624 | 56 | 2506 | 0 |
| 042 | 9307 | 1624 | 61 | 2501 | 2 |
| 043 | 9305 | 1624 | 61 | 2501 | 0 |
| 044 | 9310 | 1632 | 61 | 2493 | 0 |
| 045 | 9311 | 1632 | 65 | 2489 | 0 |
| 046 | 9332 | 1649 | 75 | 2462 | 0 |
| 047 | 9351 | 1668 | 83 | 2435 | 1 |
| 048 | 9350 | 1668 | 83 | 2435 | 0 |
| 049 | 9355 | 1679 | 84 | 2423 | 0 |
| 050 | 9356 | 1680 | 84 | 2422 | 0 |
| 051 | 9372 | 1719 | 88 | 2379 | 0 |
| 052 | 9372 | 1719 | 88 | 2379 | 0 |
| 053 | 9382 | 1735 | 90 | 2361 | 0 |
| 054 | 9389 | 1735 | 92 | 2359 | 1 (MyAccount.logout incoming edge) |
| 055 | 9388 | 1735 | 92 | 2359 | 0 (sup MyAccount$4.onClick -> MyAccount.logout) |
| 056 | 9411 | 1744 | 92 | 2350 | 0 (part 033) |
| 057 | 9419 | 1782 | 97 | 2307 | 4 (part 038 merged; warnings: automatic CALL edges into 4 UNREACHABLE methods of StudyOptionsFragment) |
| 058 | 9414 | 1782 | 97 | 2307 | 0 (sup for part 038, 5 automatic edges removed) |
| 059 | 9426 | 1793 | 97 | 2296 | 0 (part 039; 12 EDGE rows and 4 citations fixed by the orchestrator) |
| 060 | 9448 | 1807 | 97 | 2282 | 0 (part 036; kinds added to 22 EDGE item cells, one reason cell with | characters fixed) |
| 061 | 9450 | 1807 | 97 | 2282 | 0 (addenda: StudyOptionsFragment.openReviewer -> Reviewer.<init>, AbstractFlashcardViewer.playVideo -> VideoPlayer.<init>; playVideo and VideoPlayer.<init> still have no path until batch 099 (Sound) is merged) |
| 062 | 9472 | 1836 | 100 | 2250 | 0 (part 037, Statistics; 22 EDGE item cells given their kinds and 8 bare Statistics.java citations qualified before the merge) |
| 063 | 9481 | 1864 | 102 | 2220 | 2 (part 040 merged; automatic CALL edges DeckTask.onCancelled and DeckTask$TaskListener.onProgressUpdate into CustomStudyDialog$4 UNREACHABLE methods) |
| 064 | 9478 | 1864 | 102 | 2220 | 0 (sup for part 040: the three automatic edges above suppressed) |
| 065 | 9487 | 1866 | 102 | 2218 | 0 (part 042; DeckPicker dialogs and context menu listeners; no sup needed) |
| 066 | 9498 | 1884 | 106 | 2196 | 1 (part 041; automatic CALL DatabaseErrorDialog.onCreateDialog -> DatabaseErrorDialog$2.<init>, UNREACHABLE branch_never_taken) |
| 067 | 9497 | 1884 | 106 | 2196 | 0 (sup for part 041: the one pair above suppressed) |
| 068 | 9514 | 1893 | 108 | 2185 | 2 (part 025, CardTemplateEditor part 1; automatic CALL DeckTask.onCancelled and DeckTask$TaskListener.onProgressUpdate into CardTemplateEditor$1 UNREACHABLE methods) |
| 069 | 9511 | 1893 | 108 | 2185 | 0 (sup for part 025: the three automatic edges above suppressed) |
| 070 | 9522 | 1904 | 108 | 2174 | 0 (part 043, ExportDialog and ImportDialog; no UNREACHABLE, no sup needed) |
| 071 | 9533 | 1903 | 111 | 2172 | 1 (part 045, SyncErrorDialog; automatic CALL SyncErrorDialog.onCreateDialog -> SyncErrorDialog$2.<init> into an UNREACHABLE constructor) |
| 072 | 9532 | 1903 | 111 | 2172 | 0 (sup for part 045: the pair above suppressed) |
| 073 | 9539 | 1911 | 111 | 2164 | 0 (part 044, MediaCheckDialog, ModelBrowserContextMenu, ModelEditorContextMenu, NoteEditorRescheduleCard, SimpleMessageDialog; no UNREACHABLE, no sup needed) |
| 074 | 9555 | 1932 | 111 | 2143 | 0 (part 046, TagsDialog; no UNREACHABLE, no sup needed) |
| 075 | 9562 | 1927 | 121 | 2138 | 6 (part 048, MultimediaEditFieldActivity and PickStringDialogFragment; automatic CALL warnings into the closed createSpareMenu, gtxt and the listener constructors) |
| 076 | 9556 | 1927 | 121 | 2138 | 0 (sup for part 048: six pairs) |
| 077 | 9566 | 1927 | 122 | 2137 | 0 (part 047, LoadPronounciationActivity; no sup needed) |
| 078 | 9576 | 1927 | 126 | 2133 | 0 (part 049, TranslationActivity, NotificationService, KeepAliveService; no sup needed) |
| 079 | 9578 | 1928 | 142 | 2116 | 2 (part 052, FieldEditText, FlashCardsContract, Lookup, Manifest; E585bcb29 warning and Ea402ca03 review hint, both resolved in 080 and by reclassification) |
| 080 | 9577 | 1928 | 142 | 2116 | 0 (sup for part 052: one pair) |
| 081 | 9584 | 1934 | 147 | 2105 | 0 (part 050, AppCompatPreferenceActivity and AnkiFont; no sup needed) |
| 082 | 9585 | 1937 | 162 | 2087 | 7 (part 051, BackupManager, CollectionHelper, CustomExceptionHandler; automatic CALLs inside CustomExceptionHandler) |
| 083 | 9578 | 1937 | 162 | 2087 | 0 (sup for part 051: seven pairs) |
| 084 | 9581 | 1937 | 169 | 2080 | 0 (part 053, MetaDB and ReadText; no sup needed) |
| 085 | 9585 | 1937 | 172 | 2077 | 0 (part 057, AudioView and BeolingusParser; no sup needed) |
| 086 | 9610 | 1990 | 176 | 2020 | 4 (part 055, AddContentApi; CHA and guarded CALLs into CompatV1 and hasReadWritePermission) |
| 087 | 9605 | 1990 | 176 | 2020 | 0 (sup for part 055: five pairs) |
| 088 | 9606 | 1990 | 179 | 2017 | 2 (part 054, UIUtils and Whiteboard; DeckTask.onCancelled and DeckTask$TaskListener.onProgressUpdate into UIUtils$1 UNREACHABLE targets) |
| 089 | 9604 | 1990 | 179 | 2017 | 1 (sup for part 054: two pairs; left the receiver-variant src DeckTask$TaskListener.onProgressUpdate@UIUtils$1 from auto_calls.json) |
| 090 | 9603 | 1990 | 179 | 2017 | 0 (sup for part 054: third pair for the receiver-variant src) |
| 091 | 9609 | 1990 | 179 | 2017 | 0 (part 059, BasicImageFieldController and its listeners; 7 of its methods wait for the S_MULTIMEDIA_EDIT_FIELD page entry) |
| 092 | 9610 | 1990 | 190 | 2006 | 1 (part 056, the api-library and crash-dialog rows; warning: automatic CALL AnkiDroidCrashReportDialog.onCreate -> buildCustomView) |
| 093 | 9609 | 1990 | 190 | 2006 | 0 (sup for part 056: AnkiDroidCrashReportDialog.onCreate -> buildCustomView, both closed) |
| 094 | 9612 | 1985 | 200 | 2001 | 5 (part 058, AudioField and BasicAudioFieldController; warnings: UNREACHABLE AudioField getImagePath, getText, isModified, setImagePath, setText, each with IField call-site CALL edges) |
| 095 | 9601 | 1985 | 200 | 2001 | 0 (sup for part 058: 11 pairs, call sites guarded by type or by controller type) |
| 096 | 9601 | 1974 | 221 | 1991 | 12 (part 061, ImageField and TextField; automatic CALL/CHA edges into the isModified UNREACHABLE methods, all checked as type-guarded or new-object callers) |
| 097 | 9576 | 1973 | 221 | 1992 | 0 (sup for part 061: 25 pairs; one error left: no path for FieldBase.getThisModified) |
| 098 | 9580 | 1973 | 239 | 1974 | 0 (part 062 with the four-edge Gson addendum; 18 UNREACHABLE; the 12 REACHABLE rows stay UNRESOLVED until S_TRANSLATION is entered) |
| 099 | 9580 | 1973 | 239 | 1974 | 0 (fixes: E27a0753e page-to-page GUI replaced by an ENTERS edge from showCustomStudyContextMenu; E6e7e03cd evidence label) |
| 100 | 9591 | 1973 | 240 | 1973 | 1 (part 060; warning: three automatic CALL edges into FieldBase.getThisModified, UNREACHABLE now) |
| 101 | 9588 | 1973 | 240 | 1973 | 0 (sup for part 060: 3 pairs) |
| 102 | 9590 | 1973 | 256 | 1957 | 3 (part 063; warnings on LanguagesLister$1.<init>, LanguagesLister$1.compare, MultimediaEditableNote.getModelId) |
| 103 | 9587 | 1973 | 256 | 1957 | 0 (sup for part 063: 2 pairs; e() edge LanguagesLister.getLanguages -> LanguagesLister$1.compare removed, since sup() does not apply to e() edges) |
| 104 | 9587 | 1973 | 259 | 1954 | 0 (part 064: 3 UNREACHABLE; 3 REACHABLE rows stay UNRESOLVED until callers are reached) |
| 105 | 9593 | 2107 | 260 | 1819 | 0 (part 065: 6 ASYNC edges; REACHABLE +134) |
| 106 | 9596 | 2107 | 262 | 1817 | 0 (part 066: 3 FRAMEWORK edges from S_STATISTICS; 2 UNREACHABLE ChartView constructors) |
| 107 | 9610 | 2121 | 268 | 1797 | 0 (part 067: 14 edges from S_DECKPICKER, S_STATISTICS, S_CARDBROWSER; 6 UNREACHABLE; FabBehavior constructor edge cls non_standard) |
| 108 | 9610 | 2121 | 270 | 1795 | 0 (part 071, DeckTask.TaskData: getType and setCards UNREACHABLE no_trigger_in_app; no edges, no sup; C1 problems 0; errors 1816) |
| 109 | 9620 | 2121 | 270 | 1795 | 0 (part 069, DeckTask part 1: 40 REACHABLE, 10 ASYNC edges; C1 problems 0; spot-checks DeckTask.java:601, 1348-1350; FW AsyncTask.java:691-695; errors 1816) |
| 110 | 9629 | 2279 | 276 | 1631 | 1 (part 068, BaseAsyncTask, CollectionLoader, Connection; warning: auto CALLs HttpSyncer.req -> Connection$CancelCallback.setConnectionManager) |
| 111 | 9626 | 2279 | 276 | 1631 | 0 (sup for part 068: three pairs, the req variants plain, @FullSyncer, @RemoteMediaServer; errors 1652) |
| 112 | 9627 | 2279 | 286 | 1621 | 0 (part 070, DeckTask part 2: 30 REACHABLE, 10 UNREACHABLE no_trigger_in_app, 1 ASYNC edge; C1 problems 0; spot-checks DeckTask.java:1335-1337, 1376-1380, 1496-1499; DeckPicker.java:2067; FW AsyncTask.java:684-689; errors 1642) |
| 113 | 9630 | 2273 | 305 | 1608 | 15 (part 072, CompatHelper and CompatV10..V17 members; 25 automatic CALL edges into UNREACHABLE CompatV10 base bodies; errors 1629) |
| 114 | 9605 | 2273 | 305 | 1608 | 0 (sup for part 072: 25 pairs, the CompatV10 base bodies shadowed on API 27 by CompatV11..V21 overrides, and supportAddContentMenu closed by the DeckPicker fallback; errors 1629) |
| 115 | 9611 | 2274 | 317 | 1595 | 0 (part 074, StepsPreference, HtmlColors, StyledProgressDialog, Themes, DividerItemDecoration; 6 e() edges; 12 UNREACHABLE; C1 problems 0; spot-checks DeckOptions.java:523, FilteredDeckOptions.java:369-378, FW DialogPreference.java:390-395; errors 1616) |
| 116 | 9632 | 2282 | 323 | 1581 | 0 (part 075, SeekBarPreference and SlidingTabLayout; 21 e() edges; 6 UNREACHABLE; C1 problems 0; spot-checks Preferences.java:374-392, 443-446, 512-517, 612-616, 797-812; errors 1602) |
| 117 | 9648 | 2296 | 327 | 1563 | 0 (part 073, CompatV19 listeners, CustomDialogPreference, NumberRangePreference, CustomTabActivityHelper.onServiceConnected; 17 e() calls, 16 new edges (one matched an existing edge); 4 UNREACHABLE; C1 problems 0; spot-checks CustomTabsHelper.java:47, 144-146, NumberRangePreference.java:50-55, Preferences.java:241-244; errors 1584) |
| 118 | 9648 | 2296 | 330 | 1560 | 1 (part 078, Base64.OutputStream: 3 UNREACHABLE, 0 e() edges; warning: write(byte[],int,int) -> write(int) at Base64.java:1814 into an UNREACHABLE method; errors 1581) |
| 119 | 9647 | 2296 | 330 | 1560 | 0 (sup for part 078: write(byte[],int,int) is UNREACHABLE, so its loop call cannot reach write(int); errors 1581) |
| 120 | 9649 | 2296 | 335 | 1555 | 4 (part 076, SlidingTabStrip and Upgrade: 11 REACHABLE, 5 UNREACHABLE, 2 e() edges from S_STATISTICS and S_CARDTEMPLATEEDITOR to SlidingTabStrip.onDraw; C1 problems 0; warnings: 4 automatic CALL edges into UNREACHABLE methods; errors 1576) |
| 121 | 9645 | 2296 | 335 | 1555 | 0 (sup for part 076: blendColors, setCustomTabColorizer, setDividerColors, setSelectedIndicatorColors; errors 1576) |
| 122 | 9645 | 2296 | 375 | 1515 | 21 (part 077, Base64 class with nested InputStream, OutputStream and Base64$1: 40 UNREACHABLE, 0 e() edges; warnings: 50 automatic CALL edges between UNREACHABLE Base64 methods; errors 1536) |
| 123 | 9595 | 2296 | 375 | 1515 | 0 (sup for part 077: the 50 pairs, each source and destination UNREACHABLE; errors 1536) |
| 124 | 9595 | 2296 | 383 | 1507 | 1 (part 079, BitmapUtil, ExifUtil, HttpUtility, LanguageUtil, DiffEngine.DiffAction: 30 REACHABLE, 8 UNREACHABLE, 0 e() edges; C1 problems 0; warning: automatic CALL Utils.fmtPercentage(Double,int) -> LanguageUtil.getLocale; errors 1528) |
| 125 | 9594 | 2296 | 383 | 1507 | 0 (sup for part 079: fmtPercentage(Double,int) has no caller, so its call to getLocale is on no route; errors 1528) |
| 126 | 9596 | 2296 | 395 | 1495 | 2 (part 080, MethodLogger, Threads, VersionUtils, WidgetStatus, AnkiExporter/APKG: 22 REACHABLE, 12 UNREACHABLE, 2 INTENT e() edges; C1 problems 0; warnings: automatic CALL edges into MethodLogger.logInternal and Threads$SingleThreadChecker.<init>; errors 1516) |
| 127 | 9591 | 2296 | 395 | 1495 | 0 (sup for part 080: 5 pairs, every source UNREACHABLE; errors 1516) |
| 128 | 9591 | 2296 | 396 | 1494 | 0 (part 081, Card part 1: 1 UNREACHABLE Card.getCol; 39 REACHABLE rows wait for a route; C1 problems 0; errors 1515) |
| 129 | 9591 | 2296 | 399 | 1491 | 0 (part 082, Card part 2: 3 UNREACHABLE; C1 problems 0; errors 1512) |
| 130 | 9591 | 2296 | 401 | 1489 | 0 (part 083, CardStats: 2 UNREACHABLE; C1 problems 0; errors 1510) |
| 131 | 9591 | 2296 | 403 | 1487 | 0 (part 086, Consts and DB: 2 UNREACHABLE; C1 problems 0; errors 1508) |
| 132 | 9591 | 2296 | 416 | 1474 | 2 (part 084, Collection part 1: 27 REACHABLE, 13 UNREACHABLE, 0 e(); C1 problems 0; warnings: auto CALL edges into the Collection constructors and _qaData(String); errors 1495) |
| 133 | 9591 | 2296 | 426 | 1464 | 5 (part 085, Collection part 2: 23 REACHABLE, 10 UNREACHABLE, 0 e(); C1 problems 0; errors 1485) |
| 134 | 9592 | 2297 | 437 | 1452 | 9 (part 087, Decks part 1: 29 REACHABLE, 11 UNREACHABLE; orchestrator edge Decks.allSorted -> Decks$1.compare (CALL, MG812); C1 problems 0; errors 1473) |
| 135 | 9592 | 2297 | 438 | 1451 | 9 (part 088, Decks part 2: 9 REACHABLE, 1 UNREACHABLE; the 088 row kind changed to CALL; errors 1472) |
| 136 | 9592 | 2297 | 439 | 1450 | 9 (part 089, Exporter: 1 REACHABLE, 1 UNREACHABLE; C1 problems 0; errors 1471) |
| 137 | 9581 | 2297 | 439 | 1450 | 0 (orchestrator sup block at the end of graph_def.py: 11 pairs for the 9 warned methods, each source UNREACHABLE or the three-argument constructor with no caller; backup scratch/graph_def_before_sup136.py; errors 1471) |
| 138 | 9581 | 2297 | 451 | 1438 | 8 (part 090, Finder part 1: 28 REACHABLE, 12 UNREACHABLE, 0 e(); C1 problems 0; errors 1459) |
| 139 | 9581 | 2297 | 451 | 1438 | 8 (part 091, Finder part 2: 3 REACHABLE, 0 UNREACHABLE; C1 problems 0; same warnings as 138) |
| 140 | 9568 | 2297 | 451 | 1438 | 0 (orchestrator sup block at the end of graph_def.py: 13 pairs for the 8 warned Finder methods; every caller UNREACHABLE; backup scratch/graph_def_before_sup139.py; errors 1459) |
| 141 | 9568 | 2297 | 452 | 1437 | 0 (part 092, Media, 37 rows: 36 REACHABLE by CALL, Media.strip UNREACHABLE no_trigger_in_app; C1 problems 0; errors 1458) |
| 142 | 9568 | 2297 | 458 | 1431 | 0 (part 093, Models, 30 rows: 24 REACHABLE, 6 UNREACHABLE no_trigger_in_app; C1 problems 0; errors 1452) |
| 143 | 9568 | 2297 | 462 | 1427 | 0 (part 094, Note, 35 rows: 31 REACHABLE, 4 UNREACHABLE no_trigger_in_app; before the merge the Note.contains reason was corrected, because the helper's claim of an empty body was false (Note.java:222 returns mFMap.containsKey); C1 problems 0; errors 1448) |
| 144 | 9571 | 2297 | 462 | 1427 | 0 (part 095, Sched part 1, 40 REACHABLE; 3 e() edges. First merge gave 3 errors "missing/invalid evidence label" because the evidence strings lacked the SRC prefix; fixed in graph_def.py and parts/label_095.py, then rebuilt; errors 1448, warnings 0) |
| 145 | 9573 | 2299 | 462 | 1425 | 0 (part 096, Sched part 2, 40 REACHABLE; 2 reflective e() edges. First merge gave warning WARN REVIEW (two default-class edges with a reflection hint); fixed by cls='non_standard' and a reflection via in graph_def.py and parts/label_096.py, then rebuilt; errors 1446, warnings 0) |
| 146 | 9572 | 2299 | 469 | 1418 | 0 (part 097, Sched part 3, 40 rows: 33 REACHABLE, 7 UNREACHABLE no_trigger_in_app. First merge gave 2 warnings: dueForecast(int) (its only caller dueForecast() is UNREACHABLE) and removeLrn(long[]) (labelled UNREACHABLE, but buryCards 2082 and suspendCards 2061 call it unconditionally). Fixed: removeLrn(long[]) relabelled REACHABLE via buryCards; sup(('Sched.dueForecast()', 'Sched.dueForecast(int)')) appended at the end of graph_def.py (backup scratch/graph_def_before_sup146.py); errors 1439, warnings 0) |
| 147 | 9572 | 2299 | 471 | 1416 | 0 (part 098, Sched part 4, 16 rows: 14 REACHABLE by CALL, 2 UNREACHABLE no_trigger_in_app: Sched.setToday (only its declaration in the source tree) and Sched$DeckDueTreeNode.toString (no implicit string use of node variables in the files that hold them); C1 problems 0; citations spot-checked; errors 1437) |
| 148 | 9576 | 2299 | 472 | 1415 | 0 (part 099, Sound, 28 methods: 27 REACHABLE, 1 UNREACHABLE no_trigger_in_app: Sound.resetSounds(int); 4 FRAMEWORK e() edges from Sound.playSound to its listener callbacks, MG932-934; C1 problems 0; three citations spot-checked; errors 1436) |
| 149 | 9578 | 2300 | 473 | 1413 | 0 (part 100, Stats and Storage, 34 rows: 31 REACHABLE, 1 UNREACHABLE no_trigger_in_app: Storage.<init>; 2 non_standard edges: Stats$1.compare (library sort, INFERRED) and AdvancedStatistics.runFilter (hook registry, MG943); C1 problems 0; errors 1434) |
| 150 | 9575 | 2300 | 477 | 1409 | 0 (part 101, Tags, 19 rows: 15 REACHABLE, 4 UNREACHABLE no_trigger_in_app: bulkAdd(List,String), bulkAdd(List,String,boolean), bulkRem, addToStr; C1 problems 0; grep over the source tree confirms no outside callers. First merge gave 2 warnings (automatic CALL edges from UNREACHABLE bulkAdd(List,String,boolean) and bulkRem into bulkAdd(List,String,boolean) and addToStr); fixed by three sup pairs in graph_def.py (backup scratch/graph_def_before_sup150.py); errors 1430) |
| 151 | 9572 | 2301 | 487 | 1398 | 0 (part 102, Utils part 1, 41 rows, C1 problems 0. The first merge failed on names: the Utils keys lacked the libanki. prefix. graph_def.py was restored from scratch/graph_def_before_part102.py and the part merged again. Three warnings then fixed by sup151 (backup scratch/graph_def_before_sup151.py); errors 1419) |
| 152 | 9572 | 2301 | 487 | 1398 | 0 (part 103, Utils part 2, 4 rows, all REACHABLE, 0 e() edges; C1 problems 0; errors 1419) |
| 153 | 9570 | 2301 | 506 | 1379 | 0 (part 104, Hooks and ExternalHookLoader, 34 rows, 2 non_standard e() edges; C1 problems 0. The first merge gave 3 warnings, fixed by sup153 (backup scratch/graph_def_before_sup153.py); errors 1400) |
| 154 | 9568 | 2301 | 516 | 1369 | 1 (part 105, Importers, 37 rows: 27 REACHABLE, 10 UNREACHABLE no_trigger_in_app; C1 problems 0. The first merge gave 2 warnings, fixed by sup154 (backup scratch/graph_def_before_sup154.py). The remaining warning is NoteImporter.<init>, whose incoming edge comes from TextImporter.<init> (batch 106); errors 1390) |
| 155 | 9561 | 2295 | 534 | 1357 | 0 (part 106, TextImporter, FullSyncer, HttpSyncer and ProgressByteEntity, 43 rows: 22 REACHABLE, 18 UNREACHABLE, 3 FRAMEWORK e() edges (INFERRED, the library step); C1 problems 0. The first merge gave 10 warnings: NoteImporter.<init> (from TextImporter.<init>) and 9 base HttpSyncer methods with exact automatic CALL edges from Connection and Syncer. Each runtime receiver overrides the method (Syncer is built only with RemoteServer, Connection.java:281; Connection.java:318 reassigns FullSyncer before upload and download). sup155 (backup scratch/graph_def_before_sup155.py) suppresses those 10 pairs; warnings 0; errors 1378) |
| 156 | 9561 | 2295 | 534 | 1357 | 0 (part 107, MediaSyncer, RemoteMediaServer and RemoteServer, 21 REACHABLE rows, all reached by automatic CALL from Connection.doInBackgroundSync or doInBackgroundLogin; no e() edges; C1 problems 0; errors 1378) |
| 157 | 9561 | 2295 | 538 | 1353 | 0 (part 108, Syncer and Template$1.compare, 35 rows: 31 REACHABLE, 4 UNREACHABLE no_trigger_in_app (Syncer.applyChanges, finish(), start, sync()); C1 problems 0; MG1022 on Template$1.compare for a two-modifier template tag; render_unescaped -> Template$1.compare belongs to batch 138 and is not written here; errors 1374) |
| 158 | 9561 | 2295 | 575 | 1316 | 37 (part 109, Atom and TopLevelParser methods, 37 UNREACHABLE no_trigger_in_app; C1 problems 0. The 37 warnings are automatic CALL edges from the part 110 parser methods, which were still pending; resolved in builds 159 and sup159; errors 1337) |
| 159 | 9347 | 2295 | 615 | 1276 | 0 (part 110, Expression parser, 40 rows, all UNREACHABLE no_trigger_in_app, 0 e() edges; C1 problems 0. Build 159 before sup had 74 warnings (scratch/build_159_premerge.txt): 214 automatic CALL pairs from UNREACHABLE parser methods into UNREACHABLE parser methods. sup159 (backup scratch/graph_def_before_sup159.py) suppresses all 214 after grep showed one TopLevelParser construction (TopLevelParser.java:165, in createCopy), createCopy callers only ReliefDrawer.java:632 and 693, and no new ReliefDrawer. Warnings 0; errors 1297; edges 9561 before sup, 9347 after) |
| 160 | 9347 | 2295 | 619 | 1272 | 4 (part 114, PieChart and MultiScreenPart, 19 rows: 15 REACHABLE, 4 UNREACHABLE, 0 e() edges; C1 entries 4, problems 0. Warnings: MultiScreenPart.<init>, setxRange and setyRange from PlotSheet (pending batches 115 and 116); PieChart.abortAndReset from DrawableContainer.abortAndReset (fixed by sup163); errors 1293) |
| 161 | 9323 | 2295 | 643 | 1248 | 8 after sup161 (part 111, TopLevelParser and BarGraph, 37 rows: TopLevelParser 21 UNREACHABLE; BarGraph 13 REACHABLE, 2 UNREACHABLE Function2D constructors, BarGraph.abortAndReset UNREACHABLE; C1 entries 24, problems 0. Before sup, 20 warnings (scratch/build_161_premerge.txt). sup161 (24 pairs, backup scratch/graph_def_before_sup161.py) includes BarGraph.paint -> TopLevelParser.f(double), which sits in the hasFunction branch: hasFunction is set only by the two UNREACHABLE Function2D constructors (BarGraph.java:79, 96), and ChartBuilder.java:240 passes double[][] bars; errors 1269) |
| 162 | 9321 | 2295 | 662 | 1229 | 21 after sup162 (part 113, Lines, LinesPoints, Integral and LegendDrawable, 40 rows: 20 REACHABLE, 20 UNREACHABLE; C1 entries 20, rows 40, problems 0; 0 e() edges. Before sup, 22 warnings. sup162 (2 pairs, backup scratch/graph_def_before_sup162.py): Integral.paint -> TopLevelParser.f(double) and LinesPoints.paint -> LinesPoints.drawPoint, since Integral and LinesPoints are never instantiated. The 21 remaining have sources in batches 112, 115, 116 and 118, not merged yet; errors 1251) |
| 163 | 9302 | 2295 | 696 | 1195 | 23 after sup163 (part 112, DrawableContainer, FunctionDrawer and FunctionDrawer_y, 40 rows: 6 REACHABLE, 34 UNREACHABLE; C1 entries 34, rows 40, problems 0; 0 e() edges. Before sup, 35 warnings (scratch/build_163_premerge.txt). sup163 (19 pairs, backup scratch/graph_def_before_sup163.py): DrawableContainer.paint -> FunctionDrawer.paint, FunctionDrawer_y.paint, Integral.paint, LinesPoints.paint (none of the four classes has a new or a subclass in the java root); DrawableContainer.abortAndReset -> nine abortAndReset methods (its only call site is its own body, DrawableContainer.java:62); FunctionDrawer(_y).setOnFrame() -> setOnFrame(double); FunctionDrawer(_y).paint and getMaxValue -> TopLevelParser.f(double) (getMaxValue has no call site). The 23 remaining warnings have PlotSheet (batches 115, 116) or ReliefDrawer (batch 118) sources; errors 1217) |
| 164 | 9299 | 2295 | 706 | 1185 | 29 after sup164 (part 117, PointDrawer2D and RelativeColorGradient, 10 UNREACHABLE no_trigger_in_app, 0 e() edges; C1 entries 10, problems 0. Before sup, 31 warnings (scratch/build_164_premerge.txt). sup164 (3 pairs, backup scratch/graph_def_before_sup164.py): DrawableContainer.paint -> PointDrawer2D.paint, DrawableContainer.abortAndReset -> PointDrawer2D.abortAndReset, PointDrawer2D.paint -> PointDrawer2D.drawPoint (PointDrawer2D has no new and no subclass). The 29 remaining have PlotSheet (batches 115, 116) or ReliefDrawer (batch 118; RelativeColorGradient.makeGradient and delta) sources; errors 1207) |
| 165 | 9299 | 2295 | 712 | 1179 | 35 (part 116, PlotSheet xToGraphic and yToGraphic with linear and log forms plus the coordinate log methods, 10 rows: 4 REACHABLE CALL, 6 UNREACHABLE; C1 entries 6, rows 10, problems 0; 0 e() edges). New warnings: PlotSheet callers in batch 115 (pending), and branch_never_taken targets xToGraphicLog and yToGraphicLog (setLogX and setLogY have no caller). No sup yet. |
| 166 | 9299 | 2295 | 743 | 1148 | 57 (part 118, ReliefDrawer, 31 rows: 31 UNREACHABLE no_trigger_in_app; C1 entries 31, rows 31, problems 0; 0 e() edges). ReliefDrawer has no new site and no subclass. Its inner classes are built only in ReliefDrawer methods, and RelativeColorGradient.makeGradient only in its constructors. |
| 167 | 9268 | 2295 | 752 | 1139 | 60 before sup167 (part 119, XAxis, 25 rows: 16 REACHABLE CALL, 9 UNREACHABLE (7 no_trigger_in_app, 2 branch_never_taken); C1 entries 9, rows 25, problems 0; 0 e() edges). sup167 (31 pairs, backup scratch/graph_def_before_sup167.py, premerge build_167_premerge.txt): ReliefDrawer family and the XAxis downwards-marker dead branches. After sup167: 39 warnings, all with PlotSheet sources (batch 115). |
| 168 | 9195 | 2295 | 777 | 1114 | 0 after sup168 (part 115, PlotSheet, 40 rows: 15 REACHABLE, 25 UNREACHABLE (22 no_trigger_in_app, 3 branch_never_taken: drawMultiMode, ticsCalcX, ticsCalcY); C1 entries 25, rows 40, problems 0; 0 e() edges). Merge left 49 warnings, all PlotSheet-sourced or sourced from classes never constructed. sup168 (73 pairs, backup scratch/graph_def_before_sup168.py, premerge build_168_premerge.txt): never-constructed FunctionDrawer(_y), Integral, LinesPoints, PointDrawer2D, ReliefDrawer(ReliefLegend), XAxisBarGraph, XAxisHistoGram, YAxisBarGraph, YAxisHistoGram; PlotSheet dispatch into isClusterable/isCritical/isOnFrame (no PlotSheet is ever added to a drawable list); dead branches (isMultiMode, isAutoTic, setLogX/setLogY); UNREACHABLE-only callers. Edges 9268 to 9195. |
| 169 | 9195 | 2295 | 813 | 1078 | 0 after sup169 (part 120, XAxisBarGraph and XAxisHistoGram, 36 rows; sup for 23 pairs; premerge had 17 warnings). |
| 170 | 9171 | 2295 | 821 | 1070 | 0 after sup170 (part 121, XGrid, 15 rows: 8 UNREACHABLE, 7 REACHABLE; premerge had 1 warning, DrawableContainer.abortAndReset -> XGrid.abortAndReset, sup pair added). XGrid.paint, drawGridLine, isClusterable, isCritical, isOnFrame have 'no path' errors (pending the ChartView/Statistics chain). |
| 171 | 9170 | 2295 | 831 | 1060 | 0 after sup171 (part 122, YAxis, 28 rows: 10 UNREACHABLE, 18 REACHABLE; premerge had 1 warning, DrawableContainer.abortAndReset -> YAxis.abortAndReset). |
| 172 | 9147 | 2295 | 867 | 1024 | 0 after sup172 (part 123, YAxisBarGraph and YAxisHistoGram, 36 rows; premerge had 17 warnings, 23 pairs: YAxis classes never constructed or subclassed). |
| 173 | 9126 | 2295 | 885 | 1006 | 0 after sup173 (part 124, 38 rows: 18 UNREACHABLE, 20 REACHABLE; premerge had 9 warnings, 21 pairs; DrawableContainer.abortAndReset -> YGrid.abortAndReset included). |
| 174 | 9129 | 2302 | 885 | 999 | 0 (addendum to part 106: three FRAMEWORK edges from HttpSyncer.req to EasySSLSocketFactory.connectSocket, createSocket(Socket,...) and isSecure; no sup) |
| 175 | 9121 | 2302 | 895 | 989 | 0 after sup175 (part 125, 40 rows; premerge had 2 warnings, GraphicsWrap.drawRect and GraphicsWrap.drawImage; 8 pairs: five drawBar closed branches, LinesPoints.drawPoint, Lines.drawPoint, ReliefDrawer.drawColoredRelief) |
| 176 | 9122 | 2303 | 899 | 984 | 0 (part 126, 14 rows: EasySSLSocketFactory and EasyX509TrustManager; equals and hashCode stay INFERRED, see conflicts.md) |
| 177 | 9122 | 2303 | 901 | 982 | 0 after sup177 (part 127, 38 rows: 34 REACHABLE, 2 UNREACHABLE, 2 EDGE; premerge had 2 warnings; 2 pairs: AnkiDroidApp.onCreate to ProductionCrashReportingTree.<init> and <clinit>, closed by the BuildConfig.DEBUG branch) |
| 178 | 9125 | 2307 | 901 | 978 | 0 (part 128, 42 rows, 3 ASYNC edges; no sup) |
| 179 | 9116 | 2606 | 908 | 672 | 0 after sup179 (part 129, 39 rows; premerge had 7 warnings; 11 pairs: CompatV10, CompatV11 and Nook bodies shadowed on API 27 by CompatV21 inheritance, plus CompatHelper.<init> to the Nook constructor) |
| 180 | 9116 | 2606 | 908 | 672 | 0 (part 130, Collection.java, 34 rows, all REACHABLE; every method already had a route from automatic CALL edges, so the counts do not move; the labels add SOURCE confirmation) |
| 181 | 9116 | 2606 | 908 | 672 | 0 (part 131, DB, Decks and LaTeX, 40 rows, all REACHABLE; counts do not move; Decks.<clinit> labelled REACHABLE from the class-file route, body not decoded (javap unavailable)) |
| 182 | 9116 | 2606 | 908 | 672 | 0 (part 132, libanki Media and LaTeX filter, 9 rows, all REACHABLE through automatic CALL edges; counts do not move) |
| 183 | 9116 | 2606 | 908 | 672 | 0 (part 133, Models, 39 rows, all REACHABLE through automatic CALL edges; counts do not move; Models._transformFields dispatch to the three visitors is over-approximate and not suppressed) |

Files: graphs/AnkiDroid/scratch/build_NNN.txt. Parts merged at each build and the reason for each sup() are in handoff/HANDOFF_V2.md, "Convert run decisions". Exit code 1 is expected (unresolved and page errors).

## Batch plan (C3)
Table batch | classes | methods | helper | status is kept in scratch/batches/plan.tsv (batch | classes | methods). Helper and status columns are filled as helpers start. 139 batches including the gap batches 127 to 139, max 40 methods. Classes over 40 methods are split by method order (recorded under "## Convert run decisions" in handoff/HANDOFF_V2.md).

## Ownership rule (cross-batch edges)
An edge is written by the part that contains its source method; if the source is a page (S_*), by the part that contains the destination method. Helpers are told this (HANDOFF_V2 "Convert run decisions", 2026-10-27). Exceptions, all orchestrator addenda because a part omitted the edge: the DeckPicker INTENT addendum (HANDOFF_V2, 2026-10-28); the CardBrowser INTENT and REGISTER addendum; the NoteEditor.onCollectionLoaded -> JSONNameComparator.compare addendum; the part 017 REGISTER addendum for DeckPicker$18.<init>; the DeckOptions.buildLists -> DeckOptions$JSONNameComparator.compare CALL addendum (build 050, part 028 gap).

## Open items
- Card.<clinit> (part 081): settled 2026-10-28 22:15. auto_calls.json holds the CALL edges Collection.getCard -> Card.<clinit> (Collection.java:421) and Collection._newCard -> Card.<clinit> (Collection.java:759), and build_graph.py reads auto_calls.json (USE_AUTO). The label_081.md row now cites them. No route or e() edge is needed.
- decl_line in scratch/node_names.tsv is wrong for several nodes (DeckPicker$8 onClick should be 401, $9 onClick 463, DeckPicker$10, $13, $14-$17; NoteEditor fetchIntentInformation 405 should be 550; NoteEditor SetNoteTypeListener/EditNoteTypeListener onItemSelected and onNothingSelected: 1544/1586 and 1594/1646). No merged citation has been confirmed to use decl_line; check before any part cites it.
- AbsSpinner.java is not in fw_src. Batch 013's NoteEditor$3.onNothingSelected UNREACHABLE reading (INFERRED) depends on AbsSpinner's setAdapter and setSelection steps, which are not checked. Helpers must not cite AbsSpinner.java.
- Bug finding: CardBrowser.closeCardBrowser(int) always throws NullPointerException (CardBrowser.java:1120-1132, line 1130). Its callers are checked in the part that holds them; the finding goes under "Hazard candidates" in readme_notes.md.
- Batch 038 must not re-add the two StudyOptions onRequireDeckListUpdate CALL edges (the sup() pairs in graph_def.py).
- Batch 038 must not write S_STUDYOPTIONS_FRAG -> FilteredDeckOptions.<init> (INTENT) or S_STUDYOPTIONS_FRAG -> DeckOptions.<init> (INTENT). They were written in parts 029 and 027 by the destination rule (HANDOFF_V2, part 027 and part 029 entries).
- Batch 080 INTENT lead: WidgetStatus$UpdateDeckStatusAsyncTask.onPostExecute -> AnkiDroidWidgetSmall$UpdateService.<init> (WidgetStatus.java:106-109, STATE_SETTINGS). Batch 080 must write it (HANDOFF_V2).
- Plan gap (422 methods in no batch file): resolved by the batch 017 resume and batches 127 to 139 (HANDOFF_V2). Those batches run after batch 126.
- Batch 015 is merged. Its three legacy auto CALLs are suppressed (see HANDOFF_V2 "Convert run decisions").
- The batch 015 helper's getCustomFonts lead (Preferences.java:734-735) was wrong. The calls are at 738-739, and auto_calls.json covers them. No edge needed.
- NoteEditor.onCollectionLoaded and its JSONNameComparator methods have no path until the AnkiActivity part (AnkiActivity.onLoadFinished) merges.
- parts/label_010.py header line 11 is wrong (see HANDOFF_V2). The merged part is not edited.
- graph_def.py before the CardBrowser addendum was not backed up separately; scratch/graph_def_before_part012.py holds the file with that addendum (HANDOFF_V2).
- __pycache__ folders from py_compile under graphs/AnkiDroid/ and parts/ are not deleted (no-delete rule). Ask the user before cleanup (HANDOFF_V2).
- The DeckPicker$18 registration condition is MG112 (text only, batch 017). It is not a gate constant until the constants are added before STRICT.

## Decisions made by Muse (for the user and Yang to review)
- Build type: the standard configuration is the debug APK in DATASET.txt, so the release branch (AnkiDroidApp.java:164-171, ProductionCrashReportingTree) is UNREACHABLE closed_by_configuration. Revisit only if the ground truth is the release build (HANDOFF_V2 "Convert run decisions", 2026-10-27 21:50).
- DeckPicker$8 onClick: closed only on API 27 and up. minSdk is 10 (build.gradle line 12), so the fallback branch runs on API 10 to 13. The standard configuration (API 27) is used. Revisit only if the ground truth is an API 10-13 device (HANDOFF_V2, 2026-10-27 22:15 EDT entry).

## Blocked
- Batch 020, first attempt: the helper stopped before writing label_020.py or label_020.md, citing a pause instruction. handoff/PAUSE_KIRO.md is addressed to Kiro for AmazeFileManager only, so it does not apply to this run. Relaunched as a new helper; the run continues.
- Batch 020, second attempt: stopped after 32 tool calls with no output files (status INCOMPLETE, no usage-limit message). Its brief pointed at the wrong sections of AGENT_BRIEF_V2 for the row format; the format is in handoff/SCHEMA_V2.md. The helper's blocker about finishNoStorageAvailable and calculateDynamicFontSize was checked: those are in batch 019 and not in batch_020.txt. Relaunched a third time with the corrected brief and incremental writes.
- Batches 023, 024 and 025, first launch in this session: each helper failed with "Can't reach the API server (ENOTFOUND)" before writing output. This is an API error, not a session, usage or rate limit. Batch 024 was relaunched and completed (merged as part 024). Batch 023 was relaunched and is running.
- Batch 025 (CardTemplateEditor part 1, 40 methods, MG192-201): the helper failed with ENOTFOUND on the relaunch too. Resolved at 12:36: the retry (helper a9bfbed3836664be7, STATUS DONE 12:35) passed C1 (problems 0) and the citation spot-check, and was merged as part 025 with build 068 (2 warnings, DeckTask automatic CALL edges into CardTemplateEditor$1.onCancelled and onProgressUpdate) and build 069 (sup for part 025, warnings 0). Batch 026 was labelled independently and is not held by this block.
- 2026-10-29, after batch 133 (build 183): AnkiDroid is blocked, not DONE. Build 183: methods 4186, edges 9116, REACHABLE 2606, UNREACHABLE 908, UNRESOLVED 672, errors 694, warnings 0. The verdict depends only on graph routes and UNREACHABLE entries (tools/build_graph.py), so the 672 UNRESOLVED methods in 212 classes (counted from out/methods.csv) need source-verified graph edges, or source-verified UNREACHABLE entries, before the app can finish. Causes: the 22 zero-caller roots and the Reviewer chain in "## Current step" (missing LIFECYCLE edge into AbstractFlashcardViewer.onCreate@Reviewer; S_REVIEWER has no incoming edge); the ChartView chain (ChartView.addFragment and onDraw UNRESOLVED; ChartView.<init>(Context) UNREACHABLE); and the batch 125 GraphicsWrap and PieChart callers. Labels cannot reduce the count. The connector pass has not been done in this run. Stopped per handoff/KIRO_CONVERT_APPS.md line 87; MMEX was not started. Resume: add connector parts after 133, rebuild, and work through the UNRESOLVED rows in out/methods.csv. Batches 134-139 and the Hooks.runFilter to AdvancedStatistics.runFilter pair (suspect automatic CALL, not suppressed) are still open.
- 2026-10-30, labelling run (build 184, graphs/AnkiDroid/scratch/build_184.txt): no graph change. Methods 4186, edges 9116, REACHABLE 2606, UNREACHABLE 908, UNRESOLVED 672, errors 694, warnings 0, the same as build 183. Blocked: the 672 UNRESOLVED methods need source-verified graph edges, which this run does not add. The run moved on. PROGRESS_V2.md line 17 set to [B].
- 2026-10-30, overnight labelling run (labelling only): labelled. Parts 134-150 merged as builds 189-204. Build 204 (graphs/AnkiDroid/scratch/build_204.txt): REACHABLE 3275, UNREACHABLE 911, UNRESOLVED 0, errors 0, warnings 0. Open, not in the gate: Card.toString is UNREACHABLE (no_trigger_in_app) but APE executed it (coverage_baseline.json). Decisions are in handoff/HANDOFF_V2.md "## Convert run decisions (AnkiDroid overnight labelling, 2026-10-30)". Route checks not started.

## Finish run 2026-11-01 — B2 check-2 citations (auditor PASS, audit/B2/AUDIT.md)
- Applied the 3 exact word-form citation replacements from helper/b2-citations/EDITS.md.
- graph_def.py: NotificationService.java:47 -> (line 47); :46-54 -> (lines 46-54); graph_def_mod/01.py: :37 -> (line 37).
- New edge ids E6d79dde5, E3c7d7dc4, E10b85314; old ids E50d68ebc, E16231eaa, Ed8355a39 gone; total edges still 9178.
- Local build: methods 4186, REACHABLE 3275, UNREACHABLE 911, unclassified 0, errors 0, warnings 0.
- check_citations.py: 273 distinct, 0 problems (was 276/3). Root cause: tools/check_citations.py:20 ROOT_STYLE
  is an unanchored regex matching the services/...java:<digits> substring inside the full-path SRC citation;
  the citation-side word-form fix is the only in-rules resolution (tools/ read-only, untouched).

## Finish run 2026-11-01 — B3 check-4 bytecode lines (auditor PASS, audit/B3/AUDIT.md)
- Appended ONE combined EDIT after the module-loader block in graph_def.py (single EDIT definition):
  23 TaskData/ChartBuilder/DisplayPair entries (helper b3-taskdata, incl. DeckPicker.deleteDeck 2017->2067)
  + 25 Utils-pin/MockNoteFactory-INFERRED entries (helper b3-utils-mock). Dicts verbatim from EDITS.md.
- Verified in the rebuilt trigger JSON: 48/48 new evidence strings present, 0 old remnants.
- Local build: methods 4186, edges 9178, REACHABLE 3275, UNREACHABLE 911, errors 0, warnings 0.
- check_bytecode_lines.py AnkiDroid --all: 6904 checked, 1001 skipped, 211 implicit,
  0 where the cited line does not show the callee. Disclosed caveat: the 23 B3-a edges drop out of the
  checker's checked set because their (bytecode line was N) form doesn't match its pattern; verification
  rests on printed lines + auditor re-prints + merger spot-prints. check_citations still 273/0.
- MockNoteFactory wording (auditor-confirmed): source under multimediacard/test/ is pruned from the checker
  source index; NOT the brief's literal "no source in the upload" (the file exists, 2600 bytes, cited lines
  printed and correct).

## Finish run 2026-11-01 — B4 check-8 explanations (auditor PASS with binding correction, audit/B4/AUDIT.md)
- Paint-sync helper's "8 NEW entries" are NOT new: all 8 axis-paint pairs already exist in graph_def_mod/01.py
  multi-pair sup() blocks (XAxisBarGraph :3699/:3700, XAxisHistoGram :3711/:3712, YAxisBarGraph :3796/:3800,
  YAxisHistoGram :3795/:3799). VERIFY-ONLY; nothing added.
- Applied the 1 ReliefLegend reason reword at graph_def_mod/01.py:3488-3490: getLegend() has no caller and
  ReliefDrawer itself is never constructed, so the creation site never runs (ReliefDrawer.java:473-474 shows
  getLegend() DOES create a ReliefLegend; labels and the 3 SUPPRESS entries stand).
- Wrote graphs/AnkiDroid/scratch/check8_explained.md: all 169 scan lines, 205 method-section pairs,
  partition 106 sibling-only / 52 remainder-only / 11 mixed; every entry caller-named with helper section.
- scan_unreachable.py --callers still 169 of 911. Local build: methods 4186, edges 9178, 3275/911, errors 0,
  warnings 0; check_citations 273/0; check_bytecode_lines --all 0 not-show; greps 5/6/7 all 0.
- 0 routes, 0 label changes from B4.

## Finish run 2026-11-02 — B6 route-check fixes (audits F1-F5 all PASS)

- F1 (routes 01-06, audit b6fix-r01-06/AUDIT.md PASS): NO graph edit.
  Helper trigger JSON SHA-identical to the merger-tree baseline; 0 edges
  added/removed/changed; methods.csv byte-identical. Route table uses
  C01-C06, never BFS. C02 steps 13-15 carry the auditor-verified ids
  E3a5b3438, E51823c2c, E0c0d5268.
- F2 (routes 07-12, audit b6fix-r07-12/AUDIT.md PASS): 115 lines appended
  to graph_def.py (B6_GUARD / B6_EVIDENCE / B6_STATE_* / B6_NEEDS_STATE,
  wrapper around the B3 EDIT, saved and called first). Build: 4186/9178,
  3275/911, 0/0; rebuilt JSON SHA-identical to the helper build; 23 edges
  changed, 0 added/removed. Route 08 rename $15 -> $16 HELD (bytecode:
  $15 = CHECK_DATABASE, $16 = CHECK_MEDIA); route 08 UNCLEAR (step 11
  INFERRED, support-v4 source absent); route 12 WRONG with no graph edit
  (rebuilt reviewer-flow route in the table).
- F3 (routes 13-18, audit b6fix-r13-18/AUDIT.md FAIL narrow + rework
  audit b6fix-r13-18-rework/AUDIT.md PASS): literal edits (ENV_BEOLINGUS,
  ENV_PREFS_PATH, STATE_FIELD_TEXT constants; 10 main-body edge edits) +
  B6FIX_EVIDENCE/GUARD folded into the single combined EDIT (helper's
  B3+B6FIX def EDIT kept verbatim, F2 wrapper chained after it) + 2
  insertions in graph_def_mod/01.py (needs_state STATE_FIELD_TEXT,
  guard 'source text non-empty'). Build: 4186/9178, 3275/911, 0/0;
  exactly 19 edges changed vs the F2 build, 0 added/removed;
  needs_state 140 -> 141, methods with STATE 367 -> 405. Route-17 step-6
  applied by edge+line ONLY (887 block, evidence line 890, new id
  Ec31ec494); the RESULT edge (evidence line 973/980) is byte-identical.
  The EDITS.md uniqueness sentence was amended at merge time to record
  the two-occurrence exception (re-audit section 8 item 2, superseding
  the coordinator's earlier no-amendment note). Audit C1 confirmed:
  route 13 step 15 guard is exactly !editModelMode (NoteEditor.java:
  1116-1121). BackgroundPost Ecba7dfd7 stays ENV_NETWORK (second cycle
  not expanded into explicit steps).
- F4 (routes 19-24, audit b6fix-r19-24/AUDIT.md PASS): route-21 variant
  split (2 page defs, 4 GUI moves, 2 ENTERS E81c3cc95/E6b094d43, generic
  page kept for types 2,3,4,6,7,8) + route-24 guard hand edges (5).
  Build: 4186/9180, pages 45, 3275/911, 0/0; auto 8146 -> 8141;
  ENTERS 56 -> 58; generic GUI ids gone; new ENTERS present.
  Route 20 NO-split honoured (table uses UPDATE_FACT + mUpdateCardHandler,
  never RenderBrowserQA -> AFV$9); route 21 table uses the hkey-empty
  prefix, never the BFS route (BFS ignores guard text).
- F5 (routes 25-30, audit b6fix-r25-30/AUDIT.md PASS): main-body retargets
  (FULLSYNC / NOTEEDITOR_CHANGETYPE / MODELFIELDEDITOR_RENAME pages,
  3 new SCREENS) + trailing B6 block (15 hand edges) + 3 edits in
  graph_def_mod/01.py (DialogHandler retarget, CollectionLoader guard +
  citation drop, BackupManager no-space guard). Build: 4186/9183, pages
  48, 3275/911, 0/0; auto 8129; ENTERS 59; new ENTERS E30f7c51d present;
  superseded ids Eeded0833, Ef2c97ad2, E27363954, E5798aa47, E9d88d57c
  absent. Builder duplicate note: F4 and F5 hand edges coexist for the
  two overlapping pairs (exceededCursorSizeLimit, getCol -> Storage),
  both guards true for the same call sites; no label/route effect.
- Labels: 0 flips in all of B6 (3275/911 throughout).
- Redraw: verify_sample.py AnkiDroid 30 20261025 on the post-B6 graph
  gives a DIFFERENT sample (297 distinct edges; 5 methods swap in/out
  — see scratch/route_table.md "REDRAW NOTE"). Per the merger's assigned
  task, the route table covers the FIRST-draw 30 routes; the 5
  redraw-only methods are unjudged and flagged for a coordinator ruling.
- Final BFS routes re-printed from the post-B6 graph into
  scratch/route_print/ (30 files); first-draw prints backed up in
  merger/route_print_firstdraw/ (work dir, not pushed).
- Route table: scratch/route_table.md — WRONG 18, FIXED 9, UNCLEAR 2,
  CORRECT 1; first-draw error rate 27/28 = 0.9643.

## Finish run 2026-11-02 — B7 verification log (writer modelled on AnyMemo)

- make_verification.py (new; AnkiDroid had no writer before): path rows
  use the BUILT route (methods.csv route_edge_ids) with the audited
  route-table verdict; WRONG-route notes point at the corrected
  derivation in scratch/route_table.md (the built route is wrong for
  those routes, so the table — not the BFS route — is the judged route).
  Path confirmed_by is SOURCE only when every built-route edge is
  source-evidenced, else INFERRED (same rule as the label rows). Label
  rows: 911 UNREACHABLE (graph labels) + 30 sampled REACHABLE. Edge
  rows: 7 B6 variant-page edges (ids re-derived from the final graph
  by pair, asserted unique) + one row per distinct FW-SRC citation
  with line numbers. Rows: path 30 (WRONG 18, FIXED 9, UNCLEAR 2,
  CORRECT 1), label 941, edge 231. The writer raises (STOPs) on any
  mismatch: missing method, non-REACHABLE path item, ref not on the
  route evidence, empty note, non-unique variant pair, missing edge.
- Determinism: two runs byte-identical (cmp passed); verification.csv
  479,626 B, 1203 lines (header + 1202 rows), header exactly
  type,item,result,confirmed_by,ref,edges,note.
- Checks on the final graph (saved in merger/checks_final/): check 2
  273 distinct, 0 problems; check 3 0 routes flagged; check 4 6901
  checked, 0 where the cited line does not show the callee (6901 vs
  B3's 6904: 3 auto bytecode edges replaced by B6 hand edges); check 8
  scan --callers 169 of 911 have a bytecode caller outside the set
  (all 169 explained in scratch/check8_explained.md, B4); greps:
  DEAD/FRAMEWORK_ONLY 0, FW-MEMORY 0, PENDING 0; STRICT = True.
- readme_notes.md (five headings in order) + LESSONS.md (8 bullets)
  written. The redraw/sample divergence is recorded in both
  route_table.md and readme_notes.md as a coordinator ruling item.

## Finish run 2026-11-02 — D1/D3 device preparation (audit + re-audit PASS)

- D1: device/routes/AnkiDroid/ROUTES.csv — 30 rows (first-draw sample,
  seed 20261025), Currency 10-column header, routes in order 01-30.
  Status: 27 scripted, 3 unscriptable = 10.0%, exactly at (not over)
  the 10% cap; no over-cap acceptance is triggered by the arithmetic.
  If the cap is read as strictly below 10%, the coordinator must rule
  (audit note); the cap alone must not block F1 per the user's ruling.
- D3: 28 scripts under device/routes/AnkiDroid/ (27 scripted routes
  + route_26b.py, the second script for route 26's rename-flow
  route B; route A is route_26.py and the CSV row). Scripts follow
  the corrected routes for WRONG routes (never BFS where the audit
  says BFS misleads), the final BFS route for FIXED/CORRECT routes.
  Unscriptable reason files: ROUTE_UNSCRIPTABLE_02.md (real AnkiWeb
  account + real HTTPS sync; the user's account/credential exception),
  ROUTE_UNSCRIPTABLE_15.md (external host app via exported
  CardContentProvider; harness has no provider-call action),
  ROUTE_UNSCRIPTABLE_25.md (no-space dialog; no UI action produces
  it, threshold unverified, revival path recorded).
- Audit: device-draft/AUDIT.md FAIL narrowly on 5 r.comment calls
  missing the required edge argument (D1-D5, routes 19/20/22/28);
  fixed by attaching the auditor-specified following edges; narrow
  re-audit device-draft/REAUDIT.md PASS (AST 0 bare comment calls,
  4 fixed scripts exit 0 under branch-harness --dry-run, CSVs
  re-parsed 30 rows, permissions normalised to the qualified form).
  Full-audit rulings (a)-(f) all RULED-ACCEPTED, including route 21
  menu-sync entry (not onResume), route 10 trigger substitution,
  routes 06/08 scripted despite INFERRED steps. Dry-run status: all
  28 scripts exit 0 under harness --dry-run (24 in the full audit +
  4 in the re-audit); no emulator/adb/device was started. The full
  device/drycheck.py run and D9 remain coordinator gates.
- D7: make_verification.py carries the DEVICE-row block (pattern
  copied from AnyMemo's D7 writer): if
  graphs/AnkiDroid/device/results.csv exists (written by the CI
  device run, not by this run), one DEVICE-confirmed path row per
  results row is appended after all existing rows; otherwise the
  output is the B7 file exactly. Verified: two runs with the D7
  block and no results file are byte-identical to the pushed B7
  verification.csv, so verification.csv is NOT re-pushed here.
  DEVICE rows never feed back into labels, edges, or route checks.
- Gaps carried (flagged in the drafts and confirmed by audit, not
  resolved silently): selectors needing a live uiautomator dump
  (drawer "Navigate up", "More options", route_10 FIXTURE_CARD_TEXT,
  route_11 FIXTURE_DYN_DECK, route_14 Advanced-screen navigation);
  fixtures (tablet config for 05/11, route_08 integrity-check
  assumption, route_12 video fixture, route_20 StudyOptions entry
  variant, route_27 focused-deck mechanism, route_01 language
  spinners, glosbe.com/Beolingus reachability unchecked here).
- 2026-11-06 04:41 UTC: Kiro, re-audit W4 done for AnkiDroid (RTA on); next W5 (ESR_CREATION).
- 2026-11-06 04:46 UTC: Kiro, re-audit W5 done for AnkiDroid (ESR_CREATION on; library_edges.csv); next W6 (outside data).
- 2026-11-06 04:53 UTC: Kiro, re-audit W6 done for AnkiDroid (outside_data.csv); next W7 (guards).
- 2026-11-06 05:02 UTC: Kiro, re-audit W7 round 1 done for AnkiDroid (pre-screen, checked-case guards; most flagged steps PENDING); next W8 (CI, re-verify routes, device runs).
