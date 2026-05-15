## Plan: Implement Solitaire command handling

TL;DR: Extend the current Klondike game state and command loop in `cs417/final_project/src/main.py` to support the `$$` stock draw command, `WW` waste stack, foundation movement commands like `AS`, and tableau move commands like `9C-XD` and `6H-7C`.

**Steps**
1. Review current game architecture in `cs417/final_project/src/main.py`, `src/deck.py`, and `src/stack.py`.
2. Refactor the main game state so it includes:
   - `stock` as existing `Deck`
   - `waste` stack named `WW`
   - four foundation stacks `CC`, `DD`, `HH`, `SS`
   - seven tableau piles `W1`..`W7` with face-down and face-up cards separately tracked
3. Implement a tableau pile abstraction:
   - support initial deal of 1..7 cards
   - flip the top card face-up after dealing
   - allow querying visible cards and moving a depot of cards from a visible card onward
4. Add command parsing and card parsing to support:
   - `$$` to draw up to three cards from stock into waste, recycling waste to stock when needed
   - card codes like `AC`, `2C`, `XH`, `JS`, `QS`, `KS`
   - move commands of the form `VR-VR` where both sides are card codes
   - singleton foundation commands like `AS` for the Ace of Spades to the Spades foundation
5. Implement movement rules and validation:
   - foundation build-up by suit from Ace through King
   - tableau build-down by alternate colors only
   - empty tableau piles accept only Kings or King-led depots
   - errors for invisible source cards, invalid destination rules, and invalid command syntax
6. Update rendering and output:
   - show `$$` stock line, `WW` waste top, foundations, and the full visible card lists for each tableau depot column
   - render state after each valid command and print error messages for invalid commands
7. Add tests or manual verification scenarios for the new commands:
   - `$$` with full stock and partial stock
   - stock recycle when empty
   - moving waste top to tableau or foundation
   - legal and illegal tableau moves
   - command parser edge cases

**Relevant files**
- `/workspaces/courses/cs417/final_project/src/main.py` — main game loop, state, command handling, rendering
- `/workspaces/courses/cs417/final_project/src/deck.py` — card representation and parsing behavior
- `/workspaces/courses/cs417/final_project/src/stack.py` — basic stack operations; may need extension or a new tableau class

**Confirmed Behavior**
1. Only `$$` is accepted for drawing from stock.
2. Single-token commands like `AS` should move that card to its foundation if legal.
3. Waste-to-tableau and waste-to-foundation moves are supported by the same `VR-VR` syntax, with the waste top card represented implicitly.
4. The tableau output should display the full list of visible cards in each depot column, following the examples in `design.md`.
5. The implementation keeps exact face-down/face-up tracking for each tableau pile, and depots are modeled as lists.
6. The top state line should render stock, waste, and foundations together as a single row.
7. Empty foundations render as `__`.
8. Empty waste renders as `__`.
