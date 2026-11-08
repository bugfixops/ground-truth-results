#!/usr/bin/env python3
"""AmazeFileManager per-route setup for route_04 (GlideRequests.load).

Generates route04.zip at run time into the run's gen dir (see
--gen-dir). The zip contains exactly one entry, sub/note.txt, as
route_04's header requires ("a folder entry named 'sub' containing
at least one file"). run_app.sh pushes the generated file to
/sdcard/Download/route04.zip before route_04 runs (see the route's
ROUTES.csv fixture cell, gen: form); this script itself pushes
nothing to the device and the generated file is never committed —
it lives only under the run's out dir.

Usage (invoked by run_app.sh; all arguments optional except --gen-dir
when run standalone):
    setup_route_04.py --package <pkg> --log <log> --outdir <dir> \
        --gen-dir <dir>
"""

import argparse
import os
import sys
import zipfile


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="AmazeFileManager route_04 setup: generate route04.zip")
    parser.add_argument("--package", default="")
    parser.add_argument("--log", default=None)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--gen-dir", default=None)
    args = parser.parse_args(argv)
    gen_dir = args.gen_dir or os.path.join(os.getcwd(), "gen")
    os.makedirs(gen_dir, exist_ok=True)
    out_path = os.path.join(gen_dir, "route04.zip")
    with zipfile.ZipFile(out_path, "w",
                         compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("sub/note.txt",
                    "AmazeFileManager route_04 fixture.\n"
                    "Opened by the archive viewer via ACTION_VIEW.\n")
    size = os.path.getsize(out_path)
    line = "generated route04.zip (%d bytes, 1 entry: sub/note.txt)\n" % size
    if args.log:
        with open(args.log, "a", encoding="utf-8") as f:
            f.write(line)
    sys.stdout.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
