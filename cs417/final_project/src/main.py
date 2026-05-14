# CS 417, Yámato Lutton

"""
This program lets people play Klondike Solitaire on a terminal.
"""

from deck import Deck
from stack import Stack


def main() -> None:
    stock = Deck()    # Initialize a standard 52-card deck
    stock.shuffle()   # Shuffle the deck before drawing

    working_stacks = {f"W{i}": Stack() for i in range(1, 8)}

    # Deal cards from stock into W1 through W7:
    for i in range(1, 8): # Runs for each stack W1..W7, where i is also the number of cards to draw for that stack
        stack_name = f"W{i}"
        for _ in range(i):
            card = stock.draw(1)[0] # Draw one card at a time from the stock, and get the single Card object from the list
            working_stacks[stack_name].push(card) # Push card onto the appropriate working stack

    # Debugging output: show cards in each stack W1..W7
    for name, stack in working_stacks.items():
        print(f"{name}: {list(stack)}")


if __name__ == "__main__":
    main()
