# AnkiDroid batch 027 (LABEL helper). DeckOptions: 40 methods (graphs/AnkiDroid/scratch/batches/batch_027.txt).
# The full row list is in graphs/AnkiDroid/parts/label_027.md.
#
# Page node: S_DECKOPTIONS (the deck options preference screen).
# Gates: STATE_DECK on the page GUI edges (a deck exists); STATE_SETTINGS on the preference write edges and the
# commit DeckTask ASYNC edges (the changed preference value selects the route); ENV_SDCARD_EVENT on the SD eject receiver.
# Route ownership:
# - The <init> INTENT edges from DeckPicker and Reviewer are already in graph_def.py (lines 1285, 1318).
#   The lifecycle edge <init> -> onCreate comes from lc_chain (graph_def.py:173-174). Neither is written here.
# - The page edge S_STUDYOPTIONS_FRAG -> DeckOptions.<init> is written here by the destination rule. Batch 038 must not repeat it.
# - The RESULT edges from S_DECKOPTIONS are owned by batches 007, 008 and 020.
#   S_DECKOPTIONS -> Editor$1.onPositive and remConf -> Editor$2 ASYNC edges are owned by batch 028.
# - Automatic bytecode CALL edges (auto_calls.json) are not repeated. The one CALL written here,
#   Editor.commit -> onSharedPreferenceChanged, is missing from auto_calls.json.

# --- Read route: onCreate inflates the preference XML and reads each stored value through the store.
e('DeckOptions.onCreate', 'DeckOptions.getSharedPreferences', 'FRAMEWORK',
  'the inflate in onCreate asks the activity for its preference store',
  env=None,
  evidence='SRC com/ichi2/anki/DeckOptions.java:491-495, 523; FW-SRC core/java/android/preference/Preference.java:1199-1204; FW-SRC core/java/android/preference/PreferenceManager.java:506-510',
  note='The store is mPref (set at DeckOptions.java:520). The route is PreferenceActivity.addPreferencesFromResource (PreferenceActivity.java:1546-1549), then Preference.onAttachedToHierarchy (Preference.java:1320-1328).')

e('DeckOptions.onCreate', 'DeckOptions$DeckPreferenceHack.contains', 'FRAMEWORK',
  'the initial-value dispatch checks each keyed preference for a stored value during the inflate',
  env=None,
  evidence='SRC com/ichi2/anki/DeckOptions.java:415-417, 523; FW-SRC core/java/android/preference/Preference.java:1547-1560',
  note='Preference.dispatchSetInitialValue calls contains(key) (Preference.java:1554-1555) and calls onSetInitialValue only when the key is present.')

e('DeckOptions.onCreate', 'DeckOptions$DeckPreferenceHack.getBoolean', 'FRAMEWORK',
  'the checkbox preferences read their stored values during the inflate (newBury, revBury, showAnswerTimer, autoPlayAudio, replayQuestion)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckOptions.java:433-435, 523; SRC res/xml/deck_options.xml:100-102, 131-133, 174-181; FW-SRC core/java/android/preference/TwoStatePreference.java:187-189; FW-SRC core/java/android/preference/Preference.java:1909-1921',
  note='TwoStatePreference.onSetInitialValue calls getPersistedBoolean (TwoStatePreference.java:187-189), which calls the store getBoolean (Preference.java:1909-1921). getBoolean delegates to getString (DeckOptions.java:434).')

e('DeckOptions.onCreate', 'DeckOptions$DeckPreferenceHack.getInt', 'FRAMEWORK',
  'the number preferences read their stored values during the inflate (newPerDay, newGradIvl, newEasy, newFactor, revPerDay, easyBonus, revIvlFct, revMaxIvl, lapNewIvl, lapMinIvl, lapLeechThres, maxAnswerTime)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckOptions.java:445-447, 523; SRC com/ichi2/preferences/NumberRangePreference.java:74-77; SRC res/xml/deck_options.xml:76-168; FW-SRC core/java/android/preference/Preference.java:1747-1758; FW-SRC core/java/android/preference/EditTextPreference.java:157-161',
  note='NumberRangePreference.getPersistedString calls getPersistedInt (NumberRangePreference.java:74-77), which calls the store getInt (Preference.java:1747-1758). EditTextPreference.onSetInitialValue (EditTextPreference.java:157-161) starts the route.')

