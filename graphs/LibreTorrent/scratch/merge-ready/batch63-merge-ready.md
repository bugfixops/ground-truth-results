**REVISION 2026-11-01 (Stream A Phase 1c, APPLY DECISIONS, batches 62-67 worker): DECISIONS.md applied mechanically only; no other row touched. No push. Build: not run. C1: not run.**
D4e (invalidateAll REACHABLE-on-inflate): rows 7, 21 OPEN -> REACHABLE proposed INFERRED. D4f: rows 6, 20 hasPendingBindings stay OPEN (already confirmed_by —, no change). D4g ($N count-match accepted): rows 12, 13, 26-35 stand REACHABLE proposed INFERRED, assignment source-order only, no change. D4a standing getters rows 1, 15 stay OPEN (already —, no change); D4d standing setVariable rows 10, 24 stay OPEN (already —, no change). D1: no OPEN confirmed_by needed normalising in this file (all OPEN rows already —). Counts mechanically verified from the label column, 40 rows, sequence 1-40 intact: before 32 REACHABLE / 0 UNREACHABLE / 8 OPEN; after 34 REACHABLE / 0 UNREACHABLE / 6 OPEN. OPEN after: 1, 6, 10, 15, 20, 24. No conflict found.

**REVISION 2026-11-01 (OPEN-closing round 2, group G10): 0 rows flipped. Counts unchanged: 32/0/8.**
Backed up first to `~/workspace/libretorrent-merge-backup-pre-openclose2/batch63-merge-ready.md` (md5-identical to the pre-edit file).
No GitHub connector fetch was needed or made in this pass (all needed files were already local), so no 429 was hit. Nothing was pushed.
Fresh source for this pass: `~/workspace/b626364-openclose2-src/` (copies of the round-1 layout files + a fresh grep file).
$N count-match re-verified on the SAME layout blobs as round 1 (connector blob SHAs, identical to round 1):
dialog_go_to_folder.xml blob `907a43a5fe36c309773e20680824e48a6e8a3d88`, 30 lines, exactly ONE `@={}` at :27 (`viewModel.path`) — matches
the already-REACHABLE GoToFolder $1 pair (rows 12-13); dialog_log_filter.xml blob `c6c7c0fec4b60248ddb13ceb7609abd96885fd68`,
62 lines, exactly FIVE `@={}` at :24 `logSessionFilter`, :33 `logDhtFilter`, :42 `logPeerFilter`, :51 `logPortmapFilter`,
:60 `logTorrentFilter` — matches the already-REACHABLE LogFilter $1-$5 pairs (rows 26-35). Per-$N assignment remains source-order
only, NOT bytecode-verified; if the merger rejects count-match $N reasoning, rows 12-13 and 26-35 revert to OPEN together with
batch 62 $N rows 1-2 and 17-28. No $N label was changed in this pass (none was OPEN).
Fresh corpus grep re-run in this pass (`b626364-openclose2-src/grep_ruleF_corpus_626364_round2.txt`, 252 app Java files in
`~/workspace/ruleF-src`): ZERO hits for `hasPendingBindings`, `invalidateAll`, `setVariable`, `getViewModel`, `onFieldChange`,
`executePendingBindings`. That grep is app-Java-tree only (generated Impl bodies absent), so it flips NOTHING. No generated
`*BindingImpl` body, `DataBinderMapperImpl`, or androidx `ViewDataBinding` library body was found locally.
Rows still OPEN (8, unchanged): 1, 15 (`getViewModel`, convention (v)); 6, 20 (`hasPendingBindings`); 7, 21 (`invalidateAll`);
10, 24 (`setVariable`, contradiction (xv) — see the conditional table in the appendix; NOT decided here). No row was flipped to
UNREACHABLE: no saved full-repo grep exists, and zero hits in a partial corpus alone never flip a row. Build: not run. C1: not run.
FLAG (not decided here): batches 63/64/65 MUST use ONE `setVariable` rule, and the merger should also settle ONE `invalidateAll`
rule — batch 65 marks `invalidateAll` REACHABLE on inflate (batch 65 rows 12, 23, 34) while batch 63 keeps `invalidateAll` OPEN on
the same inflate evidence. This pass changes neither side.

