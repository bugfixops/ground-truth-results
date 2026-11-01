#!/usr/bin/env python3
"""NEW LOCAL TOOL — NOT a branch file. DRAFT, Aegis scope only.

make_verification.py: build graphs/<App>/verification.csv from an
individually-checked-rows input, and inject the matching `verification`
object into the schema-2 trigger-graph JSON that tools/gen_readme_v2.py
reads.

Status of this file: written 2026-11-01 by Stream C phase-2 leaf B as a
LOCAL draft. It has NOT been copied to tools/ on any branch, NOT run to
produce a final Aegis verification.csv (its inputs do not exist yet — see
missing_inputs_report.md in this same directory), and NOT merged anywhere.
The coordinator copies it to tools/ only when the final inputs exist and
the run below is performed on a full checkout.

Why this tool exists (grounded, not guessed):
- graphs/Aegis/verification.csv does not exist on branch work-2026-10-31
  (phase-1 leaf: absent from both graphs/Aegis/ and graphs/Aegis/out/
  listings), and tools/make_verification.py does not exist either
  (phase-1 leaf: tools/ lists 52 files, none of that name).
- tools/gen_readme_v2.py (140 lines, SHA 15337a8675cde3a08fe8722b238764a577e8303c,
  read via the GitHub connector 2026-11-01) reads verification counts NOT
  from verification.csv directly but from the trigger-graph JSON's
  `verification` object (`ver = g.get('verification') or {}`); if that
  object is absent it prints "No verification log yet". So writing the CSV
  alone does NOT finish the v2 readme — the JSON injection below is
  required, and this tool does both from one validated input so the two
  can never disagree.
- gen_readme_v2.py aggregates exactly three types — `label`, `edge`,
  `path` — and prints, per type, Rows = v['checked'] + v['unclear'].
  That arithmetic RESOLVES the phase-1 open question (§4c): the JSON
  `checked` field must EXCLUDE unclear rows (checked = correct +
  errors_found), otherwise the published Rows figure double-counts.
  This tool enforces that identity with an assertion on every run.
- gen_readme_v2.py indexes `ver[t]` for all three types unconditionally,
  so the injected object always carries all three types, even when one
  has zero rows.

Row plan (from phase-1 logs_gap.md §4, confirmed against the script):
- CSV header, exactly: type,item,result,confirmed_by,ref,edges,note
- `type` is label, edge, or path — nothing else. No summary/count rows:
  counts are derived by aggregating these rows, so the CSV row count and
  the published table agree.
- `label` rows: one row per method label INDIVIDUALLY checked. `item` is
  the method (Class.method, overloads as Class.method(Type,Type)). A
  label row may claim `correct` only if its best route was read step by
  step against source; a label whose route was not read is not a row at
  all ("The rows are the items that were individually checked, not a
  random sample of all labels." — gen_readme_v2.py).
- `edge` rows: one row per framework claim or other edge claim read
  against source. `item` is the edge id (edge ids are a hash of the edge
  content, so they stay stable when other edges change — gen_readme_v2.py
  JSON-shape note). `edges` repeats the id when omitted.
- `path` rows: one row per sampled route read step by step in the FINAL
  sample (not round 7). `item` is the route's target method + sample id.
  `edges` is the route's edge ids in order (required for path rows).
  `result` is `correct` only if every step was read and no ERROR step
  remains; `error_found` if any step is ERROR; `unclear` if any step is
  UNCLEAR and none is ERROR.
- `result` values in the CSV are: correct, error_found, unclear. The
  JSON aggregation maps error_found -> errors_found.
- `confirmed_by` takes ONLY SOURCE or INFERRED. Anything else — DYN,
  FW-MEMORY, UNVERIFIED, empty — is rejected and the run fails with a
  non-zero exit before anything is written. No exceptions.
- `ref` is required on every row: the where, a file:line citation
  (app source, fw_src, or graph edge line).
- `edges` in the CSV is a ';'-joined list; it is empty for pure label
  rows.

Input format (--rows): a JSON list of row objects, each with keys
type, item, result, confirmed_by, ref, and optional edges (list of edge
ids, or a ';'-joined string) and note (string). Example (ILLUSTRATIVE
ONLY — these are not Aegis data and must never be shipped as rows):

    [{"type": "label", "item": "ExampleClass.exampleMethod",
      "result": "correct", "confirmed_by": "SOURCE",
      "ref": "app/src/main/java/com/example/ExampleClass.java:10-20",
      "edges": [], "note": "best route read step by step"},
     {"type": "path", "item": "ExampleClass.exampleMethod (final sample, seed TO-VERIFY)",
      "result": "unclear", "confirmed_by": "INFERRED",
      "ref": "graphs/Aegis/scratch/route_check_final/ExampleClass_exampleMethod.txt",
      "edges": ["E00000000"], "note": "one step UNCLEAR under D2"}]

The rows file is produced by the final step-by-step route-check phase;
this tool never invents rows, never types in counts, and never reads a
label universe to pad the CSV. If --rows is missing, the tool fails and
names it as the missing input — it does not emit an empty "final" CSV.

Usage (from a full checkout, Aegis):
    python3 -I tools/make_verification.py --app Aegis \\
        --rows graphs/Aegis/scratch/verification_rows_final.json \\
        --graph-json graphs/Aegis/out/aegis_trigger_graph.json \\
        --csv-out graphs/Aegis/verification.csv \\
        [--json-out graphs/Aegis/out/aegis_trigger_graph.json]
    --json-out defaults to overwriting --graph-json in place, after
    writing a <path>.bak copy. Use --dry-run to validate and print the
    aggregation without writing anything.

Exit codes: 0 on success; 1 on any missing input, validation failure,
or schema mismatch. A failed run writes nothing.
"""

