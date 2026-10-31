"""AST helpers for editing graph_def.py by statement span (run with python3 -I from work/)."""
import ast
import sys


def load(path):
    src = open(path, encoding='utf-8').read()
    return src, src.split('\n'), ast.parse(src)


def unreach_assigns(path):
    """Module-level statements UNREACHABLE['key'] = ... : [(key, lineno, end_lineno)]."""
    src, lines, tree = load(path)
    out = []
    for st in tree.body:
        if isinstance(st, ast.Assign) and len(st.targets) == 1:
            t = st.targets[0]
            if isinstance(t, ast.Subscript) and isinstance(t.value, ast.Name) and t.value.id == 'UNREACHABLE':
                key = t.slice.value if isinstance(t.slice, ast.Constant) else None
                out.append((key, st.lineno, st.end_lineno))
    return out


def unreach_dict_entries(path):
    """Dict-literal entries of module-level  NAME = { 'key': (...), ... }  whose NAME starts with UNREACHABLE.
    Returns [(name, key, key_lineno, value_end_lineno)]."""
    src, lines, tree = load(path)
    out = []
    for st in tree.body:
        if isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Name):
            name = st.targets[0].id
            if name.startswith('UNREACHABLE') and isinstance(st.value, ast.Dict):
                for k, v in zip(st.value.keys, st.value.values):
                    if isinstance(k, ast.Constant):
                        out.append((name, k.value, k.lineno, v.end_lineno))
    return out


def show(path, lo, hi):
    lines = open(path, encoding='utf-8').read().split('\n')
    for i in range(lo, hi + 1):
        print('%6d| %s' % (i, lines[i - 1][:260]))


if __name__ == '__main__':
    p = sys.argv[1]
    for k, ln, end in unreach_assigns(p):
        print('ASSIGN', ln, end, k)
    for name, k, ln, end in unreach_dict_entries(p):
        print('DICT', name, ln, end, k)
