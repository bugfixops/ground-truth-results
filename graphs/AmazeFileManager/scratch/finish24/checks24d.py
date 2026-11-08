import os, re, json

ROOT = '/Users/darshan/Desktop/yang/work/final_java_only/AmazeFileManager'
APP = ROOT + '/app/AmazeFileManager-#1837/app/src/main'
W = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager'
GD = open(W + '/graph_def.py', encoding='utf-8').read().split('\n')


def files(fn):
    out = []
    for r, _, fs in os.walk(ROOT):
        if fn in fs:
            out.append(os.path.join(r, fn))
    return out


def lines_of(p):
    return open(p, encoding='utf-8', errors='replace').read().split('\n')


def enclosing(L, n):
    # nearest line above n at 4-space method indent that looks like a declaration
    pat = re.compile(r'^    (?!if|else|for|while|switch|return|try|catch|new|case)(public |private |protected |static |final |synchronized |@\w+ )*[\w<>\[\], .?]+\s+\w+\s*\(|^    (public |private |protected )?[A-Z]\w*\s*\(')
    for i in range(n - 1, 0, -1):
        if pat.match(L[i]) and not L[i].rstrip().endswith(';'):
            return i + 1, L[i].strip()[:140]
    return None


def grep(p, rx, lo=1, hi=10**9):
    L = lines_of(p)
    for i, l in enumerate(L, 1):
        if lo <= i <= hi and re.search(rx, l):
            print('    %d: %s' % (i, l.strip()[:150]))


print('== XML inflation sites')
for pat in [r'Indicator', r'CircularColorsView', r'RoundedImageView']:
    for r, _, fs in os.walk(APP + '/res'):
        for fn in fs:
            if fn.endswith('.xml'):
                p = os.path.join(r, fn)
                for i, l in enumerate(lines_of(p), 1):
                    if re.search(pat, l) and '<' in l:
                        print('  %s %s:%d %s' % (pat, fn, i, l.strip()[:120]))

print('== graph refs')
for i, l in enumerate(GD, 1):
    if re.search(r"CircularColorsView\.<init>|Indicator\.<init>|RoundedImageView|describeContents|LayoutElementParcelable\.<init>|S_XML|S_PARCEL", l):
        print('  %d %s' % (i, l.strip()[:150]))

print('== SevenZFile coder calls and ctors')
sz = [p for p in files('SevenZFile.java') if 'sevenz' in p]
for p in sz:
    print(' ', p.split('/java/')[-1] if '/java/' in p else p)
    grep(p, r'Coders\.|public SevenZFile\(|private SevenZFile\(|SevenZFile\(|BoundedFileChannelInputStream\(|readHeaders\(|readStackEncodersAsCoders|getBytesForCoder|getOptionsFromCoder|buildDecodingStream\(', 1, 1100)

print('== SevenZipHelperTask (compress) 50-80')
p = APP + '/java/com/amaze/filemanager/asynchronous/asynctasks/compress/SevenZipHelperTask.java'
L = lines_of(p)
for n in [69, 70]:
    print('  line', n, '->', enclosing(L, n))
grep(p, r'public SevenZipHelperTask|protected .*doInBackground|class SevenZipHelperTask', 1, 200)

print('== RootHelper enclosing')
p = APP + '/java/com/amaze/filemanager/filesystem/RootHelper.java'
L = lines_of(p)
for n in [232, 300, 327]:
    print('  line', n, '->', enclosing(L, n))
grep(p, r'static .*getFilesList\(|public static .*\(', 215, 340)

print('== GeneralDialogCreation lambdas 999-1100')
p = APP + '/java/com/amaze/filemanager/ui/dialogs/GeneralDialogCreation.java'
grep(p, r'->|public static void showSortDialog|public static void showHistoryDialog', 995, 1100)

print('== ColorPref setRestartActivity / lambdas')
p = APP + '/java/com/amaze/filemanager/fragments/preference_fragments/ColorPref.java'
grep(p, r'setRestartActivity|->|void onCreate|void loadSection|void colorChangeDialog|private void|public void|protected void', 1, 400)

print('== FileUtils openFile/openWith')
p = APP + '/java/com/amaze/filemanager/utils/files/FileUtils.java'
grep(p, r'public static void openFile|public static void openWith|DatabaseViewerActivity', 560, 960)

print('== LayoutElementParcelable header')
p = APP + '/java/com/amaze/filemanager/adapters/data/LayoutElementParcelable.java'
grep(p, r'class LayoutElementParcelable|describeContents', 1, 200)

print('== AsyncTaskResult ctor sites and ColorPickerDialog SavedState ctors')
p = APP + '/java/com/amaze/filemanager/ui/dialogs/ColorPickerDialog.java'
grep(p, r'SavedState\(', 240, 300)
