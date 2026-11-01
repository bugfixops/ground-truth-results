# R5 verdicts — batch 34 (1 row)

Scope: row verified OPEN in the main table of `phase3/work/batch34-merge-ready.md`.
No L1–L5 verdict file judges this row. Corpus as in batch28.md; P2 applies.
No decided rule covers a plain POJO setter row (D14–D16 are binding-only).

## 34/1 — FileTree.setType — stays OPEN — confirmed_by —

- Work-file identity: main-table row L182, OPEN, `—`.
- Definition: FileTree.java:159 (`isLeaf = (type == FileNode.Type.FILE)`).
  The work file notes ctors set the field directly.
- New grep (setters_getters_addItem.txt): every `.setType(` hit in the
  corpus names another type's method (Intent `sharingIntent.setType`,
  dialog/storage `setTitle` analogues are separate methods; no
  FileTree-typed receiver). Zero `.setType(` calls name a FileTree
  receiver. The `isLeaf` field is set by the ctors and read directly by
  `isFile()`, never through this setter in the corpus.
- Verdict: stays OPEN.
- What would change it: a printed FileTree.setType call site, or a
  saved full-repo grep. Never UNREACHABLE on corpus-zero alone (P2).
