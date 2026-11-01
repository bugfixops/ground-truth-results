# Stream A Phase 2 spot-check — batch 120

Source re-derived from already-fetched local copies only
(`~/workspace/b119120-src/`); no connector fetch was needed, no 429 hit.
The merge-ready file was NOT edited; no label was changed here.
Batch 120 has only 3 rows; all 3 were checked, per task.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | TorrentTagsList.lambda$buildChip$0 | REACHABLE / INFERRED | PASS | Close-icon click lambda TorrentTagsList.java:69-73 (`setOnCloseIconClickListener`, calls `listener.onTagRemoved(info)` at :71); chip built by buildChip :54-76, called from submit :49. Material Chip close-icon dispatch unprinted. |
| 2 | TorrentTagsList.setListener | REACHABLE / SOURCE | PASS | Definition TorrentTagsList.java:40-42; called directly at DetailTorrentInfoFragment.java:112 `binding.tagsList.setListener(tagsListener)`. |
| 3 | TorrentTagsList.submit | REACHABLE / INFERRED | PASS | Definition TorrentTagsList.java:44-52 (calls buildChip per tag at :49, re-adds the add-tag button at :51); reached only via the Rx method reference `binding.tagsList::submit` at DetailTorrentInfoFragment.java:181, called from onStart at :201. Rx dispatch unprinted. |

## Totals

- Checked: 3 rows. PASS: 3. FAIL: 0.
- Proposed corrections: none.

## Notes

- Build/sampler/C1: not run (not this task).
