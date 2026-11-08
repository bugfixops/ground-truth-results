# check_bytecode_lines.py — NOT RUN (this re-verification run)
Blocker: the checker needs tools/show_route.py's source index over the FULL app
tree (final_java_only/Vanilla-Music/app/*/, 115 .java files + res XML) plus every
file cited by bytecode edges (94 distinct files in auto_calls.json calls). This
run reconstructed only: all graph/tool inputs, the 10 Cases() build inputs, the
38 further app .java files + manifest + 5 res XML cited on the 30 sampled
routes, and the 47 FW-SRC files cited in the built graph. Running the checker
now would report "file not found" for most edges — a missing-cache artefact,
not a graph verdict — so it was not run as a gate.
Partial mitigation actually done: every bytecode single-line citation on the 30
sampled routes was checked by eye against the fetched sources during route
reading (all matched). Carry-over evidence only (not re-claimed): the prior
session's pass on the byte-identical-count rebuild.
