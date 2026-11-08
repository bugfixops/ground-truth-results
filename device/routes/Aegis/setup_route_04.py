#!/usr/bin/env python3
# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# Per-route setup for new setup_route_04. Run-time generation only; nothing here is
# committed as a binary. Interface: --package --log --outdir --gen-dir (GEN_DIR
# fallback). No real emulator/adb run, no CI request, no drycheck pass claimed.

"""Aegis route_04 setup: generate twofas_backup.json at run time.

Run-time generated fixture for ROUTES.csv gen form
gen:twofas_backup.json -> /sdcard/Download/twofas_backup.json.
run_app.sh pushes the generated file to /sdcard/Download/ before
route_04 runs; this script itself pushes nothing to the device and
the generated file is never committed -- it lives only under the
run's out dir.

Format (TwoFASImporter.java): JSON with schemaVersion <= 4 and
"servicesEncrypted" =
base64(ciphertext-with-tag):base64(salt):base64(iv). The key is
PBKDF2WithHmacSHA256 (10000 iterations, 256 bit) over the typed
password "aegis-test-password", and the cipher is AES/GCM/NoPadding
(CryptoUtils.createDecryptCipher). The decrypted plaintext is a JSON
array of 2FAS service objects.

Usage (invoked by run_app.sh; all arguments optional except --gen-dir
when run standalone):
    setup_route_04.py --package <pkg> --log <log> --outdir <dir> \
        --gen-dir <dir>
"""

import argparse
import os
import sys
import hashlib
import json
import struct


# ---- Pure-Python AES (encrypt only) + modes, stdlib only ----
# Validated against the FIPS-197 AES-256 vector and pycryptodome
# (ECB block cross-checks, GCM ciphertext/tag cross-checks) during
# development. No third-party module is imported at run time.
_SBOX = [
0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76,
0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0,
0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15,
0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75,
0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84,
0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf,
0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8,
0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2,
0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73,
0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb,
0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79,
0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08,
0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a,
0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e,
0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf,
0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16]
_RCON = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1b,0x36,0x6c,0xd8,0xab,0x4d]


def _xtime(a):
    return ((a << 1) ^ 0x1b) & 0xff if a & 0x80 else (a << 1) & 0xff


def _mul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a = _xtime(a)
        b >>= 1
    return r


