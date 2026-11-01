# Stream A Phase 2 spot-check — batch 116

Source re-derived from already-fetched local copies only
(`~/workspace/b115116-src/`); no connector fetch was needed, no 429 hit.
The merge-ready file was NOT edited; no label was changed here.
Phase 1 label changes: none listed in this file's revision notes, so
the checked set is the sample rows 1, 6, 11, 16, 21, 26, 31, 36 only.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | AppearanceSettingsFragment.lambda$onPreferenceChange$2 | REACHABLE / INFERRED | PASS | Snackbar action lambda at AppearanceSettingsFragment.java:234 `.setAction(R.string.apply, (v) -> restartMainActivity())`; descriptor (View)V matches; Snackbar action dispatch unprinted. Lambda numbering is source-order, not bytecode-verified; label unaffected. |
| 6 | AppearanceSettingsFragment.onViewCreated | REACHABLE / INFERRED | PASS | Definition AppearanceSettingsFragment.java:66-71, setting `coordinatorLayout` at :70 (needed by row 1's Snackbar); framework lifecycle dispatch unprinted. |
| 11 | BehaviorSettingsFragment.disableBatteryControl | REACHABLE / SOURCE | PASS | Called in onPreferenceChange at BehaviorSettingsFragment.java:209; definition :267-275, calling row 12 at :274. |
| 16 | BehaviorSettingsFragment.onCreate | REACHABLE / INFERRED | PASS | Definition BehaviorSettingsFragment.java:63-157 (loads repo/dialog ViewModel, binds preferences, registers the row-13 lambda at :151); framework lifecycle after newInstance. |
| 21 | BehaviorSettingsFragment.showCustomBatteryDialog | REACHABLE / SOURCE | PASS | Called in onPreferenceChange at BehaviorSettingsFragment.java:221; definition :247-265. |
| 26 | FeedSettingsFragment.newInstance | REACHABLE / SOURCE | PASS | Called by SettingsFragment.java:195 (large-screen) and :198 (small-screen startActivity), and by PreferenceActivity.java:114; definition FeedSettingsFragment.java:42-48 (`new FeedSettingsFragment()` :44). |
| 31 | LimitationsSettingsFragment.\<init\> | REACHABLE / SOURCE | PASS | Implicit default ctor; called by newInstance at LimitationsSettingsFragment.java:46 `new LimitationsSettingsFragment()`. |
| 36 | LimitationsSettingsFragment.lambda$onCreate$3 | REACHABLE / INFERRED | PASS | Max-active-uploads bind lambda at LimitationsSettingsFragment.java:117 `setOnBindEditTextListener((editText) -> editText.setFilters(queueingFilter))`; queueingFilter built at :60-65 (min -1, max Integer.MAX_VALUE). Fourth onCreate lambda in source order (:77 $0, :88 $1, :99 $2, :117 $3), matching the filed $3; numbering not bytecode-verified, label unaffected. |

## Totals

- Checked: 8 rows. PASS: 8. FAIL: 0.
- Proposed corrections: none.

## Notes

- One cross-file misstatement flagged for the coordinator (found while
  checking batch 115): this batch's caveat 5 says batch 115 row 40's
  descriptor "includes the captured SettingsRepository" — it does not
  (row 40 is `(ActivityResult)V`; the capturing descriptor belongs to
  batch 115 row 39). No batch 116 row is affected.
- Build/sampler/C1: not run (not this task).
