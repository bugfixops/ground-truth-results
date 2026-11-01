# LibreTorrent batch 103 — Phase 2 spot-check — UNVERIFIED spot-check, NOT a merge

- Batch: 103. Source checked: already-fetched local copies in ~/workspace/b103104-src/ (FileManagerDialog.java, FileManagerNode.java, FileManagerSpinnerAdapter.java) and ~/workspace/overnight/stream-A/corpus/java/; no connector fetch needed, no 429.
- Rows checked (12): samples 1, 6, 11, 16, 21, 26, 31, 36 PLUS must-include OPEN rows 34, 35, 37, 40 (left OPEN, no flip ordered in Phase 1c / open-closing round 2).
- Build/sampler/C1: not run (not this task). No edit made to the merge-ready file. No convention decided. D2 variants adopted in the merge-ready file were verified as filed; no strict launcher-entry revert was re-imposed (per task instruction).

## Per-row verdicts

| # | Method | Filed label | Verdict | Evidence (printed source) |
|---|---|---|---|---|
| 1 | FileManagerDialog.openHomeDirectory | REACHABLE SOURCE | PASS | FileManagerDialog.java:504 `openHomeDirectory()` in onOptionsItemSelected home branch; def :518-522 → goToDirectory. |
| 6 | FileManagerDialog.returnDirectoryUri | REACHABLE SOURCE | PASS | FileManagerDialog.java:510 `returnDirectoryUri()` in onOptionsItemSelected OK branch (non-SAVE mode); def :557-568. |
| 11 | FileManagerDialog.showReplaceFileDialog | REACHABLE SOURCE | PASS | FileManagerDialog.java:577 `showReplaceFileDialog()` in createFile (file exists, not replace); def :606-619. |
| 16 | FileManagerDialog$1.<init> | REACHABLE SOURCE | PASS | FileManagerDialog.java:176 `binding.fileName.addTextChangedListener(new TextWatcher() {`. |
| 21 | FileManagerDialog$2.onItemSelected | REACHABLE INFERRED | PASS | Registered FileManagerDialog.java:214 (spinner listener); def :216-233 (getItem, isDirectoryExists, jumpToDirectory); Spinner dispatch, not printed. |
| 26 | FileManagerDialog$MediaReceiver.onReceive | REACHABLE INFERRED | PASS | Registered FileManagerDialog.java:286 (filter :282-285 MEDIA_MOUNTED/UNMOUNTED, file scheme); def :687-690 → reloadSpinner(); broadcast dispatch, not printed. |
| 31 | FileManagerNode.getType | REACHABLE SOURCE | PASS | FileManagerDialog.java:441 (DIR check) and :452 (FILE check) in onItemClicked; def FileManagerNode.java:59-62. |
| 34 | FileManagerNode.setEnabled | OPEN — | PASS | Def FileManagerNode.java:75-78. No node-typed call in the printed/corpus files: corpus filemanager hits are only FileManagerAdapter.java:135 `itemView.setEnabled(item.isEnabled())` (a View receiver that reads isEnabled). Correctly left OPEN — no flip ordered, no saved full-repo grep claimed. |
| 35 | FileManagerNode.setName | OPEN — | PASS | Def FileManagerNode.java:53-56. No node-typed call found; the only same-name setter nearby is FileManagerSpinnerAdapter$StorageSpinnerItem.setName (a different class). Correctly left OPEN. |
| 36 | FileManagerNode.setType | OPEN — | PASS | Def FileManagerNode.java:65-68. No node-typed call found in the printed/corpus files. Correctly left OPEN (also a sample row). |
| 37 | FileManagerNode.toString | OPEN — | PASS | Def FileManagerNode.java:109-116. No node-typed toString/concatenation/logging use in the filemanager files; FileManagerDialog toString hits are Editable/Exception only. Correctly left OPEN. |
| 40 | FileManagerSpinnerAdapter.addItem | OPEN — | PASS | Def FileManagerSpinnerAdapter.java:105-108. Zero `.addItem(` calls tree-wide in the corpus check; only addItems at FileManagerDialog.java:210 and :645. Correctly left OPEN (singular vs plural distinguished, as filed). |

## Totals

- PASS: 12 / FAIL: 0 (of 12 checked).
- Proposed corrections: none.
