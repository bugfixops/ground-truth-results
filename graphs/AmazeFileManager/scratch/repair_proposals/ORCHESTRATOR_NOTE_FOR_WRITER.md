# Note for the repair writer and reviewer (from the orchestrator, 2026-10-28)

Read this before you apply repair_proposals/1.md, 3.md or 4.md.

1. Proposal 1.md has 84 REMOVE rows for "inherited methods not declared in app classes" (e.g. FtpService.onCreate). Do NOT apply those blindly. For each one:
   - If the bad node is the SRC of edges that carry a chain (bad node -> app method), re-source those edges from the callback the class really declares (e.g. onStartCommand) or from its real caller. Check this against the printed source.
   - If a superclass in the app declares the method, retarget to that superclass's canonical node.
   - REMOVE only edges that model framework internals and carry no app chain.
2. Treat UNDECIDABLE overloads as unresolved edges (leave them out). Do not guess.
3. Package-path to canonical-name fixes (161 in 1.md) are mechanical and fine to apply after a spot-check.
4. The regression check is mandatory after every batch: REACHABLE + UNREACHABLE must not fall. A drop means a removal cut a real chain, so restore and re-source.
