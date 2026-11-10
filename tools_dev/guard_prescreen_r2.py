#!/usr/bin/env python3
"""Round 2 guard pre-screen (Kiro, 2026-11-10): the kinds of condition the W7 pre-screen did not show.

Round 1 of the tuning-half measurement (review/rounds/1/adjudication.csv) found 8 never-run methods labelled gui or
library whose route needs stored state. The W7 pre-screen (tools_dev/guard_prescreen.py) read only the guard blocks
around the cited line of a step, cut each guard text at 120 characters and its first line, and did not look at the
condition that makes the TRIGGER of a GUI step available. This screen adds four kinds, for every step on the best
route of every never-run method whose class is gui or library (review/TASK_NOTE.md mapping on out/methods.csv):

  cond_chain   the cited call sits inside a multi-clause condition (if/while/return/?:) after an && or || clause, or the
               condition spans several lines; the full condition is printed (Aegis-49: the ON_STOP check was shown,
               the lock-on-minimize setting on the next line was not).
  setting      the step's condition (the W7 guard text or the full condition) reads a stored setting: a preference
               read, or a field the same file assigns from a preference read (its default is printed).
  visibility   the step's trigger (a view, a menu item or a preference named near the cited line) is hidden or
               disabled somewhere: setVisible/setVisibility/setEnabled on it in the app source, or
               android:visible/enabled="false" / android:dependency on it in res/ (AnkiDroid-01, -15; Aegis-05).
  stored_row   the step's condition or callee needs a stored row or record: an earlier exit or guard that tests a
               validation, a load by id, a cursor, a list size or a null record, or a step into load()/first()/
               validateData() (MMEX-17, -21); or the step is an item callback of a list (an adapter, an item lookup)
               (LibreTorrent-49).

Usage, from the repo root:  python3 -I tools_dev/guard_prescreen_r2.py <App>
Writes graphs/<App>/scratch/reaudit/guard_steps_r2.csv: step, kind, src, dst, cited, flags, evidence (what was found,
with file:line), w7 decision of the same src/dst/kind, targets (how many targets use the step).
Flagged steps are judged from the printed source (tools_dev/guard_judge.py --r2) into
graphs/<App>/scratch/reaudit/r2_judged.csv; the app's graph_def.py applies its STATE and ENV rows like w7_judged.csv."""
import collections
import csv
import glob
import json
import os
import re
import sys

G = {}
exec(open('tools_dev/guard_prescreen.py', encoding='utf-8').read().split("\ndef main():")[0], G)
Sources, strip_code, class_of = G['Sources'], G['strip_code'], G['class_of']

SRC_ANY = re.compile(r'(?:SRC\s+)?([\w/$.-]+\.java):(\d+)')
PREF = re.compile(r'getBoolean\(|getString\(|getInt\(|getLong\(|getStringSet\(|SharedPreferences|getSharedPrefs|'
                  r'\b[Pp]refs?\b|[Pp]references\b|\bmPref\w*|\bSettings\w*\.|AppSettings|isAutoLock\w*\(|'
                  r'\bis\w+Enabled\(')
STORED = re.compile(r'validate\w*\(|isValid\w*\(|\bload\w*\(|moveToFirst\(|moveToNext\(|getCount\(\)|isEmpty\(\)|'
                    r'\.size\(\)\s*[=<>!]|hasId\(|exists\(|NOT_SET|containsKey\(')
STORED_DST = re.compile(r'\.(load|first|validateData|loadRecurringTransaction|getById|findById)$')
ITEM_CB = re.compile(r'ItemLookup|ItemDetails|onBindViewHolder|ViewHolder\.|\$ViewHolder|getItemId$|'
                     r'onItemClick|onItemLongClick|onListItemClick|onChildClick|onGroupClick')
VIS = re.compile(r'setVisible\(|setVisibility\(|setEnabled\(|setDependency\(|setShowAsAction\(|setFocusable\w*\(')
FIELD = re.compile(r'\b(m[A-Z]\w*|_[a-z]\w*)\b')


def cond_at(lines, n, callee=''):
    """The full condition that holds the call of callee on line n, when the call sits inside a parenthesised if/while
    condition or a return/?: expression and comes after an && or || clause (or the condition spans several lines).
    Returns (start_line, full condition text, True) or None."""
    s_n = strip_code(lines[n - 1])
    pos = s_n.find(callee + '(') if callee and callee + '(' in s_n else -1
    upto = s_n[:pos] if pos >= 0 else s_n
    for k in range(n, max(0, n - 8), -1):
        head = strip_code(lines[k - 1])
        if k < n and re.search(r'[;{}]\s*$', head):
            break
        m = re.search(r'\b(if|while)\s*\(|\breturn\b|\?', head)
        if not m:
            continue
        before_txt = ' '.join(strip_code(lines[j - 1]).strip() for j in range(k, n)) + ' ' + upto
        start = before_txt.find(m.group(0))
        seg = before_txt[start:]
        depth = seg.count('(') - seg.count(')')
        if m.group(1) and depth <= 0:
            continue
        if not re.search(r'&&|\|\||\?', seg[len(m.group(0)):]) and k == n:
            return None
        full = ' '.join(strip_code(lines[j - 1]).strip() for j in range(k, min(len(lines), n + 4)))
        f = full[full.find(m.group(0)):]
        d, cut = 0, len(f)
        for idx, ch in enumerate(f):
            d += (ch == '(') - (ch == ')')
            if m.group(1) and d == 0 and idx > len(m.group(0)):
                cut = idx + 1
                break
        if re.search(r'&&|\|\|', seg) or k < n:
            return k, f[:cut][:400], True
        return None
    return None


