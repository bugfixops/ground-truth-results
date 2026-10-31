# ---- batch 094: WatchlistItemsFragment (27 methods), its listeners WatchlistItemsFragment$1, $2 and $3 (6 methods), and WatchlistViewHolder.<init> (1 method): 34 methods.
# Rows and printed lines: graphs/MMEX/parts/label_094.md. Grep and sed evidence: graphs/MMEX/parts/label_094.grep.txt (sections A-G).
# Edges are written only for destinations that this batch owns (D1). CALL edges already in auto_calls.json are not repeated (D7).
# Page key: S_WATCHLIST is defined in label_092.py:7 (SCREENS.update) and reused here (D9). No new key is defined in this part.
# UNREACHABLE entries: none. All 34 methods are REACHABLE.
# sup pairs: none written (no UNREACHABLE caller in this batch, D14). The merged sup pair at graph_def.py:3786 (BaseListFragment$2.onClick -> WatchlistItemsFragment.onFloatingActionButtonClicked) stays as it is; it cuts the plain CALL, so the GUI edge below is the route to onFloatingActionButtonClicked.
# Not repeated (already merged): graph_def.py:7386 (WatchlistItemsFragment.openEditInvestmentActivity -> InvestmentTransactionEditActivity.<init>, INTENT, batch 086) and graph_def.py:7631 (WatchlistItemsFragment.onContextItemSelected -> PriceEditActivity.<init>, INTENT, batch 088).
# Edges written: 16 (LIFECYCLE 6, FRAMEWORK 4, GUI 5 from S_WATCHLIST, RESULT 1).

# ---- fragment lifecycle (androidx Fragment; library source not read: INFERRED)

e('WatchlistItemsFragment.<init>', 'WatchlistItemsFragment.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the implicit default constructor (reached from newInstance)',
  evidence='SRC investment/watchlist/WatchlistItemsFragment.java:77-79 (no constructor declared), 88-91 (newInstance); INFERRED androidx Fragment lifecycle (library source not read)')

e('WatchlistItemsFragment.onCreate', 'WatchlistItemsFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate (onCreate reads accountId from the saved state or the arguments, lines 109-113)',
  evidence='SRC WatchlistItemsFragment.java:103-115, 117-123; INFERRED androidx Fragment lifecycle (library source not read)')

e('WatchlistItemsFragment.onCreateView', 'WatchlistItemsFragment.onActivityCreated', 'LIFECYCLE',
  'the framework calls onActivityCreated after onCreateView (the layout is inflated at line 120)',
  evidence='SRC WatchlistItemsFragment.java:117-127; INFERRED androidx Fragment lifecycle (library source not read)')

e('WatchlistItemsFragment.onActivityCreated', 'WatchlistItemsFragment.onSaveInstanceState', 'LIFECYCLE',
  'approximation: the host activity saves the fragment state before it stops (ActivityThread), and no app method calls this; the edge stands in for the live fragment state after onActivityCreated (same pattern as batch 087)',
  evidence='SRC WatchlistItemsFragment.java:126-174, 348-353; FW-SRC core/java/android/app/ActivityThread.java:4022-4025 (callCallActivityOnSaveInstanceState before the stop); INFERRED androidx state save (library source not read)')

