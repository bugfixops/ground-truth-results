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
                    # round 3 (AmazeFileManager-colour finding): a key named by a constant of another class
                    # (findPreference(PreferencesConstants.PREFERENCE_SKIN), case PreferencesConstants.PREFERENCE_SKIN:)
                    ids |= set(re.findall(r'findPreference\(\s*(?:getString\()?\s*(?:[\w$]+\.)+([A-Z][A-Z0-9_]{2,})', l))
                    ids |= set(re.findall(r'\bcase\s+(?:[\w$]+\.)*([A-Z][A-Z0-9_]{2,})\s*:', l))
                    ids |= set(re.findall(r'"(pref_\w+)"', l))
                ids -= {'PreferencesConstants', 'PreferenceConstants', 'R'}
                for ident in sorted(ids - seen_ids)[:10]:
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


# ======================================================================== round 3
# Round 3 (Kiro, 2026-11-10): a blind check of 40 random gui-labelled never-run methods found about 1 in 5 with a gate
# the graph lacks: a setting that must be non-default, an empty list or cursor, an early return on empty data, a boolean
# field that only an earlier gated action sets, a reflection edge. --r3 screens the best routes of every never-run
# method labelled gui for these kinds (general rules over the source):
#   setting      the step's condition, or a setVisible/setEnabled/setVisibility of its trigger, depends on a stored
#                setting: a preference read, or a local or field computed from one (its default is printed)
#   empty_data   the cited call runs inside a loop over a collection or cursor (for (x : c), while (moveToNext/hasNext),
#                forEach), inside a per-item callback (adapter binding, item lookup), after a non-empty check
#                (getCount() > 0, !isEmpty(), size() > 0, moveToFirst()), or after an early return on empty data
#   flag_field   the step's condition reads a boolean field whose declaration is false (or unset) and that only other
#                methods set true (the assignments are printed: the earlier action that sets it)
#   reflection   the cited lines create the callee by reflection (newInstance, Class.forName, getDeclaredConstructor,
#                a Class<?> argument), or the edge is non_standard
# Baselines (review/TASK_NOTE.md): Aegis a vault with 2 entries; MMEX one account and nothing else; AnkiDroid the
# sample deck; LibreTorrent and AmazeFileManager nothing. The flagged steps are judged into r3_judged.csv.
LOOP = re.compile(r'\bfor\s*\([^;]*:\s*[^)]+\)|\bwhile\s*\([^)]*(moveToNext|hasNext|moveToPosition)|\.forEach\s*\(|'
                  r'\.stream\(\)|\bfor\s*\(\s*int\s+\w+\s*=\s*0\s*;\s*\w+\s*<\s*[\w.]+\.(size|length|getCount)\(')
NONEMPTY = re.compile(r'getCount\(\)\s*(>|!=)\s*0|!\s*[\w.()]+\.isEmpty\(\)|\.size\(\)\s*(>|!=)\s*0|moveToFirst\(\)|'
                      r'length\s*>\s*0|\.size\(\)\s*>=\s*1')
EMPTYRET = re.compile(r'(isEmpty\(\)|getCount\(\)\s*(==|<=)\s*0|\.size\(\)\s*(==|<=|<)\s*[01]|\b[cC]ursor\w*\s*==\s*null|'
                      r'!\s*\w*[cC]ursor\w*\.moveToFirst\(\))[^;{]*\)\s*(\{\s*)?return\b')
# newInstance() on a Class object (X.class.newInstance(), cls.newInstance()), not a static factory newInstance(...)
REFLECT = re.compile(r'\.class\s*\.\s*newInstance\s*\(|\b\w*(?:[Cc]lass|clazz|cls)\w*\s*\.\s*newInstance\s*\(\s*\)|'
                     r'Class\.forName\s*\(|getDeclaredConstructor\s*\(|\.getConstructor\s*\(')