def refs_of(evidence):
    """(file, line) pairs of the step's SRC citations, ranges and comma lists expanded to their first and last line."""
    out = []
    for m in re.finditer(r'(?:SRC\s+)?([\w/$.-]+\.java):([\d ,\-]+)', evidence or ''):
        f = m.group(1)
        for part in m.group(2).split(','):
            nums = [int(x) for x in re.findall(r'\d+', part)]
            if nums:
                out.append((f, nums[0], nums[-1]))
    return out


def ids_near(lines, n):
    win = ' '.join(lines[max(0, n - 3):min(len(lines), n + 2)])
    ids = set(re.findall(r'R\.id\.(\w+)', win))
    ids |= set(re.findall(r'findPreference\(\s*(?:getString\()?\s*(?:R\.string\.)?"?(\w+)', win))
    ids |= set(re.findall(r'"(pref_\w+)"', win))
    return ids


class Res:
    def __init__(self, app):
        self.java = glob.glob('final_java_only/%s/app/**/src/main/java/**/*.java' % app, recursive=True)
        self.xml = [p for p in glob.glob('final_java_only/%s/app/**/src/main/res/**/*.xml' % app, recursive=True)
                    if re.search(r'/(layout|menu|xml)[\w-]*/', p)]
        self._t = {}

    def text(self, p):
        if p not in self._t:
            self._t[p] = open(p, encoding='utf-8', errors='replace').read().split('\n')
        return self._t[p]

    def visibility(self, ident, own_file=None):
        """file:line hits that hide, disable or make the element named ident depend on another one."""
        hits = []
        files = [own_file] if own_file else []
        for p in files + [q for q in self.java if q != own_file and ident in open(q, encoding='utf-8', errors='replace').read()][:12]:
            L = self.text(p)
            fields = {m.group(1) for l in L for m in [re.search(r'(\w+)\s*=\s*(?:\(\w+\)\s*)?\w*\.?(?:findViewById|findItem|findPreference)\([^)]*\b%s\b' % re.escape(ident), l)] if m}
            for i, l in enumerate(L, 1):
                c = strip_code(l)
                if VIS.search(c) and (re.search(r'\b%s\b' % re.escape(ident), c) or any(re.search(r'\b%s\s*\.' % re.escape(f), c) for f in fields)):
                    if re.search(r'setVisible\(\s*true\s*\)|setVisibility\(\s*View\.VISIBLE\s*\)|setEnabled\(\s*true\s*\)', c):
                        continue
                    hits.append('%s:%d: %s' % (os.path.basename(p), i, l.strip()[:110]))
        for p in self.xml:
            L = self.text(p)
            for i, l in enumerate(L, 1):
                if re.search(r'(@\+id/|android:key="|key=")%s"' % re.escape(ident), l):
                    blk = ' '.join(L[i - 3:i + 8])
                    m = re.search(r'android:(visible|enabled)="false"|android:dependency="(\w+)"', blk)
                    if m:
                        hits.append('%s:%d: %s' % (os.path.relpath(p).split('/res/')[-1], i, m.group(0)))
        return hits[:6]


def setting_fields(L, cond):
    out = []
    for f in set(FIELD.findall(cond)):
        for i, l in enumerate(L, 1):
            c = strip_code(l)
            if re.search(r'\b%s\s*=[^=]' % re.escape(f), c) and PREF.search(c):
                d = re.search(r'getBoolean\([^,]+,\s*(\w+)\)', c)
                out.append('%s set from a setting at :%d%s: %s' % (f, i, ' (default %s)' % d.group(1) if d else '', l.strip()[:120]))
                break
    return out


