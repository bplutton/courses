import pytest

from src.deck import Card, Deck
from src.main import TableauPile, has_legal_moves, move_card_command, move_to_foundation, parse_card
from src.stack import Stack


def test_parse_card_valid() -> None:
    assert parse_card("AS") == Card(rank="A", suit="Spades")
    assert parse_card("XH") == Card(rank="10", suit="Hearts")
    assert str(parse_card("10C")) == "XC"


def test_parse_card_invalid() -> None:
    with pytest.raises(ValueError):
        parse_card("1Z")


def test_move_to_foundation_from_waste() -> None:
    waste = Stack()
    waste.push(Card.from_code("AS"))
    tableau = {f"W{i}": TableauPile() for i in range(1, 8)}
    foundations = {name: Stack() for name in ["CC", "DD", "HH", "SS"]}

    assert move_to_foundation("AS", waste, tableau, foundations)
    assert len(foundations["SS"]) == 1
    assert foundations["SS"].peek() == Card.from_code("AS")
    assert len(waste) == 0


def test_move_waste_king_to_empty_tableau() -> None:
    waste = Stack()
    waste.push(Card.from_code("KD"))
    tableau = {f"W{i}": TableauPile() for i in range(1, 8)}

    assert move_card_command("WW", "W1", waste, tableau)
    assert len(waste) == 0
    assert tableau["W1"].visible_cards() == [Card.from_code("KD")]


def test_move_waste_nonking_to_empty_tableau_fails() -> None:
    waste = Stack()
    waste.push(Card.from_code("QD"))
    tableau = {f"W{i}": TableauPile() for i in range(1, 8)}

    assert not move_card_command("WW", "W1", waste, tableau)
    assert len(waste) == 1
    assert tableau["W1"].is_empty()


def test_has_legal_moves_with_stock() -> None:
    stock = Deck()
    tableau = {f"W{i}": TableauPile() for i in range(1, 8)}
    foundations = {name: Stack() for name in ["CC", "DD", "HH", "SS"]}

    assert has_legal_moves(stock, Stack(), foundations, tableau)


def test_has_legal_moves_with_no_draw_but_tableau_move() -> None:
    stock = Deck()
    stock._cards.clear()
    waste = Stack()
    tableau = {f"W{i}": TableauPile() for i in range(1, 8)}
    tableau["W1"].add_face_up(Card.from_code("9H"))
    tableau["W2"].add_face_up(Card.from_code("XC"))
    foundations = {name: Stack() for name in ["CC", "DD", "HH", "SS"]}

    assert has_legal_moves(stock, waste, foundations, tableau)


def test_has_no_legal_moves() -> None:
    stock = Deck()
    stock._cards.clear()
    waste = Stack()
    tableau = {f"W{i}": TableauPile() for i in range(1, 8)}
    tableau["W1"].add_face_up(Card.from_code("2C"))
    tableau["W2"].add_face_up(Card.from_code("2D"))
    foundations = {name: Stack() for name in ["CC", "DD", "HH", "SS"]}

    assert not has_legal_moves(stock, waste, foundations, tableau)


def test_move_depot_between_tableau() -> None:
    tableau = {f"W{i}": TableauPile() for i in range(1, 8)}
    tableau["W1"].add_face_up(Card.from_code("9H"))
    tableau["W1"].add_face_up(Card.from_code("8C"))
    tableau["W2"].add_face_up(Card.from_code("XC"))

    assert move_card_command("9H", "XC", Stack(), tableau)
    assert [card.code for card in tableau["W2"].visible_cards()] == ["XC", "9H", "8C"]
    assert tableau["W1"].is_empty()
