# Remaining UI route audit 2: Feed and Streaming settings

Scope: source-backed entry and preference callback routes for `FeedSettingsFragment` and `StreamingSettingsFragment`. The exact printed excerpts are in `scratch/routes_remaining_2_printed.txt`. This audit uses at most 14 app methods across these two sections; it does not claim AndroidX callback dispatch is verified.

Both fragments are reached from the Settings UI by selecting their preference row in `SettingsFragment.openPreference`, which calls the section's `newInstance()` and either installs the result in the two-pane container or starts `PreferenceActivity` with the fragment class name. The legacy `PreferenceActivity` configured-fragment factory also calls both `newInstance()` methods. These app-level calls are printed. The enclosing header click and preference-screen lifecycle dispatch come from AndroidX and remain inferred, matching the existing settings audit convention.

| Source | Target | Proposed edge | Guard / route qualification | Printed evidence |
|---|---|---|---|---|
| `SettingsFragment.openPreference()` | `FeedSettingsFragment.newInstance()` | explicit | `case FeedSettings`; occurs when the category is selected | `routes_remaining_2_printed.txt`, SettingsFragment lines 193–199 |
| `SettingsFragment.openPreference()` | `StreamingSettingsFragment.newInstance()` | explicit | `case StreamingSettings`; occurs when the category is selected | same, lines 202–208 |
| `FeedSettingsFragment.newInstance()` | `FeedSettingsFragment.<init>()` | explicit | Factory body | Feed source lines 42–48 |
| `StreamingSettingsFragment.newInstance()` | `StreamingSettingsFragment.<init>()` | explicit | Factory body | Streaming source lines 43–49 |
| `PreferenceActivity` configured factory | `FeedSettingsFragment.newInstance()` | explicit | Fragment name matches `FeedSettingsFragment` simple name | printed PreferenceActivity lines 113–114 |
| `PreferenceActivity` configured factory | `StreamingSettingsFragment.newInstance()` | explicit | Fragment name matches `StreamingSettingsFragment` simple name | printed PreferenceActivity lines 115–116 |
| settings host fragment transaction / PreferenceActivity fragment host | each section `onCreate(Bundle)` | non-standard (AndroidX fragment lifecycle) | Factory result must be selected/installed; implementation callback dispatch not printed from AndroidX | Existing `scratch/s3_settingsfragment_printed.txt`, `scratch/s3_preferenceactivity_printed.txt`; do not mark standard |
| each section `onCreate(Bundle)` | `RepositoryHelper.getSettingsRepository(Context)` | explicit | Both bodies directly assign `pref` from this helper | Feed lines 51–56; Streaming lines 51–56 |
| each section `onCreate(Bundle)` | `bindOnPreferenceChangeListener(Preference)` | explicit | One direct call per successfully resolved preference (null checks are ordinary guards) | Feed lines 57–109; Streaming lines 58–84 |
| each section `onCreate(Bundle)` | `Preference.setOnBindEditTextListener(...)` | explicit | Streaming port preference exists; listener installs `InputFilterRange.PORT_FILTER` | Streaming lines 74–84 |
| `onCreatePreferences(Bundle,String)` | `PreferenceFragmentCompat.setPreferencesFromResource(...)` | explicit | Direct call selects `pref_feed` / `pref_streaming` | Feed lines 113–117; Streaming lines 87–91 |
| `bindOnPreferenceChangeListener(Preference)` | `Preference.setOnPreferenceChangeListener(...)` | explicit | Direct listener registration (`this`) | Feed lines 119–122; Streaming lines 93–96 |
| AndroidX Preference change dispatch | each section `onPreferenceChange(Preference,Object)` | non-standard (AndroidX) | Requires user change of a registered preference; callback delivery remains inferred | Feed lines 124–162; Streaming lines 98–117 |
| `FeedSettingsFragment.onPreferenceChange(...)` | `Scheduler.runPeriodicalRefreshFeeds(Context,long)` | explicit | Auto-refresh changed to true, or interval changed | Feed lines 129–143 |
| `FeedSettingsFragment.onPreferenceChange(...)` | `Scheduler.cancelPeriodicalRefreshFeeds(Context)` | explicit | Auto-refresh changed to false | Feed lines 129–137 |
| each section `onPreferenceChange(...)` | corresponding `SettingsRepository` setter(s) | explicit | Branch on preference key; Feed has seven keys, Streaming has three | Feed lines 129–159; Streaming lines 101–114 |

The `onPreferenceChange` targets should remain reachable only through the inferred AndroidX callback edge, not by treating the listener registration itself as proof of a user event. The ordinary key checks, null checks, empty-string check, and boolean switch values are branch conditions, not structured environment/state gates. The Feed scheduler helper calls are direct app calls; scheduling a future receiver event is outside this screen-local route.

## Method count

Distinct app methods in this proposed screen-local set: `SettingsFragment.openPreference`, both section `newInstance` factories, both constructors, both section `onCreate`, both `onCreatePreferences`, both `bindOnPreferenceChangeListener`, both `onPreferenceChange`, plus configured factory dispatch in `PreferenceActivity` = 14. No graph files, labels, or build outputs were changed.
