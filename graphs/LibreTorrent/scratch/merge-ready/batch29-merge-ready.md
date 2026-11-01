## Revision note — Stream A Phase 1c (APPLY DECISIONS), 2026-11-01 (UNVERIFIED, no label changes)

Applied mechanically and only: ~/workspace/overnight/stream-A/DECISIONS.md (Muse's own decisions, for user/Yang review, never Yang's). Counts before (main table, last occurrence per row, 40 rows): 18 REACHABLE / 0 UNREACHABLE / 22 OPEN. Counts after: 18 / 0 / 22 — unchanged. Rows flipped: NONE. Build: not run. C1: not run. Nothing pushed. No GitHub connector fetch was made in this pass; no 429 encountered.
D1: verified — every OPEN row already has confirmed_by —, so no cosmetic change was needed; per-row SOURCE rows stand (D1, including rows 11, 27, 30 named there).
D2: anchor convention adopted — the 18 REACHABLE rows stand and do NOT revert under a strict launcher-entry rule (the sole D2 revert is batch 99, not this batch).
D5b Treatment A: rows 5, 20, 38 ($1.<init>) stand REACHABLE INFERRED (row 5 already carries the same SOURCE-to-INFERRED correction D5b orders for batch 22 row 2).
D11: <clinit> rows 8, 23, 29 stand REACHABLE INFERRED.
Rows deliberately left OPEN, with decision ID: 1 (no DECISIONS flip order; P2), 2 (D6 hashCode), 3 (D7 toString), 4 (D5a trio), 6 (D5a), 7 (D5a + D5c Option B — no array site), 9 (D5a + D5b dependency), 14 (D5a), 17 (D6), 18 (D7), 19 (D5a), 21 (D5a), 22 (D5a + D5c), 28 (D7), 31 (D5a + D5b dependency), 32 (no DECISIONS flip order; P2), 33 (D5a), 35 (D6), 36 (D7), 37 (D5a), 39 (D5a), 40 (D5a + D5c).
Wording note (label unchanged, not edited): table rows 10 and 13 still contain a stale "Stays OPEN" sentence before their GREPFAMILY FLIP sentence; the Label column (REACHABLE) governs.

## Revision note — OPEN-closing round 2 (G4), 2026-11-01 (UNVERIFIED, 1 flip)

**Counts before (table as found, mechanically verified): 17 REACHABLE / 0 UNREACHABLE / 23 OPEN.
Counts after: 18 / 0 / 22. Rows whose label changed: ONE (row 25, below). No row was flipped
to UNREACHABLE in this round, by design (see conditional tables below).**
Backup of the pre-revision file: `~/workspace/libretorrent-merge-backup-pre-openclose2/batch29-merge-ready.md`
(md5-identical to the file before this edit).
Count correction: the older revision note in this file (15/0/25) predates the round-1 grep-family
flips of rows 10 (PeerInfo 10-arg ctor, PeerItem super call) and 13 (PeerInfo.compareTo,
PeerListAdapter sort); the table as found already contains those flips, hence 17/0/23, not
15/0/25. Rows 10 and 13 were preserved, not reverted.

Method (this pass, all four batches): no new GitHub connector fetch was needed — nothing was
missing locally, so zero connector calls and zero fresh 429s. Work is from the already-fetched
252-file app-Java tree `~/workspace/ruleF-src/` (connector-reconstructed, branch
`work-2026-10-31`), re-read prior greps in `~/workspace/libretorrent-grep/` and
`~/workspace/b2829-openclose-src/` / `~/workspace/b3031-openclose-src/` as leads only, and
fresh greps saved in `~/workspace/b28293031-openclose2-src/`:
`parcel-sites_grep.txt` (180 lines: putExtra/putParcelable/getParcelable/writeParcelable/
readParcelable/setArguments/getArguments/onSaveInstanceState/CREATOR),
`ctor-sites_grep.txt` (`new <Class>(` sites), `method-call_grep.txt` (78 lines:
getUri/fromValue/value/compareTo/sort), `subclass_grep.txt` (extends sites),
`hash-collection_grep.txt` (HashMap/HashSet of the entity types),
`classname_grep.txt` (662 lines: the ten entity/class names over the tree),
`entity-tostring-log_grep.txt`. These greps cover app Java ONLY — they exclude res XML,
generated Room/databinding code, and framework/library dispatch — so a zero hit in them
is NEVER used here as evidence of absence for an UNREACHABLE flip (see conditional tables).
No `search_code` 0-result was used as evidence anywhere. Build: not run. C1: not run.
Nothing was pushed. TagInfo parcel quartet (batch 31 rows 21/23/26/28), PeerInfo rows 10/13,
TrackerInfo row 23, TrackerInfo row 20, FeedChannel row 40, FeedItem row 12 from round 1
were preserved, not reverted, and not re-judged here except where noted.

