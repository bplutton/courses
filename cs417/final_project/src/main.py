# CS 417, Yámato Lutton

"""
This program lets people play Klondike Solitaire on a terminal.
"""

from deck import Deck
from stack import Stack


def print_tableau(stock: Deck, waste: Stack, working_stacks: dict[str, Stack]) -> None:
    """
    $$ WW

    ?0 ?1 ?2 ?3 ?4 ?5 ?6

    where ?n represents a random upturned card (?) placed on top of a stack
    of n downturned cards, $$ is the stock of remaining cards, and WW is the
    waste top card.
    """
    print("$$", str(waste.peek()) if len(waste) else "__")
    print()
    top_cards = []
    for i in range(1, 8):
        stack = working_stacks[f"W{i}"]
        top_cards.append(str(stack.peek()) if len(stack) else "__")
    print(" ".join(top_cards))


def main() -> None:
    stock = Deck()    # Initialize a standard 52-card deck
    stock.shuffle()   # Shuffle the deck before drawing
    waste = Stack()

    working_stacks = {f"W{i}": Stack() for i in range(1, 8)}

    # Deal cards from stock into W1 through W7:
    for i in range(1, 8): # Runs for each stack W1..W7, where i is also the number of cards to draw for that stack
        stack_name = f"W{i}"
        for _ in range(i):
            card = stock.draw(1)[0] # Draw one card at a time from the stock, and get the single Card object from the list
            working_stacks[stack_name].push(card) # Push card onto the appropriate working stack

    print_tableau(stock, waste, working_stacks) # Print the initial tableau after dealing cards

    while True:
        command = input("Enter a command (e.g., '$$', 'quit'): ").strip().lower()
        if command == "quit":
            print("Thanks for playing!")
            break
        elif command == "$$":
            if len(stock) == 0:
                while len(waste) > 0:
                    stock._cards.insert(0, waste.pop())
            for _ in range(min(3, len(stock))):
                waste.push(stock.draw(1)[0])
            print_tableau(stock, waste, working_stacks)
        elif command.startswith("move"):
            # This is where you would implement the logic to move cards between stacks
            print("Move command received. (This feature is not implemented yet.)")
        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()
