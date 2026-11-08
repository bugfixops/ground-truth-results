# AGENT_NOTES (Vanilla-Music, schema 2 conversion) - DONE

## Final status
All of steps 1-9 of AGENT_BRIEF_V2.md are complete. Step 9 checks all pass (ran fresh, just now):
- `python3 -I tools/build_graph.py graphs/Vanilla-Music vanilla`: errors 0, warnings 0, STRICT = True.
  methods 1473, pages 44, edges 3429. REACHABLE 1325, UNREACHABLE 148 (no_trigger_in_app 144, branch_never_taken 4).
  labels confirmed by: SOURCE 1157, INFERRED 316.
- `python3 -I tools/check_citations.py Vanilla-Music`: 100 distinct citations, 0 problems, 0 FW-MEMORY/DYN/UNVERIFIED.
- `python3 -I tools/check_routes.py Vanilla-Music`: 0 routes flagged.
- `python3 -I tools/check_bytecode_lines.py Vanilla-Music`: 2020 checked, 0 where the cited line does not show the callee.
- `python3 -I tools/tests/check_v2.py`: apps with problems: 0.
- `grep -c "DEAD\|FRAMEWORK_ONLY" graphs/Vanilla-Music/graph_def.py`: 0.

Files in this folder: `graph_def.py` (hand-written schema 2 definition), `generated_draft_graph_def.py.txt` (the old draft, kept for reference, never built), `verification.csv` (audit log), `make_verification.py` (generator, asserts every note against the graph), `readme_notes.md` (5 required headings), `LESSONS.md`, `out/` (build artifacts: methods.csv, the trigger-graph JSON/HTML, sanity_check.csv, build_report.txt, README.md).

## What this session did (continuing from a prior session that had written sections A-H of graph_def.py but left section I, the UNREACHABLE/gates/classify section, unwritten)

The orchestrator's handoff claimed "1 error, 23 warnings" from a fresh build; the actual fresh build this session found was **88 errors** (not 1) plus the 23 warnings. Trusted the build output, not the handoff's count, per instructions, and worked from there.

1. **Fixed 88 -> 0 errors**: 4 "unknown dst node" (IdlePreference/ListPreferenceSummary do not override onGetDefaultValue/onSetInitialValue, only SeekBarPreference does - fixed the shared for-loop), and ~84 "no path" methods, split into:
   - A stub `for ...: pass` loop that never wired `PlaybackService.onSharedPreferenceChanged` at all (a real bug, not just a missing classification); fixing it, plus wiring the per-settings-screen `OSPC_V` variants (which had NO incoming edge at all), cascaded ~10 more methods to REACHABLE for free (CoverCache.evictAll, RemoteControlImplLp.reloadPreference, ShowQueueFragment.recreate, ...).
   - ~35 methods wired by reading their source and adding the missing framework/call edges (see graph_def.py sections marked "this session": H2a/H2b block, the TabOrderActivity Checkable chain, PermissionRequestActivity (E5, written fresh - no wiring existed for it at all before this session), JumpToTimeDialog, FolderPickerActivity's onCreateOptionsMenu/onNothingSelected/remaining TextWatcher callbacks, VanillaImageButton.setImageResource (base-typed-field dispatch gap), ArrowedText.onDraw, LibraryActivity$1.run -> BottomBarControls.setCover, PlaylistObserver.onUpgrade/$2.onEvent, PreferencesMediaLibrary$1$1.run, ReadaheadThread.handleMessage, SongTimeline's two Comparators, FileSystemAdapter's own adapter framework entry + its FilenameFilter/Comparator/FileObserver inner classes, SlidingTabLayout.populateTabStrip -> VanillaTabLayout.createDefaultTabView, DragSortItemView onLayout/onMeasure, DragSortItemViewCheckable.setChecked -> DraggableRow.setChecked (the real Checkable delegation chain through the ListView's row wrapper), LazyCoverView's handleMessage/BitmapLruCache pipeline, CoverCache$BitmapDiskCache onCreate/onUpgrade).
   - ~40 methods classified UNREACHABLE (section I5) after confirming no caller anywhere in app+library source with grep: MediaScanPlan.addOptionalStep/addChainedStep, CoverBitmap.<init>, ThemeHelper.usesDarkTheme, Common.debug, Mp4File.printDebugAtomPath (DEBUG-constant pattern, branch_never_taken), Song.compareTo/toString, several unused convenience constructors (SlidingView, VanillaImageButton, VanillaTabLayout, SlidingTabLayout x2, FastScrollGuardedListView x3), SlidingTabLayout's unused setContentDescription/setCustomTabColorizer/setCustomTabView + SlidingTabStrip.setCustomTabColorizer, DraggableRow.isChecked/toggle + DragSortItemViewCheckable.isChecked/toggle (confirmed by reading AbsListView.java/ListView.java that the framework only ever calls setChecked, never isChecked/toggle, on a row view), DragSortItemView.getGravity, PlaylistObserver$Database.<init>, SongTimeline.reshuffleTimeline.
   - One UNREACHABLE guess reversed: initially called CoverCache$CoverKey.equals dead, but the "UNREACHABLE but has incoming edges" warning caught that LazyCoverView$CoverMsg.isRecent() does call it (missed on first grep pass - only grepped CoverCache.java, not LazyCoverView.java).