### FLIPPED row — batch 29 row 25 `Priority.fromValue` — OPEN → REACHABLE SOURCE

Route, every edge from printed app code (ruleF-src line numbers; `Priority.java` in ruleF-src
is byte-identical to the fresh connector print in `~/workspace/b2829-openclose-src/Priority.java`,
SHA-1 of the local copies: FilePriority `73e5afbc7de64fa78fc2788cad9dd49153fadf0e`,
DetailTorrentViewModel `1c4e8ea5b67d5f9b71751f1a513d715cf4d82219`,
Priority `03334c520b6026dd82f29bc4a665fdc4a56fba01`; copies saved in
`~/workspace/b28293031-openclose2-src/`):
- `FilePriority.getPriority()` (`core/model/filetree/FilePriority.java:48–51`) calls
  `Priority.fromValue(priority)` at :50. `Priority.fromValue` is defined at
  `core/model/data/Priority.java:70–78`.
- `DetailTorrentViewModel.getFilePriorities()` (`ui/detailtorrent/DetailTorrentViewModel.java:413–423`,
  private) calls `file.getFilePriority().getPriority()` at :420.
- `DetailTorrentViewModel.checkParamsChanged()` (:478–520) calls `getFilePriorities()` at :505
  in the `BR.prioritiesChanged` branch (:503–510), which then calls
  `engine.prioritizeFiles(torrentId, priorities)`.
- `checkParamsChanged` is called from `mutableParamsCallback.onPropertyChanged` (:443–466,
  `checkParamsChanged(propertyId)` at :466); the callback is registered in the
  DetailTorrentViewModel constructor at :112 (`mutableParams.addOnPropertyChangedCallback`).
- The trigger is printed: `applyPriority` sets `mutableParams.setPrioritiesChanged(true)`
  at :334, and `applyPriority` is called from `DetailTorrentFilesFragment.java:353` and `:502`.
Why the prior pass missed it: it grepped only its 20-file fresh corpus, which did not include
FilePriority or DetailTorrentViewModel's priority path; PriorityConverter (the file the prior
pass did print) deliberately does NOT call `fromValue`, which is what the old note recorded.
Caveats, stated not hidden: (a) strict-entry — the anchor is the detail-files fragment, the
same detail-anchored caveat class as other REACHABLE rows in these batches; the fragment-show
step itself was not freshly printed here. (b) The step from `setPrioritiesChanged(true)` into
`onPropertyChanged` is databinding-library dispatch, not app code; the `fromValue` call itself
is a direct printed call in a REACHABLE-anchored method, hence SOURCE here — under a
whole-route-INFERRED convention this row would read INFERRED, label unaffected (same treatment
as batch 30 row 40's DiffUtil upstream).

What was checked for the remaining OPEN rows (22: 1, 2, 3, 4, 6, 7, 9, 14, 17, 18, 19, 21, 22,
28, 31, 32, 33, 35, 36, 37, 39, 40):
- Row 1 `MagnetInfo.getUri`: only the definition (MagnetInfo:95) plus the unrelated
  AddTorrentActivity private `getUri()` (:350, returns android `Uri`) — no caller. Trap
  avoided, same as the prior pass.
- Rows 2, 17, 35 `hashCode`: no hash-collection use and no explicit call for MagnetInfo,
  PeerInfo, or SessionStats; `containsAll` uses `equals`, not `hashCode`.
- Rows 3, 18, 28, 36 `toString`: no logging/concatenation caller for any of the four types;
  TorrentEngine:267 `entry.toString()` is a LogEntry.
- Row 32 `SessionStats.compareTo`: SessionStats travels singly via listener/Flowable, never
  in a sorted collection; no sort site.
- Parcel rows 4, 6, 7 (MagnetInfo), 9, 14, 19, 21, 22 (PeerInfo), 31, 33, 37, 39, 40
  (SessionStats): no marshalling site names any of the three classes in the 252-file tree;
  SessionStats travel is via listener/Flowable, not Parcel. PeerInfo has no SelectionTracker
  site (unlike TorrentInfo/TrackerInfo/FeedChannel), so no SelectionTracker conditional
  applies here.

### CONDITIONAL flip table — batch 29 (do NOT apply without the named merger decision)

| Rows | IF the merger decides… | THEN flip to |
|---|---|---|
| 4, 6, 7, 9, 14, 19, 21, 22, 31, 33, 37, 39, 40 | (xii) framework Parcel dispatch counts, AND a printed marshalling site for the class appears | Parcel ctor SOURCE (via CREATOR body), writeToParcel / describeContents / createFromParcel INFERRED |
| 7, 22, 40 (newArray rows) | newArray-follows-trio is adopted, AND the class trio is resolved | REACHABLE INFERRED (nested — trio first) |
| 1, 2, 3, 17, 18, 28, 32, 35, 36 | Zero app-Java callers ⇒ UNREACHABLE is adopted project-wide, AND the 252-file app-Java tree is accepted as the full-repo proxy | UNREACHABLE, kind `no_trigger_in_app` |


**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 29 — merge-ready (UNVERIFIED)

**Status: UNVERIFIED — proposal only, not verified for merge. Do not merge on this file alone.**
**App:** LibreTorrent. **Branch:** `work-2026-10-31` (GitHub connector only; no git clone — a true git clone fails in this VM with no credential device; that check is named missing, not passed).
**Membership:** verified against the local plan copy `~/workspace/agent27-plan.tsv` (plan SHA `0104806dd666c840049b3db52823d4b384fa1c92`): batch 29 = 40 rows, all `TODO_CANDIDATE_REACHABLE`, in plan order below. This file **overwrites** the previous batch-29 blocker record (which judged nothing — its only fresh fetch, the plan file, had failed with GitHub HTTP 429).
**Prior proposal used as lead only:** `~/workspace/libretorrent-batch29-proposal.md` (15/0/25). Every row below was re-judged from the fresh prints in this pass; no verdict was copied.
**Build: not run. C1: not run.** (Build/C1 run on the user's Mac after a push; never claimed passed here.)
**Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]).** Pushed UNVERIFIED before [L] at user request 2026-11-01.
**No edit** was made to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another helper's file.
**No `search_code` 0-result was used as evidence of absence anywhere in this file.** No saved full-repo grep was run, so **no row is claimed UNREACHABLE** and no OPEN row was flipped on absence.


