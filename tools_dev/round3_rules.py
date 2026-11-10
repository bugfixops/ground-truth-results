# Round 3 rules (Kiro, 2026-11-10), executed at the end of graphs/<App>/graph_def.py after the round 2 rules, in the
# graph_def namespace (R3_APP is set there). They fix the causes of the defects the independent round-3 checks found:
#   J   judged steps: graphs/<App>/scratch/reaudit/r3_judged.csv (the round-3 screen of tools_dev/guard_prescreen_r2.py
#       --r3 and the named defects), applied like r2_judged.csv
#   P   generated protobuf-lite classes: the runtime reaches their members (non_standard, library); no code calls the
#       static parser() accessor (Aegis GoogleAuthProtos)
#   K   onConfigurationChanged of an activity runs only for changes its manifest entry lists in android:configChanges
#   R   the transaction editors' shared helper (MMEX EditTransactionCommonFunctions) holds the editor's own entity: a
#       call into RecurringTransaction runs only in the recurring editor
#   Q   launch-time ContentResolver queries on the app's own provider (MMEX) reach MmxContentProvider.query
#   S   a session tag that is a device fact, not a UI session, is dropped (Aegis scanner)
import csv as _r3_csv
import glob as _r3_glob
import os as _r3_os
import re as _r3_re

_R3_ROOT = _r3_os.path.normpath(_r3_os.path.join(GDIR, '..', '..'))
R3_LOG = {'J': 0, 'P': 0, 'K': 0, 'R': 0, 'Q': 0, 'S': 0}


def _r3_note(x, text):
    x['note'] = ((x.get('note') + ' | ') if x.get('note') else '') + text


# ---------------------------------------------------------------- J
_R3J = {}
_r3_path = _r3_os.path.join(GDIR, 'scratch', 'reaudit', 'r3_judged.csv')
if _r3_os.path.exists(_r3_path):
    for _r in _r3_csv.DictReader(open(_r3_path, encoding='utf-8')):
        if _r['decision'] in ('STATE', 'ENV'):
            _R3J.setdefault((_r['src'], _r['dst'], _r['kind']), []).append(
                (_r['decision'], _r['text'], [k for k in _r['kinds'].split('+') if k], _r.get('match') or ''))

# ---------------------------------------------------------------- P
# Aegis GoogleAuthProtos (generated protobuf-javalite classes): app code calls parseFrom, newBuilder, getDefaultInstance
# and the generated getters (otp/GoogleAuthInfo.java:195-460); no app code calls the static parser() accessor (grep of
# the app tree), and the lite runtime parses through dynamicMethod(GET_PARSER) on the default instance, not through the
# static accessor, so the two parser() edges written in graph_def.py (batch B24) have no basis. Every other edge the
# graph gives the runtime (evidence 'INFERRED protobuf-lite runtime') is a library dispatch: non_standard.
_R3_PROTO_DEAD = [('GoogleAuthProtos$MigrationPayload.parseFrom(byte[])', 'GoogleAuthProtos$MigrationPayload.parser'),
                  ('GoogleAuthProtos$MigrationPayload.dynamicMethod', 'GoogleAuthProtos$MigrationPayload$OtpParameters.parser')]
_R3_PROTO_REASON = ('no app code calls the static parser() accessor (grep of the app tree; otp/GoogleAuthInfo.java:195-460 '
                    'uses parseFrom, newBuilder and the getters), and the protobuf-lite runtime parses through dynamicMethod '
                    'of the default instance, not through this accessor')

# ---------------------------------------------------------------- K
_R3_KILLED = {}
_R3_LIVE = set()
_R3_ORIG_UNREACH = set(UNREACHABLE)


def _r3_manifest():
    ps = _r3_glob.glob(_r3_os.path.join(_R3_ROOT, 'final_java_only', R3_APP, 'app', '**', 'src', 'main', 'AndroidManifest.xml'),
                       recursive=True)
    acts, cfg = set(), set()
    for p in ps:
        t = open(p, encoding='utf-8', errors='replace').read()
        for m in _r3_re.finditer(r'<activity\b(.*?)>', t, _r3_re.S):
            n = _r3_re.search(r'android:name="([^"]+)"', m.group(1))
            if not n:
                continue
            s = n.group(1).split('.')[-1]
            acts.add(s)
            if _r3_re.search(r'android:configChanges="[^"]+"', m.group(1)):
                cfg.add(s)
    return acts, cfg


