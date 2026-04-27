# Part 1:
## Solution A
This function returns each item and the number of times that it occurs.

This is complexity O(n log k). There is no nested loop. We just go
through the loop twice. The first loop is to count the items and the second loop is to create
the list of tuples. The heapq.nlargest function runs in O(n log k) time, which is efficient for small k.

O(n log k) is dominant because it is greater than O(n).

## Solution_B
The complexity of the return statement is O(k). The sort operation
is O(n log n) where n is the number of unique items. The list comprehension is O(n) to create the list of entries. Therefore, the
overall complexity is O(n log n) due to the sorting step, which dominates the other operations.

## Solution_C
The complexity of this function is O(n^2) in the worst case. The first loop
runs in O(n) time to build the seen_order list. The second loop runs in O(m * n) time, where m is the
number of unique items, because for each unique item we call items.count(), which itself is O(n). The
sort operation runs in O(m log m) time, where m is the number of unique items. Since m
can be at most n (if all items are unique), the overall complexity is dominated by the O(n^2) term from
counting occurrences, making it O(n^2) in the worst case.


## Prediction 1:
**Solution C** will break first because it has the highest complexity, which is O(n^2).

## Prediction 2:
I would trust **Solution A** the best at 3am during an outage because it has the smallest complexity, which is O(n log k).
Therefore, it will work the quickest.


# Part 2:
Best: Solution A
Good: Solution B
Worst: Solution C

They all handle k = 0 the same.

When k is larger than the number of items, solutions B and C both crash. None of them seems to mutate the input.

Solutions A and B have a loop in their output, while solution C buffers.

None of them seem to change their input.

Solution C is the easiest for me to understand.

In solutions A and B, the type hints actually match the things that they return. However, in solution C, the type hint
is "list[int]", which suggests that it would return a list of integers, but it returns a list of tuples instead.

# Part 3
=== Regime 1 — small fixed vocabulary (50 distinct items) ===
         n |   unique |     A (heap) |     B (sort) |     C (loop)
------------------------------------------------------------------------
       100 |       50 |       0.09ms |       0.04ms |       0.13ms
     1,000 |       50 |       0.12ms |       0.33ms |       1.06ms
    10,000 |       50 |       0.89ms |       0.66ms |       7.51ms
   100,000 |       50 |      42.65ms |      36.15ms |     254.00ms

=== Regime 2 — vocabulary scales with n (unique ≈ n/2) ===
         n |   unique |     A (heap) |     B (sort) |     C (loop)
------------------------------------------------------------------------
       100 |       50 |       0.06ms |       0.19ms |       0.14ms
     1,000 |      500 |       1.45ms |       0.36ms |      29.87ms
    10,000 |    5,000 |      10.87ms |      13.92ms |    1987.66ms
    50,000 |   25,000 |      16.17ms |      19.85ms |   15496.33ms

How to read the tables:
  - Per-row: 10x more input. If a column's time grows ~10x, that's linear.
    If it grows ~100x, that's roughly quadratic.
  - Compare across regimes: which solutions are sensitive to unique-count?
    Which are insensitive? Which workload would you choose each for?


    As n got larger, its impact on solutions A and B both diminished. However, solution C continues
    to be sensitive. Solutions A and B are less sensitive.

    In regime 1, I would choose B, whereas in regime 2, I would choose A.

    A and B seem to be roughly competitive with each other. However, when I tried running them, I got
    an error message saying:

    "src/solution_c.py:29: error: Incompatible return value type (got "list[tuple[str, int]]", expected "list[int]")  [return-value]
    Found 1 error in 1 file (checked 3 source files)"

    - Did the benchmark numbers confirm or change your ranking from Part 2?
    - Which variant did `mypy --strict` catch? What did it say?
    - Was the Regime 1 picture different from the Regime 2 picture? What does the
      difference suggest about *which kind of workload each variant is suited for*?

    The benchmarks approximately confirm my ranking from Part 2. Solution C got an error when I ran mypy.

    Yes, the Regime 1 picture is different from the Regime 2 picture. More specifically, Regime 1 says that
    solution B is the fastest, while Regime 2 says that solution A is the fastest.