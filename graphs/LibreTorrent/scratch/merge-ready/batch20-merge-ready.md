# LibreTorrent batch 20 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED merge-ready part only. NOT verified for merge. NOT pushed. No edit to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**

**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push, so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1 check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 20 only, 40 methods, no other batch, no other app, no device replay, no Aegis.
- Source: existing proposal `~/workspace/libretorrent-batch20-proposal.md` (plus its Agent 4 update header) used as an INPUT / lead list only. Every row below was re-derived in this pass against source freshly fetched from branch `work-2026-10-31` via the GitHub connector, one file at a time with pauses. No verdict was copied without that re-check.
- Membership verified first, not guessed: exactly the 40 batch-20 rows in `handoff/LIBRETORRENT_BATCH_PLAN.tsv` (local plan copy `~/workspace/agent27-plan.tsv`, plan blob SHA `0104806dd666c840049b3db52823d4b384fa1c92`), all `TODO_CANDIDATE_REACHABLE`, in plan order. Plan status is a generator candidate, not evidence.
- Printed source freshly fetched in this pass, saved in `~/workspace/b202122-src/`, no fresh HTTP 429 hit, no `search_code` result used as evidence for any row:
  - `org/proninyaroslav/libretorrent/core/filter/TorrentFilterCollection.java` — SHA `6b00d42a…`, 105 lines.
  - `org/proninyaroslav/libretorrent/core/logger/LogEntry.java` — SHA `c0418b28…`, 115 lines.
  - `org/proninyaroslav/libretorrent/core/logger/Logger.java` — SHA `97ab16a7…`, 539 lines (also used for batch 21).
  - `org/proninyaroslav/libretorrent/core/model/session/SessionLogger.java` — SHA `f51ba318…`, 203 lines.
  - `org/proninyaroslav/libretorrent/core/model/session/TorrentSessionImpl.java` — SHA `aef9618c…`, 1721 lines.
  - `org/proninyaroslav/libretorrent/core/model/session/IPFilterImpl.java` — SHA `bf7e877d…`, 69 lines.
  - `org/proninyaroslav/libretorrent/core/model/session/IPFilterParser.java` — SHA `ead6fb8b…`, 271 lines.
  - `org/proninyaroslav/libretorrent/core/utils/Utils.java` — SHA `e726369e…`, 927 lines.
  - `org/proninyaroslav/libretorrent/core/model/TorrentEngine.java` — SHA `17d06efe…`, 1659 lines.
  - `org/proninyaroslav/libretorrent/ui/addtorrent/AddTorrentViewModel.java` — SHA `bec2f6ee…`, 575 lines.
  - `org/proninyaroslav/libretorrent/ui/main/MainViewModel.java` — SHA `73938fbb…`, 190 lines.
  - `org/proninyaroslav/libretorrent/ui/main/MainActivity.java` — SHA `d21f8b70…`, 812 lines.
  - `org/proninyaroslav/libretorrent/ui/log/LogAdapter.java` — SHA `4b5f83de…`, 113 lines.
  - `org/proninyaroslav/libretorrent/ui/log/LogViewModel.java` — SHA `f6374daf…`, 228 lines.
  - Exception definitions, all freshly fetched: `core/exception/FetchLinkException.java` SHA `31e6df97…` (40 lines), `FreeSpaceException.java` SHA `9c7c5641…` (41 lines), `IPFilterException.java` SHA `194f239b…` (36 lines), `NoFilesSelectedException.java` SHA `2bfa6571…` (31 lines), `NormalizeUrlException.java` SHA `35ec54e0…` (32 lines), `TorrentAlreadyExistsException.java` SHA `7a549138…` (31 lines), `UnknownUriException.java` SHA `bb3e1125…` (27 lines).
- `confirmed_by` convention used here, per row (not decided project-wide): SOURCE = a printed app-code line names the method (direct call, construction, or a call site inside printed app code naming it); INFERRED = unprinted framework/library/Rx dispatch where the definition plus registration, factory call, or enclosing call is printed. Under a whole-route INFERRED convention, SOURCE rows whose route passes through unprinted dispatch would flip to INFERRED; labels are unaffected. This convention is recorded, not decided.

## Counts — mechanically verified

- 40 rows, sequence 1–40 intact, in plan order.
- **REACHABLE proposed: 36 / 40 (SOURCE 24 / INFERRED 12)**
- **UNREACHABLE proposed: 0**
- **OPEN: 4 / 40 (rows 3, 6, 8, 39)**
- **Verified for merge: 0**

## Trunks (fresh prints)

