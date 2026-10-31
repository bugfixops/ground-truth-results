import json, os, re
ROOT = '/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo'
def find_file(cls_short):
    for dp, dn, fn in os.walk(ROOT):
        if cls_short + '.java' in fn:
            return os.path.join(dp, cls_short + '.java')
    return None
def decl_line(cls_full, name, ctor=False):
    short = cls_full.split('$')[0].split('.')[-1]
    p = find_file(short)
    if not p:
        return None
    lines = open(p, encoding='utf-8', errors='replace').read().split('\n')
    if ctor:
        pat = re.compile(r'\b(class|interface|enum)\s+' + re.escape(cls_full.split('$')[-1]) + r'\b')
        if '$' in cls_full:
            pat = re.compile(r'\b(class|interface)\s+' + re.escape(cls_full.split('$')[-1]) + r'\b')
    else:
        pat = re.compile(r'\b' + re.escape(name) + r'\s*\(')
    for i, l in enumerate(lines, 1):
        if pat.search(l) and not l.strip().startswith(('return', '//', '*')) and ('new ' + name) not in l:
            rel = os.path.relpath(p, ROOT)
            return '%s:%d' % (rel, i)
    return None
items = []   # (method, kind, reason)
for c in ['CSVExporter','CSVImporter','Mnemosyne2CardsExporter','Mnemosyne2CardsImporter','MnemosyneXMLExporter',
          'MnemosyneXMLImporter','QATxtExporter','QATxtImporter','Supermemo2008XMLImporter','SupermemoXMLImporter',
          'TabTxtImporter','ZipExporter','ZipImporter']:
    items.append(('%s.getSrcExtension' % c, 'no_trigger_in_app',
        'getSrcExtension() is implemented by every converter and declared on the Converter interface; no call of it exists in the app (grep: declarations only; bytecode: no invoke site)'))
for m in ['ErrorUtil.showFatalError', 'ErrorUtil.showNonFatalError']:
    items.append((m, 'no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)'))
for m in ['AMStringUtils.isInteger', 'AMUiUtil.convertPxToDp', 'AMGUIUtility.getDialogFinishListener', 'RecentListUtil.getRecentDBPath',
          'DownloaderUtils.validateDBName', 'DownloaderUtils.validateEmail', 'AnyMemoExecutor.waitTask', 'NotificationUtil.getNewCount',
          'SetAlarmReceiver.setWidgetUpdateAlarm', 'SetAlarmReceiver.cancelWidgetUpdateAlarm', 'CardDaoImpl.getRandomReviewedCards',
          'CardDaoImpl.searchPrevCard', 'CategoryDaoImpl.populateCategory', 'FilterDaoImpl.getActiveFilter',
          'AbstractDownloaderFragment.getDownloadItemCount', 'CardImageGetter.scaleBitmap', 'GradeButtonsFragment.setButtonText',
          'FlipableCardFragment.flipTo', 'EditTabFragment.setRecentListUtil', 'CardPlayerService$LocalBinder.getCurrentPlayingCard']:
    items.append((m, 'no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)'))
out = []
bad = []
for m, kind, reason in items:
    cls_full, name = m.rsplit('.', 1)
    ref = decl_line(cls_full, name)
    if ref is None:
        bad.append(m); continue
    out.append("UNREACHABLE['%s'] = ('%s', %r, 'SRC %s', 'SOURCE')" % (m, kind, reason, ref))
open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch/L1.py', 'w').write('\n'.join(out) + '\n')
print('written', len(out), 'missing', bad)
