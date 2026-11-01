# Spot-check — LibreTorrent batch 77 (Stream A Phase 2)

- Source file checked: `~/workspace/overnight/stream-A/work/batch77-merge-ready.md` (UNVERIFIED proposal, not a result; not edited).
- Method: each row below was re-derived from already-fetched printed source in `~/workspace/overnight/stream-A/corpus/java/` (no connector fetch needed, no 429, no missing file). No build/sampler/C1 run (not this task).
- Check set: sample rows 1, 6, 11, 16, 21, 26, 31, 36. No dated 2026-11-01 revision note in this file lists a Phase 1 label flip, so no extra changed rows apply.
- Filed labels: all 8 checked rows filed REACHABLE proposed (confirmed_by recorded as — / SOURCE or — / INFERRED in this file's two-column notation; the second value is the one judged here).

## Per-row verdicts

- Row 1 — AddLinkDialog.lambda$initAlertDialog$4 — PASS. Filed REACHABLE INFERRED. One of the two View onClick bodies in initAlertDialog: AddLinkDialog.java:240 (addButton → addLink) and :243–244 (cancelButton → finish CANCEL), installed by the setOnShowListener body at :238–245, reached via initLayoutView :225 from onCreateDialog. ($n-to-body mapping within the group is unverified, as the file itself notes; the label holds for either body.) Framework click dispatch unprinted = INFERRED as filed.
- Row 6 — AddLinkDialog.lambda$onResume$0 — PASS. Filed REACHABLE INFERRED. Body AddLinkDialog.java:93–111 (onResume); setOnKeyListener lambda at :98, BACK + ACTION_DOWN → onBackPressed :103. Framework key dispatch unprinted = INFERRED as filed.
- Row 11 — AddLinkDialog.onCreateDialog — PASS. Filed REACHABLE SOURCE. Body AddLinkDialog.java:171–191 (ViewModelProvider get AddLinkViewModel :176–177, binding inflate :184, initLayoutView :187, focus listener registration :189, returns alert :191). Framework calls it after the printed show at AddLinkActivity.java:32 (newInstance :31). SOURCE as filed under the file's framework-after-printed-show treatment.
- Row 16 — AddLinkDialog.showClipboardDialog — PASS. Filed REACHABLE SOURCE. Body AddLinkDialog.java:248–259 (isAdded guard, child FragmentManager, ClipboardDialog.newInstance + show if absent). Called from the clipboardButton click listener at AddLinkDialog.java:221 (row 4's click listener in this batch's numbering, inside initLayoutView). Printed call on a printed route = SOURCE as filed.
- Row 21 — AddLinkDialog$1.<init> — PASS. Filed REACHABLE INFERRED. Anonymous TextWatcher instantiated AddLinkDialog.java:205–219 inside initLayoutView. Framework TextWatcher dispatch unprinted = INFERRED as filed.
- Row 26 — AddLinkViewModel.initLinkFromClipboard — PASS. Filed REACHABLE SOURCE. Body AddLinkViewModel.java:45–59; called AddLinkDialog.java:223 from initLayoutView. Direct printed call = SOURCE as filed.
- Row 31 — AddTagActivity.onCreate — PASS. Filed REACHABLE SOURCE. Body AddTagActivity.java:47–60 (ViewModelProvider get AddTagViewModel :51–52, findFragmentByTag, else newInstance + show :58–59). SOURCE as filed under the file's framework-after-manifest-entry treatment.
- Row 36 — AddTagDialog.addTag — PASS. Filed REACHABLE SOURCE. Body AddTagDialog.java:196–223 (checkName guard, viewModel.saveTag() subscribed, success → finish OK); called from the positive-button click at AddTagDialog.java:187 (initAlertDialog). Printed call on a printed route = SOURCE as filed.

## Totals

- Rows checked: 8. PASS: 8. FAIL: 0.

## Proposed corrections

- None. No label or confirmed_by change proposed; the merge-ready file was not edited.
