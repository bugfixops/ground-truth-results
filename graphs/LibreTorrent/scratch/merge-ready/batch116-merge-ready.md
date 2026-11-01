# LibreTorrent batch 116 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another helper's file.**
**Build: not run. C1: not run.** Build and C1 run on the user's Mac after a push, so they are marked "not run" here, never passed. No sampler, full-repo grep, or `py_compile` was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 116 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, from printed source. The prior batch-116 proposal (`~/workspace/libretorrent-batch116-proposal.md`) was used as an INPUT, not a result; every row below was re-judged against freshly printed source in this pass.

## Membership — verified, not guessed

Exactly the 40 rows for batch 116 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the local plan copy `~/workspace/agent27-plan.tsv` (4,733 lines incl. header; plan blob SHA `0104806dd666c840049b3db52823d4b384fa1c92`). All 40 rows are `TODO_CANDIDATE_REACHABLE` in the plan (candidates, not evidence), in plan order. This file was generated from the plan rows, so names and JVM descriptors cannot drift; the verification section below re-checks them mechanically.

## Printed source used in this pass (fresh, branch `work-2026-10-31`, GitHub connector only, one file at a time with ~25 s pauses, no fresh HTTP 429)

Java base `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`, saved under `~/workspace/b115116-src/` (raw connector JSON kept alongside the earlier helper fetches where present; this pass saved plain files):
- `ui/settings/SettingsFragment.java` (242 lines, sha256 `06161ca59281…`)
- `ui/settings/SettingsViewModel.java` (28 lines, `e102a7efdbc1…`)
- `ui/settings/SettingsActivity.java` (73 lines, `24af6befd1a4…`)
- `ui/settings/PreferenceActivity.java` (132 lines, `85013c5862ff…`)
- `ui/settings/customprefs/SummaryPreference.java` (93 lines, `2115b5a552f5…`)
- `ui/settings/customprefs/SwitchBarPreference.java` (90 lines, `5ee6f1b8e29e…`)
- `ui/settings/customprefs/TimePreference.java` (127 lines, `e4f7f5205e53…`)
- `ui/settings/customprefs/TimePreferenceDialogFragmentCompat.java` (104 lines, `b8fb9e2079e0…`)
- `ui/settings/sections/AnonymousModeSettingsFragment.java` (83 lines, `0a4fa9a57d46…`)
- `ui/settings/sections/AppearanceSettingsFragment.java` (271 lines, `4187e60d2241…`)
- `ui/settings/sections/BehaviorSettingsFragment.java` (285 lines, `134fb30aa995…`)
- `ui/settings/sections/FeedSettingsFragment.java` (163 lines, `1466517d6363…`)
- `ui/settings/sections/LimitationsSettingsFragment.java` (257 lines, `1d99b4ee793a…`)
- `ui/settings/sections/NetworkSettingsFragment.java` (414 lines, `5c77f3857ad4…`, anonymous-mode click site only)
- `ui/settings/sections/SchedulingSettingsFragment.java` (242 lines, `c302e6019bf7…`, TimePreference anchor + dialog-display step only)
XML base `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/res/xml/`, same directory:
- `pref_anonymous_mode.xml` (9 lines, `a10d060afecc…`) — declares SwitchBarPreference (key anonymous_mode) AND SummaryPreference (summary only, no key).
- `pref_appearance.xml` (89 lines, `b12a00c33420…`) — theme, torrent-finish-notify, legacy notify prefs (play_sound, notify_sound, led_indicator, led_indicator_color, vibration), foreground-notify prefs.
- `pref_behavior.xml` (88 lines, `e2d1f559faf1…`), `pref_feed.xml` (62 lines, `b89b1cb6f6…`), `pref_limitations.xml` (77 lines, `0f8c7044133e…`), `pref_scheduling.xml` (46 lines, `fc9032596ae9…`, declares TimePreference twice), `pref_network.xml` (136 lines, `96449b45d671…`).
Layout base `.../app/src/main/res/layout/`, same directory:
- `activity_settings_portrait.xml` (16 lines, `22226a77064f…`) and `activity_settings_two_pane.xml` (45 lines, `9c772627d00f…`) — BOTH host SettingsFragment via FragmentContainerView class `org.proninyaroslav.libretorrent.ui.settings.SettingsFragment`. There is no plain `activity_settings.xml` in the layout directory listing (69 files); the two variants are what `R.layout.activity_settings` resolves to. A first fetch of `activity_settings.xml` returned a clean file-not-found (not a 429).