**REVISION 2026-11-01 (OPEN-closing pass): 0 rows flipped. Counts unchanged: 32/0/8.**
Fresh layouts printed in this pass (~/workspace/b626364-openclose-src/): dialog_go_to_folder.xml (30 lines, SHA 907a43a5…;
viewModel variable, sole @={} at :27 viewModel.path), dialog_log_filter.xml (62 lines, SHA c6c7c0fe…; viewModel variable,
exactly 5 @={} at :24/:33/:42/:51/:60 — matching the already-REACHABLE $1-$5 rows), dialog_select_tag.xml (25 lines,
SHA cf0ea57e…; NO <data> block at all — confirms batch 64 rows 1-4 have no variable/observable to trigger onFieldChange or
setVariable, but per the undecided no-variable-layout rule (xv) they stay OPEN, not UNREACHABLE).
Corpus grep (grep_ruleF_corpus_626364.txt, full 252-file app-Java tree, NOT full-repo): zero hits for `.hasPendingBindings(`,
`.invalidateAll(`, `.setVariable(`, `.getViewModel()`. This confirms no printed app caller for rows 6, 7, 10, 20, 21, 24 and
for the getViewModel rows 1, 15, but does NOT flip them: framework-internal calls are unprinted, and rows 1/15 additionally
rest on the undecided binding-getViewModel convention (v) — executeBindings reads the mViewModel field, not the getter —
which this pass does NOT decide. Host steps printed fresh: FileManagerDialog:550-553 (GoToFolderDialog.newInstance + show),
LogActivity:254-255 (SessionLogFilterDialog.newInstance + show). Counts before and after: 32/0/8. Build: not run. C1: not run.

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 63 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** Build and C1 run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 63 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. Prior proposal (Agent 21,
  `~/workspace/libretorrent-batch63-proposal.md`) was used as an INPUT / lead list only;
  every anchor citation below was re-checked against a fresh connector fetch in this pass,
  and every OPEN row was re-judged against that fresh print (see "Fresh re-check" below).
  No proposal verdict was copied as a result without that re-check.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 63 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/crosscheck/batch_plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-63 rows are `TODO_CANDIDATE_REACHABLE` in the plan (candidates, not evidence).
Method names, JVM descriptors, and plan order were checked row-for-row against the table
below in this pass: 40 rows, sequence 1-40 intact, zero mismatches vs the plan.
All 40 rows are generated data-binding classes.

## Fresh re-check in this pass (branch work-2026-10-31, connector, one file at a time, 20 s pauses)

All paths under `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`,
saved in `~/workspace/b626364-src/`:
- `ui/filemanager/GoToFolderDialog.java` — fresh SHA `3d0f97b4…`, 167 lines: onCreateDialog, DataBindingUtil.inflate dialog_go_to_folder at :99, binding.setViewModel(viewModel) at :100, binding.path TextWatcher at :109, initAlertDialog(binding.getRoot()) at :125. No `binding.getViewModel()` call in the file. Matches the proposal exactly.
- `ui/filemanager/GoToFolderViewModel.java` — fresh SHA `a408917d…`, 35 lines, NEW in this pass (not in the proposal): `public ObservableField<String> path = new ObservableField<>();` at :29. This prints the observable behind rows 8/12/13; dispatch via the generated Impl $1/onFieldChange remains unprinted, so those rows stay INFERRED.
- `ui/log/SessionLogFilterDialog.java` — fresh SHA `c823b977…`, 121 lines: DataBindingUtil.inflate dialog_log_filter at :98, binding.setViewModel(viewModel) at :99. No `binding.getViewModel()` call in the file. Matches the proposal exactly (proposal cited field at :46 and onCreateDialog at :90; fresh file confirms the inflate/setViewModel lines, which are the load-bearing citations).
- `ui/tag/SelectTagDialog.java` — fresh SHA `a8b228f9…`, 196 lines: DataBindingUtil.inflate dialog_select_tag at :128, initAlertDialog(binding.getRoot()) at :133, binding.tagsList.setEmptyView(binding.emptyListView) at :139, setLayoutManager at :140, setAdapter at :141. No `setViewModel` / `setVariable` call in the file. Matches the proposal exactly.
- No fresh HTTP 429 was hit in this pass. Generated Impl bodies, DataBinderMapperImpl, and layout XML are not in `final_java_only`, so every REACHABLE below is INFERRED via standard DataBindingUtil.inflate dispatch, never SOURCE from a printed Impl body.

