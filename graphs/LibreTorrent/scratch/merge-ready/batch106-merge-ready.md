# LibreTorrent batch 106 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler or full-repo grep was run
or is claimed in this file. No `search_code` result was used as evidence for any row.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 106 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior batch-106 proposal
  (`~/workspace/libretorrent-batch106-proposal.md`) was used as an INPUT / lead list only;
  every row below was re-judged against source freshly fetched in this pass, and no
  prior verdict was copied as a result.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 106 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from
the local plan copy `~/workspace/agent27-plan.tsv` (4,733 lines incl. header; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`), all `TODO_CANDIDATE_REACHABLE`
(generator candidates, not evidence), in plan order:
6 LogActivity rows, 2 LogActivity$1 rows, 3 LogActivity$2 rows, 10 LogAdapter rows,
5 LogDataSource rows, 14 LogMutableParams rows. Rows 1–40 below are those 40 rows,
in plan order.

## Printed source used in this pass

All files freshly connector-fetched from branch `work-2026-10-31`, one file at a time
with pauses, saved in `~/workspace/b105-106-src/` (base path
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`).
No fresh HTTP 429 was hit in this pass.

- `ui/log/LogActivity.java` — 470 lines, SHA `3569e10e4b0dd52e9f5f69dd7b5ee60fdd0116f1`.
- `ui/log/LogAdapter.java` — 112 lines, SHA `4b5f83de94b76cdce46cd154227c48eef5e3da42`.
- `ui/log/LogDataSource.java` — 118 lines, SHA `db760e765f36f46642c153c5f34a4ea564ee212f`.
- `ui/log/LogSourceFactory.java` — 43 lines, SHA `14a5c1dc94ce2ee970e887dde9f3f3f143f9a01e`.
- `ui/log/LogMutableParams.java` — 121 lines, SHA `e994c2d9be388ef09d73262abfcb1501b5d1f162`.
- `ui/log/LogViewModel.java` — 227 lines, SHA `f6374daf682f89108f17eb211a0dbefdbb962462`.
- `ui/main/MainActivity.java` — 811 lines, SHA `d21f8b70fb50fa09c7b3708243c4f251176f4517`
  — **new in this pass** (see route L).

All SHAs are byte-identical to the prior proposal's SHAs; line counts differ by one in
some files only because of trailing-newline counting.

## Shared routes (printed steps, cited once here and reused by row)

**L — MainActivity menu -> LogActivity (NEW in this pass, freshly printed).**
MainActivity.onOptionsItemSelected :754-755 (`R.id.log_menu` -> showLog()) ->
showLog() :801-802 (`startActivity(new Intent(this, LogActivity.class))`) ->
framework activity instantiation (INFERRED) -> LogActivity lifecycle.
This replaces the prior proposal's sibling-agent lead, which is now printed evidence.
The remaining strict-entry gap for LogActivity rows is only the launcher -> MainActivity
step, which was NOT freshly printed in this pass (AndroidManifest.xml was not fetched
here; the batch 107–108 report's manifest:43, MAIN/LAUNCHER:53-55 is a lead only, not
fresh evidence here). Under a strict launcher-to-leaf rule, rows 1–11 revert to OPEN on
that single unprinted step alone. This strict-entry convention is UNDECIDED at project
level; it is recorded here per row, not decided.
Inside LogActivity (freshly printed): onCreate :77-147 sets adapter = new LogAdapter(this) :116,
setAdapter :117, observeLog observer :119-120, addOnScrollListener(scrollCallback) :122;
scrollCallback is the LogActivity$2 anonymous class :338-406; paramsCallback is the
LogActivity$1 anonymous class :175-183, registered in onStart :172 and removed in
onStop :164. showFabUp :408-413 (postDelayed hideFabUpRunnable :412), showFabDown
:422-426 (postDelayed hideFabDownRunnable :425), hideFabUp :415-419, hideFabDown
:429-432; onOptionsItemSelected :232-248 routes to showFilterDialog :250-257
(SessionLogFilterDialog.newInstance + show), showLogSettings :259-262 (startActivity
LogSettingsActivity), toggleRecord :281-302, updateToolbarSubtitle :443-450
(viewModel.getLogEntriesCount).

