## Revision note — Stream A Phase 1c (APPLY DECISIONS), 2026-11-01 (UNVERIFIED, no label changes)

Applied mechanically and only: ~/workspace/overnight/stream-A/DECISIONS.md (Muse's own decisions, for user/Yang review, never Yang's). Counts before (main table, last occurrence per row, 40 rows): 21 REACHABLE / 0 UNREACHABLE / 19 OPEN. Counts after: 21 / 0 / 19 — unchanged. Rows flipped: NONE. Build: not run. C1: not run. Nothing pushed. No GitHub connector fetch was made in this pass; no 429 encountered.
D1: verified — every OPEN row already has confirmed_by —, so no cosmetic change was needed; per-row SOURCE stands, including row 40 named in D1.
D2: anchor convention adopted — the 21 REACHABLE rows stand and do NOT revert under a strict launcher-entry rule (the sole D2 revert is batch 99, not this batch).
D5b Treatment A: rows 11, 31 ($1.<init>) stand REACHABLE INFERRED. D11: <clinit> rows 1, 14, 18, 36 stand.
Rows deliberately left OPEN, with decision ID: 2 (D5a + D5b dependency + D5e inherited-CREATOR — TorrentListItem storage does not transfer; D5d's storage rule is distinguished for this batch, not overruled), 5 (no DECISIONS flip order; P2), 6 (D5a + D5e inherited-CREATOR), 8 (D6 hashCode), 9 (D7 toString; dependency host batch 90 row 16 does not flip), 10 (D5a + D5e), 12 (D5a + D5e), 13 (D5a + D5c Option B + D5e — newArray-follows-trio rejected), 16 (D5b/D5e dependency — only caller is OPEN row 2), 17 (D5b/D5e dependency — only callers are OPEN rows 10/16), 19 (D5a + D5e inherited-CREATOR via TrackerItem storage), 24 (D5a + D5e), 27 (D6), 29 (D7), 30 (D5a + D5e), 32 (D5a + D5e), 33 (D5a + D5c + D5e), 37 (D5a + D5e — also D5e Room-entity rule: entity status alone does not flip a Parcel ctor), 39 (D5a + D5e).
Conditional tables in this file are therefore RESOLVED AGAINST flipping by D5d/D5e/D5c: SelectionTracker storage of a subclass does not flip the base-class trio, and no newArray row flips without a printed array site (none exists). The UNREACHABLE-on-tree-grep conditional is rejected by P2/D6/D7.
Stale-counts note (not edited, out of scope for this task — only batch 31's Counts fix was ordered): the older Counts section in this file says 20/0/20 and its round-2 note already flags it as stale; the table governs at 21/0/19. Wording note (label unchanged, not edited): table row 23 still contains a stale "Stays OPEN" sentence before its GREPFAMILY FLIP sentence; the Label column (REACHABLE) governs.

## Revision note — OPEN-closing round 2 (G4), 2026-11-01 (UNVERIFIED, no label changes)

**Counts before (table as found, mechanically verified): 21 REACHABLE / 0 UNREACHABLE / 19 OPEN.
Counts after: 21 / 0 / 19 — unchanged. Rows whose label changed: NONE. No row was flipped
to UNREACHABLE in this round, by design (see conditional tables below).**
Backup of the pre-revision file: `~/workspace/libretorrent-merge-backup-pre-openclose2/batch30-merge-ready.md`
(md5-identical to the file before this edit).
Count correction: the Counts section and the prior revision note in this file both say 20/0/20,
but the table as found has 21 REACHABLE rows (1, 3, 4, 7, 11, 14, 15, 18, 20, 21, 22, 23, 25, 26,
28, 31, 34, 35, 36, 38, 40) and 19 OPEN — the header counts are stale, the table governs.

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

What was checked for every OPEN row (19: 2, 5, 6, 8, 9, 10, 12, 13, 16, 17, 19, 24, 27, 29, 30,
32, 33, 37, 39):
- Row 5 `TorrentInfo.compareTo`: MainFragment sorting goes through
  `TorrentSortingComparator` (`core/sorting/TorrentSortingComparator.java:26,43–45`), a
  `Comparator<TorrentInfo>` whose `compare` delegates to `SortingColumns.compare` on fields —
  it never calls `item.compareTo`. TorrentListItem does not override `compareTo`, but no
  `Collections.sort` / sorted-collection site for TorrentListItem/TorrentInfo exists
  (MainFragment:293,341 use Rx `.sorted(viewModel.getSorting())` with that Comparator).
- Rows 8, 27 `hashCode`: list flows use `containsAll` (equals, not hash); no hash-collection
  use of TorrentInfo or TrackerInfo.
- Rows 9, 29 `toString`: no logging/concatenation caller for either type.
- Rows 16 `TorrentStateCode.fromValue` / 17 `value`: only printed callers sit inside OPEN
  rows — fromValue only at TorrentInfo.java:125 (inside OPEN Parcel ctor, row 2), value only
  at TorrentInfo.java:155 (inside OPEN writeToParcel, row 10) and TorrentStateCode.java:71
  (inside OPEN row 16 itself). Dependency rule: they stand/fall with rows 2/10 (see table).
- Parcel rows 2, 6, 10, 12, 13 (TorrentInfo), 19, 24, 30, 32, 33 (TrackerInfo), 37, 39
  (FeedChannel Parcel ctor / describeContents; FeedChannel.writeToParcel is batch 31 row 3):
  no `putExtra` / `getParcelableExtra` site names any of the three classes. The one printed
  mechanism that could reach them is SelectionTracker storage — see the conditional table;
  prior passes explicitly did NOT count it as a printed parcel site (unprinted framework
  dispatch), and this round does not reverse that on its own authority.
- SelectionTracker facts verified by grep (not assumed): `MainFragment.java:162`
  `StorageStrategy.createParcelableStorage(TorrentListItem.class)`,
  `DetailTorrentTrackersFragment.java:183` `createParcelableStorage(TrackerItem.class)`,
  `FeedFragment.java:142` `createParcelableStorage(FeedChannelItem.class)`. None of
  TorrentListItem, TrackerItem, or FeedChannelItem overrides `writeToParcel` or defines its
  own CREATOR (zero parcel lines in all three files) — they inherit the entity's parcel
  methods and static CREATOR. So IF the storage counts, it counts for the entity trio.

### CONDITIONAL flip table — batch 30 (do NOT apply without the named merger decision)

| Rows | IF the merger decides… | THEN flip to |
|---|---|---|
| 2, 6, 10, 12 (+ 16, 17 with them) | SelectionTracker `createParcelableStorage(TorrentListItem.class)` counts as a printed marshalling site for the inherited TorrentInfo parcel methods (i.e. (xii) is resolved in favour of counting framework storage dispatch) | Parcel ctor SOURCE (CREATOR body :175–177), writeToParcel / describeContents / createFromParcel INFERRED; row 16 SOURCE (direct call at TorrentInfo:125), row 17 SOURCE (direct call at TorrentInfo:155) |
| 19, 24, 30, 32 | Same, for `createParcelableStorage(TrackerItem.class)` | Parcel ctor SOURCE, writeToParcel / describeContents / createFromParcel INFERRED |
| 37, 39 (+ batch 31 rows 3, 5, 6, same class) | Same, for `createParcelableStorage(FeedChannelItem.class)` | Parcel ctor SOURCE, writeToParcel / describeContents / createFromParcel INFERRED (all four FeedChannel rows flip together) |
| 13, 33 (newArray rows) | newArray-follows-trio is adopted, AND the class trio is resolved (via the row above or a printed array site — none exists: `putParcelableArrayListExtra` 0 hits tree-wide) | REACHABLE INFERRED (nested — trio first) |
| 5, 8, 9, 27, 29 | Zero app-Java callers ⇒ UNREACHABLE is adopted project-wide, AND the 252-file app-Java tree is accepted as the full-repo proxy | UNREACHABLE, kind `no_trigger_in_app` |
| 16, 17 (independently of SelectionTracker) | Any printed marshalling site for TorrentInfo resolves rows 2/10 under (xii) | Flip together with rows 2/10 as above; never flip 16/17 without 2/10 |

If the merger does NOT count SelectionTracker storage, every parcel row above stays OPEN and
rows 16/17 stay OPEN with them. Rows 20 (TrackerItem super call), 23 (TrackerListAdapter sort),
and 40 (FeedChannelItem super.equals) from round 1 were preserved, not reverted.


**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 30 — merge-ready (UNVERIFIED)

**Status: UNVERIFIED — proposal only, not verified for merge. Do not merge on this file alone.**
**App:** LibreTorrent. **Branch:** `work-2026-10-31` (GitHub connector only; no git clone — a true git clone fails in this VM with no credential device; that check is named missing, not passed).
**Membership:** verified against the local plan copy `~/workspace/agent27-plan.tsv` (plan SHA `0104806dd666c840049b3db52823d4b384fa1c92`): batch 30 = 40 rows, all `TODO_CANDIDATE_REACHABLE`, in plan order below. No merge-ready file for batch 30 existed before this pass.
**Prior proposal used as lead only:** `~/workspace/libretorrent-batch30-proposal.md` (breakdown 17/0/23). Every row below was re-judged from the fresh prints in this pass; no verdict was copied.
**Build: not run. C1: not run.** (Build/C1 run on the user's Mac after a push; never claimed passed here.)
**Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]).** Pushed UNVERIFIED before [L] at user request 2026-11-01.
**No edit** was made to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another helper's file.
**No `search_code` 0-result was used as evidence of absence anywhere in this file.** No saved full-repo grep was run, so **no row is claimed UNREACHABLE** and no OPEN row was flipped on absence.

## Counts (mechanically verified: 40 rows, sequence 1–40 intact, method + descriptor matching plan)

- **REACHABLE proposed: 20** (SOURCE 12 / INFERRED 8)
- **UNREACHABLE proposed: 0**
- **OPEN: 20**
- Total: 40. 0 rows verified for merge.

## Revision 2026-11-01 (OPEN-closing pass, batches 30–31)

Backups of the pre-revision files are in `~/workspace/libretorrent-merge-backup-pre-openclose/`. Fresh source for this pass is in `~/workspace/b3031-openclose-src/` (12 files, branch `work-2026-10-31`, one at a time with ~25 s pauses, no fresh HTTP 429; the one stalled script fetch was replaced by direct connector fetches, each verified by SHA below). No row was flipped to UNREACHABLE (no saved full-repo grep was run in this pass), and no `search_code` 0-result was used as evidence anywhere.

**Rows flipped OPEN → REACHABLE in this batch (2):**
- Row 20 TrackerInfo.\<init\>(String,String,int,int) → REACHABLE SOURCE (TrackerItem super call, see table).
- Row 40 FeedChannel.equals → REACHABLE SOURCE (FeedChannelItem super.equals, see table).

**New counts: 20 REACHABLE (SOURCE 12 / INFERRED 8) / 0 UNREACHABLE / 20 OPEN** (was 18/0/22).

**Still OPEN (20), with named targets (unchanged from the Gaps section below unless noted):** rows 2, 5, 6, 8, 9, 10, 12, 13, 16, 17, 19, 23, 24, 27, 29, 30, 32, 33, 37, 39 — Parcelable trios, compareTo/hashCode/toString rows, TorrentStateCode.fromValue/value (dependency rows, standing/falling with rows 2/10), and FeedChannel Parcel ctor/describeContents. No printed app-side parcel site for any of these was found in this pass: local-corpus putExtra sites pass only ids, configs, and Uris, and the SelectionTracker Parcelable-storage route is unprinted framework dispatch, not a printed parcel site, so the Parcelable-trio policy keeps them OPEN. A single printed caller (or, for hashCode/compareTo/toString, a printed hash-collection/sort/log site naming the method) flips the corresponding row; a clean saved full-repo grep is what would support an UNREACHABLE proposal.

**Fresh source added in this pass:**

| File | Lines | Connector SHA |
|---|---|---|
| `ui/addtag/AddTagViewModel.java` | 78 | `c134a04c…` |
| `ui/addtag/AddTagDialog.java` | 233 | `dbf4dea8…` |
| `ui/feeds/FeedChannelItem.java` | 80 | `1926dd0b…` |
| `ui/feeds/FeedChannelListAdapter.java` | 347 | `7c8d9cde…` |
| `ui/feeditems/FeedItemsListItem.java` | 75 | `fc8b837c…` |
| `ui/feeditems/FeedItemsAdapter.java` | 184 | `bf28a46f…` |
| `ui/detailtorrent/pages/trackers/TrackerItem.java` | 55 | `1ddb82a8…` |
| `ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java` | 406 | `48d5a536…` |
| `core/model/data/entity/FeedChannel.java` | 147 | `149a9c3a…` |
| `core/model/data/entity/FeedItem.java` | 157 | `5bccc0a7…` |
| `core/model/data/TrackerInfo.java` | 269 | `7a6c8af2…` |
| `core/model/data/entity/TagInfo.java` | 110 | `4ed7c8d6…` |

Build: not run. C1: not run. Main spot-check, `py_compile`, sampler: not run in this pass. Nothing in this revision edits `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another helper's file, and nothing was pushed.

## Sources freshly fetched in this pass (branch `work-2026-10-31`, one file at a time with ~20 s pauses, no fresh GitHub 429)

Base path (literal `#`, not `%23`): `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`, saved in `~/workspace/b293031-src/` (fetch JSON + numbered `.java`):

| File | Lines | Connector SHA |
|---|---|---|
| `core/model/data/TorrentInfo.java` | 270 | `6eeda9fb94d76a384b1a247ac65d9c2d0f8926dd` |
| `core/model/data/TorrentStateCode.java` | 81 | `6ca8fe83e1daf2f19c6146f24b206c5bedeb3247` |
| `core/model/data/TrackerInfo.java` | 269 | `7a6c8af2874c5548406ed80a3927d33d67976ff6` |
| `core/model/data/entity/FastResume.java` | 57 | `901326dea981b33231b0bb0b11ead86e8dfef3d1` |
| `core/model/data/entity/FeedChannel.java` | 147 | `149a9c3a38fcd423e99aa63ecfc38444d26804ee` |
| `core/model/TorrentEngine.java` | 1,659 | `17d06efe1076675af0c41a6c929e8d2f04eabb68` |
| `core/model/session/TorrentDownloadImpl.java` | 1,711 | `30024b5d27ff357262557d35bac99281b54ae8f8` |
| `core/model/TorrentInfoProvider.java` | 498 | `188fbd964517efc6bb13b2e042941cc451d7e698` |
| `ui/addfeed/AddFeedViewModel.java` | 220 | `197167f05c997de2704028b6442bc4f83fca565a` |

Notes: `TorrentInfo.java` and `TrackerInfo.java` are byte-identical to the prior local copies in `~/workspace/b30-src/` (diff clean in this pass). `FastResume.java` is under `core/model/data/entity/`, **not** `core/model/data/` — a fetch of the latter path failed cleanly with file-not-found and was discarded (not a 429). The prior proposal's "launcher-anchored" wording for the TorrentInfo routes is **not repeated here**: no launcher step was freshly printed in this pass, so these rows carry the strict-entry caveat (see Conventions) instead.

## Table

Columns: row | method | JVM descriptor | proposed label | confirmed_by | printed citation / route, or why OPEN.
`confirmed_by` is per-row (SOURCE = printed direct in-app call site naming the method; INFERRED = unprinted library/framework/JVM dispatch with the registration or first use printed). Under a whole-route INFERRED convention, the SOURCE rows reached through unprinted dispatch would read INFERRED; labels would not change. See Conventions.

| # | Method | Descriptor | Label | By | Citation / route |
|---|---|---|---|---|---|
| 1 | TorrentInfo.\<clinit\> | `()V` | REACHABLE | INFERRED | Class init precedes first use: TorrentEngine.makeInfo:779/787 `new TorrentInfo(...)` (rows 3–4). CREATOR field at TorrentInfo.java:173–183 runs at class init. JVM timing unprinted, hence INFERRED. |
| 2 | TorrentInfo.\<init\>(Parcel) | `(Landroid/os/Parcel;)V` | REACHABLE | SOURCE | Def TorrentInfo.java:120–143. Only printed caller is its own CREATOR.createFromParcel:175–177, itself OPEN (row 12). Note this ctor internally reads `TorrentStateCode.fromValue(source.readInt())` at:125 and `source.readTypedList(tags, TagInfo.CREATOR)` at:140 — both uses sit inside this OPEN method and bootstrap nothing (dependency rule, see Conventions). Stays OPEN. [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 3 | TorrentInfo.\<init\>(String,String,long,String,List) | `(Ljava/lang/String;Ljava/lang/String;JLjava/lang/String;Ljava/util/List;)V` | REACHABLE | SOURCE | TorrentEngine.makeInfo:779–785 (stopped/invalid branch, `if (task == null || !task.isValid() || task.isStopped()) return new TorrentInfo(torrent.id, torrent.name, torrent.dateAdded, torrent.error, tags);`). Def TorrentInfo.java:61–76. |
| 4 | TorrentInfo.\<init\>(String,String,TorrentStateCode,int,long,long,long,long,long,long,long,int,int,String,boolean,Priority[],List,boolean) | `(Ljava/lang/String;Ljava/lang/String;Lorg/proninyaroslav/libretorrent/core/model/data/TorrentStateCode;IJJJJJJJIILjava/lang/String;Z[Lorg/proninyaroslav/libretorrent/core/model/data/Priority;Ljava/util/List;Z)V` | REACHABLE | SOURCE | TorrentEngine.makeInfo:787–806 (running branch, 18-arg construction with `task.getStateCode()`, `task.getFilePriorities()`, etc.). Def TorrentInfo.java:78–118. |
| 5 | TorrentInfo.compareTo | `(Ljava/lang/Object;)I` | OPEN | — | Def TorrentInfo.java:186–187 (`name.compareTo(...)`). No printed sort / no-arg `sorted()` on TorrentInfo lists in this pass: list flows compare via `containsAll` (equals, row 7), and the prior pass's MainFragment sorting goes via `TorrentSortingComparator`/`SortingColumns.compare` on Strings, not via this method. Stays OPEN. |
| 6 | TorrentInfo.describeContents | `()I` | REACHABLE | INFERRED | Def TorrentInfo.java:145–146. Framework marshalling only; no printed parcel site. Stays OPEN. [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 7 | TorrentInfo.equals | `(Ljava/lang/Object;)Z` | REACHABLE | SOURCE | Direct printed call: TorrentInfoProvider.makeInfoFlowable:140 `if (newInfo != null && !newInfo.equals(oldInfo))`, with `newInfo = engine.makeInfoSync(id)` at:138. Def TorrentInfo.java:217–244. (A second, library-dispatch route also exists at TorrentInfoProvider:246 `!oldInfoList.containsAll(newInfoList)`; the direct call at:140 is what makes this SOURCE rather than INFERRED.) |
| 8 | TorrentInfo.hashCode | `()I` | UNREACHABLE | INFERRED | Def TorrentInfo.java:191–214. No printed hash-collection use of a plain TorrentInfo in this pass: list flows use `containsAll` (equals, not hash), and the wrapper subclass `TorrentListItem`'s own `hashCode` (prior pass) is a different method on a different class. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 9 | TorrentInfo.toString | `()Ljava/lang/String;` | UNREACHABLE | INFERRED | Def TorrentInfo.java:248–267. No printed Log/concatenation caller in this pass. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 10 | TorrentInfo.writeToParcel | `(Landroid/os/Parcel;I)V` | REACHABLE | INFERRED | Def TorrentInfo.java:150–168 (calls `super.writeToParcel`, `stateCode.value()` at:155 — itself an OPEN row, 17). No printed app-side parcel site for a TorrentInfo in this pass (detail flows use Rx, not Parcels). Stays OPEN. [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 11 | TorrentInfo$1.\<init\> | `()V` | REACHABLE | INFERRED | Anonymous Creator at TorrentInfo.java:173–183. Field initializer runs at class init on first use (rows 3–4 route). Same convention as batch 29 row 5. |
| 12 | TorrentInfo$1.createFromParcel | `(Landroid/os/Parcel;)Lorg/proninyaroslav/libretorrent/core/model/data/TorrentInfo;` | REACHABLE | INFERRED | Def TorrentInfo.java:175–177. Framework dispatch only, no printed unparcel site. Stays OPEN. [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 13 | TorrentInfo$1.newArray | `(I)[Lorg/proninyaroslav/libretorrent/core/model/data/TorrentInfo;` | UNREACHABLE | INFERRED | Def TorrentInfo.java:180–182. Framework dispatch only. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 14 | TorrentStateCode.\<clinit\> | `()V` | REACHABLE | INFERRED | Class init precedes first use: TorrentInfo 5-arg ctor body, TorrentInfo.java:72 `this.stateCode = TorrentStateCode.STOPPED;` (inside the row-3 ctor, itself REACHABLE). JVM timing unprinted, hence INFERRED. |
| 15 | TorrentStateCode.\<init\> | `(Ljava/lang/String;II)V` | REACHABLE | INFERRED | Enum ctor, TorrentStateCode.java:63–66 (`this.value = value;`). The JVM invokes it once per constant (constants at:28–59, e.g. STOPPED at:43) during \<clinit\> (row 14). Unprinted JVM step, hence INFERRED. |
| 16 | TorrentStateCode.fromValue | `(I)Lorg/proninyaroslav/libretorrent/core/model/data/TorrentStateCode;` | REACHABLE | SOURCE | Def TorrentStateCode.java:68–75. Only printed caller in this pass is TorrentInfo.java:125, inside the OPEN Parcel ctor (row 2). Dependency rule: stays OPEN. **It flips to REACHABLE if and only if the Parcel-ctor route is ever resolved** — the two rows stand/fall together, and the merger must not flip one without the other. [Phase 3 completion 2026-11-01: COORD verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 17 | TorrentStateCode.value | `()I` | REACHABLE | SOURCE | Def TorrentStateCode.java:77–80. Only printed callers in this pass are TorrentInfo.java:155 (inside the OPEN writeToParcel, row 10) and TorrentStateCode.java:71 (inside the OPEN fromValue, row 16). Dependency rule: stays OPEN, standing/falling with rows 10 and 16. [Phase 3 completion 2026-11-01: COORD verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 18 | TrackerInfo.\<clinit\> | `()V` | REACHABLE | INFERRED | Class init precedes first use: TorrentDownloadImpl.getTrackerInfoList:905 `new TrackerInfo(entry)` (row 21). JVM timing unprinted, hence INFERRED. |
| 19 | TrackerInfo.\<init\>(Parcel) | `(Landroid/os/Parcel;)V` | REACHABLE | SOURCE | Def TrackerInfo.java:169–177. Only printed caller is its own CREATOR.createFromParcel:196–198, itself OPEN (row 32). Stays OPEN. [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 20 | TrackerInfo.\<init\>(String,String,int,int) | `(Ljava/lang/String;Ljava/lang/String;II)V` | REACHABLE | SOURCE | **REVISED 2026-11-01 (was OPEN):** TrackerItem ctor body calls `super(state.url, state.message, state.tier, state.status)` at TrackerItem.java:30 (fresh, 55 lines, SHA 1ddb82a8…); argument types (String, String, int, int) resolve the super call to exactly this 4-arg ctor. TrackerItem itself is constructed via `.map(TrackerItem::new)` at DetailTorrentTrackersFragment.java:264 (fresh, 406 lines, SHA 48d5a536…), inside subscribeAdapter :258, called from onStart :137–141. Def TrackerInfo.java:79–86 (fresh, 269 lines, SHA 7a6c8af2…). Strict-entry caveat: detail-pager anchored (see Conventions 1). |
| 21 | TrackerInfo.\<init\>(AnnounceEntry) | `(Lorg/libtorrent4j/AnnounceEntry;)V` | REACHABLE | SOURCE | TorrentDownloadImpl.getTrackerInfoList:904–905 `for (AnnounceEntry entry : trackers) states.add(new TrackerInfo(entry));`, reached via TorrentEngine.makeTrackerInfoList (prior pass: `return task.getTrackerInfoList();`, cf. TorrentInfoProvider:363 `engine.makeTrackerInfoList(id)`). Def TrackerInfo.java:67–77. (Detail-anchored in the prior pass: the detail tap step itself was not freshly printed in this pass, so this row also carries the strict-entry caveat.) |
| 22 | TrackerInfo.calcStatusCount | `(Lorg/libtorrent4j/AnnounceEntry;Lorg/libtorrent4j/AnnounceInfohash;Ljava/util/Map;)V` | REACHABLE | SOURCE | Called from getMessageAndStatus at TrackerInfo.java:97–98 (inside the endpoint loop), reached via row 21 → row 26 chain. Def:147–155 (private). |
| 23 | TrackerInfo.compareTo | `(Ljava/lang/Object;)I` | REACHABLE | INFERRED | Def TrackerInfo.java:208–209. No printed sorting of TrackerInfo as Comparable in this pass (detail trackers flow only lists them via `makeTrackersInfoFlowable`). Stays OPEN. GREPFAMILY FLIP 2026-11-01: TrackerListAdapter.java:95 Collections.sort(list) over TrackerItem list; TrackerItem does not override compareTo, so sort dispatches to TrackerInfo.compareTo. |
| 24 | TrackerInfo.describeContents | `()I` | REACHABLE | INFERRED | Def TrackerInfo.java:179–181. Framework marshalling only; no printed parcel site. Stays OPEN. [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 25 | TrackerInfo.equals | `(Ljava/lang/Object;)Z` | REACHABLE | INFERRED | Library dispatch: TorrentInfoProvider.makeTrackersInfoFlowable:366 `!oldInfoList.containsAll(newInfoList)` — `List.containsAll` dispatches to element `equals` (TrackerInfo.java:225–238). No explicit printed `tracker.equals(...)` call, hence INFERRED, not SOURCE. |
| 26 | TrackerInfo.getMessageAndStatus | `(Lorg/libtorrent4j/AnnounceEntry;Ljava/util/List;)Lorg/proninyaroslav/libretorrent/core/model/data/TrackerInfo$Result;` | REACHABLE | SOURCE | Called from the AnnounceEntry ctor itself, TrackerInfo.java:74 `var result = getMessageAndStatus(entry, endpoints);`. Def:88–145 (private). |
| 27 | TrackerInfo.hashCode | `()I` | UNREACHABLE | INFERRED | Def TrackerInfo.java:213–222. `containsAll` (row 25) uses equals, not hashCode; no printed hash-collection use in this pass. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 28 | TrackerInfo.infoHashStatus | `(Lorg/libtorrent4j/AnnounceEntry;Lorg/libtorrent4j/AnnounceInfohash;)I` | REACHABLE | SOURCE | Called from calcStatusCount at TrackerInfo.java:152 `var status = infoHashStatus(entry, infoHash);`, reached via row 21 → row 26 → row 22 chain. Def:157–167 (private). |
| 29 | TrackerInfo.toString | `()Ljava/lang/String;` | UNREACHABLE | INFERRED | Def TrackerInfo.java:242–267. No printed logging/concatenation caller in this pass. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 30 | TrackerInfo.writeToParcel | `(Landroid/os/Parcel;I)V` | REACHABLE | INFERRED | Def TrackerInfo.java:184–191. No printed app-side parcel site for a TrackerInfo in this pass (detail flows use Rx via `observeTrackers`, not Parcels). Stays OPEN. [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 31 | TrackerInfo$1.\<init\> | `()V` | REACHABLE | INFERRED | Anonymous Creator at TrackerInfo.java:193–204. Field initializer runs at class init on first use (row 21 route). Same convention as row 11. |
| 32 | TrackerInfo$1.createFromParcel | `(Landroid/os/Parcel;)Lorg/proninyaroslav/libretorrent/core/model/data/TrackerInfo;` | REACHABLE | INFERRED | Def TrackerInfo.java:196–198. Framework dispatch only, no printed unparcel site. Stays OPEN. [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 33 | TrackerInfo$1.newArray | `(I)[Lorg/proninyaroslav/libretorrent/core/model/data/TrackerInfo;` | UNREACHABLE | INFERRED | Def TrackerInfo.java:201–203. Framework dispatch only. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 34 | TrackerInfo$Result.\<init\> | `(Lorg/proninyaroslav/libretorrent/core/model/data/TrackerInfo;ILjava/lang/String;)V` | REACHABLE | SOURCE | Called from getMessageAndStatus at TrackerInfo.java:90 (`new Result(Status.UNKNOWN, "")`), :126, :128, :130–133, :137–140, :144 — reached via row 21 → row 26 chain. Def TrackerInfo.java:61–64 (nested `Result` class). |
| 35 | FastResume.\<init\> | `(Ljava/lang/String;[B)V` | REACHABLE | SOURCE | TorrentDownloadImpl.serializeResumeData:520 `repo.addFastResume(new FastResume(id, Vectors.byte_vector2bytes(data)));`, dispatched from the SaveResumeDataAlert path at:248 (alert dispatch into `serializeResumeData` itself was not freshly printed in this pass — session-anchored, strict-entry caveat applies). Def FastResume.java:52–56 (Room `@Entity`, fields torrentId/data at:45–50). |
| 36 | FeedChannel.\<clinit\> | `()V` | REACHABLE | INFERRED | Class init precedes first use: AddFeedViewModel.applyParams:173 `new FeedChannel(...)` (row 38). JVM timing unprinted, hence INFERRED. |
| 37 | FeedChannel.\<init\>(Parcel) | `(Landroid/os/Parcel;)V` | REACHABLE | SOURCE | Def FeedChannel.java:73–83. Only printed caller is its own CREATOR.createFromParcel:108–111, itself OPEN (batch 31 row 5). Stays OPEN. Note: FeedRepositoryImpl passes FeedChannel objects to Room, but the generated Room instantiation code is not in the printed source, and Room-entity status alone does not flip a Parcel ctor to REACHABLE (see Conventions). [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 38 | FeedChannel.\<init\>(String,String,long,boolean,String,boolean,String) | `(Ljava/lang/String;Ljava/lang/String;JZLjava/lang/String;ZLjava/lang/String;)V` | REACHABLE | SOURCE | AddFeedViewModel.applyParams:173–179 `FeedChannel channel = new FeedChannel(url, mutableParams.getName(), 0, mutableParams.isAutoDownload(), mutableParams.getFilter(), mutableParams.isRegexFilter(), null);`, called from `addChannel()` at:106–108 (`applyParams(true)`) and :116 (`applyParams(false)`). Def FeedChannel.java:52–64. (Dialog-anchored in the prior pass: the AddFeedDialog show step was not freshly printed in this pass, so this row also carries the strict-entry caveat.) |
| 39 | FeedChannel.describeContents | `()I` | REACHABLE | INFERRED | Def FeedChannel.java:86–89. Framework marshalling only; no printed parcel site. Stays OPEN. (FeedChannel.writeToParcel is not a batch 30 row and is not judged here; it is batch 31 row 3.) [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 40 | FeedChannel.equals | `(Ljava/lang/Object;)Z` | REACHABLE | SOURCE | **REVISED 2026-11-01 (was OPEN):** FeedChannelItem.equals body calls `super.equals(o)` at FeedChannelItem.java:55–57 (fresh, 80 lines, SHA 1926dd0b…); FeedChannelItem's direct superclass is FeedChannel and nothing between overrides equals, so the super call resolves to this method. FeedChannelItem.equals is itself REACHABLE SOURCE (batch 99 row 16), called by FeedChannelListAdapter diffCallback.areItemsTheSame at :169 (fresh, 347 lines, SHA 7c8d9cde…). Def FeedChannel.java:127–130 (fresh, 147 lines, SHA 149a9c3a…). Under a whole-route INFERRED convention this row would read INFERRED (DiffUtil dispatch upstream); label unaffected. Strict-entry: feed-anchored; the FeedActivity→FeedFragment attachment step was not freshly printed here (batch 99 caveat). |

## Changes vs prior proposal (lead only, breakdown 17/0/23)

- **One label change: row 25 TrackerInfo.equals OPEN → REACHABLE INFERRED**, on the freshly verified `containsAll` site at TorrentInfoProvider.java:366. The prior proposal's own route text already described this dispatch; this file adopts the route (verified fresh) rather than the prior breakdown's count. All other labels match the prior breakdown: TorrentInfo 5/8, TorrentStateCode 2/2, TrackerInfo now 8/9 (was 7/10 in the breakdown), FastResume 1/0, FeedChannel 2/3. **New totals: 18/0/22 vs prior 17/0/23.**
- **Confirmed_by note:** row 7 TorrentInfo.equals is SOURCE here on the direct call at TorrentInfoProvider:140, not merely INFERRED via the :246 `containsAll` route — both routes were freshly verified; the direct call governs.
- **Dropped wording:** the prior proposal's "launcher-anchored" claim for the TorrentInfo routes is not repeated — no launcher step was freshly printed in this pass (see Conventions 1).

## Conventions (recorded, not decided — merger must pick project-wide)

1. **Strict-entry:** no launcher step was freshly printed in this pass. Every REACHABLE row above is anchored at engine/provider/download/ViewModel sites and **reverts to OPEN under a strict launcher-entry rule**. In particular, rows 21/22/26/28/34 are detail-anchored (detail tap not freshly printed) and row 38 is dialog-anchored (AddFeedDialog show step not freshly printed); they stand only under the anchor convention used here.
2. **Per-row confirmed_by** (see table header). Under a whole-route INFERRED convention, SOURCE rows reached through unprinted dispatch would read INFERRED; labels unchanged.
3. **Parcelable Creator `$1.<init>`:** INFERRED when the enclosing class is first used on a printed route, because the CREATOR field initializer runs at class init (JVM timing unprinted). Applied to rows 11, 31. It does **not** extend to `createFromParcel`/`newArray`, which run only on framework unparcel.
4. **`<clinit>`:** INFERRED when any method/ctor/field of the class is used on a printed route. Applied to rows 1, 14, 18, 36.
5. **Parcelable-trio policy:** `writeToParcel` / `describeContents` / Parcel ctor / `$1.createFromParcel` / `$1.newArray` stay OPEN unless a printed app-side parcel/unparcel site is found. A CREATOR definition alone is not a caller.
6. **Library-dispatch equals:** `containsAll` dispatches to element `equals` by library code, so row 25 is INFERRED, not SOURCE. An explicit printed `x.equals(y)` call is SOURCE (row 7).
7. **Room-generated instantiation policy:** a Room `@Entity`'s Parcel ctor (row 37) or any ctor is not flipped to REACHABLE on entity status alone; only a printed construction or a printed generated-instantiation step counts. (Row 38 is REACHABLE on a printed `new FeedChannel`, not on entity status.)
8. **Dependency rule:** a method whose only printed caller sits inside an OPEN method does not become REACHABLE. Rows 16/17 stand/fall with rows 2/10; row 2's internal `TagInfo.CREATOR` use at TorrentInfo.java:140 does not bootstrap TagInfo (batch 31 row 19/27 rest on the equals routes, not on this site).
9. **No OPEN → UNREACHABLE flip on absence** without a saved full-repo grep in rule-F/C5 form.

## Gaps / named resolvers (all OPEN rows, plus the grep owed for any future UNREACHABLE claim)

- **Saved full-repo grep** (rule F/C5 form, covering generated code) for each OPEN row's exact call site, in particular: TorrentInfo Parcelable trio (rows 2, 6, 10, 12, 13), TorrentInfo.compareTo/hashCode/toString (rows 5, 8, 9), TorrentStateCode.fromValue/value (rows 16, 17 — resolve together with rows 2/10), TrackerInfo Parcelable trio + 4-arg ctor + compareTo/hashCode/toString (rows 19, 20, 23, 24, 27, 29, 32, 33), FeedChannel Parcel ctor/describeContents/equals (rows 37, 39, 40). A single printed caller flips the corresponding row to REACHABLE; a clean saved full-repo grep is the evidence that would support an UNREACHABLE proposal, subject to the merger's decision.
- **No UNREACHABLE row is claimed in this batch**, so no UNREACHABLE grep is owed for a label.
- **Merger re-checks:** detail-tap step for rows 21/22/26/28/34 and AddFeedDialog show step for row 38 were not freshly printed in this pass (prior-pass anchors only); TorrentEngine.makeTrackerInfoList's delegation to `task.getTrackerInfoList()` was cited from the prior pass, not freshly re-printed in this pass (TorrentInfoProvider:363 `engine.makeTrackerInfoList(id)` was freshly verified).
- **Still owed (not run):** main spot-check 1 in 5, `py_compile`, build, Mac build/C1, sampler. None claimed passed.
