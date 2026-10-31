import json,sys,re
a=json.load(open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/auto_calls.json'))
pat=re.compile(sys.argv[1])
seen=set()
for c in a['calls']:
    d=c['dst'].split('(')[0]
    if d.endswith('.<init>') and pat.search(d):
        k=(d,c['src'],c['file'],c['line'])
        if k not in seen:
            seen.add(k); print('%s <- %s  %s:%s' % (d, c['src'], c['file'], c['line']))
