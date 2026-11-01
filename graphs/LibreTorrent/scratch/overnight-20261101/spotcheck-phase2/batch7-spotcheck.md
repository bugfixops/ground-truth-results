# Stream A Phase 2 spot-check — batch 7 — UNVERIFIED (spot-check only, not a merge verdict)

- Source checked: `~/workspace/overnight/stream-A/work/batch7-merge-ready.md` (UNVERIFIED proposal, not a result).
- Branch: `work-2026-10-31`, repo `bugfixops/ground-truth-results`. Labels only; no device checks.
- Checked set (per task, special handling for batches 5–9): the 40 rows flipped to UNREACHABLE `no_trigger_in_app` in Phase 1a are NOT re-derived individually. Instead (a) the saved greps were verified to cover each flipped class with 0 direct `XBinding.inflate/bind` calls, and (b) the sample rows 1, 6, 11, 16, 21, 26, 31, 36 were individually re-derived. Total individually checked: 8 rows; grep-coverage checked: all 40 rows / 7 classes touched by this batch (rows 1–4 DrawerEmptyTagsListItemBinding — continued from batch 6 — 5–10 DrawerNoTagsListItemBinding, 11–16 DrawerTagsListItemBinding, 17–22 FragmentAddTorrentFilesBinding, 23–28 FragmentAddTorrentInfoBinding, 29–34 FragmentDetailTorrentBinding, 35–40 FragmentDetailTorrentFilesBinding).
- Greps verified: `~/workspace/overnight/stream-A/greps/batch5-9-complete-tree-grep.txt` (SHA-256 prefix 110b8bad, matching the citation in every row) — 252 main files + 20 other-source-set files, one section per class, every section "direct inflate/bind calls = 0" — AND `~/workspace/overnight/stream-A/greps/batch5-9-missing29-grep.txt` — the 29 files the first grep did not cover (28 feedparser + NanoHTTPD.java), 0 direct calls and 0 bare-name hits for all 37 batches 5–10 classes. Together these close the complete 301-file Java tree (252 + 28 + 1 main + 20 test/other).
- Independent re-run (this spot-check, not just trusting the saved files): grep for `<37-class alternation>\.(inflate|bind)\(` over the local corpus (281 main Java files), other-source-sets (20 files), and corpus-missing29 (29 files) = 0 direct-call hits in all three corpora. Bare-name hits in the main tree are imports, field declarations, and `DataBindingUtil.inflate(...)` assignments only — none is a direct base-static call.
- Method: no connector fetch was needed; no 429 encountered. No merge-ready file was edited; no tick written.
- Verdict vocabulary: PASS = label consistent with the re-derived evidence. PASS* = the factual grep premise is verified, but the label itself rests on the Phase 1 convention that supersedes DECISIONS.md D4h ("stay OPEN") for this family — a project convention decision that is for user review and is NOT decided here; the label is left as-is. FAIL = evidence contradicts the label. No FAILs in this batch.
- Scope limit: generated `*BindingImpl` bodies are not in the corpus, so no generated-to-generated dispatch was printed either way; the layout section of the saved grep is supporting evidence only and is not relied on for these verdicts.

## Per-row verdicts (sample rows, individually re-derived)

| Row | Method (short) | Label in file | Verdict | Evidence (re-derived) |
|---|---|---|---|---|
| 1 | DrawerEmptyTagsListItemBinding.inflate(LayoutInflater) | UNREACHABLE no_trigger_in_app, INFERRED | PASS* | Saved grep: direct calls = 0; bare hits are TagsAdapter.java:38 (import), :64 (`DataBindingUtil.inflate(...)` assignment), :227 (field), :229 (ctor parameter) — none a base-static call. Independent grep confirms 0. Same convention caveat as header. |
| 6 | DrawerNoTagsListItemBinding.bind(View, Object) | UNREACHABLE no_trigger_in_app, INFERRED | PASS* | Saved grep: direct calls = 0; bare hits are TagsAdapter.java:39 (import), :82 (`DataBindingUtil.inflate(...)` assignment), :273 (field), :275 (ctor parameter). Independent grep confirms 0. Same convention caveat. |
| 11 | DrawerTagsListItemBinding.bind(View) | UNREACHABLE no_trigger_in_app, INFERRED | PASS* | Saved grep: direct calls = 0; bare hits are TagsAdapter.java:40 (import), :73 (`DataBindingUtil.inflate(...)` assignment), :168 (field), :170 (ctor parameter). Independent grep confirms 0. Same convention caveat. |
| 16 | DrawerTagsListItemBinding.inflate(LayoutInflater, Object) | UNREACHABLE no_trigger_in_app, INFERRED | PASS* | Same class section as row 11: 0 direct calls in all three corpora. Same convention caveat. |
| 21 | FragmentAddTorrentFilesBinding.inflate(LayoutInflater, ViewGroup, boolean, Object) | UNREACHABLE no_trigger_in_app, INFERRED | PASS* | Saved grep: direct calls = 0; bare hits only AddTorrentFilesFragment.java:40 (import) and :60 (field). Independent grep confirms 0. Same convention caveat. |
| 26 | FragmentAddTorrentInfoBinding.inflate(LayoutInflater, ViewGroup, boolean) | UNREACHABLE no_trigger_in_app, INFERRED | PASS* | Saved grep: direct calls = 0; bare hits only AddTorrentInfoFragment.java:49 (import) and :71 (field). Independent grep confirms 0. Same convention caveat. |
| 31 | FragmentDetailTorrentBinding.inflate(LayoutInflater) | UNREACHABLE no_trigger_in_app, INFERRED | PASS* | Saved grep: direct calls = 0; bare hits only DetailTorrentFragment.java:73 (import) and :103 (field). Independent grep confirms 0. Same convention caveat. |
| 36 | FragmentDetailTorrentFilesBinding.bind(View, Object) | UNREACHABLE no_trigger_in_app, INFERRED | PASS* | Saved grep: direct calls = 0; bare hits only DetailTorrentFilesFragment.java:59 (import) and :88 (field). Independent grep confirms 0. Same convention caveat. |

## Grep-coverage verification (all 40 flipped rows, by class)

- DrawerEmptyTagsListItemBinding, DrawerNoTagsListItemBinding, DrawerTagsListItemBinding, FragmentAddTorrentFilesBinding, FragmentAddTorrentInfoBinding, FragmentDetailTorrentBinding, FragmentDetailTorrentFilesBinding: each has a section in the complete-tree grep (main 252 + other 20) reporting 0 direct calls, and each is in the missing29 grep's 37-class list with 0 direct and 0 bare-name hits. Coverage: COMPLETE for this batch — no flipped class is missing from either grep file.
- Non-sample rows were verified only through this per-class coverage, per the task's special handling — not individually re-derived.

## Totals

- Rows individually checked: 8. PASS: 8 (of which PASS* caveated: 8 — all rest on the superseding-D4h convention). FAIL: 0.
- Rows covered by grep verification (not individually re-derived): 32 further rows, all in classes verified at 0 direct calls.
- Batch label counts re-verified from the row list: 40 rows = 40 UNREACHABLE / 0 REACHABLE / 0 OPEN. Consistent with the file header.
- Proposed corrections: none. No label change proposed; no file edited. The convention question (D4h vs the Phase 1 flip) is flagged for user review, not decided here.

## Notes for the coordinator

- Build/sampler/C1: not run (not this task).