2. **Fixed 23 -> 0 warnings**: sup()'d 29 dead-cluster-internal bytecode edges (section I6, same pattern openlauncher used for its own dead cluster), classified 20 of 29 REVIEW-flagged edges `non_standard` (genuine XML/reflection instantiation: ShowQueueFragment's `<fragment>` tag, PreferenceActivity's header-fragment list, 3 nested-PreferenceScreen fragments, 3 custom-Preference-row XML tags), and explicitly set `cls='standard'` (with a comment) on the other 9 (ShortcutPseudoActivity's explicit-component-intent service starts, which only matched the regex because the trigger text contains "setAction(").
3. **Set STRICT = True**; rebuilt to 0 errors / 0 warnings.
4. **`scan_unreachable.py --all --callers`**: 3 of 148 UNREACHABLE methods have a bytecode caller outside the set, all 3 already explained in their own reason text (LiftAnimator.onStart/onUpdate via the never-constructed LiftAnimator, DragSortListView.removeItem(int) via the never-configured CLICK_REMOVE mode). Nothing to fix.
5. **`check_citations.py`**: found and fixed 1 problem (ListPreferenceSummary.onDialogClosed cited a ListPreference.java line range past the end of the file, pointing at the unrelated SavedState class; re-cited to the real onPrepareDialogBuilder/onDialogClosed lines after printing and reading them). New fw_src file: `fw_src/android-8.1.0_r1/core/java/android/util/LruCache.java`.
6. **`verify_sample.py Vanilla-Music 30`**, read with a local *read-only* copy of `tools/show_route.py` (kept in the scratchpad, not under `work/tools/` - see "Tool bug" below) against the cited source lines, including enclosing guards (CS.guard_of). Found and fixed:
   - **A structural reachability bug** (found on the very first route read): `LibraryActivity`/`FullPlaybackActivity` share one un-overridden `onResume` node (`SlidingPlaybackActivity.onResume`); `MiniPlaybackActivity`/`AudioPickerActivity` share another (`PlaybackActivity.onResume`). The screen-ENTERS edges were attached to the bare shared node, so a route could enter via the launcher and exit through a sibling activity's screen with no gate. Fixed with 4 context variants (`@LibraryActivity`, `@FullPlaybackActivity`, `@MiniPlaybackActivity`, `@AudioPickerActivity`); this is why 19 of the 30 final-sample paths are logged `fixed` in verification.csv (their route runs through the fix).
   - 3 guard-less bytecode edges on the drag-sort-list touch dispatch chain (DragSortController.onTouch -> stopDragWithVelocity; DragSortListView.onTouchEvent -> onDragTouchEvent -> stopDrag(boolean)): each only valid inside an `if` the bytecode scan cannot see; added guard + STATE.
   - A stale pre-existing citation (LibraryPagerAdapter.java:895, inside onItemClick, wrongly cited for 8 MediaAdapter row-reading framework edges whose real trigger is line 353); re-cited.
   - A line-off citation this session's own new edge introduced (LibraryActivity.java:578 -> 579 for BottomBarControls.setCover).
   Redrew the sample twice (after the onResume fix, and after the drag-remove guard fix) and read the final 30 against the final build.
7. **verification.csv** written by `make_verification.py` (every note asserted against the final graph JSON): 30 path rows (19 fixed, 11 correct, 0 wrong), 178 label rows (148 UNREACHABLE + 30 REACHABLE-sample, all correct), 80 edge rows (10 fixed, 70 correct incl. every distinct FW-SRC citation). **readme_notes.md** (5 required headings) + `gen_readme_v2.py` run. **LESSONS.md** written (7 bullets).
8. Step 9 final checks all re-run fresh at the end and pass (see "Final status" above).

## Tool bug found and reported (not fixed - out of `work/tools/` scope)
`tools/show_route.py`'s evidence-reference regex stops at the first whitespace, so a multi-range citation written in this codebase's own established style (`SRC File.java:403, 408-424` - comma then a space before the next range) gets truncated to `File.java:403,` with a dangling comma, and `snippet()` then crashes with `ValueError: invalid literal for int() with base 10: ''`. Reproducible on e.g. `show_route.py Vanilla-Music "PlaybackActivity.onOptionsItemSelected@PREFS"`. The openlauncher session hit and reported the identical bug. Worked around with a local read-only copy of the script kept in the scratchpad (not under `work/tools/`), identical except the reference-splitting regex keeps a comma-separated range list together; used only to read routes, nothing was built or verified with it that `check_routes.py`/`check_citations.py`/`check_bytecode_lines.py` (the real gates) did not independently confirm.

## Nothing left open.

## Finish run 2026-11-01 (T6 + D1/D3/D7; merger's own session, private tree)

