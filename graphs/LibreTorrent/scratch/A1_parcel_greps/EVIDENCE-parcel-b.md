# A1 parcel evidence — LibreTorrent batches 29 / 31 / 32 (helper, NOT merger)

Scope: 26 OPEN Parcelable-related rows. No merge-ready file, graph file,
parts file, verification.csv, or PROGRESS file was edited. Nothing was pushed.
Source root read (read-only branch tree, HEAD 6805252):

`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java`
(paths below are relative to that root; all file:lines were printed with
`sed -n` / `grep -n` during this pass).

## Method

For each of the 7 classes, the full marshalling grep was saved:

- `grep -rn --include="*.java" -E "putExtra|putParcelable|putParcelableArrayList|writeParcelable|setArguments|getArguments|getParcelable"` over the whole app Java tree: **120 lines total** (identical Section B in every grep file).
- Plus, per class: all occurrences of the class name, extended Parcel APIs
  (`readParcelable|writeTypedList|readTypedList|createTypedArrayList|getParcelableArrayList|writeToParcel|createFromParcel|readTypedArray`),
  and Bundle/Intent state APIs.
- Torrent note: plain substring `Torrent` over-matches (`TorrentEngine`,
  `TorrentDownload`, …). `grep_Torrent.txt` carries a corrected
  word-boundary section A (`grep -rn -w "Torrent"`, 113 lines) at the top;
  the word-boundary list is what the Torrent verdicts rest on.

## Shared negative evidence (applies to every row below)

1. `putParcelableArrayList` / `getParcelableArrayList`: **zero hits** in the
   whole tree.
2. Every `putParcelable` payload in the tree is one of: a `Uri`
   (`ui/addfeed/AddFeedDialog.java:83`, `:198`), a `TagInfo`
   (`ui/addtag/AddTagDialog.java:71`), a RecyclerView layout-manager state
   (`*ListState` Parcelables in `AddTorrentFilesFragment`, `DetailTorrentFilesFragment`,
   `DetailTorrentPeersFragment`, `DetailTorrentTrackersFragment`,
   `FeedItemsFragment`, `FeedFragment`, `FileManagerDialog`, `MainFragment`),
   or `super.onSaveInstanceState()` (`ui/customviews/ExpansionHeader.java:168`).
   None is a MagnetInfo, PeerInfo, SessionStats, FeedItem, Torrent,
   BencodeFileItem, or TorrentMetaInfo.
3. Every `getParcelable*` read in the tree returns a `Uri`, a `TagInfo`, a
   layout-manager state, a `FileManagerConfig`, or a
   `PreferenceActivityConfig` — never one of the 7 classes. The full list
   is in Section B of each grep file.
4. Every `putExtra` payload in the tree is a String / long / boolean / `Uri` /
   `long[]` / `FileManagerConfig` / `PreferenceActivityConfig` / `TagInfo`
   (`item.info` at `ui/main/MainActivity.java:323` and
   `ui/tag/SelectTagDialog.java:181`). The two multi-line `putExtra` sites
   are `long[]` tag-id arrays (`ui/addtorrent/AddTorrentInfoFragment.java:171`,
   `ui/detailtorrent/pages/DetailTorrentInfoFragment.java:159`). None is one
   of the 7 classes.
5. Every `setArguments` bundle in the tree is either empty (`new Bundle()`)
   or carries no Parcelable of these classes — verified site by site, e.g.
   `ui/detailtorrent/DetailTorrentFragment.java:119` (`setArguments(new Bundle())`,
   id passed separately via `setTorrentId`), `DetailTorrentInfoFragment.java:85`,
   `DetailTorrentStateFragment.java:56`, `DetailTorrentFilesFragment.java:106`,
   `AddTorrentFilesFragment.java:73`, `AddTorrentInfoFragment.java:78`,
   `FeedItemsFragment.java:84` (all empty bundles; `FeedItemsFragment` passes
   only a `long feedId` via `setFeedId`).
6. No app-side `CREATOR` use outside the defining files except two
   parcel-internal ones: `TorrentInfo.java:140`
   (`source.readTypedList(tags, TagInfo.CREATOR)`) and
   `TorrentMetaInfo.java:123` (`source.readTypedList(fileList, BencodeFileItem.CREATOR)`).
   The second is inside TorrentMetaInfo's own Parcel ctor, which itself has
   no app-side site (see 32/26), so it is a dead chain, not a reachable route.
