**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

**OPEN-CLOSING REVISION 2026-11-01 (UNVERIFIED, no push, no merge): 0 label changes. Counts before = after: 39 REACHABLE / 0 UNREACHABLE / 1 OPEN (row 1).**
**OPEN-CLOSING ROUND 2 REVISION 2026-11-01 (UNVERIFIED, no push, no merge): 1 label change: row 1 OPEN → UNREACHABLE on saved 252-file app-Java greps in /home/hatch/workspace/b90929495969799102-openclose2-src/. Counts before 39 REACHABLE / 0 UNREACHABLE / 1 OPEN → after 39 / 1 / 0. Flips together with batch 96 row 40 (same adapter, same missing KeyProvider). Build: not run. C1: not run. 0 rows verified for merge.**
Fresh source for this pass saved in ~/workspace/b90929495969799102-openclose-src/ (branch work-2026-10-31, one file at a time with ~25 s pauses, no fresh HTTP 429; each file plus its raw connector JSON saved; fresh-corpus grep in grep_fresh_corpus.txt — a PRINTED-SUBSET grep only, NOT a saved full-repo grep, so it cannot flip any row to UNREACHABLE).
Fresh files re-verified for the OPEN row: `ui/feeditems/FeedItemsAdapter.java` (184 lines, SHA bf28a46f9c2f149b4557aefe5308c5310fab23c4), `ui/feeditems/FeedItemsFragment.java` (329 lines, SHA c612894b16f58bf5c7780fa683a4a8cbcefda97f).
Row 1: getItemPosition definition re-confirmed fresh at FeedItemsAdapter.java:100-103 (getCurrentList().indexOf(key), equals-only); the adapter has no inner KeyProvider. Fresh FeedItemsFragment.java has ZERO hits for SelectionTracker/KeyProvider/getItemKey/getItemPosition/Selectable and uses the adapter only via :152/:153/:218/:233 as in batch 96 row 40. Consistent with batch 96 row 40 (getItemKey OPEN) and batch 94 rows 7-8 (peers Selectable OPEN). Row 1 stays OPEN; named target: a saved full-repo grep for an external Selectable/KeyProvider consumer of FeedItemsAdapter (one hit flips rows 96/40 and 97/1 together). Build: not run. C1: not run. 0 rows verified for merge.


# LibreTorrent batch 97 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED merge-ready proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push, so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1 check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 97 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Source task: re-derive from printed source. The prior batch-97 proposal (`~/workspace/libretorrent-batch97-proposal.md`) was used as an INPUT, not a result; membership and the table below were checked against the plan and against printed source in this pass (see Re-derivation check).

## Membership — verified first, not guessed

Exactly the 40 rows for batch 97 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA `0104806dd666c840049b3db52823d4b384fa1c92`), all `TODO_CANDIDATE_REACHABLE` in the plan (generator candidates, not evidence), in plan order:
FeedItemsAdapter rows 1-4, FeedItemsAdapter$1 rows 5-7, FeedItemsAdapter$ViewHolder rows 8-12, FeedItemsFragment rows 13-40.
Method names, JVM descriptors and order were checked against the plan in this pass and match the table below row for row.

## Printed source used

