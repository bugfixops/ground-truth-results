# W5 consistency fix for LibreTorrent (Kiro, after the reviewer's round-1 check). Usage, from the repo root:
#   python3 -I graphs/LibreTorrent/scratch/reaudit/w5b_consistency.py [--print]
# Lists the non_standard edges whose via is one of the mechanisms the other four apps treat as standard:
#   AndroidX Fragment / FragmentManager / DialogFragment / ViewPager2 lifecycle; JVM class initialisation on first
#   use; TextWatcher dispatch; the AndroidX Activity Result API; the AppCompat action bar.
# Excluded on purpose: any via that also names data binding, a mapper, newInstance or layout inflation (a class built
# from XML or by reflection stays library), preference, SearchView, ActionMode and page-change callbacks (not in
# the reviewer's list). graph_def.py imports MATCH from this file's logic (same regexes, copied there).
# --print writes w5b_printed.txt: every matched edge with its evidence and the cited app source lines.
import glob
import json
import re
import sys

INCLUDE = [
    r'^(AndroidX |Android |Framework )?(Fragment|FragmentManager|DialogFragment)( show and DialogFragment| transaction and| and)? lifecycle( dispatch)?( after show)?$',
    r'^(ViewPager2 fragment lifecycle dispatch|AndroidX ViewPager2 / FragmentStateAdapter|FragmentStateAdapter dispatch|ViewPager2 dispatch after setAdapter)$',
    r'^JVM (class|enum|enum class|interface|superclass)[ -](init|initiali[sz]ation)\b',
    r'^TextWatcher (framework )?dispatch$',
    r'Activity ?Result',
    r'^AndroidX AppCompat action bar$',
]
EXCLUDE = r'[Dd]ata[Bb]inding|DataBindingUtil|mapper|newInstance|inflation'


def via_text(e):
    v = e.get('via')
    return ' '.join(map(str, v)) if isinstance(v, list) else str(v or '')


def matches(v):
    return bool(v) and not re.search(EXCLUDE, v) and any(re.search(p, v) for p in INCLUDE)


if __name__ == '__main__':
    g = json.load(open('graphs/LibreTorrent/out/libretorrent_trigger_graph.json', encoding='utf-8'))
    hit = [e for e in g['edges'] if e['edge_class'] == 'non_standard' and matches(via_text(e))]
    print('matched non_standard edges:', len(hit))
    if '--print' in sys.argv:
        src = {}
        for p in glob.glob('final_java_only/LibreTorrent/app/**/src/main/java/**/*.java', recursive=True):
            src.setdefault(p.rsplit('/', 1)[-1], []).append(p)
        with open('graphs/LibreTorrent/scratch/reaudit/w5b_printed.txt', 'w', encoding='utf-8') as f:
            for e in sorted(hit, key=lambda e: (via_text(e), e['src'], e['dst'])):
                f.write('== %s %s %s -> %s\n   via: %s\n   evidence: %s\n' % (e['id'], e['kind'], e['src'], e['dst'], via_text(e), e['evidence']))
                for m in re.finditer(r'(?:SRC )?([\w/$.-]+\.java):(\d+)(?:-(\d+))?', e['evidence'] or ''):
                    name = m.group(1).rsplit('/', 1)[-1]
                    cands = [p for p in src.get(name, []) if p.endswith(m.group(1))] or src.get(name, [])
                    if not cands:
                        continue
                    lines = open(cands[0], encoding='utf-8', errors='replace').read().split('\n')
                    a = int(m.group(2)); b = min(int(m.group(3) or a), a + 6)
                    for k in range(a, b + 1):
                        if 0 < k <= len(lines):
                            f.write('   %s:%d: %s\n' % (m.group(1), k, lines[k - 1].strip()[:150]))
                    break
        print('wrote graphs/LibreTorrent/scratch/reaudit/w5b_printed.txt')