7. No direct `Parcel.obtain` / external `.writeToParcel(` call site exists.
   The only `.writeToParcel(` hits outside definitions are `super.writeToParcel`
   calls inside other Parcelable subclasses (`PeerInfo.java:152`,
   `SessionStats.java:69`, plus `AdvancedTorrentInfo`, `TorrentInfo`,
   `TrackerInfo`, `DownloadableFileItem`, `TorrentContentFileItem`) — each runs
   only if that subclass's own `writeToParcel` runs, and none of those
   subclasses is parcelled app-side either.
8. Bytecode cross-check (read-only `graphs/LibreTorrent/auto_calls.json`,
   2,213,052 B): its `calls` list contains **zero** app-side edges into any
   `writeToParcel` / `createFromParcel` / `describeContents` of these 7
   classes; the `framework_calls` entries for them list only the Parcel
   writes inside the methods themselves (e.g. `MagnetInfo.writeToParcel ->
   [Parcel.writeList, Parcel.writeString]`). This matches the source grep.
9. None of the 7 classes implements `Serializable`, so no serializable
   detour exists either.

Rule applied per the task: a printed write/read site on a reachable route
would make the method REACHABLE; with no such site after the full grep, the
method is UNREACHABLE — kind `framework_never_calls` for `describeContents`,
kind `no_trigger_in_app` otherwise. Class-level use (Room, Flowable, plain
construction) is NOT a parcel site and does not flip a parcel method.

## Per-row proposals

### 29/4 — MagnetInfo.writeToParcel — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/MagnetInfo.java:71` — `public void writeToParcel(Parcel dest, int flags)`, writes `uri`, `sha1hash`, `name`, `filePriorities` (`:72-76`).
- Evidence: no site parcels a MagnetInfo. Its non-definition uses are
  `fetchMagnet`/`parseMagnet` returns (`core/model/TorrentEngine.java:415,419,427`,
  `core/model/session/TorrentSessionImpl.java:427,439,444,450`) and
  `ui/addtorrent/AddTorrentViewModel.java:237` — all plain returns/variables,
  never a `putExtra`/`putParcelable` argument. Grep file: `grep_MagnetInfo.txt`.

### 29/6 — MagnetInfo$1.createFromParcel — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/MagnetInfo.java:83` — `return new MagnetInfo(source);`
  inside `CREATOR` (`:79-86`).
- Evidence: framework dispatch only. No `getParcelable*` read of a MagnetInfo
  exists anywhere (see shared evidence 3), and no `CREATOR` reference to
  MagnetInfo exists outside this file. Grep file: `grep_MagnetInfo.txt`.

### 29/9 — PeerInfo.\<init\>(Parcel) — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/PeerInfo.java:92-107` (Parcel ctor).
- Evidence: only printed caller is its own `CREATOR.createFromParcel`
  (`PeerInfo.java:170-172`, row 29/21, itself UNREACHABLE below). No
  app-side unparcel site for a PeerInfo. Its live uses are plain lists:
  `core/model/session/TorrentDownloadImpl.java:911,924` (`new PeerInfo(peer, status)`),
  `core/model/TorrentInfoProvider.java:114,390-410` (Flowable lists).
  Subclass note: `ui/detailtorrent/pages/peers/PeerItem.java:24`
  (`public class PeerItem extends PeerInfo`) has no CREATOR and no Parcelable
  implementation of its own, and is never parcelled; its ctor (`:28-33`)
  calls the non-parcel `super(...)` ctor, not the Parcel ctor.
  Grep file: `grep_PeerInfo.txt`.

### 29/14 — PeerInfo.describeContents — UNREACHABLE, framework_never_calls
- Def: `core/model/data/PeerInfo.java:144-146` — `return 0;`.
- Evidence: `describeContents` runs only as part of framework marshalling of
  a PeerInfo; per 29/9 and 29/19 no PeerInfo is ever marshalled, so the
  framework never calls it. Grep file: `grep_PeerInfo.txt`.