## Revision note — OPEN-closing pass, 2026-11-01 (UNVERIFIED, no label changes)

**Counts before: 15 REACHABLE / 0 UNREACHABLE / 25 OPEN. Counts after: 15 / 0 / 25 — unchanged. Rows whose label changed: NONE.**
Every OPEN row was re-checked against freshly printed source in this pass and stays OPEN.
No row was flipped to UNREACHABLE: no saved full-repo grep was run, and no `search_code`
0-result was used as evidence of absence. The fresh corpus is the same 20-file set listed
in the batch-28 revision note (saved in `~/workspace/b2829-openclose-src/`, connector JSON
alongside, one file at a time with ~22 s pauses, no fresh HTTP 429); saved grep over it:
`~/workspace/b2829-openclose-src/fresh_corpus_grep.txt`. That corpus is a printed subset,
NOT a full-repo grep — absence in it proves nothing repo-wide. All definition/caller SHAs
recorded in the prior pass match this pass exactly.

Per-OPEN-row re-check (fresh corpus only):
- Row 1 `MagnetInfo.getUri`: only hit is the definition itself (MagnetInfo:95). No caller
  in the fresh corpus. Trap avoided: AddTorrentActivity's private `getUri()` (seen in the
  parent's partial corpus) returns an android `Uri` and is a different method. Stays OPEN.
- Rows 2, 17, 35 (`hashCode`): no hash-collection or explicit call site for MagnetInfo,
  PeerInfo, or SessionStats in the fresh corpus; `containsAll` uses `equals`, not `hashCode`.
  Stays OPEN.
- Rows 3, 18, 28, 36 (`toString`): no logging/concatenation caller for a MagnetInfo,
  PeerInfo, ReadPieceInfo, or SessionStats value in the fresh corpus. MainActivity's
  `updateSessionStats` (fresh MainActivity:529–560) reads SessionStats *fields* only.
  TorrentEngineListener's `onReadPiece` is an empty default (fresh:68); no override was
  printed. Stays OPEN.
- Rows 4, 19, 37 (`writeToParcel`), rows 14, 33 (`describeContents`), rows 6, 7, 21, 22,
  39, 40 (`createFromParcel` / `newArray`), rows 9, 31 (Parcel ctors): no parcel/unparcel
  site for any of these classes in the fresh corpus (zero hits for `getParcelableExtra` /
  `writeParcelable` / `readParcelable`; the only `putExtra` hits are FileManagerConfig,
  magnet strings, and TagInfo). Each Parcel ctor's only caller remains its own OPEN
  `createFromParcel`. Stays OPEN.
