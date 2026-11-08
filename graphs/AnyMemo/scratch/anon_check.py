import sys, os, re, json, glob
sys.path.insert(0, '/Users/darshan/Desktop/yang/work/tools')
import extract_calls as X
BUILD = '/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/build/intermediates/javac/devDebug/compileDevDebugJavaWithJavac/classes/'
G = '/Users/darshan/Desktop/yang/work/graphs/AnyMemo'
def class_lines():
    out = {}
    for f in glob.glob(BUILD + '**/*.class', recursive=True):
        ci = X.parse_class(f)
        cname = ci.name.replace('/', '.')
        ls = set()
        for (name, desc), m in ci.methods.items():
            if name in ('<init>', '<clinit>'):
                continue
            ls |= set(m['linenos'])
        out[cname] = sorted(ls)
    return out
if __name__ == '__main__':
    CL = class_lines()
    json.dump(CL, open(G + '/scratch/class_lines.json', 'w'))
    print('classes', len(CL), 'with lines', sum(1 for v in CL.values() if v))