def _r3_extends():
    sup_ = {}
    for p in _r3_glob.glob(_r3_os.path.join(_R3_ROOT, 'final_java_only', R3_APP, 'app', '**', 'src', 'main', 'java', '**',
                                            '*.java'), recursive=True):
        for m in _r3_re.finditer(r'\bclass\s+(\w+)(?:<[^>]*>)?\s+extends\s+([\w.]+)', open(p, encoding='utf-8', errors='replace').read()):
            sup_[m.group(1)] = m.group(2).split('.')[-1]
    return sup_


_R3_ACTS, _R3_CFG = _r3_manifest()
_R3_SUP = _r3_extends() if R3_APP in ('AmazeFileManager', 'Aegis', 'AnkiDroid', 'LibreTorrent', 'MMEX') else {}


def _r3_ancestors(c):
    out, k = [c], 0
    while c in _R3_SUP and k < 20:
        c = _R3_SUP[c]
        out.append(c)
        k += 1
    return out


def _r3_config_dead(cls):
    """True when cls is an activity class (declared, or a base of a declared activity) and no declared activity that
    is cls or extends it lists android:configChanges, so the framework never calls its onConfigurationChanged."""
    simple = cls.split('$')[-1]
    users = [a for a in _R3_ACTS if simple in _r3_ancestors(a)]
    if not users:
        return False
    return not any(a in _R3_CFG for a in users)


_R3_CFG_DEAD = set()

# ---------------------------------------------------------------- R (MMEX)
_R3_REC_EDITOR = 'RecurringTransactionEditActivity.onCreate'

_R3_ORIG_EDIT = EDIT


def _r3_kill(x, kind, text, ref):
    x['kind'] = 'REGISTER'
    x['edge_class'] = 'standard'
    x['needs_state'], x['state_kinds'], x['env'], x['env_kinds'] = None, [], None, []
    _r3_note(x, 'round 3: never runs, kept as a REGISTER record: ' + text)
    _R3_KILLED.setdefault(x['dst'].split('@')[0], (kind, text, ref))


