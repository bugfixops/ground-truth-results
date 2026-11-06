#!/usr/bin/env python3
"""W7 guard pre-screen (re-audit brief W7 points 1-2; Kiro, tool lead).

Usage, from the repo root:
    python3 -I tools_dev/guard_prescreen.py <App>            # writes guard_steps.csv and prints counts
    python3 -I tools_dev/guard_prescreen.py --test           # the MMEX-41 test (PayeeReportFragment.java:216-221)

1. Scope. Targets are the app's never-run methods (monkey_hit 0 and ape_hit 0 in out/sanity_check.csv) whose
   class is gui, library or state (review/TASK_NOTE.md mapping on out/methods.csv). The steps are the distinct
   edges on their best routes, without ENTERS edges and edges into a page (GUI steps are kept).
2. Pre-screen. For each step the first cited 'SRC file:line' is read in the app source
   (final_java_only/<App>/app/.../src/main/java). The step is flagged when
     - the line sits inside an if, else, switch/case, ?:, loop, try, catch or finally block of its method, or has
       a ?: on it, or comes after a return, throw, break or continue earlier in the same method; or
     - the step is a GUI step that needs a list item, a selection or an open dialog (by its trigger, gui text, src
       or dst: an item/row/child/group click, a selection or action mode, a context menu, a dialog button).
   A step without an app source line (only FW-SRC or INFERRED evidence) cannot be read: it is listed with
   flag 'no_source' and counts as flagged, so a person reads it.
Output: graphs/<App>/scratch/reaudit/guard_steps.csv with
   edge id, kind, src, dst, cited file:line, flag (yes/no/no_source), reason, guard line (the enclosing
   control statement or the earlier exit), targets (how many target methods use the step).
"""
import collections
import csv
import glob
import json
import os
import re
import sys

CONTROL = re.compile(r'\b(if|else|for|while|do|switch|try|catch|finally|case|default)\b')
EXIT = re.compile(r'\b(return|throw|break|continue)\b')
GUI_NEEDS = re.compile(r'onItemClick|onItemLongClick|onListItem|onChildClick|onGroupClick|onContextItemSelected|'
                       r'ActionMode|onActionItemClicked|selection|selected|Selection|\brow\b|\bitem\b|list item|'
                       r'long[- ]press|Dialog|dialog', re.I)
SRC_REF = re.compile(r'SRC\s+([\w/$.-]+\.java):(\d+)')


def class_of(r):
    if r['verdict'] != 'REACHABLE':
        return 'dead/config'
    if [k for k in (r['env_kinds'] or '').split(';') if k and k != 'permission']:
        return 'env'
    if r['state_kinds']:
        return 'state'
    if r['explicit_standard_route'] == 'no':
        return 'library'
    return 'gui'


class Sources:
    def __init__(self, app):
        self.by_name = collections.defaultdict(list)
        for p in glob.glob('final_java_only/%s/app/**/src/main/java/**/*.java' % app, recursive=True):
            self.by_name[os.path.basename(p)].append(p)
        self.cache = {}

    def find(self, ref):
        cands = self.by_name.get(os.path.basename(ref), [])
        if len(cands) > 1:
            suff = [c for c in cands if c.endswith('/' + ref)]
            cands = suff or cands
        return cands[0] if cands else None

    def lines(self, path):
        if path not in self.cache:
            self.cache[path] = open(path, encoding='utf-8', errors='replace').read().split('\n')
        return self.cache[path]


def strip_code(s):
    """Drop string/char literals and // comments from one line (block comments are handled by the caller)."""
    s = re.sub(r'"(\\.|[^"\\])*"', '""', s)
    s = re.sub(r"'(\\.|[^'\\])'", "''", s)
    return s.split('//', 1)[0]


