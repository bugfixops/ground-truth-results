import csv,json,glob,re,collections,sys
os_ = 'graphs/AmazeFileManager/'
g=json.load(open(glob.glob(os_+'out/*_trigger_graph.json')[0]))
E={e['id']:e for e in g['edges']}
FAM=re.compile(r'^(SevenZ|Sevenz|Rar|Tar|Bzip2|Gzip|Lzma|Xz|Coders|Folder|Archive$|AES256|LZMA|Delta|BoundedFileChannel|StreamMap|SubStreams|StartHeader|BindPair|Coder$|CoderBase|NID|JunrarFile|\w*Rar)')
def fam(m):
    c=m.split('@')[0].split('(')[0].rsplit('.',1)[0]
    return bool(FAM.match(c.split('$')[0]))
rows=list(csv.DictReader(open(os_+'out/methods.csv')))
sf=[r for r in rows if r['verdict']=='REACHABLE' and 'file' in r['state_kinds'].split(';') and not [k for k in r['env_kinds'].split(';') if k and k!='permission']]
ent=collections.Counter(); via=0
for r in sf:
    ids=r['route_edge_ids'].split()
    for i in ids:
        e=E[i]
        if fam(e['dst']) and not fam(e['src']):
            ent[i]+=1; break
    else:
        if any(fam(E[i]['dst']) for i in ids): ent['inside-only']+=1
print(len(sf))
for i,n in ent.most_common(60):
    if i=='inside-only': print(n,i); continue
    e=E[i]; print(n,i,e['src'],'->',e['dst'],e['kind'],'|',(e.get('needs_state') or '')[:30])
