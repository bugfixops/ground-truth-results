# R2 summary — LibreTorrent 115/7 and 115/8 (Stream A Phase 3 completion)

## Verdicts (one line each, detail in the per-row files)

- **115/7 SummaryPreference.setSummary(int) — OPEN (held).**
- **115/8 SummaryPreference.setSummary(CharSequence) — OPEN (held).**

Both rows verified against `~/workspace/overnight/stream-A/phase3/work/batch115-merge-ready.md`
(rows 7–8, both OPEN on entry); no work file under `phase3/work/` was edited, no push, no
branch edit, no token used, no tick marker written. All verdict files are under
`~/workspace/overnight/stream-A/phase3/verdicts/R2/`.

## What was actually printed (not guessed)

1. **Row identities and definitions** — from the batch file and the corpus copy of
   `SummaryPreference.java` (`corpus/java/ui/settings/customprefs/SummaryPreference.java`):
   `setSummary(CharSequence)` :79-85, `setSummary(int)` :87-92; both dereference
   `summaryView`, assigned only in `onBindViewHolder` (:69), hence null until bind.
2. **Saved grep over the complete local corpus** (commands + full output in `grep_full.txt`):
   - `grep -rn "setSummary" java/` (281 app Java files): 53 lines, zero on a
     `SummaryPreference`-typed receiver. All non-definition hits are on other receiver types;
     the look-alikes `AppearanceSettingsFragment:141/:209` (`notifySound`, plain `Preference`)
     and `NetworkSettingsFragment:245/:411` (`anonymousMode`, plain `<Preference>` in
     `pref_network.xml:10-14`) are confirmed not this class.
   - `grep -rn "SummaryPreference" java/`: referenced nowhere outside its own file.
   - Layout XML (`corpus/res-layout/`, 73 files): zero `SummaryPreference` /
     `android:summary` hits.
   - Saved pref-XML copies (`~/workspace/b115116-src/pref_*.xml`): the ONLY
     `SummaryPreference` declaration is `pref_anonymous_mode.xml:8-9`, with
     `android:summary="@string/pref_anonymous_mode_summary"` and no key. Corpus caveat: the
     corpus holds layout XML only, no `res/xml/` — the pref-XML half of the grep is over the
     saved `b115116-src` copies, and library/framework code is in neither tree, so this is
     NOT a full-repo grep and is not claimed as one.
3. **androidx source search — failed to obtain the named print.** Six-plus web searches for
   `androidx.preference.Preference` source returned API reference pages only (log in
   `searches_androidx.txt`); no androidx source URL was returned and none was guessed. The
   pinned androidx preference version for LibreTorrent 3.5.2 is also not established locally
   (no `build.gradle` in the corpus or `b115116-src/`).
4. **Adjacent print, NOT used as the verdict basis.** The framework
   `android.preference.Preference` constructor was fetched in full (verbatim search-result URL
   https://www.javatips.net/api/android-imf-ext-master/android-ws/frameworks/base/core/java/android/preference/Preference.java;
   excerpt in `framework_api27_preference_excerpt.txt`, independently present as API-27
   `fw_src` in stream-D). It assigns the XML summary directly to its field
   (`mSummary = a.getString(attr)` / `mSummary = a.getText(attr)`) with NO `setSummary` call
   in the constructor, and its `setSummary(int)` delegates to `setSummary(CharSequence)`.
   That is the direct-field-assignment pattern — but for `android.preference`, a different
   class from the `androidx.preference.Preference` that `SummaryPreference` extends. Per the
   task rule, it does not flip either row, and API docs were not used either.

## Reasoning, including the summaryView-null observation

- The null observation cuts as follows, from the print rather than assumption: in the
  framework print, construction never touches the subclass view field, so inflation does not
  crash — consistent with direct assignment, but only for the framework class. If the
  androidx constructor DID dispatch virtually to either override, inflating
  `pref_anonymous_mode.xml` would dereference null `summaryView` before any bind and crash
  the anonymous-mode screen. That tension is why the androidx print matters and why it must
  not be guessed: the null observation supports direct assignment only if the androidx
  constructor matches the framework one, which is unprinted.
- The two overloads were judged separately: 115/7 needs an int-shaped caller/dispatch,
  115/8 needs a CharSequence-shaped caller or a virtual dispatch from construction. The single
  XML `android:summary` attribute is CharSequence-shaped, so it is a candidate dispatch for
  115/8 only — but a candidate is not a printed dispatch, and no caller exists for either.
  A resolver-side note (not a verdict driver): IF a future androidx print shows the base
  `setSummary(int)` delegating virtually to `setSummary(CharSequence)`, then any future
  direct int caller on a `SummaryPreference` receiver would also trigger 115/8.

## Exact missing print (the one item that would close both rows)

The `androidx.preference.Preference` base-class constructor source at the androidx preference
version pinned by LibreTorrent 3.5.2, showing whether the XML `android:summary` attribute is
assigned directly to the base field or dispatched via a virtual `setSummary` call — plus, if
the constructor alone is ambiguous, the androidx `PreferenceInflater` inflation path for
XML-declared preferences. Suggested next route (not attempted here, needs parent/eligible
delegation if it involves a live browser or repo access beyond this task): obtain the
pinned version from the app's `build.gradle` (not in the local corpus) and fetch the matching
androidx source (e.g. via the AndroidX repository / a source mirror) — the web search tool
here surfaced no such URL to fetch.

## Files written (verdicts/R2/ only)

- `115_7.md` — 115/7 verdict + reasoning.
- `115_8.md` — 115/8 verdict + reasoning (judged separately).
- `R2_SUMMARY.md` — this file.
- `grep_full.txt` — saved grep commands + full output (app Java, SummaryPreference refs,
  layout XML, saved pref XML).
- `grep_setSummary_appjava.txt`, `grep_SummaryPreference_refs.txt` — the two main greps.
- `grep_android_summary_res.txt`, `grep_pref_decls_res.txt` — empty (corpus has no `res/xml/`;
  pref-XML results are in `grep_full.txt`).
- `searches_androidx.txt` — androidx source search log.
- `framework_api27_preference_excerpt.txt` — framework (non-androidx) constructor/setSummary
  excerpt, labelled as adjacent evidence only.
