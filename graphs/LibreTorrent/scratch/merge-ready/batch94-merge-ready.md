## Revision note — GREP-FLIP RE-CHECK, 2026-11-01 (UNVERIFIED, NOT merged, NO push)

Scope: Stream A Phase 1 worker, batches 85/86/94/96/97/102 ONLY. This file: rows 7, 8, 31 re-checked against the COMPLETE app Java tree (281 files: ruleF 252 + branch-enumerated missing 29 = com.ernieyu.feedparser 28 + org.nanohttpd 1, enumerated via GitHub connector listings on branch work-2026-10-31, repo bugfixops/ground-truth-results) PLUS res layout XML (69 layout/ files, filename set verified identical to branch listing, + 4 variant-layout files fetched fresh via connector 2026-11-01). Build: not run. C1: not run.
Result: ALL THREE flips SURVIVED, labels unchanged. Counts BEFORE = AFTER: 37 REACHABLE / 3 UNREACHABLE / 0 OPEN (mechanically verified from the label column, 40 rows, sequence 1-40 intact).
New evidence, saved under ~/workspace/overnight/stream-A/greps/grep_recheck_selectable_setfilename_complete.txt (rows 7-8) and greps/grep_recheck_3arg_ctors_complete.txt (row 31): rows 7-8 — the only selectable.getItemKey/getItemPosition call sites in the 281 files are inside the four KeyProvider-owning adapters (TorrentListAdapter :344/:350, FeedChannelListAdapter :289/:295, TrackerListAdapter :241/:247, TorrentContentFilesAdapter :280/:286); PeerListAdapter has no KeyProvider, DetailTorrentPeersFragment has no SelectionTracker, the fragment uses the adapter only via ClickListener and new PeerListAdapter(this) :126, and layouts contain no Selectable/SelectionTracker/KeyProvider/getItemKey/getItemPosition reference (only unrelated android:textIsSelectable attributes). Row 31 — 0 `new PiecesView(` hits, 0 `extends PiecesView` hits, 0 reflection lookups, 2-arg ctor :57-63 calls super(context, attrs) only, the sole PiecesView layout declaration (fragment_detail_torrent_pieces.xml :73-77) carries NO style attribute, and branch fw_src LayoutInflater.java (fetched fresh 2026-11-01, SHA 47b8d921da2e4ae728480228ef9da525a9e530cb) looks up ONLY the 2-arg ctor (:88, :90-91, :615).

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

**OPEN-CLOSING REVISION 2026-11-01 (UNVERIFIED, no push, no merge): 0 label changes. Counts before = after: 37 REACHABLE / 0 UNREACHABLE / 3 OPEN (rows 7, 8, 31).**
**OPEN-CLOSING ROUND 2 REVISION 2026-11-01 (UNVERIFIED, no push, no merge): 3 label changes, all OPEN → UNREACHABLE on saved 252-file app-Java greps in /home/hatch/workspace/b90929495969799102-openclose2-src/ (see rows 7, 8, 31). Counts before 37 REACHABLE / 0 UNREACHABLE / 3 OPEN → after 37 / 3 / 0. No REACHABLE label changed; batch-92 drift citations, batch-99 :169 and batch-102 trailing-newline notes untouched (other files). Build: not run. C1: not run. 0 rows verified for merge.**
Fresh source for this pass saved in ~/workspace/b90929495969799102-openclose-src/ (branch work-2026-10-31, one file at a time with ~25 s pauses, no fresh HTTP 429; each file plus its raw connector JSON saved; fresh-corpus grep in grep_fresh_corpus.txt — a PRINTED-SUBSET grep only, NOT a saved full-repo grep, so it cannot flip any row to UNREACHABLE).
Fresh files re-verified for the OPEN rows: `ui/detailtorrent/pages/peers/PeerListAdapter.java` (177 lines, SHA 1c5d275e81512e779c4d32c215469ee23de2491c), `ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java` (202 lines, SHA d164a15e3f393009779ead158ca2bb920ec7149c), `ui/detailtorrent/pages/pieces/PiecesView.java` (141 lines, SHA 3388596fc52fcebd46defe25648119d516d5da10), `fragment_detail_torrent_pieces.xml` (81 lines, SHA 2c343b2b11bb3dd2862f433a18187e89bf028c70), plus `ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java` (543 lines, SHA a1f2ccc63a8b38c9ddf7ba95c6cb60db5b7f56b7) for the batch-93 contrast.
Rows 7-8: batch-93 difference RE-VERIFIED FRESH ON BOTH SIDES — the files fragment DOES build a SelectionTracker with its adapter's KeyProvider (DetailTorrentFilesFragment.java:222-228, setSelectionTracker :286), while the peers fragment has ZERO hits for SelectionTracker/KeyProvider/getItemKey/getItemPosition/Selectable in its fresh 202-line print and uses the adapter only via new PeerListAdapter(this) :126, setAdapter :142, submitList :182 (DiffUtil, not getItemKey). PeerListAdapter itself defines no inner KeyProvider (contrast TorrentContentFilesAdapter:267-286). Rows 7-8 stay OPEN; named target: a saved full-repo grep for an external Selectable/KeyProvider consumer of PeerListAdapter. Row 31: 2-arg ctor :57-63 (super + create, does NOT chain to 3-arg) and 3-arg ctor :64-69 re-confirmed fresh; the fresh layout declares PiecesView at :73-77 with id, match_parent size and app:pieces_cellColor but NO style attribute (the style= hits at :41/:48/:53/:71 are other views), so layout inflation uses the 2-arg ctor (row 30). Lead-only cross-check (NOT fresh evidence, NOT a full-repo grep): no `new PiecesView(` anywhere in the parent's 252-file app-Java reconstruction. Row 31 stays OPEN; named target: a saved full-repo grep for a `new PiecesView(` site or another layout declaring PiecesView. Build: not run. C1: not run. 0 rows verified for merge.


