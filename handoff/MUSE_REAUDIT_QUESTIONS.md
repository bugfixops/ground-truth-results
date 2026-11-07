# MUSE_REAUDIT_QUESTIONS — re-audit of five apps (Aegis, AmazeFileManager, AnkiDroid, LibreTorrent, MMEX)

Questions are recorded here with the default used; work carries on with the default until the user or the reviewer answers. (Brief: handoff/MUSE_REAUDIT_5APPS.md, Appendix D and section 10.)

## Q1. Do LiveData observer callbacks count as library edges?
Default used: **No change** — LiveData and ViewModel observers keep their current class. The task note does not name them. (Brief W5 point 4.)

## Q2. Is MMEX's first-run tutorial a setup-only screen like Aegis's intro?
Default used: **Yes** — it goes into `SETUP_ONLY` in W2. (Brief W2, MMEX.)

## Q3. Is the Aegis setup vault encrypted, i.e. is unlocking state?
Default used: **Unlocking is typing the password, a GUI action** — never state. (Brief W2, Aegis.)

## Q4. Markor's onboarding is part of the baseline, but Markor is not in this job.
Default used: **Do not touch Markor**; count how many Markor best routes pass its intro and report it in the summary. (User confirmed 2026-11-05: only the five apps change.)

## Q5. AmazeFileManager-20 (`HybridFile$9.execute`): the brief's W1 test expects RTA to make it lose its route, and W4's acceptance expects it UNREACHABLE; the task note says it is created only inside the uncalled no-arg `HybridFile.getInputStream()`. The source and the current graph disagree with that premise in two places:
- a hand edge `HybridFile.listFiles -> HybridFile$9.<init>` ("creates SFtpClientTemplate for SFTP file listing", HybridFile.java:810) makes the class instantiated under T2's rule (creation anywhere reachable counts), so RTA keeps the cha edge `SshClientUtils$2.execute -> HybridFile$9.execute`;
- a hand FRAMEWORK edge `SshClientUtils.execute(SFtpClientTemplate) -> HybridFile$9.execute` also reaches it, and RTA never drops hand edges.
Default used: **RTA is implemented exactly as T2 specifies** (it dropped 1 cha edge in AmazeFileManager, to `HybridFile$2.execute`, which stays reachable otherwise; 0 methods lost every route). The two hand edges are re-judged from the printed source in W4; the UNREACHABLE verdict for `HybridFile$9.execute` stands or falls on that evidence, not on bending the switch. Raised 2026-11-06 (W1 merge).

## Q6. Aegis baseline: what are the two vault entries, and which security does the setup vault use?
Default used: **two default TOTP entries (SHA1, 6 digits, 30 s) in a password-protected vault.** A new entry defaults to TOTP (VaultEntry.java:253-255) with SHA1 and 6 digits (OtpInfo.java:14-15) and a 30 s period (TotpInfo.java:14, 20); the password follows Q3. So W2 clears the Google Authenticator export gate, the password-slot gate and the encrypted-vault gate, and keeps the MOTP, Yandex, HOTP, biometric-slot and plain-text-vault gates. Raised by Kiro 2026-11-06 04:18 UTC (Aegis W2).

**Q5 answered by Kiro (2026-11-06 04:39 UTC, W4):** javap shows listFiles creates HybridFile$8 and only the uncalled no-arg getInputStream() creates HybridFile$9. The two hand edges in Q5 named the wrong anonymous class (the hand block was one number off from $4 on); after the fix, HybridFile$9.execute is UNREACHABLE with evidence (graphs/AmazeFileManager/scratch/reaudit/w4_hybridfile_javap.txt).

## Q7. Aegis settings sub-pages: PreferencesActivity opens each settings page with FragmentFactory.instantiate(getClassLoader(), pref.getFragment()) for the tapped header (PreferencesActivity.java:80-84). Is that reflection (library) or standard navigation?
Default used: **standard navigation** (Kiro, 2026-11-06 05:02 UTC, W7). The checked cases Aegis-38 and Aegis-39 have source class gui ("Settings > Security reaches the same code without any gate", review/TASK_NOTE.md item 2), and their only route opens the Security page this way; the seven header edges are set to standard. All other reflection edges keep non_standard.

## Q-W8-1 (Kiro, 2026-11-06): the "framework calls X after construction" edge family in AmazeFileManager
135 hand edges carry the evidence "INFERRED framework calls <Class>.<method> after construction of <Class>" (for example MainActivity.<init> -> MainFragment.hide, RecyclerAdapter.<init> -> MainFragment.rename, BasicActivity.<init> -> MainActivity.onActivityResult). Several are false: the method is called by app code (an action mode item, a click) or by nobody. They shorten best routes and can make a gui route skip a step. Default used: only the edges on re-verified sampled routes were fixed (MainActivity.<init> -> MainFragment.hide dropped; the onNewIntent and onActivityResult entries gated). The other edges are kept. A decision is needed on whether to audit all 135.

## Q-W8-2 (Kiro, 2026-11-06): the W7 pre-screen misses helper-call steps
Edges such as RecyclerAdapter.onBindViewHolder -> GlideRequests.load(Integer) were not flagged, because the call sits in a helper (showThumbnailWithBackground, showRoundedThumbnail) that the edge's source method does not contain. Their guards are therefore not in guard_steps.csv. Default used: gates written by hand where a sampled route exposed one; no re-run of the pre-screen.

