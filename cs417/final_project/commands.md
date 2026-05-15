The syntax of commands is as follows:

## Examples

$$     # Pops three cards from stock and pushes them onto waste stack. If there are fewer than
       # three cards, then pop the remaining cards. If there are no remaining cards, pop all
       # of the cards in the waste stack and push them onto stock, then pop up to three cards
       # back to waste as described previously.

AS     # Moves the Ace of Spades to the Spade foundation. If the Ace of Spades is not visible,
       # return an error.

9C-XD  # Moves the 9 of Clubs on top of the 10 of Diamonds. If the 9 of Clubs is not visible,
       # return an error. If there is a depot of cards on top of the 9 of Clubs, move
       # the entire depot as a unit.

6H-7C  # Moves the 6 of Hearts on top of the 7 of Clubs. If the 6 of Hearts is not visible,
       # return an error. If there is a depot of cards on top of the 6 of Hearts, move
       # the entire depot as a unit.

## Command Structure

The commands are modeled on chess notation: VR-VR, where "V" represents the value of a card
and "R" represents the rank. This command format moves the card on the left onto the card
on the right.

## Rules for Movement

-   The four [foundations](https://en.wikipedia.org/wiki/Glossary_of_patience_terms#foundation) are [built up](https://en.wikipedia.org/wiki/Glossary_of_patience_terms#build_up) by [suit](https://en.wikipedia.org/wiki/Playing_card_suit) from [Ace](https://en.wikipedia.org/wiki/Ace) (low in this game) to [King](https://en.wikipedia.org/wiki/King_(playing_card)), and the tableau piles can be [built down](https://en.wikipedia.org/wiki/Glossary_of_patience_terms#build_down) by [alternate colors](https://en.wikipedia.org/wiki/Glossary_of_patience_terms#alternating_colour).
-   Every face-up card in a partial pile, or a complete pile, can be moved, as a unit, to another tableau pile on the basis of its highest card.
-   Any empty piles can be filled with a King, or a pile of cards with a King.
-   Three cards can be turned at once from the stock to the waste with no limit on passes through the deck.

