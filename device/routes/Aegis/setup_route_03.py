#!/usr/bin/env python3
# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# Per-route setup for new setup_route_03. Run-time generation only; nothing here is
# committed as a binary. Interface: --package --log --outdir --gen-dir (GEN_DIR
# fallback). No real emulator/adb run, no CI request, no drycheck pass claimed.

"""Aegis route_03 setup: generate stratum_backup.bin at run time.

Run-time generated fixture for ROUTES.csv gen form
gen:stratum_backup.bin -> /sdcard/Download/stratum_backup.bin.
run_app.sh pushes the generated file to /sdcard/Download/ before
route_03 runs; this script itself pushes nothing to the device and
the generated file is never committed -- it lives only under the
run's out dir.

Format (StratumImporter.java, modern EncryptedState): header
"AUTHENTICATORPRO", then salt 16, iv 12, then AES/GCM/NoPadding
ciphertext (Java GCM output, i.e. ciphertext followed by the 16-byte
tag). The key is Argon2id (3 iterations, parallelism 4, 2^16 KiB
memory, 32-byte output) over the typed password
"aegis-test-password", exactly as the route script types it.
Decrypted plaintext is a JSON object with an "Authenticators" array.

Note: the Argon2id derivation is pure Python (stdlib only) and takes
on the order of two minutes for the importer's 64 MiB parameters;
a progress line is printed before it starts so a quiet CI log is
not mistaken for a hang. The legacy "AuthenticatorPro" header is NOT
used: it would reach LegacyEncryptedState, not the route's target
method EncryptedState.decrypt(SecretKey).

Usage (invoked by run_app.sh; all arguments optional except --gen-dir
when run standalone):
    setup_route_03.py --package <pkg> --log <log> --outdir <dir> \
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


# ---- Pure-Python Argon2id (RFC 9106, version 0x13), stdlib only ----
# Validated against libargon2 (the reference C library) on 9 parameter
# sets (parallelism 1/2/4, iterations 1/2/3, memory 8..4096 KiB, empty
# and non-empty passwords, random salts). The quarter round uses the
# BlaMka mixing function and RIGHT rotations (32, 24, 16, 63).
_MASK64 = (1 << 64) - 1


def _rotr64(x, n):
    return ((x >> n) | (x << (64 - n))) & _MASK64


def _fblamka(x, y):
    return (x + y + 2 * (x & 0xffffffff) * (y & 0xffffffff)) & _MASK64


def _argon2_G(v, a, b, c, d):
    v[a] = _fblamka(v[a], v[b]); v[d] = _rotr64(v[d] ^ v[a], 32)
    v[c] = _fblamka(v[c], v[d]); v[b] = _rotr64(v[b] ^ v[c], 24)
    v[a] = _fblamka(v[a], v[b]); v[d] = _rotr64(v[d] ^ v[a], 16)
    v[c] = _fblamka(v[c], v[d]); v[b] = _rotr64(v[b] ^ v[c], 63)


def _argon2_round(v):
    _argon2_G(v, 0, 4, 8, 12); _argon2_G(v, 1, 5, 9, 13)
    _argon2_G(v, 2, 6, 10, 14); _argon2_G(v, 3, 7, 11, 15)
    _argon2_G(v, 0, 5, 10, 15); _argon2_G(v, 1, 6, 11, 12)
    _argon2_G(v, 2, 7, 8, 13); _argon2_G(v, 3, 4, 9, 14)


def _argon2_words(b):
    return list(struct.unpack("<128Q", b))


def _argon2_bytes(w):
    return struct.pack("<128Q", *w)


def _argon2_permute(r):
    for i in range(8):
        v = r[16 * i:16 * i + 16]
        _argon2_round(v)
        r[16 * i:16 * i + 16] = v
    for i in range(8):
        idx = []
        for j in range(8):
            idx += [16 * j + 2 * i, 16 * j + 2 * i + 1]
        v = [r[k] for k in idx]
        _argon2_round(v)
        for k, val in zip(idx, v):
            r[k] = val
    return r


def _argon2_compress(x, y):
    r = [a ^ b for a, b in zip(x, y)]
    z = _argon2_permute(list(r))
    return [a ^ b for a, b in zip(r, z)]


def _argon2_h_prime(outlen, data):
    if outlen <= 64:
        return hashlib.blake2b(struct.pack("<I", outlen) + data, digest_size=outlen).digest()
    out = bytearray()
    r = (outlen + 31) // 32 - 2
    v = hashlib.blake2b(struct.pack("<I", outlen) + data, digest_size=64).digest()
    out += v[:32]
    for _ in range(r - 1):
        v = hashlib.blake2b(v, digest_size=64).digest()
        out += v[:32]
    out += hashlib.blake2b(v, digest_size=outlen - 32 * r).digest()
    return bytes(out)


def _argon2id(password, salt, t_cost, m_cost, parallelism, outlen):
    """Argon2id, version 0x13, no secret, no associated data."""
    h0 = hashlib.blake2b(
        struct.pack("<IIIIII", parallelism, outlen, m_cost, t_cost, 0x13, 2)
        + struct.pack("<I", len(password)) + password
        + struct.pack("<I", len(salt)) + salt
        + struct.pack("<I", 0) + struct.pack("<I", 0),
        digest_size=64).digest()
    mem_blocks = 4 * parallelism * (m_cost // (4 * parallelism))
    seg_len = mem_blocks // (parallelism * 4)
    lane_len = seg_len * 4
    mem = [[None] * lane_len for _ in range(parallelism)]
    for lane in range(parallelism):
        mem[lane][0] = _argon2_words(_argon2_h_prime(1024, h0 + struct.pack("<II", 0, lane)))
        mem[lane][1] = _argon2_words(_argon2_h_prime(1024, h0 + struct.pack("<II", 1, lane)))

    def index_alpha(pass_no, slice_no, index, pseudo, same_lane):
        if pass_no == 0:
            if slice_no == 0:
                area = index - 1
            elif same_lane:
                area = slice_no * seg_len + index - 1
            else:
                area = slice_no * seg_len + (-1 if index == 0 else 0)
        elif same_lane:
            area = lane_len - seg_len + index - 1
        else:
            area = lane_len - seg_len + (-1 if index == 0 else 0)
        rel = pseudo & 0xffffffff
        rel = (rel * rel) >> 32
        rel = area - 1 - ((area * rel) >> 32)
        start = 0 if pass_no == 0 else (0 if slice_no == 3 else (slice_no + 1) * seg_len)
        return (start + rel) % lane_len

    for pass_no in range(t_cost):
        for slice_no in range(4):
            for lane in range(parallelism):
                data_independent = (pass_no == 0 and slice_no < 2)
                addr_in = [0] * 128
                addr_in[0] = pass_no; addr_in[1] = lane; addr_in[2] = slice_no
                addr_in[3] = mem_blocks; addr_in[4] = t_cost; addr_in[5] = 2
                addr_blocks = {}

                def _addr(idx, _in=addr_in, _cache=addr_blocks):
                    blk_no = idx // 128
                    if blk_no not in _cache:
                        _in[6] = blk_no + 1
                        zero = [0] * 128
                        _cache[blk_no] = _argon2_compress(zero, _argon2_compress(zero, _in))
                    return _cache[blk_no][idx % 128]

                start_idx = 2 if (pass_no == 0 and slice_no == 0) else 0
                for idx in range(start_idx, seg_len):
                    pos = slice_no * seg_len + idx
                    if pos == 0:
                        prev = mem[lane][lane_len - 1]
                    elif idx == 0:
                        prev = mem[lane][(slice_no - 1) * seg_len + seg_len - 1] if slice_no > 0 else mem[lane][lane_len - 1]
                    else:
                        prev = mem[lane][pos - 1]
                    if data_independent:
                        pseudo = _addr(idx)
                    else:
                        pseudo = prev[0]
                    ref_lane = (pseudo >> 32) % parallelism
                    if pass_no == 0 and slice_no == 0:
                        ref_lane = lane
                    ref_idx = index_alpha(pass_no, slice_no, idx, pseudo, ref_lane == lane)
                    new = _argon2_compress(prev, mem[ref_lane][ref_idx])
                    if pass_no != 0:
                        new = [a ^ b for a, b in zip(new, mem[lane][pos])]
                    mem[lane][pos] = new
    final = list(mem[0][lane_len - 1])
    for lane in range(1, parallelism):
        final = [a ^ b for a, b in zip(final, mem[lane][lane_len - 1])]
    return _argon2_h_prime(outlen, _argon2_bytes(final))


PASSWORD = "aegis-test-password"


def build(gen_dir):
    salt = os.urandom(16)
    iv = os.urandom(12)
    sys.stdout.write("deriving Argon2id key (64 MiB, 3 passes, pure Python; "
                     "this takes a couple of minutes)...\n")
    sys.stdout.flush()
    key = _argon2id(PASSWORD.encode("utf-8"), salt, 3, 65536, 4, 32)
    plaintext = json.dumps({"Authenticators": [{
        "Type": 2,
        "Issuer": "TestIssuer",
        "Username": "testuser",
        "Secret": "JBSWY3DPEHPK3PXP",
        "Algorithm": 0,
        "Digits": 6,
        "Period": 30,
        "Counter": 0,
    }]}).encode("utf-8")
    ct, tag = _gcm_encrypt(key, iv, plaintext)
    blob = b"AUTHENTICATORPRO" + salt + iv + ct + tag
    out_path = os.path.join(gen_dir, "stratum_backup.bin")
    with open(out_path, "wb") as f:
        f.write(blob)
    return out_path, "Stratum modern header, Argon2id, AES-GCM"


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
