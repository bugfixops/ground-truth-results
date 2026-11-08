# Stream A Phase 2 spot-check — batch 112

Source re-derived from already-fetched local copies only
(`~/workspace/b111112-src/`); no connector fetch was needed, no 429 hit.
The merge-ready file was NOT edited; no label was changed here.
Phase 1 label changes: none (Phase 1c: 0 label flips, 1 cosmetic fix).
Checked set: sample rows 1, 6, 11, 16, 21, 26, 31, 36 PLUS the
must-include rows 1 (D2 launcher-step-only variant) and 30 (D1 cosmetic
confirmed_by normalisation).

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | TorrentListAdapter.\<init\> | REACHABLE / SOURCE | PASS | MainFragment.java:136 `new TorrentListAdapter(this)`. D2 variant (a) verified: AndroidManifest.xml:53-55 MAIN/LAUNCHER, MainActivity.java:182 `setContentView(R.layout.activity_main)` and :185 `findFragmentById(R.id.main_fragmentContainer)`. Stands REACHABLE SOURCE under the adopted launcher-step-only variant; the every-step-fresh variant (b) was not adopted and was not applied. |
| 6 | TorrentListAdapter.onBindViewHolder | REACHABLE / INFERRED | PASS | Override TorrentListAdapter.java:88-105 (calls `holder.setSelected` :95 and `holder.bind` :102); invoked by RecyclerView dispatch, unprinted. |
| 11 | TorrentListAdapter$1.areItemsTheSame | REACHABLE / INFERRED | PASS | TorrentListAdapter.java:318-322 (`oldItem.equals(newItem)`); invoked by DiffUtil/ListAdapter on submitList (MainFragment.java:297/:345), library dispatch unprinted. |
| 16 | TorrentListAdapter$ItemLookup.getItemDetails | REACHABLE / INFERRED | PASS | TorrentListAdapter.java:390-400, with the printed `ViewHolder.getItemDetails` call at :396; invoked by SelectionTracker on touch, library dispatch unprinted. |
| 21 | TorrentListAdapter$ViewHolder.bind | REACHABLE / SOURCE | PASS | Definition TorrentListAdapter.java:171-275; printed caller onBindViewHolder at :102. |
| 26 | TorrentListAdapter$ViewHolder.setSelected | REACHABLE / SOURCE | PASS | Definition TorrentListAdapter.java:277-280; printed caller onBindViewHolder at :95. |
| 30 | TorrentListItem.hashCode | OPEN / — | PASS | Definition TorrentListItem.java:56-58 (`torrentId.hashCode()`). No printed app call site in the fetched corpus: the only `hashCode` hit in TorrentListItem.java is the definition itself; `getItemPosition` uses `List.indexOf` (TorrentListAdapter.java:119, equals only) and the SelectionTracker storage at MainFragment.java:162 is `createParcelableStorage` (Parcelable, not hash storage). OPEN stands; confirmed_by is "—" as normalised (D1 cosmetic fix verified). Not flipped to UNREACHABLE: no saved full-repo grep exists and a tree zero alone never flips. |
| 31 | AbstractTagItem.\<init\> | REACHABLE / INFERRED | PASS | Implicit default ctor; printed subclass constructions in MainActivity.java: new EmptyTagItem() :332, :475, :498, :509; new NoTagsItem() :476, :501; TagItem::new map :477. The super-call itself is implicit in the unprinted subclass ctor bodies, hence INFERRED as filed. |
| 36 | DrawerExpandableAdapter.getGroup | REACHABLE / SOURCE | PASS | MainActivity.java:560 (`saveGroupExpandState`) and :584 (`onDrawerGroupsCreated` loop). |

## Totals

- Checked: 9 rows. PASS: 9. FAIL: 0.
- Proposed corrections: none.

## Notes

- Build/sampler/C1: not run (not this task).
