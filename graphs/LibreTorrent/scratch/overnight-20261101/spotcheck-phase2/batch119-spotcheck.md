# Stream A Phase 2 spot-check — batch 119

Source re-derived from already-fetched local copies only
(`~/workspace/b119120-src/`); no connector fetch was needed, no 429 hit.
The merge-ready file was NOT edited; no label was changed here.
Phase 1 label changes: none listed (no OPEN rows in this batch), so the
checked set is the sample rows 1, 6, 11, 16, 21, 26, 31, 36 only.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | SelectTagDialog.\<init\> | REACHABLE / SOURCE | PASS | Implicit default ctor; SelectTagDialog.java:64 `new SelectTagDialog()` in newInstance, called from SelectTagActivity.java:51. |
| 6 | SelectTagDialog.lambda$initAlertDialog$2 | REACHABLE / INFERRED | PASS | Cancel click lambda SelectTagDialog.java:159-161 (`cancelButton.setOnClickListener`, calls `finish(..., CANCEL)` at :160); view-click dispatch unprinted. |
| 11 | SelectTagDialog.onAttach | REACHABLE / INFERRED | PASS | Definition SelectTagDialog.java:74-80; DialogFragment lifecycle, no app call site printed. |
| 16 | SelectTagDialog.onStop | REACHABLE / INFERRED | PASS | Definition SelectTagDialog.java:107-111 (`disposables.clear()` :110); DialogFragment lifecycle dispatch unprinted. |
| 21 | SelectTagViewModel.observeTags | REACHABLE / SOURCE | PASS | SelectTagViewModel.java:62-64; called directly at SelectTagDialog.java:166. |
| 26 | tag.TagsAdapter.\<clinit\> | REACHABLE / INFERRED | PASS | Static `diffCallback` field TagsAdapter.java:65-82; first printed use SelectTagDialog.java:130 `new TagsAdapter(this)`. Class-init timing is the unprinted JVM rule; convention (ix) undecided, stands as INFERRED as filed. |
| 31 | tag.TagsAdapter$1.areContentsTheSame | REACHABLE / INFERRED | PASS | Definition TagsAdapter.java:68-73 (calls `oldItem.equals(newItem)` at :72); called only by DiffUtil during submitList (SelectTagDialog.java:174); DiffUtil dispatch unprinted. |
| 36 | TorrentTagsList.\<init\>(Context,AttributeSet) | REACHABLE / INFERRED | PASS | Definition TorrentTagsList.java:29-33 (`super(context, attrs)`, `init(context)` :32); layout-inflation ctor: fragment_detail_torrent_info.xml:150-154 declares TorrentTagsList with `android:id="@+id/tags_list"` (:151), inflated by DetailTorrentInfoFragment.java:100 and used at :112. The ctor call itself is LayoutInflater framework dispatch, hence INFERRED as filed. |

## Totals

- Checked: 8 rows. PASS: 8. FAIL: 0.
- Proposed corrections: none.

## Notes

- Build/sampler/C1: not run (not this task).
