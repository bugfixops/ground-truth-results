# Kiro k01 (2026-11-03, handover Step 6): clear the "UNREACHABLE but has incoming edges" warnings.
# Each edge below starts at a method that never runs in the standard configuration (fresh install, API 27),
# so the call it records never runs either; the target keeps its UNREACHABLE label.
# Printed lines: graphs/LibreTorrent/scratch/kiro/prints/step6_warnings.txt.
# The 5 hand-written edges of this set are dropped by _K6_HAND_DROPS near the top of graph_def.py
# (SUPPRESS only removes automatic bytecode edges).

SUPPRESS.update({
    # Parcelable CREATOR.createFromParcel -> the Parcel constructor. Each createFromParcel is UNREACHABLE
    # (no_trigger_in_app: no unparcel site of that type in the app; reasons in methods.csv), and its body
    # is only "return new X(source);" at the cited line.
    ('AdvancedTorrentInfo$1.createFromParcel', 'AdvancedTorrentInfo.<init>(Parcel)'),   # AdvancedTorrentInfo.java:123-126
    ('MagnetInfo$1.createFromParcel', 'MagnetInfo.<init>(Parcel)'),                     # MagnetInfo.java:83-86
    ('PeerInfo$1.createFromParcel', 'PeerInfo.<init>(Parcel)'),                         # PeerInfo.java:170-173
    ('SessionStats$1.createFromParcel', 'SessionStats.<init>(Parcel)'),                 # SessionStats.java:83-86
    ('FeedItem$1.createFromParcel', 'FeedItem.<init>(Parcel)'),                         # FeedItem.java:118-121
    ('Torrent$1.createFromParcel', 'Torrent.<init>(Parcel)'),                           # Torrent.java:160-163
    ('BencodeFileItem$1.createFromParcel', 'BencodeFileItem.<init>(Parcel)'),           # BencodeFileItem.java:99-102
    ('TorrentMetaInfo$1.createFromParcel', 'TorrentMetaInfo.<init>(Parcel)'),           # TorrentMetaInfo.java:153-156
    # AppearanceSettingsFragment.lambda$new$1 (ringtone-picker result, UNREACHABLE closed_by_api_level: launched
    # only from initLegacyNotifySettings, which runs only when SDK_INT < O) -> pref.notifySound(...) at :213.
    ('AppearanceSettingsFragment.lambda$new$1', 'SettingsRepositoryImpl.notifySound(String)'),
    # PercentEncoder.unhex (UNREACHABLE branch_never_taken, inherited from decode) -> pow(16, i) at :111.
    ('PercentEncoder.unhex', 'PercentEncoder.pow'),
    # TorrentContentFileItem.toString (UNREACHABLE no_trigger_in_app) -> super.toString() at :105.
    ('TorrentContentFileItem.toString', 'FileItem.toString'),
    # TorrentInputStream.read() (UNREACHABLE, parts/b041.py) -> toUnsignedByte at :234/:248 (ruling D2).
    # The hand edge is dropped by _K6_HAND_DROPS; this removes the automatic copy of the same call.
    ('TorrentInputStream.read()', 'TorrentInputStream.toUnsignedByte'),
})