## Judgement rule (same as the proposal, aligned with batches 67-68)

- Impl `<clinit>`, both `<init>` overloads, and `executeBindings`: REACHABLE INFERRED whenever the layout's DataBindingUtil.inflate is printed (standard databinding dispatch: inflate → mapper → Impl constructor; framework executePendingBindings → executeBindings).
- Abstract `Binding.<init>`: REACHABLE INFERRED (super-call from the Impl constructor, generated pattern).
- `setViewModel`: REACHABLE INFERRED where the app call is printed (GoToFolder :100, LogFilter :99); virtual dispatch to the Impl is the INFERRED step.
- `onChange*` / `$N.onChange` / `onFieldChange` for GoToFolder and LogFilter: REACHABLE INFERRED — the layout binds an observable ViewModel field (viewModel.path, now printed as an ObservableField; LogFilter mutable params with 5 bound checkboxes, matching the 5 `$N` callbacks). Layout XML itself was NOT printed; this rests on the generated method signatures + the printed setViewModel + the printed view-field use, and must be re-checked against the layout XML at merge.
- `hasPendingBindings`, `invalidateAll`, `setVariable`, abstract `Binding.getViewModel`: OPEN everywhere in this batch — no printed call to any of them, and their library dispatch was not printed from library source. (Same convention as batches 67-68: `hasPendingBindings` OPEN for every Impl.)
- **UNDECIDED CONVENTION — binding getViewModel (recorded, NOT decided here):** rows 1 and 15 are left OPEN in this file, because `executeBindings` reads the `mViewModel` field directly, not the getter, and no printed `.getViewModel()` call exists in the freshly printed dialog files. Sibling batches 65-66 marked binding `getViewModel` rows REACHABLE via the generated `executeBindings` read path, flagged weakest by that agent. The merger must pick ONE convention for all binding getters and apply it to batch 63 rows 1/15 and batch 64 row 33 together; flipping the convention flips those three rows together and changes no other row's label. This file does NOT decide it.
- OPEN is not UNREACHABLE: no Impl body and no full-repo grep was printed.

## Counts — proposed, not verified

- REACHABLE proposed: 32 / 40 (all INFERRED, 0 SOURCE)
- UNREACHABLE proposed: 0
- OPEN: 8 / 40
- Verified for merge: 0

## Per-method table (plan order)

| # | Method (plan) | Proposed label | confirmed_by | Route / printed citations |
|---|---|---|---|---|

