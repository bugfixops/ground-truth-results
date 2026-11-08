# Stream A Phase 2 spot-check — batch 6 — UNVERIFIED (spot-check only, not a merge verdict)

- Source checked: `~/workspace/overnight/stream-A/work/batch6-merge-ready.md` (UNVERIFIED proposal, not a result).
- Branch: `work-2026-10-31`, repo `bugfixops/ground-truth-results`. Labels only; no device checks.
- Checked set (per task, special handling for batches 5–9): the 40 rows flipped to UNREACHABLE `no_trigger_in_app` in Phase 1a are NOT re-derived individually. Instead (a) the saved greps were verified to cover each flipped class with 0 direct `XBinding.inflate/bind` calls, and (b) the sample rows 1, 6, 11, 16, 21, 26, 31, 36 were individually re-derived. Total individually checked: 8 rows; grep-coverage checked: all 40 rows / 8 classes touched by this batch (rows 1–2 DialogAddLinkBinding — continued from batch 5 — 3–8 DialogAddTagBinding, 9–14 DialogCreateTorrentBinding, 15–20 DialogErrorBinding, 21–26 DialogGoToFolderBinding, 27–32 DialogLogFilterBinding, 33–38 DialogSelectTagBinding, 39–40 DrawerEmptyTagsListItemBinding — continued into batch 7).
- Greps verified: `~/workspace/overnight/stream-A/greps/batch5-9-complete-tree-grep.txt` (SHA-256 prefix 110b8bad, matching the citation in every row) — 252 main files + 20 other-source-set files, one section per class, every section "direct inflate/bind calls = 0" — AND `~/workspace/overnight/stream-A/greps/batch5-9-missing29-grep.txt` — the 29 files the first grep did not cover (28 feedparser + NanoHTTPD.java), 0 direct calls and 0 bare-name hits for all 37 batches 5–10 classes. Together these close the complete 301-file Java tree (252 + 28 + 1 main + 20 test/other).
- Independent re-run (this spot-check, not just trusting the saved files): grep for `<37-class alternation>\.(inflate|bind)\(` over the local corpus (281 main Java files), other-source-sets (20 files), and corpus-missing29 (29 files) = 0 direct-call hits in all three corpora. Bare-name hits in the main tree are imports, field declarations, and `DataBindingUtil.inflate(...)` assignments only — none is a direct base-static call.
- Method: no connector fetch was needed; no 429 encountered. No merge-ready file was edited; no tick written.
- Verdict vocabulary: PASS = label consistent with the re-derived evidence. PASS* = the factual grep premise is verified, but the label itself rests on the Phase 1 convention that supersedes DECISIONS.md D4h ("stay OPEN") for this family — a project convention decision that is for user review and is NOT decided here; the label is left as-is. FAIL = evidence contradicts the label. No FAILs in this batch.
- Scope limit: generated `*BindingImpl` bodies are not in the corpus, so no generated-to-generated dispatch was printed either way; the layout section of the saved grep is supporting evidence only and is not relied on for these verdicts.

## Per-row verdicts (sample rows, individually re-derived)

| Row | Method (short) | Label in file | Verdict | Evidence (re-derived) |
|---|---|---|---|---|
| 1 | DialogAddLinkBinding.inflate(LayoutInflater, ViewGroup, boolean, Object) | UNREACHABLE no_trigger_in_app, INFERRED | PASS* | Saved grep: DialogAddLinkBinding direct calls = 0; bare hits only AddLinkDialog.java:51 (import) and :67 (field). Independent grep confirms 0. Same convention caveat as header. |
| 6 | DialogAddTagBinding.inflate(LayoutInflater, ViewGroup, boolean) | UNREACHABLE no_trigger_in_app, INFERRED | PASS* | Saved grep: direct calls = 0; bare hits only AddTagDialog.java:49 (import) and :64 (field). Independent grep confirms 0. Same convention caveat. |
| 11 | DialogCreateTorrentBinding.inflate(LayoutInflater) | UNREACHABLE no_trigger_in_app, INFERRED | PASS* | Saved grep: direct calls = 0; bare hits only CreateTorrentDialog.java:55 (import) and :82 (field). Independent grep confirms 0. Same convention caveat. |
| 16 | DialogErrorBinding.bind(View, Object) | UNREACHABLE no_trigger_in_app, INFERRED | PASS* | Saved grep: direct calls = 0; bare hits are ErrorReportDialog.java:28 (import), :68 (`DataBindingUtil.inflate(...)` assignment, not a base-static call), :77 (parameter type). Independent grep confirms 0 direct calls. Same convention caveat. |
| 21 | DialogGoToFolderBinding.bind(View) | UNREACHABLE no_trigger_in_app, INFERRED | PASS* | Saved grep: direct calls = 0; bare hits only GoToFolderDialog.java:43 (import) and :52 (field). Independent grep confirms 0. Same convention caveat. |
| 26 | DialogGoToFolderBinding.inflate(LayoutInflater, Object) | UNREACHABLE no_trigger_in_app, INFERRED | PASS* | Same class section as row 21: 0 direct calls in all three corpora. Same convention caveat. |
| 31 | DialogLogFilterBinding.inflate(LayoutInflater, ViewGroup, boolean, Object) | UNREACHABLE no_trigger_in_app, INFERRED | PASS* | Saved grep: direct calls = 0; bare hits only SessionLogFilterDialog.java:38 (import) and :46 (field). Independent grep confirms 0. Same convention caveat. |
| 36 | DialogSelectTagBinding.inflate(LayoutInflater, ViewGroup, boolean) | UNREACHABLE no_trigger_in_app, INFERRED | PASS* | Saved grep: direct calls = 0; bare hits only SelectTagDialog.java:42 (import) and :60 (field). Independent grep confirms 0. Same convention caveat. |

## Grep-coverage verification (all 40 flipped rows, by class)

- DialogAddLinkBinding, DialogAddTagBinding, DialogCreateTorrentBinding, DialogErrorBinding, DialogGoToFolderBinding, DialogLogFilterBinding, DialogSelectTagBinding, DrawerEmptyTagsListItemBinding: each has a section in the complete-tree grep (main 252 + other 20) reporting 0 direct calls, and each is in the missing29 grep's 37-class list with 0 direct and 0 bare-name hits. Coverage: COMPLETE for this batch — no flipped class is missing from either grep file.
- Non-sample rows were verified only through this per-class coverage, per the task's special handling — not individually re-derived.

## Totals

- Rows individually checked: 8. PASS: 8 (of which PASS* caveated: 8 — all rest on the superseding-D4h convention). FAIL: 0.
- Rows covered by grep verification (not individually re-derived): 32 further rows, all in classes verified at 0 direct calls.
- Batch label counts re-verified from the row list: 40 rows = 40 UNREACHABLE / 0 REACHABLE / 0 OPEN. Consistent with the file header.
- Proposed corrections: none. No label change proposed; no file edited. The convention question (D4h vs the Phase 1 flip) is flagged for user review, not decided here.

## Notes for the coordinator

- Build/sampler/C1: not run (not this task).
