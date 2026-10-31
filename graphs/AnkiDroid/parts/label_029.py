# AnkiDroid batch 029 (LABEL helper). FilteredDeckOptions: 37 methods. The full row list is in
# graphs/AnkiDroid/parts/label_029.md.
#
# Gates: MG232 (Editor.commit -> onDestroy) and MG233 (onCreate -> onDestroy). Predefined constants used: STATE_DECK
# (the screen is open for a filtered deck; the check is FilteredDeckOptions.java:369-373) and ENV_SDCARD_EVENT
# (the SD card eject receiver). Page nodes: S_FILTEREDDECKOPTIONS (the screen) and S_STUDYOPTIONS_FRAG.
#
# Automatic CALL edges (auto_calls.json) are not written here. S_STUDYOPTIONS_FRAG -> FilteredDeckOptions.<init> is
# written here by the destination rule, but graph_def.py:1148-1149 assigns page edges from S_STUDYOPTIONS_FRAG to
# batch 038: the orchestrator should dedupe it.

# --- Entry from the study options page (StudyOptionsFragment) and the lifecycle.
e('S_STUDYOPTIONS_FRAG', 'FilteredDeckOptions.<init>', 'INTENT',
  'open the filtered deck options from the study options screen',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:138-139, 149-153, 296-297, 558; SRC com/ichi2/anki/FilteredDeckOptions.java:59',
  note='The intent is built at StudyOptionsFragment.java:150 and started at line 152. The call at line 297 is under the filtered-deck check (lines 296-297); the call at line 558 was not checked for its guard. Dedupe with batch 038 (graph_def.py:1148-1149).')

e('FilteredDeckOptions.onCreate', 'FilteredDeckOptions.getSharedPreferences', 'FRAMEWORK',
  'the preference screen is inflated and the framework asks the activity for its preference store',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:343-347, 369-378; FW-SRC core/java/android/preference/PreferenceActivity.java:638, 1546-1551',
  note='The inflate at line 378 runs only after the filtered-deck check (lines 369-373). The hop from the screen to its child preferences is INFERRED (PreferenceGroup is not in fw_src).')

e('FilteredDeckOptions.onCreate', 'FilteredDeckOptions.onSharedPreferenceChanged', 'REGISTER',
  'the screen registers itself as a listener of its preference store',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:322, 375-376',
  note='The registration at line 376 is after the filtered-deck check (lines 369-373). The listener is called from Editor.commit (see that edge).')

e('FilteredDeckOptions.onCreate', 'FilteredDeckOptions.onDestroy', 'FRAMEWORK',
  'the screen finishes at once (no collection, or the deck is not a filtered deck) and the framework destroys it',
  env=None,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:355-357, 369-373; FW-SRC core/java/android/app/Activity.java:5526-5528, 7204-7208',
  note='MISSING GATE MG233: the collection is null (lines 355-357) or the deck is not a filtered deck (lines 369-373; finish at line 372). No predefined kind covers this. env and needs_state unset.')

e('FilteredDeckOptions.closeDeckOptions', 'FilteredDeckOptions.onDestroy', 'FRAMEWORK',
  'the screen closes (back key or up button) and the framework destroys it',
  env=None,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:431-438; FW-SRC core/java/android/app/Activity.java:5526-5528, 7204-7208',
  note='finish at line 436, after the optional rebuild (lines 432-435). Both callers are user actions on the screen, so no gate is written.')

e('FilteredDeckOptions$1.onReceive', 'FilteredDeckOptions.onDestroy', 'FRAMEWORK',
  'the SD card is ejected while the screen is open, the screen finishes and the framework destroys it',
  env=ENV_SDCARD_EVENT,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:503-508; FW-SRC core/java/android/app/Activity.java:5526-5528, 7204-7208',
  note='finish at line 507 inside the MEDIA_EJECT check (line 506 onwards).')

e('FilteredDeckOptions$DeckPreferenceHack$Editor.commit', 'FilteredDeckOptions.onDestroy', 'FRAMEWORK',
  'saving the filtered deck fails (a RuntimeException), the screen finishes and the framework destroys it',
  env=None,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:185-192; FW-SRC core/java/android/app/Activity.java:5526-5528, 7204-7208',
  note='MISSING GATE MG232: the save throws (caught at lines 185-192, finish at line 191). No predefined kind covers a save failure. env and needs_state unset.')