NOT_SETTING = re.compile(r'getArguments\(\)|savedInstanceState|getIntent\(\)|getExtras\(\)|\bobj\.|\bjson\w*\.|getJSON')
PREF_READ = re.compile(r'getBoolean\(|getString\(|getInt\(|getLong\(|getStringSet\(|getSharedPreferences|'
                       r'PreferenceManager|sharedPref|mPrefs?\b|_prefs\b|Settings\(\)|\bget\w*Settings\(\)')


def method_of(L, n):
    """(start, end) of the method around line n: the nearest header above n with its brace-matched end."""
    for s in range(n, max(0, n - 400), -1):
        l = strip_code(L[s - 1])
        if re.search(r'^\s*(public|protected|private|static|final|synchronized|@\w+|\s)*[\w<>\[\],.? ]+\s+\w+\s*\([^;]*\)?\s*'
                     r'(throws [\w.,\s]+)?\{?\s*$', l) and not re.search(r'\b(if|for|while|switch|catch|return|new|else)\b', l):
            depth, seen = 0, False
            for j in range(s, min(len(L), s + 2000) + 1):
                t = strip_code(L[j - 1])
                depth += t.count('{') - t.count('}')
                seen = seen or '{' in t
                if seen and depth <= 0:
                    return (s, j) if j >= n else None
            return None
    return None


def setting_arg(L, line):
    """Names in the argument of a setter line that the file computes from a stored setting."""
    arg = line.split('(', 1)[-1]
    hits = []
    here = method_of(L, next((k for k, x in enumerate(L, 1) if x == line), 1))
    lo, hi = (here if here else (1, len(L)))
    for name in set(re.findall(r'\b([a-z_]\w*)\b', arg)) - {'true', 'false', 'null', 'view', 'menu', 'item', 'id'}:
        for i, l in enumerate(L[lo - 1:hi], lo):
            c = strip_code(l)
            if re.search(r'\b%s\s*=(?!=)' % re.escape(name), c):
                blk = ' '.join(strip_code(x) for x in L[i - 1:i + 2])
                if PREF_READ.search(blk) and not NOT_SETTING.search(blk):
                    d = re.search(r'get(?:Boolean|Int|String)\([^,]+,\s*([\w.]+)\)', blk)
                    hits.append('%s computed from a setting at :%d%s' % (name, i, ' (default %s)' % d.group(1) if d else ''))
                    break
    return hits


def flag_fields(L, cond, here):
    """Boolean fields read in cond that are false by default and set true only outside the method range here."""
    out = []
    for f in set(re.findall(r'\b(_[a-z]\w*|m[A-Z]\w*|is[A-Z]\w*)\b', cond)):
        decl = [i for i, l in enumerate(L, 1) if re.search(r'\bboolean\s+%s\s*(=\s*false\s*)?;' % re.escape(f), strip_code(l))]
        if not decl:
            continue
        sets = [i for i, l in enumerate(L, 1) if re.search(r'\b%s\s*=\s*(true|[^=;][^;]*)\s*;' % re.escape(f), strip_code(l))
                and not re.search(r'\bboolean\s+%s' % re.escape(f), l)]
        outside = [i for i in sets if not (here and here[0] <= i <= here[1])]
        if outside:
            out.append('%s (boolean, false by default at :%d) is set at :%s' % (f, decl[0], ','.join(map(str, outside[:6]))))
    return out


ACCESSOR = re.compile(r'\b\w*(?:[Pp]refs?|[Pp]references|[Ss]ettings|[Rr]epository)\w*\s*\.\s*(?:get|is)?\w+\(\s*\)')
ERROR_DST = re.compile(r'\.(onException|onError\w*|onFailure|onFailed|onCancelled\w*|showError\w*|lambda\$showError\w*|'
                       r'lambda\$showDetailedMultiErrorDialog\w*|\w*ErrorDialog\w*)$')