**A — LogAdapter (freshly printed in LogAdapter.java).**
LogActivity:116 new LogAdapter(this) -> LogAdapter.<init> :39-44 (super(diffCallback) :41,
listener field :43). diffCallback static field :67-82 is a DiffUtil.ItemCallback
anonymous class ($1): areContentsTheSame :70-74 (oldItem.equals(newItem) :73),
areItemsTheSame :77-81 (getId comparison :80). RecyclerView/PagedListAdapter dispatch
(INFERRED, library code not printed) -> onCreateViewHolder :48-57 (inflate
R.layout.item_log_list :51-54, return new ViewHolder(binding) :56) ->
ViewHolder.<init> :93-98 -> onBindViewHolder :60-65 (getItem :62, holder.bind(entry,
listener) :64) -> ViewHolder.bind :100-110 (itemView.setOnClickListener lambda :102-105
-> listener.onItemClicked(entry) :104, tag/msg/timeStamp text :107-109).

**D — LogDataSource via LogViewModel / LogSourceFactory (freshly printed).**
LogActivity:92 ViewModelProvider.get(LogViewModel.class) -> LogViewModel.<init> :65-78:
sourceFactory = new LogSourceFactory(sessionLogger) :75, initMutableParams() :77.
LogSourceFactory.create :39-42 returns new LogDataSource(logger) :41. LogDataSource.<init>
:38-44 subscribes logger.observeDataSetChanged() -> invalidate() :42-43 (Rx dispatch
INFERRED). Paging framework dispatch (INFERRED, library code not printed) ->
loadInitial :55-90 and loadRange :93-117 (both call logger.isPaused/getNumEntries/getEntries/
pause/resume). Paging framework may also call invalidate() :47-52 (disposable.dispose :49,
super.invalidate :51).

**M — LogMutableParams via LogViewModel (freshly printed).**
LogViewModel field :56 mutableParams = new LogMutableParams() (construction site printed;
LogViewModel itself is created via ViewModelProvider at LogActivity:92, framework dispatch
INFERRED upstream). LogViewModel.initMutableParams :80-90 calls setLogging :82,
setLogSessionFilter :83, setLogDhtFilter :84, setLogPeerFilter :85, setLogPortmapFilter :86,
setLogTorrentFilter :87. LogViewModel.paramsCallback :107-138 (data-binding Observable
dispatch INFERRED) calls isLogging :114, isLogSessionFilter :122, isLogDhtFilter :125,
isLogPeerFilter :128, isLogPortmapFilter :131, isLogTorrentFilter :134. LogActivity
onPrepareOptionsMenu :206 also calls mutableParams.isLogging(). Definitions in
LogMutableParams.java: isLogging :37-40, setLogging :42-46, isLogSessionFilter :49-52,
setLogSessionFilter :54-58, isLogDhtFilter :60-64, setLogDhtFilter :66-70,
isLogPeerFilter :72-76, setLogPeerFilter :78-82, isLogPortmapFilter :84-88,
setLogPortmapFilter :90-94, isLogTorrentFilter :96-100, setLogTorrentFilter :102-106,
toString :110-120. Note: setLogPortmapFilter :93 notifies BR.logPeerFilter, not
BR.logPortmapFilter — a source oddity, not a reachability change.

**confirmed_by convention used here (per-row, not whole-route; UNDECIDED at project level,
recorded not decided):** SOURCE = the row's immediate call site is printed app code;
INFERRED = the row is reached only through a framework/library dispatch step
(lifecycle, menu, RecyclerView/Paging/DiffUtil/Rx/data-binding/Observable, JVM class
initialisation, field-initialiser execution during framework activity creation) that was
not printed from fw_src. Under a whole-route INFERRED convention, SOURCE rows would
change confirmed_by only; labels are unaffected.

## Counts — batch 106, proposed not verified

- REACHABLE proposed: 39
  - SOURCE: 23
  - INFERRED: 16
- UNREACHABLE proposed: 0
- OPEN: 1 (LogMutableParams.toString, row 40)
- Total: 40
- Verified for merge: 0

## Per-method table (all 40 rows, in plan order)

