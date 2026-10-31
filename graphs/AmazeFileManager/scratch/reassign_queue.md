# Reassignment Queue - Classes Needing Proper Edge-Backed Labels

Generated: 2026-10-27 after quality gate rejection of Helpers 1-3

## Rejection Reasons

- **Helper 1**: Complete rejection - 0 edges, claimed 297 REACHABLE without routes
- **Helper 2**: Partial rejection - only 30/305 have edges with source, rest are assertions
- **Helper 3**: Partial rejection - only 120/562 have edges, rest use vague "INFERRED typical usage"
- **Helper 4**: Honest incomplete - 30 accepted, 959 remaining

## Quality Requirements for Reassignment

Per sections 3 and 5:
1. **REACHABLE** requires real e(...) edges showing route from entry point  
2. **Library/generated methods**: need printed app call site OR grep -rn showing NO call site (then UNREACHABLE)
3. **UNREACHABLE** is EXPECTED for: dead utility methods, unused generated code, config-closed branches, API-level guards
4. **Every claim** needs printed source lines (sed -n verification)
5. Labeling everything REACHABLE is a REJECTED shortcut

## Classes Requiring Reassignment

Total: ~350+ classes need proper edge-backed labels

(See scratch/reassign_chunks/chunk_*.txt for divided assignments)
