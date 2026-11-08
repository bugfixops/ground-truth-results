# AnkiDroid batch 038 (LABEL helper). StudyOptionsFragment: 38 methods. The full row list is in
# graphs/AnkiDroid/parts/label_038.md.
#
# Ownership: CALL edges (auto_calls.json) and the lc_chain LIFECYCLE edges (graph_def.py:215-216) are not written here.
# The two existing INTENT edges (S_STUDYOPTIONS_FRAG -> FilteredDeckOptions.<init>, DeckOptions.<init>) and the sup()
# pairs (graph_def.py:1235-1236) are not repeated here.
# Page-sourced edges into batch-038 methods are written here (start button, toolbar menu, phone back arrow), and the
# custom study page edge (graph_def.py:1148-1149). DeckTask ASYNC launch edges go from the launcher to the listener
# callback $3.onPostExecute, as in label_019.py:43.
#
# Gates: MG324 (1000 new cards), MG323 and MG325 (toolbar items), MG327 (phone layout), MG329 (congrats button).
# Predefined constants used: STATE_CARDS (start button), STATE_DECK (toolbar and custom study).
# Page nodes: S_STUDYOPTIONS_FRAG (the fragment, in both hosts) and S_DLG_CUSTOM_STUDY.

# --- Page edges into the fragment's own methods.

# Start button (R.id.studyoptions_start), set in initAllContentViews (StudyOptionsFragment.java:265).
e('S_STUDYOPTIONS_FRAG', 'StudyOptionsFragment$1.onClick', 'GUI',
  'tap the Start button of the study options page (study the deck, or open custom study on the congrats content)',
  env=None,
  needs_state=STATE_CARDS,
  gui=['tap the Start button of the study options page (study the deck, or open custom study on the congrats content)'],
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:120-136, 265, 570-586',
  note='The Start button is shown with the study-options content only when cards are due or learning (lines 581-585), so STATE_CARDS is the gate. On the congrats content (lines 570-574) the same button opens custom study (line 130); that case is MISSING GATE MG329: it needs a non-filtered deck with no cards due.')

# Toolbar menu (configureToolbar sets the listener to the fragment at StudyOptionsFragment.java:343).
e('S_STUDYOPTIONS_FRAG', 'StudyOptionsFragment.onMenuItemClick', 'GUI',
  'tap an item of the study options toolbar menu (undo, deck options, custom study, unbury, rebuild, empty, rename, delete, export)',
  env=None,
  needs_state=STATE_DECK,
  gui=['tap an item of the study options toolbar menu (undo, deck options, custom study, unbury, rebuild, empty, rename, delete, export)'],
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:186, 287-343, 346-370',
  note='Item gates: MISSING GATE MG322 for unbury (visible only when cards are buried, line 370); MISSING GATE MG323 for custom study (lines 346-357); MISSING GATE MG325 for rebuild and empty (visible only for a filtered deck, lines 346-348). Rename, delete and export (lines 328-335) call DeckPicker methods: confirmDeckDeletion and exportDeck have edges from S_STUDYOPTIONS_FRAG in label_002.py:207-212; renameDeckDialog has no edge in any part (lead). Undo, deck options and custom study call openReviewer, openFilteredDeckOptions and showCustomStudyContextMenu by CALL (auto_calls.json).')

# Back arrow on the fragment toolbar, set in configureToolbar (lines 380-388) only when mFragmented is false.
e('S_STUDYOPTIONS_FRAG', 'StudyOptionsFragment$2.onClick', 'GUI',
  'tap the back arrow of the study options toolbar in the phone layout (hosted by StudyOptionsActivity)',
  env=None,
  gui=['tap the back arrow of the study options toolbar in the phone layout (hosted by StudyOptionsActivity)'],
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:180, 380-388',
  note='MISSING GATE MG327: the arrow exists only when mFragmented is false, which is the StudyOptionsActivity host (phone layout, StudyOptionsFragment.java:180). No predefined ENV or STATE covers the device layout. env and needs_state unset.')

