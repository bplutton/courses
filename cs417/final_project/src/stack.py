from __future__ import annotations

from typing import Generic, Iterable, Iterator, List, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """A simple last-in, first-out stack."""

    def __init__(self, items: Iterable[T] | None = None) -> None:
        self._items: List[T] = list(items) if items is not None else []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __repr__(self) -> str:
        return f"Stack({list(self._items)!r})"
