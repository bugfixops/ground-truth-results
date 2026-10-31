# AnkiDroid batch 008 (LABEL helper). Reviewer activity: lifecycle, options menu, whiteboard, bury/suspend submenus, activity results.
# Edges written here have a source method in batch 008, or a page source (S_DECKPICKER, S_REVIEWER, S_NOTEEDITOR, S_CARDBROWSER,
# S_DECKOPTIONS, S_STATISTICS) whose destination is in batch 008 (coordinator rule 1). Routes through other batches' nodes are cited in
# graphs/AnkiDroid/parts/label_008.md.
# No UNREACHABLE entries: all 34 batch methods have a route. Some routes need a setting (customButtonAddCard, customButtonBury,
# customButtonSuspend) or a note state; those are set on the edge.
# Missing gates (notes only, env and needs_state unset): MG24 per-deck whiteboard state (MetaDB), MG25 note with two or more cards,
# MG26 filtered deck hides the deck options item.
# ActionProvider callbacks (hasSubMenu, onCreateActionView, onPrepareSubMenu, onMenuItemClick) come from the support library, which is
# not in fw_src; their routes are confirmed_by INFERRED.

e('S_DECKPICKER', 'Reviewer.<init>', 'INTENT',
  'the user taps a deck that has cards to study, and the Reviewer opens',
  needs_state=STATE_CARDS,
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:2128-2131; SRC com/ichi2/anki/Reviewer.java:56',
  note='Page edge; the destination is in batch 008, so this part writes it. Shortcut: the route passes DeckPicker.openReviewer (batch_003), whose INTENT edge DeckPicker.openReviewer -> Reviewer.<init> is not in label_003.py. batch_003 should add that edge; both routes end at the same method, so there is no conflict.')

e('Reviewer.onOptionsItemSelected', 'DeckOptions.<init>', 'INTENT',
  'the user taps Deck options in the Reviewer menu',
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:208-211; SRC com/ichi2/anki/AbstractFlashcardViewer.java:1759',
  note='MISSING GATE MG26: the item is hidden for a filtered deck (Reviewer.java:302-304, Decks.isDyn), and no STATE models a filtered deck, so needs_state is unset. customButtonDeckOptions defaults to 0, which shows the item in the menu, so no setting gate applies.')

e('Reviewer.addNote', 'NoteEditor.<init>', 'INTENT',
  'the user taps Add note in the Reviewer menu, when the item is shown',
  needs_state=STATE_SETTINGS,
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:230-234, 237-244; SRC com/ichi2/anki/AbstractFlashcardViewer.java:173, 1754',
  note='customButtonAddCard defaults to 3 (MENU_DISABLED, AbstractFlashcardViewer.java:173). setCustomButtons hides action_add_note_reviewer when the value is 3 (Reviewer.java:239-244), so the route needs the preference set to 0, 1 or 2. The intent carries EXTRA_CALLER = CALLER_REVIEWER_ADD (Reviewer.java:232).')

e('Reviewer.openCardBrowser', 'CardBrowser.<init>', 'INTENT',
  'the user taps Browse cards in the navigation drawer while studying',
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:508-517; SRC com/ichi2/anki/NavigationDrawerActivity.java:262-263',
  note='The CALL edge NavigationDrawerActivity.onNavigationItemSelected -> Reviewer.openCardBrowser is owned by batch_036 (NavigationDrawerActivity.java:262-263). The request code is REQUEST_BROWSE_CARDS (Reviewer.java:517).')

e('S_NOTEEDITOR', 'Reviewer.onActivityResult', 'RESULT',
  'the note editor, opened from the Reviewer to add a note, returns',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:960-963; SRC com/ichi2/anki/Reviewer.java:61, 232-233, 533-547',
  note='Page edge; the destination is in batch 008. The request code is ADD_NOTE (Reviewer.java:61, 233). Other NoteEditor callers return to their own activities (not this batch).')

e('S_CARDBROWSER', 'Reviewer.onActivityResult', 'RESULT',
  'the card browser, opened from the Reviewer, returns',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:1132; SRC com/ichi2/anki/Reviewer.java:517, 533-547',
  note='Page edge; the destination is in batch 008. The request code is REQUEST_BROWSE_CARDS (Reviewer.java:534). The result data carries allDecksSelected and originalDeck, which Reviewer.onActivityResult reads (Reviewer.java:536-544).')

e('S_DECKOPTIONS', 'Reviewer.onActivityResult', 'RESULT',
  'the deck options screen, opened from the Reviewer menu, returns',
  env=None,
  evidence='SRC com/ichi2/anki/DeckOptions.java:590-593; SRC com/ichi2/anki/Reviewer.java:208-211, 533-547',
  note='Page edge; the destination is in batch 008. The request code is DECK_OPTIONS (Reviewer.java:210). Reviewer.onActivityResult passes it to super (546), which handles the request code (AbstractFlashcardViewer.java:1080-1088).')

