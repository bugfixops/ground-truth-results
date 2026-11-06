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
            meth = [x for x in stack if x[0] == 'method']
            screen_line.last_method = meth[-1][2] if meth else ''
            # The step line itself. Record EVERY guard of the line, not only the innermost block (reviewer
            # finding on round 1): all enclosing control blocks of its method (outermost first), a ?: or a
            # control statement on the line, and every earlier exit in the method.
            guards = []
            for x in stack[(method_depth or 0):]:
                if x[0] in ('control', 'control-1'):
                    kw = CONTROL.search(x[2])
                    guards.append((kw.group(1) if kw else 'control', x[1], x[2].strip()[:120]))
            if re.search(r'\?[^:]*:', s) and '?' in s:
                guards.append(('?:', i, raw.strip()[:120]))
            if CONTROL.search(header + s.split('{')[0]) and re.search(r'\b(if|for|while|switch|case)\b', s):
                kw = re.search(r'\b(if|for|while|switch|case)\b', s)
                guards.append((kw.group(1) + ' (on the line)', i, raw.strip()[:120]))
            for _d, ln, txt in exits:
                kw = EXIT.search(txt)
                guards.append(('earlier ' + (kw.group(1) if kw else 'exit'), ln, txt.strip()[:120]))
            if not guards:
                return 'no', 'straight-line code of its method', None, ''
            kinds = [g[0] for g in guards]
            text = ' || '.join('%s@%d: %s' % g for g in guards)
            if all(k in ('try', 'finally') for k in kinds):
                # the only enclosing blocks are try/finally bodies, which run on the normal path
                return 'yes', 'only inside try/finally blocks', guards[-1][1], text
            real = [g for g in guards if g[0] not in ('try', 'finally')]
            return 'yes', 'guarded: ' + ', '.join(k for k in kinds), real[-1][1], text
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


def method_name(header):
    """The name of the method whose header text is given (the identifier before its parameter list)."""
    h = re.sub(r'\([^()]*\)', '()', header or '')
    m = re.search(r'([A-Za-z_$][\w$]*)\s*\(\)\s*(throws [\w.,\s]+)?$', h.strip())
    return m.group(1) if m else ''


def src_method_name(src):
    """'Foo$1.onBindViewHolder@X' -> 'onBindViewHolder'; '' for constructors, lambdas and generated names."""
    n = src.split('@')[0].split('(')[0].split('.')[-1]
    return '' if n.startswith(('<', 'lambda$', 'access$')) else n


def method_body(lines, name):
    """(start, end) 1-based line range of the first method declaration called name in the file, or None."""
    decl = re.compile(r'^\s*(public|protected|private|static|final|synchronized|abstract|@\w+|\s)*[\w<>\[\],.? ]+\s+'
                      + re.escape(name) + r'\s*\(')
    for i, l in enumerate(lines, 1):
        if decl.search(l) and not l.rstrip().endswith(';'):
            depth, seen = 0, False
            for j in range(i, len(lines) + 1):
                t = strip_code(lines[j - 1])
                depth += t.count('{') - t.count('}')
                seen = seen or '{' in t
                if seen and depth <= 0:
                    return i, j
            return None
    return None


