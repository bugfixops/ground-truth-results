# Round 2 rules (Kiro, 2026-11-10), executed at the end of graphs/<App>/graph_def.py of the five re-audited apps, in the
# graph_def namespace (R2_APP and R2_DIALOG_RULE are set there before the exec). They fix the causes of the 21 wrong
# class labels that review/rounds/1/adjudication.csv found (source_supports = sample):
#   A  state gates the W7 pre-screen did not show (tools_dev/guard_prescreen_r2.py; judged rows in
#      graphs/<App>/scratch/reaudit/r2_judged.csv, which also holds the judged ENV rows of cause B)
#   B  env gates for data and devices only outside systems provide
#   C  dispatch and trigger rules for methods that never run
#   D  runtime-permission prompts and menus opened in the same GUI sequence are GUI actions, not state
#   E  the dialog rule (review/TASK_NOTE.md: a UI session, an open dialog, a selection or an unsaved form, is state),
#      behind R2_DIALOG_RULE
# An edge that never runs is turned into a REGISTER edge (the builder neither follows nor warns about REGISTER edges),
# so hand-written and automatic edges are handled alike; its note keeps the reason. A method whose every incoming
# edge is turned off this way gets an UNREACHABLE entry with the rule's kind and reason.
import csv as _r2_csv
import glob as _r2_glob
import os as _r2_os
import re as _r2_re

_R2_ROOT = _r2_os.path.normpath(_r2_os.path.join(GDIR, '..', '..'))
_R2_SRC = None


def _r2_sources():
    global _R2_SRC
    if _R2_SRC is None:
        _R2_SRC = {}
        for p in _r2_glob.glob(_r2_os.path.join(_R2_ROOT, 'final_java_only', R2_APP, 'app', '**', 'src', 'main', 'java',
                                                '**', '*.java'), recursive=True):
            _R2_SRC[p] = open(p, encoding='utf-8', errors='replace').read()
    return _R2_SRC


def _r2_note(x, text):
    x['note'] = ((x.get('note') + ' | ') if x.get('note') else '') + text


# ---------------------------------------------------------------- A: judged rows (r2_judged.csv)
_R2J = {}
_r2_path = _r2_os.path.join(GDIR, 'scratch', 'reaudit', 'r2_judged.csv')
if _r2_os.path.exists(_r2_path):
    for _r in _r2_csv.DictReader(open(_r2_path, encoding='utf-8')):
        if _r['decision'] in ('STATE', 'ENV'):
            _R2J.setdefault((_r['src'], _r['dst'], _r['kind']), []).append(
                (_r['decision'], _r['text'], [k for k in _r['kinds'].split('+') if k], _r.get('match') or ''))

# ---------------------------------------------------------------- B: data and devices from outside
# (regex on an existing STATE gate text, env text, env kinds): the gate is moved from state to env.
_R2_STATE_TO_ENV = {
    # AmazeFileManager-03, -15, -37: a saved SFTP entry is written only after getConnection() reached a real SSH
    # server (host key fetch and authentication, SftpConnectDialog.java:343-354; SshConnectionPool.java:146); the
    # emulator network has no SSH server. The same holds for every step that reads a saved SFTP connection, and for
    # the cloud/SMB/SFTP drawer entries (a cloud account or an SMB host is outside data too).
    'AmazeFileManager': [
        # Round 3 (reviewer): SMB is not in this gate. A saved SMB entry is made without any server
        # (SmbConnectDialog.java:220-281; MainActivity.addConnection :1679-1687), so a step that a saved SMB entry
        # satisfies (the cloud/SMB/SFTP drawer entry) keeps its state gate.
        (r'^(?!.*\bSMB\b).*(saved SFTP connection|SFTP entry|ssh:/ entry)',
         'a saved SFTP connection exists only after a connect to a real SSH server '
         '(SftpConnectDialog.java:343-354; SshConnectionPool.java:146); the emulator network has none', ['network']),
        # D for the same app: a storage-permission denial is a GUI action on the system prompt
    ],
    # Aegis-05: a biometric slot and every biometric preference need an enrolled strong biometric on the device
    # (BiometricsHelper.isAvailable, helpers/BiometricsHelper.java:13-27); the API 27 emulator has none.
    'Aegis': [
        (r'[Bb]iometric',
         'the device has an enrolled strong biometric (BiometricsHelper.isAvailable, helpers/BiometricsHelper.java:13-27); '
         'a biometric slot exists only on such a device; the API 27 emulator has none', ['hardware']),
    ],
}
# AmazeFileManager-41: launchSAF runs only when checkFolder returns 2: the folder is on a removable SD card that the
# app cannot write directly (filesystem/Operations.java:300-305,491-520; filesystem/FileUtil.java:739-759,813). The
# API 27 emulator has no removable card, so every edge into an ErrorCallBack.launchSAF is env hardware.
_R2_SAF_ENV = ('a removable SD card holds the folder and the app cannot write to it directly (checkFolder returns 2, '
               'filesystem/Operations.java:300-305,491-520; filesystem/FileUtil.java:739-759,813); the API 27 '
               'emulator has no removable card')

