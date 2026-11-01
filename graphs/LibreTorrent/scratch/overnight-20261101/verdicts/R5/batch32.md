# R5 verdicts — batch 32 (5 rows)

Scope: rows verified OPEN in the main table of `phase3/work/batch32-merge-ready.md`.
No L1–L5 verdict file judges these rows (L2/batch32.md covers trio and
$1.\<init\> rows only). Corpus as in batch28.md; P2 applies. No decided rule
covers a plain POJO equals row or a plain POJO setter row (D14–D16 are
binding-only and do not extend).

## 32/6 — TorrentTagInfo.equals — stays OPEN — confirmed_by —

- Work-file identity: main-table row L160, OPEN, `—`.
- Definition: TorrentTagInfo.java:63 (body at :70, `torrentId.equals(...)`
  on a String field — not a call to this method).
- New grep (equals triage files): no printed `.equals(` call names a
  TorrentTagInfo receiver, and no DiffUtil site compares TorrentTagInfo
  objects. TorrentTagInfo travels through Room DAO / repository paths
  (TagInfoDao, TorrentRepositoryImpl), not through an equals site.
- Verdict: stays OPEN.
- What would change it: a printed TorrentTagInfo.equals caller, or a
  saved full-repo grep / a decided equals rule. Never UNREACHABLE on
  corpus-zero alone (P2).

## 32/17 — BencodeFileItem.setIndex — stays OPEN — confirmed_by —

- Work-file identity: main-table row L171, OPEN, `—`.
- Definition: BencodeFileItem.java:76. The work file notes Utils uses the
  ctor, not setters.
- New grep (greps/R5/greps/setters_getters_addItem.txt, misc_methods.txt):
  zero `.setIndex(` call sites exist anywhere in the corpus (only the
  definition at BencodeFileItem.java:76 and the FileTree definition at
  FileTree.java:142). Construction goes through the ctor
  (Utils.java:145 `new BencodeFileItem`, per L2) and fields are written
  by writeToParcel, not by setters.
- Verdict: stays OPEN.
- What would change it: a printed BencodeFileItem.setIndex call site, or
  a saved full-repo grep. Never UNREACHABLE on corpus-zero alone (P2).

## 32/18 — BencodeFileItem.setPath — stays OPEN — confirmed_by —

- Work-file identity: main-table row L172, OPEN, `—`.
- Definition: BencodeFileItem.java:56.
- New grep (same files as 32/17): zero `.setPath(` call sites exist
  anywhere in the corpus (only the definition itself).
- Verdict: stays OPEN.
- What would change it: a printed BencodeFileItem.setPath call site, or
  a saved full-repo grep. Never UNREACHABLE on corpus-zero alone (P2).

## 32/19 — BencodeFileItem.setSize — stays OPEN — confirmed_by —

- Work-file identity: main-table row L173, OPEN, `—`.
- Definition: BencodeFileItem.java:66.
- New grep (same files as 32/17): zero `.setSize(` call sites on a
  BencodeFileItem anywhere in the corpus (the only `.setSize(` hit is
  FileManagerSpinnerAdapter.java:89, a different class's method).
- Verdict: stays OPEN.
- What would change it: a printed BencodeFileItem.setSize call site, or
  a saved full-repo grep. Never UNREACHABLE on corpus-zero alone (P2).

## 32/32 — TorrentMetaInfo.equals — stays OPEN — confirmed_by —

- Work-file identity: main-table row L186, OPEN, `—`.
- Definition: TorrentMetaInfo.java:172 (body at :182–185, field
  `.equals(...)` calls on Strings — not calls to this method).
- New grep (equals triage files): no printed `.equals(` call names a
  TorrentMetaInfo receiver, and no DiffUtil site compares TorrentMetaInfo
  objects.
- Verdict: stays OPEN.
- What would change it: a printed TorrentMetaInfo.equals caller, or a
  saved full-repo grep / a decided equals rule. Never UNREACHABLE on
  corpus-zero alone (P2).