e('DeckOptions.onCreate', 'DeckOptions$DeckPreferenceHack.getString', 'FRAMEWORK',
  'the list and text preferences read their stored values during the inflate (deckConf, newOrder, lapLeechAct, desc)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckOptions.java:457-464, 523; SRC res/xml/deck_options.xml:20-22, 71-74, 162-164, 185-186; FW-SRC core/java/android/preference/ListPreference.java:294-295; FW-SRC core/java/android/preference/EditTextPreference.java:159-160',
  note='ListPreference.onSetInitialValue (ListPreference.java:294-295) and EditTextPreference.onSetInitialValue (EditTextPreference.java:159-160) call getPersistedString, which calls the store getString. updateSummaries and buildLists also call getString (automatic CALL, not repeated here).')

# --- Page GUI edges (STATE_DECK: the screen is open for a deck).
e('S_DECKOPTIONS', 'DeckOptions.onOptionsItemSelected', 'GUI',
  'tap the Up button in the action bar of the deck options screen',
  env=None,
  needs_state=STATE_DECK,
  gui=['tap the Up button in the action bar of the deck options screen'],
  evidence='SRC com/ichi2/anki/DeckOptions.java:545-552',
  note='The android.R.id.home item calls closeWithResult (DeckOptions.java:547-548). LC_NO_TRIGGER lists this method (graph_def.py:37), but the route is a GUI callback, so the page edge is written here.')

e('S_DECKOPTIONS', 'DeckOptions.onKeyDown', 'GUI',
  'press the Back key on the deck options screen',
  env=None,
  needs_state=STATE_DECK,
  gui=['press the Back key on the deck options screen'],
  evidence='SRC com/ichi2/anki/DeckOptions.java:579-587, 589-597',
  note='KEYCODE_BACK with repeat count 0 calls closeWithResult (DeckOptions.java:581-583), which sets the result and calls finish (589-597).')

e('S_DECKOPTIONS', 'DeckOptions.onPreferenceTreeClick', 'GUI',
  'tap any preference row on the deck options screen',
  env=None,
  needs_state=STATE_DECK,
  gui=['tap any preference row on the deck options screen'],
  evidence='SRC com/ichi2/anki/DeckOptions.java:565-576; FW-SRC core/java/android/preference/Preference.java:1140-1148; FW-SRC core/java/android/preference/PreferenceActivity.java:638-639',
  note='Preference.performClick calls the tree-click listener, which is this activity (PreferenceActivity.java:639). The body only sets a dialog background (DeckOptions.java:570-573) and returns false (575).')

# --- Preference write route (STATE_SETTINGS: the tap changes a stored value).
e('S_DECKOPTIONS', 'DeckOptions$DeckPreferenceHack.edit', 'GUI',
  'a preference value changes on the deck options screen',
  env=None,
  needs_state=STATE_SETTINGS,
  gui=['a preference value changes on the deck options screen'],
  evidence='SRC com/ichi2/anki/DeckOptions.java:421-423; FW-SRC core/java/android/preference/PreferenceManager.java:674-687; FW-SRC core/java/android/preference/Preference.java:1878-1896',
  note='The persist path calls PreferenceManager.getEditor, which calls getSharedPreferences().edit() (PreferenceManager.java:686), which is this method. The automatic CALL to Editor.<init> (DeckOptions.java:422) is not repeated.')

e('S_DECKOPTIONS', 'DeckOptions$DeckPreferenceHack$Editor.putBoolean', 'GUI',
  'tap a checkbox on the deck options screen (newBury, revBury, showAnswerTimer, autoPlayAudio, replayQuestion)',
  env=None,
  needs_state=STATE_SETTINGS,
  gui=['tap a checkbox on the deck options screen (newBury, revBury, showAnswerTimer, autoPlayAudio, replayQuestion)'],
  evidence='SRC com/ichi2/anki/DeckOptions.java:310-313; FW-SRC core/java/android/preference/TwoStatePreference.java:60-66, 75-82; FW-SRC core/java/android/preference/Preference.java:1878-1896',
  note='TwoStatePreference.onClick calls setChecked (60-66), which calls persistBoolean (75-82, 81), which calls putBoolean (Preference.java:1893).')

