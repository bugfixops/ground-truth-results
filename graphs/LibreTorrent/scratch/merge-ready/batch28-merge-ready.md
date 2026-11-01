## Revision note — Stream A Phase 1c (APPLY DECISIONS), 2026-11-01 (UNVERIFIED, no label changes)

Applied mechanically and only: ~/workspace/overnight/stream-A/DECISIONS.md (Muse's own decisions, for user/Yang review, never Yang's). Counts before (main table, last occurrence per row, 40 rows): 27 REACHABLE / 0 UNREACHABLE / 13 OPEN. Counts after: 27 / 0 / 13 — unchanged. Rows flipped: NONE. Build: not run. C1: not run. Nothing pushed. No GitHub connector fetch was made in this pass; no 429 encountered.
D1: verified — every OPEN row already has confirmed_by —, so no cosmetic change was needed; per-row SOURCE rows stand (D1, including the notifyListeners/method-reference rule, D1(b)).
D2: anchor convention adopted — the 27 REACHABLE rows stand and do NOT revert under a strict launcher-entry rule (the sole D2 revert is batch 99, not this batch).
D12: rows 2 and 8 stand REACHABLE (listener-error rows, condition on the route, not a blocker).
D5b Treatment A: row 31 (AdvancedTorrentInfo$1.<init>) stands REACHABLE INFERRED.
Rows deliberately left OPEN, with decision ID: 18 (D5b dependency — sole super-call site uncalled), 19 (D5a + D5b dependency), 21 (D5a + D5b dependency — all super-callers OPEN), 23 (D5a + D5b dependency), 25 (no DECISIONS flip order; P2 — app-tree zero alone is never UNREACHABLE), 26 (D5a), 28 (D6 hashCode, printed-trigger rule), 29 (D7 toString, printed-trigger rule; dependency host batch 90 row 16 does not flip), 30 (D5a), 32 (D5a), 33 (D5a + D5c Option B — no printed Parcelable-array site), 35 (D5a + D5b dependency), 37 (D5a).
Conditional tables in this file are NOT applied beyond the decisions above: the parcel (xii) conditional requires a printed marshalling site for AdvancedTorrentInfo/MagnetInfo (none in DECISIONS for these classes), the newArray-follows-trio conditional is rejected by D5c Option B, and the UNREACHABLE-on-tree-grep conditional is rejected by P2/D6/D7 (app-tree zero alone never flips to UNREACHABLE).

## Revision note — OPEN-closing round 2 (G4), 2026-11-01 (UNVERIFIED, no label changes)

**Counts before (table as found, mechanically verified): 27 REACHABLE / 0 UNREACHABLE / 13 OPEN.
Counts after: 27 / 0 / 13 — unchanged. Rows whose label changed: NONE. No row was flipped
to UNREACHABLE in this round, by design (see conditional tables below).**
Backup of the pre-revision file: `~/workspace/libretorrent-merge-backup-pre-openclose2/batch28-merge-ready.md`
(md5-identical to the file before this edit).

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

What was checked for every OPEN row (13: 18, 19, 21, 23, 25, 26, 28, 29, 30, 32, 33, 35, 37):
- Row 18 `AbstractInfoParcel.<init>()`: the sole printed super-call site is
  `AdvancedTorrentInfo()` :49–52 (`super()`), and the full-tree ctor grep finds ZERO
  `new AdvancedTorrentInfo()` sites (only the 12-arg site at TorrentEngine:846 and the
  Parcel-ctor CREATOR site). The caller exists but is itself uncalled — dependency-OPEN,
  not zero-caller. A parcel site would NOT flip this row.
- Row 19 `AbstractInfoParcel.<init>(Parcel)`: printed callers are only subclass Parcel ctors
  (TorrentInfo:121, AdvancedTorrentInfo:76–77, PeerInfo:94, TrackerInfo:170, plus
  MagnetInfo/SessionStats/FeedChannel/FeedItem/Torrent equivalents), every one of which is
  itself an OPEN row. Dependency rule: stays OPEN; flips only together with a subclass
  Parcel ctor (see conditional table).
- Row 21 `AbstractInfoParcel.writeToParcel`: the five printed super-callers are exactly
  AdvancedTorrentInfo:103, PeerInfo:152, SessionStats:69, TorrentInfo:151, TrackerInfo:185 —
  each inside that subclass's own `writeToParcel`, all OPEN. No printed marshalling site
  for any subclass was found. Stays OPEN; flips SOURCE the moment any subclass
  `writeToParcel` flips, via its super call.