import argparse
import csv
import json
import os
import sys

HEADER = ["type", "item", "result", "confirmed_by", "ref", "edges", "note"]
TYPES = ("label", "edge", "path")
RESULTS = ("correct", "error_found", "unclear")
CONFIRMED_BY = ("SOURCE", "INFERRED")


def fail(msg):
    print("make_verification: ERROR: %s" % msg, file=sys.stderr)
    raise SystemExit(1)


def load_rows(path):
    if not os.path.isfile(path):
        fail("rows input missing: %s (produce it from the final "
             "step-by-step route checks; refusing to emit an empty "
             "or invented verification.csv)" % path)
    try:
        with open(path, encoding="utf-8") as f:
            rows = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        fail("cannot read rows input %s: %s" % (path, e))
    if not isinstance(rows, list) or not rows:
        fail("rows input %s must be a non-empty JSON list of row objects"
             % path)
    return rows


def normalise_rows(raw):
    seen = set()
    rows = []
    for i, r in enumerate(raw):
        if not isinstance(r, dict):
            fail("row %d is not an object" % i)
        t = r.get("type")
        if t not in TYPES:
            fail("row %d: type %r not in %s" % (i, t, list(TYPES)))
        item = r.get("item")
        if not isinstance(item, str) or not item.strip():
            fail("row %d: item must be a non-empty string" % i)
        key = (t, item)
        if key in seen:
            fail("row %d: duplicate row for type=%s item=%s "
                 "(one row per checked item)" % (i, t, item))
        seen.add(key)
        result = r.get("result")
        if result not in RESULTS:
            fail("row %d: result %r not in %s" % (i, result, list(RESULTS)))
        cb = r.get("confirmed_by")
        if cb not in CONFIRMED_BY:
            fail("row %d: confirmed_by %r rejected (only SOURCE or "
                 "INFERRED; never DYN, FW-MEMORY, or UNVERIFIED)"
                 % (i, cb))
        ref = r.get("ref")
        if not isinstance(ref, str) or not ref.strip():
            fail("row %d: ref is required (file:line citation)" % i)
        edges = r.get("edges", [])
        if isinstance(edges, str):
            edges = [e for e in edges.split(";") if e.strip()]
        if not isinstance(edges, list) or not all(
                isinstance(e, str) and e.strip() for e in edges):
            fail("row %d: edges must be a list of edge ids" % i)
        if t == "label" and edges:
            fail("row %d: label rows carry no edges (edges must be empty)"
                 % i)
        if t == "path" and not edges:
            fail("row %d: path rows require the route edge ids in order"
                 % i)
        if t == "edge" and not edges:
            edges = [item]
        note = r.get("note", "")
        if not isinstance(note, str):
            fail("row %d: note must be a string" % i)
        rows.append({
            "type": t, "item": item, "result": result,
            "confirmed_by": cb, "ref": ref,
            "edges": ";".join(edges), "note": note,
        })
    return rows


