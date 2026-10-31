# AnkiDroid batch 073 (LABEL helper). CompatV19 and CompatV21 display paths, the CompatV16 openUrl route into the
# Custom Tabs helper, the Custom Tabs service callbacks, CustomDialogPreference and NumberRangePreference: 38 methods.
# The full row list is in graphs/AnkiDroid/parts/label_073.md.
#
# Route ownership:
# - The automatic CALL edges (auto_calls.json) are not written here. The rows name them.
# - Page edges (S_DECKOPTIONS, S_PREFERENCES, S_FILTEREDDECKOPTIONS) into methods of this batch are written here.
# - Edges into CustomTabActivityHelper.bindCustomTabsService (CustomTabActivityHelper.java:96-104) belong to the batch
#   that holds AnkiActivity.onStart. The support-library callbacks therefore have no inbound edge in this part.
# - Preferences.initPreference line 413 calls NumberRangePreference.setValue with no automatic edge. That edge belongs
#   to the batch that holds Preferences.initPreference and is not written here.
# - MG672 is the only MISSING GATE written on an edge here. MG673 to MG675 (Custom Tabs) appear in the rows only.

e('CompatV19$1.<init>', 'CompatV19$1.onSystemUiVisibilityChange', 'REGISTER',
  'decor view listener registered in setFullScreen; the framework calls it when the system UI visibility changes',
  evidence='SRC com/ichi2/compat/CompatV19.java:42-43; FW-SRC core/java/android/view/View.java:22684-22700; FW-SRC core/java/android/view/ViewRootImpl.java:5990-6007',
  note='MISSING GATE MG672: the callback fires when the system bars show or hide (a system or touch event). The app does not drive it and no constant fits, so env and needs_state are unset.')

e('CompatV19$2.<init>', 'CompatV19$2.onAnimationEnd', 'REGISTER',
  'AnimatorListenerAdapter set on the hide animation; the animator calls onAnimationEnd when the fade-out ends',
  evidence='SRC com/ichi2/compat/CompatV19.java:78-88; FW-SRC core/java/android/view/ViewPropertyAnimator.java:375-378, 1112-1122',
  note='setListener (CompatV19.java:82) stores the listener and ViewPropertyAnimator dispatches onAnimationEnd to it (1121-1122). No gate: the animation starts in hideViewWithAnimation.')

e('S_DECKOPTIONS', 'CustomDialogPreference.<init>', 'FRAMEWORK',
  'deck options screen inflates deck_options.xml, which holds the CustomDialogPreference entries',
  evidence='SRC com/ichi2/anki/DeckOptions.java:521-524; SRC res/xml/deck_options.xml:34-55; FW-SRC core/java/android/preference/GenericInflater.java:56-57',
  note='addPreferencesFromResource at DeckOptions.java:523 inflates the XML. The inflater uses the (Context, AttributeSet) constructor (GenericInflater.java:56-57). No gate.')

e('S_PREFERENCES', 'CustomDialogPreference.<init>', 'FRAMEWORK',
  'advanced preferences subscreen inflates preferences_advanced.xml, which holds the Reset Languages CustomDialogPreference',
  evidence='SRC com/ichi2/anki/Preferences.java:307-309; SRC res/xml/preferences_advanced.xml:106; FW-SRC core/java/android/preference/GenericInflater.java:56-57',
  note='addPreferencesFromResource at Preferences.java:308. No gate.')

e('S_DECKOPTIONS', 'CustomDialogPreference.onClick', 'GUI',
  'tap a deck option group preference (reset, remove, set subdecks) and then OK on its dialog',
  evidence='SRC com/ichi2/preferences/CustomDialogPreference.java:40-66; FW-SRC core/java/android/preference/DialogPreference.java:274-296, 386-388',
  gui=['tap a deck option group preference (reset, remove, set subdecks) and then OK on its dialog'],
  note='The preference opens its dialog through DialogPreference.onClick() (274-277) and showDialog (287-296). The positive button calls CustomDialogPreference.onClick (40). The preference title picks the branch (lines 42-56).')

