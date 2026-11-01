# scan_unreachable.py --all — NOT RUN (this re-verification run)
Blocker: --all searches the FULL app source tree (final_java_only/Vanilla-Music/
app/*/, 115 .java files + res XML); only route-cited sources are reconstructed
locally (see check_bytecode_lines_NOT_RUN.md). Running it with the partial
source set would falsely report "no other mention" for methods whose callers
live in unfetched files, so it was not run. --callers WAS run and passed
(3 of 148, each explained in its own reason; see scratch/scan_callers.txt).
Carry-over evidence only (not re-claimed): the prior session's --all pass on
the byte-identical-count rebuild.
