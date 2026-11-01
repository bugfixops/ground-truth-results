# A1 R5 evidence — LibreTorrent batches 28–34 (helper only, NOT the merger)

Scope: 21 OPEN rows. Nothing in the merge-ready files, graph, parts, verification.csv,
PROGRESS files, or notes was edited. Nothing was pushed.
Read-only inputs: branch tree at `/home/hatch/workspace/finish/clone/` (work-2026-10-31,
HEAD 6805252); batch files under `graphs/LibreTorrent/scratch/merge-ready/`;
app source root `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main`
(shorthanded below as `SRC/`); bytecode `graphs/LibreTorrent/auto_calls.json`
(5,496 entries in its `calls` list).

Method for every row: (a) `grep -rn` over the app Java tree for the method name and for
the class name, saved per row as `grep_<Batch>_<Row>.txt` in this directory
(sections: A method-pattern grep, B class-name grep, C implicit-use grep for
equals/compareTo rows, D res-XML grep, E bytecode-lookup addendum);
(b) lookup of the exact method as a `dst` in `auto_calls.json` `calls`;
(c) for each apparent caller, its surrounding lines were printed and its receiver
checked, so same-named methods on other classes were excluded, not counted.
For equals/compareTo rows, implicit use was checked (sorting, sets/maps,
contains/remove, DiffUtil-style equals calls) and is reported only where found.
A "no caller" proposal below rests on the saved full grep PLUS the bytecode
lookup, never on grep alone.

## Summary of proposals (21 rows)

- REACHABLE: 2 — 28/18 (INFERRED), 31/33 (INFERRED)
- UNREACHABLE no_trigger_in_app: 19 — 28/25, 29/1, 29/32, 30/5, 31/35, 32/6,
  32/17, 32/18, 32/19, 32/32, 33/24, 33/26, 33/30, 33/31, 33/36, 33/38, 33/39,
  33/40, 34/1
- UNDECIDED: 0

## 28/18 — AbstractInfoParcel.\<init\>() — REACHABLE INFERRED

- Definition: `SRC/java/org/proninyaroslav/libretorrent/core/model/data/AbstractInfoParcel.java:36-39`
  (`protected AbstractInfoParcel()`; `parcelId = UUID.randomUUID().toString()`).
- Chain (printed): `TorrentSessionImpl.java:1095-1096` alert dispatch
  `case SESSION_STATS: handleStats();` → `TorrentSessionImpl.java:1168-1179`
  `handleStats()` builds `new SessionStats(dhtNodes(), getTotalDownload(), ...)`.
- The `SessionStats(long,long,long,long,long,int)` constructor at
  `SRC/java/org/proninyaroslav/libretorrent/core/model/data/SessionStats.java:37-47`
  has no explicit `super(...)` in source, so Java inserts the no-arg super call.
  Bytecode confirms it: `SessionStats.<init>(long,long,long,long,long,int)` →
  `AbstractInfoParcel.<init>()` at `SessionStats.java:39`.
- The other bytecode super-caller, `AdvancedTorrentInfo.<init>()` →
  `AbstractInfoParcel.<init>()` at `AdvancedTorrentInfo.java:51` (explicit `super()`
  at `AdvancedTorrentInfo.java:49-52`), is NOT itself called anywhere: source grep
  for `new AdvancedTorrentInfo` finds only the 12-arg call at `TorrentEngine.java:846`
  and the Parcel CREATOR call at `AdvancedTorrentInfo.java:125`. The verdict rests
  on the SessionStats path, not on the AdvancedTorrentInfo path.
- Kind note for the merger: INFERRED, not SOURCE, because the decisive
  constructor→super link is compiler-inserted and is evidenced by bytecode,
  not by a printed `super()` line in the SessionStats constructor.
- Grep file: `grep_28_18.txt`

## 28/25 — AdvancedTorrentInfo.compareTo(Object) — UNREACHABLE no_trigger_in_app

- Definition: `AdvancedTorrentInfo.java:136-139`
  (`return torrentId.compareTo(((AdvancedTorrentInfo)another).torrentId);`).