def helper_level(lines, n, src, flag, reason, gl, gt):
    """Review 2 (Kiro): follow one helper-call level. When the cited line of a step sits in a helper method, not in
    the step's source method, the call of that helper in the source method is screened too, and its guards are
    added to the step's guards (the reviewer's Q-W8-2 finding: RecyclerAdapter.onBindViewHolder ->
    GlideRequests.load(Integer) cited a line in showRoundedThumbnail)."""
    helper = method_name(getattr(screen_line, 'last_method', ''))
    own = src_method_name(src)
    if not helper or not own or helper == own:
        return flag, reason, gl, gt
    body = method_body(lines, own)
    if not body:
        return flag, reason, gl, gt
    call = re.compile(r'\b' + re.escape(helper) + r'\s*\(')
    sites = [k for k in range(body[0] + 1, body[1] + 1) if call.search(strip_code(lines[k - 1]))]
    extra = []
    for k in sites:
        f2, r2, g2, t2 = screen_line(lines, k)
        if f2 == 'yes':
            extra.append((k, r2, g2, t2))
    if not extra:
        return flag, reason, gl, gt
    k, r2, g2, t2 = extra[0]
    text = ' || '.join(x for x in (gt, 'helper %s called at %d: %s' % (helper, k, t2)) if x)
    why = 'helper-call guarded (%s called from %s at line %d: %s)' % (helper, own, k, r2)
    if flag == 'yes':
        why = reason + '; ' + why
    return 'yes', why, gl or g2, text


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
                flag, reason, gl, gt = helper_level(src.lines(path), int(m.group(2)), e['src'], flag, reason, gl, gt)
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
    if sys.argv[1] == '--rescreen':
        # Re-screen the step list of an existing guard_steps.csv with the current rule (the list itself was taken
        # on the pre-W7 build; re-deriving it on a later build would change the scope).
        app = sys.argv[2]
        path = 'graphs/%s/scratch/reaudit/guard_steps.csv' % app
        rows = list(csv.DictReader(open(path, encoding='utf-8')))
        src = Sources(app)
        for r in rows:
            m = re.match(r'([\w/$.-]+\.java):(\d+)$', r['cited'] or '')
            if not m:
                continue
            p = src.find(m.group(1))
            if not p:
                continue
            flag, reason, gl, gt = screen_line(src.lines(p), int(m.group(2)))
            flag, reason, gl, gt = helper_level(src.lines(p), int(m.group(2)), r['src'], flag, reason, gl, gt)
            if flag == 'no' and r['kind'] == 'GUI' and GUI_NEEDS.search(' '.join((r['src'], r['dst']))):
                flag, reason = 'yes', 'GUI step on a list item, selection or dialog'
            if flag == 'no' and r['reason'] == 'GUI step on a list item, selection or dialog':
                flag, reason = 'yes', r['reason']
            r['flag'], r['reason'], r['guard_line'], r['guard_text'] = flag, reason, gl or '', gt
        with open(path, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        c = collections.Counter(r['flag'] for r in rows)
        t = sum(1 for r in rows if r['reason'] == 'only inside try/finally blocks')
        print('%s: rescreened %d steps: flagged %d (try/finally only %d), unflagged %d, no_source %d'
              % (app, len(rows), c['yes'], t, c['no'], c['no_source']))
        return 0
    if sys.argv[1] == '--merge':
        # Review 2 (Kiro): re-run the pre-screen on the CURRENT build and merge it into guard_steps.csv. Rows already
        # listed keep their place (and their judgments, which are keyed by edge id) and are re-screened with the
        # helper-call level; steps on the current best routes of the targets that the pre-W7 list did not have are
        # appended (their targets count is from the current build).
        app = sys.argv[2]
        path = 'graphs/%s/scratch/reaudit/guard_steps.csv' % app
        rows = list(csv.DictReader(open(path, encoding='utf-8')))
        have = {r['edge_id'] for r in rows}
        keys = {(r['kind'], r['src'], r['dst']) for r in rows}
        src = Sources(app)
        changed = 0
        for r in rows:
            m = re.match(r'([\w/$.-]+\.java):(\d+)$', r['cited'] or '')
            if not m:
                continue
            p = src.find(m.group(1))
            if not p:
                continue
            flag, reason, gl, gt = screen_line(src.lines(p), int(m.group(2)))
            flag, reason, gl, gt = helper_level(src.lines(p), int(m.group(2)), r['src'], flag, reason, gl, gt)
            if flag == 'no' and r['kind'] == 'GUI' and GUI_NEEDS.search(' '.join((r['src'], r['dst']))):
                flag, reason = 'yes', 'GUI step on a list item, selection or dialog'
            if flag == 'no' and r['reason'] == 'GUI step on a list item, selection or dialog':
                flag, reason = 'yes', r['reason']
            if (flag, reason) != (r['flag'], r['reason']):
                changed += 1
            r['flag'], r['reason'], r['guard_line'], r['guard_text'] = flag, reason, gl or '', gt
        _t, out = prescreen(app)
        added = 0
        for o in out:
            if o[0] in have or (o[1], o[2], o[3]) in keys:
                continue
            rows.append(dict(zip(['edge_id', 'kind', 'src', 'dst', 'cited', 'flag', 'reason', 'guard_line',
                                  'guard_text', 'targets'], [str(x) for x in o])))
            added += 1
        with open(path, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        c = collections.Counter(r['flag'] for r in rows)
        print('%s: merged: %d rows re-screened with a changed flag or reason, %d new steps from the current build; '
              'flagged %d, unflagged %d, no_source %d' % (app, changed, added, c['yes'], c['no'], c['no_source']))
        return 0
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
