import json, re, sys
G = json.load(open('graphs/AnyMemo/out/anymemo_trigger_graph.json'))
V = G['verdict']
for pat in sys.argv[1:]:
    rx = re.compile(pat)
    hits = [(k, v) for k, v in sorted(V.items()) if rx.search(k)]
    for k, v in hits[:12]:
        print('%-8s %s' % (v[:5], k))
    if len(hits) > 12:
        print('   ... %d more matching %s' % (len(hits) - 12, pat))
