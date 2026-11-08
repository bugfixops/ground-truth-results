# LibreTorrent batch 84 review

Batch 84 contains exactly 40 plan rows; membership and source/caller evidence are in `scratch/batch_084_plan.txt`, `scratch/batch_084_printed.txt`, `scratch/batch_084_helper.md`, and `scratch/batch_084_helper_printed.txt`.

All 40 rows remain OPEN. Source shows CreateTorrentDialog forwarding configuration into CreateTorrentViewModel, view-model build/validation helpers, and activity-result handling. Those local call chains do not establish full app-entry, framework result dispatch, or all branch conditions for each target. No row is labeled from generator candidates or local calls alone, and no coverage evidence was used.

| Finding | Count |
|---|---:|
| REACHABLE | 0 |
| UNREACHABLE | 0 |
| OPEN | 40 |

No graph changes; no build was run.
