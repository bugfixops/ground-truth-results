# LibreTorrent batch 89 review

Batch 89 contains exactly 40 plan rows; membership and source/caller evidence are in `scratch/batch_089_plan.txt`, `scratch/batch_089_printed.txt`, `scratch/batch_089_helper.md`, and `scratch/batch_089_helper_printed.txt`.

All 40 rows remain OPEN. DetailTorrentViewModel source has local callers in the main detail fragment and child pages, including tracker, files and pieces pages; it also contains asynchronous file-tree work and Rx-based observations. The reviewed evidence does not verify complete app-entry, page selection, and callback dispatch paths for each target. No row is labeled from local calls alone, and no coverage evidence was used.

| Finding | Count |
|---|---:|
| REACHABLE | 0 |
| UNREACHABLE | 0 |
| OPEN | 40 |

No graph changes; no build was run.
