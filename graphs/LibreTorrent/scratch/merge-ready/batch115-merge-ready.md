## Revision 2026-11-01 — OPEN-closing round 2, group G16 (UNVERIFIED, 0 flips)

0 of 2 OPEN rows closed in this pass; counts unchanged (35 REACHABLE / 3 UNREACHABLE / 2 OPEN).
New evidence this pass: fresh greps over the already-fetched 252-file app Java tree
(~/workspace/ruleF-src), saved in ~/workspace/b103106112114115-openclose2-src/grep_rest.txt and grep_extra.txt, plus the
already-fetched pref xmls (~/workspace/b115116-src/pref_*.xml). No GitHub connector fetch was
needed; no fresh 429. Generated code, AndroidX Preference internals and res/layout are NOT in
that tree, so it is NOT a full-repo grep.
- Rows 7-8 SummaryPreference.setSummary(int)/(CharSequence): SummaryPreference is referenced
  tree-wide ONLY in its own file; every setSummary hit in the tree is on another receiver type
  (typed Preference/EditTextPreference/ListPreference variables, or generic Preference
  parameters — e.g. AppearanceSettingsFragment notifySound is a Preference at :141/:209,
  NetworkSettingsFragment anonymousMode is a Preference at :245/:411). AnonymousModeSettingsFragment
  retrieves only the SwitchBarPreference via findPreference (key pref_key_anonymous_mode); the
  SummaryPreference XML entry has NO key (pref_anonymous_mode.xml:8-9, same in the b111213 copy),
  so no app code can findPreference it, and no settings code iterates the preference screen
  (getPreferenceScreen hits in ui/settings are nil apart from DialogPreference getPreference()
  in TimePreferenceDialogFragmentCompat). onBindViewHolder uses getSummary (SummaryPreference
  :75), not setSummary; the overrides dereference summaryView, null until bind (:79-92), so
  inflation cannot be routing through the override — an argument, not a printed call site.
NOT flipped to UNREACHABLE: no saved full-repo grep exists (AndroidX Preference internals
unprinted); a 252-tree zero alone never flips. Named targets unchanged: a printed setSummary
call on a SummaryPreference instance, or a saved full-repo grep.
Coupled group 115/38-39-40 (DECIDE TOGETHER, NEVER SEPARATELY — no separate flip made):
re-verified against the ruleF-src copy of AppearanceSettingsFragment.java: the API-27 gate is
:118-119 (if SDK_INT < O, initLegacyNotifySettings(pref)); row 39's only trigger is
ringtonePicker.launch(intent) at :164, inside initLegacyNotifySettings; row 40's lambda is
registered only inside initLegacyNotifySettings (:144-167 notifySound click listener); tree-wide
ringtonePicker hits are only :164 and the field at :198-217 (the result callback for that
launch). Rows 38, 39 and 40 therefore stand or fall together under the API-27 gate decision;
all three stay UNREACHABLE closed_by_api_level in this file. Lambda numbering for rows 39-40
remains source-order only, NOT bytecode-verified.
NOT done here, per task: batch 11's 1-arg ctors were NOT flipped on this file's 2-arg
delegation reasoning (SummaryPreference :39-42 -> :47); batch 11 is outside G16 and was not
re-read. Strict-entry note (unchanged): the FeedSettingsFragment opening step is printed
(SettingsFragment.java:122, :195-198; PreferenceActivity.java:113-114), which drops the
strict-entry caveat FOR THAT STEP ONLY; launcher -> MainActivity and MainActivity
settings-menu -> SettingsActivity remain sibling-batch prints (109-110, 114), not fresh in 115,
so the caveat is NOT dropped globally. Build: not run. C1: not run.

