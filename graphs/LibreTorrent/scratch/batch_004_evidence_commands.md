# Batch 4 evidence command record

Source root used for every command below:
`/Users/darshan/Desktop/yang/work/final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent`

The command used to save printed source excerpts to `scratch/batch_004_printed.txt` was:

```sh
SRC='/Users/darshan/Desktop/yang/work/final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent'
{
  nl -ba "$SRC/core/urlnormalizer/NormalizeUrl.java" | sed -n '155,192p'
  nl -ba "$SRC/core/storage/TorrentRepositoryImpl.java" | sed -n '130,182p'
  nl -ba "$SRC/core/system/FileSystemFacadeImpl.java" | sed -n '155,180p;325,370p'
  nl -ba "$SRC/core/system/SafFsModule.java" | sed -n '30,175p'
  nl -ba "$SRC/core/system/SafFileSystem.java" | sed -n '90,165p;370,500p'
  nl -ba "$SRC/core/settings/SettingsRepositoryImpl.java" | sed -n '30,85p'
  nl -ba "$SRC/core/sorting/BaseSorting.java" | sed -n '20,65p'
  nl -ba "$SRC/core/storage/DatabaseMigration.java" | sed -n '35,145p'
  nl -ba "$SRC/core/storage/FeedRepositoryImpl.java" | sed -n '50,90p'
  nl -ba "$SRC/core/storage/TorrentRepositoryImpl.java" | sed -n '35,60p;140,174p'
  nl -ba "$SRC/core/storage/converter/UriConverter.java" | sed -n '20,60p'
  nl -ba "$SRC/core/utils/BencodeFileTreeUtils.java" | sed -n '35,58p'
  nl -ba "$SRC/core/utils/BindingAdapterUtils.java" | sed -n '30,54p'
  nl -ba "$SRC/core/utils/DateUtils.java" | sed -n '24,48p'
  nl -ba "$SRC/core/utils/TorrentContentFileTreeUtils.java" | sed -n '34,58p'
  nl -ba "$SRC/core/utils/Utils.java" | sed -n '32,60p;215,232p'
  nl -ba "$SRC/core/urlnormalizer/PathResolver.java" | sed -n '1,28p'
  nl -ba "$SRC/core/urlnormalizer/PercentEncoder.java" | sed -n '1,30p'
  nl -ba "$SRC/core/system/SystemFacadeHelper.java" | sed -n '24,60p'
} > /Users/darshan/Desktop/yang/work/graphs/LibreTorrent/scratch/batch_004_printed.txt
```

Exact occurrence searches were run against the source root and saved to `scratch/batch_004_exact_calls.txt`. Each call used `rg -n -F '<literal>' "$SRC"`; the literals, in order, were:

```text
getSerializeFileFormat(
getSerializeMimeType(
getTorrentDataDir(
makeTorrentDataDir(
new FileDataModel(
new UriConverter(
fromValue(
normalizeURL(
new SystemFacadeHelper(
new SettingsRepositoryImpl.Default(
isDownloading(
Direction.fromValue(
new DatabaseMigration(
new OldDataModel(
new RoomDatabaseMigration.OldDataModel(
new RoomDatabaseMigration(
new TorrentRepositoryImpl.FileDataModel(
new FileDataModel(
new SystemFacadeHelper(
new NormalizeUrl(
NormalizeUrl.normalize(
new PathResolver(
new PercentEncoder(
new BencodeFileTreeUtils(
new BindingAdapterUtils(
new DateUtils(
new TorrentContentFileTreeUtils(
new Utils(
```

The complete printed occurrence output is `scratch/batch_004_exact_calls.txt`. The source-range inspection and direct call-site output from the helper pass is preserved separately in `scratch/batch_004_helper_printed.txt`.
