import ast, os, re, subprocess, sys

WORK = '/Users/darshan/Desktop/yang/work'
APP = os.path.join(WORK, 'final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main')
ROOTS = [os.path.join(APP, 'java'), APP, os.path.join(WORK, 'fw_src/android-8.1.0_r1'), os.path.join(WORK, 'final_java_only/AnkiDroid/app/AnkiDroid-#4200')]
CITE = re.compile(r'((?:[\w$.\-]+/)*[\w$.\-]+\.(?:java|xml|kt))\s?:\s?(\d+)(?:\s?-\s?(\d+))?')
STATUS_LAST = re.compile(r'^STATUS: DONE \d{2}:\d{2}$')
STATUS_FIRST = re.compile(r'^STATUS: RUNNING \d{2}:\d{2}$')


def cited_ok(text):
    hits = CITE.findall(text)
    if not hits:
        return 'no file:line'
    for f, a, b in hits:
        lo, hi = int(a), int(b or a)
        path = None
        if f.startswith('fw_src/android-8.1.0_r1/'):
            f = f[len('fw_src/android-8.1.0_r1/'):]
        for r in ROOTS:
            cand = os.path.join(r, f)
            if os.path.isfile(cand):
                path = cand
                break
        if path is None:
            return 'file not found: ' + f
        n = sum(1 for _ in open(path, encoding='utf-8', errors='replace'))
        if not (1 <= lo <= hi <= n):
            return 'range %d-%d outside %s (%d lines)' % (lo, hi, f, n)
    return None


def py_items(path):
    tree = ast.parse(open(path, encoding='utf-8').read(), path)
    items, bad = [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ('e', 'gui'):
            a = node.args
            if node.func.id == 'gui':
                kind = 'GUI'
                need = 2
            else:
                kind = None
                need = 3
            if len(a) < need or not all(isinstance(x, ast.Constant) and isinstance(x.value, str) for x in a[:need]):
                bad.append('%s() without constant src/dst at line %d' % (node.func.id, node.lineno))
                continue
            if kind is None:
                kind = a[2].value
            items.append(('EDGE', '%s -> %s (%s)' % (a[0].value, a[1].value, kind)))
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            t = node.targets[0]
            if isinstance(t, ast.Subscript) and isinstance(t.value, ast.Name) and t.value.id == 'UNREACHABLE':
                if isinstance(t.slice, ast.Constant):
                    items.append(('UNREACHABLE', t.slice.value))
                else:
                    bad.append('UNREACHABLE key not a constant at line %d' % node.lineno)
    return items, bad


def md_rows(path):
    rows = []
    for line in open(path, encoding='utf-8').read().splitlines():
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 5 or cells[0] in ('item', '') or set(cells[0]) <= set('-: '):
            continue
        rows.append(cells)
    return rows


def main(part_py, part_md):
    problems = []
    try:
        compile(open(part_py, encoding='utf-8').read(), part_py, 'exec')
    except SyntaxError as ex:
        problems.append('compile failed: %s' % ex)
    items, bad = py_items(part_py)
    problems += bad
    rows = md_rows(part_md)
    by_item = {}
    for cells in rows:
        by_item.setdefault(cells[0], []).append(cells)
    item_keys = {k for _, k in items}
    for kind, key in items:
        if key not in by_item:
            problems.append('no row for %s %s' % (kind, key))
    for cells in rows:
        item, label = cells[0], cells[1]
        if label not in ('REACHABLE', 'UNREACHABLE', 'EDGE'):
            problems.append('bad label "%s" for %s' % (label, item))
        if label != 'REACHABLE' and item not in item_keys:
            problems.append('row without a matching entry in the .py: %s' % item)
        msg = cited_ok(cells[4])
        if msg:
            problems.append('row %s: %s' % (item, msg))
    lines = [l.strip() for l in open(part_md, encoding='utf-8').read().splitlines() if l.strip()]
    if not lines or not STATUS_FIRST.match(lines[0]):
        problems.append('first line is not "STATUS: RUNNING HH:MM"')
    if not lines or not STATUS_LAST.match(lines[-1]):
        problems.append('last line is not "STATUS: DONE HH:MM"')
    print('entries %d, rows %d, problems %d' % (len(items), len(rows), len(problems)))
    for p in problems:
        print('PROBLEM', p)
    return 0 if not problems else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2]))
