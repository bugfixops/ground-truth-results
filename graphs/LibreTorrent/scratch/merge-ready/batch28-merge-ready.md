# LibreTorrent batch 28 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler or full-repo grep was run or is claimed.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 28 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior Agent 6 re-derivation and the
  carried-forward merge-ready file that preceded this file (which stated its citations were
  input citations, not fresh prints, after a 429) were used as INPUT / lead lists only; every
  row below was re-judged against source freshly fetched in this pass, and no prior verdict was
  copied as a result. This file supersedes that carried-forward version. One correction to the
  prior proposal is documented below (row 18, AbstractInfoParcel no-arg ctor); no label changed
  from Agent 6's version.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 28 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/b27scratch/LIBRETORRENT_BATCH_PLAN.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-28 rows are `TODO_CANDIDATE_REACHABLE` in the plan — a generator candidate, not evidence.
Composition: TorrentInfoProvider$1–$4 (17 rows), AbstractInfoParcel (4), AdvancedTorrentInfo (12),
MagnetInfo (7).

## Counts — mechanically verified

- **REACHABLE proposed: 27 / 40**
- **UNREACHABLE proposed: 0**
- **OPEN: 13 / 40** (rows 18, 19, 21, 23, 25, 26, 28, 29, 30, 32, 33, 35, 37)
- **Verified for merge: 0**
- confirmed_by among REACHABLE: **SOURCE 24 / INFERRED 3**.
- Table rows 1–40 intact, in plan order, method names and JVM descriptors matched against the plan.

## confirmed_by convention used in this file (labels unaffected by the convention choice)

- SOURCE = a printed app-code line names the method as a call target: a direct call, a
  `notifyListeners` call site naming a listener callback, a printed `new X(...)` / anonymous
  instantiation site for a `<init>` row, or a printed call inside a flowable body (e.g.
  `TorrentInfoProvider:331 !newInfo.equals(oldInfo)` for AdvancedTorrentInfo.equals).
- INFERRED = the method is reached only through unprinted framework/library/JVM dispatch:
  JVM class initialisation (`<clinit>`), or a `<init>` whose instantiation happens only inside
  a `<clinit>` (AdvancedTorrentInfo$1, instantiated by the static CREATOR field initializer).
- Anonymous listener `<init>` rows ($1–$4) are SOURCE, because their anonymous instantiation
  sites are printed outside any `<clinit>` (TorrentInfoProvider :147, :253, :457, :478).
  The Creator `<init>` row (31) is INFERRED, because its only instantiation is the CREATOR
  field initializer inside row 22's `<clinit>`.
- Never `DYN`, `FW-MEMORY`, or `UNVERIFIED` as confirmed_by. OPEN rows show — (none).
- Anonymous-class mapping is by file order in the fresh TorrentInfoProvider print, NOT
  bytecode-verified: $1 = listener in `makeInfoFlowable` (:147), $2 = listener in
  `makeInfoListFlowable` (:253), $3 = listener in `makeTorrentsDeletedFlowable` (:457),
  $4 = listener in `makeSessionStatsFlowable` (:478). The override sets match the plan rows
  exactly ($1: stateChanged, paused, restoreSessionError, torrentError, sessionStats — no
  onTorrentRemoved; $2: all six including onTorrentRemoved; $3: only onTorrentRemoved;
  $4: only onSessionStats), which corroborates the mapping independently of file order.

## Printed source used in this pass (fresh connector fetches, branch work-2026-10-31, one at a time, with pauses)