- Source grep for `compareTo` finds only definitions and String/other-class
  comparisons; no call site passes an `AdvancedTorrentInfo` receiver, and no
  `List<AdvancedTorrentInfo>` / sort / TreeSet use of the class exists in the tree.
- Bytecode: dst `AdvancedTorrentInfo.compareTo` = 0 hits. Do not conflate with the
  sibling `AdvancedTorrentInfo.equals`, which IS called at
  `TorrentInfoProvider.java:331` — that is a different method.
- Implicit use found: none.
- Grep file: `grep_28_25.txt`

## 29/1 — MagnetInfo.getUri() — UNREACHABLE no_trigger_in_app

- Definition: `MagnetInfo.java:95-98` (`return uri;`).
- Source grep for `getUri(` finds only other classes' methods: feedparser
  `Element`/`BaseElement`, NanoHTTPD session, `SafFileSystem` DocumentFile calls,
  and `AddTorrentActivity`'s own private `getUri()` at `:350`. No call site has a
  `MagnetInfo` receiver. Callers of `MagnetInfo` objects use the sibling getters
  instead, e.g. `AddTorrentViewModel.java:242` `magnetInfo.getName()`,
  `magnetInfo.getSha1hash()`, and `:246` `magnetInfo.getFilePriorities()`.
- Bytecode: dst `MagnetInfo.getUri` = 0 hits. Res-XML grep for `MagnetInfo`: no hits.
- Grep file: `grep_29_1.txt`

## 29/32 — SessionStats.compareTo(Object) — UNREACHABLE no_trigger_in_app

- Definition: `SessionStats.java:111-114`
  (`return parcelId.compareTo(((SessionStats)o).parcelId);`).
- Source grep for `compareTo` finds no call site on a `SessionStats` receiver and
  no `List<SessionStats>` / sort use; the class travels singly via the listener
  Flowable (`TorrentInfoProvider.java:475-485`, `onSessionStats`).
- Bytecode: dst `SessionStats.compareTo` = 0 hits. Do not conflate with the sibling
  `SessionStats.equals`, called at `TorrentInfoProvider.java:482`
  (`if (!newStats.equals(oldStats))`) — different method.
- Implicit use found: none.
- Grep file: `grep_29_32.txt`

## 30/5 — TorrentInfo.compareTo(Object) — UNREACHABLE no_trigger_in_app

- Definition: `TorrentInfo.java:186-187`
  (`return name.compareTo(((TorrentInfo) another).name);`).
- The only sorting of `TorrentInfo` lists in the tree goes through an explicit
  comparator, not this method: `TorrentService.java:89`
  (`private TorrentSortingComparator itemsSorting;`), `:287` and `:304`
  (`.sorted(itemsSorting)`), and `TorrentSorting.java:42-44` (the `name` column
  compares `item1.name.compareTo(item2.name)` — String comparison, not
  `TorrentInfo.compareTo`). List flow otherwise uses `containsAll`/equals.
- Bytecode: dst `TorrentInfo.compareTo` = 0 hits. Do not conflate with the sibling
  `TorrentInfo.equals`, called at `TorrentInfoProvider.java:140`
  (`!newInfo.equals(oldInfo)`) — different method.
- Implicit use found: none (no no-arg `sorted()` / `Collections.sort` on a
  `TorrentInfo` list; `TorrentListItem` wraps `TorrentInfo` and overrides its own
  `equals`, it does not call `TorrentInfo.compareTo`).
- Grep file: `grep_30_5.txt`

## 31/33 — Torrent.\<init\>(String,String,Uri,String,boolean,long,boolean,boolean) (8-arg) — REACHABLE INFERRED

- Definition: `Torrent.java:89-101` (delegates to the 7-arg constructor at `:98`,
  then sets `magnet` at `:100`). This is the non-`@Ignore` Room entity constructor;
  the 7-arg constructor at `:72` is `@Ignore`.
- App-source grep for `new Torrent(` finds only the 7-arg call at
  `TorrentSessionImpl.java:263` and the Parcel CREATOR call at `Torrent.java:162` —
  no app-source 8-arg construction. The 8-arg constructor is reached through
  generated Room code instead.
