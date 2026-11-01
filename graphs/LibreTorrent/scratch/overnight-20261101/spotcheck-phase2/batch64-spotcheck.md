# Spot-check — LibreTorrent batch 64 (Phase 2)

- Source file checked (read-only, NOT edited): `~/workspace/overnight/stream-A/work/batch64-merge-ready.md`
- Branch: work-2026-10-31, repo bugfixops/ground-truth-results. No pushes, no edits to any merge-ready file.
- Method: re-derived each checked row from already-fetched local source (no connector fetch needed, so no 429). Build/sampler/C1: not run (not this task).
- Batch totals re-verified from the label column: 40 rows, sequence 1–40 intact, 26 REACHABLE proposed / 8 UNREACHABLE proposed / 6 OPEN — matches the Phase 1c header (OPEN: 1, 10, 19, 28, 33, 38).
- Conventions (D4a/D4c/D4e/D4f) were applied as recorded in `~/workspace/overnight/stream-A/DECISIONS.md`; no convention was decided here. D4c/D4d composition was checked explicitly: rows 4, 13, 22, 31 are D4c UNREACHABLE, not D4d OPEN, exactly as DECISIONS.md D4c/D4d composition states.

## Rows checked (18)
Sample rows 1, 6, 11, 16, 21, 26, 31, 36, plus Phase 1c flips: D4c rows 3, 12, 21, 30 (onFieldChange) and 4, 13, 22, 31 (setVariable), D4e rows 2, 11, 20, 29, 39. Must-include extras 4, 13, 22, 31 are inside that set.

## Verdicts

| Row | Method | Label in file | Verdict | Evidence |
|---|---|---|---|---|
| 1 | DialogSelectTagBindingImpl.hasPendingBindings | OPEN, — | PASS | OPEN correct per D4f (64/1). No printed caller; D4c explicitly does not cover hasPendingBindings. |
| 2 | DialogSelectTagBindingImpl.invalidateAll | REACHABLE proposed, INFERRED | PASS | D4e flip, listed in DECISIONS.md D4e flips (64/2). |
| 3 | DialogSelectTagBindingImpl.onFieldChange | UNREACHABLE proposed, INFERRED | PASS | D4c flip, listed in DECISIONS.md D4c flips (64/3). Preconditions verified locally: dialog_select_tag.xml declares no `<data>`/variable and has 0 `@{` expressions; SelectTagDialog.java:139–141 uses binding fields only (tagsList/emptyListView/adapter), as cited; 0 `.onFieldChange` hits in the 252-file corpus grep; the D4c include check (`~/workspace/b686970-openclose2-src/include_check_686970.txt`) finds no layout including this layout. |
| 4 | DialogSelectTagBindingImpl.setVariable | UNREACHABLE proposed, INFERRED | PASS | D4c flip (64/4), taking precedence over D4d OPEN per DECISIONS.md composition — correctly applied, not reverted to OPEN. Same no-variable preconditions as row 3; 0 `.setVariable(` hits in the corpus grep; SelectTagDialog.java never sets a variable. |
| 6 | DrawerEmptyTagsListItemBindingImpl.<clinit> | REACHABLE proposed, INFERRED | PASS | TagsAdapter.java:64–69 inflate of drawer_empty_tags_list_item (316-line fetch), verified locally. |
| 11 | DrawerEmptyTagsListItemBindingImpl.invalidateAll | REACHABLE proposed, INFERRED | PASS | D4e flip, listed in DECISIONS.md D4e flips (64/11). |
| 12 | DrawerEmptyTagsListItemBindingImpl.onFieldChange | UNREACHABLE proposed, INFERRED | PASS | D4c flip (64/12). drawer_empty_tags_list_item.xml: no `<data>`/variable, 0 expressions (verified locally); holder uses binding fields (TagsAdapter.java:227–229 EmptyItemViewHolder, verified). |
| 13 | DrawerEmptyTagsListItemBindingImpl.setVariable | UNREACHABLE proposed, INFERRED | PASS | D4c flip (64/13), precedence over D4d correctly applied as row 4. No printed setVariable call in TagsAdapter (corpus grep 0 hits). |
| 16 | DrawerNoTagsListItemBindingImpl.<init>(DataBindingComponent,View) | REACHABLE proposed, INFERRED | PASS | TagsAdapter.java:82–84 inflate of drawer_no_tags_list_item, verified locally; mapper dispatch, INFERRED, correctly stated. |
| 20 | DrawerNoTagsListItemBindingImpl.invalidateAll | REACHABLE proposed, INFERRED | PASS | D4e flip, listed in DECISIONS.md D4e flips (64/20). |
| 21 | DrawerNoTagsListItemBindingImpl.onFieldChange | UNREACHABLE proposed, INFERRED | PASS | D4c flip (64/21). drawer_no_tags_list_item.xml: no `<data>`/variable, 0 expressions (verified locally). |
| 22 | DrawerNoTagsListItemBindingImpl.setVariable | UNREACHABLE proposed, INFERRED | PASS | D4c flip (64/22), precedence over D4d correctly applied as row 4. |
| 26 | DrawerTagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE proposed, INFERRED | PASS | "Called by the 2-arg generated constructor" is the correct delegation direction (2-arg calls 3-arg). DrawerTagsListItemBinding inflated at TagsAdapter.java:73 (verified in the same file). |
| 29 | DrawerTagsListItemBindingImpl.invalidateAll | REACHABLE proposed, INFERRED | PASS | D4e flip, listed in DECISIONS.md D4e flips (64/29). |
| 30 | DrawerTagsListItemBindingImpl.onFieldChange | UNREACHABLE proposed, INFERRED | PASS | D4c flip (64/30). drawer_tags_list_item.xml: no `<data>`/variable, 0 expressions (verified locally); cited bind() use verified: TagsAdapter.java:190 `binding.name`, :191 `binding.color`, :198 `binding.menu` — fields only. |
| 31 | DrawerTagsListItemBindingImpl.setVariable | UNREACHABLE proposed, INFERRED | PASS | D4c flip (64/31), precedence over D4d correctly applied as row 4. |
| 36 | FragmentAddTorrentFilesBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE proposed, INFERRED | PASS | AddTorrentFilesFragment.java:81 inflate of fragment_add_torrent_files, verified locally; 3-arg called by 2-arg, correct direction as row 26. |
| 39 | FragmentAddTorrentFilesBindingImpl.invalidateAll | REACHABLE proposed, INFERRED | PASS | D4e flip, listed in DECISIONS.md D4e flips (64/39). |

## Totals
- Checked: 18. PASS: 18. FAIL: 0.

## Proposed corrections
None. In particular, the D4c-over-D4d composition for rows 4, 13, 22, 31 is correct and must NOT be "fixed" back to OPEN.
