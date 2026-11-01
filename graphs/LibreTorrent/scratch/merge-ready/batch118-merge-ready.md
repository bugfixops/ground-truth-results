**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 118 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED merge-ready part only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**

**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push, so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1 check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).

- Scope: batch 118 only, 40 methods, no other batch, no other app, no device replay, no Aegis.

- Source: existing proposal `~/workspace/libretorrent-batch118-proposal.md` used as an INPUT, not a result. Membership was re-verified in this pass against the local plan copy `~/workspace/agent27-plan.tsv` (4,733 lines incl. header; plan blob SHA `0104806dd666c840049b3db52823d4b384fa1c92`): all 40 plan methods match the table below in plan order, all TODO_CANDIDATE_REACHABLE.

- Printed source: prior-session connector prints saved in `~/workspace/batch117-118-src/` (Limitations, Network, Proxy, Scheduling, Storage, Streaming, SettingsFragment, SelectTagActivity, SelectTagDialog, TorrentTagsList, AddTagButton — one file at a time in that pass). In this pass the table citations were spot-checked against those saved copies (see Spot-checks below), and one file was freshly re-fetched from branch `work-2026-10-31` with a 30 s pause and found byte-identical: `ui/settings/SettingsFragment.java` (10,437 bytes, no diff vs the saved copy). No fresh HTTP 429 was hit in this pass. Remaining files were NOT freshly re-fetched in this pass — the merger must still confirm the trunk line numbers against a fresh branch print if it requires fresh evidence for every row, but no row below rests on a search_code result or on an unprinted caller.

- Counts (mechanically verified): **40 REACHABLE proposed / 0 UNREACHABLE proposed / 0 OPEN**, 40/40 rows judged, sequence 1–40 intact. confirmed_by: 13 SOURCE / 27 INFERRED, never DYN, FW-MEMORY, or UNVERIFIED.

- OPEN/disputed rows: NONE. There were no OPEN rows in the batch 118 proposal to re-derive, and no disputed row was left by the prior pass. No row is claimed UNREACHABLE in this batch: no saved full-repo grep was run, and absence of a printed caller was never treated as proof of absence. No search_code 0-result was used as evidence of absence.


## Per-row judgements (carried from the proposal table, membership and citations spot-checked in this pass)

