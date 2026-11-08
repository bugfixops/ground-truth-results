# Spot-check — batch 56 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Row 16 is in both sets; checked once, under Changed. Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (7, all confirmed_by-only)

All seven are L4 D28 normalisations (SOURCE → INFERRED); label and kind unchanged and correct; no stale-prose sentence found. Work prose supports each kind (full-tree re-check 2026-11-01, 281 Java + 73 XML, cited in the rows).

- 56/2 NormalizeUrl.join(CharSequence,String[]) — UNREACHABLE branch_never_taken INFERRED — PASS. Only call site doNormalize :268, inside `if (options.removeDirectoryIndex.length > 0)` :263; default is empty (:90) and the saved 252-file grep finds ZERO assignments to removeDirectoryIndex anywhere in the app tree.
- 56/3 NormalizeUrl.makeUserInfo(String,String) — UNREACHABLE branch_never_taken INFERRED — PASS. Only call site urlToString :397, guarded `user != null && !user.isEmpty()` :396; doNormalize :232-234 nulls user/password whenever removeAuthentication is true; default is true (:100) and the saved 252-file grep finds ZERO assignments to removeAuthentication anywhere in the app tree.
- 56/13 PercentEncoder.\<clinit\>() — UNREACHABLE branch_never_taken INFERRED — PASS. Kind inherited from row 14: the class's first active use is decode (row 14); decode sits behind the never-taken `if (options.decode)` branch, so the class is never actively used in app code and its static initialiser never runs.
- 56/14 PercentEncoder.decode(String) — UNREACHABLE branch_never_taken INFERRED — PASS. Only call site doNormalize :217, inside `if (options.decode)` :216; all 3 normalize callers tree-wide set decode = false (DetailTorrentFragment :720, CreateTorrentViewModel :309, AddLinkViewModel :68); the saved 252-file grep finds no `decode = true` assignment and no caller of 1-arg normalize(String) (:165-168).
- 56/15 PercentEncoder.needsUnescaping(String) — UNREACHABLE branch_never_taken INFERRED — PASS. Kind inherited from row 14: only call site decode :35; decode never runs (row 14), so this method never runs.
- 56/16 PercentEncoder.pow(int,int) — UNREACHABLE branch_never_taken INFERRED — PASS. Kind inherited from rows 14/17: only call site unhex :111; unhex runs only from decode (row 17), which never runs (row 14).
- 56/17 PercentEncoder.unhex(char[]) — UNREACHABLE branch_never_taken INFERRED — PASS. Kind inherited from row 14: only call sites decode :54 and :79; decode never runs (row 14), so this method never runs.

## Sample rows (7 sample-only)

- 56/1 NormalizeUrl.isMatch(String,String[]) — REACHABLE SOURCE — PASS. Prior print :304-315; called from doNormalize :282 (query-filter loop; default removeQueryParameters is ["utm_\\w+"] :71, so guard :278 satisfied on a URL with a query); route: DetailTorrentFragment (fresh) :726 → normalize → doNormalize → here.
- 56/6 NormalizeUrl.parseQuery(String) — REACHABLE SOURCE — PASS. Prior print :333-362; called unconditionally from doNormalize :225; route as row 1.
- 56/11 PathResolver.resolve(String,String) — REACHABLE SOURCE — PASS. Prior print :27-34; called from doNormalize :259 (when path != null); route as row 9.
- 56/21 BindingAdapterUtils.formatETA(Context,long) — REACHABLE INFERRED — PASS. Fresh fragment_detail_torrent_state.xml:146 `android:text="@{BindingAdapterUtils.formatETA(context, viewModel.info.torrentInfo.ETA)}"`; layout expression, generated dispatch, hence INFERRED; state layout inflated by DetailTorrentStateFragment :73.
- 56/26 BindingAdapterUtils.formatProgress(Context,long,long,int) — REACHABLE INFERRED — PASS. Fresh fragment_detail_torrent_state.xml:125 `android:text="@{BindingAdapterUtils.formatProgress(context, viewModel.info.torrentInfo.receivedBytes, viewModel.info.torrentInfo.totalBytes, viewModel.info.torrentInfo.progress)}"`; layout expression, generated dispatch, hence INFERRED.
- 56/31 DateUtils.endOfWeek(long) — REACHABLE SOURCE — PASS. Fresh DateUtils :140-152; called from TorrentFilterCollection (fresh) :73.
- 56/36 DateUtils.initFormatStrings(Context) — REACHABLE INFERRED — PASS. Fresh DateUtils :92-104; called from 3-arg formatElapsedTime :80 (now REACHABLE row 35); same INFERRED note as row 34.

Totals: checked 14 (7 changed + 7 sample-only) — PASS 14, FAIL-prose 0, FAIL-label 0.