- Exceptions: `TorrentEngine.addTorrentSync` free-space check; `AddTorrentViewModel` add-torrent check (`:493/:496`); `TorrentSessionImpl.addTorrent` (`:282`); `Utils.fetchHttpUrl` (`:462`, called from `AddTorrentViewModel:254` and `FeedDownloaderWorker:140`); IP-filter chain `TorrentSessionImpl:731` → `IPFilterParser.parseFile:59` → `parseDAT:96` / `parseP2P:180` → `filter.addRange` (`:163` / `:241`) → `IPFilterImpl.addRange:39` throws (`:44/:54/:58`). TorrentService anchor (fresh): `onCreate:109` `TorrentEngine.getInstance`, `init:131` `engine.doStart()`, `init:132` `engine.addListener`, `stopEngine:161` `engine.doStop()`, `onStartCommand` step calls `init:191`.
- Filters: `TorrentFilterCollection` static factories called from `MainViewModel:53-55` (all three filters initialised to `all()`), `MainActivity` tag clicks (`:300/:304/:306/:335/:499/:502/:510/:521`) and drawer clicks (`:590/:596/:615/:623` via `Utils.getDrawerGroupStatusFilter` / `getDrawerGroupDateAddedFilter`), and `Utils:841-887` (both drawer groups). `MainViewModel.getFilter:118-122` combines the four filters with `.test(state)`, which invokes the lambda body held in each filter object.
- Log: `SessionLogger.send(Alert):117-166` constructs `LogEntry` at `:124/:132/:144/:152/:158`, then `send(entry):166` → `Logger.send`. `LogAdapter` (PagedListAdapter) `diffCallback` and `ViewHolder.bind` name the LogEntry accessors (see table). `Logger.write` private overload `:425-443` prints `entry.toStringWithTimeStamp()` / `entry.toString()` at `:437`; `LogViewModel` clipboard path calls `entry.toString()` at `:222`.

## Table — 40 rows, plan order