# ---------------------------------------------------------------- C: dispatch and trigger rules
# C1 dead dispatch: a call that reaches a base method only for objects that never get there.
_R2_DEAD_DISPATCH = {
    'Aegis': [
        # Aegis-15: processDecryptedImporterState calls convert only on a decrypted state (ImportEntriesActivity.java:
        # 178-208); every decrypted or plain state class overrides convert (the 19 importers' State/DecryptedState
        # classes) and none calls super.convert; the encrypted states, which keep the base convert, are decrypted
        # first (their decrypt listeners hand on only decrypted states).
        ('ImportEntriesActivity.processDecryptedImporterState', 'DatabaseImporter$State.convert',
         'no_trigger_in_app', 'every state that reaches processDecryptedImporterState overrides convert (no super.convert); '
         'encrypted states are decrypted first (ImportEntriesActivity.java:178-208; importers/DatabaseImporter.java:163)',
         'SRC com/beemdevelopment/aegis/ui/ImportEntriesActivity.java:178-208; com/beemdevelopment/aegis/importers/DatabaseImporter.java:163'),
    ],
}
# C2 hook dispatch (AnkiDroid-39): Hooks.runFilter(name, ...) runs only the hooks that addHook registered under that
# name (libanki/hooks/Hooks.java:138-150). Registrations: fmod_hint (HintFilter.java), fmod_kanji, fmod_kana,
# fmod_furigana (FuriganaFilters.java:35-37), advancedStatistics (AdvancedStatistics.java:48), mungeQA (LaTeX,
# HebrewFixFilter, ChessFilter), leech (Leech.java). No hook is registered under mungeFields.
_R2_HOOKS = {
    'Hooks.runFilter@mungeFields': set(),
    'Hooks.runFilter@advancedStatistics': {'AdvancedStatistics'},
    'Hooks.runFilter@mungeQA': {'LaTeX$LaTeXFilter', 'HebrewFixFilter', 'ChessFilter'},
    'Hooks.runFilter': {'HintFilter$Hint', 'FuriganaFilters$Kanji', 'FuriganaFilters$Kana', 'FuriganaFilters$Furigana'},
}
_R2_HOOK_REF = 'SRC com/ichi2/libanki/hooks/Hooks.java:138-150; com/ichi2/libanki/hooks/FuriganaFilters.java:35-37'
# C3 AsyncTask.onCancelled (AmazeFileManager-11): the framework calls onCancelled only after AsyncTask.cancel()
# (fw core/java/android/os/AsyncTask.java:462,479). When no file that creates the task class (new X() or the class's
# own file) calls cancel( on anything, the callback never runs.
# C4 Parcelable.describeContents (LibreTorrent-23): the framework calls describeContents of an app object only from
# Bundle/Intent.hasFileDescriptors on unparcelled extras; the start of an activity checks them in system_server, where
# the extras are parcelled and the native check is used (fw core/java/android/os/Bundle.java:316-340;
# core/java/android/content/Intent.java:6958,9552; services/core/java/com/android/server/am/ActivityStarter.java:681).
# So a framework edge into an app describeContents never runs; direct app calls are kept.
_R2_DESC_REF = ('FW-SRC core/java/android/os/Bundle.java:316-340; core/java/android/content/Intent.java:6958,9552; '
                'services/core/java/com/android/server/am/ActivityStarter.java:681')

# ---------------------------------------------------------------- D: GUI actions, not state
_R2_NOT_STATE = {
    # Aegis-33: the floating action menu and the search box are opened by the GUI sequence itself; the written rule
    # (review/TASK_NOTE.md) counts a selection, an open dialog or an unsaved form as a UI session, not an open menu.
    'Aegis': [r'^The floating action menu is open', r'^The search box is expanded'],
    # a denial on the runtime-permission prompt is a GUI action (TASK_NOTE: permission prompts are GUI)
    'AmazeFileManager': [r'^the storage permission was denied once before'],
}

