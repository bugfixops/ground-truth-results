## Revision note — GREP-FLIP RE-CHECK, 2026-11-01 (UNVERIFIED, NOT merged, NO push)

Scope: Stream A Phase 1 worker, batches 85/86/94/96/97/102 ONLY. This file: row 40 re-checked against the COMPLETE app Java tree (281 files: ruleF 252 + branch-enumerated missing 29 = com.ernieyu.feedparser 28 + org.nanohttpd 1, enumerated via GitHub connector listings on branch work-2026-10-31, repo bugfixops/ground-truth-results) PLUS res layout XML (69 layout/ files, filename set verified identical to branch listing, + 4 variant-layout files fetched fresh via connector 2026-11-01). Build: not run. C1: not run.
Result: THE flip SURVIVED, label unchanged. Counts BEFORE = AFTER: 39 REACHABLE / 1 UNREACHABLE / 0 OPEN (mechanically verified from the label column, 40 rows, sequence 1-40 intact).
New evidence, saved under ~/workspace/overnight/stream-A/greps/grep_recheck_selectable_setfilename_complete.txt: the only selectable.getItemKey call sites in the 281 files are the four KeyProvider getKey methods (TorrentListAdapter :344, FeedChannelListAdapter :289, TrackerListAdapter :241, TorrentContentFilesAdapter :280); FeedItemsAdapter has no KeyProvider, FeedItemsFragment has no SelectionTracker, the fragment uses the adapter only via ClickListener and new FeedItemsAdapter(this) :152, and layouts contain no Selectable/SelectionTracker/KeyProvider/getItemKey/getItemPosition reference (only unrelated android:textIsSelectable attributes). Consistent with batch 97 row 1 (same adapter, same missing KeyProvider).

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

**OPEN-CLOSING REVISION 2026-11-01 (UNVERIFIED, no push, no merge): 0 label changes. Counts before = after: 39 REACHABLE / 0 UNREACHABLE / 1 OPEN (row 40).**
**OPEN-CLOSING ROUND 2 REVISION 2026-11-01 (UNVERIFIED, no push, no merge): 1 label change: row 40 OPEN → UNREACHABLE on saved 252-file app-Java greps in /home/hatch/workspace/b90929495969799102-openclose2-src/. Counts before 39 REACHABLE / 0 UNREACHABLE / 1 OPEN → after 39 / 1 / 0. Flips together with batch 97 row 1 (same adapter, same missing KeyProvider). Build: not run. C1: not run. 0 rows verified for merge.**
Fresh source for this pass saved in ~/workspace/b90929495969799102-openclose-src/ (branch work-2026-10-31, one file at a time with ~25 s pauses, no fresh HTTP 429; each file plus its raw connector JSON saved; fresh-corpus grep in grep_fresh_corpus.txt — a PRINTED-SUBSET grep only, NOT a saved full-repo grep, so it cannot flip any row to UNREACHABLE).
Fresh files re-verified for the OPEN row: `ui/feeditems/FeedItemsAdapter.java` (184 lines, SHA bf28a46f9c2f149b4557aefe5308c5310fab23c4), `ui/feeditems/FeedItemsFragment.java` (329 lines, SHA c612894b16f58bf5c7780fa683a4a8cbcefda97f).
Row 40: getItemKey definition re-confirmed fresh at FeedItemsAdapter.java:91-97; the adapter itself has no inner KeyProvider and no SelectionTracker reference (only the Selectable import :40 and interface :49). Fresh FeedItemsFragment.java has ZERO hits for SelectionTracker/KeyProvider/getItemKey/getItemPosition/Selectable and uses the adapter only via new FeedItemsAdapter(this) :152, setAdapter :153, submitList :218/:233 (DiffUtil, not getItemKey). Consistent with batch 97 row 1 (getItemPosition OPEN) and batch 94 rows 7-8 (peers Selectable OPEN); contrast batch 99 rows 21-22/38-39 where the feed adapter's KeyProvider calls getItemKey/getItemPosition. Row 40 stays OPEN; named target: a saved full-repo grep for an external Selectable/KeyProvider consumer of FeedItemsAdapter. Lead-only cross-check (NOT fresh evidence, NOT a full-repo grep): no external getItemKey/getItemPosition consumer for this adapter in the parent's 252-file app-Java reconstruction. Build: not run. C1: not run. 0 rows verified for merge.


# LibreTorrent batch 96 — MERGE-READY — UNVERIFIED

