# LibreTorrent batch 92 review

Batch 92 contains exactly 40 plan rows; membership and source/caller evidence are in `scratch/batch_092_plan.txt`, `scratch/batch_092_printed.txt`, `scratch/batch_092_helper.md`, and `scratch/batch_092_helper_printed.txt`.

All 40 rows remain OPEN. DetailTorrentFilesFragment and TorrentContentFilesAdapter show local click, selection, action-mode, and parcelable paths. These require RecyclerView and selection-framework callback dispatch, in addition to the unresolved route from the app's detail screen to the page. That complete route was not verified for every target. No row is labeled from local calls alone, and no coverage evidence was used.

| Finding | Count |
|---|---:|
| REACHABLE | 0 |
| UNREACHABLE | 0 |
| OPEN | 40 |

No graph changes; no build was run.
