# Task 1 (20%): Number Statistics

In this task, you are asked to write a Python3 script (`task1.py`) that:

- Prompts the user to input **only positive integer numbers** at the terminal (numbers with decimals, negative numbers, or characters will not be accepted).
- Assigns those numbers to a list, removes any duplicate numbers, and informs the user of the removed duplicates.
- Counts the number of unique numbers in the list.
- Calculates the product, range, and variance of the numbers.
- Identifies the even and odd numbers from the list and stores them in separate lists. 
  - If the list of even numbers is empty, print a message saying "No even numbers were provided."
  - If the list of odd numbers is empty, print a message saying "No odd numbers were provided."
- Prints all the above information to the terminal.

**Important Notes:**

- The script should start and end without issues. There should be no 'crashing' or 'unhandled exceptions' due to erroneous input.
- The use of any built-in method that performs the above operations is **not allowed**.
- Importing of modules is also **not allowed**.
- The code must be commented, including header comments and inline comments following the PEP 8 style.
- Consideration must be given to the naming convention of variables and function names.

# Task 2 (80%): Variant of the Wordle Game

**Background**: Wordle is a word-based game released in 2013, where a user must guess a 5-letter word within six tries. For this task, you will develop a variant of the game as described below.

## Task Description
Implement a Python3 script (`task2.py`) with multiple functions and appropriate comments following PEP 8 guidelines. The game should be playable via the terminal (graphical user interface is not required).

### Basic Features:

- The script will randomly select one 5-letter word from a given dictionary (`dictionary.txt`). This random word is the answer the user must find within six turns.
- During each turn, the user provides a word as a guess.
  - This word must be a real word, i.e., a word that exists within the dictionary.
  - If the word does not exist, the user gets a warning and loses a turn.
- After every guess, the code should provide a clue by assigning the symbols `*`, `+`, and `_` for each letter of the guess:
  - `*` indicates that the letter is correct and in the correct position.
  - `+` means that the corresponding letter is in the answer but not in the right position.
  - `_` indicates that the corresponding letter is not in the answer at all.
  - The above symbols should be separated by spaces when printed at the terminal.
  - **Example**: if the user’s guess is `audio` and the provided clue is `_ * _ + _`, it means that the letter `u` is in the correct position, `i` is in the answer but not at the correct position, and `a`, `d`, and `o` are not part of the random word.
- Multiple instances of the same letter in a guess (e.g., the "o"s in "robot") will be assigned `*` or `+` only if the letter also appears multiple times in the answer. Otherwise, all repeated letters will be assigned `_`.
- The player should have the option to give up anytime by ending the game using an appropriate input. In this case, the randomly selected word should be revealed.
- If the player fails to find the answer within six turns or gives up, they lose the game. If they find the correct answer, they win the game. An appropriate message should be printed in both cases.

### Desired Features:

- At the beginning of the game, the code should prompt the user to provide a name or alias and measure the time in seconds needed to solve the puzzle. This info should be stored in a `winners.txt` file, updated only after a win.
- The user may opt to see past winners and their times (contents of `winners.txt`) before starting a puzzle.
- After each guess, the program should:
  - Provide the clue.
  - Display a list of all letters used by the user that are not part of the correct answer.
- The player has 30 seconds to make a guess. If they provide a word after 30 seconds, their turn is lost.
- Any erroneous input from the player should be handled appropriately, with no crashes or unhandled exceptions.

### Advanced Features:

- The player can select to play with a four, five, or six-letter word and can also choose a "hard mode" for each:
  - In hard mode, players must include letters marked as `*` and `+` in subsequent guesses.
- The player has the option to use a hint **only once**. This hint will reveal a letter that is part of the answer without specifying its location. The player loses one turn when using the hint.
- The player can ask for help with vocabulary. This will provide all tentative solutions in the dictionary that match the clues given so far.

**Important Notes:**

- You may only import the following four modules: `time`, `sys`, `random`, and `NumPy`. Any other modules except user-defined ones are **prohibited**.
- The program should run “cleanly” with no errors at the start or end.
- There should be no "crashing" or "unhandled exceptions" due to erroneous input.
- The code must be commented, including header comments and inline comments, following PEP 8 guidelines.
- Consideration must be given to naming conventions for variables and function names.
