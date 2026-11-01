# Spot-check — batch 54 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 54/1 DefaultFsModule.getParentDirUri — REACHABLE INFERRED — PASS. Flipped in this pass; definition DFM L127-132; dispatcher: FSFI.getParentDirUri (row 23), freshly called by CreateTorrentViewModel L357; file-URI branch INFERRED.
- 54/6 FileDescriptorWrapperImpl.open — REACHABLE SOURCE — PASS. Definition FDWI L46-51; called by FSFI.write(byte[]) L225 and FSFI.write(CharSequence) L237 (w.open("rw")), and by TE L380-381 (w.open("r") on the wrapper from fs.getFD); the FSFI.write(byte[]) chain alone anchors it via TE L980-984.
- 54/11 FileSystemFacadeImpl.createFile — REACHABLE SOURCE — PASS. Definition FSFI L199-218; called by TE.saveTorrentFile L980 (fs.createFile(destDir, name, true)).
- 54/16 FileSystemFacadeImpl.getDirPath — REACHABLE SOURCE — PASS. Definition FSFI L418-423; called by Storage fragment onCreate L99 (also L126, L153, L180, L271).
- 54/21 FileSystemFacadeImpl.getFileUri(Uri,String) — REACHABLE SOURCE — PASS. Flipped in this pass; definition FSFI L122-136; fresh TorrentDownloadImpl.java L1299 (fs.getFileUri(torrent.downloadPath, "." + ti.infoHash() + ".parts")); row correctly notes FSFI.createFile calls the *module* method directly at L205/L213, not this facade method — that was the prior pass's only printed chain; this row has its own fresh caller.
- 54/26 FileSystemFacadeImpl.isStorageReadable — REACHABLE SOURCE — PASS. Definition FSFI L185-191; called by TRI.getSessionFile L110 and TRI.getTorrentDataDir L146 via the SFH facade singleton. Trunk caveat stated in row: the callers of those repository methods were not freshly printed in this pass (see Strict-entry caveat).
- 54/31 FileSystemFacadeImpl.normalizeFileSystemPath — REACHABLE SOURCE — PASS. Flipped in this pass; definition FSFI L404-411; fresh Utils.java L646 and fresh AddTorrentViewModel.java L259.
- 54/36 FsModuleResolverImpl.resolveFsByUri — REACHABLE SOURCE — PASS. Definition FMRI L42-50; called by every FSFI dispatch method, including reachable ones: getFD L62, deleteFile L112, createFile L203, getDirAvailableBytes L272, getDirPath L420, getFilePath L432.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
