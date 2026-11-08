# A1 parcel evidence — LibreTorrent batches 73 / 82 (helper, NOT the merger)

Scope: read-only evidence for six OPEN rows. No merge-ready file, graph_def.py,
parts file, verification.csv, PROGRESS file, or AGENT_NOTES was edited.
Nothing was pushed. All line numbers below were printed with `sed -n` or `grep -n`
during this pass.

## Sources and method

- Batch rows read first from:
  - `graphs/LibreTorrent/scratch/merge-ready/batch73-merge-ready.md`
    (rows 29, 35; table lines 127, 133)
  - `graphs/LibreTorrent/scratch/merge-ready/batch82-merge-ready.md`
    (rows 10, 12, 14, 16; table lines 71, 73, 75, 77)
- App source root grepped (read-only):
  `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main`
  (633 files, 281 Java files). Paths below are relative to that root.
- Grep patterns run over the whole root (Java + res XML):
  `putExtra`, `putParcelable`, `putParcelableArrayList`, `writeParcelable`,
  `setArguments`, `getArguments`, `getParcelable*`, `readParcelable`,
  `createFromParcel`, `Parcelable`, plus `SelectionTracker` /
  `StorageStrategy` / `createParcelableStorage` / `onSaveInstanceState`.
- Saved full-grep proof files (in this work dir):
  - `grep_FileItem.txt` (342 lines: Section A = every `FileItem` hit,
    lines 1-122; Section B = every marshalling-pattern hit, lines 123-342)
  - `grep_DownloadableFileItem.txt` (244 lines: Section A = every
    `DownloadableFileItem` hit, lines 1-24; Section B = same marshalling
    hits, lines 25-244)
- Cross-check (read-only, names/edges only): `graphs/LibreTorrent/auto_calls.json`.

## Whole-tree marshalling census (why "no site" is a finding, not an absence of looking)

- `putParcelable`: 13 sites, none naming FileItem or DownloadableFileItem.
  Values are: `uri` (Uri) in `ui/addfeed/AddFeedDialog.java:83` and `:198`;
  `initInfo` (TagInfo) in `ui/addtag/AddTagDialog.java:71` and `:122`;
  LayoutManager scroll state (`listFilesState` / `*ListState`, a framework
  `Parcelable`, not an item) in `ui/addtorrent/AddTorrentFilesFragment.java:159`,
  `ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:308`,
  `ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:149`,
  `ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:234`,
  `ui/feeditems/FeedItemsFragment.java:188`, `ui/feeds/FeedFragment.java:244`,
  `ui/filemanager/FileManagerDialog.java:407`,
  `ui/main/MainFragment.java:274`; `super.onSaveInstanceState()` in
  `ui/customviews/ExpansionHeader.java:168`.
- `putParcelableArrayList`: 0 sites in the whole root.
- `putExtra`: 43 sites; values are `long` ids, `Uri`, `String` (magnet/url/ip),
  `long[]`, `FileManagerConfig`, `PreferenceActivityConfig`, `TagInfo`
  (`item.info`). Two multi-line sites printed in full to confirm the value:
  `ui/addtorrent/AddTorrentInfoFragment.java:171-176` puts a `long[]` of tag ids;
  `ui/addtorrent/AddTorrentInfoFragment.java:211` and
  `ui/detailtorrent/pages/DetailTorrentInfoFragment.java:192` put a
  `FileManagerConfig` named `config`. None puts a FileItem or DownloadableFileItem.
- `getParcelable*`: 19 sites; values are `Uri`, `TagInfo`, `FileManagerConfig`,
  `PreferenceActivityConfig`, and the same LayoutManager scroll-state
  Parcelables. None reads a FileItem or DownloadableFileItem.
- `writeParcelable`: 2 sites only, both a `Uri` named `downloadPath`:
  `core/model/AddTorrentParams.java:102`,
  `core/model/data/entity/Torrent.java:146`.
- `readTypedList` / `createTypedArrayList`: only `TagInfo.CREATOR` in
  `core/model/data/TorrentInfo.java:140` and `BencodeFileItem.CREATOR` in
  `core/model/data/metainfo/TorrentMetaInfo.java:123`. BencodeFileItem is a
  separate class, not a FileItem subclass.