def enclosing_if(L, ln, here):
    """(line, condition) of the if/else-if whose body holds line ln (a braced body, or the one statement after it)."""
    lo = here[0] if here else max(1, ln - 40)
    for k in range(ln, lo - 1, -1):
        t = strip_code(L[k - 1])
        m = re.search(r'\bif\s*\((.*)\)\s*\{?\s*$', t) or re.search(r'\bif\s*\((.*)\)\s*\S', t) if k == ln else \
            re.search(r'\bif\s*\((.*)\)\s*\{?\s*$', t)
        if not m:
            continue
        if k == ln or k == ln - 1:
            return k, m.group(1)
        depth = sum(strip_code(L[j - 1]).count('{') - strip_code(L[j - 1]).count('}') for j in range(k, ln))
        if '{' in t and depth > 0:
            return k, m.group(1)
        return None
    return None


def accessor_locals(L, cond, here):
    """Names tested in cond that the method assigns from a settings accessor call, or accessor calls in cond itself."""
    out = [m.group(0) for m in ACCESSOR.finditer(cond)]
    lo, hi = here if here else (1, len(L))
    for name in set(re.findall(r'\b([a-z]\w*)\b', cond)) - {'true', 'false', 'null', 'this'}:
        for i in range(lo, hi + 1):
            c = strip_code(L[i - 1])
            m = re.search(r'\b%s\s*=(?!=)\s*([^;]+)' % re.escape(name), c)
            if m and ACCESSOR.search(m.group(1)) and not NOT_SETTING.search(m.group(1)):
                out.append('%s = %s (:%d)' % (name, m.group(1).strip()[:80], i))
                break
    return out


def in_catch(L, ln, here):
    """True when line ln sits in a catch block of its method."""
    lo = here[0] if here else max(1, ln - 40)
    for k in range(ln, lo - 1, -1):
        t = strip_code(L[k - 1])
        if re.search(r'\bcatch\s*\(', t):
            depth = sum(strip_code(L[j - 1]).count('{') - strip_code(L[j - 1]).count('}') for j in range(k, ln))
            return depth > 0 or k == ln
        if re.search(r'\btry\s*\{', t) or re.search(r'^\s*\}\s*$', t) and k < ln - 0:
            depth = sum(strip_code(L[j - 1]).count('{') - strip_code(L[j - 1]).count('}') for j in range(k, ln))
            if depth <= 0 and re.search(r'\btry\s*\{', t):
                return False
    return False