Branch: work-2026-10-31, repo bugfixops/ground-truth-results. Local only — NO push
(pushed UNVERIFIED before [L] at user request 2026-11-01), no edit to graph_def.py, out/,
PROGRESS_V2, AGENT_NOTES, tools/, or another helper's file.

Membership: exactly the 40 plan rows of handoff/LIBRETORRENT_BATCH_PLAN.tsv batch 96
(local copy ~/workspace/agent27-plan.tsv, git blob SHA
0104806dd666c840049b3db52823d4b384fa1c92), all TODO_CANDIDATE_REACHABLE, sequence
1–40 intact, in plan order. Prior proposal (~/workspace/libretorrent-batch96-proposal.md)
was used as a lead list only; every row below was re-judged against source freshly
fetched in this pass. No row is copied on the proposal's authority alone.

Counts: 40 rows judged: **39 REACHABLE proposed (SOURCE 17 / INFERRED 22),
1 UNREACHABLE (row 40, round 2, SOURCE), 0 OPEN. 0/40 verified for merge.**

## Printed sources used (all freshly connector-fetched this pass, branch work-2026-10-31, one file at a time with ~25 s pauses, no fresh HTTP 429)

Saved in ~/workspace/b9596-src/ (same directory as the batch 95 pass):

- `ui/detailtorrent/pages/trackers/TrackerListAdapter.java` — 299 lines, connector SHA
  320b9e7722766b56e3aba2ddeabd593356cedec1 (rows 1–18).
- `ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java` — 406 lines,
  connector SHA 48d5a5360febbf5e8ac10f6b08d106d88aff0126 (selection-tracker
  construction :181–182, :224; adapter construction :160).
- `ui/errorreport/ErrorReportActivity.java` — 143 lines, connector SHA
  baf34c0ae8fec1acb348415d8429ea1d50c440e5 (rows 19–27).
- `ui/errorreport/ErrorReportDialog.java` — 84 lines, connector SHA
  04f19fd256e9a648606fef0fcf5532b99c9974b6 (rows 28–33).
- `ui/feeditems/FeedItemsActivity.java` — 67 lines, connector SHA
  951104d8d5c6c7d858bea615e35202ae078195e2 (rows 34–37).
- `ui/feeditems/FeedItemsAdapter.java` — 184 lines, connector SHA
  bf28a46f9c2f149b4557aefe5308c5310fab23c4 (rows 38–40).
- `ui/feeditems/FeedItemsFragment.java` — 329 lines, connector SHA
  c612894b16f58bf5c7780fa683a4a8cbcefda97f (adapter construction :152,
  submitList :218/:233, fragment→activity callback :320–327).
- `ui/detailtorrent/DetailTorrentFragment.java` — 832 lines, connector SHA
  c24e0912e62088e962894f04ee427bbe317e83e7 (second ErrorReportDialog.newInstance
  caller :557).
- `app/src/main/AndroidManifest.xml` — 295 lines, connector SHA
  875a8aa7de97caac5d9457836b0ea30f1c3d51ea (same SHA as the batch 109–110 pass):
  ErrorReportActivity declared :167–172 (theme Translucent, process ":acra",
  singleInstance), FeedItemsActivity declared :176.

Abbreviations in citations: "adapter" = TrackerListAdapter.java,
"fragment" = DetailTorrentTrackersFragment.java, "ERA" = ErrorReportActivity.java,
"ERD" = ErrorReportDialog.java, "FIA" = FeedItemsActivity.java,
"FIApt" = FeedItemsAdapter.java, "FIF" = FeedItemsFragment.java.
Line numbers are fresh-file lines.

## Entry notes (printed, with caveats)

- TrackerListAdapter rows (1–18): entry via the batch 95 trunk
  (DetailTorrentFragment → pager → DetailTorrentTrackersFragment.newInstance →
  onViewCreated :160/:181–182/:224). Strict-entry caveat as in batch 95.
- ErrorReportActivity rows (19–27): declared in the manifest as the ACRA-process
  activity (:167–172); the ACRA framework start that launches it was NOT printed,
  so activity lifecycle rows are INFERRED (external-library dispatch), not SOURCE.
- FeedItemsActivity rows (34–37): declared in the manifest :176; the in-app Intent
  that starts it was NOT printed in this pass, so its lifecycle rows are INFERRED.
  Its onFragmentFinished row (37) is SOURCE, not contract-only — see the row.
- FeedItemsAdapter rows (38–40): FIF (hosted by FIA's layout fragment container,
  FIA :54–59) constructs the adapter :152.

