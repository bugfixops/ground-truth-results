import sys
P = '/Users/darshan/Desktop/yang/work/graphs/AnyMemo/graph_def.py'
t = open(P, encoding='utf-8').read()
def swap(t, a, b, na, nb):
    assert t.count(a) == na, (a, t.count(a))
    assert t.count(b) == nb, (b, t.count(b))
    t = t.replace(a, '@@SW@@').replace(b, a).replace('@@SW@@', b)
    return t
# 1. renames: the bytecode class numbering is the authority (anon_table.py)
t = swap(t, 'CardEditor$1.', 'CardEditor$2.', 2, 2)
t = swap(t, 'ConverterFragment$2.', 'ConverterFragment$3.', 2, 2)
t = swap(t, 'MiscTabFragment$3.', 'MiscTabFragment$4.', 2, 2)
t = swap(t, 'PreviewEditActivity$2.', 'PreviewEditActivity$3.', 2, 2)
t = swap(t, 'PreviewEditActivity$2$1.', 'PreviewEditActivity$3$1.', 2, 2)
# 2. the menu swap is a framework dialog callback, not a CALL into the listener
old = "e('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity$3.onClick', 'CALL', 'menu_context_swap', evidence='SRC ui/PreviewEditActivity.java:351-384')\n"
new = ("gui('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity$3.onClick', 'Choose the swap menu item, then tap Yes (swap question and answer of every card)', kind='FRAMEWORK', evidence=FW_DIALOGFRAG + '; SRC ui/PreviewEditActivity.java:352-367')\n"
       "gui('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity$2.onClick', 'Choose the swap menu item, then tap the neutral button (swap, keep duplicates)', kind='FRAMEWORK', evidence=FW_DIALOGFRAG + '; SRC ui/PreviewEditActivity.java:368-379')\n")
assert t.count(old) == 1; t = t.replace(old, new)
# 3. the stale duplicate gui line (its text is the generic one, now replaced above)
old = "gui('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity$2.onClick', 'Tap a dialog button (listener at ui/PreviewEditActivity.java:368)', kind='FRAMEWORK', evidence=FW_DIALOGFRAG + '; SRC ui/PreviewEditActivity.java:368-379')\n"
assert t.count(old) == 1, t.count(old); t = t.replace(old, '')
# 4. the swap listeners' doProgressTask inner tasks need the framework hop to doUITask (as PreviewEditActivity$1 has)
anchor = "e('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity$4.doHeavyTask'"
assert t.count(anchor) == 1
hop = ("e('PreviewEditActivity$3$1.doHeavyTask', 'PreviewEditActivity$3$1.doUITask', 'FRAMEWORK', 'doProgressTask runs doHeavyTask() on a background Thread, then posts doUITask() to the main thread', evidence=FW_HANDLER + '; SRC utils/AMGUIUtility.java:80-112')\n"
       "e('PreviewEditActivity$2$1.doHeavyTask', 'PreviewEditActivity$2$1.doUITask', 'FRAMEWORK', 'doProgressTask runs doHeavyTask() on a background Thread, then posts doUITask() to the main thread', evidence=FW_HANDLER + '; SRC utils/AMGUIUtility.java:80-112')\n")
t = t.replace(anchor, hop + anchor)
# 5. the editmenu_list_id entry starts in onOptionsItemSelected (lines 285-294), not in the Edit button listener ($10, lines 620-627)
old = "e('PreviewEditActivity$10.onClick', 'CardListActivity.<init>', 'ENTRY', 'editmenu_list_id"
assert t.count(old) == 1
t = t.replace(old, "e('PreviewEditActivity.onOptionsItemSelected', 'CardListActivity.<init>', 'ENTRY', 'editmenu_list_id")
open(P, 'w', encoding='utf-8').write(t)
print('ok')