# Custom study page edge (graph_def.py:1148-1149 ownership). The dialog callbacks are label_002 and label_007.
e('StudyOptionsFragment.showCustomStudyContextMenu', 'S_DLG_CUSTOM_STUDY', 'ENTERS',
  'the custom study menu dialog is created and shown by showCustomStudyContextMenu (toolbar item, or the congrats start button)',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:272-276; SRC com/ichi2/anki/StudyOptionsFragment.java:127-131, 306-307',
  note='The user step is the GUI edge S_STUDYOPTIONS_FRAG -> StudyOptionsFragment.onMenuItemClick (label_038). MISSING GATE MG323: the toolbar item is hidden for filtered decks and on the congrats content (StudyOptionsFragment.java:346-357). MISSING GATE MG329: the congrats button is shown only for a non-filtered deck with no cards due (lines 570-574). The custom study dialog callbacks are label_002 (DeckPicker) and label_007 (StudyOptionsActivity).')

# --- DeckTask ASYNC launch edges into the listener callback $3.onPostExecute (same pattern as label_019.py:43).

e('StudyOptionsFragment.onMenuItemClick', 'StudyOptionsFragment$3.onPostExecute', 'ASYNC',
  'the rebuild or empty cram task started from the toolbar finishes and calls its listener',
  env=None,
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:314-327, 503-504, 511; SRC com/ichi2/async/DeckTask.java:129, 358-365, 1306-1309',
  note='MISSING GATE MG325: the rebuild and empty items are visible only for a filtered deck (StudyOptionsFragment.java:346-348). Task types: TASK_TYPE_REBUILD_CRAM (line 318) and TASK_TYPE_EMPTY_CRAM (line 325). The launch CALL inside DeckTask.launchDeckTask (DeckTask.java:129) is not written here. needs_state unset.')

e('StudyOptionsFragment.refreshInterface(boolean,boolean)', 'StudyOptionsFragment$3.onPostExecute', 'ASYNC',
  'the update-values task started by the interface refresh finishes and calls its listener',
  env=None,
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:489-494, 511; SRC com/ichi2/async/DeckTask.java:77, 129, 358-365, 1306-1309',
  note='Task type TASK_TYPE_UPDATE_VALUES_FROM_DECK (23, DeckTask.java:77). The refresh is reached from onCreateView (line 190) and onResume (line 209), so no gate is needed. The launch CALL (DeckTask.java:129) is not written here.')

# --- Full new count thread (StudyOptionsFragment.java:618-641), gated by a deck with at least 1000 new cards.

e('StudyOptionsFragment$3.onPostExecute', 'StudyOptionsFragment$3$1.run', 'ASYNC',
  'the full new count thread starts when the deck has at least 1000 new cards (the count was truncated)',
  env=None,
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:608-618, 641; INFERRED JVM Thread.start (not in fw_src, source not read)',
  note='MISSING GATE MG324: totalNew must be at least NEW_CARD_COUNT_TRUNCATE_THRESHOLD = 1000 (StudyOptionsFragment.java:65, 608). This is a data state with no predefined STATE constant and it is not in the standard fixture. needs_state unset.')

e('StudyOptionsFragment$3$1.run', 'StudyOptionsFragment$3$1$1.run', 'ASYNC',
  'the count thread posts the full new count text to the new-cards view',
  env=None,
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:628-636; FW-SRC core/java/android/view/View.java:15777-15787; FW-SRC core/java/android/os/Handler.java:97, 355-357, 776-781, 789',
  note='MISSING GATE MG324 as in the thread start edge, and fullNewCount must be above 0 (StudyOptionsFragment.java:628). The post goes to the attach handler or to the run queue (View.java:15777-15787), and Handler dispatch runs it (Handler.java:97, 789).')

# --- UNREACHABLE entries.

