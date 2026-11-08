# AnkiDroid batch 030 (LABEL helper). Info (the About page and the new-version page) and its inner classes: 11 methods,
# all REACHABLE. The full row list is in graphs/AnkiDroid/parts/label_030.md.
#
# Route ownership:
# - Automatic CALL edges from auto_calls.json are not written here: Info.onCreate -> Info$1.<init> (Info.java:77),
#   Info.onCreate -> Info$2.<init> (:87), Info.onCreate -> Info$3.<init> (:148), Info$2.onClick -> Info.finishWithAnimation
#   (:108), Info$3.onClick -> Info.copyDebugInfo (:151), Info.onKeyDown -> Info.finishWithAnimation (:174).
# - The graph_def.py INTENT edge DeckPicker.showStartupScreensAndDialogs -> Info.<init> is not written here. Its only
#   start in the source is behind VersionUtils.isReleaseVersion() (DeckPicker.java:938), which is false for the build
#   here (versionCode 20600206), so that route is closed.
# - No gate in this batch needs an MG id or a state or environment constant, so no UNREACHABLE entries are written.

# --- The About row of the advanced settings starts Info as TYPE_ABOUT.
e('S_PREFERENCES', 'Info.<init>', 'INTENT',
  'the About row of the advanced settings starts Info with no TYPE_EXTRA, so the page is TYPE_ABOUT',
  env=None,
  evidence='SRC res/xml/preferences_advanced.xml:137-143; SRC res/xml/preference_headers.xml:65-73; SRC com/ichi2/anki/NavigationDrawerActivity.java:273-277; SRC com/ichi2/anki/Preferences.java:233, 307-308, 785-788; SRC com/ichi2/anki/Info.java:66; FW-SRC core/java/android/preference/PreferenceScreen.java:240-249; FW-SRC core/java/android/preference/Preference.java:1129, 1151-1153',
  note='The Settings item of the navigation drawer starts Preferences. The advanced header is a SettingsFragment with the subscreen extra; its onCreate calls initSubscreen, which adds the advanced preferences. The About row has an intent with targetClass com.ichi2.anki.Info and no TYPE_EXTRA. A tap goes to PreferenceScreen.onItemClick, then Preference.performClick, which calls startActivity(mIntent).')

# --- Info.onCreate lays out the page (S_INFO is entered from this method).
e('Info.onCreate', 'S_INFO', 'ENTERS',
  'Info.onCreate lays out the About page or the new-version page',
  env=None,
  evidence='SRC com/ichi2/anki/Info.java:59-68, 143-166; FW-SRC core/java/android/app/Activity.java:6993-6999',
  note='Activity.performCreate calls onCreate when the activity starts. The page node S_INFO is entered from this method.')

# --- GUI taps and key presses on the About page.
e('S_INFO', 'Info$2.onClick', 'GUI',
  'tap the market button on the About page (rate the app, or the Amazon link on a Kindle)',
  env=None,
  gui=['tap the market button on the About page (rate the app, or the Amazon link on a Kindle)'],
  evidence='SRC com/ichi2/anki/Info.java:86-99; SRC res/layout/info.xml:60-61',
  note='The TYPE_ABOUT branch (Info.java:90-99) is the route. The new-version branch (101-108) is not used on the About page.')

e('S_INFO', 'Info$3.onClick', 'GUI',
  'tap the debug copy button on the About page (copies the debug info to the clipboard)',
  env=None,
  gui=['tap the debug copy button on the About page (copies the debug info to the clipboard)'],
  evidence='SRC com/ichi2/anki/Info.java:145-153; SRC res/layout/info.xml:53-58',
  note='The button is gone in the layout and is made VISIBLE in the TYPE_ABOUT case (Info.java:147).')

e('S_INFO', 'Info.onKeyDown', 'GUI',
  'press the back key on the About page',
  env=None,
  gui=['press the back key on the About page'],
  evidence='SRC com/ichi2/anki/Info.java:170-178; FW-SRC core/java/android/app/Activity.java:3255-3272; FW-SRC core/java/android/view/KeyEvent.java:2687-2691',
  note='KEYCODE_BACK with repeat count 0 (Info.java:171). Activity.dispatchKeyEvent ends with event.dispatch, which calls receiver.onKeyDown.')

# --- Framework callback: the WebView progress report while the About page loads.
e('S_INFO', 'Info$1.onProgressChanged', 'FRAMEWORK',
  'the WebView reports load progress while the About page loads (INFERRED: the WebView dispatch is not in fw_src, source not read)',
  env=None,
  evidence='SRC com/ichi2/anki/Info.java:77-84, 143; INFERRED (source not read): WebView progress callback',
  note='When progress is 100 the progress bar is hidden (Info.java:80-81). The WebView dispatch to WebChromeClient is not in fw_src.')
