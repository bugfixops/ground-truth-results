# AnkiDroid batch 007 (LABEL helper): the 14 StudyOptionsActivity methods. The full row list is in
# graphs/AnkiDroid/parts/label_007.md.
#
# Ownership: an edge is written in the part that holds its source method. Page-sourced edges into batch-007
# methods are written here (GUI, RESULT). Written here: ENTERS from onCreate and loadStudyOptionsFragment (source
# is in this batch); GUI from S_STUDYOPTIONS and S_DLG_CUSTOM_STUDY; RESULT from the five result pages.
# Not written here: DeckPicker.openStudyOptions -> StudyOptionsActivity.<init> (INTENT, batch 003); the page edges
# from S_STUDYOPTIONS_FRAG (DeckOptions, FilteredDeckOptions, custom study dialog; batch 038); the page edges from the
# navigation drawer (Statistics, Preferences, CardBrowser; batch 036); the suppression of the unguarded bytecode CALL
# StudyOptionsFragment$3.onPostExecute -> StudyOptionsActivity.onRequireDeckListUpdate (batch 038, sup()).
#
# UNREACHABLE entries: StudyOptionsActivity.onOptionsItemSelected and StudyOptionsActivity.onRequireDeckListUpdate.
# Constants: none. Missing gates are text only (note='MISSING GATE MGn: ...', MG14 to MG16); no env or needs_state gate.

# ---- ENTERS (2): method -> page ----

e('StudyOptionsActivity.onCreate', 'S_STUDYOPTIONS', 'ENTERS',
  'the study options screen is shown: studyoptions.xml is inflated and the navigation drawer is set up',
  env=None,
  evidence='SRC com/ichi2/anki/StudyOptionsActivity.java:36-48; SRC res/layout/studyoptions.xml:16-18',
  note='onCreate is in this part. The start edge (DeckPicker.openStudyOptions -> StudyOptionsActivity.<init>, INTENT) is batch 003. Phone layout only: DeckPicker.java:365-367 sets mFragmented false when studyoptions_fragment is absent (it exists only in res/layout-xlarge/homescreen.xml:19).')

e('StudyOptionsActivity.loadStudyOptionsFragment', 'S_STUDYOPTIONS_FRAG', 'ENTERS',
  'the study options fragment is committed into the studyoptions_frame container of the activity',
  env=None,
  evidence='SRC com/ichi2/anki/StudyOptionsActivity.java:45-57; SRC res/layout/studyoptions.xml:16',
  note='Runs from onCreate only when savedInstanceState is null (StudyOptionsActivity.java:45-46). The withDeckOptions extra is set by DeckPicker.openStudyOptions (DeckPicker.java:1700-1701, batch 003).')

# ---- GUI (3): page -> method, via gui() ----

gui('S_STUDYOPTIONS', 'StudyOptionsActivity.onBackPressed',
    'press the Back key while the navigation drawer is closed',
    env=None,
    evidence='SRC com/ichi2/anki/StudyOptionsActivity.java:107-115; SRC com/ichi2/anki/NavigationDrawerActivity.java:240-247; FW-SRC core/java/android/app/Activity.java:2975-2981, 3272; FW-SRC core/java/android/view/KeyEvent.java:2715',
    note='MISSING GATE MG16: the drawer must be closed. With the drawer open the Back key closes the drawer instead (NavigationDrawerActivity.java:241-243; StudyOptionsActivity.java:109). Not modelled as a gate.')

gui('S_DLG_CUSTOM_STUDY', 'StudyOptionsActivity.onCreateCustomStudySession',
    'choose a Forgotten, Ahead, Random or Preview option in the custom study menu, then confirm; the custom study deck is built and the listener is called',
    env=None,
    evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:272-276, 304-307, 346-349; SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:184-185, 258-279, 415, 424-430, 467',
    note='MISSING GATE MG14: createCustomStudySession returns early (CustomStudyDialog.java:424-430) when a deck with the custom study name exists and its type flag is not 1; the standard fixture is assumed to have no such deck. MISSING GATE MG15: the custom study menu item is hidden for filtered decks (StudyOptionsFragment.java:346-349); the page edge from S_STUDYOPTIONS_FRAG is batch 038. A second route, through the tags dialog (CustomStudyDialog.java:145-176), reaches the same callback from another page; that page edge is not written here.')

gui('S_DLG_CUSTOM_STUDY', 'StudyOptionsActivity.onExtendStudyLimits',
    'choose the new-card limit or the review limit in the custom study menu and confirm',
    env=None,
    evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:272-276; SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:78-79, 184-185, 234-253, 482-488',
    note='MISSING GATE MG15: the custom study menu item is hidden for filtered decks (StudyOptionsFragment.java:346-349). jumpToReviewer is false on this path (the two-argument newInstance at CustomStudyDialog.java:78-79 is used at StudyOptionsFragment.java:273-274), so onLimitsExtended calls the listener (CustomStudyDialog.java:488).')

# ---- RESULT (5): page -> StudyOptionsActivity.onActivityResult ----

e('S_DECKOPTIONS', 'StudyOptionsActivity.onActivityResult', 'RESULT',
  'the deck options screen started from the study options fragment returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:294-301; FW-SRC core/java/android/app/Activity.java:748, 4486-4493, 7265-7266; FW-SRC core/java/android/app/ActivityThread.java:4264-4265',
  note='The fragment starts DeckOptions with getActivity().startActivityForResult (StudyOptionsFragment.java:300), so the result goes to this activity. The page edge from S_STUDYOPTIONS_FRAG is batch 038 and is not written here.')