def screen_line(lines, n):
    """n is 1-based. Returns (flag, reason, guard_line_no, guard_text)."""
    stack = []          # entries: [kind, line_no, text]; kind in control / method / other
    exits = []          # (depth, line_no, text) of exits inside the current method
    in_comment = False
    header = ''         # text since the last ; { or } (the statement that opens the next block)
    header_line = 0
    method_depth = None
    for i in range(1, min(n, len(lines)) + 1):
        raw = lines[i - 1]
        s = raw
        if in_comment:
            if '*/' in s:
                s = s.split('*/', 1)[1]
                in_comment = False
            else:
                continue
        while '/*' in s:
            a, b = s.split('/*', 1)
            if '*/' in b:
                s = a + ' ' + b.split('*/', 1)[1]
            else:
                s = a
                in_comment = True
        s = strip_code(s)
        if i == n:
            # the step line itself: blocks opened earlier decide; a ?: on the line also flags
            ctl = [x for x in stack[(method_depth or 0):] if x[0] in ('control', 'control-1')]
            if ctl:
                kw = CONTROL.search(ctl[-1][2])
                return 'yes', 'inside a %s block' % (kw.group(1) if kw else 'control'), ctl[-1][1], ctl[-1][2].strip()[:160]
            if re.search(r'\?[^:]*:', s) and '?' in s:
                return 'yes', 'on a ?: expression', i, raw.strip()[:160]
            if CONTROL.search(header + s.split('{')[0]) and re.search(r'\b(if|for|while|switch|case)\b', s):
                return 'yes', 'on the control statement line', i, raw.strip()[:160]
            if exits:
                kw = EXIT.search(exits[-1][2])
                return 'yes', 'after an earlier %s in the method' % (kw.group(1) if kw else 'exit'), exits[-1][1], exits[-1][2].strip()[:160]
            return 'no', 'straight-line code of its method', None, ''
        for ch_i, ch in enumerate(s):
            if ch == '{':
                txt = (header + s[:ch_i]).strip()
                if CONTROL.search(txt) or txt.endswith('->') or txt.endswith(')') and re.search(r'\b(if|for|while|switch|catch)\s*\(', txt):
                    kind = 'control' if CONTROL.search(txt) else 'other'
                elif re.search(r'\)\s*(throws [\w.,\s]+)?$', txt) and not re.search(r'\bnew\b', txt):
                    kind = 'method'
                else:
                    kind = 'other'
                kw = CONTROL.search(txt)
                stack.append([kind, header_line or i, (kw.group(0) + ' ... ' if kw else '') + txt[-200:]])
                if kind == 'method':
                    method_depth = len(stack)
                    exits = []
                header = ''
                header_line = 0
            elif ch == '}':
                if stack:
                    top = stack.pop()
                    if top[0] == 'method':
                        method_depth = None
                        exits = []
                        for j in range(len(stack) - 1, -1, -1):
                            if stack[j][0] == 'method':
                                method_depth = j + 1
                                break
                header = ''
                header_line = 0
            elif ch == ';':
                stmt = (header + s[:ch_i]).strip()
                if method_depth is not None and EXIT.search(stmt):
                    exits.append((len(stack), i, raw))
                header = ''
                header_line = 0
        rest = re.split(r'[;{}]', s)[-1]
        if rest.strip():
            if not header:
                header_line = i
            header += ' ' + rest
        # a braceless if/else/for/while: the next statement is guarded
        if re.match(r'\s*(if|else|for|while)\b', s) and not s.rstrip().endswith(('{', ';')) and method_depth is not None:
            stack.append(['control-1', i, s.strip()])
        elif stack and stack[-1][0] == 'control-1' and s.strip() and i < n:
            if s.rstrip().endswith(';'):
                stack.pop()
    return 'no_source', 'line beyond the end of the file', None, ''


def prescreen(app):
    g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % app)[0], encoding='utf-8'))
    E = {e['id']: e for e in g['edges']}
    screens = set(g['screens']) if isinstance(g['screens'], list) and g['screens'] and isinstance(g['screens'][0], str) else {
        (s if isinstance(s, str) else s.get('id')) for s in g['screens']}
    sanity = {r['method']: r for r in csv.DictReader(open('graphs/%s/out/sanity_check.csv' % app, encoding='utf-8'))}
    rows = list(csv.DictReader(open('graphs/%s/out/methods.csv' % app, encoding='utf-8')))
    targets = []
    for r in rows:
        s = sanity.get(r['method'])
        if s is None:
            continue
        if str(s.get('monkey_hit', '0')) not in ('0', '') or str(s.get('ape_hit', '0')) not in ('0', ''):
            continue
        if class_of(r) in ('gui', 'library', 'state'):
            targets.append(r)
    use = collections.Counter()
    for r in targets:
        for i in (r['route_edge_ids'] or '').split():
            e = E[i]
            if e['kind'] == 'ENTERS' or e['dst'] in screens:
                continue
            use[i] += 1
    src = Sources(app)
    out = []
    for i, n in use.most_common():
        e = E[i]
        m = SRC_REF.search(e.get('evidence') or '')
        ref = '%s:%s' % (m.group(1), m.group(2)) if m else ''
        flag, reason, gl, gt = 'no_source', 'no app source line cited (FW-SRC or INFERRED only)', None, ''
        if m:
            path = src.find(m.group(1))
            if path:
                flag, reason, gl, gt = screen_line(src.lines(path), int(m.group(2)))
            else:
                reason = 'cited file not found in the app source'
        if flag == 'no' and e['kind'] == 'GUI':
            t = ' '.join(str(x) for x in (e.get('trigger'), ' '.join(e.get('gui') or []), e['src'], e['dst']))
            if GUI_NEEDS.search(t):
                flag, reason = 'yes', 'GUI step on a list item, selection or dialog'
        out.append([i, e['kind'], e['src'], e['dst'], ref, flag, reason, gl or '', gt, n])
    return targets, out


def main():
    if sys.argv[1] == '--test':
        lines = Sources('MMEX')
        p = lines.find('PayeeReportFragment.java')
        L = lines.lines(p)
        res = [screen_line(L, k) for k in range(216, 222)]
        for k, r in zip(range(216, 222), res):
            print(k, r[:3], L[k - 1].strip()[:80])
        ok = any(r[0] == 'yes' for r in res)
        print('MMEX-41 test (PayeeReportFragment.java:216-221 flagged):', 'PASS' if ok else 'FAIL')
        return 0 if ok else 1
    app = sys.argv[1]
    targets, out = prescreen(app)
    path = 'graphs/%s/scratch/reaudit/guard_steps.csv' % app
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['edge_id', 'kind', 'src', 'dst', 'cited', 'flag', 'reason', 'guard_line', 'guard_text', 'targets'])
        w.writerows(out)
    c = collections.Counter(o[5] for o in out)
    files = {o[4].split(':')[0] for o in out if o[4]}
    print('%s: targets %d, code steps %d, source files %d, flagged %d, unflagged %d, no_source %d'
          % (app, len(targets), len(out), len(files), c['yes'], c['no'], c['no_source']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
