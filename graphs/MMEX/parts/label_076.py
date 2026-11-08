# ================================================================== batch 076 (label_076)
# Rows, printed lines and counts: graphs/MMEX/parts/label_076.md (32 REACHABLE, 6 UNREACHABLE, 0 INCOMPLETE).
# Grep evidence for the library-based UNREACHABLE rows: graphs/MMEX/parts/label_076.grep.txt (sections 1 and 2).
# This file writes:
#   - 1 FRAMEWORK edge: AllDataListFragment.changeTransactionStatus -> DrawerMenuItemAdapter.getView (the Change status dialog rows);
#   - 9 FRAMEWORK edges: HomeFragment.renderAccountsList -> the HomeAccountsExpandableAdapter callbacks that no auto record reaches
#     (the label_015 pattern: the list view takes the adapter at setAdapter, then the framework calls each callback);
#   - 6 UNREACHABLE entries: DrawerMenuItem.withDivider (SOURCE); DrawerMenuItemRecyclerAdapter.<init> and add (SOURCE);
#     getItemCount, onBindViewHolder, onCreateViewHolder (RecyclerView overrides, INFERRED).
# Not written: CALL edges (D7: every other route is an auto CALL record); GUI edges (S_HOME and S_ALL_DATA are not in SCREENS);
#   sup pairs (D14a: no auto CALL record has an UNREACHABLE caller in this batch; queried auto_calls.json).
# env_text and state_text: only the child-row gate below is inline (D2, no new constants).

# ---- the Change status dialog (batch 021 route): AlertDialog shows the adapter as its row list
e('AllDataListFragment.changeTransactionStatus', 'DrawerMenuItemAdapter.getView', 'FRAMEWORK',
  'the Change status dialog shows the adapter as its row list: setAdapter stores it, the dialog installs it in its ListView, and the list view asks the adapter for each visible row view',
  guard='the dialog is created and shown (AllDataListFragment.java:912-913), so its rows are laid out',
  evidence='SRC common/AllDataListFragment.java:860, 891, 912-913; FW android/app/AlertDialog.java:425, 764; FW com/android/internal/app/AlertController.java:255, 891-892; FW android/widget/AbsListView.java:2335-2365 (obtainView calls mAdapter.getView at 2348, 2365); INFERRED Dialog.show calls onCreate (Dialog.java not read)')

