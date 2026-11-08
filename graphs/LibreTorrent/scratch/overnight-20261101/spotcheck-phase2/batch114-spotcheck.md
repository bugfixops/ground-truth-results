# Stream A Phase 2 spot-check — batch 114

Source re-derived from already-fetched local copies only
(`~/workspace/b113-114-src/`); no connector fetch was needed, no 429 hit.
The merge-ready file was NOT edited; no label was changed here.
Phase 1 label changes: none (Phase 1c: 0 flips; OPEN-closing round 2:
0 flips). Checked set: sample rows 1, 6, 11, 16, 21, 26, 31, 36 PLUS
must-include row 27 (D5c Option B).

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | drawer.TagsAdapter$ItemViewHolder.bind(AbstractTagItem,OnClickListener) | REACHABLE / SOURCE | PASS | Printed call TagsAdapter.java:99 `holder.bind(item, listener)`; body :177-184 checks `instanceof TagItem` then calls the typed overload at :182. |
| 6 | drawer.TagsAdapter$NoTagsItemViewHolder.\<init\> | REACHABLE / SOURCE | PASS | Printed construction TagsAdapter.java:88 `new NoTagsItemViewHolder(binding)`; definition :275-279 (`super(binding.getRoot())` :276). |
| 11 | PreferenceActivity.\<init\> | REACHABLE / INFERRED | PASS | Implicit default ctor (none declared in PreferenceActivity.java); framework instantiation on SettingsFragment.java:240 `startActivity(i)` (Intent built at :234 for PreferenceActivity.class). |
| 16 | PreferenceActivityConfig.\<clinit\> | REACHABLE / INFERRED | PASS | Static CREATOR field PreferenceActivityConfig.java:79-93; first printed use SettingsFragment.java:235 `new PreferenceActivityConfig(...)`. Class-init timing is the unprinted JVM rule, hence INFERRED. |
| 21 | PreferenceActivityConfig.getTitle | REACHABLE / SOURCE | PASS | PreferenceActivity.java:71 `title = config.getTitle()`; definition PreferenceActivityConfig.java:61-64. |
| 26 | PreferenceActivityConfig$1.createFromParcel | REACHABLE / INFERRED | PASS | Body PreferenceActivityConfig.java:83-86 `new PreferenceActivityConfig(source)`; framework unparcel dispatch on PreferenceActivity.java:69 `getParcelableExtra(TAG_CONFIG)`. |
| 27 | PreferenceActivityConfig$1.newArray | OPEN / — | PASS | Definition PreferenceActivityConfig.java:89-92. Stays OPEN under D5c Option B (newArray requires a printed Parcelable-array site): the only printed parcel sites are the single extra SettingsFragment.java:239 `putExtra` / PreferenceActivity.java:69 `getParcelableExtra`; grep over the printed files finds ZERO `getParcelableArrayExtra` / `putParcelableArray*` sites. A single extra never calls newArray, but that alone is not proof no array site exists elsewhere, so no flip to UNREACHABLE. The batch 102/114 inconsistency (batch 102 row 17 REACHABLE on single-extra dispatch alone) remains flagged, not decided here. |
| 31 | SettingsActivity.onCreate | REACHABLE / INFERRED | PASS | Body SettingsActivity.java:42-62 (ViewModel :47, setContentView :49, observer :58-61); framework lifecycle on MainActivity.java:743 `startActivity(new Intent(this, SettingsActivity.class))`. |
| 36 | SettingsFragment.onAttach | REACHABLE / INFERRED | PASS | Body SettingsFragment.java:73-79 (`super.onAttach` :75, activity capture :77-78); framework lifecycle dispatch unprinted. |

## Totals

- Checked: 9 rows. PASS: 9. FAIL: 0.
- Proposed corrections: none.

## Notes

- Rows 22/23 (PreferenceActivityConfig setters) were not in the checked
  set, but the re-grep confirms the filed position: no `config.setFragment`
  / `config.setTitle` site in the printed files (the `setFragment` /
  `setTitle` hits are SettingsFragment.setFragment and
  `toolbar.setTitle`, different methods).
- Build/sampler/C1: not run (not this task).