| # | Method | Label proposed | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | FetchLinkException.<init>(String) | REACHABLE | SOURCE | Def FetchLinkException.java:30 (String ctor; (Exception) ctor is :35, distinct). Throw sites Utils.java:467 (`throw new FetchLinkException("No network connection")` inside fetchHttpUrl :462-475), :493, :509, :522 (String sites; :474 is the (Exception) overload, not this row). Callers of fetchHttpUrl printed: AddTorrentViewModel:254, FeedDownloaderWorker:140. |
| 2 | FreeSpaceException.<init>() | REACHABLE | SOURCE | Def FreeSpaceException.java:28 (no-arg; String ctor :30, (Exception) ctor :35, distinct). Throw sites TorrentEngine.java:1201 (addTorrentSync free-space check) and AddTorrentViewModel.java:496 (add-torrent check). |
| 3 | FreeSpaceException.<init>(String) | OPEN | — | Def FreeSpaceException.java:30. No String-ctor throw site in any file freshly fetched in this pass (both printed throw sites use the no-arg ctor). Not a global-unused claim; pending saved full-repo grep. NOT UNREACHABLE on this evidence. |
| 4 | IPFilterException.<init>(String) | REACHABLE | SOURCE | Def IPFilterException.java:26 (String ctor; no-arg :24, (Exception) :31, distinct). Throw sites IPFilterImpl.java:44, :54, :58, reached via TorrentSessionImpl.java:731 parseFile → IPFilterParser.java:163 (parseDAT) / :241 (parseP2P) addRange → IPFilterImpl.addRange:39. |
| 5 | NoFilesSelectedException.<init>() | REACHABLE | SOURCE | Def NoFilesSelectedException.java:24 (no-arg; String ctor :26, distinct). Throw site AddTorrentViewModel.java:493 (selectedFiles empty in add-torrent check). |
| 6 | NormalizeUrlException.<init>(String,Exception) | OPEN | — | Def NormalizeUrlException.java:21 (2-arg ctor; a (String) overload exists at :27 and is NOT this row). No throw site for either overload in any file freshly fetched in this pass. Not a global-unused claim; pending saved full-repo grep. NOT UNREACHABLE on this evidence. |
| 7 | TorrentAlreadyExistsException.<init>() | REACHABLE | SOURCE | Def TorrentAlreadyExistsException.java:24 (no-arg; String ctor :26, distinct). Throw site TorrentSessionImpl.java:282 (repo already contains torrent id, inside addTorrent). |
| 8 | UnknownUriException.<init> | OPEN | — | Def UnknownUriException.java:23 (only ctor, String; JVM descriptor `(Ljava/lang/String;)V`). Fresh corpus shows only declarations and catches (TorrentEngine.java:408/:973/:1155/:1182, TorrentSessionImpl.java:258/:319/:328/:408, AddTorrentViewModel.java:359, DetailTorrentViewModel.java:385/:455, FeedDownloaderWorker.java:154, SaveLogWorker.java:99) — no `new UnknownUriException(String)` site in any file freshly fetched in this pass. A catch is not a construction site. Pending saved full-repo grep. NOT UNREACHABLE on this evidence. |
| 9 | TorrentFilterCollection.all | REACHABLE | SOURCE | Def TorrentFilterCollection.java:27-29. Callers MainViewModel.java:53-55, MainActivity.java:304/:335/:499/:510, Utils.java:841/:851/:858/:870/:879. |
| 10 | TorrentFilterCollection.dateAddedMonth | REACHABLE | SOURCE | Def :77-85. Caller Utils.java:866. |
| 11 | TorrentFilterCollection.dateAddedToday | REACHABLE | SOURCE | Def :47-55. Caller Utils.java:860. |
| 12 | TorrentFilterCollection.dateAddedWeek | REACHABLE | SOURCE | Def :67-75. Caller Utils.java:864. |
| 13 | TorrentFilterCollection.dateAddedYear | REACHABLE | SOURCE | Def :87-95. Caller Utils.java:868. |
| 14 | TorrentFilterCollection.dateAddedYesterday | REACHABLE | SOURCE | Def :57-65. Caller Utils.java:862. |
| 15 | TorrentFilterCollection.lambda$all$0 | REACHABLE | INFERRED | Lambda body TorrentFilterCollection.java:28 (`(state) -> true`, inside `all()`). $0 = first lambda in source order. Invoked via `TorrentFilter.test` in MainViewModel.getFilter:118-122; Predicate dispatch unprinted, hence INFERRED, not SOURCE. Numbering source-order, NOT bytecode-verified. |
| 16 | TorrentFilterCollection.lambda$dateAddedMonth$8 | REACHABLE | INFERRED | Lambda body :78-84 (inside `dateAddedMonth()`). $8 = ninth lambda in source order. Same test() dispatch as row 15. |
| 17 | TorrentFilterCollection.lambda$dateAddedToday$5 | REACHABLE | INFERRED | Lambda body :48-54 (inside `dateAddedToday()`). $5 = sixth lambda in source order. Same test() dispatch as row 15. |
| 18 | TorrentFilterCollection.lambda$dateAddedWeek$7 | REACHABLE | INFERRED | Lambda body :69-74 (inside `dateAddedWeek()`). $7 = eighth lambda in source order. Same test() dispatch as row 15. |
| 19 | TorrentFilterCollection.lambda$dateAddedYear$9 | REACHABLE | INFERRED | Lambda body :88-94 (inside `dateAddedYear()`). $9 = tenth lambda in source order. Same test() dispatch as row 15. |
| 20 | TorrentFilterCollection.lambda$dateAddedYesterday$6 | REACHABLE | INFERRED | Lambda body :58-64 (inside `dateAddedYesterday()`). $6 = seventh lambda in source order. Same test() dispatch as row 15. |
| 21 | TorrentFilterCollection.lambda$noTags$11 | REACHABLE | INFERRED | Lambda body :102 (inside `noTags()`). $11 = twelfth lambda in source order. Same test() dispatch as row 15. |
| 22 | TorrentFilterCollection.lambda$statusDownloaded$2 | REACHABLE | INFERRED | Lambda body :36 (inside `statusDownloaded()`). $2 = third lambda in source order. Same test() dispatch as row 15. |
| 23 | TorrentFilterCollection.lambda$statusDownloading$1 | REACHABLE | INFERRED | Lambda body :32 (inside `statusDownloading()`). $1 = second lambda in source order. Same test() dispatch as row 15. |
| 24 | TorrentFilterCollection.lambda$statusDownloadingMetadata$3 | REACHABLE | INFERRED | Lambda body :40 (inside `statusDownloadingMetadata()`). $3 = fourth lambda in source order. Same test() dispatch as row 15. |
| 25 | TorrentFilterCollection.lambda$statusError$4 | REACHABLE | INFERRED | Lambda body :44 (inside `statusError()`). $4 = fifth lambda in source order. Same test() dispatch as row 15. |
| 26 | TorrentFilterCollection.lambda$tag$10 | REACHABLE | INFERRED | Lambda body :98 (inside `tag(TagInfo)`). $10 = eleventh lambda in source order. Same test() dispatch as row 15. |
| 27 | TorrentFilterCollection.noTags | REACHABLE | SOURCE | Def :101-103. Callers MainActivity.java:306, :502. |
| 28 | TorrentFilterCollection.statusDownloaded | REACHABLE | SOURCE | Def :35-37. Callers Utils.java:845, :883. |
| 29 | TorrentFilterCollection.statusDownloading | REACHABLE | SOURCE | Def :31-33. Callers Utils.java:843, :881. |
| 30 | TorrentFilterCollection.statusDownloadingMetadata | REACHABLE | SOURCE | Def :39-41. Callers Utils.java:847, :885. |
| 31 | TorrentFilterCollection.statusError | REACHABLE | SOURCE | Def :43-45. Callers Utils.java:849, :887. |
| 32 | TorrentFilterCollection.tag | REACHABLE | SOURCE | Def :97-99. Callers MainActivity.java:300, :521. |
| 33 | LogEntry.<init> | REACHABLE | SOURCE | Def LogEntry.java:39-47 (int,String,String,long). Construction sites SessionLogger.java:124, :132, :144, :152, :158 (inside send(Alert)), then send(entry):166 → Logger.send. |
| 34 | LogEntry.equals | REACHABLE | SOURCE | Def LogEntry.java:77-90. Call site LogAdapter.java:73 (`oldItem.equals(newItem)` in diffCallback.areContentsTheSame). DiffUtil invocation of the callback is framework dispatch (INFERRED), but the call site naming equals is printed app code. |
| 35 | LogEntry.getId | REACHABLE | SOURCE | Def LogEntry.java:49-52. Call site LogAdapter.java:80 (`oldItem.getId() == newItem.getId()` in areItemsTheSame). Same framework-dispatch note as row 34. |
| 36 | LogEntry.getMsg | REACHABLE | SOURCE | Def LogEntry.java:60-64. Call site LogAdapter.java:108 (`binding.msg.setText(entry.getMsg())` in ViewHolder.bind). |
| 37 | LogEntry.getTag | REACHABLE | SOURCE | Def LogEntry.java:55-58. Call site LogAdapter.java:107 (`binding.tag.setText(entry.getTag())`). |
| 38 | LogEntry.getTimeStampAsString | REACHABLE | SOURCE | Def LogEntry.java:71-74. Call sites LogAdapter.java:109 (`binding.timeStamp.setText(entry.getTimeStampAsString())`) and LogEntry.java:105 (toStringWithTimeStamp, batch 21 row 1). Note: `getTimeStamp()` (long, LogEntry.java:66-69) is NOT a batch 20/21 row — do not conflate. |
| 39 | LogEntry.hashCode | OPEN | — | Def LogEntry.java:93-101 only. No hashCode caller in any file freshly fetched in this pass. The printed `equals` call (row 34) does not by itself print a hashCode call. Pending saved full-repo grep. NOT UNREACHABLE on this evidence. |
| 40 | LogEntry.toString | REACHABLE | SOURCE | Def LogEntry.java:110-113. Call sites Logger.java:437 (`entry.toStringWithTimeStamp() : entry.toString()` in private write) and LogViewModel.java:222 (clipboard text). |

