import json, re, collections, sys
d = json.load(open('graphs/AnyMemo/out/anymemo_trigger_graph.json'))
E = d['edges']
COND = re.compile(r'\b(if|only|when|unless|provided|except|first launch|first time|first run|must|depends|empty|null|not set|enabled|disabled|available)\b', re.I)
STATE = re.compile(r'\b(after|once|previously|already|saved|has been|was (set|chosen|shown)|earlier|previous|configured|chosen|selected earlier|stored|set up|setup|logged in|signed in|imported|created before)\b', re.I)
ENV = re.compile(r'\b(network|internet|wifi|wi-fi|online|offline|permission|camera|microphone|dropbox|google drive|drive|oauth|server|download|upload|http|tls|certificate|battery|charging|boot|reboot|alarm|timer|clock|time|midnight|notification|other app|another app|broadcast|intent from|hardware|bluetooth|sensor|screen off|screen on|locale|language|tts|speech|tts engine|storage|sd card|external|usb|phone call)\b', re.I)
hand = [e for e in E if e.get('evidence') and not re.search(r'\(bytecode\)', e.get('evidence') or '')]
auto = [e for e in E if e not in hand]
print('edges', len(E), 'hand (non-bytecode evidence)', len(hand), 'bytecode', len(auto))
def txt(e):
    return ' '.join(filter(None, [e.get('trigger') or '', e.get('note') or '', ' '.join(e.get('gui') or [])]))
c1 = [e for e in E if COND.search(txt(e)) and not e.get('guard')]
c2 = [e for e in E if STATE.search(txt(e)) and not e.get('needs_state') and not e.get('state_kinds')]
c3 = [e for e in E if ENV.search(txt(e)) and not e.get('env_kinds') and e['kind'] not in ('CALL',)]
print('cond words, no guard', len(c1), collections.Counter(e['kind'] for e in c1).most_common())
print('state words, no needs_state/state_kinds', len(c2), collections.Counter(e['kind'] for e in c2).most_common())
print('env words (non-CALL), no env_kinds', len(c3), collections.Counter(e['kind'] for e in c3).most_common())
json.dump({'cond': [e['id'] for e in c1], 'state': [e['id'] for e in c2], 'env': [e['id'] for e in c3]}, open('graphs/AnyMemo/scratch/step5_ids.json', 'w'))
