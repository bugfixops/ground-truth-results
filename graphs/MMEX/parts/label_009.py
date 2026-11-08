# ================================================================== batch 009 (label_009): AccountStatuses (5 methods)
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_009.md.
# No e(...) edge is written here: the four REACHABLE methods get their only incoming edges from
# auto_calls.json (USE_AUTO adds them, D7), and every caller is a method of another batch.

# ---- AccountStatuses.equalsName: no caller in the app (grep output: label_009.grep.txt)
UNREACHABLE['AccountStatuses.equalsName'] = (
  'no_trigger_in_app',
  'Public instance method (case-insensitive title comparison). No caller in the app: its name occurs only at its declaration and at AccountTypes.equalsName, a different method. No auto_calls.json call edge reaches it, and no layout or manifest names it.',
  'AccountStatuses.java:39-41; AccountTypes.java:59; label_009.grep.txt; auto_calls.json:72633-72635, 90036-90037',
  'SOURCE')
