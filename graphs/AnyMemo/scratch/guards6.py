import sys
sys.path.insert(0, '/Users/darshan/Desktop/yang/work/tools')
import cases

CS = cases.Cases('AnyMemo')

# each arg: File.java:LINE  (scratch check only, read-only)
for arg in sys.argv[1:]:
    fname, line = arg.rsplit(':', 1)
    line = int(line)
    try:
        lines, text = CS._load(fname)
        src = lines[line - 1].rstrip() if line - 1 < len(lines) else '<past EOF>'
        meth = CS.enclosing(fname, line)
        g = CS.guard_of(fname, line)
    except KeyError as ex:
        src, meth, g = 'KEYERROR %s' % ex, None, []
    print('%s:%d | in=%s | %s' % (fname, line, meth, src.strip()[:150]))
    for x in g:
        print('     guard: %s' % x)
