# R5 verdicts — batch 31 (2 rows)

Scope: rows verified OPEN in the main table of `phase3/work/batch31-merge-ready.md`.
No L1–L5 verdict file judges these rows. Corpus as in batch28.md; P2 applies.

## 31/33 — Torrent.\<init\>(String,String,Uri,String,boolean,long,boolean,boolean) (8-arg) — stays OPEN — confirmed_by —

- Work-file identity: main-table row L189, OPEN, `—`. (L87 is the Room-SET
  conditional table, not a label row for this ctor.)
- Definition: Torrent.java:89–101 (8-arg ctor, delegates to the 7-arg ctor
  at :98 then sets magnet at :100). The delegation inside the ctor is not
  a caller of it.
- Decided rule: D5e (Room-entity-status rule) — a Room `@Entity`'s ctor is
  NOT flipped to REACHABLE on entity status alone; only a printed
  construction or a printed generated-instantiation step counts.
- New grep (greps/R5/greps/new_Torrent.txt): the only `new Torrent(` sites
  in the corpus are Torrent.java:162 (the Parcel-ctor CREATOR body) and
  TorrentSessionImpl.java:263, which passes 7 arguments (id, downloadPath,
  name, addPaused, currentTimeMillis, sequentialDownload,
  firstLastPiecePriority) — the 7-arg ctor at Torrent.java:72, with magnet
  set afterwards via `setMagnetUri` (TorrentSessionImpl:277, per the work
  file). No 8-arg construction site exists in the corpus.
- Verdict: stays OPEN under D5e.
- What would change it: a printed 8-arg `new Torrent(...)` site, or a
  printed generated-instantiation step for the 8-arg ctor. Never
  UNREACHABLE on corpus-zero alone (P2).

## 31/35 — Torrent.equals — stays OPEN — confirmed_by —

- Work-file identity: main-table row L191, OPEN, `—`.
- Definition: Torrent.java:179–182 (identity or equal `id`).
- New grep (greps/R5/greps/equals_contains_triage.txt, equals_other.txt):
  the only Torrent.equals-shaped evidence in the corpus is the definition
  body itself (Torrent.java:181, field `id.equals(...)` calls — a String
  call, not a Torrent call). No printed `.equals(` call names a Torrent
  receiver, and no DiffUtil `areContentsTheSame` site compares Torrent
  objects (DiffUtil sites in the corpus compare DownloadableFileItem,
  TorrentContentFileItem, PeerItem, TrackerItem, FeedItemsListItem,
  FeedChannelItem, and FileManagerNode items — none is Torrent). Repo
  lookups use id strings (TorrentSessionImpl:280 `repo.getTorrentById(torrent.id)`),
  per the work file.
- No decided rule covers a plain POJO equals row (D6/D7 are hashCode/
  toString only; the D6 trap note treats `List.contains` as equals-only
  for hashCode purposes and does not itself decide any equals row, and no
  contains site over Torrent objects is printed in any case).
- Verdict: stays OPEN.
- What would change it: a printed Torrent.equals caller (direct call, or
  a printed contains/DiffUtil site over Torrent objects from REACHABLE
  code), or a saved full-repo grep / a decided equals rule. Never
  UNREACHABLE on corpus-zero alone (P2).