def _expand_key(key):
    nk = len(key) // 4
    nr = nk + 6
    w = [list(key[4 * i:4 * i + 4]) for i in range(nk)]
    for i in range(nk, 4 * (nr + 1)):
        t = list(w[i - 1])
        if i % nk == 0:
            t = [_SBOX[t[1]] ^ _RCON[i // nk - 1], _SBOX[t[2]], _SBOX[t[3]], _SBOX[t[0]]]
        elif nk > 6 and i % nk == 4:
            t = [_SBOX[b] for b in t]
        w.append([w[i - nk][j] ^ t[j] for j in range(4)])
    return w, nr


def _encrypt_block(key, block):
    w, nr = _expand_key(key)
    s = [[block[4 * c + r] for c in range(4)] for r in range(4)]

    def add_rk(rnd):
        for c in range(4):
            for r in range(4):
                s[r][c] ^= w[4 * rnd + c][r]

    add_rk(0)
    for rnd in range(1, nr + 1):
        for r in range(4):
            for c in range(4):
                s[r][c] = _SBOX[s[r][c]]
        for r in range(1, 4):
            row = [s[r][c] for c in range(4)]
            s[r] = [row[(c + r) % 4] for c in range(4)]
        if rnd < nr:
            for c in range(4):
                a = [s[r][c] for r in range(4)]
                s[0][c] = _mul(a[0], 2) ^ _mul(a[1], 3) ^ a[2] ^ a[3]
                s[1][c] = a[0] ^ _mul(a[1], 2) ^ _mul(a[2], 3) ^ a[3]
                s[2][c] = a[0] ^ a[1] ^ _mul(a[2], 2) ^ _mul(a[3], 3)
                s[3][c] = _mul(a[0], 3) ^ a[1] ^ a[2] ^ _mul(a[3], 2)
        add_rk(rnd)
    return bytes(s[r][c] for c in range(4) for r in range(4))


def _ghash(h, data):
    y = 0
    hint = int.from_bytes(h, "big")
    for off in range(0, len(data), 16):
        y ^= int.from_bytes(data[off:off + 16], "big")
        z = 0
        v = hint
        for i in range(128):
            if (y >> (127 - i)) & 1:
                z ^= v
            if v & 1:
                v = (v >> 1) ^ 0xe1000000000000000000000000000000
            else:
                v >>= 1
        y = z
    return y.to_bytes(16, "big")


def _gcm_encrypt(key, nonce12, plaintext):
    """AES-GCM encryption with a 12-byte nonce; returns (ct, tag)."""
    h = _encrypt_block(key, bytes(16))
    j0 = nonce12 + b"\x00\x00\x00\x01"
    out = bytearray()
    ctr = int.from_bytes(j0, "big")
    for off in range(0, len(plaintext), 16):
        ctr += 1
        ks = _encrypt_block(key, ctr.to_bytes(16, "big"))
        chunk = plaintext[off:off + 16]
        out += bytes(a ^ b for a, b in zip(chunk, ks))
    ct = bytes(out)

    def pad16(b):
        return b + bytes((-len(b)) % 16)

    s_data = pad16(b"") + pad16(ct) + (0).to_bytes(8, "big") + (len(ct) * 8).to_bytes(8, "big")
    tag = bytes(a ^ b for a, b in zip(_ghash(h, s_data), _encrypt_block(key, j0)))
    return ct, tag


def _cbc_encrypt(key, iv, plaintext):
    """AES-CBC encryption with PKCS#7 padding."""
    pad = 16 - (len(plaintext) % 16)
    data = plaintext + bytes([pad]) * pad
    out = bytearray()
    prev = iv
    for off in range(0, len(data), 16):
        block = bytes(a ^ b for a, b in zip(data[off:off + 16], prev))
        prev = _encrypt_block(key, block)
        out += prev
    return bytes(out)


import base64

PASSWORD = "aegis-test-password"


def build(gen_dir):
    salt = os.urandom(16)
    iv = os.urandom(12)
    key = hashlib.pbkdf2_hmac("sha256", PASSWORD.encode("utf-8"), salt, 10000, 32)
    services = [{
        "secret": "JBSWY3DPEHPK3PXP",
        "name": "TestIssuer",
        "otp": {
            "account": "testuser",
            "issuer": "TestIssuer",
            "digits": 6,
            "algorithm": "SHA1",
            "period": 30,
            "tokenType": "TOTP",
        },
    }]
    plaintext = json.dumps(services).encode("utf-8")
    ct, tag = _gcm_encrypt(key, iv, plaintext)
    enc = base64.b64encode(ct + tag).decode("ascii")
    obj = {
        "schemaVersion": 4,
        "servicesEncrypted": "%s:%s:%s" % (
            enc,
            base64.b64encode(salt).decode("ascii"),
            base64.b64encode(iv).decode("ascii")),
    }
    out_path = os.path.join(gen_dir, "twofas_backup.json")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(obj))
    return out_path, "2FAS schemaVersion 4, PBKDF2-SHA256, AES-GCM"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--package", default="")
    parser.add_argument("--log", default=None)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--gen-dir", default=None)
    args = parser.parse_args(argv)
    gen_dir = args.gen_dir or os.path.join(os.getcwd(), "gen")
    os.makedirs(gen_dir, exist_ok=True)
    out_path, detail = build(gen_dir)
    size = os.path.getsize(out_path)
    line = "generated %s (%d bytes, %s)\n" % (os.path.basename(out_path), size, detail)
    if args.log:
        with open(args.log, "a", encoding="utf-8") as f:
            f.write(line)
    sys.stdout.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
