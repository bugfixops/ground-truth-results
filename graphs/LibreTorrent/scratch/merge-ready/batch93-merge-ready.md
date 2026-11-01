# LibreTorrent batch 93 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 93 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior proposal
  (`~/workspace/libretorrent-batch93-proposal.md`) was used as an INPUT / lead list only;
  every row below was checked against the printed source listed here, and no prior
  verdict was copied as a result without a cited printed route.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 93 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,733 lines including header; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 rows are `TODO_CANDIDATE_REACHABLE` in the plan with current label
"REACHABLE (generator candidate, no hand route yet)" — candidates, not evidence.
Rows 1–23: TorrentContentFilesAdapter and nested classes.
Rows 24–40: DetailTorrentPeersFragment and its $1 anonymous class.
Descriptors checked against the plan: e.g. row 1 `<init>` takes a
`TorrentContentFilesAdapter$ClickListener`, rows 21–22 are the two `lambda$bind$`
methods taking (ClickListener, TorrentContentFileItem, View), row 40 is
`DetailTorrentPeersFragment$1.<init>` taking the enclosing fragment.

## Printed source used in this pass

Re-read in full from previously connector-fetched local copies (NOT freshly
fetched in this pass, except where noted — the merger's spot-check should
re-print at least one file fresh; the byte-identical fresh fetch of the peers
fragment below raises confidence in this corpus but does not replace that check):
- `~/workspace/b9394scratch/TorrentContentFilesAdapter.java` (337 lines)
- `~/workspace/b9394scratch/DetailPagerAdapter.java` (76 lines)
- `~/workspace/b9394scratch/DetailTorrentFilesFragment.java` (543 lines)
- `~/workspace/b27scratch/DetailTorrentPeersFragment.java`
- `~/workspace/b27scratch/DetailTorrentFragment.java`
- `~/workspace/b27scratch/DetailTorrentViewModel.java`

Freshly fetched in this pass, branch `work-2026-10-31`, one file at a time:
- `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java`,
  saved to `~/workspace/b9394-merge-src/DetailTorrentPeersFragment.java`, SHA-256
  `d8987250c729bd8de8fcefc5ffcc8a4d8e070c2e1d19f65d309a10d3a27bb494`,
  byte-identical to `~/workspace/b27scratch/DetailTorrentPeersFragment.java`.
  Grep of the fresh file: zero hits for `SelectionTracker`, `KeyProvider`,
  `getItemKey`, or `getItemPosition` — relevant to batch 94, not to any batch 93 row.
  Fresh lines confirmed: `new PeerListAdapter(this)` :126, animator construction :132,
  `canReuseUpdatedViewHolder` :134, `adapter.submitList(children)` :182,
  `onItemLongClick` :186–191, `sharePeerIp` :193.

No connector `search_code` result was used as evidence of absence anywhere in this file.
No full-repo grep was run; no row below is claimed UNREACHABLE, so no row depends on a grep.

## Shared trunk (proposed, strict-entry caveat below)

`DetailTorrentFragment.onViewCreated` creates the pager adapter
(`DetailTorrentFragment.java:185`, `binding.fragmentViewpager.setAdapter(adapter)` :186);
`DetailPagerAdapter.createFragment` returns `DetailTorrentFilesFragment.newInstance()`
at FILES_FRAG_POS (:59–60) and `DetailTorrentPeersFragment.newInstance()` at
PEERS_FRAG_POS (:63–64). ViewPager2/FragmentStateAdapter fragment creation is standard
framework dispatch (INFERRED, not printed from fw_src/androidx). The launcher →
DetailTorrentFragment step was NOT printed in this session, so under a strict
entry-route rule all 40 rows below revert to OPEN. They are judged REACHABLE
(proposed) on the pager-anchored trunk, as in prior detail batches.
Undecided convention recorded, not decided: that strict-entry rule itself, and
the binding/SelectionTracker conventions noted in the caveats.

## confirmed_by convention in this file

