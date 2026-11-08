# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# Per-route setup for new setup_route_15. Run-time generation only; nothing here is
# committed as a binary. Interface: --package --log --outdir --gen-dir (GEN_DIR
# fallback). No real emulator/adb run, no CI request, no drycheck pass claimed.
"""Per-route setup for Aegis route 15 (IconPackExistsException.getIconPack).

Generates device-icon-pack.zip: a ZIP with pack.json at the root (per IconPack.fromJson) plus one SVG icon. The route imports this file twice; the second import collides with the first and raises IconPackExistsException. The zip is built at run time with stdlib zipfile and never committed.

Interface: --package PKG --log LOG --outdir DIR --gen-dir DIR (GEN_DIR env fallback). Writes only into --gen-dir. Exits 1 on any failure, including a failed zip self-check."""

import argparse
import os
import sys


def _fail(msg):
    print("setup FAILED: " + msg, file=sys.stderr)
    sys.exit(1)


def _args():
    p = argparse.ArgumentParser()
    p.add_argument("--package", default="")
    p.add_argument("--log", default="")
    p.add_argument("--outdir", default="")
    p.add_argument("--gen-dir", default="")
    a = p.parse_args()
    gen_dir = a.gen_dir or os.environ.get("GEN_DIR", "")
    if not gen_dir:
        _fail("no --gen-dir and no GEN_DIR")
    return a, gen_dir


def _log(a, msg):
    line = msg + "\n"
    if a.log:
        try:
            with open(a.log, "a", encoding="utf-8") as f:
                f.write(line)
        except OSError:
            pass
    sys.stdout.write(line)
    sys.stdout.flush()


SVG_ICON = """<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48"><circle cx="24" cy="24" r="20" fill="#336699"/><text x="24" y="30" font-size="20" text-anchor="middle" fill="white">D</text></svg>
"""

# Fixed UUID so the pack identity is stable across runs; the route
# imports this same file twice, so the second import always collides
# with the first (that collision is route 15's target).
PACK_UUID = "11111111-2222-3333-4444-555555555555"


def main():
    import json
    import zipfile

    a, gen_dir = _args()
    os.makedirs(gen_dir, exist_ok=True)
    pack = {
        "uuid": PACK_UUID,
        "name": "Device Icon Pack",
        "version": 1,
        "icons": [{
            "filename": "device-icon.svg",
            "name": "Device Icon",
            "category": "general",
            "issuer": ["Device Issuer"],
        }],
    }
    out = os.path.join(gen_dir, "device-icon-pack.zip")
    try:
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.writestr("pack.json",
                        json.dumps(pack, indent=2).encode("utf-8"))
            zf.writestr("device-icon.svg", SVG_ICON.encode("utf-8"))
    except OSError as exc:
        _fail("write failed: %s" % exc)
    # Self-check: the zip must open and pack.json must parse with the
    # exact fields IconPack.fromJson requires.
    try:
        with zipfile.ZipFile(out, "r") as zf:
            names = zf.namelist()
            if "pack.json" not in names or "device-icon.svg" not in names:
                raise ValueError("missing entries: %s" % names)
            obj = json.loads(zf.read("pack.json").decode("utf-8"))
            if obj["uuid"] != PACK_UUID or obj["name"] != "Device Icon Pack":
                raise ValueError("pack.json identity mismatch")
            if obj["icons"][0]["filename"] != "device-icon.svg":
                raise ValueError("icon filename mismatch")
    except (OSError, ValueError, KeyError, IndexError) as exc:
        _fail("self-check failed: %s" % exc)
    _log(a, "generated device-icon-pack.zip (%d bytes) pack=%s"
         % (os.path.getsize(out), PACK_UUID))


if __name__ == "__main__":
    main()
