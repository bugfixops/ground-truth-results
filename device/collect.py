#!/usr/bin/env python3
"""Collect downloaded device artifacts into committed text only (brief D5).

Usage: python3 -I device/collect.py <collected_dir> <dest_dir>

The workflow downloads artifacts device-<App>/ into <collected_dir>.
For each artifact this writes ONLY small text files under
<dest_dir>/<App>/: results.csv, run.log, steps/route_NN.log, and for
dry runs dryrun_report.txt. Screenshots (.png), UI dumps (.xml),
coverage files, and anything else are NEVER copied (they stay in the
30-day artifacts). Any copied log over 5 MB is truncated with a marker.
Also writes <dest_dir>/SUMMARY.md: one table per app with routes,
reached, not reached, script failed, unscriptable (from results.csv),
or PASS and FAIL (from dryrun_report.txt). A row can count in both
"not reached" and "script failed" (a failed script usually also did
not reach its method); the columns are per-column counts, not a
partition.
"""

import csv
import os
import sys

MAX_LOG_BYTES = 5 * 1024 * 1024
ALLOWLIST = {"results.csv", "run.log", "dryrun_report.txt"}


def copy_capped(src, dst):
    """Copy a text file, truncating over MAX_LOG_BYTES with a marker."""
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    size = os.path.getsize(src)
    with open(src, "rb") as f_in, open(dst, "wb") as f_out:
        if size <= MAX_LOG_BYTES:
            f_out.write(f_in.read())
        else:
            f_out.write(f_in.read(MAX_LOG_BYTES))
            f_out.write(("\n... [truncated by device/collect.py: "
                         "original %d bytes]\n" % size).encode("utf-8"))


def collect_app(artifact_dir, dest_app_dir):
    """Copy allowlisted files; returns (copied, skipped) file counts."""
    copied, skipped = 0, 0
    for name in ALLOWLIST:
        src = os.path.join(artifact_dir, name)
        if os.path.isfile(src):
            copy_capped(src, os.path.join(dest_app_dir, name))
            copied += 1
    steps_src = os.path.join(artifact_dir, "steps")
    if os.path.isdir(steps_src):
        for name in sorted(os.listdir(steps_src)):
            src = os.path.join(steps_src, name)
            if os.path.isfile(src) and name.endswith(".log"):
                copy_capped(src, os.path.join(dest_app_dir, "steps", name))
                copied += 1
            else:
                skipped += 1
    for root, _dirs, files in os.walk(artifact_dir):
        rel = os.path.relpath(root, artifact_dir)
        if rel == ".":
            for name in files:
                if name not in ALLOWLIST and name != "run.log":
                    skipped += 1
        elif rel == "steps":
            continue
        else:
            skipped += len(files)
    return copied, skipped


def summarize_results(path):
    """(routes, reached, not_reached, script_failed, unscriptable)."""
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    reached = sum(1 for r in rows if r["reached"] == "yes")
    not_reached = sum(1 for r in rows if r["reached"] == "no")
    failed = sum(1 for r in rows
                 if r["script_status"].startswith("failed") or
                 r["script_status"] == "timeout")
    unscript = sum(1 for r in rows if r["script_status"] == "unscriptable")
    return len(rows), reached, not_reached, failed, unscript


def summarize_dryrun(path):
    """(n_pass, n_fail) from a dryrun_report.txt (ignores final line)."""
    n_pass = n_fail = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or ": " in line and "PASS," in line:
                continue
            if line.endswith(" PASS"):
                n_pass += 1
            elif " FAIL " in line or line.endswith(" FAIL"):
                n_fail += 1
    return n_pass, n_fail


def main(argv):
    if len(argv) != 2:
        sys.stderr.write("usage: collect.py <collected_dir> <dest_dir>\n")
        return 2
    collected, dest = argv[0], argv[1]
    os.makedirs(dest, exist_ok=True)
    sections = []
    apps = []
    if os.path.isdir(collected):
        for name in sorted(os.listdir(collected)):
            artifact = os.path.join(collected, name)
            if not os.path.isdir(artifact) or not name.startswith("device-"):
                continue
            app = name[len("device-"):]
            dest_app = os.path.join(dest, app)
            copied, skipped = collect_app(artifact, dest_app)
            apps.append(app)
            lines = ["## %s\n" % app,
                     "copied %d text file(s), skipped %d non-text/other file(s).\n" % (copied, skipped)]
            res = os.path.join(dest_app, "results.csv")
            dry = os.path.join(dest_app, "dryrun_report.txt")
            if os.path.isfile(res):
                routes, reached, notreached, failed, unscript = \
                    summarize_results(res)
                lines.append("| routes | reached | not reached | script failed | unscriptable |")
                lines.append("|---|---|---|---|---|")
                lines.append("| %d | %d | %d | %d | %d |" % (
                    routes, reached, notreached, failed, unscript))
            if os.path.isfile(dry):
                n_pass, n_fail = summarize_dryrun(dry)
                lines.append("| PASS | FAIL |")
                lines.append("|---|---|")
                lines.append("| %d | %d |" % (n_pass, n_fail))
            if not os.path.isfile(res) and not os.path.isfile(dry):
                lines.append("no results.csv or dryrun_report.txt in artifact.\n")
            sections.append("\n".join(lines))
    with open(os.path.join(dest, "SUMMARY.md"), "w", encoding="utf-8") as f:
        f.write("# Device collection summary\n\n")
        if not apps:
            f.write("No device-* artifacts found.\n")
        else:
            f.write("Apps: %s\n\n" % ", ".join(apps))
            f.write("\n\n".join(sections) + "\n")
    print("collected %d app(s): %s" % (len(apps), ", ".join(apps)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