e('S_PREFERENCES', 'CustomDialogPreference.onClick', 'GUI',
  'tap Reset Languages on the advanced preferences screen and then OK on its dialog',
  evidence='SRC com/ichi2/preferences/CustomDialogPreference.java:40-66; SRC res/xml/preferences_advanced.xml:106; FW-SRC core/java/android/preference/DialogPreference.java:274-296, 386-388',
  gui=['tap Reset Languages on the advanced preferences screen and then OK on its dialog'],
  note='Same dialog path as the deck options edge. Reset Languages takes the else branch (MetaDB.resetLanguages, CustomDialogPreference.java:59).')

e('S_PREFERENCES', 'NumberRangePreference.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'reviewing preferences subscreen inflates preferences_reviewing.xml, which holds NumberRangePreference entries',
  evidence='SRC com/ichi2/anki/Preferences.java:241-244; SRC res/xml/preferences_reviewing.xml:43-49; FW-SRC core/java/android/preference/GenericInflater.java:56-57',
  note='addPreferencesFromResource at Preferences.java:243. No gate.')

e('S_DECKOPTIONS', 'NumberRangePreference.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'deck options screen inflates deck_options.xml, which holds NumberRangePreference entries (lines 76-167)',
  evidence='SRC com/ichi2/anki/DeckOptions.java:521-524; SRC res/xml/deck_options.xml:76-167; FW-SRC core/java/android/preference/GenericInflater.java:56-57',
  note='addPreferencesFromResource at DeckOptions.java:523. No gate.')

e('S_FILTEREDDECKOPTIONS', 'NumberRangePreference.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'filtered deck options screen inflates cram_deck_options.xml, which holds one NumberRangePreference (line 26)',
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:376-379; SRC res/xml/cram_deck_options.xml:26; FW-SRC core/java/android/preference/GenericInflater.java:56-57',
  note='addPreferencesFromResource at FilteredDeckOptions.java:378. No gate.')

e('S_PREFERENCES', 'NumberRangePreference.getPersistedString', 'FRAMEWORK',
  'the screen reads the stored number preference value on load (Preference.dispatchSetInitialValue, then EditTextPreference.onSetInitialValue)',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/Preferences.java:241-244; SRC com/ichi2/preferences/NumberRangePreference.java:74-77; FW-SRC core/java/android/preference/Preference.java:1547-1562; FW-SRC core/java/android/preference/EditTextPreference.java:158-161',
  note='Runs only when the key is stored (Preference.java:1555-1560). If a preference data store is set (1548-1549) the call runs without a stored value; whether DeckOptions sets a data store was not checked.')

e('S_DECKOPTIONS', 'NumberRangePreference.getPersistedString', 'FRAMEWORK',
  'the deck options screen reads the stored number preference value on load',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/DeckOptions.java:521-524; SRC com/ichi2/preferences/NumberRangePreference.java:74-77; FW-SRC core/java/android/preference/Preference.java:1547-1562; FW-SRC core/java/android/preference/EditTextPreference.java:158-161',
  note='Same route as the reviewing screen. The key must be stored (Preference.java:1555-1560). The data-store branch (1548-1549) is not checked.')

e('S_FILTEREDDECKOPTIONS', 'NumberRangePreference.getPersistedString', 'FRAMEWORK',
  'the filtered deck options screen reads the stored number preference value on load',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:376-379; SRC com/ichi2/preferences/NumberRangePreference.java:74-77; FW-SRC core/java/android/preference/Preference.java:1547-1562; FW-SRC core/java/android/preference/EditTextPreference.java:158-161',
  note='Same route as the reviewing screen. The key must be stored (Preference.java:1555-1560). The data-store branch (1548-1549) is not checked.')

e('S_PREFERENCES', 'NumberRangePreference.onDialogClosed', 'GUI',
  'tap a number preference on the reviewing screen, then OK on its dialog',
  evidence='SRC com/ichi2/preferences/NumberRangePreference.java:58-64; FW-SRC core/java/android/preference/DialogPreference.java:274-296, 386-396',
  gui=['tap a number preference on the reviewing screen, then OK on its dialog'],
  note='DialogPreference.onDismiss calls onDialogClosed with the positive result (FW-SRC 395). showDialog sets up the dialog (287-296). Lines 61-62 call getValidatedRangeFromString and setValue (automatic edges).')