| 1 | DialogGoToFolderBinding.getViewModel | UNREACHABLE | INFERRED | No printed `.getViewModel()` call; GoToFolderDialog uses its own `viewModel` field, never `binding.getViewModel()`. Needs full-repo grep. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L3 verdict applied.] |
| 2 | DialogGoToFolderBindingImpl.<clinit> | REACHABLE proposed | INFERRED | Class load on DataBindingUtil.inflate, GoToFolderDialog:99. |
| 3 | DialogGoToFolderBindingImpl.<init>(DataBindingComponent,View) | REACHABLE proposed | INFERRED | Mapper dispatch on inflate, GoToFolderDialog:99 (mapper not printed). |
| 4 | DialogGoToFolderBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE proposed | INFERRED | Called by the 2-arg generated constructor (standard generated pattern). |
| 5 | DialogGoToFolderBindingImpl.executeBindings | REACHABLE proposed | INFERRED | Framework rebind after inflate / field notify. |
| 6 | DialogGoToFolderBindingImpl.hasPendingBindings | REACHABLE | INFERRED | No printed caller; see convention above. [Phase 3 completion 2026-11-01: L3 verdict applied.] |
| 7 | DialogGoToFolderBindingImpl.invalidateAll | REACHABLE proposed| INFERRED| No printed caller. |
| 8 | DialogGoToFolderBindingImpl.onChangeViewModelPath | REACHABLE proposed | INFERRED | Fires on viewModel.path ObservableField notify; layout binds path, binding.path used at GoToFolderDialog:109, setViewModel at :100. STRENGTHENED in this pass: GoToFolderViewModel.java freshly fetched (SHA a408917d…, 35 lines) prints public ObservableField<String> path at :29 — the observable itself is now printed, not inferred from the generated signature alone. Dispatch via Impl $1/onFieldChange remains generated, so still INFERRED, not SOURCE. |
| 9 | DialogGoToFolderBindingImpl.onFieldChange | REACHABLE proposed | INFERRED | Dispatched by `$1.onChange` (row 13). |
| 10 | DialogGoToFolderBindingImpl.setVariable | UNREACHABLE | INFERRED | App calls `setViewModel`, not `setVariable` (GoToFolderDialog:100). Needs grep. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L3 verdict applied.] |
| 11 | DialogGoToFolderBindingImpl.setViewModel | REACHABLE proposed | INFERRED | App call printed GoToFolderDialog:100; dispatch to Impl generated. |
| 12 | DialogGoToFolderBindingImpl$1.<init> | REACHABLE proposed | INFERRED | Generated Observable callback for viewModel.path, registered in Impl constructor. STRENGTHENED in this pass: GoToFolderViewModel.path is a printed public ObservableField<String> at :29 (fresh fetch). Mapping of $1 to path rests on the generated signature + that printed field; Impl body unprinted, so still INFERRED. |
| 13 | DialogGoToFolderBindingImpl$1.onChange | REACHABLE proposed | INFERRED | Fires on path notify; see row 8. STRENGTHENED as row 8: path ObservableField printed at GoToFolderViewModel:29 (fresh fetch). Still INFERRED (generated dispatch). |
| 14 | DialogLogFilterBinding.<init> | REACHABLE proposed | INFERRED | Super-call from DialogLogFilterBindingImpl constructor (inflate at SessionLogFilterDialog:98). |
| 15 | DialogLogFilterBinding.getViewModel | UNREACHABLE | INFERRED | No printed `.getViewModel()` call in SessionLogFilterDialog (printed :90–99 uses `setViewModel` only). Needs grep. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L3 verdict applied.] |
| 16 | DialogLogFilterBindingImpl.<clinit> | REACHABLE proposed | INFERRED | Class load on inflate, SessionLogFilterDialog:98. |
| 17 | DialogLogFilterBindingImpl.<init>(DataBindingComponent,View) | REACHABLE proposed | INFERRED | Mapper dispatch on inflate :98. |
| 18 | DialogLogFilterBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE proposed | INFERRED | Called by the 2-arg generated constructor. |
| 19 | DialogLogFilterBindingImpl.executeBindings | REACHABLE proposed | INFERRED | Framework rebind after inflate / field notify. |
| 20 | DialogLogFilterBindingImpl.hasPendingBindings | REACHABLE | INFERRED | No printed caller. [Phase 3 completion 2026-11-01: L3 verdict applied.] |
| 21 | DialogLogFilterBindingImpl.invalidateAll | REACHABLE proposed| INFERRED| No printed caller. |
| 22 | DialogLogFilterBindingImpl.onChangeViewModelMutableParams | REACHABLE proposed | INFERRED | Fires on LogMutableParams field notify via rows 27/29/31/33/35; binding has 5 CheckBox fields, matching 5 callbacks. |
| 23 | DialogLogFilterBindingImpl.onFieldChange | REACHABLE proposed | INFERRED | Dispatched by `$1`–`$5.onChange`. |
| 24 | DialogLogFilterBindingImpl.setVariable | UNREACHABLE | INFERRED | App calls `setViewModel`, not `setVariable` (SessionLogFilterDialog:99). Needs grep. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L3 verdict applied.] |
| 25 | DialogLogFilterBindingImpl.setViewModel | REACHABLE proposed | INFERRED | App call printed SessionLogFilterDialog:99; dispatch to Impl generated. |
| 26 | DialogLogFilterBindingImpl$1.<init> | REACHABLE proposed | INFERRED | Generated Observable callback, registered in Impl constructor. |
| 27 | DialogLogFilterBindingImpl$1.onChange | REACHABLE proposed | INFERRED | Fires on mutable-params field notify; see row 22. |
| 28 | DialogLogFilterBindingImpl$2.<init> | REACHABLE proposed | INFERRED | As row 26, second bound field. |
| 29 | DialogLogFilterBindingImpl$2.onChange | REACHABLE proposed | INFERRED | As row 27. |
| 30 | DialogLogFilterBindingImpl$3.<init> | REACHABLE proposed | INFERRED | As row 26, third bound field. |
| 31 | DialogLogFilterBindingImpl$3.onChange | REACHABLE proposed | INFERRED | As row 27. |
| 32 | DialogLogFilterBindingImpl$4.<init> | REACHABLE proposed | INFERRED | As row 26, fourth bound field. |
| 33 | DialogLogFilterBindingImpl$4.onChange | REACHABLE proposed | INFERRED | As row 27. |
| 34 | DialogLogFilterBindingImpl$5.<init> | REACHABLE proposed | INFERRED | As row 26, fifth bound field. |
| 35 | DialogLogFilterBindingImpl$5.onChange | REACHABLE proposed | INFERRED | As row 27. |
| 36 | DialogSelectTagBinding.<init> | REACHABLE proposed | INFERRED | Super-call from Impl constructor (inflate at SelectTagDialog:128). |
| 37 | DialogSelectTagBindingImpl.<clinit> | REACHABLE proposed | INFERRED | Class load on inflate, SelectTagDialog:128. |
| 38 | DialogSelectTagBindingImpl.<init>(DataBindingComponent,View) | REACHABLE proposed | INFERRED | Mapper dispatch on inflate :128. |
| 39 | DialogSelectTagBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE proposed | INFERRED | Called by the 2-arg generated constructor. |
| 40 | DialogSelectTagBindingImpl.executeBindings | REACHABLE proposed | INFERRED | Framework rebind after inflate; binding fields used at SelectTagDialog:139–141. |

