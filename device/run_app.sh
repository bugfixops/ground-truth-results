#!/usr/bin/env bash
# Route replay runner (brief D4). Run from the repo root:
#   bash device/run_app.sh <App> <glob> <outdir> [--dry-run]
#   <glob> selects route scripts, e.g. "route_*.py" (matched against the
#   script basename in device/routes/<App>/).
#
# Real mode (default): waits for the device, roots it, installs the
# instrumented APK WITHOUT -g (each route grants only its own
# permissions, unlike the work-emulator tool runner), then per route:
#   (1) pm clear; (2) setup.py (if present) + ROUTES.csv fixtures and
#   grants; (3) one coverage dump, discarded; (4) route script with a
#   10-minute timeout; (5) final coverage dump; (6) JaCoCo report for
#   that dump (--classfiles from $WEMU ci/app_env.py CLASSES);
#   (7) device/jacoco_lookup.py maps the target method in the report.
# Writes <outdir>/results.csv (columns: app,route,method,edges,reached,
# script_status,steps_done,steps_total,error,run_id), per-route steps
# logs, screens/route_NN/ and logcat/route_NN.txt evidence.
#   reached = yes | no | not_run; script_status = ok | failed_at_step_N
#   | timeout | unscriptable. Coverage truth is reported even when the
#   script failed or timed out; a missing/invalid final dump gives
#   reached=not_run with error=coverage_missing. A lookup of "absent"
#   gives reached=no with error=method_absent_in_report.
#   failed_at_step_0 = setup or fixture phase; failed_at_step_1 after
#   steps_done=0 also covers a dry-plan failure (see below).
# Dry-run mode (--dry-run): no adb at all. Runs device/drycheck.py
# --load-scripts, which writes <outdir>/dryrun_report.txt (one line per
# route, PASS or FAIL with reason, plus "<App>: N PASS, M FAIL").
#
# Environment: WEMU (work-emulator checkout, required); RUN_ID (default
# local-<UTC timestamp>); JACOCO_JAR (default $WEMU/.cache/jacococli.jar,
# fetched via $WEMU/ci/get_jacoco.sh when missing).
set -u

APP="${1:-}"; GLOB="${2:-}"; OUTDIR="${3:-}"; DRY=0
if [ "${4:-}" = "--dry-run" ]; then DRY=1; fi
if [ -z "$APP" ] || [ -z "$GLOB" ] || [ -z "$OUTDIR" ]; then
  echo "usage: run_app.sh <App> <glob> <outdir> [--dry-run]" >&2; exit 2
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$SCRIPT_DIR")"
DEVICE_DIR="$SCRIPT_DIR"
WEMU="${WEMU:-}"
if [ -z "$WEMU" ]; then echo "run_app.sh: \$WEMU is not set" >&2; exit 2; fi
RUN_ID="${RUN_ID:-local-$(date -u +%Y%m%dT%H%M%SZ)}"

log() { echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) $*" | tee -a "$OUTDIR/run.log"; }

mkdir -p "$OUTDIR"
: > "$OUTDIR/run.log"

if [ "$DRY" = 1 ]; then
  log "dry run for $APP (no adb)"
  python3 -I "$DEVICE_DIR/drycheck.py" "$APP" --root "$ROOT" --wemu "$WEMU" \
    --out "$OUTDIR" --load-scripts
  exit $?
fi

# --- real mode: app environment from work-emulator -------------------
eval "$(cd "$WEMU" && python3 ci/app_env.py "$APP")"  # sets PKG RECEIVER APK CLASSES
APK_ABS="$WEMU/$APK"
JACOCO_JAR="${JACOCO_JAR:-$WEMU/.cache/jacococli.jar}"
if [ ! -f "$JACOCO_JAR" ]; then
  log "fetching JaCoCo CLI via $WEMU/ci/get_jacoco.sh"
  (cd "$WEMU" && bash ci/get_jacoco.sh) || true
fi
if [ ! -f "$JACOCO_JAR" ]; then echo "run_app.sh: no $JACOCO_JAR" >&2; exit 2; fi
command -v adb >/dev/null 2>&1 || { echo "run_app.sh: adb not found" >&2; exit 2; }

