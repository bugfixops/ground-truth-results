import os, re, sys
SRC = "/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo"
texts = {}
for root, _, fs in os.walk(SRC):
    for f in fs:
        if f.endswith(".java"):
            p = os.path.join(root, f)
            texts[p] = open(p, encoding="utf-8", errors="replace").read()
rows = []
for line in open(sys.argv[1]):
    m = line.split("\t")[0]
    if not m.endswith(".<init>") and not m.endswith(".<clinit>"):
        continue
    if m.startswith(("fantastischmemo.", "baseAdapters.", "databinding.", "Dagger", "AppModules_", "DaggerApp")) or "InstanceHolder" in m:
        continue
    if "DaoImpl" in m or "Binding" in m or "$" in m:
        continue
    cls = m.split(".")[0]
    simple = cls
    own = [p for p in texts if p.endswith("/" + cls + ".java")]
    if not own:
        continue
    t = texts[own[0]]
    injctor = bool(re.search(r"@Inject\s*\n?\s*(public\s+|private\s+|protected\s+)?" + re.escape(simple) + r"\s*\(", t))
    injfield = bool(re.search(r"@Inject\s+(?:public\s+|private\s+|protected\s+|static\s+|final\s+)*[\w<>\[\], ?]+\s+\w+\s*;", t))
    news = sum(len(re.findall(r"new\s+" + re.escape(simple) + r"\s*[(<]", tt)) for tt in texts.values())
    statuse = sum(len(re.findall(r"\b" + re.escape(simple) + r"\.\w+\s*\(", tt)) for p, tt in texts.items() if p != own[0])
    rows.append((m, injctor, injfield, news, statuse, os.path.basename(own[0])))
for r in rows:
    print("%-70s injctor=%-5s injfield=%-5s new=%-2d staticuse=%-3d %s" % r)