## OPEN rows — what resolves them (all stay OPEN, none flipped to UNREACHABLE)

- Row 3 `FreeSpaceException.<init>(String)`: one printed `new FreeSpaceException(String)` throw site.
- Row 6 `NormalizeUrlException.<init>(String,Exception)`: one printed throw site for the 2-arg overload (the (String) overload at :27 is a different row in no batch — do not count it).
- Row 8 `UnknownUriException.<init>(String)`: one printed `new UnknownUriException(String)` throw site (catches/declarations do not count).
- Row 39 `LogEntry.hashCode`: one printed hashCode caller (e.g. a hash-based collection use or an explicit call), or a saved full-repo grep for `LogEntry` hash use.

## Caveats the merger must see (recorded, not decided)

1. **Strict-entry:** no launcher step was printed in this pass. Filter rows anchor at MainActivity/MainViewModel/Utils, exception rows at AddTorrentViewModel/TorrentEngine/TorrentSessionImpl/Utils, log rows at SessionLogger/LogAdapter. Under a strict launcher-entry rule all 36 REACHABLE rows revert to OPEN on that point alone. TorrentService anchor above (onCreate/init/stopEngine) is printed, but who starts TorrentService was not printed in this pass.
2. **Lambda numbering:** TorrentFilterCollection $0–$11 are source-order only, NOT bytecode-verified. A swap within the group would not change any label, since every factory method in the file has a printed caller and every lambda body is the filter held by that factory.
3. **confirmed_by:** per-row convention stated at the top. Under a whole-route INFERRED convention, the SOURCE rows whose routes pass through framework/Rx dispatch (notably rows 34–35 via DiffUtil) would read INFERRED; labels unaffected.
4. **Overload traps avoided:** FetchLinkException (Exception) site Utils:474 does not establish row 1; FreeSpaceException String/(Exception) ctors do not establish row 2; NormalizeUrlException (String) :27 does not establish row 6; LogEntry.getTimeStamp() does not establish row 38.

## Not claimed / still owed before merge

- No build, sampler, full-repo grep, or C1 — build and C1 marked **not run** (Mac after push, never claimed passed). No push made. Main-agent spot-check (1 in 5) and `py_compile` remain outstanding.
- Saved full-repo grep for the 4 OPEN rows before any flip to UNREACHABLE.
- Scope strictly batch 20, LibreTorrent labels only, branch `work-2026-10-31` only, no other batch/app, no device replay, no Aegis.
