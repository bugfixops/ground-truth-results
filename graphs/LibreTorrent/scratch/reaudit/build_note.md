# W2 LibreTorrent — build note (2026-11-06)

## What W2 changed for this app
- `graphs/LibreTorrent/graph_def.py`: one added block after line 11 —
  a W2 comment recording the first-run check plus `SETUP_ONLY = set()`.
  No EDIT change (no gate was cleared), no edge changes.
- New files under `graphs/LibreTorrent/scratch/reaudit/`:
  `state_gates.csv`, `check_w2_acceptance.py`, `check_w2_output.txt`,
  this note.

## Build status: NOT RUN in the W2 copy — environment blocker, parent to run
Two blockers in this subagent session, both verified by direct tests:
1. The `cp -a` that created `~/workspace/w2/LibreTorrent` partially failed
   with "Operation not permitted" on writes; in particular the copy's
   `tools/build_graph.py` is 0 bytes (source is 51,055 bytes). The files
   W2 depends on copied byte-identically (md5-verified): graph_def.py,
   out/methods.csv, out/libretorrent_trigger_graph.json.
2. This session's exec sandbox rejects every file write() syscall with
   EPERM (even a 16-byte write to /tmp or /dev/shm, repeatedly, also after
   a 45 s wait), so no builder run here could write its outputs. File-tool
   writes (used for all W2 deliverables above) are unaffected.

Parent: apply the graph_def.py block in the real tree (or repair the
copy's tools/ from the real tree) and run:
    python3 -I tools/build_graph.py LibreTorrent
(or `bash handoff/ci/rebuild.sh LibreTorrent`), then re-run
`graphs/LibreTorrent/scratch/reaudit/check_w2_acceptance.py`.

## Expected result (proof, not a guess)
Outputs should be byte-identical to the current ones. With SETUP_ONLY
empty, the builder takes its aliasing path (tools/build_graph.py in the
real tree, lines 536-539: the *_all route dicts alias the filtered ones
when `setup_only` is empty, and setup_only_methods stays empty) — the
same switches-off identity the W1 work verified for all 13 apps. The W2
edit adds no edges, clears no gate and does not touch the EDIT chain
(final assignment `EDIT = _kiro_k4_edit`, graph_def.py tail).

## Before numbers (current outputs, CI-verified tree 8c7c00c8)
- methods 4732: REACHABLE 3967, UNREACHABLE 765
- build_report.txt: errors: 0, warnings: 0
- edges with needs_state in the whole graph: 13; distinct needs_state
  texts on REACHABLE best routes: exactly 1 ("adapter.getItemCount() > 0",
  2 methods) — decided KEEP, see state_gates.csv.