- No reference to `FileItem.CREATOR`, `DownloadableFileItem.CREATOR`, or
  `TorrentContentFileItem.CREATOR` exists outside the three item files
  themselves (other `CREATOR` hits are unrelated classes: TagInfo, Torrent,
  FileManagerConfig, etc.).
- Fragment arguments for the two owning fragments carry no item:
  `ui/addtorrent/AddTorrentFilesFragment.java:68-73` builds an empty
  `Bundle args` and calls `fragment.setArguments(args)`;
  `ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:102-107`
  does the same. Neither `getArguments()` read in those fragments returns an item.

## The one near-miss, and why it does not reach any of the six rows

- `ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:222-227`
  builds a `SelectionTracker` with
  `StorageStrategy.createParcelableStorage(TorrentContentFileItem.class)`,
  and `:309` calls `selectionTracker.onSaveInstanceState(outState)`.
  That parcels/unparcels **TorrentContentFileItem** keys, via
  **TorrentContentFileItem.CREATOR** — a different class's creator.
  It cannot dispatch to FileItem's creator or DownloadableFileItem's creator:
  framework creator dispatch is keyed by the parcelled object's runtime class.
- The same subclass logic disposes of the super-call argument for the
  FileItem rows: both subclasses override `describeContents` and
  `writeToParcel` (TorrentContentFileItem overrides at its own
  `describeContents`/`writeToParcel`; DownloadableFileItem at
  `ui/addtorrent/DownloadableFileItem.java:48-51` and `:54-59`, the latter
  calling `super.writeToParcel(dest, flags)` at `:56`). So parceling a
  subclass instance invokes the **subclass's** `describeContents`, never
  FileItem's; and it invokes the **subclass's** creator, never FileItem's.
  (The super `writeToParcel` call is why batch 73 row 33, FileItem.writeToParcel,
  is already REACHABLE — it is not one of my rows and is unaffected here.)
- AddTorrentFilesFragment uses no SelectionTracker at all: its items reach
  the adapter only via `ui/addtorrent/AddTorrentFilesFragment.java:117`
  (`.map(DownloadableFileItem::new)`) and `:122` (`adapter.submitList(children)`).
  `submitList` does not parcel.
- `new FileItem(...)` outside the creator body: zero sites. The only
  `new FileItem(source)` in the tree is inside FileItem's own creator
  (`ui/FileItem.java:76`); the only `new DownloadableFileItem(source)` is
  inside its own creator (`ui/addtorrent/DownloadableFileItem.java:67`).
  Construction of a plain FileItem never happens elsewhere, and construction
  alone would not parcel it anyway.
- Bytecode cross-check (`auto_calls.json`, `calls` array): the ONLY call edge
  whose destination is any of the six methods is edge 653,
  `DownloadableFileItem$1.createFromParcel` -> `DownloadableFileItem.<init>(Parcel)`
  at `DownloadableFileItem.java:67` — the creator body calling its own Parcel
  constructor. That is internal to the creator, not an external trigger: it
  runs only if the framework dispatches through that creator, which requires
  a DownloadableFileItem parcel site, of which there is none. No call edge
  targets 73/29, 73/35, 82/12, 82/14, or 82/16 at all.

## Per-row proposals

### 73/29 — FileItem.describeContents ()I — proposed UNREACHABLE, framework_never_calls

- Definition printed: `ui/FileItem.java:55-59` (`return 0;`).
- No printed site parcels a plain FileItem (see census above; the only
  parcel-storage site names TorrentContentFileItem, whose own
  `describeContents` override shadows this one).
- Proof: `grep_FileItem.txt` (full root grep, Sections A + B).
- Note for the merger: batch 73's conditional table groups rows 29/35/36
  together; row 36 (newArray) is NOT one of my rows and I propose nothing
  for it, but the same no-site finding would apply to it under the
  task's kind rule for newArray.

### 73/35 — FileItem$1.createFromParcel (Parcel)FileItem — proposed UNREACHABLE, no_trigger_in_app

