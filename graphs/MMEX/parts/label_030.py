# batch 030 (label_030): com.money.manager.ex.common.CategoryListFragment, methods 41-43 of 43: CategoryListFragment$8.onChildClick, CategoryListFragment$9.<init>, CategoryListFragment$9.onGroupClick. Rows and printed lines: graphs/MMEX/parts/label_030.md.
# Both listeners are installed in addListClickHandlers only when the list was opened with ACTION_PICK (CategoryListFragment.java:661-662 and 681-682). The page S_CATEGORY_LIST is defined at graph_def.py:1214 and reused here (D9).
# No ENTERS edge is written to S_CATEGORY_LIST: its ENTERS edge is in batch 029 (label_029.py:15), and batches 028 and 029 own the decision about it.
# CALL edges come from auto_calls.json: the listener constructor record (auto_calls.json:38846-38849) and the calls inside the two listeners (auto_calls.json:34974-35012 and 36998-37028). None are written here (D7). No auto edge out of these methods is blocked on API 27, so no sup cut is written.
# ExpandableListView is not in fw_src, so the dispatch of a row click to the listener is INFERRED (grep: graphs/MMEX/parts/label_030.grep.txt, section A).
# ExpandableListFragment.java:364 (mList.setOnChildClickListener(this)) would replace the picker listener if it ran after CategoryListFragment.java:662. It sits in onContentChanged, which no app code calls (grep: label_030.grep.txt, section C; the androidx Fragment base is not read: INFERRED).
# No UNREACHABLE entry in this batch: each method has a route through the picker (label_030.md).

# ---- user actions on the category list in picker mode (page S_CATEGORY_LIST). The picker is opened by tapping the category field of the transaction editor (EditTransactionCommonFunctions.java:459-466).

gui('S_CATEGORY_LIST', 'CategoryListFragment$8.onChildClick', 'Tap a subcategory row in the category list opened to pick a category',
  guard='the list was opened with ACTION_PICK, so the child-click listener is installed (CategoryListFragment.java:661-662)',
  evidence='SRC common/CategoryListFragment.java:661-662, 665-676 (the listener sets the chosen sub-category at 671 and calls setResultAndFinish at 675); SRC transactions/EditTransactionCommonFunctions.java:459-466 (the category field opens the picker with ACTION_PICK at 465); SRC common/CategoryListActivity.java:56-57 (the intent action becomes mAction); INFERRED ExpandableListView calls OnChildClickListener on a child-row click (ExpandableListView not in fw_src, not read)')

gui('S_CATEGORY_LIST', 'CategoryListFragment$9.onGroupClick', 'Tap a top-level category row in the category list opened to pick a category',
  guard='the list was opened with ACTION_PICK, so the group-click listener is installed (CategoryListFragment.java:661, 681-682)',
  evidence='SRC common/CategoryListFragment.java:681-684, 686-698 (the category is marked at 690; setResultAndFinish is called at 695 only when the category has no sub-categories, see 693-694); SRC transactions/EditTransactionCommonFunctions.java:459-466 (picker opened with ACTION_PICK); SRC common/CategoryListActivity.java:56-57; INFERRED ExpandableListView calls OnGroupClickListener on a group-row click (ExpandableListView not in fw_src, not read)')