# onActivityResult: the fragment is never a result target. Every startActivityForResult in this class is called on
# getActivity() (lines 152, 230, 300), and the request codes are small (BROWSE_CARDS=3, STATISTICS=4, DECK_OPTIONS=5,
# lines 53-55), so the support-library fragment index bits are zero. The host activities receive the results.
UNREACHABLE['StudyOptionsFragment.onActivityResult'] = ('framework_never_calls', 'the fragment is never a result target: every startActivityForResult in StudyOptionsFragment is called on getActivity() (lines 152, 230, 300), so results go to the host activity; the request codes are small (BROWSE_CARDS=3, STATISTICS=4, DECK_OPTIONS=5, lines 53-55), so the support-library fragment index bits are zero; the host activities handle their own results (StudyOptionsActivity.onActivityResult, DeckPicker.onActivityResult). INFERRED: support-library dispatch is not in fw_src (source not read).', 'SRC com/ichi2/anki/StudyOptionsFragment.java:53-55, 152, 230, 300, 393; SRC com/ichi2/anki/StudyOptionsActivity.java:83-91; SRC com/ichi2/anki/DeckPicker.java:634', 'INFERRED')

# closeStudyOptions: the only caller is onActivityResult (line 402), which is unreachable.
UNREACHABLE['StudyOptionsFragment.closeStudyOptions'] = ('framework_never_calls', 'the only caller is onActivityResult (line 402), and the framework never calls onActivityResult on this fragment (support-library result dispatch, INFERRED: source not read)', 'SRC com/ichi2/anki/StudyOptionsFragment.java:213-224, 401-403', 'INFERRED')

# setFragmentContentView: the only caller in the app tree is onActivityResult (line 444).
UNREACHABLE['StudyOptionsFragment.setFragmentContentView'] = ('framework_never_calls', 'the only caller in the app tree is onActivityResult (line 444), and the framework never calls onActivityResult on this fragment (support-library result dispatch, INFERRED: source not read)', 'SRC com/ichi2/anki/StudyOptionsFragment.java:279-283, 443-444', 'INFERRED')

# $3.onCancelled: no DeckTask of the three types used here is ever cancelled.
UNREACHABLE['StudyOptionsFragment$3.onCancelled'] = ('no_trigger_in_app', 'DeckTask.onCancelled calls the listener only after an AsyncTask cancel (DeckTask.java:368-370). The only DeckTask cancel path is cancelTask(int) (DeckTask.java:181-184), which cancels only when the latest task type matches; its callers pass SEARCH_CARDS and RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). The no-argument cancelTask() (DeckTask.java:168-178) is called only from cancelTask(int). The three task types this fragment launches (23 UPDATE_VALUES_FROM_DECK, 26 REBUILD_CRAM, 27 EMPTY_CRAM) are never cancelled. TaskOperations.stopTaskGracefully cancels a non-DeckTask task (TaskOperations.java:33).', 'SRC com/ichi2/anki/StudyOptionsFragment.java:668-670; SRC com/ichi2/async/DeckTask.java:77-80, 168-184, 368-370; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; SRC com/ichi2/anki/runtimetools/TaskOperations.java:33', 'SOURCE')

# $3.onProgressUpdate: none of the three task bodies calls publishProgress.
UNREACHABLE['StudyOptionsFragment$3.onProgressUpdate'] = ('no_trigger_in_app', 'the listener onProgressUpdate runs only when a task calls publishProgress (DeckTask.java:352-355). The publishProgress calls are in other task bodies (DeckTask.java:380, 420, 422, 457, 565, 601, 633, 659). None is in doInBackgroundUpdateValuesFromDeck (697-718), doInBackgroundRebuildCram (728-735) or doInBackgroundEmptyCram (736-743), the only three task types this fragment launches (TASK_TYPE_UPDATE_VALUES_FROM_DECK 23, TASK_TYPE_REBUILD_CRAM 26, TASK_TYPE_EMPTY_CRAM 27).', 'SRC com/ichi2/anki/StudyOptionsFragment.java:663-665; SRC com/ichi2/async/DeckTask.java:352-355, 380-659, 697-743', 'SOURCE')
