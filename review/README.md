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
| `sample_tune/<App>.csv` | the tuning half of the sample: every row whose id ends in an odd number, plus the 23 checked cases |
| `sample_holdout/<App>.csv` | the held-out half: every row whose id ends in an even number, except the 23 checked cases (114 rows) |
| `checked_cases.csv` | the 23 disagreements decided from the source |
| `measure.py` | compares the full labels with a sample folder: agreement, confusion table, weighted class shares, and blind A/B files for adjudication |
| `blind_check/` | the protocol and the reader instructions of the blind check: readers classify methods from the source without seeing any label |
| `rounds/<n>/` | the report of each measurement round: `agreement.txt`, `disagreements.csv`, `blind.csv`, `blind_key.csv`, `adjudication.csv`, `result.txt` (round 0 has no adjudication; see its `result.txt`) |

## The held-out half

The rows whose id ends in an even number, except the 23 checked cases, are the held-out half. This split was fixed on 2026-11-05, before any re-audit result existed.

After the CI of the last graph change (80a2a913) the held-out half was built by script (`tools_dev/build_holdout.py`, 114 rows) into `sample_holdout/` and measured once (`rounds/holdout/`). No graph change was made from it.

| Status | Part | What | Where |
|---|---|---|---|
| **Done** | Agreement | 81 of 114 rows agree on the class (71.1%): Aegis 6 of 22, AmazeFileManager 15 of 22, AnkiDroid 23 of 24, LibreTorrent 19 of 23, MMEX 18 of 23. The tuning half at the same commit: 115 of 136 (84.6%). | `rounds/holdout/agreement.txt`, `rounds/3/` |
| **Done** | Who is right in the 33 disagreements | Judged blind from the source by two adjudicators each, a third for 4 rows: the full label in 18, the sample in 12, neither in 3. The source supports the full label in 99 of 114 rows (86.8%) and the sample in 93 (81.6%). | `rounds/holdout/result.txt`, `rounds/holdout/adjudication.csv` |
| **Left** | Causes of the 15 wrong full labels | Gates the screens do not see (AmazeFileManager, LibreTorrent), a reflection-made page labelled library (MMEX), one config method (AnkiDroid). Not fixed: the held-out half is a measurement. | `rounds/holdout/result.txt` |
| **Left** | Rows that depend on the dialog rule | 6 adjudicated rows change class if an open dialog counts as state. | `rounds/holdout/result.txt` |
| **Left** | Independent human check | The adjudicators were AI agents, not independent people. | `rounds/holdout/adjudicators/` |
