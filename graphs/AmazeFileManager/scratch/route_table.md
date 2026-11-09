# AmazeFileManager — route table (B6 final draw, seed 20261025)

Sample: `python3 -I tools/verify_sample.py AmazeFileManager 30 20261025`
after the last graph fix (rebuild 6, 2026-11-01 ~19:39 UTC).
30 of 2512 reachable methods, 229 distinct edges on their routes.
Prints: `scratch/route_print/` (30 files, one per route below).
Every route below was re-read from its regenerated print after the last fix;
all 30 reach their targets (verified programmatically: last step destination
equals the method for all 30).

Verdict key: correct = no fix needed during B6 judging; fixed = at least one
citation, edge, or re-route fix applied during B6 and re-verified in the
final print; wrong/unclear = a route that could not be repaired (none here).
A route fixed during B6 counts as "fixed" even though its final print is clean.

| Method | Steps | Verdict | Notes |
|---|---|---|---|
| ApkImageDataFetcher.cancel | 14 | correct | Drawer/Glide factory chain; framework lifecycle steps INFERRED standard |
| CloudIconDataFetcher.cancel | 14 | fixed | Citations only (Drawer, factory build route); spurious factory `<init>` edge deleted in batch v2. Caveat (route_01 follow-up): steps 10-14 need a String -> Bitmap cloud-model load (CloudIconModelLoader implements ModelLoader<String, Bitmap>, handles only cloud/smb/ssh prefixes); the Apps preload is String -> Drawable, so live replay proves the chain only to factory construction |
| CompressedExplorerFragment.onDestroyView | 10 | fixed | Citations only; route requires a zip/rar VIEW intent from another app (ENV other_app, no env field on the edge — see notes) |
| FileUtils.lambda$scanFile$1 | 8 | fixed | Citations only (doInBackground/onPostExecute/scanFile lines) |
| FtpTileService.updateTileState | 11 | fixed | Citations only (manifest, lambda, EventBus post site, updateTileState call) |
| GenericCopyUtil.doCopy | 10 | fixed | Citations only (CopyService ENTRY, execute, copyFiles) |
| GlideRequests.load(Integer) | 6 | fixed | Citations only (goBack/changePath) |
| HybridFile$11.<init> | 7 | fixed | Citations only: CryptUtil encrypt -> getOutputStream :246 -> :247 (real call line) |
| ImmutableEntry.getValue | 5 | fixed | Citations only: manifest :115-125 -> :129-144; getValue site :67-69 (constructor) -> :91,95 (keyMapEntry.getValue()); SearchTextTask edge 'find' clause -> true :449 afterTextChanged site |
| Indicator$PendingRevealAnimator$1.onAnimationEnd | 12 | fixed | Citations only (goToMain, listener registration, animator call) |
| ItemPopupMenu$2.onButtonPressed(Intent,String) | 12 | fixed | Citations only: dialog -> lambda$16 :760-772 -> :752-764 (the .onPositive registration + body) |
| MainFragment.onDetach | 13 | fixed | Citations only + summary edge given real evidence (TabFragment addTab :113-141 + :351) |
| PasteHelper.<init>(Parcel) | 6 | fixed | Citations only (MainActivity$1 creation, createFromParcel -> `<init>(Parcel)`) |
| PasteHelper.writeToParcel | 2 | correct | No fix needed |
| PasteHelper$1.createFromParcel | 5 | fixed | Citations only (MainActivity$1 creation) |
| PemToKeyPairTask.toastOnParseError | 13 | fixed | Citations only (class decl, dialog decl, picker, task execute, publishProgress, lambdas) + route_08 follow-up prefix correction: the B6 options-menu -> CloudSheetFragment prefix was false (the :1953 site is in FabActionListener.onActionSelected); the finder now prints the shorter true Drawer entry (onResume -> refreshDrawer -> saved-server item -> showSftpDialog -> SftpConnectDialog); steps after onCreateDialog unchanged |
| ProcessViewerFragment$CustomServiceConnection$1.<init> | 7 | correct | bindService x5 (:159-171) + anonymous ProgressListener at :416 |
| ProcessViewerFragment$CustomServiceConnection$1.lambda$onUpdate$0 | 8 | fixed | Citations only: onUpdate -> lambda :421 -> :423 (runOnUiThread lambda; the :422 cite was a closing brace) |
| ReadFileTask$ReturnedValues.<init>(int) | 5 | fixed | WRONG route re-routed: the DatabaseViewerActivity -> BasicActivity -> TextEditorActivity.onCreate prefix was invalid (both activities extend ThemedActivity, not BasicActivity; printed TextEditorActivity.java:87, DatabaseViewerActivity.java:64). Four false BasicActivity edges deleted; new route S_ENTRY -> TextEditorActivity.<init> -> onCreate -> load -> ReadFileTask.doInBackground -> ReturnedValues (ENV other_app: another app opens a text file) |
| ShareAdapter$ViewHolder.lambda$render$0 | 12 | fixed | Citations only + menu-click share edge given real evidence (AppsAdapter :170,:181-185) |
| SmbSearchDialog$1.lambda$computerFound$0 | 15 | fixed | Citations only + SubnetScanner start/run/computerFound evidence + route_08 follow-up prefix correction: the B6 options-menu -> CloudSheetFragment prefix was false (the :1953 site is in FabActionListener.onActionSelected); the route now prints the true FAB prefix (onCreate -> initialiseFab -> FabActionListener -> onActionSelected, menu_new_cloud case :1952-1956 -> CloudSheetFragment); steps after setupDialog unchanged |
| SshAuthenticationTask$1.getPublic | 12 | fixed | Citations only + CopyService mkdir summary evidence |
| SshConnectionPool$AsyncRemoveConnection.onPostExecute | 13 | fixed | WRONG route re-routed (route_08 follow-up): the B6 print's options-menu prefix was false (the :1953 site is in FabActionListener.onActionSelected, not onOptionsItemSelected) and its step 8 linked the focus listener (:132, which only selectAlls on focus) to removeConnection. True route, re-verified from printed source + bytecode: Drawer saved-ssh item -> showSftpDialog -> SftpConnectDialog onCreateDialog -> onPositive lambda$onCreateDialog$9 (:157-160) -> removeConnection (:176, STATE gate: saved SSH host key exists, :175 !isEmpty(sshHostKey)) -> AsyncRemoveConnection -> onPostExecute (:301). False focus -> removeConnection edge deleted; $0/$9 registration evidence corrected; the same repair block's $0-action duplicates and the inverted $null$6/7/8 edges deleted (all pairs already covered by true edges); FAB menu_new_cloud entry (:1952-1956) added as the alternate true entry to the dialog. Label stands (REACHABLE via onPositive). Drawer prefix needs a saved ssh:/ server item in the drawer. Re-check 2026-11-08 (W9 state 7): step 12 (now E34ff4c36) carries env network instead of the saved-key STATE (the host key is stored only after a connection, SftpConnectDialog.java:168-180); the class is env |
| StreamNotFoundException.<init>(Throwable) | 7 | fixed | Citations only: manifest :115-125 -> :129-144; onOptionsItemSelected :355 (blank) -> :357 (decl) |
| StreamSource.getCurrentPosition | 17 | fixed | Citations only + launchCloud/handleResponse evidence |
| StreamSource.read(byte[],int,int) | 14 | correct | SMB StreamServer sendResponse :672 reads the SmbStreamer StreamSource (:75-79 override); the bogus SMB -> CloudStreamSource edge was deleted in round-2 |
| TextEditorActivity$2.onAnimationEnd | 6 | fixed | Citations only: manifest :115-125 -> :129-144; onOptionsItemSelected :355 -> :357 |
| TextEditorActivity$3.onAnimationEnd | 6 | fixed | Citations only: manifest :115-125 -> :129-144; onOptionsItemSelected :355 -> :357 |
| ThemedImageView.getActivity | 10 | fixed | Review 6 fix 3 re-check: step 2 is now the Settings row tap (FRAMEWORK edge with the user action, PrefFrag.java:88-90) in place of the invented CALL E4d630b84; same route, still correct. Earlier: Citations only (PrefFrag listener) + route_24 follow-up: the onPreferenceClick -> selectItem citation :221 was the ADVANCEDSEARCH case; the route goes through the FRAGMENT_FOLDERS case :211-213 (FOLDERS_PREFERENCE -> FoldersPref, sidebar_folders_title) |
| UtilsHandler.getSshAuthPrivateKeyColumn | 7 | correct | Drawer refresh -> addNewItem lambda -> onNavigationItemActionClick :494 -> showSftpDialog :626 -> getSshAuthPrivateKeyName :1656 -> getSshAuthPrivateKeyColumn :427; lambda$addNewItem$5 identity follows the graph's bytecode-derived numbering (not re-derived) |