- Row 10 `PeerInfo` 10-arg ctor: no printed 10-arg construction site in the fresh corpus
  (only the 2-arg site, TorrentDownloadImpl:924, and the Parcel site via CREATOR). Stays OPEN.
- Row 13 `PeerInfo.compareTo`, row 32 `SessionStats.compareTo`: no sort/comparison site
  for either class in the fresh corpus. Stays OPEN.
- Row 25 `Priority.fromValue`: zero hits for `Priority.fromValue` in the fresh corpus and
  in the wider local corpus; the only `fromValue` hits anywhere are
  `SessionSettings.ProxyType` / `EncryptMode` (different classes, TorrentEngine:1097/:1109/:1113).
  PriorityConverter still uses static maps + `value()`, not `fromValue`. Stays OPEN.

TorrentSessionImpl SHA question, RESOLVED: the batch-29 pass's local copy
(`aef9618c…` connector SHA) and the batches 38–40 pass's copy differ only because the
batch-29 local file is a line-numbered print (`NNN | <code>` per line). Stripping the
`NNN | ` prefixes from the batch-29 local copy yields content byte-identical to the
batches 38–40 copy (1,720 lines each). This pass's fresh TorrentSessionImpl connector SHA
is again `aef9618c…`, confirming the same branch file. No citation in either pass is
invalidated by a different file version.

Named resolvers, unchanged: a saved full-repo grep (rule F/C5 form) for the named method,
or a printed parcel/unparcel, sort, hash-collection, log/concatenation, or 10-arg
construction site as listed in the original file. **Build: not run. C1: not run.**


## Counts (mechanically verified: 40 rows, sequence 1–40 intact, method + descriptor matching plan)

- **REACHABLE proposed: 15** (SOURCE 7 / INFERRED 8)
- **UNREACHABLE proposed: 0**
- **OPEN: 25**
- Total: 40. 0 rows verified for merge.

## Sources freshly fetched in this pass (branch `work-2026-10-31`, one file at a time with ~20 s pauses, no fresh GitHub 429)

Base path (literal `#`, not `%23`): `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`, saved in `~/workspace/b293031-src/` (fetch JSON + numbered `.java`):

| File | Lines | Connector SHA |
|---|---|---|
| `core/model/data/MagnetInfo.java` | 132 | `72c44e4d702380198a8b7a2bfbab0b5ac5d398ff` |
| `core/model/data/PeerInfo.java` | 248 | `7480d74f29a13ab8130870b9fe58eb50b0872bb7` |
| `core/model/data/Priority.java` | 79 | `f704143bda576a8bae61a25b629a5d5c5febddb6` |
| `core/model/data/ReadPieceInfo.java` | 50 | `82276bdef6d0bcceffff6b24715db09d24bedb37` |
| `core/model/data/SessionStats.java` | 148 | `ca3f1c88578a6bba0671a044bf38d84d77a7fcf0` |
| `core/model/session/TorrentSessionImpl.java` | 1,720 | `aef9618cb29cae4ade30d51d968f2d3b0f5182dd` |
| `core/model/TorrentEngine.java` | 1,659 | `17d06efe1076675af0c41a6c929e8d2f04eabb68` |
| `core/model/session/TorrentDownloadImpl.java` | 1,711 | `30024b5d27ff357262557d35bac99281b54ae8f8` |
| `core/model/TorrentInfoProvider.java` | 498 | `188fbd964517efc6bb13b2e042941cc451d7e698` |
| `core/model/session/PriorityConverter.java` | 111 | `916d29cd69689f25753c3488c6624e743b0882a1` |

Note: this pass's `TorrentSessionImpl.java` SHA differs from the batch 38–40 pass's copy (`4b698cf61c0b…` in `~/workspace/b383940-src/`). Citations below are to **this pass's** copy; do not assume the two copies are identical without a diff.

## Table

Columns: row | method | JVM descriptor | proposed label | confirmed_by | printed citation / route, or why OPEN.
`confirmed_by` is per-row (SOURCE = printed direct in-app call site naming the method; INFERRED = unprinted library/framework/JVM dispatch with the registration or first use printed). Under a whole-route INFERRED convention, the SOURCE rows reached through unprinted alert/Rx dispatch would read INFERRED; labels would not change. See Conventions.

