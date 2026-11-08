import os, re, sys
ROOT = '/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo'
# usage: srcgrep.py PATTERN [PATTERN ...]   (python regex; prints relpath:line: text, max 6 per pattern)
for pat in sys.argv[1:]:
    rx = re.compile(pat)
    hits = []
    for dp, dn, fn in os.walk(ROOT):
        for f in fn:
            if not f.endswith('.java'):
                continue
            p = os.path.join(dp, f)
            for i, line in enumerate(open(p, encoding='utf-8', errors='replace'), 1):
                if rx.search(line):
                    hits.append('%s:%d: %s' % (os.path.relpath(p, ROOT), i, line.strip()[:150]))
    print('== %s: %d' % (pat, len(hits)))
    for h in hits[:6]:
        print('   ' + h)