# ---- the home accounts list: renderAccountsList gives the adapter to the expandable list (mExpandableListView.setAdapter, line 814)
e('HomeFragment.renderAccountsList', 'HomeAccountsExpandableAdapter.getGroupView', 'FRAMEWORK',
  'the list view takes the adapter (mExpandableListView.setAdapter, HomeFragment.java:814); the framework then asks the adapter for the header view of each group',
  evidence='SRC home/HomeFragment.java:811-814; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('HomeFragment.renderAccountsList', 'HomeAccountsExpandableAdapter.getGroupCount', 'FRAMEWORK',
  'the list view takes the adapter (mExpandableListView.setAdapter, HomeFragment.java:814); the framework then asks the adapter for the number of groups',
  evidence='SRC home/HomeFragment.java:811-814; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('HomeFragment.renderAccountsList', 'HomeAccountsExpandableAdapter.getGroup', 'FRAMEWORK',
  'the list view takes the adapter (mExpandableListView.setAdapter, HomeFragment.java:814); the framework then asks the adapter for the group object at each group position',
  evidence='SRC home/HomeFragment.java:811-814; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('HomeFragment.renderAccountsList', 'HomeAccountsExpandableAdapter.getGroupId', 'FRAMEWORK',
  'the list view takes the adapter (mExpandableListView.setAdapter, HomeFragment.java:814); the framework then asks the adapter for the id of each group',
  evidence='SRC home/HomeFragment.java:811-814; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('HomeFragment.renderAccountsList', 'HomeAccountsExpandableAdapter.getChildrenCount', 'FRAMEWORK',
  'the list view takes the adapter (mExpandableListView.setAdapter, HomeFragment.java:814); the framework then asks the adapter for the number of child rows of each group',
  evidence='SRC home/HomeFragment.java:811-814; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('HomeFragment.renderAccountsList', 'HomeAccountsExpandableAdapter.getChildId', 'FRAMEWORK',
  'the list view takes the adapter (mExpandableListView.setAdapter, HomeFragment.java:814); the framework then asks the adapter for the id of each child row',
  needs_state=state_text('a child row exists: the account type group holds at least one account (mAccountsByType, HomeAccountsExpandableAdapter.java:77)', ('data',)),
  evidence='SRC home/HomeFragment.java:811-814; SRC home/HomeAccountsExpandableAdapter.java:76-78; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('HomeFragment.renderAccountsList', 'HomeAccountsExpandableAdapter.getChildView', 'FRAMEWORK',
  'the list view takes the adapter (mExpandableListView.setAdapter, HomeFragment.java:814); the framework then draws the child rows of each group the user expands (a tap on the group row)',
  needs_state=state_text('a child row exists: the account type group holds at least one account (mAccountsByType, HomeAccountsExpandableAdapter.java:77)', ('data',)),
  evidence='SRC home/HomeFragment.java:811-814; SRC home/HomeAccountsExpandableAdapter.java:196-216; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('HomeFragment.renderAccountsList', 'HomeAccountsExpandableAdapter.hasStableIds', 'FRAMEWORK',
  'the list view takes the adapter (mExpandableListView.setAdapter, HomeFragment.java:814); the framework then asks the adapter whether its ids are stable',
  evidence='SRC home/HomeFragment.java:811-814; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('HomeFragment.renderAccountsList', 'HomeAccountsExpandableAdapter.isChildSelectable', 'FRAMEWORK',
  'the list view takes the adapter (mExpandableListView.setAdapter, HomeFragment.java:814); the framework then asks the adapter whether a child row is selectable',
  needs_state=state_text('a child row exists: the account type group holds at least one account (mAccountsByType, HomeAccountsExpandableAdapter.java:77)', ('data',)),
  evidence='SRC home/HomeFragment.java:811-814; SRC home/HomeAccountsExpandableAdapter.java:236-239; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

# ---- UNREACHABLE (6). Tuple: (kind, reason, evidence, confirmed_by)
UNREACHABLE['DrawerMenuItem.withDivider'] = ('no_trigger_in_app',
  'no call site in the app source: the two withDivider calls in MainActivity (1105, 1116) are comments, so mDivider stays false and hasDivider is always false',
  'SRC home/DrawerMenuItem.java:81-84; SRC home/MainActivity.java:1105, 1116; label_076.grep.txt section 2',
  'SOURCE')

UNREACHABLE['DrawerMenuItemRecyclerAdapter.<init>'] = ('no_trigger_in_app',
  'no caller: no code creates a DrawerMenuItemRecyclerAdapter (the name appears only in its own file)',
  'SRC home/DrawerMenuItemRecyclerAdapter.java:34-36; label_076.grep.txt section 1',
  'SOURCE')

UNREACHABLE['DrawerMenuItemRecyclerAdapter.add'] = ('no_trigger_in_app',
  'no caller: add runs only on an adapter instance, and no instance is created',
  'SRC home/DrawerMenuItemRecyclerAdapter.java:57-59; label_076.grep.txt section 1',
  'SOURCE')

UNREACHABLE['DrawerMenuItemRecyclerAdapter.getItemCount'] = ('no_trigger_in_app',
  'RecyclerView.Adapter override: RecyclerView calls it only for an adapter attached to a RecyclerView, and no instance is created',
  'SRC home/DrawerMenuItemRecyclerAdapter.java:52-55; label_076.grep.txt section 1; INFERRED RecyclerView dispatch (androidx library not read)',
  'INFERRED')

UNREACHABLE['DrawerMenuItemRecyclerAdapter.onBindViewHolder'] = ('no_trigger_in_app',
  'RecyclerView.Adapter override (empty body): RecyclerView calls it only for an adapter attached to a RecyclerView, and no instance is created',
  'SRC home/DrawerMenuItemRecyclerAdapter.java:47-50; label_076.grep.txt section 1; INFERRED RecyclerView dispatch (androidx library not read)',
  'INFERRED')

UNREACHABLE['DrawerMenuItemRecyclerAdapter.onCreateViewHolder'] = ('no_trigger_in_app',
  'RecyclerView.Adapter override (returns null): RecyclerView calls it only for an adapter attached to a RecyclerView, and no instance is created',
  'SRC home/DrawerMenuItemRecyclerAdapter.java:40-45; label_076.grep.txt section 1; INFERRED RecyclerView dispatch (androidx library not read)',
  'INFERRED')
