# ================================================================== batch 073 (label_073): StockHistory (5 methods),
# PayeeListFragment (20 methods) and PayeeListFragment$1 to $4 (8 methods): 33 in total (graphs/MMEX/scratch/batches/batch_073.txt).
# Rows, printed lines and counts: graphs/MMEX/parts/label_073.md.
# Edges written here: the PayeeListFragment routes the framework or the user starts (lifecycle, options menu, loaders, context menu,
# row tap, search box, sort menu), the dialog OK and Cancel listeners, and one judgement cut (sup) on the shared list listener.
# StockHistory has no e() edges: its callers are auto CALL records (auto_calls.json), so none are written here (D7).
# PayeeListFragment$N.<init> and the lambda are auto records (CALL and REGISTER); no edge is written for them here.
# UNREACHABLE: StockHistory.<init>(Parcel) and StockHistory.getHistId, both SOURCE (no caller in the app source root).
# No grep file: neither UNREACHABLE claim depends on a library or generated class.
# Dialog listeners: $1 and $3 are the Cancel bodies, $2 and $4 are the OK bodies. The class files decide this:
# $1 and $3 hold only dialog.cancel(), $2 holds PayeeRepository.delete and restartLoader (and captures payeeId, <init>(PayeeListFragment,int)),
# $4 holds PayeeService.createNew, PayeeService.update and restartLoader.

# ---- lifecycle: PayeeActivity.onCreate adds this fragment (PayeeActivity.java:56-61), then the framework calls onActivityCreated
e('PayeeActivity.onCreate', 'PayeeListFragment.onActivityCreated', 'FRAMEWORK',
  'PayeeActivity.onCreate adds this fragment with a fragment transaction and commits it (lines 56-61); the framework then calls onActivityCreated on it. Same route as AccountListActivity.onCreate to AccountListFragment.onActivityCreated (graph_def.py:929)',
  evidence='SRC final_java_only/MMEX/app/MMEX-#v2024.06.14/app/src/main/java/com/money/manager/ex/PayeeActivity.java:56-61; SRC fragment/PayeeListFragment.java:81; INFERRED androidx FragmentManager calls onActivityCreated after commit (library not read)')

e('PayeeListFragment.onActivityCreated', 'PayeeListFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'onActivityCreated calls setHasOptionsMenu(true) (line 93); the activity then builds its options menu and the framework calls the fragment onCreateOptionsMenu, which this class overrides (line 124). Pattern: AccountListFragment.onActivityCreated (graph_def.py:3752)',
  evidence='SRC fragment/PayeeListFragment.java:93, 124-126; INFERRED androidx options menu dispatch (library not read)')

e('PayeeListFragment.onActivityCreated', 'PayeeListFragment.onCreateLoader', 'FRAMEWORK',
  'initLoader (line 114) registers this fragment as the LoaderCallbacks, so the LoaderManager calls onCreateLoader. Pattern: graph_def.py:954',
  evidence='SRC fragment/PayeeListFragment.java:114; INFERRED androidx LoaderManager calls LoaderCallbacks (library not read)')

e('PayeeListFragment.onCreateLoader', 'PayeeListFragment.onLoadFinished', 'FRAMEWORK',
  'the loader delivers its cursor to onLoadFinished when the load completes. Pattern: graph_def.py:958',
  evidence='SRC fragment/PayeeListFragment.java:255-263 (MmxCursorLoader), 274-296; INFERRED androidx Loader delivery (library not read)')

# ---- loader restart: restartLoader (lines 454-456) is called by the sort menu, the search box and the dialog OK buttons
e('PayeeListFragment.restartLoader', 'PayeeListFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader asks the LoaderManager to restart the loader, which calls onCreateLoader again. Pattern: graph_def.py:2323',
  evidence='SRC fragment/PayeeListFragment.java:454-456; INFERRED androidx LoaderManager (library not read)')

e('PayeeListFragment.restartLoader', 'PayeeListFragment.onLoaderReset', 'FRAMEWORK',
  'the restart destroys the previous loader, which calls onLoaderReset on the callbacks. Pattern: graph_def.py:2331',
  evidence='SRC fragment/PayeeListFragment.java:454-456; INFERRED androidx LoaderManager (library not read)')

# ---- context menu: a plain row tap outside picker mode opens the row menu (line 450)
e('PayeeListFragment.onListItemClick', 'PayeeListFragment.onCreateContextMenu', 'FRAMEWORK',
  'a row tap outside picker mode calls getActivity().openContextMenu(v) (line 450), and the framework then calls onCreateContextMenu. Pattern: AccountListFragment.onListItemClick (graph_def.py:968)',
  evidence='SRC fragment/PayeeListFragment.java:437-452 (openContextMenu at 450); INFERRED Activity.openContextMenu dispatch (framework source not read)')

# ---- dialogs: showDialogDeletePayee (context menu DELETE on an unused payee) and showDialogEditPayeeName (EDIT, FAB)
e('PayeeListFragment.showDialogDeletePayee', 'PayeeListFragment$2.onClick', 'FRAMEWORK',
  'the OK button of the delete dialog: setPositiveButton stores the listener (source lines 339-349) and the framework calls its onClick on a tap. Body: PayeeRepository.delete, Toast, restartLoader. Pattern: label_024.py:10-15',
  evidence='SRC fragment/PayeeListFragment.java:334-349; build class fragment/PayeeListFragment$2.class (constant pool: PayeeRepository, delete, restartLoader, Toast; <init>(PayeeListFragment,int) captures payeeId); INFERRED AlertDialog stores and calls the listener (FW-SRC not read)')

