# LibreTorrent batch 82 — Phase 2 spot-check — UNVERIFIED (spot-check only, not a merge verdict)

- Batch: 82. Work file checked: `~/workspace/overnight/stream-A/work/batch82-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (13): sample rows 1, 6, 11, 16, 21, 26, 31, 36, plus must-include extras 10, 12, 13, 14, 17 (row 16 is in both sets, counted once). Phase 1c label flips in this file: 0 (stated in its 2026-11-01 Phase 1c revision note).
- Method: re-derived from already-fetched source on disk (`~/workspace/b81-82-src/`, `~/workspace/ruleF-src/`, `~/workspace/b818284-openclose2-src/grep_DownloadableFileItem.txt`); no GitHub connector fetch was needed, no 429 hit, no file missing.
- No edit was made to the merge-ready file. No push. Build/sampler/C1: not run (not this task).
- D5c vs together-rule tension (parcel group): NOT decided here, per task. Rows 10, 12, 14, 16, 17 are verified as OPEN as filed; no flip is ordered or proposed.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (file:line, local copy) |
|---|---|---|---|---|
| 1 | AddTorrentViewModel$DecodeState.<init>(Status) | REACHABLE / SOURCE | PASS | Def AddTorrentViewModel.java:123-125 (delegating ctor); caller :142 `new DecodeState(Status.UNKNOWN)` on the printed route, plus :229/:234/:251/:318/:322. |
| 6 | AddTorrentViewModel$TorrentDecodeTask.onPostExecute | REACHABLE / INFERRED | PASS | Def AddTorrentViewModel.java:301-325; reached via AsyncTask dispatch after executeOnExecutor :199, unprinted → INFERRED correct. |
| 10 | DownloadableFileItem.<init>(Parcel) | OPEN / — | PASS | Def DownloadableFileItem.java:40-45, called only by CREATOR.createFromParcel :67. Tree grep shows no parcel/unparcel site naming DownloadableFileItem; the only putParcelable/getParcelable sites are LayoutManager state (AddTorrentFilesFragment.java:159/:170), Uri (AddTorrentActivity.java:359), TagInfo (AddTorrentInfoFragment.java:142). OPEN as filed. |
| 11 | DownloadableFileItem.<init>(BencodeFileTree) | REACHABLE / INFERRED | PASS | Method reference AddTorrentFilesFragment.java:117 `.map(DownloadableFileItem::new)` inside an Rx chain; def DownloadableFileItem.java:33-38. Rx dispatch → INFERRED correct. |
| 12 | DownloadableFileItem.describeContents | OPEN / — | PASS | Def DownloadableFileItem.java:48-51; runs only when an instance is parcelled, and no parcel site is printed (see row 10). OPEN as filed. |
| 13 | DownloadableFileItem.toString | OPEN / — | PASS | Def DownloadableFileItem.java:79-85; its body :82 `super.toString()` is a conditional hit FOR FileItem.toString (batch 73 row 32), not an inbound caller for this row. No external caller in the tree grep (fragment/adapter use item.name/isFile only). OPEN as filed; hosts 73/32, which also stays OPEN — no dependency flip. |
| 14 | DownloadableFileItem.writeToParcel | OPEN / — | PASS | Def DownloadableFileItem.java:54-59; same no-parcel-site finding as row 10. OPEN as filed. |
| 16 | DownloadableFileItem$1.createFromParcel | OPEN / — | PASS | Def DownloadableFileItem.java:65-68; framework Parcelable dispatch, no printed unparcel site (see row 10). OPEN as filed. |
| 17 | DownloadableFileItem$1.newArray | OPEN / — | PASS | Def DownloadableFileItem.java:71-74; no array-extra site naming this class in the tree grep. OPEN as filed. Under D5c an array site would be needed specifically for this row; that tension with the file's together-rule is recorded, NOT resolved here. |
| 21 | DownloadableFilesAdapter.onCreateViewHolder | REACHABLE / SOURCE | PASS | Standard RecyclerView.Adapter callback after printed setAdapter (AddTorrentFilesFragment.java:140); def DownloadableFilesAdapter.java:57-65 (inflates binding, returns new ViewHolder). |
| 26 | DownloadableFilesAdapter$ViewHolder.bind | REACHABLE / SOURCE | PASS | Called by onBindViewHolder DownloadableFilesAdapter.java:71; def :102-145. |
| 31 | CreateTorrentActivity.onBackPressed | REACHABLE / SOURCE | PASS | Standard Activity callback; def CreateTorrentActivity.java:136-139 (createTorrentDialog.onBackPressed()). |
| 36 | CreateTorrentActivity.subscribeAlertDialog | REACHABLE / SOURCE | PASS | Called from onStart CreateTorrentActivity.java:99; def :109-127. (Its Rx lambda is row 30, INFERRED, not checked here.) |

## Totals

- PASS: 13 / 13. FAIL: 0 / 13.

## Proposed corrections

- None. No row label or confirmed_by needs changing on the evidence checked. The D5c/together-rule tension is left for the merger, not decided here.
