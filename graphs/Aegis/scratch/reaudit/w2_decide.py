# W2 decisions for Aegis (Kiro, self-checked only). Run from the repo root on
# the pre-W2 build: python3 -I graphs/Aegis/scratch/reaudit/w2_decide.py
# Writes state_gates.csv (needs_state, count, decision, reason, evidence) and
# prints the CLEAR texts with their edge notes for graph_def.py.
# Baseline (review/TASK_NOTE.md): onboarding passed and a vault with two
# entries; the setup vault is password-protected (MUSE_REAUDIT_QUESTIONS Q3);
# the two entries are default TOTP entries (Q6). Source root:
# final_java_only/Aegis/app/Aegis-#v3.4.2/app/src/main/java/com/beemdevelopment/aegis/
import collections
import csv
import json
import sys

D = 'graphs/Aegis/'
OUT = D + 'scratch/reaudit/state_gates.csv'

# (text prefix, decision, reason, evidence file:line)
DEC = [
    ('The intro security picker chose none', 'CLEAR',
     'baseline: the onboarding (first-run setup) is passed; the intro picker branch belongs to that setup, and the intro pages are in SETUP_ONLY',
     'IntroActivity.java:50-55'),
    ('The Welcome slide did not import a vault', 'CLEAR',
     'baseline: the onboarding is passed with a new vault, not an imported one; the intro Done branch belongs to the setup, and the intro pages are in SETUP_ONLY',
     'IntroActivity.java:86-100'),
    ('The vault is loaded in this process', 'CLEAR',
     'baseline: the setup vault exists; a normal start reads it and, when it is encrypted, opens AuthActivity, where unlocking is typing the password (a GUI action, Q3)',
     'MainActivity.java:950-976'),
    ('This MainActivity instance has loaded the entry list', 'CLEAR',
     'baseline: once the vault is loaded, MainActivity.onStart calls loadEntries on the normal start, which sets the entries of the list',
     'MainActivity.java:991-992; MainActivity.java:1133-1138'),
    ('The vault icons are not marked optimised yet', 'KEEP',
     'a vault created by this version has icons_optimized true (field default, written by toJson); it is false only when the stored vault JSON lacks icons_optimized, i.e. a vault file an older app version wrote',
     'Vault.java:18; Vault.java:46; Vault.java:92-93'),
    ('The floating action menu is open', 'KEEP', 'UI session (an open menu); not part of the baseline', 'FabMenuHelper.java:76-102'),
    ('A vault file exists in the app data', 'CLEAR',
     'baseline: the onboarding created the vault file, which MainActivity.onStart reads',
     'MainActivity.java:950-953'),
    ('The vault holds a TOTP or HOTP entry with SHA-1 and 6 digits', 'CLEAR',
     'baseline: the vault holds two entries; a new entry defaults to TOTP with SHA1 and 6 digits (Q6), so the export list is not empty',
     'ImportExportPreferencesFragment.java:352-360; VaultEntry.java:253-255; OtpInfo.java:14-15'),
    ('A plain-text vault file exists in the app data', 'KEEP',
     'the setup vault is password-protected (Q3); a plain-text vault needs a different setup choice or turning encryption off (stored state)',
     'MainActivity.java:968-970'),
    ('The current intro slide is not finished', 'SETUP_ONLY',
     'the gate leaves the intro page S_INTRO_SETUP, which is in SETUP_ONLY; the text itself is kept',
     'IntroBaseActivity.java:84-88'),
    ('At least one entry row is bound', 'CLEAR',
     'baseline: the vault holds two entries, so the list binds their rows when the main screen shows them',
     'EntryAdapter.java:569; MainActivity.java:1137'),
    ('The vault holds at least one entry', 'CLEAR',
     'baseline: the setup vault holds two entries, so the loop in Vault.toJson runs', 'Vault.java:9-12'),
    ('An icon pack is already installed', 'KEEP', 'needs an icon pack imported earlier (stored file); not part of the baseline', 'IconPackManager.java:33'),
    ('The selection action mode is open', 'KEEP', 'UI session (a selection); not part of the baseline', 'MainActivity.java:1303-1308'),
    ('The vault has a password slot', 'CLEAR',
     'baseline: the setup vault is password-protected (Q3), so it has a password slot', 'AuthActivity.java:172-174 (unlock with the password slots); MUSE_REAUDIT_QUESTIONS.md Q3'),
    ('The panic trigger preference is on', 'KEEP', 'non-default setting (default off)', 'Preferences.java:107-108'),
    ('The vault file exists but cannot be read', 'KEEP', 'needs a damaged vault file; not part of the baseline', 'MainActivity.java:954-955'),
    ('The search box is expanded', 'KEEP', 'UI session (open search); not part of the baseline', 'MainActivity.java:1021-1024'),
    ('The main screen shows an error card', 'KEEP', 'needs a condition that sets an error card; not part of the baseline', 'MainActivity.java:1163-1197'),
    ('The vault has a biometric slot', 'KEEP', 'needs a biometric slot; the setup vault is password-only', 'AuthActivity.java:132-137'),
    ('The vault file holds a MOTP entry', 'KEEP', 'the baseline entries are default TOTP entries (Q6)', 'OtpInfo.java:134-136'),
    ('The assign-groups dialog is open', 'KEEP', 'UI session (an open dialog)', 'MainActivity.java:533-601'),
    ('The save-filter chip is visible', 'KEEP', 'UI session (a changed group filter)', 'MainActivity.java:335; MainActivity.java:373-377'),
    ('the entry list passed in is not empty', 'CLEAR',
     'baseline: the setup vault holds two entries, so loadEntries passes a non-empty list', 'EntryAdapter.java:301; MainActivity.java:1137'),
    ('The vault file holds a Yandex entry', 'KEEP', 'the baseline entries are default TOTP entries (Q6)', 'OtpInfo.java:131-133'),
    ('The Welcome slide imported a vault file', 'KEEP', 'the import branch of the intro; the baseline setup creates a new vault, and the intro pages are in SETUP_ONLY', 'IntroActivity.java:59'),
    ('The vault is encrypted', 'CLEAR',
     'baseline: the setup vault is password-protected (Q3), so it has credentials and isEncryptionEnabled is true', 'VaultRepository.java:352-354'),
    ('The vault file holds a HOTP entry', 'KEEP', 'the baseline entries are default TOTP entries (Q6)', 'OtpInfo.java:128-129'),
    ('The camera provider is ready', 'KEEP', 'device camera state', 'ScannerActivity.java:70; ScannerActivity.java:79-88'),
    ('SEARCH_IN_GROUPS is set', 'KEEP', 'non-default setting', 'MainActivity.java:234; BehaviorPreferencesFragment.java:57'),
    ('The icon picker returned an SVG file', 'KEEP', 'picker result (outside the app)', 'EditEntryActivity.java:148-158'),
    ('The clipboard import dialog is open', 'KEEP', 'needs an otpauth link on the clipboard', 'MainActivity.java:476-491'),
    ('Biometrics are available on the device', 'KEEP', 'device capability', 'BiometricsHelper.java:27-29'),
    ('An AegisActivity is open and registered as a lock listener', 'CLEAR',
     'baseline: every AegisActivity registers itself as a lock listener in onCreate, so any open app screen satisfies it', 'AegisActivity.java:76-77'),
    ('The edit page has unsaved changes', 'KEEP', 'UI session (an unsaved form)', 'EditEntryActivity.java:955-957'),
    ('The delete-entries dialog is open', 'KEEP', 'UI session (an open dialog)', 'MainActivity.java:1508-1516'),
]

