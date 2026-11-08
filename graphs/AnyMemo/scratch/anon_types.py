import json,re,os,csv,collections
SRCROOT='/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo'
amap=json.load(open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch/anon_map2.json'))
from anon2 import NEW
from anon import strip
types={}
cache={}
for cname,a in amap.items():
    f=os.path.join(SRCROOT,a['file'])
    if f not in cache:
        s=strip(open(f,encoding='utf-8',errors='replace').read())
        cache[f]=s
    s=cache[f]
    # line -> offset of first line
    lines=s.split('\n')
    ln=a['new']
    seg='\n'.join(lines[ln-1:ln+2])
    m=re.search(r'new\s+([\w.<>?,\s]+?)\s*\(', seg)
    types[cname]=m.group(1).strip() if m else '?'
json.dump(types,open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch/anon_types.json','w'),indent=0)
print(collections.Counter(types.values()).most_common(50))
