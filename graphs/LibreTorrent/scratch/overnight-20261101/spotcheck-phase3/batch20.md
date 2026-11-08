# Spot-check — batch 20 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (1)

- 20/39 LogEntry.hashCode — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose (label, kind, confirmed_by correct per L1: definition core/logger/LogEntry.java:93-101, String hashes inside body only; zero external .hashCode() on LogEntry in greps/L1/grep_all_calls.txt; zero hash collection of LogEntry in greps/L1/grep_hash_collections.txt — Logger holds ArrayList\<LogEntry\>, not a hash collection). Stale prose: "row stays OPEN pending the project-wide hashCode rule — see round-2 note above" and "REVISION 2026-11-01 Phase 1c (D6 printed-trigger rule): stays OPEN — zero receiver-typed hits + zero hash collections in the app-Java tree alone neither flips to REACHABLE nor to UNREACHABLE".

## Sample rows (8)

- 20/1 FetchLinkException.\<init\>(String) — REACHABLE SOURCE — PASS. Definition :30 (distinct from the (Exception) ctor at :35); throw sites Utils.java:467, :493, :509, :522.
- 20/6 NormalizeUrlException.\<init\>(String,Exception) — REACHABLE SOURCE — PASS. Definition NormalizeUrlException.java:21 (distinct from the (String) overload at :27); throw site NormalizeUrl.java:185, called at DetailTorrentFragment.java:726, CreateTorrentViewModel.java:311, AddLinkViewModel.
- 20/11 TorrentFilterCollection.dateAddedToday — REACHABLE SOURCE — PASS. Definition :47-55; caller Utils.java:860.
- 20/16 TorrentFilterCollection.lambda$dateAddedMonth$8 — REACHABLE INFERRED — PASS. Lambda body :78-84 inside dateAddedMonth(); same test() dispatch as row 15.
- 20/21 TorrentFilterCollection.lambda$noTags$11 — REACHABLE INFERRED — PASS. Lambda body :102 inside noTags(); same test() dispatch as row 15.
- 20/26 TorrentFilterCollection.lambda$tag$10 — REACHABLE INFERRED — PASS. Lambda body :98 inside tag(TagInfo); same test() dispatch as row 15.
- 20/31 TorrentFilterCollection.statusError — REACHABLE SOURCE — PASS. Definition :43-45; callers Utils.java:849, :887.
- 20/36 LogEntry.getMsg — REACHABLE SOURCE — PASS. Definition LogEntry.java:60-64; call site LogAdapter.java:108 (binding.msg.setText(entry.getMsg()) in ViewHolder.bind).

Totals: checked 9 (1 changed + 8 sample-only) — PASS 8, FAIL-prose 1, FAIL-label 0.