g = json.load(open(D + 'out/aegis_trigger_graph.json', encoding='utf-8'))
E = {e['id']: e for e in g['edges']}
rows = list(csv.DictReader(open(D + 'out/methods.csv', encoding='utf-8')))
cnt = collections.Counter()
for r in rows:
    if r['verdict'] != 'REACHABLE':
        continue
    seen = set()
    for i in (r['route_edge_ids'] or '').split():
        t = (E.get(i) or {}).get('needs_state')
        if t and t not in seen:
            seen.add(t)
            cnt[t] += 1

out, clear, missing = [], {}, []
for t, n in cnt.most_common():
    hit = [d for d in DEC if t.startswith(d[0])]
    if len(hit) != 1:
        missing.append(t)
        continue
    _, dec, why, ev = hit[0]
    out.append((t, n, dec, why, ev))
    if dec == 'CLEAR':
        clear[t] = '%s (%s)' % (why, ev)
if missing:
    print('UNDECIDED:', missing)
    sys.exit(1)
with open(OUT, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['needs_state', 'count', 'decision', 'reason', 'evidence file:line', 'checked_by'])
    for row in out:
        w.writerow(list(row) + ['self'])
print('texts:', len(out), dict(collections.Counter(r[2] for r in out)))
if '--emit' in sys.argv:
    print('_W2_CLEARED = {')
    for t, note in clear.items():
        print('    %r:\n        %r,' % (t, note))
    print('}')
