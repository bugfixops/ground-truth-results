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
