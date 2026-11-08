# R5 verdicts — batch 29 (2 rows)

Scope: rows verified OPEN in the main table of `phase3/work/batch29-merge-ready.md`.
No L1–L5 verdict file judges these rows. Corpus as in batch28.md; P2 applies;
no decided rule covers a plain getter or a compareTo row.

## 29/1 — MagnetInfo.getUri — stays OPEN — confirmed_by —

- Work-file identity: main-table row L200, OPEN, `—`.
- Definition: MagnetInfo.java:95–98 (`return uri;`); the `uri` field is
  private (MagnetInfo.java:35), so the getter is the only access path — but
  that does not create a caller.
- New grep (greps/R5/greps/getUri.txt and misc_methods.txt): every
  `.getUri(` hit in the corpus names another type's method (TorrentStream
  session, SafFileSystem files, feed-parser elements, NanoHTTPD session).
  Zero hits name a MagnetInfo receiver, and no `MagnetInfo::getUri` method
  reference exists. The work file's note stands: TorrentEngine uses
  `getSha1hash()`, AddTorrentViewModel uses `getName()`/`getSha1hash()`/
  `getFilePriorities()`.
- No decided rule covers a plain POJO getter.
- Verdict: stays OPEN.
- What would change it: a printed `MagnetInfo.getUri()` call site, or a
  saved full-repo grep. Never UNREACHABLE on corpus-zero alone (P2).

## 29/32 — SessionStats.compareTo — stays OPEN — confirmed_by —

- Work-file identity: main-table row L231, OPEN, `—`.
- Definition: SessionStats.java:110–114 (`parcelId.compareTo(...)`).
- New grep (greps/R5/greps/compareTo_sort.txt): no sort site in the corpus
  sorts SessionStats objects (sort sites enumerated in batch28.md, 28/25);
  SessionStats travels singly via the listener/Flowable
  (TorrentInfoProvider:480–485, per the work file), not in a sorted
  collection. No direct `.compareTo(` call names a SessionStats receiver.
- No decided rule covers compareTo.
- Verdict: stays OPEN.
- What would change it: a printed sort/comparison site for SessionStats
  objects, or a saved full-repo grep. Never UNREACHABLE on corpus-zero
  alone (P2).
