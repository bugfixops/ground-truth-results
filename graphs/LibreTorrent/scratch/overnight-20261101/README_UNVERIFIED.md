# Overnight push 2026-11-01 — UNVERIFIED

Everything in this push is UNVERIFIED staged work from the 2026-11-01
overnight run (all 13 apps except device checks). Nothing here is merged
into any graph_def.py, no PROGRESS_V2.md line was changed, and no [K] line
is claimed by this push. Builds, samples, checks, and logs are to run on
the user's Mac against the full repo.

Layout:
- graphs/LibreTorrent/scratch/merge-ready/batch<N>-merge-ready.md (120):
  updated LibreTorrent labels, 3964 REACHABLE / 691 UNREACHABLE / 77 OPEN
  of 4732 (see MERGE_PREP_TOTALS_UNVERIFIED.txt). These supersede the
  previously pushed merge-ready files.
- graphs/LibreTorrent/scratch/overnight-20261101/: LibreTorrent decisions,
  run log, spot-checks (Phase 2 + Phase 3), verdicts, greps, apply logs,
  batch-99 verification, totals, this README, the D29 user decision, and
  stream-reports/ (cross-app Stream B/D run logs, decisions, and the
  Stream D final report, staged here for want of a global scratch dir).
- graphs/<App>/scratch/overnight-20261101/: per-app overnight reports,
  decisions, drafted logs (readme_notes, LESSONS, AGENT_NOTES mirrors),
  check/sample outputs, and proposals for AmazeFileManager, AnkiDroid,
  MMEX, Currency, Diary, hash-checker, Omni-Notes, openlauncher,
  Vanilla-Music, Markor, AnyMemo, and Aegis.
- graphs/Aegis/make_verification.py and graphs/MMEX/make_verification.py:
  newly authored local tools (UNVERIFIED drafts). No make_verification.py
  was placed in tools/. Where an app already had one on the branch, the
  branch copy was left untouched.
- No verification.csv is pushed: the Vanilla-Music file regenerated overnight
  was verified byte-identical to the branch copy (same blob SHA), and all
  other apps' verification.csv files were preserved branch copies, so none
  is included here; no branch verification.csv was overwritten.

Decisions in these files are Muse's own, recorded for user/Yang review,
except D29_USER_DECISION.md, which records a decision by the user.
