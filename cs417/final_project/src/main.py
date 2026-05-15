# CS 417, Yámato Lutton

"""Klondike solitaire command loop."""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

try:
    from .deck import Card, Deck
    from .stack import Stack
except ImportError:
    from deck import Card, Deck
    from stack import Stack


TABLEAU_NAMES = [f"W{i}" for i in range(1, 8)]
FOUNDATION_NAMES = ["CC", "DD", "HH", "SS"]
FOUNDATION_SUIT_MAP = {
    "CC": "Clubs",
    "DD": "Diamonds",
    "HH": "Hearts",
    "SS": "Spades",
}


class TableauPile:
    def __init__(self) -> None:
        self.face_down: Stack[Card] = Stack()
        self.face_up: List[Card] = []

    def push_face_down(self, card: Card) -> None:
        self.face_down.push(card)

    def add_face_up(self, card: Card) -> None:
        self.face_up.append(card)

    def make_visible_top(self) -> None:
        if len(self.face_up) == 0 and len(self.face_down) > 0:
            self.face_up.append(self.face_down.pop())

    def hidden_count(self) -> int:
        return len(self.face_down)

    def visible_cards(self) -> List[Card]:
        return list(self.face_up)

    def top_card(self) -> Optional[Card]:
        return self.face_up[-1] if self.face_up else None

    def is_empty(self) -> bool:
        return self.hidden_count() == 0 and len(self.face_up) == 0

    def get_depot(self, card_code: str) -> Optional[List[Card]]:
        for i, card in enumerate(self.face_up):
            if card.code == card_code:
                return self.face_up[i:]
        return None

    def remove_depot(self, card_code: str) -> Optional[List[Card]]:
        depot = self.get_depot(card_code)
        if depot is None:
            return None
        start = self.face_up.index(depot[0])
        self.face_up = self.face_up[:start]
        self.make_visible_top()
        return depot

    def add_depot(self, cards: List[Card]) -> None:
        self.face_up.extend(cards)


def render_game(
    stock: Deck,
    waste: Stack[Card],
    foundations: Dict[str, Stack[Card]],
    tableau: Dict[str, TableauPile],
) -> None:
    waste_top = str(waste.peek()) if len(waste) else "__"
    foundation_display = [str(foundations[name].peek()) if len(foundations[name]) else "__" for name in FOUNDATION_NAMES]
    # Print top row without labels or stock count: stock symbol, waste top, then foundations
    # Place three spaces between the waste stack and the first foundation
    # add one additional space to separate waste and foundations
    print(f"$$ {waste_top}    {foundation_display[0]} {foundation_display[1]} {foundation_display[2]} {foundation_display[3]}")
    print()

    max_depth = max(pile.hidden_count() + len(pile.face_up) for pile in tableau.values())
    for row in range(max_depth):
        row_cards: List[str] = []
        for name in TABLEAU_NAMES:
            pile = tableau[name]
            hidden = pile.hidden_count()
            if row < hidden:
                row_cards.append("##")
            else:
                visible_index = row - hidden
                if visible_index < len(pile.face_up):
                    row_cards.append(str(pile.face_up[visible_index]))
                else:
                    row_cards.append("__")
        print(" ".join(row_cards))
    print()


def parse_card(code: str) -> Card:
    try:
        return Card.from_code(code)
    except ValueError as error:
        raise ValueError("invalid card code") from error


def find_tableau_source(
    card_code: str,
    waste: Stack[Card],
    tableau: Dict[str, TableauPile],
) -> Optional[Tuple[str, str, List[Card]]]:
    if len(waste) and waste.peek().code == card_code:
        return "WW", "WW", [waste.peek()]
    for name, pile in tableau.items():
        depot = pile.get_depot(card_code)
        if depot is not None:
            return "tableau", name, depot
    return None


def find_tableau_destination(
    token: str,
    tableau: Dict[str, TableauPile],
) -> Optional[Tuple[str, Optional[Card], TableauPile]]:
    if token in tableau:
        return token, tableau[token].top_card(), tableau[token]
    for name, pile in tableau.items():
        top = pile.top_card()
        if top is not None and top.code == token:
            return name, top, pile
    return None


def can_move_to_tableau(source_cards: List[Card], dest_card: Optional[Card]) -> bool:
    source_top = source_cards[0]
    if dest_card is None:
        return source_top.rank == "K"
    return source_top.can_stack_on_tableau(dest_card)


def can_move_to_foundation(card: Card, foundation: Stack[Card], pile_name: str) -> bool:
    if FOUNDATION_SUIT_MAP[pile_name] != card.suit:
        return False
    if len(foundation) == 0:
        return card.rank == "A"
    top = foundation.peek()
    return card.can_stack_on_foundation(top)


def move_to_foundation(
    card_code: str,
    waste: Stack[Card],
    tableau: Dict[str, TableauPile],
    foundations: Dict[str, Stack[Card]],
) -> bool:
    source = find_tableau_source(card_code, waste, tableau)
    if source is None:
        print(f"Cannot find visible card {card_code}.")
        return False

    source_type, source_name, cards = source
    if len(cards) != 1:
        print("Only a single card can be moved to a foundation.")
        return False

    card = cards[0]
    foundation_name = next((name for name, suit in FOUNDATION_SUIT_MAP.items() if suit == card.suit), None)
    if foundation_name is None:
        print(f"No foundation for card {card_code}.")
        return False

    foundation = foundations[foundation_name]
    if not can_move_to_foundation(card, foundation, foundation_name):
        print(f"Cannot move {card_code} to foundation {foundation_name}.")
        return False

    if source_type == "WW":
        waste.pop()
    else:
        tableau[source_name].remove_depot(card_code)
    foundation.push(card)
    return True


