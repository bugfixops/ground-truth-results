import sys
sys.path.insert(0, '/Users/darshan/Desktop/yang/work/tools')
import cases

# usage: python3 -I gcheck.py <App> <file> <line> [<file> <line> ...]
app = sys.argv[1]
args = sys.argv[2:]
CS = cases.Cases(app)
for i in range(0, len(args), 2):
    f, ln = args[i], int(args[i + 1])
    try:
        enc = CS.enclosing(f, ln)
    except KeyError as ex:
        print(f, ln, 'KEYERROR', ex)
        continue
    try:
        g = CS.guard_of(f, ln)
    except KeyError as ex:
        g = 'KEYERROR %s' % ex
    print('%s:%d  enclosing=%s  guard=%s' % (f, ln, enc, g))
