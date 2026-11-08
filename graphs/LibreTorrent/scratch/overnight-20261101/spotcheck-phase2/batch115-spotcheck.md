# Stream A Phase 2 spot-check — batch 115

Source re-derived from already-fetched local copies only
(`~/workspace/b115116-src/`); no connector fetch was needed, no 429 hit.
The merge-ready file was NOT edited; no label was changed here.
Phase 1 label changes: none (Phase 1c: 0 flips; OPEN-closing round 2:
0 flips). Checked set: sample rows 1, 6, 11, 16, 21, 26, 31, 36 PLUS
must-include rows 38, 39, 40 (D10 closed_by_api_level group).

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | SettingsFragment.startActivity | REACHABLE / SOURCE | PASS | Definition SettingsFragment.java:232-241; called from openPreference small-screen branches :144, :153, :162, :171, :180, :189, :198, :207. |
| 6 | SummaryPreference.onBindViewHolder | REACHABLE / INFERRED | PASS | Definition SummaryPreference.java:65-76; anchored by pref_anonymous_mode.xml:8-9 declaring SummaryPreference and AnonymousModeSettingsFragment.java:67 loading that screen. Framework bind dispatch unprinted. |
| 11 | SwitchBarPreference.\<init\>(Context,AttributeSet,int,int) | REACHABLE / SOURCE | PASS | Called by the 3-arg ctor at SwitchBarPreference.java:53 `this(context, attrs, defStyleAttr, defStyleAttr)`; definition :56-61. |
| 16 | TimePreference.\<init\>(Context,AttributeSet,int) | REACHABLE / SOURCE | PASS | Called by the 2-arg ctor at TimePreference.java:41-42 `this(context, attrs, R.attr.preferenceStyle)`; definition :45-50. |
| 21 | TimePreference.getTime | REACHABLE / SOURCE | PASS | TimePreferenceDialogFragmentCompat.java:59 `((TimePreference) preference).getTime()`; definition TimePreference.java:65-68. |
| 26 | TimePreferenceDialogFragmentCompat.newInstance | REACHABLE / SOURCE | PASS | SchedulingSettingsFragment.java:179 `newInstance(preference.getKey())` inside onDisplayPreferenceDialog (:175-189), shown at :183-184; definition TimePreferenceDialogFragmentCompat.java:32-41. |
| 31 | AnonymousModeSettingsFragment.bindOnPreferenceChangeListener | REACHABLE / SOURCE | PASS | Called in onCreate at AnonymousModeSettingsFragment.java:60; definition :70-73. |
| 36 | AppearanceSettingsFragment.\<init\> | REACHABLE / SOURCE | PASS | Implicit default ctor; called by newInstance at AppearanceSettingsFragment.java:59 `new AppearanceSettingsFragment()`. |
| 38 | AppearanceSettingsFragment.initLegacyNotifySettings | UNREACHABLE closed_by_api_level / SOURCE | PASS (label; see tension note) | API gate verified: AppearanceSettingsFragment.java:118-119 `if (Build.VERSION.SDK_INT < Build.VERSION_CODES.O) initLegacyNotifySettings(pref)`. O = 26, standard API 27, so 27 < 26 is false and the only call site never runs at API 27. Body :128-190. Label stands under D10's method-vs-branch rule. |
| 39 | AppearanceSettingsFragment.lambda$initLegacyNotifySettings$0 | UNREACHABLE closed_by_api_level / SOURCE | FAIL — citation/body swapped with row 40 (label stands after correction) | Filed citation (result lambda :200-217, field :198-217) does NOT match this row's name/descriptor. Name `lambda$initLegacyNotifySettings$0` with descriptor `(SettingsRepository, Preference)Z` is the notify-sound click lambda INSIDE initLegacyNotifySettings at AppearanceSettingsFragment.java:144-167: it captures the `pref` (SettingsRepository) parameter, takes a Preference, returns boolean, and calls `ringtonePicker.launch(intent)` at :164. The :200-217 body is the `registerForActivityResult` result callback, which is a field initialiser, takes an ActivityResult, and returns void — i.e. row 40's method. Proposed correction: row 39's body is :144-167, registered only inside the gated initLegacyNotifySettings, so the UNREACHABLE closed_by_api_level label still holds after the swap. |
| 40 | AppearanceSettingsFragment.lambda$new$1 | UNREACHABLE closed_by_api_level / SOURCE | FAIL — citation/body swapped with row 39 (label stands after correction) | Filed citation (click lambda :144-167) does NOT match this row's name/descriptor. Name `lambda$new$1` with descriptor `(ActivityResult)V` is the `registerForActivityResult` result callback at AppearanceSettingsFragment.java:198-217 (field :198, `result -> {...}` body :200-217). The :144-167 body is the initLegacy click lambda, i.e. row 39's method. Proposed correction: row 40's body is :198-217; its only trigger is `ringtonePicker.launch(intent)` at :164 inside the gated initLegacyNotifySettings, so the UNREACHABLE closed_by_api_level label still holds after the swap. |

## Totals

- Checked: 11 rows. PASS: 9. FAIL: 2 (rows 39, 40 — citation swap only; no label flip proposed).
- Proposed corrections: swap the row 39 / row 40 body citations as
  detailed above (39 -> :144-167; 40 -> :198-217). Do not change the
  labels or the confirmed_by values in this spot-check file.

## Tension reported, not resolved (do not change confirmed_by)

- Rows 38, 39, 40 are filed with confirmed_by SOURCE, while D10
  (DECISIONS.md, "API-gate consistency") states the
  closed_by_api_level rows may be marked UNREACHABLE
  `closed_by_api_level` (INFERRED). The filed SOURCE follows the
  per-row convention (a printed call site / printed registration
  names the method, even though the call site is gated off at API 27);
  D10's parenthetical says INFERRED. This tension is reported for the
  coordinator/merger; confirmed_by was NOT changed here.
- Related misstatement flagged (not in this batch's file, for the
  coordinator): the batch 116 file's caveat 5 says batch 115 row 40's
  descriptor "includes the captured SettingsRepository" — it does not.
  Row 40's descriptor is `(ActivityResult)V`; the
  SettingsRepository-capturing descriptor `(SettingsRepository,
  Preference)Z` belongs to row 39. This is consistent with the swap
  found above.

## Notes

- Build/sampler/C1: not run (not this task).
