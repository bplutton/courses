CLI Klondike

[Klondike Solitaire](https://en.wikipedia.org/wiki/Klondike_(solitaire)) is an unreliable stack sorting process implemented with a physical deck of 52 playing cards and a human.

The goal of this project is to demonstrate the use of stacks by implementing a Python version of Klondike Solitaire that runs in a terminal.

# Starting State

The starting state consists of a randomized deck of 52 cards:

\$\$

# Objective

The objective is to sort the deck into stacks alphabetically by suit (Clubs = C, Diamonds = D, Hearts = H and Spades = S) and within each of those stacks by numeric value (Ace = 1, 2, 3 … 10, J = 11, Q = 12, K = 13). The desired ending state is four stacks (C through S) called the “foundations” with the lowest value (A) at the bottom and the highest value (K) at the top:

\$\$ =\> KC KD KH KS

# “Working Memory”

Working memory consists of eight stacks and seven lists. The first seven stacks range in capacity from one card through seven (a total capacity of 28 cards):

W1 W2 W3 W4 W5 W6 W7

The remainder of the deck is a stack of 24 cards randomly selected and ordered cards called the “[stock](https://en.wikipedia.org/wiki/Talon_(cards))”.

Visually, this collection of stacks is represented thusly, with \$\$ representing the stock, W1, W2, W3, … W7 and WW (called the “[waste](https://en.wikipedia.org/wiki/Solitaire_terminology)”) representing the working memory, and CC, DD, HH and SS representing the foundations.

\$\$ WW CC DD HH SS

W1 W2 W3 W4 W5 W6 W7

# Rules

## Setup

1.  Twenty-eight cards are dealt from a randomized deck of 52 face down to working memory stacks W1 through W7 (one to W1, two to W2, three to W3, et cetera).
2.  The top card of each working memory stack is turned face up to create a “tableau” (several “depots”, where columns of overlapping cards may be formed by the human).

After setup the “layout” of cards dealt to the table looks like this, where ?n represents a random upturned card (?) placed on top of a stack of n downturned cards and \$\$ is the stock of 24 randomized cards.

\$\$

?0 ?1 ?2 ?3 ?4 ?5 ?6

## Play (The “Sorting Process”)

-   The four [foundations](https://en.wikipedia.org/wiki/Glossary_of_patience_terms#foundation) are [built up](https://en.wikipedia.org/wiki/Glossary_of_patience_terms#build_up) by [suit](https://en.wikipedia.org/wiki/Playing_card_suit) from [Ace](https://en.wikipedia.org/wiki/Ace) (low in this game) to [King](https://en.wikipedia.org/wiki/King_(playing_card)), and the tableau piles can be [built down](https://en.wikipedia.org/wiki/Glossary_of_patience_terms#build_down) by [alternate colors](https://en.wikipedia.org/wiki/Glossary_of_patience_terms#alternating_colour).
-   Every face-up card in a partial pile, or a complete pile, can be moved, as a unit, to another tableau pile on the basis of its highest card.
-   Any empty piles can be filled with a King, or a pile of cards with a King.
-   Three cards can be turned at once from the stock to the waste with no limit on passes through the deck.

## Winning

When a stack of cards starting with Ace and ending with King, all of the same suit, is on each of the four foundations the player has won.

## Losing

When no meaningful (non-repetitive) play remains the player has lost.

# CLI

-   The terminal interface is modeled on chess notation:  
    XX – YY means “place card XX (including any on top of it in a pile) on card YY”.
-   Cards are named “AC (ace of clubs) through “KS” (king of spades).
-   There are variations as needed, such as:  
    SS means “turn three cards at once from the stock to the waste”.

# Output

After each valid command the new layout is rendered.

After each invalid command an error message is displayed.