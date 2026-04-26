"""Solution C — Top-K most frequent items."""
from __future__ import annotations


def top_k_frequent(items: list[str], k: int) -> list[int]:
    """Find the k most frequent items in items along with their counts,
    most frequent first. Ties broken by first-appearance order.
    """
    if k <= 0:
        return []

    # Walk the input once to record each unique item in first-appearance order.
    seen_order: list[str] = []
    seen: set[str] = set()
    for x in items:
        if x not in seen:
            seen.add(x)
            seen_order.append(x)

    # For each unique item, count its occurrences in the input.
    pairs: list[tuple[str, int]] = []
    for item in seen_order:
        count = items.count(item)
        pairs.append((item, count))

    # Stable sort by descending count — first-appearance order is preserved on ties.
    pairs.sort(key=lambda p: -p[1])

    return pairs[:k]

"""
The complexity of this function is O(n^2) in the worst case. The first loop
runs in O(n) time to build the seen_order list. The second loop runs in O(m * n) time, where m is the
number of unique items, because for each unique item we call items.count(), which itself is O(n). The
sort operation runs in O(m log m) time, where m is the number of unique items. Since m
can be at most n (if all items are unique), the overall complexity is dominated by the O(n^2) term from
counting occurrences, making it O(n^2) in the worst case.
"""