e('S_STATISTICS', 'Reviewer.onActivityResult', 'RESULT',
  'the statistics screen, opened from the navigation drawer while studying, returns',
  env=None,
  evidence='SRC com/ichi2/anki/Statistics.java:708; SRC com/ichi2/anki/NavigationDrawerActivity.java:265-268; SRC com/ichi2/anki/Reviewer.java:533-547',
  note='Page edge; the destination is in batch 008. The request code is REQUEST_STATISTICS (NavigationDrawerActivity.java:265-268). Reviewer.onActivityResult stores the selected deck and restores originalDeck (Reviewer.java:534-544).')

e('S_REVIEWER', 'Reviewer.onCreateOptionsMenu', 'FRAMEWORK',
  'the Reviewer shows its options menu, and again after each invalidateOptionsMenu (each new question)',
  env=None,
  evidence='FW-SRC core/java/android/app/Activity.java:3386-3388; FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:631; SRC com/ichi2/anki/Reviewer.java:251-255',
  note='The framework calls onCreatePanelMenu, which calls onCreateOptionsMenu. Reviewer.java:252 says it runs on every new question. The menu build also creates the Suspend and Bury providers (Reviewer.java:310-311).')

e('S_REVIEWER', 'Reviewer.onWindowFocusChanged', 'FRAMEWORK',
  'the Reviewer window gains or loses focus (a dialog, system UI, or returning to the app)',
  env=None,
  evidence='FW-SRC core/java/com/android/internal/policy/DecorView.java:1559-1571; FW-SRC core/java/android/app/Activity.java:3157-3159, 6938; SRC com/ichi2/anki/Reviewer.java:522-530',
  note='DecorView calls the window callback (DecorView.java:1571), which is the Activity (Activity.attach sets the callback at Activity.java:6938). Activity.onWindowFocusChanged runs first, then this override.')

e('S_REVIEWER', 'Reviewer$BuryProvider.hasSubMenu', 'FRAMEWORK',
  'the Bury item is shown or tapped, and the support library asks whether it has a dropdown',
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:159-165, 629-631 (in-app call at 161)',
  note='INFERRED: ActionProvider is a support-library class and is not in fw_src. The in-app call at Reviewer.java:161 is a virtual call on the ActionProvider type and is not in auto_calls.json, so this page edge carries the route. hasSubMenu returns dismissNoteAvailable(BURY_NOTE) (Reviewer.java:630).')

e('S_REVIEWER', 'Reviewer$SuspendProvider.hasSubMenu', 'FRAMEWORK',
  'the Suspend item is shown or tapped, and the support library asks whether it has a dropdown',
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:167-173, 587-589 (in-app call at 169)',
  note='INFERRED: same reason as the Bury edge (support-library ActionProvider, not in fw_src). hasSubMenu returns dismissNoteAvailable(SUSPEND_NOTE) (Reviewer.java:588).')

e('S_REVIEWER', 'Reviewer$BuryProvider.onCreateActionView', 'FRAMEWORK',
  'the Bury item is shown as an action-bar button (customButtonBury is 1 or 2)',
  needs_state=STATE_SETTINGS,
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:624-626; SRC com/ichi2/anki/AbstractFlashcardViewer.java:1760; SRC com/ichi2/anki/Reviewer.java:237-246',
  note='INFERRED: the support library creates the action view. customButtonBury defaults to 0 (never shown as an action, AbstractFlashcardViewer.java:1760), so the route needs the preference set to 1 or 2. The method returns null (Reviewer.java:625).')

e('S_REVIEWER', 'Reviewer$SuspendProvider.onCreateActionView', 'FRAMEWORK',
  'the Suspend item is shown as an action-bar button (customButtonSuspend is 1 or 2)',
  needs_state=STATE_SETTINGS,
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:582-584; SRC com/ichi2/anki/AbstractFlashcardViewer.java:1761; SRC com/ichi2/anki/Reviewer.java:237-246',
  note='INFERRED: same reason as the Bury edge. customButtonSuspend defaults to 0 (never shown as an action, AbstractFlashcardViewer.java:1761), so the route needs the preference set to 1 or 2.')

