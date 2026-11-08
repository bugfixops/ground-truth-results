import sys
sys.path.insert(0, '/Users/darshan/Desktop/yang/work/tools')
import cases
CS = cases.Cases('AnyMemo')
for arg in sys.argv[1:]:
    f, l = arg.rsplit(':', 1)
    l = int(l)
    try:
        enc = CS.enclosing(f, l)
    except Exception as ex:
        enc = 'ERR %s' % ex
    try:
        g = CS.guard_of(f, l)
    except Exception as ex:
        g = 'ERR %s' % ex
    print(arg, '| enclosing:', enc, '| guard:', g)
