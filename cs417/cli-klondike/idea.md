Checkpoint 1 — Problem Statement

What problem are you solving? One or two sentences, plain English. Assume I don't know the domain.
I am going to create a Klondike Solitaire game that runs on a command line.

Why does this problem matter? Who has it, and what's annoying or broken about the current situation?
This problem matters because some people might want to play Klondike Solitaire in a retro style. This can also be used to train an AI agent to play solitaire.

What would "working" look like? If your project succeeds, what can a user actually do that they couldn't before?
A user would be able to play solitaire on a terminal and train an AI to do the same.
It would look a bit like this:

$$       00 00 00 00

2D $$ $$ $$ $$ $$ $$
   7C $$ $$ $$ $$ $$
      JH $$ $$ $$ $$
         5C $$ $$ $$
            XD $$ $$
               QS $$
                  8H

> $$

$$ AS    00 00 00 00

2D $$ $$ $$ $$ $$ $$
   7C $$ $$ $$ $$ $$
      JH $$ $$ $$ $$
         5C $$ $$ $$
            XD $$ $$
               QS $$
                  8H

> AS

$$ 9C    AS 00 00 00

2D $$ $$ $$ $$ $$ $$
   7C $$ $$ $$ $$ $$
      JH $$ $$ $$ $$
         5C $$ $$ $$
            XD $$ $$
               QS $$
                  8H

> 9C-XD

$$ 6H    AS 00 00 00

2D $$ $$ $$ $$ $$ $$
   7C $$ $$ $$ $$ $$
      JH $$ $$ $$ $$
         5C $$ $$ $$
            XD $$ $$
            9C QS $$
                  8H

> 6H-7C

$$       AS 00 00 00

2D $$ $$ $$ $$ $$ $$
   7C $$ $$ $$ $$ $$
   6H JH $$ $$ $$ $$
         5C $$ $$ $$
            XD $$ $$
            9C QS $$
                  8H

