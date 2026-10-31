# ---- batch 093: WatchlistFragment anonymous listeners $3 to $9 (15 methods; rows in label_093.md, evidence in label_093.grep.txt)
# Edges are written only for destinations owned by this batch (D1). The <init> methods have auto CALL records in auto_calls.json, so no edge is written for them (D7).
# SCREENS: none written here. S_WATCHLIST is defined by batch 092 (label_092.py:7) and reused for the page of these listeners.
# UNREACHABLE entries: none (all 15 methods are REACHABLE). sup pairs: none. The sup for WatchlistFragment$4.onClick -> SecurityPriceUpdaterBase.downloadPrices is in label_091.py:41.
# Mapping of the anonymous class numbers to the listeners rests on the class-file refs (grep.txt section 1), not on the auto_calls line numbers, which differ by one or more lines from the new expressions (grep.txt sections 2 and 3).

# ---- the two confirmation dialogs opened from the options menu (D9: shown on the watchlist page)

gui('S_WATCHLIST', 'WatchlistFragment$3.onClick',
    'Tap Update prices in the options menu, then Cancel in the confirmation dialog',
    cls='non_standard',
    via='platform AlertDialog negative button: AlertController ButtonHandler sends the click to the OnClickListener (FW-SRC AlertController.java:125-145, 160-166; setButton 344-360)',
    evidence='SRC investment/watchlist/WatchlistFragment.java:478-483 (setNegativeButton at 478; onClick 480-482; dismiss 481); SRC res/menu/menu_watchlist.xml:22-26 (menu_update_prices); SRC WatchlistFragment.java:258 (confirmPriceUpdate); class file WatchlistFragment$3 refs DialogInterface.dismiss only (grep.txt section 1)')

gui('S_WATCHLIST', 'WatchlistFragment$4.onClick',
    'Tap Update prices in the options menu, then OK in the confirmation dialog (downloads the prices of the shown securities)',
    cls='non_standard',
    via='platform AlertDialog positive button: same dispatch as the Cancel button (AlertController.java:160-166)',
    evidence='SRC WatchlistFragment.java:463-477 (setPositiveButton at 463; onClick 465-476; getAllShownSymbols 467; getUpdaterInstance 473; downloadPrices 474); SRC res/menu/menu_watchlist.xml:22-26; auto_calls.json records WatchlistFragment$4.onClick -> getAllShownSymbols (467), getUpdaterInstance (473), downloadPrices (474, cha); class file WatchlistFragment$4 refs downloadPrices (grep.txt sections 1-2)')

# ---- the account spinner in the action bar (a standard AdapterView selection, as in AccountTransactionListFragment$3.onItemSelected, graph_def.py:1155)

gui('S_WATCHLIST', 'WatchlistFragment$5.onItemSelected',
    'Pick an investment account in the account spinner of the action bar',
    evidence='SRC investment/watchlist/WatchlistFragment.java:514-538 (action bar 514; spinner 522; setOnItemSelectedListener 530; onItemSelected 532-539, switchAccount at 538); FW-SRC core/java/android/widget/AdapterView.java:903-930 (selectionChanged), 937-949 (fireOnSelected calls onItemSelected at 944)')

e('WatchlistFragment.selectCurrentAccount', 'WatchlistFragment$5.onItemSelected', 'FRAMEWORK',
  'selectCurrentAccount selects the row of the current account (spinner.setSelection at line 671); when the selected row changes, the framework calls onItemSelected for the new row, which calls switchAccount (switchAccount returns early at line 675 when the account is unchanged)',
  guard='the current account is a row of the spinner (loop at 659-669), and its position differs from the previous selection (AdapterView.java:1104-1106)',
  evidence='SRC investment/watchlist/WatchlistFragment.java:650-672 (position loop 659-669; setSelection 671), 674-675 (switchAccount early return); FW-SRC core/java/android/widget/AdapterView.java:1103-1115 (checkSelectionChanged; selectionChanged at 1105), 937-949 (fireOnSelected; onItemSelected at 944); AbsSpinner.java is not in fw_src (the path from setSelection to checkSelectionChanged is INFERRED)')

