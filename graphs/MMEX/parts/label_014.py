# ================================================================== batch 014 (label_014): AllDataAdapter, AllDataViewHolder (24 methods)
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_014.md.
# Every edge below has a batch 014 method as its destination (newView or bindView).
# CALL edges come from auto_calls.json (USE_AUTO) and are not written here.
# Framework claims cite FW-SRC lines printed for this batch. The app imports androidx.cursoradapter.widget.CursorAdapter
# (AllDataAdapter.java:47), which is not in the dataset: its claims are INFERRED from the android.widget.CursorAdapter source.

# ---- all-data list: changeCursor relays out the list, the framework calls getView -> newView / bindView

e('AllDataListFragment.onLoadFinished', 'AllDataAdapter.newView', 'FRAMEWORK',
  'adapter.changeCursor(data) (AllDataListFragment.java:269) swaps in the new cursor and notifies the list; the list relayouts and the framework calls getView, which calls newView for a row that has no scrap view (the first layout of the data)',
  evidence='SRC common/AllDataListFragment.java:266-269 (changeCursor at 269); androidx CursorAdapter: not in the dataset, INFERRED to match FW-SRC core/java/android/widget/CursorAdapter.java:348-353 (changeCursor calls swapCursor), 365-381 (swapCursor calls notifyDataSetChanged at 381), 276-289 (getView calls newView at 285 when convertView is null); FW-SRC core/java/android/widget/BaseAdapter.java:51-53 (notifyDataSetChanged); DataSetObservable is not in fw_src: INFERRED that notifyChanged calls onChanged on each observer; FW-SRC core/java/android/widget/AdapterView.java:833-848 (AdapterDataSetObserver.onChanged calls requestLayout at 848); FW-SRC core/java/android/widget/ListView.java:578-579 (observer registered in setAdapter), 1624 (layoutChildren), 1784-1803 (fill methods), 2037-2052 (makeAndAddView calls obtainView at 2052); FW-SRC core/java/android/widget/AbsListView.java:2151-2164 (onLayout calls layoutChildren at 2164), 2335-2368 (obtainView calls getView at 2348 and 2365), 6796-6807 (getScrapView returns null when no scrap view is kept; retrieveFromScrap not printed: INFERRED that it returns null for an empty list)')

e('AllDataListFragment.onLoadFinished', 'AllDataAdapter.bindView', 'FRAMEWORK',
  'adapter.changeCursor(data) (AllDataListFragment.java:269) notifies the list; on the relayout the framework calls getView, which calls bindView for every visible row',
  evidence='SRC common/AllDataListFragment.java:266-269; androidx CursorAdapter INFERRED as above; FW-SRC core/java/android/widget/CursorAdapter.java:276-289 (getView calls bindView at 289), 365-381 (swapCursor calls notifyDataSetChanged at 381); FW-SRC core/java/android/widget/BaseAdapter.java:51-53; FW-SRC core/java/android/widget/AdapterView.java:833-848; FW-SRC core/java/android/widget/ListView.java:578-579, 1624, 1784-1803, 2037-2052; FW-SRC core/java/android/widget/AbsListView.java:2151-2164, 2335-2368')

# ---- recurring list: setListAdapter gives the list a new adapter; the framework calls getView -> newView / bindView

e('RecurringTransactionListFragment.onLoadFinished', 'AllDataAdapter.newView', 'FRAMEWORK',
  'setListAdapter(adapter) (RecurringTransactionListFragment.java:252) gives the list a new adapter; ListView.setAdapter resets the list and the list relayouts, and the framework calls getView, which calls newView for a row that has no scrap view',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:250-252; SRC core/AbsListFragment.java:253-257 (setListAdapter calls mList.setAdapter at 257); FW-SRC core/java/android/widget/ListView.java:552-558 (setAdapter: resetList at 557, mRecycler.clear at 558), 570 (super.setAdapter), 578-579 (observer), 603 (requestLayout); FW-SRC core/java/android/widget/AbsListView.java:2151-2164, 2335-2368 (getView at 2365 with scrapView from getScrapView at 2364), 6796-6807 (getScrapView returns null when no scrap view is kept; retrieveFromScrap not printed: INFERRED that it returns null for an empty list); FW-SRC core/java/android/widget/CursorAdapter.java:276-289 (getView calls newView at 285 when convertView is null); FW-SRC core/java/android/widget/ListView.java:1624, 1784-1803, 2037-2052; androidx CursorAdapter INFERRED as above')

e('RecurringTransactionListFragment.onLoadFinished', 'AllDataAdapter.bindView', 'FRAMEWORK',
  'setListAdapter(adapter) (RecurringTransactionListFragment.java:252) gives the list a new adapter; the list relayouts and the framework calls getView, which calls bindView for every visible row',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:250-252; SRC core/AbsListFragment.java:253-257; FW-SRC core/java/android/widget/ListView.java:552-558, 570, 578-579, 603; FW-SRC core/java/android/widget/AbsListView.java:2151-2164, 2335-2368; FW-SRC core/java/android/widget/CursorAdapter.java:276-289 (getView calls bindView at 289); androidx CursorAdapter INFERRED as above')
