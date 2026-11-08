# R6E: Aegis 3.4.2 route check (2 routes)

Read-only check of G5_1.txt and G5_2.txt against the app source at
/Users/darshan/Desktop/yang/work/final_java_only/Aegis/app/Aegis-#v3.4.2/app/src/main/ and the build classes.
Framework lines are from work/fw_src/android-8.1.0_r1. No graph, tool or handoff file was edited.

## MainActivity.onIntroResult (steps: 22)

| step | edge | result | reason |
|---|---|---|---|
| 1 | Eb9515d18 | OK | AndroidManifest.xml:22 sets android:name=".AegisApplication" |
| 2 | E5b266140 | OK | AegisApplication extends Hilt_AegisApplication (build class); Hilt file is generated, so INFERRED |
| 3 | E1ef992ce | OK | Call to AegisApplicationBase.onCreate in the build class (line 43) |
| 4 | E88ed9829 | OK | AegisApplicationBase.java:45-67 |
| 5 | E28ffc58c | OK | AndroidManifest.xml:44-51 MAIN / LAUNCHER on MainActivity |
| 6 | Eb76444fd | OK | MainActivity.java:192-194 onCreate |
| 7 | E3a06baed | OK | MainActivity.java:938-940 onStart |
| 8 | E0602e719 | OK | isVaultInitNeeded (VaultManager.java:226-228) is true on a fresh install; :942-946 starts the intro |
| 9 | E4ce5043a | OK | startIntroActivity (:603-609); _isDoingIntro is false on a fresh start |
| 10 | E5e63fbe7 | OK | IntroActivity.java:35-41 onCreate |
| 11 | E93598a00 | OK | addSlide calls at IntroActivity.java:38-41 |
| 12 | E1440feb8 | OK | IntroBaseActivity.java:174-188; the first slide is Welcome |
| 13 | E6830b6dc | OK | goToNextSlide (IntroBaseActivity.java:80-93); the imported skip (IntroActivity.java:57-62) does not apply |
| 14 | E32450899 | OK | rb_none at fragment_security_picker_slide.xml:41; the radio check is INFERRED (RadioGroup not read) |
| 15 | E553f11f7 | OK | IntroBaseActivity.java:47 click listener |
| 16 | E251ac3f4 | OK | IntroBaseActivity.java:47 calls goToNextSlide |
| 17 | E7216511b | OK | setPagerPosition (:149-151) calls onBeforeSlideChanged |
| 18 | E8da5177a | OK | IntroActivity.java:50-55; cryptType NONE from step 14 skips to Done |
| 19 | E3f8e1ae8 | OK | skipToSlide (IntroBaseActivity.java:104) |
| 20 | E0182bb68 | OK | Done slide Next: goToNextSlide calls onDonePressed (:91) |
| 21 | E1dcf1457 | ERROR | The guard is "vault created". That state is produced by VaultManager.initNew at IntroActivity.java:100, and this route has no edge that calls it before step 21. The none path reaches :100 with creds null (checks at :92-96). |
| 22 | E5f44da38 | OK | MainActivity.java:142-148 launcher calls onIntroResult when RESULT_OK |

Verdict: ERROR 1, UNCLEAR 0, OK 21.

Fixes:
- Insert a CALL edge IntroActivity.onDonePressed -> VaultManager.initNew at IntroActivity.java:100 (guard: cryptType NONE and creds null, :92-96) after step 20 and before step 21.

## EntryAdapter.lambda$doesAnyGroupMatchSearchFilter$1 (steps: 15)

| step | edge | result | reason |
|---|---|---|---|
| 1 | Eb9515d18 | OK | AndroidManifest.xml:22 |
| 2 | E5b266140 | OK | Same as route 1 step 2 |
| 3 | E1ef992ce | OK | Same as route 1 step 3 |
| 4 | E88ed9829 | OK | AegisApplicationBase.java:45-67 |
| 5 | E28ffc58c | OK | AndroidManifest.xml:44-51 |
| 6 | Eb76444fd | OK | MainActivity.java:192-194 |
| 7 | E8e6d6f10 | OK | onCreateOptionsMenu (MainActivity.java:1011-1016); the androidx call is INFERRED |
| 8 | Ed60e6cbd | ERROR | Guard _submittedSearchQuery != null (MainActivity.java:1070). Its only producer is the search submit at :1039-1040. The value survives a recreate only through onSaveInstanceState (:419-420) and onCreate restore (:204-205). This run is a fresh launch with no submit and no restore edge, so the guard cannot hold. |
| 9 | Ececfe4d5 | OK | Direct call at EntryListView.java:279-284; the guard inherits from step 8 |
| 10 | Ef330c979 | OK | EntryAdapter.java:271-273; the new text differs from the null _searchFilter; inherits from step 8 |
| 11 | Ed33e097b | OK | refreshEntryList calls calculateShownEntries (EntryAdapter.java:280) |
| 12 | E21f79a09 | ERROR | Guard "entries list not empty" (EntryAdapter.java:301). The entries come from MainActivity.loadEntries (:1133-1142, via onIntroResult :752-754) or onAddEntryResult (:618-625). The route has neither, so the list is empty. |
| 13 | E9b4d2bef | OK | isEntryFiltered (EntryAdapter.java:200) requires _searchFilter, set in step 10; stream behaviour INFERRED |
| 14 | E399cebc2 | ERROR | Guard _searchBehaviorMask includes SEARCH_IN_GROUPS. The default mask is ISSUER or NAME (Preferences.java:198). The GROUPS bit comes only from BehaviorPreferencesFragment.java:57 via Preferences.setSearchBehaviorMask (:207-208), read at MainActivity.java:234 during onCreate. The route has no such write. |
| 15 | E4bf8b9e0 | OK | lambda$doesAnyGroupMatchSearchFilter$1 is the filter at EntryAdapter.java:227 (build class signature (Set,VaultGroup)Z); inherits from step 14 |

Verdict: ERROR 3 (steps 8, 12, 14), UNCLEAR 0, OK 12 (steps 1-7, 9, 10, 11, 13, 15).
Steps 9, 10, 11, 13 and 15 are correct in code. Their guards come from the ERROR producers and will pass once those are fixed.

Fixes:
- Step 8: insert the search submit (MainActivity.java:1039-1040, sets _submittedSearchQuery) before step 8, with a recreate and the restore at :204-205, or start the route from a prior run that saved the query.
- Step 12: insert a producer of a non-empty entry list before step 12, such as MainActivity.loadEntries (:1133-1142) or onAddEntryResult (:618-625, :622 setEntries).
- Step 14: add a prior-run producer that writes the GROUPS bit (BehaviorPreferencesFragment.java:57, Preferences.setSearchBehaviorMask :207-208) so MainActivity.java:234 reads it during onCreate before step 6.