## Error rate

correct 5, fixed 25, wrong 0, unclear 0.
Error rate = (fixed + wrong) / (correct + fixed + wrong) = 25 / 30 = 0.833.

## Post-fix verification note

After the last fix (round-4, citations only) the graph was rebuilt
(methods 2981, REACHABLE 2512, UNREACHABLE 469, errors 0, warnings 0;
check 2: 0, check 3: 0, check 4: 0, checks 5-7: 0, check 8: 3 of 469 —
the 3 B4-explained pairs), the sample was redrawn (same 30 methods,
226 distinct edges — stable across the redraw), all 30 routes were
reprinted, and every route's final print was confirmed to reach its
target with the fixed citations present.

Route_08 follow-up (2026-11-01, after the B6 push): the graph was rebuilt
again (methods 2981, REACHABLE 2512, UNREACHABLE 469, errors 0, warnings 0;
check 2: 0, check 3: 0, check 4: 0, checks 5-7: 0, check 8: 3 of 469 — the
same 3 B4-explained pairs; edges 7758 -> 7747), the same 30 B6 methods were
reprinted (229 distinct edges; 5 prints changed, 25 byte-identical), and
all 30 routes were confirmed to reach their targets. Verdicts unchanged:
correct 5, fixed 25, wrong 0, unclear 0; error rate 25/30 = 0.833.
Verdict note: route_08 stays "fixed" under this table's verdict key
("wrong = a route that could not be repaired"; route_08 WAS repaired and
re-verified), following the ReadFileTask precedent ("fixed | WRONG route
re-routed"); the brief's alternative tally (fixed 24, wrong 1, same rate
0.833) was considered and not adopted, because it would label a repaired,
cleanly re-verified route as unrepaired and would treat route_08
differently from the two prefix-sharing routes repaired the same way.
Redraw note: a fresh draw at seed 20261025 after this fix gives 29/30
overlap (MediaStoreHack.mkfile replaces UtilsHandler.getSshAuthPrivateKeyColumn,
233 distinct edges); the B6 sample is RETAINED as the judged sample for
this follow-up — adopting the redraw would require judging the new route
and re-tallying, which is a coordinator decision, not done silently here.
The redraw output is saved at scratch/sample_30_redraw_after_route08fix.txt
(diagnostic only, NOT the adopted sample).