e('S_DECKOPTIONS', 'NumberRangePreference.onDialogClosed', 'GUI',
  'tap a number on the deck options screen, then OK on its dialog',
  evidence='SRC com/ichi2/preferences/NumberRangePreference.java:58-64; SRC com/ichi2/anki/DeckOptions.java:521-524; FW-SRC core/java/android/preference/DialogPreference.java:274-296, 386-396',
  gui=['tap a number on the deck options screen, then OK on its dialog'],
  note='Same dialog path as the reviewing screen (FW-SRC 395 calls onDialogClosed).')

e('S_FILTEREDDECKOPTIONS', 'NumberRangePreference.onDialogClosed', 'GUI',
  'tap a number on the filtered deck options screen, then OK on its dialog',
  evidence='SRC com/ichi2/preferences/NumberRangePreference.java:58-64; SRC com/ichi2/anki/FilteredDeckOptions.java:376-379; FW-SRC core/java/android/preference/DialogPreference.java:274-296, 386-396',
  gui=['tap a number on the filtered deck options screen, then OK on its dialog'],
  note='Same dialog path as the reviewing screen (FW-SRC 395 calls onDialogClosed).')

e('NumberRangePreference.setValue', 'NumberRangePreference.persistString', 'FRAMEWORK',
  'setValue writes the value through setText, which persists the text',
  evidence='SRC com/ichi2/preferences/NumberRangePreference.java:179-183; FW-SRC core/java/android/preference/EditTextPreference.java:88-94',
  note='setValue calls setText (181). EditTextPreference.setText calls persistString (FW-SRC 94), which dispatches to the override at NumberRangePreference.java:81-82 (persistInt). No gate.')

e('CustomTabActivityHelper.onServiceConnected', 'CustomTabActivityHelper.getSession', 'CALL',
  'the Custom Tabs service connected: onServiceConnected calls getSession to create a session',
  evidence='SRC com/ichi2/compat/customtabs/CustomTabActivityHelper.java:120-125, 83-90',
  note='Direct call at line 124. Not in auto_calls.json: the exact-match inbound query for getSession lists only CompatV16.openUrl (line 79). Gate MG673 applies to the callback, not to this call.')

# UNREACHABLE entries. Source references are printed lines in the .md rows.
UNREACHABLE['CustomTabsHelper.<init>'] = ('no_trigger_in_app', 'private empty constructor; no caller in the source root (grep for "new CustomTabsHelper" and "CustomTabsHelper()" finds only the declaration)', 'com/ichi2/compat/customtabs/CustomTabsHelper.java:47', 'SOURCE')
UNREACHABLE['CustomTabsHelper.getPackages'] = ('no_trigger_in_app', 'no caller in the source root (grep for CustomTabsHelper.getPackages finds only the declaration at line 144)', 'com/ichi2/compat/customtabs/CustomTabsHelper.java:144-146', 'SOURCE')
UNREACHABLE['NumberRangePreference.<init>(Context)'] = ('framework_never_calls', 'the inflater selects constructors with the (Context, AttributeSet) signature only (GenericInflater.java:56-57); no app code calls new NumberRangePreference(context)', 'com/ichi2/preferences/NumberRangePreference.java:50-55; core/java/android/preference/GenericInflater.java:56-57', 'SOURCE')
UNREACHABLE['NumberRangePreference.<init>(Context,AttributeSet,int)'] = ('framework_never_calls', 'the inflater uses the (Context, AttributeSet) signature only (GenericInflater.java:56-57); the (Context, AttributeSet) constructor calls super(context, attrs) and does not chain to this one; no app caller', 'com/ichi2/preferences/NumberRangePreference.java:34-39; core/java/android/preference/GenericInflater.java:56-57', 'SOURCE')