# --- Screen page edges (back key, up button, SD card eject, preference change).
e('S_FILTEREDDECKOPTIONS', 'FilteredDeckOptions.onKeyDown', 'GUI',
  'press the back key on the filtered deck options screen',
  env=None,
  needs_state=STATE_DECK,
  gui=['press the back key on the filtered deck options screen'],
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:421-429; FW-SRC core/java/android/app/Activity.java:3266-3272; FW-SRC core/java/android/view/KeyEvent.java:2684-2691',
  note='Repeat count 0 and KEYCODE_BACK (line 423) call closeDeckOptions (automatic CALL, line 425).')

e('S_FILTEREDDECKOPTIONS', 'FilteredDeckOptions.onOptionsItemSelected', 'GUI',
  'press the up button in the action bar of the filtered deck options screen',
  env=None,
  needs_state=STATE_DECK,
  gui=['press the up button in the action bar of the filtered deck options screen'],
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:398-410; FW-SRC core/java/android/app/Activity.java:3439-3450',
  note='The android.R.id.home case calls closeDeckOptions (automatic CALL, line 406). The support action bar hop is not in fw_src: INFERRED.')

e('S_FILTEREDDECKOPTIONS', 'FilteredDeckOptions$1.onReceive', 'SYSTEM',
  'the SD card is ejected while the filtered deck options screen is open',
  env=ENV_SDCARD_EVENT,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:503-513; SRC com/ichi2/anki/receiver/SdCardReceiver.java:37, 42-47; AndroidManifest.xml:269, 278',
  note='The receiver is registered at lines 511-513. The system-to-manifest hop is INFERRED (not in fw_src).')

e('S_FILTEREDDECKOPTIONS', 'FilteredDeckOptions$DeckPreferenceHack.edit', 'GUI',
  'change a setting on the filtered deck options screen (the preference is persisted through the store)',
  env=None,
  needs_state=STATE_DECK,
  gui=['change a setting on the filtered deck options screen (the preference is persisted through the store)'],
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:272-275; FW-SRC core/java/android/preference/PreferenceManager.java:674-686; FW-SRC core/java/android/preference/TwoStatePreference.java:81; FW-SRC core/java/android/preference/EditTextPreference.java:94',
  note='Preference.persistX calls PreferenceManager.getEditor, which calls getSharedPreferences().edit(). The check box path is TwoStatePreference.setChecked (line 81); the text path is EditTextPreference.setText (line 94).')

# --- Restore path: the framework reads the stored values when the screen is inflated.
e('FilteredDeckOptions.getSharedPreferences', 'FilteredDeckOptions$DeckPreferenceHack.contains', 'FRAMEWORK',
  'the screen restores its settings: the framework asks whether each key has a stored value',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:267-270, 343-347; FW-SRC core/java/android/preference/Preference.java:1547-1560',
  note='dispatchSetInitialValue calls contains on the object that getSharedPreferences returns (line 346). The screen gate is the onCreate inflate (see the getSharedPreferences edge).')

e('FilteredDeckOptions.getSharedPreferences', 'FilteredDeckOptions$DeckPreferenceHack.getBoolean', 'FRAMEWORK',
  'the screen restores a check box: its saved boolean is read',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:285-287, 343-347; SRC res/xml/cram_deck_options.xml:38, 43; FW-SRC core/java/android/preference/TwoStatePreference.java:187-188; FW-SRC core/java/android/preference/Preference.java:1909-1919',
  note='TwoStatePreference.onSetInitialValue calls getPersistedBoolean, which reads the store. CheckBoxPreference extends TwoStatePreference (FW-SRC core/java/android/preference/CheckBoxPreference.java:35).')

e('FilteredDeckOptions.getSharedPreferences', 'FilteredDeckOptions$DeckPreferenceHack.getInt', 'FRAMEWORK',
  'the screen restores the limit entry: its saved int is read',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:297-299, 343-347; SRC com/ichi2/preferences/NumberRangePreference.java:75-76; FW-SRC core/java/android/preference/EditTextPreference.java:159-160; FW-SRC core/java/android/preference/Preference.java:1747-1757',
  note='EditTextPreference.onSetInitialValue leads to NumberRangePreference.getPersistedString (lines 75-76), then getPersistedInt, then getSharedPreferences().getInt. The limit entry is res/xml/cram_deck_options.xml:26.')

