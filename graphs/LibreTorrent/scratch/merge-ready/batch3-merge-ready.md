**REVISION 2026-11-01 (Stream A Phase 1c — DECISIONS.md applied, labels only) — UNVERIFIED.** Decisions applied mechanically from `~/workspace/overnight/stream-A/DECISIONS.md` (Muse's own decisions, for user/Yang review). D6: row 26 `TagInfo.hashCode` stays OPEN — neither delegator is REACHABLE (tag TagItem.hashCode, batch 11 row 7, UNREACHABLE-proposed; drawer TagItem.hashCode, batch 10 row 39, OPEN), no printed trigger exists, and app-tree zero alone does not close a hashCode row. D1 (cosmetic only): row 26 OPEN `confirmed_by` INFERRED → —. D11: row 35 stands UNREACHABLE as tabled (converse case — no first-use print), no edit. No label flipped. Counts UNCHANGED, mechanically re-verified from the label column: 0 REACHABLE / 39 UNREACHABLE proposed / 1 OPEN (40 rows). Build: not run. C1: not run. No push made; no other file touched.

**REVISION 2026-11-01 (grep-flip re-check, Stream A Phase 1) — UNVERIFIED.** Re-checked row 31 (the batch's only 252-file-tree OPEN-closing flip) against the complete tree: SURVIVED, no label change. Counts UNCHANGED: 0 REACHABLE / 39 UNREACHABLE proposed / 1 OPEN (row 26, untouched). Grep: `~/workspace/overnight/stream-A/greps/recheck_complete_tree_grep_20261101.txt` §G1 (281 main Java files = 252 ruleF + 28 feedparser + NanoHTTPD, plus 20 test/androidTest, plus 87 res layout/xml files). CAVEAT (disclosed, not hidden): two fresh connector 429s stopped the final ui-subtree listings, so the feedparser files used are the missing-29 worker's branch copies (18/28 byte-identical to independently printed b1-src copies, packages verified, app imports match) and NanoHTTPD is the b394142 branch copy (sidecar SHA bdb2ab67, byte-identical to b2-src); menu (16 files), xml-v26, debug/release XML were NOT grepped (layout/xml were). No row was flipped in this pass. Build: not run. C1: not run.

**REVISION 2026-11-01 (OPEN-closing round 2) — UNVERIFIED.** Original for this round backed up in `~/workspace/libretorrent-merge-backup-pre-openclose2/batch3-merge-ready.md` (verified identical before editing). Counts UNCHANGED: 0 REACHABLE / 39 UNREACHABLE proposed / 1 OPEN. No label flipped. What was checked: fresh round-2 grep over the 252 app Java files (`~/workspace/b12341112-openclose2-src/round2_grep_20261101.txt`, sections G7–G8, H1–H3) re-confirms round 1 — the only `.hashCode()` hits on the tag/TorrentInfo types are the two TagItem wrappers delegating to `info.hashCode()` (ui/tag/TagItem.java:50, ui/main/drawer/TagItem.java:51), TorrentInfo.java:210 `tags.hashCode()` (a List call inside TorrentInfo.hashCode itself), and field hashes inside other hashCode definitions; no caller of TorrentInfo.hashCode anywhere in the tree; no HashSet/HashMap/hash-collection use of TagInfo, either TagItem, or TorrentInfo (the one HashSet hit, SelectTagViewModel.java:51, holds Long ids). The tag leg of the dependency is still closed (batch 11 row 7, tag TagItem.hashCode, UNREACHABLE proposed) but the drawer leg is still OPEN (batch 10 row 39, drawer TagItem.hashCode — another group's row, not edited here), so row 26 stays OPEN under the dependency rule; see the conditional table in the OPEN section. Rows 1–25, 27–30, 32–40 were NOT re-judged in round 2 (only the OPEN row was in scope) and are unchanged. Also fixed in this round: the stale "Weakest rows" line that still called row 31 OPEN — row 31 has been UNREACHABLE proposed since the round-1 revision. Build: not run. C1: not run.

**REVISION 2026-11-01 (OPEN-closing) — UNVERIFIED.** Original backed up in `~/workspace/libretorrent-merge-backup-pre-openclose/batch3-merge-ready.md`. Counts CHANGED: was 0 REACHABLE / 38 UNREACHABLE proposed / 2 OPEN; now 0 REACHABLE / 39 UNREACHABLE proposed / 1 OPEN. ONE label flipped: row 31 `PriorityConverter.convert(Priority)` (lib->app single overload) OPEN -> UNREACHABLE proposed, kind `no_trigger_in_app`, INFERRED — see the row. All other rows unchanged: row 26 `TagInfo.hashCode` stays OPEN (dependency rule — its only callers are tag TagItem.hashCode, UNREACHABLE proposed in batch 11, and drawer TagItem.hashCode, OPEN in batch 10; the saved grep also shows no HashSet/HashMap/hash-collection use of TagInfo, and TorrentInfo.java:210 `tags.hashCode()` is a List call, not a TagInfo call); rows 1-25, 27-30, 32-40 UNREACHABLE-proposed re-verified against the saved grep (construction grep: only 0-arg/String/Exception forms printed for the exception ctors, 7-arg FeedChannel at AddFeedViewModel:173-179 and Parcel-ctor at FeedChannel:110 only, no 1-arg FeedChannel, no 0-arg AdvancedTorrentInfo/IPFilterParser, no String-only NormalizeUrlException beyond the (String,Exception) site at NormalizeUrl:185, no boolean IPFilterParser, no (Exception) FreeSpace/IPFilter exceptions, no 1-arg FixedRingBuffer beyond Logger's 2-arg sites; method grep: no caller for getTimeStamp, getEntry, stopRecording(OutputStream), write(OutputStream), addTorrent(AddTorrentParams,boolean) or its lambda $8, getInstance(TorrentEngine,TagRepository), getMaxConnections/getMaxUploads/getSize/getTorrentId/isAutoManaged, isMoving/isSaveResume, Type.<clinit>). Build: not run. C1: not run. Saved grep: saved grep `~/workspace/b12341112-openclose-src/ruleF_grep_20261101.txt` (2,043 lines; Corpus A: 252 app Java files in `~/workspace/ruleF-src`, connector-reconstructed from branch work-2026-10-31 and verified 252/252 against the walk list; Corpus B: printed library files in `~/workspace/b1-src` + `~/workspace/b2-src`; scope: res/ XML, generated sources and library sources outside Corpus B are NOT in the grep — see caveats).

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 3 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No graph_def.py, out/, PROGRESS_V2, AGENT_NOTES, tools/, or another agent's file was edited.**
Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only. Never main or result.
Build: **not run**. C1: **not run**. Sampler: **not run**. Full-repo grep: **not run**.
These run on the user's Mac after a push (per the 22:44 instruction); nothing here claims them passed.
0 rows are verified for merge until the main agent spot-checks 1 in 5, runs py_compile, and the Mac build/C1 return.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 3 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`,
plan SHA `0104806dd666c840049b3db52823d4b384fa1c92`, confirmed by a fresh
connector fetch this session (SHA matches) and by the local plan copy
`~/workspace/agent27-plan.tsv` (same SHA). Plan order, rows 81–120 of the plan
file, batch-3 sequence 1–40 below. Plan statuses: 39 DONE_LABEL, 1
TODO_CANDIDATE_REACHABLE (row 31). Plan current_labels are NOT adopted:
every row below was re-derived from printed source in this session.

Prior work is an INPUT, not a result: Agent 50's audit (batch 3: plan
39 UNREACHABLE + 1 candidate; audit 38 UNREACHABLE + 1 REACHABLE + 1 OPEN)
and the branch audit file `graphs/LibreTorrent/scratch/batch_003.md` (fetched
fresh this session, SHA `8cfdcc1ceda8f612de0ea1d6b4ee0326b1a1b2a9`) were used
only as a lead list for which files to print and which overload contrasts
to check. Where this re-derivation disagrees with the audit, the disagreement
is stated explicitly — row 31, below.

## confirmed_by convention used here

All rows are marked INFERRED, deliberately, following the batch-2
merge-ready precedent. Reason: an UNREACHABLE proposal on printed files
alone rests on (a) a printed definition, (b) printed caller sites that use
a *different* overload or a *different* method, and (c) no caller printed
for this exact overload in the files fetched this session — but no saved
full-repo grep exists, so no UNREACHABLE row is claimed SOURCE. An OPEN row
was INFERRED for the same reason (evidence incomplete, not a printed direct
route); 2026-11-01 D1 revision: row 26 OPEN is now —, cosmetic only. No row uses DYN, FW-MEMORY, or UNVERIFIED as confirmed_by. If the
merger adopts a per-row SOURCE convention for rows whose definition +
overload contrast are both freshly printed, labels are unaffected; only
confirmed_by would change, and the merger must still run the saved
full-repo grep before flipping any OPEN row to UNREACHABLE.

## Printed source used (fresh connector fetches, branch work-2026-10-31, one at a time with pauses)

Base path for app source:
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`
Saved in `~/workspace/libretorrent-merge/b3-src/` (same relative paths):
- `core/RepositoryHelper.java`, `core/collections/FixedRingBuffer.java`
- `core/exception/DecodeException.java`, `FetchLinkException.java`,
  `FileAlreadyExistsException.java`, `FreeSpaceException.java`,
  `IPFilterException.java`, `NoFilesSelectedException.java`,
  `NormalizeUrlException.java`, `TorrentAlreadyExistsException.java`
- `core/filter/TorrentFilterCollection.java`, `core/logger/LogEntry.java`,
  `core/logger/Logger.java`
- `core/model/TorrentEngine.java` (1658 lines), `core/model/TorrentInfoProvider.java`
- `core/model/data/AdvancedTorrentInfo.java`, `PeerInfo.java`, `TrackerInfo.java`,
  `TorrentInfo.java`, `data/entity/FeedChannel.java`, `data/entity/TagInfo.java`,
  `data/metainfo/TorrentMetaInfo.java`
- `core/model/filetree/FileNode.java`, `FileTree.java`, `BencodeFileTree.java`,
  `TorrentContentFileTree.java`
- `core/model/session/IPFilterParser.java`, `IPFilterImpl.java`,
  `PriorityConverter.java`, `SessionErrors.java`, `TorrentCriticalWork.java`,
  `TorrentDownload.java`, `TorrentDownloadImpl.java` (1711 lines),
  `TorrentSessionImpl.java` (1720 lines)
- `core/urlnormalizer/NormalizeUrl.java`, `core/utils/Utils.java`
- `service/TorrentService.java`, `service/SaveLogWorker.java`
- `ui/addtorrent/AddTorrentViewModel.java`, `ui/addfeed/AddFeedViewModel.java`,
  `ui/createtorrent/CreateTorrentViewModel.java`, `ui/log/LogViewModel.java`,
  `ui/main/drawer/TagItem.java`, `ui/tag/TagItem.java`
- Branch audit/route files fetched fresh as locators only (not verdicts):
  `graphs/LibreTorrent/scratch/batch_003.md`,
  `graphs/LibreTorrent/scratch/s3_route_priority_final.txt`
- One fetch in this session returned a JSON parse error on first attempt
  (`TorrentDownload.java`); a single spaced retry succeeded (SHA
  `5d5a1b096719782766f8eff5445c14726b11ace3`). No fetch hit HTTP 429.
  No connector `search_code` result was used as evidence of absence.
  Local copies in `~/workspace/batch35_38/src/` and
  `~/workspace/b113-114-src/` were used only to locate paths; every
  citation below is from a file freshly fetched this session, except
  where a row explicitly says a caller file was not freshly printed.

Line numbers below are from the freshly fetched files in `b3-src/`
(verified by grep after fetch, not hand-counted).

## Headline correction to the audit — row 31 is UNREACHABLE, not REACHABLE (flipped from OPEN in the 2026-11-01 revision)

The audit's hand route for row 31 (`s3_route_priority_final.txt`, step 12)
cites `PriorityConverter.java:94-101` and `TorrentSessionImpl.java:1541-1575`
(`:1574 convert(priority).swig()`). That is the **app→lib** single overload,
`convert(Priority)` at PriorityConverter.java:94
(`public static org.libtorrent4j.Priority convert(@NonNull Priority priority)`),
where `Priority` is the app class. Row 31's plan descriptor is the opposite
overload, **lib→app** single convert at PriorityConverter.java:103
(`public static Priority convert(@NonNull org.libtorrent4j.Priority priority)`),
descriptor `(Lorg/libtorrent4j/Priority;)Lorg/proninyaroslav/libretorrent/core/model/data/Priority;`.
All six convert call sites printed fresh in TorrentDownloadImpl.java and
TorrentSessionImpl.java are the other three overloads, not row 31:
- array app→lib (:54) — TorrentDownloadImpl.java:731
- single app→lib (:94) — TorrentDownloadImpl.java:1139, TorrentSessionImpl.java:1574
- array lib→app (:74) — TorrentDownloadImpl.java:1646, TorrentSessionImpl.java:437, :451
No printed caller for single lib→app (:103) appears in any file fetched
this session. The route trunk (AddTorrentActivity → AddTorrentViewModel
Thread → TorrentEngine.addTorrentSync → TorrentSessionImpl.addTorrent →
download, with STATE `isRunning()` at TorrentEngine.java:409-412) is
consistent with reaching `download()`, but its final step misidentifies
the overload, so it does **not** establish row 31. Row 31 therefore stays
OPEN (named grep target below), and must NOT be flipped to UNREACHABLE
without a saved full-repo grep, per the task rule. If the merger's grep
finds a single-arg lib→app caller, flip row 31 to REACHABLE; if a saved
full-repo grep finds none, only then flip it to UNREACHABLE
`no_trigger_in_app`.

## Table — 40 rows, plan order

| # | Method (JVM descriptor) | Label proposed | Kind / reason | confirmed_by | Printed citations |
|---|---|---|---|---|---|
| 1 | RepositoryHelper.<init> ()V | UNREACHABLE proposed | no_trigger_in_app — class has no explicit ctor (implicit default only); only static accessors exist, no construction printed | INFERRED | RepositoryHelper.java:36, :43, :52, :61, :69 |
| 2 | FixedRingBuffer.<init>(int) (I)V | UNREACHABLE proposed | no_trigger_in_app — 1-arg ctor delegates to 2-arg; Logger constructs 2-arg only | INFERRED | FixedRingBuffer.java:45-49 (`this(0, capacity)`); Logger.java:68, :89 (2-arg `new FixedRingBuffer<>(calcInitBufCapacity(...), maxStoredLogs)`) |
| 3 | DecodeException.<init>() ()V | UNREACHABLE proposed | no_trigger_in_app — only (Exception) constructions printed | INFERRED | DecodeException.java:28 (def); TorrentMetaInfo.java:69, :79, :92 (`new DecodeException(e)`); TorrentEngine.java:387 (`new DecodeException(e)`) |
| 4 | DecodeException.<init>(String) (Ljava/lang/String;)V | UNREACHABLE proposed | no_trigger_in_app — only (Exception) constructions printed, never String-only | INFERRED | DecodeException.java:30 (def); same constructions as row 3 |
| 5 | FetchLinkException.<init>() ()V | UNREACHABLE proposed | no_trigger_in_app — constructions are String or Exception, never 0-arg | INFERRED | FetchLinkException.java:28 (def); Utils.java:467, :493, :509, :522 (String), :474 (Exception) |
| 6 | FileAlreadyExistsException.<init>() ()V | UNREACHABLE proposed | no_trigger_in_app — NO construction printed in any file fetched this session; weakest UNREACHABLE in this batch, grep owed | INFERRED | FileAlreadyExistsException.java:24 (def); no `new FileAlreadyExistsException` in fresh prints |
| 7 | FileAlreadyExistsException.<init>(String) (Ljava/lang/String;)V | UNREACHABLE proposed | no_trigger_in_app — same as row 6, no construction printed | INFERRED | FileAlreadyExistsException.java:26 (def); no construction in fresh prints |
| 8 | FreeSpaceException.<init>(Exception) (Ljava/lang/Exception;)V | UNREACHABLE proposed | no_trigger_in_app — constructions are 0-arg or String, never (Exception) | INFERRED | FreeSpaceException.java:35 (def); TorrentEngine.java:1201 (0-arg); TorrentDownloadImpl.java:417 (String); AddTorrentViewModel.java:496 (0-arg) |
| 9 | IPFilterException.<init>() ()V | UNREACHABLE proposed | no_trigger_in_app — constructions are String-only | INFERRED | IPFilterException.java:24 (def); IPFilterImpl.java:44, :54, :58 (String) |
| 10 | IPFilterException.<init>(Exception) (Ljava/lang/Exception;)V | UNREACHABLE proposed | no_trigger_in_app — constructions are String-only, never (Exception) | INFERRED | IPFilterException.java:31 (def); IPFilterImpl.java:44, :54, :58 |
| 11 | NoFilesSelectedException.<init>(String) (Ljava/lang/String;)V | UNREACHABLE proposed | no_trigger_in_app — only construction printed is 0-arg | INFERRED | NoFilesSelectedException.java:26 (def); AddTorrentViewModel.java:493 (0-arg) |
| 12 | NormalizeUrlException.<init>(String) (Ljava/lang/String;)V | UNREACHABLE proposed | no_trigger_in_app — only construction printed is (String, Exception) | INFERRED | NormalizeUrlException.java:27 (String def), :21 ((String, Exception) def); NormalizeUrl.java:185 (`new NormalizeUrlException("Cannot normalize URL", e)`) |
| 13 | TorrentAlreadyExistsException.<init>(String) (Ljava/lang/String;)V | UNREACHABLE proposed | no_trigger_in_app — only construction printed is 0-arg | INFERRED | TorrentAlreadyExistsException.java:26 (def); TorrentSessionImpl.java:282 (0-arg) |
| 14 | TorrentFilterCollection.<init> ()V | UNREACHABLE proposed | no_trigger_in_app — no explicit ctor; static factories only, no construction printed in fresh files | INFERRED | TorrentFilterCollection.java:26, :27-101 (static `all/status*/date*/tag/noTags` only) |
| 15 | LogEntry.getTimeStamp ()J | UNREACHABLE proposed | no_trigger_in_app — timestamp formatting reads `getTimeStampAsString`, not this accessor; no caller printed | INFERRED | LogEntry.java:66 (def), :71 (`getTimeStampAsString`), :105 (`toStringWithTimeStamp` uses `getTimeStampAsString`) |
| 16 | Logger.getEntry (I)Lorg/proninyaroslav/libretorrent/core/logger/LogEntry; | UNREACHABLE proposed | no_trigger_in_app — printed logger callers use getNumEntries/pause/resume/startRecording/stopRecording/write, never getEntry(int) | INFERRED | Logger.java:301 (def); LogViewModel.java:164 (`getNumEntries`), :142, :153, :176, :183; SaveLogWorker.java:93, :95 |
| 17 | Logger.stopRecording(OutputStream) (Ljava/io/OutputStream;)I | UNREACHABLE proposed | no_trigger_in_app — callers use 0-arg or 2-arg form, never 1-arg | INFERRED | Logger.java:367 (1-arg def, delegates :372), :362 (0-arg), :372 (2-arg); LogViewModel.java:183 (0-arg); SaveLogWorker.java:93 (2-arg `stopRecording(fout, true)`) |
| 18 | Logger.write(OutputStream) (Ljava/io/OutputStream;)I | UNREACHABLE proposed | no_trigger_in_app — caller uses 2-arg form, never 1-arg | INFERRED | Logger.java:405 (1-arg def, delegates :410), :410 (2-arg); SaveLogWorker.java:95 (`write(fout, true)`) |
| 19 | TorrentEngine.addTorrent(AddTorrentParams,boolean) (Lorg/proninyaroslav/libretorrent/core/model/AddTorrentParams;Z)V | UNREACHABLE proposed | no_trigger_in_app — internal callers use URI overloads; external printed caller uses URI overload; no caller of this params overload in fresh files | INFERRED | TorrentEngine.java:329-340 (def, Completable Runnable); :1149 (`addTorrentCompletable(uri)`), :1173 (`addTorrent(Uri.fromFile(file))`); CreateTorrentViewModel.java:376 (`engine.addTorrent(torrentFilePath, path)` — URI overload) |
| 20 | TorrentEngine.lambda$addTorrent$8 (Lorg/proninyaroslav/libretorrent/core/model/AddTorrentParams;Z)V | UNREACHABLE proposed | no_trigger_in_app — synthetic body registered only inside the uncalled row-19 overload; inherits row 19's status | INFERRED | TorrentEngine.java:329-340; lambda $8 numbering NOT bytecode-verified — if a row-19 caller is found, this row flips with it |
| 21 | TorrentInfoProvider.getInstance(TorrentEngine,TagRepository) (Lorg/proninyaroslav/libretorrent/core/model/TorrentEngine;Lorg/proninyaroslav/libretorrent/core/storage/TagRepository;)Lorg/proninyaroslav/libretorrent/core/model/TorrentInfoProvider; | UNREACHABLE proposed | no_trigger_in_app — printed service caller uses the Context overload, never this overload | INFERRED | TorrentInfoProvider.java:63-75 (Engine overload def), :76- (Context overload def); TorrentService.java:110 (`getInstance(getApplicationContext())`) |
| 22 | AdvancedTorrentInfo.<init>() ()V | UNREACHABLE proposed | no_trigger_in_app — printed construction is parameterized or Parcel, never 0-arg | INFERRED | AdvancedTorrentInfo.java:49 (0-arg def), :54 (parameterized def), :76 (Parcel def), :123-125 (CREATOR → Parcel ctor); TorrentEngine.java:846-858 (parameterized construction) |
| 23 | PeerInfo$ConnectionType.<init> ()V | UNREACHABLE proposed | no_trigger_in_app — no explicit ctor (implicit only); integer constants only, no construction printed | INFERRED | PeerInfo.java:49-54 (constants BITTORRENT/WEB/UTP only) |
| 24 | TrackerInfo$Status.<init> ()V | UNREACHABLE proposed | no_trigger_in_app — no explicit ctor (implicit only); integer constants only, no construction printed | INFERRED | TrackerInfo.java:49-55 (constants UNKNOWN/WORKING/UPDATING/NOT_CONTACTED/NOT_WORKING only) |
| 25 | FeedChannel.<init>(String) (Ljava/lang/String;)V | UNREACHABLE proposed | no_trigger_in_app — printed construction is 7-arg or Parcel, never 1-arg | INFERRED | FeedChannel.java:67 (1-arg def, @Ignore), :52 (7-arg def), :73 (Parcel def); AddFeedViewModel.java:173-179 (7-arg construction) |
| 26 | TagInfo.hashCode ()I | UNREACHABLE | Trigger unestablished — see OPEN section below; do NOT flip to UNREACHABLE without a saved full-repo grep | INFERRED | TagInfo.java:94-99 (def, fresh); drawer/TagItem.java:50-51, tag/TagItem.java:49-50 (both delegate to `info.hashCode()`); TorrentInfo.java:191-213, :210 (`tags.hashCode()` in TorrentInfo.hashCode) REVISION 2026-11-01 (D6/D1): D6 decides this row stays OPEN (neither delegator REACHABLE; no printed trigger; app-tree zero alone does not close it); D1 normalises OPEN confirmed_by to —, cosmetic only, label unchanged. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: COORD verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 27 | FileNode$Type.<init> ()V | UNREACHABLE proposed | no_trigger_in_app — Type class has no explicit ctor; static DIR/FILE constants only, no construction printed | INFERRED | FileNode.java:30-36 (Type: `DIR = 0`, `FILE = 1` only) |
| 28 | FileTree.<init>(int,String,long,int) (ILjava/lang/String;JI)V | UNREACHABLE proposed | no_trigger_in_app — subclass super calls use 3-arg string-first, 4-arg string-first+parent, or 5-arg, never int-first 4-arg | INFERRED | FileTree.java:61 (int-first 4-arg def, delegates :66), :51, :56, :66; BencodeFileTree.java:37, :42, :47; TorrentContentFileTree.java:35, :42, :48 (super calls listed in text) |
| 29 | IPFilterParser.<init>(boolean) (Z)V | UNREACHABLE proposed | no_trigger_in_app — only construction printed is 0-arg | INFERRED | IPFilterParser.java:54 (boolean def), :49 (0-arg def); TorrentSessionImpl.java:731 (`new IPFilterParser().parseFile(...)`) |
| 30 | PriorityConverter.<init> ()V | UNREACHABLE proposed | no_trigger_in_app — no explicit ctor (implicit only); package-private class used only through static methods, no construction printed | INFERRED | PriorityConverter.java:28 (class, no ctor), :54, :74, :94, :103 (static converts only) |
| 31 | PriorityConverter.convert(Priority) (Lorg/libtorrent4j/Priority;)Lorg/proninyaroslav/libretorrent/core/model/data/Priority; | UNREACHABLE proposed | no_trigger_in_app — saved full-repo grep (2026-11-01, app tree) finds exactly six `PriorityConverter.convert` call sites, all other overloads, and zero calls with a single `org.libtorrent4j.Priority` argument: TorrentDownloadImpl:731 (app→lib array), :1139 (app→lib single, argument is app Priority `newPriority`), :1646 (lib→app array, getFilePriorities return), TorrentSessionImpl:437/:451 (lib→app array, Arrays.asList result), :1574 (app→lib single, argument is app Priority, result `.swig()` is a lib Priority). The method is a package-private static utility in the app tree, so app code is its only possible caller set; no static-import alias exists (grep for `PriorityConverter` finds only these sites + the definition). REVISION 2026-11-01: OPEN -> UNREACHABLE proposed on this grep; the audit REACHABLE claim stays refuted on overload grounds (see correction section). | INFERRED | PriorityConverter.java:103-110 (row-31 def, lib→app single), :94-101 (other single overload, app→lib); saved grep `~/workspace/b12341112-openclose-src/ruleF_grep_20261101.txt` sections A1/A3/A5, argument types verified in ruleF-src TorrentDownloadImpl.java:1125-1145 and TorrentSessionImpl.java:1565-1580 RE-CHECK 2026-11-01 (SURVIVED): complete-tree grep ~/workspace/overnight/stream-A/greps/recheck_complete_tree_grep_20261101.txt §G1 over 281 main Java files (252 ruleF + 28 feedparser + NanoHTTPD) + 20 test/androidTest + 87 res layout/xml files still shows exactly the six convert sites, all other overloads, zero single-lib-Priority-arg calls; feedparser imports zero app classes (§G14). Label stands. |
| 32 | SessionErrors.<init> ()V | UNREACHABLE proposed | no_trigger_in_app — no explicit ctor; package-private utility used only through static methods, no construction printed | INFERRED | SessionErrors.java:26 (class, no ctor); TorrentSessionImpl.java:1117-1134, TorrentDownloadImpl.java:352-371 (static `getErrorMsg`/`isNonCritical` uses only) |
| 33 | TorrentCriticalWork.isMoving ()Z | UNREACHABLE proposed | no_trigger_in_app — printed uses are setters and state observation, never this getter | INFERRED | TorrentCriticalWork.java:63 (def); TorrentDownloadImpl.java:286, :504, :512, :526, :550, :1217 (`setMoving`/`setSaveResume`/`observeStateChanging` only) |
| 34 | TorrentCriticalWork.isSaveResume ()Z | UNREACHABLE proposed | no_trigger_in_app — same as row 33, getter never printed | INFERRED | TorrentCriticalWork.java:74 (def); same TorrentDownloadImpl uses as row 33 |
| 35 | TorrentCriticalWork$Type.<clinit> ()V | UNREACHABLE proposed | no_trigger_in_app — enum constants unreferenced in fresh files; <clinit> runs only on first use | INFERRED | TorrentCriticalWork.java:32-36 (enum MOVING/SAVE_RESUME); no `Type.MOVING`/`Type.SAVE_RESUME` in fresh TorrentDownloadImpl/TorrentSessionImpl/TorrentEngine (only libtorrent `AlertType.SAVE_RESUME_DATA`, a different enum) |
| 36 | TorrentDownloadImpl.getMaxConnections ()I | UNREACHABLE proposed | no_trigger_in_app — no printed caller via the TorrentDownload interface in fresh files; internal code uses the setter, not the getter | INFERRED | TorrentDownloadImpl.java:1436-1448 (def); TorrentDownload.java:166 (interface); no interface caller printed in fresh TorrentEngine/TorrentSessionImpl/TorrentDownloadImpl |
| 37 | TorrentDownloadImpl.getMaxUploads ()I | UNREACHABLE proposed | no_trigger_in_app — same as row 36 | INFERRED | TorrentDownloadImpl.java:1453-1465 (def); TorrentDownload.java:170 (interface); no interface caller printed |
| 38 | TorrentDownloadImpl.getSize ()J | UNREACHABLE proposed | no_trigger_in_app — no printed caller on TorrentDownload in fresh files | INFERRED | TorrentDownloadImpl.java:745-752 (def); TorrentDownload.java:70 (interface); no interface caller printed |
| 39 | TorrentDownloadImpl.getTorrentId ()Ljava/lang/String; | UNREACHABLE proposed | no_trigger_in_app — no printed caller on TorrentDownload in fresh files; do NOT conflate with same-named methods on other classes (e.g. DetailTorrentFragment), which were not printed here | INFERRED | TorrentDownloadImpl.java:531-538 (def); TorrentDownload.java:45 (interface); no interface caller printed |
| 40 | TorrentDownloadImpl.isAutoManaged ()Z | UNREACHABLE proposed | no_trigger_in_app — no printed caller in fresh files | INFERRED | TorrentDownloadImpl.java:690-697 (def); TorrentDownload.java:59 (interface); no caller printed |

## Counts — mechanically verified

- 40 rows, sequence 1–40 intact, plan order, no duplicates, no missing row.
- **39 UNREACHABLE proposed / 0 REACHABLE proposed / 1 OPEN** (row 26 only; row 31 flipped to UNREACHABLE proposed in the 2026-11-01 revision above).
- confirmed_by: 39 INFERRED / 1 — (row 26 OPEN, D1 cosmetic only) / 0 SOURCE (see convention section — deliberate, not an oversight).
- This differs from the audit (38 / 1 / 1) only by row 31: REACHABLE → UNREACHABLE,
  on the overload evidence above (OPEN-closing 2026-11-01). Row 26 stays OPEN as in the audit.

## OPEN rows — named evidence still owed (do not merge as UNREACHABLE on this file alone)

1. **Row 26 TagInfo.hashCode** — possible trigger paths, none closed:
   (a) drawer TagItem.hashCode (:50-51) → TagInfo.hashCode, and tag
   TagItem.hashCode (:49-50) → TagInfo.hashCode, but no printed caller of
   either wrapper hashCode in this session; DiffUtil in the drawer adapter
   uses equals/isSame (batch-113 lead, not freshly printed here), not hash.
   REVISION 2026-11-01: saved grep confirms both wrappers are still the only callers (drawer wrapper OPEN in batch 10, tag wrapper UNREACHABLE proposed in batch 11), and finds no HashSet/HashMap/hash-collection use of TagInfo — so row 26 stays OPEN under the dependency rule, not UNREACHABLE.
   REVISION 2026-11-01 (OPEN-closing round 2): fresh grep (`~/workspace/b12341112-openclose2-src/round2_grep_20261101.txt`, G7–G8 + H1–H3) re-confirms every leg — no caller of TorrentInfo.hashCode anywhere in the 252-file tree; no hash collection holds TagInfo, either TagItem, or TorrentInfo; the tag leg is still closed (batch 11 row 7 UNREACHABLE proposed) and the drawer leg is still OPEN (batch 10 row 39, another group's row, read-only here). CONDITIONAL flip table for row 26 (apply mechanically once the named items resolve; do not apply partially):
   - If batch 10 row 39 (drawer TagItem.hashCode) flips to UNREACHABLE **and** the project hashCode rule says implicit dispatch does not count without a printed trigger **and** TorrentInfo.hashCode stays untriggered → row 26 → UNREACHABLE `no_trigger_in_app`, INFERRED.
   - If batch 10 row 39 flips to REACHABLE, or a printed trigger appears for TorrentInfo.hashCode, or a printed hash-collection/log/concatenation caller of a TagInfo/TagItem instance appears → row 26 → REACHABLE (SOURCE if the trigger site itself is printed, else INFERRED via the wrapper).
   - Otherwise (any leg still OPEN, or the hashCode rule still undecided) → row 26 stays OPEN. The round-2 grep alone does NOT flip it: a hashCode can be invoked implicitly by library/framework code with no app-Java call site, which is exactly the undecided project-wide question.
   (b) TorrentInfo.hashCode (:191-213) calls `tags.hashCode()` at :210,
   and List.hashCode() calls each element's hashCode — but no printed
   caller of TorrentInfo.hashCode in this session.
   Grep targets (saved full-repo grep, before any flip): callers of
   `drawer.TagItem.hashCode`, `tag.TagItem.hashCode`, `TorrentInfo.hashCode`,
   and any HashSet/HashMap/Hash table use of TagInfo or either TagItem.
   Until that grep is saved, row 26 is OPEN, not `no_trigger_in_app`.
2. **Row 31 PriorityConverter.convert (lib→app, single)** — CLOSED 2026-11-01: the saved full-repo grep found zero calls with a single lib Priority argument (all six sites are other overloads, argument types verified). Row 31 is now UNREACHABLE proposed, not OPEN; see the revised table row.

## Strict-entry caveats

- No REACHABLE rows are proposed, so no strict-entry revert applies to
  this batch's labels.
- If row 31 later flips to REACHABLE, its route trunk is NOT freshly
  printed here: the AddTorrentActivity exported SEND/VIEW entry and the
  AddTorrentActivity → AddTorrentViewModel steps come from the audit
  route file (a lead, not fresh evidence this session), and the
  TorrentEngine → TorrentSessionImpl step is freshly printed
  (TorrentEngine.java:401-412, STATE `isRunning()` at :409-410, and
  TorrentSessionImpl addTorrent/download). Under a strict launcher-entry
  rule, a flipped row 31 would revert to OPEN until the launcher →
  AddTorrentActivity step is freshly printed.
- UNREACHABLE proposals in this batch do not depend on an entry point:
  they rest on overload contrasts and absence in printed files, and they
  remain INFERRED proposals until the saved full-repo grep and the
  main-agent spot-check.

## Weakest rows (merger spot-check priority, 1 in 5 must include these)

- Rows 6–7 (FileAlreadyExistsException, both overloads): absence only,
  no construction printed anywhere this session.
- Row 31 (PriorityConverter single lib→app): audit contradiction, resolved UNREACHABLE proposed in the 2026-11-01 revision (corrected from a stale OPEN note in OPEN-closing round 2).
- Row 26 (TagInfo.hashCode): two delegation paths, no trigger, OPEN.
- Rows 36–40 (TorrentDownloadImpl interface accessors): interface
  methods could be called from UI files not printed this session;
  the saved full-repo grep is the deciding evidence, not these prints.
- Row 20 (lambda$addTorrent$8): $ numbering not bytecode-verified;
  tied to row 19.
- Row 35 (TorrentCriticalWork$Type.<clinit>): enum-use absence only.

## Not claimed

- No build, sampler, grep, or C1 passed — all marked "not run" above.
  A true git clone fails in this VM (named missing check, not passed);
  work was via the GitHub connector only, one file at a time with pauses.
- Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). Nothing was edited in graph_def.py, out/,
  PROGRESS_V2, AGENT_NOTES, tools/, or another agent's files.
- Search_code 0 results were never used as evidence of absence.
