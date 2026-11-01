**GREP-FLIP RE-CHECK 2026-11-01 (Stream A Phase 1): rows 2, 3, 13, 14, 15, 16, 17 SURVIVED — labels unchanged, still UNREACHABLE branch_never_taken. Re-checked against the COMPLETE tree enumerated via the GitHub connector: 281 Java files (252 org.proninyaroslav.libretorrent + 28 com.ernieyu.feedparser + 1 org.nanohttpd.NanoHTTPD) plus 73 layout XML files (69 res/layout + 2 layout-large-land-notouch + 2 layout-sw600dp-land). New greps: `~/workspace/overnight/stream-A/greps/recheck-47-56-57_local252.txt` (252-file re-run) and `~/workspace/overnight/stream-A/greps/recheck-47-56-57_complete-tree-plus-xml.txt` (101 freshly fetched files, zero target-pattern hits in every one). Complete-tree result: zero assignments to removeDirectoryIndex or removeAuthentication outside their defaults (empty / true), zero `decode = true` assignments, zero callers of 1-arg normalize(String), zero additional NormalizeUrl.normalize callers beyond DetailTorrentFragment :726, CreateTorrentViewModel :311, AddLinkViewModel :69, and zero additional PercentEncoder.decode callers beyond NormalizeUrl :217. No other row changed. Counts mechanically verified, unchanged: 40 rows, 33 REACHABLE / 7 UNREACHABLE / 0 OPEN (the Counts section below previously still read 33/0/7 from before round 2; corrected here to 33/7/0). Build: not run. C1: not run. No push.**

**REVISION 2026-11-01 (OPEN-closing round 2, group G8 — batches 56/57/58 only). Status remains UNVERIFIED, NOT verified for merge. Build: not run. C1: not run. Nothing pushed.**
Flips in this revision (7): rows 2, 3, 13, 14, 15, 16, 17 OPEN -> UNREACHABLE, all kind `branch_never_taken`, all on the saved full-repo grep in `~/workspace/b565758-openclose2-src/grep-full-tree-252.txt` + `grep-full-tree-252b.txt` over the 252-file app Java tree (`~/workspace/ruleF-src/`, connector-reconstructed; NormalizeUrl SHA `2e123d9a4a9bbb9da53abea9a9fba02a98ae5e91aa523b19ea2a357001d27c3f`, PercentEncoder SHA `6c2181bb2c74f4d3c480aa0494efb1dcde8ccfda54abdd2a1b690811f3fd1366` — identical to the round-1 fresh copies) plus the printed guards below. Corpus caveat, read with every flip: this is a reconstructed Java tree, not a git-checkout grep; res XML was checked separately for these names (0 hits) and no layout expression can call these package-private/option-gated methods, but if the merger adopts a stricter grep rule (git checkout only), these 7 rows revert to OPEN — they are NOT claimed on a partial corpus. No other row changed. Counts: 33/0/7 -> 33/7/0.

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 56 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** Build and C1 run on the user's Mac after a push, so they
are marked "not run" here, never passed. No sampler, full-repo grep, or C1 check was run
or is claimed in this file. No connector `search_code` 0-result was used as evidence of
absence. No row was flipped to UNREACHABLE: no saved full-repo grep exists.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 56 only, LibreTorrent labels only, no other batch/app, no device replay, no Aegis.
- Membership: exactly the 40 rows of batch 56 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`,
  local copy `~/workspace/agent27-plan.tsv`, plan SHA `0104806dd666c840049b3db52823d4b384fa1c92`,
  all `TODO_CANDIDATE_REACHABLE`, in plan order. Method names/descriptors checked against that copy.
- Prior proposal (`~/workspace/libretorrent-batch56-proposal.md`) was used as a lead list only;
  every row below was re-checked in this pass against the printed source listed below.
  Where a verdict is unchanged, the reason is restated from printed source, not copied as a result.

## Printed source in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with pauses,
saved in `~/workspace/b565758-src/` (base
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`):
- `core/utils/Utils.java` (926 lines) — not a batch-56 definition file, used for grep checks only.
- `ui/main/MainActivity.java` (811 lines) — anchors checked, no new batch-56 caller found.
- `core/filter/TorrentFilterCollection.java` (104 lines) — fresh, confirms DateUtils calls below.
- `ui/detailtorrent/DetailTorrentFragment.java` (832 lines) — fresh, confirms NormalizeUrl anchor
  at :719 `new NormalizeUrl.Options()`, :720 `options.decode = false`, :726 `NormalizeUrl.normalize(url, options)`,
  and no other option assignment in that fragment.
