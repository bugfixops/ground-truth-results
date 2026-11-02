# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# Per-route setup for new setup_route_16. Run-time generation only; nothing here is
# committed as a binary. Interface: --package --log --outdir --gen-dir (GEN_DIR
# fallback). No real emulator/adb run, no CI request, no drycheck pass claimed.
"""Per-route setup for Aegis route 16 (GoogleAuthProtos$MigrationPayload.parser).

Generates device-qr-export.png: a QR code encoding an otpauth-migration://offline URI whose data parameter is a hand-built MigrationPayload protobuf (standard base64 with padding, percent-encoded). Parsing it on the device calls the generated parser(), which is the route target. The QR encoder is embedded below (byte mode, EC level M; verified: matrices identical to the qrcode library, OpenCV decodes exactly).

Interface: --package PKG --log LOG --outdir DIR --gen-dir DIR (GEN_DIR env fallback). Writes only into --gen-dir. Exits 1 on any failure."""

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

"""Minimal QR encoder: byte mode, EC level M (or L), versions 1-10.

Standard library only. Implements ISO/IEC 18004 placement, format and
version info (BCH), Reed-Solomon EC codewords, mask selection by the
four penalty rules, and PNG output (zlib). Verified by decoding the
output with OpenCV's QRCodeDetector in test_qr.py.
"""

import struct
import zlib

# (total codewords, EC codewords per block, block count) per version/level
_TABLE = {
    1: (26, {"L": (7, 1), "M": (10, 1)}),
    2: (44, {"L": (10, 1), "M": (16, 1)}),
    3: (70, {"L": (15, 1), "M": (26, 1)}),
    4: (100, {"L": (20, 1), "M": (18, 2)}),
    5: (134, {"L": (26, 1), "M": (24, 2)}),
    6: (172, {"L": (18, 2), "M": (16, 4)}),
    7: (196, {"L": (20, 2), "M": (18, 4)}),
    8: (242, {"L": (24, 2), "M": (22, 4)}),
    9: (292, {"L": (30, 2), "M": (22, 5)}),
    10: (346, {"L": (18, 4), "M": (26, 5)}),
}
_ALIGN = {
    1: [], 2: [6, 18], 3: [6, 22], 4: [6, 26], 5: [6, 30], 6: [6, 34],
    7: [6, 22, 38], 8: [6, 24, 42], 9: [6, 26, 46], 10: [6, 28, 50],
}
_REMAINDER = {1: 0, 2: 7, 3: 7, 4: 7, 5: 7, 6: 7, 7: 0, 8: 0, 9: 0, 10: 0}
_EC_BITS = {"L": 1, "M": 0}


# --- GF(256), polynomial 0x11D ---
_EXP = [0] * 512
_LOG = [0] * 256
_x = 1
for _i in range(255):
    _EXP[_i] = _x
    _LOG[_x] = _i
    _x <<= 1
    if _x & 0x100:
        _x ^= 0x11D
for _i in range(255, 512):
    _EXP[_i] = _EXP[_i - 255]


def _gf_mul(a, b):
    return 0 if a == 0 or b == 0 else _EXP[_LOG[a] + _LOG[b]]


def _rs_gen(degree):
    # Generator polynomial prod_i (xx + alpha^i), coefficients in
    # DESCENDING power order (leading 1 first). The LFSR in _rs_ec
    # taps gen[1..degree] in this order; an ascending polynomial here
    # silently produces wrong EC codewords (caught against segno).
    poly = [1]
    for i in range(degree):
        a = _EXP[i]
        new = [0] * (len(poly) + 1)
        new[0] = poly[0]
        for j in range(1, len(poly)):
            new[j] = poly[j] ^ _gf_mul(a, poly[j - 1])
        new[len(poly)] = _gf_mul(a, poly[-1])
        poly = new
    return poly


def _rs_ec(data, degree):
    gen = _rs_gen(degree)
    res = [0] * degree
    for b in data:
        factor = b ^ res.pop(0)
        res.append(0)
        for i in range(degree):
            res[i] ^= _gf_mul(gen[i + 1], factor)
    return res