## Notes and caveats

- The CompressedExplorerFragment.onDestroyView route requires launching
  with a zip/rar VIEW intent from another app (ENV other_app). The edge
  carries no env field; the requirement is recorded here, not encoded.
- The ReadFileTask route family carries ENV other_app (ACTION_VIEW
  text/* from another app, manifest :129-144).
- The PasteHelper route family requires a pending copy/cut (needs_state
  "copy or cut pending") for the MainActivity paste case; recorded here,
  not encoded on the edge.
- Lambda numbering (e.g. lambda$addNewItem$5, lambda$onUpdate$0) follows
  the graph's bytecode-derived mapping and was not re-derived; where a
  lambda's body was printed it matched the edge (e.g. onUpdate's
  runOnUiThread lambda at ProcessViewerFragment.java:423).
- The route_08 onPositive -> removeConnection link carries STATE "saved SSH
  host key exists" (data kind) with guard !isEmpty(sshHostKey)
  (SftpConnectDialog.java:175); the Drawer entry to that route needs a
  saved ssh:/ server item in the drawer.
- The CloudIconDataFetcher.cancel chain proves to factory construction on
  a live Apps-list replay (String -> Drawable preload); steps 10-14 need a
  String -> Bitmap cloud-model load.
- Routes dropped from earlier draws by redraws (FtpNotification.buildNotification,
  PrepareCopyTask.lambda$showDialog$1, StreamSource.open, ZipService.onDestroy,
  ApkImageDataFetcher.cleanup, GeneralDialogCreation$2.onTextChanged,
  HybridFile$10.<init>, ZipService.setProgressListener, CloudStreamSource.read,
  EncryptService.getProgressHandler, FtpTileService.lambda$onClick$0,
  FtpReceiver.<clinit>, FtpTileService.onStartListening,
  FtpTileService.onStopListening, ObtainableServiceBinder.getService) were
  judged and fixed in their own draws; their fixes are in fix_log.md but
  they are NOT in this final table, per the brief (final table = final draw).

## W8 re-verification (Kiro, 2026-11-06, self-checked only, second: pending reviewer)

After the re-audit, 20 of the 30 sampled routes changed. Each new step was read in the source (tools_dev/route_diff.py
lists them). The verdicts and notes are the `p8(...)` rows in graphs/AmazeFileManager/make_verification.py: 20 correct,
with "kind caveat" where a real user action is written as a LIFECYCLE/FRAMEWORK/CALL edge. Reading them found missing
gates (now in graph_def.py and scratch/reaudit/w7_judged.csv) and 154 wrong INFERRED "framework calls ... after
construction" edges, now dropped (graph_def.py, top; tools_dev/inferred_family.py lists them).
