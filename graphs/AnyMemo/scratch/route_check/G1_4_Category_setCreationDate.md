# G1-4 Category.setCreationDate (checker G1)

- Label: REACHABLE (show_route: confirmed_by=INFERRED, path=UNCHECKED)
- Steps: 22 (show_route.py --dedupe; copy in scratchpad g1_4_route.txt); checked: 22
- Verdict: WRONG (5 wrong steps: 11, 15, 17, 18, 22)

## WRONG steps

**Step 11** MiscTabFragment.onClick -> DatabaseMerger.<init> (ENTRY)
- Edge and source agree (MiscTabFragment.java:346-349, `if(v == mergeButton)` starts DatabaseMerger). The guard is only in the description text; the edge has no guard= field.
- Fix: add guard='v == mergeButton (MiscTabFragment.java:346)' to both duplicate edges, graph_def.py:1034 and :1393.

**Step 15** DatabaseMerger.onClick -> DatabaseMerger$1.doHeavyTask (CALL)
- (a) No guard=. The call sits inside `if(v == mergeButton)` (DatabaseMerger.java:115).
- (b) Kind. doHeavyTask does not run inside onClick. doProgressTask (DatabaseMerger.java:116) starts a background Thread (AMGUIUtility.java:80, start at :112), and doHeavyTask runs there (:83). The sup() at graph_def.py:906 suppresses the bytecode copy by design, so this direct edge is the intended per-task edge, but it must show the thread hop.
- Fix: graph_def.py:1041 add guard='v == mergeButton (DatabaseMerger.java:115)'; change kind CALL -> ASYNC; description "doProgressTask starts a background Thread that runs doHeavyTask (AMGUIUtility.java:80-83)".

**Step 17** DatabaseUtil.mergeDatabases -> CardDaoImpl.createCards (CALL, auto edge)
- The call is real (DatabaseUtil.java:72). But line 72 is reached only when destPath != srcPath: DatabaseUtil.java:47-48 throws IllegalArgumentException first. The edge has no guard.
- Fix: EDIT guard for key ('DatabaseUtil.mergeDatabases', 'CardDaoImpl.createCards'): guard='destPath != srcPath (DatabaseUtil.java:47-48)'.

**Step 18** CardDaoImpl.createCards -> CardDaoImpl$2.call (FRAMEWORK, labelled RxJava 2)
- Endpoints are right: CardDaoImpl.java:491-496 passes an anonymous Callable, and $2 is correct (the anonymous classes are at :49 = $1, :491 = $2).
- The label is wrong. callBatchTasks here is the override at AbstractHelperDaoImpl.java:149-151, which calls super.callBatchTasks, an ORMLite BaseDaoImpl method (import at :5). Neither CardDaoImpl.java nor AbstractHelperDaoImpl.java references RxJava or io.reactivex (grep). Transaction behaviour is INFERRED (ORMLite source not read).
- The graph also omits the hop through AbstractHelperDaoImpl.callBatchTasks.
- Fix: graph_def.py:1438 replace FW_RX evidence with an ORMLite BaseDaoImpl.callBatchTasks citation (AbstractHelperDaoImpl.java:5, :149-151); add CardDaoImpl.createCards -> AbstractHelperDaoImpl.callBatchTasks (CALL, CardDaoImpl.java:491) before it. The same RxJava mislabel is at graph_def.py:1471 (DatabaseUtil$1.call, DatabaseUtil.java:60), outside this route.

**Step 22** AbstractHelperDaoImpl.create -> Category.setCreationDate (CALL, auto edge)
- Wrong target for this route. The route reaches line 122 via CardDaoImpl.create (steps 20-21: CardDaoImpl.java:859, :228), so `domain` is a Card. The call dispatches to Card.setCreationDate (Card.java:116), not Category.setCreationDate (Category.java:63). The graph has no receiver-type information, so the Card path reaches the Category node.
- The real category path is createCardsNoBatch -> categoryDao.create(card.getCategory()) at CardDaoImpl.java:852, guarded by :846-851 (category name not already in the destination's map and not empty). CategoryDaoImpl does not override create (its methods are createOrReturn, populateCategory, removeCategory), so AbstractHelperDaoImpl.create runs with a Category. Category implements VersionableDomainObject (Category.java:12), so the instanceof test at AbstractHelperDaoImpl.java:121 is true.
- Fix (graph_def terms): add node CategoryDaoImpl.create (inherited); edges CardDaoImpl.createCardsNoBatch -> CategoryDaoImpl.create (CALL, CardDaoImpl.java:852, guard as above), CategoryDaoImpl.create -> AbstractHelperDaoImpl.create (CALL), and CategoryDaoImpl.create -> Category.setCreationDate (CALL, AbstractHelperDaoImpl.java:122, guard 'domain is a Category'). Add sup(('AbstractHelperDaoImpl.create', 'Category.setCreationDate')) so the Card path no longer reaches the Category node. Check that AbstractHelperDaoImpl.create -> Card.setCreationDate still exists.

## Steps checked OK
- 1-9: AndroidManifest.xml:23-46 (MAIN/LAUNCHER); AnyMemo.java:115-141 (onCreate; the API <= 29 guard at :124-134 matches the edge guard); :187 initDrawer; :263 setSelectedItemId (library dispatch INFERRED); listener guards :240-241 (recent) and :249-250 (misc); replace at :254-256. Step 9: onCreateView is at MiscTabFragment.java:154.
- 10: MiscTabFragment.onCreateView -> onClick. mergeButton.setOnClickListener(this) at :204-205 is unconditional within onCreateView (starts :154).
- 12: DatabaseMerger.<init> -> onCreate (DatabaseMerger.java:52-55). The FW Activity citation has no line numbers (citation gap only).
- 13: onCreate -> S_DB_MERGER; setContentView at :56.
- 14: S_DB_MERGER -> onClick; listeners at :66-69, onClick at :100 (view dispatch INFERRED).
- 16: DatabaseMerger$1.doHeavyTask -> DatabaseUtil.mergeDatabases at DatabaseMerger.java:120, unconditional within doHeavyTask (:117-121). $1 is the only anonymous class in DatabaseMerger (freeDebug class list has DatabaseMerger$1.class).
- 19: CardDaoImpl$2.call -> createCardsNoBatch at :493, unconditional within call().
- 20: createCardsNoBatch -> CardDaoImpl.create at :859, inside the loop at :841-860. The call is real; it is not on a route to Category (see step 22).
- 21: CardDaoImpl.create -> AbstractHelperDaoImpl.create at :228 (super.create), after the ordinal block, unconditional within the try.

## Could not check / INFERRED
- Activity lifecycle, androidx fragments, Material BottomNavigationView and ORMLite callBatchTasks: framework/library source not read (INFERRED labels).
- Other Category route, not in this route: CategoryEditorFragment.java:250 -> CategoryDaoImpl.createOrReturn (CategoryDaoImpl.java:26-37; create(nc) at :37) -> AbstractHelperDaoImpl.create -> Category.setCreationDate. Not traced further.