def _bits_of(data, version, ecl):
    total, (ec, blocks) = _TABLE[version][0], _TABLE[version][1][ecl]
    data_cw = total - ec * blocks
    ccbits = 8 if version <= 9 else 16
    bits = []
    def put(value, length):
        for i in range(length - 1, -1, -1):
            bits.append((value >> i) & 1)
    put(0b0100, 4)
    put(len(data), ccbits)
    for b in data:
        put(b, 8)
    cap = data_cw * 8
    term = min(4, cap - len(bits))
    bits.extend([0] * term)
    while len(bits) % 8:
        bits.append(0)
    pads = [0xEC, 0x11]
    k = 0
    while len(bits) < cap:
        put(pads[k % 2], 8)
        k += 1
    codewords = []
    for i in range(0, len(bits), 8):
        v = 0
        for bit in bits[i:i + 8]:
            v = (v << 1) | bit
        codewords.append(v)
    assert len(codewords) == data_cw
    # split into blocks: short blocks first, then long blocks
    short_len = data_cw // blocks
    long_count = data_cw % blocks
    blks = []
    off = 0
    for i in range(blocks):
        ln = short_len + (1 if i >= blocks - long_count else 0)
        blks.append(codewords[off:off + ln])
        off += ln
    ec_blks = [_rs_ec(b, ec) for b in blks]
    out = []
    for i in range(max(len(b) for b in blks)):
        for b in blks:
            if i < len(b):
                out.append(b[i])
    for i in range(ec):
        for e in ec_blks:
            out.append(e[i])
    out_bits = []
    for cw in out:
        for i in range(7, -1, -1):
            out_bits.append((cw >> i) & 1)
    out_bits.extend([0] * _REMAINDER[version])
    return out_bits


def _format_bits(ecl, mask):
    data = (_EC_BITS[ecl] << 3) | mask
    rem = data
    for _ in range(10):
        rem = (rem << 1) ^ ((rem >> 9) * 0x537)
    return ((data << 10) | rem) ^ 0x5412


def _version_bits(version):
    rem = version
    for _ in range(12):
        rem = (rem << 1) ^ ((rem >> 11) * 0x1F25)
    return (version << 12) | rem