### 29/19 — PeerInfo.writeToParcel — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/PeerInfo.java:150-164` (`super.writeToParcel` at `:152`,
  then field writes).
- Evidence: no site parcels a PeerInfo (shared evidence 2–4). The
  `super.writeToParcel` at `:152` targets `AbstractInfoParcel.writeToParcel`
  (`core/model/data/AbstractInfoParcel.java`, writes only `parcelId`) and runs
  only if this method runs. Grep file: `grep_PeerInfo.txt`.

### 29/21 — PeerInfo$1.createFromParcel — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/PeerInfo.java:170-172` — `return new PeerInfo(source);`.
- Evidence: framework dispatch only; no printed unparcel site for a PeerInfo
  (shared evidence 3). Grep file: `grep_PeerInfo.txt`.

### 29/31 — SessionStats.\<init\>(Parcel) — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/SessionStats.java:48-58` (`super(source)` at `:50`).
- Evidence: only printed caller is its own `CREATOR.createFromParcel`
  (`SessionStats.java:83-86`, row 29/39, itself UNREACHABLE below).
  SessionStats travels via listener/Flowable, not Parcel:
  `core/model/session/TorrentSessionImpl.java:1173-1174`
  (`listener.onSessionStats(new SessionStats(...))`),
  `core/model/TorrentInfoProvider.java:126,474-481`,
  `ui/main/MainActivity.java:456-460,529` (`updateSessionStats`). The
  `putExtra` sites in `MainActivity.java:323,671` carry a `TagInfo` and a
  String id respectively, not a SessionStats (file-level co-occurrence only).
  Grep file: `grep_SessionStats.txt`.

### 29/33 — SessionStats.describeContents — UNREACHABLE, framework_never_calls
- Def: `core/model/data/SessionStats.java:61-64` — `return 0;`.
- Evidence: as 29/14 — no SessionStats is ever marshalled, so the framework
  never calls it. Grep file: `grep_SessionStats.txt`.

### 29/37 — SessionStats.writeToParcel — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/SessionStats.java:67-77` (`super.writeToParcel` at `:69`).
- Evidence: no site parcels a SessionStats (shared evidence 2–4); its only
  travel is the Flowable route cited at 29/31. Grep file: `grep_SessionStats.txt`.

### 29/39 — SessionStats$1.createFromParcel — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/SessionStats.java:83-86` — `return new SessionStats(source);`.
- Evidence: framework dispatch only; no printed unparcel site for a
  SessionStats. Grep file: `grep_SessionStats.txt`.

### 31/9 — FeedItem.\<init\>(Parcel) — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/entity/FeedItem.java:83-93` (Parcel ctor, `@Ignore`).
- Evidence: only printed caller is its own `CREATOR.createFromParcel`
  (`FeedItem.java:118-121`, row 31/17, itself UNREACHABLE below). FeedItem
  travels via Room/Flowable, not Parcel: `core/storage/dao/FeedDao.java:82,97,100,109`,
  `core/FeedParser.java:89,109`, `service/FeedFetcherWorker.java:165,212-215`.
  Grep file: `grep_FeedItem.txt`.

### 31/11 — FeedItem.describeContents — UNREACHABLE, framework_never_calls
- Def: `core/model/data/entity/FeedItem.java:96-99` — `return 0;`.
- Evidence: as 29/14 — no FeedItem is ever marshalled, so the framework never
  calls it. Grep file: `grep_FeedItem.txt`.

### 31/15 — FeedItem.writeToParcel — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/entity/FeedItem.java:102-112`.
- Evidence: no site parcels a FeedItem. The marshalling sites in files that
  mention FeedItem are for other payloads: `ui/feeditems/FeedItemsFragment.java:188`
  (`outState.putParcelable(TAG_ITEMS_LIST_STATE, itemsListState)` where
  `:186` shows `itemsListState = layoutManager.onSaveInstanceState()` — a
  layout-manager state, not a FeedItem) and `:293`
  (`i.putExtra(AddTorrentActivity.TAG_URI, Uri.parse(item.downloadUrl))` —
  payload is a `Uri` derived from a FeedItem field, not the FeedItem).
  `ui/feeds/FeedActivity.java:222` carries a `long feedId`;
  `FeedFragment.java:244` carries a layout state. Grep file: `grep_FeedItem.txt`.

