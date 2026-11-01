# AnkiDroid readme notes — DRAFT ONLY

This draft was NOT produced by running tools/gen_readme_v2.py (that tool
needs out/ankidroid_trigger_graph.json, which could not be fetched; its run
fails with IndexError — see scratch/attempted_runs.txt). It will be
finalised by the agent with a full checkout, after the sample is drawn and
judged. Headings are the required five, in order.

## What the re-audit changed (compared with the schema 1 graph)

Labels and routes for 4,186 methods were built by hand from printed source
in the convert run (branch build 205: 3,275 REACHABLE, 911 UNREACHABLE,
errors 0, warnings 0 — branch output, not a run by this leaf). Schema 1
DEAD / FRAMEWORK_ONLY verdicts were replaced by UNREACHABLE entries with a
kind, a reason, and a source reference; gates were structured into ENV and
STATE kinds; edge classes distinguish explicit, standard, and non_standard
links. No change was made to any label by this leaf tonight.

## How the checked paths were chosen

Not yet done by this leaf. The intended sample is
python3 -I tools/verify_sample.py AnkiDroid 30 20261025 (stratified: NONSTD,
INFERRED, STATE, ENV, LONG, PLAIN), every step printed and judged against
its cited lines, wrong routes fixed from printed source, final sample
redrawn after the last fix. Tonight's source judging covered only the open
items (Card.toString, EasySSLSocketFactory equals/hashCode, the
Hooks.runFilter registry edge, Compat API-27 dispatch) — see
route_judging_note.md. No sample table and no error rate exist yet.

## What waits for a device (API 27)

Device replay of the sampled paths (DEVICE confirmation), delivery claims
between apps or through the launcher, IME behaviour, and replaying any
route whose step rests on a framework or library dispatch not printed from
fw_src. The EasySSL library question (DECISIONS.md decision A) and the
targetSdk framework surface (decision B) also wait for printed evidence,
not for a device. No emulator, adb, APK, or device run was done tonight.

## Hazard candidates (from reading the code, not reproduced)

Carried from the convert run's notes, not re-verified tonight: Finder
_findDupes (split(",", 1) returning one element, so a length check always
returns null); CardBrowser.closeCardBrowser(int) always throwing
NullPointerException (line ~1130); Storage.java:357 holding malformed SQL
(not executed). None of these was reproduced, and none changes a label:
the methods are entered, so they stay REACHABLE where labelled so.

## Limits

- The branch graph (graph_def.py, auto_calls.json, methods.csv,
  trigger_graph.json) could not be fetched through the connector (display
  size limit); all counts quoted here are branch build 205 output, verified
  by blob SHA, not this leaf's own build.
- Library and generated-code steps stay INFERRED where their source was not
  read (Apache HttpClient, androidx, ORMLite, and similar); framework claims
  cite only printed fw_src lines or are marked INFERRED with "source not
  read".
- The Card.toString APE contradiction and the EasySSL library dispatch are
  open (see DECISIONS.md); the Hooks.runFilter MG943 gate attachment and
  the targetSdk pre-tick grep are also open at merge time.
