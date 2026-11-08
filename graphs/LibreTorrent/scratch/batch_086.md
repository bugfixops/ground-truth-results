# LibreTorrent batch 86 review

Batch 86 contains exactly 40 plan rows; membership and bounded source/caller output are in `scratch/batch_086_plan.txt` and `scratch/batch_086_printed.txt`.

All 40 rows remain OPEN. The batch mixes custom UI widgets, pager/activity/detail-torrent methods, and fragment callbacks. Source search shows candidate callers and UI class definitions, but does not establish complete routes from app entry through XML inflation, Android lifecycle, RecyclerView/framework callbacks, and detail-screen dispatch for every row. No row is labeled from local callers or inferred absence, and no coverage evidence was used.

| Finding | Count |
|---|---:|
| REACHABLE | 0 |
| UNREACHABLE | 0 |
| OPEN | 40 |

No graph changes; no build was run.
