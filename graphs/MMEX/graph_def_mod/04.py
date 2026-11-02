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
e('SyncManager.triggerSynchronization@MAIN', 'SyncManager.invokeSyncService', 'CALL',
  'triggerSynchronization invokes the sync service with the SYNC action after validating paths',
  guard='sync active AND local path non-empty AND remote path non-empty (SyncManager.java:332-348)',
  evidence='SRC sync/SyncManager.java:332-348 (isActive return at 332; empty-localPath return; empty-remotePath return; invokeSyncService(INTENT_ACTION_SYNC) at 348); variant @MAIN')
