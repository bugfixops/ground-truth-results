# LibreTorrent batch 90 — Phase 2 spot-check — UNVERIFIED (spot-check only, not a merge verdict)

- Batch: 90. Work file checked: `~/workspace/overnight/stream-A/work/batch90-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (9): sample rows 1, 6, 11, 16, 21, 26, 31, 36, plus must-include row 28 (row 16 is in both sets, counted once). Phase 1c made NO label flip in this batch (D1 cosmetic confirmed_by normalisation only: rows 16 and 28 INFERRED → —, labels unchanged); both rows are verified below as OPEN with confirmed_by —.
- Method: re-derived from already-fetched source on disk (`~/workspace/b89-90-src/`, `~/workspace/ruleF-src/`, `~/workspace/b90929495969799102-openclose2-src/` greps); no GitHub connector fetch was needed, no 429 hit, no file missing.
- No edit was made to the merge-ready file. No push. Build/sampler/C1: not run (not this task).
- Strict-entry caveat: the launcher → DetailTorrentActivity → DetailTorrentFragment step was not printed in this pass; under a strict entry-route rule all REACHABLE rows would revert to OPEN. That convention is undecided and NOT decided here. Row 5's layout basis (fragment_detail_torrent_info.xml) was not printed, so row 5 is not in the checked set; it is unaffected by this spot-check.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (file:line, local copy) |
|---|---|---|---|---|
| 1 | MsgDetailTorrentViewModel.fragmentInActionMode | REACHABLE / SOURCE | PASS | Callers DetailTorrentTrackersFragment.java:308 (true) and :333 (false), DetailTorrentFilesFragment.java:388 (true) and :411 (false) in the ruleF tree copy; def MsgDetailTorrentViewModel.java:31-34. |
| 6 | TorrentDetailsInfo.getMetaInfo | REACHABLE / SOURCE | PASS | Caller DetailTorrentViewModel (dvm_fresh.java):536 (makeFileTree `info.getMetaInfo()`); def TorrentDetailsInfo.java:102-105. |
| 11 | TorrentDetailsInfo.setDirName | REACHABLE / SOURCE | PASS | Caller DetailTorrentViewModel (dvm_fresh.java):454 (mutableParamsCallback `info.setDirName(...)`); def TorrentDetailsInfo.java:83-86. |
| 16 | TorrentDetailsInfo.toString | OPEN / — | PASS | Def TorrentDetailsInfo.java:115-125. Saved 252-file grep (grep_class_TorrentDetailsInfo.txt) shows only the definition file and ViewModel field/construction sites, no .toString() call or concatenation site on this type; grep_toString_calls.txt has no hit naming this type. OPEN with confirmed_by — as filed (D1 normalisation verified). A saved full-repo grep covering implicit dispatch is still the named resolver; the toString-dispatch convention is undecided and NOT decided here. |
| 21 | TorrentDetailsMutableParams.isPrioritiesChanged | REACHABLE / SOURCE | PASS | Caller DetailTorrentViewModel (dvm_fresh.java):504 (checkParamsChanged, BR.prioritiesChanged branch `mutableParams.isPrioritiesChanged()`); def TorrentDetailsMutableParams.java:74-77. |
| 26 | TorrentDetailsMutableParams.setPrioritiesChanged | REACHABLE / SOURCE | PASS | Caller DetailTorrentViewModel (dvm_fresh.java):334 (applyPriority subscribe lambda `mutableParams.setPrioritiesChanged(true)`); def TorrentDetailsMutableParams.java:79-82. |
| 28 | TorrentDetailsMutableParams.toString | OPEN / — | PASS | Def TorrentDetailsMutableParams.java:99-109. Saved 252-file grep (grep_class_TorrentDetailsMutableParams.txt) shows only the definition file and ViewModel field/construction sites, no .toString() call or concatenation site on this type. OPEN with confirmed_by — as filed (D1 normalisation verified). Same named resolver and undecided convention as row 16. |
| 31 | DetailTorrentInfoFragment.checkNameField | REACHABLE / SOURCE | PASS | Callers DetailTorrentInfoFragment.java:226 (subscribeAlertDialog POSITIVE branch) and :320 (TextWatcher afterTextChanged in initEditNameDialog); def :259-272. |
| 36 | DetailTorrentInfoFragment.lambda$onCreateView$1 | REACHABLE / INFERRED | PASS | editNameButton click lambda DetailTorrentInfoFragment.java:111 (`showEditNameDialog()`); View click dispatch unprinted → INFERRED correct. Numbering by source order, not bytecode-verified. |

## Totals

- PASS: 9 / 9. FAIL: 0 / 9.

## Proposed corrections

- None. No row label or confirmed_by needs changing on the evidence checked. Rows 16 and 28 are confirmed OPEN with confirmed_by — exactly as the Phase 1c D1 normalisation states.
