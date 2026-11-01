# Spot-check — LibreTorrent batch 79 (Stream A Phase 2)

- Source file checked: `~/workspace/overnight/stream-A/work/batch79-merge-ready.md` (UNVERIFIED proposal, not a result; not edited).
- Method: each row below was re-derived from already-fetched printed source in `~/workspace/overnight/stream-A/corpus/java/` (no connector fetch needed, no 429, no missing file). No build/sampler/C1 run (not this task).
- Check set: sample rows 1, 6, 11, 16, 21, 26, 31, 36. No dated 2026-11-01 revision note in this file lists a Phase 1 label flip, so no extra changed rows apply.
- Filed labels: all 8 checked rows filed REACHABLE.

## Per-row verdicts

- Row 1 — AddTorrentActivity.lambda$initLayout$0 — PASS. Filed REACHABLE INFERRED. TabLayoutMediator tab-config lambda AddTorrentActivity.java:291–302 (attach :302) inside initLayout :277–303, called from onCreate :138. TabLayoutMediator attach dispatch unprinted = INFERRED as filed.
- Row 6 — AddTorrentActivity.onOptionsItemSelected — PASS. Filed REACHABLE INFERRED. Override AddTorrentActivity.java:552–570; add-menu branch calls addTorrent :557–558. Framework menu dispatch unprinted = INFERRED as filed.
- Row 11 — AddTorrentActivity.onStopDecode — PASS (label; confirmed_by convention note below). Filed REACHABLE SOURCE. Body AddTorrentActivity.java:336–347; called from the observe lambda at :323 (observeDecodeState :305–326, LiveData observe at :307). The call site naming the method is printed; whether a call inside a LiveData-observe body counts as SOURCE (this file) or INFERRED (cf. batch 76's Rx-body rule) is a merger convention question, NOT decided here — no flip proposed. Label REACHABLE holds either way.
- Row 16 — AddTorrentActivity$1.<init> — PASS. Filed REACHABLE SOURCE. Anonymous PermissionManager.Callback constructed in onCreate at AddTorrentActivity.java:105 (construction site :105–129). <init> runs at that printed construction site = SOURCE as filed. ($1 = first anonymous class in source order, as the file notes.)
- Row 21 — AddTorrentFilesFragment.<clinit> — PASS (label and confirmed_by; minor citation correction proposed below, no label change). Filed REACHABLE INFERRED. A <clinit> exists because of the non-constant static initialiser TAG at AddTorrentFilesFragment.java:55 (`getSimpleName()`); class initialisation precedes newInstance (row 25). JVM class-load dispatch unprinted = INFERRED as filed. The file's own caveat stands: if the merger requires an explicit static block, this row reverts to OPEN — recorded, not decided here.
- Row 26 — AddTorrentFilesFragment.onAttach — PASS. Filed REACHABLE INFERRED. Body AddTorrentFilesFragment.java:87–93. FragmentManager lifecycle dispatch unprinted = INFERRED as filed.
- Row 31 — AddTorrentFilesFragment.onSaveInstanceState — PASS. Filed REACHABLE INFERRED. Body AddTorrentFilesFragment.java:156–162. Lifecycle dispatch unprinted = INFERRED as filed.
- Row 36 — AddTorrentFilesFragment.subscribeAdapter — PASS. Filed REACHABLE SOURCE. Body AddTorrentFilesFragment.java:111–125; called from onStart :108. Direct printed call = SOURCE as filed.

## Totals

- Rows checked: 8. PASS: 8. FAIL: 0.

## Proposed corrections

- One citation refinement, NO label or confirmed_by change: row 21's evidence cites both TAG (:55) and TAG_LIST_FILES_STATE (:57) as "non-constant initialisers". TAG_LIST_FILES_STATE = `"list_files_state"` (AddTorrentFilesFragment.java:57) IS a compile-time string constant and does not by itself force a <clinit>; the <clinit> is established by TAG at :55 alone (`getSimpleName()`). Proposed correction: cite only :55 as the <clinit> evidence. Label (REACHABLE) and confirmed_by (INFERRED) are unchanged. The merge-ready file was not edited; this correction is recorded here for the coordinator.
- No other corrections. The row 11 SOURCE/INFERRED boundary question is left for the merger (see verdict above).
