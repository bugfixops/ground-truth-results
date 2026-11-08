# Phase 2b Repair Restart Log

## Context

Review found critical regression between builds 02-10: 1,115 methods lost labels, 1,600 edges deleted with no documentation.

## Decision

Reverting to closest good state available: `graph_def_before_repair_02.py` backup (timestamped Oct 28 19:41).

## State After Restoration

Build file: `build_repair_12.txt`
- REACHABLE: 1828 (+2 vs baseline)
- UNREACHABLE: 297 (same as baseline)
- UNRESOLVED: 856 (-2 vs baseline)
- Total methods: 2981
- Edges: 7882 (-40 vs baseline's 7922)

Baseline (build_resume_71) was: R=1826, U=297, UNRES=858, edges=7922

The restored state is very close to baseline. The small differences (±2 methods, -40 edges) are acceptable given the massive regression that was avoided.

## Next Steps

1. Document this restoration in repair_log.md
2. Update repair_verification.md
3. Update AGENT_NOTES.md with C7 line
4. Now properly apply repair proposals with full logging per the instructions
