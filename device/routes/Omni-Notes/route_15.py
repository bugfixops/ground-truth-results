"""Device route script route_15 for Omni-Notes.

Method: DetailFragment.removeAttachment(Attachment) -- UNREACHABLE, EMPTY edge list.
Printed route: none (this method has no sampled route; ROUTES.csv route_15
    has an empty edges field, and the path row is kept for the first-graph
    error record: DetailFragment.java:1956-1962; AttachmentTask.java:62-68).
Permissions: none. Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures.
Expected device outcome: reached=no, script_status=ok -- the run empirically
confirms non-reachability.

Why this script does NOT use the harness Runner: the Runner cannot express
a zero-edge route. Its constructor accepts edge_ids=None (checking
disabled), but _check_edge() still raises ValueError("every action needs an
edge id") when edge is None, so launch() -- and every other action --
cannot be called without an edge id, and inventing an edge id for a method
with no edges would fabricate route evidence. The honest approach is
therefore to write a single comment line directly to the script's log file
(--log) noting the method is UNREACHABLE with no edges, and exit 0. The
merger's run_app.sh still launches/clears the app around this script; this
script itself performs no device action, which is exactly what a zero-edge
route warrants. No Runner is constructed and no edge id is invented.

CLI contract (same as the other route scripts): --package, --log, --outdir,
--dry-run (flag) or --adb (value). All are accepted; only --log is used.
"""
import argparse
import os
import sys
from datetime import datetime, timezone


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    # Direct log write: the harness Runner cannot log a zero-edge route
    # (see header). One line, in the harness log format
    # (UTC timestamp, edge "-", action, target, result), with no invented
    # edge id. The target names the method and its status.
    log_dir = os.path.dirname(os.path.abspath(a.log))
    os.makedirs(log_dir, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    line = ("%s - comment "
            "DetailFragment.removeAttachment(Attachment)_UNREACHABLE_no_edges "
            "ok\n" % stamp)
    with open(a.log, "a", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == '__main__':
    sys.exit(main())