- Rows 23, 26, 30, 32, 33 (AdvancedTorrentInfo parcel trio + ctor) and 35, 37 (MagnetInfo
  Parcel ctor / describeContents): no `putExtra` / `putParcelable` / `getParcelableExtra` /
  Bundle / `setArguments` site names either class anywhere in the 252-file tree, and no
  `putParcelableArrayListExtra` / `getParcelableArrayListExtra` site exists tree-wide.
  MagnetInfo's `writeToParcel` is not a batch-28 row and was not judged here.
- Row 25 `compareTo`: no sort or comparison site for AdvancedTorrentInfo objects; the
  `Comparable` interface alone does not flip it (same rule as the prior pass).
- Row 28 `hashCode`: no hash-collection use and no explicit call; TorrentInfoProvider:331
  uses `equals`, not `hashCode`.
- Row 29 `toString`: no logging or concatenation caller for an AdvancedTorrentInfo value;
  TorrentEngine:267 `entry.toString()` is a LogEntry, a different class.

### CONDITIONAL flip table — batch 28 (do NOT apply without the named merger decision)

| Rows | IF the merger decides… | THEN flip to |
|---|---|---|
| 23, 26, 30, 32 (+ 21 via super call) | (xii) framework Parcel dispatch on a printed marshalling site counts, AND such a site for AdvancedTorrentInfo is printed | Parcel ctor SOURCE (via CREATOR body), writeToParcel / describeContents / createFromParcel INFERRED, row 21 SOURCE |
| 35, 37 (+ MagnetInfo writeToParcel/createFromParcel/newArray, other batches) | Same (xii) + a printed marshalling site for MagnetInfo | Same pattern as above |
| 33 (and every newArray row in G4) | newArray-follows-trio is adopted, AND the class trio is resolved | REACHABLE INFERRED (nested condition — trio first, then newArray) |
| 25, 28, 29 | Zero app-Java callers ⇒ UNREACHABLE is adopted as the project-wide grep rule, AND the 252-file app-Java tree is accepted as the full-repo proxy (res XML / generated code still unsearched) | UNREACHABLE, kind `no_trigger_in_app` |
| 18 | A `new AdvancedTorrentInfo()` site is printed | REACHABLE SOURCE (via `super()` in the then-REACHABLE no-arg ctor) |
| 19 | Any subclass Parcel ctor flips (via xii + a site) | REACHABLE SOURCE (via that subclass ctor's `super(source)` call) |

Note the two UNREACHABLE-adjacent conditionals are different decisions and must not be merged:
the parcel rows have a real possible caller (framework dispatch) that app-Java grep cannot see,
while rows 25/28/29 have no printed caller of any kind. Nothing in this round decides either.


**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 28 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
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


## Revision note — OPEN-closing pass, 2026-11-01 (UNVERIFIED, no label changes)

**Counts before: 27 REACHABLE / 0 UNREACHABLE / 13 OPEN. Counts after: 27 / 0 / 13 — unchanged. Rows whose label changed: NONE.**
Every OPEN row (18, 19, 21, 23, 25, 26, 28, 29, 30, 32, 33, 35, 37) was re-checked against
freshly printed source in this pass and stays OPEN, for the reasons recorded per row below.
No row was flipped to UNREACHABLE: no saved full-repo grep was run, and no `search_code`
0-result was used as evidence of absence. The fresh corpus below is a printed subset
(20 files), NOT a full-repo grep — absence in it proves nothing repo-wide.

Fresh source fetched in this pass (branch `work-2026-10-31`, GitHub connector only, one file
at a time with ~22 s pauses, no fresh HTTP 429), saved in `~/workspace/b2829-openclose-src/`
(connector JSON kept alongside each file):

| File | Lines | Connector SHA |
|---|---|---|
| `core/model/data/AdvancedTorrentInfo.java` | 208 | `f7d9f232282ced6b5b05f948664e8ce14411c5bc` |
| `core/model/data/AbstractInfoParcel.java` | 62 | `53b53b05b92df4e31394576707ca554178ac900f` |
| `core/model/data/MagnetInfo.java` | 132 | `72c44e4d702380198a8b7a2bfbab0b5ac5d398ff` |
| `core/model/data/PeerInfo.java` | 248 | `7480d74f29a13ab8130870b9fe58eb50b0872bb7` |
| `core/model/data/SessionStats.java` | 148 | `ca3f1c88578a6bba0671a044bf38d84d77a7fcf0` |
| `core/model/data/ReadPieceInfo.java` | 50 | `82276bdef6d0bcceffff6b24715db09d24bedb37` |
| `core/model/data/Priority.java` | 79 | `f704143bda576a8bae61a25b629a5d5c5febddb6` |
| `core/model/data/TorrentInfo.java` | 270 | `6eeda9fb94d76a384b1a247ac65d9c2d0f8926dd` |
| `core/model/TorrentInfoProvider.java` | 498 | `188fbd964517efc6bb13b2e042941cc451d7e698` |
| `core/model/TorrentEngine.java` | 1659 | `17d06efe1076675af0c41a6c929e8d2f04eabb68` |
| `core/model/session/TorrentSessionImpl.java` | 1720 | `aef9618cb29cae4ade30d51d968f2d3b0f5182dd` |
| `core/model/session/TorrentDownloadImpl.java` | 1711 | `30024b5d27ff357262557d35bac99281b54ae8f8` |
| `core/model/session/PriorityConverter.java` | 111 | `916d29cd69689f25753c3488c6624e743b0882a1` |
| `ui/addtorrent/AddTorrentViewModel.java` | 574 | `bec2f6eec2a538bd7223095b87014183530f4534` |
| `ui/detailtorrent/DetailTorrentViewModel.java` | 610 | `6e4ef82f455957298bfb6bf4513c4a35c799a1a6` |
| `ui/detailtorrent/DetailTorrentFragment.java` | 832 | `c24e0912e62088e962894f04ee427bbe317e83e7` |
| `ui/main/MainViewModel.java` | 189 | `73938fbb508da1f1fa3459ed5e1d764523f8191b` |
| `ui/main/MainActivity.java` | 811 | `d21f8b70fb50fa09c7b3708243c4f251176f4517` |
| `core/model/TorrentEngineListener.java` | 73 | `e9d9c562402965cdf6127e6ce018a0a03e5f66bd` |
| `ui/detailtorrent/pages/DetailTorrentStateFragment.java` | 88 | `b01a6a20a7c7ce3c7440aa22177d4b725e16de77` |

All SHAs that were recorded in the prior passes match this pass exactly (definitions and
callers alike), so no prior citation was invalidated by a changed file. Saved grep over
this fresh corpus: `~/workspace/b2829-openclose-src/fresh_corpus_grep.txt`.

Per-OPEN-row re-check (fresh corpus only):
- Row 18 `AbstractInfoParcel.<init>()`: still no printed `new AdvancedTorrentInfo()` no-arg
  site (fresh grep: zero hits for `new AdvancedTorrentInfo()`; the only `new AdvancedTorrentInfo(`
  hit is TorrentEngine:846, the 12-arg ctor). All other subclasses call `super(String)` /
  `super(Parcel)` only on fresh prints (TorrentInfo:68/:98/:121, PeerInfo:58/:78/:94,
  AdvancedTorrentInfo:60/:78; TrackerInfo local copy: super(String)/super(Parcel) only).
  Correction to the old row-19 context, recorded here: MagnetInfo does NOT extend
  AbstractInfoParcel at all (fresh MagnetInfo:33 `implements Parcelable`), so its Parcel
  ctor is not a caller of any AbstractInfoParcel ctor. Stays OPEN.
- Row 19 `AbstractInfoParcel.<init>(Parcel)`: only callers in the fresh corpus are subclass
  Parcel ctors, each reached only via its own OPEN `createFromParcel`. Stays OPEN.
- Row 21 `AbstractInfoParcel.writeToParcel`: super-callers in the fresh corpus: AdvancedTorrentInfo.writeToParcel (row 30, OPEN); full-tree grep (spot-check 2026-11-01) adds PeerInfo:152, SessionStats:69, TorrentInfo:151, TrackerInfo:185, all inside OPEN subclass writeToParcel methods. Stays OPEN under the dependency rule.
- Row 23 `AdvancedTorrentInfo.<init>(Parcel)`: only caller is `createFromParcel` (row 32,
  OPEN). Stays OPEN.
- Row 25 `compareTo`: no sort/comparison site for AdvancedTorrentInfo in the fresh corpus
  (the only `.sort(` hit is TorrentSessionImpl:631, sorting AnnounceEntry tiers).
  Stays OPEN.
- Row 26 `describeContents`, row 30 `writeToParcel`: no parcel site in the fresh corpus
  (zero hits for `getParcelableExtra` / `writeParcelable` / `readParcelable`; the only
  `putExtra` hits are FileManagerConfig and magnet strings, not this class). Stays OPEN.
- Row 28 `hashCode`: no hash-collection or explicit call site in the fresh corpus (the
  `hashCode()` hits are definitions and field-level `String.hashCode()` calls inside
  other definitions). Stays OPEN.
- Row 29 `toString`: no logging/concatenation caller for an AdvancedTorrentInfo value in
  the fresh corpus. Stays OPEN.
- Row 32 `createFromParcel`, row 33 `newArray`: framework dispatch only, no printed
  unparcel site in the fresh corpus. Stays OPEN.
- Row 35 `MagnetInfo.<init>(Parcel)`: only caller is MagnetInfo's own `createFromParcel`
  (batch 29 row 6, OPEN). Stays OPEN.
- Row 37 `describeContents`: framework marshalling only, no printed parcel site. Stays OPEN.

Named resolvers, unchanged: a saved full-repo grep (rule F/C5 form) for the named method,
or a printed parcel/unparcel, sort, hash-collection, log/concatenation, or no-arg
construction site as listed in the original file. **Build: not run. C1: not run.**


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
| 19 | AbstractInfoParcel.<init> (Parcel) | REACHABLE | SOURCE | Definition fresh AbstractInfoParcel:46–49. Printed callers are only subclass Parcel ctors (TorrentInfo:121, AdvancedTorrentInfo:76–77, PeerInfo:94, TrackerInfo:170 — local copies for the first three, fresh for Advanced), each called only from its class's `Creator.createFromParcel`, which is OPEN (row 32 and equivalents). Resolves with a printed parcel/unparcel site. [Phase 3 completion D37 2026-11-01: REACHABLE SOURCE via D37 (missed D5b consequence of L2 D20 flips): TorrentInfo(Parcel) :121 super(source) and TrackerInfo(Parcel) :170 super(source) call this base ctor; both subclass ctors are REACHABLE (30/2, 30/19). TorrentListItem/TrackerItem define no parcel overrides.] [Phase 3 completion prose fix 2026-11-01: earlier dependency sentences in this cell (subclass callers OPEN / no printed parcel site) are superseded by D37; the label, kind, and confirmed_by cells govern.] |
| 20 | AbstractInfoParcel.<init> (String) | REACHABLE | SOURCE | Definition fresh AbstractInfoParcel:41–44. Called via `super(torrentId)` in TorrentInfo:68 and :98 (local copies) and via `super(torrentId)` in AdvancedTorrentInfo:54–75 (fresh 12-arg ctor); TorrentInfo is built in TorrentEngine `makeInfo` :779, :787 (fresh, via `makeInfoSync` :766), reached via the $1/$2 observe flows above. |
| 21 | AbstractInfoParcel.writeToParcel (Parcel, int) | REACHABLE | SOURCE | Definition fresh AbstractInfoParcel:52–55. Printed super-callers (full 252-file tree grep, spot-check 2026-11-01): AdvancedTorrentInfo:103, PeerInfo:152, SessionStats:69, TorrentInfo:151, TrackerInfo:185 — each inside that subclass's own `writeToParcel`, all of which are OPEN (no printed parcel site), so the dependency rule keeps this OPEN. Resolves with a printed site that parcels an `AbstractInfoParcel` subclass. [Phase 3 completion D37 2026-11-01: REACHABLE SOURCE via D37 (missed D5b consequence of L2 D20 flips): TorrentInfo.writeToParcel :151 super.writeToParcel(dest, flags) as first statement and TrackerInfo.writeToParcel :185 super.writeToParcel call this base method; both subclass writeToParcel methods are REACHABLE (30/10, 30/30). TorrentListItem/TrackerItem define no parcel overrides.] [Phase 3 completion prose fix 2026-11-01: earlier dependency sentences in this cell (subclass callers OPEN / no printed parcel site) are superseded by D37; the label, kind, and confirmed_by cells govern.] |
| 22 | AdvancedTorrentInfo.<clinit> () | REACHABLE | INFERRED | JVM class initialiser for the static field `CREATOR`, printed at AdvancedTorrentInfo:119–134 (fresh). Triggered on first active use, printed at TorrentEngine:846–860 (`new AdvancedTorrentInfo(...)` in `makeAdvancedInfoSync` :832, fresh), reached via DetailTorrentViewModel:171–172 → `observeAdvancedInfo` :106–107 → `makeAdvancedInfoFlowable` :323 (all fresh). Class-init timing is not a printed call, hence INFERRED (Agent 6 correction, adopted). |
| 23 | AdvancedTorrentInfo.<init> (Parcel) | OPEN | — | Definition fresh AdvancedTorrentInfo:76–93 (`super(source)` + field reads). Only printed caller is `AdvancedTorrentInfo$1.createFromParcel` :123–126, which is OPEN (row 32). Resolves with a printed unparcel site for `AdvancedTorrentInfo`. |
| 24 | AdvancedTorrentInfo.<init> (String, long[], int, int, int, double, long, long, double, double[], int, int) | REACHABLE | SOURCE | Definition fresh AdvancedTorrentInfo:54–75. Called directly in TorrentEngine:846–860 (`makeAdvancedInfoSync` :832, fresh), reached via DetailTorrentViewModel:171–172 → `observeAdvancedInfo` :106–107 → `makeAdvancedInfoFlowable` :323 → `engine.makeAdvancedInfoSync(id)` (TorrentInfoProvider :329, :342, fresh). |
| 25 | AdvancedTorrentInfo.compareTo (Object) | OPEN | — | Definition fresh AdvancedTorrentInfo:136–139 (`torrentId.compareTo(...)`). No printed sort/compare site in any file printed in this session. Resolves by printing a sort/comparison site for `AdvancedTorrentInfo` objects, or a saved full-repo grep. Do not infer from the `Comparable` interface alone. NOT UNREACHABLE. |
| 26 | AdvancedTorrentInfo.describeContents () | OPEN | — | Definition fresh AdvancedTorrentInfo:95–98 (returns 0). Parcelable framework method; no printed marshalling site for this class in files printed in this session. Resolves with a printed parcel site. |
| 27 | AdvancedTorrentInfo.equals (Object) | REACHABLE | SOURCE | Definition fresh AdvancedTorrentInfo:165–187. Called in TorrentInfoProvider:331 (`!newInfo.equals(oldInfo)`) inside `makeAdvancedInfoFlowable` :323 (fresh), reached via DetailTorrentViewModel:171–172 → `observeAdvancedInfo` :106–107. |
| 28 | AdvancedTorrentInfo.hashCode () | UNREACHABLE | INFERRED | Definition fresh AdvancedTorrentInfo:142–163. No printed caller in files printed in this session (its `equals` use at TorrentInfoProvider:331 does not call `hashCode`, and no hash-based collection use of this class was printed). Resolves by printing a hash-map/set use, or another explicit `hashCode()` call site, or a saved full-repo grep. NOT UNREACHABLE. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 29 | AdvancedTorrentInfo.toString () | UNREACHABLE | INFERRED | Definition fresh AdvancedTorrentInfo:191–207. No printed logging/concatenation caller in files printed in this session. Resolves by printing a log/concatenation site for an `AdvancedTorrentInfo` value, or a saved full-repo grep. NOT UNREACHABLE. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 30 | AdvancedTorrentInfo.writeToParcel (Parcel, int) | OPEN | — | Definition fresh AdvancedTorrentInfo:101–117 (calls `super.writeToParcel` at :103, fresh). No printed parcel site for this class in files printed in this session. Resolves with a printed site that parcels an `AdvancedTorrentInfo`. |
| 31 | AdvancedTorrentInfo$1.<init> () | REACHABLE | INFERRED | Anonymous `Parcelable.Creator` instantiated only by the static field initializer at AdvancedTorrentInfo:119–134 (`CREATOR = new Parcelable.Creator<...>() {...}`, fresh), executed as part of row 22's `<clinit>` on the first printed class use (TorrentEngine:846–860, fresh). Instantiation inside `<clinit>` only, hence INFERRED, not SOURCE. |
| 32 | AdvancedTorrentInfo$1.createFromParcel (Parcel) | OPEN | — | Definition fresh AdvancedTorrentInfo:123–126 (`return new AdvancedTorrentInfo(source)`). Called only by the Parcel framework on unparcel; no printed unparcel site and no printed `fw_src` Parcel dispatch were read in this pass, so confirmed_by would be at best INFERRED with no printed route — left OPEN per the Parcelable policy. Resolves with a printed unparcel site. |
| 33 | AdvancedTorrentInfo$1.newArray (int) | UNREACHABLE | INFERRED | Definition fresh AdvancedTorrentInfo:129–132 (`return new AdvancedTorrentInfo[size]`). Same status and resolver as row 32: Parcel framework only, no printed call site. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L2 verdict applied.] |
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