| # | Method | Label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | LogActivity.showFabDown | REACHABLE | SOURCE | LogActivity.java:349/:367 scroll callbacks call showFabDown; def :422-426; route L |
| 2 | LogActivity.showFabUp | REACHABLE | SOURCE | LogActivity.java:352/:370 scroll callbacks call showFabUp; def :408-413; route L |
| 3 | LogActivity.showFilterDialog | REACHABLE | SOURCE | LogActivity.java:242 onOptionsItemSelected calls showFilterDialog; def :250-257 (SessionLogFilterDialog.newInstance + show) |
| 4 | LogActivity.showLogSettings | REACHABLE | SOURCE | LogActivity.java:244 onOptionsItemSelected calls showLogSettings; def :259-262 (startActivity LogSettingsActivity) |
| 5 | LogActivity.toggleRecord | REACHABLE | SOURCE | LogActivity.java:238 onOptionsItemSelected calls toggleRecord; def :281-302 |
| 6 | LogActivity.updateToolbarSubtitle | REACHABLE | SOURCE | LogActivity.java:102 onCreate, :440 handleUpdateAdapter; def :443-450 |
| 7 | LogActivity$1.<init> | REACHABLE | INFERRED | LogActivity.java:175-183 paramsCallback field (anonymous OnPropertyChangedCallback); field runs during framework activity creation, dispatch INFERRED; registered onStart :172 |
| 8 | LogActivity$1.onPropertyChanged | REACHABLE | INFERRED | Data-binding Observable dispatch INFERRED; def LogActivity.java:178-182 (BR.logging -> invalidateOptionsMenu) |
| 9 | LogActivity$2.<init> | REACHABLE | INFERRED | LogActivity.java:338-406 scrollCallback field (anonymous OnScrollListener); field runs during framework activity creation, dispatch INFERRED; registered :122 |
| 10 | LogActivity$2.onScrollStateChanged | REACHABLE | INFERRED | RecyclerView dispatch INFERRED; def LogActivity.java:359-405 (calls show/hide fabs, updates scrollPosition/autoScroll) |
| 11 | LogActivity$2.onScrolled | REACHABLE | INFERRED | RecyclerView dispatch INFERRED; def LogActivity.java:343-356 (calls hide/show fabs on dy direction) |
| 12 | LogAdapter.<clinit> | REACHABLE | INFERRED | JVM class initialisation INFERRED on first LogAdapter reference (LogActivity.java:116); static diffCallback field LogAdapter.java:67 |
| 13 | LogAdapter.<init> | REACHABLE | SOURCE | LogActivity.java:116 new LogAdapter(this); def LogAdapter.java:39-44; route A |
| 14 | LogAdapter.onBindViewHolder | REACHABLE | INFERRED | RecyclerView/PagedListAdapter dispatch INFERRED; def LogAdapter.java:60-65 (holder.bind :64) |
| 15 | LogAdapter.onCreateViewHolder | REACHABLE | INFERRED | RecyclerView/PagedListAdapter dispatch INFERRED; def LogAdapter.java:48-57 (new ViewHolder :56) |
| 16 | LogAdapter$1.<init> | REACHABLE | INFERRED | Anonymous DiffUtil.ItemCallback, static field LogAdapter.java:67; runs at class initialisation, INFERRED (see row 12) |
| 17 | LogAdapter$1.areContentsTheSame | REACHABLE | INFERRED | DiffUtil library dispatch INFERRED; def LogAdapter.java:70-74 (oldItem.equals :73) |
| 18 | LogAdapter$1.areItemsTheSame | REACHABLE | INFERRED | DiffUtil library dispatch INFERRED; def LogAdapter.java:77-81 (getId comparison :80) |
| 19 | LogAdapter$ViewHolder.<init> | REACHABLE | SOURCE | LogAdapter.java:56 onCreateViewHolder returns new ViewHolder(binding); def :93-98 |
| 20 | LogAdapter$ViewHolder.bind | REACHABLE | SOURCE | LogAdapter.java:64 onBindViewHolder calls holder.bind(entry, listener); def :100-110 |
| 21 | LogAdapter$ViewHolder.lambda$bind$0 | REACHABLE | INFERRED | Click listener registered LogAdapter.java:102; framework View-click dispatch INFERRED; body :102-105 calls listener.onItemClicked(entry) (LogActivity.onItemClicked, batch 105 row 31) |
| 22 | LogDataSource.<init> | REACHABLE | SOURCE | LogSourceFactory.java:41 create() returns new LogDataSource(logger); def LogDataSource.java:38-44; route D |
| 23 | LogDataSource.invalidate | REACHABLE | INFERRED | Rx subscribe lambda LogDataSource.java:43 calls invalidate(); Rx/Paging dispatch INFERRED; def :47-52 |
| 24 | LogDataSource.lambda$new$0 | REACHABLE | INFERRED | Rx subscribe lambda LogDataSource.java:42-43 ((__) -> invalidate()); Rx dispatch INFERRED |
| 25 | LogDataSource.loadInitial | REACHABLE | INFERRED | Paging framework dispatch INFERRED; def LogDataSource.java:55-90 (logger.getNumEntries/getEntries/pause/resume) |
| 26 | LogDataSource.loadRange | REACHABLE | INFERRED | Paging framework dispatch INFERRED; def LogDataSource.java:93-117 |
| 27 | LogMutableParams.<init> | REACHABLE | SOURCE | LogViewModel.java:56 field mutableParams = new LogMutableParams(); LogViewModel created via ViewModelProvider at LogActivity.java:92 (framework dispatch INFERRED upstream); route M |
| 28 | LogMutableParams.isLogDhtFilter | REACHABLE | SOURCE | LogViewModel.java:125 paramsCallback calls isLogDhtFilter; def LogMutableParams.java:60-64 |
| 29 | LogMutableParams.isLogPeerFilter | REACHABLE | SOURCE | LogViewModel.java:128 paramsCallback calls isLogPeerFilter; def LogMutableParams.java:72-76 |
| 30 | LogMutableParams.isLogPortmapFilter | REACHABLE | SOURCE | LogViewModel.java:131 paramsCallback calls isLogPortmapFilter; def LogMutableParams.java:84-88 |
| 31 | LogMutableParams.isLogSessionFilter | REACHABLE | SOURCE | LogViewModel.java:122 paramsCallback calls isLogSessionFilter; def LogMutableParams.java:49-52 |
| 32 | LogMutableParams.isLogTorrentFilter | REACHABLE | SOURCE | LogViewModel.java:134 paramsCallback calls isLogTorrentFilter; def LogMutableParams.java:96-100 |
| 33 | LogMutableParams.isLogging | REACHABLE | SOURCE | LogViewModel.java:114 paramsCallback and LogActivity.java:206 onPrepareOptionsMenu call isLogging; def LogMutableParams.java:37-40 |
| 34 | LogMutableParams.setLogDhtFilter | REACHABLE | SOURCE | LogViewModel.java:84 initMutableParams calls setLogDhtFilter; def LogMutableParams.java:66-70 |
| 35 | LogMutableParams.setLogPeerFilter | REACHABLE | SOURCE | LogViewModel.java:85 initMutableParams calls setLogPeerFilter; def LogMutableParams.java:78-82 |
| 36 | LogMutableParams.setLogPortmapFilter | REACHABLE | SOURCE | LogViewModel.java:86 initMutableParams calls setLogPortmapFilter; def LogMutableParams.java:90-94 (notifies BR.logPeerFilter :93) |
| 37 | LogMutableParams.setLogSessionFilter | REACHABLE | SOURCE | LogViewModel.java:83 initMutableParams calls setLogSessionFilter; def LogMutableParams.java:54-58 |
| 38 | LogMutableParams.setLogTorrentFilter | REACHABLE | SOURCE | LogViewModel.java:87 initMutableParams calls setLogTorrentFilter; def LogMutableParams.java:102-106 |
| 39 | LogMutableParams.setLogging | REACHABLE | SOURCE | LogViewModel.java:82 initMutableParams calls setLogging; def LogMutableParams.java:42-46 |
| 40 | LogMutableParams.toString | OPEN | — | Def LogMutableParams.java:110-120 printed. No caller printed in any file fetched in this pass (LogActivity, LogAdapter, LogDataSource, LogSourceFactory, LogMutableParams, LogViewModel, GoToFolderDialog, GoToFolderViewModel, FileManagerDialog, MainActivity — grep of those files finds only LogEntry.toString() at LogViewModel.java:222 and unrelated String toString() calls, never LogMutableParams.toString). NOT flipped to UNREACHABLE: toString is commonly reached via logging/concatenation, and no saved full-repo grep was done. Highest-priority grep target for this batch, as tasked. |

## Remaining before merge

- Printed launcher -> MainActivity step (AndroidManifest.xml, not fetched in this pass),
  if a strict launcher-anchored route is required for LogActivity rows 1–11. The
  LogActivity starter itself is now freshly printed (MainActivity :754-755, :801-802).
- Saved full-repo grep for LogMutableParams.toString (row 40, OPEN) before any
  UNREACHABLE decision; that grep also confirms no other caller was missed for the
  REACHABLE rows.
- Main-agent spot-check (1 in 5), py_compile, build, Mac build/C1 — not run, never claimed.
