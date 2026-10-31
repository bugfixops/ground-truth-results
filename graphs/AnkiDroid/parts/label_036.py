# AnkiDroid batch 036 (LABEL helper). NavigationDrawerActivity (the navigation drawer) and Previewer: 30 methods.
# The full row list is in graphs/AnkiDroid/parts/label_036.md. This part writes 22 edges and no UNREACHABLE entries.
#
# Route ownership:
# - Automatic CALL edges (bytecode builder) are not written here, for example DeckPicker.onCreate -> initNavigationDrawer,
#   Previewer.onCreate -> disableDrawerSwipe and showBackIcon, and DeckPicker.onBackPressed -> super.onBackPressed.
# - Edges whose source is in another part are not written here: AnkiActivity.onLoadFinished -> Previewer.onCollectionLoaded,
#   AbstractFlashcardViewer.onCollectionLoaded -> Previewer.initLayout / setTitle / updateScreenCounts,
#   AbstractFlashcardViewer.onResume -> Previewer.updateScreenCounts, and the start-long-click runnable (batch 021) ->
#   Previewer.executeCommand.
# - The virtual dispatch from NavigationDrawerActivity.onNavigationItemSelected to the DeckPicker and Reviewer
#   openCardBrowser overrides is written here (E9, E10).
#
# Gates: MG302 (the chosen drawer item is not already checked), MG303 (the activity has a toolbar). Predefined constants
# used: ENV_CONFIG_CHANGE, STATE_SETTINGS. Page nodes used: S_ENTRY, S_DECKPICKER, S_STUDYOPTIONS, S_CARDBROWSER,
# S_STATISTICS, S_REVIEWER, S_PREVIEWER.

# --- Drawer page edges (the drawer is on five screens; the destination is in this part).
e('S_DECKPICKER', 'NavigationDrawerActivity.onNavigationItemSelected', 'GUI',
  'pick an item in the navigation drawer on the deck list',
  env=None,
  gui=['pick an item in the navigation drawer on the deck list'],
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:68, 249-290; SRC com/ichi2/anki/DeckPicker.java:110',
  note='Page edge. The NavigationView dispatch is the support library, not in fw_src: INFERRED.')

e('S_STUDYOPTIONS', 'NavigationDrawerActivity.onNavigationItemSelected', 'GUI',
  'pick an item in the navigation drawer on the study options screen',
  env=None,
  gui=['pick an item in the navigation drawer on the study options screen'],
  evidence='SRC com/ichi2/anki/StudyOptionsActivity.java:31; SRC com/ichi2/anki/NavigationDrawerActivity.java:249-290',
  note='Page edge. The same drawer listener as S_DECKPICKER.')

e('S_CARDBROWSER', 'NavigationDrawerActivity.onNavigationItemSelected', 'GUI',
  'pick an item in the navigation drawer on the card browser',
  env=None,
  gui=['pick an item in the navigation drawer on the card browser'],
  evidence='SRC com/ichi2/anki/CardBrowser.java:86; SRC com/ichi2/anki/NavigationDrawerActivity.java:249-290',
  note='Page edge. The same drawer listener as S_DECKPICKER.')

e('S_STATISTICS', 'NavigationDrawerActivity.onNavigationItemSelected', 'GUI',
  'pick an item in the navigation drawer on the statistics screen',
  env=None,
  gui=['pick an item in the navigation drawer on the statistics screen'],
  evidence='SRC com/ichi2/anki/Statistics.java:59; SRC com/ichi2/anki/NavigationDrawerActivity.java:249-290',
  note='Page edge. The same drawer listener as S_DECKPICKER.')