def screen(app):
    g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % app)[0], encoding='utf-8'))
    E = {e['id']: e for e in g['edges']}
    sanity = {r['method']: r for r in csv.DictReader(open('graphs/%s/out/sanity_check.csv' % app, encoding='utf-8'))}
    S = 'graphs/%s/scratch/reaudit/' % app
    w7 = {}
    for r in csv.DictReader(open(S + 'w7_judged.csv', encoding='utf-8')):
        w7.setdefault((r['src'], r['dst'], r['kind']), r['decision'])
    old = {r['edge_id']: r for r in csv.DictReader(open(S + 'guard_steps.csv', encoding='utf-8'))}
    old_k = {(r['src'], r['dst'], r['kind']): r for r in old.values()}
    use = collections.Counter()
    ntarget = 0
    for r in csv.DictReader(open('graphs/%s/out/methods.csv' % app, encoding='utf-8')):
        s = sanity.get(r['method'])
        if s is None or str(s.get('monkey_hit', '0')) not in ('0', '') or str(s.get('ape_hit', '0')) not in ('0', ''):
            continue
        if class_of(r) not in ('gui', 'library'):
            continue
        ntarget += 1
        for i in (r['route_edge_ids'] or '').split():
            use[i] += 1
    src = Sources(app)
    res = Res(app)
    out = []
    for i, n in use.most_common():
        e = E[i]
        if e['src'] == 'S_ENTRY' or e['kind'] in ('LIFECYCLE',):
            continue
        flags, ev = [], []
        refs = refs_of(e.get('evidence'))[:4]
        cited = '%s:%d' % refs[0][:2] if refs else ''
        callee = e['dst'].split('@')[0].split('(')[0].split('.')[-1]
        callee = '' if callee.startswith(('<', 'lambda$')) else callee
        trig = e['kind'] in ('GUI', 'FRAMEWORK', 'ENTERS', 'SYSTEM') or bool(re.search(
            r'\.(onOptionsItemSelected|onContextItemSelected|onPreference\w*|onClick|onMenuItemClick)$', e['src'].split('@')[0]))
        guard, cond, seen_ids = '', '', set()
        for k, (f, ln, ln2) in enumerate(refs):
            p = src.find(f)
            if not p:
                continue
            L = src.lines(p)
            if ln > len(L):
                continue
            if k == 0:
                gflag, _r, _gl, gt = G['screen_line'](L, ln)
                guard = gt if gflag == 'yes' else ''
                c = cond_at(L, ln, callee)
                if c:
                    flags.append('cond_chain')
                    cond = c[1]
                    ev.append('condition from %s:%d: %s' % (os.path.basename(p), c[0], c[1][:300]))
                alltext = guard + ' ' + cond
                if PREF.search(alltext):
                    flags.append('setting')
                    ev.append('setting read in the condition')
                sf = setting_fields(L, alltext)
                if sf:
                    if 'setting' not in flags:
                        flags.append('setting')
                    ev.extend(sf[:3])
                st = sorted(set(m.group(0) for m in STORED.finditer(alltext)))
                if st:
                    flags.append('stored_row')
                    ev.append('condition tests a stored row or a validation: %s' % ', '.join(st)[:160])
            if trig:
                # the trigger's view, menu item or preference: named within the cited lines (+-15 lines)
                lo, hi = max(1, ln - 15), min(len(L), ln2 + 15)
                win = L[lo - 1:hi]
                ids = set()
                for l in win:
                    ids |= set(re.findall(r'R\.id\.(\w+)', l))
                    ids |= set(re.findall(r'findPreference\(\s*(?:getString\()?\s*(?:R\.string\.)?"?(\w+)', l))
                    ids |= set(re.findall(r'"(pref_\w+)"', l))
                for ident in sorted(ids - seen_ids)[:6]:
                    seen_ids.add(ident)
                    h = res.visibility(ident, p)
                    if h:
                        if 'visibility' not in flags:
                            flags.append('visibility')
                        ev.append('%s: %s' % (ident, ' | '.join(h)))
                # a setter in the cited lines whose argument is a field set from a setting (focusable, visible, enabled)
                for j, l in enumerate(win, lo):
                    if VIS.search(strip_code(l)):
                        sf = setting_fields(L, l.split('(', 1)[-1])
                        if sf:
                            if 'setting' not in flags:
                                flags.append('setting')
                            ev.append(':%d %s; %s' % (j, l.strip()[:90], sf[0]))
        if STORED_DST.search(e['dst'].split('@')[0]) and 'stored_row' not in flags:
            flags.append('stored_row')
            ev.append('step into a load/first/validate method')
        if ITEM_CB.search(e['dst']) and e['kind'] in ('FRAMEWORK', 'GUI', 'CALL') and 'stored_row' not in flags:
            flags.append('stored_row')
            ev.append('item callback of a list: needs an item in the list')
        if not flags:
            continue
        out.append([i, e['kind'], e['src'], e['dst'], cited, '+'.join(flags), ' || '.join(ev)[:900],
                    w7.get((e['src'], e['dst'], e['kind']), ''), n])
    path = S + 'guard_steps_r2.csv'
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['step', 'kind', 'src', 'dst', 'cited', 'flags', 'evidence', 'w7_decision', 'targets'])
        w.writerows(out)
    c = collections.Counter(k for o in out for k in o[5].split('+'))
    print('%s: targets %d, route steps %d, flagged %d (%s); flagged uses %d of %d' % (
        app, ntarget, len(use), len(out), ', '.join('%s %d' % kv for kv in sorted(c.items())),
        sum(o[8] for o in out), sum(use.values())))


if __name__ == '__main__':
    screen(sys.argv[1])
