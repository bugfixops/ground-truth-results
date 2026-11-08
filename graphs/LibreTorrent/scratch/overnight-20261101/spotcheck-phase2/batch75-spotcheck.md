# Spot-check — LibreTorrent batch 75 (Stream A Phase 2)

- Source file checked: `~/workspace/overnight/stream-A/work/batch75-merge-ready.md` (UNVERIFIED proposal, not a result; not edited).
- Method: each row below was re-derived from already-fetched printed source in `~/workspace/overnight/stream-A/corpus/java/` (no connector fetch needed, no 429, no missing file). No build/sampler/C1 run (not this task).
- Check set: sample rows 1, 6, 11, 16, 21, 26, 31, 36. No dated 2026-11-01 revision note in this file lists a Phase 1 label flip, so no extra changed rows apply.
- Filed labels: all 8 checked rows filed REACHABLE.

## Per-row verdicts

- Row 1 — AddFeedDialog.initAlertDialog — PASS. Filed REACHABLE SOURCE. Called AddFeedDialog.java:255 from initLayoutView; body :258–288, setOnShowListener :275. Direct printed call = SOURCE as filed.
- Row 6 — AddFeedDialog.lambda$initAlertDialog$6 — PASS (label; confirmed_by convention note below). Filed REACHABLE SOURCE. One of the four button click lambdas in initAlertDialog: AddFeedDialog.java:279 (edit), :280 (delete), :283 (add), :286 (cancel), installed by the setOnShowListener body at :275–288, itself reached via initAlertDialog (:255) from initLayoutView from onCreateDialog. The lambda body is printed and registered on a printed route, so the REACHABLE label holds. ($n-to-body mapping within the $4–$7 group is not bytecode-verified, as the file notes for the group; the label does not turn on which of the four buttons $6 is.)
- Row 11 — AddFeedDialog.lambda$new$0 — PASS. Filed REACHABLE INFERRED. Field lambda AddFeedDialog.java:112–113 (onFocusChanged → switchClipboardButton), registered onCreateDialog :207, removed onDestroyView :215. Framework focus-change dispatch unprinted = INFERRED as filed.
- Row 16 — AddFeedDialog.newInstance(Uri) — PASS. Filed REACHABLE SOURCE. Called AddFeedActivity.java:63 from onCreate (else branch); body AddFeedDialog.java:78–87. Direct printed call = SOURCE as filed.
- Row 21 — AddFeedDialog.onResume — PASS (label; confirmed_by convention note below). Filed REACHABLE SOURCE. Body AddFeedDialog.java:141–158, key listener installed :146. Standard lifecycle edge as the file treats it; see convention note.
- Row 26 — AddFeedDialog.subscribeClipboardManager — PASS (label; confirmed_by convention note below). Filed REACHABLE SOURCE. Body AddFeedDialog.java:100–103 (`addPrimaryClipChangedListener(clipListener)` :102), called from onStart :175. Direct printed call = SOURCE as filed.
- Row 31 — AddFeedDialog$1.afterTextChanged — PASS (label; confirmed_by convention note below). Filed REACHABLE SOURCE. Body AddFeedDialog.java:230–234, TextWatcher registered :222. Registered callback on a printed route; see convention note.
- Row 36 — AddFeedDialog$2.beforeTextChanged — PASS (label; confirmed_by convention note below). Filed REACHABLE SOURCE. Empty body AddFeedDialog.java:238, TextWatcher registered :236. Registered callback on a printed route; see convention note.

## Convention note (not a failure, not decided here)

- This file marks "standard View click / dialog listener / lifecycle edges" as SOURCE (rows 6, 21, 31, 36), while batches 77–80 mark comparable listener/lifecycle dispatch as INFERRED. Whether a printed registration site alone makes a callback SOURCE, or whether unprinted framework dispatch makes it INFERRED, is a merger convention question. It is NOT decided here and no confirmed_by flip is proposed; every REACHABLE label above is verified on printed evidence regardless of which side of that boundary the merger adopts.

## Totals

- Rows checked: 8. PASS: 8. FAIL: 0.

## Proposed corrections

- None. No label or confirmed_by change proposed; the merge-ready file was not edited.