- Bytecode (generated code, not present as source in the final_java_only tree):
  dst `Torrent.<init>(String,String,Uri,String,boolean,long,boolean,boolean)` is
  called by `TorrentDao_Impl.getAllTorrents` at `TorrentDao_Impl.java:380`,
  `TorrentDao_Impl.getTorrentById` at `:465`, `TorrentDao_Impl$7.call` at `:554`,
  and `TorrentDao_Impl$8.call` at `:651`.
- The DAO methods are reached from app code: `TorrentRepositoryImpl.java:72`
  (`return db.torrentDao().getTorrentById(id);`) and `:86-87`
  (`db.torrentDao().getAllTorrents()`), called in turn e.g. at
  `TorrentEngine.java:817` (`for (Torrent torrent : repo.getAllTorrents())`) and
  `TorrentSessionImpl.java:401`. `AppDatabase.java:61` declares
  `public abstract TorrentDao torrentDao();`.
- Kind note for the merger: INFERRED, never SOURCE, because the direct caller is
  generated Room code evidenced by bytecode only, matching the batch-31
  generated-Room-code convention.
- Grep file: `grep_31_33.txt`

## 31/35 — Torrent.equals(Object) — UNREACHABLE no_trigger_in_app

- Definition: `Torrent.java:179-182`
  (`return o instanceof Torrent && (o == this || id.equals(((Torrent)o).id));`).
- Source grep for `equals(` in `Torrent`-mentioning code finds no call on a
  `Torrent` (entity) receiver; repository lookups use id strings, e.g.
  `TorrentSessionImpl.java:280` (`repo.getTorrentById(torrent.id)`). No
  `contains`/`remove` on a `Torrent` collection was found; `List<Torrent>` occurs
  only as the DAO/repository return type (`TorrentDao.java:49`,
  `TorrentRepositoryImpl.java:86-87`).
- Bytecode: dst `Torrent.equals` = 0 hits.
- Implicit use found: none.
- Grep file: `grep_31_35.txt`

## 32/6 — TorrentTagInfo.equals(Object) — UNREACHABLE no_trigger_in_app

- Definition: `TorrentTagInfo.java:63-70` (identity, then `torrentId.equals(...)`).
- `TorrentTagInfo` objects are only constructed for DAO insert/delete:
  `TorrentRepositoryImpl.java:125` (`tagInfoList.add(new TorrentTagInfo(...))`),
  `:132` (`db.torrentDao().addTag(new TorrentTagInfo(...))`),
  `:137` (`db.torrentDao().deleteTag(new TorrentTagInfo(...))`).
  Room delete matches by primary key, not by this `equals`; no source call site
  invokes it, and the `ArrayList<TorrentTagInfo>` at `:123` is only added to.
- Bytecode: dst `TorrentTagInfo.equals` = 0 hits.
- Implicit use found: none.
- Grep file: `grep_32_6.txt`

## 32/17 — BencodeFileItem.setIndex(int) — UNREACHABLE no_trigger_in_app

- Definition: `BencodeFileItem.java:76-79` (`this.index = index;`).
- Source grep for `setIndex(` finds only two definitions: this one and
  `FileTree.setIndex` at `FileTree.java:142` (a different class). The sole
  construction path sets fields via the constructor:
  `Utils.java:145` (`new BencodeFileItem(storage.filePath(i), i, storage.fileSize(i))`).
  Getters are called (`BencodeFileTreeUtils.java:105` `getIndex()`), setters are not.
- Bytecode: dst `BencodeFileItem.setIndex` = 0 hits.
- Grep file: `grep_32_17.txt`

## 32/18 — BencodeFileItem.setPath(String) — UNREACHABLE no_trigger_in_app

- Definition: `BencodeFileItem.java:56-59` (`this.path = path;`).
- Source grep for `setPath(` finds this definition only. Same construction path
  as 32/17 (`Utils.java:145`); the Parcel path also reads fields directly.
  Callers use `getPath()` (`BencodeFileTreeUtils.java:96`), never `setPath`.
- Bytecode: dst `BencodeFileItem.setPath` = 0 hits.
- Grep file: `grep_32_18.txt`

## 32/19 — BencodeFileItem.setSize(long) — UNREACHABLE no_trigger_in_app

