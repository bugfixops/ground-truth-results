# AnkiDroid batch 015 (LABEL helper). Preferences part 1: the Preferences activity methods, the class initialiser,
# and the subscreen listeners Preferences$1 to Preferences$7. Preferences$8 and Preferences$SettingsFragment are batch 016.
# 40 methods; the full row list is in graphs/AnkiDroid/parts/label_015.md.
#
# Ownership: an edge is written in the part that holds its source method. For a page source (S_PREFERENCES) it is written
# in the part that holds the destination method, so the page edges into this part are written here.
# Written here: the lifecycle edge Preferences.onCreate -> Preferences.onResume; the page edges S_PREFERENCES -> (FRAMEWORK,
# GUI) into this part; the REGISTER edges from the <init>s of Preferences$2 to $7; the INTENT edges from $3, $6 and $7 into
# Preferences.<init>; the entry Preferences.<clinit> -> Preferences.<init>.
# Not written here: the bytecode CALL edges inside Preferences and from Preferences$SettingsFragment (auto_calls.json, batch 016);
# the lifecycle chain of graph_def.py lines 200-201 (orchestrator; see the leads in label_015.md); the DeckPicker.onCreate ->
# Preferences.<init> INTENT edge (graph_def.py:1240, orchestrator); NavigationDrawerActivity.java:277 -> Preferences.<init>
# (batch 036).
#
# Gates (Missing gates are text only, in note=; env and needs_state are not set on those edges):
#   MG95 the Reviewing screen is open (its header was tapped; batch 016 starts it through SettingsFragment.onCreate)
#   MG96 the Advanced screen is open (its header was tapped)
#   MG97 the Custom buttons screen is open (it is started by the Custom buttons link, see Preferences$3)
#   MG98 the settings activity is started fresh (no saved state) and its start intent has no EXTRA_NO_HEADERS
#
# UNREACHABLE entries: Preferences.onCreateDialog, Preferences$1.<init>, Preferences$1.onPositive (closed_by_api_level: the
# only showDialog call sits in the fixHebrewText case, which needs a checked checkbox, and that checkbox is removed on SDK >= 16);
# Preferences.onSharedPreferenceChanged (closed_by_api_level: the activity is registered only in the isHoneycomb-false branch).
# Constants: none.

# ---- Preferences.onCreate -> onResume (lifecycle). lc_chain (graph_def.py:200) gives onResume only the route through
# onCreateDialog, which is not a lifecycle callback; this edge gives onResume its framework route directly.
e('Preferences.onCreate', 'Preferences.onResume', 'LIFECYCLE',
  'the framework resumes the settings activity after onCreate (onStart is between them and is not a method of this class)',
  evidence='FW-SRC core/java/android/app/Activity.java:989, 1311; SRC com/ichi2/anki/Preferences.java:109, 175',
  note='graph_def.py line 200 chains onCreate -> onCreateDialog -> onResume -> onPause. LC_RANK gives onCreateDialog rank 2, between onCreate (1) and onResume (4), so onResume is reached only through onCreateDialog, which the framework never calls as a lifecycle step. Lead for the orchestrator: remove onCreateDialog from that lc_chain list. This edge is the framework order.')

# ---- Page edges from the settings screen (S_PREFERENCES) into this part.
e('S_PREFERENCES', 'Preferences.onBuildHeaders', 'FRAMEWORK',
  'the framework builds the header list when the settings screen opens without EXTRA_NO_HEADERS',
  evidence='FW-SRC core/java/android/preference/PreferenceActivity.java:588, 605-607, 772-774; SRC com/ichi2/anki/Preferences.java:140-142',
  note='MISSING GATE MG98: the activity is started fresh (PreferenceActivity.java:588 is the saved-state test, the else branch at 605) and its start intent has no EXTRA_NO_HEADERS (PreferenceActivity.java:772-774). The navigation drawer start (NavigationDrawerActivity.java:277, batch 036) is a plain intent and reaches this edge; the CompatV11 subscreen intents set EXTRA_NO_HEADERS (CompatV11.java:47) and do not. env and needs_state unset.')

e('S_PREFERENCES', 'Preferences.isValidFragment', 'FRAMEWORK',
  'the framework checks the fragment name when the user opens a header, or when the activity starts with EXTRA_SHOW_FRAGMENT',
  evidence='FW-SRC core/java/android/preference/PreferenceActivity.java:610-611, 1246-1249, 1277-1286, 1295-1305, 968-973; SRC com/ichi2/anki/Preferences.java:146-148',
  note='The check is PreferenceActivity.java:1249 (switchToHeaderInner), reached from a header tap (switchToHeader(Header) at 1295-1305) or from the initial fragment at 610-611. The name in res/xml/preference_headers.xml is com.ichi2.anki.Preferences$SettingsFragment, so the method returns true. The subscreen intents of Preferences$3, $6 and $7 carry the same EXTRA_SHOW_FRAGMENT name. No gate: the check runs on every header tap or fragment start.')

