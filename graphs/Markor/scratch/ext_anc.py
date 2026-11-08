import json, collections, re
G='/Users/darshan/Desktop/yang/work/graphs/Markor/'
hier=json.load(open(G+'scratch/hier.json'))
ml=json.load(open(G+'method_list.json'))
man={l.split('\t')[0]:l.split('\t')[1].strip() for l in open(G+'scratch/manual_list.txt')}
clsof={}
for m in ml:
    clsof[m['short']]=m
def anc(c, out):
    h=hier.get(c)
    if not h: return out
    for p in ([h['super']] if h['super'] else [])+h['ifaces']:
        if p and p not in out:
            out.add(p); anc(p,out)
    return out
cnt=collections.Counter(); names=collections.Counter()
lib=[n for n,v in man.items() if v.startswith('instance method overriding')]
for n in lib:
    cls=n.rsplit('.',1)[0]
    simp=n.split('(')[0]
    # find class internal name by simple match
    cands=[k for k in hier if k.split('/')[-1]==cls]
    if not cands:
        cnt['noclass']+=1; continue
    A=anc(cands[0], set())
    ext=sorted(a for a in A if a not in hier and a!='java/lang/Object')
    for e in ext: cnt[e]+=1
print(len(lib), cnt.most_common(40))
