# ================================================================== batch 082 (label_082): MainActivity$4.onChildClick, MainActivity$4$1.<init>, MainActivity$4$1.run (graphs/MMEX/scratch/batches/batch_082.txt)
# Rows, printed lines and counts: graphs/MMEX/parts/label_082.md. No grep file: every row is REACHABLE, so no library or generated class is UNREACHABLE.
# Edges written here: the tap on a child row of the navigation drawer (GUI, from the home screen S_HOME, defined in label_077.py and reused here: no new SCREENS key) and the Handler.postDelayed runnable (FRAMEWORK).
# CALL edges come from auto_calls.json and are not written here (D7): MainActivity$4.onChildClick -> MainActivity$4$1.<init> (MainActivity.java:975) and MainActivity$4$1.run -> MainActivity.onDrawerMenuAndOptionMenuSelected (MainActivity.java:978).
# The listener is installed by createExpandableDrawer (batch 080, MainActivity.java:965), and that runs only after initializeDrawer finds the drawer (batch 080, MainActivity.java:1291-1301). Those edges are batch 080's and are not written here.
# UNREACHABLE: none. sup(): none (no auto CALL caller of a method in this batch is UNREACHABLE).

# ---- user action: a tap on a child row of the navigation drawer, opened from the home screen (MainActivity shows HomeFragment first, MainActivity.java:238, then initializeDrawer at 240)

gui('S_HOME', 'MainActivity$4.onChildClick',
    'Open the navigation drawer, expand a group with child rows (for example Accounts in the Entities group) and tap a child row',
    guard='the drawer exists: initializeDrawer finds drawerLayout (MainActivity.java:1291-1294) and createExpandableDrawer installs this listener (line 965); onChildClick returns false when mDrawer is null (line 968)',
    evidence='SRC home/MainActivity.java:965-968, 1289-1301, 238-240, 862-868; SRC res/layout/main_activity.xml:18-21, 46; SRC res/layout/merge_drawer.xml:72-76; INFERRED ExpandableListView calls OnChildClickListener on a child-row tap (ExpandableListView not in fw_src, not read); INFERRED DrawerLayout opens the drawer (androidx not read)')

# ---- the runnable that onChildClick posts with a 200 ms delay; the framework runs run() when the delay ends (the same pattern as label_041.py)

e('MainActivity$4.onChildClick', 'MainActivity$4$1.run', 'FRAMEWORK',
  'onChildClick posts the Runnable to a new Handler with a 200 ms delay (postDelayed); the framework runs run() when the delay ends, and run() calls onDrawerMenuAndOptionMenuSelected (auto CALL, line 978)',
  guard='selectedItem is not null (MainActivity.java:974)',
  evidence='SRC home/MainActivity.java:973-980; FW-SRC core/java/android/os/Handler.java:427-429 (postDelayed calls sendMessageDelayed), 596 (sendMessageDelayed), 97-99 (dispatchMessage calls handleCallback), 789-790 (handleCallback runs message.callback.run())')
