"""Round 1b query helper: print compact rows of the built graph (out/anymemo_trigger_graph.json).
Usage: python3 r1b_q.py SRC_PREFIX [DST_PREFIX]   (exact match with --exact, otherwise startswith)
"""
import json
import sys

G = '/Users/darshan/Desktop/yang/work/graphs/AnyMemo/out/anymemo_trigger_graph.json'


def rows(src=None, dst=None, exact=False):
    g = json.load(open(G))
    out = []
    for x in g['edges']:
        s, d = x['src'], x['dst']
        ok_s = src is None or (s == src if exact else s.startswith(src))
        ok_d = dst is None or (d == dst if exact else d.startswith(dst))
        if ok_s and ok_d:
            out.append('%s | %s -> %s | %s | guard=%s | state=%s | env=%s | %s' % (
                x.get('id'), s, d, x['kind'], bool(x.get('guard')), bool(x.get('needs_state')),
                bool(x.get('env')), (x.get('evidence') or '')[:70]))
    return out


if __name__ == '__main__':
    src = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] != '-' else None
    dst = sys.argv[2] if len(sys.argv) > 2 else None
    exact = '--exact' in sys.argv
    for r in rows(src, dst, exact):
        print(r)
