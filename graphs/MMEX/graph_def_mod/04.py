# §9 getContext 32-edge repair — CORRECTED §4 design (applied by the MMEX
# merger 2026-11-02 from helper/getcontext32-design/DESIGN.md §4; audit
# PASS on the implementation package).
# Design-literal texts throughout. Audit D5: the mirror trigger below is copied
# VERBATIM from the plain hand edge (graph_def_mod/03.py:941-944); the variant
# note lives in the evidence only. Expected mirror id: Eafb31232 (NOT the
# helper test-build E4fb43ddd, which came from differing trigger text).
# Audit D1: the plain-dispatcher / @RECURRING feeder omissions below rest on
# the CORRECTED rationale (plain feeder redundant for the genuine group tap
# and over-generating for the impossible child tap; @RECURRING is the
# recurring-transactions item's variant, not Synchronization's) — not on the
# design §4.3 wording that the plain dispatcher is fed only by $4$1.run.
# Audit D3: @MAIN gains 10 auto outs (not "all 11"); the 11th out is the hand
# invokeSyncService edge, mirrored by hand below.

# §4.1 — 6 dead-ends (contradicted callers). HONESTY NOTE (design §4.1):
# each caller DOES call getDatabasePath in source, on the early-return branch
# (stored path exists). sup() removes a real call from the graph because the
# graph cannot express "calls but early-returns": the single edge conflates
# the early-return branch with the fall-through branch, and only the
# fall-through branch reaches getContext. Deliberate, confined abstraction
# loss (6 edges, all into the one method whose fall-through is at issue).
# If the coordinator judges any deletion of a real call unacceptable, keep
# the §9 fallback (A0) — do NOT apply half of this design.
sup(('MainActivity.showCurrentDatabasePath', 'DatabaseManager.getDatabasePath'),
    ('MmexApplication.createDbInstance', 'DatabaseManager.getDatabasePath'),
    ('MainActivity.onOpenDatabaseClick', 'DatabaseManager.getDatabasePath'),
    ('DatabaseMetadataFactory.createDefaultEntry', 'DatabaseManager.getDatabasePath'),
    ('HomeFragment.createWelcomeView', 'DatabaseManager.getDatabasePath'),
    ('SyncManager.useDownloadedDatabase', 'DatabaseManager.getDatabasePath'))

# §4.2 step 2 — the one justified drawer feeder (@GROUP only; see §4.3 for
# the feeders deliberately NOT written). Side effect (intended): by
# base-pair suppression this also removes the auto plain-dispatcher and
# @RECURRING-dispatcher edges to plain triggerSync.
e('MainActivity.onDrawerMenuAndOptionMenuSelected@GROUP', 'SyncManager.triggerSynchronization@MAIN', 'CALL',
  'the drawer menu handler runs the Sync case and triggers synchronization (MainActivity-fed triggerSync only; variant @GROUP)',
  guard='item id == R.id.menu_sync (MainActivity.java:613-616); the tapped group has null children (MainActivity.java:860-861: Synchronization childItems null)',
  evidence='SRC home/MainActivity.java:613-616 (menu_sync case; call at 615); SRC home/MainActivity.java:1071 (menu_sync is a GROUP item); SRC home/MainActivity.java:860-861 (Synchronization has null children); variant @GROUP: group-tap dispatcher only')

# §4.2 step 3 — SUPPRESS the base pair. This kills the auto getDatabasePath
# edge for plain AND for every variant (including @MAIN, which is the whole
# point). Without this, auto-mirroring would supply @MAIN with a fresh
# getDatabasePath edge and the partition would fail entirely.
sup(('SyncManager.triggerSynchronization', 'DatabaseManager.getDatabasePath'))

# §4.2 step 4 — hand re-assert for PLAIN only. Plain keeps its
# getDatabasePath out; @MAIN does not get one (auto suppressed, no hand
# edge written for it).
e('SyncManager.triggerSynchronization', 'DatabaseManager.getDatabasePath', 'CALL',
  'Direct call',
  evidence='SRC sync/SyncManager.java:336 (bytecode)')

# §4.2 step 5 — hand mirror for the one HAND out. Trigger/guard copied
# VERBATIM from the plain hand edge (03.py:941-944); variant note in the
# evidence only. The other 9 @MAIN outs arrive by auto-mirroring for free
# and must NOT be hand-mirrored (each hand mirror would suppress the
# corresponding plain auto out and force a pointless re-assert).
e('SyncManager.triggerSynchronization@MAIN', 'SyncManager.invokeSyncService@SYNC', 'CALL',
  'triggerSynchronization invokes the sync service with the SYNC action after validating paths',
  guard='sync active AND local path non-empty AND remote path non-empty (SyncManager.java:332-348)',
  evidence='SRC sync/SyncManager.java:332-348 (isActive return at 333; empty-localPath return; empty-remotePath return; invokeSyncService(INTENT_ACTION_SYNC) at 348); variant @MAIN; reconciled Sync v2: dst retargeted to @SYNC (was plain invokeSyncService)')