e('S_PREFERENCES', 'Preferences.onKeyDown', 'GUI',
  'press the Back key on a settings screen',
  gui=['press the Back key on a settings screen'],
  evidence='SRC com/ichi2/anki/Preferences.java:191-197; FW-SRC core/java/android/app/Activity.java:3255-3274',
  note='Preferences.onKeyDown handles Back only when event.getRepeatCount() is 0 (Preferences.java:192) and then calls closePreferences (auto CALL, Preferences.java:194). The step from Activity.dispatchKeyEvent (Activity.java:3272-3273, event.dispatch) to onKeyDown is inside KeyEvent, which is not printed (INFERRED). No ENV gate.')

e('S_PREFERENCES', 'Preferences.onOptionsItemSelected', 'GUI',
  'tap the Up (home) arrow in the action bar of a settings screen',
  gui=['tap the Up (home) arrow in the action bar of a settings screen'],
  evidence='SRC com/ichi2/anki/Preferences.java:128-129, 152-158; SRC com/ichi2/ui/AppCompatPreferenceActivity.java:43; FW-SRC core/java/android/app/Activity.java:3439-3450',
  note='The home arrow is enabled at Preferences.java:128-129. The base class com/ichi2/ui/AppCompatPreferenceActivity.java overrides onCreate only (no onOptionsItemSelected or onKeyDown). The step from the AppCompat home button to Activity.onMenuItemSelected is INFERRED. Activity.onMenuItemSelected calls onOptionsItemSelected (Activity.java:3450). The only menu case is android.R.id.home, which calls finish (Preferences.java:154-155).')

# ---- Subscreen listeners of initSubscreen. REGISTER from each <init> (the builder does not follow REGISTER for reachability;
# the route is the GUI edge from the page).
e('Preferences$2.<init>', 'Preferences$2.onPreferenceChange', 'REGISTER',
  'the reviewing screen sets the full-screen mode change listener on the fullscreenMode preference',
  evidence='SRC com/ichi2/anki/Preferences.java:242-248',
  note='onPreferenceChange is in this part. The route is the S_PREFERENCES GUI edge below.')

e('S_PREFERENCES', 'Preferences$2.onPreferenceChange', 'GUI',
  'change the Full screen mode in the Reviewing screen',
  gui=['change the Full screen mode in the Reviewing screen'],
  evidence='SRC com/ichi2/anki/Preferences.java:248-259; FW-SRC core/java/android/preference/Preference.java:1079-1081',
  note='MISSING GATE MG95: the Reviewing screen is open (its header was tapped). Preference.callChangeListener (Preference.java:1079-1081) calls the listener. The ListPreference change path that reaches callChangeListener is not printed (INFERRED). The value 2 with gestures off returns false and shows a toast (Preferences.java:251-256). env and needs_state unset.')

e('Preferences$3.<init>', 'Preferences$3.onPreferenceClick', 'REGISTER',
  'the reviewing screen sets the click listener on the custom_buttons_link preference',
  evidence='SRC com/ichi2/anki/Preferences.java:262-263',
  note='onPreferenceClick is in this part. The route is the S_PREFERENCES GUI edge below.')

e('S_PREFERENCES', 'Preferences$3.onPreferenceClick', 'GUI',
  'tap Custom buttons in the Reviewing screen',
  gui=['tap Custom buttons in the Reviewing screen'],
  evidence='SRC com/ichi2/anki/Preferences.java:262-270; FW-SRC core/java/android/preference/Preference.java:1129-1140',
  note='MISSING GATE MG95: the Reviewing screen is open. Preference.performClick calls onClick and then the listener (Preference.java:1137).')

e('Preferences$3.onPreferenceClick', 'Preferences.<init>', 'INTENT',
  'the custom buttons screen opens in a new settings activity (CompatV11 subscreen intent)',
  env=None,
  evidence='SRC com/ichi2/anki/Preferences.java:264-266; SRC com/ichi2/compat/CompatV11.java:41-49; SRC com/ichi2/compat/CompatHelper.java:35-36; SRC com/ichi2/compat/CompatV21.java:13; SRC com/ichi2/compat/CompatV19.java:21; SRC com/ichi2/compat/CompatV17.java:11; SRC com/ichi2/compat/CompatV16.java:27; SRC com/ichi2/compat/CompatV15.java:11; SRC com/ichi2/compat/CompatV12.java:10',
  note='On API 27 the Compat object is CompatV21 (CompatHelper.java:35-36). CompatV21 -> CompatV19 -> CompatV17 -> CompatV16 -> CompatV15 -> CompatV12 -> CompatV11 is the class chain, and getPreferenceSubscreenIntent is declared only in CompatV11 (line 41) and CompatV10 (line 183), so the CompatV11 version is inherited. The intent names Preferences and sets EXTRA_NO_HEADERS (CompatV11.java:47). MISSING GATE MG95 (the tap) applies. Preferences is android:exported="false" (AndroidManifest.xml:192-196), so only AnkiDroid starts it.')

