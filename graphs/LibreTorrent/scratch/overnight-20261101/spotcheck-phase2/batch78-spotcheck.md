# Spot-check — LibreTorrent batch 78 (Stream A Phase 2)

- Source file checked: `~/workspace/overnight/stream-A/work/batch78-merge-ready.md` (UNVERIFIED proposal, not a result; not edited).
- Method: each row below was re-derived from already-fetched printed source in `~/workspace/overnight/stream-A/corpus/java/` (no connector fetch needed, no 429, no missing file). No build/sampler/C1 run (not this task).
- Check set: sample rows 1, 6, 11, 16, 21, 26, 31, 36. No dated 2026-11-01 revision note in this file lists a Phase 1 label flip, so no extra changed rows apply.
- Filed labels: all 8 checked rows filed REACHABLE proposed (confirmed_by recorded as — / SOURCE or — / INFERRED in this file's two-column notation; the second value is the one judged here).

## Per-row verdicts

- Row 1 — AddTagDialog.lambda$addTag$5 — PASS. Filed REACHABLE INFERRED. Subscribe success lambda in addTag: AddTagDialog.java:204 (`() -> finish(...)` OK) within the subscribe at :200–205; addTag reached via the positive-button click (initAlertDialog :187). Rx subscribe dispatch unprinted = INFERRED as filed.
- Row 6 — AddTagDialog.lambda$initLayoutView$1 — PASS. Filed REACHABLE INFERRED. Color click listener AddTagDialog.java:153–155 (`ColorPickerDialog.newBuilder().setColor(viewModel.state.getColor()).show(activity)`); initLayoutView called from onCreateDialog :131. Framework click dispatch unprinted = INFERRED as filed.
- Row 11 — AddTagDialog.onCreateDialog — PASS. Filed REACHABLE SOURCE. Body AddTagDialog.java:112–134 (ViewModelProvider get AddTagViewModel :117–118, setInitValues :121 or setRandomColor :124, binding inflate, initLayoutView :131, initAlertDialog :132, returns alert). SOURCE as filed under the file's framework-after-printed-show treatment.
- Row 16 — AddTagDialog$1.beforeTextChanged — PASS. Filed REACHABLE SOURCE. Empty body AddTagDialog.java:140–141; TextWatcher registered at :138 (same registration as row 15's afterTextChanged). Registered callback on a printed route = SOURCE as filed.
- Row 21 — AddTagState.getName — PASS. Filed REACHABLE SOURCE. Definition AddTagState.java:43–45. Direct printed callers: AddTagDialog.java:160 (checkName, via viewModel.state.getName()) and AddTagViewModel.java:59/:61 (saveTag). Direct printed calls = SOURCE as filed.
- Row 26 — AddTagViewModel.lambda$saveTag$0 — PASS. Filed REACHABLE INFERRED. Completable.fromCallable body AddTagViewModel.java:63–74 (getByName → throw TagAlreadyExistsException or insert, else update); subscribed in AddTagDialog.addTag :200. Rx fromCallable dispatch unprinted = INFERRED as filed.
- Row 31 — AddTorrentActivity.<clinit> — PASS. Filed REACHABLE INFERRED. Static TAG at AddTorrentActivity.java:73 (`AddTorrentActivity.class.getSimpleName()`, not a compile-time constant), so a <clinit> exists; it runs on first class use, i.e. framework instantiation after AddLinkDialog.addLink's startActivity (AddLinkDialog.java:283–285). Class-load step unprinted = INFERRED as filed. (The file's <clinit>-timing flag is noted, not decided here; the label stands.)
- Row 36 — AddTorrentActivity.getUri — PASS. Filed REACHABLE SOURCE. Definition AddTorrentActivity.java:350–360; called AddTorrentActivity.java:310 (observeDecodeState UNKNOWN branch → startDecode). Direct printed call = SOURCE as filed.

## Totals

- Rows checked: 8. PASS: 8. FAIL: 0.

## Proposed corrections

- None. No label or confirmed_by change proposed; the merge-ready file was not edited.