e('S_DECKOPTIONS', 'DeckOptions$DeckPreferenceHack$Editor.putInt', 'GUI',
  'tap OK on a number dialog on the deck options screen (NumberRangePreference keys)',
  env=None,
  needs_state=STATE_SETTINGS,
  gui=['tap OK on a number dialog on the deck options screen (NumberRangePreference keys)'],
  evidence='SRC com/ichi2/anki/DeckOptions.java:324-327; SRC com/ichi2/preferences/NumberRangePreference.java:81-83; FW-SRC core/java/android/preference/EditTextPreference.java:90-96, 142-150; FW-SRC core/java/android/preference/Preference.java:1716-1734',
  note='EditTextPreference.onDialogClosed (142-150) calls setText (90-96), which calls persistString (94). NumberRangePreference.persistString (81-83) turns the value into persistInt, which calls putInt (Preference.java:1731).')

e('DeckOptions$DeckPreferenceHack$Editor.putBoolean', 'DeckOptions$DeckPreferenceHack$Editor.apply', 'FRAMEWORK',
  'the framework commits the checkbox value',
  env=None,
  evidence='FW-SRC core/java/android/preference/Preference.java:1587-1591, 1878-1896; SRC com/ichi2/anki/DeckOptions.java:352-354',
  note='persistBoolean calls tryCommit (Preference.java:1894), and tryCommit calls editor.apply (Preference.java:1590). apply calls commit (DeckOptions.java:353), an automatic CALL.')

e('DeckOptions$DeckPreferenceHack$Editor.putInt', 'DeckOptions$DeckPreferenceHack$Editor.apply', 'FRAMEWORK',
  'the framework commits the number value',
  env=None,
  evidence='FW-SRC core/java/android/preference/Preference.java:1587-1591, 1716-1734; SRC com/ichi2/anki/DeckOptions.java:352-354',
  note='persistInt calls tryCommit (Preference.java:1732), and tryCommit calls editor.apply (Preference.java:1590).')

# --- Commit route: the listener loop and the conf-change DeckTask launches.
e('DeckOptions$DeckPreferenceHack$Editor.commit', 'DeckOptions.onSharedPreferenceChanged', 'CALL',
  'the commit notifies the registered listener (DeckOptions) that a preference changed',
  env=None,
  evidence='SRC com/ichi2/anki/DeckOptions.java:301-303, 521, 556-560',
  note='The listener loop in commit (DeckOptions.java:301-303) calls onSharedPreferenceChanged, which sets mPreferenceChanged and calls updateSummaries (556-559). This CALL is missing from auto_calls.json, so it is written here.')

e('DeckOptions$DeckPreferenceHack$Editor.commit', 'DeckOptions$DeckPreferenceHack$Editor$2.onPreExecute', 'ASYNC',
  'a changed conf, order, reset or subdeck value starts a conf-change DeckTask whose listener onPreExecute runs',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/DeckOptions.java:170-171, 223-224, 232-233, 276-277, 363-369; SRC com/ichi2/async/DeckTask.java:129-134, 344-347, 1298-1301',
  note='launchDeckTask (DeckTask.java:129-134) runs execute, which calls onPreExecute (DeckTask.java:344-347); the TaskListener default forwards to this method (DeckTask.java:1298-1301). The launches are at lines 170 (newOrder), 223 (deckConf), 232 (confReset) and 276 (confSetSubdecks), so the gate is the changed preference.')

e('DeckOptions$DeckPreferenceHack$Editor.commit', 'DeckOptions$DeckPreferenceHack$Editor$2.onPostExecute', 'ASYNC',
  'the conf-change DeckTask finishes and calls its listener onPostExecute (cacheValues, buildLists, updateSummaries, dismiss, restartActivity)',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/DeckOptions.java:170-171, 223-224, 232-233, 276-277, 378-385; SRC com/ichi2/async/DeckTask.java:358-365, 1298-1313',
  note='onPostExecute (DeckTask.java:358-365) forwards to the listener, and the TaskListener default forwards to this method (DeckTask.java:1305-1307). The body is at DeckOptions.java:378-385.')

# --- SD card eject receiver and lifecycle close.
e('S_DECKOPTIONS', 'DeckOptions$1.onReceive', 'SYSTEM',
  'the SD card is ejected while the deck options screen is open (MEDIA_EJECT broadcast)',
  env=ENV_SDCARD_EVENT,
  evidence='SRC com/ichi2/anki/DeckOptions.java:762-772; SRC com/ichi2/anki/receiver/SdCardReceiver.java:37, 41-46',
  note='The receiver is registered in onCreate (DeckOptions.java:514, 772). SdCardReceiver re-broadcasts MEDIA_EJECT (41-46); onReceive calls finish (766). Precedent: label_013.py:105-109.')

