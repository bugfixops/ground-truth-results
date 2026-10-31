# G2-5 route check: FloatEditTextPreference.getPersistedString

- Method: FloatEditTextPreference.getPersistedString(String) (ui/widgets/FloatEditTextPreference.java:47-49, `protected`, returns `String.valueOf(getPersistedFloat(-1))`)
- Label: REACHABLE
- Steps: 16; checked: 16 (every step read in the source or fw_src)
- Verdict: CORRECT (0 wrong steps)

Rule used: a step is WRONG if the transition cannot happen, or if its guard or STATE is false or missing. Kind labels, skipped hops that do not change the outcome, and citation errors are listed below and not counted.

## Wrong steps
None.

## Steps checked as OK (short)
- 1-6 cold start, as in G2-1 steps 1-6. Step 6 guard itemId == recent_tab_menu (AnyMemo.java:240-241).
- 7 GUI: drawer NavigationView listener (AnyMemo.java:209-232; binding.navView is `nav_view`, main_tabs.xml:52). The drawer must be opened first; this is not a node, which is normal for GUI.
- 8 INTENT: itemId == option_tab_menu (AnyMemo.java:222-223); option_tab_menu is in res/menu/main_screen_drawer_menu.xml.
- 9 OptionScreen.<init> -> onCreate, LIFECYCLE (OptionScreen.java:44-46; OptionScreen extends PreferenceActivity, line 36).
- 10 onCreate -> S_OPTION_SCREEN (addPreferencesFromResource, line 46).
- 11 FRAMEWORK: the preference click listener is set in onCreate (OptionScreen.java:50-51). The anonymous class is OptionScreen$1, the first anonymous class in the file (line 66).
- 12 ENTERS: AlertDialog built and shown in onPreferenceClick (OptionScreen.java:68-78).
- 13 GUI: tap OK; positive button listener is OptionScreen$1$1 (nested anonymous, lines 71-76).
- 14 ENTRY: startActivity(AlgorithmCustomizationScreen) (OptionScreen.java:73-74). AlgorithmCustomizationScreen extends PreferenceActivity (line 36).
- 15 LIFECYCLE <init> -> onCreate (AlgorithmCustomizationScreen.java:42-44).
- 16 FRAMEWORK, STATE "key exists in SharedPreferences". fw_src core/java/android/preference/Preference.java:1323-1328 calls dispatchSetInitialValue from onAttachedToHierarchy. Lines 1547-1562 call onSetInitialValue(true, null) only when `getSharedPreferences().contains(mKey)`. EditTextPreference.java:159-160 calls getPersistedString(mText) when restoreValue is true, and the virtual call reaches the FloatEditTextPreference override. The STATE matches line 1555.
- The three FloatEditTextPreference entries are declared in res/xml/algorithm_customization_screen.xml (lines 25, 31, 37), so onCreate's addPreferencesFromResource (line 44) inflates them.

## Citation and compression notes (not counted)
- Step 13 evidence says "androidx.fragment.app.DialogFragment shows an android.app.Dialog". OptionScreen uses `new AlertDialog.Builder(...).show()` inside the PreferenceActivity, with no DialogFragment. The edge is still right; fix the evidence text.
- Step 16 evidence says core/java/android/preference/Preference.java and EditTextPreference.java "not found in the source tree". Both files exist in fw_src (core/java/android/preference/), so the citation should point to them with the lines above.
- Step 16 skips the inflation hops (PreferenceManager inflate -> setPreferenceScreen -> onAttachedToHierarchy). The outcome is right and all of them run inside onCreate.
- Steps 9 and 15 cite Activity.java with no line numbers. The lifecycle dispatch is ActivityThread -> Instrumentation.callActivityOnCreate (Instrumentation.java:1212-1214) -> Activity.performCreate.

## Not checked
- androidx DialogFragment and the platform AlertDialog button dispatch not read (INFERRED for steps 7, 11, 13).
- The option_screen.xml key for "Customize scheduling algorithm" not read (the step text is taken from the listener's key constant).
- Runtime state: the route assumes the preference is saved (STATE), so the framework path is only taken on a non-fresh install; not run on a device.
