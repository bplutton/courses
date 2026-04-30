# Expense Refactor — Grading Rubric

Total: **100 points**

---

## Part 1 — CSV + JSON Parsing (25 pts)

| Criterion | Points |
|---|---|
| `test_csv_parsing_no_io` and `test_json_parsing_no_io` both pass | 10 |
| Parsing logic is **not duplicated** between CSV and JSON paths | 10 |
| Parser is a separable component (a class, callable, or module) — `build_report` does not switch on file type internally | 5 |

**Common deductions:**
- −5 if there is an `if input.endswith(".json")` somewhere inside the report-building code
- −5 if CSV parsing and JSON parsing share more than ~3 lines of duplicated logic

---

## Part 2 — Configurable Categorizer (25 pts)

| Criterion | Points |
|---|---|
| `test_swap_categorizer` passes | 10 |
| Categories are loaded from `data/categories.json`, not hard-coded | 5 |
| Loading the config and using the config are **separate concerns** (the pipeline takes a `Categorizer`, not a filename) | 10 |

**Common deductions:**
- −5 if categories are a global / module-level dict
- −5 if there is no way to pass a different categorizer in for testing without monkeypatching

---

## Part 3 — Pure Pipeline (35 pts)

| Criterion | Points |
|---|---|
| `test_pipeline_does_no_io` passes (no `open()`, no `print()`) | 15 |
| Core logic (`build_report` or equivalent) returns a value; does not print | 10 |
| I/O isolated to a CLI entry point (`main`, `__main__`, or similar) | 10 |

**Common deductions:**
- −10 if they monkeypatched the test instead of refactoring the code
- −5 if `print()` happens inside `build_report` but they "fixed" it by capturing stdout in the test
- −5 if the test passes but `main()` no longer works (running the script as before should still produce the same report)

---

## Part 4 — Reflection (15 pts)

| Criterion | Points |
|---|---|
| Q1 (before/after) — concrete, not generic | 4 |
| Q2 (name the patterns) — points at specific lines or functions | 4 |
| Q3 (which hurt most) — names a real first-attempt mistake | 4 |
| Q4 (imagined future change) — gives a believable estimate, walks through what they'd add | 3 |

**Common deductions:**
- −2 per question that is generic ("I learned a lot about coupling") rather than specific
- −5 if the reflection is < 1/2 page — this is the assessment that distinguishes "passed the tests" from "understood why"

---

## What "good" looks like

A submission that scores in the 90s typically has these properties:

- **Three small modules** in `src/`: something like `parsers.py`,
  `categorizer.py`, and `pipeline.py` (or `report.py`). Names will vary.
- **A thin `main()`** that reads the file, builds the right parser, builds the
  categorizer, calls `build_report`, prints the result. ~15-25 lines.
- **A `build_report(parser, categorizer, source)` function** with no I/O,
  no print, no globals, no defaults that hide a filename.
- **Tests pass on first run after uncommenting** — meaning the student's
  refactor matched the contract the test expects, not "I made the test
  pass somehow."
- **A reflection that names patterns from class** and points at specific
  files/functions where they show up.

---

## What "barely passing" looks like

- Tests pass, but the refactor is shallow — e.g., extracted `parse_csv` and
  `parse_json` as standalone functions but the pipeline still has a
  conditional that picks between them.
- Categories loaded from JSON but still as a module global.
- `main()` is still 50 lines and the "pure" function is just a thin wrapper.

These submissions land in the 70-80 range. Use the reflection to decide
whether the student understood the principle or just satisfied the test
mechanically — that's the difference between 70 and 80.

---

## What "failing" looks like

- Tests don't pass and there's no clear refactor visible
- Reflection is missing or generic
- They monkeypatched the I/O test rather than refactoring

These submissions land below 60. The fix is conversation in office hours,
not a regrade — the lesson is the refactor, and they didn't do it.
