
# ---- W8 re-verification (Kiro, 2026-11-07, self-checked only, second: pending reviewer): all 30 sampled routes changed in
# the re-audit (tools_dev/route_diff.py AnkiDroid). The shared change is step 4: DeckPicker.onCreate now enters the deck list
# directly once the collection is open (DeckPicker.java:357, 415-417; the baseline collection opens), replacing the longer
# onResume/loader prefix. Each other new step was read in the source. Review 3 fix 4: a first verdict 'wrong' is kept; the
# re-check is in the note. Format: method -> (re-check result, note).
W8_RECHECK = {
    'Phrase.<init>': ('correct', 'New steps 4-7: deck list, the + button and Add note open the note editor (DeckPicker.java:463-485). The rest as before (sync env).'),
    'EasyX509TrustManager.<init>': ('correct', 'New steps 4-16: Sync in the options menu with no saved login shows the not-logged-in dialog (DeckPicker.java:1280-1282), its login button opens MyAccount, Log in starts the LOGIN connection task -> RemoteServer.hostKey -> HttpSyncer.req; the network env is on the route.'),
    'Stats$1.compare': ('correct', 'New steps 4-6: deck list and the drawer Statistics item (NavigationDrawerActivity, the base-class branch). The rest as before.'),
    'Sched._cntFnNew': ('correct', 'New steps 4-7: deck list, a deck tap -> handleDeckSelection -> Sched.reset (DeckPicker.java:195-207, 1736-1744). The rest as before.'),
    'libanki.Utils$1.<init>': ('correct', 'Only step 4 changed (the deck list entered from onCreate). The rest as before.'),
    'Sched.revDue': ('correct', 'New steps 4-7: deck list, a deck tap -> handleDeckSelection -> Sched.revDue (DeckPicker.java:195-207, 1744).'),
    'MediaCheckDialog$3.<init>': ('correct', 'New steps 4-7: deck list, Check media in the options menu -> showMediaCheckDialog -> MediaCheckDialog.newInstance -> <init>.'),
    'ModelEditorContextMenu.onCreateDialog': ('correct', 'New steps 4, 7, 10, 11: deck list; a note type tap in the note type list opens its field editor; a field row tap. The rest as before.'),
    'StudyOptionsActivity.closeStudyOptions(int)': ('correct', 'New steps 4-5: deck list and a tap on a deck with no cards to study opens the study options (DeckPicker.java:1695, 1736); Back closes them (steps 6-11 as before). The false step of the first verification is no longer on the route.'),
    'Finder.findNotes': ('correct', 'New steps 4-7: deck list, the + button and Add note open the note editor. The rest as before.'),
    'Template$1.compare': ('correct', 'New steps 4-12: deck list, a deck with cards opens the Reviewer, the collection loads and the first card is fetched (ANSWER_CARD task) and rendered (Card._getQA -> Collection._renderQA); the template state is on the route.'),
    'HttpFetcher.downloadFileToSdCardMethod': ('correct', 'New steps 4-7 and 13: deck list, Add note opens the note editor; the say button of a text field (BasicTextFieldController$2). The network env is on the route.'),
    'Sound.notifyConfigurationChanged': ('wrong', 'New steps 4-16: the deck list + button opens the note editor, and step 8 returns from it to AbstractFlashcardViewer.onActivityResult, then a playsound link plays a video (state: a card with a video). Not one real execution: the editor was started from DeckPicker, so its result does not reach the reviewer (shared S_NOTEEDITOR screen, Q-R5-2). The class (env: configuration change) is right either way.'),
    'Anki2Importer._mediaPick': ('correct', 'New steps 4, 7, 9, 14: deck list; Add in the import dialog (state: an .apkg in the AnkiDroid folder); the import task; _mungeMedia for notes with media. The rest as before.'),
    'Models.rem': ('correct', 'New steps 4 and 7: deck list; a long press on a note type opens its context menu. The rest as before.'),
    'Models$TransformFieldDelete.<init>': ('correct', 'New steps 4, 7, 10, 11: deck list; note type tap -> field editor -> field row tap. The rest as before.'),
    'Models$TransformFieldMove.<init>': ('correct', 'New steps 4, 7, 10, 11: deck list; note type tap -> field editor -> field row tap. The rest as before.'),
    'Models.validateBrackets': ('correct', 'New steps 4-9 and 15: deck list, Restore backup in the options menu -> its confirmation -> the backup list (DatabaseErrorDialog) -> restoreFromBackup -> importReplace (state: a backup or .apkg in the AnkiDroid folder; the app writes backups itself). The false step of the first verification is no longer on the route.'),
    'FullSyncer.syncURL': ('correct', 'New steps 4-17: Sync, the sync-conflict dialog keep-remote confirmation passes "download" (SyncErrorDialog.java:153), the full sync download request (network env, HttpSyncer.java:127, 152-236).'),
    'Sched.sortCards(long[],int,int,boolean,boolean)': ('correct', 'New steps 4-6: deck list, the options menu, the export dialog. The rest as before.'),
    'Sched.getToday': ('wrong', 'New steps 4-15: the deck list + button opens the note editor (DeckPicker.addNote), and step 8 returns from the editor to CardBrowser.onActivityResult. Not one real execution: the editor result goes back to the activity that started it (DeckPicker), and the graph joins every caller of the shared S_NOTEEDITOR screen (Q-R5-2). The class (gui) is right: the card browser opens the editor itself.'),
    'AdvancedStatistics$Card.setIvl': ('correct', 'New steps 4-6 and 17-25: deck list, the drawer Statistics item; the advancedStatistics hook and the review simulator carry the advanced-statistics setting state (Hooks.java:61).'),
    'DiffEngine.diff_cleanupSemanticScore': ('correct', 'New steps 4-5 and 13-16: deck list and the Reviewer; the typed-answer diff carries its state (a type-in field answered with a different text, AbstractFlashcardViewer.java:759-769).'),
    'UIUtils$1.onPostExecute': ('correct', 'Only steps 4 and 8 changed: deck list; the save-collection task delivers its result to the listener. The rest as before.'),
    'DB.insert': ('correct', 'New steps 4-14: deck list, a long press on a deck, Delete -> confirmDeckDeletion -> deleteDeck -> DELETE_DECK task -> Decks.rem logs the removal (Decks.java:296, unconditional except for the Default deck). The W8 read added three gates on the shorter routes it found first: empty cards (STATE data, DeckPicker.java:2181-2195), damaged notes in Check database (STATE file, Collection.java:1351-1409) and duplicate deck names in deckDueList (ENV other, Sched.java:386-408).'),
    'CollectionLoader.deliverResult': ('correct', 'New steps 4-7: deck list, a deck with cards opens the Reviewer, whose onCreate starts the collection loader. The rest as before.'),
    'Decks.id(String,boolean)': ('correct', 'New steps 4-6: deck list, + -> New deck -> OK in the name dialog -> Decks.id (DeckPicker.java:463-485).'),
    'Collection.getServer': ('wrong', 'New steps 4-11: DeckPicker.onCreate -> showStartupScreensAndDialogs -> getCol -> CollectionHelper.getCol -> Storage.Collection -> Media.connect -> getServer. Still not one real execution: showStartupScreensAndDialogs runs only after the collection is open (guard firstCollectionOpen), while CollectionHelper.getCol opens the collection only when it is not open (CollectionHelper.java:88); the real first open is earlier in onCreate. The class (gui) is right either way.'),
    'SimpleMessageDialog.<init>': ('correct', 'New steps 4-9: deck list, Empty cards in the options menu; on the baseline the search finds none and the no-empty-cards message is shown (DeckPicker.java:2182-2183). The W8 read added the unused-media state to the Delete unused button (MediaCheckDialog.java:114-128), which moved the earlier route.'),
    'AnkiActivity.openUrl': ('correct', 'New steps 4-6: deck list, select an empty deck and tap Help in the snackbar (DeckPicker.java:1769-1778). The rest as before.'),
}
assert set(W8_RECHECK) == set(sample), ('W8 rows != sample', sorted(set(sample) ^ set(W8_RECHECK)))
for _m, (_rc, _n) in W8_RECHECK.items():
    _first = VERDICT[_m]
    NOTE[_m] = 'W8 re-verified 2026-11-07 (first verification: %s; re-check: %s). %s Earlier: %s' % (_first, _rc, _n, NOTE[_m])
    if _first not in ('wrong', 'fixed'):
        VERDICT[_m] = _rc
