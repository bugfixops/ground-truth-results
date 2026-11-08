import ast, shutil, sys

G = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager'
GD = G + '/graph_def.py'
BACKUP = G + '/scratch/graph_def_before_finish_24.py'
APPLY = '--apply' in sys.argv

lines = open(GD, encoding='utf-8').read().split('\n')


def at(n):
    return lines[n - 1]


assert at(5962) == '    # AppListLoader lifecycle methods - framework calls', at(5962)
assert at(5963).startswith("    'AppListLoader.onReset': ('framework_never_calls'"), at(5963)
assert at(5966).strip() == "'SOURCE'),", repr(at(5966))
assert at(5967) == '    ', repr(at(5967))
assert at(16319) == "    ('AppListLoader.onReset', 'AppListLoader.onReleaseResources'),", repr(at(16319))

drop = set(range(5962, 5968)) | {16319}
new = [l for i, l in enumerate(lines, 1) if i not in drop]
text = '\n'.join(new)
if not text.endswith('\n'):
    text += '\n'

PAIRS = [
    ('AppDataParcelable$1.createFromParcel', 'AppDataParcelable.<init>(Parcel)'),
    ('FileUtil$MediaFile.getTemporaryAlbumId', 'FileUtil$MediaFile.installTemporaryTrack'),
    ('FileUtil.copyDummyFiles', 'FileUtil.copyDummyFile'),
    ('HybridFile.length()', 'HybridFile$2.<init>'),
    ('Coders.addEncoder', 'CoderBase.encode'),
    ('Coders.addEncoder', 'Coders$BCJDecoder.encode'),
    ('Coders.addEncoder', 'Coders$BZIP2Decoder.encode'),
    ('Coders.addEncoder', 'Coders$CopyDecoder.encode'),
    ('Coders.addEncoder', 'Coders$DeflateDecoder.encode'),
    ('Coders$DeflateDecoder.encode', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.<init>'),
    ('Coders.addEncoder', 'DeltaDecoder.encode'),
    ('Coders.addEncoder', 'LZMA2Decoder.encode'),
    ('LZMA2Decoder.encode', 'LZMA2Decoder.getOptions'),
    ('SevenZFile.getStatisticsForCurrentEntry', 'SevenZFile$2.<init>'),
    ('PropertiesSheet.setupDialog', 'PropertiesSheet$1.<init>'),
    ('SmbConnectDialog.setTint', 'SmbConnectDialog.createEditTextColorStateList'),
]

add = ['', 'sup(']
for a, b in PAIRS:
    add.append('    (%r, %r),' % (a, b))
add.append(')')
add += [
    '',
    "e('AppListLoader.onStopLoading', 'AppListLoader.onReset', 'LIFECYCLE',",
    "  'Loader reset runs after the loader is stopped: LoaderManager resets the loader when its host is destroyed, and onReset calls onStopLoading first (androidx source not read)',",
    "  evidence='SRC AppListLoader.java:143-146 onReset() calls onStopLoading(); INFERRED LoaderManager calls Loader.reset() when the host is destroyed')",
    '',
    "e('CompressedExplorerFragment$1.onActionItemClicked', 'Decompressor.decompress(String,String[])@RarDecompressor', 'CALL',",
    "  'Extract action on a .rar: the fragment decompressor is a RarDecompressor (CompressedHelper.getCompressorInstance), and decompress(String,String[]) runs with that receiver',",
    "  evidence='SRC fragments/CompressedExplorerFragment.java:329 decompressor.decompress(compressedFile.getPath(), dirs); SRC filesystem/compressed/CompressedHelper.java:113-114')",
    '',
    "e('CompressedExplorerAdapter.lambda$onBindViewHolder$2', 'Decompressor.decompress(String,String[])@RarDecompressor', 'CALL',",
    "  'Tap-to-extract on a .rar: the adapter decompressor is the RarDecompressor the fragment passes in (CompressedHelper.getCompressorInstance)',",
    "  evidence='SRC adapters/CompressedExplorerAdapter.java:290 decompressor.decompress(...); SRC fragments/CompressedExplorerFragment.java:215,243')",
]
text += '\n'.join(add) + '\n'

ast.parse(text)
print('lines removed:', len(drop), 'old', len(lines), 'new', len(text.split('\n')))
print('sup pairs added:', len(PAIRS))

if APPLY:
    shutil.copy2(GD, BACKUP)
    open(GD, 'w', encoding='utf-8').write(text)
    print('written', GD, 'backup', BACKUP)
else:
    print('dry run; pass --apply to write')