## Shared routes (printed steps, cited once and reused by row)

**R-SETTINGS — MainActivity menu → SettingsActivity → SettingsFragment → section fragments.** MainActivity settings-menu → SettingsActivity and the launcher → MainActivity step were printed in sibling batches (114 and 109–110) but were NOT freshly printed in this pass — see Caveats. Fresh in this pass: SettingsActivity.onCreate :42–62 (ViewModelProvider :47, setContentView(R.layout.activity_settings) :49, detailTitle observer :58–61); both settings layouts host SettingsFragment (portrait + two-pane, above); SettingsFragment.onViewCreated :82–129 (ViewModelProvider :88, two-pane default Appearance fragment :94–95, click listeners on every section preference :98–128); SettingsFragment.openPreference :136–212 (large-screen setFragment(newInstance()) vs small-screen startActivity(class) per section); SettingsFragment.setFragment :220–230 (writes viewModel.detailTitleChanged :222, replaces detail_fragment_container :225–228); SettingsFragment.startActivity :232–241 (builds the PreferenceActivity intent + config parcel :235–239, startActivity :240); PreferenceActivity.onCreate :52–83 (small-screen guard :58–61 finishes on large screens; reads the config parcel :68–71; setFragment(getFragment(fragment)) :82); PreferenceActivity.getFragment :94–122 (dispatches each section simple name back to its newInstance()).

**Confirmed_by convention used here.** SOURCE = the method's own call site is printed in app code (explicit `new`, method call, or a printed call inside the same file). INFERRED = the only step into the method is a framework/library dispatch (fragment/activity lifecycle, preference inflation, widget/listener dispatch, Rx subscription, ViewModelProvider instantiation, JVM class initialisation) from a printed registration/start site. A row whose upstream dispatch is INFERRED but whose own call site is a printed explicit call is marked SOURCE, with the upstream caveat noted. Under a whole-route INFERRED convention, those SOURCE rows would flip to INFERRED; labels are unaffected, only confirmed_by would change at merge.

## Counts — proposed, not verified (mechanically verified: 40 rows, sequence 1–40 intact)

- REACHABLE proposed: 40 / 40 (SOURCE 14, INFERRED 26)
- UNREACHABLE proposed: 0
- OPEN: 0 / 40
- Verified for merge: 0

## Per-method table (all 40 rows, in plan order)

