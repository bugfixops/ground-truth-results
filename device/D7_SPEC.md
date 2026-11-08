# D7 specification: DEVICE rows in make_verification.py

For each app's merger. The device lead defines this format; mergers
implement it in their app's `graphs/<App>/make_verification.py` and
test it in a private copy before pushing.

## Rule

- If `graphs/<App>/device/results.csv` does NOT exist, running
  `make_verification.py` must produce output byte-identical to
  today's output (`cmp` prints nothing). The DEVICE code path must
  not run at all in that case.
- If it exists, append one row per route AFTER all existing rows, in
  `device/results.csv` order (route order). Do NOT re-sort existing
  rows: several apps' current row order differs from a
  (type, item, confirmed_by) sort, and re-sorting would break the
  byte-identical requirement for the no-results case.
- Row fields (header `type,item,result,confirmed_by,ref,edges,note`):
  - `type` = `path`
  - `item` = the route's method (the `method` column)
  - `result` = `correct` when `reached` is `yes`, otherwise `unclear`
  - `confirmed_by` = `DEVICE`
  - `ref` = `device run <run>/<script>` (the `run` and `script`
    columns, e.g. `device run run-42-1/route_01.py`)
  - `edges` = the route's edges (the `edges` column, unchanged)
  - `note` = script status; for `unclear` rows the reason: not
    reached (`reached=no`), script failed (`script_status` is
    `failed_at_step_N` or `timeout`), or unscriptable
    (`script_status=unscriptable`).
- A route not reached NEVER becomes `wrong`. No label changes.
  DEVICE rows never feed back into labels, edges, or route checks.

## Input format (from device/compare.py)

`graphs/<App>/device/results.csv` columns:
`route,method,edges,reached,script_status,run,script`.
`reached` is `yes`, `no`, or `not_run`; `script_status` is `ok`,
`failed_at_step_N`, `timeout`, or `unscriptable`.

## Synthetic-results test (required before pushing a D7 change)

1. Copy the app's `make_verification.py` plus its inputs into a
   private directory (never the shared tree).
2. Run it once with no `device/results.csv` present: output must be
   byte-identical to the current committed `verification.csv`.
3. Add a synthetic `device/results.csv` with at least these rows:
   - one `reached=yes, script_status=ok` route -> expect a DEVICE
     row with `result=correct`;
   - one `reached=no, script_status=ok` route -> expect `unclear`
     with note naming not reached;
   - one `script_status=failed_at_step_3` route -> expect `unclear`
     with note naming the script failure;
   - one `script_status=unscriptable` route -> expect `unclear`
     with note naming unscriptable.
4. Run again: the ONLY differences from step 2 must be the appended
   DEVICE rows, in input order, after all existing rows. Run twice:
   both runs byte-identical.
5. Report the diff (added rows only) to the merger review; never
   push a D7 change whose only evidence is "it ran".
