# R5 verdicts — batch 28 (2 rows)

Scope: rows verified OPEN in the main table of `phase3/work/batch28-merge-ready.md`
before any R5 change. No L1–L5 verdict file judges these rows (L2/batch28.md
covers trio rows only and names 28/18 as out of scope, untouched).
Corpus: `~/workspace/overnight/stream-A/corpus/java` (281 app-Java files) plus
L2's saved greps where cited. Corpus-zero alone is never UNREACHABLE (P2);
no decided rule covers a plain ctor or a compareTo row (D6/D7 cover
hashCode/toString only; D14–D16 are binding-only and do not extend).

## 28/18 — AbstractInfoParcel.\<init\>() — stays OPEN — confirmed_by —

- Work-file identity: main-table row L345, OPEN, `—`. (L75 is the conditional
  flip table, not a label row.)
- Definition: AbstractInfoParcel:36–39. Sole printed super-call site is
  `AdvancedTorrentInfo()` :49–52 (`super()`), per the work file.
- New grep (greps/R5/greps/new_AdvancedTorrentInfo.txt): the only
  `new AdvancedTorrentInfo` sites in the corpus are TorrentEngine.java:846
  (the 12-arg ctor — verified: it calls `super(torrentId)` at
  AdvancedTorrentInfo.java:54+, NOT the no-arg ctor), the CREATOR body
  AdvancedTorrentInfo.java:125 (`new AdvancedTorrentInfo(source)`), and the
  newArray return at :131. No `new AdvancedTorrentInfo()` no-arg site exists
  in the corpus. Grep of `super()` across `core/model/data/` finds only
  AdvancedTorrentInfo.java:51 (greps/R5/greps/super_noarg.txt); no other
  subclass calls the no-arg super-ctor. Other-sourcesets grep: no hits.
- Verdict: stays OPEN. The no-arg ctor's only printed entry is itself
  uncalled; the 12-arg TorrentEngine site does not reach it.
- What would change it: a printed `new AdvancedTorrentInfo()` no-arg site,
  or a saved full-repo grep for that ctor (the work file's stated resolver).
  Never UNREACHABLE on this evidence.

## 28/25 — AdvancedTorrentInfo.compareTo (Object) — stays OPEN — confirmed_by —

- Work-file identity: main-table row L352, OPEN, `—`.
- Definition: AdvancedTorrentInfo.java:136–139 (`torrentId.compareTo(...)`).
- New grep (greps/R5/greps/compareTo_sort.txt): every `Collections.sort` /
  `.sort(` / `.sorted(` site in the corpus sorts a different type —
  BencodeFileItem (BencodeFileTreeUtils.java:55, TorrentContentFileTreeUtils.java:55),
  PeerInfo (PeerListAdapter.java:80), TrackerItem (TrackerListAdapter.java:95),
  FeedItem (FeedItemsAdapter.java:85), FeedChannelItem
  (FeedChannelListAdapter.java:113), FileManagerNode via a comparator
  (FileManagerAdapter.java:91), AnnounceEntry tiers via a comparator
  (TorrentSessionImpl.java:631), or TorrentInfo names via TorrentSorting
  (TorrentSorting.java:42–44, MainFragment.java:293/:341, TorrentService.java:287/:304).
  No sort site sorts AdvancedTorrentInfo objects, and no direct
  `.compareTo(` call names an AdvancedTorrentInfo receiver.
- No decided rule covers compareTo: D6/D7 are hashCode/toString only.
- Verdict: stays OPEN.
- What would change it: a printed sort/comparison site for
  AdvancedTorrentInfo objects, or a saved full-repo grep. Never UNREACHABLE
  on corpus-zero alone (P2).