# ---------------------------------------------------------------- E: the dialog rule (behind R2_DIALOG_RULE)
_R2_DIALOG_DST = _r2_re.compile(
    r'\.(onPositive|onNegative|onNeutral|onAny|onSelection|onInput|onClick|confirm|onSelected|onTagClicked|'
    r'onActionItemClicked|onCreateActionMode|onPrepareActionMode|onDestroyActionMode|onItemCheckedStateChanged|'
    r'onSelectionChanged|onItemStateChanged)$|lambda\$')
_R2_DIALOG_SRC = _r2_re.compile(r'Dialog|dialog|ActionMode|MultiChoice|Selection')
_R2_DIALOG_TEXT = ('session: the step runs inside an open dialog, selection or action mode that the same GUI sequence '
                   'opened (review/TASK_NOTE.md: a UI session is state)')


def _r2_is_dialog_page(n):
    return bool(_r2_re.match(r'S_(DLG|DIALOG)', n)) or '_DLG_' in n


# ---------------------------------------------------------------- the EDIT hook
_R2_KILLED = {}      # dst -> (kind, text, ref) for edges turned off
_R2_LIVE = set()     # dst with a live incoming edge
_R2_ORIG_UNREACH = set(UNREACHABLE)
R2_LOG = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
_R2_ORIG_EDIT = EDIT


def _r2_kill(x, kind, text, ref):
    x['kind'] = 'REGISTER'
    x['edge_class'] = 'standard'
    x['needs_state'], x['state_kinds'], x['env'], x['env_kinds'] = None, [], None, []
    _r2_note(x, 'round 2 C: never runs, kept as a REGISTER record: ' + text)
    _R2_KILLED.setdefault(x['dst'].split('@')[0], (kind, text, ref))
    R2_LOG['C'] += 1


_R2_CANCEL = {}


def _r2_cancel_called(cls):
    """True when some app code can cancel a task of class cls: a variable or field of that type, or one assigned a new
    instance of it, has .cancel( called on it anywhere in the app, or the class's own file calls cancel(."""
    simple = cls.split('$')[-1]
    if simple in _R2_CANCEL:
        return _R2_CANCEL[simple]
    S = _r2_sources()
    names = set()
    for t in S.values():
        names |= set(_r2_re.findall(r'\b%s(?:<[^>]*>)?\s+(\w+)\s*[=;,)]' % _r2_re.escape(simple), t))
        names |= set(_r2_re.findall(r'\b(\w+)\s*=\s*new\s+(?:[\w.]+\.)?%s\s*\(' % _r2_re.escape(simple), t))
    hit = any(_r2_re.search(r'\b(%s)\s*\.cancel\s*\(' % '|'.join(map(_r2_re.escape, names)), t) for t in S.values()) if names else False
    # an instance that leaves its creator (returned, or created inside a return statement) may be held under a
    # supertype such as AsyncTask and cancelled there (AnkiDroid Statistics.java:414,543): count it as cancellable
    if names and any(_r2_re.search(r'\breturn\s+(%s)\s*;' % '|'.join(map(_r2_re.escape, names)), t) for t in S.values()):
        hit = True
    if any(_r2_re.search(r'\breturn\s+new\s+(?:[\w.]+\.)?%s\s*\(' % _r2_re.escape(simple), t) for t in S.values()):
        hit = True
    own = [t for p, t in S.items() if _r2_os.path.basename(p) == simple + '.java']
    hit = hit or any(_r2_re.search(r'(?<![\w.])cancel\s*\(\s*(true|false)\s*\)', t) for t in own)
    _R2_CANCEL[simple] = hit
    return hit