**CORRECTION 2026-11-01 (FeedSettingsFragment entry): the step that opens FeedSettingsFragment is now freshly printed — SettingsFragment.java:122 (feed preference registered), :131-134 (click listener -> openPreference), :195-196 (large-screen setFragment(FeedSettingsFragment.newInstance())), :198-199 (small-screen startActivity(FeedSettingsFragment.class)), and PreferenceActivity.java:113-114 (getFragment dispatch returns FeedSettingsFragment.newInstance()). Source saved in ~/workspace/b_feedsettings_src/. The "strict entry rule" caveat is therefore DROPPED for the FeedSettingsFragment opening step only; it is not dropped globally for other steps, and no label in this file changes on this print alone.**


## Revision 2026-11-01 — OPEN-closing pass (UNVERIFIED, no label changes)

0 of 2 OPEN rows closed in this pass; counts unchanged (35 REACHABLE / 3 UNREACHABLE / 2 OPEN).
New evidence, freshly connector-fetched from branch work-2026-10-31 (one file at a time, ~25 s pauses, no fresh HTTP 429),
saved in ~/workspace/b103106112115-openclose-src/: SummaryPreference.java (93 lines), LogSettingsFragment.java (101).
Plus the saved full app Java tree grep (252 files, ~/workspace/b103106112115-openclose-src/grep_app_java_tree.txt;
res/layout, res/xml, generated code and library/framework code NOT in it, so explicitly NOT a full-repo grep):
every setSummary hit in the tree is on another receiver type (Appearance/Behavior/Limitations/Network/Proxy/Storage/
Streaming fragments' EditTextPreference/ListPreference/Preference variables, LogSettingsFragment's EditTextPreference
maxLogSize at :71 and generic Preference at :96) — NONE is on a SummaryPreference instance, and no file in the tree
declares a SummaryPreference variable or calls setSummary on one. The two LogSettingsFragment setSummary hits are
specifically NOT this row: maxLogSize is an EditTextPreference (LogSettingsFragment.java:69), not a SummaryPreference.
Rows 7-8 (SummaryPreference.setSummary(int) / (CharSequence)) therefore stay OPEN; the summaryView-null-until-bind
argument is still NOT used as a flip reason, per the task note (the XML android:summary attribute may be handled
by the Preference base class, but that is an argument about inflation, not a printed call site).
Named targets unchanged: a printed setSummary call on a SummaryPreference instance, or a saved full-repo grep
(res pref XML databinding/inflation dispatch and AndroidX Preference internals still unsearched).
Build: not run. C1: not run.

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 115 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another helper's file.**
**Build: not run. C1: not run.** Build and C1 run on the user's Mac after a push, so they are marked "not run" here, never passed. No sampler, full-repo grep, or `py_compile` was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 115 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, from printed source. The prior batch-115 proposal (`~/workspace/libretorrent-batch115-proposal.md`) was used as an INPUT, not a result; every row below was re-judged against freshly printed source in this pass.

## Membership — verified, not guessed

Exactly the 40 rows for batch 115 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the local plan copy `~/workspace/agent27-plan.tsv` (4,733 lines incl. header; plan blob SHA `0104806dd666c840049b3db52823d4b384fa1c92`). All 40 rows are `TODO_CANDIDATE_REACHABLE` in the plan (candidates, not evidence), in plan order. This file was generated from the plan rows, so names and JVM descriptors cannot drift; the verification section below re-checks them mechanically.

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

- REACHABLE proposed: 35 / 40 (SOURCE 17, INFERRED 18)
- UNREACHABLE proposed: 3
- OPEN: 2 / 40
- Verified for merge: 0

## Per-method table (all 40 rows, in plan order)

