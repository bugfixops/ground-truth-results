# Removes section H (the UNREACHABLE literal and the SUPPRESS call) from graph_def.py, so the next build lists every
# method the rules have not decided. Needed before scratch/plan.py: plan.py reads the unresolved list of a build, and a
# build with section H present has no unresolved methods left.
# Usage: python3 -I scratch/strip_unreach.py   (then build, then plan.py, then emit_unreach.py)
GD = '/Users/darshan/Desktop/yang/work/graphs/Markor/graph_def.py'
MARK = '# ================================================================== H. UNREACHABLE entries'
src = open(GD, encoding='utf-8').read()
if MARK in src:
    src = src[:src.index(MARK)].rstrip('\n') + '\n'
    open(GD, 'w', encoding='utf-8').write(src)
    print('section H removed')
else:
    print('section H not present')