### 31/17 — FeedItem$1.createFromParcel — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/entity/FeedItem.java:118-121` — `return new FeedItem(source);`.
- Evidence: framework dispatch only; no printed unparcel site for a FeedItem.
  Grep file: `grep_FeedItem.txt`.

### 31/31 — Torrent.\<init\>(Parcel) — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/entity/Torrent.java:104-117` (Parcel ctor, `@Ignore`).
- Evidence: only printed caller is its own `CREATOR.createFromParcel`
  (`Torrent.java:160-163`, row 32/3, itself UNREACHABLE below). Torrent
  travels via Room/Flowable and by id string, not Parcel:
  `ui/TorrentNotifier.java:233` (`openIntent.putExtra(DetailTorrentActivity.TAG_TORRENT_ID, torrent.id)`),
  `ui/main/MainActivity.java:671` (`i.putExtra(DetailTorrentActivity.TAG_TORRENT_ID, id)`),
  read back as a String at `ui/detailtorrent/DetailTorrentActivity.java:71`
  (`getIntent().getStringExtra(TAG_TORRENT_ID)`).
  Grep file: `grep_Torrent.txt` (word-boundary section A).

### 31/34 — Torrent.describeContents — UNREACHABLE, framework_never_calls
- Def: `core/model/data/entity/Torrent.java:136-139` — `return 0;`.
- Evidence: as 29/14 — no Torrent is ever marshalled, so the framework never
  calls it. (`Torrent.writeToParcel` is not a batch-31 row and is judged
  separately at 32/1.) Grep file: `grep_Torrent.txt` (word-boundary section A).

### 32/1 — Torrent.writeToParcel — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/entity/Torrent.java:142-155`.
- Evidence: no site parcels a Torrent (see 31/31: only its id String is
  passed). The `dest.writeParcelable(downloadPath, flags)` at
  `Torrent.java:146` parcels the Torrent's own `Uri` field and runs only
  inside this method — it is not an app-side site for a Torrent.
  Grep file: `grep_Torrent.txt` (word-boundary section A).

### 32/3 — Torrent$1.createFromParcel — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/entity/Torrent.java:160-163` — `return new Torrent(source);`.
- Evidence: framework dispatch only; no printed unparcel site for a Torrent.
  Grep file: `grep_Torrent.txt` (word-boundary section A).

### 32/10 — BencodeFileItem.\<init\>(Parcel) — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/metainfo/BencodeFileItem.java:44-48` (Parcel ctor).
- Evidence: printed callers are only (a) its own `CREATOR.createFromParcel`
  (`BencodeFileItem.java:99-101`, row 32/23, itself UNREACHABLE below) and
  (b) `TorrentMetaInfo`'s Parcel ctor via
  `TorrentMetaInfo.java:123` (`source.readTypedList(fileList, BencodeFileItem.CREATOR)`).
  Path (b) runs only if a TorrentMetaInfo is unmarshalled, which never
  happens app-side (see 32/26). Its live uses are plain list access:
  `core/utils/Utils.java:142-145` (`new BencodeFileItem(...)` from storage),
  `ui/addtorrent/AddTorrentViewModel.java:375`, `ui/detailtorrent/DetailTorrentViewModel.java:539,557`.
  Grep file: `grep_BencodeFileItem.txt`.

### 32/13 — BencodeFileItem.describeContents — UNREACHABLE, framework_never_calls
- Def: `core/model/data/metainfo/BencodeFileItem.java:82-85` — `return 0;`.
- Evidence: as 29/14 — no BencodeFileItem is ever marshalled app-side (its
  only typed-list route sits inside the never-invoked TorrentMetaInfo Parcel
  ctor), so the framework never calls it. Grep file: `grep_BencodeFileItem.txt`.

### 32/21 — BencodeFileItem.writeToParcel — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/metainfo/BencodeFileItem.java:88-93`.
- Evidence: the only typed-list write is `TorrentMetaInfo.java:144`
  (`dest.writeTypedList(fileList)`), inside `TorrentMetaInfo.writeToParcel`
  (row 32/36, itself UNREACHABLE below) — a dead chain, not a reachable
  route. No app-side site parcels a BencodeFileItem directly.
  Grep file: `grep_BencodeFileItem.txt`.

