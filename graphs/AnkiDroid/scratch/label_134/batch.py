import json
row=[l for l in open('/Users/darshan/Desktop/yang/work/graphs/AnkiDroid/scratch/batches_ai.tsv').read().splitlines() if l.split('\t')[0]=='134'][0]
meths=row.split('\t')[3].split(';')
g=json.load(open('/Users/darshan/Desktop/yang/work/graphs/AnkiDroid/out/ankidroid_trigger_graph.json'))
auto=json.load(open('/Users/darshan/Desktop/yang/work/graphs/AnkiDroid/auto_calls.json'))
