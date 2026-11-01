# Batch 56 — Phase 2 spot-check (UNVERIFIED proposal check only; nothing merged, nothing pushed)

- Source file checked: `~/workspace/overnight/stream-A/work/batch56-merge-ready.md`
- Evidence base: already-fetched files only (`~/workspace/ruleF-src/`, `~/workspace/b565758-openclose2-src/`,
  `~/workspace/overnight/stream-A/corpus/`, `~/workspace/overnight/stream-A/greps/`). No connector fetch was needed;
  no 429; no missing file.
- Rows checked (15): sample 1, 6, 11, 16, 21, 26, 31, 36 + Phase 1 flips 2, 3, 13, 14, 15, 16, 17
  (row 16 is both sample and flip).
- Batch Counts verified mechanically from the label column AND against the Counts section: 33 REACHABLE / 7 UNREACHABLE / 0 OPEN.
  The stale Counts lines the task mentions were corrected in Phase 1 — the section now states 33/7/0 and matches the table.
- Build/sampler/C1: not run (not this task).

## Per-row verdicts

| Row | Label in file | Verdict | Evidence (printed source) |
|-----|---------------|---------|---------------------------|
| 1 `NormalizeUrl.isMatch(String,String[])` | REACHABLE SOURCE | PASS | NormalizeUrl.java:304 (def); called from doNormalize :282 inside the query-filter loop; default `removeQueryParameters = ["utm_\\w+"]` :71, guard :278; route DetailTorrentFragment :726 → normalize → doNormalize → here (fragment :726 verified). |
| 2 `NormalizeUrl.join(CharSequence,String[])` | UNREACHABLE SOURCE `branch_never_taken` | PASS | Only call site doNormalize :268, inside `if (options.removeDirectoryIndex.length > 0)` :263; default empty :90; ruleF-tree grep finds zero assignments to `removeDirectoryIndex` outside NormalizeUrl.java, and the saved 252-file grep (`grep-full-tree-252.txt`) contains no assignment either. Exactly 3 normalize callers tree-wide (DetailTorrentFragment :726, CreateTorrentViewModel :311, AddLinkViewModel :69), none setting the field. |
| 3 `NormalizeUrl.makeUserInfo(String,String)` | UNREACHABLE SOURCE `branch_never_taken` | PASS | Only call site urlToString :397, guarded `user != null && !user.isEmpty()` :396; doNormalize :232-234 nulls user/password when `removeAuthentication` is true; default true :100; zero assignments tree-wide (same greps as row 2). |
| 6 `NormalizeUrl.parseQuery(String)` | REACHABLE SOURCE | PASS | NormalizeUrl.java:333 (def); called unconditionally from doNormalize :225 (verified). Same route as row 1. |
| 11 `PathResolver.resolve(String,String)` | REACHABLE SOURCE | PASS | PathResolver.java:27 (def); called from doNormalize :259 (verified by grep). |
| 13 `PercentEncoder.<clinit>()` | UNREACHABLE SOURCE `branch_never_taken` | PASS | Inherited from row 14: the class's only tree-wide active use is `PercentEncoder.decode` (NormalizeUrl :217; no other `PercentEncoder.` reference in ruleF-src outside its own file); decode never runs (row 14), so the class is never actively used and its static initialiser never runs. `utf8Masks` at PercentEncoder.java:16 verified. |
| 14 `PercentEncoder.decode(String)` | UNREACHABLE SOURCE `branch_never_taken` | PASS | Only call site doNormalize :217, inside `if (options.decode)` :216; all 3 normalize callers set `decode = false` (DetailTorrentFragment :720, CreateTorrentViewModel :309, AddLinkViewModel :68 — all verified); zero `decode = true` assignments tree-wide; no caller of 1-arg `normalize(String)` (:165-168) tree-wide (only the 3 two-arg sites found). |
| 15 `PercentEncoder.needsUnescaping(String)` | UNREACHABLE SOURCE `branch_never_taken` | PASS | Only call site decode :35 (verified); decode never runs (row 14). |
| 16 `PercentEncoder.pow(int,int)` | UNREACHABLE SOURCE `branch_never_taken` | PASS | Only call site unhex :111 (verified); unhex runs only from decode (row 17), which never runs. |
| 17 `PercentEncoder.unhex(char[])` | UNREACHABLE SOURCE `branch_never_taken` | PASS | Only call sites decode :54 and :79 (both verified); decode never runs (row 14). |
| 21 `BindingAdapterUtils.formatETA(Context,long)` | REACHABLE INFERRED | PASS | Corpus layout fragment_detail_torrent_state.xml:146 `@{BindingAdapterUtils.formatETA(context, viewModel.info.torrentInfo.ETA)}` — exact match. Generated dispatch unprinted, so INFERRED is correct. |
| 26 `BindingAdapterUtils.formatProgress(Context,long,long,int)` | REACHABLE INFERRED | PASS | Same layout :125 `@{BindingAdapterUtils.formatProgress(context, viewModel.info.torrentInfo.receivedBytes, viewModel.info.torrentInfo.totalBytes, viewModel.info.torrentInfo.progress)}` — exact match. INFERRED correct. |
| 31 `DateUtils.endOfWeek(long)` | REACHABLE SOURCE | PASS | DateUtils.java:140 (def); TorrentFilterCollection.java:73 `dateAdded <= DateUtils.endOfWeek(timeMillis)` (verified). SOURCE correct. |
| 36 `DateUtils.initFormatStrings(Context)` | REACHABLE INFERRED | PASS | DateUtils.java:92 (def); called from 3-arg formatElapsedTime :80 (verified). Row 35's route stands; INFERRED note (generated dispatch) as recorded in the file. |

## Totals

- PASS: 15, FAIL: 0 (of 15 checked).
- Proposed corrections: none. All seven UNREACHABLE flips (rows 2, 3, 13, 14, 15, 16, 17) survived re-check against the
  printed tree and the saved 252-file greps; the corrected Counts section (33/7/0) matches the table.
- Caveat (not a failure): UNREACHABLE verdicts rest on the saved 252-file grep plus the ruleF-tree grep, i.e. a reconstructed
  tree, not a git-checkout grep — the file itself records this corpus caveat, and it is preserved here.
