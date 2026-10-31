import ast
import os
import shutil
import sys

W = '/Users/darshan/Desktop/yang/work/'
BASE = W + 'graphs/AmazeFileManager/'
G = BASE + 'graph_def.py'
dry = '--dry' in sys.argv

DEL = {
    ('SshClientSessionTemplate.execute', 'Statvfs$Response.getFileSystemId'),
    ('SshClientSessionTemplate.execute', 'Statvfs$Response.getRawFileSystemId'),
}
NEW = [
    "UNREACHABLE['SortHandler.getAllEntries'] = ('no_trigger_in_app', 'SortHandler.getAllEntries is defined but has no call site in the app; the getAllEntries calls in the app bind to CryptHandler (MainFragment.java:956, EncryptDecryptUtils.java:149) and CloudHandler (MainActivity.java:1863)', 'SRC database/SortHandler.java:124', 'SOURCE')",
    "UNREACHABLE['Statvfs$Response.toString'] = ('no_trigger_in_app', 'toString is an override with no explicit call and no string conversion of Statvfs.Response in the app; HybridFile.java:655 and 708 only construct and retrieve the response', 'SRC filesystem/ssh/Statvfs.java:208-224', 'SOURCE')",
    "UNREACHABLE['Statvfs$Response.getFileSystemId'] = ('no_trigger_in_app', 'Called only from Statvfs$Response.toString (Statvfs.java:219), which has no caller; no other reference to getFileSystemId in the app', 'SRC filesystem/ssh/Statvfs.java:178', 'SOURCE')",
]

src = open(G, encoding='utf-8').read()
lines = src.split('\n')
tree = ast.parse(src)
spans = []
for st in tree.body:
    if isinstance(st, ast.Expr) and isinstance(st.value, ast.Call) and getattr(st.value.func, 'id', '') == 'e':
        a = st.value.args
        key = (a[0].value, a[1].value)
        if key in DEL:
            spans.append((st.lineno, st.end_lineno, key))
assert sorted(k for _, _, k in spans) == sorted(DEL), spans
for name in ['SortHandler.getAllEntries', 'Statvfs$Response.toString', 'Statvfs$Response.getFileSystemId']:
    assert "UNREACHABLE['%s']" % name not in src, name
for s, e_, k in sorted(spans, reverse=True):
    print('delete lines', s, e_, k)
    del lines[s - 1:e_]
text = '\n'.join(lines).rstrip('\n') + '\n\n' + '\n'.join(NEW) + '\n'
ast.parse(text)
if dry:
    sys.exit(0)
backup = BASE + 'scratch/graph_def_before_finish_20.py'
if not os.path.exists(backup):
    shutil.copy(G, backup)
open(G, 'w', encoding='utf-8').write(text)
print('written', G, 'backup', backup)
