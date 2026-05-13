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

import argparse
import json
import sys
from pathlib import Path


# -----------------------------------------------------------------------------
# TODO Part 1 — fill these in. (See README "Part 1 — Add JSON support".)
# -----------------------------------------------------------------------------

def parse_csv(text: str) -> list[dict]:
    """Return a list of row dicts: {"date", "vendor", "amount", "note"}.
    Skip lines that don't have 4 comma-separated fields.
    """
    raise NotImplementedError("Part 1: implement parse_csv")


def parse_json(text: str) -> list[dict]:
    """Return a list of row dicts: {"date", "vendor", "amount", "note"}.
    Input is JSON text — same fields as the CSV, just JSON-shaped.
    """
    raise NotImplementedError("Part 1: implement parse_json")


# -----------------------------------------------------------------------------
# TODO Part 2 — fill this in. (See README "Part 2 — Configurable categories".)
# -----------------------------------------------------------------------------

def categorize(vendor: str, categories: dict) -> str:
    """Return the category for `vendor` based on `categories`.

    `categories` maps {category_name: [keyword, keyword, ...]}.
    A vendor matches a category if any of the keywords appears in the
    vendor name (case-insensitive). Return "other" if no category matches.
    """
    raise NotImplementedError("Part 2: implement categorize")


# -----------------------------------------------------------------------------
# TODO Part 3 — fill this in. (See README "Part 3 — A pure pipeline".)
# -----------------------------------------------------------------------------

def build_report(rows: list[dict], categories: dict) -> dict:
    """Return {category_name: total_amount} for a list of parsed rows.

    Pure: must NOT open files, read stdin, or print anything.
    """
    raise NotImplementedError("Part 3: implement build_report")


# -----------------------------------------------------------------------------
# main() — I/O lives here. Once Parts 1-3 are done, this should shrink to
# just the I/O glue: read files, call parse_*, call build_report, print.
# Right now it has everything inline.
# -----------------------------------------------------------------------------

def parse_csv(text: str) -> list[dict]:
    """
        text = (
        "date,vendor,amount,note\n"
        "2026-04-01,Starbucks,4.85,coffee\n"
        "2026-04-02,Shell,52.30,gas\n"
        "bad,line\n"  # malformed — should be skipped
    )
    """

    rows = []
    for line in text.splitlines()[1:]:
        parts = line.strip().split(",")
        if len(parts) != 4:
            continue
        parts_dict = {
            "date": parts[0],
            "vendor": parts[1],
            "amount": parts[2],
            "note": parts[3]
        }
        print(parts_dict)
        rows.append(parts_dict)
        print(rows)
    return rows


def parse_csv_file(filepath: str) -> list[dict]:
    rows = []
    with open("data/transactions.csv") as f:
        text = f.read()
    return parse_csv(text)
    # rows.append(parts)
    # return rows


def parse_json(filepath: str) -> list[dict]:
    with open(filepath) as f:
        data = json.load(f)
    return data


def main():

    # parser = argparse.ArgumentParser(description="Process expense report.")

    # parser.add_argument("filename", help="The source file to process")

    # args = parser.parse_args()

    # filepath = args.filename
    filepath = "data/transactions.csv"

    print("ENTERED MAIN")

    # rows = []
    # if filepath.endswith(".csv"):
    #     rows = parse_csv(filepath)
    # elif filepath.endswith(".json"):
    #     rows = parse_json(filepath)
    # else:
    #     print(f"Error: Unsupported file type for {filepath}", file=sys.stderr)
    #     exit(1)

    rows = parse_csv_file(filepath)
    
    # CHECK 0: Use Argparse to accept the input filename as a command-line argument, instead of hard-coding it here.
    # CHECK 1: Extract the parsing logic into parse_csv() and parse_json(), and call them here.
    # CHECK 2: Add a JSON parser.
    # CHECK 3: Add a statement to select the correct parser based on the file extension (.csv vs .json).

    categories = {
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

    totals = {}
    print("*"*40)
    for date, vendor, amount, _ in rows:
        cat = "other"
        for key, c in categories.items():
            if key in vendor.upper():
                cat = c
        print(f"**** TOTAL: {totals[cat]} ****\n") # DEBUG
        totals[cat] = totals.get(cat, 0.0) + float(amount)

    print("=== Expense Report ===")
    for cat, total in sorted(totals.items()):
        print(f"  {cat:<15} ${total:>8.2f}")
    print(f"  {'TOTAL':<15} ${sum(totals.values()):>8.2f}")


if __name__ == "__main__":
    main()
