#!/usr/bin/env bash
# Rebuild the trigger graphs and run the eight checks for the apps named as arguments ("all" or none = every app).
# Run from the repo root. Writes graphs/<App>/out/ (build outputs and README) and graphs/<App>/scratch/ci_latest/
# (1_build.txt ... 8b_scan_callers.txt and SUMMARY.txt). Used by .github/workflows/rebuild-graphs.yml; runs the same
# on any machine with python3 (no packages needed).
set -u
apps_all="Currency Diary hash-checker Omni-Notes openlauncher Vanilla-Music Markor AnyMemo Aegis AmazeFileManager AnkiDroid MMEX LibreTorrent"
prefix() {
  case "$1" in
    Currency) echo currency ;; Diary) echo diary ;; hash-checker) echo hash-checker ;; Omni-Notes) echo omni-notes ;;
    openlauncher) echo openlauncher ;; Vanilla-Music) echo vanilla ;; Markor) echo markor ;; AnyMemo) echo anymemo ;;
    Aegis) echo aegis ;; AmazeFileManager) echo amazefilemanager ;; AnkiDroid) echo ankidroid ;; MMEX) echo mmex ;;
    LibreTorrent) echo libretorrent ;; *) echo "" ;;
  esac
}
apps="$*"
if [ -z "$apps" ] || [ "$apps" = "all" ]; then apps="$apps_all"; fi
for a in $apps; do
  x=$(prefix "$a")
  if [ -z "$x" ]; then echo "unknown app: $a"; continue; fi
  o="graphs/$a/scratch/ci_latest"
  rm -rf "$o"; mkdir -p "$o"
  # the tools read the first graphs/<App>/out/*_trigger_graph.json they find: remove outputs of other prefixes first
  for f in graphs/$a/out/*_trigger_graph.json graphs/$a/out/*_trigger_graph.html; do
    [ -e "$f" ] || continue
    case "$(basename "$f")" in "${x}_trigger_graph.json"|"${x}_trigger_graph.html") ;; *) rm -f "$f"; echo "removed stale $f" ;; esac
  done
  python3 -I tools/build_graph.py "graphs/$a" "$x" > "$o/1_build.txt" 2>&1; echo "exit $?" >> "$o/1_build.txt"
  python3 -I tools/gen_readme_v2.py "$a" > "$o/gen_readme.txt" 2>&1
  python3 -I tools/check_citations.py "$a" > "$o/2_citations.txt" 2>&1
  python3 -I tools/check_routes.py "$a" > "$o/3_routes.txt" 2>&1
  python3 -I tools/check_bytecode_lines.py "$a" > "$o/4_bytecode.txt" 2>&1
  files="graphs/$a/graph_def.py"
  [ -d "graphs/$a/graph_def_mod" ] && files="$files $(ls graphs/$a/graph_def_mod/*.py)"
  [ "$a" = "LibreTorrent" ] && [ -d graphs/$a/parts ] && files="$files $(ls graphs/$a/parts/*.py 2>/dev/null)"
  {
    echo "DEAD|FRAMEWORK_ONLY lines: $(cat $files | grep -c 'DEAD\|FRAMEWORK_ONLY')"
    echo "FW-MEMORY lines: $(cat $files | grep -c 'FW-MEMORY')"
    echo "PENDING lines: $(cat $files | grep -c 'PENDING')"
    echo "STRICT = True line in graph_def.py: $(grep -c '^STRICT = True' graphs/$a/graph_def.py)"
    echo "files searched: $files"
  } > "$o/5_7_greps.txt"
  python3 -I tools/scan_unreachable.py "$a" --all > "$o/8a_scan_all.txt" 2>&1
  python3 -I tools/scan_unreachable.py "$a" --callers > "$o/8b_scan_callers.txt" 2>&1
  {
    echo "app $a | commit $(git rev-parse --short HEAD 2>/dev/null) | $(date -u '+%Y-%m-%d %H:%M UTC')"
    grep -E '^(methods|verdicts|unreachable by kind|labels confirmed by|verification (label|edge|path|device)|errors|warnings|exit)' "$o/1_build.txt"
    echo "check 2: $(grep -E '^citations' "$o/2_citations.txt" || tail -1 "$o/2_citations.txt")"
    echo "check 3: $(tail -1 "$o/3_routes.txt")"
    echo "check 4: $(grep -E 'where the cited line does not show the callee' "$o/4_bytecode.txt" || echo 'no summary line (see 4_bytecode.txt; a traceback means the check crashed)')"
    head -4 "$o/5_7_greps.txt" | sed 's/^/check 5-7: /'
    echo "check 8 (--callers): $(tail -1 "$o/8b_scan_callers.txt")"
    if [ -f "graphs/$a/verification.csv" ]; then
      echo "verification.csv rows: path $(grep -c '^path,' graphs/$a/verification.csv; true), DEVICE $(grep -c ',DEVICE,' graphs/$a/verification.csv; true)"
    else
      echo "verification.csv: missing"
    fi
  } > "$o/SUMMARY.txt"
  echo "== $a"; cat "$o/SUMMARY.txt"
done