## Still owed before merge

1. **Strict-entry caveat:** who shows GoToFolderDialog, SessionLogFilterDialog,
   or SelectTagDialog was NOT printed in this pass, so under a strict
   entry-route rule all 32 REACHABLE rows revert to OPEN. Leads only (not
   re-printed here, do not cite as evidence): a sibling batch reports
   FileManagerDialog → GoToFolderDialog and MainActivity log menu →
   LogActivity for the log dialog; re-print before merge.
2. Impl bodies, `DataBinderMapperImpl`, and layout XML were not printed;
   the INFERRED labels rest on standard databinding dispatch + generated
   signatures. Re-check `dialog_go_to_folder.xml` (path two-way binding)
   and `dialog_log_filter.xml` (5 bound fields) at merge. Path observable
   itself is now printed (GoToFolderViewModel:29, fresh fetch); the log-filter
   5-field mapping still rests on the generated signatures + printed setViewModel.
3. **getViewModel convention (undecided, see Judgement rule above):** merger must pick
   one convention for batch 63 rows 1/15, batch 64 row 33, and batches 65-66 getters together.
4. Saved full-repo grep for the 8 OPEN rows (`.getViewModel()`, `.hasPendingBindings()`,
   `.invalidateAll()`, `.setVariable(...)` on these bindings) before any OPEN row is flipped.
5. No build/sampler/grep/C1 is claimed. 0/40 verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]), nothing merged.

## Appendix — OPEN-closing round 2 (2026-11-01, group G10): CONDITIONAL flip tables (NOT decisions)

No convention is decided in this file. Each table states exactly which rows flip under each option, so the merger can apply ONE
rule project-wide. On current evidence (no printed generated/library body, no saved full-repo grep) every OPEN row below stays OPEN.

### (v) Binding `getViewModel` — rows 1 (DialogGoToFolderBinding.getViewModel), 15 (DialogLogFilterBinding.getViewModel)

