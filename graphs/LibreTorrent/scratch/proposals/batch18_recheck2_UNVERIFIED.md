# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# LibreTorrent batch 18 — re-check 2 (InputFilterRange / Builder rows only)

**UNVERIFIED proposal — NOT merged. No build, sampler, grep, or C1 count is claimed.**
Connector-only work (GitHub connector, branch `work-2026-10-31`, repo `bugfixops/ground-truth-results`).
No token, no local checkout, no push, no edit to `graph_def.py` / `out` / `progress` / `tools`.

## Scope

Batch 18 has 40 rows in `handoff/LIBRETORRENT_BATCH_PLAN.tsv` (plan SHA
`0104806dd666c840049b3db52823d4b384fa1c92`). Its 10 previously-OPEN rows are
exactly the InputFilterRange / InputFilterRange$Builder rows:

- `InputFilterRange.<clinit> ()V`
- `InputFilterRange.<init> (Ljava/lang/Integer;Ljava/lang/Integer;)V`
- `InputFilterRange.filter (Ljava/lang/CharSequence;IILandroid/text/Spanned;II)Ljava/lang/CharSequence;`
- `InputFilterRange.getMax ()Ljava/lang/Integer;`
- `InputFilterRange.getMin ()Ljava/lang/Integer;`
- `InputFilterRange.inRange (I)Z`
- `InputFilterRange$Builder.<init> ()V`
- `InputFilterRange$Builder.build ()Lorg/proninyaroslav/libretorrent/core/InputFilterRange;`
- `InputFilterRange$Builder.setMax (I)Lorg/proninyaroslav/libretorrent/core/InputFilterRange$Builder;`
- `InputFilterRange$Builder.setMin (I)Lorg/proninyaroslav/libretorrent/core/InputFilterRange$Builder;`

The other 30 batch-18 rows are unchanged by this re-check (previously proposed
REACHABLE; not re-judged here).

## New evidence — the attach site (printed in full, 2026-10-31)

File: `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/ui/log/LogSettingsFragment.java`

```
51:     public void onCreate(Bundle savedInstanceState)
...
59:         InputFilter[] maxFilter = new InputFilter[] {
60:                 new InputFilterRange.Builder()
61:                         .setMin(1)
62:                         .setMax(Integer.MAX_VALUE)
63:                         .build()
64:         };
...
66:         String keyMaxLogSize= getString(R.string.pref_key_max_log_size);
67:         EditTextPreference maxLogSize  = findPreference(keyMaxLogSize);
68:         if (maxLogSize != null) {
69:             String value = Integer.toString(pref.maxLogSize());
70:             maxLogSize.setOnBindEditTextListener((editText) -> editText.setFilters(maxFilter));
71:             maxLogSize.setSummary(value);
72:             maxLogSize.setText(value);
73:             bindOnPreferenceChangeListener(maxLogSize);
74:         }
```

File: `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/core/InputFilterRange.java` (printed in full)

```
public class InputFilterRange implements InputFilter
{
    public static final InputFilterRange PORT_FILTER = new InputFilterRange.Builder()
            .setMin(0)
            .setMax(65535)
            .build();

    public static final InputFilterRange UNSIGNED_INT = new InputFilterRange.Builder()
            .setMin(0)
            .setMax(Integer.MAX_VALUE)
            .build();

    private Integer min;
    private Integer max;

    private InputFilterRange(Integer min, Integer max)
    {
        this.min = min;
        this.max = max;
    }

    @Nullable
    public Integer getMin()
    {
        return min;
    }

    @Nullable
    public Integer getMax()
    {
        return max;
    }

    @Override
    public CharSequence filter(CharSequence source, int start, int end,
                               Spanned dest, int dstart, int dend)
    {
        if (source.length() == 1 && source.charAt(0) == '-')
            return null;

        try {
            int input = Integer.parseInt(dest.toString() + source.toString());
            if (inRange(input))
                return null;

        } catch (NumberFormatException e) {
            /* Ignore */
        }

        return "";
    }

    private boolean inRange(int num)
    {
        return (min == null || num >= min) && (max == null || num <= max);
    }

    public static class Builder
    {
        private Integer min;
        private Integer max;

        public Builder setMin(int min)
        {
            this.min = min;

            return this;
        }

        public Builder setMax(int max)
        {
            this.max = max;

            return this;
        }

        public InputFilterRange build()
        {
            if (min != null && max != null && min > max)
                throw new IllegalArgumentException("max < min");

            return new InputFilterRange(min, max);
        }
    }
}
```

Hosting-activity check (printed): `ui/log/LogSettingsActivity.java` `onCreate`
(lines 37–50) only sets the content view (`R.layout.activity_log_settings`)
and the toolbar; it does **not** programmatically attach
`LogSettingsFragment`. Fragment attachment via the layout XML was not printed.