e('S_FILTEREDDECKOPTIONS', 'StudyOptionsActivity.onActivityResult', 'RESULT',
  'the filtered deck options screen started from the study options fragment returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:138-139, 149-152, 296-297; FW-SRC core/java/android/app/Activity.java:748, 4486-4493, 7265-7266; FW-SRC core/java/android/app/ActivityThread.java:4264-4265',
  note='openFilteredDeckOptions (StudyOptionsFragment.java:149-152) is reached from the deck options item for a filtered deck (lines 296-297). The page edge from S_STUDYOPTIONS_FRAG is batch 038 and is not written here.')

e('S_STATISTICS', 'StudyOptionsActivity.onActivityResult', 'RESULT',
  'the statistics screen started from the navigation drawer returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:265-268; FW-SRC core/java/android/app/Activity.java:748, 4486-4493, 7265-7266; FW-SRC core/java/android/app/ActivityThread.java:4264-4265',
  note='nav_stats branch of the navigation drawer (line 265) starts Statistics with REQUEST_STATISTICS (line 268). The drawer is batch 036; its page edge is not written here.')

e('S_PREFERENCES', 'StudyOptionsActivity.onActivityResult', 'RESULT',
  'the preferences screen started from the navigation drawer returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:273-277; FW-SRC core/java/android/app/Activity.java:748, 4486-4493, 7265-7266; FW-SRC core/java/android/app/ActivityThread.java:4264-4265',
  note='nav_settings branch of the navigation drawer (line 273) starts Preferences with REQUEST_PREFERENCES_UPDATE (line 277). The drawer is batch 036; its page edge is not written here.')

e('S_CARDBROWSER', 'StudyOptionsActivity.onActivityResult', 'RESULT',
  'the card browser started from the navigation drawer returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:262-264, 295-298; FW-SRC core/java/android/app/Activity.java:748, 4486-4493, 7265-7266; FW-SRC core/java/android/app/ActivityThread.java:4264-4265',
  note='nav_browser branch (line 262) calls openCardBrowser (line 263), which starts CardBrowser with REQUEST_BROWSE_CARDS (line 298). The drawer is batch 036; its page edge is not written here.')

# ---- UNREACHABLE (2) ----

UNREACHABLE['StudyOptionsActivity.onOptionsItemSelected'] = (
    'framework_never_calls',
    "The framework calls this method from Activity.onMenuItemSelected for the options panel (Activity.java:3450). The panel is built in Activity.onCreatePanelMenu (Activity.java:3386-3390) from onCreateOptionsMenu and from the fragment manager's options-menu dispatch. StudyOptionsActivity, NavigationDrawerActivity and AnkiActivity do not override onCreateOptionsMenu, and StudyOptionsFragment never calls setHasOptionsMenu (grep of the app tree), so the activity has no options-panel item to select. The fragment's own toolbar menu (StudyOptionsFragment.java:186) sends its clicks to the fragment listener (StudyOptionsFragment.java:343), not to this activity. The home button is the only other source: its click listener is the Toolbar navigation listener (NavigationDrawerActivity.java:77-86), which opens the drawer because mNavButtonGoesBack stays false here (it is set only by showBackIcon, NavigationDrawerActivity.java:308, and showBackIcon is called only from Previewer.java:40 and 50). Toolbar and AppCompat dispatch is not in the dataset, so this claim is INFERRED. The body (StudyOptionsActivity.java:66-79) is therefore not reached.",
    'SRC com/ichi2/anki/StudyOptionsActivity.java:66-79; SRC com/ichi2/anki/StudyOptionsFragment.java:186, 343; SRC com/ichi2/anki/NavigationDrawerActivity.java:71-86, 301-309; FW-SRC core/java/android/app/Activity.java:3386-3390, 3439-3452',
    'INFERRED')

UNREACHABLE['StudyOptionsActivity.onRequireDeckListUpdate'] = (
    'branch_never_taken',
    "Two app call sites exist. StudyOptionsFragment.java:657-658 calls the listener only when mFragmented && refreshDecklist holds, and mFragmented is set at line 180 to getActivity().getClass() != StudyOptionsActivity.class, so it is false in this activity and the call is never made here. DeckPickerContextMenu.java:154 is the other call site; its only host is DeckPicker (DeckPicker.java:233 is the only DeckPickerContextMenu.newInstance call in the app tree), so the cast there is to DeckPicker and this method is not called on this activity. The bytecode extractor adds an unguarded CALL edge StudyOptionsFragment$3.onPostExecute -> StudyOptionsActivity.onRequireDeckListUpdate (auto_calls.json, line 11373, source StudyOptionsFragment.java:658); it ignores the guard at line 657 and must be suppressed by batch 038 with sup(). The body (StudyOptionsActivity.java:137) is not reached.",
    'SRC com/ichi2/anki/StudyOptionsFragment.java:180, 657-658; SRC com/ichi2/anki/dialogs/DeckPickerContextMenu.java:154; SRC com/ichi2/anki/DeckPicker.java:233, 2123; SRC com/ichi2/anki/StudyOptionsActivity.java:136-138',
    'SOURCE')