# LibreTorrent batch 94 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 94 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior proposal
  (`~/workspace/libretorrent-batch94-proposal.md`) was used as an INPUT / lead list only;
  every row below was checked against the printed source listed here, and no prior
  verdict was copied as a result without a cited printed route.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 94 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,733 lines including header; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 rows are `TODO_CANDIDATE_REACHABLE` in the plan with current label
"REACHABLE (generator candidate, no hand route yet)" — candidates, not evidence.
Row 1: DetailTorrentPeersFragment$1; rows 2–4: PeerItem; rows 5–17: PeerListAdapter and
nested classes; rows 18–29: DetailTorrentPiecesFragment; rows 30–35: PiecesView;
rows 36–40: DetailTorrentTrackersFragment.
Descriptors checked against the plan: row 17 `lambda$bind$0` returns boolean (a
long-click lambda), row 20 `lambda$subscribeAdapter$0` takes `boolean[]`, row 40
`lambda$deleteTrackers$3` takes a TrackerItem and returns String — all matching the
bodies cited below.

## Printed source used in this pass

Re-read in full from previously connector-fetched local copies (NOT freshly
fetched in this pass, except where noted):
- `~/workspace/b9394scratch/PeerItem.java` (57 lines)
- `~/workspace/b9394scratch/PeerListAdapter.java` (177 lines)
- `~/workspace/b9394scratch/PiecesView.java` (140 lines)
- `~/workspace/b9394scratch/DetailPagerAdapter.java` (76 lines)
- `~/workspace/b27scratch/DetailTorrentPeersFragment.java`
- `~/workspace/b27scratch/DetailTorrentPiecesFragment.java`
- `~/workspace/b27scratch/DetailTorrentTrackersFragment.java`
- `~/workspace/b27scratch/DetailTorrentFragment.java`
- `~/workspace/b27scratch/DetailTorrentViewModel.java`

Freshly fetched in this pass, branch `work-2026-10-31`, one file at a time with a pause:
- `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java`,
  saved to `~/workspace/b9394-merge-src/DetailTorrentPeersFragment.java`, SHA-256
  `d8987250c729bd8de8fcefc5ffcc8a4d8e070c2e1d19f65d309a10d3a27bb494`,
  byte-identical to `~/workspace/b27scratch/DetailTorrentPeersFragment.java`.
  Grep of the fresh file: zero hits for `SelectionTracker`, `KeyProvider`,
  `getItemKey`, or `getItemPosition`. This is the fresh re-derivation of the
  batch 94 OPEN rows 7–8 (see below), not a search_code absence claim.
- `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/res/layout/fragment_detail_torrent_pieces.xml`,
  saved to `~/workspace/b9394-merge-src/fragment_detail_torrent_pieces.xml` (3,643 bytes).
  It declares `<org.proninyaroslav.libretorrent.ui.detailtorrent.pages.pieces.PiecesView
  android:id="@+id/piece_map" ...>` with no style attribute — this upgrades row 30
  from the prior proposal's binding-only inference to a layout-printed inference
  (see row 30). No fresh HTTP 429 was hit in this pass.