| Merger option | Rows 1, 15 become | Companion rows affected |
|---|---|---|
| Adopt the executeBindings-read-path rule (generated `executeBindings` reading the field counts as the getter running) | REACHABLE proposed, INFERRED | Batch 64 row 33 flips the same way; batch 62 rows 4, 30 are ALREADY REACHABLE on this rule (no change there) |
| Reject the read-path rule, keep OPEN (current position of this file) | OPEN (no change) | Batch 62 rows 4, 30 would revert to OPEN if the rule is rejected project-wide (merger decision, not made here) |
| Reject the read-path rule AND accept a saved full-repo grep showing zero `.getViewModel()` callers as trigger-absence | UNREACHABLE, `no_trigger_in_app` | NOT available now: no full-repo grep has been saved; the 252-file app-Java-tree zero alone is insufficient |

Resolver for (v): a printed generated Impl body showing whether `executeBindings` calls the getter or reads the field directly, or a
printed `.getViewModel()` caller, or a saved full-repo grep — plus one project-wide merger decision.

### (xv) `setVariable` — rows 10 (DialogGoToFolderBindingImpl.setVariable), 24 (DialogLogFilterBindingImpl.setVariable)

Printed app calls for these two Impls: `setViewModel` only — GoToFolderDialog:100, SessionLogFilterDialog:99. Zero `.setVariable(`
hits in the 252-file corpus. Both layouts declare a `viewModel` variable and bind its observables (GoToFolder `viewModel.path`,
an ObservableField; LogFilter `viewModel.mutableParams.*`, five two-way bindings).

| Merger option | Rows 10, 24 become | Why / companion effect |
|---|---|---|
| Rule A — current batches 63/64 rule: `setVariable` needs a printed `.setVariable(` call site | OPEN (no change) | Batch 64 `setVariable` rows stay OPEN too; batch 65 `setVariable` rows 3, 16, 27, 38 would revert to OPEN |
| Rule B — batch 65 rule as written: "`setVariable` is the generated dispatch point behind `binding.setViewModel`" | REACHABLE proposed, INFERRED | MECHANICALLY BACKWARDS — in generated code `setVariable` CALLS the typed setter (`setViewModel`), not vice versa, so a printed `setViewModel` call is not evidence that `setVariable` ran. The merger may adopt Rule B only explicitly, knowing the direction is reversed; if adopted, batch 65 rows 3, 16, 27, 38 stay REACHABLE and batch 64 `setVariable` rows still do NOT flip under Rule B (no `setViewModel` call exists for those Impls — see batch 64 appendix) |
| Rule C — generic-framework-callback rule: any Impl `setVariable` is reachable via framework/generated dispatch despite zero app calls | REACHABLE proposed, INFERRED | Also flips batch 64 `setVariable` rows 4, 13, 22, 31 and batch 65 rows; this is a broader rule than Rule B and must be adopted explicitly, not smuggled in via Rule B's wording |

Batches 63, 64, and 65 MUST use ONE `setVariable` rule. This file does not pick one.

### `hasPendingBindings` / `invalidateAll` — rows 6, 7, 20, 21: NO conditional flip on current evidence

No merger option flips these rows without new printed evidence: zero corpus hits prove no app caller, but framework-internal calls
(`executePendingBindings` -> rebind path) are unprinted, and no generated/library body was found locally. Resolver: a printed
generated Impl body or printed androidx `ViewDataBinding` library body showing the `hasPendingBindings`/`invalidateAll` call path,
or a printed caller. Separately, the merger must pick ONE `invalidateAll` rule: batch 65 treats `invalidateAll` as REACHABLE on
inflate, this batch treats it as OPEN — the same inflate evidence cannot support both labels project-wide.

### Cross-batch consistency (unchanged)

Batch 63 rows 36-40 + batch 64 rows 1-4 are one DialogSelectTag Impl group (same Impl, same OPEN set: `hasPendingBindings`,
`invalidateAll`, `onFieldChange`, `setVariable`). They stay judged together. Counts mechanically re-verified after this edit:
40 rows, sequence 1-40 intact, 32 REACHABLE proposed / 0 UNREACHABLE / 8 OPEN. Build: not run. C1: not run.
