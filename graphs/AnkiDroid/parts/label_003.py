# AnkiDroid batch 003 (LABEL helper). DeckPicker lifecycle, options menu, undo, sync, dialog entry points.
# Edges written here have a source method in batch 003, or a page source (S_DECKPICKER) whose destination is in batch 003
# (coordinator rule 1). Routes through other batches' nodes are cited in graphs/AnkiDroid/parts/label_003.md.
# No UNREACHABLE entries: all 40 batch methods have a route from S_ENTRY.
# Missing gates are notes only (MISSING GATE ...); env and needs_state are unset on those edges.
# Lifecycle edges (DeckPicker.onResume/onPause/onStop) come from the lc_chain in graph_def.py line 176 and are not repeated here.

e('S_DECKPICKER', 'DeckPicker.onPrepareOptionsMenu', 'GUI',
  'the user opens the options menu of the deck list',
  gui=['the user opens the options menu of the deck list'],
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:505; FW-SRC core/java/android/app/Activity.java:3404-3406',
  note='Page edge; the destination is in batch 003, so this part writes it. The framework calls onPrepareOptionsMenu through onPreparePanel.')

e('S_DECKPICKER', 'DeckPicker.openCardBrowser', 'GUI',
  'the user taps Browse in the navigation drawer',
  gui=['the user taps Browse in the navigation drawer'],
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1708; SRC com/ichi2/anki/NavigationDrawerActivity.java:262-263',
  note='NavigationDrawerActivity (batch_036) also reaches this override by virtual dispatch at line 263; this page edge is the DeckPicker route.')

e('S_DECKPICKER', 'DeckPicker.openReviewer', 'GUI',
  'the user taps a deck that has cards to study',
  gui=['the user taps a deck that has cards to study'],
  needs_state=STATE_CARDS,
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:2128, 1739',
  note='handleDeckSelection (batch_002) calls openReviewer at line 1739 for a deck with cards.')

e('S_DECKPICKER', 'DeckPicker.openStudyOptions', 'GUI',
  'the user taps a deck without cards to study',
  gui=['the user taps a deck without cards to study'],
  needs_state=STATE_DECK,
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1695, 1736',
  note='handleDeckSelection (batch_002) calls openStudyOptions(false) at lines 1736, 1743, 1768, 1780 and 1796.')

e('S_DECKPICKER', 'DeckPicker.undo', 'GUI',
  'the user taps Undo in the options menu',
  gui=['the user taps Undo in the options menu'],
  evidence='SRC com/ichi2/anki/DeckPicker.java:996, 511, 551-553',
  note='MISSING GATE MG2: undo available. The Undo item is visible only when getCol().undoAvailable() is true (DeckPicker.java:511-517). env and needs_state unset.')

e('S_DECKPICKER', 'DeckPicker.sync()', 'GUI',
  'the user taps Sync in the options menu',
  gui=['the user taps Sync in the options menu'],
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1266, 556-558',
  note='No gate is needed to reach sync(); the offline case changes only the outcome (MISSING GATE MG4 is noted on the sync(String) ASYNC edge).')

e('S_DECKPICKER', 'DeckPicker.showImportDialog(int)', 'GUI',
  'the user taps Import in the options menu',
  gui=['the user taps Import in the options menu'],
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1088, 561-563',
  note='showImportDialog(int) delegates to showImportDialog(int,String) at line 1089.')

e('S_DECKPICKER', 'DeckPicker.showMediaCheckDialog(int)', 'GUI',
  'the user taps Check media in the options menu',
  gui=['the user taps Check media in the options menu'],
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1033, 600-602',
  note='Options menu action_check_media case (DeckPicker.java:600-602).')

e('S_DECKPICKER', 'DeckPicker$1.onClick', 'GUI',
  'the user taps the expander arrow next to a deck',
  gui=['the user taps the expander arrow next to a deck'],
  evidence='SRC com/ichi2/anki/DeckPicker.java:183-187',
  note='MISSING GATE (unnumbered): deck has subdecks. The listener only acts when children exist (DeckPicker.java:185). env and needs_state unset.')

e('DeckPicker.onPause', 'DeckPicker.onSaveInstanceState', 'FRAMEWORK',
  'the framework saves the activity state after onPause and before onStop',
  evidence='SRC com/ichi2/anki/DeckPicker.java:716; FW-SRC core/java/android/app/ActivityThread.java:4023-4025',
  note='MISSING GATE (unnumbered): activity not finishing (ActivityThread saves only when !mFinished and saveState). env and needs_state unset.')

e('DeckPicker.updateDeckList', 'DeckPicker$22.onPostExecute', 'ASYNC',
  'the deck-count load task finishes and calls its listener',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1823, 1834',
  note='Listener DeckPicker$22 is in batch_005. onPostExecute calls scrollDecklistToDeck at DeckPicker.java:1868.')

e('DeckPicker.undo', 'DeckPicker$13.onPostExecute', 'ASYNC',
  'the undo task finishes and calls its listener',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:999, 1011-1014',
  note='Listener DeckPicker$13 is in batch_004. The route into undo carries MG2 (see the S_DECKPICKER -> DeckPicker.undo edge).')

e('DeckPicker.sync(String)', 'DeckPicker$17.onPostExecute', 'ASYNC',
  'the sync task finishes and calls its listener',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1284, 1291, 1404',
  note='MISSING GATE MG4: offline. The onDisconnected branch (DeckPicker.java:1299) shows the offline message. env and needs_state unset.')

e('DeckPicker$1.<init>', 'DeckPicker$1.onClick', 'REGISTER',
  'the expander click listener is registered with the deck list',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:181, 183',
  note='The builder does not follow REGISTER for reachability (see label_001.py note); the route to onClick is the S_DECKPICKER -> DeckPicker$1.onClick edge.')

e('DeckPicker$10.<init>', 'DeckPicker$10.onClick', 'REGISTER',
  'the add-shared FAB click listener is registered',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:488, 492',
  note='onClick is in batch_004. The builder does not follow REGISTER for reachability.')