def aggregate(rows):
    ver = {}
    for t in TYPES:
        subset = [r for r in rows if r["type"] == t]
        correct = sum(1 for r in subset if r["result"] == "correct")
        errors = sum(1 for r in subset if r["result"] == "error_found")
        unclear = sum(1 for r in subset if r["result"] == "unclear")
        # gen_readme_v2.py prints Rows = checked + unclear, so checked
        # MUST exclude unclear rows or the published table double-counts.
        checked = correct + errors
        assert checked + unclear == len(subset)
        ver[t] = {"checked": checked, "correct": correct,
                  "errors_found": errors, "unclear": unclear}
    return ver


def load_graph(path):
    if not os.path.isfile(path):
        fail("trigger-graph JSON missing: %s (run the final build first; "
             "the verification object is injected into this file)" % path)
    try:
        with open(path, encoding="utf-8") as f:
            g = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        fail("cannot read trigger-graph JSON %s: %s" % (path, e))
    if g.get("schema") != 2:
        fail("trigger-graph JSON %s is not schema 2 (gen_readme_v2.py "
             "requires schema 2)" % path)
    return g


def main(argv):
    ap = argparse.ArgumentParser(
        description="Build verification.csv and inject its counts into "
                    "the schema-2 trigger-graph JSON for gen_readme_v2.py.")
    ap.add_argument("--app", required=True)
    ap.add_argument("--rows", required=True,
                    help="JSON list of individually checked rows")
    ap.add_argument("--graph-json", required=True,
                    help="schema-2 trigger-graph JSON to inject into")
    ap.add_argument("--csv-out", required=True)
    ap.add_argument("--json-out", default=None,
                    help="where to write the updated JSON "
                         "(default: overwrite --graph-json in place, "
                         "after a .bak copy)")
    ap.add_argument("--dry-run", action="store_true",
                    help="validate and print the aggregation; write nothing")
    args = ap.parse_args(argv)

    rows = normalise_rows(load_rows(args.rows))
    ver = aggregate(rows)
    g = load_graph(args.graph_json)

    total = len(rows)
    print("app: %s" % args.app)
    for t in TYPES:
        v = ver[t]
        print("%s: rows=%d correct=%d errors_found=%d unclear=%d "
              "checked=%d (published Rows=%d)"
              % (t, v["checked"] + v["unclear"], v["correct"],
                 v["errors_found"], v["unclear"], v["checked"],
                 v["checked"] + v["unclear"]))
    print("total rows: %d" % total)
    if args.dry_run:
        print("dry run: wrote nothing")
        return 0

    g["verification"] = ver
    json_out = args.json_out or args.graph_json
    if os.path.abspath(json_out) == os.path.abspath(args.graph_json):
        bak = args.graph_json + ".bak"
        with open(args.graph_json, encoding="utf-8") as f:
            orig = f.read()
        with open(bak, "w", encoding="utf-8") as f:
            f.write(orig)
        print("backup: %s" % bak)
    with open(json_out, "w", encoding="utf-8") as f:
        json.dump(g, f, indent=2, sort_keys=True)
        f.write("\n")
    print("wrote %s (verification object injected)" % json_out)
    csv_dir = os.path.dirname(os.path.abspath(args.csv_out))
    os.makedirs(csv_dir, exist_ok=True)
    with open(args.csv_out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=HEADER)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print("wrote %s (%d rows)" % (args.csv_out, total))
    print("next: run tools/gen_readme_v2.py %s for the final out/README.md"
          % args.app)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