def _build_matrix(data_bits, version, ecl, mask):
    size = 21 + 4 * (version - 1)
    mod = [[None] * size for _ in range(size)]
    func = [[False] * size for _ in range(size)]

    def setf(xx, y, val):
        mod[y][xx] = 1 if val else 0
        func[y][xx] = True

    # finder patterns + separators
    for dx in (-1, 0, 1, 2, 3, 4, 5, 6, 7):
        pass
    for (fx, fy) in ((0, 0), (size - 7, 0), (0, size - 7)):
        for dy in range(-1, 8):
            for dx in range(-1, 8):
                xx, y = fx + dx, fy + dy
                if 0 <= xx < size and 0 <= y < size:
                    if 0 <= dx <= 6 and 0 <= dy <= 6:
                        v = 1 if (dx in (0, 6) or dy in (0, 6) or 2 <= dx <= 4 and 2 <= dy <= 4) else 0
                        setf(xx, y, v)
                    else:
                        setf(xx, y, 0)
    # timing
    for i in range(8, size - 8):
        v = 1 if i % 2 == 0 else 0
        setf(6, i, v)
        setf(i, 6, v)
    # alignment (skip only the three finder-corner combinations; patterns
    # on row/col 6 are drawn over the timing pattern, per spec)
    pos = _ALIGN[version]
    for r in pos:
        for c in pos:
            if (r == 6 and c == 6) or (r == 6 and c == pos[-1]) or (r == pos[-1] and c == 6):
                continue
            for dy in range(-2, 3):
                for dx in range(-2, 3):
                    v = 1 if (abs(dx) == 2 or abs(dy) == 2 or (dx == 0 and dy == 0)) else 0
                    setf(c + dx, r + dy, v)
    # format info
    fb = _format_bits(ecl, mask)
    def bit(i):
        return (fb >> i) & 1
    for i in range(6):
        setf(8, i, bit(i))
    setf(8, 7, bit(6))
    setf(8, 8, bit(7))
    setf(7, 8, bit(8))
    for i in range(9, 15):
        setf(14 - i, 8, bit(i))
    for i in range(8):
        setf(size - 1 - i, 8, bit(i))
    for i in range(8, 15):
        setf(8, size - 15 + i, bit(i))
    # Dark module: row 4V+9 (= size-8), column 8. NOT (size-8, 8):
    # that cell is format second-copy bit 7 and must keep its value.
    # (Transposing this was the last matrix mismatch vs segno/qrcode.)
    setf(8, size - 8, 1)
    # version info
    if version >= 7:
        vb = _version_bits(version)
        for i in range(18):
            v = (vb >> i) & 1
            a = size - 11 + i % 3
            b = i // 3
            setf(a, b, v)
            setf(b, a, v)
    # data placement
    def mask_bit(xx, y):
        if mask == 0:
            return (xx + y) % 2 == 0
        if mask == 1:
            return y % 2 == 0
        if mask == 2:
            return xx % 3 == 0
        if mask == 3:
            return (xx + y) % 3 == 0
        if mask == 4:
            return (y // 2 + xx // 3) % 2 == 0
        if mask == 5:
            return (xx * y) % 2 + (xx * y) % 3 == 0
        if mask == 6:
            return ((xx * y) % 2 + (xx * y) % 3) % 2 == 0
        return ((xx + y) % 2 + (xx * y) % 3) % 2 == 0

    idx = 0
    for right in range(size - 1, 0, -2):
        if right <= 6:
            right -= 1
        for vert in range(size):
            for j in range(2):
                xx = right - j
                y = size - 1 - vert if ((right + 1) & 2) == 0 else vert
                if func[y][xx]:
                    continue
                v = data_bits[idx] if idx < len(data_bits) else 0
                idx += 1
                if mask_bit(xx, y):
                    v ^= 1
                mod[y][xx] = v
    return mod, func


def _penalty(mod):
    size = len(mod)
    score = 0
    # rule 1: runs
    for y in range(size):
        run, prev = 1, mod[y][0]
        for xx in range(1, size):
            if mod[y][xx] == prev:
                run += 1
            else:
                if run >= 5:
                    score += run - 2
                run, prev = 1, mod[y][xx]
        if run >= 5:
            score += run - 2
    for xx in range(size):
        run, prev = 1, mod[0][xx]
        for y in range(1, size):
            if mod[y][xx] == prev:
                run += 1
            else:
                if run >= 5:
                    score += run - 2
                run, prev = 1, mod[y][xx]
        if run >= 5:
            score += run - 2
    # rule 2: 2x2 blocks
    for y in range(size - 1):
        for xx in range(size - 1):
            v = mod[y][xx]
            if mod[y][xx + 1] == v and mod[y + 1][xx] == v and mod[y + 1][xx + 1] == v:
                score += 3
    # rule 3: finder-like patterns
    pat = [1, 0, 1, 1, 1, 0, 1]
    for y in range(size):
        for xx in range(size - 10):
            seg = mod[y][xx:xx + 11]
            if seg[4:11] == pat or seg[0:7] == pat:
                before = all(v == 0 for v in seg[0:4]) if seg[4:11] == pat else True
                after = all(v == 0 for v in seg[7:11]) if seg[0:7] == pat else True
                if (seg[4:11] == pat and before) or (seg[0:7] == pat and after):
                    score += 40
    for xx in range(size):
        col = [mod[y][xx] for y in range(size)]
        for y in range(size - 10):
            seg = col[y:y + 11]
            if seg[4:11] == pat or seg[0:7] == pat:
                before = all(v == 0 for v in seg[0:4]) if seg[4:11] == pat else True
                after = all(v == 0 for v in seg[7:11]) if seg[0:7] == pat else True
                if (seg[4:11] == pat and before) or (seg[0:7] == pat and after):
                    score += 40
    # rule 4: dark ratio
    dark = sum(sum(row) for row in mod)
    total = size * size
    percent = dark * 100 // total
    score += (abs(percent - 50) // 5) * 10
    return score


def choose_version(data, ecl):
    for v in range(1, 11):
        total, (ec, blocks) = _TABLE[v][0], _TABLE[v][1][ecl]
        data_cw = total - ec * blocks
        ccbits = 8 if v <= 9 else 16
        if data_cw * 8 >= 4 + ccbits + 8 * len(data):
            return v
    raise ValueError("data too long for versions 1-10 at level %s" % ecl)


def encode_matrix(text, ecl="M"):
    data = text.encode("utf-8")
    version = choose_version(data, ecl)
    bits = _bits_of(data, version, ecl)
    best, best_score = None, None
    for mask in range(8):
        mod, _func = _build_matrix(bits, version, ecl, mask)
        s = _penalty(mod)
        if best_score is None or s < best_score:
            best, best_score = mod, s
    return best, version


def matrix_to_png(mod, scale=8, quiet=4):
    size = len(mod)
    full = size + 2 * quiet
    px = full * scale
    raw = bytearray()
    for y in range(full):
        row = bytearray([0])
        for xx in range(full):
            my, mx = y - quiet, xx - quiet
            dark = 0 <= my < size and 0 <= mx < size and mod[my][mx] == 1
            row.extend(bytes([0 if dark else 255]) * scale)
        for _ in range(scale):
            raw.extend(row)
    def chunk(ctype, payload):
        c = struct.pack(">I", len(payload)) + ctype + payload
        c += struct.pack(">I", zlib.crc32(ctype + payload) & 0xFFFFFFFF)
        return c
    ihdr = struct.pack(">IIBBBBB", px, px, 8, 0, 0, 0, 0)
    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", ihdr)
    png += chunk(b"IDAT", zlib.compress(bytes(raw), 9))
    png += chunk(b"IEND", b"")
    return png

def _varint(n):
    out = bytearray()
    while True:
        b = n & 0x7F
        n >>= 7
        if n:
            out.append(b | 0x80)
        else:
            out.append(b)
            return bytes(out)


def _tag(field, wire):
    return _varint((field << 3) | wire)


def _len_delim(field, payload):
    return _tag(field, 2) + _varint(len(payload)) + payload


def _var_field(field, value):
    return _tag(field, 0) + _varint(value)


def main():
    import base64
    import urllib.parse

    a, gen_dir = _args()
    os.makedirs(gen_dir, exist_ok=True)
    # MigrationPayload per proto/google_auth.proto: OtpParameters
    # secret=1, name=2, issuer=3, algorithm=4 (SHA1=1), digits=5
    # (SIX=1), type=6 (TOTP=2); payload otp_parameters=1, version=2,
    # batch_size=3, batch_index=4, batch_id=5.
    secret = bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    otp = b"".join([
        _len_delim(1, secret),
        _len_delim(2, b"Device Test"),
        _len_delim(3, b"Device Issuer"),
        _var_field(4, 1),
        _var_field(5, 1),
        _var_field(6, 2),
    ])
    payload = b"".join([
        _len_delim(1, otp),
        _var_field(2, 1),
        _var_field(3, 1),
        _var_field(4, 0),
        _var_field(5, 1),
    ])
    b64 = base64.b64encode(payload).decode("ascii")  # standard, padded
    uri = ("otpauth-migration://offline?data="
           + urllib.parse.quote(b64, safe=""))
    try:
        mod, version = encode_matrix(uri, "M")
        png = matrix_to_png(mod, scale=8, quiet=4)
    except ValueError as exc:
        _fail("QR encode failed: %s" % exc)
    out = os.path.join(gen_dir, "device-qr-export.png")
    try:
        with open(out, "wb") as f:
            f.write(png)
    except OSError as exc:
        _fail("write failed: %s" % exc)
    _log(a, "generated device-qr-export.png (QR version %d, %d bytes)"
         % (version, os.path.getsize(out)))


if __name__ == "__main__":
    main()