e('WatchlistFragment.selectCurrentAccount', 'WatchlistFragment$5.onNothingSelected', 'FRAMEWORK',
  'selectCurrentAccount finds no row for the current account, so position stays Constants.NOT_SET (-1) and spinner.setSelection(-1) clears the selected row; the framework then calls onNothingSelected (empty body)',
  needs_state=state_text('the spinner had a valid selected row before this call (the framework fires onNothingSelected only when the selection changes to none), and the current account is not one of its rows (WatchlistFragment.java:659-669)', ('account',)),
  evidence='SRC investment/watchlist/WatchlistFragment.java:541-544 (empty onNothingSelected), 659 (position = NOT_SET), 661-669 (row loop), 671 (setSelection); FW-SRC core/java/android/widget/AdapterView.java:937-949 (fireOnSelected calls onNothingSelected for a negative position, at 947), 1103-1115 (checkSelectionChanged fires only on a change, 1104-1106), 1086-1093 (nothing-selected branch in handleDataChanged, checkSelectionChanged at 1093); Constants.java:22 (NOT_SET = -1); AbsSpinner.java is not in fw_src, so the setSelection(-1) to checkSelectionChanged path is INFERRED')

# ---- the account header (favourite star and goto icon); the header row is hidden for all accounts (switchAccount, lines 694-700)

gui('S_WATCHLIST', 'WatchlistFragment$6.onClick',
    'Tap the favourite star (R.id.imageViewAccountFav) in the account header of the watchlist',
    needs_state=state_text('an investment account is selected: switchAccount hides the header row (headerRow GONE) for all accounts (NOT_SET) and shows it otherwise (WatchlistFragment.java:694-700)', ('account',)),
    evidence='SRC investment/watchlist/WatchlistFragment.java:554-569 (favourite listener; setFavorite 556, save 559, setImageViewFavorite 566), 694-700 (headerRow GONE at 694, VISIBLE at 700); SRC res/layout/fragment_watchlist_header.xml:27 (headerRow, no android:visibility), 78 (imageViewAccountFav); auto_calls.json records WatchlistFragment$6.onClick -> Account.setFavorite (556), AccountRepository.save (559), setImageViewFavorite (566, access$600)')

gui('S_WATCHLIST', 'WatchlistFragment$7.onClick',
    'Tap the goto-account icon (R.id.imageViewGotoAccount) in the watchlist header',
    needs_state=state_text('an investment account is selected: switchAccount hides the header row (headerRow GONE) for all accounts (NOT_SET) and shows it otherwise (WatchlistFragment.java:694-700)', ('account',)),
    evidence='SRC investment/watchlist/WatchlistFragment.java:573-581 (goto listener; intent 576, putExtra 577, setAction 578, startActivity 579), 694-700; SRC res/layout/fragment_watchlist_header.xml:69 (imageViewGotoAccount); auto_calls.json record WatchlistFragment$7.onClick -> getAccountId (577, access$700); the INTENT edge from this method to AccountEditActivity.<init> is written by batch 006 (label_006.py:30-33), not here')

# ---- the purge-history dialog (menu_purge_history, WatchlistFragment.java:264)

gui('S_WATCHLIST', 'WatchlistFragment$8.onClick',
    'Tap Purge price history in the options menu, then Cancel in the confirmation dialog',
    cls='non_standard',
    via='platform AlertDialog negative button: same dispatch as WatchlistFragment$3.onClick (AlertController.java:160-166)',
    evidence='SRC investment/watchlist/WatchlistFragment.java:638-643 (setNegativeButton at 638; onClick 640-642; dismiss 641); SRC res/menu/menu_watchlist.xml:32-36 (menu_purge_history); SRC WatchlistFragment.java:264 (purgePriceHistory); class file WatchlistFragment$8 refs DialogInterface.dismiss only (grep.txt section 1)')

gui('S_WATCHLIST', 'WatchlistFragment$9.onClick',
    'Tap Purge price history in the options menu, then OK in the confirmation dialog',
    cls='non_standard',
    via='platform AlertDialog positive button: same dispatch as WatchlistFragment$4.onClick (AlertController.java:160-166)',
    evidence='SRC investment/watchlist/WatchlistFragment.java:618-636 (setPositiveButton at 618; onClick 620-636; deleteAllPriceHistory 622; SyncManager.dataChanged 625; dismiss 635); SRC res/menu/menu_watchlist.xml:32-36; auto_calls.json records WatchlistFragment$9.onClick -> StockHistoryRepository.deleteAllPriceHistory (622), SyncManager.dataChanged (625); class file WatchlistFragment$9 refs deleteAllPriceHistory and dataChanged (grep.txt sections 1-2)')
