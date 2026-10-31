# ================================================================== batch 015 (label_015): CategoryExpandableListAdapter (17 methods and its $1 listener), CategoryListItemViewHolderChild.<init>, CategoryListItemViewHolderGroup.<init>, MoneySimpleCursorAdapter (4 methods)

# ---- screen: the category list opened to pick a category (ACTION_PICK). Batches 029 and 030 reuse this key and do not redefine it.

SCREENS.update({
    'S_CATEGORY_LIST': 'Category list (CategoryListFragment): the expandable list of categories and subcategories. Opened to pick a category (ACTION_PICK), each top-level category row shows a selector icon',
})

# ---- picker mode: the selector icon of a top-level category row (shown only when the list was opened with ACTION_PICK)

e('S_CATEGORY_LIST', 'CategoryExpandableListAdapter$1.onClick', 'GUI',
  'tap the selector icon of a top-level category row in the category list opened to pick a category',
  gui=['Tap the selector icon on a top-level category row of the category list opened to pick a category'],
  guard='the list was opened with ACTION_PICK, so the selector is shown (CategoryListFragment.java:431; CategoryExpandableListAdapter.java:181)',
  evidence='SRC adapter/CategoryExpandableListAdapter.java:181-198 (selector visible and click listener set only when mShowSelector); SRC common/CategoryListFragment.java:431 (showSelector = mAction.equals(ACTION_PICK))')

# ---- framework-dispatched adapter callbacks. ExpandableListFragment.setListAdapter hands the adapter to the list view
# (mList.setAdapter, line 164). The framework then calls the callbacks below (ExpandableListView and its connector are not in
# fw_src and were not read: INFERRED). No auto_calls.json edge reaches these methods, so each gets one FRAMEWORK edge here.

e('ExpandableListFragment.setListAdapter', 'CategoryExpandableListAdapter.getChildView', 'FRAMEWORK',
  'the list view takes the adapter (mList.setAdapter, line 164); the framework then asks the adapter for the view of each visible subcategory row',
  guard='the list view exists: mList is not null (ExpandableListFragment.java:163)',
  evidence='SRC common/ExpandableListFragment.java:160-164; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('ExpandableListFragment.setListAdapter', 'CategoryExpandableListAdapter.getGroupView', 'FRAMEWORK',
  'the list view takes the adapter (mList.setAdapter, line 164); the framework then asks the adapter for the view of each visible category row',
  guard='the list view exists: mList is not null (ExpandableListFragment.java:163)',
  evidence='SRC common/ExpandableListFragment.java:160-164; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('ExpandableListFragment.setListAdapter', 'CategoryExpandableListAdapter.getChildId', 'FRAMEWORK',
  'the list view takes the adapter (mList.setAdapter, line 164); the framework then asks the adapter for the id of each subcategory row',
  guard='the list view exists: mList is not null (ExpandableListFragment.java:163)',
  evidence='SRC common/ExpandableListFragment.java:160-164; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('ExpandableListFragment.setListAdapter', 'CategoryExpandableListAdapter.getGroupId', 'FRAMEWORK',
  'the list view takes the adapter (mList.setAdapter, line 164); the framework then asks the adapter for the id of each category row',
  guard='the list view exists: mList is not null (ExpandableListFragment.java:163)',
  evidence='SRC common/ExpandableListFragment.java:160-164; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('ExpandableListFragment.setListAdapter', 'CategoryExpandableListAdapter.getGroup', 'FRAMEWORK',
  'the list view takes the adapter (mList.setAdapter, line 164); the framework then asks the adapter for the category object at each group position',
  guard='the list view exists: mList is not null (ExpandableListFragment.java:163)',
  evidence='SRC common/ExpandableListFragment.java:160-164; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('ExpandableListFragment.setListAdapter', 'CategoryExpandableListAdapter.getGroupCount', 'FRAMEWORK',
  'the list view takes the adapter (mList.setAdapter, line 164); the framework then asks the adapter for the number of category rows',
  guard='the list view exists: mList is not null (ExpandableListFragment.java:163)',
  evidence='SRC common/ExpandableListFragment.java:160-164; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('ExpandableListFragment.setListAdapter', 'CategoryExpandableListAdapter.hasStableIds', 'FRAMEWORK',
  'the list view takes the adapter (mList.setAdapter, line 164); the framework then asks the adapter whether its ids are stable',
  guard='the list view exists: mList is not null (ExpandableListFragment.java:163)',
  evidence='SRC common/ExpandableListFragment.java:160-164; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('ExpandableListFragment.setListAdapter', 'CategoryExpandableListAdapter.isChildSelectable', 'FRAMEWORK',
  'the list view takes the adapter (mList.setAdapter, line 164); the framework then asks the adapter whether a subcategory row is selectable',
  guard='the list view exists: mList is not null (ExpandableListFragment.java:163)',
  evidence='SRC common/ExpandableListFragment.java:160-164; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

# ---- MoneySimpleCursorAdapter.setViewText: the androidx SimpleCursorAdapter calls it while it binds each row of the account list.
# AccountListFragment.onLoadFinished gives the adapter its cursor (changeCursor, line 192). Library source not read: INFERRED.

e('AccountListFragment.onLoadFinished', 'MoneySimpleCursorAdapter.setViewText', 'FRAMEWORK',
  'the account loader delivers its cursor; onLoadFinished calls changeCursor (line 192) and the androidx SimpleCursorAdapter binds each row, calling setViewText for the mapped text view',
  guard='the cursor is from the account loader: loader.getId() == LOADER_ACCOUNT (AccountListFragment.java:188)',
  evidence='SRC account/AccountListFragment.java:187-192, 78-82 (text1 mapping at line 81); INFERRED androidx SimpleCursorAdapter.changeCursor -> bindView -> setViewText (library source not read)')