| # | Method (plan) | JVM descriptor | Proposed label | confirmed_by | Route / printed citations |
|---|---|---|---|---|---|
| 1 | AppearanceSettingsFragment.lambda$onPreferenceChange$2 | `(Landroid/view/View;)V` | REACHABLE | INFERRED | Snackbar action lambda (v) -> restartMainActivity(), registered in onPreferenceChange theme branch, AppearanceSettingsFragment.java:234 (.setAction(R.string.apply, (v) -> restartMainActivity())); Snackbar action dispatch unprinted. Runs after a theme change when the user taps Apply. Descriptor (View)V matches. |
| 2 | AppearanceSettingsFragment.newInstance | `()Lorg/proninyaroslav/libretorrent/ui/settings/sections/AppearanceSettingsFragment;` | REACHABLE | SOURCE | Called by SettingsFragment.java:94 (two-pane default) and :141 (openPreference, large-screen branch), and by PreferenceActivity.java:98 (small-screen dispatch). Def AppearanceSettingsFragment.java:57-63. |
| 3 | AppearanceSettingsFragment.onCreate | `(Landroid/os/Bundle;)V` | REACHABLE | INFERRED | Def AppearanceSettingsFragment.java:74-120; fragment lifecycle after newInstance (row 2). Loads the repo, finds theme/notify preferences, binds listeners, and (API-gated) calls the legacy setup -- see batch 115 rows 38-40 for the API 27 gate, which does NOT affect onCreate itself. |
| 4 | AppearanceSettingsFragment.onCreatePreferences | `(Landroid/os/Bundle;Ljava/lang/String;)V` | REACHABLE | INFERRED | Def AppearanceSettingsFragment.java:193-196; framework calls it; it loads R.xml.pref_appearance (freshly printed: contains theme, torrent-finish-notify, legacy notify prefs, foreground-notify prefs). |
| 5 | AppearanceSettingsFragment.onPreferenceChange | `(Landroidx/preference/Preference;Ljava/lang/Object;)Z` | REACHABLE | INFERRED | Registered via bindOnPreferenceChangeListener in onCreate (AppearanceSettingsFragment.java:85, :92, :100, :108, :115); framework dispatch on preference change; body :225-263 handles theme/notify keys (theme branch shows the Snackbar of row 1). Note: the legacy-key branches (:240-250) have no listener at API 27 (bound only in dead initLegacy), but the method itself is reachable via the theme etc. branches. |
| 6 | AppearanceSettingsFragment.onViewCreated | `(Landroid/view/View;Landroid/os/Bundle;)V` | REACHABLE | INFERRED | Def AppearanceSettingsFragment.java:66-71; framework lifecycle; it sets coordinatorLayout (view.findViewById(R.id.coordinator_layout)), which row 1's Snackbar needs. |
| 7 | AppearanceSettingsFragment.restartMainActivity | `()V` | REACHABLE | SOURCE | Called by row 1's Snackbar action lambda (AppearanceSettingsFragment.java:234); def :265-270 starts MainActivity with FLAG_ACTIVITY_CLEAR_TOP | FLAG_ACTIVITY_NEW_TASK. |
| 8 | BehaviorSettingsFragment.<clinit> | `()V` | REACHABLE | INFERRED | Non-constant TAG = BehaviorSettingsFragment.class.getSimpleName() (BehaviorSettingsFragment.java:45) plus first use via newInstance (row 15). Convention (ix) undecided; reverts to OPEN if the merger requires more. (TAG_CUSTOM_BATTERY_DIALOG :47 is a constant string and is not the basis.) |
| 9 | BehaviorSettingsFragment.<init> | `()V` | REACHABLE | SOURCE | Implicit default ctor, called by newInstance (BehaviorSettingsFragment.java:55 new BehaviorSettingsFragment()). |
| 10 | BehaviorSettingsFragment.bindOnPreferenceChangeListener | `(Landroidx/preference/Preference;)V` | REACHABLE | SOURCE | Called in onCreate for every preference (BehaviorSettingsFragment.java:75, :82, :89, :96, :103, :112, :121, :130, :137, :144, :155); def :193-196 sets the fragment as change listener. |
| 11 | BehaviorSettingsFragment.disableBatteryControl | `()V` | REACHABLE | SOURCE | Called in onPreferenceChange only-charging branch (BehaviorSettingsFragment.java:209); def :267-275 unchecks battery control and calls row 12 at :274. |
| 12 | BehaviorSettingsFragment.disableCustomBatteryControl | `()V` | REACHABLE | SOURCE | Called in onPreferenceChange battery-control branch (:215), by the subscribe lambda (:182), and by row 11 (:274); def :277-284 unchecks custom battery control. |
| 13 | BehaviorSettingsFragment.lambda$onCreate$0 | `(Landroid/widget/EditText;)V` | REACHABLE | INFERRED | EditText lambda (editText) -> editText.setSingleLine(false), registered at BehaviorSettingsFragment.java:151 (defaultTrackersList.setOnBindEditTextListener(...)); EditTextPreference dialog-binding dispatch unprinted. Descriptor (EditText)V matches. |
| 14 | BehaviorSettingsFragment.lambda$subscribeAlertDialog$1 | `(Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog$Event;)V` | REACHABLE | INFERRED | Rx subscribe lambda in subscribeAlertDialog (BehaviorSettingsFragment.java:178-184): on a NEGATIVE_BUTTON_CLICKED event for TAG_CUSTOM_BATTERY_DIALOG it calls row 12. Rx event dispatch is library code, unprinted. Descriptor (BaseAlertDialog$Event)V matches. |
| 15 | BehaviorSettingsFragment.newInstance | `()Lorg/proninyaroslav/libretorrent/ui/settings/sections/BehaviorSettingsFragment;` | REACHABLE | SOURCE | Called by SettingsFragment.java:150 (large-screen) and :153 (small-screen startActivity), and by PreferenceActivity.java:100. Def BehaviorSettingsFragment.java:53-59. |
| 16 | BehaviorSettingsFragment.onCreate | `(Landroid/os/Bundle;)V` | REACHABLE | INFERRED | Def BehaviorSettingsFragment.java:63-157; fragment lifecycle after newInstance; loads repo and dialog ViewModel, finds and binds all behaviour preferences, registers row 13. |
| 17 | BehaviorSettingsFragment.onCreatePreferences | `(Landroid/os/Bundle;Ljava/lang/String;)V` | REACHABLE | INFERRED | Def BehaviorSettingsFragment.java:188-191; framework calls it; it loads R.xml.pref_behavior (freshly printed: keys match the onCreate findPreference calls). |
| 18 | BehaviorSettingsFragment.onPreferenceChange | `(Landroidx/preference/Preference;Ljava/lang/Object;)Z` | REACHABLE | INFERRED | Registered via row 10; framework dispatch; body :199-245 handles autostart/charging/battery/custom-battery/roaming/keep-alive/trackers keys and calls rows 11, 12, 21. |
| 19 | BehaviorSettingsFragment.onStart | `()V` | REACHABLE | INFERRED | Def BehaviorSettingsFragment.java:168-173; fragment lifecycle; it calls subscribeAlertDialog (row 22) at :172. |
| 20 | BehaviorSettingsFragment.onStop | `()V` | REACHABLE | INFERRED | Def BehaviorSettingsFragment.java:160-165; fragment lifecycle; it clears disposables. |
| 21 | BehaviorSettingsFragment.showCustomBatteryDialog | `()V` | REACHABLE | SOURCE | Called in onPreferenceChange custom-battery-control branch (BehaviorSettingsFragment.java:221); def :247-265 shows a BaseAlertDialog with tag TAG_CUSTOM_BATTERY_DIALOG (guarded by isAdded() and an existing-fragment check). |
| 22 | BehaviorSettingsFragment.subscribeAlertDialog | `()V` | REACHABLE | SOURCE | Called in onStart (BehaviorSettingsFragment.java:172); def :175-185 subscribes dialogViewModel.observeEvents() with row 14's lambda and adds the disposable. |
| 23 | FeedSettingsFragment.<clinit> | `()V` | REACHABLE | INFERRED | Non-constant TAG = FeedSettingsFragment.class.getSimpleName() (FeedSettingsFragment.java:38) plus first use via newInstance (row 26). Convention (ix) undecided; reverts to OPEN if the merger requires more. |
| 24 | FeedSettingsFragment.<init> | `()V` | REACHABLE | SOURCE | Implicit default ctor, called by newInstance (FeedSettingsFragment.java:44 new FeedSettingsFragment()). |
| 25 | FeedSettingsFragment.bindOnPreferenceChangeListener | `(Landroidx/preference/Preference;)V` | REACHABLE | SOURCE | Called in onCreate for every preference (FeedSettingsFragment.java:61, :71, :78, :85, :95, :102, :109); def :119-122 sets the fragment as change listener (setOnPreferenceChangeListener call at :121). |
| 26 | FeedSettingsFragment.newInstance | `()Lorg/proninyaroslav/libretorrent/ui/settings/sections/FeedSettingsFragment;` | REACHABLE | SOURCE | Called by SettingsFragment.java:195 (large-screen) and :198 (small-screen), and by PreferenceActivity.java:114. Def FeedSettingsFragment.java:42-48. |
| 27 | FeedSettingsFragment.onCreate | `(Landroid/os/Bundle;)V` | REACHABLE | INFERRED | Def FeedSettingsFragment.java:51-111; fragment lifecycle after newInstance; loads repo, finds auto-refresh/interval/unmetered/roaming/keep-time/start-torrents/remove-duplicates preferences and binds listeners. |
| 28 | FeedSettingsFragment.onCreatePreferences | `(Landroid/os/Bundle;Ljava/lang/String;)V` | REACHABLE | INFERRED | Def FeedSettingsFragment.java:114-117; framework calls it; it loads R.xml.pref_feed (freshly printed: keys match the onCreate findPreference calls). |
| 29 | FeedSettingsFragment.onPreferenceChange | `(Landroidx/preference/Preference;Ljava/lang/Object;)Z` | REACHABLE | INFERRED | Registered via row 25; framework dispatch; body :125-162 writes settings and, for auto-refresh/interval keys, calls Scheduler.runPeriodicalRefreshFeeds (:134, :142) / cancelPeriodicalRefreshFeeds (:136). (Proposal cited cancel at :137; fresh file has it at :136 -- label unaffected.) |
| 30 | LimitationsSettingsFragment.<clinit> | `()V` | REACHABLE | INFERRED | Non-constant TAG = LimitationsSettingsFragment.class.getSimpleName() (LimitationsSettingsFragment.java:40) plus first use via newInstance (row 31). Convention (ix) undecided; reverts to OPEN if the merger requires more. |
| 31 | LimitationsSettingsFragment.<init> | `()V` | REACHABLE | SOURCE | Implicit default ctor, called by newInstance (LimitationsSettingsFragment.java:46 new LimitationsSettingsFragment()). |
| 32 | LimitationsSettingsFragment.bindOnPreferenceChangeListener | `(Landroidx/preference/Preference;)V` | REACHABLE | SOURCE | Called in onCreate for every preference (LimitationsSettingsFragment.java:80, :91, :102, :109, :120, :131, :142, :153, :164); def :174-177 sets the fragment as change listener. |
| 33 | LimitationsSettingsFragment.lambda$onCreate$0 | `([Landroid/text/InputFilter;Landroid/widget/EditText;)V` | REACHABLE | INFERRED | EditText lambda for max download speed: editText.setFilters(speedFilter), registered at LimitationsSettingsFragment.java:77; dialog-binding dispatch unprinted. speedFilter = InputFilterRange.UNSIGNED_INT (:59). Descriptor (EditText)V matches; numbering source-order, NOT bytecode-verified. |
| 34 | LimitationsSettingsFragment.lambda$onCreate$1 | `([Landroid/text/InputFilter;Landroid/widget/EditText;)V` | REACHABLE | INFERRED | EditText lambda for max upload speed: same speedFilter, registered at :88. Same caveats as row 33. |
| 35 | LimitationsSettingsFragment.lambda$onCreate$2 | `([Landroid/text/InputFilter;Landroid/widget/EditText;)V` | REACHABLE | INFERRED | EditText lambda for max connections: editText.setFilters(maxFilter), registered at :99; maxFilter built at :66-70 (max = Integer.MAX_VALUE). Same caveats as row 33. |
| 36 | LimitationsSettingsFragment.lambda$onCreate$3 | `([Landroid/text/InputFilter;Landroid/widget/EditText;)V` | REACHABLE | INFERRED | EditText lambda for max active uploads: editText.setFilters(queueingFilter), registered at :117; queueingFilter built at :60-65 (min -1, max Integer.MAX_VALUE). Same caveats as row 33. |
| 37 | LimitationsSettingsFragment.lambda$onCreate$4 | `([Landroid/text/InputFilter;Landroid/widget/EditText;)V` | REACHABLE | INFERRED | EditText lambda for max active downloads: same queueingFilter, registered at :128. Same caveats as row 33. |
| 38 | LimitationsSettingsFragment.lambda$onCreate$5 | `([Landroid/text/InputFilter;Landroid/widget/EditText;)V` | REACHABLE | INFERRED | EditText lambda for max active torrents: same queueingFilter, registered at :139. Same caveats as row 33. |
| 39 | LimitationsSettingsFragment.lambda$onCreate$6 | `([Landroid/text/InputFilter;Landroid/widget/EditText;)V` | REACHABLE | INFERRED | EditText lambda for max connections per torrent: editText.setFilters(maxFilter), registered at :150. Same caveats as row 33. |
| 40 | LimitationsSettingsFragment.lambda$onCreate$7 | `([Landroid/text/InputFilter;Landroid/widget/EditText;)V` | REACHABLE | INFERRED | EditText lambda for max uploads per torrent: editText.setFilters(queueingFilter), registered at :161. Same caveats as row 33. |