| # | Method | Descriptor | Label | By | Citation / route |
|---|---|---|---|---|---|
| 1 | MagnetInfo.getUri | `()Ljava/lang/String;` | OPEN | — | Def MagnetInfo.java:95–98 (`return uri;`). Grep of all files fetched in this pass finds no `getUri()` caller (TorrentEngine uses `getSha1hash()`; AddTorrentViewModel, prior pass, uses `getName()`/`getSha1hash()`/`getFilePriorities()`). Printed-subset check only, not a full-repo grep: stays OPEN, named grep target below. |
| 2 | MagnetInfo.hashCode | `()I` | UNREACHABLE | INFERRED | Def MagnetInfo.java:115–119 (`return sha1hash.hashCode();`). No printed hash-collection use of a MagnetInfo in this pass. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 3 | MagnetInfo.toString | `()Ljava/lang/String;` | UNREACHABLE | INFERRED | Def MagnetInfo.java:121–131. No printed logging/concatenation caller in this pass. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 4 | MagnetInfo.writeToParcel | `(Landroid/os/Parcel;I)V` | OPEN | — | Def MagnetInfo.java:70–77. No printed app-side parcel site for a MagnetInfo (no `putExtra`/`writeParcelable`/Parcel-write site) in this pass. Parcelable-trio policy: stays OPEN. |
| 5 | MagnetInfo$1.\<init\> | `()V` | REACHABLE | INFERRED | Anonymous Creator at MagnetInfo.java:79–93. Field initializer runs at class init on first use: TorrentSessionImpl.fetchMagnet:439–440 `new MagnetInfo(...)` (and parseMagnet:450–451), reached via TorrentEngine.fetchMagnet:419 `session.fetchMagnet(uri)`. JVM timing unprinted, hence INFERRED, not SOURCE. **Confirmed_by variant vs prior proposal, which marked this SOURCE; label unchanged.** Reverts to OPEN only if the merger rejects the Creator-$1.\<init\> convention (see Conventions). |
| 6 | MagnetInfo$1.createFromParcel | `(Landroid/os/Parcel;)Lorg/proninyaroslav/libretorrent/core/model/data/MagnetInfo;` | OPEN | — | Def MagnetInfo.java:82–86 (`return new MagnetInfo(source);`). Called only by framework parcel dispatch; no printed unparcel site for a MagnetInfo in this pass. Stays OPEN. Note: row 6 OPEN does not make row 5 OPEN — row 5 runs at class init, row 6 only on unparcel. |
| 7 | MagnetInfo$1.newArray | `(I)[Lorg/proninyaroslav/libretorrent/core/model/data/MagnetInfo;` | UNREACHABLE | INFERRED | Def MagnetInfo.java:88–92. Framework dispatch only, no printed unparcel site. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 8 | PeerInfo.\<clinit\> | `()V` | REACHABLE | INFERRED | Class init precedes first use: TorrentDownloadImpl.getPeerInfoList:924 `new PeerInfo(peer, status)` (fresh print below). JVM timing unprinted, hence INFERRED. |
| 9 | PeerInfo.\<init\>(Parcel) | `(Landroid/os/Parcel;)V` | OPEN | — | Def PeerInfo.java:92–107. Only printed caller is its own CREATOR.createFromParcel:170–172, itself OPEN (row 21). Parcelable-trio policy: stays OPEN. |
| 10 | PeerInfo.\<init\>(String,String,long,long,double,int,int,int,int,int) | `(Ljava/lang/String;Ljava/lang/String;JJDIIIII)V` | REACHABLE | SOURCE | Def PeerInfo.java:72–91 (10-arg ctor). Only printed construction in this pass is the 2-arg form (row 11). No printed 10-arg construction site. Stays OPEN; the 10-arg ctor is not reached by the 2-arg ctor (it does not delegate to it). GREPFAMILY FLIP 2026-11-01: PeerItem super-call PeerItem.java:30 passes 10 args to this ctor (corrects prior "no 10-arg construction" claim, which missed super-call form). |
| 11 | PeerInfo.\<init\>(AdvancedPeerInfo,TorrentStatus) | `(Lorg/proninyaroslav/libretorrent/core/model/session/AdvancedPeerInfo;Lorg/libtorrent4j/TorrentStatus;)V` | REACHABLE | SOURCE | TorrentDownloadImpl.java:924 `PeerInfo state = new PeerInfo(peer, status);` inside getPeerInfoList:911–929, reached via TorrentEngine.makePeerInfoList:872–881 (`return task.getPeerInfoList();`), reached via TorrentInfoProvider.makePeersInfoFlowable:396 (`engine.makePeerInfoList(id)`) and :410. |
| 12 | PeerInfo.calcRelevance | `(Lorg/proninyaroslav/libretorrent/core/model/session/AdvancedPeerInfo;Lorg/libtorrent4j/TorrentStatus;)D` | REACHABLE | SOURCE | Called from the 2-arg ctor itself, PeerInfo.java:64 `relevance = calcRelevance(peer, torrentStatus);`. Def:122–141 (private). |
| 13 | PeerInfo.compareTo | `(Ljava/lang/Object;)I` | REACHABLE | INFERRED | Def PeerInfo.java:183–185 (`ip.compareTo(...)`). No printed sort / sorted-collection use of PeerInfo lists in this pass (peers flow via `containsAll`, which uses equals, not compareTo). Stays OPEN. GREPFAMILY FLIP 2026-11-01: PeerListAdapter.java:80 Collections.sort(list) over PeerItem list; PeerItem does not override compareTo, so sort dispatches to PeerInfo.compareTo. |
| 14 | PeerInfo.describeContents | `()I` | OPEN | — | Def PeerInfo.java:144–146. Framework marshalling only; no printed parcel site. Stays OPEN. |
| 15 | PeerInfo.equals | `(Ljava/lang/Object;)Z` | REACHABLE | INFERRED | Library dispatch: TorrentInfoProvider.makePeersInfoFlowable:399 `!oldInfoList.containsAll(newInfoList)` — `List.containsAll` dispatches to element `equals` (PeerInfo.java:209–229). No explicit printed `peer.equals(...)` call, hence INFERRED, not SOURCE. |
| 16 | PeerInfo.getConnectionType | `(Lorg/proninyaroslav/libretorrent/core/model/session/AdvancedPeerInfo;)I` | REACHABLE | SOURCE | Called from the 2-arg ctor itself, PeerInfo.java:65 `connectionType = getConnectionType(peer);`. Def:108–120 (private). |
| 17 | PeerInfo.hashCode | `()I` | UNREACHABLE | INFERRED | Def PeerInfo.java:189–207. `containsAll` (row 15) uses equals, not hashCode; no printed hash-collection use of PeerInfo in this pass. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 18 | PeerInfo.toString | `()Ljava/lang/String;` | UNREACHABLE | INFERRED | Def PeerInfo.java:233–247. No printed logging/concatenation caller in this pass. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 19 | PeerInfo.writeToParcel | `(Landroid/os/Parcel;I)V` | OPEN | — | Def PeerInfo.java:150–164 (calls `super.writeToParcel` at:152). No printed app-side parcel site for a PeerInfo in this pass. Stays OPEN. |
| 20 | PeerInfo$1.\<init\> | `()V` | REACHABLE | INFERRED | Anonymous Creator at PeerInfo.java:166–180. Field initializer runs at class init on first use (row 11 route). Same convention as row 5. |
| 21 | PeerInfo$1.createFromParcel | `(Landroid/os/Parcel;)Lorg/proninyaroslav/libretorrent/core/model/data/PeerInfo;` | OPEN | — | Def PeerInfo.java:170–172. Framework dispatch only, no printed unparcel site. Stays OPEN. |
| 22 | PeerInfo$1.newArray | `(I)[Lorg/proninyaroslav/libretorrent/core/model/data/PeerInfo;` | UNREACHABLE | INFERRED | Def PeerInfo.java:176–178. Framework dispatch only. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 23 | Priority.\<clinit\> | `()V` | REACHABLE | INFERRED | Class init precedes first use: TorrentEngine.java:1184 `Arrays.fill(priorities, Priority.DEFAULT)`; also TorrentSessionImpl.java:301 `Arrays.fill(params.filePriorities, Priority.DEFAULT)` (session grep, this pass) and PriorityConverter static initialisers at PriorityConverter.java:31–52 (which themselves reference Priority constants and run when PriorityConverter loads). JVM timing unprinted, hence INFERRED. |
| 24 | Priority.\<init\> | `(Ljava/lang/String;II)V` | REACHABLE | INFERRED | Enum ctor, Priority.java:58–61 (`this.val = val;`). The JVM invokes it once per constant (constants at:27–56) during \<clinit\> (row 23). Unprinted JVM step, hence INFERRED. |
| 25 | Priority.fromValue | `(I)Lorg/proninyaroslav/libretorrent/core/model/data/Priority;` | REACHABLE | SOURCE | **REVISED 2026-11-01 OPEN-closing round 2 (was OPEN):** direct printed call at FilePriority.java:50 (`return Priority.fromValue(priority);`, inside `FilePriority.getPriority()` :48–51), called at DetailTorrentViewModel.java:420 (`file.getFilePriority().getPriority()`, inside private `getFilePriorities()` :413–423), called at :505 inside `checkParamsChanged()` :478–520 (`BR.prioritiesChanged` branch), reached via `mutableParamsCallback.onPropertyChanged` :443–466 registered in the ViewModel constructor at :112, triggered by `applyPriority` :334 (`mutableParams.setPrioritiesChanged(true)`), called from DetailTorrentFilesFragment.java:353 and :502. Def Priority.java:70–78. Prior pass missed this because its 20-file corpus excluded FilePriority and this ViewModel path (PriorityConverter indeed does not call it). Strict-entry caveat: detail-files-fragment anchored; the callback step is databinding-library dispatch, so under a whole-route-INFERRED convention this would read INFERRED, label unaffected. |
| 26 | Priority.value | `()I` | REACHABLE | SOURCE | PriorityConverter.java:32–39 (static initialiser: `Priority.IGNORE.value()` … `Priority.TOP_PRIORITY.value()`), :64 (app→lib array convert) and :96 (app→lib single convert at:94–101). Def Priority.java:65–68. |
| 27 | ReadPieceInfo.\<init\> | `(IIJLjava/lang/Exception;)V` | REACHABLE | SOURCE | TorrentDownloadImpl.handleReadPiece:447–450 `new ReadPieceInfo(alert.piece(), alert.size(), alert.bufferPtr(), err)`, then listener dispatch at:452–453. Def ReadPieceInfo.java:31–37. (The listener consumer, `TorrentEngineListener.onReadPiece`, has an empty default per the prior pass; construction itself is printed, so the ctor row stands regardless of whether any listener overrides it.) |
| 28 | ReadPieceInfo.toString | `()Ljava/lang/String;` | UNREACHABLE | INFERRED | Def ReadPieceInfo.java:39–49. No printed logging/concatenation caller in this pass (the only printed consumer path, `onReadPiece`, is an empty default). Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 29 | SessionStats.\<clinit\> | `()V` | REACHABLE | INFERRED | Class init precedes first use: TorrentSessionImpl.handleStats:1174 `new SessionStats(...)` (fresh print below). JVM timing unprinted, hence INFERRED. |
| 30 | SessionStats.\<init\>(long,long,long,long,long,int) | `(JJJJJI)V` | REACHABLE | SOURCE | TorrentSessionImpl.handleStats:1173–1179: `notifyListeners((listener) -> listener.onSessionStats(new SessionStats(dhtNodes(), getTotalDownload(), getTotalUpload(), getDownloadSpeed(), getUploadSpeed(), getListenPort())))`. Def SessionStats.java:36–46. `handleStats` is invoked from the session's alert/stat path (batch 38–40 pass: `handleStats` at TorrentSessionImpl:1168–1181, dispatched via InnerListener alert SESSION_STATS); the alert-dispatch step itself was not freshly printed in this pass, so this row carries the strict-entry caveat (see Conventions). |
| 31 | SessionStats.\<init\>(Parcel) | `(Landroid/os/Parcel;)V` | OPEN | — | Def SessionStats.java:48–58 (calls `super(source)` at:50). Only printed caller is its own CREATOR.createFromParcel:82–86, itself OPEN (row 39). Stays OPEN. |
| 32 | SessionStats.compareTo | `(Ljava/lang/Object;)I` | OPEN | — | Def SessionStats.java:110–114 (`parcelId.compareTo(...)`). SessionStats travels singly via the listener/Flowable (TorrentInfoProvider:480–485), not in a sorted collection; no printed sort caller in this pass. Stays OPEN. |
| 33 | SessionStats.describeContents | `()I` | OPEN | — | Def SessionStats.java:60–64 (`return 0;`). Framework marshalling only; no printed parcel site. Stays OPEN. |
| 34 | SessionStats.equals | `(Ljava/lang/Object;)Z` | REACHABLE | SOURCE | Direct printed call: TorrentInfoProvider.makeSessionStatsFlowable:482 `if (!newStats.equals(oldStats))`, inside `onSessionStats` at:480, listener registered at:491 `engine.addListener(listener)`. Def SessionStats.java:116–133. |
| 35 | SessionStats.hashCode | `()I` | UNREACHABLE | INFERRED | Def SessionStats.java:95–108. The printed equals use (row 34) is a direct call, not a hash-collection use; no printed HashMap/HashSet use of SessionStats in this pass. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 36 | SessionStats.toString | `()Ljava/lang/String;` | UNREACHABLE | INFERRED | Def SessionStats.java:135–147. No printed logging/concatenation caller in this pass. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 37 | SessionStats.writeToParcel | `(Landroid/os/Parcel;I)V` | OPEN | — | Def SessionStats.java:66–77 (calls `super.writeToParcel` at:69). Printed SessionStats travel is via listener/Flowable, not Parcel. Stays OPEN. |
| 38 | SessionStats$1.\<init\> | `()V` | REACHABLE | INFERRED | Anonymous Creator at SessionStats.java:79–93. Field initializer runs at class init on first use (row 30 route). Same convention as row 5. |
| 39 | SessionStats$1.createFromParcel | `(Landroid/os/Parcel;)Lorg/proninyaroslav/libretorrent/core/model/data/SessionStats;` | OPEN | — | Def SessionStats.java:82–86. Framework dispatch only, no printed unparcel site. Stays OPEN. |
| 40 | SessionStats$1.newArray | `(I)[Lorg/proninyaroslav/libretorrent/core/model/data/SessionStats;` | UNREACHABLE | INFERRED | Def SessionStats.java:88–92. Framework dispatch only. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |

