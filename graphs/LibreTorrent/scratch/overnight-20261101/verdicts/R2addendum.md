# Coordinator addendum — 115/7, 115/8 (supersedes R2's OPEN hold)

R2 held both rows OPEN because the pinned androidx Preference print could not be
obtained. The coordinator has now obtained the print below. This addendum decides
both rows as Muse's own decision (never Yang's), for user/Yang review.

## Pinned version (from the branch, not guessed)

`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/build.gradle`
(branch work-2026-10-31, connector fetch, blob SHA 0c0170bc88e129a6bdf1bc01a96c9a5215a99a09):
`implementation 'androidx.preference:preference:1.2.1'`.

## Print obtained (version caveat stated, not hidden)

`androidx/androidx`, ref `androidx-main`, path
`preference/preference/src/main/java/androidx/preference/Preference.java`,
connector fetch, blob SHA fe0222a17ffef41bb3037b57b1c4fce9952a5421
(2,260 lines, saved locally as /tmp/Preference_main.java during the session).
The 1.2.1 tag could NOT be resolved through the connector
(`androidx.preference:preference:1.2.1` and `androidx-preference-1.2.1` both
failed ref resolution — recorded, not retried in a loop). The print below is
therefore androidx-main, NOT pinned 1.2.1. Revert condition: if a pinned 1.2.1
print shows the constructor dispatching virtually to setSummary, both rows
revert to OPEN (and to REACHABLE only if the inflation path is then confirmed).

## What the print shows

- Constructor (4-arg, lines 203+): `mSummary = TypedArrayUtils.getText(a,
  R.styleable.Preference_summary, R.styleable.Preference_android_summary);`
  (line 219) — DIRECT field assignment. No setSummary call anywhere in the
  constructor. The same direct-assignment shape holds for title (mTitle, line
  216-217) and every other attribute read there.
- `setSummary(CharSequence)` (lines 750-758): assigns mSummary + notifyChanged.
  `setSummary(int)` (lines 770-772): calls `setSummary(mContext.getString(...))`.
  No base-class code calls either overload: the only setSummary call sites in
  the whole file are the int→CharSequence delegation at :771. (Grep for
  `setSummary(` over the file: definitions :750/:770, call :771, javadoc refs.)
- Bind path uses `getSummary()` (lines 510, 1976), never setSummary.
  SummaryPreference overrides setSummary only — it does NOT override
  getSummary — so binding never touches the overrides either.
- Corroboration (different class, not the basis): framework
  `android.preference.Preference` (API 27 fw_src, fetched by R2) also assigns
  the XML summary directly to its field in the constructor.

## Combined with R2's saved grep

R2's full-corpus grep: 53 setSummary lines, ZERO on a SummaryPreference-typed
receiver; the class is referenced nowhere outside its own file; the only
SummaryPreference XML declaration is pref_anonymous_mode.xml:8-9 (summary
attribute, no key). The XML `android:summary` attribute therefore reaches the
object only through the constructor's direct assignment — never through the
override. The summaryView-null observation is consistent: inflation cannot
crash on null summaryView precisely because construction never dispatches to
the override.

## Verdicts (coordinator decision D35)

- 115/7 SummaryPreference.setSummary(int) — OPEN → UNREACHABLE
  no_trigger_in_app INFERRED. Reason: zero callers in the saved full-corpus
  grep; XML summary handled by base-constructor direct assignment (print
  above); no SummaryProvider set on any SummaryPreference (zero references
  outside its own file).
- 115/8 SummaryPreference.setSummary(CharSequence) — OPEN → UNREACHABLE
  no_trigger_in_app INFERRED. Same reason. (The int overload's delegation
  to this overload is irrelevant: the int overload itself is never called.)

Neither row flips on the framework print alone; the androidx-main print is the
basis, with the 1.2.1 revert condition above.