e('PayeeListFragment.showDialogDeletePayee', 'PayeeListFragment$1.onClick', 'FRAMEWORK',
  'the Cancel button of the delete dialog: setNegativeButton stores the listener (lines 350-355) and the framework calls its onClick on a tap. Body: dialog.cancel() only',
  evidence='SRC fragment/PayeeListFragment.java:350-355; build class fragment/PayeeListFragment$1.class (constant pool: cancel only; <init>(PayeeListFragment) captures nothing)')

e('PayeeListFragment.showDialogEditPayeeName', 'PayeeListFragment$4.onClick', 'FRAMEWORK',
  'the OK button of the edit dialog: setPositiveButton stores the listener (lines 375-412) and the framework calls its onClick on a tap. Body: createNew (insert) or update, sendResultToActivity on a PICK intent, restartLoader',
  evidence='SRC fragment/PayeeListFragment.java:375-412; build class fragment/PayeeListFragment$4.class (constant pool: PayeeService createNew and update, restartLoader, access$100, and a reference to the synthetic PayeeListFragment$5 holder); INFERRED AlertDialog stores and calls the listener (FW-SRC not read)')

e('PayeeListFragment.showDialogEditPayeeName', 'PayeeListFragment$3.onClick', 'FRAMEWORK',
  'the Cancel button of the edit dialog: setNegativeButton stores the listener (lines 414-419) and the framework calls its onClick on a tap. Body: dialog.cancel() only',
  evidence='SRC fragment/PayeeListFragment.java:414-419; build class fragment/PayeeListFragment$3.class (constant pool: cancel only)')

# ---- GUI edges from the one screen S_PAYEE (PayeeActivity.onCreate ENTERS it, graph_def.py:144)
gui('S_PAYEE', 'PayeeListFragment.onOptionsItemSelected',
    'Tap Sort by name or Sort by usage in the payee options menu (menu_sort_name, menu_sort_usage), or the Up arrow (android.R.id.home)',
    evidence='SRC fragment/PayeeListFragment.java:147-173; SRC res/menu/menu_payee.xml:30, 33 (ids menu_sort_name, menu_sort_usage); auto_calls PayeeListFragment.onOptionsItemSelected -> restartLoader (line 164); pattern graph_def.py:3777')

gui('S_PAYEE', 'PayeeListFragment.onCreateContextMenu',
    'Long-press a payee row (the list is registered for the context menu at line 104)',
    evidence='SRC fragment/PayeeListFragment.java:104, 177-188; INFERRED long-press on a registered view opens its context menu (Android source not read); pattern graph_def.py:2338')

gui('S_PAYEE', 'PayeeListFragment.onContextItemSelected',
    'Tap Edit, Delete or View transactions in the menu of a payee row',
    evidence='SRC fragment/PayeeListFragment.java:185-187 (menu items), 190-241 (EDIT 213, DELETE 217, VIEW_TRANSACTIONS 232); INFERRED the framework dispatches the chosen item to the fragment; pattern graph_def.py:2341')

gui('S_PAYEE', 'PayeeListFragment.onListItemClick',
    'Tap a payee row: in picker mode the payee is returned to the caller, otherwise the row menu opens',
    evidence='SRC core/AbsListFragment.java:41-46 (onItemClick calls onListItemClick at 44), 306; SRC fragment/PayeeListFragment.java:437-452; the shared-listener CHA record to this method is cut by sup below; pattern graph_def.py:2691')

gui('S_PAYEE', 'PayeeListFragment.onQueryTextChange',
    'Type in the search box of the payee list',
    evidence='SRC common/BaseListFragment.java:119-130; SRC fragment/PayeeListFragment.java:298-306; auto_calls record BaseListFragment.onPreQueryTextChange@PayeeListFragment -> PayeeListFragment.onQueryTextChange (BaseListFragment.java:226); INFERRED androidx SearchView calls the listener (not in fw_src); pattern graph_def.py:983-984')

# ---- judgement cut (same kind as the batch 026 FAB cut and the batch 046 listener cut): AbsListFragment$1.onItemClick is the
# shared list listener, and its CHA record fans out to every list's onListItemClick, so a tap on another list would reach this method.
# The payee-list route is the gui edge above.
sup(('AbsListFragment$1.onItemClick', 'PayeeListFragment.onListItemClick'))  # auto_calls.json, AbsListFragment.java:44, dispatch cha

# ---- UNREACHABLE: StockHistory (both are SOURCE: no caller in the app source root)
UNREACHABLE['StockHistory.<init>(Parcel)'] = ('no_trigger_in_app',
  'protected Parcel constructor with no caller. The class has no CREATOR and does not implement Parcelable (StockHistory.java:21-61), so no parcel is ever read into a StockHistory. The only object creation in app source is the no-arg new StockHistory() at StockHistoryRepository.java:183',
  'SRC domainmodel/StockHistory.java:50-52; SRC datalayer/StockHistoryRepository.java:183 (no-arg call only); source grep for "StockHistory(" and "StockHistory.CREATOR" in final_java_only app src/main/java finds only the declaration and that call',
  'SOURCE')

UNREACHABLE['StockHistory.getHistId'] = ('no_trigger_in_app',
  'public getter with no caller: the grep of app src/main/java for getHistId finds only its declaration (StockHistory.java:54-56). Nothing calls it, so the value is never read',
  'SRC domainmodel/StockHistory.java:54-56; source grep for getHistId in final_java_only app src/main/java (declaration only)',
  'SOURCE')
