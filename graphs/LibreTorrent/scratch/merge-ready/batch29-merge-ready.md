# LibreTorrent batch 29 — merge-ready (UNVERIFIED)

**Status: UNVERIFIED — proposal only, not verified for merge. Do not merge on this file alone.**
**App:** LibreTorrent. **Branch:** `work-2026-10-31` (GitHub connector only; no git clone — a true git clone fails in this VM with no credential device; that check is named missing, not passed).
**Membership:** verified against the local plan copy `~/workspace/agent27-plan.tsv` (plan SHA `0104806dd666c840049b3db52823d4b384fa1c92`): batch 29 = 40 rows, all `TODO_CANDIDATE_REACHABLE`, in plan order below. This file **overwrites** the previous batch-29 blocker record (which judged nothing — its only fresh fetch, the plan file, had failed with GitHub HTTP 429).
**Prior proposal used as lead only:** `~/workspace/libretorrent-batch29-proposal.md` (15/0/25). Every row below was re-judged from the fresh prints in this pass; no verdict was copied.
**Build: not run. C1: not run.** (Build/C1 run on the user's Mac after a push; never claimed passed here.)
**No push.** Pushes are held until verified and merged to `[L]`.
**No edit** was made to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another helper's file.
**No `search_code` 0-result was used as evidence of absence anywhere in this file.** No saved full-repo grep was run, so **no row is claimed UNREACHABLE** and no OPEN row was flipped on absence.

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
| 2 | MagnetInfo.hashCode | `()I` | OPEN | — | Def MagnetInfo.java:115–119 (`return sha1hash.hashCode();`). No printed hash-collection use of a MagnetInfo in this pass. Stays OPEN. |
| 3 | MagnetInfo.toString | `()Ljava/lang/String;` | OPEN | — | Def MagnetInfo.java:121–131. No printed logging/concatenation caller in this pass. Stays OPEN. |
| 4 | MagnetInfo.writeToParcel | `(Landroid/os/Parcel;I)V` | OPEN | — | Def MagnetInfo.java:70–77. No printed app-side parcel site for a MagnetInfo (no `putExtra`/`writeParcelable`/Parcel-write site) in this pass. Parcelable-trio policy: stays OPEN. |
| 5 | MagnetInfo$1.\<init\> | `()V` | REACHABLE | INFERRED | Anonymous Creator at MagnetInfo.java:79–93. Field initializer runs at class init on first use: TorrentSessionImpl.fetchMagnet:439–440 `new MagnetInfo(...)` (and parseMagnet:450–451), reached via TorrentEngine.fetchMagnet:419 `session.fetchMagnet(uri)`. JVM timing unprinted, hence INFERRED, not SOURCE. **Confirmed_by variant vs prior proposal, which marked this SOURCE; label unchanged.** Reverts to OPEN only if the merger rejects the Creator-$1.\<init\> convention (see Conventions). |
| 6 | MagnetInfo$1.createFromParcel | `(Landroid/os/Parcel;)Lorg/proninyaroslav/libretorrent/core/model/data/MagnetInfo;` | OPEN | — | Def MagnetInfo.java:82–86 (`return new MagnetInfo(source);`). Called only by framework parcel dispatch; no printed unparcel site for a MagnetInfo in this pass. Stays OPEN. Note: row 6 OPEN does not make row 5 OPEN — row 5 runs at class init, row 6 only on unparcel. |
| 7 | MagnetInfo$1.newArray | `(I)[Lorg/proninyaroslav/libretorrent/core/model/data/MagnetInfo;` | OPEN | — | Def MagnetInfo.java:88–92. Framework dispatch only, no printed unparcel site. Stays OPEN. |
| 8 | PeerInfo.\<clinit\> | `()V` | REACHABLE | INFERRED | Class init precedes first use: TorrentDownloadImpl.getPeerInfoList:924 `new PeerInfo(peer, status)` (fresh print below). JVM timing unprinted, hence INFERRED. |
| 9 | PeerInfo.\<init\>(Parcel) | `(Landroid/os/Parcel;)V` | OPEN | — | Def PeerInfo.java:92–107. Only printed caller is its own CREATOR.createFromParcel:170–172, itself OPEN (row 21). Parcelable-trio policy: stays OPEN. |
| 10 | PeerInfo.\<init\>(String,String,long,long,double,int,int,int,int,int) | `(Ljava/lang/String;Ljava/lang/String;JJDIIIII)V` | OPEN | — | Def PeerInfo.java:72–91 (10-arg ctor). Only printed construction in this pass is the 2-arg form (row 11). No printed 10-arg construction site. Stays OPEN; the 10-arg ctor is not reached by the 2-arg ctor (it does not delegate to it). |
| 11 | PeerInfo.\<init\>(AdvancedPeerInfo,TorrentStatus) | `(Lorg/proninyaroslav/libretorrent/core/model/session/AdvancedPeerInfo;Lorg/libtorrent4j/TorrentStatus;)V` | REACHABLE | SOURCE | TorrentDownloadImpl.java:924 `PeerInfo state = new PeerInfo(peer, status);` inside getPeerInfoList:911–929, reached via TorrentEngine.makePeerInfoList:872–881 (`return task.getPeerInfoList();`), reached via TorrentInfoProvider.makePeersInfoFlowable:396 (`engine.makePeerInfoList(id)`) and :410. |
| 12 | PeerInfo.calcRelevance | `(Lorg/proninyaroslav/libretorrent/core/model/session/AdvancedPeerInfo;Lorg/libtorrent4j/TorrentStatus;)D` | REACHABLE | SOURCE | Called from the 2-arg ctor itself, PeerInfo.java:64 `relevance = calcRelevance(peer, torrentStatus);`. Def:122–141 (private). |
| 13 | PeerInfo.compareTo | `(Ljava/lang/Object;)I` | OPEN | — | Def PeerInfo.java:183–185 (`ip.compareTo(...)`). No printed sort / sorted-collection use of PeerInfo lists in this pass (peers flow via `containsAll`, which uses equals, not compareTo). Stays OPEN. |
| 14 | PeerInfo.describeContents | `()I` | OPEN | — | Def PeerInfo.java:144–146. Framework marshalling only; no printed parcel site. Stays OPEN. |
| 15 | PeerInfo.equals | `(Ljava/lang/Object;)Z` | REACHABLE | INFERRED | Library dispatch: TorrentInfoProvider.makePeersInfoFlowable:399 `!oldInfoList.containsAll(newInfoList)` — `List.containsAll` dispatches to element `equals` (PeerInfo.java:209–229). No explicit printed `peer.equals(...)` call, hence INFERRED, not SOURCE. |
| 16 | PeerInfo.getConnectionType | `(Lorg/proninyaroslav/libretorrent/core/model/session/AdvancedPeerInfo;)I` | REACHABLE | SOURCE | Called from the 2-arg ctor itself, PeerInfo.java:65 `connectionType = getConnectionType(peer);`. Def:108–120 (private). |
| 17 | PeerInfo.hashCode | `()I` | OPEN | — | Def PeerInfo.java:189–207. `containsAll` (row 15) uses equals, not hashCode; no printed hash-collection use of PeerInfo in this pass. Stays OPEN. |
| 18 | PeerInfo.toString | `()Ljava/lang/String;` | OPEN | — | Def PeerInfo.java:233–247. No printed logging/concatenation caller in this pass. Stays OPEN. |
| 19 | PeerInfo.writeToParcel | `(Landroid/os/Parcel;I)V` | OPEN | — | Def PeerInfo.java:150–164 (calls `super.writeToParcel` at:152). No printed app-side parcel site for a PeerInfo in this pass. Stays OPEN. |
| 20 | PeerInfo$1.\<init\> | `()V` | REACHABLE | INFERRED | Anonymous Creator at PeerInfo.java:166–180. Field initializer runs at class init on first use (row 11 route). Same convention as row 5. |
| 21 | PeerInfo$1.createFromParcel | `(Landroid/os/Parcel;)Lorg/proninyaroslav/libretorrent/core/model/data/PeerInfo;` | OPEN | — | Def PeerInfo.java:170–172. Framework dispatch only, no printed unparcel site. Stays OPEN. |
| 22 | PeerInfo$1.newArray | `(I)[Lorg/proninyaroslav/libretorrent/core/model/data/PeerInfo;` | OPEN | — | Def PeerInfo.java:176–178. Framework dispatch only. Stays OPEN. |
| 23 | Priority.\<clinit\> | `()V` | REACHABLE | INFERRED | Class init precedes first use: TorrentEngine.java:1184 `Arrays.fill(priorities, Priority.DEFAULT)`; also TorrentSessionImpl.java:301 `Arrays.fill(params.filePriorities, Priority.DEFAULT)` (session grep, this pass) and PriorityConverter static initialisers at PriorityConverter.java:31–52 (which themselves reference Priority constants and run when PriorityConverter loads). JVM timing unprinted, hence INFERRED. |
| 24 | Priority.\<init\> | `(Ljava/lang/String;II)V` | REACHABLE | INFERRED | Enum ctor, Priority.java:58–61 (`this.val = val;`). The JVM invokes it once per constant (constants at:27–56) during \<clinit\> (row 23). Unprinted JVM step, hence INFERRED. |
| 25 | Priority.fromValue | `(I)Lorg/proninyaroslav/libretorrent/core/model/data/Priority;` | OPEN | — | Def Priority.java:70–78. Grep of all files fetched in this pass finds no `Priority.fromValue` caller (the `fromValue` hits in TorrentEngine.java:1097/:1109/:1113 are `SessionSettings.ProxyType`/`EncryptMode`, different classes). PriorityConverter deliberately does NOT call it — it uses static `SparseArray` maps at PriorityConverter.java:30–52 and `value()` at:64/:97. Stays OPEN; a saved full-repo grep is the named resolver. |
| 26 | Priority.value | `()I` | REACHABLE | SOURCE | PriorityConverter.java:32–39 (static initialiser: `Priority.IGNORE.value()` … `Priority.TOP_PRIORITY.value()`), :64 (app→lib array convert) and :97 (app→lib single convert at:94–101). Def Priority.java:65–68. |
| 27 | ReadPieceInfo.\<init\> | `(IIJLjava/lang/Exception;)V` | REACHABLE | SOURCE | TorrentDownloadImpl.handleReadPiece:447–450 `new ReadPieceInfo(alert.piece(), alert.size(), alert.bufferPtr(), err)`, then listener dispatch at:452–453. Def ReadPieceInfo.java:31–37. (The listener consumer, `TorrentEngineListener.onReadPiece`, has an empty default per the prior pass; construction itself is printed, so the ctor row stands regardless of whether any listener overrides it.) |
| 28 | ReadPieceInfo.toString | `()Ljava/lang/String;` | OPEN | — | Def ReadPieceInfo.java:39–49. No printed logging/concatenation caller in this pass (the only printed consumer path, `onReadPiece`, is an empty default). Stays OPEN. |
| 29 | SessionStats.\<clinit\> | `()V` | REACHABLE | INFERRED | Class init precedes first use: TorrentSessionImpl.handleStats:1174 `new SessionStats(...)` (fresh print below). JVM timing unprinted, hence INFERRED. |
| 30 | SessionStats.\<init\>(long,long,long,long,long,int) | `(JJJJJI)V` | REACHABLE | SOURCE | TorrentSessionImpl.handleStats:1173–1179: `notifyListeners((listener) -> listener.onSessionStats(new SessionStats(dhtNodes(), getTotalDownload(), getTotalUpload(), getDownloadSpeed(), getUploadSpeed(), getListenPort())))`. Def SessionStats.java:36–46. `handleStats` is invoked from the session's alert/stat path (batch 38–40 pass: `handleStats` at TorrentSessionImpl:1168–1181, dispatched via InnerListener alert SESSION_STATS); the alert-dispatch step itself was not freshly printed in this pass, so this row carries the strict-entry caveat (see Conventions). |
| 31 | SessionStats.\<init\>(Parcel) | `(Landroid/os/Parcel;)V` | OPEN | — | Def SessionStats.java:48–58 (calls `super(source)` at:50). Only printed caller is its own CREATOR.createFromParcel:82–86, itself OPEN (row 39). Stays OPEN. |
| 32 | SessionStats.compareTo | `(Ljava/lang/Object;)I` | OPEN | — | Def SessionStats.java:110–114 (`parcelId.compareTo(...)`). SessionStats travels singly via the listener/Flowable (TorrentInfoProvider:480–485), not in a sorted collection; no printed sort caller in this pass. Stays OPEN. |
| 33 | SessionStats.describeContents | `()I` | OPEN | — | Def SessionStats.java:60–64 (`return 0;`). Framework marshalling only; no printed parcel site. Stays OPEN. |
| 34 | SessionStats.equals | `(Ljava/lang/Object;)Z` | REACHABLE | SOURCE | Direct printed call: TorrentInfoProvider.makeSessionStatsFlowable:482 `if (!newStats.equals(oldStats))`, inside `onSessionStats` at:480, listener registered at:491 `engine.addListener(listener)`. Def SessionStats.java:116–133. |
| 35 | SessionStats.hashCode | `()I` | OPEN | — | Def SessionStats.java:95–108. The printed equals use (row 34) is a direct call, not a hash-collection use; no printed HashMap/HashSet use of SessionStats in this pass. Stays OPEN. |
| 36 | SessionStats.toString | `()Ljava/lang/String;` | OPEN | — | Def SessionStats.java:135–147. No printed logging/concatenation caller in this pass. Stays OPEN. |
| 37 | SessionStats.writeToParcel | `(Landroid/os/Parcel;I)V` | OPEN | — | Def SessionStats.java:66–77 (calls `super.writeToParcel` at:69). Printed SessionStats travel is via listener/Flowable, not Parcel. Stays OPEN. |
| 38 | SessionStats$1.\<init\> | `()V` | REACHABLE | INFERRED | Anonymous Creator at SessionStats.java:79–93. Field initializer runs at class init on first use (row 30 route). Same convention as row 5. |
| 39 | SessionStats$1.createFromParcel | `(Landroid/os/Parcel;)Lorg/proninyaroslav/libretorrent/core/model/data/SessionStats;` | OPEN | — | Def SessionStats.java:82–86. Framework dispatch only, no printed unparcel site. Stays OPEN. |
| 40 | SessionStats$1.newArray | `(I)[Lorg/proninyaroslav/libretorrent/core/model/data/SessionStats;` | OPEN | — | Def SessionStats.java:88–92. Framework dispatch only. Stays OPEN. |

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
