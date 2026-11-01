# Spot-check — Batch 31 (Stream A Phase 2)

- Work file: `~/workspace/overnight/stream-A/work/batch31-merge-ready.md` (UNVERIFIED proposal, not a result).
- Method: re-derived from already-fetched local source only (`~/workspace/overnight/stream-A/corpus/java/`). No GitHub connector fetch was needed; no 429 encountered. No edit was made to the work file.
- Phase 1 label changes in this batch: NONE (Phase 1c note: "Rows flipped: NONE"; OPEN-closing round 2 and grep-flip re-check also 0 flips). Rows checked = sample rows 1, 6, 11, 16, 21, 26, 31, 36 + must-include extras 20, 22 (21 already in sample) + Counts section check.
- Build / sampler / C1: not run (not this task).

## Per-row verdicts

| Row | Method | Table label | Verdict | Printed evidence (local corpus copies, branch work-2026-10-31) |
|---|---|---|---|---|
| 1 | FeedChannel.hashCode | OPEN | PASS | Def FeedChannel.java:121 (`public int hashCode()`), body `(int)(id ^ (id >>> 32))` at :121–124 as cited. No hash-collection use of a FeedChannel found in the corpus grep; OPEN recording is accurate (OPEN is not an absence claim). |
| 6 | FeedChannel$1.newArray | OPEN | PASS | Def FeedChannel.java:114 (`public FeedChannel[] newArray(int size)`), body through :117 as cited. Framework dispatch only; OPEN stands. |
| 11 | FeedItem.describeContents | OPEN | PASS | Def FeedItem.java:96 (`public int describeContents()`), body through :99 as cited. No printed parcel site for a FeedItem; OPEN stands. |
| 16 | FeedItem$1.<init> | REACHABLE / INFERRED | PASS | Anonymous Creator at FeedItem.java:114–128 as cited. Class-init-on-first-use inference, anchored on the REACHABLE row 8 route (FeedParser.getItems, 5-arg FeedItem ctor). INFERRED (not SOURCE) is the correct confirmed_by for this convention; convention itself not decided here. |
| 20 | TagInfo.<init>(long,String,int) | REACHABLE / SOURCE | PASS | AddTagViewModel.java:61 `info = new TagInfo(existsTagId, state.getName(), state.getColor())` — exact 3-arg ctor; def TagInfo.java:38–42 as cited. Anchor AddTagDialog.java:200 `viewModel.saveTag()` and :118 `provider.get(AddTagViewModel.class)` both confirmed. Strict-entry caveat (dialog show step not printed) is disclosed in the row and does not change the label under the adopted anchor convention. |
| 21 | TagInfo.<init>(Parcel) | REACHABLE / SOURCE | PASS | Def TagInfo.java:51–55; CREATOR.createFromParcel at :71–73 calls this ctor directly (printed). Unparcel sites all confirmed: DetailTorrentInfoFragment.java:137, AddTorrentInfoFragment.java:142 (`getParcelableExtra(TAG_RESULT_SELECTED_TAG)`), AddTagActivity.java:57 (`getParcelableExtra(TAG_INIT_INFO)`), AddTagDialog.java:119 (`getParcelable(TAG_INIT_INFO)`). See D5e note below. The row's stale "Stays OPEN" sentence (flagged in the file's own wording note) does not govern; the Label column does. |
| 22 | TagInfo.<init>(String,int) | REACHABLE / SOURCE | PASS | AddTagViewModel.java:59 `info = new TagInfo(state.getName(), state.getColor())` in the `existsTagId == null` branch — exact 2-arg `@Ignore` ctor; def TagInfo.java:45–48 as cited. Same AddTagDialog anchor as row 20. Reached on a printed app-code construction site, not on Room-entity status. |
| 26 | TagInfo.writeToParcel | REACHABLE / INFERRED | PASS | Def TagInfo.java:63–67 as cited. Parcel sites confirmed: SelectTagDialog.java:181 (`putExtra(TAG_RESULT_SELECTED_TAG, item.info)`), MainActivity.java:323 (`putExtra(TAG_INIT_INFO, item.info)`). Framework calls writeToParcel when parceling, so INFERRED is correct. |
| 31 | Torrent.<init>(Parcel) | OPEN | PASS | Def Torrent.java:104–117 as cited; CREATOR.createFromParcel at :160–163 as cited. No printed invocation of the CREATOR; OPEN stands. |
| 36 | Torrent.getMagnet | REACHABLE / SOURCE | PASS | TorrentSessionImpl.java:413–415 (`if (path != null && torrent.isDownloadingMetadata()) { loadTask.putMagnet(torrent.getMagnet(), …)`) exactly as cited; def Torrent.java:124–127 as cited. |

## Counts section check — PASS

- Counts section now reads **20 REACHABLE / 0 UNREACHABLE / 20 OPEN (SOURCE 10 / INFERRED 10)**. Independently recounted from the main table (last occurrence per row): 20 REACHABLE, 20 OPEN, SOURCE 10 / INFERRED 10 among REACHABLE. The stale 16/0/24 figure survives only in older revision-note history (disclosed in the Phase 1c note as stale), not in the Counts section. **The must-include Counts check passes: it reads 20/0/20, not 16/0/24.**

## D5e tension (rows 20, 21, 22) — reported, NOT decided

DECISIONS.md's D5e lists "31/20, 31/21, 31/22 (TagInfo ctors + Parcel ctor)" among rows staying OPEN, while the table marks all three REACHABLE. Re-derivation from printed source shows each REACHABLE label rests on **non-entity evidence**: rows 20 and 22 on direct printed `new TagInfo` sites (AddTagViewModel.java:61/:59), row 21 on the printed unparcel round trip (sites listed above) plus the printed CREATOR→ctor call. On that evidence the REACHABLE labels hold independently of TagInfo's Room-entity status. Whether D5e's sentence orders these three rows OPEN (in which case it would conflict) or only rules out entity status as a sole basis (in which case there is no conflict) is a merger ruling — **I do not decide the D5e reading, and no label is changed here.**

## Totals

- Rows checked: 10. **PASS: 10. FAIL: 0.**
- Proposed corrections: none (label or citation). The file's own wording note about stale "Stays OPEN" sentences in rows 21, 23, 26, 28 is accurate and needs no action from this spot-check.