e('S_REVIEWER', 'Reviewer.onOptionsItemSelected', 'GUI',
  'the user taps an item in the Reviewer action bar or overflow menu',
  gui=['the user taps an item in the Reviewer action bar or overflow menu'],
  env=None,
  evidence='FW-SRC core/java/android/app/Activity.java:3440-3450; SRC com/ichi2/anki/Reviewer.java:125-127',
  note='Page edge; the destination is in batch 008. Activity.onMenuItemSelected calls onOptionsItemSelected (Activity.java:3450). The default case calls AnkiActivity.onOptionsItemSelected (Reviewer.java:224).')

e('S_REVIEWER', 'Reviewer.onKeyUp', 'GUI',
  'the user releases a key while the Reviewer is on screen',
  gui=['the user releases a key while the Reviewer is on screen'],
  env=None,
  evidence='FW-SRC core/java/android/app/Activity.java:2975; SRC com/ichi2/anki/Reviewer.java:331-333, 391',
  note='Page edge. The body acts only when the answer field exists and is not focused (Reviewer.java:333); other keys fall through to super (391). No ENV models keyboard input, so env is unset.')

e('S_REVIEWER', 'Reviewer$1.onTouch', 'GUI',
  'the user touches the whiteboard area while it is on screen',
  gui=['the user touches the whiteboard area while it is on screen'],
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:461-471',
  note='MISSING GATE MG24: the whiteboard is on per deck (MetaDB state, Reviewer.java:103 and 446). No STATE models it, so needs_state is unset. The listener is registered in createWhiteboard (Reviewer.java:461), which runs when the whiteboard is enabled (448).')

e('S_REVIEWER', 'Reviewer$BuryProvider.onPrepareSubMenu', 'GUI',
  'the user taps Bury in the Reviewer menu and the bury dropdown opens',
  gui=['the user taps Bury in the Reviewer menu and the bury dropdown opens'],
  needs_state=STATE_NOTE,
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:159-161, 630, 634-640',
  note='INFERRED: the support library calls onPrepareSubMenu after hasSubMenu returns true. MISSING GATE MG25: the dropdown needs a note with two or more cards (Reviewer.java:556 and 559-568). No STATE models the sibling count, so only STATE_NOTE is set.')

e('S_REVIEWER', 'Reviewer$BuryProvider.onMenuItemClick', 'GUI',
  'the user taps Bury card or Bury note in the bury dropdown',
  gui=['the user taps Bury card or Bury note in the bury dropdown'],
  needs_state=STATE_NOTE,
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:636-639, 643-654',
  note='Page edge. The entries are added and registered by onPrepareSubMenu (REGISTER edge below), and REGISTER is not followed for reachability, so this page edge carries the route. MISSING GATE MG25 as on the Bury onPrepareSubMenu edge.')

e('S_REVIEWER', 'Reviewer$SuspendProvider.onPrepareSubMenu', 'GUI',
  'the user taps Suspend in the Reviewer menu and the suspend dropdown opens',
  gui=['the user taps Suspend in the Reviewer menu and the suspend dropdown opens'],
  needs_state=STATE_NOTE,
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:167-169, 588, 592-598',
  note='INFERRED: the support library calls onPrepareSubMenu after hasSubMenu returns true. MISSING GATE MG25: the dropdown needs a note with two or more cards (Reviewer.java:556 and 559-564). No STATE models the sibling count, so only STATE_NOTE is set.')

e('S_REVIEWER', 'Reviewer$SuspendProvider.onMenuItemClick', 'GUI',
  'the user taps Suspend card or Suspend note in the suspend dropdown',
  gui=['the user taps Suspend card or Suspend note in the suspend dropdown'],
  needs_state=STATE_NOTE,
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:594-597, 601-612',
  note='Page edge. The entries are added and registered by onPrepareSubMenu (REGISTER edge below). MISSING GATE MG25 as on the Suspend onPrepareSubMenu edge.')

e('Reviewer$1.<init>', 'Reviewer$1.onTouch', 'REGISTER',
  'the whiteboard touch listener is set on the whiteboard view',
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:461-471',
  note='Same convention as label_003.py line 93 (DeckPicker$1.<init> -> DeckPicker$1.onClick). Not followed for reachability.')

e('Reviewer$BuryProvider.onPrepareSubMenu', 'Reviewer$BuryProvider.onMenuItemClick', 'REGISTER',
  'each bury dropdown entry is given this provider as its click listener',
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:636-639',
  note='Registration only (setOnMenuItemClickListener). Not followed for reachability; the GUI page edge above carries the route.')

e('Reviewer$SuspendProvider.onPrepareSubMenu', 'Reviewer$SuspendProvider.onMenuItemClick', 'REGISTER',
  'each suspend dropdown entry is given this provider as its click listener',
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:594-597',
  note='Registration only (setOnMenuItemClickListener). Not followed for reachability; the GUI page edge above carries the route.')
