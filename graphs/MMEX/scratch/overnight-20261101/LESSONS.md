# MMEX — lessons (local mirror draft, 2026-11-01; pending faithful build)

- Connector display refuses files above ~1 MB; verify local part copies by git
  blob SHA against the connector directory listing instead of re-fetching them
  (100 MMEX parts verified that way this session, zero mismatches).
- A rate-limit detector that greps tool output for "429" false-fires on line
  numbers inside successfully downloaded file content; detect limits
  structurally (no resource text plus an explicit limit message), never by
  substring.
- REGISTER edges do not confer reachability (build bfs skips REGISTER), so
  methods reachable only through registration need explicit dispatch edges —
  that is why part 146 exists, and why a REGISTER edge alone never proves a route.
- Shared env text across the debug/release Timber trees misstates the
  configuration: DebugTree (debug) and ScreenTree (release) need separate env
  texts, and "an error is logged" understates DebugTree's INFO-or-above post.
- ACTION_PICK gates what setResult() returns (RESULT_OK vs CANCELED / no result),
  not the finish call itself: home-arrow and Back-key routes to
  setResultAndFinish are ungated, so guard wording must be scoped to the gated step.
- Auto (bytecode) edges carry no guards, so a release-only dispatch (Timber.e to
  ScreenTree) appears as a route in the built graph; route checks must judge each
  step against printed source guards, not against edge presence.
- A search_code 0 / incomplete result proves nothing in this repo (the index
  misses known-present files); absence claims need a printed grep or a directory
  listing, not a search result.
- A branch build_report showing 0 errors / 0 warnings does not mean every edge
  is valid under the standard configuration: edges without a config filter can
  carry release-only routes into a debug-config graph, which only step-by-step
  route reading catches.
