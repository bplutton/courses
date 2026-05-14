 1. If the user had to check multiple files, there would be no way of checking all of them.
    It would be more convenient if it had a way to enter each file name separately.
    Hard-coded things are hard to change.

    After: This change was not required.

 2. This program has a list of hard-coded categories. It should get the categories either from the user or from a file.

    After: This change was required.

 3. Different people might want the list to be in different orders.

    After: This change was not required.

*single responsibility*, *dependency injection*, *separation of I/O from logic*, *strategy / pluggable parts*.

Part 1: Design idea: Separation of I/O from logic

Part 2: Design idea: Single responsibility

Part 3: Design idea: Strategy / Pluggable parts

3. **The change request that hurt the most.** Which of the three was
   hardest, and why? What was your *first* attempt before you realized
   it wouldn't work?

   Part 1 was the hardest. This is because I tried to use argparse when it was unnecessary.

4. **One imagined future change.** If next week the requirement is
   *"now pull transactions from a remote API,"* walk through what you'd
   add or change in your refactored code. (You don't have to actually
   implement it. About a paragraph is enough.)

   If I were to call a remote API, I would expect the data to be in JSON.

   I already have a JSON-parsing function. I would just need to change "main()" to pull transactions from a
   remote API instead of a file.
