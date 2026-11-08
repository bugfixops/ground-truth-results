import os, re, json, collections
# Writes scratch/textcount.json: identifier -> number of occurrences in app .java, .kt and .xml files (build dirs excluded).
# Declarations are subtracted later (method_list.json) to get textual references.
ROOT = '/Users/darshan/Desktop/yang/final_java_only/Markor/app/Markor-#v2.16.1/app'
G = '/Users/darshan/Desktop/yang/work/graphs/Markor/'
cnt = collections.Counter()
dot = collections.Counter()   # identifier used as a call on an object: 'x.name(' (java, kt)
nfiles = 0
for d, dirs, fs in os.walk(ROOT):
    dirs[:] = [x for x in dirs if x not in ('build', '.gradle')]
    for f in fs:
        if f.endswith(('.java', '.kt', '.xml')):
            nfiles += 1
            txt = open(os.path.join(d, f), encoding='utf-8', errors='replace').read()
            cnt.update(re.findall(r'[A-Za-z_][A-Za-z0-9_]*', txt))
            if f.endswith(('.java', '.kt')):
                dot.update(re.findall(r'\.([A-Za-z_][A-Za-z0-9_]*)\s*\(', txt))
json.dump(dict(cnt), open(G + 'scratch/textcount.json', 'w'))
json.dump(dict(dot), open(G + 'scratch/dotcount.json', 'w'))
print('files', nfiles, 'identifiers', len(cnt))
