import pathlib

G = pathlib.Path('/Users/darshan/Desktop/yang/work/graphs/AnyMemo')
gd = G / 'graph_def.py'
txt = gd.read_text(encoding='utf-8')
lines = txt.split('\n')


def rep(s, old, new, n=1):
    c = s.count(old)
    assert c == n, (c, old[:90])
    return s.replace(old, new)


# 1. replace the old downloader block (lines 1067..1096, 1-based) with the per-host block
assert 'I. downloader' in lines[1066] and lines[1066].startswith('# ====='), lines[1066][:120]
assert lines[1095].startswith("e('AbstractDownloaderFragment$FetchDatabaseTask.onPostExecute', 'S_DLG_DOWNLOAD_FAIL'"), lines[1095][:120]
assert lines[1096].startswith('# Load more (AbstractDownloaderFragment$3'), lines[1096][:120]

block = (G / 'scratch' / 'g12_block.txt').read_text(encoding='utf-8')
block = rep(block,
    "# The row click starts the category and back Callables directly (framework ASYNC edges). RetrieveTask.doInBackground\n"
    "# is shown only on the refresh path, where it is the step that calls initialRetrieve() through task.call().\n",
    "# A row click starts its Callable directly (ASYNC edge to the Callable node). A shared RetrieveTask.doInBackground\n"
    "# would carry one CALL to the refresh Callable, so the click paths would appear to run initialRetrieve(); doInBackground@X\n"
    "# therefore appears only on the refresh path. The row listener is registered in the shared getView; the edge is drawn\n"
    "# from onCreateView@X so that each host's rows lead to that host's methods.\n")
block = rep(block,
    "'the download succeeds (fetchDatabase: AnyMemo source needs the network, Dropbox source needs Dropbox+network)'",
    "'the download succeeds: success dialog, then the path is added to the recent list'")
block = rep(block,
    "evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:316-343')",
    "evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:316-325')")
block_lines = block.rstrip('\n').split('\n')
lines = lines[:1066] + block_lines + lines[1096:]
txt = '\n'.join(lines)


# 2. remove the generated base-name downloader edges (they fan out to both hosts)
def drop_prefix(s, prefix, n):
    ls = s.split('\n')
    hits = {i for i, l in enumerate(ls) if l.startswith(prefix)}
    assert len(hits) == n, (len(hits), prefix)
    return '\n'.join(l for i, l in enumerate(ls) if i not in hits)


txt = drop_prefix(txt, "e('AbstractDownloaderFragment$DownloadListAdapter$1.onClick', 'AbstractDownloaderFragment$RetrieveTask.", 2)
txt = drop_prefix(txt, "e('AbstractDownloaderFragment$RetrieveTask.doInBackground', 'AbstractDownloaderFragment$RetrieveTask.onPostExecute'", 2)
txt = drop_prefix(txt, "e('AbstractDownloaderFragment.refreshList', 'AbstractDownloaderFragment$RetrieveTask.", 2)
txt = drop_prefix(txt, "e('AbstractDownloaderFragment.startFetchDatabaseTask', 'AbstractDownloaderFragment$FetchDatabaseTask.onPreExecute'", 1)
txt = drop_prefix(txt, "e('AbstractDownloaderFragment.onCreateView', 'AbstractDownloaderFragment$DownloadListAdapter.getView'", 1)

# 3. DropboxListActivity.refreshList calls the Dropbox host's refreshList, source line 95
txt = rep(txt,
    "e('DropboxListActivity.refreshList', 'AbstractDownloaderFragment.refreshList', 'CALL', 'fragment.refreshList()', evidence='SRC downloader/dropbox/DropboxListActivity.java:88-90')",
    "e('DropboxListActivity.refreshList', 'AbstractDownloaderFragment.refreshList@DBX', 'CALL', 'fragment.refreshList() (Dropbox list fragment)', evidence='SRC downloader/dropbox/DropboxListActivity.java:95')")

# 4. SCREENS: the confirm dialog is now one page per host
txt = rep(txt,
    "    'S_DLG_DOWNLOAD_CONFIRM': 'Confirm downloading one shared database',\n",
    "    'S_DLG_DOWNLOAD_CONFIRM_AM': 'Confirm downloading one AnyMemo database (AnyMemo source)',\n"
    "    'S_DLG_DOWNLOAD_CONFIRM_DBX': 'Confirm downloading one Dropbox database (Dropbox source)',\n")

gd.write_text(txt, encoding='utf-8')
print('edit ok; graph_def.py lines:', len(txt.split('\n')))