## Q-R3-1 (Kiro, 2026-11-06): is a selection, an open dialog or a typed form "state"? (review 3, fix 6)
review/TASK_NOTE.md lists "a UI session (a selection, an open dialog, an unsaved form)" as state, but a dialog the route itself opens is a GUI action on the route. Default used, applied the same way in all five apps:
- A selection that exists before the route's step (a row selected, an action mode open, a checked item) is STATE, kind `session`. The route cannot always make it, and the baseline has none.
- A dialog that a step on the route opens, and a form the user types into after the dialog opens, are GUI: the open or the typing is a GUI action on the step itself, so there is no gate. A dialog that is already open when the route starts (for example one left open by an earlier run) would be STATE; no row uses that.
- A form field that already holds saved text (an edited entry, an unsaved draft kept across a rotation) is STATE kind `session`.
W0 will test this default against the sample: if the labelled sample treats a typed form or an open dialog as state, the rows with text beginning "GUI: the ... dialog" are the ones to flip, and the rule is then one grep over `w7_judged.csv`.

## Q-R3-2 (Kiro, 2026-11-06): which files are STATE, which ENV? (review 3, fix 1)
Rule used: a file is STATE only when an in-app action can create it (a zip written by ZipService, an .aze from Encrypt, a vault or .apk backup the app writes, an .apkg export, a .torrent from Create torrent, the feeds backup); any other file comes from another app or the user and is ENV `other_app` (or `network` for a download). Applied:
- AmazeFileManager: 27 STATE file rows for .7z, .rar, .tar, .bz2, .tgz, .tbz, lzma, .xz, password-protected and AES archives became ENV other_app (the app creates only zip: ZipService and zip4j; SevenZOutputFile is never constructed).
- Aegis: the icon-pack rows (4 w7 rows, hand edges with ST_ICON_PACK_INSTALLED) became ENV other_app (Aegis imports an icon pack but cannot make one); the "vault missing or unreadable" rows became ENV other (no in-app action corrupts the vault).
- LibreTorrent: yes, the app creates and saves .torrent files itself (CreateTorrentDialog with the in-app FileManagerDialog in SAVE_FILE_MODE; CreateTorrentViewModel.java:211-217 `fs.write(bencode, savePath)`). So every .torrent row is STATE file (Ebd400945, Edcd2b301, Eb11be73f, E35438c83, E88a51caa, Ecc03ef24, Ed4fca1c6; Eda355555 is settings+file). IP filter files come from the system picker: ENV other_app.
Exceptions kept, with the reason: (a) the checked cases AmazeFileManager-01 (DatabaseViewerActivity.getDbTableNames) and AmazeFileManager-46 (FileUtils.installApk) have source class state in Appendix B, and openFile picks the viewer by the file extension only, so a file created with New file and named x.db or x.apk starts them: .db and .apk gates stay STATE in AmazeFileManager. (b) AnkiDroid-07 BackupManager.repairCollection has source class state, so the broken-collection file rows stay STATE.
Question for the reviewer: should the 7z, rar and tar gates follow the same extension argument (New file can name a file x.7z)? Default used: no, because those routes need the parsed content of a real archive, while openFile only checks the extension.

## Q-R3-3 (Kiro, 2026-11-06): the AmazeFileManager Ec06d0db3 row has no call line in onCreate
`MainActivity.onCreate -> AppConfig.runInBackground` has no direct call in onCreate (the runInBackground calls are at MainActivity.java:1001, 1012, 1701, 1720, all in other methods; onCreate starts its work with runInParallel at :365). The row's ref points at :365 and its text is kept ("unconditional"). Default used: leave the edge as a NONE row until W0 or the reviewer says it is an invented edge.

**Q-R3-2 and Q-R3-3 answered by the reviewer (review 4, 2026-11-07):** name-level archive steps stay STATE file, content-dependent steps are ENV other_app (REAUDIT-R4-ARCHIVE); Ec06d0db3 is cut (REAUDIT-R4-HELPER).

## Q-R4-1 (Kiro, 2026-11-07): MMEX Icepick state classes
MmxBaseFragmentActivity.onCreate and onSaveInstanceState reach the generated `<Activity>$$Icepick` classes of every activity (25 caller classes; Icepick looks the helper up by the runtime class). The edges are written from the base class, so MainActivity reaches AccountEditActivity$$Icepick.restore in 4 steps. Default used: left as it is in this round (the methods are generated code; a real route exists through each activity's own onCreate). Question: should each `$$Icepick` edge start at its own activity's onCreate, as REAUDIT-R4-HELPER does for lambdas? That would move about 15 methods from 4-step routes to the activity's own route; the class stays gui either way.

## Q-R5-1 (Kiro, 2026-11-07, LibreTorrent W8): shared host activities joined path-insensitively
PreferenceActivity hosts whichever settings fragment the intent names (PreferenceActivity.java:85-108), and TorrentService.onStartCommand handles shutdown actions for whichever intent started it (TorrentService.java:184-205). The graph joins any caller with any fragment or action, so two re-checked routes are not one real execution: SettingsRepositoryImpl.proxyRequiresAuth(boolean) (Settings -> PreferenceActivity -> ProxySettingsFragment, while the proxy page opens only from NetworkSettingsFragment) and TorrentCriticalWork.lambda$emitChangedEvent$0 (the engine start intent -> shutdown). Default used: both rows are WRONG (first verdict kept for the first; re-check WRONG for the second), and the class of each target is right either way (gui and state). Question: should these hosts get per-caller clones (@PROXY, @SHUTDOWN), as the Aegis importer variants do? That would fix the route print, not the class.