def move_card_command(
    source_token: str,
    dest_token: str,
    waste: Stack[Card],
    tableau: Dict[str, TableauPile],
) -> bool:
    source_token = source_token.upper()
    dest_token = dest_token.upper()

    if source_token == "WW":
        if len(waste) == 0:
            print("Waste is empty.")
            return False
        source = ("WW", "WW", [waste.peek()])
    else:
        source = find_tableau_source(source_token, waste, tableau)
    if source is None:
        print(f"Source card {source_token} is not visible.")
        return False

    source_type, source_name, cards = source
    dest = find_tableau_destination(dest_token, tableau)
    if dest is None:
        print(f"Destination {dest_token} is not a visible tableau card or empty tableau pile.")
        return False

    _, dest_top, dest_pile = dest
    if not can_move_to_tableau(cards, dest_top):
        if dest_top is None:
            print("Only a King or a King-led depot can be moved to an empty pile.")
        else:
            print(f"Cannot move {source_token} onto {dest_top.code}.")
        return False

    if source_type == "WW":
        waste.pop()
    else:
        tableau[source_name].remove_depot(source_token)
    dest_pile.add_depot(cards)
    return True


def recycle_waste(stock: Deck, waste: Stack[Card]) -> None:
    while len(waste) > 0:
        stock._cards.insert(0, waste.pop())


def draw_from_stock(stock: Deck, waste: Stack[Card]) -> None:
    if len(stock) == 0 and len(waste) > 0:
        recycle_waste(stock, waste)

    count = min(3, len(stock))
    if count == 0:
        print("No cards left to draw.")
        return
    for _ in range(count):
        waste.push(stock.draw(1)[0])


def build_tableau(stock: Deck) -> Dict[str, TableauPile]:
    tableau: Dict[str, TableauPile] = {name: TableauPile() for name in TABLEAU_NAMES}
    for i, name in enumerate(TABLEAU_NAMES, start=1):
        for card_index in range(i):
            card = stock.draw(1)[0]
            if card_index < i - 1:
                tableau[name].push_face_down(card)
            else:
                tableau[name].add_face_up(card)
    return tableau


def game_won(foundations: Dict[str, Stack[Card]]) -> bool:
    return all(len(stack) == 13 for stack in foundations.values())


def has_legal_moves(
    stock: Deck,
    waste: Stack[Card],
    foundations: Dict[str, Stack[Card]],
    tableau: Dict[str, TableauPile],
) -> bool:
    if len(stock) > 0 or len(waste) > 0:
        return True

    for source_name, pile in tableau.items():
        visible_cards = pile.visible_cards()
        if not visible_cards:
            continue

        top_card = visible_cards[-1]
        foundation_name = next(
            (name for name, suit in FOUNDATION_SUIT_MAP.items() if suit == top_card.suit),
            None,
        )
        if foundation_name and can_move_to_foundation(top_card, foundations[foundation_name], foundation_name):
            return True

        for index in range(len(visible_cards)):
            depot = visible_cards[index:]
            for dest_name, dest_pile in tableau.items():
                if source_name == dest_name:
                    continue
                if can_move_to_tableau(depot, dest_pile.top_card()):
                    return True

    return False


def main() -> None:
    stock = Deck()
    stock.shuffle()
    waste: Stack[Card] = Stack()
    foundations: Dict[str, Stack[Card]] = {name: Stack() for name in FOUNDATION_NAMES}
    tableau = build_tableau(stock)

    render_game(stock, waste, foundations, tableau)

    while True:
        raw_input = input("Enter a command ($$, AS, 9C-XD, quit): ").strip()
        if not raw_input:
            continue
        command = raw_input.strip().upper()
        if command == "QUIT":
            print("Thanks for playing!")
            break
        if command == "$$":
            draw_from_stock(stock, waste)
            render_game(stock, waste, foundations, tableau)
            if not has_legal_moves(stock, waste, foundations, tableau):
                print("No legal moves remain. You have lost.")
                break
            continue

        if "-" in command:
            source_token, dest_token = (part.strip() for part in command.split("-", 1))
            if move_card_command(source_token, dest_token, waste, tableau):
                if game_won(foundations):
                    render_game(stock, waste, foundations, tableau)
                    print("Congratulations! You have completed the four foundations and won the game.")
                    break
                render_game(stock, waste, foundations, tableau)
                if not has_legal_moves(stock, waste, foundations, tableau):
                    print("No legal moves remain. You have lost.")
                    break
            continue

        try:
            card = parse_card(command)
        except ValueError:
            print("Unknown command. Please enter $$, a card code like AS, or a move like 9C-XD.")
            continue

        if move_to_foundation(command, waste, tableau, foundations):
            if game_won(foundations):
                render_game(stock, waste, foundations, tableau)
                print("Congratulations! You have completed the four foundations and won the game.")
                break
            render_game(stock, waste, foundations, tableau)
            if not has_legal_moves(stock, waste, foundations, tableau):
                print("No legal moves remain. You have lost.")
                break
        else:
            continue


if __name__ == "__main__":
    main()