| # | Method | Label proposed | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | SchedulingSettingsFragment.lambda$subscribeAlertDialog$0 | REACHABLE | INFERRED | Event lambda inside `subscribeAlertDialog` `:129-140` (tag check vs `TAG_EXACT_ALARM_PERMISSION_DIALOG`, POSITIVE_BUTTON_CLICKED → `Utils.requestExactAlarmPermission`). Subscribed via Rx `.subscribe(...)` `:130`; Rx dispatch unprinted. `subscribeAlertDialog` itself is row 10. |
| 2 | SchedulingSettingsFragment.newInstance | REACHABLE | SOURCE | Def `:53-57`. Called by SettingsFragment.java:186 (large-screen branch). |
| 3 | SchedulingSettingsFragment.onCreate | REACHABLE | INFERRED | Def `:62-112` (loads repo + dialog ViewModel, finds/binds enable-start, enable-stop, start-time, stop-time, run-only-once, switch-WiFi). Lifecycle after row 2. |
| 4 | SchedulingSettingsFragment.onCreatePreferences | REACHABLE | INFERRED | Def `:164-166` (`setPreferencesFromResource(R.xml.pref_scheduling, rootKey)`). |
| 5 | SchedulingSettingsFragment.onDisplayPreferenceDialog | REACHABLE | INFERRED | Def `:175-189`: for a `TimePreference` it shows `TimePreferenceDialogFragmentCompat.newInstance(preference.getKey())` (`:179`, target fragment set `:182`, shown `:183-184`); otherwise delegates to super (`:186`). Framework dialog dispatch unprinted. |
| 6 | SchedulingSettingsFragment.onPreferenceChange | REACHABLE | INFERRED | Registered via batch 117 row 40 (`bindOnPreferenceChangeListener`, Scheduling `:169-171`). Def `:191-235` (enable start/stop → `Scheduler.setStartAppAlarm`/`setStopAppAlarm` or cancel, `Utils.enableBootReceiver`; start/stop time setters). Calls row 9 at `:201,:214,:224,:230` when an alarm cannot be set. Dispatch unprinted. |
| 7 | SchedulingSettingsFragment.onStart | REACHABLE | INFERRED | Def `:122-127` (calls row 10). Lifecycle; dispatch unprinted. |
| 8 | SchedulingSettingsFragment.onStop | REACHABLE | INFERRED | Def `:114-119` (`disposables.clear()`). Lifecycle; dispatch unprinted. |
| 9 | SchedulingSettingsFragment.showExactAlarmPermissionDialog | REACHABLE | SOURCE | Def `:143-161` (guarded by `isAdded()` and `findFragmentByTag`, shows `BaseAlertDialog.newInstance(...)` with tag `TAG_EXACT_ALARM_PERMISSION_DIALOG`). Called from onPreferenceChange at `:201,:214,:224,:230`. |
| 10 | SchedulingSettingsFragment.subscribeAlertDialog | REACHABLE | SOURCE | Def `:129-141` (`dialogViewModel.observeEvents().subscribe(...)`, `disposables.add(d)`). Called from onStart `:126`. |
| 11 | StorageSettingsFragment.<clinit> | REACHABLE | INFERRED | Static `TAG = StorageSettingsFragment.class.getSimpleName()` (`:54`); class initialisation on first use via row 20. (`TAG_DIR_CHOOSER_BIND_PREF` is a compile-time constant and needs no <clinit>.) |
| 12 | StorageSettingsFragment.<init> | REACHABLE | SOURCE | Implicit default ctor, called by `newInstance` `:65` (`new StorageSettingsFragment()`). |
| 13 | StorageSettingsFragment.bindOnPreferenceChangeListener | REACHABLE | SOURCE | Def `:222-224`. Called in onCreate at `:116` (move after download), `:143` (save torrent files), `:170` (watch dir), `:197` (watch-dir delete file), `:204` (POSIX disk I/O). |
| 14 | StorageSettingsFragment.dirChooseDialog | REACHABLE | SOURCE | Def `:227-239` (Intent to FileManagerDialog in DIR_CHOOSER_MODE, `downloadDirChoose.launch(i)` `:238`). Called by the four dir-chooser click lambdas at `:105,:132,:159,:186` (rows 16–19). |
| 15 | StorageSettingsFragment.lambda$new$4 | REACHABLE | INFERRED | `downloadDirChoose` ActivityResult callback body `:242-275` (RESULT_OK + bound preference → writes `pref.dirToWatch` / `moveAfterDownloadIn` / `saveTorrentFilesIn` / `saveTorrentsIn`, updates summary). $ numbering: the four onCreate click lambdas are $0–$3 (rows 16–19), so this field callback is $4; confirm against bytecode. Result dispatch unprinted. |
| 16 | StorageSettingsFragment.lambda$onCreate$0 | REACHABLE | INFERRED | Save-torrents-in click lambda `:103-108` (sets `dirChooserBindPref`, calls row 14 with the saved URI). Synthetic signature `(Uri,Preference)Z` = captured `uri` + click argument. Click dispatch unprinted. |
| 17 | StorageSettingsFragment.lambda$onCreate$1 | REACHABLE | INFERRED | Move-after-download-in click lambda `:130-135`, same pattern as row 16. |
| 18 | StorageSettingsFragment.lambda$onCreate$2 | REACHABLE | INFERRED | Save-torrent-files-in click lambda `:157-162`, same pattern. |
| 19 | StorageSettingsFragment.lambda$onCreate$3 | REACHABLE | INFERRED | Dir-to-watch click lambda `:184-189`, same pattern. |
| 20 | StorageSettingsFragment.newInstance | REACHABLE | SOURCE | Def `:64-69`. Called by SettingsFragment.java:168 (large-screen branch). |
| 21 | StorageSettingsFragment.onCreate | REACHABLE | INFERRED | Def `:81-207` (restores `dirChooserBindPref` from saved state `:85-86`, loads fs/repo, finds/binds dir + switch preferences). Lifecycle after row 20. |
| 22 | StorageSettingsFragment.onCreatePreferences | REACHABLE | INFERRED | Def `:217-219` (`setPreferencesFromResource(R.xml.pref_storage, rootKey)`). |
| 23 | StorageSettingsFragment.onPreferenceChange | REACHABLE | INFERRED | Registered via row 13. Def `:279-295` (watch dir, move after download, save torrent files, watch-dir delete file, POSIX disk I/O + reboot Snackbar). Dispatch unprinted. |
| 24 | StorageSettingsFragment.onSaveInstanceState | REACHABLE | INFERRED | Def `:209-214` (`outState.putString(TAG_DIR_CHOOSER_BIND_PREF, dirChooserBindPref)`). Framework save dispatch unprinted. |
| 25 | StorageSettingsFragment.onViewCreated | REACHABLE | INFERRED | Def `:73-79` (`coordinatorLayout = view.findViewById(R.id.coordinator_layout)`). Lifecycle; dispatch unprinted. |
| 26 | StreamingSettingsFragment.<clinit> | REACHABLE | INFERRED | Static `TAG = StreamingSettingsFragment.class.getSimpleName()` (`:39`); class initialisation on first use via row 30. |
| 27 | StreamingSettingsFragment.<init> | REACHABLE | SOURCE | Implicit default ctor, called by `newInstance` `:44` (`new StreamingSettingsFragment()`). |
| 28 | StreamingSettingsFragment.bindOnPreferenceChangeListener | REACHABLE | SOURCE | Def `:93-95`. Called in onCreate at `:62` (enable), `:71` (hostname), `:83` (port). |
| 29 | StreamingSettingsFragment.lambda$onCreate$0 | REACHABLE | INFERRED | Port bind lambda `:80` (`editText.setFilters(portFilter)`), the only lambda in onCreate, hence $0. Dialog-binding dispatch unprinted. |
| 30 | StreamingSettingsFragment.newInstance | REACHABLE | SOURCE | Def `:43-48`. Called by SettingsFragment.java:204 (large-screen branch). |
| 31 | StreamingSettingsFragment.onCreate | REACHABLE | INFERRED | Def `:52-86` (loads repo, enable/hostname/port preferences, binds listeners). Lifecycle after row 30. |
| 32 | StreamingSettingsFragment.onCreatePreferences | REACHABLE | INFERRED | Def `:88-90` (`setPreferencesFromResource(R.xml.pref_streaming, rootKey)`). |
| 33 | StreamingSettingsFragment.onPreferenceChange | REACHABLE | INFERRED | Registered via row 28. Def `:99-113` (hostname, port, enable streaming). Dispatch unprinted. |
| 34 | AddTagButton.<init>(Context) | REACHABLE | SOURCE | Def `AddTagButton.java:37-41` (calls `init(context)` `:40`). Constructed by `TorrentTagsList.buildAddTagButton` `:79` (`new AddTagButton(context)`); `buildAddTagButton` is called from `TorrentTagsList.init` `:36`. (The 2-arg and 3-arg ctors are NOT batch 118 rows and were not judged.) |
| 35 | AddTagButton.init | REACHABLE | SOURCE | Def `AddTagButton.java:59-78` (sets text/icon/colours from theme attributes). Called from all three ctors (`:40,:46,:56`); the batch-118 route is via row 34. |
| 36 | SelectTagActivity.<init> | REACHABLE | INFERRED | Implicit default ctor. Framework instantiates the activity when started via Intent; the in-app start site was not freshly printed in this pass (batch 119 lead: DetailTorrentInfoFragment tags listener launches SelectTagActivity — re-print at merge to upgrade). |
| 37 | SelectTagActivity.onBackPressed | REACHABLE | INFERRED | Def `SelectTagActivity.java:69-70` (`dialog.onBackPressed()`). Framework back dispatch unprinted; requires the activity/dialog to be showing (row 38). |
| 38 | SelectTagActivity.onCreate | REACHABLE | INFERRED | Def `SelectTagActivity.java:42-53`: finds an existing dialog by tag or creates one via `SelectTagDialog.newInstance(excludeTagsId)` (`:51`) and shows it (`:52`). Activity lifecycle; start Intent not freshly printed (see row 36). |
| 39 | SelectTagActivity.onFragmentFinished | REACHABLE | SOURCE | Def `SelectTagActivity.java:57-66` (RESULT_OK → `setResult`, then `finish()`). Called by `SelectTagDialog.finish` (`SelectTagDialog.java:191-193`: `((FragmentCallback) activity).onFragmentFinished(this, intent, code)`), reached from dialog cancel (`:160`), tag click (`:183`), and back press (`:188`). |
| 40 | SelectTagDialog.<clinit> | REACHABLE | INFERRED | Static `TAG = SelectTagDialog.class.getSimpleName()` (`SelectTagDialog.java:52`); class initialisation on first use via `SelectTagDialog.newInstance` (`:63-64`, called from SelectTagActivity.onCreate `:51`). |