e('S_DECKOPTIONS', 'DeckOptions.onDestroy', 'LIFECYCLE',
  'the deck options screen closes (Up, back, SD eject or an error finish)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckOptions.java:601-606, 505, 518, 133; graph_def.py:37, 45-46',
  note='lc_chain skips onDestroy (LC_NO_TRIGGER, graph_def.py:37; skip at lines 45-46), so this page edge is the only route. onDestroy unregisters the receiver (DeckOptions.java:603-604).')

# --- UNREACHABLE entries.
UNREACHABLE['DeckOptions.addMissingValues'] = ('branch_never_taken',
  'The only call is the JSONException catch in DeckPreferenceHack.cacheValues (the try block is DeckOptions.java:95-130). The standard configuration has every key (Decks.defaultConf sets replayq, restoreToDefault copies it, the default deck has conf and desc, both fixture collections have one conf with replayq), so the catch is not taken. Caveat: a legacy collection whose conf lacks a key would take it.',
  'SRC com/ichi2/anki/DeckOptions.java:95-134, 777-789; grep: DeckOptions.java:132 is the only call; SRC com/ichi2/libanki/Decks.java:51-59, 85-88, 117-121, 754-762; fixtures final_java_only/_fixtures/Download/sample_deck.apkg and final_java_only/AnkiDroid/app/AnkiDroid-#4200/tools/test-decks/templates.apkg',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack.getAll'] = ('framework_never_calls',
  'No caller of getAll on this store. The framework preference package and the app source root have no call.',
  'SRC com/ichi2/anki/DeckOptions.java:427-429; grep of FW-SRC core/java/android/preference and the app source root: no call',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack.getFloat'] = ('framework_never_calls',
  'Only reached through Preference.getPersistedFloat (Preference.java:1801-1811), which has no caller in the framework preference package or the app source root. deck_options.xml has no float preference.',
  'SRC com/ichi2/anki/DeckOptions.java:439-441; FW-SRC core/java/android/preference/Preference.java:1801-1811; grep: no caller of getPersistedFloat',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack.getStringSet'] = ('framework_never_calls',
  'The only framework path is Preference.persistStringSet and getPersistedStringSet (Preference.java:1662-1703), and neither has a caller in the framework preference package or the app source root. deck_options.xml has no multi-select preference.',
  'SRC com/ichi2/anki/DeckOptions.java:481-484; FW-SRC core/java/android/preference/Preference.java:1662-1703; grep: no caller',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack.unregisterOnSharedPreferenceChangeListener'] = ('framework_never_calls',
  'No caller on this store. The two app callers (Preferences.java:168, 806) unregister on the Preferences screen own store, not on DeckOptions mPref, and the framework never calls this method.',
  'SRC com/ichi2/anki/DeckOptions.java:475-477; SRC com/ichi2/anki/Preferences.java:168, 806 (other object); grep of FW-SRC core/java/android/preference: no caller',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack$Editor.clear'] = ('framework_never_calls',
  'The framework preference package never calls Editor.clear on a preference store. The only app caller is DeckPicker.java:967, which clears the app preferences object (AnkiDroidApp.getSharedPrefs, AnkiDroidApp.java:219), not the DeckOptions store.',
  'SRC com/ichi2/anki/DeckOptions.java:143-147; SRC com/ichi2/anki/DeckPicker.java:964-968; SRC com/ichi2/anki/AnkiDroidApp.java:219; grep of FW-SRC core/java/android/preference: no edit().clear()',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack$Editor.putFloat'] = ('framework_never_calls',
  'persistFloat (Preference.java:1770-1785) has no caller in the framework preference package or the app source root. deck_options.xml has no float preference.',
  'SRC com/ichi2/anki/DeckOptions.java:317-320; FW-SRC core/java/android/preference/Preference.java:1770-1785; grep: no caller of persistFloat',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack$Editor.putLong'] = ('framework_never_calls',
  'persistLong (Preference.java:1824-1839) has no caller in the framework preference package or the app source root. deck_options.xml has no long preference. FilteredDeckOptions.java:229 has its own putLong in a different class.',
  'SRC com/ichi2/anki/DeckOptions.java:331-334; FW-SRC core/java/android/preference/Preference.java:1824-1839; grep: no caller of persistLong; SRC com/ichi2/anki/FilteredDeckOptions.java:229',
  'SOURCE')

e('S_STUDYOPTIONS_FRAG', 'DeckOptions.<init>', 'INTENT',
  'open the deck options from the study options screen',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:296-300; SRC com/ichi2/anki/DeckOptions.java:71')
