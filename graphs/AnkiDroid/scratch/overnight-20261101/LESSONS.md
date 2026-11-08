# AnkiDroid — LESSONS (from this leaf's run; DRAFT, not finalised)

These bullets record what actually found errors or blocked work tonight.
They are a draft: the route sample and the eight checks never ran, so no
bullet here claims a verified route fix.

- A connector directory listing is not a checkout: file sizes and blob SHAs
  can verify a small file exactly (build_report.txt, conflicts.md,
  method_list.json all matched), while every file over the display limit
  (graph_def.py, auto_calls.json, methods.csv, trigger_graph.json) stays
  unreachable no matter how many listings succeed.
- A download link in a connector response is not a fallback when it carries
  a token: the token rule forbids using it, so "too large to display"
  is a hard stop for that file, not a detour.
- Parts do not reconstruct a graph: sup blocks and orchestrator addenda
  live only inside graph_def.py, and auto edges (8,146 of 9,178) live in
  auto_calls.json, so an assembled file would silently differ from the
  branch build — better to stop and name the blocker than to present it.
- Tool coverage never settles a label: the single Card.toString APE hit
  survived three rounds of source reading precisely because every printed
  stringification site turned out to be the inner AdvancedStatistics Card,
  not libanki Card.
- A library comment is not a dispatch: EasySSLSocketFactory's "some
  connection managers" comment is consistent with both outcomes, so the
  equals/hashCode pair needs a printed library call, not a reading of
  the comment, to flip.
- Version gates must name their source: CompatHelper's gates are all
  SDK_INT (device level), which settles the Compat chain under API 27
  regardless of target 23 — but that argument does not extend to
  framework behaviour keyed on targetSdk, which needs its own printed line.
- A registry edge is not an explicit edge: Hooks.runFilter dispatches
  through the Hook interface (line 150), so the Stats -> AdvancedStatistics
  link is non_standard via the registry, and any direct explicit edge for
  the same pair would be wrong even though the method is reachable.
- Gate text is part of the edge, not a note: the MG943
  advanced_statistics_enabled condition was recorded as a note on the
  label_100 edge, which is why it still needs attaching as a STATE
  settings gate at merge time.
