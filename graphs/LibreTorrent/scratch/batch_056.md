# LibreTorrent batch 56 review

Batch 56 contains exactly 40 plan rows. The helper's row-by-row audit and printed sources are in `scratch/batch_056_helper.md` and `scratch/batch_056_helper_printed.txt`.

The methods cover URL normalization, path resolution, percent decoding, bencoded file-tree construction, data-binding formatting adapters, and date/time utilities. Source bodies and local callers are documented. They remain OPEN because end-to-end app-entry routes were not traced; the binding adapter runtime dispatch is also generated and unavailable in the printed source. No caller absence was used to infer unreachability, and no coverage evidence was used.

| Finding | Count |
|---|---:|
| REACHABLE | 0 |
| UNREACHABLE | 0 |
| OPEN | 40 |

No graph changes; no build was run.