- `ui/addtorrent/AddTorrentViewModel.java` — fresh, confirms `BencodeFileTreeUtils.buildFileTree(files)` at :379.
- `core/utils/DateUtils.java` — fresh, confirms definitions for rows 28-40 (see below).

Definition files freshly printed in the 2026-11-01 open-close pass (this revision):
`core/urlnormalizer/NormalizeUrl.java` (423 lines), `core/urlnormalizer/PathResolver.java`,
`core/urlnormalizer/PercentEncoder.java` (125 lines), `core/utils/BindingAdapterUtils.java`
(112 lines), `core/utils/DateUtils.java` (218 lines) — all in `~/workspace/b565758-openclose-src/`.
`core/utils/BencodeFileTreeUtils.java` line numbers remain the prior print (not re-fetched this
revision); rows 18-19 rest on the prior print plus the fresh AddTorrentViewModel call site.

## Revision note — OPEN-closing pass, 2026-11-01 (UNVERIFIED)

Counts before: 22 REACHABLE / 0 UNREACHABLE / 18 OPEN. Counts after: 33 / 0 / 7.
Flips, all OPEN → REACHABLE on freshly printed layouts/source in `~/workspace/b565758-openclose-src/`:
rows 20-27 (all 8 `BindingAdapterUtils.format*` methods) → REACHABLE INFERRED on printed layout
attributes/expressions (see row citations; inflate sites for the state/pieces/info fragments are
carried from prior fresh passes, flagged per row — the generated dispatch step itself is INFERRED);
rows 34-36 (`DateUtils.formatElapsedTime` ×2, `initFormatStrings`) → REACHABLE INFERRED via the
printed `formatETA` → `formatElapsedTime` chain (internal call sites printed; INFERRED/SOURCE
alternative recorded in row 34). Still OPEN (7): rows 2, 3 (NormalizeUrl option gates — the three
fresh `normalize` callers all set only `decode = false`), rows 13-17 (PercentEncoder chain, rooted
at `decode` under `if (options.decode)` with no printed `decode = true` caller and no printed
1-arg `normalize` caller). No row flipped to UNREACHABLE (no saved full-repo grep). Build: not run.
C1: not run. Nothing merged, nothing pushed.

## Counts — mechanically verified

- **40 rows, sequence 1–40 intact, in plan order.**
- **33 REACHABLE proposed / 7 UNREACHABLE proposed / 0 OPEN (corrected 2026-11-01 re-check; the round-2 revision at the top already stated 33/7/0).**
- REACHABLE confirmed_by: SOURCE 21 / INFERRED 12 (row 28 `<clinit>`, rows 20-27 binding dispatch, rows 34-36 via generated dispatch).
- **0 rows verified for merge** until main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1.

## Shared routes

- NormalizeUrl: DetailTorrentFragment (fresh) :719-720, :726 → `normalize` → `doNormalize`.
  Inside `doNormalize` (prior print): `decode` only at :217 under `if (options.decode)`; `parseQuery` :225;
  `PathResolver.resolve(path, path)` :259 (only if `path != null`); `isMatch` :267 (directory-index
  block) and :282 (query-filter loop); `join` :268 (inside `removeDirectoryIndex` block);
  `urlToString` :290-291; `makeUserInfo` only from `urlToString` :397 under `user != null && !user.isEmpty()`,
  while `doNormalize` :232-235 nulls `user`/`password` when `options.removeAuthentication` is true (default).
  The printed caller changes only `decode`, leaving `removeDirectoryIndex` at default empty and
  `removeAuthentication` at default true. Rows whose only path runs through a condition the printed
  caller does not satisfy are OPEN, not UNREACHABLE: another, unprinted caller could set those options.
