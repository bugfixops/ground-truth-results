# R5 verdicts — batch 114 (2 rows)

Scope: rows verified OPEN in the main table of `phase3/work/batch114-merge-ready.md`.
No L1–L5 verdict file judges these rows (L2/batch114.md covers trio rows only
and names 114/22, 114/23 as out of scope, untouched plain setters). Corpus as
in batch28.md; P2 applies. No decided rule covers a plain POJO setter row.

## 114/22 — PreferenceActivityConfig.setFragment — stays OPEN — confirmed_by —

- Work-file identity: main-table row L122, OPEN, `—`.
- Definition: PreferenceActivityConfig.java:46–49. The work file notes
  SettingsFragment uses the 2-arg ctor (:235–237) and PreferenceActivity
  uses only the getters (:70–71).
- New grep (misc_methods.txt): zero `setFragment` hits anywhere in the
  corpus. Verified in print: PreferenceActivity.java:70–71 uses only
  `config.getFragment()` / `config.getTitle()`, and
  SettingsFragment.java:235 constructs via `new PreferenceActivityConfig(...)`.
  The fragment field is set by the ctor, never via this setter, in the corpus.
- Verdict: stays OPEN.
- What would change it: a printed PreferenceActivityConfig.setFragment
  call site, or a saved full-repo grep. Never UNREACHABLE on corpus-zero
  alone (P2).

## 114/23 — PreferenceActivityConfig.setTitle — stays OPEN — confirmed_by —

- Work-file identity: main-table row L123, OPEN, `—`.
- Definition: PreferenceActivityConfig.java:56–59. The work file notes
  `toolbar.setTitle(title)` (PreferenceActivity.java:76) is a different
  method.
- New grep (setters_getters_addItem.txt): every `.setTitle(` hit names a
  toolbar/dialog/menu receiver, never a PreferenceActivityConfig. Zero
  setter call sites in the corpus; the title field is set by the ctor.
- Verdict: stays OPEN.
- What would change it: a printed PreferenceActivityConfig.setTitle call
  site, or a saved full-repo grep. Never UNREACHABLE on corpus-zero
  alone (P2).
