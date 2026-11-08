# Stream A Phase 2 spot-check — batch 118

Source re-derived from already-fetched local copies only
(`~/workspace/batch117-118-src/` plus `~/workspace/b119120-src/` for the
row-36 start-site cross-check); no connector fetch was needed, no 429
hit. The merge-ready file was NOT edited; no label was changed here.
Phase 1 label changes: none listed (no OPEN rows in this batch), so the
checked set is the sample rows 1, 6, 11, 16, 21, 26, 31, 36 only.
The owed D10 API-gate extension to batch 118 was NOT decided here, per
task; sampled rows were re-derived as filed and screened for any verdict
turning on that extension (see D10 note below).

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | SchedulingSettingsFragment.lambda$subscribeAlertDialog$0 | REACHABLE / INFERRED | PASS | Event lambda inside subscribeAlertDialog at SchedulingSettingsFragment.java:129-141 (tag check vs TAG_EXACT_ALARM_PERMISSION_DIALOG, POSITIVE_BUTTON_CLICKED -> `Utils.requestExactAlarmPermission`); subscribed via Rx `.subscribe(...)` at :130; Rx dispatch unprinted. |
| 6 | SchedulingSettingsFragment.onPreferenceChange | REACHABLE / INFERRED | PASS | Definition SchedulingSettingsFragment.java:191-235; calls row 9 (showExactAlarmPermissionDialog) at :201, :214, :224, :230. Registered via batch 117 row 40's bind method; framework dispatch unprinted. |
| 11 | StorageSettingsFragment.\<clinit\> | REACHABLE / INFERRED | PASS | Non-constant static `TAG = StorageSettingsFragment.class.getSimpleName()` at StorageSettingsFragment.java:54; first use via newInstance (row 20), called from SettingsFragment.java:168. Convention (ix) undecided; stands as INFERRED as filed. |
| 16 | StorageSettingsFragment.lambda$onCreate$0 | REACHABLE / INFERRED | PASS | Save-torrents-in click lambda StorageSettingsFragment.java:103-108 (sets `dirChooserBindPref`, calls row 14 `dirChooseDialog(uri)` at :105). Click dispatch unprinted. |
| 21 | StorageSettingsFragment.onCreate | REACHABLE / INFERRED | PASS | Definition StorageSettingsFragment.java:81-207 (restores `dirChooserBindPref` from saved state :85-86, loads fs/repo, finds/binds preferences); framework lifecycle after newInstance. |
| 26 | StreamingSettingsFragment.\<clinit\> | REACHABLE / INFERRED | PASS | Non-constant static `TAG = StreamingSettingsFragment.class.getSimpleName()` at StreamingSettingsFragment.java:39; first use via newInstance (row 30), called from SettingsFragment.java:204. Convention (ix) undecided; stands as INFERRED as filed. |
| 31 | StreamingSettingsFragment.onCreate | REACHABLE / INFERRED | PASS | Definition StreamingSettingsFragment.java:52-86 (loads repo, enable/hostname/port preferences, binds listeners at :62, :71, :83); framework lifecycle after newInstance. |
| 36 | SelectTagActivity.\<init\> | REACHABLE / INFERRED | PASS | Implicit default ctor; framework instantiation. The start site the batch-118 file left unprinted is now confirmed from the batch-119 print: DetailTorrentInfoFragment.java:158 builds `new Intent(activity, SelectTagActivity.class)` and :163 launches it via `selectTag.launch(i)`; SelectTagActivity.onCreate at SelectTagActivity.java:42-53 then creates/shows the dialog (:51-52). This strengthens, not weakens, the filed INFERRED verdict; the strict-entry caveat for the detail host step itself is unchanged and undecided. |

## Totals

- Checked: 8 rows. PASS: 8. FAIL: 0.
- Proposed corrections: none.

## D10 note (flagged, not decided)

- No sampled row's verdict turns on the owed D10 API-gate extension:
  grep over all batch-118 source files (Scheduling, Storage, Streaming,
  AddTagButton, SelectTagActivity, SelectTagDialog, TorrentTagsList)
  finds ZERO `SDK_INT` / `VERSION_CODES` hits, and no sampled row cites
  an API gate. The extension decision for batch 118 (DECISIONS.md: apply
  D10 to batches 45/46/118 on their own files) remains owed and is NOT
  decided here; nothing in this spot-check presupposes its outcome.
- Build/sampler/C1: not run (not this task).