Base path (all files):
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`
- `ui/feeditems/FeedItemsAdapter.java` — saved at `~/workspace/b9798-src/FeedItemsAdapter.java` (184 lines; SHA bf28a46f… in the b67 listing). Re-read in full in the prior proposal pass; re-checked in this pass at :91-103 (getItemKey/getItemPosition definitions) and :105-120 (DiffUtil callback).
- `ui/feeditems/FeedItemsFragment.java` — saved at `~/workspace/b9798-src/FeedItemsFragment.java` (329 lines; SHA c612894b…). Re-checked in this pass at :80-97 (newInstance/setFeedId), :159-165 (onStart -> subscribeAdapter/subscribeRefreshStatus), :202-210 (subscribeAdapter/observeFeedItems), :325-328 (finish -> onFragmentFinished).
- `ui/feeds/FeedActivity.java` — freshly connector-fetched in the prior pass, saved at `~/workspace/b9798-src/FeedActivity.java` (SHA 90d65973…, 412 lines). Re-checked in this pass at :91-107 (onCreate) and :203-224 (showFeedItems, two-pane newInstance :207 / transaction replace :215-218, single-pane Intent to FeedItemsActivity :221-223).
- `ui/feeditems/FeedItemsActivity.java` — freshly connector-fetched in the prior pass, saved at `~/workspace/b9798-src/FeedItemsActivity.java` (SHA 951104d8…, 67 lines). Re-checked in this pass at :42-60 (onCreate, layout-declared fragment by id :54-55, setFeedId :58).
Line numbers below are from those files (FIA = FeedItemsAdapter.java, FIF = FeedItemsFragment.java, FA = FeedActivity.java, FItA = FeedItemsActivity.java).

## Re-derivation check in this pass (not a copy)

- Plan membership: 40/40 rows, sequence 1-40 intact, descriptors match the plan. Counts below were mechanically verified from the table in this pass.
- OPEN row re-derived: row 1 `FeedItemsAdapter.getItemPosition` was re-checked against printed source in this pass. Definition FIA:100-103 (`return getCurrentList().indexOf(key)`). A grep of the printed Fragment and Adapter files finds NO SelectionTracker, NO KeyProvider, and NO caller of getItemKey/getItemPosition in the Fragment — the only hits are the two Selectable definitions themselves (FIA:91-97 getItemKey, FIA:100-103 getItemPosition). FeedItemsFragment builds no SelectionTracker/KeyProvider, unlike FeedChannelListAdapter (batch 99) where a KeyProvider calls getItemKey/getItemPosition. **Row 1 therefore stays OPEN, not UNREACHABLE**: no saved full-repo grep was run in this pass, no connector search_code 0-result was used as evidence of absence, and a grep hit for a KeyProvider/Selectable consumer elsewhere would flip it to REACHABLE.
- Consistency, as instructed: row 1 is judged consistently with batch 96 row 40 (`FeedItemsAdapter.getItemKey`, OPEN — same fragment, same reason: no SelectionTracker/KeyProvider setup in the printed Fragment, adapter defines only the Selectable method, no saved full-repo grep) and with batch 94 rows 7-8 (`PeerListAdapter.getItemKey/getItemPosition`, OPEN — DetailTorrentPeersFragment builds NO SelectionTracker/KeyProvider for peers, pending saved full-repo grep). A grep hit for one Selectable method does NOT by itself close the other; each needs its own printed consumer. Note: `FeedItemsAdapter.getItemKey` itself is a batch-96 row, not judged here except for this consistency note.
- Trunk re-checked: FA.showFeedItems :203-224, FItA.onCreate :42-60, FIF.onStart :159-165, FIF.finish :325-328 all match the citations in the table. The FeedItemsFragment.finish -> onFragmentFinished call at FIF:327 is a printed caller for `FeedActivity.onFragmentFinished` (batch 99 row 2, left OPEN there) — recorded here as a cross-batch lead only, not judged here, and it flips nothing in this batch.
- No other row was changed from the prior proposal in this pass: the remaining 39 REACHABLE citations were spot-checked against the printed files above and hold on the evidence cited in the table. Lambda $ numbering is source-order matched to plan signatures, not bytecode-verified (notably ViewHolder.bind $1 vs $2, the two View-click lambdas); labels are unaffected by that $1/$2 assignment.

## Shared trunk / strict-entry caveat (applies to every REACHABLE row below) — UNDECIDED convention, recorded not decided

Two-pane route, printed: FA.showFeedItems :203-219 — newInstance :207, fragment transaction replace :215-218. Single-pane route, printed: FA.showFeedItems :220-224, Intent to FeedItemsActivity :221-223; FItA.onCreate :42-59 (layout-declared fragment found by id :54-55, setFeedId :58).
**The in-app starter of FeedActivity itself was NOT printed in this pass** (same gap as batch 99). Under a strict launcher-entry rule every REACHABLE row below reverts to OPEN until that starter is printed. Rows are proposed REACHABLE on the FeedActivity/FeedItemsActivity-anchored trunk above, the convention used by sibling detail/feed batches. The merger must pick one strict-entry convention for all batches; this file does not decide it.

## confirmed_by convention (stated so the merger can reconcile it) — UNDECIDED convention, recorded not decided

SOURCE = a direct app-code call site naming the method is printed (including a direct internal call and a method reference / lambda body that names it, e.g. adapter::submitList, holder.bind, new ViewHolder).
INFERRED = reached only through unprinted framework/library dispatch (RecyclerView, DiffUtil, fragment/activity lifecycle, Rx, view/popup click listeners, ViewModelProvider) with the definition and registration printed.
This is the per-row convention, not the whole-route convention used in some earlier batches; labels are unaffected, only confirmed_by would change at merge if the merger adopts the whole-route convention.

## Counts — proposed, not verified (mechanically verified from the table)

- REACHABLE proposed: 39 / 40 (SOURCE 12, INFERRED 27)
- UNREACHABLE proposed: 1 / 40 (row 1, round 2, SOURCE)
- OPEN: 0 / 40
- Verified for merge: 0 / 40

Round 2: row 1 IS now claimed UNREACHABLE on the saved 252-file greps named in the row (the pre-round-2 condition is satisfied under that grep standard); connector search_code was not used as evidence of absence anywhere.

## Rows

| # | Method | Label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | FeedItemsAdapter.getItemPosition(FeedItemsListItem)I | UNREACHABLE | SOURCE | FIA:100-103 definition only. No printed caller: FIF builds no SelectionTracker/KeyProvider (unlike FeedChannelListAdapter, batch 99 rows 21-22, 38-39, where KeyProvider calls getItemKey/getItemPosition), and no other printed code calls this Selectable method. Consistent with batch 96 row 40 (FeedItemsAdapter.getItemKey OPEN) and batch 94 rows 7-8 (PeerListAdapter getItemKey/getItemPosition OPEN). [Pre-round-2 note, superseded by the ROUND 2 flip below.] 2026-11-01 OPEN-closing re-check (fresh): definition re-confirmed FeedItemsAdapter.java:100-103 (indexOf, equals-only); fresh FeedItemsFragment.java ZERO SelectionTracker/KeyProvider hits. [Pre-round-2 status, superseded by the ROUND 2 flip below.] 2026-11-01 OPEN-closing ROUND 2: FLIPPED OPEN → UNREACHABLE, kind no_trigger_in_app, confirmed_by SOURCE, together with batch 96 row 40. Saved greps: grep_selectable_methods.txt (the only selectable.getItemPosition call sites are the four KeyProvider getPosition methods — TorrentListAdapter :350, FeedChannelListAdapter :295, TrackerListAdapter :247, TorrentContentFilesAdapter :286; FeedItemsAdapter has none), grep_Selectable_all.txt (no Selectable-typed reference to FeedItemsAdapter outside its own file), grep_class_FeedItemsAdapter.txt (6 lines), grep_selectiontracker.txt (no SelectionTracker/KeyProvider for feed items). Dispatch premise as batch 94 rows 7-8: only an app KeyProvider calls a Selectable method. Reverts to OPEN if the merger rejects the 252-file app-Java grep as the full-repo standard. Consistency note updated: batch 96 row 40 is now UNREACHABLE on the same evidence, not OPEN — the pair stays consistent. |
| 2 | FeedItemsAdapter.onBindViewHolder(ViewHolder,int)V | REACHABLE | INFERRED | FIA:76-79 body calls holder.bind(getItem(position), listener) :78. Adapter set on the RecyclerView at FIF:153; RecyclerView dispatch to onBindViewHolder is library code, not printed. |
| 3 | FeedItemsAdapter.onCreateViewHolder(ViewGroup,int)ViewHolder | REACHABLE | INFERRED | FIA:64-73 body inflates item_feed_items_list :67-70 and returns new ViewHolder :72. RecyclerView dispatch unprinted, same as row 2. |
| 4 | FeedItemsAdapter.submitList(List)V | REACHABLE | SOURCE | FIF:218 (observeFeedItems subscribe adapter::submitList) and FIF:233 (getAllFeedItemsSingle subscribe adapter::submitList). Body FIA:82-88 sorts the list :85 then super.submitList :87. |
| 5 | FeedItemsAdapter$1.<init>()V | REACHABLE | INFERRED | FIA:105-120 anonymous DiffUtil.ItemCallback assigned to static diffCallback; instance created at class initialisation when the adapter is constructed (FIF:152 new FeedItemsAdapter(this)). JVM/library dispatch unprinted. |
| 6 | FeedItemsAdapter$1.areContentsTheSame(FeedItemsListItem,FeedItemsListItem)Z | REACHABLE | INFERRED | FIA:108-112 body calls oldItem.equalsContent(newItem) :111. Reached when ListAdapter diffs a submitted list (row 4, FIF:218/:233). DiffUtil dispatch is library code, not printed. |
| 7 | FeedItemsAdapter$1.areItemsTheSame(FeedItemsListItem,FeedItemsListItem)Z | REACHABLE | INFERRED | FIA:115-119 body calls oldItem.equals(newItem) :118. Same DiffUtil route as row 6. |
| 8 | FeedItemsAdapter$ViewHolder.<init>(ItemFeedItemsListBinding)V | REACHABLE | SOURCE | FIA:72 new ViewHolder(binding) in onCreateViewHolder. Body FIA:133-138 super(binding.getRoot()). |
| 9 | FeedItemsAdapter$ViewHolder.bind(FeedItemsListItem,ClickListener)V | REACHABLE | SOURCE | FIA:78 holder.bind(getItem(position), listener) in onBindViewHolder. Body FIA:140-182. |
| 10 | FeedItemsAdapter$ViewHolder.lambda$bind$0(ClickListener,FeedItemsListItem,MenuItem)Z | REACHABLE | INFERRED | FIA:156-160 popup setOnMenuItemClickListener lambda; body calls listener.onItemMenuClicked(menuItem.getItemId(), item) :158. Popup/menu dispatch unprinted. Signature (MenuItem) identifies this as the menu-item lambda. |
| 11 | FeedItemsAdapter$ViewHolder.lambda$bind$1(FeedItemsListItem,ClickListener,View)V | REACHABLE | INFERRED | One of the two View-click lambdas registered in bind: menu-button click FIA:144 (binding.menu.setOnClickListener, shows the popup) and item-row click FIA:164 (itemView.setOnClickListener, calls listener.onItemClicked). $1 vs $2 assignment not bytecode-verified; both run on a printed registration. |
| 12 | FeedItemsAdapter$ViewHolder.lambda$bind$2(ClickListener,FeedItemsListItem,View)V | REACHABLE | INFERRED | The other View-click lambda of row 11 (FIA:144 or :164). Same route and caveat as row 11. |
| 13 | FeedItemsFragment.<clinit>()V | REACHABLE | INFERRED | FIF:66 TAG = FeedItemsFragment.class.getSimpleName(), a non-constant static initialiser; runs on first use of the class (newInstance FIF:82, or FragmentManager layout inflation via FItA:54-55). JVM dispatch unprinted. |
| 14 | FeedItemsFragment.<init>()V | REACHABLE | SOURCE | FIF:82 new FeedItemsFragment() in newInstance. Also the no-arg ctor FragmentManager uses for the layout-declared fragment (FItA:54-55). |
| 15 | FeedItemsFragment.finish(Intent,ResultCode)V | REACHABLE | SOURCE | FIF:322 onBackPressed body calls finish(new Intent(), FragmentCallback.ResultCode.BACK). Body FIF:325-328 calls ((FragmentCallback)activity).onFragmentFinished(this, intent, code) :327. Cross-note for the merger (not judged here): that :327 call IS a printed in-app caller for FeedActivity.onFragmentFinished, which batch 99 row 2 left OPEN for want of a printed caller. |
| 16 | FeedItemsFragment.getAllFeedItemsSingle()V | REACHABLE | SOURCE | FIF:204 subscribeAdapter body calls getAllFeedItemsSingle(). Body FIF:223-235 subscribes viewModel.getItemsByFeedIdSingle() with adapter::submitList. |
| 17 | FeedItemsFragment.getFeedId()J | REACHABLE | SOURCE | FA:211 ((FeedItemsFragment)fragment).getFeedId() in showFeedItems (two-pane same-feed check); also FA:186 f.getFeedId() in subscribeMsgViewModel. Body FIF:89-92. |
| 18 | FeedItemsFragment.lambda$getAllFeedItemsSingle$4(List)SingleSource | REACHABLE | INFERRED | FIF:227-231 flatMap lambda (Observable.fromIterable -> map FeedItemsListItem::new -> toList). Rx dispatch unprinted. |
| 19 | FeedItemsFragment.lambda$getAllFeedItemsSingle$5(Throwable)V | REACHABLE | INFERRED | FIF:234-235 error lambda (Log.e "Getting item list error"). Rx dispatch unprinted. |
| 20 | FeedItemsFragment.lambda$observeFeedItems$2(List)SingleSource | REACHABLE | INFERRED | FIF:212-216 flatMapSingle lambda (Flowable.fromIterable -> map FeedItemsListItem::new -> toList). Rx dispatch unprinted. |
| 21 | FeedItemsFragment.lambda$observeFeedItems$3(Throwable)V | REACHABLE | INFERRED | FIF:219-220 error lambda (Log.e "Getting item list error"). Rx dispatch unprinted. |
| 22 | FeedItemsFragment.lambda$onViewCreated$0(View)V | REACHABLE | INFERRED | FIF:143 toolbar setNavigationOnClickListener lambda (v) -> onBackPressed(). View-click dispatch unprinted. |
| 23 | FeedItemsFragment.lambda$onViewCreated$1()V | REACHABLE | INFERRED | FIF:155 swipeContainer setOnRefreshListener lambda () -> viewModel.refreshChannel(). Swipe dispatch unprinted. |
| 24 | FeedItemsFragment.newInstance(long)FeedItemsFragment | REACHABLE | SOURCE | FA:207 FeedItemsFragment.newInstance(feedId) in showFeedItems (two-pane branch). Body FIF:80-87 (new fragment, setFeedId, setArguments). Single-pane path instead uses the layout-declared fragment (FItA:54-55), so this call site is the two-pane route. |
| 25 | FeedItemsFragment.observeFeedItems()Disposable | REACHABLE | SOURCE | FIF:205 subscribeAdapter body: disposables.add(observeFeedItems()). Body FIF:208-221 subscribes viewModel.observeItemsByFeedId() with adapter::submitList. |
| 26 | FeedItemsFragment.onAttach(Context)V | REACHABLE | INFERRED | FIF:100-106 body (captures AppCompatActivity). Fragment lifecycle dispatch unprinted. |
| 27 | FeedItemsFragment.onBackPressed()V | REACHABLE | SOURCE | FIF:143 toolbar navigation lambda body calls onBackPressed(); also FIF:310 menu home branch calls onBackPressed(). Body FIF:320-323 calls finish :322. |
| 28 | FeedItemsFragment.onCreateOptionsMenu(Menu,MenuInflater)V | REACHABLE | INFERRED | FIF:298-303 body inflates R.menu.feed_items :302. Framework menu dispatch unprinted; fragment opts in via setHasOptionsMenu(true) FIF:139 (non-two-pane branch). |
| 29 | FeedItemsFragment.onCreateView(LayoutInflater,ViewGroup,Bundle)View | REACHABLE | INFERRED | FIF:109-114 body inflates fragment_feed_items :111 and returns binding.getRoot() :113. Fragment lifecycle dispatch unprinted. |
| 30 | FeedItemsFragment.onItemClicked(FeedItemsListItem)V | REACHABLE | INFERRED | ClickListener implementation: item-row click lambda FIA:164-167 calls listener.onItemClicked(item) :166, and the fragment is the listener (FIF:152 new FeedItemsAdapter(this)). Interface dispatch unprinted, hence INFERRED, not SOURCE. Body FIF:246-249 calls openDownloadUrl :248. |
| 31 | FeedItemsFragment.onItemMenuClicked(int,FeedItemsListItem)V | REACHABLE | INFERRED | ClickListener implementation: menu-item lambda FIA:156-160 calls listener.onItemMenuClicked(menuItem.getItemId(), item) :158, listener is the fragment (FIF:152). Interface dispatch unprinted. Body FIF:252-261 dispatches to openArticle / markAsRead / markAsUnread. |
| 32 | FeedItemsFragment.onOptionsItemSelected(MenuItem)Z | REACHABLE | INFERRED | FIF:307-318 body (home -> onBackPressed, refresh -> viewModel.refreshChannel, mark-as-read -> viewModel.markAllAsRead). Registered via toolbar method reference FIF:134 (two-pane) and framework options-menu dispatch (non-two-pane, setHasOptionsMenu FIF:139); dispatch itself unprinted. |
| 33 | FeedItemsFragment.onResume()V | REACHABLE | INFERRED | FIF:176-182 body restores itemsListState :181. Fragment lifecycle dispatch unprinted. |
| 34 | FeedItemsFragment.onSaveInstanceState(Bundle)V | REACHABLE | INFERRED | FIF:185-191 body saves layoutManager state :187-188. Fragment lifecycle dispatch unprinted. |
| 35 | FeedItemsFragment.onStart()V | REACHABLE | INFERRED | FIF:159-165 body calls subscribeAdapter :163 and subscribeRefreshStatus :164. Fragment lifecycle dispatch unprinted. |
| 36 | FeedItemsFragment.onStop()V | REACHABLE | INFERRED | FIF:168-173 body clears disposables :172. Fragment lifecycle dispatch unprinted. |
| 37 | FeedItemsFragment.onViewCreated(View,Bundle)V | REACHABLE | INFERRED | FIF:117-156 body (ViewModelProvider :123, clearData/setFeedId :127-128, toolbar setup, adapter construction :152, setAdapter :153, swipe listener :155). Fragment lifecycle dispatch unprinted. |
| 38 | FeedItemsFragment.onViewStateRestored(Bundle)V | REACHABLE | INFERRED | FIF:194-200 body restores itemsListState :199. Fragment lifecycle dispatch unprinted. |
| 39 | FeedItemsFragment.openArticle(FeedItemsListItem)V | REACHABLE | SOURCE | FIF:255 onItemMenuClicked body calls openArticle(item) for R.id.open_article_menu. Body FIF:263-278 (empty-URL snackbar, else viewModel.markAsRead :273, ACTION_VIEW intent :275-277). |
| 40 | FeedItemsFragment.openDownloadUrl(FeedItemsListItem)V | REACHABLE | SOURCE | FIF:248 onItemClicked body calls openDownloadUrl(item). Body FIF:280-295 (empty-URL snackbar, else viewModel.markAsRead :290, AddTorrentActivity intent :292-294). |

## Caveats / still owed before merge

1. [SUPERSEDED by ROUND 2: row 1 flipped OPEN -> UNREACHABLE together with batch 96 row 40 and
   batch 94 rows 7-8 on the saved Selectable greps; batch 97 now has 0 OPEN rows.]
2. Strict-entry gap (above): who starts FeedActivity was not printed; under a strict launcher-entry rule all 39 REACHABLE rows revert to OPEN.
3. Adapter/Fragment line numbers rest on the b67 local copies re-read in full in the prior pass and re-checked here; the merger should still re-verify them against a fresh connector fetch if it requires it. FeedActivity/FeedItemsActivity were freshly fetched in the prior pass and corroborate the shared trunk.
4. Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run here, never claimed passed.
5. No saved full-repo grep was run in this pass; no connector search_code result was used as evidence of absence. No row was flipped to UNREACHABLE.
6. Lambda $ numbering is source-order matched to plan signatures, not bytecode-verified (notably ViewHolder.bind $1 vs $2).
7. No fresh HTTP 429 was hit in this pass (this pass worked from printed source saved in `~/workspace/b9798-src/` and the local plan copy; no new connector fetch was required to close any row, and none was retried in a loop).
8. Scope kept exactly: this batch only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis, no push, no graph edits.
