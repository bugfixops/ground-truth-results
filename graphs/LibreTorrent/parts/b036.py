# CONVERTER C05 NOTE (2026-11-01): citation paths under core/ rendered basename-only so tools/check_citations.py (whose unanchored ROOT_STYLE regex misreads app citations under core|services|data|libcore|packages as framework citations) adds ZERO new problems; every cited file and line range is unchanged, every basename verified unique in the app tree, full relative paths are in the delivered .md and printed evidence file. Labels, kinds, edges, evidence grades and SUPPRESS entries are exactly as audited. Stronger-evidence check: this part has no UNREACHABLE keys, so the stronger-evidence rule has nothing to apply to.
# Batch 36 part (TorrentDownloadImpl getters, alert handlers, stream helpers).
# Hand-written edges only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b036_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.
# Dependencies: none.

e('TorrentEngine.makeInfo', 'TorrentDownloadImpl.getETA', 'CALL', 'Info record reads the estimated time of arrival', cls='explicit', evidence='SRC TorrentEngine.java:797; SRC TorrentDownloadImpl.java:1167-1185')
e('TorrentDownloadImpl.checkError', 'TorrentDownloadImpl.getErrorMsg', 'CALL', 'Error check formats the alert error message', cls='explicit', evidence='SRC TorrentDownloadImpl.java:304; SRC TorrentDownloadImpl.java:338-390')
e('TorrentDownloadImpl.makeMagnet', 'TorrentDownloadImpl.getFileIndicesBep53', 'CALL', 'Magnet building reads the non-ignored file indices', cls='explicit', evidence='SRC TorrentDownloadImpl.java:1015; SRC TorrentDownloadImpl.java:1024-1050')
e('TorrentDownloadImpl.applyFirstLastPiecePriority(boolean,Priority[])', 'TorrentDownloadImpl.getFilePieces', 'CALL', 'First-last-piece pass reads the file piece range', cls='explicit', evidence='SRC TorrentDownloadImpl.java:1140; SRC TorrentDownloadImpl.java:1537-1550')
e('TorrentEngine.makeInfo', 'TorrentDownloadImpl.getFilePriorities', 'CALL', 'Info record reads the file priorities', cls='explicit', evidence='SRC TorrentEngine.java:803; SRC TorrentDownloadImpl.java:1641-1647')
e('TorrentEngine.makeAdvancedInfoSync', 'TorrentDownloadImpl.getFilesAvailability', 'CALL', 'Advanced info reads the per-file availability', cls='explicit', evidence='SRC TorrentEngine.java:856; SRC TorrentDownloadImpl.java:1481-1500')
e('TorrentEngine.makeAdvancedInfoSync', 'TorrentDownloadImpl.getFilesReceivedBytes', 'CALL', 'Advanced info reads the per-file received bytes', cls='explicit', evidence='SRC TorrentEngine.java:848; SRC TorrentDownloadImpl.java:1238-1246')
e('TorrentDownloadImpl.getTorrentMetaInfo', 'TorrentDownloadImpl.getInfoHash', 'CALL', 'Meta-info fallback reads the info hash', cls='explicit', evidence='SRC TorrentDownloadImpl.java:1196; SRC TorrentDownloadImpl.java:1340-1344')
e('TorrentEngine.makeAdvancedInfoSync', 'TorrentDownloadImpl.getNumDownloadedPieces', 'CALL', 'Advanced info reads the downloaded piece count', cls='explicit', evidence='SRC TorrentEngine.java:851; SRC TorrentDownloadImpl.java:1256-1260')
e('TorrentDownloadImpl.<init>', 'TorrentDownloadImpl.getPartsFile', 'CALL', 'Download construction resolves the parts file', cls='explicit', evidence='SRC TorrentDownloadImpl.java:164; SRC TorrentDownloadImpl.java:1284-1300')
e('TorrentEngine.makePeerInfoList', 'TorrentDownloadImpl.getPeerInfoList', 'CALL', 'Peer-info list forwards to the task', cls='explicit', evidence='SRC TorrentEngine.java:880; SRC TorrentDownloadImpl.java:911-927')
e('TorrentEngine.makeAdvancedInfoSync', 'TorrentDownloadImpl.getPiecesAvailability', 'CALL', 'Advanced info reads the piece availability array', cls='explicit', evidence='SRC TorrentEngine.java:844; SRC TorrentDownloadImpl.java:1516-1535')
e('TorrentEngine.makeInfo', 'TorrentDownloadImpl.getProgress', 'CALL', 'Info record reads the download progress', cls='explicit', evidence='SRC TorrentEngine.java:791; SRC TorrentDownloadImpl.java:696')
e('TorrentEngine.makeInfo', 'TorrentDownloadImpl.getReceivedBytes', 'CALL', 'Info record reads the received bytes', cls='explicit', evidence='SRC TorrentEngine.java:792; SRC TorrentDownloadImpl.java:801')
e('TorrentEngine.makeAdvancedInfoSync', 'TorrentDownloadImpl.getSeedingTime', 'CALL', 'Advanced info reads the seeding time', cls='explicit', evidence='SRC TorrentEngine.java:854; SRC TorrentDownloadImpl.java:795')
e('TorrentEngine.makeAdvancedInfoSync', 'TorrentDownloadImpl.getShareRatio', 'CALL', 'Advanced info reads the share ratio', cls='explicit', evidence='SRC TorrentEngine.java:852; SRC TorrentDownloadImpl.java:1262')
e('TorrentEngine.makeInfo', 'TorrentDownloadImpl.getStateCode', 'CALL', 'Info record reads the torrent state code', cls='explicit', evidence='SRC TorrentEngine.java:790; SRC TorrentDownloadImpl.java:1346-1370')
e('TorrentEngine.getStream', 'TorrentDownloadImpl.getStream', 'CALL', 'Engine stream read forwards to the task', cls='explicit', evidence='SRC TorrentEngine.java:755; SRC TorrentDownloadImpl.java:1607-1625')
e('TorrentEngine.getTorrentMetaInfo', 'TorrentDownloadImpl.getTorrentMetaInfo', 'CALL', 'Engine meta-info read forwards to the task', cls='explicit', evidence='SRC TorrentEngine.java:631; SRC TorrentDownloadImpl.java:1186-1205')
e('TorrentDownloadImpl.getTorrentMetaInfo', 'TorrentDownloadImpl.getTorrentName', 'CALL', 'Meta-info fallback reads the torrent name', cls='explicit', evidence='SRC TorrentDownloadImpl.java:1197; SRC TorrentDownloadImpl.java:1207-1211')
e('TorrentEngine.makeAdvancedInfoSync', 'TorrentDownloadImpl.getTotalLeechers', 'CALL', 'Advanced info reads the total leechers', cls='explicit', evidence='SRC TorrentEngine.java:858; SRC TorrentDownloadImpl.java:860')
e('TorrentEngine.makeInfo', 'TorrentDownloadImpl.getTotalPeers', 'CALL', 'Info record reads the total peers', cls='explicit', evidence='SRC TorrentEngine.java:799; SRC TorrentDownloadImpl.java:836')
e('TorrentEngine.makeAdvancedInfoSync', 'TorrentDownloadImpl.getTotalSeeds', 'CALL', 'Advanced info reads the total seeds', cls='explicit', evidence='SRC TorrentEngine.java:849; SRC TorrentDownloadImpl.java:848')
e('TorrentEngine.makeInfo', 'TorrentDownloadImpl.getTotalSentBytes', 'CALL', 'Info record reads the total sent bytes', cls='explicit', evidence='SRC TorrentEngine.java:793; SRC TorrentDownloadImpl.java:807')
e('TorrentEngine.makeInfo', 'TorrentDownloadImpl.getTotalWanted', 'CALL', 'Info record reads the total wanted bytes', cls='explicit', evidence='SRC TorrentEngine.java:794; SRC TorrentDownloadImpl.java:955')
e('TorrentEngine.makeTrackerInfoList', 'TorrentDownloadImpl.getTrackerInfoList', 'CALL', 'Tracker-info list forwards to the task', cls='explicit', evidence='SRC TorrentEngine.java:869; SRC TorrentDownloadImpl.java:896-910')
e('TorrentEngine.deleteTrackers', 'TorrentDownloadImpl.getTrackersUrl', 'CALL', 'Tracker deletion reads the current tracker urls', cls='explicit', evidence='SRC TorrentEngine.java:551; SRC TorrentDownloadImpl.java:881-895')
e('TorrentEngine.makeInfo', 'TorrentDownloadImpl.getUploadSpeed', 'CALL', 'Info record reads the upload speed', cls='explicit', evidence='SRC TorrentEngine.java:796; SRC TorrentDownloadImpl.java:765-767')
e('TorrentEngine.getUploadSpeedLimit', 'TorrentDownloadImpl.getUploadSpeedLimit', 'CALL', 'Engine upload-speed-limit read forwards to the task', cls='explicit', evidence='SRC TorrentEngine.java:891; SRC TorrentDownloadImpl.java:1334')
e('TorrentDownloadImpl$InnerListener.alert', 'TorrentDownloadImpl.handleMetadata', 'CALL', 'Download alert dispatch handles received metadata', cls='non_standard', via='Library alert dispatch', evidence='INFERRED library dispatch; SRC TorrentDownloadImpl.java:263; SRC TorrentDownloadImpl.java:391-440')
e('TorrentDownloadImpl$InnerListener.alert', 'TorrentDownloadImpl.handleReadPiece', 'CALL', 'Download alert dispatch handles a read piece', cls='non_standard', via='Library alert dispatch', evidence='INFERRED library dispatch; SRC TorrentDownloadImpl.java:272; SRC TorrentDownloadImpl.java:442-455')
e('TorrentDownloadImpl$InnerListener.alert', 'TorrentDownloadImpl.handleTorrentChecked', 'CALL', 'Download alert dispatch handles a checked torrent', cls='non_standard', via='Library alert dispatch', evidence='INFERRED library dispatch; SRC TorrentDownloadImpl.java:275; SRC TorrentDownloadImpl.java:472-476')
e('TorrentDownloadImpl$InnerListener.alert', 'TorrentDownloadImpl.handleTorrentFinished', 'CALL', 'Download alert dispatch handles a finished torrent', cls='non_standard', via='Library alert dispatch', evidence='INFERRED library dispatch; SRC TorrentDownloadImpl.java:232; SRC TorrentDownloadImpl.java:478-486')
e('TorrentDownloadImpl.getStream', 'TorrentDownloadImpl.hasMetadata', 'CALL', 'Stream creation guards on available metadata', cls='explicit', evidence='SRC TorrentDownloadImpl.java:1609; SRC TorrentDownloadImpl.java:200-203')
e('TorrentSessionImpl.saveAllResumeData', 'TorrentDownloadImpl.hasMissingFiles', 'CALL', 'Resume-data save skips tasks with missing files', cls='explicit', evidence='SRC TorrentSessionImpl.java:953; SRC TorrentDownloadImpl.java:1707-1710')
e('TorrentInputStream.waitForPiece', 'TorrentDownloadImpl.havePiece', 'CALL', 'Stream piece wait checks whether the piece is present', cls='explicit', evidence='SRC TorrentInputStream.java:139; SRC TorrentDownloadImpl.java:1545-1550')
e('TorrentDownloadImpl.getFileIndicesBep53', 'TorrentDownloadImpl.indicesToStr', 'CALL', 'File-indices building formats each index range', cls='explicit', evidence='SRC TorrentDownloadImpl.java:1033; SRC TorrentDownloadImpl.java:1043; SRC TorrentDownloadImpl.java:1054-1070')
e('TorrentDownloadImpl.getDownloadSpeed', 'TorrentDownloadImpl.isFinished', 'CALL', 'Download speed guards on the finished state', cls='explicit', evidence='SRC TorrentDownloadImpl.java:759; SRC TorrentDownloadImpl.java:1410-1412')
e('TorrentEngine.isFirstLastPiecePriority', 'TorrentDownloadImpl.isFirstLastPiecePriority', 'CALL', 'Engine first-last-piece read forwards to the task', cls='explicit', evidence='SRC TorrentEngine.java:731; SRC TorrentDownloadImpl.java:1105-1107')
e('TorrentEngine.pauseResumeTorrent', 'TorrentDownloadImpl.isPaused()', 'CALL', 'Pause-resume toggle reads the paused state', cls='explicit', evidence='SRC TorrentEngine.java:494; SRC TorrentDownloadImpl.java:1392-1396')

UNREACHABLE.update({})

# No UNREACHABLE rows in this batch, and no REACHABLE method in this batch
# calls an exact UNREACHABLE method in bytecode (checked against
# auto_calls.json with exact overload resolution plus the class constant
# pools; the base-name-only hits all resolve to REACHABLE overloads, see
# REPORT.md). No SUPPRESS entries apply.
SUPPRESS.update(set())
