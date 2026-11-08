# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# Per-route setup for new setup_route_14. Run-time generation only; nothing here is
# committed as a binary. Interface: --package --log --outdir --gen-dir (GEN_DIR
# fallback). No real emulator/adb run, no CI request, no drycheck pass claimed.
"""Per-route setup for Aegis route 14 (AegisImporter$DecryptedState.getCredentials).

Generates aegis-vault.json: a password-protected Aegis vault file (password 'testpassword') that the route imports through the system document picker. Crypto is pure-stdlib AES-256-GCM (embedded below, verified against pycryptodome) with scrypt key derivation (N=32768, r=8, p=1) exactly as the app derives it. The file is generated at run time and never committed.

Interface: --package PKG --log LOG --outdir DIR --gen-dir DIR (GEN_DIR env fallback). Writes only into --gen-dir. Exits 1 on any failure, including a failed decrypt self-check."""

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

"""Pure-Python AES-256 + GCM (NIST SP 800-38D), standard library only.

The S-box is computed from first principles (GF(2^8) inverse + affine
transform), not copied from a table, so this module has no lookup data
to mistype. Verified against pycryptodome in test_crypto.py.
"""

# --- GF(2^8), polynomial 0x11B ---
def _gf_mul(a, b):
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        hi = a & 0x80
        a = (a << 1) & 0xFF
        if hi:
            a ^= 0x1B
        b >>= 1
    return p


def _gf_inv(a):
    if a == 0:
        return 0
    # a^254 by square-and-multiply
    result = 1
    base, exp = a, 254
    while exp:
        if exp & 1:
            result = _gf_mul(result, base)
        base = _gf_mul(base, base)
        exp >>= 1
    return result


def _rotl8(x, n):
    return ((x << n) | (x >> (8 - n))) & 0xFF


_SBOX = []
for _x in range(256):
    _inv = _gf_inv(_x)
    _s = _inv ^ _rotl8(_inv, 1) ^ _rotl8(_inv, 2) ^ _rotl8(_inv, 3) ^ _rotl8(_inv, 4) ^ 0x63
    _SBOX.append(_s & 0xFF)
_INVSBOX = [0] * 256
for _i, _v in enumerate(_SBOX):
    _INVSBOX[_v] = _i

_RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36,
         0x6C, 0xD8, 0xAB, 0x4D]