- DateUtils: TorrentFilterCollection (fresh) date-added predicates call the start/end pairs below;
  those predicates are returned by Utils drawer-group filters (batch 57, MainActivity fresh anchors there).
- Non-conflations checked: `TorrentService.java:415` uses `android.text.format.DateUtils.formatElapsedTime`,
  NOT this `DateUtils` — excluded. `NormalizeUrl.join` ≠ `PathResolver.join` (different classes, rows 2 vs 9).
  `TorrentContentFileTreeUtils.buildFileTree` (batch 57, different class) ≠ `BencodeFileTreeUtils.buildFileTree` (row 18).

## Rows

| # | Method | Label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | NormalizeUrl.isMatch(String,String[]) | REACHABLE | SOURCE | Prior print :304-315. Called from `doNormalize` :282 (query-filter loop; default `removeQueryParameters` is `["utm_\\w+"]` :71, so guard :278 satisfied on a URL with a query). Route: DetailTorrentFragment (fresh) :726 → `normalize` → `doNormalize` → here. |
| 2 | NormalizeUrl.join(CharSequence,String[]) | UNREACHABLE | INFERRED | Kind `branch_never_taken`. Only call site `doNormalize` :268, inside `if (options.removeDirectoryIndex.length > 0)` :263. Default is empty (:90) and the saved 252-file grep finds ZERO assignments to `removeDirectoryIndex` anywhere in the app tree, so the guard can never be satisfied in app code. The only 3 `normalize` callers tree-wide are DetailTorrentFragment :726, CreateTorrentViewModel :311, AddLinkViewModel :69, none of which sets the field. Re-check 2026-11-01 complete-tree+XML (281 Java + 73 XML, greps above): SURVIVED, still zero assignments and zero additional callers. |
| 3 | NormalizeUrl.makeUserInfo(String,String) | UNREACHABLE | INFERRED | Kind `branch_never_taken`. Only call site `urlToString` :397, guarded `user != null && !user.isEmpty()` :396. `doNormalize` :232-234 nulls `user`/`password` whenever `removeAuthentication` is true; default is true (:100) and the saved 252-file grep finds ZERO assignments to `removeAuthentication` anywhere in the app tree, so `user` is always null at the `urlToString` :290 call and the guard can never be satisfied in app code. Re-check 2026-11-01 complete-tree+XML (281 Java + 73 XML, greps above): SURVIVED, still zero assignments. |
| 4 | NormalizeUrl.mapToQuery(Map) | REACHABLE | SOURCE | Prior print :364-385. Called unconditionally from `doNormalize` :290-291. Route as row 1. |
| 5 | NormalizeUrl.normalize(String,Options) | REACHABLE | SOURCE | Prior print :178-189. Called from DetailTorrentFragment (fresh) :726. |
| 6 | NormalizeUrl.parseQuery(String) | REACHABLE | SOURCE | Prior print :333-362. Called unconditionally from `doNormalize` :225. Route as row 1. |
| 7 | NormalizeUrl.urlToString(String×7) | REACHABLE | SOURCE | Prior print :387-414. Called unconditionally from `doNormalize` :290-291. Route as row 1. |
| 8 | NormalizeUrl$Options.<init>() | REACHABLE | SOURCE | Prior print :42-156 (implicit default ctor). Called from DetailTorrentFragment (fresh) :719 and from `doNormalize` :197 (when `options == null`). |
| 9 | PathResolver.join(CharSequence,List) | REACHABLE | SOURCE | Prior print :110-124. Called from `resolve(String[])` :107. Route: DetailTorrentFragment (fresh) :726 → `normalize` → `doNormalize` :259 → `resolve(String,String)` → `resolve(String[])` → here. Distinct from row 2. |
| 10 | PathResolver.merge(String,String) | REACHABLE | SOURCE | Prior print :46-63. Called from `resolve(String,String)` :28. Route as row 9. |
| 11 | PathResolver.resolve(String,String) | REACHABLE | SOURCE | Prior print :27-34. Called from `doNormalize` :259 (when `path != null`). Route as row 9. |
| 12 | PathResolver.resolve(String[]) | REACHABLE | SOURCE | Prior print :72-108. Called from `resolve(String,String)` :33. Route as row 9. |
| 13 | PercentEncoder.<clinit>() | UNREACHABLE | INFERRED | Kind `branch_never_taken` (inherited from row 14). The class's first active use is `decode` (row 14); `decode` sits behind the never-taken `if (options.decode)` branch, so the class is never actively used in app code and its static initialiser never runs. `utf8Masks` field is PercentEncoder :16. Re-check 2026-11-01 complete-tree+XML (281 Java + 73 XML, greps above): SURVIVED. |
| 14 | PercentEncoder.decode(String) | UNREACHABLE | INFERRED | Kind `branch_never_taken`. Only call site `doNormalize` :217, inside `if (options.decode)` :216. All 3 `normalize` callers tree-wide set `decode = false` (DetailTorrentFragment :720, CreateTorrentViewModel :309, AddLinkViewModel :68); the saved 252-file grep finds no `decode = true` assignment and no caller of 1-arg `normalize(String)` (:165-168, which would default `decode = true` via :197). The branch is therefore never taken in app code. Re-check 2026-11-01 complete-tree+XML (281 Java + 73 XML, greps above): SURVIVED, still no `decode = true` and no 1-arg caller. |
| 15 | PercentEncoder.needsUnescaping(String) | UNREACHABLE | INFERRED | Kind `branch_never_taken` (inherited from row 14). Only call site `decode` :35; `decode` never runs (row 14), so this method never runs. Re-check 2026-11-01 complete-tree+XML (281 Java + 73 XML, greps above): SURVIVED. |
| 16 | PercentEncoder.pow(int,int) | UNREACHABLE | INFERRED | Kind `branch_never_taken` (inherited from rows 14/17). Only call site `unhex` :111; `unhex` runs only from `decode` (row 17), which never runs (row 14). Re-check 2026-11-01 complete-tree+XML (281 Java + 73 XML, greps above): SURVIVED. |
| 17 | PercentEncoder.unhex(char[]) | UNREACHABLE | INFERRED | Kind `branch_never_taken` (inherited from row 14). Only call sites `decode` :54 and :79; `decode` never runs (row 14), so this method never runs. Re-check 2026-11-01 complete-tree+XML (281 Java + 73 XML, greps above): SURVIVED. |
| 18 | BencodeFileTreeUtils.buildFileTree(List) | REACHABLE | SOURCE | Prior print :46-117. Called from AddTorrentViewModel (fresh) :379 `BencodeFileTreeUtils.buildFileTree(files)`. ViewModel entry (which activity/fragment creates the ViewModel) was not freshly printed; proposed REACHABLE on the printed ViewModel call site, same convention as other batches — strict-entry caveat below. |
| 19 | BencodeFileTreeUtils.makeObject(int,String,long,BencodeFileTree,boolean) | REACHABLE | SOURCE | Prior print :119-126. Called from `buildFileTree` :102-104 whenever a path node is not already in the parent tree — satisfied by any non-empty file list. Inherits row 18 route. |
| 20 | BindingAdapterUtils.formatDate(TextView,long) | REACHABLE | INFERRED | Fresh `add_torrent_info.xml`:259 `app:formatDate="@{viewModel.info.creationDate}"` and fresh `fragment_detail_torrent_info.xml`:270/:292 `app:formatDate`. Generated binding dispatch from the printed attribute, hence INFERRED. Inflate chain: AddTorrentInfoFragment (prior fresh print) :93 inflates `fragment_add_torrent_info`, which freshly includes `@layout/add_torrent_info` at :16-17; DetailTorrentInfoFragment (prior fresh prints, b8788/b9192/b119120) :100 inflates `fragment_detail_torrent_info`. |
| 21 | BindingAdapterUtils.formatETA(Context,long) | REACHABLE | INFERRED | Fresh `fragment_detail_torrent_state.xml`:146 `android:text="@{BindingAdapterUtils.formatETA(context, viewModel.info.torrentInfo.ETA)}"`. Layout expression, generated dispatch, hence INFERRED. State layout inflated by DetailTorrentStateFragment (prior fresh prints, b9192/b383940) :73. Prior print :68-72 body calls `DateUtils.formatElapsedTime` :71 — that is rows 34-36, not this row. |
| 22 | BindingAdapterUtils.formatFileSize(TextView,long,String) | REACHABLE | INFERRED | Fresh `add_torrent_info.xml`:178/:187, `fragment_detail_torrent_info.xml`:189/:198, `fragment_detail_torrent_state.xml`:176, all `app:fileSize`. Generated dispatch from printed attributes, hence INFERRED. Inflate chain as row 20, plus DetailTorrentStateFragment :73 (prior fresh print) for the state layout. |
| 23 | BindingAdapterUtils.formatFloat(TextView,double,int) | REACHABLE | INFERRED | Fresh `fragment_detail_torrent_state.xml`:197/:299 `app:floatNum`, matching prior print `@BindingAdapter({"floatNum","floatPrecision"})`. Generated dispatch, hence INFERRED. State layout inflated by DetailTorrentStateFragment :73 (prior fresh print). |
| 24 | BindingAdapterUtils.formatPieces(Context,int,int,int) | REACHABLE | INFERRED | Fresh `fragment_detail_torrent_state.xml`:278 `android:text="@{BindingAdapterUtils.formatPieces(context, viewModel.info.advancedInfo.downloadedPieces, viewModel.info.metaInfo.numPieces, viewModel.info.metaInfo.pieceLength)}"`. Layout expression, generated dispatch, hence INFERRED. |
| 25 | BindingAdapterUtils.formatPiecesInfo(Context,int,int,int) | REACHABLE | INFERRED | Fresh `fragment_detail_torrent_pieces.xml`:47 `android:text="@{BindingAdapterUtils.formatPiecesInfo(context, viewModel.info.advancedInfo.downloadedPieces, viewModel.info.metaInfo.numPieces, viewModel.info.metaInfo.pieceLength)}"`. Layout expression, generated dispatch, hence INFERRED. Pieces layout inflated by DetailTorrentPiecesFragment (prior fresh prints, b27/b67) :71. |
| 26 | BindingAdapterUtils.formatProgress(Context,long,long,int) | REACHABLE | INFERRED | Fresh `fragment_detail_torrent_state.xml`:125 `android:text="@{BindingAdapterUtils.formatProgress(context, viewModel.info.torrentInfo.receivedBytes, viewModel.info.torrentInfo.totalBytes, viewModel.info.torrentInfo.progress)}"`. Layout expression, generated dispatch, hence INFERRED. |
| 27 | BindingAdapterUtils.formatSpeed(Context,long,long) | REACHABLE | INFERRED | Fresh `fragment_detail_torrent_state.xml`:45 `android:text="@{BindingAdapterUtils.formatSpeed(context, viewModel.info.torrentInfo.uploadSpeed, viewModel.info.torrentInfo.downloadSpeed)}"`. Layout expression, generated dispatch, hence INFERRED. |
| 28 | DateUtils.<clinit>() | REACHABLE | INFERRED | Fresh DateUtils static fields :33-35, :41; no explicit static block. First printed use is TorrentFilterCollection (fresh) calling start/end pairs below. JVM initialisation dispatch, hence INFERRED. |
| 29 | DateUtils.endOfMonth(long) | REACHABLE | SOURCE | Fresh DateUtils :167-178. Called from TorrentFilterCollection (fresh) :83. |
| 30 | DateUtils.endOfToday(long) | REACHABLE | SOURCE | Fresh DateUtils :106-116. Called from TorrentFilterCollection (fresh) :53 and from `endOfYesterday` :132. |
| 31 | DateUtils.endOfWeek(long) | REACHABLE | SOURCE | Fresh DateUtils :140-152. Called from TorrentFilterCollection (fresh) :73. |
| 32 | DateUtils.endOfYear(long) | REACHABLE | SOURCE | Fresh DateUtils :193-204. Called from TorrentFilterCollection (fresh) :93. |
| 33 | DateUtils.endOfYesterday(long) | REACHABLE | SOURCE | Fresh DateUtils :130-133 (calls `endOfToday` :132). Called from TorrentFilterCollection (fresh) :63. |
| 34 | DateUtils.formatElapsedTime(Context,long) | REACHABLE | INFERRED | Fresh DateUtils :43-46, delegates to 3-arg overload :45. Caller is `BindingAdapterUtils.formatETA` (fresh :71, now REACHABLE row 21). INFERRED because the route's first step is generated binding dispatch; the internal call sites (formatETA :71, 2-arg :45, 3-arg :80) are printed, so under a strict per-row-source reading these three rows would read SOURCE — labels unaffected, merger to pick one. |
| 35 | DateUtils.formatElapsedTime(Context,StringBuilder,long) | REACHABLE | INFERRED | Fresh DateUtils :48-90. Called from 2-arg overload :45 (now REACHABLE row 34). Same INFERRED note as row 34. |
| 36 | DateUtils.initFormatStrings(Context) | REACHABLE | INFERRED | Fresh DateUtils :92-104. Called from 3-arg `formatElapsedTime` :80 (now REACHABLE row 35). Same INFERRED note as row 34. |
| 37 | DateUtils.startOfMonth(long) | REACHABLE | SOURCE | Fresh DateUtils :180-191. Called from TorrentFilterCollection (fresh) :82. |
| 38 | DateUtils.startOfToday(long) | REACHABLE | SOURCE | Fresh DateUtils :118-128. Called from TorrentFilterCollection (fresh) :52 and from `startOfYesterday` (batch 57 row 1, fresh :135-138). |
| 39 | DateUtils.startOfWeek(long) | REACHABLE | SOURCE | Fresh DateUtils :154-165. Called from TorrentFilterCollection (fresh) :72. |
| 40 | DateUtils.startOfYear(long) | REACHABLE | SOURCE | Fresh DateUtils :206-217. Called from TorrentFilterCollection (fresh) :92. |