- Definition printed: `ui/FileItem.java:71-77`
  (`return new FileItem(source);` at `:76`).
- No printed unparcel site for a FileItem: no `getParcelable*` site returns
  one, no `createParcelableStorage(FileItem.class)` exists, no
  `FileItem.CREATOR` reference exists outside the file. The subclass
  storage site (DetailTorrentFilesFragment.java:227) dispatches through
  TorrentContentFileItem.CREATOR, not this creator.
- Proof: `grep_FileItem.txt`.

### 82/10 — DownloadableFileItem.<init>(Parcel) (Parcel)V — proposed UNREACHABLE, no_trigger_in_app

- Definition printed: `ui/addtorrent/DownloadableFileItem.java:40-44`
  (`super(source);` then `selected = source.readByte() != 0;`).
- Sole caller in source and in bytecode is its own creator
  (`ui/addtorrent/DownloadableFileItem.java:65-68`, `return new
  DownloadableFileItem(source);` at `:67`; auto_calls edge 653). No printed
  site parcels or unparcels a DownloadableFileItem, so that creator is
  never framework-dispatched.
- Proof: `grep_DownloadableFileItem.txt`.

### 82/12 — DownloadableFileItem.describeContents ()I — proposed UNREACHABLE, framework_never_calls

- Definition printed: `ui/addtorrent/DownloadableFileItem.java:47-51`
  (`return 0;`).
- Framework calls `describeContents` only while parceling an instance of
  this class; no printed site parcels one (see census; AddTorrentFilesFragment
  only `submitList`s them, `:117`/`:122`, and has no SelectionTracker).
- Proof: `grep_DownloadableFileItem.txt`.

### 82/14 — DownloadableFileItem.writeToParcel (Parcel,I)V — proposed UNREACHABLE, no_trigger_in_app

- Definition printed: `ui/addtorrent/DownloadableFileItem.java:53-59`
  (`super.writeToParcel(dest, flags);` at `:56`, then writes `selected`).
- Same trigger analysis as 82/12: framework calls it only while parceling
  a DownloadableFileItem, and no printed site does so.
- Proof: `grep_DownloadableFileItem.txt`.

### 82/16 — DownloadableFileItem$1.createFromParcel (Parcel)DownloadableFileItem — proposed UNREACHABLE, no_trigger_in_app

- Definition printed: `ui/addtorrent/DownloadableFileItem.java:61-68`
  (`return new DownloadableFileItem(source);` at `:67`).
- No printed unparcel site for a DownloadableFileItem: no `getParcelable*`
  site returns one, no `createParcelableStorage(DownloadableFileItem.class)`
  exists, no `DownloadableFileItem.CREATOR` reference exists outside the file.
- Proof: `grep_DownloadableFileItem.txt`.
- Note for the merger: batch 82's conditional table groups rows 10/12/14/16/17
  together; row 17 (newArray) is NOT one of my rows and I propose nothing
  for it, but the same no-site finding would apply to it under the
  task's kind rule for newArray (and under D5c it would additionally need a
  Parcelable-array site, of which there are zero `putParcelableArrayList`
  sites in the whole root).

## Scope caveat (stated, not a blocker)

The saved greps cover `src/main` (app Java + res XML, 633 files). Generated
databinding code and framework internals are not in that tree, so a
generated-code parcel site would not appear here. Within the assigned
method — grep the app source root for marshalling sites — no site exists
for either class, and the bytecode cross-check shows no external call edge
into any of the six methods. No row is left undecided.

## Counts printed in this pass

- Rows examined: 6. Proposed UNREACHABLE: 6 (framework_never_calls: 2;
  no_trigger_in_app: 4). Proposed REACHABLE: 0. Undecided: 0.
- Grep files saved: 2 (`grep_FileItem.txt` 342 lines,
  `grep_DownloadableFileItem.txt` 244 lines).
- Marshalling census: `putParcelable` 13, `putParcelableArrayList` 0,
  `putExtra` 43, `getParcelable*` 19, `writeParcelable` 2 (both Uri),
  `setArguments` 37 (both owning fragments pass an empty Bundle).