## Caveats the merger must see (recorded, NOT decided)

1. **Strict-entry:** the entry chain is now printed from SettingsActivity.onCreate through the settings layouts to SettingsFragment and on to every section fragment (see R-SETTINGS). What was NOT freshly printed in *this* pass is launcher → MainActivity and MainActivity settings-menu → SettingsActivity (printed in sibling batches 109–110 and 114, not fresh here). Under a rule requiring every step freshly printed in this pass, all REACHABLE rows revert to OPEN; under the trunk convention used by sibling batches, all stand.
2. **confirmed_by:** per-row convention (see above). Under a whole-route INFERRED convention, SOURCE rows crossing unprinted Rx/ActivityResult/framework dispatch would read INFERRED; labels unaffected.
3. **Preference-inflation ctor (convention (xi) family):** AndroidX dispatch itself was NOT printed (no fw_src/AndroidX print in this pass), so the 2-arg ctor rows are INFERRED. But they are robust under either inflation hypothesis: each class's 1-arg ctor delegates to its 2-arg ctor (SummaryPreference :39–42, SwitchBarPreference :40–43, TimePreference :32–36), so the 2-arg ctor runs whether inflation calls the 1-arg or the 2-arg ctor, and the 3-/4-arg ctors follow by printed delegation. This is the mirror of batch 11 rows 2–4, where the 1-arg ctors stay OPEN precisely because inflation may use the 2-arg ctor instead — do not flip batch 11 on this file's reasoning without re-reading batch 11.
4. **<clinit> on first use (convention (ix)):** rows resting on non-constant `TAG = ...getSimpleName()` plus a printed first use (batch 115 row 29; batch 116 rows 8, 23, 30) are INFERRED and revert to OPEN if the merger requires more than first-use evidence.
5. **Lambda/anonymous numbering:** source-order / enclosing-method mapping only, NOT bytecode-verified (batch 115 rows 39–40; batch 116 rows 1, 13, 14, 33–40). Labels do not depend on it except for the descriptor match noted per row (e.g. batch 115 row 40's descriptor includes the captured SettingsRepository, matching the initLegacy lambda).
6. **API-27 gate (batch 115 rows 38–40):** these are call-site-gated, not body-early-return: the only call site of initLegacyNotifySettings never runs at API 27, and both lambdas' only triggers sit inside it. Under the method-vs-branch rule they are closed_by_api_level candidates. Contrast batch 44–46, where the same Appearance/TorrentNotifier gates were used for ledIndicator getters — consistent treatment, but the merger must apply one rule to all of them. The onPreferenceChange legacy branches (Appearance :240–250) are likewise listener-less at API 27, but onPreferenceChange itself is reachable via the bound preferences, so that row stays REACHABLE.
7. **SummaryPreference.setSummary rows (batch 115 rows 7–8) stay OPEN** on a printed-corpus check only: no caller in any freshly fetched file, and the override dereferences summaryView (null until onBindViewHolder), which argues the XML summary attribute is not routed through the override. A saved full-repo grep is still owed before any flip to UNREACHABLE; a grep hit flips them to REACHABLE.

## Still owed before merge

- Saved full-repo grep for batch 115 rows 7–8 (setSummary) before any flip to UNREACHABLE.
- Fresh prints of launcher → MainActivity and MainActivity settings-menu → SettingsActivity, if the merger requires every entry step freshly printed in this pass (sibling-batch prints exist but are not fresh here).
- Bytecode confirmation of lambda numbering, if the merger requires it.
- Main-agent spot-check (1 in 5), `py_compile`, build, sampler, Mac build/C1 — all not run, never claimed passed.
- No push was made; pushes are held until verified and merged to [L].

Scope kept exactly: batch 116 only, LibreTorrent labels only, branch `work-2026-10-31` only, no device replay, no Aegis.