## confirmed_by convention used (per-row, recorded not decided)

SOURCE = a printed app-code line names the method (direct call, construction, or
method reference). INFERRED = the method runs only through unprinted
framework/library/Rx dispatch (RecyclerView, SelectionTracker, Activity/Dialog
lifecycle, Rx subscription) where definition and registration are printed. Under
a whole-route INFERRED convention, SOURCE rows whose route crosses unprinted
framework dispatch would read INFERRED; labels are unaffected. OPEN rows carry no
confirmed_by (shown as —), consistent with sibling merge-ready files.

## Rows

| # | Method | Label | confirmed_by | Printed route / citation |
|---|---|---|---|---|
| 1 | TrackerListAdapter.onCreateViewHolder (Landroid/view/ViewGroup;I)Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerListAdapter$ViewHolder; | REACHABLE | INFERRED | RecyclerView framework dispatch (standard adapter callback); definition adapter :70–79 (inflates item_trackers_list, `new ViewHolder(binding)` :78). Framework code not printed. |
| 2 | TrackerListAdapter.setSelectionTracker (Landroidx/recyclerview/selection/SelectionTracker;)V | REACHABLE | SOURCE | Called in fragment.onViewCreated :224 (`adapter.setSelectionTracker(selectionTracker)`); definition adapter :63–66. |
| 3 | TrackerListAdapter.submitList (Ljava/util/List;)V | REACHABLE | SOURCE | Called from subscribeAdapter subscribe lambda in fragment (`adapter.submitList(children)`, fragment :258–269, call at :268); definition adapter :92–98 (sorts, super.submitList). |
| 4 | TrackerListAdapter$1.<init> ()V | REACHABLE | INFERRED | Anonymous DiffUtil.ItemCallback (diffCallback) instantiated at class init (adapter :115); runs when the class is first used (`new TrackerListAdapter()`, fragment :160). $ numbering by source order, NOT bytecode-verified. |
| 5 | TrackerListAdapter$1.areContentsTheSame (Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerItem;Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerItem;)Z | REACHABLE | INFERRED | DiffUtil framework dispatch during ListAdapter diffing (definition adapter :118–123, calls oldItem.equalsContent); framework code not printed. |
| 6 | TrackerListAdapter$1.areItemsTheSame (Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerItem;Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerItem;)Z | REACHABLE | INFERRED | DiffUtil framework dispatch (definition adapter :125–130, calls oldItem.equals); framework code not printed. |
| 7 | TrackerListAdapter$ItemDetails.<init> (Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerItem;I)V | REACHABLE | SOURCE | Constructed by ViewHolder.getItemDetails (adapter :216–219, `new ItemDetails(selectionKey, getBindingAdapterPosition())`); definition adapter :256–260. |
| 8 | TrackerListAdapter$ItemDetails.getPosition ()I | REACHABLE | INFERRED | Selection framework dispatch (definition adapter :270–273, returns adapterPosition); framework code not printed. |
| 9 | TrackerListAdapter$ItemDetails.getSelectionKey ()Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerItem; | REACHABLE | INFERRED | Selection framework dispatch (definition adapter :264–267, returns selectionKey); framework code not printed. |
| 10 | TrackerListAdapter$ItemLookup.<init> (Landroidx/recyclerview/widget/RecyclerView;)V | REACHABLE | SOURCE | Constructed in fragment.onViewCreated :182 (`new TrackerListAdapter.ItemLookup(binding.trackerList)`); definition adapter :280–284. |
| 11 | TrackerListAdapter$ItemLookup.getItemDetails (Landroid/view/MotionEvent;)Landroidx/recyclerview/selection/ItemDetailsLookup$ItemDetails; | REACHABLE | INFERRED | SelectionTracker framework dispatch on touch (definition adapter :287–296, findChildViewUnder → ViewHolder.getItemDetails); framework code not printed. |
| 12 | TrackerListAdapter$KeyProvider.<init> (Lorg/proninyaroslav/libretorrent/ui/Selectable;)V | REACHABLE | SOURCE | Constructed in fragment.onViewCreated :181 (`new TrackerListAdapter.KeyProvider(adapter)`); definition adapter :230–236 (super SCOPE_MAPPED). |
| 13 | TrackerListAdapter$KeyProvider.getKey (I)Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerItem; | REACHABLE | INFERRED | SelectionTracker framework dispatch (definition adapter :239–242, `selectable.getItemKey(position)`); framework code not printed. |
| 14 | TrackerListAdapter$KeyProvider.getPosition (Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerItem;)I | REACHABLE | INFERRED | SelectionTracker framework dispatch (definition adapter :245–248, `selectable.getItemPosition(key)`); framework code not printed. |
| 15 | TrackerListAdapter$ViewHolder.<init> (Lorg/proninyaroslav/libretorrent/databinding/ItemTrackersListBinding;)V | REACHABLE | SOURCE | Constructed by onCreateViewHolder (adapter :78, `new ViewHolder(binding)`); definition adapter :145–151 (super(binding.getRoot())). |
| 16 | TrackerListAdapter$ViewHolder.bind (Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerItem;)V | REACHABLE | SOURCE | Called by onBindViewHolder (adapter :82–90, `holder.bind(item)` :88); definition adapter :152–207 (url/status/message binding). |
| 17 | TrackerListAdapter$ViewHolder.getItemDetails ()Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerListAdapter$ItemDetails; | REACHABLE | SOURCE | Called by ItemLookup.getItemDetails (adapter :293, `((ViewHolder)viewHolder).getItemDetails()`); definition adapter :216–219. |
| 18 | TrackerListAdapter$ViewHolder.setSelected (Z)V | REACHABLE | SOURCE | Called by onBindViewHolder (adapter :86, `holder.setSelected(selectionTracker.isSelected(item))`); definition adapter :210–213. |
| 19 | ErrorReportActivity.<clinit> ()V | REACHABLE | INFERRED | Static TAG field init (ERA :46, getSimpleName(), non-constant); runs on class load when the manifest-declared ACRA activity (manifest :167–172, process ":acra") starts. ACRA start not printed; <clinit>-on-first-use convention recorded, not decided. |
| 20 | ErrorReportActivity.<init> ()V | REACHABLE | INFERRED | Framework activity instantiation for the manifest-declared ACRA activity; no explicit in-app `new` (correct for an Activity). ACRA start not printed. |
| 21 | ErrorReportActivity.finish ()V | REACHABLE | SOURCE | Called from handleAlertDialogEvent (ERA :108 POSITIVE branch, :113 NEGATIVE branch); definition ERA :119–125 (dismisses errDialog, super.finish()). |
| 22 | ErrorReportActivity.getStackTrace ()Ljava/lang/String; | REACHABLE | SOURCE | Called from onCreate (ERA :67, argument to ErrorReportDialog.newInstance); definition ERA :127–143 (helper.getReportData → STACK_TRACE, null on IOException). |
| 23 | ErrorReportActivity.handleAlertDialogEvent (Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog$Event;)V | REACHABLE | INFERRED | Rx dispatch via method reference `this::handleAlertDialogEvent` subscribed in subscribeAlertDialog (ERA :91); definition ERA :95–117 (POSITIVE → helper.sendCrash + finish; NEGATIVE → helper.cancelReports + finish). Rx dispatch not printed. |
| 24 | ErrorReportActivity.onCreate (Landroid/os/Bundle;)V | REACHABLE | INFERRED | Framework activity lifecycle dispatch; definition ERA :55–72 (CrashReportDialogHelper, dialogViewModel, find/newInstance dialog + show). ACRA start not printed. |
| 25 | ErrorReportActivity.onStart ()V | REACHABLE | INFERRED | Framework activity lifecycle dispatch; definition ERA :82–87 (subscribeAlertDialog). |
| 26 | ErrorReportActivity.onStop ()V | REACHABLE | INFERRED | Framework activity lifecycle dispatch; definition ERA :74–80 (disposables.clear()). |
| 27 | ErrorReportActivity.subscribeAlertDialog ()V | REACHABLE | SOURCE | Called from onStart (ERA :86); definition ERA :89–93 (dialogViewModel.observeEvents().subscribe(this::handleAlertDialogEvent)). |
| 28 | ErrorReportDialog.<clinit> ()V | REACHABLE | INFERRED | Static TAG/TAG_DETAIL_ERROR field init (ERD :33/:35, TAG non-constant); runs on first class use via newInstance (see row 32). Class-init dispatch not printed. |
| 29 | ErrorReportDialog.<init> ()V | REACHABLE | SOURCE | Constructed by newInstance (ERD :41, `new ErrorReportDialog()`); BaseAlertDialog subclass, no-arg constructor. |
| 30 | ErrorReportDialog.initLayoutView (Lorg/proninyaroslav/libretorrent/databinding/DialogErrorBinding;)V | REACHABLE | SOURCE | Called from onCreateDialog (ERD :71); definition ERD :77–83 (expansionHeader click listener toggling expandableLayout). |
| 31 | ErrorReportDialog.lambda$initLayoutView$0 (Lorg/proninyaroslav/libretorrent/databinding/DialogErrorBinding;Landroid/view/View;)V | REACHABLE | INFERRED | View click dispatch to the listener set in initLayoutView (ERD :79–82); $ index by source order, NOT bytecode-verified. |
| 32 | ErrorReportDialog.newInstance (Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Lorg/proninyaroslav/libretorrent/ui/errorreport/ErrorReportDialog; | REACHABLE | SOURCE | Called from ERA.onCreate (ERA :64–67, error/app_error_occurred/getStackTrace) and from DetailTorrentFragment :557 (error/error_save_torrent_file/stack trace); definition ERD :39–54 (sets TAG_TITLE/TAG_MESSAGE/TAG_DETAIL_ERROR args). |
| 33 | ErrorReportDialog.onCreateDialog (Landroid/os/Bundle;)Landroid/app/Dialog; | REACHABLE | INFERRED | Framework DialogFragment dispatch; definition ERD :56–75 (super.onCreateDialog, inflate dialog_error, setDetailError, initLayoutView, buildDialog with report/cancel). |
| 34 | FeedItemsActivity.<clinit> ()V | REACHABLE | INFERRED | Static TAG/TAG_FEED_ID field init (FIA :37/:39, TAG non-constant); runs on class load when the manifest-declared activity (:176) starts. In-app start Intent not printed. |
| 35 | FeedItemsActivity.<init> ()V | REACHABLE | INFERRED | Framework activity instantiation for the manifest-declared activity; no explicit in-app `new`. Start Intent not printed. |
| 36 | FeedItemsActivity.onCreate (Landroid/os/Bundle;)V | REACHABLE | INFERRED | Framework activity lifecycle dispatch; definition FIA :42–60 (theme, two-pane finish guard :47–50, setContentView activity_feed_items, fragment setFeedId from TAG_FEED_ID extra :58). |
| 37 | FeedItemsActivity.onFragmentFinished (Landroidx/fragment/app/Fragment;Landroid/content/Intent;Lorg/proninyaroslav/libretorrent/ui/FragmentCallback$ResultCode;)V | REACHABLE | SOURCE | **Upgraded from the prior proposal (INFERRED, contract-only) on a freshly printed caller:** FIF.finish :325–327 `((FragmentCallback)activity).onFragmentFinished(this, intent, code)`, called from FIF.onBackPressed :320–322, itself called from FIF.onOptionsItemSelected home branch :310–311. FIA implements FragmentCallback (FIA :34–35) and hosts FIF in its layout container (FIA :54–59, findFragmentById + setFeedId), so the cast target is this activity; definition FIA :62–67 (finish()). Caveat, recorded not decided (FragmentCallback convention (viii) family): dispatch is via an interface cast, and the onOptionsItemSelected step itself is framework menu dispatch (INFERRED) — under a whole-route INFERRED convention this row reads INFERRED; label unaffected. This matches the batch 82/86 precedent of upgrading equivalent onFragmentFinished rows to SOURCE on a printed finish() caller. Note the two-pane guard: FIA finishes immediately on two-pane screens (FIA :47–50), so this route runs on small screens only — a printed configuration branch, not OPEN. |
| 38 | FeedItemsAdapter.<clinit> ()V | REACHABLE | INFERRED | Static TAG field init (FIApt :51, getSimpleName(), non-constant); runs on first class use (`new FeedItemsAdapter(this)`, FIF :152). Class-init dispatch not printed. |
| 39 | FeedItemsAdapter.<init> (Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsAdapter$ClickListener;)V | REACHABLE | SOURCE | Constructed by FIF.onViewCreated (FIF :152, `new FeedItemsAdapter(this)`); definition FIApt :55–59 (super(diffCallback), listener field). |
| 40 | FeedItemsAdapter.getItemKey (I)Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsListItem; | UNREACHABLE | INFERRED | No printed caller in this pass: FIF has no SelectionTracker/KeyProvider setup in the freshly printed file (grep over FIF finds no KeyProvider/SelectionTracker/getItemKey), and FIApt itself defines only the Selectable method (FIApt :91–97). FIF uses the adapter only via construction :152, setAdapter, and submitList references :218/:233. NOT labelled UNREACHABLE: no saved full-repo grep was run. Highest-priority grep target before merge; contrast TrackerListAdapter.getItemKey (batch 95 row 38), which HAS a printed KeyProvider caller (adapter :239–242 via fragment :181). Note: FIApt.getItemPosition (not a row in this batch) uses indexOf (equals only), which does not call getItemKey. 2026-11-01 OPEN-closing re-check (fresh): definition re-confirmed FeedItemsAdapter.java:91-97; fresh FeedItemsFragment.java (329 lines, SHA c612894b...) ZERO hits for SelectionTracker/KeyProvider/getItemKey/getItemPosition/Selectable; adapter used only via :152/:153/:218/:233. Stays OPEN; named target: saved full-repo grep for an external Selectable consumer (flips 96/40 + 97/1 together). 2026-11-01 OPEN-closing ROUND 2: FLIPPED OPEN → UNREACHABLE, kind no_trigger_in_app, confirmed_by SOURCE, together with batch 97 row 1. Saved greps: grep_selectable_methods.txt (the only selectable.getItemKey call sites are the four KeyProvider getKey methods — TorrentListAdapter :344, FeedChannelListAdapter :289, TrackerListAdapter :241, TorrentContentFilesAdapter :280; FeedItemsAdapter has none), grep_Selectable_all.txt (no Selectable-typed reference to FeedItemsAdapter outside its own file; the fragment uses it only via ClickListener and new FeedItemsAdapter(this) :152), grep_class_FeedItemsAdapter.txt (6 lines), grep_selectiontracker.txt (no SelectionTracker/KeyProvider for feed items). Dispatch premise as batch 94 rows 7-8: only an app KeyProvider calls a Selectable method; androidx SelectionTracker calls ItemKeyProvider, never Selectable. Reverts to OPEN if the merger rejects the 252-file app-Java grep as the full-repo standard. 2026-11-01 grep-flip re-check: SURVIVED on complete-tree + XML grep (greps/grep_recheck_selectable_setfilename_complete.txt). |

## Counts (mechanically verified, see verification below)

- REACHABLE proposed: 39 (SOURCE 17: rows 2, 3, 7, 10, 12, 15, 16, 17, 18, 21, 22, 27, 29, 30, 32, 37, 39; INFERRED 22: rows 1, 4, 5, 6, 8, 9, 11, 13, 14, 19, 20, 23, 24, 25, 26, 28, 31, 33, 34, 35, 36, 38)
- UNREACHABLE proposed: 1 (row 40 FeedItemsAdapter.getItemKey, round 2, SOURCE)
- OPEN: 0

## Change vs prior proposal (one, flagged — not silent)

Row 37 FeedItemsActivity.onFragmentFinished: INFERRED (contract-only) → REACHABLE
SOURCE, on the freshly printed FIF.finish caller (:325–327) above, which the prior
proposal had not printed. All other 39 verdicts are unchanged; their evidence base
is now fully fresh prints (see source list), not carried citations.

## Still owed before merge

1. Saved full-repo grep for FeedItemsAdapter.getItemKey (row 40) — the only OPEN row.
   A printed KeyProvider/SelectionTracker caller flips it to REACHABLE; a saved
   full-repo grep with no such caller would support UNREACHABLE (kind to be
   decided at merge, not here).
2. Printed ACRA start of ErrorReportActivity and printed in-app start Intent for
   FeedItemsActivity (strict-entry completeness). Under a strict launcher-entry
   rule, all REACHABLE rows in this file revert to OPEN (anchors are the pager
   trunk, the manifest-declared activities, and FIF construction — no printed
   launcher step).
3. Bytecode confirmation of anonymous/lambda $ numbering (rows 4, 31).
4. Merger decisions (recorded, not decided): strict-entry convention, per-row vs
   whole-route confirmed_by convention, FragmentCallback convention (viii) for
   row 37, <clinit>-on-first-use convention (ix) for rows 19, 28, 34, 38.
5. Main-agent spot-check (1 in 5), py_compile, build, sampler, C1 — build: not run,
   C1: not run (both run on the user's Mac after a push, never claimed passed).
   No sampler or full-repo grep was run in this pass. No search_code result was
   used anywhere, and no search_code 0 was used as evidence of absence.
6. True git clone: NOT attempted — it fails in this VM (no credential device);
   that check is named missing, never passed. All source above came via the
   GitHub connector from branch work-2026-10-31.

## Scope

Batch 96 only in this file. LibreTorrent labels only. No other batch/app, no
device replay, no Aegis. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). Nothing merged.