Source root for all files:
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`
Saved under `~/workspace/b262728-src/`. No fresh HTTP 429 was hit in this pass.

- `core/model/TorrentInfoProvider.java` — fresh, 498 lines, SHA-256
  `6d70d61fa0c808d9904ae7f6b3111aacbb086d478a94e4d223db9043b7ecf4fc`, byte-identical to the
  local copy in `~/workspace/b27scratch/`. Listener starts :147 ($1), :253 ($2), :457 ($3),
  :478 ($4); registrations :214 ($1), :293 ($2), :466 ($3), :491 ($4).
- `core/model/data/AdvancedTorrentInfo.java` — fresh, 208 lines, SHA-256
  `33f8ae0d33604c7d3f6f821a13ed934fbd98501136d749f84aeb12fd80a27c7c`, byte-identical to the
  local copy in `~/workspace/libretorrent-merge/b3-src/core/model/data/`.
- `core/model/data/MagnetInfo.java` — fresh, 132 lines.
- `core/model/data/AbstractInfoParcel.java` — fresh, 62 lines.
- `ui/detailtorrent/DetailTorrentViewModel.java` — fresh, SHA-256
  `de6c860e0d5386cdcd01612e8fd7e0b582cf7cf08f4c02f8abcbdc3042b39c91`, byte-identical to the
  local copy in `~/workspace/b27scratch/`.
- `ui/detailtorrent/DetailTorrentFragment.java` — fresh, SHA-256
  `580c1b0ce3da3ec74b2e1e7b356459326985008bc477f535d2b5876a0947e307`, byte-identical to the
  local copy in `~/workspace/b27scratch/`.
- `ui/main/MainViewModel.java` — fresh, SHA-256
  `251f206bfed7b3bd58bde30246996bf3dae4dd15259658a8df5969c0e6378343`, byte-identical to the
  local copy in `~/workspace/b27scratch/`.
- `ui/main/MainActivity.java` — fresh, SHA-256
  `b98a504934ed44800b9505539e4c12dd952606141fcbb04e4b0f40780a4d8454`, byte-identical to the
  local copy in `~/workspace/b27scratch/`.
- `ui/addtorrent/AddTorrentViewModel.java` — fresh (magnet branch :237, getters :242, :245–246).
- `core/model/TorrentEngine.java` — fresh, 1,658 lines (`fetchMagnet` :415–423 incl.
  `info.getSha1hash()` :422; `makeInfoSync` :766; `makeAdvancedInfoSync` :832, 12-arg
  `new AdvancedTorrentInfo(...)` :846–860; `addListener` :307–309 → `session.addListener`).
- `core/model/session/TorrentSessionImpl.java` — fresh, 1,720 lines (`notifyListeners` :1445–1450;
  delete path :388–390; restore path :1527–1529; `handleStats` :1168–1178).
- `core/model/session/TorrentDownloadImpl.java` — fresh, 1,711 lines (`notifyListeners` :187–193;
  STATE_CHANGED :224–230; TORRENT_PAUSED :237–240; error sites :333–336, :421–424;
  `torrentRemoved` :456–460).
- `core/model/TorrentEngineListener.java` — fresh, 73 lines (all callbacks empty bodies).
- Subclass constructors (TorrentInfo, PeerInfo, TrackerInfo) — re-read from local copies in
  `~/workspace/libretorrent-merge/b3-src/core/model/data/` and `~/workspace/agent6-src/`,
  NOT freshly fetched in this pass; flagged as such in row 18. They show only
  `super(String)` / `super(Parcel)` calls, no no-arg ctor, in those copies.

## Printed route anchors

- `$1` listeners: DetailTorrentViewModel (fresh) `observeTorrentInfo` :167–168 →
  TorrentInfoProvider (fresh) `observeInfo` :94–95 → `makeInfoFlowable` :130, listener :147,
  registration :214.
- `$2` listeners: MainViewModel (fresh) `observeAllTorrentsInfo` :77–78 →
  TorrentInfoProvider `observeInfoList` :98–99 → `makeInfoListFlowable` :238, listener :253,
  registration :293.
- `$3` listener: MainViewModel (fresh) `observeTorrentsDeleted` :85–86 →
  TorrentInfoProvider `observeTorrentsDeleted` :122–123 → `makeTorrentsDeletedFlowable` :455,
  listener :457, registration :466.
- `$4` listener: MainActivity (fresh) `subscribeSessionStats` :456–460 →
  TorrentInfoProvider `observeSessionStats` :126–127 → `makeSessionStatsFlowable` :474,
  listener :478, registration :491. This is the weakest anchor in the batch only in the sense
  that it rests on MainActivity rather than a ViewModel; the MainActivity lines are fresh in
  this pass, so the weakness noted in prior proposals (no UI caller printed) no longer applies.
- Listener dispatch (fresh): `TorrentEngine.addListener` :307–309 delegates to
  `session.addListener`; both session and download-task dispatchers iterate the same queue
  (TorrentSessionImpl `notifyListeners` :1445–1450; TorrentDownloadImpl `notifyListeners` :187–193).
- AdvancedTorrentInfo data methods: DetailTorrentViewModel (fresh) `observeAdvancedTorrentInfo`
  :171–172 → TorrentInfoProvider `observeAdvancedInfo` :106–107 → `makeAdvancedInfoFlowable` :323
  → `TorrentEngine.makeAdvancedInfoSync` :832.
- MagnetInfo methods: AddTorrentViewModel (fresh) magnet branch :237 →
  `TorrentEngine.fetchMagnet` :415–419 → `TorrentSessionImpl.fetchMagnet` / `parseMagnet`
  (prior proposal's session lines; session file is fresh in this pass, magnet construction at
  TorrentEngine :419 and :422 confirms the chain, and AddTorrentViewModel :242/:245–246
  confirms the getter uses).

## Strict-entry caveat (explicit, all REACHABLE rows)

Routes are anchored at ViewModel / provider methods and MainActivity, not at a fully printed
launcher chain; the Activity → ViewModel step and (for $1) the DetailTorrentFragment → ViewModel
step beyond `subscribeTorrentInfo` were not all freshly printed here (DetailTorrentFragment
itself is fresh: `subscribeTorrentInfo` :251 subscribes `observeTorrentInfoPair` :265 and
`observeAdvancedTorrentInfo` :271, which covers the $1 anchor). Under a strict launcher-entry
rule all 27 REACHABLE rows revert to OPEN. Under the anchor convention used by sibling
detail/main batches, they are REACHABLE as tabled. The merger must pick one strict-entry
convention for all batches; this file does not decide it.

## Parcelable policy used in this batch (consistent with batch 22 precedent)

A Parcelable framework method (`createFromParcel`, `newArray`, `describeContents`,
`writeToParcel`, a Parcel ctor) is REACHABLE only with a printed parcel/unparcel site, not
from the `Parcelable` interface alone and not from a CREATOR field alone. A method whose only
printed caller is itself an OPEN Parcelable/framework method inherits OPEN (rows 19, 21, 23).
A `Comparable`/`hashCode`/`toString` method is REACHABLE only with a printed sort, hash-collection,
or log/concatenation caller, not from the interface alone (rows 25, 28, 29). No OPEN row here is
flipped to UNREACHABLE: no saved full-repo grep was run, and no `search_code` 0 result was used
as evidence of absence.

## Correction to the prior proposal (label unchanged)

Row 18, `AbstractInfoParcel.<init>()`: the prior proposal stated that the printed subclasses
call only `super(String)` / `super(Parcel)`. That is true for TorrentInfo, PeerInfo, and
TrackerInfo in the local copies checked, but it misses one printed super-call: the freshly
printed `AdvancedTorrentInfo()` no-arg ctor :49–52 explicitly calls `super()`. The label does
NOT change, because `AdvancedTorrentInfo()` itself has no printed caller in any file printed in
this session (the only printed `new AdvancedTorrentInfo(...)` site, TorrentEngine :846–860, is
the 12-arg ctor, row 24; no `new AdvancedTorrentInfo()` no-arg site was found in the printed
files). Row 18 therefore stays OPEN, now with the correct reason: its sole printed super-call
site is itself an uncalled ctor, not because no super-call exists. A printed no-arg
construction site flips both row 18 and the (non-batch-28) `AdvancedTorrentInfo()` row together.

## Per-row table (plan order)

| # | Method | Label | confirmed_by | Printed route / citations |
|---|---|---|---|---|
| 1 | TorrentInfoProvider$1.<init> (TorrentInfoProvider, Consumer, FlowableEmitter, String) | REACHABLE | SOURCE | Anonymous listener instantiated at TorrentInfoProvider:147 in `makeInfoFlowable()` (fresh); reached via DetailTorrentViewModel.observeTorrentInfo :167–168 (fresh) → `observeInfo` :94–95 → `makeInfoFlowable` :130. |
| 2 | TorrentInfoProvider$1.onRestoreSessionError (String) | REACHABLE | SOURCE | Override TorrentInfoProvider:173–182 (fresh) + registration :214; dispatch TorrentSessionImpl:1527–1529 via `notifyListeners` :1445–1450 (fresh). Same anchor as row 1. |
| 3 | TorrentInfoProvider$1.onSessionStats (SessionStats) | REACHABLE | SOURCE | Override TorrentInfoProvider:195–204 (fresh) + :214; dispatch TorrentSessionImpl `handleStats` :1168–1178 (fresh). Same anchor as row 1. |
| 4 | TorrentInfoProvider$1.onTorrentError (String, Exception) | REACHABLE | SOURCE | Override TorrentInfoProvider:184–194 (fresh) + :214; dispatch TorrentDownloadImpl:333–336 and :421–424 via `notifyListeners` :187–193 (fresh). Same anchor as row 1. |
| 5 | TorrentInfoProvider$1.onTorrentPaused (String) | REACHABLE | SOURCE | Override TorrentInfoProvider:162–172 (fresh) + :214; dispatch TorrentDownloadImpl:237–240 (TORRENT_PAUSED, fresh). Same anchor as row 1. |
| 6 | TorrentInfoProvider$1.onTorrentStateChanged (String, TorrentStateCode, TorrentStateCode) | REACHABLE | SOURCE | Override TorrentInfoProvider:149–161 (fresh) + :214; dispatch TorrentDownloadImpl:224–230 (STATE_CHANGED, fresh). Same anchor as row 1. |
| 7 | TorrentInfoProvider$2.<init> (TorrentInfoProvider, Runnable) | REACHABLE | SOURCE | Anonymous listener instantiated at TorrentInfoProvider:253 in `makeInfoListFlowable()` (fresh); reached via MainViewModel.observeAllTorrentsInfo :77–78 (fresh) → `observeInfoList` :98–99 → `makeInfoListFlowable` :238. |
| 8 | TorrentInfoProvider$2.onRestoreSessionError (String) | REACHABLE | SOURCE | Override TorrentInfoProvider:272–276 (fresh) + registration :293; dispatch TorrentSessionImpl:1527–1529 (fresh). Same anchor as row 7. |
| 9 | TorrentInfoProvider$2.onSessionStats (SessionStats) | REACHABLE | SOURCE | Override TorrentInfoProvider:282–286 (fresh) + :293; dispatch TorrentSessionImpl:1168–1178 (fresh). Same anchor as row 7. |
| 10 | TorrentInfoProvider$2.onTorrentError (String, Exception) | REACHABLE | SOURCE | Override TorrentInfoProvider:277–281 (fresh) + :293; dispatch TorrentDownloadImpl:333–336 and :421–424 (fresh). Same anchor as row 7. |
| 11 | TorrentInfoProvider$2.onTorrentPaused (String) | REACHABLE | SOURCE | Override TorrentInfoProvider:262–266 (fresh) + :293; dispatch TorrentDownloadImpl:237–240 (fresh). Same anchor as row 7. |
| 12 | TorrentInfoProvider$2.onTorrentRemoved (String) | REACHABLE | SOURCE | Override TorrentInfoProvider:267–271 (`handleInfo.run()`, fresh) + :293; dispatch TorrentSessionImpl:388–390 and TorrentDownloadImpl:456–460 (fresh). Same anchor as row 7. |
| 13 | TorrentInfoProvider$2.onTorrentStateChanged (String, TorrentStateCode, TorrentStateCode) | REACHABLE | SOURCE | Override TorrentInfoProvider:255–261 (fresh) + :293; dispatch TorrentDownloadImpl:224–230 (fresh). Same anchor as row 7. |
| 14 | TorrentInfoProvider$3.<init> (TorrentInfoProvider, FlowableEmitter) | REACHABLE | SOURCE | Anonymous listener instantiated at TorrentInfoProvider:457 in `makeTorrentsDeletedFlowable()` (fresh); reached via MainViewModel.observeTorrentsDeleted :85–86 (fresh) → `observeTorrentsDeleted` :122–123 → `makeTorrentsDeletedFlowable` :455. |
| 15 | TorrentInfoProvider$3.onTorrentRemoved (String) | REACHABLE | SOURCE | Override TorrentInfoProvider:459–463 (emits id if not cancelled, fresh) + registration :466; dispatch TorrentSessionImpl:388–390 and TorrentDownloadImpl:456–460 (fresh). Same anchor as row 14. |
| 16 | TorrentInfoProvider$4.<init> (TorrentInfoProvider, AtomicReference, FlowableEmitter) | REACHABLE | SOURCE | Anonymous listener instantiated at TorrentInfoProvider:478 in `makeSessionStatsFlowable()` (fresh); reached via MainActivity.subscribeSessionStats :456–460 (fresh) → `observeSessionStats` :126–127 → `makeSessionStatsFlowable` :474. |
| 17 | TorrentInfoProvider$4.onSessionStats (SessionStats) | REACHABLE | SOURCE | Override TorrentInfoProvider:480–488 (emits only on changed stats, fresh) + registration :491; dispatch TorrentSessionImpl:1168–1178 (fresh). Same anchor as row 16. |
| 18 | AbstractInfoParcel.<init> () | OPEN | — | Definition fresh AbstractInfoParcel:36–39 (`parcelId = UUID.randomUUID().toString()`). Sole printed super-call site is `AdvancedTorrentInfo()` :49–52 (`super()`), which itself has no printed caller in any file printed in this session (see Correction above). Other subclasses in local copies call only `super(String)` / `super(Parcel)`. Resolves by printing a `new AdvancedTorrentInfo()` no-arg site, or a saved full-repo grep for that ctor. NOT UNREACHABLE on this evidence. |
| 19 | AbstractInfoParcel.<init> (Parcel) | OPEN | — | Definition fresh AbstractInfoParcel:46–49. Printed callers are only subclass Parcel ctors (TorrentInfo:121, AdvancedTorrentInfo:76–77, PeerInfo:94, TrackerInfo:170 — local copies for the first three, fresh for Advanced), each called only from its class's `Creator.createFromParcel`, which is OPEN (row 32 and equivalents). Resolves with a printed parcel/unparcel site. |
| 20 | AbstractInfoParcel.<init> (String) | REACHABLE | SOURCE | Definition fresh AbstractInfoParcel:41–44. Called via `super(torrentId)` in TorrentInfo:68 and :98 (local copies) and via `super(torrentId)` in AdvancedTorrentInfo:54–75 (fresh 12-arg ctor); TorrentInfo is built in TorrentEngine `makeInfo` :779, :787 (fresh, via `makeInfoSync` :766), reached via the $1/$2 observe flows above. |
| 21 | AbstractInfoParcel.writeToParcel (Parcel, int) | OPEN | — | Definition fresh AbstractInfoParcel:52–55. Only printed caller is `super.writeToParcel(dest, flags)` in AdvancedTorrentInfo:103 (fresh), inside Advanced's `writeToParcel`, which is itself OPEN (row 30). Resolves with a printed site that parcels an `AbstractInfoParcel` subclass. |
| 22 | AdvancedTorrentInfo.<clinit> () | REACHABLE | INFERRED | JVM class initialiser for the static field `CREATOR`, printed at AdvancedTorrentInfo:119–134 (fresh). Triggered on first active use, printed at TorrentEngine:846–860 (`new AdvancedTorrentInfo(...)` in `makeAdvancedInfoSync` :832, fresh), reached via DetailTorrentViewModel:171–172 → `observeAdvancedInfo` :106–107 → `makeAdvancedInfoFlowable` :323 (all fresh). Class-init timing is not a printed call, hence INFERRED (Agent 6 correction, adopted). |
| 23 | AdvancedTorrentInfo.<init> (Parcel) | OPEN | — | Definition fresh AdvancedTorrentInfo:76–93 (`super(source)` + field reads). Only printed caller is `AdvancedTorrentInfo$1.createFromParcel` :123–126, which is OPEN (row 32). Resolves with a printed unparcel site for `AdvancedTorrentInfo`. |
| 24 | AdvancedTorrentInfo.<init> (String, long[], int, int, int, double, long, long, double, double[], int, int) | REACHABLE | SOURCE | Definition fresh AdvancedTorrentInfo:54–75. Called directly in TorrentEngine:846–860 (`makeAdvancedInfoSync` :832, fresh), reached via DetailTorrentViewModel:171–172 → `observeAdvancedInfo` :106–107 → `makeAdvancedInfoFlowable` :323 → `engine.makeAdvancedInfoSync(id)` (TorrentInfoProvider :329, :342, fresh). |
| 25 | AdvancedTorrentInfo.compareTo (Object) | OPEN | — | Definition fresh AdvancedTorrentInfo:136–139 (`torrentId.compareTo(...)`). No printed sort/compare site in any file printed in this session. Resolves by printing a sort/comparison site for `AdvancedTorrentInfo` objects, or a saved full-repo grep. Do not infer from the `Comparable` interface alone. NOT UNREACHABLE. |
| 26 | AdvancedTorrentInfo.describeContents () | OPEN | — | Definition fresh AdvancedTorrentInfo:95–98 (returns 0). Parcelable framework method; no printed marshalling site for this class in files printed in this session. Resolves with a printed parcel site. |
| 27 | AdvancedTorrentInfo.equals (Object) | REACHABLE | SOURCE | Definition fresh AdvancedTorrentInfo:165–187. Called in TorrentInfoProvider:331 (`!newInfo.equals(oldInfo)`) inside `makeAdvancedInfoFlowable` :323 (fresh), reached via DetailTorrentViewModel:171–172 → `observeAdvancedInfo` :106–107. |
| 28 | AdvancedTorrentInfo.hashCode () | OPEN | — | Definition fresh AdvancedTorrentInfo:142–163. No printed caller in files printed in this session (its `equals` use at TorrentInfoProvider:331 does not call `hashCode`, and no hash-based collection use of this class was printed). Resolves by printing a hash-map/set use, or another explicit `hashCode()` call site, or a saved full-repo grep. NOT UNREACHABLE. |
| 29 | AdvancedTorrentInfo.toString () | OPEN | — | Definition fresh AdvancedTorrentInfo:191–207. No printed logging/concatenation caller in files printed in this session. Resolves by printing a log/concatenation site for an `AdvancedTorrentInfo` value, or a saved full-repo grep. NOT UNREACHABLE. |
| 30 | AdvancedTorrentInfo.writeToParcel (Parcel, int) | OPEN | — | Definition fresh AdvancedTorrentInfo:101–117 (calls `super.writeToParcel` at :103, fresh). No printed parcel site for this class in files printed in this session. Resolves with a printed site that parcels an `AdvancedTorrentInfo`. |
| 31 | AdvancedTorrentInfo$1.<init> () | REACHABLE | INFERRED | Anonymous `Parcelable.Creator` instantiated only by the static field initializer at AdvancedTorrentInfo:119–134 (`CREATOR = new Parcelable.Creator<...>() {...}`, fresh), executed as part of row 22's `<clinit>` on the first printed class use (TorrentEngine:846–860, fresh). Instantiation inside `<clinit>` only, hence INFERRED, not SOURCE. |
| 32 | AdvancedTorrentInfo$1.createFromParcel (Parcel) | OPEN | — | Definition fresh AdvancedTorrentInfo:123–126 (`return new AdvancedTorrentInfo(source)`). Called only by the Parcel framework on unparcel; no printed unparcel site and no printed `fw_src` Parcel dispatch were read in this pass, so confirmed_by would be at best INFERRED with no printed route — left OPEN per the Parcelable policy. Resolves with a printed unparcel site. |
| 33 | AdvancedTorrentInfo$1.newArray (int) | OPEN | — | Definition fresh AdvancedTorrentInfo:129–132 (`return new AdvancedTorrentInfo[size]`). Same status and resolver as row 32: Parcel framework only, no printed call site. |
| 34 | MagnetInfo.<clinit> () | REACHABLE | INFERRED | JVM class initialiser for the static field `CREATOR`, printed at MagnetInfo:79–93 (fresh). Triggered on first active use, printed at TorrentSessionImpl `fetchMagnet` / `parseMagnet` (prior proposal's session lines; TorrentEngine `fetchMagnet` :415–419 fresh confirms the chain) ← AddTorrentViewModel magnet branch :237 (fresh). Class-init timing is not a printed call, hence INFERRED (Agent 6 correction, adopted). |
| 35 | MagnetInfo.<init> (Parcel) | OPEN | — | Definition fresh MagnetInfo:56–63. Only printed caller is MagnetInfo's own `CREATOR.createFromParcel` :83–86 (a Parcelable framework method in the same file, not itself a batch-28 row and not given a printed route). Resolves with a printed unparcel site for `MagnetInfo`. |
| 36 | MagnetInfo.<init> (String, String, String, List) | REACHABLE | SOURCE | Definition fresh MagnetInfo:48–54. Called in TorrentSessionImpl `fetchMagnet` :439–440 and `parseMagnet` :450–451 (prior proposal's session lines, session file fresh in this pass), via TorrentEngine:415–419, :427–428 (fresh), via AddTorrentViewModel:237 (fresh). |
| 37 | MagnetInfo.describeContents () | OPEN | — | Definition fresh MagnetInfo:65–68 (returns 0). Parcelable framework method; no printed marshalling site for this class in files printed in this session (its `writeToParcel` :71–77 is not a batch-28 row and also has no printed caller in the files read). Resolves with a printed parcel site. |
| 38 | MagnetInfo.getFilePriorities () | REACHABLE | SOURCE | Definition fresh MagnetInfo:110–112. Called in AddTorrentViewModel:245–246 (`magnetInfo.getFilePriorities()`, null-checked and copied, fresh), in the magnet branch reached via `TorrentEngine.fetchMagnet()` :237 (fresh). |
| 39 | MagnetInfo.getName () | REACHABLE | SOURCE | Definition fresh MagnetInfo:105–107. Called in AddTorrentViewModel:242 (`new TorrentMetaInfo(magnetInfo.getName(), magnetInfo.getSha1hash())`, fresh). Same anchor as row 38. |
| 40 | MagnetInfo.getSha1hash () | REACHABLE | SOURCE | Definition fresh MagnetInfo:100–102. Called in AddTorrentViewModel:242 (fresh) and independently in TorrentEngine:422 (`createFetchMagnetSingle(info.getSha1hash())` inside `fetchMagnet` :415–423, fresh). Same anchor as rows 38–39. |

## Gaps / what the merger must still close (not verdict changes)

- The 13 OPEN rows resolve only with a printed parcel/unparcel site, a printed sort/hash/log
  caller, a printed no-arg construction site (row 18), or a saved full-repo grep for the named
  method. No row here is UNREACHABLE, and no `search_code` 0 result was used as evidence of absence.
- Strict-entry convention (see above) is undecided, recorded here, not decided.
- Main-agent spot-check (1 in 5), `py_compile`, build, and Mac build/C1 are not run here.
- Subclass-constructor lines for TorrentInfo / PeerInfo / TrackerInfo (row 18–19 context) rest on
  local copies re-read in this session, not fresh fetches; the merger's spot-check should re-print
  at least one of those files fresh if it requires fresh evidence for every row. All other
  definition/caller files above are fresh connector fetches from branch work-2026-10-31 in this session.