wait_for_device() {
  adb wait-for-device
  local i boot
  for i in $(seq 1 120); do
    boot="$(adb shell getprop sys.boot_completed 2>/dev/null | tr -d '\r')"
    [ "$boot" = "1" ] && break
    sleep 5
  done
}

dump_once() {  # dump_once <outfile> ; 0 when the dump is valid
  local out="$1"
  adb shell am broadcast -a edu.gatech.m3.emma.COLLECT_COVERAGE -n "$PKG/$RECEIVER" >/dev/null 2>&1
  sleep 2
  rm -f "$out"
  if ! adb pull "/data/data/$PKG/files/coverage.ec" "$out" >/dev/null 2>&1; then
    adb shell run-as "$PKG" cat files/coverage.ec > "$out" 2>/dev/null || true
  fi
  [ -s "$out" ] || return 1
  local magic size
  magic="$(od -An -tx1 -N3 "$out" | tr -d ' \n')"
  size="$(wc -c < "$out" | tr -d ' ')"
  [ "$magic" = "01c0c0" ] && [ "$size" -gt 5 ]
}

jacoco_report() {  # jacoco_report <ec> <xml>
  local ec="$1" xml="$2" args=() c
  for c in $CLASSES; do args+=(--classfiles "$WEMU/$c"); done
  java -jar "$JACOCO_JAR" report "$ec" "${args[@]}" --xml "$xml" >/dev/null 2>&1
}

csv_escape() { echo "$1" | tr ',' ';' | tr '\n' ' ' | tr '\t' ' '; }

wait_for_device
adb root >/dev/null 2>&1 || true
adb wait-for-device
log "installing $APK_ABS WITHOUT -g"
adb install -r -t "$APK_ABS" || { echo "run_app.sh: install failed" >&2; exit 1; }

mkdir -p "$OUTDIR/steps" "$OUTDIR/steps_dry" "$OUTDIR/screens" \
  "$OUTDIR/logcat" "$OUTDIR/dumps" "$OUTDIR/coverage"
echo "app,route,method,edges,reached,script_status,steps_done,steps_total,error,run_id" > "$OUTDIR/results.csv"

ROUTES_DIR="$ROOT/device/routes/$APP"
python3 -I "$DEVICE_DIR/route_info.py" "$APP" --all --root "$ROOT" > "$OUTDIR/.routes.tsv" || {
  echo "run_app.sh: cannot read ROUTES.csv for $APP" >&2; exit 1; }

