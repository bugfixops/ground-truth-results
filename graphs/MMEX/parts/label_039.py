# batch 039 (label_039): com.money.manager.ex.core TransactionStatuses (6 methods: <clinit>, <init>, contains, from, get, getCode) and TransactionTypes (4 methods: <clinit>, <init>, contains, getCode). 10 methods: 7 REACHABLE, 3 UNREACHABLE. Rows and printed lines: graphs/MMEX/parts/label_039.md; grep output: graphs/MMEX/parts/label_039.grep.txt.
# No e() edges: REACHABLE rows rest on auto_calls.json CALL records (the build adds them). No new sup pairs: the three callers of TransactionStatuses.from (StatusFilter.add, remove, contains(String)) are already cut by the batch 013 sup at graph_def.py:1410-1412, and TransactionStatuses.contains and TransactionTypes.contains have no incoming edge at all.

# ================================================================== UNREACHABLE (batch 039)

UNREACHABLE['TransactionStatuses.contains'] = ('no_trigger_in_app',
  'Public instance method with no caller. No app code calls TransactionStatuses.contains: the only .contains( call on a status value is AccountTransactionListFragment.java:799, on mFilter.transactionStatus, which is a StatusFilter (TransactionFilter.java:34), so that call is StatusFilter.contains(int). No auto_calls.json CALL record has TransactionStatuses.contains as dst (label_039.grep.txt sections A, C, E).',
  'SRC core/TransactionStatuses.java:64-75; SRC account/AccountTransactionListFragment.java:799; SRC account/TransactionFilter.java:34; label_039.grep.txt',
  'SOURCE')

UNREACHABLE['TransactionStatuses.from'] = ('no_trigger_in_app',
  'Static lookup by name. Its only callers are StatusFilter.add (line 65), StatusFilter.remove (line 72) and StatusFilter.contains(String) (line 79). All three are UNREACHABLE in batch 013 (no caller; graph_def.py:1418, 1423, 1428), and their CALL edges into from are already cut by the sup at graph_def.py:1410-1412, so from has no live incoming edge. No other call site in the source root (label_039.grep.txt sections A, D, G).',
  'SRC core/TransactionStatuses.java:29-39; SRC account/StatusFilter.java:64-66, 71-73, 78-80; graph_def.py:1410-1412, 1418, 1423, 1428; auto_calls.json:46104-46105, 46128-46129, 46152-46153; label_039.grep.txt',
  'SOURCE')

UNREACHABLE['TransactionTypes.contains'] = ('no_trigger_in_app',
  'Public instance method with no caller. No app code calls TransactionTypes.contains: every .contains( call in the source root has a receiver whose name is not a TransactionTypes value (receiver names found by grep include mAccountIdList, categories, currencies and mFilter.transactionStatus; none is a TransactionTypes value). No auto_calls.json CALL record has TransactionTypes.contains as dst (label_039.grep.txt sections A, C, E).',
  'SRC core/TransactionTypes.java:41-52; label_039.grep.txt',
  'SOURCE')