## Strict-entry caveat (explicit)

The route below is anchored at `LogSettingsFragment.onCreate`, a fragment
lifecycle entry — **not** a launcher entry. No printed step in this pass goes
launcher → `LogSettingsActivity` → fragment attachment, and the layout-XML
fragment attachment was not printed. These rows are therefore REACHABLE
**proposed**, not verified, and the launcher-to-entry step remains open.

## Per-row verdicts

| # | Method (batch 18) | Verdict (proposed) | confirmed_by | Route / citation |
|---|---|---|---|---|
| 1 | `InputFilterRange.<clinit> ()V` | REACHABLE | INFERRED | `LogSettingsFragment.onCreate` L59–64 builds the filter; `Builder.build()` returns `new InputFilterRange(min, max)` (InputFilterRange.java), and JVM class initialisation runs before that first instantiation, executing the `PORT_FILTER` / `UNSIGNED_INT` static initialisers. The class-init ordering is JVM semantics, not a printed app line — hence INFERRED, not SOURCE. |
| 2 | `InputFilterRange.<init> (Integer, Integer)V` | REACHABLE | SOURCE | Called directly by `Builder.build()`: `return new InputFilterRange(min, max);` (InputFilterRange.java), reached from `LogSettingsFragment.onCreate` L60–63. |
| 3 | `InputFilterRange.filter (…)` | REACHABLE | INFERRED | The built filter is registered on the preference's EditText: `maxLogSize.setOnBindEditTextListener((editText) -> editText.setFilters(maxFilter))` (LogSettingsFragment L70). Android's EditText framework then invokes `filter()` on text input. The framework dispatch itself is not a printed app line — hence INFERRED. Runs only when the user edits the max-log-size field. |
| 4 | `InputFilterRange.getMax ()Integer` | OPEN | — | No printed caller. `filter()` and `inRange()` read the `max` field directly; neither calls `getMax()`, and `LogSettingsFragment` does not call it. Missing evidence: full-repo grep for `getMax()` call sites on `InputFilterRange` instances. |
| 5 | `InputFilterRange.getMin ()Integer` | OPEN | — | No printed caller. Same as `getMax`: `filter()` / `inRange()` read the `min` field directly. Missing evidence: full-repo grep for `getMin()` call sites on `InputFilterRange` instances. |
| 6 | `InputFilterRange.inRange (I)Z` | REACHABLE | SOURCE for the internal call; INFERRED for reaching `filter()` | Called directly by `filter()`: `if (inRange(input)) return null;` (InputFilterRange.java). Inherits the framework-dispatch caveat of `filter()` (row 3). |
| 7 | `InputFilterRange$Builder.<init> ()V` | REACHABLE | SOURCE | `new InputFilterRange.Builder()` (LogSettingsFragment L60). No explicit constructor is printed; this is the implicit default constructor invoked by that `new` expression. |
| 8 | `InputFilterRange$Builder.build ()InputFilterRange` | REACHABLE | SOURCE | `.build()` (LogSettingsFragment L63). |
| 9 | `InputFilterRange$Builder.setMax (I)Builder` | REACHABLE | SOURCE | `.setMax(Integer.MAX_VALUE)` (LogSettingsFragment L62). |
| 10 | `InputFilterRange$Builder.setMin (I)Builder` | REACHABLE | SOURCE | `.setMin(1)` (LogSettingsFragment L61). |

## Totals for the 10 re-checked rows

- REACHABLE proposed: **8** (`<clinit>`, `<init>`, `filter`, `inRange`,
  `Builder.<init>`, `build`, `setMax`, `setMin`)
- UNREACHABLE proposed: **0** (no UNREACHABLE verdict is claimed; none of the
  10 meets the bar of exactly one kind / reason / source reference for
  unreachability)
- OPEN: **2** (`getMin`, `getMax`)

## What would resolve the 2 OPEN rows

- A full-repo grep for `\.getMin\(\)` and `\.getMax\(\)` applied to
  `InputFilterRange` objects (or any other printed caller file). A printed
  caller would move the row to REACHABLE proposed; a completed, saved grep
  over the full source tree with no caller would be the basis for an
  UNREACHABLE proposal — a connector `search_code` 0 / incomplete result was
  **not** used as evidence of absence, per the task rules.
- Separately, printing the launcher → `LogSettingsActivity` step and the
  `activity_log_settings` layout fragment attachment would close the
  strict-entry caveat for all 10 rows.

## Method note

- `search_code` returned 0 / incomplete for this repository and was ignored
  (not treated as absence).
- No verdict above was changed without printed lines; every REACHABLE row
  cites printed lines from `LogSettingsFragment.java` and/or
  `InputFilterRange.java`.
- No DYN / FW-MEMORY / UNVERIFIED confirmation labels are used for these
  rows; `confirmed_by` is SOURCE or INFERRED only, as specified.
