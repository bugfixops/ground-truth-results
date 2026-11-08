# LibreTorrent batch 86 — Phase 2 spot-check — UNVERIFIED (spot-check only, not a merge verdict)

- Batch: 86. Work file checked: `~/workspace/overnight/stream-A/work/batch86-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (27): sample rows 1, 6, 11, 16, 21, 26, 31, 36, plus every row whose label changed in the file's dated 2026-11-01 revision notes — OPEN-close pass flips to REACHABLE: 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15, 16, 18, 19, 20, 22, 23, 24, 25, 26; OPEN-close round-2 flips to UNREACHABLE: 12, 17, 21. (Rows 1, 6, 11, 16, 21, 26 are in both sets, counted once.) Row 7 (ExpansionHeader.setText(int)) was NOT flipped and is not in the checked set.
- Method: re-derived from already-fetched source on disk (`~/workspace/b8586-src/`, `~/workspace/b8586-openclose-src/`, `~/workspace/b10171819-openclose-src/fw_src/`, `~/workspace/b8586-openclose2-src/grep_3arg_ctors_full_252_grep.txt`, `~/workspace/overnight/stream-A/greps/grep_recheck_3arg_ctors_complete.txt`); no GitHub connector fetch was needed, no 429 hit, no file missing.
- No edit was made to the merge-ready file. No push. Build/sampler/C1: not run (not this task).
- Convention note (NOT decided here): the UNREACHABLE rows 12, 17, 21 rest on the LayoutInflater 2-arg-only rule plus absence greps, with the file's all-five-together revert condition (with batch 85 rows 31/40) and batch 94's PiecesView 3-arg ctor still OPEN on the same evidence shape. The merger must apply one rule to all 3-arg ctors; this spot-check passes rows 12/17/21 as filed under the file's stated rule.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (file:line, local copy) |
|---|---|---|---|---|
| 1 | ExpansionHeader.createRotateAnimator | REACHABLE / SOURCE | PASS | Called by setExpanded(boolean,boolean) ExpansionHeader.java:105 and :111; def :117-124. |
| 2 | ExpansionHeader.init | REACHABLE / SOURCE | PASS | Called by the ctors ExpansionHeader.java:67 (2-arg) and :74 (3-arg); def :126-158. |
| 3 | ExpansionHeader.onRestoreInstanceState | REACHABLE / INFERRED | PASS | Def ExpansionHeader.java:175-185; framework callback after ExpansionHeader inflation (drawer_group_header.xml root, main_drawer_content.xml:27-28). |
| 4 | ExpansionHeader.onSaveInstanceState | REACHABLE / INFERRED | PASS | Def ExpansionHeader.java:164-173; same inflation route as row 3. |
| 5 | ExpansionHeader.setExpanded(boolean) | REACHABLE / SOURCE | PASS | MainActivity.java:280 `tagsGroupHeader.setExpanded(tagsExpanded)`; view is ExpansionHeader per main_drawer_content.xml:27-28. |
| 6 | ExpansionHeader.setExpanded(boolean,boolean) | REACHABLE / SOURCE | PASS | DrawerExpandableAdapter.java:209 `groupHeader.setExpanded(...)`. |
| 8 | ExpansionHeader.setText(CharSequence) | REACHABLE / SOURCE | PASS | DrawerExpandableAdapter.java:205 `groupHeader.setText(group.name)`. |
| 9 | ExpansionHeader.setTextAppearance | REACHABLE / SOURCE | PASS | Called by init ExpansionHeader.java:147. |
| 10 | ExpansionHeader.toggleExpand | REACHABLE / SOURCE | PASS | MainActivity.java:284 `tagsGroupHeader.toggleExpand()` in click listener :282-284. |
| 11 | FixHintTextInputEditText.<init> (2-arg) | REACHABLE / INFERRED | PASS | dialog_create_torrent.xml declares FixHintTextInputEditText 4x (:143, :172, :200, :271); CreateTorrentDialog.java:185 inflates that layout; LayoutInflater 2-arg dispatch → INFERRED correct. |
| 12 | FixHintTextInputEditText.<init> (3-arg) | UNREACHABLE / INFERRED | PASS | Kind no_trigger_in_app as filed. Def FixHintTextInputEditText.java:43-49; 2-arg ctor :39-40 calls super(context, attrs) only, never this(...,int). Same LayoutInflater evidence (fw :88/:90-91/:615) and zero-hit saved greps as batch 85. See convention note above. |
| 13 | FixHintTextInputEditText.getAutofillType | REACHABLE / INFERRED | PASS | Def FixHintTextInputEditText.java:52-56: SDK_INT == O returns NONE, otherwise super's value — so at API 27 it is NOT closed_by_api_level; framework autofill callback after row-11 inflation. |
| 14 | RecyclerViewDividerDecoration.<init>(Drawable) | REACHABLE / SOURCE | PASS | addItemDecoration sites MainFragment.java:153, FeedFragment.java:133 (plus LogActivity/FeedItems/Trackers/Peers sites as filed); def RecyclerViewDividerDecoration.java:39-42. |
| 15 | RecyclerViewDividerDecoration.onDrawOver | REACHABLE / INFERRED | PASS | Def RecyclerViewDividerDecoration.java:50+; ItemDecoration framework callback after row-14 addItemDecoration. |
| 16 | SwitchBar.<init> (2-arg) | REACHABLE / INFERRED | PASS | preference_switchbar.xml:6 declares SwitchBar id switchButton; SwitchBarPreference sets that layout and finds the view; LayoutInflater 2-arg dispatch → INFERRED correct. |
| 17 | SwitchBar.<init> (3-arg) | UNREACHABLE / INFERRED | PASS | Kind no_trigger_in_app as filed. Def SwitchBar.java:51-56; 2-arg ctor :44-46 calls super(ContextThemeWrapper..., attrs) only, never this(...,int). Same LayoutInflater evidence and zero-hit saved greps. See convention note above. |
| 18 | SwitchBar.init | REACHABLE / SOURCE | PASS | Called by ctors SwitchBar.java:48 and :55; def :58-67. |
| 19 | SwitchBar.setChecked | REACHABLE / SOURCE | PASS | SwitchBarPreference.java:71 `switchButton.setChecked(isChecked())` and :83 `setChecked(!isChecked)`. |
| 20 | ThemedSpeedDialView.<init> (2-arg) | REACHABLE / INFERRED | PASS | fragment_main.xml:33 declares ThemedSpeedDialView id fab_button; MainFragment.java:433/:439/:445 `binding.fabButton.addActionItem(...)` confirms the binding type; LayoutInflater 2-arg dispatch → INFERRED correct. |
| 21 | ThemedSpeedDialView.<init> (3-arg) | UNREACHABLE / INFERRED | PASS | Kind no_trigger_in_app as filed. Def ThemedSpeedDialView.java:46-51; 2-arg ctor :40-42 calls super(context, attrs) only, never this(...,int). Same LayoutInflater evidence and zero-hit saved greps. See convention note above. |
| 22 | ThemedSpeedDialView.addActionItem | REACHABLE / SOURCE | PASS | MainFragment.java:433, :439, :445 `binding.fabButton.addActionItem(...)`. |
| 23 | ThemedSwipeRefreshLayout.<init> | REACHABLE / INFERRED | PASS | fragment_feed.xml:10 and fragment_feed_items.xml:28 declare ThemedSwipeRefreshLayout id swipe_container; LayoutInflater 2-arg dispatch → INFERRED correct. |
| 24 | BlankFragment.<init> | REACHABLE / SOURCE | PASS | Constructed in newInstance BlankFragment.java:38. |
| 25 | BlankFragment.newInstance | REACHABLE / SOURCE | PASS | MainActivity.java:679 and FeedActivity.java:195, both inside Utils.isTwoPane branches — a printed configuration branch, not OPEN. |
| 26 | BlankFragment.onCreateView | REACHABLE / INFERRED | PASS | Def BlankFragment.java:47-54; framework lifecycle after the replace transactions (MainActivity:680-683, FeedActivity:196-199). |
| 31 | DetailTorrentActivity.<init> | REACHABLE / INFERRED | PASS | Default constructor (no explicit ctor in DetailTorrentActivity.java); framework instantiation on activity start. Label PASS. Note only: batch 82 row 29 marks the same framework-instantiation pattern SOURCE for CreateTorrentActivity.<init> — a confirmed_by variance across batches, not a label error; flagged for the coordinator, not counted as a FAIL. |
| 36 | DetailTorrentActivity.onStop | REACHABLE / INFERRED | PASS | Def DetailTorrentActivity.java:80-86 (clears disposables :84); framework lifecycle dispatch unprinted → INFERRED correct. |

## Totals

- PASS: 27 / 27. FAIL: 0 / 27.

## Proposed corrections

- None for any row label. The row-31 confirmed_by variance vs batch 82 row 29 is flagged above for the coordinator to normalise project-wide if desired; it does not change any label.