def _expand_key(key):
    # key: 32 bytes -> 15 round keys of 16 bytes (AES-256, Nk=8, Nr=14)
    w = [list(key[4 * i:4 * i + 4]) for i in range(8)]
    for i in range(8, 60):
        temp = list(w[i - 1])
        if i % 8 == 0:
            temp = [_SBOX[temp[1]] ^ _RCON[i // 8 - 1], _SBOX[temp[2]],
                    _SBOX[temp[3]], _SBOX[temp[0]]]
        elif i % 8 == 4:
            temp = [_SBOX[b] for b in temp]
        w.append([w[i - 8][j] ^ temp[j] for j in range(4)])
    rounds = []
    for r in range(15):
        rk = []
        for c in range(4):
            rk.extend(w[4 * r + c])
        rounds.append(rk)
    return rounds


def _add_rk(state, rk):
    return [s ^ k for s, k in zip(state, rk)]


def _sub(state):
    return [_SBOX[b] for b in state]


def _shift_rows(state):
    # state is column-major: index = 4*col + row
    out = [0] * 16
    for r in range(4):
        for c in range(4):
            out[4 * c + r] = state[4 * ((c + r) % 4) + r]
    return out


def _mix_col(col):
    a0, a1, a2, a3 = col
    return [
        _gf_mul(a0, 2) ^ _gf_mul(a1, 3) ^ a2 ^ a3,
        a0 ^ _gf_mul(a1, 2) ^ _gf_mul(a2, 3) ^ a3,
        a0 ^ a1 ^ _gf_mul(a2, 2) ^ _gf_mul(a3, 3),
        _gf_mul(a0, 3) ^ a1 ^ a2 ^ _gf_mul(a3, 2),
    ]


def _mix_cols(state):
    out = [0] * 16
    for c in range(4):
        mixed = _mix_col(state[4 * c:4 * c + 4])
        out[4 * c:4 * c + 4] = mixed
    return out


def aes256_encrypt_block(key, block):
    rounds = _expand_key(key)
    state = list(block)
    state = _add_rk(state, rounds[0])
    for r in range(1, 14):
        state = _sub(state)
        state = _shift_rows(state)
        state = _mix_cols(state)
        state = _add_rk(state, rounds[r])
    state = _sub(state)
    state = _shift_rows(state)
    state = _add_rk(state, rounds[14])
    return bytes(state)


# --- GCM ---
def _gf128_mul(x, y):
    # x, y: 16-byte strings, GCM bit convention (bit-reflected)
    x_int = int.from_bytes(x, "big")
    y_int = int.from_bytes(y, "big")
    z, v = 0, y_int
    for i in range(128):
        if (x_int >> (127 - i)) & 1:
            z ^= v
        if v & 1:
            v = (v >> 1) ^ 0xE1000000000000000000000000000000
        else:
            v >>= 1
    return z.to_bytes(16, "big")


def _ghash(h, ciphertext, aad=b""):
    def pad16(b):
        return b + b"\x00" * ((-len(b)) % 16)
    data = pad16(aad) + pad16(ciphertext)
    data += (len(aad) * 8).to_bytes(8, "big") + (len(ciphertext) * 8).to_bytes(8, "big")
    y = b"\x00" * 16
    for i in range(0, len(data), 16):
        block = bytes(a ^ b for a, b in zip(y, data[i:i + 16]))
        y = _gf128_mul(block, h)
    return y


def aes256_gcm_encrypt(key, nonce12, plaintext, aad=b""):
    """Returns (ciphertext_without_tag, tag16)."""
    if len(key) != 32 or len(nonce12) != 12:
        raise ValueError("need a 32-byte key and a 12-byte nonce")
    h = aes256_encrypt_block(key, b"\x00" * 16)
    j0 = nonce12 + b"\x00\x00\x00\x01"
    # CTR starting at J0+1
    counter = int.from_bytes(j0, "big") + 1
    out = bytearray()
    for off in range(0, len(plaintext), 16):
        ks = aes256_encrypt_block(key, counter.to_bytes(16, "big"))
        chunk = plaintext[off:off + 16]
        out.extend(a ^ b for a, b in zip(chunk, ks))
        counter += 1
    s = _ghash(h, bytes(out), aad)
    ej0 = aes256_encrypt_block(key, j0)
    tag = bytes(a ^ b for a, b in zip(s, ej0))
    return bytes(out), tag

def _gcm_decrypt(key, nonce12, ciphertext, tag):
    """Decrypt + verify (CTR is symmetric; tag recomputed via GHASH)."""
    h = aes256_encrypt_block(key, b"\x00" * 16)
    j0 = nonce12 + b"\x00\x00\x00\x01"
    counter = int.from_bytes(j0, "big") + 1
    out = bytearray()
    for off in range(0, len(ciphertext), 16):
        ks = aes256_encrypt_block(key, counter.to_bytes(16, "big"))
        chunk = ciphertext[off:off + 16]
        out.extend(a ^ b for a, b in zip(chunk, ks))
        counter += 1
    s = _ghash(h, ciphertext)  # GHASH runs over ciphertext, not plaintext
    ej0 = aes256_encrypt_block(key, j0)
    expect = bytes(a ^ b for a, b in zip(s, ej0))
    if expect != tag:
        raise ValueError("GCM tag mismatch")
    return bytes(out)


def main():
    import base64
    import hashlib
    import json
    import uuid

    a, gen_dir = _args()
    os.makedirs(gen_dir, exist_ok=True)
    password = b"testpassword"  # must match the password typed by route_14.py
    master = os.urandom(32)
    slot_salt = os.urandom(32)
    slot_nonce = os.urandom(12)
    hdr_nonce = os.urandom(12)
    slot_key = hashlib.scrypt(password, salt=slot_salt, n=32768, r=8, p=1, maxmem=128 * 1024 * 1024,
                              dklen=32)
    slot_ct, slot_tag = aes256_gcm_encrypt(slot_key, slot_nonce, master)
    db_obj = {"version": 3, "entries": [], "groups": [],
              "icons_optimized": False}
    db_bytes = json.dumps(db_obj, separators=(",", ":")).encode("utf-8")
    db_ct, db_tag = aes256_gcm_encrypt(master, hdr_nonce, db_bytes)
    vault = {
        "version": 1,
        "header": {
            "slots": [{
                "type": 1,
                "uuid": str(uuid.uuid4()),
                "key": slot_ct.hex(),
                "key_params": {"nonce": slot_nonce.hex(),
                               "tag": slot_tag.hex()},
                "n": 32768, "r": 8, "p": 1,
                "salt": slot_salt.hex(),
                "repaired": True,
                "is_backup": False,
            }],
            "params": {"nonce": hdr_nonce.hex(), "tag": db_tag.hex()},
        },
        "db": base64.b64encode(db_ct).decode("ascii"),
    }
    # Self-check: re-derive and decrypt exactly as the app will.
    try:
        key2 = hashlib.scrypt(password, salt=slot_salt, n=32768, r=8, p=1, maxmem=128 * 1024 * 1024,
                              dklen=32)
        master2 = _gcm_decrypt(key2, slot_nonce, slot_ct, slot_tag)
        if master2 != master:
            raise ValueError("slot round-trip mismatch")
        db2 = _gcm_decrypt(master2, hdr_nonce, db_ct, db_tag)
        if json.loads(db2.decode("utf-8")) != db_obj:
            raise ValueError("db round-trip mismatch")
    except ValueError as exc:
        _fail("self-check failed: %s" % exc)
    out = os.path.join(gen_dir, "aegis-vault.json")
    try:
        with open(out, "w", encoding="utf-8") as f:
            json.dump(vault, f)
    except OSError as exc:
        _fail("write failed: %s" % exc)
    _log(a, "generated aegis-vault.json (%d bytes) password=testpassword"
         % os.path.getsize(out))


if __name__ == "__main__":
    main()