| # | Method (plan) | JVM descriptor | Proposed label | confirmed_by | Route / printed citations |
|---|---|---|---|---|---|
| 1 | SettingsFragment.startActivity | `(Ljava/lang/Class;Ljava/lang/String;)V` | REACHABLE | SOURCE | SettingsFragment.java:232-241 def (builds PreferenceActivity intent, startActivity(i) :240); called from openPreference small-screen branches :144 (Appearance), :153 (Behavior), :162 (Network), :171 (Storage), :180 (Limitations), :189 (Scheduling), :198 (Feed), :207 (Streaming). |
| 2 | SettingsViewModel.<init> | `()V` | REACHABLE | INFERRED | Implicit default ctor (SettingsViewModel.java:25, no explicit ctor; field detailTitleChanged). Framework instantiates via ViewModelProvider: SettingsFragment.java:88 new ViewModelProvider(activity).get(SettingsViewModel.class); SettingsActivity.java:47 new ViewModelProvider(this).get(SettingsViewModel.class). |
| 3 | SummaryPreference.<init>(Context,AttributeSet) | `(Landroid/content/Context;Landroid/util/AttributeSet;)V` | REACHABLE | INFERRED | Framework preference inflation (AndroidX dispatch unprinted, not from fw_src). Anchored by printed XML use in a loaded screen: pref_anonymous_mode.xml:8-9 declares org...customprefs.SummaryPreference; AnonymousModeSettingsFragment.java:67 onCreatePreferences loads R.xml.pref_anonymous_mode. Robust under either inflation-ctor hypothesis: the 1-arg ctor (SummaryPreference.java:39-42) delegates to this 2-arg ctor, so this ctor runs whether inflation calls the 1-arg or the 2-arg ctor. Def :44-48. |
| 4 | SummaryPreference.<init>(Context,AttributeSet,int) | `(Landroid/content/Context;Landroid/util/AttributeSet;I)V` | REACHABLE | SOURCE | Called by the 2-arg ctor, SummaryPreference.java:47 this(context, attrs, R.attr.preferenceStyle). Def :50-54. |
| 5 | SummaryPreference.<init>(Context,AttributeSet,int,int) | `(Landroid/content/Context;Landroid/util/AttributeSet;II)V` | REACHABLE | SOURCE | Called by the 3-arg ctor, SummaryPreference.java:52 this(context, attrs, defStyleAttr, defStyleAttr). Def :55-62. |
| 6 | SummaryPreference.onBindViewHolder | `(Landroidx/preference/PreferenceViewHolder;)V` | REACHABLE | INFERRED | Def SummaryPreference.java:65-76. Framework binds the row when the anonymous-mode screen is shown (same screen as row 3: pref_anonymous_mode.xml declares the class, AnonymousModeSettingsFragment loads it :67). Framework bind dispatch unprinted. |
| 7 | SummaryPreference.setSummary(int) | `(I)V` | OPEN | — | Def SummaryPreference.java:87-92. No printed caller in any freshly fetched file. XML android:summary is handled by the Preference base class (field assignment during construction), not via this override -- and the override dereferences summaryView (:91), which is null until onBindViewHolder, so inflation cannot be calling it. Named grep target; NOT UNREACHABLE without a saved full-repo grep. |
| 8 | SummaryPreference.setSummary(CharSequence) | `(Ljava/lang/CharSequence;)V` | OPEN | — | Def SummaryPreference.java:79-85. No printed caller in any freshly fetched file. Same reasoning as row 7 (override dereferences summaryView :83, null until bind; XML summary attribute does not call the override). Named grep target; NOT UNREACHABLE without a saved full-repo grep. |
| 9 | SwitchBarPreference.<init>(Context,AttributeSet) | `(Landroid/content/Context;Landroid/util/AttributeSet;)V` | REACHABLE | INFERRED | Framework preference inflation (dispatch unprinted). Anchored by printed XML use AND a printed app-code use: pref_anonymous_mode.xml:3-6 declares SwitchBarPreference with key pref_key_anonymous_mode; AnonymousModeSettingsFragment.java:57 findPreference(keyAnonymousMode) cast to SwitchBarPreference, :59 setChecked, :60 bindOnPreferenceChangeListener. Def :45-49. Same inflation-ctor robustness as row 3 (1-arg ctor :40-43 delegates to this ctor). |
| 10 | SwitchBarPreference.<init>(Context,AttributeSet,int) | `(Landroid/content/Context;Landroid/util/AttributeSet;I)V` | REACHABLE | SOURCE | Called by the 2-arg ctor, SwitchBarPreference.java:48 this(context, attrs, R.attr.preferenceStyle). Def :51-55. |
| 11 | SwitchBarPreference.<init>(Context,AttributeSet,int,int) | `(Landroid/content/Context;Landroid/util/AttributeSet;II)V` | REACHABLE | SOURCE | Called by the 3-arg ctor, SwitchBarPreference.java:53 this(context, attrs, defStyleAttr, defStyleAttr). Def :56-61. |
| 12 | SwitchBarPreference.onBindViewHolder | `(Landroidx/preference/PreferenceViewHolder;)V` | REACHABLE | INFERRED | Def SwitchBarPreference.java:64-72; registers the checked-change listener at :70. Framework binds the row when the anonymous-mode screen is shown (row 9 anchor). Framework bind dispatch unprinted. |
| 13 | SwitchBarPreference$1.<init> | `(Lorg/proninyaroslav/libretorrent/ui/settings/customprefs/SwitchBarPreference;)V` | REACHABLE | INFERRED | Anonymous OnCheckedChangeListener field instance, SwitchBarPreference.java:74; created with the enclosing preference instance (row 9 anchor). Only anonymous class in the file; numbering not bytecode-verified but no other candidate exists. |
| 14 | SwitchBarPreference$1.onCheckedChanged | `(Landroid/widget/CompoundButton;Z)V` | REACHABLE | INFERRED | Registered at SwitchBarPreference.java:70 switchButton.setOnCheckedChangeListener(listener); widget dispatch unprinted. Body :76-88 calls callChangeListener / setChecked. |
| 15 | TimePreference.<init>(Context,AttributeSet) | `(Landroid/content/Context;Landroid/util/AttributeSet;)V` | REACHABLE | INFERRED | Framework preference inflation (dispatch unprinted). Anchored by printed XML use in a loaded screen AND printed app-code use: pref_scheduling.xml declares TimePreference twice (start-time and shutdown-time entries); SchedulingSettingsFragment.java:166 onCreatePreferences loads R.xml.pref_scheduling; :84/:91 findPreference casts to TimePreference. Same inflation-ctor robustness as row 3 (1-arg ctor TimePreference.java:32-36 delegates to this ctor). Def :38-43. |
| 16 | TimePreference.<init>(Context,AttributeSet,int) | `(Landroid/content/Context;Landroid/util/AttributeSet;I)V` | REACHABLE | SOURCE | Called by the 2-arg ctor, TimePreference.java:41-42 this(context, attrs, R.attr.preferenceStyle). Def :45-50. |
| 17 | TimePreference.<init>(Context,AttributeSet,int,int) | `(Landroid/content/Context;Landroid/util/AttributeSet;II)V` | REACHABLE | SOURCE | Called by the 3-arg ctor, TimePreference.java:48 this(context, attrs, defStyleAttr, defStyleAttr). Def :51-62. |
| 18 | TimePreference.formatTime | `()Ljava/lang/String;` | REACHABLE | SOURCE | Called by getSummary, TimePreference.java:120 return prefix + formatTime(). Def :123-125. |
| 19 | TimePreference.getDialogLayoutResource | `()I` | REACHABLE | INFERRED | Def TimePreference.java:99-102. The dialog machinery reads it when the dialog is built; the dialog display step is now printed (SchedulingSettingsFragment.java:175-184, see row 26), but the framework read itself is unprinted. |
| 20 | TimePreference.getSummary | `()Ljava/lang/CharSequence;` | REACHABLE | INFERRED | Def TimePreference.java:116-121; framework calls it to display the preference summary (it prefixes super.getSummary() and appends formatTime() :120). Framework summary dispatch unprinted. |
| 21 | TimePreference.getTime | `()I` | REACHABLE | SOURCE | Called by TimePreferenceDialogFragmentCompat.java:59 ((TimePreference) preference).getTime() in onBindDialogView. Def TimePreference.java:65-68. |
| 22 | TimePreference.onGetDefaultValue | `(Landroid/content/res/TypedArray;I)Ljava/lang/Object;` | REACHABLE | INFERRED | Def TimePreference.java:88-95; framework calls it while inflating the preference's default value (screen now printed: pref_scheduling.xml + SchedulingSettingsFragment :166). Framework inflation callback unprinted. |
| 23 | TimePreference.onSetInitialValue | `(ZLjava/lang/Object;)V` | REACHABLE | INFERRED | Def TimePreference.java:108-114; framework calls it on inflation; it calls setTime at :111. Framework inflation callback unprinted. |
| 24 | TimePreference.setTime | `(I)V` | REACHABLE | SOURCE | Called by SchedulingSettingsFragment.java:86 (startTime.setTime) and :93 (stopTime.setTime), by onSetInitialValue (TimePreference.java:111), and by TimePreferenceDialogFragmentCompat.java:99 (onDialogClosed). Def :75-84. |
| 25 | TimePreferenceDialogFragmentCompat.<init> | `()V` | REACHABLE | SOURCE | Implicit default ctor, called by newInstance (TimePreferenceDialogFragmentCompat.java:35 new TimePreferenceDialogFragmentCompat()). |
| 26 | TimePreferenceDialogFragmentCompat.newInstance | `(Ljava/lang/String;)Lorg/proninyaroslav/libretorrent/ui/settings/customprefs/TimePreferenceDialogFragmentCompat;` | REACHABLE | SOURCE | Printed caller closes the proposal caveat: SchedulingSettingsFragment.java:179 dialogFragment = TimePreferenceDialogFragmentCompat.newInstance(preference.getKey()) inside onDisplayPreferenceDialog (:175-188), shown at :183-184. Def :32-41. |
| 27 | TimePreferenceDialogFragmentCompat.onBindDialogView | `(Landroid/view/View;)V` | REACHABLE | INFERRED | Def TimePreferenceDialogFragmentCompat.java:44-72; framework dialog lifecycle after the printed show() (SchedulingSettingsFragment.java:183-184). Lifecycle dispatch unprinted; it reads the TimePicker and calls getTime (:59). |
| 28 | TimePreferenceDialogFragmentCompat.onDialogClosed | `(Z)V` | REACHABLE | INFERRED | Def TimePreferenceDialogFragmentCompat.java:80-103; framework calls it on dialog close; on positive result it calls callChangeListener and setTime (:97-99). Lifecycle dispatch unprinted. |
| 29 | AnonymousModeSettingsFragment.<clinit> | `()V` | REACHABLE | INFERRED | Non-constant TAG = AnonymousModeSettingsFragment.class.getSimpleName() (AnonymousModeSettingsFragment.java:36) plus first use via newInstance (row 32). <clinit>-on-first-use convention (ix) is UNDECIDED project-wide; reverts to OPEN if the merger requires more than this. |
| 30 | AnonymousModeSettingsFragment.<init> | `()V` | REACHABLE | SOURCE | Implicit default ctor, called by newInstance (AnonymousModeSettingsFragment.java:42 new AnonymousModeSettingsFragment()). |
| 31 | AnonymousModeSettingsFragment.bindOnPreferenceChangeListener | `(Landroidx/preference/Preference;)V` | REACHABLE | SOURCE | Called in onCreate (AnonymousModeSettingsFragment.java:60); def :70-73 sets the fragment as change listener. |
| 32 | AnonymousModeSettingsFragment.newInstance | `()Lorg/proninyaroslav/libretorrent/ui/settings/sections/AnonymousModeSettingsFragment;` | REACHABLE | SOURCE | Called by NetworkSettingsFragment.java:248 (setFragment(AnonymousModeSettingsFragment.newInstance(), ...) in the large-screen branch of the anonymous-mode click listener) and by PreferenceActivity.java:109-110 (getFragment dispatch for the simple name, small-screen path). Def AnonymousModeSettingsFragment.java:40-47. |
| 33 | AnonymousModeSettingsFragment.onCreate | `(Landroid/os/Bundle;)V` | REACHABLE | INFERRED | Def AnonymousModeSettingsFragment.java:50-62; fragment lifecycle after newInstance (row 32); it loads the repo, finds the SwitchBarPreference, sets checked state and binds the listener. |
| 34 | AnonymousModeSettingsFragment.onCreatePreferences | `(Landroid/os/Bundle;Ljava/lang/String;)V` | REACHABLE | INFERRED | Def AnonymousModeSettingsFragment.java:65-68; framework calls it; it loads R.xml.pref_anonymous_mode. |
| 35 | AnonymousModeSettingsFragment.onPreferenceChange | `(Landroidx/preference/Preference;Ljava/lang/Object;)Z` | REACHABLE | INFERRED | Registered via row 31 (AnonymousModeSettingsFragment.java:70-73); framework dispatch on preference change; body :76-83 writes pref.anonymousMode((boolean)newValue). |
| 36 | AppearanceSettingsFragment.<init> | `()V` | REACHABLE | SOURCE | Implicit default ctor, called by newInstance (AppearanceSettingsFragment.java:59 new AppearanceSettingsFragment()). |
| 37 | AppearanceSettingsFragment.bindOnPreferenceChangeListener | `(Landroidx/preference/Preference;)V` | REACHABLE | SOURCE | Called in onCreate (AppearanceSettingsFragment.java:85, :92, :100, :108, :115) and in initLegacyNotifySettings (:134, :174, :181, :188 -- those calls are dead at API 27, but the onCreate calls suffice); def :219-222. |
| 38 | AppearanceSettingsFragment.initLegacyNotifySettings | `(Lorg/proninyaroslav/libretorrent/core/settings/SettingsRepository;)V` | UNREACHABLE closed_by_api_level | SOURCE | Only caller is onCreate under if (Build.VERSION.SDK_INT < Build.VERSION_CODES.O) (AppearanceSettingsFragment.java:118-119); at standard-config API 27 the guard is false (27 < 26 false), so the body (:128-190) never runs. This is a call-site-gated method (its only call site never runs at API 27), not a body-early-return case. Kind closed_by_api_level, per the method-vs-branch rule. |
| 39 | AppearanceSettingsFragment.lambda$initLegacyNotifySettings$0 | `(Lorg/proninyaroslav/libretorrent/core/settings/SettingsRepository;Landroidx/preference/Preference;)Z` | UNREACHABLE closed_by_api_level | SOURCE | Ringtone-picker result lambda, AppearanceSettingsFragment.java:200-217 (registered via registerForActivityResult field :198-217). Its only trigger is ringtonePicker.launch(intent) at :164, inside initLegacyNotifySettings (row 38), which is gated off at API 27. No other launch site in any freshly fetched file. Descriptor (ActivityResult)V matches the result callback. Lambda numbering is per-enclosing-field-init ($1), NOT bytecode-verified. |
| 40 | AppearanceSettingsFragment.lambda$new$1 | `(Landroidx/activity/result/ActivityResult;)V` | UNREACHABLE closed_by_api_level | SOURCE | Notify-sound click-listener lambda, registered only inside initLegacyNotifySettings (AppearanceSettingsFragment.java:144-167, notifySound.setOnPreferenceClickListener((preference) -> ... ringtonePicker.launch(intent) ...)). Same API 27 gate as row 38. Descriptor (SettingsRepository, Preference)Z matches the lambda capturing initLegacy's pref parameter plus the Preference argument. Lambda numbering NOT bytecode-verified. |

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
- Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]); pushed UNVERIFIED before [L] at user request 2026-11-01.

Scope kept exactly: batch 115 only, LibreTorrent labels only, branch `work-2026-10-31` only, no device replay, no Aegis.
