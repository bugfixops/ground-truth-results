# LibreTorrent batch 46 review

The plan TSV is the sole membership source; batch 46 contains exactly 40 rows. The row-by-row helper audit is in `scratch/batch_046_helper.md`; printed `SettingsRepositoryImpl` bodies, interface declarations, and app-use search are in `scratch/batch_046_helper_printed.txt`.

The rows cover proxy type, aggregate session settings, feed refresh interval, torrent-file storage, scheduling preferences, seeding/network behavior, storage paths, permission warning state, NAT error behavior, shutdown completion, streaming configuration, theme and notification settings, unmetered connections, random ports, and HTTPS tracker validation. Source evidence shows preference bodies and local usages, but the full entry-to-method paths are not established with hand-authored edges. Scheduling and preference callback routes also remain unresolved. Keep all 40 OPEN; absence of a caller match is not proof of unreachability.

| Finding | Count |
|---|---:|
| REACHABLE | 0 |
| UNREACHABLE | 0 |
| OPEN | 40 |

No graph changes; no build was run. No coverage evidence was used.
