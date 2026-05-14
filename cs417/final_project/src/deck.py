from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Iterator, List

SUITS = ("Clubs", "Diamonds", "Hearts", "Spades")
RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")


@dataclass(frozen=True)
class Card:
    rank: str
    suit: str

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __repr__(self) -> str:
        return f"Card(rank={self.rank!r}, suit={self.suit!r})"


class Deck:
    """A standard 52-card deck.

    The deck is initialized in a sorted order by suit then rank. Use :meth:`shuffle`
    to randomize card order before drawing.
    """

    def __init__(self) -> None:
        self._original: List[Card] = [Card(rank, suit) for suit in SUITS for rank in RANKS]
        self._cards: List[Card] = list(self._original)

    def shuffle(self) -> None:
        """Shuffle the remaining cards in the deck."""
        random.shuffle(self._cards)

    def reset(self) -> None:
        """Reset the deck to the original ordered 52 cards."""
        self._cards = list(self._original)

    def draw(self, count: int = 1) -> List[Card]:
        """Draw one or more cards from the top of the deck.

        Args:
            count: Number of cards to draw.

        Returns:
            A list of drawn Card objects.

        Raises:
            ValueError: If the requested count is more than the cards left.
        """
        if count < 1:
            raise ValueError("draw count must be at least 1")
        if count > len(self._cards):
            raise ValueError(f"cannot draw {count} cards from deck with {len(self._cards)} cards")

        drawn = self._cards[:count]
        self._cards = self._cards[count:]
        return drawn

    def deal(self, hands: int, cards_per_hand: int) -> List[List[Card]]:
        """Deal cards into a specified number of hands."""
        total = hands * cards_per_hand
        if total > len(self._cards):
            raise ValueError("not enough cards to deal")

        dealt: List[List[Card]] = []
        for _ in range(hands):
            dealt.append(self.draw(cards_per_hand))
        return dealt

    def peek(self, count: int = 1) -> List[Card]:
        """Return the next card(s) without removing them from the deck."""
        if count < 1:
            raise ValueError("peek count must be at least 1")
        if count > len(self._cards):
            raise ValueError(f"cannot peek {count} cards from deck with {len(self._cards)} cards")
        return list(self._cards[:count])

    def is_empty(self) -> bool:
        return len(self._cards) == 0

    def count(self) -> int:
        return len(self._cards)

    def __len__(self) -> int:
        return len(self._cards)

    def __iter__(self) -> Iterator[Card]:
        return iter(self._cards)

    def __repr__(self) -> str:
        return f"Deck({len(self._cards)} cards)"
