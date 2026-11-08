# Batch 58 — Phase 2 spot-check (UNVERIFIED proposal check only; nothing merged, nothing pushed)

- Source file checked: `~/workspace/overnight/stream-A/work/batch58-merge-ready.md`
- Evidence base: already-fetched files only (`~/workspace/b565758-openclose-src/`, `~/workspace/b565758-openclose2-src/`,
  `~/workspace/b5354-openclose-src/`, `~/workspace/b5354-55-src/`, `~/workspace/ruleF-src/`,
  `~/workspace/overnight/stream-A/corpus/`). No connector fetch was needed; no 429; no missing file.
- Rows checked (13): sample 1, 6, 11, 16, 21, 26, 31, 36 + round-2 flip 8 + must-include extras 32, 34, 35, 37.
- Batch Counts verified mechanically from the label column AND against the Counts section: 36 REACHABLE / 0 UNREACHABLE / 4 OPEN.
- Build/sampler/C1: not run (not this task).

## Per-row verdicts

| Row | Label in file | Verdict | Evidence (printed source) |
|-----|---------------|---------|---------------------------|
| 1 `Utils.isMetered(Context)Z` | REACHABLE SOURCE | PASS | Utils.java:196-201 (def verified); TorrentEngine checkPauseTorrents :1035 `stop = Utils.isMetered(appContext)` (verified, unmeteredOnly branch). |
| 6 `Utils.isValidTrackerUrl(String)Z` | REACHABLE SOURCE | PASS | Utils.java:261-269 (def verified); CreateTorrentViewModel.java:317 and DetailTorrentFragment.java:662 (both verified). |
| 8 `Utils.makeSha1Hash(String)String` | REACHABLE SOURCE | PASS | Utils.java:567-583 (def verified); TorrentStream ctor :44 `this.id = Utils.makeSha1Hash(torrentId + selectedFileIndex)` (verified, ctor :40-44); full chain verified: TE handleOnSessionStarted :1046 → startStreamingServer :1058-1063 → new TorrentStreamServer :1069 → TorrentStreamServer handleTorrent :124 → engine.getStream :142 → TE getStream :747 → TorrentDownloadImpl getStream :1607 → new TorrentStream :1621. The round-2 flip (caller outside the 70-file round-1 corpus) is justified. |
| 11 `Utils.requestExactAlarmPermission(Context)V` | REACHABLE SOURCE | PASS | Utils.java:671-675 (def verified); SchedulingSettingsFragment :137 `Utils.requestExactAlarmPermission(getContext())` inside subscribeAlertDialog (:129), subscribed from onStart (:122) — all verified. The row correctly notes the method's own S-gate affects batch-57 row 5, not this method's callability. |
| 16 `Utils.startServiceBackground(Context,Intent)V` | REACHABLE SOURCE | PASS | Utils.java:426-434 (def verified); TorrentEngine forceStop body :285 `Utils.startServiceBackground(appContext, i)` (verified); handleAutoStop :143-146 → forceStop (verified). |
| 21 `Utils$1.onResponseHandle(HttpURLConnection,int,String)V` | REACHABLE INFERRED | PASS | onResponseHandle def at Utils.java:484, body :485-499 (HTTP_OK → read body, else FetchLinkException — verified); same registration/run as row 18; listener dispatch unprinted, so INFERRED is correct. (Nit, not a failure: the cited range :485-499 covers the body; the def line itself is :484.) |
| 26 `Utils$2.getAcceptedIssuers()[X509Certificate` | REACHABLE INFERRED | FAIL (citation; label stands) | The method exists and the label is supported, but the cited lines are wrong: the row cites ":598-600", which in the fresh Utils print is `checkClientTrusted` (:598 def, :599 delegate, :600 close), NOT getAcceptedIssuers. The real location is Utils.java:594 (def) / :595 (`return origTrustManager.getAcceptedIssuers()`), verified by sed :592-602. Proposed correction: change the citation to :594-595; label REACHABLE INFERRED unchanged (TLS dispatch unprinted, as row 24's note). |
| 31 `ActivityAddTorrentBindingImpl.executeBindings()V` | REACHABLE INFERRED | PASS | Row 33 invalidateAll is REACHABLE INFERRED (generated Impl ctor calls invalidateAll, D4e pattern as in batch 59); framework rebind then runs executeBindings. Generated file unprinted, so INFERRED is correct. |
| 32 `ActivityAddTorrentBindingImpl.hasPendingBindings()Z` | OPEN | PASS | Correctly left OPEN: zero `hasPendingBindings` hits in the saved 252-file greps (`grep-full-tree-252.txt`, `grep-full-tree-252b.txt` — no hits found on re-check), and generated/framework dispatch is unprinted. Zero hits alone were correctly NOT treated as absence evidence. Matches the Phase 1c note (D4f: every OPEN hasPendingBindings row stays OPEN). |
| 34 `ActivityAddTorrentBindingImpl.onFieldChange(int,Object,int)Z` | OPEN | PASS | Correctly left OPEN and NOT flipped: `activity_add_torrent.xml` (saved in b565758-openclose2-src) declares NO `<data>` block (grep count 0 for `<data>`/`@{`), and AddTorrentActivity uses binding views only (toolbar/viewpager/tabLayout/progress :279-331, no setViewModel/setVariable call found). The task's D4c-scope question is answered: D4c's flip list names batch-60 appbar rows, not batch-58 rows, and the file's Phase 1c note records exactly that — rows 34/35 are deliberately OPEN, and this spot-check does NOT flip them and does NOT extend D4c. |
| 35 `ActivityAddTorrentBindingImpl.setVariable(int,Object)Z` | OPEN | PASS | Same as row 34: no printed setVariable call, zero `setVariable` hits in the 252-file corpus grep (binding-callbacks grep: setVariable 0), layout declares no variable. OPEN is correctly recorded; not flipped, D4c not extended. |
| 36 `ActivityFilemanagerDialogBinding.<init>(...)` | REACHABLE INFERRED | PASS | FileManagerDialog.java:120 onCreate, :142 `DataBindingUtil.setContentView(this, R.layout.activity_filemanager_dialog)` (both verified). Base binding ctor called by the generated Impl ctor (generated, INFERRED). The row's strict-entry caveat (dialog starter not printed) is preserved. |
| 37 `ActivityFilemanagerDialogBinding.getViewModel()FileManagerViewModel` | OPEN | PASS | Correctly left OPEN: FileManagerDialog.java:143 calls the SETTER (`binding.setViewModel(viewModel)`), not this getter; layout `activity_filemanager_dialog.xml` DOES declare the viewModel variable (:7-8) with `@{viewModel.config...}` expressions (:74, :94 — both verified), so the variable is bound but no printed getter call exists, and generated executeBindings reads the field directly (D4a v-field, per the file). Zero `getViewModel` hits in the 252-file greps on re-check. OPEN under the undecided (v) read-path convention; left as-is, no convention decided here. |

## Totals

- PASS: 12, FAIL: 1 (of 13 checked). The single FAIL is citation-only; no label is wrong in this batch.
- Proposed corrections:
  1. Row 26: citation `:598-600` → `:594-595` (getAcceptedIssuers def/delegate). Label REACHABLE INFERRED unchanged.
- Must-include confirmation: batch 58 rows 34 and 35 are correctly recorded OPEN; they were not flipped and D4c was not extended to them.
