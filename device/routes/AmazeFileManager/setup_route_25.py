#!/usr/bin/env python3
"""AmazeFileManager per-route setup for route_25 (CompressedExplorerFragment).

Generates sample.zip at run time into the run's gen dir (see
--gen-dir). The zip contains exactly one text entry, as route_25's
header requires ("a minimal zip containing one text entry").
route_25's script pushes the generated file from $GEN_DIR (falling
back to its beside-script fixtures/ path for manual runs) to
/sdcard/Download/sample.zip, then sends the other-app VIEW intent
that launches MainActivity. This script itself pushes nothing to the
device and the generated file is never committed — it lives only
under the run's out dir.

Usage (invoked by run_app.sh):
    setup_route_25.py --package <pkg> --log <log> --outdir <dir> \
        --gen-dir <dir>
"""

import argparse
import os
import sys
import zipfile


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="AmazeFileManager route_25 setup: generate sample.zip")
    parser.add_argument("--package", default="")
    parser.add_argument("--log", default=None)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--gen-dir", default=None)
    args = parser.parse_args(argv)
    gen_dir = args.gen_dir or os.path.join(os.getcwd(), "gen")
    os.makedirs(gen_dir, exist_ok=True)
    out_path = os.path.join(gen_dir, "sample.zip")
    with zipfile.ZipFile(out_path, "w",
                         compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("entry.txt",
                    "AmazeFileManager route_25 fixture.\n"
                    "One text entry, opened via ACTION_VIEW.\n")
    size = os.path.getsize(out_path)
    line = "generated sample.zip (%d bytes, 1 entry: entry.txt)\n" % size
    if args.log:
        with open(args.log, "a", encoding="utf-8") as f:
            f.write(line)
    sys.stdout.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
