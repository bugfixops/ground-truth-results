import ast

CAND = 'graphs/AmazeFileManager/scratch/graph_def_candidate.py'
OUT = 'graphs/AmazeFileManager/scratch/graph_def_candidate2.py'
SAVED = 'CustomNavigationView$SavedState'
DROP = {'CustomSshJConfig.initSignatureFactories', 'CustomSshJConfig.initRandomFactory',
        'FileUtils$5.launchSAF(HybridFile,HybridFile)'}

src = open(CAND, encoding='utf-8').read()
lines = src.split('\n')
tree = ast.parse(src)


def ukey(st):
    if (isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Subscript)
            and isinstance(st.targets[0].value, ast.Name) and st.targets[0].value.id == 'UNREACHABLE'
            and isinstance(st.targets[0].slice, ast.Constant)):
        return st.targets[0].slice.value
    return None


remove = set()
moved = []
dropped = []
for st in tree.body:
    k = ukey(st)
    if k is None:
        continue
    if k in DROP:
        dropped.append(k)
    elif k.startswith(SAVED):
        moved.append(k)
    else:
        continue
    for i in range(st.lineno, st.end_lineno + 1):
        remove.add(i)

moved_text = []
for st in tree.body:
    k = ukey(st)
    if k is not None and k.startswith(SAVED):
        moved_text.append('\n'.join(lines[st.lineno - 1:st.end_lineno]))

kept = [line for i, line in enumerate(lines, start=1) if i not in remove]
text = '\n'.join(kept).rstrip('\n') + '\n\n'
text += '# Saved-state entries sit below the UNREACHABLE dict rebinding, which discards earlier assignments.\n'
text += '\n\n'.join(moved_text) + '\n'
ast.parse(text)
open(OUT, 'w', encoding='utf-8').write(text)
print('dropped:', sorted(dropped))
print('moved SavedState keys:', len(moved), sorted(moved))
