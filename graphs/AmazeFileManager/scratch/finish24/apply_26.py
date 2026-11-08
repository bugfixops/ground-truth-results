import difflib
import re
import sys

PATH = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py'
APPLY = '--apply' in sys.argv
GD = open(PATH, encoding='utf-8').read().split('\n')
ORIG = list(GD)


def dd(line):
    s = re.sub(r"'[^']*'", '', line)
    return s.count('(') - s.count(')')


def span(n):
    i = n - 1
    d, j = 0, i
    while True:
        d += dd(GD[j])
        if d <= 0:
            return i, j
        j += 1
        assert j < len(GD), n


def arg(n, prefix, extra):
    assert GD[n - 1].startswith(prefix), (n, GD[n - 1][:120])
    i, j = span(n)
    last = GD[j]
    assert last.endswith(')'), (n, last[-80:])
    GD[j] = last[:-1] + ', ' + extra + ')'


def drop(a, b, expect):
    assert GD[a - 1] == expect, (a, GD[a - 1])
    assert GD[a].startswith("e('CloudStreamServer.<init>(File)'"), (a, GD[a][:120])
    assert GD[b - 1].endswith("(second constructor)')"), (b, GD[b - 1][:120])
    del GD[a - 1:b]


def block(a, b, first, last, new):
    assert GD[a - 1].startswith(first), (a, GD[a - 1][:120])
    assert GD[b - 1].startswith(last), (b, GD[b - 1][:120])
    GD[a - 1:b] = new


UNREACH = [
    "UNREACHABLE['CloudStreamServer.lambda$new$1'] = ('no_trigger_in_app',",
    "  'lambda in the CloudStreamServer(File) constructor; that constructor has no caller in the app',",
    "  'SRC CloudStreamServer.java:226-229; SRC CloudStreamer.java:31 calls super(int,File) only', 'SOURCE')",
]

HEADER = [
    "# ==== AboutActivity (src/fdroid; labelled in the overnight convert run 2026-10-30)",
    "e('PrefFrag.onPreferenceClick', 'AboutActivity.<init>', 'INTENT', 'Intent created for AboutActivity from the about preference',",
    "  evidence='SRC PrefFrag.java:204')",
    "e('AboutActivity.<init>', 'AboutActivity.onCreate', 'FRAMEWORK', 'Framework calls onCreate after construction',",
    "  evidence=FW_ACTIVITY)",
    "e('AboutActivity.onCreate', 'AboutActivity.calculateHeaderViewParams', 'CALL', 'onCreate sizes the header from the screen width',",
    "  evidence='SRC AboutActivity.java:79')",
    "e('AboutActivity.onCreate', 'AboutActivity.switchIcons', 'CALL', 'onCreate switches divider colours for dark themes',",
    "  evidence='SRC AboutActivity.java:87')",
    "e('AboutActivity.onCreate', 'AboutActivity.lambda$onCreate$0', 'CALL', 'Palette.generate listener sets scrim colours',",
    "  evidence='SRC AboutActivity.java:93-98')",
    "e('AboutActivity.onCreate', 'AboutActivity.lambda$onCreate$1', 'CALL', 'AppBarLayout offset listener sets title alpha',",
    "  evidence='SRC AboutActivity.java:100-102')",
    "e('AboutActivity.onCreate', 'AboutActivity.onClick', 'GUI', 'activity_about.xml views declare android:onClick=\"onClick\"; setContentView in onCreate inflates them',",
    "  evidence='SRC res/layout/activity_about.xml:89,132,167; SRC AboutActivity.java:69', cls='non_standard', via='android:onClick reflection lookup of onClick(View)')",
    "e('AboutActivity.onCreate', 'AboutActivity.onOptionsItemSelected', 'FRAMEWORK', 'Toolbar home-up click is delivered to onOptionsItemSelected',",
    "  evidence=FW_ACTIVITY + '; SRC AboutActivity.java:83')",
    "e('AboutActivity.onClick', 'AboutActivity.openURL', 'CALL', 'onClick opens a URL for the row tapped',",
    "  evidence='SRC AboutActivity.java:170,174,206,210,214,218,222,226')",
]

i, j = span(14570)
assert GD[14569].startswith("UNREACHABLE['CloudStreamServer.<init>(File)']"), GD[14569][:120]
GD[j + 1:j + 1] = UNREACH

block(13456, 13460, '# ==== AboutActivity (flavor-only', '# These must be marked INCOMPLETE', HEADER)

arg(12516, "e('PreferencesActivity.onBackPressed'", "cls='standard'")
arg(11681, "e('TextEditorActivity.lambda$load$4'", "cls='standard'")
arg(10628, "e('FtpService.onStartCommand'", "cls='non_standard', via='EventBus post of FtpReceiverActions to @Subscribe methods'")
drop(10387, 10389, '# CloudStreamServer.<init> creates lambda$new$1 (from second constructor)')
arg(3746, "e('FtpTileService.onFtpReceiverActions'", "cls='standard'")
arg(3713, "e('FtpService.run'", "cls='standard'")
arg(3566, "e('FtpServerFragment.onResume'", "cls='non_standard', via='EventBus @Subscribe delivery of FtpReceiverActions'")

diff = list(difflib.unified_diff(ORIG, GD, 'before', 'after', lineterm='', n=0))
print('changed lines:', sum(1 for d in diff if d[:1] in '+-' and d[:3] not in ('+++', '---')))
print('\n'.join(diff[:400]))

if APPLY:
    open(PATH, 'w', encoding='utf-8').write('\n'.join(GD))
    print('APPLIED')
else:
    print('DRY RUN (no write)')