# --- Write path: a preference change goes through edit, the put methods, apply, then commit.
e('FilteredDeckOptions$DeckPreferenceHack.edit', 'FilteredDeckOptions$DeckPreferenceHack$Editor.putBoolean', 'FRAMEWORK',
  'a check box changes: the framework writes its boolean through the editor',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:208-211, 272-275; FW-SRC core/java/android/preference/Preference.java:1878-1894',
  note='Preference.persistBoolean calls editor.putBoolean on the editor returned by edit().')

e('FilteredDeckOptions$DeckPreferenceHack.edit', 'FilteredDeckOptions$DeckPreferenceHack$Editor.putInt', 'FRAMEWORK',
  'the limit entry changes: the framework writes its int through the editor',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:222-225, 272-275; FW-SRC core/java/android/preference/Preference.java:1716-1732; SRC com/ichi2/preferences/NumberRangePreference.java:179-182',
  note='NumberRangePreference.setValue(int) calls persistInt (line 182), which calls editor.putInt.')

e('FilteredDeckOptions$DeckPreferenceHack.edit', 'FilteredDeckOptions$DeckPreferenceHack$Editor.putString', 'FRAMEWORK',
  'a text entry changes: the framework writes its string through the editor',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:236-239, 272-275; FW-SRC core/java/android/preference/Preference.java:1609-1626; FW-SRC core/java/android/preference/EditTextPreference.java:94',
  note='Preference.persistString calls editor.putString. EditTextPreference.setText calls persistString at line 94.')

e('FilteredDeckOptions$DeckPreferenceHack$Editor.putBoolean', 'FilteredDeckOptions$DeckPreferenceHack$Editor.apply', 'FRAMEWORK',
  'the check box value is committed: tryCommit applies the editor',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:208-211, 250-254; FW-SRC core/java/android/preference/Preference.java:1587-1590',
  note='Preference.tryCommit calls editor.apply (lines 1587-1590). apply calls commit only when mAllowCommit is set (line 252, automatic CALL).')

e('FilteredDeckOptions$DeckPreferenceHack$Editor.putInt', 'FilteredDeckOptions$DeckPreferenceHack$Editor.apply', 'FRAMEWORK',
  'the limit entry is committed: tryCommit applies the editor',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:222-225, 250-254; FW-SRC core/java/android/preference/Preference.java:1587-1590',
  note='Preference.tryCommit calls editor.apply (lines 1587-1590). apply calls commit only when mAllowCommit is set (line 252, automatic CALL).')

e('FilteredDeckOptions$DeckPreferenceHack$Editor.putString', 'FilteredDeckOptions$DeckPreferenceHack$Editor.apply', 'FRAMEWORK',
  'the text entry is committed: tryCommit applies the editor',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:236-239, 250-254; FW-SRC core/java/android/preference/Preference.java:1587-1590',
  note='Preference.tryCommit calls editor.apply (lines 1587-1590). apply calls commit only when mAllowCommit is set (line 252, automatic CALL).')

e('FilteredDeckOptions$DeckPreferenceHack$Editor.commit', 'FilteredDeckOptions.onSharedPreferenceChanged', 'CALL',
  'the save notifies the registered listeners, which include the screen',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:199-200, 376, 413-418',
  note='The listener loop (lines 199-200) calls every registered listener; the screen registers at line 376. Not an automatic edge: the loop is an interface call over a list.')

# --- UNREACHABLE: 10 methods (no call site, or no framework route).
UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack.getAll'] = (
  'no_trigger_in_app',
  'No call site. The only getAll() declarations are FilteredDeckOptions.java:279 and DeckOptions.java:427. No caller in com/ichi2 and none in the framework preference package.',
  'SRC com/ichi2/anki/FilteredDeckOptions.java:279-281; grep of SRC com/ichi2 and FW-SRC core/java/android/preference (no call)',
  'SOURCE')

UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack.getFloat'] = (
  'framework_never_calls',
  'The only framework path is Preference.getPersistedFloat (FW-SRC Preference.java:1801), and its only caller in fw_src is persistFloat, which has no caller. No entry on the screen stores a float.',
  'FW-SRC core/java/android/preference/Preference.java:1770-1786, 1801; SRC com/ichi2/anki/FilteredDeckOptions.java:290-293; SRC res/xml/cram_deck_options.xml:22-50',
  'SOURCE')

UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack.getLong'] = (
  'framework_never_calls',
  'The only framework path is Preference.getPersistedLong (FW-SRC Preference.java:1855), and its only caller in fw_src is persistLong, which has no caller. No entry on the screen stores a long.',
  'FW-SRC core/java/android/preference/Preference.java:1824-1840, 1855; SRC com/ichi2/anki/FilteredDeckOptions.java:303-305; SRC res/xml/cram_deck_options.xml:22-50',
  'SOURCE')

UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack.getStringSet'] = (
  'framework_never_calls',
  'The only framework path is Preference.getPersistedStringSet (FW-SRC Preference.java:1693, reads at 1700 and 1703), which is called only by persistStringSet (lines 1662-1668), and persistStringSet has no caller in fw_src. No entry on the screen stores a string set.',
  'SRC com/ichi2/anki/FilteredDeckOptions.java:333-336; FW-SRC core/java/android/preference/Preference.java:1662-1668, 1693, 1700, 1703; SRC res/xml/cram_deck_options.xml:22-50',
  'SOURCE')

UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack.unregisterOnSharedPreferenceChangeListener'] = (
  'no_trigger_in_app',
  'No call site has this store as receiver. The app callers (Preferences.java:168, 806) unregister on the preference screen store, not this one. fw_src has only the definition (SharedPreferencesImpl.java:223).',
  'SRC com/ichi2/anki/FilteredDeckOptions.java:327-329; SRC com/ichi2/anki/Preferences.java:168, 806; FW-SRC core/java/android/app/SharedPreferencesImpl.java:223',
  'SOURCE')

UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack$Editor.clear'] = (
  'no_trigger_in_app',
  'The editor is returned only by DeckPreferenceHack.edit, and this store is handed out only by FilteredDeckOptions.getSharedPreferences (line 346). The framework preference package never calls Editor.clear. The app clear (DeckPicker.java:967) is on another store.',
  'SRC com/ichi2/anki/FilteredDeckOptions.java:117-121, 272-275, 343-347; SRC com/ichi2/anki/DeckPicker.java:967; grep of FW-SRC core/java/android/preference (no editor clear call)',
  'SOURCE')

UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack$Editor.putFloat'] = (
  'framework_never_calls',
  'persistFloat (FW-SRC Preference.java:1770-1786) has no caller in fw_src or in com/ichi2, and no entry on the screen stores a float.',
  'SRC com/ichi2/anki/FilteredDeckOptions.java:215-218; FW-SRC core/java/android/preference/Preference.java:1770-1786; SRC res/xml/cram_deck_options.xml:22-50',
  'SOURCE')

UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack$Editor.putLong'] = (
  'framework_never_calls',
  'persistLong (FW-SRC Preference.java:1824-1840) has no caller in fw_src or in com/ichi2, and no entry on the screen stores a long.',
  'SRC com/ichi2/anki/FilteredDeckOptions.java:229-232; FW-SRC core/java/android/preference/Preference.java:1824-1840; SRC res/xml/cram_deck_options.xml:22-50',
  'SOURCE')

UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack$Editor.putStringSet'] = (
  'framework_never_calls',
  'Returns null (lines 258-261). persistStringSet (FW-SRC Preference.java:1662-1668) has no caller in fw_src, and no entry on the screen stores a string set.',
  'SRC com/ichi2/anki/FilteredDeckOptions.java:258-261; FW-SRC core/java/android/preference/Preference.java:1662-1668; SRC res/xml/cram_deck_options.xml:22-50',
  'SOURCE')

UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack$Editor.remove'] = (
  'no_trigger_in_app',
  'The app remove calls (DeckPicker.java:854, 979; com/ichi2/compat/CompatHelper.java:125-134; Preferences.java:535) are on other stores. This store is handed out only by FilteredDeckOptions.getSharedPreferences (line 346), and the framework preference package never calls Editor.remove.',
  'SRC com/ichi2/anki/FilteredDeckOptions.java:243-247, 343-347; SRC com/ichi2/anki/DeckPicker.java:854, 979; SRC com/ichi2/compat/CompatHelper.java:125-134; SRC com/ichi2/anki/Preferences.java:535; grep of FW-SRC core/java/android/preference (no editor remove call)',
  'SOURCE')
