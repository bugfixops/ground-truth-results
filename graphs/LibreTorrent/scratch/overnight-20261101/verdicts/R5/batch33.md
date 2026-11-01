# R5 verdicts — batch 33 (8 rows)

Scope: rows verified OPEN in the main table of `phase3/work/batch33-merge-ready.md`.
No L1–L5 verdict file judges these rows. Corpus as in batch28.md; P2 applies.
No decided rule covers a plain POJO compareTo, equals, getter, or setter row
(D6/D7 are hashCode/toString only; D14–D16 are binding-only).

## 33/24 — FileTree.compareTo — stays OPEN — confirmed_by —

- Work-file identity: main-table row L192, OPEN, `—`.
- Definition: FileTree.java:187–189 (`name.compareTo(another.getName())`).
- New grep (greps/R5/greps/compareTo_sort.txt): both file-tree sort sites
  sort `List<BencodeFileItem>` (BencodeFileTreeUtils.java:55,
  TorrentContentFileTreeUtils.java:55), dispatching BencodeFileItem.compareTo
  (BencodeFileItem.java:114), not FileTree.compareTo. No sort site sorts
  FileTree objects and no direct `.compareTo(` call names a FileTree
  receiver. This confirms the work file's note (BencodeFileTreeUtils sorts
  BencodeFileItem, not FileTree) and extends it to TorrentContentFileTreeUtils.
- Verdict: stays OPEN.
- What would change it: a printed sort/comparison site for FileTree
  objects, or a saved full-repo grep. Never UNREACHABLE on corpus-zero
  alone (P2).

## 33/26 — FileTree.equals — stays OPEN — confirmed_by —

- Work-file identity: main-table row L194, OPEN, `—`.
- Definition: FileTree.java:193 (body at :204, field `name.equals(...)`
  calls — String calls, not calls to this method).
- New grep (filetree_contains.txt, equals triage): no printed `.equals(`
  call names a FileTree receiver. The apparent lead
  `parentTree.contains(nodes[i])` (BencodeFileTreeUtils.java:100,
  TorrentContentFileTreeUtils.java:100) is FileTree.contains(String)
  (FileTree.java:80), implemented as `children.containsKey(name)` — a Map
  key lookup on Strings, not an equals dispatch on FileTree objects.
  No DiffUtil site compares FileTree objects.
- Verdict: stays OPEN.
- What would change it: a printed FileTree.equals caller, or a saved
  full-repo grep / a decided equals rule. Never UNREACHABLE on
  corpus-zero alone (P2).

## 33/30 — FileTree.getChildrenIndexes — stays OPEN — confirmed_by —

- Work-file identity: main-table row L198, OPEN, `—`.
- Definition: FileTree.java:100.
- New grep (misc_methods.txt): the only `getChildren*` hits in the corpus
  are the definitions themselves and `getChildren()` / `getChildrenCount()`
  call sites (AddTorrentViewModel.java:411/:420, DetailTorrentViewModel.java:230/:240)
  — never `getChildrenIndexes()`. Zero call sites in the corpus.
- Verdict: stays OPEN.
- What would change it: a printed FileTree.getChildrenIndexes call site,
  or a saved full-repo grep. Never UNREACHABLE on corpus-zero alone (P2).

## 33/31 — FileTree.getChildrenName — stays OPEN — confirmed_by —

- Work-file identity: main-table row L199, OPEN, `—`.
- Definition: FileTree.java:95.
- New grep (misc_methods.txt): as for 33/30 — zero `getChildrenName()`
  call sites in the corpus; only the definition and the distinct
  `getChildren()` / `getChildrenCount()` sites.
- Verdict: stays OPEN.
- What would change it: a printed FileTree.getChildrenName call site, or
  a saved full-repo grep. Never UNREACHABLE on corpus-zero alone (P2).

## 33/36 — FileTree.getType — stays OPEN — confirmed_by —

- Work-file identity: main-table row L204, OPEN, `—`.
- Definition: FileTree.java:153. The work file notes FileTree.isFile reads
  the type field directly.
- New grep (filetree_getType.txt, setters_getters_addItem.txt): every
  `.getType()` hit in the corpus names another type — FilePriority.getType
  (FilePriority.java:102; TorrentContentFileTree.java:96/:115/:136/:138/:156),
  FileManagerNode.getType (FileManagerDialog.java:441/:452), Uri/Intent/
  enclosure types. Zero hits name a FileTree receiver.
- Verdict: stays OPEN.
- What would change it: a printed FileTree.getType call site with a
  FileTree-typed receiver, or a saved full-repo grep. Never UNREACHABLE on
  corpus-zero alone (P2).

## 33/38 — FileTree.setIndex — stays OPEN — confirmed_by —

- Work-file identity: main-table row L206, OPEN, `—`.
- Definition: FileTree.java:142. The work file notes ctors set the field
  directly.
- New grep (setters_getters_addItem.txt, misc_methods.txt): zero
  `.setIndex(` call sites exist anywhere in the corpus (only the two
  definitions: FileTree.java:142, BencodeFileItem.java:76).
- Verdict: stays OPEN.
- What would change it: a printed FileTree.setIndex call site, or a
  saved full-repo grep. Never UNREACHABLE on corpus-zero alone (P2).

## 33/39 — FileTree.setName — stays OPEN — confirmed_by —

- Work-file identity: main-table row L207, OPEN, `—`.
- Definition: FileTree.java:131.
- New grep (setters_getters_addItem.txt): every `.setName(` hit names
  another type's method (libtorrent `add_torrent_params` `p` in
  TorrentSessionImpl.java:484/:1643, `*MutableParams.setName` in the
  add/detail ViewModels, Thread/Dialog setName/setTitle analogues).
  Zero hits name a FileTree receiver, and the FileTree ctors set the
  field directly.
- Verdict: stays OPEN.
- What would change it: a printed FileTree.setName call site, or a
  saved full-repo grep. Never UNREACHABLE on corpus-zero alone (P2).

## 33/40 — FileTree.setParent — stays OPEN — confirmed_by —

- Work-file identity: main-table row L208, OPEN, `—`.
- Definition: FileTree.java:125. The work file notes ctors set the field
  directly.
- New grep: zero `.setParent(` call sites exist in the corpus (no hit in
  any R5 grep; the field is assigned by the ctors, e.g. the
  BencodeFileTree/TorrentContentFileTree construction in the two
  `*FileTreeUtils.buildFileTree` methods, which pass the parent as a
  ctor argument).
- Verdict: stays OPEN.
- What would change it: a printed FileTree.setParent call site, or a
  saved full-repo grep. Never UNREACHABLE on corpus-zero alone (P2).