e('WatchlistItemsFragment.onSaveInstanceState', 'WatchlistItemsFragment.onStop', 'LIFECYCLE',
  'the activity stops after its state is saved (ActivityThread saves the state before performStop), so the fragment gets onStop',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:4022-4032 (state save at 4025, performStop at 4032); SRC WatchlistItemsFragment.java:355-372; INFERRED androidx dispatchStop (library source not read)')

e('WatchlistItemsFragment.onStop', 'WatchlistItemsFragment.onDestroy', 'LIFECYCLE',
  'the framework calls onDestroy after onStop when the fragment is removed or the host activity finishes',
  evidence='SRC WatchlistItemsFragment.java:274-277, 355-357; INFERRED androidx Fragment lifecycle (library source not read)')

# ---- loader callbacks (LoaderManager, androidx; library source not read: INFERRED)

e('WatchlistItemsFragment.reloadData', 'WatchlistItemsFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader creates the loader for ID_LOADER and calls the LoaderCallbacks (this fragment) through onCreateLoader',
  evidence='SRC WatchlistItemsFragment.java:386-393 (restartLoader with this as the callbacks, line 392); INFERRED androidx LoaderManager.restartLoader (library source not read)')

e('WatchlistItemsFragment.onCreateLoader', 'WatchlistItemsFragment.onLoadFinished', 'FRAMEWORK',
  'the loader runs its query and delivers the cursor to onLoadFinished',
  evidence='SRC WatchlistItemsFragment.java:282-314 (MmxCursorLoader at 309), 323-341; INFERRED androidx loader delivery (library source not read)')

e('WatchlistItemsFragment.onLoadFinished', 'WatchlistItemsFragment.onLoaderReset', 'FRAMEWORK',
  'the loader manager resets a loader that has delivered data (for example when restartLoader replaces it)',
  guard='onLoaderReset is called only for a loader whose data was delivered by onLoadFinished (INFERRED androidx LoaderInfo)',
  evidence='SRC WatchlistItemsFragment.java:316-321 (body), 323-341; INFERRED androidx LoaderManager reset (library source not read)')

e('WatchlistItemsFragment$1.onItemClick', 'WatchlistItemsFragment.onCreateContextMenu', 'FRAMEWORK',
  'a row tap calls getActivity().openContextMenu(view); the framework builds the menu by calling the fragment, which registered itself as the context menu listener (line 165)',
  evidence='SRC WatchlistItemsFragment.java:140-150 (openContextMenu at 147), 165 (registerForContextMenu); FW-SRC core/java/android/app/Activity.java:3791-3793 (openContextMenu -> view.showContextMenu()); core/java/android/view/View.java:6448-6449 (showContextMenu), 12578-12588 (createContextMenu calls the listener at 12588); core/java/android/view/ViewGroup.java:860-866; INFERRED root step (ViewRootImpl not read) and registerForContextMenu (androidx, not read)')

# ---- the result of the price editor (PriceEditActivity, batch 088)

e('PriceEditActivity.onOptionsItemSelected', 'WatchlistItemsFragment.onActivityResult', 'RESULT',
  'the price editor saves and finishes with RESULT_OK; the platform delivers the result to the fragment that started it (request code RequestCodes.PRICE)',
  guard='requestCode == RequestCodes.PRICE (line 180) and resultCode == RESULT_OK (line 181); the editor was started at line 253 with RequestCodes.PRICE',
  evidence='SRC investment/PriceEditActivity.java:111-126 (save 120, setResult 121, finish 122); SRC investment/watchlist/WatchlistItemsFragment.java:176-185, 253; FW-SRC core/java/android/app/Activity.java:7259-7284 (dispatchActivityResult to the fragment); INFERRED fragment routing by request prefix (androidx, not read)')

# ---- page-to-method GUI edges from S_WATCHLIST (the watchlist screen; key from label_092.py:7, reused, D9)

gui('S_WATCHLIST', 'WatchlistItemsFragment$1.onItemClick',
    'Tap a security row of the watchlist (not the header row): the row opens its context menu',
    evidence='SRC investment/watchlist/WatchlistItemsFragment.java:140-150 (header guard at 144; openContextMenu at 147); FW-SRC core/java/android/widget/AdapterView.java:316-318 (performItemClick calls mOnItemClickListener.onItemClick)')

gui('S_WATCHLIST', 'WatchlistItemsFragment.onContextItemSelected',
    'Tap an item of the context menu of a security row: Download price, Edit price or Delete',
    cls='non_standard',
    via='the activity forwards the context item to the fragment: FW-SRC core/java/android/app/Activity.java:3470 (onMenuItemSelected context case), then INFERRED androidx forwarding (not read)',
    evidence='SRC investment/watchlist/WatchlistItemsFragment.java:214-272 (switch 233; DownloadPrice 234-238; EditPrice 240-264; DELETE 266-268); SRC investment/watchlist/WatchlistItemsFragment.java:189-207 (the menu built by onCreateContextMenu)')

gui('S_WATCHLIST', 'WatchlistItemsFragment.onFloatingActionButtonClicked',
    'Tap the + button on the watchlist: opens the new investment transaction editor',
    cls='non_standard',
    via='BaseListFragment$2.onClick (batch 026, common/BaseListFragment.java:241-246) calls onFloatingActionButtonClicked() at line 244; the plain CALL is cut by the merged sup pair at graph_def.py:3786, so this GUI edge is the route',
    evidence='SRC investment/watchlist/WatchlistItemsFragment.java:172-173 (FAB shown and attached), 343-346 (override); SRC common/BaseListFragment.java:238-248 (listener 241-246, call 244); label_026.md row BaseListFragment$2.onClick (REACHABLE, GUI from S_PAYEE); INFERRED FAB library dispatch (com.melnykov FAB is not in fw_src)')

gui('S_WATCHLIST', 'WatchlistItemsFragment$2.onClick',
    'Tap Cancel in the delete confirmation dialog (opened by the Delete item of a row context menu): the dialog closes and nothing is deleted',
    cls='non_standard',
    via='platform AlertDialog button: FW-SRC core/java/com/android/internal/app/AlertController.java:125-140 (mButtonHandler posts the button message at 140), 149-166 (ButtonHandler calls the listener at 166)',
    evidence='SRC investment/watchlist/WatchlistItemsFragment.java:266-268 (DELETE), 472-498 (dialog; Cancel listener body 493-496, dialog.cancel() at 495); auto_calls.json has no record with src WatchlistItemsFragment$2.onClick (grep file, section D)')

gui('S_WATCHLIST', 'WatchlistItemsFragment$3.onClick',
    'Tap OK in the delete confirmation dialog: deletes the security (StockRepository.delete) and restarts the loader',
    cls='non_standard',
    via='platform AlertDialog button: FW-SRC core/java/com/android/internal/app/AlertController.java:125-140, 149-166 (as for $2.onClick)',
    evidence='SRC investment/watchlist/WatchlistItemsFragment.java:479-490 (OK listener; body 482-488: delete at 483, toast at 484, reloadData at 488); auto_calls.json records with src WatchlistItemsFragment$3.onClick at lines 482-488 (grep file, section D)')
