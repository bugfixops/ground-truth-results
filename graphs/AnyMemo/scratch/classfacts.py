import os, re, sys, collections
SRC = "/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main"
JAVA = os.path.join(SRC, "java")
MANIFEST = os.path.join(SRC, "AndroidManifest.xml")
files = []
for root, _, fs in os.walk(SRC):
    for f in fs:
        if f.endswith(".java") or f.endswith(".xml"):
            files.append(os.path.join(root, f))
texts = {}
for p in files:
    try:
        texts[p] = open(p, encoding="utf-8", errors="replace").read()
    except Exception:
        pass
manifest = open(MANIFEST, encoding="utf-8", errors="replace").read()
classes = [l.split("\t")[0] for l in open(sys.argv[1])]
seen = set()
for m in classes:
    if m.startswith(("fantastischmemo.", "baseAdapters.", "databinding.")):
        continue
    cls = m.split(".")[0]
    if cls in seen:
        continue
    seen.add(cls)
    top = cls.split("$")[0]
    simple = cls.split("$")[-1]
    own = [p for p in texts if p.endswith("/" + top + ".java")]
    newsites = []
    inj = []
    outside = []
    for p, t in texts.items():
        if not p.endswith(".java"):
            continue
        if re.search(r"new\s+" + re.escape(simple) + r"\s*[(<]", t):
            newsites.append(os.path.basename(p))
        if own and p in own and "@Inject" in t:
            inj.append(os.path.basename(p))
        if p not in own and re.search(r"\b" + re.escape(simple) + r"\b", t):
            outside.append(os.path.basename(p))
    man = top in manifest or ("." + simple + '"') in manifest
    print("%-45s own=%s new=%s inject=%s outside=%s manifest=%s" % (
        cls, [os.path.basename(x) for x in own][:1], newsites[:3], inj[:2], sorted(set(outside))[:4], man))