### 32/23 — BencodeFileItem$1.createFromParcel — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/metainfo/BencodeFileItem.java:99-101` — `return new BencodeFileItem(source);`.
- Evidence: framework dispatch only, plus the dead-chain reference at
  `TorrentMetaInfo.java:123` (see 32/10). No printed unparcel site for a
  BencodeFileItem outside a never-invoked Parcel ctor.
  Grep file: `grep_BencodeFileItem.txt`.

### 32/26 — TorrentMetaInfo.\<init\>(Parcel) — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/metainfo/TorrentMetaInfo.java:113-126` (Parcel ctor,
  including `readTypedList` at `:123`).
- Evidence: only printed caller is its own `CREATOR.createFromParcel`
  (`TorrentMetaInfo.java:153-155`, row 32/38, itself UNREACHABLE below).
  Live constructions are all non-parcel: `core/model/TorrentEngine.java:384`
  (`new TorrentMetaInfo(is)`), `:464` (`new TorrentMetaInfo(bencode)`),
  `core/model/session/TorrentDownloadImpl.java:406,1194,1200`,
  `service/FeedDownloaderWorker.java:141`; carriage is via ViewModel/field
  (`ui/detailtorrent/TorrentDetailsInfo.java:35,102,107`,
  `DetailTorrentViewModel.java:199,536`). The marshalling sites in
  `DetailTorrentFragment.java:119,544,602-603` carry an empty bundle, a
  `FileManagerConfig`, and share Strings — not a TorrentMetaInfo.
  Grep file: `grep_TorrentMetaInfo.txt`.

### 32/31 — TorrentMetaInfo.describeContents — UNREACHABLE, framework_never_calls
- Def: `core/model/data/metainfo/TorrentMetaInfo.java:129-132` — `return 0;`.
- Evidence: as 29/14 — no TorrentMetaInfo is ever marshalled, so the
  framework never calls it. Grep file: `grep_TorrentMetaInfo.txt`.

### 32/36 — TorrentMetaInfo.writeToParcel — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/metainfo/TorrentMetaInfo.java:135-147`
  (`writeTypedList(fileList)` at `:144`).
- Evidence: no site parcels a TorrentMetaInfo (shared evidence 2–4; see
  32/26 for its actual non-parcel routes). Its `writeTypedList` is the
  dead-chain write counterpart of 32/21. Grep file: `grep_TorrentMetaInfo.txt`.

### 32/38 — TorrentMetaInfo$1.createFromParcel — UNREACHABLE, no_trigger_in_app
- Def: `core/model/data/metainfo/TorrentMetaInfo.java:153-155` — `return new TorrentMetaInfo(source);`.
- Evidence: framework dispatch only; no printed unparcel site for a
  TorrentMetaInfo. Grep file: `grep_TorrentMetaInfo.txt`.

## Counts printed

- Rows judged: 26 (all assigned rows; none left undecided).
- Proposed REACHABLE: 0.
- Proposed UNREACHABLE: 26 — of which kind `no_trigger_in_app`: 20,
  kind `framework_never_calls` (all `describeContents` rows): 6
  (29/14, 29/33, 31/11, 31/34, 32/13, 32/31).
- Undecided / guessed: 0. Every "no site" claim rests on a saved full-grep
  file listed above, not on absence alone; the nearest apparent sites were
  checked value-by-value (id String vs Torrent, `Uri` vs FeedItem,
  layout-manager state vs FeedItem, `TagInfo`/`FileManagerConfig` vs the
  7 classes, and the TorrentMetaInfo→BencodeFileItem typed-list chain,
  which is dead because TorrentMetaInfo itself is never parcelled).

## Files delivered in this work dir

- `EVIDENCE.md` (this file)
- `grep_MagnetInfo.txt`, `grep_PeerInfo.txt`, `grep_SessionStats.txt`,
  `grep_FeedItem.txt`, `grep_Torrent.txt` (word-boundary section A at top),
  `grep_BencodeFileItem.txt`, `grep_TorrentMetaInfo.txt`