## Changes vs prior proposal (lead only, 15/0/25)

- **Same label set, same counts (15/0/25).** No row changed label in this re-derive.
- **One confirmed_by change:** row 5 MagnetInfo$1.\<init\> SOURCE → INFERRED, under the uniform Creator-$1.\<init\> treatment in Conventions (JVM class-init timing is unprinted). Label unchanged.
- All other rows re-verified on fresh prints at the lines cited above; the prior proposal's route text held up, including the PriorityConverter static-map point (row 25) and the SessionStats singly-travelled point (row 32).

## Conventions (recorded, not decided — merger must pick project-wide)

1. **Strict-entry:** no launcher step was freshly printed in this pass. Every REACHABLE row above is anchored at session/engine/provider/download sites and **reverts to OPEN under a strict launcher-entry rule** (printed launcher → host step required). Do not claim a launcher anchor from a sibling batch's print.
2. **Per-row confirmed_by** (see table header). Under a whole-route INFERRED convention, SOURCE rows reached through unprinted alert/Rx dispatch (notably rows 11, 27, 30) would read INFERRED; labels unchanged.
3. **Parcelable Creator `$1.<init>`:** INFERRED when the enclosing class is first used on a printed route, because the CREATOR field initializer runs at class init (JVM timing unprinted). This is applied uniformly to rows 5, 20, 38. It does **not** extend to `createFromParcel`/`newArray`, which run only on framework unparcel.
4. **`<clinit>`:** INFERRED when any method/ctor/field of the class is used on a printed route (class init precedes first use). Applied to rows 8, 23, 29.
5. **Parcelable-trio policy:** `writeToParcel` / `describeContents` / Parcel ctor / `$1.createFromParcel` / `$1.newArray` stay OPEN unless a printed app-side parcel/unparcel site is found (Intent/Bundle `putExtra`/`getParcelableExtra`, `writeParcelable`, or a printed unparcel site). A CREATOR definition alone is not a caller.
6. **Library-dispatch equals:** `contains`/`containsAll`/`remove` on a List dispatch to element `equals` by library code, so such rows are INFERRED, not SOURCE (row 15). An explicit printed `x.equals(y)` call is SOURCE (batch 30 row 7, batch 29 row 34).
7. **No OPEN → UNREACHABLE flip on absence** without a saved full-repo grep in rule-F/C5 form. The greps reported above are over the fetched subset only and prove nothing elsewhere.
8. **Dependency rule:** a method whose only printed caller sits inside an OPEN method does not become REACHABLE (rows 9, 21, 31, 39 illustrate the Parcel-ctor/CREATOR loop; row 25 illustrates the converter's deliberate non-use).

## Gaps / named resolvers (all OPEN rows, plus the grep owed for any future UNREACHABLE claim)

- **Saved full-repo grep** (rule F/C5 form, covering generated code) for each OPEN row's exact call site, in particular: `MagnetInfo.getUri()` (row 1), `Priority.fromValue` (row 25), `PeerInfo` 10-arg ctor (row 10), all Parcelable-trio rows (4, 6, 7, 9, 14, 19, 21, 22, 31, 33, 37, 39, 40), all `hashCode`/`toString`/`compareTo` rows (2, 3, 13, 17, 18, 28, 32, 35, 36). A single printed caller flips the corresponding row to REACHABLE (confirmed_by judged at that time); a clean saved full-repo grep is the evidence that would support an UNREACHABLE proposal, subject to the merger's decision.
- **No UNREACHABLE row is claimed in this batch**, so no UNREACHABLE grep is owed for a label. If the merger wants any OPEN row proposed UNREACHABLE, the grep above is the prerequisite.
- **Merger re-checks:** `TorrentSessionImpl.java` SHA differs from the batch 38–40 pass's copy — diff the two copies before merging any row that cites both passes; `handleStats` alert-dispatch step (row 30) was not freshly printed in this pass.
- **Still owed (not run):** main spot-check 1 in 5, `py_compile`, build, Mac build/C1, sampler. None claimed passed.