def screen_r3(app, out_name='guard_steps_r3.csv'):
    g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % app)[0], encoding='utf-8'))
    E = {e['id']: e for e in g['edges']}
    sanity = {r['method']: r for r in csv.DictReader(open('graphs/%s/out/sanity_check.csv' % app, encoding='utf-8'))}
    S = 'graphs/%s/scratch/reaudit/' % app
    done = {}
    for fn in ('w7_judged.csv', 'r2_judged.csv', 'r3_judged.csv', 'r3b_judged.csv'):
        if os.path.exists(S + fn):
            for r in csv.DictReader(open(S + fn, encoding='utf-8')):
                done.setdefault((r['src'], r['dst'], r['kind']), '%s:%s' % (fn.split('_')[0], r['decision']))
    use = collections.Counter()
    ntarget = 0
    for r in csv.DictReader(open('graphs/%s/out/methods.csv' % app, encoding='utf-8')):
        s = sanity.get(r['method'])
        if s is None or str(s.get('monkey_hit', '0')) not in ('0', '') or str(s.get('ape_hit', '0')) not in ('0', ''):
            continue
        if class_of(r) != 'gui':
            continue
        ntarget += 1
        for i in (r['route_edge_ids'] or '').split():
            use[i] += 1
    src = Sources(app)
    res = Res(app)
    out = []
    for i, n in use.most_common():
        e = E[i]
        if e['src'] == 'S_ENTRY' or e['kind'] in ('LIFECYCLE', 'ENTERS'):
            continue
        flags, ev = [], []
        if e.get('edge_class') == 'non_standard':
            flags.append('reflection')
            ev.append('non_standard edge (%s)' % (e.get('via') or ''))
        refs = refs_of(e.get('evidence'))[:3]
        cited = '%s:%d' % refs[0][:2] if refs else ''
        callee = e['dst'].split('@')[0].split('(')[0].split('.')[-1]
        callee = '' if callee.startswith(('<', 'lambda$')) else callee
        for k, (f, ln, ln2) in enumerate(refs[:1]):
            p = src.find(f)
            if not p:
                continue
            L = src.lines(p)
            if ln > len(L):
                continue
            here = method_of(L, ln)
            gflag, _r, _gl, gt = G['screen_line'](L, ln)
            guard = gt if gflag == 'yes' else ''
            c = cond_at(L, ln, callee)
            cond = (c[1] if c else '') + ' ' + guard
            body_before = ' '.join(strip_code(x) for x in L[(here[0] if here else max(1, ln - 30)) - 1:ln - 1])
            # a call inside a lambda body that the method returns or passes on (a per-item filter, comparator or
            # callback, LibreTorrent TorrentFilterCollection finding): the body runs only for the items it gets
            lam = None
            for s0 in range(ln, (here[0] if here else max(1, ln - 30)) - 1, -1):
                t0 = strip_code(L[s0 - 1])
                if '->' in t0:
                    depth = 0
                    for s1 in range(s0, ln):
                        tt = strip_code(L[s1 - 1])
                        depth += tt.count('{') - tt.count('}')
                    if depth > 0 or (s0 == ln and re.search(r'->.*\b%s\s*\(' % re.escape(callee or 'x\x00'), t0)):
                        lam = s0
                    break
            if lam and re.search(r'\breturn\s*\(?\s*\w+\s*\)?\s*->|\.(filter|map|flatMap|forEach|sort|removeIf|anyMatch|allMatch|noneMatch|collect|reduce|comparing)\s*\(|Comparator', strip_code(L[lam - 1])):
                flags.append('empty_data')
                ev.append('inside a lambda body (from :%d): it runs per item it is called with: %s' % (lam, L[lam - 1].strip()[:120]))
            # empty_data
            if LOOP.search(guard) or NONEMPTY.search(cond):
                flags.append('empty_data')
                ev.append('loop or non-empty check: %s' % (guard or cond)[:250])
            elif EMPTYRET.search(body_before):
                flags.append('empty_data')
                ev.append('early return on empty data before :%d: %s' % (ln, EMPTYRET.search(body_before).group(0)[:160]))
            # setting
            if PREF_READ.search(cond) and not NOT_SETTING.search(cond):
                flags.append('setting')
                ev.append('setting read in the condition: %s' % cond.strip()[:200])
            else:
                sf = [x for x in setting_fields(L, cond) if not NOT_SETTING.search(x)]
                if sf:
                    flags.append('setting')
                    ev.extend(sf[:2])
            # round 3b: a setting read through a settings object (pref.batteryControl(), AppSettings getters) into a local
            # that the enclosing if tests (blind pass 1, LibreTorrent battery control and logging)
            cl = ln
            if callee:
                for (f3, a3, b3) in refs:
                    if src.find(f3) == p:
                        hit = [j for j in range(a3, min(len(L), b3) + 1) if re.search(r'\b%s\s*\(' % re.escape(callee), strip_code(L[j - 1]))]
                        if hit:
                            cl = hit[0]
                            break
            here_c = method_of(L, cl) or here
            if 'setting' not in flags:
                ic = enclosing_if(L, cl, here_c)
                if ic:
                    acc = accessor_locals(L, ic[1], here_c)
                    if acc:
                        flags.append('setting')
                        ev.append('setting accessor in the enclosing if at :%d (%s): %s' % (ic[0], ic[1][:120], '; '.join(acc[:2])))
            # round 3b: an error-only path (blind pass 1, Aegis error dialog and onException): the step runs only after
            # a failure: inside a catch block, or into an error callback or error dialog
            if (ERROR_DST.search(e['dst'].split('@')[0].split('(')[0]) or ERROR_DST.search(e['src'].split('@')[0].split('(')[0])
                    or in_catch(L, cl, here_c)):
                flags.append('error_path')
                ev.append('error-only path: %s' % ('inside a catch block at :%d' % cl if in_catch(L, cl, here_c)
                                                    else 'error callback or dialog %s' % e['dst']))
            # flag_field
            ff = flag_fields(L, cond, here)
            if ff:
                flags.append('flag_field')
                ev.extend(ff[:3])
            # reflection in the cited lines
            win = ' '.join(strip_code(x) for x in L[max(0, ln - 2):min(len(L), ln2 + 1)])
            if REFLECT.search(win) and 'reflection' not in flags:
                flags.append('reflection')
                ev.append('reflection in the cited lines: %s' % REFLECT.search(win).group(0))
            # trigger visibility depending on a setting (every cited range of the same file, not only the first line)
            if e['kind'] in ('GUI', 'FRAMEWORK', 'SYSTEM') or re.search(r'\.(onOptionsItemSelected|onPreference\w*|onClick)$', e['src'].split('@')[0]):
                ids = set()
                wins = []
                for (f2, a2, b2) in refs:
                    if src.find(f2) == p:
                        wins.extend(L[max(0, a2 - 16):min(len(L), b2 + 15)])
                for l in wins:
                    ids |= set(re.findall(r'R\.id\.(\w+)', l))
                    ids |= set(re.findall(r'findPreference\(\s*(?:getString\()?\s*(?:[\w$]+\.)*"?(\w+)', l))
                    ids |= set(re.findall(r'\bcase\s+(?:[\w$]+\.)*([A-Z][A-Z0-9_]{2,})\s*:', l))
                    ids |= set(re.findall(r'"(pref_\w+)"', l))
                ids -= {'PreferencesConstants', 'PreferenceConstants', 'R', 'string'}
                for ident in sorted(ids)[:10]:
                    for h in res.visibility(ident, p):
                        fname, _, rest = h.partition(':')
                        try:
                            hl = int(rest.split(':')[0])
                        except ValueError:
                            continue
                        hp = res.java and [q for q in res.java if os.path.basename(q) == fname]
                        HL = res.text(hp[0]) if hp else L
                        sa = setting_arg(HL, HL[hl - 1]) if hl <= len(HL) else []
                        if sa:
                            if 'setting' not in flags:
                                flags.append('setting')
                            ev.append('%s: %s; %s' % (ident, h[:120], sa[0]))
        if ITEM_CB.search(e['dst']) and 'empty_data' not in flags:
            flags.append('empty_data')
            ev.append('per-item callback of a list')
        if not flags:
            continue
        out.append([i, e['kind'], e['src'], e['dst'], cited, '+'.join(dict.fromkeys(flags)), ' || '.join(ev)[:900],
                    done.get((e['src'], e['dst'], e['kind']), ''), n])
    path = S + out_name
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['step', 'kind', 'src', 'dst', 'cited', 'flags', 'evidence', 'judged_before', 'targets'])
        w.writerows(out)
    c = collections.Counter(k for o in out for k in o[5].split('+'))
    print('%s: gui targets %d, route steps %d, flagged %d (%s); flagged uses %d of %d' % (
        app, ntarget, len(use), len(out), ', '.join('%s %d' % kv for kv in sorted(c.items())),
        sum(o[8] for o in out), sum(use.values())))


if __name__ == '__main__':
    if sys.argv[1] == '--r3':
        screen_r3(sys.argv[2])
    elif sys.argv[1] == '--r3b':
        screen_r3(sys.argv[2], 'guard_steps_r3b.csv')
    else:
        screen(sys.argv[1])