## Undecided conventions recorded, not decided

- **Strict-entry:** routes anchor at DetailTorrentFragment, AddTorrentViewModel, and TorrentFilterCollection
  call sites, not at a printed launcher entry. Under a strict launcher-entry rule, all 22 REACHABLE
  rows revert to OPEN. Merger must pick one strict-entry convention for all batches.
- **Confirmed_by:** per-row convention used here — SOURCE = a printed direct app-code call site naming
  the method (including internal calls from a SOURCE-anchored method); INFERRED = JVM/generated/framework
  dispatch where registration or first use is printed. Labels are unaffected; only `confirmed_by`
  would change at merge under a whole-route convention.
- **Gated OPEN rows (rows 2, 3, 14):** OPEN is a condition-satisfaction statement, not a kind.
  A grep finding a caller with `removeDirectoryIndex` non-empty, `removeAuthentication=false`, or
  `decode=true` flips the corresponding row(s) to REACHABLE; finding none would be needed before
  any `closed_by_configuration` / `branch_never_taken` claim, and no such claim is made here.

## Still owed before merge

- Saved full-repo grep for the 7 remaining OPEN rows (2, 3, 13-17): (a) other
  `NormalizeUrl.normalize` callers and option settings (rows 2, 3, 14); (b) any other
  `PercentEncoder.decode` caller (rows 13-17). Rows 20-27 and 34-36 are closed by the fresh
  layouts above, not by a grep. No row was flipped to UNREACHABLE: no saved full-repo grep exists.
- Fresh definition prints for rows 1-27 (NormalizeUrl/PathResolver/PercentEncoder/BencodeFileTreeUtils/
  BindingAdapterUtils) if the merger requires them fresh, not prior-print.
- Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run.
- No fresh HTTP 429 was hit in this pass or in the 2026-11-01 open-close revision (70 fresh
  connector fetches across batches 56-58, one at a time with 25 s pauses, all succeeded).