T6 (logs only; no label, edge, route, or graph_def.py change):
- `make_verification.py` run twice in the private tree; both runs
  byte-identical to each other and to the current verification.csv
  (cmp silent). Counts printed: label correct 178, edge correct 70,
  path fixed 19, path correct 11, edge fixed 10; 288 rows + header;
  30 path rows; header exactly type,item,result,confirmed_by,ref,edges,note.
- Fresh local build (`python3 -I tools/build_graph.py graphs/Vanilla-Music vanilla`,
  private tree): methods 1473, REACHABLE 1325, UNREACHABLE 148
  (no_trigger_in_app 144, branch_never_taken 4), errors 0, warnings 0,
  STRICT = True (graph_def.py line 20). check_citations: 100 distinct,
  0 problems. check_routes: 0 flagged. check_bytecode_lines: 2020
  checked, 0 where the cited line does not show the callee. Greps:
  DEAD|FRAMEWORK_ONLY 0, FW-MEMORY 0, PENDING 0.
- Check 8 (`scan_unreachable.py --all` / `--callers`, fresh): exactly 3
  methods with a bytecode caller outside the set, all confirmed
  explained in their own reason text: DragSortListView$LiftAnimator.onStart
  <- SmoothAnimator.start@LiftAnimator (DragSortListView.java:1177) and
  .onUpdate <- SmoothAnimator.run@LiftAnimator (:1209), both reasoned as
  "mLiftAnimator is never constructed (the line is commented out)";
  DragSortListView.removeItem(int) <- DragSortController.onSingleTapUp
  (:455), reasoned as the CLICK_REMOVE-only 1-argument overload while
  every layout leaves remove_mode at flingRemove. Nothing to fix.
- LESSONS.md already present with 8 bullets (within the 3-8 range);
  readme_notes.md already carries the five required headings in order;
  gen_readme_v2.py re-run in the private tree writes out/README.md
  (53 lines), byte-identical to the branch copy. No changes needed to
  either file. CI request for Vanilla-Music is the coordinator's to
  send (REBUILD_REQUEST); acceptance per T1 with path rows 30.

D1 (device route list): device/routes/Vanilla-Music/ROUTES.csv (30 rows,
one per verification.csv path row) plus ROUTES_NOTES.md were produced
by the device lead's D1 helpers and verified mechanically by me in
this session: methods, edges, source refs, env_kinds, and state_kinds
match verification.csv / out/methods.csv exactly; every edge id
resolves in out/vanilla_trigger_graph.json; drycheck chain/method/
permission/fixture checks pass (only "missing script" failures remain
until D3 lands). Statuses: 30 scripted, 0 unscriptable. Permissions on
exactly 4 rows (13, 15, 16, 26): READ_EXTERNAL_STORAGE +
WRITE_EXTERNAL_STORAGE. Setup on every row: push fixtures/Music +
media scan. ROUTES.csv + ROUTES_NOTES.md are pushed as the D1 item.

D3 (one script per route): 5 helpers fanned out (routes 01-05, 06-10,
11-15, 16-20, 21-25; one helper dir per group under
finish/work/Vanilla-Music/helper/d3-routes-*); I wrote routes 26-30
myself plus device/routes/Vanilla-Music/setup.py (pushes
fixtures/Music, broadcasts MEDIA_SCANNER_SCAN_FILE per file). All five
of my scripts pass drycheck --load-scripts in the private tree, and
each script's dry-run log references only its own route's edge ids;
setup.py dry-runs with 30 planned lines (15 pushes + 15 broadcasts).
Known selector caveats for the device lead: route_29's overflow
("More options") and search item titles; route_30's swipe-up is done
via scroll_to (res_id previous) since the harness has no raw swipe;
route_26 revokes the request set first so the permission flow can run.
Scripts are pushed only after the coordinator-assigned auditor reads
at least 1 in 3 against the printed routes and agrees, plus the dry run.

D7 (DEVICE rows in make_verification.py): added a guarded block that
reads graphs/Vanilla-Music/device/results.csv only when it exists and
appends one DEVICE path row per run row (correct when reached, else
unclear; never wrong; no label changes). Tested in the private tree:
without the file the output is byte-identical to today's (cmp silent);
with a synthetic 4-row results file exactly 4 DEVICE rows are added
with the expected result/note mapping; after removing the synthetic
file the output is identical again. No real device/results.csv exists
or is written in this run.

## Current step

T6 local verification done; D1 verified; D3 helpers running (routes
01-25) and my routes 26-30 + setup.py dry-passing; D7 implemented and
tested. Next: push AGENT_NOTES (T6 item), ROUTES.csv + ROUTES_NOTES
(D1 item), make_verification.py (D7 item) under the push lock; then
collect helper scripts, drycheck --load-scripts on all 30, await
auditor PASS, push scripts + setup.py; then report F1 readiness to the
coordinator (CI REBUILD_REQUEST + D9 dry run are the coordinator's).

## Decisions made by Muse (for the user and Yang to review)

No new decisions this session. All prior Vanilla-Music decisions stand
as recorded in scratch/overnight-20261101/DECISIONS.md and the earlier
AGENT_NOTES sections above.