e('S_REVIEWER', 'NavigationDrawerActivity.onNavigationItemSelected', 'GUI',
  'pick an item in the navigation drawer on the reviewer',
  env=None,
  gui=['pick an item in the navigation drawer on the reviewer'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:110; SRC com/ichi2/anki/Reviewer.java:56; SRC com/ichi2/anki/NavigationDrawerActivity.java:249-290',
  note='Page edge. The Reviewer is an AbstractFlashcardViewer, which extends NavigationDrawerActivity.')

# --- Drawer items (MG302: the item must not already be checked, NavigationDrawerActivity.java:252).
e('NavigationDrawerActivity.onNavigationItemSelected', 'DeckPicker.<init>', 'INTENT',
  'choose the Decks item in the drawer: start DeckPicker with CLEAR_TOP and NEW_TASK',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:252-260',
  note='MISSING GATE MG302: the Decks item is not already checked (NavigationDrawerActivity.java:252 returns true when it is). env and needs_state unset.')

e('NavigationDrawerActivity.onNavigationItemSelected', 'Statistics.<init>', 'INTENT',
  'choose the Statistics item in the drawer: start Statistics with the selected deck',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:265-268',
  note='MISSING GATE MG302: the Statistics item is not already checked (NavigationDrawerActivity.java:252). The request code is REQUEST_STATISTICS. env and needs_state unset.')

e('NavigationDrawerActivity.onNavigationItemSelected', 'Preferences.<init>', 'INTENT',
  'choose the Settings item in the drawer: start Preferences with REQUEST_PREFERENCES_UPDATE',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:273-277',
  note='MISSING GATE MG302: the Settings item is not already checked (NavigationDrawerActivity.java:252). graph_def.py:1240 is a different edge (DeckPicker.onCreate to Preferences.<init>). env and needs_state unset.')

e('NavigationDrawerActivity.onNavigationItemSelected', 'DeckPicker.openCardBrowser', 'CALL',
  'choose the Card browser item in the drawer on the deck list (virtual dispatch to the DeckPicker override)',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:262-264; SRC com/ichi2/anki/DeckPicker.java:1707-1713',
  note='MISSING GATE MG302: the Card browser item is not already checked (NavigationDrawerActivity.java:252). The call at line 263 resolves to the DeckPicker override by virtual dispatch. env and needs_state unset.')

e('NavigationDrawerActivity.onNavigationItemSelected', 'Reviewer.openCardBrowser', 'CALL',
  'choose the Card browser item in the drawer on the reviewer (virtual dispatch to the Reviewer override)',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:262-264; SRC com/ichi2/anki/Reviewer.java:507-513',
  note='MISSING GATE MG302: the Card browser item is not already checked (NavigationDrawerActivity.java:252). The call at line 263 resolves to the Reviewer override by virtual dispatch. env and needs_state unset.')

e('NavigationDrawerActivity.openCardBrowser', 'CardBrowser.<init>', 'INTENT',
  'open the card browser from the drawer on the study options or statistics screen',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:295-299',
  note='Start CardBrowser with the selected deck and REQUEST_BROWSE_CARDS. The DeckPicker and Reviewer overrides already have this edge (graph_def.py:1272, 1331).')

e('NavigationDrawerActivity.onNavigationItemSelected', 'NavigationDrawerActivity$2.onCheckedChanged', 'FRAMEWORK',
  'choose the night-mode item in the drawer: performClick toggles the switch and fires its listener',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:270-272, 89-105',
  note='MISSING GATE MG302: the night-mode item is not already checked (NavigationDrawerActivity.java:252). The click dispatch on SwitchCompat/CompoundButton is the support library, not in fw_src: INFERRED. env and needs_state unset.')

# --- Night-mode switch and toolbar button (page edges), and drawer listener edges.
e('S_DECKPICKER', 'NavigationDrawerActivity$2.onCheckedChanged', 'GUI',
  'toggle the night-mode switch in the drawer on the deck list',
  env=None,
  gui=['toggle the night-mode switch in the drawer on the deck list'],
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:89-105',
  note='Page edge. The listener saves the invertedColors preference and restarts the activity (NavigationDrawerActivity.java:96-103).')

e('S_DECKPICKER', 'NavigationDrawerActivity$1.onClick', 'GUI',
  'tap the toolbar navigation button on the deck list (opens the drawer)',
  env=None,
  gui=['tap the toolbar navigation button on the deck list (opens the drawer)'],
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:69-86',
  note='MISSING GATE MG303: the activity has a toolbar (NavigationDrawerActivity.java:69-70 tests toolbar != null). mNavButtonGoesBack stays false on the deck list, so the listener opens the drawer (line 83). env and needs_state unset.')

e('NavigationDrawerActivity$1.onClick', 'NavigationDrawerActivity$3.onDrawerOpened', 'FRAMEWORK',
  'openDrawer at line 83 calls the drawer listener, which runs onDrawerOpened',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:83, 116-120',
  note='The DrawerLayout dispatch to the listener is the support library, not in fw_src: INFERRED.')

e('NavigationDrawerActivity.onNavigationItemSelected', 'NavigationDrawerActivity$3.onDrawerClosed', 'FRAMEWORK',
  'closeDrawers at line 288 calls the drawer listener, which runs onDrawerClosed',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:288, 110-113',
  note='The DrawerLayout dispatch to the listener is the support library, not in fw_src: INFERRED.')

e('NavigationDrawerActivity.onBackPressed', 'NavigationDrawerActivity$3.onDrawerClosed', 'FRAMEWORK',
  'closeDrawers at line 243 calls the drawer listener, which runs onDrawerClosed',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:241-243, 110-113',
  note='The Back key with the drawer open closes it. The DrawerLayout dispatch to the listener is the support library, not in fw_src: INFERRED.')

# --- Configuration change and lifecycle.
e('S_ENTRY', 'NavigationDrawerActivity.onConfigurationChanged', 'SYSTEM',
  'the device configuration changes while the app runs (rotation, locale, screen size)',
  env=ENV_CONFIG_CHANGE,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:173-180; FW-SRC core/java/android/app/ActivityThread.java:4785-4804; FW-SRC core/java/android/app/Activity.java:2196-2200; SRC final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/AndroidManifest.xml:132-138',
  note='DeckPicker declares configChanges keyboardHidden, orientation, screenSize, locale (AndroidManifest.xml lines 132-138), so the change reaches the running activity without a restart.')

e('S_DECKPICKER', 'NavigationDrawerActivity.onPostCreate', 'LIFECYCLE',
  'the framework calls onPostCreate after the deck list starts',
  env=None,
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2757-2760; SRC com/ichi2/anki/NavigationDrawerActivity.java:164-171; FW-SRC core/java/android/app/Activity.java:1198-1202',
  note='S_DECKPICKER is entered by DeckPicker.onCreate (ENTERS, graph_def.py:835). The framework callback path (callActivityOnPostCreate) is FW-SRC; the dispatch from the page is the lifecycle order.')

# --- Previewer.
e('S_PREVIEWER', 'Previewer.displayCardAnswer', 'GUI',
  'tap the show-answer control on the preview screen',
  env=None,
  gui=['tap the show-answer control on the preview screen'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:382-394, 1384; SRC com/ichi2/anki/Previewer.java:67-74',
  note='Page edge. The flip listener calls displayCardAnswer at AbstractFlashcardViewer.java:392, which dispatches virtually to this override.')

e('Previewer.onCollectionLoaded', 'S_PREVIEWER', 'ENTERS',
  'the preview screen is shown after the card loads and the question is displayed',
  env=None,
  evidence='SRC com/ichi2/anki/Previewer.java:45-51',
  note='Method to page (ENTERS). The loader delivery edge into onCollectionLoaded is the AnkiActivity part (AnkiActivity.java:283-286).')

e('S_PREVIEWER', 'Previewer.executeCommand', 'GUI',
  'long-press the card area on the preview screen when the long-click workaround is on',
  env=None,
  needs_state=STATE_SETTINGS,
  gui=['long-press the card area on the preview screen when the long-click workaround is on'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:373-378, 468-481, 1334-1335, 1719-1720; SRC com/ichi2/anki/Previewer.java:83-86',
  note='The long-click listener is set only when !mDisableClipboard and mLongClickWorkaround (the dictionary preference is not "0", and textSelectionLongclickWorkaround is true). Both are STATE_SETTINGS. The gesture branches (AbstractFlashcardViewer.java:2681-2752) reach the same override only when gestures are on (STATE_SETTINGS); the run body of the long-click runnable is batch 021.')
