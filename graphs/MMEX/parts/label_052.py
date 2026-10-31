# ================================================================== batch 052 (label_052): QueryAccountBills (24 methods),
# QueryAllData (2), QueryBillDeposits (3, including <clinit>).
# Result: 26 REACHABLE, 3 UNREACHABLE (see the .md rows). Rows and printed lines: graphs/MMEX/parts/label_052.md.
# This file writes:
#   - no e() edges: every route into these methods is an auto CALL record (auto_calls.json) or a route owned by another batch,
#   - UNREACHABLE entries: getFavoriteAcct and getStatus (no caller), getFilterAccountSelection (the framework never binds
#     the widget RemoteViewsService that calls it; checked against fw_src android-8.1.0_r1, see the reason and the open point),
#   - 4 sup pairs (D14a): auto CALL records whose caller is getFilterAccountSelection, which is UNREACHABLE in this batch.
# getFavoriteAcct and getStatus are getters with no outgoing CALL record, so they have no sup pairs.

UNREACHABLE['QueryAccountBills.getFavoriteAcct'] = ('no_trigger_in_app',
    'no caller: the only occurrence of getFavoriteAcct() in the app source is its definition; auto_calls.json has no CALL record with it as src or dst; the field is written by setFavoriteAcct (called from setValueFromCursor, line 220) and never read',
    'QueryAccountBills.java:141, 220', 'SOURCE')

UNREACHABLE['QueryAccountBills.getStatus'] = ('no_trigger_in_app',
    'no caller: no getStatus() call in the app resolves to QueryAccountBills (the receivers are Account, AccountTransaction, RecurringTransaction, ITransactionEntity and TransactionStatuses; QueryAccountBills extends Dataset and does not implement ITransactionEntity); auto_calls.json has no CALL record with it as dst; the field is written by setStatus (called from setValueFromCursor, line 223) and never read',
    'QueryAccountBills.java:169, 223; MainActivity.java:1271; CalculateRunningBalanceTask2.java:145', 'SOURCE')

UNREACHABLE['QueryAccountBills.getFilterAccountSelection'] = ('framework_never_calls',
    'the only caller is AllAccountBillsViewFactory.onDataSetChanged (line 113), which runs only when the framework binds the widget RemoteViewsService. The host binds it through AppWidgetManager.bindRemoteViewsService (fw_src RemoteViewsAdapter.java:178); AppWidgetServiceImpl.bindRemoteViewsService refuses a service that does not declare BIND_REMOTEVIEWS (fw_src AppWidgetServiceImpl.java:1251, 3608-3611). AccountBillsWidgetService declares BIND_JOB_SERVICE (AndroidManifest.xml:402-403), so the bind throws SecurityException, which RemoteViewsAdapter catches (lines 184-188). onGetViewFactory (AccountBillsWidgetService.java:26-27) and onDataSetChanged therefore never run. Checked against fw_src android-8.1.0_r1 only (see the open point).',
    'QueryAccountBills.java:155; AllAccountBillsViewFactory.java:108-113; AccountBillsWidgetService.java:26-27; AndroidManifest.xml:402-403; fw_src RemoteViewsAdapter.java:178, 184-188; fw_src AppWidgetServiceImpl.java:1251, 3608-3611', 'INFERRED')

# auto CALL records with src = QueryAccountBills.getFilterAccountSelection (auto_calls.json, 4 records): cut by sup because the caller is UNREACHABLE.
sup(('QueryAccountBills.getFilterAccountSelection', 'LookAndFeelSettings.getViewFavouriteAccounts'))
sup(('QueryAccountBills.getFilterAccountSelection', 'LookAndFeelSettings.getViewOpenAccounts'))
sup(('QueryAccountBills.getFilterAccountSelection', 'AppSettings.getLookAndFeelSettings'))
sup(('QueryAccountBills.getFilterAccountSelection', 'AppSettings.<init>'))
