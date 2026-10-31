#!/bin/bash
# Overnight convert run for AnkiDroid, MMEX and LibreTorrent (prompt: handoff/RESUME_PROMPT_CONVERT.md).
# Starts a headless Claude Code run and starts another one while handoff/PROGRESS_V2.md still has a "- [C]" app.
# It does not wait for the Aegis run and does not use its stop file.
# Stop: touch /Users/darshan/Desktop/yang/work/handoff/STOP_CONVERT (the run that is going keeps going until it ends).
ROOT=/Users/darshan/Desktop/yang
H=$ROOT/work/handoff
LOCK=$H/WORKING_LOCK
LOG=$H/resume_convert.log
CLAUDE=${CLAUDE:-claude}
MAX_RUN=${MAX_RUN:-172800}
RUN_PATTERN="claude -p You are continuing the convert job"
echo $$ > "$H/resume_convert.pid"
log() { echo "$(date '+%F %T') $*" >> "$LOG"; }
todo() { grep -c '^- \[C\]' "$H/PROGRESS_V2.md" 2>/dev/null; }
model() { tr -d ' \n\r\t' < "$H/MODEL_V2" 2>/dev/null || echo claude-haiku-5-5; }
strikes=0
log "convert runner started (pid $$)"
while true; do
  [ -e "$H/STOP_CONVERT" ] && { log "stop file found"; exit 0; }
  n=$(todo)
  [ "${n:-0}" -eq 0 ] && { log "no [C] app left: done"; exit 0; }
  if pgrep -f "$RUN_PATTERN" >/dev/null 2>&1; then sleep 60; continue; fi
  m=$(model)
  out="$H/resume_convert_run_$(date +%Y%m%d_%H%M%S).log"
  before=$(md5 -q "$H/PROGRESS_V2.md" 2>/dev/null)
  log "run: $n app(s) left, model $m, output $out"
  t0=$(date +%s)
  ( cd "$ROOT/work" && touch "$LOCK" && export CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0 && caffeinate -i "$CLAUDE" -p "$(cat "$H/RESUME_PROMPT_CONVERT.md")" --permission-mode auto --model "$m" --output-format json < /dev/null > "$out" 2>&1 ) &
  pid=$!
  while kill -0 "$pid" 2>/dev/null; do
    if [ $(( $(date +%s) - t0 )) -gt "$MAX_RUN" ]; then
      log "run longer than $MAX_RUN s: stopping it"
      pkill -P "$pid" 2>/dev/null; kill "$pid" 2>/dev/null
      break
    fi
    sleep 60
  done
  wait "$pid" 2>/dev/null; rc=$?
  dt=$(( $(date +%s) - t0 ))
  rm -f "$LOCK"
  after=$(md5 -q "$H/PROGRESS_V2.md" 2>/dev/null)
  log "run ended rc=$rc after ${dt}s, progress file changed: $([ "$before" != "$after" ] && echo yes || echo no)"
  if grep -qiE 'usage limit|session limit|limit reached|hit your|resets [0-9]|rate limit|try again later|quota' "$out" 2>/dev/null; then
    log "limit message in the output: waiting 20 minutes"; sleep 1200; continue
  fi
  if [ "$before" = "$after" ] && [ "$dt" -lt 300 ]; then
    strikes=$((strikes + 1))
    [ "$strikes" -ge 3 ] && { log "3 quick runs without progress: giving up (check the last output for an error)"; exit 1; }
    sleep 600
  else
    strikes=0
    sleep 60
  fi
done