SOURCE = a printed app-code body contains the call (or the construction) of the method.
INFERRED = the method's definition and its registration/construction are printed, but the
actual invocation is only framework/library dispatch (Fragment lifecycle, RecyclerView,
DiffUtil, SelectionTracker, Rx, view click listeners, class loading) not printed from
fw_src or androidx source. This matches "standard registration with only internal
dispatch INFERRED". No row uses `DYN`, `FW-MEMORY`, or `UNVERIFIED` as `confirmed_by`.

## Counts — proposed, not verified, mechanically checked

- REACHABLE proposed: 40 / 40
- UNREACHABLE proposed: 0
- OPEN: 0
- Of the REACHABLE rows: SOURCE 14, INFERRED 26.
- Verified for merge: 0.

## Per-method table (plan order)

| # | Method | Label | confirmed_by | Printed route / citations |
|---|---|---|---|---|
| 1 | TorrentContentFilesAdapter.<init> | REACHABLE | SOURCE | TorrentContentFilesAdapter.java:59–63; constructed DetailTorrentFilesFragment.java:207 `new TorrentContentFilesAdapter(this)`. |
| 2 | TorrentContentFilesAdapter.getItemKey | REACHABLE | INFERRED | TorrentContentFilesAdapter.java:95–102; called by KeyProvider.getKey :278–280; KeyProvider registered in SelectionTracker.Builder, DetailTorrentFilesFragment.java:225. SelectionTracker framework dispatch INFERRED. Contrast batch 94 rows 7–8: here the KeyProvider registration IS printed, so these rows are not OPEN. |
| 3 | TorrentContentFilesAdapter.getItemPosition | REACHABLE | INFERRED | TorrentContentFilesAdapter.java:104–107; called by KeyProvider.getPosition :284–286; same SelectionTracker registration as row 2. |
| 4 | TorrentContentFilesAdapter.onBindViewHolder | REACHABLE | INFERRED | TorrentContentFilesAdapter.java:85–92; RecyclerView framework calls it; body calls getItem :86, holder.setSelected :89, holder.bind :91. Adapter set on RecyclerView, DetailTorrentFilesFragment.java:220. |
| 5 | TorrentContentFilesAdapter.onCreateViewHolder | REACHABLE | INFERRED | TorrentContentFilesAdapter.java:73–82; RecyclerView framework calls it; body constructs ViewHolder :81. |
| 6 | TorrentContentFilesAdapter.setSelectionTracker | REACHABLE | SOURCE | TorrentContentFilesAdapter.java:66–69; called DetailTorrentFilesFragment.java:286 `adapter.setSelectionTracker(selectionTracker)`. |
| 7 | TorrentContentFilesAdapter$1.<init> | REACHABLE | INFERRED | Anonymous DiffUtil.ItemCallback class, TorrentContentFilesAdapter.java:109–125; instance `diffCallback` passed to super :61. Compiler-generated init; DiffUtil framework uses it. |
| 8 | TorrentContentFilesAdapter$1.areContentsTheSame | REACHABLE | INFERRED | TorrentContentFilesAdapter.java:112–117; DiffUtil framework calls it; body calls oldItem.equalsContent. |
| 9 | TorrentContentFilesAdapter$1.areItemsTheSame | REACHABLE | INFERRED | TorrentContentFilesAdapter.java:119–124; DiffUtil framework calls it; body calls oldItem.equals. |
| 10 | TorrentContentFilesAdapter$ItemDetails.<init> | REACHABLE | SOURCE | TorrentContentFilesAdapter.java:295–299; constructed ViewHolder.getItemDetails :250 `new ItemDetails(selectionKey, getBindingAdapterPosition())`. |
| 11 | TorrentContentFilesAdapter$ItemDetails.getPosition | REACHABLE | INFERRED | TorrentContentFilesAdapter.java:309–312; SelectionTracker framework reads ItemDetails; definition printed, no app-code caller printed. |
| 12 | TorrentContentFilesAdapter$ItemDetails.getSelectionKey | REACHABLE | INFERRED | TorrentContentFilesAdapter.java:303–307; same SelectionTracker dispatch as row 11. |
| 13 | TorrentContentFilesAdapter$ItemLookup.<init> | REACHABLE | SOURCE | TorrentContentFilesAdapter.java:319–323; constructed DetailTorrentFilesFragment.java:226 `new TorrentContentFilesAdapter.ItemLookup(binding.fileList)`. |
| 14 | TorrentContentFilesAdapter$ItemLookup.getItemDetails | REACHABLE | INFERRED | TorrentContentFilesAdapter.java:326–335; SelectionTracker framework calls it on touch; body calls ViewHolder.getItemDetails :332. |
| 15 | TorrentContentFilesAdapter$KeyProvider.<init> | REACHABLE | SOURCE | TorrentContentFilesAdapter.java:269–274; constructed DetailTorrentFilesFragment.java:225 `new TorrentContentFilesAdapter.KeyProvider(adapter)`. |
| 16 | TorrentContentFilesAdapter$KeyProvider.getKey | REACHABLE | INFERRED | TorrentContentFilesAdapter.java:278–281; SelectionTracker framework calls it; body calls selectable.getItemKey (row 2). |
| 17 | TorrentContentFilesAdapter$KeyProvider.getPosition | REACHABLE | INFERRED | TorrentContentFilesAdapter.java:284–287; SelectionTracker framework calls it; body calls selectable.getItemPosition (row 3). |
| 18 | TorrentContentFilesAdapter$ViewHolder.<init> | REACHABLE | SOURCE | TorrentContentFilesAdapter.java:139–145; constructed onCreateViewHolder :81 `new ViewHolder(binding)`. |
| 19 | TorrentContentFilesAdapter$ViewHolder.bind | REACHABLE | SOURCE | TorrentContentFilesAdapter.java:147–240; called onBindViewHolder :91 `holder.bind(item, listener)`. |
| 20 | TorrentContentFilesAdapter$ViewHolder.getItemDetails | REACHABLE | SOURCE | TorrentContentFilesAdapter.java:248–251; called ItemLookup.getItemDetails :332 `((ViewHolder)viewHolder).getItemDetails()`. |
| 21 | TorrentContentFilesAdapter$ViewHolder.lambda$bind$0 | REACHABLE | INFERRED | Item-view click listener set TorrentContentFilesAdapter.java:166; body calls listener.onItemClicked :171. Framework click dispatch INFERRED; lambda numbering follows source order in bind (first listener set), NOT bytecode-verified. |
| 22 | TorrentContentFilesAdapter$ViewHolder.lambda$bind$1 | REACHABLE | INFERRED | Priority click listener set TorrentContentFilesAdapter.java:173; body calls listener.onItemCheckedChanged :175. Framework click dispatch INFERRED; numbering NOT bytecode-verified. |
| 23 | TorrentContentFilesAdapter$ViewHolder.setSelected | REACHABLE | SOURCE | TorrentContentFilesAdapter.java:242–245 (private); called onBindViewHolder :89 `holder.setSelected(selectionTracker.isSelected(item))`. |
| 24 | DetailTorrentPeersFragment.<clinit> | REACHABLE | INFERRED | Static fields DetailTorrentPeersFragment.java:56–62 (TAG, TAG_LIST_TRACKER_STATE); class loaded when the pager creates the fragment (DetailPagerAdapter.java:63–64). Compiler-generated init, no explicit body printed. |
| 25 | DetailTorrentPeersFragment.<init> | REACHABLE | SOURCE | Implicit constructor invoked DetailTorrentPeersFragment.java:74 `new DetailTorrentPeersFragment()` inside newInstance :72–79. |
| 26 | DetailTorrentPeersFragment.lambda$subscribeAdapter$0 | REACHABLE | INFERRED | flatMapSingle lambda DetailTorrentPeersFragment.java:176–181 (`.map(PeerItem::new)` :178); Rx dispatch INFERRED. Called from subscribeAdapter, itself called by onStart :111. |
| 27 | DetailTorrentPeersFragment.lambda$subscribeAdapter$1 | REACHABLE | INFERRED | Subscribe consumer DetailTorrentPeersFragment.java:182 `adapter.submitList(children)`; Rx dispatch INFERRED. |
| 28 | DetailTorrentPeersFragment.newInstance | REACHABLE | SOURCE | DetailTorrentPeersFragment.java:72–79; called DetailPagerAdapter.java:63–64 (PEERS_FRAG_POS case). |
| 29 | DetailTorrentPeersFragment.onAttach | REACHABLE | INFERRED | DetailTorrentPeersFragment.java:90–97; standard Fragment lifecycle, framework dispatch INFERRED. |
| 30 | DetailTorrentPeersFragment.onCreateView | REACHABLE | INFERRED | DetailTorrentPeersFragment.java:82–88; standard Fragment lifecycle, framework dispatch INFERRED. |
| 31 | DetailTorrentPeersFragment.onItemLongClick | REACHABLE | SOURCE | DetailTorrentPeersFragment.java:186–191; printed caller is the PeerListAdapter ViewHolder long-click lambda (PeerListAdapter.java:138–142 `listener.onItemLongClick(item)`); body calls sharePeerIp :188. |
| 32 | DetailTorrentPeersFragment.onResume | REACHABLE | INFERRED | DetailTorrentPeersFragment.java:164–170; standard Fragment lifecycle, framework dispatch INFERRED. |
| 33 | DetailTorrentPeersFragment.onSaveInstanceState | REACHABLE | INFERRED | DetailTorrentPeersFragment.java:146–153; standard Fragment lifecycle, framework dispatch INFERRED. |
| 34 | DetailTorrentPeersFragment.onStart | REACHABLE | INFERRED | DetailTorrentPeersFragment.java:107–112; standard Fragment lifecycle; body calls subscribeAdapter :111. |
| 35 | DetailTorrentPeersFragment.onStop | REACHABLE | INFERRED | DetailTorrentPeersFragment.java:99–105; standard Fragment lifecycle, framework dispatch INFERRED. |
| 36 | DetailTorrentPeersFragment.onViewCreated | REACHABLE | INFERRED | DetailTorrentPeersFragment.java:115–143; standard Fragment lifecycle; body constructs PeerListAdapter :126 and the $1 animator :132. |
| 37 | DetailTorrentPeersFragment.onViewStateRestored | REACHABLE | INFERRED | DetailTorrentPeersFragment.java:155–161; standard Fragment lifecycle, framework dispatch INFERRED. |
| 38 | DetailTorrentPeersFragment.sharePeerIp | REACHABLE | SOURCE | DetailTorrentPeersFragment.java:193–201; called onItemLongClick :188 `sharePeerIp(item.ip)`. |
| 39 | DetailTorrentPeersFragment.subscribeAdapter | REACHABLE | SOURCE | DetailTorrentPeersFragment.java:172–184; called onStart :111. Body: viewModel.observePeers() :174 → DetailTorrentViewModel.java:183–184 → TorrentInfoProvider.observePeersInfo. |
| 40 | DetailTorrentPeersFragment$1.<init> | REACHABLE | INFERRED | Anonymous DefaultItemAnimator subclass DetailTorrentPeersFragment.java:132–137; instantiated onViewCreated :132. Compiler-generated init; RecyclerView framework uses the animator. |

## Caveats / still owed before merge

- Strict-entry caveat: launcher → DetailTorrentFragment step not printed; under a strict rule all 40 revert to OPEN.
- Anonymous/lambda numbering ($1, bind$0/$1, subscribeAdapter$0/$1) follows source order, NOT verified against bytecode — merger must confirm.
- No full-repo grep: nothing here is claimed UNREACHABLE, and no row depends on a grep.
- Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run.
- 0/40 verified for merge. No build, sampler, grep, or C1 run in this session.
