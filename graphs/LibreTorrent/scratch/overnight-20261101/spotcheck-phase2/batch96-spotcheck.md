# Stream A Phase 2 spot-check — 96 — UNVERIFIED spot-check, NOT a merge decision
Scope: batch 96 only, LibreTorrent labels only. Source file checked: ~/workspace/overnight/stream-A/work/batch96-merge-ready.md (UNVERIFIED proposal, not a result).
Method: each row below was re-derived from printed source, searched in already-fetched local copies first (~/workspace/overnight/stream-A/corpus/, 281 app-Java files; ~/workspace/b9192-src/; ~/workspace/b90929495969799102-openclose-src/; ~/workspace/overnight/stream-A/greps/). No merge-ready file was edited, no tick written, no push made. Build/sampler/C1: not run (not this task).
Verdict rule used: PASS = the row's label is correct and its controlling evidence (including any dated 2026-11-01 revision note in the file, which supersedes older row text) locates the route. FAIL = the label is wrong, or the stated evidence mislocates the route (wrong caller/branch) with no superseding note. Two things are NOT failed: (a) confirmed_by SOURCE vs INFERRED on lifecycle/framework rows — both are permitted values and the classification convention is not decided here; (b) lambda/anonymous $ numbering, which the work files themselves state is source-order, NOT bytecode-verified, and a swap within a group would not change any label. Off-by-one definition spans are noted as corrections, not failures. A row turning on an undecided project convention is left as-is and flagged, never decided here.
No fresh 429 occurred in this pass (4 connector fetches, batch 99 only, one at a time with ~30 s pauses; no token used).

Rows checked (9): sample rows 1, 6, 11, 16, 21, 26, 31, 36, PLUS Phase-1 changed row 40 (OPEN → UNREACHABLE, grep-flip re-check SURVIVED).

- Row 1 TrackerListAdapter.onCreateViewHolder — PASS (REACHABLE, INFERRED). Definition :70-79 (inflates item_trackers_list, new ViewHolder :78); RecyclerView dispatch INFERRED.
- Row 6 TrackerListAdapter$1.areItemsTheSame — PASS (REACHABLE, INFERRED). Definition :125-130, calls oldItem.equals :128; DiffUtil dispatch INFERRED.
- Row 11 TrackerListAdapter$ItemLookup.getItemDetails — PASS (REACHABLE, INFERRED). Definition :287-296 (findChildViewUnder → ViewHolder.getItemDetails :293); SelectionTracker dispatch INFERRED.
- Row 16 TrackerListAdapter$ViewHolder.bind — PASS (REACHABLE, SOURCE). Called by onBindViewHolder :88; definition :152-207 (row cites :152-207; bind closes at :208 after a.recycle() :207 — immaterial).
- Row 21 ErrorReportActivity.finish — PASS (REACHABLE, SOURCE). Called from handleAlertDialogEvent POSITIVE branch :108 and NEGATIVE branch :113; definition :119-125 (dismisses errDialog, super.finish()).
- Row 26 ErrorReportActivity.onStop — PASS (REACHABLE, INFERRED). Definition :74-80 (disposables.clear :78); lifecycle dispatch INFERRED.
- Row 31 ErrorReportDialog.lambda$initLayoutView$0 — PASS (REACHABLE, INFERRED). Click listener set in initLayoutView :79-82 (toggle :80-81); view-click dispatch INFERRED; $ index source-order, not bytecode-verified.
- Row 36 FeedItemsActivity.onCreate — PASS (REACHABLE, INFERRED). Definition :42-60; two-pane finish guard :47-50, setContentView activity_feed_items :52, fragment setFeedId :58; lifecycle dispatch INFERRED.
- Row 40 FeedItemsAdapter.getItemKey — PASS (UNREACHABLE stands). Definition :91-97 (Selectable implementation). FeedItemsFragment.java has zero SelectionTracker/KeyProvider/getItemKey/getItemPosition/Selectable hits (re-verified locally); the fragment uses the adapter only via construction :152, setAdapter :153, and submitList :218/:233. Complete-tree re-check (grep_recheck_selectable_setfilename_complete.txt): the only selectable.getItemKey call sites are the four KeyProvider getKey methods; FeedItemsAdapter has none. Same recorded framework premise as batch 94 rows 7-8, not re-decided here. Consistent with batch 97 row 1 (same adapter, same missing KeyProvider).

Totals: 9 rows checked — 9 PASS, 0 FAIL.
Proposed corrections: none to any label.
