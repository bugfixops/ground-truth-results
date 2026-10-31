# LibreTorrent batch 49 review

The plan TSV is the sole membership source; batch 49 contains exactly 40 rows. Source definitions and migration/repository caller evidence are saved in `scratch/batch_049_helper_printed.txt`; row-by-row findings are in `scratch/batch_049_helper.md`.

This batch includes Room migration callbacks/helpers, feed repository methods, and tag repository methods. Evidence establishes local calls and object creation through the repository helper, UI view models, feed workers, and Room migration registration. Those relationships do not complete hand-authored entry-to-method routes; framework migration dispatch and app lifecycle/UI paths remain unresolved. Keep all 40 OPEN. No missing caller match was treated as proof of unreachability.

| Finding | Count |
|---|---:|
| REACHABLE | 0 |
| UNREACHABLE | 0 |
| OPEN | 40 |

No graph changes; no build was run. No coverage evidence was used.
