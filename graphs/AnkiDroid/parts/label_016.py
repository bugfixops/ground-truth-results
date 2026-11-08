# AnkiDroid batch 016 (LABEL helper). Preferences part 2: the advanced-screen click listener Preferences$8 (force full
# sync, set in Preferences.initSubscreen, case advanced) and the settings fragment Preferences$SettingsFragment (<init>,
# onCreate, onResume, onPause, onSharedPreferenceChanged). 7 methods; the full row list is in
# graphs/AnkiDroid/parts/label_016.md.
#
# Ownership: an edge is written in the part that holds its source method. Written here: the REGISTER edges from
# Preferences$8.<init> and SettingsFragment.onResume (the builder does not follow REGISTER for reachability, so the
# routes are the S_PREFERENCES GUI and FRAMEWORK edges below); the LIFECYCLE edges inside SettingsFragment; and the
# page edges S_PREFERENCES -> my methods (the part holding the destination writes page-source edges).
# Not written here (leads, not my edges): the CALL edges from Preferences.initSubscreen to Preferences$8.<init>
# (batch_015); from SettingsFragment.onCreate to Preferences.initSubscreen and Preferences.initAllPreferences
# (Preferences.java:788-789); from SettingsFragment.onResume and onSharedPreferenceChanged to
# Preferences.updatePreference (Preferences.java:801, 812); and from Preferences$8.onPreferenceClick to
# Collection.modSchemaNoCheck and Collection.setMod (Preferences.java:350-351, other batches). These CALL edges come
# from auto_calls.json (USE_AUTO) and are not written by hand here.
#
# INTENT check: none of the 7 methods starts an app-class activity. The subscreen intent (CompatV11.java:41-48, started by
# DeckPicker.java:427) has its INTENT edge in graph_def.py (DeckPicker.onCreate -> Preferences.<init>).
#
# UNREACHABLE entries: none. All 7 methods have a route.
# Gates: MG105 is text only (note=) on the subscreen route. Predefined constants used: ENV_STORAGE on the force-full-sync
# click; STATE_SETTINGS on the onSharedPreferenceChanged GUI edge. Only MG105 is needed; MG106 to MG111 are not used.

# ---- Preferences$8: force_full_sync click listener (set in Preferences.initSubscreen, case advanced, Preferences.java:347-355) ----

e('Preferences$8.<init>', 'Preferences$8.onPreferenceClick', 'REGISTER',
  'the force-full-sync click listener is set on the force_full_sync preference',
  env=None,
  evidence='SRC com/ichi2/anki/Preferences.java:347-355',
  note='REGISTER. The builder does not follow REGISTER for reachability; the route is the S_PREFERENCES GUI edge below.')

e('S_PREFERENCES', 'Preferences$8.onPreferenceClick', 'GUI',
  'tap Force full sync on the Advanced settings screen',
  gui=['tap Force full sync on the Advanced settings screen'],
  env=ENV_STORAGE,
  evidence='SRC com/ichi2/anki/Preferences.java:347-355; SRC res/xml/preferences_advanced.xml:34-37; FW-SRC core/java/android/preference/PreferenceScreen.java:240-250; FW-SRC core/java/android/preference/Preference.java:1129-1139',
  note='Page edge. The row is a plain Preference in the advanced screen (preferences_advanced.xml:28, 34-37): no category, no enabled or hidden attribute. Preference.performClick returns early when disabled (Preference.java:1131), which does not apply here. The handler needs the collection: getCol (Preferences.java:350) opens it (CollectionHelper.java:85-101) and returns null only when the AnkiDroid directory cannot be initialised (CollectionHelper.java:90-96); line 350 then throws a NullPointerException. So env is ENV_STORAGE. needs_state unset: getCol opens the collection itself, and the route does not check its file state.')

# ---- Preferences$SettingsFragment (Preferences.java:782-814): lifecycle chain and listener registration ----

e('Preferences$SettingsFragment.<init>', 'Preferences$SettingsFragment.onCreate', 'LIFECYCLE',
  'lifecycle callback of Preferences$SettingsFragment (PreferenceFragment): onCreate follows the constructor',
  env=None,
  evidence='FW-SRC core/java/android/app/Fragment.java:2483-2490; FW-SRC core/java/android/app/FragmentManager.java:1237; SRC com/ichi2/anki/Preferences.java:782-790',
  note='The fragment is constructed by Fragment.instantiate (PreferenceActivity.java:1254). Its onCreate runs from FragmentManager.moveToState (FragmentManager.java:1237), which calls performCreate (Fragment.java:2489).')

e('Preferences$SettingsFragment.onCreate', 'Preferences$SettingsFragment.onResume', 'LIFECYCLE',
  'lifecycle callback of Preferences$SettingsFragment: onResume follows onCreate',
  env=None,
  evidence='FW-SRC core/java/android/app/Fragment.java:2547-2554; FW-SRC core/java/android/app/FragmentManager.java:1322; SRC com/ichi2/anki/Preferences.java:792-796',
  note='FragmentManager.java:1322 calls performResume, which calls onResume (Fragment.java:2554). The fragment is resumed while the settings screen is on top.')

