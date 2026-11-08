#!/bin/bash
# Keeps the schema 2 work going (version 5: records the model each run really used). Starts a fresh headless Claude Code session (prompt: handoff/RESUME_PROMPT_V2.md) while handoff/PROGRESS_V2.md
# still has an unchecked app. The model is read from handoff/MODEL_V2 at the start of every run (claude-haiku-5-5 or claude-sonnet-5-5; the aliases
# "haiku" and "sonnet" are NOT used: in this Claude Code version "haiku" means Haiku 4.5).
# A run lasts until it has finished, including the background helpers it starts (CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0). It is stopped after MAX_RUN seconds.
# A usage-limit message is waited out (20 minutes, then a new try).
# Before a run starts it waits (a) while another headless run of this job is still going (RUN_PATTERN), and (b) while there was activity after the end of
# our own last run: an interactive session or helper that touched handoff/WORKING_LOCK in the last 30 minutes, or a Claude transcript of this project
# written in the last 30 minutes.
# Start:  DEADLINE_HOURS=240 nohup caffeinate -i /Users/darshan/Desktop/yang/work/tools/resume_v4.sh <start_epoch_seconds> >/dev/null 2>&1 &
# Cancel: touch /Users/darshan/Desktop/yang/work/handoff/STOP_RESUME_V2   (or kill the pid in handoff/resume_v2.pid)
ROOT=/Users/darshan/Desktop/yang
H=${H:-$ROOT/work/handoff}
START=${1:-0}
DEADLINE=$((START + ${DEADLINE_HOURS:-48} * 3600))
MAX_RUN=${MAX_RUN:-172800}
LOG=$H/resume_v2.log
LOCK=$H/WORKING_LOCK
TDIR=${TDIR:-$HOME/.claude/projects/-Users-darshan-Desktop-yang}
CLAUDE=${CLAUDE:-claude}
TOOLS=${TOOLS:-/Users/darshan/Desktop/yang/work/tools}
RUN_PATTERN=${RUN_PATTERN:-claude -p You are continuing an unattended job}
echo $$ > "$H/resume_v2.pid"
log() { echo "$(date '+%F %T') $*" >> "$LOG"; }
todo() { grep -c '^- \[ \]' "$H/PROGRESS_V2.md" 2>/dev/null; }
mtime() { stat -f %m "$1" 2>/dev/null || echo 0; }
newest() { find "$TDIR" -name '*.jsonl' -exec stat -f %m {} + 2>/dev/null | sort -n | tail -1; }
model() { tr -d ' \n\r\t' < "$H/MODEL_V2" 2>/dev/null || echo claude-sonnet-5-5; }
last_run_end=$START
busy() {
  local now last lk
  now=$(date +%s)
  last=$(newest); last=${last:-0}
  [ "$last" -gt "$last_run_end" ] && [ $((now - last)) -lt 1800 ] && return 0
  lk=$(mtime "$LOCK")
  [ "$lk" -gt "$last_run_end" ] && [ $((now - lk)) -lt 1800 ] && return 0
  return 1
}
log "watcher v5 started (pid $$), start epoch $START ($(date -r "$START" '+%F %T' 2>/dev/null)), deadline in ${DEADLINE_HOURS:-48} h"
while [ "$(date +%s)" -lt "$START" ]; do
  [ -e "$H/STOP_RESUME_V2" ] && { log "stop file found while waiting"; exit 0; }
  sleep 30
done
while pgrep -f "$RUN_PATTERN" >/dev/null 2>&1; do sleep 60; done
last_run_end=$(date +%s)
runs=0; strikes=0
while [ "$(date +%s)" -lt "$DEADLINE" ]; do
  [ -e "$H/STOP_RESUME_V2" ] && { log "stop file found"; exit 0; }
  n=$(todo)
  [ "${n:-1}" -eq 0 ] && { log "no unchecked app left: done"; exit 0; }
  if pgrep -f "$RUN_PATTERN" >/dev/null 2>&1; then sleep 60; continue; fi
  if busy; then sleep 120; continue; fi
  runs=$((runs + 1))
  m=$(model)
  out="$H/resume_v2_run_$(date +%Y%m%d_%H%M%S).log"
  before=$(md5 -q "$H/PROGRESS_V2.md" 2>/dev/null)
  log "run $runs: $n app(s) left, model $m, starting headless claude -> $out"
  t0=$(date +%s)
  ( cd "$ROOT" && touch "$LOCK" && export CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0 && "$CLAUDE" -p "$(cat "$H/RESUME_PROMPT_V2.md")" --permission-mode auto --model "$m" --output-format json < /dev/null > "$out" 2>&1 ) &
  pid=$!
  while kill -0 "$pid" 2>/dev/null; do
    if [ $(( $(date +%s) - t0 )) -gt "$MAX_RUN" ]; then
      log "run $runs longer than $MAX_RUN s: stopping it"
      pkill -P "$pid" 2>/dev/null; kill "$pid" 2>/dev/null
      break
    fi
    sleep 60
  done
  wait "$pid" 2>/dev/null; rc=$?
  models=$(python3 -I "$TOOLS/run_models.py" "$out" 2>/dev/null)
  dt=$(( $(date +%s) - t0 ))
  last_run_end=$(date +%s)
  rm -f "$LOCK"
  after=$(md5 -q "$H/PROGRESS_V2.md" 2>/dev/null)
  log "run $runs ended rc=$rc after ${dt}s, progress file changed: $([ "$before" != "$after" ] && echo yes || echo no); $models"
  if grep -qiE 'usage limit|session limit|limit reached|hit your|resets [0-9]|rate limit|try again later|quota' "$out"; then
    log "limit message in the output: waiting 20 minutes"; sleep 1200; continue
  fi
  if [ "$before" = "$after" ] && [ "$dt" -lt 300 ]; then
    strikes=$((strikes + 1))
    [ "$strikes" -ge 3 ] && { log "3 quick runs without progress: giving up"; exit 1; }
    sleep 600
  else
    strikes=0
    sleep 60
  fi
done
log "deadline reached"
