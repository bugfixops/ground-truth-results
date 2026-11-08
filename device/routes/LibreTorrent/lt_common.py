"""Shared helpers for the LibreTorrent per-route setup scripts (Kiro, 2026-11-03).

Python 3 standard library plus adb only. Used by setup_route_NN.py; route scripts do not import it.

make_torrent(path): writes a small single-file .torrent (bencoded by hand) for a 32 KiB file
    "kiro_sample.bin" with two 16 KiB pieces and one tracker URL on a reserved, unresolvable
    host (RFC 6761 ".invalid"), so adding it needs no network and no peer. The data itself is
    never present: the torrent is added and listed, it is not downloaded.
add_torrent(adb, pkg, gen_dir, log): pushes that file to /sdcard/Download, grants storage
    (AddTorrentActivity reads the file:// source; MainActivity.java:177-178 asks for storage on
    every start while it is not granted), opens it with an explicit VIEW intent to
    AddTorrentActivity (AndroidManifest.xml:62-92) and taps the "Add torrent" menu item
    (res/menu/add_torrent.xml:5-8). It then goes HOME, so the route script starts from a launch.
"""

import hashlib
import os
import subprocess
import sys
import time

TORRENT_NAME = "kiro_sample.bin"
TORRENT_FILE = "kiro_sample.torrent"
TORRENT_DEVICE_PATH = "/sdcard/Download/" + TORRENT_FILE
PIECE = 16384
LENGTH = 2 * PIECE
ANNOUNCE = "udp://tracker.kiro.invalid:6969/announce"
ADD_TORRENT = "org.proninyaroslav.libretorrent.ui.addtorrent.AddTorrentActivity"
MAIN = "org.proninyaroslav.libretorrent.ui.main.MainActivity"
STORAGE = ("android.permission.READ_EXTERNAL_STORAGE", "android.permission.WRITE_EXTERNAL_STORAGE")


def _bencode(v):
    if isinstance(v, int):
        return b"i%de" % v
    if isinstance(v, str):
        v = v.encode("utf-8")
    if isinstance(v, bytes):
        return b"%d:%s" % (len(v), v)
    if isinstance(v, dict):
        out = b"d"
        for k in sorted(v):
            out += _bencode(k) + _bencode(v[k])
        return out + b"e"
    raise TypeError(type(v))


def make_torrent(path):
    data = b"\0" * LENGTH
    pieces = b"".join(hashlib.sha1(data[i:i + PIECE]).digest() for i in range(0, LENGTH, PIECE))
    info = {"length": LENGTH, "name": TORRENT_NAME, "piece length": PIECE, "pieces": pieces}
    with open(path, "wb") as f:
        f.write(_bencode({"announce": ANNOUNCE, "info": info}))
    return path


def fail(msg):
    print("setup FAILED: " + msg, file=sys.stderr)
    sys.exit(1)


def adb_run(adb, args, timeout=60):
    try:
        proc = subprocess.run([adb] + args, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        fail("adb %s timed out" % " ".join(args))
    if proc.returncode != 0:
        fail("adb %s failed (%s): %s" % (" ".join(args), proc.returncode, proc.stderr.strip()[:300]))
    return proc.stdout


def grant_storage(adb, pkg):
    for perm in STORAGE:
        adb_run(adb, ["shell", "pm", "grant", pkg, perm])


def add_torrent(adb, pkg, gen_dir, runner, log):
    local = make_torrent(os.path.join(gen_dir, TORRENT_FILE))
    adb_run(adb, ["push", local, TORRENT_DEVICE_PATH])
    log("pushed %s -> %s" % (local, TORRENT_DEVICE_PATH))
    grant_storage(adb, pkg)
    adb_run(adb, ["shell", "am", "start", "-W", "-a", "android.intent.action.VIEW",
                  "-d", "file://" + TORRENT_DEVICE_PATH, "-t", "application/x-bittorrent",
                  "-n", "%s/%s" % (pkg, ADD_TORRENT)])
    runner.wait_for(edge="setup", res_id="add_torrent_dialog_add_menu", timeout=30)
    runner.tap(edge="setup", res_id="add_torrent_dialog_add_menu")
    time.sleep(3)
    runner.key("KEYCODE_HOME", edge="setup")
    log("added torrent %s" % TORRENT_NAME)