e('Preferences$4.<init>', 'Preferences$4.onPreferenceClick', 'REGISTER',
  'the custom buttons screen sets the click listener on reset_custom_buttons',
  evidence='SRC com/ichi2/anki/Preferences.java:279-285; SRC res/xml/preferences_custom_buttons.xml:27-28',
  note='onPreferenceClick is in this part. The route is the S_PREFERENCES GUI edge below.')

e('S_PREFERENCES', 'Preferences$4.onPreferenceClick', 'GUI',
  'tap Reset custom buttons in the Custom buttons screen',
  gui=['tap Reset custom buttons in the Custom buttons screen'],
  evidence='SRC com/ichi2/anki/Preferences.java:285-305; SRC res/xml/preferences_custom_buttons.xml:27-28',
  note='MISSING GATE MG97: the Custom buttons screen is open. It is entered only through the INTENT edge Preferences$3.onPreferenceClick -> Preferences.<init> (MG95 for the tap there). env and needs_state unset.')

e('Preferences$5.<init>', 'Preferences$5.onPreferenceChange', 'REGISTER',
  'the advanced screen sets the change listener on the deckPath preference',
  evidence='SRC com/ichi2/anki/Preferences.java:311-312',
  note='onPreferenceChange is in this part. The route is the S_PREFERENCES GUI edge below.')

e('S_PREFERENCES', 'Preferences$5.onPreferenceChange', 'GUI',
  'change the collection path (deckPath) in the Advanced screen',
  gui=['change the collection path (deckPath) in the Advanced screen'],
  evidence='SRC com/ichi2/anki/Preferences.java:311-324; SRC res/xml/preferences_advanced.xml:31',
  note='MISSING GATE MG96: the Advanced screen is open. CollectionHelper.initializeAnkiDroidDirectory (auto CALL, Preferences.java:316) is in another batch and is not read here; it either returns or throws StorageAccessException (line 318, toast and false). env and needs_state unset.')

e('Preferences$6.<init>', 'Preferences$6.onPreferenceClick', 'REGISTER',
  'the advanced screen sets the click listener on custom_sync_server_link',
  evidence='SRC com/ichi2/anki/Preferences.java:326-327; SRC res/xml/preferences_advanced.xml:39',
  note='onPreferenceClick is in this part. The route is the S_PREFERENCES GUI edge below.')

e('S_PREFERENCES', 'Preferences$6.onPreferenceClick', 'GUI',
  'tap Custom sync server in the Advanced screen',
  gui=['tap Custom sync server in the Advanced screen'],
  evidence='SRC com/ichi2/anki/Preferences.java:326-334; SRC res/xml/preferences_advanced.xml:39; FW-SRC core/java/android/preference/Preference.java:1129-1140',
  note='MISSING GATE MG96: the Advanced screen is open (its header was tapped). env and needs_state unset.')

e('Preferences$6.onPreferenceClick', 'Preferences.<init>', 'INTENT',
  'the custom sync server screen opens in a new settings activity (CompatV11 subscreen intent)',
  env=None,
  evidence='SRC com/ichi2/anki/Preferences.java:329-331; SRC com/ichi2/compat/CompatV11.java:41-49',
  note='The intent is built by CompatV11.getPreferenceSubscreenIntent, inherited on API 27 (see the Preferences$3 INTENT edge). MISSING GATE MG96 (the tap in the Advanced screen) applies.')

e('Preferences$7.<init>', 'Preferences$7.onPreferenceClick', 'REGISTER',
  'the advanced screen sets the click listener on advanced_statistics_link',
  evidence='SRC com/ichi2/anki/Preferences.java:336-337; SRC res/xml/preferences_advanced.xml:132',
  note='onPreferenceClick is in this part. The route is the S_PREFERENCES GUI edge below.')

e('S_PREFERENCES', 'Preferences$7.onPreferenceClick', 'GUI',
  'tap Advanced statistics in the Advanced screen',
  gui=['tap Advanced statistics in the Advanced screen'],
  evidence='SRC com/ichi2/anki/Preferences.java:336-344; SRC res/xml/preferences_advanced.xml:132; FW-SRC core/java/android/preference/Preference.java:1129-1140',
  note='MISSING GATE MG96: the Advanced screen is open (its header was tapped). env and needs_state unset.')

