# Review of the labels of five apps

An external review on 3 November 2026 compared the full labels of Aegis, AmazeFileManager, AnkiDroid, LibreTorrent and MMEX (`run_result/apps/<App>/graph/methods.csv`) with an independent hand-labelled sample of 50 unreached methods per app, and decided 23 disagreements from the source.

## What it found

- **Agreement:** on 249 sampled methods, the full labels agree with the sample on only 59% of the classes.
- **Too much gui:** many methods labelled gui need state or the environment, or are dead.
- **Too little state:** many methods labelled env have an in-app route that needs only state.
- **Causes,** all in how the best route is derived:
  - conditions on the route are ignored;
  - some routes start from an exported or external entry although an in-app route exists;
  - some calls are dispatched to types that are never created;
  - data from other apps, older app versions or servers is missed;
  - one-time intro screens are used as routes.
- **What holds up:** the dead verdicts.

We re-checked the review: it read our labels correctly in all 23 cases, and 6 of 6 cases we checked in the source agreed with it. A re-audit of the five apps follows the task note; see `handoff/MUSE_REAUDIT_5APPS.md`.

## Files

| File | What it is |
|---|---|
| `TASK_NOTE.md` | the reviewer's task note: goal, baseline, class rule, what to fix, how to measure |
| `sample_tune/<App>.csv` | the tuning half of the sample: every row whose id ends in an odd number, plus the 23 checked cases (added when received) |
| `checked_cases.csv` | the 23 disagreements decided from the source (added when received) |
| `measure.py` | compares the full labels with a sample folder: agreement, confusion table, weighted class shares, and blind A/B files for adjudication |
| `rounds/<n>/` | the report of each re-audit round |

## The held-out half

The rows whose id ends in an even number, except the 23 checked cases, are the held-out half. It stays out of this repository until the re-audit is finished. Then the reviewer measures it once, and adds it as `sample_holdout/`.

This split was fixed on 2026-11-05, before any re-audit result existed.
