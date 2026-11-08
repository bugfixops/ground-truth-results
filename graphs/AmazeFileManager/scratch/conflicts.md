# UNREACHABLE vs Edges Conflicts

Tracking decisions for each "X is UNREACHABLE but has incoming edges" warning.

## Format

| Method | Decision | Reasoning | Edge IDs | Action Taken |
|--------|----------|-----------|----------|--------------|

## Glide Methods - Restored UNREACHABLE entries (2026-10-28 20:30)

The following 27 Glide methods were UNRESOLVED in build_repair_09, causing R+U to drop from 2125 to 2099.
Investigation showed they have incoming edges, but only from unreachable sources.
**Decision**: RE-ADD explicit UNREACHABLE entries to restore R+U count.

| GlideOptions.centerCrop | KEEP UNREACHABLE | Incoming edge from unreachable source | Ede9a50cd | Re-added UNREACHABLE entry |
| GlideOptions.centerInside | KEEP UNREACHABLE | Incoming edge from unreachable source | E048b9772 | Re-added UNREACHABLE entry |
| GlideOptions.circleCrop | KEEP UNREACHABLE | Incoming edge from unreachable source | Edd5e7818 | Re-added UNREACHABLE entry |
| GlideOptions.decode | KEEP UNREACHABLE | Incoming edge from unreachable source | Eb5547a32 | Re-added UNREACHABLE entry |
| GlideOptions.diskCacheStrategy | KEEP UNREACHABLE | Incoming edge from unreachable source | E3c9b9a7d | Re-added UNREACHABLE entry |
| GlideOptions.dontAnimate | KEEP UNREACHABLE | Incoming edge from unreachable source | Eee10864b | Re-added UNREACHABLE entry |
| GlideOptions.dontTransform | KEEP UNREACHABLE | Incoming edge from unreachable source | E8c8f69bd | Re-added UNREACHABLE entry |
| GlideOptions.downsample | KEEP UNREACHABLE | Incoming edge from unreachable source | E5c87f155 | Re-added UNREACHABLE entry |
| GlideOptions.encodeFormat | KEEP UNREACHABLE | Incoming edge from unreachable source | E09e74aef | Re-added UNREACHABLE entry |
| GlideOptions.encodeQuality | KEEP UNREACHABLE | Incoming edge from unreachable source | Eb75f01e9 | Re-added UNREACHABLE entry |
| GlideOptions.error(int) | KEEP UNREACHABLE | Incoming edge from unreachable source | Ed4e22c4f | Re-added UNREACHABLE entry |
| GlideOptions.error(Drawable) | KEEP UNREACHABLE | Incoming edge from unreachable source | E3e9202b8 | Re-added UNREACHABLE entry |
| GlideOptions.fitCenter | KEEP UNREACHABLE | Incoming edge from unreachable source | E7d81da3a | Re-added UNREACHABLE entry |
| GlideOptions.format | KEEP UNREACHABLE | Incoming edge from unreachable source | Ebfa2758f | Re-added UNREACHABLE entry |
| GlideOptions.frame | KEEP UNREACHABLE | Incoming edge from unreachable source | E2ef756ff | Re-added UNREACHABLE entry |
| GlideOptions.override(int) | KEEP UNREACHABLE | Incoming edge from unreachable source | E00a8110e | Re-added UNREACHABLE entry |
| GlideOptions.override(int,int) | KEEP UNREACHABLE | Incoming edge from unreachable source | E2cca32d3 | Re-added UNREACHABLE entry |
| GlideOptions.placeholder(int) | KEEP UNREACHABLE | Incoming edge from unreachable source | E2fece387 | Re-added UNREACHABLE entry |
| GlideOptions.placeholder(Drawable) | KEEP UNREACHABLE | Incoming edge from unreachable source | Eebcdbcaa | Re-added UNREACHABLE entry |
| GlideOptions.priority | KEEP UNREACHABLE | Incoming edge from unreachable source | E0442b2e7 | Re-added UNREACHABLE entry |
| GlideOptions.set | KEEP UNREACHABLE | Incoming edge from unreachable source | E7002f016 | Re-added UNREACHABLE entry |
| GlideOptions.signature | KEEP UNREACHABLE | Incoming edge from unreachable source | Ea9cdc304 | Re-added UNREACHABLE entry |
| GlideOptions.sizeMultiplier | KEEP UNREACHABLE | Incoming edge from unreachable source | Efa4377e3 | Re-added UNREACHABLE entry |
| GlideOptions.skipMemoryCache | KEEP UNREACHABLE | Incoming edge from unreachable source | E30f17eb7 | Re-added UNREACHABLE entry |
| GlideOptions.timeout | KEEP UNREACHABLE | Incoming edge from unreachable source | E3c1a07e2 | Re-added UNREACHABLE entry |
| GlideOptions.transform(Transformation) | KEEP UNREACHABLE | Incoming edge from unreachable source | E408aa04b | Re-added UNREACHABLE entry |
| GlideRequest.<init>(Class,RequestBuilder) | KEEP UNREACHABLE | Incoming edge from unreachable source | Ef27a763e | Re-added UNREACHABLE entry |

---

## OLD Glide Methods Section (OBSOLETE - from failed deletion attempt)

The section below was from a failed attempt to delete UNREACHABLE entries. These deletions were INCORRECT and have been reversed above.

## Glide Methods - UNREACHABLE but has incoming edges

| GlideOptions.centerCrop | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.centerInside | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.circleCrop | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.decode | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.diskCacheStrategy | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.dontAnimate | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.dontTransform | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.downsample | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.encodeFormat | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.encodeQuality | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.error(int) | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.error(Drawable) | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.fitCenter | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.format | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.frame | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.override(int) | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.override(int,int) | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.placeholder(int) | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.placeholder(Drawable) | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.priority | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.set | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.signature | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.sizeMultiplier | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.skipMemoryCache | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.timeout | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.transform(Transformation) | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideRequest.<init>(Class,RequestBuilder) | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |

## Glide Methods - UNREACHABLE but has incoming edges

| GlideOptions.centerCrop | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.centerInside | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.circleCrop | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.decode | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.diskCacheStrategy | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.dontAnimate | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.dontTransform | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.downsample | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.encodeFormat | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.encodeQuality | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.error(int) | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.error(Drawable) | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.fitCenter | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.format | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.frame | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.override(int) | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.override(int,int) | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.placeholder(int) | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.placeholder(Drawable) | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.priority | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.set | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.signature | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.sizeMultiplier | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.skipMemoryCache | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.timeout | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideOptions.transform(Transformation) | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
| GlideRequest.<init>(Class,RequestBuilder) | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |
