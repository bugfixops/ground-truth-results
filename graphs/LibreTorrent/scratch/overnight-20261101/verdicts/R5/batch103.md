# R5 verdicts — batch 103 (4 rows)

Scope: rows verified OPEN in the main table of `phase3/work/batch103-merge-ready.md`.
No L1–L5 verdict file judges these rows. Corpus as in batch28.md; P2 applies.
No decided rule covers a plain POJO setter row or an adapter addItem row
(D14–D16 are binding-only).

## 103/34 — FileManagerNode.setEnabled — stays OPEN — confirmed_by —

- Work-file identity: main-table row L228, OPEN, `—`.
- Definition: FileManagerNode.java:75–78. The work file notes the dialog
  only reads `isEnabled`.
- New grep (setters_getters_addItem.txt): every `.setEnabled(` hit names a
  View/widget receiver (ProxySettingsFragment switches, etc.); the one
  FileManagerNode-adjacent hit is FileManagerAdapter.java:135
  `itemView.setEnabled(item.isEnabled())` — a View call that READS the
  getter, not a call to FileManagerNode.setEnabled. FileManagerNode's
  `enabled` field is set by its ctor (FileManagerNode.java:39–43).
  Zero setter call sites in the corpus.
- Verdict: stays OPEN.
- What would change it: a printed FileManagerNode.setEnabled call site,
  or a saved full-repo grep. Never UNREACHABLE on corpus-zero alone (P2).

## 103/35 — FileManagerNode.setName — stays OPEN — confirmed_by —

- Work-file identity: main-table row L229, OPEN, `—`.
- Definition: FileManagerNode.java:53–56.
- New grep (setters_getters_addItem.txt): every `.setName(` hit names
  another type (libtorrent params `p` in TorrentSessionImpl.java:484/:1643,
  `*MutableParams.setName` in the add/detail ViewModels, Thread.setName).
  Zero hits name a FileManagerNode receiver. The field is set by the ctor.
- Verdict: stays OPEN.
- What would change it: a printed FileManagerNode.setName call site, or
  a saved full-repo grep. Never UNREACHABLE on corpus-zero alone (P2).

## 103/36 — FileManagerNode.setType — stays OPEN — confirmed_by —

- Work-file identity: main-table row L230, OPEN, `—`.
- Definition: FileManagerNode.java:65–68.
- New grep (setters_getters_addItem.txt): every `.setType(` hit names
  another type (Intent.setType, etc.). Zero hits name a FileManagerNode
  receiver. The field is set by the ctor (FileManagerNode.java:39).
- Verdict: stays OPEN.
- What would change it: a printed FileManagerNode.setType call site, or
  a saved full-repo grep. Never UNREACHABLE on corpus-zero alone (P2).

## 103/40 — FileManagerSpinnerAdapter.addItem — stays OPEN — confirmed_by —

- Work-file identity: main-table row L234, OPEN, `—`.
- Definition: FileManagerSpinnerAdapter.java:105–108 (singular `addItem`).
- New grep (setters_getters_addItem.txt, misc_methods.txt): zero
  `.addItem(` call sites exist anywhere in the corpus — the only
  `addItem*` hits are `addItemDecoration` (RecyclerView API, unrelated)
  and the plural `addItems` used by FileManagerDialog.java:210/:645
  (`storageAdapter.addItems(spinnerItems)`), exactly as the work file
  states. The singular method is defined but never called in the corpus.
- Verdict: stays OPEN.
- What would change it: a printed `addItem(...)` call site (distinct from
  `addItems`), or a saved full-repo grep. Never UNREACHABLE on
  corpus-zero alone (P2).
