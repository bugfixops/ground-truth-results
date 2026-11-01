# LibreTorrent batch 56 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
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

Prior full prints relied on for definition line numbers (NOT re-fetched this pass; merger must
re-verify if it requires fresh definition prints): `core/urlnormalizer/NormalizeUrl.java`,
`core/urlnormalizer/PathResolver.java`, `core/urlnormalizer/PercentEncoder.java`,
`core/utils/BencodeFileTreeUtils.java`, `core/utils/BindingAdapterUtils.java`.
Those line numbers below are the prior proposal's printed numbers, cross-checked for internal
consistency in this pass (call sites inside NormalizeUrl/PathResolver/PercentEncoder chain as
described there), not newly fetched.

## Counts — mechanically verified

- **40 rows, sequence 1–40 intact, in plan order.**
- **22 REACHABLE proposed / 0 UNREACHABLE proposed / 18 OPEN.**
- REACHABLE confirmed_by: SOURCE 21 / INFERRED 1 (row 28 `<clinit>` only).
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
| 2 | NormalizeUrl.join(CharSequence,String[]) | OPEN | — | Prior print :317-331. Only call site `doNormalize` :268, inside `if (options.removeDirectoryIndex.length > 0)` :263. Default empty :90; fresh DetailTorrentFragment sets no `removeDirectoryIndex`. Pending saved full-repo grep for other `normalize` callers / `removeDirectoryIndex` assignments. NOT UNREACHABLE. |
| 3 | NormalizeUrl.makeUserInfo(String,String) | OPEN | — | Prior print :416-422. Only call site `urlToString` :397, guarded `user != null && !user.isEmpty()` :396. `doNormalize` :232-235 nulls user/password when `removeAuthentication` true (default :100); fresh caller does not change it. Pending full-repo grep. NOT UNREACHABLE. |
| 4 | NormalizeUrl.mapToQuery(Map) | REACHABLE | SOURCE | Prior print :364-385. Called unconditionally from `doNormalize` :290-291. Route as row 1. |
| 5 | NormalizeUrl.normalize(String,Options) | REACHABLE | SOURCE | Prior print :178-189. Called from DetailTorrentFragment (fresh) :726. |
| 6 | NormalizeUrl.parseQuery(String) | REACHABLE | SOURCE | Prior print :333-362. Called unconditionally from `doNormalize` :225. Route as row 1. |
| 7 | NormalizeUrl.urlToString(String×7) | REACHABLE | SOURCE | Prior print :387-414. Called unconditionally from `doNormalize` :290-291. Route as row 1. |
| 8 | NormalizeUrl$Options.<init>() | REACHABLE | SOURCE | Prior print :42-156 (implicit default ctor). Called from DetailTorrentFragment (fresh) :719 and from `doNormalize` :197 (when `options == null`). |
| 9 | PathResolver.join(CharSequence,List) | REACHABLE | SOURCE | Prior print :110-124. Called from `resolve(String[])` :107. Route: DetailTorrentFragment (fresh) :726 → `normalize` → `doNormalize` :259 → `resolve(String,String)` → `resolve(String[])` → here. Distinct from row 2. |
| 10 | PathResolver.merge(String,String) | REACHABLE | SOURCE | Prior print :46-63. Called from `resolve(String,String)` :28. Route as row 9. |
| 11 | PathResolver.resolve(String,String) | REACHABLE | SOURCE | Prior print :27-34. Called from `doNormalize` :259 (when `path != null`). Route as row 9. |
| 12 | PathResolver.resolve(String[]) | REACHABLE | SOURCE | Prior print :72-108. Called from `resolve(String,String)` :33. Route as row 9. |
| 13 | PercentEncoder.<clinit>() | OPEN | — | Prior print :16 static `utf8Masks`. First active use would be `decode`, which is OPEN (row 14). Inherits OPEN. |
| 14 | PercentEncoder.decode(String) | OPEN | — | Prior print :33-89. Only call site `doNormalize` :217, inside `if (options.decode)` :216. Fresh caller sets `decode = false` (DetailTorrentFragment :720). No printed caller of 1-arg `normalize(String)` (:165-168, `null` → default `decode=true` :197) or `decode=true` caller found. Pending full-repo grep. NOT UNREACHABLE. |
| 15 | PercentEncoder.needsUnescaping(String) | OPEN | — | Prior print :24-26. Only call site `decode` :35. Inherits row 14 OPEN. |
| 16 | PercentEncoder.pow(int,int) | OPEN | — | Prior print :116-124. Only call site `unhex` :111. Inherits row 17 OPEN. |
| 17 | PercentEncoder.unhex(char[]) | OPEN | — | Prior print :96-114. Only call sites `decode` :54 and :79. Inherits row 14 OPEN. |
| 18 | BencodeFileTreeUtils.buildFileTree(List) | REACHABLE | SOURCE | Prior print :46-117. Called from AddTorrentViewModel (fresh) :379 `BencodeFileTreeUtils.buildFileTree(files)`. ViewModel entry (which activity/fragment creates the ViewModel) was not freshly printed; proposed REACHABLE on the printed ViewModel call site, same convention as other batches — strict-entry caveat below. |
| 19 | BencodeFileTreeUtils.makeObject(int,String,long,BencodeFileTree,boolean) | REACHABLE | SOURCE | Prior print :119-126. Called from `buildFileTree` :102-104 whenever a path node is not already in the parent tree — satisfied by any non-empty file list. Inherits row 18 route. |
| 20 | BindingAdapterUtils.formatDate(TextView,long) | OPEN | — | Prior print `@BindingAdapter({"formatDate"})` :50-55. Generated dispatch would run only from a layout using `formatDate`. No such layout printed in this pass, no direct Java caller in fresh greps (Utils/MainActivity/TFC/DetailTorrentFragment/AddTorrentViewModel). Pending layout/full-repo grep. NOT UNREACHABLE. |
| 21 | BindingAdapterUtils.formatETA(Context,long) | OPEN | — | Prior print :68-72. No printed Java or layout caller. Note it calls `DateUtils.formatElapsedTime` :71 — that does not make `formatETA` itself reachable, and is why rows 34-36 are also OPEN. Pending full-repo grep. |
| 22 | BindingAdapterUtils.formatFileSize(TextView,long,String) | OPEN | — | Prior print `@BindingAdapter({"fileSize","formatFileSize"})` :38-48. Same as row 20: no printed layout, no direct caller. Pending layout/full-repo grep. NOT UNREACHABLE. |
| 23 | BindingAdapterUtils.formatFloat(TextView,double,int) | OPEN | — | Prior print `@BindingAdapter({"floatNum","floatPrecision"})` :74-80. Same as row 20. Pending layout/full-repo grep. NOT UNREACHABLE. |
| 24 | BindingAdapterUtils.formatPieces(Context,int,int,int) | OPEN | — | Prior print :82-91. No printed Java or layout caller. Pending full-repo grep (incl. layout expressions). NOT UNREACHABLE. |
| 25 | BindingAdapterUtils.formatPiecesInfo(Context,int,int,int) | OPEN | — | Prior print :102-111. Same as row 24. Pending full-repo grep. NOT UNREACHABLE. |
| 26 | BindingAdapterUtils.formatProgress(Context,long,long,int) | OPEN | — | Prior print :57-66. No printed Java or layout caller. Pending full-repo grep. NOT UNREACHABLE. |
| 27 | BindingAdapterUtils.formatSpeed(Context,long,long) | OPEN | — | Prior print :93-100. No printed Java or layout caller. Pending full-repo grep. NOT UNREACHABLE. |
| 28 | DateUtils.<clinit>() | REACHABLE | INFERRED | Fresh DateUtils static fields :33-35, :41; no explicit static block. First printed use is TorrentFilterCollection (fresh) calling start/end pairs below. JVM initialisation dispatch, hence INFERRED. |
| 29 | DateUtils.endOfMonth(long) | REACHABLE | SOURCE | Fresh DateUtils :167-178. Called from TorrentFilterCollection (fresh) :83. |
| 30 | DateUtils.endOfToday(long) | REACHABLE | SOURCE | Fresh DateUtils :106-116. Called from TorrentFilterCollection (fresh) :53 and from `endOfYesterday` :132. |
| 31 | DateUtils.endOfWeek(long) | REACHABLE | SOURCE | Fresh DateUtils :140-152. Called from TorrentFilterCollection (fresh) :73. |
| 32 | DateUtils.endOfYear(long) | REACHABLE | SOURCE | Fresh DateUtils :193-204. Called from TorrentFilterCollection (fresh) :93. |
| 33 | DateUtils.endOfYesterday(long) | REACHABLE | SOURCE | Fresh DateUtils :130-133 (calls `endOfToday` :132). Called from TorrentFilterCollection (fresh) :63. |
| 34 | DateUtils.formatElapsedTime(Context,long) | OPEN | — | Fresh DateUtils :43-46, delegates to 3-arg overload :45. Only printed caller is `BindingAdapterUtils.formatETA` :71, itself OPEN (row 21). `TorrentService.java:415` is android DateUtils, excluded. Pending full-repo grep. NOT UNREACHABLE. |
| 35 | DateUtils.formatElapsedTime(Context,StringBuilder,long) | OPEN | — | Fresh DateUtils :48-90. Only printed caller is 2-arg overload :45. Inherits row 34 OPEN. |
| 36 | DateUtils.initFormatStrings(Context) | OPEN | — | Fresh DateUtils :92-104. Only printed caller is 3-arg `formatElapsedTime` :80. Inherits row 35 OPEN. |
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

- Saved full-repo grep for the 18 OPEN rows, priority: (a) other `NormalizeUrl.normalize` callers
  and option settings (rows 2, 3, 14); (b) layouts using `formatDate`/`fileSize`/`floatNum` and
  expressions calling `BindingAdapterUtils.format*` (rows 20-27, which would also settle rows 34-36);
  (c) any other `PercentEncoder.decode` caller (rows 13-17).
- Fresh definition prints for rows 1-27 (NormalizeUrl/PathResolver/PercentEncoder/BencodeFileTreeUtils/
  BindingAdapterUtils) if the merger requires them fresh, not prior-print.
- Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run.
- No fresh HTTP 429 was hit in this pass (10 fresh connector fetches across batches 56-58, one at a time
  with 20-25 s pauses, all succeeded).
