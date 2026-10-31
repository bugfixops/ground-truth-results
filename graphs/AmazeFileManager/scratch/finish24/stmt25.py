import json, re, sys
W = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager'
GD = open(W + '/graph_def.py', encoding='utf-8').read().split('\n')
names = sorted(json.load(open(W + '/out/amazefilemanager_trigger_graph.json'))['verdict'].keys())
mode = sys.argv[1]
if mode == 'stmt':
    for a in sys.argv[2:]:
        n = int(a)
        buf, depth, i = [], 0, n - 1
        while True:
            l = GD[i]
            buf.append('%d: %s' % (i + 1, l.rstrip()[:160]))
            depth += l.count('(') - l.count(')')
            if depth <= 0 or i - n > 12:
                break
            i += 1
        print('\n'.join(buf))
        print('-')
else:
    for rx in sys.argv[2:]:
        hits = [n for n in names if re.search(rx, n)]
        print(rx, '=>', hits[:30])
