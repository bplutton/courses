"""Expense Report — starter code.

This script works. It reads transactions.csv, categorizes the rows,
and prints a report showing per-category totals.

It also has all of its logic crammed into one big main() function with
hard-coded filenames, a hard-coded category dict, and print() statements
woven into the calculations.

Your job is to refactor this code IN PLACE, by moving the right logic
into the four helper shapes below, in response to the change requests in
the README. Keep everything in this one file.

When you're done, the script should produce the SAME output (TOTAL = $613.87)
on the original inputs — the change requests should not change observable
behavior on the starting CSV.

DO NOT add any external libraries. Standard library only.
"""

import json
from pathlib import Path

_CATEGORIES = {
        "STARBUCKS": "food",
        "DUNKIN": "food",
        "WHOLEFOODS": "food",
        "WHOLE FOODS": "food",
        "SHELL": "gas",
        "EXXON": "gas",
        "AMAZON": "shopping",
        "TARGET": "shopping",
        "NETFLIX": "entertainment",
        "SPOTIFY": "entertainment",
        "HARDWARE": "home",
    }

# -----------------------------------------------------------------------------
# TODO Part 1 — fill these in. (See README "Part 1 — Add JSON support".)
# -----------------------------------------------------------------------------

def parse_csv(text: str) -> list[dict]:
    """Return a list of row dicts: {"date", "vendor", "amount", "note"}.
    Skip lines that don't have 4 comma-separated fields.
    
    text = (
        "date,vendor,amount,note\n"
        "2026-04-01,Starbucks,4.85,coffee\n"
        "2026-04-02,Shell,52.30,gas\n"
        "bad,line\n"  # malformed — should be skipped
    )
    """
    rows = []
    # with open("data/transactions.csv") as f:
    lines = text.split("\n")[1:]
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4:
            parts_dict = {
                "date": parts[0],
                "vendor": parts[1],
                "amount": parts[2],
                "note": parts[3],
            }
            # if len(parts) != 4:
            #     continue
            rows.append(parts_dict)
    return rows


def parse_json(text: str) -> list[dict]:
    """Return a list of row dicts: {"date", "vendor", "amount", "note"}.
    Input is JSON text — same fields as the CSV, just JSON-shaped.
    
    text = json.dumps([
        {"date": "2026-04-01", "vendor": "Starbucks", "amount": 4.85,  "note": "coffee"},
        {"date": "2026-04-02", "vendor": "Shell",     "amount": 52.30, "note": "gas"},
    ])
    """
    return json.loads(text)


# -----------------------------------------------------------------------------
# TODO Part 2 — fill this in. (See README "Part 2 — Configurable categories".)
# -----------------------------------------------------------------------------

def categorize(vendor: str, categories: dict) -> str:
    """Return the category for `vendor` based on `categories`.

    `categories` maps {category_name: [keyword, keyword, ...]}.
    A vendor matches a category if any of the keywords appears in the
    vendor name (case-insensitive). Return "other" if no category matches.

    {
    "food":          ["STARBUCKS", "DUNKIN", "WHOLEFOODS", "WHOLE FOODS"],
    "gas":           ["SHELL", "EXXON"],
    "shopping":      ["AMAZON", "TARGET"],
    "entertainment": ["NETFLIX", "SPOTIFY"],
    "home":          ["HARDWARE"]
    }

    """
    for cat, keywords in categories.items():
        for keyword in keywords:
            if keyword in vendor.upper():
                return cat
    return "other"


# -----------------------------------------------------------------------------
# TODO Part 3 — fill this in. (See README "Part 3 — A pure pipeline".)
# -----------------------------------------------------------------------------

def build_report(rows: list[dict], categories: dict) -> dict:
    """Return {category_name: total_amount} for a list of parsed rows.

    Pure: must NOT open files, read stdin, or print anything.

    rows = [
        {"date": "2026-04-01", "vendor": "Starbucks", "amount": "4.85", "note": ""},
        {"date": "2026-04-01", "vendor": "Shell",     "amount": "52.30", "note": ""},
    ]
    totals = build_report(rows, _categories())
    """
    totals = {}
    for row in rows:
        date = row["date"]
        vendor = row["vendor"]
        amount = row["amount"]
        cat = categorize(vendor, categories)  # Also fix categorization to use the helper function
        totals[cat] = totals.get(cat, 0.0) + float(amount)

    # print("=== Expense Report ===")
    # for cat, total in sorted(totals.items()):
    #     print(f"  {cat:<15} ${total:>8.2f}")
    # print(f"  {'TOTAL':<15} ${sum(totals.values()):>8.2f}")
    return totals


# -----------------------------------------------------------------------------
# main() — I/O lives here. Once Parts 1-3 are done, this should shrink to
# just the I/O glue: read files, call parse_*, call build_report, print.
# Right now it has everything inline.
# -----------------------------------------------------------------------------

def main():
    """
    DONE WHEN:

    - `main()` is now a thin shell: read the file(s), call `parse_csv`,
      call `build_report`, print the result.
    """

    rows = []
    with open("data/transactions.csv") as f:
        rows = parse_csv(f.read())
        # for line in f.readlines()[1:]:
        #     parts = line.strip().split(",")
        #     if len(parts) != 4:
        #         continue
        #     rows.append(parts)

    totals = build_report(rows, _CATEGORIES)

    print("=== Expense Report ===")
    for cat, total in sorted(totals.items()):
        print(f"  {cat:<15} ${total:>8.2f}")
    print(f"  {'TOTAL':<15} ${sum(totals.values()):>8.2f}")



if __name__ == "__main__":
    main()