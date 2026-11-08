# Spot-check — LibreTorrent batch 70 (Phase 2)

- Source file checked (read-only, NOT edited): `~/workspace/overnight/stream-A/work/batch70-merge-ready.md`
- Branch: work-2026-10-31, repo bugfixops/ground-truth-results. No pushes, no edits to any merge-ready file.
- Method: re-derived each checked row from already-fetched local source (no connector fetch needed, so no 429). Build/sampler/C1: not run (not this task).
- Batch totals re-verified from the label column: 40 rows, sequence 1–40 intact, 29 REACHABLE / 8 UNREACHABLE / 3 OPEN — matches the Phase 1c header (8 D4c flips; hasPendingBindings rows left OPEN under D4f).
- Conventions (D4c/D4f) were applied as recorded in `~/workspace/overnight/stream-A/DECISIONS.md`; no convention was decided here.
- D4c evidence base verified as a whole: `~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt` (0 hits in the 252-file app-Java tree for setVariable/onFieldChange/hasPendingBindings) and `~/workspace/b686970-openclose2-src/include_check_686970.txt` (no layout includes any of the 13 group layouts) — same files as the batch 68 spot-check.

## Rows checked (14)
Sample rows 1, 6, 11, 16, 21, 26, 31, 36, plus Phase 1c D4c flips 1, 2, 10, 11, 19, 20, 28, 29.

## Verdicts

| Row | Method | Label in file | Verdict | Evidence |
|---|---|---|---|---|
| 1 | ItemTorrentDownloadableFileBindingImpl.onFieldChange | UNREACHABLE, INFERRED | PASS | D4c flip (70/1). Corpus layout item_torrent_downloadable_file.xml: no `<data>`, 0 variables, 0 expressions. DownloadableFilesAdapter.java:60 inflate; adapter uses the binding as a ViewHolder field only, as cited. Include check + zero-hit grep as above. Phase 1c D4c annotation present. Companion note to batch 69 rows 34–40 is coherent (batch 69 row 36 is this binding's 2-arg <init>). |
| 2 | ItemTorrentDownloadableFileBindingImpl.setVariable | UNREACHABLE, INFERRED | PASS | D4c flip (70/2), precedence over D4d correctly applied. Same preconditions as row 1. |
| 6 | ItemTorrentListBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE, INFERRED | PASS | "Called by row 5 in generated code" — verified: batch 70 row 5 is the 2-arg <init> ("Mapper result of TorrentListAdapter:79 inflate"), and TorrentListAdapter.java:79 inflate is verified in the corpus file. Correct delegation direction. |
| 10 | ItemTorrentListBindingImpl.onFieldChange | UNREACHABLE, INFERRED | PASS | D4c flip (70/10). Corpus layout item_torrent_list.xml: no `<data>`, 0 variables, 0 expressions. Include check + zero-hit grep as above. Phase 1c D4c annotation present. |
| 11 | ItemTorrentListBindingImpl.setVariable | UNREACHABLE, INFERRED | PASS | D4c flip (70/11), precedence over D4d correctly applied. Same preconditions as row 10. |
| 16 | ItemTrackersListBindingImpl.executeBindings | REACHABLE, INFERRED | PASS | Row-14 construction anchor verified: batch 70 row 14 is the 2-arg <init> ("Mapper result of TrackerListAdapter:73 inflate"), and TrackerListAdapter.java:73 inflate is verified in the corpus file. Rebind after generated invalidateAll, INFERRED, correctly stated. |
| 19 | ItemTrackersListBindingImpl.onFieldChange | UNREACHABLE, INFERRED | PASS | D4c flip (70/19). Corpus layout item_trackers_list.xml: no `<data>`, 0 variables, 0 expressions. Include check + zero-hit grep as above. Phase 1c D4c annotation present. |
| 20 | ItemTrackersListBindingImpl.setVariable | UNREACHABLE, INFERRED | PASS | D4c flip (70/20), precedence over D4d correctly applied. Same preconditions as row 19. |
| 21 | TagsListItemBinding.<init> | REACHABLE, INFERRED | PASS | TagsAdapter.java (ui/tag, 111-line corpus file):48–52 inflate of tags_list_item, verified. Abstract ctor via Impl <init> (rows 23–24), INFERRED, correctly stated. |
| 26 | TagsListItemBindingImpl.hasPendingBindings | OPEN, — | PASS | OPEN correct per D4f (70/26 is in the D4f stay-OPEN list). Zero hits in the grep re-run (including executePendingBindings); named resolver correctly stated. D4c correctly not applied. |
| 28 | TagsListItemBindingImpl.onFieldChange | UNREACHABLE, INFERRED | PASS | D4c flip (70/28). Corpus layout tags_list_item.xml: no `<data>`, 0 variables, 0 expressions (verified locally, matching the row's "declares NO <data> variable (fresh)"). Include check + zero-hit grep as above. Phase 1c D4c annotation present, superseding the row's older "strengthens OPEN, does not close it" sentence. |
| 29 | TagsListItemBindingImpl.setVariable | UNREACHABLE, INFERRED | PASS | D4c flip (70/29), precedence over D4d correctly applied. Cited field-only use verified: ui/tag TagsAdapter.java:102 `binding.name`, :103 `binding.color`, :104 `binding.getRoot()` — all inside the cited :100–108 range (the bind method spans :98–108). Layout declares no variable, as cited. |
| 31 | BootReceiver.initScheduling | REACHABLE, SOURCE | PASS | BootReceiver.java: onReceive starts :39, initScheduling definition :60–73 — all verified in the corpus file (74 lines). App-code call site printed, hence SOURCE, correctly stated (not INFERRED). Both branches claim is consistent with the printed onReceive body calling initScheduling. |
| 36 | ConnectionReceiver.onReceive | REACHABLE, INFERRED | PASS | TorrentEngine.java:1020 `appContext.registerReceiver(connectionReceiver, ConnectionReceiver.getFilter())` — verified in the corpus file. ConnectionReceiver.java:37–44 onReceive body gating on CONNECTIVITY_ACTION — verified (body spans :37–44, closing brace :44). Framework broadcast dispatch, hence INFERRED, correctly stated; the row's own strict-entry caveat (TorrentEngine entry step not freshly printed) is correctly retained. |

## Totals
- Checked: 14. PASS: 14. FAIL: 0.

## Proposed corrections
None. No label, confirmed_by, or citation in the checked rows needs changing.
