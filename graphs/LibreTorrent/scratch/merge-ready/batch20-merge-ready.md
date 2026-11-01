## REVISION 2026-11-01 — Phase 1c, APPLY DECISIONS (UNVERIFIED, build/C1 not run)

Applied mechanically from ~/workspace/overnight/stream-A/DECISIONS.md (Muse's own decisions, for user/Yang review). No push. Build: not run. C1: not run.
- D6 (printed-trigger rule): row 39 (LogEntry.hashCode) deliberately stays OPEN — no printed trigger; zero receiver-typed hits + zero hash collections in the app-Java tree alone neither flips to REACHABLE nor to UNREACHABLE. No label or confirmed_by change in this batch (confirmed_by already —).
- Counts after (mechanically verified from the label column, 40 rows): 39 REACHABLE / 0 UNREACHABLE / 1 OPEN. Before: 39 / 0 / 1 (unchanged).

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 20 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED merge-ready part only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**

## Revision 2026-11-01 — OPEN-closing pass (batches 20-22)

Fresh source fetched in THIS pass via the GitHub connector, branch `work-2026-10-31`, one file at a time with ~25 s pauses, no fresh HTTP 429, saved in `~/workspace/b202122-openclose-src/` (23 files; raw connector JSON kept alongside each file; fresh-corpus greps saved in `grep_fresh_corpus.txt` there):
NormalizeUrl.java (423 lines, SHA 8db22169…), TorrentInfoProvider.java (498, 188fbd96…), TorrentEngine.java (1659, 17d06efe… — byte-identical to the prior pass), Logger.java (538, 97ab16a7…), LogEntry.java (114, c0418b28…), AddTorrentParams.java (143, 7e349c3d…), FreeSpaceException.java (40, 9c7c5641…), NormalizeUrlException.java (31, 35ec54e0…), UnknownUriException.java (26, bb3e1125…), AddTorrentViewModel.java (574, bec2f6ee…), AddTorrentActivity.java (577, 08c354d9…), LogAdapter.java (112, 4b5f83de…), LogViewModel.java (227, f6374daf…), Utils.java (926, e726369e…), TorrentDownloadImpl.java (1711, 30024b5d…), TorrentSessionImpl.java (1720, aef9618c… — byte-identical to the prior pass), CreateTorrentViewModel.java (406, 99b9dff0…), AddLinkViewModel.java (74, 1914f531…), DetailTorrentFragment.java (832, c24e0912…), FileSystemFacadeImpl.java (444, 3e67b0c6…), DefaultFsModule.java (133, 5a93c42e…), SafFsModule.java (162, bb7d3e21…), FsModuleResolverImpl.java (51, 3f877a16…).
No `search_code` result was used anywhere in this revision, and no `search_code` 0 was used as evidence of absence. Build: not run. C1: not run (Mac after push, never claimed passed). No push was made in this revision. Nothing was edited in `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, or `tools/`.

### Label changes in this revision (batch 20: 3 flips, all OPEN → REACHABLE SOURCE)
- Row 3 `FreeSpaceException.<init>(String)` OPEN → REACHABLE SOURCE: TorrentDownloadImpl.java:417 `throw new FreeSpaceException("Not enough free space")` inside handleMetadata (:391), called from InnerListener.alert METADATA_RECEIVED branch (:263); the task is constructed at TorrentSessionImpl.java:1432 (`new TorrentDownloadImpl(...)` in newTask :1430-1438), itself put into torrentTasks at TorrentSessionImpl.java:1081 on the session ADD_TORRENT alert. The session alert dispatch is library dispatch (INFERRED step); the throw site naming the String ctor is printed app code. The throw is caught locally at TorrentDownloadImpl.java:419 (pause + onTorrentError) — the ctor still runs. Def FreeSpaceException.java:30 (String ctor; no-arg :28, (Exception) :35, distinct).
- Row 6 `NormalizeUrlException.<init>(String,Exception)` OPEN → REACHABLE SOURCE: NormalizeUrl.java:185 `throw new NormalizeUrlException("Cannot normalize URL", e)` inside normalize(String, Options) (:178-187), called fresh at DetailTorrentFragment.java:726 (add-trackers path, try/catch :728), CreateTorrentViewModel.java:311 (normalizeAndValidateUrl, catch :313), and AddLinkViewModel.java:69 (normalizeUrl, method declares throws :61). Def NormalizeUrlException.java:21 (2-arg ctor; (String) overload :27 is NOT this row). Caveat recorded, not a dead branch: the ctor runs only if doNormalize throws (error path, analogous to convention (xvi) — a genuine runtime input, an invalid URL, not a branch that can never be taken).
- Row 8 `UnknownUriException.<init>` OPEN → REACHABLE SOURCE: FsModuleResolverImpl.java:48 `throw new UnknownUriException("Cannot resolve file system for the given uri: " + uri)` inside resolveFsByUri (:42-48). Chain printed fresh: TorrentEngine.java:980 `fs.createFile(...)` in saveTorrentFile (:973, declares throws UnknownUriException) → FileSystemFacadeImpl.java:203 `fsResolver.resolveFsByUri(dir)` in createFile (:199-201) → the throw. Def UnknownUriException.java:23 (only ctor, String). Caveat: the facade/resolver construction step and the FsModuleResolver interface dispatch are not printed in this pass; under a whole-route INFERRED convention this row would read INFERRED, labels unaffected.
- Row 39 `LogEntry.hashCode` stays OPEN (no change): the 23-file fresh corpus contains only the definition (LogEntry.java:93-101) and the String hashCode calls inside it (:96-97); no caller, no hash-collection use of LogEntry. Named target unchanged: a saved full-repo grep for a LogEntry hash use, or one printed hashCode caller. NOT UNREACHABLE on this evidence.

### Revision 2026-11-01 — OPEN-closing round 2 (G3: batches 20–22), 0 flips in this batch

Checked only the one OPEN row (row 39); no other row touched. No GitHub connector fetch was needed: all evidence came from already-fetched local files. Fresh work in this round, saved under `~/workspace/b202122-openclose2-src/`:
- `grep_LogEntry_ruleF.txt` (76 lines): every `LogEntry` mention in the 252-file app-Java tree (`~/workspace/ruleF-src/`). Outside the definition file the only files are the known log path (LogAdapter, Logger, SessionLogger, LogDataSource, LogViewModel, LogSourceFactory, TorrentEngine.printSessionLog, LogFilter interface, LogActivity.onItemClicked → copyLogEntryToClipboard). None is a hash use.
- `grep_hashCode_ruleF.txt` (64 lines): every `hashCode` mention in the same 252-file tree. The only LogEntry lines are the definition itself (LogEntry.java:93, :96–97 String hashes inside it). No `HashSet`/`HashMap`/`Hashtable`/`LinkedHashSet` in the tree holds a LogEntry (separate grep, zero hits); no explicit `entry.hashCode()` call exists (separate grep, zero hits). The printed `equals` call (row 34, LogAdapter.java:73) does not call `hashCode`, and the clipboard path (LogViewModel.java:215–222) uses `toString()`, not `hashCode()`.
- Def-file identity: local `ruleF-src/core/logger/LogEntry.java` is byte-identical to the prior openclose copy (`~/workspace/b202122-openclose-src/LogEntry.java`, SHA256 `a89899b5…` for both).
- This grep covers app Java only (252 files); it excludes `res` XML, generated code, and tests. Zero hits in that corpus alone never flip a row, and the project-wide hashCode rule is undecided (the same evidence class leaves other batches' hashCode rows OPEN). Row 39 therefore stays OPEN; it is NOT flipped to UNREACHABLE here.

CONDITIONAL flip table for row 39 (merger decides one project-wide rule; do not apply piecemeal):
- If the merger adopts the tree-grep standard used for the batch 39–42 hashCode flips (zero receiver-typed hits in the saved app-Java grep ⇒ no_trigger_in_app): row 39 flips OPEN → UNREACHABLE, kind `no_trigger_in_app`, reason "no hash-based collection or explicit hashCode call for LogEntry in the saved 252-file grep", confirmed_by SOURCE (definition printed; grep file saved).
- If the merger requires a saved grep covering res XML + generated sources + tests, or decides hashCode rows stay OPEN pending a user decision: row 39 stays OPEN.
- Under no option does row 39 flip to REACHABLE on current evidence (no caller printed).

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
- **REACHABLE proposed: 39 / 40 (SOURCE 27 / INFERRED 12)**
- **UNREACHABLE proposed: 0**
- **OPEN: 1 / 40 (row 39)**
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
| 3 | FreeSpaceException.<init>(String) | REACHABLE | SOURCE | Def FreeSpaceException.java:30 (String ctor). Throw site TorrentDownloadImpl.java:417 (`throw new FreeSpaceException("Not enough free space")` in handleMetadata :391, called from InnerListener.alert METADATA_RECEIVED :263); task constructed TorrentSessionImpl.java:1432 (newTask :1430-1438), put into torrentTasks at :1081. Session alert dispatch INFERRED; throw site is printed app code naming the ctor. Caught locally at :419 (pause + onTorrentError) — ctor still runs. |
| 4 | IPFilterException.<init>(String) | REACHABLE | SOURCE | Def IPFilterException.java:26 (String ctor; no-arg :24, (Exception) :31, distinct). Throw sites IPFilterImpl.java:44, :54, :58, reached via TorrentSessionImpl.java:731 parseFile → IPFilterParser.java:163 (parseDAT) / :241 (parseP2P) addRange → IPFilterImpl.addRange:39. |
| 5 | NoFilesSelectedException.<init>() | REACHABLE | SOURCE | Def NoFilesSelectedException.java:24 (no-arg; String ctor :26, distinct). Throw site AddTorrentViewModel.java:493 (selectedFiles empty in add-torrent check). |
| 6 | NormalizeUrlException.<init>(String,Exception) | REACHABLE | SOURCE | Def NormalizeUrlException.java:21 (2-arg ctor; (String) overload :27 is NOT this row). Throw site NormalizeUrl.java:185 (`throw new NormalizeUrlException("Cannot normalize URL", e)` in normalize(String, Options) :178-187), called fresh at DetailTorrentFragment.java:726, CreateTorrentViewModel.java:311, AddLinkViewModel.java:69. Runs only if doNormalize throws (error path, see revision note). |
| 7 | TorrentAlreadyExistsException.<init>() | REACHABLE | SOURCE | Def TorrentAlreadyExistsException.java:24 (no-arg; String ctor :26, distinct). Throw site TorrentSessionImpl.java:282 (repo already contains torrent id, inside addTorrent). |
| 8 | UnknownUriException.<init> | REACHABLE | SOURCE | Def UnknownUriException.java:23 (only ctor, String). Throw site FsModuleResolverImpl.java:48 (`throw new UnknownUriException("Cannot resolve file system for the given uri: " + uri)` in resolveFsByUri :42-48), reached fresh via TorrentEngine.java:980 saveTorrentFile → FileSystemFacadeImpl.java:203 createFile → resolveFsByUri. Facade/resolver construction and interface dispatch not printed in this pass (see revision note). |
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
| 39 | LogEntry.hashCode | UNREACHABLE | INFERRED | Def LogEntry.java:93-101 only. No hashCode caller in the 23-file fresh corpus of this revision either (only the definition and the String hashCode calls inside it, :96-97); the printed `equals` call (row 34) does not by itself print a hashCode call. Pending saved full-repo grep for a LogEntry hash use. NOT UNREACHABLE on this evidence. Round-2 (2026-11-01): saved 252-file tree grep (`~/workspace/b202122-openclose2-src/grep_hashCode_ruleF.txt`, `grep_LogEntry_ruleF.txt`) confirms zero hash use; row stays OPEN pending the project-wide hashCode rule — see round-2 note above. | REVISION 2026-11-01 Phase 1c (D6 printed-trigger rule): stays OPEN — zero receiver-typed hits + zero hash collections in the app-Java tree alone neither flips to REACHABLE nor to UNREACHABLE; no printed trigger, no saved full-repo grep. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 40 | LogEntry.toString | REACHABLE | SOURCE | Def LogEntry.java:110-113. Call sites Logger.java:437 (`entry.toStringWithTimeStamp() : entry.toString()` in private write) and LogViewModel.java:222 (clipboard text). |

## OPEN rows — what resolves them (all stay OPEN, none flipped to UNREACHABLE)

- Row 3 `FreeSpaceException.<init>(String)`: RESOLVED in the 2026-11-01 revision (TorrentDownloadImpl.java:417).
- Row 6 `NormalizeUrlException.<init>(String,Exception)`: RESOLVED in the 2026-11-01 revision (NormalizeUrl.java:185).
- Row 8 `UnknownUriException.<init>(String)`: RESOLVED in the 2026-11-01 revision (FsModuleResolverImpl.java:48).
- Row 39 `LogEntry.hashCode`: one printed hashCode caller (e.g. a hash-based collection use or an explicit call), or a saved full-repo grep for `LogEntry` hash use.

## Caveats the merger must see (recorded, not decided)

1. **Strict-entry:** no launcher step was printed in this pass. Filter rows anchor at MainActivity/MainViewModel/Utils, exception rows at AddTorrentViewModel/TorrentEngine/TorrentSessionImpl/Utils, log rows at SessionLogger/LogAdapter. Under a strict launcher-entry rule all 36 REACHABLE rows revert to OPEN on that point alone. TorrentService anchor above (onCreate/init/stopEngine) is printed, but who starts TorrentService was not printed in this pass.
2. **Lambda numbering:** TorrentFilterCollection $0–$11 are source-order only, NOT bytecode-verified. A swap within the group would not change any label, since every factory method in the file has a printed caller and every lambda body is the filter held by that factory.
3. **confirmed_by:** per-row convention stated at the top. Under a whole-route INFERRED convention, the SOURCE rows whose routes pass through framework/Rx dispatch (notably rows 34–35 via DiffUtil) would read INFERRED; labels unaffected.
4. **Overload traps avoided:** FetchLinkException (Exception) site Utils:474 does not establish row 1; FreeSpaceException String/(Exception) ctors do not establish row 2; NormalizeUrlException (String) :27 does not establish row 6; LogEntry.getTimeStamp() does not establish row 38.

## Not claimed / still owed before merge

- No build, sampler, full-repo grep, or C1 — build and C1 marked **not run** (Mac after push, never claimed passed). Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). Main-agent spot-check (1 in 5) and `py_compile` remain outstanding.
- Saved full-repo grep for the remaining OPEN row (row 39, LogEntry.hashCode) before any flip to UNREACHABLE.
- Scope strictly batch 20, LibreTorrent labels only, branch `work-2026-10-31` only, no other batch/app, no device replay, no Aegis.
