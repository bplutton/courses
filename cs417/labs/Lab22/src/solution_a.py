"""Solution A — Top-K most frequent items."""
from __future__ import annotations

import heapq
from collections import Counter


def top_k_frequent(items: list[str], k: int) -> list[tuple[str, int]]:
    """Return the k most frequent items in `items`, paired with their counts,
    ordered most-frequent-first.

    Ties are broken by first-appearance order in `items` (the item that first
    appeared earlier wins). Returns [] if k <= 0.
    """
    if k <= 0:
        return []

    counts = Counter(items)
    # Counter preserves first-appearance order, so enumerating it gives a
    # stable index we can use for tiebreaking.
    indexed = [(count, -i, item) for i, (item, count) in enumerate(counts.items())]

    # nlargest by tuple compare: (count, -first_index, item).
    # Higher count wins; on ties, larger -first_index (i.e. smaller first_index,
    # i.e. earlier first appearance) wins.
    top = heapq.nlargest(k, indexed) # Returns the k largest items, sorted by the tuple order.
    return [(item, count) for count, _, item in top]

"""
This function returns each item and the number of times that it occurs.

This is complexity O(n log k). There is no nested loop. We just go
through the loop twice. The first loop is to count the items and the second loop is to create
the list of tuples. The heapq.nlargest function runs in O(n log k) time, which is efficient for small k.

O(n log k) is dominant because it is greater than O(n).
"""
