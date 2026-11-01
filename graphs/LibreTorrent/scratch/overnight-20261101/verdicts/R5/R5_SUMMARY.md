# R5 Summary — LibreTorrent 29 uncovered OPEN rows (Stream A Phase 3 completion)

All 29 rows were verified OPEN in their main-table rows in
`phase3/work/batch<N>-merge-ready.md` before judging, and none appears in any
L1–L5 verdict file (L2 mentions 28/18, 114/22, 114/23 only as out-of-scope).
No work file was edited; verdicts live only under `phase3/verdicts/R5/`
(one file per batch) with saved greps under `phase3/verdicts/R5/greps/`.
Evidence standard: printed source lines or saved corpus greps (281-file
app-Java corpus at `~/workspace/overnight/stream-A/corpus/java`, plus L2's
saved greps where cited). confirmed_by is SOURCE or INFERRED only; OPEN rows
use —. No row flips on corpus-zero alone (P2), on a search 0, or on an
invented rule: where no decided rule covers a row's family, that is stated
in its verdict file.

## Totals

- Rows judged: **29**
- Flips to REACHABLE: **2** — 30/16 (SOURCE), 30/17 (SOURCE)
- Flips to UNREACHABLE: **0**
- Stays OPEN: **27**

## Flips to REACHABLE (2)

- 30/16 TorrentStateCode.fromValue — REACHABLE SOURCE. Its only printed
  caller, TorrentInfo.java:125 inside the Parcel ctor (30/2), is REACHABLE
  per L2 (30/2 SOURCE via caller 30/12, D20 MainFragment.java:162 storage
  site). D5b positive direction; reverts if 30/2 reverts.
- 30/17 TorrentStateCode.value — REACHABLE SOURCE. Printed callers inside
  two now-REACHABLE methods: TorrentInfo.java:155 inside writeToParcel
  (30/10, REACHABLE per L2) and TorrentStateCode.java:71 inside fromValue
  (30/16, this round). Either route alone suffices.

## Stays OPEN (27) with resolvers

- 28/18 AbstractInfoParcel.\<init\>() — printed `new AdvancedTorrentInfo()`
  no-arg site, or a saved full-repo grep for that ctor. (TorrentEngine.java:846
  calls the 12-arg ctor, not the no-arg ctor; its `super()` is the only
  no-arg super-call and is itself uncalled.)
- 28/25 AdvancedTorrentInfo.compareTo — printed sort/comparison site for
  AdvancedTorrentInfo objects, or a saved full-repo grep. No decided
  compareTo rule exists.
- 29/1 MagnetInfo.getUri — printed MagnetInfo.getUri() call site, or a
  saved full-repo grep. No decided plain-getter rule exists.
- 29/32 SessionStats.compareTo — printed sort/comparison site for
  SessionStats objects, or a saved full-repo grep. No decided compareTo
  rule exists.
- 30/5 TorrentInfo.compareTo — printed sort/comparison site for TorrentInfo
  objects (not the TorrentSorting String-name comparator), or a saved
  full-repo grep. No decided compareTo rule exists.
- 31/33 Torrent.\<init\> 8-arg — printed 8-arg `new Torrent(...)` site, or a
  printed generated-instantiation step (D5e entity rule; TorrentSessionImpl.java:263
  is the 7-arg ctor).
- 31/35 Torrent.equals — printed Torrent.equals caller, or a saved
  full-repo grep / a decided equals rule (none exists).
- 32/6 TorrentTagInfo.equals — printed TorrentTagInfo.equals caller, or a
  saved full-repo grep / a decided equals rule (none exists).
- 32/17 BencodeFileItem.setIndex — printed setIndex call site, or a saved
  full-repo grep. No decided plain-setter rule exists.
- 32/18 BencodeFileItem.setPath — printed setPath call site, or a saved
  full-repo grep. No decided plain-setter rule exists.
- 32/19 BencodeFileItem.setSize — printed setSize call site, or a saved
  full-repo grep. No decided plain-setter rule exists.
