# LibreTorrent batch 103 review

Batch 103 contains exactly 40 plan rows; membership and bounded source/caller output are in `scratch/batch_103_plan.txt` and `scratch/batch_103_printed.txt`.

All 40 rows remain OPEN. FileManagerDialog local code shows directory and file return paths, input/replace dialogs, adapter and spinner subscriptions, and a media receiver; FileManagerNode supplies list data. These candidate chains do not establish complete dialog entry, Android receiver/framework dispatch, RecyclerView/spinner callbacks, or guard conditions for every target. No row is labeled from local calls alone, and no coverage evidence was used.

| Finding | Count |
|---|---:|
| REACHABLE | 0 |
| UNREACHABLE | 0 |
| OPEN | 40 |

No graph changes; no build was run.