No connector `search_code` result was used as evidence of absence anywhere in this file.
No full-repo grep was run; the 3 OPEN rows below stay OPEN for exactly that reason.

## Shared trunk (proposed, strict-entry caveat below)

`DetailTorrentFragment.onViewCreated` creates the pager adapter
(`DetailTorrentFragment.java:185`, `binding.fragmentViewpager.setAdapter(adapter)` :186);
`DetailPagerAdapter.createFragment` returns `DetailTorrentPeersFragment.newInstance()` at
PEERS_FRAG_POS (:63–64), `DetailTorrentPiecesFragment.newInstance()` at PIECES_FRAG_POS
(:65–66), and `DetailTorrentTrackersFragment.newInstance()` at TRACKERS_FRAG_POS (:61–62).
ViewPager2/FragmentStateAdapter creation is standard framework dispatch (INFERRED, not
printed from fw_src/androidx). The launcher → DetailTorrentFragment step was NOT printed
in this session, so under a strict entry-route rule all 37 REACHABLE rows below revert
to OPEN. They are judged REACHABLE (proposed) on the pager-anchored trunk, as in prior
detail batches. Undecided convention recorded, not decided: that strict-entry rule itself.

## confirmed_by convention in this file

SOURCE = a printed app-code body contains the call (or the construction) of the method.
INFERRED = the method's definition and its registration/construction are printed, but the
actual invocation is only framework/library dispatch (Fragment lifecycle, RecyclerView,
DiffUtil, Rx, view listeners, class loading, layout inflation) not printed from fw_src
or androidx source. No row uses `DYN`, `FW-MEMORY`, or `UNVERIFIED` as `confirmed_by`.

## Counts — proposed, not verified, mechanically checked

- REACHABLE proposed: 37 / 40
- UNREACHABLE proposed: 3 (rows 7, 8, 31 — round 2, SOURCE)
- OPEN: 0
- Of the REACHABLE rows: SOURCE 15, INFERRED 22.
- Verified for merge: 0.

## Per-method table (plan order)