- 32/32 TorrentMetaInfo.equals — printed TorrentMetaInfo.equals caller, or a
  saved full-repo grep / a decided equals rule (none exists).
- 33/24 FileTree.compareTo — printed sort/comparison site for FileTree
  objects, or a saved full-repo grep. (Both file-tree sort sites sort
  BencodeFileItem lists.) No decided compareTo rule exists.
- 33/26 FileTree.equals — printed FileTree.equals caller, or a saved
  full-repo grep / a decided equals rule (none exists). (`contains`
  lead discharged: FileTree.contains(String) is a Map key lookup.)
- 33/30 FileTree.getChildrenIndexes — printed getChildrenIndexes call site,
  or a saved full-repo grep. No decided plain-getter rule exists.
- 33/31 FileTree.getChildrenName — printed getChildrenName call site, or a
  saved full-repo grep. No decided plain-getter rule exists.
- 33/36 FileTree.getType — printed FileTree.getType call site with a
  FileTree-typed receiver, or a saved full-repo grep. (All corpus
  `.getType()` hits name other types.) No decided plain-getter rule exists.
- 33/38 FileTree.setIndex — printed FileTree.setIndex call site, or a
  saved full-repo grep. No decided plain-setter rule exists.
- 33/39 FileTree.setName — printed FileTree.setName call site, or a saved
  full-repo grep. No decided plain-setter rule exists.
- 33/40 FileTree.setParent — printed FileTree.setParent call site, or a
  saved full-repo grep. No decided plain-setter rule exists.
- 34/1 FileTree.setType — printed FileTree.setType call site, or a saved
  full-repo grep. No decided plain-setter rule exists.
- 103/34 FileManagerNode.setEnabled — printed FileManagerNode.setEnabled
  call site, or a saved full-repo grep. No decided plain-setter rule exists.
- 103/35 FileManagerNode.setName — printed FileManagerNode.setName call
  site, or a saved full-repo grep. No decided plain-setter rule exists.
- 103/36 FileManagerNode.setType — printed FileManagerNode.setType call
  site, or a saved full-repo grep. No decided plain-setter rule exists.
- 103/40 FileManagerSpinnerAdapter.addItem — printed `addItem(...)`
  (singular) call site, distinct from `addItems`, or a saved full-repo
  grep. No decided rule exists for this row.
- 114/22 PreferenceActivityConfig.setFragment — printed setFragment call
  site, or a saved full-repo grep. No decided plain-setter rule exists.
- 114/23 PreferenceActivityConfig.setTitle — printed setTitle call site,
  or a saved full-repo grep. No decided plain-setter rule exists.

## Verification notes (corrections to brief assumptions, checked not assumed)

- 30/16, 30/17 each occur ONCE in batch30-merge-ready.md, in the main table
  (L178, L179); their stand/fall condition lives in DECISIONS.md D5b, not as
  a second row in the file, so no last-occurrence ambiguity exists.
- 31/33's conditional-table row (L87, Room-SET) is not a label row; the main
  row is L189, OPEN.
- 28/18's conditional row (L75) is a flip condition, not a label row; the
  main row is L345, OPEN.
- Batches 28–34 in this set are NOT all trio rows: only 30/16 and 30/17 are
  trio-adjacent (D5b dependency companions). The rest are plain ctor /
  compareTo / equals / getter / setter rows, judged under P2 and the
  absence of a covering decided rule — D5a/D5b/D19/D20/D22 were applied
  only where they actually govern (30/16, 30/17 via D5b; D20's L2 flips to
  30/2, 30/10, 30/12 reused, not re-decided).
- D14–D16 (binding getters/setters) were NOT extended to these plain POJO
  rows: their completeness arguments are binding-specific (generated code
  reads fields / calls setVariable only via `bind:`), and DECISIONS.md scopes
  them to batches 58–67.
- No pushes, no branch edits, no token used, no tick marker written.
