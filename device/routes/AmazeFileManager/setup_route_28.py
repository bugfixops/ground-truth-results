#!/usr/bin/env python3
"""AmazeFileManager per-route setup for route_28 (ExtractService).

Generates route28_archive.zip at run time into the run's gen dir
(see --gen-dir). The zip contains three 20 MiB entries of highly
compressible content, as route_28's header requires ("a zip holding
three ~20 MiB entries"). The content is deterministic text (numbered
filler lines), so the compressed file is small (~3 MB for 60 MiB
uncompressed) and generation takes about half a second, while the
decompressed size still exercises ExtractService's publish path.

LIVE-RUN CAVEAT: route_28's edge binds only if the viewer is opened
while extraction publishes the entries (route_28's script opens the
viewer immediately). Highly compressible content decompresses faster
than the original fixture, so the extraction window may differ from
the original run; if the real run misses the bind, the JaCoCo result
(not the comment log) decides, and the route is unclear, never wrong.
This script itself pushes nothing to the device and the generated
file is never committed — it lives only under the run's out dir.

Usage (invoked by run_app.sh):
    setup_route_28.py --package <pkg> --log <log> --outdir <dir> \
        --gen-dir <dir>
"""

import argparse
import os
import sys
import time
import zipfile

ENTRY_SIZE = 20 * 1024 * 1024  # 20 MiB per entry, as the route requires
ENTRY_NAMES = ("entry1.bin", "entry2.bin", "entry3.bin")


def _filler_block():
    # One block of numbered lines: compresses extremely well (the
    # line pattern repeats) while still being real text content.
    lines = []
    for i in range(1024):
        lines.append("AmazeFileManager route_28 archive filler line %04d.\n"
                     % i)
    return "".join(lines).encode("utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="AmazeFileManager route_28 setup: generate "
                    "route28_archive.zip")
    parser.add_argument("--package", default="")
    parser.add_argument("--log", default=None)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--gen-dir", default=None)
    args = parser.parse_args(argv)
    gen_dir = args.gen_dir or os.path.join(os.getcwd(), "gen")
    os.makedirs(gen_dir, exist_ok=True)
    out_path = os.path.join(gen_dir, "route28_archive.zip")
    block = _filler_block()
    started = time.time()
    with zipfile.ZipFile(out_path, "w",
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for name in ENTRY_NAMES:
            with zf.open(name, "w") as entry:
                written = 0
                while written < ENTRY_SIZE:
                    chunk = block[:ENTRY_SIZE - written]
                    entry.write(chunk)
                    written += len(chunk)
    elapsed = time.time() - started
    size = os.path.getsize(out_path)
    line = ("generated route28_archive.zip (%d bytes compressed, "
            "3 x 20 MiB entries, %.1fs)\n" % (size, elapsed))
    if args.log:
        with open(args.log, "a", encoding="utf-8") as f:
            f.write(line)
    sys.stdout.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
