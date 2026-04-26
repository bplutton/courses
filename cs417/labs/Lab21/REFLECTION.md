1. Which section gave you a bug mypy caught that you wouldn’t have caught by reading the code? Be specific — what was the error message, what was the underlying mistake, and why is that kind of mistake easy to make in Python?
Section 1. The error was "typed_demo.py:10: error: Incompatible return value type (got "str", expected "int")." There was a mistake that would have made the program return "not an int" as an int.

2. Runtime cost. Type hints don’t run at runtime — Python ignores them. Mypy is a separate tool you choose to run. What’s the cost and benefit of that design choice? What would change if Python enforced types at runtime the way Java does?

If Python enforced types at runtime, it would do so every time anyone ran the code, which is more often than writing the code.

3. TypedDict vs plain dict. A dict can play two roles: a record with a fixed set of named fields (like Lab 18’s roster row), or a mapping from variable keys to values (like Lab 20’s completed dict that maps submission IDs to results). For each of these two cases, would you reach for TypedDict or dict[K, V], and why?

In lab 18, where you have a fixed set of name fields, you would use a TypedDict because we want to make sure that we always have the correct types.
When mapping variable keys to values, I would use dict[K, V] because it is not necessary to make sure that the values always have correct types.