def EDIT(x):
    if _R2_ORIG_EDIT:
        _R2_ORIG_EDIT(x)
    src, dst = x['src'], x['dst']
    bdst = dst.split('@')[0]
    # A (and judged ENV)
    for _g in _R2J.get((src, dst, x['kind']), ()):
        if _g[3] and _g[3] not in (x.get('trigger') or ''):
            continue
        if _g[0] == 'STATE' and not x.get('needs_state'):
            x['needs_state'], x['state_kinds'] = _g[1], list(_g[2])
            _r2_note(x, 'round 2 A: state gate from r2_judged.csv')
            R2_LOG['A'] += 1
        elif _g[0] == 'ENV' and not x.get('env'):
            x['env'], x['env_kinds'] = _g[1], list(_g[2])
            _r2_note(x, 'round 2 B: env gate from r2_judged.csv')
            R2_LOG['B'] += 1
    # B
    for rx, text, kinds in _R2_STATE_TO_ENV.get(R2_APP, ()):
        if x.get('needs_state') and _r2_re.search(rx, x['needs_state']):
            _r2_note(x, 'round 2 B: state gate moved to env (was: %s)' % x['needs_state'])
            if not x.get('env'):
                x['env'], x['env_kinds'] = text, list(kinds)
            x['needs_state'], x['state_kinds'] = None, []
            R2_LOG['B'] += 1
    if (R2_APP == 'AmazeFileManager' and _r2_re.search(r'\.launchSAF\(', bdst) and x['kind'] in ('CALL', 'FRAMEWORK')
            and not src.split('@')[0].startswith(bdst.split('(')[0]) and not x.get('env')):
        x['env'], x['env_kinds'] = _R2_SAF_ENV, ['hardware']
        _r2_note(x, 'round 2 B: removable SD card')
        R2_LOG['B'] += 1
    # C
    if x['kind'] != 'REGISTER':
        for s, d, kind, text, ref in _R2_DEAD_DISPATCH.get(R2_APP, ()):
            if src.split('@')[0] == s and bdst == d:
                _r2_kill(x, kind, text, ref)
                break
    if x['kind'] != 'REGISTER' and R2_APP == 'AnkiDroid' and src in _R2_HOOKS and bdst.endswith('.runFilter'):
        if bdst.rsplit('.', 1)[0] not in _R2_HOOKS[src]:
            _r2_kill(x, 'no_trigger_in_app', 'Hooks.runFilter runs only the hooks registered under its name, and %s is '
                     'not registered under %s (Hooks.java:138-150)' % (bdst.rsplit('.', 1)[0], src.partition('@')[2] or 'fmod_*'),
                     _R2_HOOK_REF)
    if (x['kind'] in ('FRAMEWORK', 'ASYNC') and bdst.endswith('.onCancelled') and not src.split('@')[0].endswith('.onCancelled')):
        c = bdst.rsplit('.', 1)[0]
        if not _r2_cancel_called(c):
            _r2_kill(x, 'framework_never_calls', 'the framework calls onCancelled only after cancel(), and no file that '
                     'creates %s calls cancel (fw AsyncTask.java:462,479)' % c,
                     'FW-SRC core/java/android/os/AsyncTask.java:462,479')
    if x['kind'] == 'FRAMEWORK' and bdst.endswith('.describeContents'):
        _r2_kill(x, 'framework_never_calls', 'the framework calls describeContents of an app object only from '
                 'hasFileDescriptors on unparcelled extras, which the activity start checks in system_server on '
                 'parcelled data (Bundle.java:316-340; ActivityStarter.java:681)', _R2_DESC_REF)
    # D
    for rx in _R2_NOT_STATE.get(R2_APP, ()):
        if x.get('needs_state') and _r2_re.search(rx, x['needs_state']):
            _r2_note(x, 'round 2 D: a GUI action in the same sequence, not state (was: %s)' % x['needs_state'])
            x['needs_state'], x['state_kinds'] = None, []
            R2_LOG['D'] += 1
    # E
    if R2_DIALOG_RULE and x['kind'] != 'REGISTER' and not x.get('needs_state'):
        if ((x['kind'] == 'GUI' and _r2_is_dialog_page(src))
                or (x['kind'] in ('FRAMEWORK', 'GUI') and _R2_DIALOG_SRC.search(src.split('@')[0]) and _R2_DIALOG_DST.search(bdst))):
            x['needs_state'], x['state_kinds'] = _R2_DIALOG_TEXT, ['session']
            _r2_note(x, 'round 2 E: dialog rule')
            R2_LOG['E'] += 1
    # bookkeeping for the UNREACHABLE entries of C
    if x['kind'] != 'REGISTER':
        _R2_LIVE.add(bdst)
        UNREACHABLE.pop(bdst, None) if (bdst in _R2_KILLED and bdst not in _R2_ORIG_UNREACH) else None
    elif bdst in _R2_KILLED and bdst not in _R2_LIVE and bdst not in _R2_ORIG_UNREACH:
        k, t, ref = _R2_KILLED[bdst]
        UNREACHABLE[bdst] = (k, 'round 2 C: ' + t, ref, 'SOURCE')
