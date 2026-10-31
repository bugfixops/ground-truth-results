# LibreTorrent batch 45 review

The sole membership source is the plan TSV; this batch contains exactly 40 rows. The helper's row-by-row audit is saved at `scratch/batch_045_helper.md` and its printed definition and app-use evidence at `scratch/batch_045_helper_printed.txt`.

All 40 rows are `SettingsRepositoryImpl` preference accessors and `observeSettingsChanged()`, covering torrent limits, download and upload speeds, log size, move-after-download, notification sound, charging policy, port ranges, POSIX disk I/O, and proxy settings. The evidence confirms their bodies and identifies local consumers in engine, service, notifier, and settings UI code. Those uses do not establish a complete route from an app entry through hand-authored graph edges; the settings callbacks and Rx lifecycle paths are also not fully traced. Retain all 40 as OPEN. No absence of caller matches was treated as proof of unreachability.

| Finding | Count |
|---|---:|
| REACHABLE | 0 |
| UNREACHABLE | 0 |
| OPEN | 40 |

No graph changes; no build was run. No coverage evidence was used.
