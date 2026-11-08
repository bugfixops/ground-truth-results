# LibreTorrent batch 95 review

Batch 95 contains exactly 40 plan rows; membership and source/caller evidence are in `scratch/batch_095_plan.txt`, `scratch/batch_095_printed.txt`, `scratch/batch_095_helper.md`, and `scratch/batch_095_helper_printed.txt`.

All 40 rows remain OPEN. DetailTorrentTrackersFragment and TrackerListAdapter show local selection, action-mode, subscription, and tracker-sharing/deletion paths. These require complete route verification from the detail activity/page and AndroidX selection/action-mode callbacks, which is not established for every row. No row is labeled from local callers alone, and no coverage evidence was used.

| Finding | Count |
|---|---:|
| REACHABLE | 0 |
| UNREACHABLE | 0 |
| OPEN | 40 |

No graph changes; no build was run.
