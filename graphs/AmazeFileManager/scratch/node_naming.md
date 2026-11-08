# Node Naming Analysis for AmazeFileManager Trigger Graph Builder

## How the Builder Forms Node Names

Based on reading `/Users/darshan/Desktop/yang/work/tools/build_graph.py`, here is how canonical node names are determined:

### Core Naming Logic (lines 112-130)

```python
def method_names(rows):
    """Base node name per method; overloads get '(params)'; classes that share a simple name get a package prefix."""
    pre = class_prefixes(rows)
    shorts = [pre.get(r['class'].split('$')[0], '') + r['short'] for r in rows]
    count = collections.Counter(shorts)
    names, by_name = [], {}
    for r, sh in zip(rows, shorts):
        n = sh if count[sh] == 1 else '%s(%s)' % (sh, param_names(r['desc']))
        k = 2
        while n in by_name:   # same class, overloads whose parameter simple names coincide
            n = '%s#%d' % (n.split('#')[0], k)
            k += 1
        names.append(n)
        by_name[n] = r
    return names, by_name
```

### Rules:

1. **Base name** comes from the `short` field in method_list.json (line 116)
   - Format: `ClassName.methodName` or `ClassName.<init>` or `ClassName.<clinit>`
   
2. **Package prefix** added when multiple classes share the same simple name (line 116)
   - Determined by `class_prefixes(rows)` which finds minimal distinguishing package tail
   - Example: if two `TagsAdapter` exist, one becomes `ui.TagsAdapter` etc.

3. **Overload disambiguation** (line 119): When multiple methods have the same `short` name:
   - Append `(params)` where params are simplified parameter types
   - `param_names(desc)` converts JVM descriptor to readable form:
     - `(Landroid/content/Context;I)Z` becomes `(Context,int)`
     - Arrays: `[B` becomes `byte[]`
     - Primitives: `I`→`int`, `J`→`long`, `Z`→`boolean`, etc.
     - Objects: take simple class name after last `/` and after last `$`

4. **Hash collision** resolution (lines 121-123): If two overloads have identical param simple names:
   - Append `#2`, `#3`, etc.

5. **Known nodes** (line 348): The validation set `known` is:
   ```python
   known = set(methods) | set(screens)
   ```
   where `methods` is the list of names from `method_names(rows)` and `screens` is from `SCREENS` dict in graph_def.py

6. **Context variants** (line 249-252): Node names can have `@suffix` for different calling contexts
   - Example: `MainActivity.<init>@GET_CONTENT` vs `MainActivity.<init>`
   - The `base(n)` function strips `@...` when checking if a node exists
   - `base(n) = n.split('@')[0]` (line 73)

7. **Edge ID suffixes** (line 286-291): Edge IDs get `-2`, `-3` when hash collides
   - Edge ID format: `E` + first 8 chars of SHA1 hash of edge content
   - If multiple edges hash to same ID, append `-2`, `-3`, etc.

### Why Names Are Rejected (Class b errors)

From build file error analysis, ~286 names are in method_list.json 'short' field but builder says "unknown node".

**Root cause**: The names in graph_def.py reference methods that:
1. **Don't exist in method_list.json at all** - inherited methods not listed
   - Example: `FtpService.onCreate` - FtpService inherits onCreate from parent Service class
   - method_list.json only contains methods *declared* in each class
   
2. **Have overloads requiring parameter disambiguation**
   - graph_def.py: `LayoutElementParcelable.<init>`
   - Builder expects: `LayoutElementParcelable.<init>(Context,String,String,String,String,long,boolean,String,boolean,boolean,OpenMode)` (or other overload)
   - When `count[sh] > 1` (line 119), params are required

3. **Inner class naming differences**
   - graph_def.py might use outer class name when method is in inner class
   - Example: `AppConfig.toast` vs actual location in inner class

### Classification from Build Resume 72 Analysis (VERIFIED)

Ran `resolve_names.py` on build_resume_72.txt:
- **Total error lines**: 1,127 (edge references to unknown nodes)
- **Unique unknown names**: 387

### Resolution Results:
- **Resolved**: 61 names (unambiguous mapping to 1 canonical name)
- **Ambiguous**: 63 names (multiple candidate matches, need manual disambiguation)
- **Not a node**: 263 names (not in method_list.json)

### Category Breakdown:

**(a) Framework/library internal: 56 names**  
Class not in method_list.json at all. Framework or library classes that the app doesn't declare.
- Examples: `Drawable`, `PreferenceScreen`, `DialogPreference`, `View.onClick`

**(b) Overload/naming mismatch: 121 names**  
Name IS in method_list.json but builder rejects because:
1. Multiple overloads exist, need parameter types: `AppConfig.toast` → `AppConfig.toast(Context,int)` vs `AppConfig.toast(Context,String)`
2. Inner class naming: `ArchivePasswordCacheHolder.<clinit>` → `ArchivePasswordCache$ArchivePasswordCacheHolder.<clinit>`
3. Package prefix differences when classes share simple names

**(c) Inherited method: 203 names**  
Class exists in method_list.json but the specific method is not declared in it (inherited from parent class).
- Examples:
  - `FtpService.onCreate` (inherited from Service)
  - `TabFragment.onCreate` (inherited from Fragment)
  - `AppsAdapter.onBindViewHolder` (inherited from RecyclerView.Adapter)

**(d) Pseudo-node: 4 names**  
Invented placeholders used in graph_def.py that don't represent real methods:
- `LAUNCHER`, `FRAMEWORK`, `INTENT_FILTER`, etc.

**(e) JVM signature form: 3 names**  
Full bytecode descriptor syntax: `GlideRequests.load([B)Lcom/amaze/filemanager/GlideRequest;`
These are auto_calls.json entries using JVM internal format.

**(f) Exact match: 0 names**  
(This category is for names that match directly - none in the error set by definition)

## Code Citations

- Line 73: `base(n) = n.split('@')[0]`
- Lines 76-91: `param_names(desc)` - JVM descriptor to readable params
- Lines 93-110: `class_prefixes(rows)` - disambiguate same-named classes
- Lines 112-130: `method_names(rows)` - main naming function
- Lines 286-291: `assign_ids(edges)` - edge ID with hash collision handling
- Lines 348-356: Node validation, generates "unknown node" errors
- Line 355: `if base(x[end]) not in known: errors.append('%s: unknown %s node %s' % (x['id'], end, x[end]))`

## Deterministic Resolution Strategy

To map bad names to canonical names:

1. **Strip context** suffix: `base(name)` to get core name
2. **Check exact match** in builder's `methods` list → use it
3. **For class (c) - inherited methods**: Not in method_list.json, mark as `NOT_A_NODE/inherited`
4. **For class (b) - overloads**: Search method_list.json for matching class+method, return candidates with params
5. **For class (a) - framework**: Not in method_list.json, mark as `NOT_A_NODE/framework`
6. **For class (d) - pseudo**: Mark as `NOT_A_NODE/pseudo`
7. **For class (f) - JVM descriptor**: Parse descriptor, convert to param form

When result is:
- 1 candidate → RESOLVED to canonical name
- 0 candidates → NOT_A_NODE with classification
- 2+ candidates → AMBIGUOUS with list of candidates