- Definition: `BencodeFileItem.java:66-69` (`this.size = size;`).
- Source grep for `setSize(` finds this definition plus an unrelated
  `FileManagerSpinnerAdapter.java:89` definition. Same construction path as
  32/17 (`Utils.java:145`); callers use `getSize()`
  (`BencodeFileTreeUtils.java:103`), never `setSize`.
- Bytecode: dst `BencodeFileItem.setSize` = 0 hits.
- Grep file: `grep_32_19.txt`

## 32/32 — TorrentMetaInfo.equals(Object) — UNREACHABLE no_trigger_in_app

- Definition: `TorrentMetaInfo.java:172-185` (field-by-field comparison).
- `TorrentMetaInfo` travels singly via Flowables (`TorrentEngine`, `DetailTorrentViewModel`
  observe/update paths); no `List`/`Set<TorrentMetaInfo>` collection, sort, or
  contains use exists in the tree, and no source call site invokes `equals` on it.
- Bytecode: dst `TorrentMetaInfo.equals` = 0 hits.
- Implicit use found: none.
- Grep file: `grep_32_32.txt`

## 33/24 — FileTree.compareTo(FileTree) — UNREACHABLE no_trigger_in_app

- Definition: `FileTree.java:187-190`
  (`return name.compareTo(another.getName());`).
- The `Collections.sort` calls near FileTree code sort `BencodeFileItem` lists,
  not FileTree lists: `BencodeFileTreeUtils.java:46-55`
  (`buildFileTree(List<BencodeFileItem> files)`; `filesCopy` is
  `List<BencodeFileItem>`; `Collections.sort(filesCopy)` invokes
  `BencodeFileItem.compareTo` at `BencodeFileItem.java:112-114`). No sort of a
  FileTree collection and no direct `compareTo` call on a FileTree receiver exists.
- Bytecode: dst `FileTree.compareTo` = 0 hits; the only `compareTo` dst in the
  whole graph is `FileManagerNode.compareTo` (`FileManagerAdapter.java:58`),
  a different class.
- Implicit use found: none.
- Grep file: `grep_33_24.txt`

## 33/26 — FileTree.equals(Object) — UNREACHABLE no_trigger_in_app

- Definition: `FileTree.java:193-207` (index/name/size/isLeaf comparison).
- `FileTree.contains(String)` at `FileTree.java:80-83` is
  `children.containsKey(name)` — a String-key map lookup, not a FileTree
  `equals` call. No source call site, set/map membership, or `contains`/`remove`
  on FileTree objects was found.
- Bytecode: dst `FileTree.equals` = 0 hits.
- Implicit use found: none.
- Grep file: `grep_33_26.txt`

## 33/30 — FileTree.getChildrenIndexes() — UNREACHABLE no_trigger_in_app

- Definition: `FileTree.java:100-108` (builds a list from `child.getIndex()`).
- Source grep for `getChildrenIndexes(` finds this definition only. Callers of
  tree children use `getChildren()` instead (bytecode: e.g.
  `AddTorrentViewModel.getChildren` → `FileTree.getChildren` at
  `AddTorrentViewModel.java:420`; `DetailTorrentViewModel.getChildren` →
  `FileTree.getChildren` at `DetailTorrentViewModel.java:240`) and `getIndex()`
  per child, never this aggregate method.
- Bytecode: dst `FileTree.getChildrenIndexes` = 0 hits. (Its body calling
  `getIndex` at `FileTree.java:105` is internal, not a caller of it.)
- Grep file: `grep_33_30.txt`

## 33/31 — FileTree.getChildrenName() — UNREACHABLE no_trigger_in_app

- Definition: `FileTree.java:95-98` (`return children.keySet();`).
- Source grep for `getChildrenName(` finds this definition only; same
  `getChildren()`-based call pattern as 33/30.
- Bytecode: dst `FileTree.getChildrenName` = 0 hits.
- Grep file: `grep_33_31.txt`

## 33/36 — FileTree.getType() — UNREACHABLE no_trigger_in_app

- Definition: `FileTree.java:153-156`
  (`return (isLeaf ? FileNode.Type.FILE : FileNode.Type.DIR);`).
- Every other `getType()` hit in the tree belongs to another class: feedparser
  `Enclosure`/`Content`, `FilePriority.getType()` (e.g.
  `TorrentContentFileTree.java:96,115,136,138,156`, all on `priority` objects),
  `FileManagerNode.getType()`, and `Intent.getType()`. In-tree code that needs
  the file/dir distinction on a FileTree reads the field directly:
  `FileTree.isFile()` at `FileTree.java:110-113` (`return isLeaf;`).
- Bytecode: dst `FileTree.getType` = 0 hits (all `getType` dst hits are
  `FilePriority`/`FileManagerNode`/feedparser).
- Grep file: `grep_33_36.txt`

## 33/38 — FileTree.setIndex(int) — UNREACHABLE no_trigger_in_app

- Definition: `FileTree.java:142-145` (`this.index = index;`).
- Source grep for `setIndex(` finds only this definition and
  `BencodeFileItem.setIndex` at `BencodeFileItem.java:76` (a different class).
  All FileTree constructors set the field directly, e.g.
  `FileTree.java:63-68` (`this.index = index; ... this.parent = parent;`).
- Bytecode: no dst `setIndex` hit anywhere.
- Grep file: `grep_33_38.txt`

## 33/39 — FileTree.setName(String) — UNREACHABLE no_trigger_in_app

- Definition: `FileTree.java:131-134` (`this.name = name;`).
- The two `p.setName(...)` hits in `TorrentSessionImpl.java:484` and `:1643`
  are on a libtorrent `add_torrent_params` object (`p.getFlags()` /
  `p.setFlags(...)` in the same blocks), not on a FileTree. All remaining
  `setName(` hits are `MutableParams`/`AddTagState`/`Thread`/`FileManagerNode`
  setters. FileTree constructors set `name` directly (`FileTree.java:63-68`).
- Bytecode: dst `FileTree.setName` = 0 hits (all `setName` dst hits are
  `MutableParams`/`AddTagState`-family).
- Grep file: `grep_33_39.txt`

## 33/40 — FileTree.setParent(F) — UNREACHABLE no_trigger_in_app

- Definition: `FileTree.java:125-128` (`this.parent = parent;`).
- Source grep for `setParent(` finds this definition only. Constructors set the
  field directly (`FileTree.java:63-68`, `this.parent = parent;`); no caller
  re-parents a node after construction.
- Bytecode: no dst `setParent` hit anywhere.
- Grep file: `grep_33_40.txt`

## 34/1 — FileTree.setType(int) — UNREACHABLE no_trigger_in_app

- Definition: `FileTree.java:159-162` (`isLeaf = (type == FileNode.Type.FILE);`).
- Source grep for `setType(` finds only the `FileNode` interface declaration
  (`FileNode.java:44`), this definition, `Intent.setType("text/plain")` calls,
  and `FileManagerNode.setType` (`FileManagerNode.java:65`). Constructors pass
  `type` and set `isLeaf` directly (`FileTree.java:63-68`).
- Bytecode: no dst `setType` hit anywhere.
- Grep file: `grep_34_1.txt`

## Caveats for the merger

1. Sibling-method traps (checked, not conflated): `AdvancedTorrentInfo.equals`
   (`TorrentInfoProvider.java:331`), `SessionStats.equals` (`:482`), and
   `TorrentInfo.equals` (`:140`) ARE called, but none of those is a call to the
   corresponding `compareTo` row in this set. Likewise `BencodeFileItem.compareTo`
   is reached via `Collections.sort` on `BencodeFileItem` lists, which does not
   reach `FileTree.compareTo`.
2. The two REACHABLE proposals both rest partly on bytecode: 28/18 on the
   compiler-inserted super call, 31/33 on generated Room code that has no source
   file in the final_java_only tree. Both are therefore proposed as INFERRED.
3. UNREACHABLE proposals rest on the combination of the saved full-tree grep and
   the 0-hit bytecode lookup for that exact method. They do not cover hypothetical
   reflective/framework dispatch that leaves no source or bytecode call edge;
   no such dispatch was found for these methods (no res-XML/databinding use, no
   method-reference use, Parcel CREATORs use the Parcel constructors, not these
   methods).
