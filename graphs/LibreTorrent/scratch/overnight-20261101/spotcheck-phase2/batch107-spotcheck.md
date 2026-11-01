# LibreTorrent batch 107 — Phase 2 spot-check — UNVERIFIED spot-check, NOT a merge

- Batch: 107. Source checked: already-fetched local copies in ~/workspace/b107-108-src/ plus layout ~/workspace/overnight/stream-A/corpus/res/layout/activity_log_settings.xml; no connector fetch needed, no 429. No Phase-1 label-change revision note was found in this file, so samples only.
- Rows checked (8): samples 1, 6, 11, 16, 21, 26, 31, 36.
- Build/sampler/C1: not run (not this task). No edit made to the merge-ready file. No convention decided.

## Per-row verdicts

| # | Method | Filed label | Verdict | Evidence (printed source) |
|---|---|---|---|---|
| 1 | LogSettingsActivity.<clinit> | REACHABLE INFERRED | PASS | Static TAG LogSettingsActivity.java:32 (`getSimpleName()`, non-constant, runs at class init); activity started by LogActivity.java:261 `startActivity(new Intent(this, LogSettingsActivity.class))` in showLogSettings. JVM step, not printed. |
| 6 | LogSettingsFragment.<init> | REACHABLE INFERRED | PASS | Implicit default constructor; framework instantiation. Stronger than the merge-ready file's caveat: activity_log_settings.xml:14 hosts the fragment (`class="org.proninyaroslav.libretorrent.ui.log.LogSettingsFragment"`) in the activity set by LogSettingsActivity.java:42, and LogSettingsFragment.java:43-45 also defines newInstance() constructing it. |
| 11 | LogSettingsFragment.onPreferenceChange | REACHABLE INFERRED | PASS | Registered via bindOnPreferenceChangeListener LogSettingsFragment.java:73 and :83-86; def :89-101 (pref_key_max_log_size); preference dispatch, not printed. |
| 16 | LogViewModel.getLogEntriesCount | REACHABLE SOURCE | PASS | LogActivity.java:445 `viewModel.getLogEntriesCount()` in updateToolbarSubtitle; def LogViewModel.java:162-165. |
| 21 | LogViewModel.observeLog | REACHABLE SOURCE | PASS | LogActivity.java:119 `viewModel.observeLog().observe(...)`; def LogViewModel.java:92-96. |
| 26 | LogViewModel.resumeLogManually | REACHABLE SOURCE | PASS | LogActivity.java:270 pauseResumeLog (newPausedState false branch) calls `viewModel.resumeLogManually()`; def LogViewModel.java:156-160. |
| 31 | LogViewModel$1.onPropertyChanged | REACHABLE INFERRED | PASS | Registered LogViewModel.java:89 `addOnPropertyChangedCallback(paramsCallback)`; callback body :107-137 (BR.logging / filter switch); databinding dispatch, not printed. |
| 36 | SessionLogFilterDialog.lambda$onResume$0 | REACHABLE INFERRED | PASS | setOnKeyListener lambda SessionLogFilterDialog.java:74 inside onResume :69-86; body calls onBackPressed :79 on KEYCODE_BACK ACTION_DOWN; key dispatch, not printed. |

## Totals

- PASS: 8 / FAIL: 0 (of 8 checked).
- Proposed corrections: none.
