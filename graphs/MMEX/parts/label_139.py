# ================================================================== batch 139 (label_139): com.money.manager.ex.utils.MmxDate (methods 41-56 of 56; 16 methods)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_139.md (13 REACHABLE, 3 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_139.grep.txt.
# This file writes 0 e() edges, 0 gui() edges, 3 UNREACHABLE entries and 0 sup pairs.
# Edges are written only for destinations owned by this batch (D1). Every route into this batch is a CALL record from auto_calls.json (USE_AUTO, D7), so none is written here.
# The routes start in other batches: the S_CATEGORIES_REPORT page (graph_def.py:9322), the S_INCOME_VS_EXPENSES listener (graph_def.py:9509, batch 105), the Morningstar Rx callbacks (batch 090), the DatabaseSettingsActivity and FileStorageHelper paths and the MainActivity lifecycle. Those routes are interim where another batch is unmerged (D8).
# The three UNREACHABLE methods have no caller record in auto_calls.json and no call site in the app tree (SOURCE).

UNREACHABLE['MmxDate.setTime'] = ('no_trigger_in_app',
  'No call site in the app folder. The only occurrence of setTime( is the declaration in MmxDate, and the setTime( calls in InvestmentTransactionEditActivity are on java.util.Calendar. auto_calls.json has no record whose dst is MmxDate.setTime, and no method reference or subclass reaches it.',
  'SRC utils/MmxDate.java:337-340 (declaration); investment/InvestmentTransactionEditActivity.java:348-349 (java.util.Calendar); label_139.grep.txt section A (setTime( grep) and section C (0 incoming records)',
  'SOURCE')

UNREACHABLE['MmxDate.setTimeToEndOfDay'] = ('no_trigger_in_app',
  'The name occurs only at its declaration in the app tree. No call site and no auto_calls.json record has this callee, so no caller can reach the method.',
  'SRC utils/MmxDate.java:326-335 (declaration); label_139.grep.txt section A (grep over the MMEX tree: declaration only) and section C (0 incoming records)',
  'SOURCE')

UNREACHABLE['MmxDate.toIsoDateShortTimeString'] = ('no_trigger_in_app',
  'The name occurs only at its declaration in the app source. The other hits in the MMEX tree are JaCoCo HTML coverage reports, which are not code. No call site and no auto_calls.json record has this callee.',
  'SRC utils/MmxDate.java:374-377 (declaration); label_139.grep.txt section A (grep: declaration in the app source and in JaCoCo HTML only) and section C (0 incoming records)',
  'SOURCE')