e('Preferences$7.onPreferenceClick', 'Preferences.<init>', 'INTENT',
  'the advanced statistics screen opens in a new settings activity (CompatV11 subscreen intent)',
  env=None,
  evidence='SRC com/ichi2/anki/Preferences.java:339-341; SRC com/ichi2/compat/CompatV11.java:41-49',
  note='The intent is built by CompatV11.getPreferenceSubscreenIntent, inherited on API 27. MISSING GATE MG96 (the tap in the Advanced screen) applies.')

# ---- Class initialiser. The static array sCollectionPreferences makes Preferences.<clinit> a real method.
e('Preferences.<clinit>', 'Preferences.<init>', 'FRAMEWORK',
  'the instance is constructed after the class is initialised',
  env=None,
  evidence='SRC com/ichi2/anki/Preferences.java:99-100, 788, 799, 812',
  note='The entries into Preferences.<clinit> are the bytecode CALL edges from Preferences$SettingsFragment.onCreate (788), onResume (799) and onSharedPreferenceChanged (812), and from Preferences$8.onPreferenceClick (350), all in auto_calls.json and batch 016. The JVM class-initialiser rule is not in the dataset: INFERRED. The DeckPicker INTENT edge (graph_def.py:1240) goes straight to Preferences.<init> and skips this node.')

# ---- UNREACHABLE: closed on API 27.
UNREACHABLE['Preferences.onCreateDialog'] = (
    'closed_by_api_level',
    "The only showDialog call is Preferences.java:479, in the fixHebrewText case of updatePreference, and that case runs only when the checkbox is checked (Preferences.java:476-478). On API 27 the checkbox cannot be checked: removeUnnecessaryAdvancedPrefs removes fixHebrewText from category_workarounds for SDK >= 16 (Preferences.java:723-724), and CompatHelper.removeHiddenPreferences removes the fixHebrewText key for SDK >= 16 (CompatHelper.java:133-134). The framework reaches onCreateDialog(int) through Activity.createDialog only from showDialog or from restoreManagedDialogs, and restoreManagedDialogs rebuilds only a dialog that was shown before (Activity.java:1154-1157, 1167-1168, 3971-3978). So there is no route. The lc_chain edges from Preferences.onCreate into onCreateDialog (graph_def.py:200) are not framework callbacks; see the lead in the Preferences.onCreate edge note.",
    'SRC com/ichi2/anki/Preferences.java:201, 476-479, 707-709, 723-724; SRC com/ichi2/compat/CompatHelper.java:133-134; FW-SRC core/java/android/app/Activity.java:1154-1157, 1167-1168, 3971-3978',
    'SOURCE')

UNREACHABLE['Preferences$1.<init>'] = (
    'closed_by_api_level',
    "The only caller in auto_calls.json is onCreateDialog (Preferences.java:209). onCreateDialog is closed on API 27 (see Preferences.onCreateDialog), so the constructor never runs.",
    'SRC com/ichi2/anki/Preferences.java:201, 209, 479, 723-724',
    'SOURCE')

UNREACHABLE['Preferences$1.onPositive'] = (
    'closed_by_api_level',
    "The positive button callback of the Hebrew font dialog (Preferences.java:209-216). The dialog is built only in onCreateDialog, which is closed on API 27 (see Preferences.onCreateDialog), so no dialog exists and the callback never runs. Its body would start the VIEW intent for the Hebrew font link (lines 212-214).",
    'SRC com/ichi2/anki/Preferences.java:201, 209-216, 479, 723-724',
    'SOURCE')

UNREACHABLE['Preferences.onSharedPreferenceChanged'] = (
    'closed_by_api_level',
    "The activity is registered as an OnSharedPreferenceChangeListener only in the legacy onResume branch (Preferences.java:178-180), which runs only when CompatHelper.isHoneycomb() is false (CompatHelper.java:61-62). On API 27 the activity is never registered, so SharedPreferences does not call this method. Its only other caller would be the settings fragment, which registers itself (Preferences.java:796) and calls Preferences.updatePreference from its own onSharedPreferenceChanged (Preferences.java:811-812), not this method. The other registrations in the app (DeckOptions.java:521, FilteredDeckOptions.java:376) are in other classes.",
    'SRC com/ichi2/anki/Preferences.java:178-180, 224-225, 796, 811-812; SRC com/ichi2/compat/CompatHelper.java:61-62; SRC com/ichi2/anki/DeckOptions.java:521; SRC com/ichi2/anki/FilteredDeckOptions.java:376',
    'SOURCE')