## Spot-checks done in this pass (against ~/workspace/batch117-118-src/ saved copies)
- Scheduling: `newInstance` :53, `subscribeAlertDialog` called from onStart :126 and defined :129-141, `showExactAlarmPermissionDialog` defined :143-161 and called :201,:214,:224,:230, TimePreference dialog `newInstance` :179.
- Storage: `newInstance` :64, `dirChooseDialog` defined :227 and called :105,:132,:159,:186, `downloadDirChoose.launch` :239.
- Streaming: `newInstance` :43, `bindOnPreferenceChangeListener` registrations :62,:71,:83, defined :93-95.
- AddTagButton/TagsList/SelectTag: `TorrentTagsList.init` :36 calls `buildAddTagButton`, which constructs `new AddTagButton(context)` :79; `SelectTagActivity.onCreate` :51-52 creates/shows the dialog via `SelectTagDialog.newInstance`; `SelectTagDialog.finish` :191-193 calls `((FragmentCallback) activity).onFragmentFinished(...)`, matching batch 118 row 39.
- <clinit> rows: non-constant `TAG = ….class.getSimpleName()` confirmed for Storage :54, Streaming :39, SelectTagDialog :52 (and Network :70, Proxy :49 in batch 117).

## Caveats the merger must see (undecided conventions recorded, not decided)
1. **Strict-entry caveat (all rows):** the launcher → SettingsActivity → SettingsFragment step was NOT printed in the prior pass and was not freshly printed in this pass. Under a strict launcher-entry rule all section rows (117 rows 1–40; 118 rows 1–33) revert to OPEN. They are judged REACHABLE on the printed settings trunk, the same convention as sibling settings batches 115–116. The merger must pick one entry convention for all settings batches.
2. **Tag rows 34–38 strict-entry gaps:** the in-app start Intent for SelectTagActivity was NOT freshly printed in the prior pass (sibling batch 119 printed the DetailTorrentInfoFragment tags-listener route — a lead only, not this pass's evidence), and the detail-info host step for TorrentTagsList was not re-printed here. Rows 34–38 are therefore entry-conditional in the same strict-entry sense as row group 1; row 39's dialog→activity call IS printed, but it presupposes the activity showing the dialog.
3. **Lambda numbering:** `$n` numbering is source-order sequential, NOT bytecode-verified — confirm at merge (notably Storage $0–$4: four onCreate click lambdas then the `downloadDirChoose` field callback $4; Streaming $0). A swap within a group does not change any label.
4. **confirmed_by convention:** SOURCE = a printed direct in-app call site naming the method (or a printed registration/call in the same file for a private helper); INFERRED = reached only through unprinted framework/library dispatch (fragment lifecycle, preference-change/click/bind-text listeners, ActivityResult callbacks, class initialisation) where definition + registration are printed but dispatch itself is not printed from fw_src. This is the per-row convention, not a whole-route convention; labels are unaffected, only confirmed_by would change at merge if the merger adopts the whole-route convention.
5. **Not claimed:** no build, sampler, full-repo grep, or C1 — no full local checkout (git clone of the private repo still fails in this VM with no credential device, named missing check, not passed). Main-agent spot-check (1 in 5), py_compile, build, and Mac build/C1 are still owed before merging. **0 rows verified for merge.**
