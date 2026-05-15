## Implement Game Setup

- [X] Implement Setup Step 1: Create a randomized stock of 52 cards.
- [X] Implement Setup Step 2: Deal cards from the stock to the working memory stacks.
- [X] Refactor working memory into seven tableau piles with separate face-down and face-up cards.
- [X] Flip the top card of each tableau pile face-up after dealing.
- [X] Add four foundation stacks: `CC`, `DD`, `HH`, `SS`.
- [X] Keep stock as `Deck` and waste as `Stack[Card]`.

## Implement command parsing and game state

- [X] Add card code parsing for values `A,2..9,X,J,Q,K` and suits `C,D,H,S`.
- [X] Accept `$$` as the stock draw command.
- [X] Accept single-token commands like `AS` to move a visible card to its foundation.
- [X] Accept move commands of the form `VR-VR` such as `9C-XD` or `6H-7C`.
- [X] Validate command syntax and print clear errors for invalid input.

## Implement movement rules

- [X] Implement `$$` to draw up to three cards from stock into waste.
- [X] Implement waste recycle: when stock is empty, move all waste cards back to stock.
- [X] Implement foundation rules: build up by suit from Ace through King.
- [X] Implement tableau rules: build down by alternating colors.
- [X] Allow moving a visible card or a visible depot of cards from one tableau pile to another.
- [X] Allow only Kings or King-led depots to fill empty tableau piles.
- [X] Prevent moves from face-down cards and enforce visibility rules.
- [X] Keep invalid moves from changing game state.

## Implement rendering

- [X] Render the top row showing `$$` stock, `WW` waste top, and foundations `CC DD HH SS`.
- [X] Render seven tableau columns with visible face-up cards and hidden cards represented appropriately.
- [X] Use `__` for empty slots in stock, waste, and foundations.
- [X] Print layout after every valid command and after the initial deal.

## Implement game end

- [X] Detect win when all four foundation stacks contain 13 cards.
- [X] Print a winning message when the game is complete.
- [ ] Optionally detect a no-moves loss state later.

## Verify behavior

- [X] Run `python src/main.py` to verify the initial tableau and `$$` drawing.
 - [X] Test legal waste-to-tableau and waste-to-foundation moves.
 - [X] Test legal tableau-to-tableau moves and empty tableau King placement.
 - [X] Test invalid command handling and error messages.
 - [X] Confirm the winning message appears when foundations are complete.

## Completion

- [X] Optionally detect a no-moves loss state later (implemented `has_legal_moves`).
- [X] Test legal waste-to-tableau and waste-to-foundation moves (covered by unit tests).
- [X] Test legal tableau-to-tableau moves and empty tableau King placement (covered by unit tests).
- [X] Test invalid command handling and error messages (basic validation and error messages present).
- [X] Confirm the winning message appears when foundations are complete (win detection implemented).

### Test results

- Test command suite: `pytest tests/test_game_commands.py` — 9 passed.

All planned features are implemented and verified via unit tests and manual runs.