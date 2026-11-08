#!/usr/bin/env python3
"""Build per-app device results from a committed run folder (brief D6).

Usage: python3 -I device/compare.py <results_dir> [--out-root R]
  <results_dir>  a committed device/results/<run>/ (or device/dryrun/
                 folder) holding <App>/results.csv files as written by
                 device/collect.py.
  --out-root R   directory holding <App>/ subdirs to write into
                 (default: <repo-root>/graphs).

For each app with a results.csv, writes <out-root>/<App>/device/
results.csv with columns route,method,edges,reached,script_status,
run,script, where run is the input directory basename and script is
<route>.py. Unscriptable rows are kept (reached=not_run) so D7 can
emit unclear DEVICE rows for them. Writes NO other files and never
touches a real graphs/ tree when --out-root points elsewhere (the
test path). Real runs in this phase write nothing: D6 output lands
only after a real device run exists.
"""

import csv
import os
import sys

OUT_COLUMNS = ["route", "method", "edges", "reached", "script_status",
               "run", "script"]


def compare(results_dir, out_root):
    run = os.path.basename(os.path.normpath(results_dir))
    written = {}
    for app in sorted(os.listdir(results_dir)):
        src = os.path.join(results_dir, app, "results.csv")
        if not os.path.isfile(src):
            continue
        with open(src, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        dest_dir = os.path.join(out_root, app, "device")
        os.makedirs(dest_dir, exist_ok=True)
        dest = os.path.join(dest_dir, "results.csv")
        with open(dest, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=OUT_COLUMNS)
            writer.writeheader()
            for r in rows:
                writer.writerow({
                    "route": r["route"],
                    "method": r["method"],
                    "edges": r["edges"],
                    "reached": r["reached"],
                    "script_status": r["script_status"],
                    "run": run,
                    "script": r["route"] + ".py",
                })
        written[app] = len(rows)
    return run, written


def main(argv):
    if not argv:
        sys.stderr.write("usage: compare.py <results_dir> [--out-root R]\n")
        return 2
    results_dir = argv[0]
    out_root = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "graphs")
    i = 1
    while i < len(argv):
        if argv[i] == "--out-root" and i + 1 < len(argv):
            out_root = argv[i + 1]
            i += 1
        else:
            sys.stderr.write("unknown argument: %s\n" % argv[i])
            return 2
        i += 1
    run, written = compare(results_dir, out_root)
    for app, n in written.items():
        print("%s: %d rows -> %s" % (app, n, os.path.join(
            out_root, app, "device", "results.csv")))
    print("run=%s apps=%d" % (run, len(written)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
