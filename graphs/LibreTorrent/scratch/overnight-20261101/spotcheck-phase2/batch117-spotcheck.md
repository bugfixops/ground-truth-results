# Stream A Phase 2 spot-check — batch 117

Source re-derived from already-fetched local copies only
(`~/workspace/batch117-118-src/`); no connector fetch was needed, no 429
hit. The merge-ready file was NOT edited; no label was changed here.
Phase 1 label changes: none listed (no OPEN rows in this batch), so the
checked set is the sample rows 1, 6, 11, 16, 21, 26, 31, 36 only.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | LimitationsSettingsFragment.newInstance | REACHABLE / SOURCE | PASS | Called by SettingsFragment.java:177 (large-screen branch); definition LimitationsSettingsFragment.java:44-49 (`new LimitationsSettingsFragment()` :46). |
| 6 | NetworkSettingsFragment.\<clinit\> | REACHABLE / INFERRED | PASS | Non-constant static `TAG = NetworkSettingsFragment.class.getSimpleName()` at NetworkSettingsFragment.java:70; first use via newInstance (row 17), called from SettingsFragment.java:159. Convention (ix) is undecided project-wide; the row stands as INFERRED as filed and reverts to OPEN only if the merger requires more. |
| 11 | NetworkSettingsFragment.lambda$new$6 | REACHABLE / INFERRED | PASS | `anonymousModeActivity` ActivityResult callback body NetworkSettingsFragment.java:405-413 (refreshes the anonymous-mode summary); launched from the anonymous-mode click branch at :257 (inside row 16's lambda). Result dispatch unprinted. Numbering ($6) is source-order, not bytecode-verified; label unaffected. |
| 16 | NetworkSettingsFragment.lambda$onCreate$4 | REACHABLE / INFERRED | PASS | Anonymous-mode click lambda NetworkSettingsFragment.java:246-262 (large-screen `setFragment(AnonymousModeSettingsFragment.newInstance())` :248; small-screen Intent + `anonymousModeActivity.launch(i)` :257). Click dispatch unprinted. |
| 21 | NetworkSettingsFragment.onPreferenceChange | REACHABLE / INFERRED | PASS | Definition NetworkSettingsFragment.java:304-359; registered via bindOnPreferenceChangeListener (row 8) at :115, :122, :129, :136, :143, :154, :166, :176, :184, :192, :199, :224, :268, :275. Framework preference-change dispatch unprinted. |
| 26 | ProxySettingsFragment.\<init\> | REACHABLE / SOURCE | FAIL — citation line off by one (label stands) | The construction site exists, but the filed line is wrong: the file cites newInstance :57 for `new ProxySettingsFragment()`, while the printed file has newInstance defined at ProxySettingsFragment.java:56, `{` at :57, and `new ProxySettingsFragment()` at :58. The filed definition range :56-61 is also short (the method returns at :62). Proposed correction: cite :58 for the construction (definition :56-63). Label REACHABLE SOURCE is unchanged — the implicit default ctor IS constructed by the printed newInstance. |
| 31 | ProxySettingsFragment.lambda$onPreferenceChange$3 | REACHABLE / INFERRED | PASS | Password-branch bind lambda ProxySettingsFragment.java:232-234 (`setOnBindEditTextListener` with the transformation-method summary). Registered inside onPreferenceChange; dialog-binding dispatch unprinted. |
| 36 | ProxySettingsFragment.onDestroy | REACHABLE / INFERRED | PASS | Definition ProxySettingsFragment.java:82-93 (shows the "apply after reboot" toast if `proxyChanged`); framework lifecycle dispatch unprinted. |

## Totals

- Checked: 8 rows. PASS: 7. FAIL: 1 (row 26 — citation line only; no label flip proposed).
- Proposed corrections: batch 117 row 26: change the cited
  construction line from :57 to :58 (definition range :56-63).

## Notes

- Build/sampler/C1: not run (not this task).