e('Preferences$SettingsFragment.onResume', 'Preferences$SettingsFragment.onPause', 'LIFECYCLE',
  'lifecycle callback of Preferences$SettingsFragment: onPause follows onResume',
  env=None,
  evidence='FW-SRC core/java/android/app/Fragment.java:2703-2709; FW-SRC core/java/android/app/FragmentManager.java:1334; SRC com/ichi2/anki/Preferences.java:804-808',
  note='FragmentManager.java:1334 calls performPause, which calls onPause (Fragment.java:2709). The framework pauses the fragment when it leaves the resumed state (the activity pauses, or the fragment is removed or replaced by a header switch at PreferenceActivity.java:1259-1260).')

e('Preferences$SettingsFragment.onResume', 'Preferences$SettingsFragment.onSharedPreferenceChanged', 'REGISTER',
  'the settings fragment registers as the SharedPreferences listener on resume',
  env=None,
  evidence='SRC com/ichi2/anki/Preferences.java:796, 806',
  note='REGISTER at Preferences.java:796; the listener is removed in onPause (Preferences.java:806). The builder does not follow REGISTER for reachability; the route is the S_PREFERENCES GUI edge below.')

# ---- page edges into the SettingsFragment methods: the Advanced subscreen (intent) and the headers list (tap) ----

e('S_PREFERENCES', 'Preferences$SettingsFragment.<init>', 'FRAMEWORK',
  'the settings screen opens straight on the Advanced subscreen: the activity is started with the subscreen extras',
  env=None,
  evidence='SRC com/ichi2/compat/CompatV11.java:41-48; SRC com/ichi2/anki/DeckPicker.java:353, 415-428; FW-SRC core/java/android/preference/PreferenceActivity.java:582, 605-611, 1246-1256; SRC com/ichi2/anki/Preferences.java:146-148; FW-SRC core/java/android/app/Fragment.java:508-524',
  note='MISSING GATE MG105: the AnkiDroid directory is not accessible and no collection is open (the subscreen intent is started only in that branch of DeckPicker.onCreate, DeckPicker.java:415-427). No predefined ENV or STATE kind covers this. env and needs_state unset. The route: CompatV11.java:41-48 puts EXTRA_SHOW_FRAGMENT (the SettingsFragment name), the subscreen argument and EXTRA_NO_HEADERS; PreferenceActivity.onCreate skips the header build when headers are hidden (PreferenceActivity.java:606) and calls switchToHeader(initialFragment, initialArguments) (610-611); isValidFragment accepts this class name (Preferences.java:146-148); Fragment.instantiate creates the fragment (PreferenceActivity.java:1254).')

e('S_PREFERENCES', 'Preferences$SettingsFragment.<init>', 'GUI',
  'tap the Advanced row in the settings headers list',
  gui=['tap the Advanced row in the settings headers list'],
  env=None,
  evidence='SRC res/xml/preference_headers.xml:64-73; FW-SRC core/java/android/preference/PreferenceActivity.java:1079-1089, 1100-1106, 1295-1307, 1246-1256; FW-SRC core/java/android/app/Fragment.java:508-524',
  note='Page edge. The Advanced header names this fragment and carries the subscreen argument (preference_headers.xml:64-73). The tap runs onListItemClick and onHeaderClick (PreferenceActivity.java:1079-1089, 1100-1106); switchToHeader(Header) (1305) then creates the fragment. The headers are built by Preferences.onBuildHeaders (batch_015, a lead). The single-pane headers list on a phone is INFERRED: onIsMultiPane reads a resource that is not in fw_src.')

e('S_PREFERENCES', 'Preferences$SettingsFragment.onSharedPreferenceChanged', 'GUI',
  'change a preference value on the settings screen (a checkbox, a text field or a list choice)',
  gui=['change a preference value on the settings screen (a checkbox, a text field or a list choice)'],
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/Preferences.java:796, 806, 810-813; FW-SRC core/java/android/app/SharedPreferencesImpl.java:448, 491-500, 551-573; FW-SRC core/java/android/preference/Preference.java:1587, 1609',
  note='Page edge. The listener runs while the fragment is resumed (registered at Preferences.java:796, removed at 806), which the open settings page implies. The framework notifies it from SharedPreferencesImpl.notifyListeners (SharedPreferencesImpl.java:561) only for a key whose value changed; an equal value is skipped (SharedPreferencesImpl.java:497-500). needs_state=STATE_SETTINGS: the new value must differ from the stored one. The widgets that make the change (for example CheckBoxPreference) are framework classes outside this part. Other writers of the default preferences reach the same method while the fragment is resumed: leads for the batches that hold those writers.')
