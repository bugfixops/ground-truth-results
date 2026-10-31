# LibreTorrent batch 91 review

Batch 91 contains exactly 40 plan rows; membership and source/caller evidence are in `scratch/batch_091_plan.txt`, `scratch/batch_091_printed.txt`, `scratch/batch_091_helper.md`, and `scratch/batch_091_helper_printed.txt`.

All 40 rows remain OPEN. DetailTorrentInfoFragment and DetailTorrentFilesFragment show local view, tag, priority-dialog, and file-selection handlers; DetailTorrentStateFragment is created in the detail pager. These chains still lack complete screen-entry, pager-selection, lifecycle, and framework/Rx callback dispatch verification for every target. No row is labeled from local calls alone, and no coverage evidence was used.

| Finding | Count |
|---|---:|
| REACHABLE | 0 |
| UNREACHABLE | 0 |
| OPEN | 40 |

No graph changes; no build was run.
