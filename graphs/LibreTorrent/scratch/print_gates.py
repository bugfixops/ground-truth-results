from pathlib import Path

ROOT = Path('/Users/darshan/Desktop/yang/work/final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main')
REFERENCES = [
    ('AndroidManifest.xml', 62, 100),
    ('AndroidManifest.xml', 141, 162),
    ('AndroidManifest.xml', 178, 205),
    ('AndroidManifest.xml', 256, 277),
    ('java/org/proninyaroslav/libretorrent/receiver/BootReceiver.java', 43, 58),
    ('java/org/proninyaroslav/libretorrent/service/TorrentService.java', 497, 522),
    ('java/org/proninyaroslav/libretorrent/service/Scheduler.java', 60, 105),
    ('java/org/proninyaroslav/libretorrent/ui/TorrentNotifier.java', 230, 239),
    ('java/org/proninyaroslav/libretorrent/ui/customviews/EmptyRecyclerView.java', 69, 76),
    ('java/org/proninyaroslav/libretorrent/ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java', 251, 280),
    ('java/org/proninyaroslav/libretorrent/ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java', 404, 414),
    ('java/org/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java', 189, 218),
    ('java/org/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java', 329, 339),
    ('java/org/proninyaroslav/libretorrent/ui/feeds/FeedFragment.java', 148, 177),
    ('java/org/proninyaroslav/libretorrent/ui/feeds/FeedFragment.java', 404, 414),
    ('java/org/proninyaroslav/libretorrent/ui/main/MainFragment.java', 168, 192),
    ('java/org/proninyaroslav/libretorrent/ui/main/MainFragment.java', 492, 502),
    ('java/org/proninyaroslav/libretorrent/ui/addtorrent/DownloadableFilesAdapter.java', 57, 57),
    ('java/org/proninyaroslav/libretorrent/ui/addtorrent/DownloadableFilesAdapter.java', 69, 69),
    ('java/org/proninyaroslav/libretorrent/ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java', 366, 366),
    ('java/org/proninyaroslav/libretorrent/ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java', 384, 408),
    ('java/org/proninyaroslav/libretorrent/ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java', 73, 73),
    ('java/org/proninyaroslav/libretorrent/ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java', 85, 85),
    ('java/org/proninyaroslav/libretorrent/ui/detailtorrent/pages/peers/PeerListAdapter.java', 59, 59),
    ('java/org/proninyaroslav/libretorrent/ui/detailtorrent/pages/peers/PeerListAdapter.java', 71, 71),
    ('java/org/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java', 298, 330),
    ('java/org/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerListAdapter.java', 70, 70),
    ('java/org/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerListAdapter.java', 82, 82),
    ('java/org/proninyaroslav/libretorrent/ui/feeditems/FeedItemsAdapter.java', 64, 64),
    ('java/org/proninyaroslav/libretorrent/ui/feeditems/FeedItemsAdapter.java', 76, 76),
    ('java/org/proninyaroslav/libretorrent/ui/feeds/FeedChannelListAdapter.java', 79, 79),
    ('java/org/proninyaroslav/libretorrent/ui/feeds/FeedChannelListAdapter.java', 91, 91),
    ('java/org/proninyaroslav/libretorrent/ui/feeds/FeedFragment.java', 356, 405),
    ('java/org/proninyaroslav/libretorrent/ui/filemanager/FileManagerAdapter.java', 74, 74),
    ('java/org/proninyaroslav/libretorrent/ui/filemanager/FileManagerAdapter.java', 82, 82),
    ('java/org/proninyaroslav/libretorrent/ui/filemanager/FileManagerSpinnerAdapter.java', 128, 128),
    ('java/org/proninyaroslav/libretorrent/ui/filemanager/FileManagerSpinnerAdapter.java', 134, 134),
    ('java/org/proninyaroslav/libretorrent/ui/log/LogAdapter.java', 48, 48),
    ('java/org/proninyaroslav/libretorrent/ui/log/LogAdapter.java', 60, 60),
    ('java/org/proninyaroslav/libretorrent/ui/main/MainFragment.java', 460, 494),
    ('java/org/proninyaroslav/libretorrent/ui/main/TorrentListAdapter.java', 76, 76),
    ('java/org/proninyaroslav/libretorrent/ui/main/TorrentListAdapter.java', 88, 88),
    ('java/org/proninyaroslav/libretorrent/ui/main/drawer/TagsAdapter.java', 60, 60),
    ('java/org/proninyaroslav/libretorrent/ui/main/drawer/TagsAdapter.java', 96, 104),
    ('java/org/proninyaroslav/libretorrent/ui/tag/TagsAdapter.java', 46, 46),
    ('java/org/proninyaroslav/libretorrent/ui/tag/TagsAdapter.java', 58, 58),
]

print('COMMAND: python3 -I graphs/LibreTorrent/scratch/print_gates.py')
for relative, first, last in REFERENCES:
    path = ROOT / relative
    print(f'### {relative}:{first}-{last}')
    lines = path.read_text(errors='replace').splitlines()
    for number in range(first, min(last, len(lines)) + 1):
        print(f'{number}: {lines[number - 1]}')
