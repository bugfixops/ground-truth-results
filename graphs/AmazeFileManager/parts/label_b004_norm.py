# ---- Helper batch_004 label part (2026-10-27)

e('ArchivePasswordCache.getInstance', 'ArchivePasswordCacheHolder.<clinit>', 'FRAMEWORK', 'static initializer for holder class', evidence='SRC ArchivePasswordCache.java:65-67')

e('ArchivePasswordCacheHolder.<clinit>', 'ArchivePasswordCache.<init>', 'FRAMEWORK', 'constructor called from static initializer', evidence='SRC ArchivePasswordCache.java:66')

e('BookSorter.<init>', 'BookSorter.compare', 'FRAMEWORK', 'Comparator.compare called by Collections.sort', evidence='SRC BookSorter.java:1-19')

UNREACHABLE['BindPair.<init>'] = (
    'branch_never_taken',
    'BindPair is a private library class in commons_compress_7z module; grep shows no app instantiation sites',
    'SRC BindPair.java:20-26',
    'INFERRED'
)

UNREACHABLE['BindPair.toString'] = (
    'no_trigger_in_app',
    'library utility method, not called from app code',
    'SRC BindPair.java:28-30',
    'INFERRED'
)

UNREACHABLE['ArchivePasswordCache.clear'] = (
    'no_trigger_in_app',
    'Map interface method, no reachable code calls this',
    'SRC ArchivePasswordCache.java:119-120',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.containsValue'] = (
    'no_trigger_in_app',
    'Map interface method, no reachable code calls this',
    'SRC ArchivePasswordCache.java:85-87',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.entrySet'] = (
    'no_trigger_in_app',
    'Map interface method, not called from reachable code',
    'SRC ArchivePasswordCache.java:92-94',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.equals'] = (
    'no_trigger_in_app',
    'Map interface method, not called from reachable code',
    'SRC ArchivePasswordCache.java:138-140',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.hashCode'] = (
    'no_trigger_in_app',
    'Map interface method, not called from reachable code',
    'SRC ArchivePasswordCache.java:135-137',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.isEmpty'] = (
    'no_trigger_in_app',
    'Map interface method, not called from reachable code',
    'SRC ArchivePasswordCache.java:82-84',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.keySet'] = (
    'no_trigger_in_app',
    'Map interface method, not called from reachable code',
    'SRC ArchivePasswordCache.java:129-131',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.putAll'] = (
    'no_trigger_in_app',
    'Map interface method, not called from reachable code',
    'SRC ArchivePasswordCache.java:117-118',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.size'] = (
    'no_trigger_in_app',
    'Map interface method, not called from reachable code',
    'SRC ArchivePasswordCache.java:80-81',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.toString'] = (
    'no_trigger_in_app',
    'Map interface method, not called from reachable code',
    'SRC ArchivePasswordCache.java:133-134',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.values'] = (
    'no_trigger_in_app',
    'Map interface method, not called from reachable code',
    'SRC ArchivePasswordCache.java:127-128',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache$ArchivePasswordCacheHolder.<init>'] = (
    'branch_never_taken',
    'private constructor of holder class, never called',
    'SRC ArchivePasswordCache.java:62-63',
    'SOURCE'
)