# ==================================================================
# ROUTE14: loader-id partition (fix round, audited design + implementation).
# Plain onLoadFinished -> $1.run deleted in 01.py (was Ef9d523dd); the
# @REPORT variant edge below replaces it. startLoader@YEARS is the seal:
# the @REPORT chain is reachable ONLY through the YEARS branch.
e('IncomeVsExpensesListFragment.onActivityCreated', 'IncomeVsExpensesListFragment.onCreateLoader@YEARS', 'FRAMEWORK',
  'initLoader(ID_LOADER_YEARS) at line 113: the LoaderManager calls onCreateLoader for the years loader (id 2) (YEARS delivery only)',
  evidence='SRC reports/IncomeVsExpensesListFragment.java:113, 142-146; INFERRED androidx LoaderManager (library not read; LoaderManager.java is not in fw_src); variant @YEARS')
e('IncomeVsExpensesListFragment.onCreateLoader@YEARS', 'IncomeVsExpensesListFragment.onLoadFinished@YEARS', 'FRAMEWORK',
  'the years loader returned by onCreateLoader (line 146) delivers its cursor, and the LoaderManager calls onLoadFinished for the years loader (id 2) (YEARS delivery only)',
  evidence='SRC reports/IncomeVsExpensesListFragment.java:142-146, 199-212; INFERRED androidx Loader delivery (library not read); variant @YEARS')
e('IncomeVsExpensesListFragment.onLoadFinished@YEARS', 'IncomeVsExpensesListFragment.startLoader@YEARS', 'CALL',
  'the years branch of onLoadFinished calls startLoader (line 212): the years cursor has been read into mYearsSelected and the report loader is restarted with those years (YEARS delivery only; this call is the only feeder of startLoader@YEARS)',
  guard='the years cursor is non-null and has a first row (IncomeVsExpensesListFragment.java:200: data != null && data.moveToFirst()); otherwise the YEARS branch never reaches startLoader',
  evidence='SRC reports/IncomeVsExpensesListFragment.java:199-212 (YEARS branch; guard 200, startLoader at 212); SRC reports/IncomeVsExpensesListFragment.java:401-410 (startLoader builds the year bundle and restarts ID_LOADER_REPORT); variant @YEARS')
e('IncomeVsExpensesListFragment.startLoader@YEARS', 'IncomeVsExpensesListFragment.onCreateLoader@REPORT', 'FRAMEWORK',
  'restartLoader(ID_LOADER_REPORT) at line 410: the LoaderManager calls onCreateLoader for the report loader (id 1) with the year list in the bundle (REPORT delivery only; fed only by the YEARS branch via startLoader@YEARS)',
  evidence='SRC reports/IncomeVsExpensesListFragment.java:401-410, 119-140; INFERRED androidx LoaderManager (library not read); variant @REPORT')
e('IncomeVsExpensesListFragment.onCreateLoader@REPORT', 'IncomeVsExpensesListFragment.onLoadFinished@REPORT', 'FRAMEWORK',
  'the report loader returned by onCreateLoader (line 140) delivers its cursor, and the LoaderManager calls onLoadFinished for the report loader (id 1) (REPORT delivery only)',
  evidence='SRC reports/IncomeVsExpensesListFragment.java:135-146, 158-162; INFERRED androidx Loader delivery (library not read); variant @REPORT')
e('IncomeVsExpensesListFragment.onLoadFinished@REPORT', 'IncomeVsExpensesListFragment$1.run', 'FRAMEWORK',
  'the report loader has data and the device shows the dual-panel layout: a Handler posts the Runnable with a 1000 ms delay, and the Runnable calls showChart on the main looper (REPORT delivery only)',
  env=env_text('tablet layout with the fragmentChart view (the sw600dp landscape or sw720dp portrait layout): IncomeVsExpensesActivity.java:46 sets mIsDualPanel only when fragmentChart exists (res layout-sw600dp-land line 38, layout-sw720dp-port line 40)', ('hardware',)),
  guard='mIsDualPanel is true (IncomeVsExpensesListFragment.java:188); the post runs only then; the REPORT cursor is non-null (onLoadFinished returns at :171 if data is null, before the post)',
  evidence='SRC reports/IncomeVsExpensesListFragment.java:188-196 (guard 188; new Handler 189; postDelayed 190-195 with 1000 at 195; run calls showChart at 193); SRC reports/IncomeVsExpensesListFragment.java:158-171 (REPORT branch; null-data return at 171, before the post); FW-SRC core/java/android/os/Handler.java:427-430 (postDelayed queues through sendMessageDelayed), 789-791 (handleCallback runs callback.run); SRC reports/IncomeVsExpensesActivity.java:46; res layout-sw600dp-land/report_chart_fragments_activity.xml:38 and layout-sw720dp-port/report_chart_fragments_activity.xml:40; variant @REPORT')