| # | Method | Label | confirmed_by | Printed route / citations |
|---|---|---|---|---|
| 1 | DetailTorrentPeersFragment$1.canReuseUpdatedViewHolder | REACHABLE | INFERRED | Anonymous DefaultItemAnimator override DetailTorrentPeersFragment.java:134–136 (`return true`); animator instantiated onViewCreated :132 and set on the RecyclerView :138. RecyclerView framework calls it. |
| 2 | PeerItem.<init> | REACHABLE | SOURCE | PeerItem.java:25–30; constructed via method reference DetailTorrentPeersFragment.java:178 `.map(PeerItem::new)` inside subscribeAdapter (:172–184), itself called by onStart :111. |
| 3 | PeerItem.equals | REACHABLE | SOURCE | PeerItem.java:44–54; printed caller PeerListAdapter.java:110–115 ($1.areItemsTheSame body `oldItem.equals(newItem)`). |
| 4 | PeerItem.equalsContent | REACHABLE | SOURCE | PeerItem.java:39–42; printed caller PeerListAdapter.java:103–108 ($1.areContentsTheSame body `oldItem.equalsContent(newItem)`). |
| 5 | PeerListAdapter.<clinit> | REACHABLE | INFERRED | Static field TAG PeerListAdapter.java:45; class loaded when constructed (row 6). Compiler-generated init, no explicit body printed. |
| 6 | PeerListAdapter.<init> | REACHABLE | SOURCE | PeerListAdapter.java:50–55; constructed DetailTorrentPeersFragment.java:126 `new PeerListAdapter(this)`. |
| 7 | PeerListAdapter.getItemKey | UNREACHABLE | INFERRED | PeerListAdapter.java:86–93 (Selectable implementation). No printed caller or registration: the peers fragment builds NO SelectionTracker/KeyProvider — grep of the freshly fetched DetailTorrentPeersFragment.java in this pass returns zero hits for SelectionTracker, KeyProvider, getItemKey, or getItemPosition, and PeerListAdapter itself constructs no KeyProvider. This is the required per-task note: stay OPEN (no SelectionTracker/KeyProvider in the peers fragment). Pending saved full-repo grep; NOT labelled UNREACHABLE on this evidence. Contrast batch 93 rows 2–3, where the files fragment DOES print a KeyProvider registration — the difference is the printed registration, not the interface. 2026-11-01 OPEN-closing re-check (fresh): peers fragment 202 lines, SHA d164a15e..., ZERO hits for SelectionTracker/KeyProvider/getItemKey/getItemPosition/Selectable; batch-93 contrast re-verified fresh (files fragment builds SelectionTracker at :222-228, setSelectionTracker :286). Stays OPEN; named target: saved full-repo grep for an external Selectable consumer. 2026-11-01 OPEN-closing ROUND 2: FLIPPED OPEN → UNREACHABLE, kind no_trigger_in_app, confirmed_by SOURCE. Saved greps: grep_selectable_methods.txt (26 lines — the only selectable.getItemKey/getItemPosition call sites in the 252-file tree are inside the four adapters that own a KeyProvider: TorrentListAdapter :344, FeedChannelListAdapter :289, TrackerListAdapter :241, TorrentContentFilesAdapter :280; PeerListAdapter has none), grep_Selectable_all.txt (no Selectable-typed reference to PeerListAdapter outside its own file; the fragment uses it only via ClickListener and new PeerListAdapter(this) :126), grep_class_PeerListAdapter.txt (6 lines), grep_selectiontracker.txt (no SelectionTracker/KeyProvider for peers). Dispatch premise, recorded: the only caller of an app Selectable method is an app KeyProvider's getKey/getPosition; androidx SelectionTracker calls ItemKeyProvider, never Selectable, so no library path reaches this method. Reverts to OPEN if the merger rejects the 252-file app-Java grep as the full-repo standard. 2026-11-01 grep-flip re-check: SURVIVED on complete-tree + XML grep (greps/grep_recheck_selectable_setfilename_complete.txt). |
| 8 | PeerListAdapter.getItemPosition | UNREACHABLE | INFERRED | PeerListAdapter.java:95–100 (Selectable implementation). Same reason as row 7: no printed caller or KeyProvider registration for peers, confirmed on the freshly fetched fragment file. Pending saved full-repo grep; NOT labelled UNREACHABLE. 2026-11-01 OPEN-closing re-check (fresh): same as row 7 — no printed caller or KeyProvider registration for peers. Stays OPEN; named target: saved full-repo grep for an external Selectable consumer. 2026-11-01 OPEN-closing ROUND 2: FLIPPED OPEN → UNREACHABLE, kind no_trigger_in_app, confirmed_by SOURCE, together with row 7 on the same saved greps (grep_selectable_methods.txt: the only selectable.getItemPosition call sites are the four KeyProvider getPosition methods — TorrentListAdapter :350, FeedChannelListAdapter :295, TrackerListAdapter :247, TorrentContentFilesAdapter :286; PeerListAdapter has none; grep_Selectable_all.txt / grep_class_PeerListAdapter.txt / grep_selectiontracker.txt as row 7). Same dispatch premise and same revert condition as row 7. 2026-11-01 grep-flip re-check: SURVIVED on complete-tree + XML grep (greps/grep_recheck_selectable_setfilename_complete.txt). |
| 9 | PeerListAdapter.onBindViewHolder | REACHABLE | INFERRED | PeerListAdapter.java:71–74; RecyclerView framework calls it; body calls holder.bind :73. Adapter set on the list DetailTorrentPeersFragment.java:142. |
| 10 | PeerListAdapter.onCreateViewHolder | REACHABLE | INFERRED | PeerListAdapter.java:59–68; RecyclerView framework calls it; body constructs ViewHolder :67. |
| 11 | PeerListAdapter.submitList | REACHABLE | SOURCE | PeerListAdapter.java:77–83; called DetailTorrentPeersFragment.java:182 `adapter.submitList(children)` in the subscribe consumer. |
| 12 | PeerListAdapter$1.<init> | REACHABLE | INFERRED | Anonymous DiffUtil.ItemCallback PeerListAdapter.java:101–116; instance `diffCallback` passed to super :52. Compiler-generated init; DiffUtil framework uses it. |
| 13 | PeerListAdapter$1.areContentsTheSame | REACHABLE | INFERRED | PeerListAdapter.java:103–108; DiffUtil framework calls it; body calls oldItem.equalsContent (row 4). |
| 14 | PeerListAdapter$1.areItemsTheSame | REACHABLE | INFERRED | PeerListAdapter.java:110–115; DiffUtil framework calls it; body calls oldItem.equals (row 3). |
| 15 | PeerListAdapter$ViewHolder.<init> | REACHABLE | SOURCE | PeerListAdapter.java:126–132; constructed onCreateViewHolder :67 `new ViewHolder(binding)`. |
| 16 | PeerListAdapter$ViewHolder.bind | REACHABLE | SOURCE | PeerListAdapter.java:134–177; called onBindViewHolder :73 `holder.bind(getItem(position), listener)`. |
| 17 | PeerListAdapter$ViewHolder.lambda$bind$0 | REACHABLE | INFERRED | Long-click listener set PeerListAdapter.java:138; body calls listener.onItemLongClick :142, i.e. DetailTorrentPeersFragment.onItemLongClick (batch 93 row 31). Framework long-click dispatch INFERRED; returns boolean, matching the plan descriptor. Numbering NOT bytecode-verified. |
| 18 | DetailTorrentPiecesFragment.<clinit> | REACHABLE | INFERRED | Static fields DetailTorrentPiecesFragment.java:47–52 (TAG, TAG_SCROLL_POSITION); class loaded when the pager creates the fragment (DetailPagerAdapter.java:65–66). |
| 19 | DetailTorrentPiecesFragment.<init> | REACHABLE | SOURCE | Implicit constructor invoked DetailTorrentPiecesFragment.java:61 `new DetailTorrentPiecesFragment()` inside newInstance :59–66. |
| 20 | DetailTorrentPiecesFragment.lambda$subscribeAdapter$0 | REACHABLE | INFERRED | Subscribe consumer DetailTorrentPiecesFragment.java:141 `binding.pieceMap.setPieces(pieces)`; Rx dispatch INFERRED. Only lambda in subscribeAdapter (:136–142). |
| 21 | DetailTorrentPiecesFragment.newInstance | REACHABLE | SOURCE | DetailTorrentPiecesFragment.java:59–66; called DetailPagerAdapter.java:65–66 (PIECES_FRAG_POS case). |
| 22 | DetailTorrentPiecesFragment.onAttach | REACHABLE | INFERRED | DetailTorrentPiecesFragment.java:77–84; standard Fragment lifecycle, framework dispatch INFERRED. |
| 23 | DetailTorrentPiecesFragment.onCreateView | REACHABLE | INFERRED | DetailTorrentPiecesFragment.java:69–75; standard Fragment lifecycle; inflates fragment_detail_torrent_pieces layout :71. |
| 24 | DetailTorrentPiecesFragment.onSaveInstanceState | REACHABLE | INFERRED | DetailTorrentPiecesFragment.java:113–122; standard Fragment lifecycle, framework dispatch INFERRED. |
| 25 | DetailTorrentPiecesFragment.onStart | REACHABLE | INFERRED | DetailTorrentPiecesFragment.java:94–99; standard Fragment lifecycle; body calls subscribeAdapter :98. |
| 26 | DetailTorrentPiecesFragment.onStop | REACHABLE | INFERRED | DetailTorrentPiecesFragment.java:86–92; standard Fragment lifecycle, framework dispatch INFERRED. |
| 27 | DetailTorrentPiecesFragment.onViewCreated | REACHABLE | INFERRED | DetailTorrentPiecesFragment.java:102–110; standard Fragment lifecycle; body obtains DetailTorrentViewModel :108 and binds it :109. |
| 28 | DetailTorrentPiecesFragment.onViewStateRestored | REACHABLE | INFERRED | DetailTorrentPiecesFragment.java:125–134; standard Fragment lifecycle, framework dispatch INFERRED. |
| 29 | DetailTorrentPiecesFragment.subscribeAdapter | REACHABLE | SOURCE | DetailTorrentPiecesFragment.java:136–142; called onStart :98. Body: viewModel.observePieces() :138 → DetailTorrentViewModel.java:187–188 → TorrentInfoProvider.observePiecesInfo. |
| 30 | PiecesView.<init>(Context,AttributeSet) | REACHABLE | INFERRED | PiecesView.java:57–62; layout-inflation constructor for the pieceMap view. Upgraded in this pass: the freshly fetched fragment_detail_torrent_pieces.xml declares `<PiecesView android:id="@+id/piece_map" ...>` with no style attribute, so standard layout inflation uses this 2-arg constructor (framework inflation dispatch itself is INFERRED, not printed from fw_src). Fragment onCreateView inflates that layout :71, and binding.pieceMap.setPieces (row 35) proves the binding field exists. |
| 31 | PiecesView.<init>(Context,AttributeSet,int) | UNREACHABLE | INFERRED | PiecesView.java:64–69. No printed caller: the freshly fetched layout declares the view with no style attribute, so layout inflation uses the 2-arg constructor (row 30), and no app code constructs PiecesView with a defStyleAttr in the printed corpus. Pending saved full-repo grep; NOT labelled UNREACHABLE. 2026-11-01 OPEN-closing re-check (fresh): 2-arg ctor :57-63 does NOT chain to 3-arg; fresh layout declares PiecesView at :73-77 with NO style attribute, so inflation uses the 2-arg ctor. Stays OPEN; named target: saved full-repo grep for new PiecesView( or another declaring layout. 2026-11-01 OPEN-closing ROUND 2: FLIPPED OPEN → UNREACHABLE, kind no_trigger_in_app, confirmed_by SOURCE. Saved greps: grep_new_PiecesView.txt — 0 `new PiecesView(` hits in the 252-file tree; grep_class_PiecesView.txt — 5 lines, definition file only. The sole declaring layout in every saved copy (fragment_detail_torrent_pieces.xml :73-77, including the 69-layout dir) carries NO style attribute, and Android layout inflation invokes the (Context, AttributeSet) ctor, so inflation uses row 30's 2-arg ctor; the 2-arg ctor does NOT chain to the 3-arg ctor (PiecesView.java:57-63 vs :64-69). Premise recorded: if the merger holds that inflation can call the 3-arg ctor, this row reverts to OPEN. 2026-11-01 grep-flip re-check: SURVIVED on complete-tree + XML grep (greps/grep_recheck_3arg_ctors_complete.txt). |
| 32 | PiecesView.create | REACHABLE | SOURCE | PiecesView.java:71–88 (package-private); called by both constructors :61 and :68. |
| 33 | PiecesView.onDraw | REACHABLE | INFERRED | PiecesView.java:119–141; standard View draw dispatch (framework); setPieces :89–99 calls invalidate()/requestLayout() when the array changes, which schedules draw/measure. |
| 34 | PiecesView.onMeasure | REACHABLE | INFERRED | PiecesView.java:104–117; standard View measure dispatch (framework); setPieces calls requestLayout() on length change :98, scheduling measure. |
| 35 | PiecesView.setPieces | REACHABLE | SOURCE | PiecesView.java:89–99; called DetailTorrentPiecesFragment.java:141 `binding.pieceMap.setPieces(pieces)`. |
| 36 | DetailTorrentTrackersFragment.<clinit> | REACHABLE | INFERRED | Static fields DetailTorrentTrackersFragment.java:71–77 (TAG, SELECTION_TRACKER_ID, TAG_LIST_TRACKER_STATE, TAG_DELETE_TRACKERS_DIALOG); class loaded when the pager creates the fragment (DetailPagerAdapter.java:61–62). |
| 37 | DetailTorrentTrackersFragment.<init> | REACHABLE | SOURCE | Implicit constructor invoked inside newInstance DetailTorrentTrackersFragment.java:93–100 (`new DetailTorrentTrackersFragment()`); newInstance called DetailPagerAdapter.java:61–62. |
| 38 | DetailTorrentTrackersFragment.deleteTrackers | REACHABLE | SOURCE | DetailTorrentTrackersFragment.java:360–372; called from subscribeAlertDialog POSITIVE_BUTTON_CLICKED branch :279 `deleteTrackers()`. |
| 39 | DetailTorrentTrackersFragment.deleteTrackersDialog | REACHABLE | SOURCE | DetailTorrentTrackersFragment.java:338–358; called from actionModeCallback.onActionItemClicked delete_tracker_url branch :317–318 `deleteTrackersDialog()`. |
| 40 | DetailTorrentTrackersFragment.lambda$deleteTrackers$3 | REACHABLE | INFERRED | Map lambda DetailTorrentTrackersFragment.java:366 `(selection -> selection.url)` inside deleteTrackers; Rx dispatch INFERRED. Lambda numbering follows the plan name, NOT verified against bytecode — merger must confirm. |

## Caveats / still owed before merge

- Strict-entry caveat: launcher → DetailTorrentFragment step not printed; under a strict rule all 37 REACHABLE revert to OPEN.
- OPEN rows: none (round 2 closed rows 7, 8, 31 on the saved greps named in those rows; the pre-round-2 'do NOT flip without a saved full-repo grep' condition is now satisfied for them, under the 252-file app-Java grep standard — see the revert conditions in rows 7/8/31).
- Anonymous/lambda numbering ($1, bind$0, subscribeAdapter$0, deleteTrackers$3) follows source order / plan names, NOT verified against bytecode.
- Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run.
- 0/40 verified for merge. No build, sampler, grep, or C1 run in this session.
