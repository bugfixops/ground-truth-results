# Currency — lessons (local re-check, 2026-11-01)

- The stratified sampler does not promise 30 routes: with seed 20261025 it
  draws 27 for Currency because strata pools exhaust, so "sample 30" in a
  brief must be read as "sample up to 30" and the drawn count reported, not
  the requested count.
- A carried verification.csv can be stale in sample membership even when
  the build is clean: the branch log's 28 paths do not match this build's
  27 (3 dropped, 2 new), yet the build still reports 0 errors — path rows
  that no longer match the best route would show as STALE, and there are
  none, because the dropped rows were the ones whose routes changed.
- Framework citations are only checkable if the framework tree is
  reconstructed too: check_citations went from 41 problems to 2 once the
  cited AOSP files were fetched, and the last 2 are a single oversize file
  (ActivityManagerService.java, 1,086,106 B), not a graph error.
- scan_unreachable --callers hits are triage, not contradictions: the one
  hit (Singleton.getList <- ChartActivity.onCreate) is exactly the call
  site the branch_never_taken reason already explains (dead else-branch).
- Unclear must stay unclear: the widget and IME routes look fully
  app-verified, but their blocking steps live in another app's code
  (launcher, IME) that was not read, so upgrading them to correct on
  app-side evidence alone would overstate the check.
- A missing prescribed tool is a blocker, not a licence to improvise:
  tools/make_verification.py does not exist on branch work-2026-10-31, so
  the two newly judged path rows are held in scratch/route_judgements.md
  instead of hand-appended to verification.csv.
