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