def EDIT(x):
    if _R3_ORIG_EDIT:
        _R3_ORIG_EDIT(x)
    src, dst = x['src'], x['dst']
    bsrc, bdst = src.split('@')[0], dst.split('@')[0]
    # J
    for _g in _R3J.get((src, dst, x['kind']), ()):
        if _g[3] and _g[3] not in (x.get('trigger') or ''):
            continue
        if _g[0] == 'STATE' and not x.get('needs_state'):
            x['needs_state'], x['state_kinds'] = _g[1], list(_g[2])
            _r3_note(x, 'round 3: state gate from r3_judged.csv')
            R3_LOG['J'] += 1
        elif _g[0] == 'ENV' and not x.get('env'):
            x['env'], x['env_kinds'] = _g[1], list(_g[2])
            _r3_note(x, 'round 3: env gate from r3_judged.csv')
            R3_LOG['J'] += 1
    # P
    if R3_APP == 'Aegis' and x['kind'] != 'REGISTER':
        if (src, dst) in _R3_PROTO_DEAD:
            _r3_kill(x, 'framework_never_calls', _R3_PROTO_REASON, 'SRC com/beemdevelopment/aegis/otp/GoogleAuthInfo.java:195-460')
            R3_LOG['P'] += 1
        elif (x.get('evidence') or '').startswith('INFERRED protobuf-lite runtime') and x.get('edge_class') != 'non_standard':
            x['edge_class'] = 'non_standard'
            x['via'] = 'protobuf-lite runtime (GeneratedMessageLite dispatch)'
            _r3_note(x, 'round 3: the protobuf-lite runtime makes this call (library)')
            R3_LOG['P'] += 1
    # K
    if x['kind'] != 'REGISTER' and bdst.endswith('.onConfigurationChanged') and _r3_config_dead(bdst.rsplit('.', 1)[0]):
        _R3_CFG_DEAD.add(bdst)
        _r3_kill(x, 'framework_never_calls', 'the activity declares no android:configChanges in the manifest, so a '
                 'configuration change recreates it and the framework never calls onConfigurationChanged',
                 'SRC AndroidManifest.xml (no android:configChanges); FW-SRC core/java/android/app/ActivityThread.java:4868-4900 (performActivityConfigurationChanged calls onConfigurationChanged only when every changed field is in getRealConfigChanged())')
        R3_LOG['K'] += 1
    elif x['kind'] != 'REGISTER' and (bsrc in _R3_CFG_DEAD or (bsrc.endswith('.onConfigurationChanged')
                                                               and _r3_config_dead(bsrc.rsplit('.', 1)[0]))):
        _r3_kill(x, 'framework_never_calls', 'called only from %s, which the framework never calls (no '
                 'android:configChanges in the manifest)' % bsrc, 'SRC AndroidManifest.xml (no android:configChanges)')
        R3_LOG['K'] += 1
    # R
    if (R3_APP == 'MMEX' and x['kind'] == 'CALL' and bsrc.startswith('EditTransactionCommonFunctions')
            and not src.endswith('@RECURRING') and bdst.startswith('RecurringTransaction.')):
        _r3_note(x, 'round 3 R: was %s -> %s; the shared editor helper holds the editor\'s own entity, a '
                    'RecurringTransaction only in RecurringTransactionEditActivity (RecurringTransactionEditActivity.java:103,442,604; '
                    'the checking editor holds an AccountTransaction, CheckingTransactionEditActivity.java:394,431-455)' % (src, dst))
        x['trigger'] = 'the recurring editor\'s helper %s calls %s on its RecurringTransaction' % (bsrc, bdst)
        x['src'] = _R3_REC_EDITOR
        R3_LOG['R'] += 1
    # reflection (MMEX RecurringTransaction.getStatus finding): showFragment(Class) makes the fragment with
    # classFragment.newInstance() (MainActivity.java:734-751) and hands that instance on; the hand-off edge carries the
    # reflection-made object, so it is non_standard like the creation edge itself
    if (R3_APP == 'MMEX' and bsrc == 'MainActivity.showFragment(Class)' and bdst.startswith('MainActivity.showFragment(Fragment')
            and x['kind'] != 'REGISTER' and x.get('edge_class') != 'non_standard'):
        x['edge_class'] = 'non_standard'
        x['via'] = 'Class.newInstance reflection in MainActivity.showFragment(Class) (MainActivity.java:743)'
        _r3_note(x, 'round 3: the fragment handed on was made by Class.newInstance (MainActivity.java:734-751)')
        R3_LOG['R'] += 1
    # S
    if (R3_APP == 'Aegis' and x.get('needs_state') and x['needs_state'].startswith('The camera provider is ready and a lens exists')):
        _r3_note(x, 'round 3: a device fact, not a UI session (was: %s)' % x['needs_state'])
        x['needs_state'], x['state_kinds'] = None, []
        R3_LOG['S'] += 1
    # bookkeeping for UNREACHABLE entries of killed targets
    if x['kind'] != 'REGISTER':
        _R3_LIVE.add(bdst)
        if bdst in _R3_KILLED and bdst not in _R3_ORIG_UNREACH:
            UNREACHABLE.pop(bdst, None)
    elif bdst in _R3_KILLED and bdst not in _R3_LIVE and bdst not in _R3_ORIG_UNREACH:
        k, t, ref = _R3_KILLED[bdst]
        UNREACHABLE[bdst] = (k, 'round 3: ' + t, ref, 'SOURCE')


# ---------------------------------------------------------------- Q (MMEX): new edges
if R3_APP == 'MMEX':
    _Q_FW = ('FW-SRC core/java/android/content/ContentResolver.java:753-755; FW-SRC core/java/android/content/'
             'ContentProvider.java:228-229, 240-241; SRC database/Dataset.java:79-80 (getUri is content://'
             '<MmxContentProvider authority>/...; MmxContentProvider.java:90,133)')
    e('MainActivity.populateScheduledTransactions', 'MmxContentProvider.query', 'FRAMEWORK',
      'at launch, with recurring-transaction notifications on (the default, BehaviourSettings.java:41-42), the due '
      'recurring transactions are queried from the app\'s own provider',
      evidence='SRC home/MainActivity.java:1231-1258; ' + _Q_FW,
      note='round 3 Q: the query runs before the per-row loop, so it needs no stored row')
    e('RecurringTransactionNotifications.notifyRepeatingTransaction_Internal', 'MmxContentProvider.query', 'FRAMEWORK',
      'the notification check queries the due recurring transactions from the app\'s own provider',
      evidence='SRC notifications/RecurringTransactionNotifications.java:60-72; ' + _Q_FW,
      note='round 3 Q')
    e('MmxCursorLoader.loadInBackground', 'MmxContentProvider.query', 'FRAMEWORK',
      'the cursor loader of a list page (for example the home account list, HomeFragment.java:222-247) queries the '
      'app\'s own provider on its background thread',
      evidence='SRC common/MmxCursorLoader.java:46-48; home/HomeFragment.java:222-247; INFERRED support-v4 CursorLoader.'
               'loadInBackground calls ContentResolver.query on the loader uri; ' + _Q_FW,
      note='round 3 Q')
    R3_LOG['Q'] += 3