while IFS="$(printf '\t')" read -r route method edges perms fixtures setup status; do
  [ -z "$route" ] && continue
  if [[ "$status" == unscriptable* ]]; then
    reason="${status#unscriptable:}"
    echo "$APP,$route,$method,$edges,not_run,unscriptable,0,0,$(csv_escape "$reason"),$RUN_ID" >> "$OUTDIR/results.csv"
    log "$route unscriptable: $reason"
    continue
  fi
  script="$ROUTES_DIR/$route.py"
  base="$(basename "$script")"
  case "$base" in
    $GLOB) ;;
    *) log "$route skipped (outside glob $GLOB)"; continue ;;
  esac
  if [ ! -f "$script" ]; then
    echo "$APP,$route,$method,$edges,not_run,failed_at_step_1,0,0,missing_script,$RUN_ID" >> "$OUTDIR/results.csv"
    log "$route missing script"
    continue
  fi
  # Dry plan first: steps_total = planned action lines.
  if ! python3 -I "$script" --package "$PKG" --log "$OUTDIR/steps_dry/$route.log" \
      --outdir "$OUTDIR" --dry-run >>"$OUTDIR/run.log" 2>&1 < /dev/null; then
    echo "$APP,$route,$method,$edges,no,failed_at_step_1,0,0,dry_run_failed,$RUN_ID" >> "$OUTDIR/results.csv"
    log "$route dry plan failed"
    continue
  fi
  steps_total="$(wc -l < "$OUTDIR/steps_dry/$route.log" | tr -d ' ')"
  adb shell pm clear "$PKG" >/dev/null 2>&1
  # Setup (per-app setup.py, if the merger shipped one): once per route.
  if [ -f "$ROUTES_DIR/setup.py" ]; then
    if ! python3 -I "$ROUTES_DIR/setup.py" --package "$PKG" \
        --log "$OUTDIR/steps/$route.setup.log" --outdir "$OUTDIR" \
        >>"$OUTDIR/run.log" 2>&1 < /dev/null; then
      echo "$APP,$route,$method,$edges,no,failed_at_step_0,0,$steps_total,setup_failed,$RUN_ID" >> "$OUTDIR/results.csv"
      log "$route setup failed"
      continue
    fi
  fi
  # Fixtures + media scan, then per-route permission grants.
  fixture_failed=0
  if [ -n "$fixtures" ]; then
    oldifs="$IFS"; IFS=';'
    for fix in $fixtures; do
      fix="$(echo "$fix" | sed 's/^ *//;s/ *$//')"
      [ -z "$fix" ] && continue
      if ! adb push "$WEMU/fixtures/$fix" "/sdcard/$fix" >>"$OUTDIR/run.log" 2>&1; then
        fixture_failed=1; log "$route fixture push failed: $fix"; break
      fi
      case "$fix" in
        Music/*|Pictures/*)
          adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE \
            -d "file:///sdcard/$fix" >/dev/null 2>&1 || true ;;
      esac
    done
    IFS="$oldifs"
  fi
  if [ "$fixture_failed" = 1 ]; then
    echo "$APP,$route,$method,$edges,no,failed_at_step_0,0,$steps_total,fixture_push_failed,$RUN_ID" >> "$OUTDIR/results.csv"
    continue
  fi
  if [ -n "$perms" ]; then
    oldifs="$IFS"; IFS=';'
    for perm in $perms; do
      perm="$(echo "$perm" | sed 's/^ *//;s/ *$//')"
      [ -z "$perm" ] && continue
      adb shell pm grant "$PKG" "$perm" >>"$OUTDIR/run.log" 2>&1 || \
        log "$route grant failed (continuing): $perm"
    done
    IFS="$oldifs"
  fi
  # Discard dump (receiver resets counters), then the real run.
  dump_once "$OUTDIR/coverage/$route.discard.ec" || true
  rm -f "$OUTDIR/coverage/$route.discard.ec"
  timeout 600 python3 -I "$script" --package "$PKG" --log "$OUTDIR/steps/$route.log" \
    --outdir "$OUTDIR" --adb adb >>"$OUTDIR/run.log" 2>&1 < /dev/null
  rc=$?
  if [ -f "$OUTDIR/steps/$route.log" ]; then
    steps_done="$(wc -l < "$OUTDIR/steps/$route.log" | tr -d ' ')"
  else
    steps_done=0
  fi
  if [ "$rc" = 124 ]; then script_status="timeout";
  elif [ "$rc" = 0 ]; then script_status="ok";
  else script_status="failed_at_step_$((steps_done + 1))"; fi
  adb logcat -d > "$OUTDIR/logcat/$route.txt" 2>/dev/null || true
  adb logcat -c >/dev/null 2>&1 || true
  # Final dump + JaCoCo report + method lookup.
  reached="not_run"; error="coverage_missing"
  if dump_once "$OUTDIR/coverage/$route.ec"; then
    if jacoco_report "$OUTDIR/coverage/$route.ec" "$OUTDIR/coverage/$route.xml"; then
      hit="$(python3 -I "$DEVICE_DIR/jacoco_lookup.py" \
        "$ROOT/graphs/$APP/method_list.json" "$OUTDIR/coverage/$route.xml" \
        "$method" --tools "$ROOT/tools" 2>/dev/null || echo absent)"
      case "$hit" in
        reached) reached="yes"; error="" ;;
        not_reached) reached="no"; error="" ;;
        *) reached="no"; error="method_absent_in_report" ;;
      esac
    else
      error="jacoco_report_failed"
    fi
  fi
  echo "$APP,$route,$method,$edges,$reached,$script_status,$steps_done,$steps_total,$(csv_escape "$error"),$RUN_ID" >> "$OUTDIR/results.csv"
  log "$route $script_status reached=$reached steps=$steps_done/$steps_total $error"
done < "$OUTDIR/.routes.tsv"
rm -f "$OUTDIR/.routes.tsv"
log "done $APP; results in $OUTDIR/results.csv"
