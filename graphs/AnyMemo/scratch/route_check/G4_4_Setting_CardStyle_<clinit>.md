# G4-4: Setting$CardStyle.<clinit>

- Method: Setting$CardStyle.<clinit> (the static initialiser of the nested enum CardStyle in entity/Setting.java). It runs on the first use of CardStyle.
- Label: REACHABLE (cold start AnyMemo -> Recent tab (auto) -> recent-list loaders -> loadRecentItemsWithDetails -> AnyMemoDBOpenHelper.getCardDao -> onCreate (version 0) -> Setting.<init> -> CardStyle class initialiser)
- Steps: 16 (show_route.py --dedupe). Checked: 16.
- Verdict: WRONG (4 wrong steps: 9, 13, 14, 16)

## Wrong steps

Step 9: RecentListFragment.onCreate -> RecentListFragment.onResume (LIFECYCLE), from the lc_chain helper at graph_def.py:80.
- Wrong: onCreateView is skipped. Fragment order is onCreate -> onCreateView -> onResume. lc_chain (graph_def.py:72-82) sets the source of every callback after onAttach/onCreate to cls.onCreate, so onResume (and onCreateView, onDestroy, onCreateOptionsMenu) all hang off onCreate. This is a helper bug, not only a route bug: every fragment or activity built with lc_chain has the same skipped steps.
- Fix: at graph_def.py:80, use the previous callback in the list as the source (keep a prev variable: s = cls + '.' + prev, then prev = cb). Then the chain is onCreate -> onCreateView -> onResume. Rebuild all graphs that use lc_chain (not only AnyMemo), since the same error exists in them.

Step 13: RecentListFragment.loadRecentItemsWithDetails -> AnyMemoDBOpenHelper.getCardDao (CALL), RecentListFragment.java:344.
- Wrong (guards and state missing): the call sits inside `for (final RecentItem ri : ril)` (guard_of, :337) and after `if (context == null) { break; }` (:339-341). The graph has neither guard. The list ril is the recent list after loadRecentItemsWithName drops entries that fail databaseUtil.checkDatabase (:312-325, deleteFromRecentList). So the call needs a recent entry, which is NEED_RECENT.
- Fix: add guard='the Recent list has at least one usable entry (RecentListFragment.java:337), context is not null (:339-341)' and needs_state=NEED_RECENT (graph_def.py:158) to this edge. A fresh install has no recent entry, so the route is not reachable from a clean start without NEED_RECENT.

Step 14: AnyMemoDBOpenHelper.getCardDao -> AnyMemoDBOpenHelper.onCreate (FRAMEWORK, ORMLite), with the STATE text 'the database file is new or its schema version changed (fresh install, upgrade or downgrade)'.
- Wrong (STATE text): the guard is right and now verified: FW-SRC core/java/android/database/sqlite/SQLiteOpenHelper.java:332-333 (`if (version == 0) { onCreate(db); }`; printed from the AOSP 8.1.0_r1 tag and saved under work/fw_src/android-8.1.0_r1/). But onCreate runs only for version 0. An upgrade calls onUpgrade and a downgrade calls onDowngrade (SQLiteOpenHelper.java:334-338), so the STATE text says more than the code does.
- Fix: change the STATE text to 'the database file has schema version 0 (a new or empty file, never set up by AnyMemo)'. Keep the guard. The ORMLite call path (getCardDao to getWritableDatabase) stays INFERRED.

Step 16: Setting.<init> -> Setting$CardStyle.<clinit> (CALL, 'Direct call'), cited as Setting.java:45.
- Wrong (line and label): Setting.java:45 is the annotation `@DatabaseField(defaultValue = "SINGLE_SIDED")`. The CardStyle reference is on :46, `private CardStyle cardStyle = CardStyle.SINGLE_SIDED;`, which runs in the constructor. Also a class initialiser is not a method call, so 'Direct call' overstates it: the trigger is the first getstatic of CardStyle, and the rule that runs <clinit> on first use is the JVM class-initialiser rule (not available here, so INFERRED).
- Fix: cite Setting.java:46 and label the edge INFERRED with the text 'first use of CardStyle in the field initialiser (JVM class initialisation)'.

## Steps checked and OK

1. ENTRY: AndroidManifest.xml:23-46 OK.
2. AnyMemo.<init> -> AnyMemo.onCreate: AnyMemo.java:116 OK. The framework citation has no line numbers. Printed: FW-SRC core/java/android/app/Activity.java:6989-6999 (performCreate calls onCreate). Fix the citation (not counted).
3. onCreate -> loadUiComponents: guard matches AnyMemo.java:124-134 OK.
4. loadUiComponents -> initDrawer: AnyMemo.java:187 OK.
5. initDrawer -> AnyMemo$2.onNavigationItemSelected@INIT: setSelectedItemId at :263 after the listener at :234. Library dispatch INFERRED.
6. Guard itemId == recent_tab_menu (AnyMemo.java:240-241); call at :241 OK.
7. RecentListFragment.<init> -> onAttach: onAttach at RecentListFragment.java:135-137 OK (androidx INFERRED).
8. onAttach -> onCreate: onCreate at :127-132 OK (androidx INFERRED).
10. onResume -> RecentListDetailLoaderCallbacks.onCreateLoader: restartLoader(2) at :219, no enclosing if (guard_of = []). OK (LoaderManager INFERRED).
11. onCreateLoader -> loadInBackground: forceLoad at :293, no guard. OK (ASYNC INFERRED).
12. loadInBackground -> loadRecentItemsWithDetails: return at :290, no guard. OK.
15. AnyMemoDBOpenHelper.onCreate -> Setting.<init>: getSettingDao().create(new Setting()) at AnyMemoDBOpenHelper.java:61, inside try (:53), no if (guard_of = []). OK.

## Not checked

- databaseUtil.checkDatabase (the check that keeps an entry in the recent list): not read. It decides whether a version-0 file can reach step 13.
- androidx LoaderManager / Fragment dispatch and ORMLite (getCardDao, getWritableDatabase): no source in the tree, INFERRED stays.
- The JVM class-initialiser order for CardStyle: INFERRED (not available here).
