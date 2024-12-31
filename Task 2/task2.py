import random
import time
import sys

# Hope you don't cheat :)
DEBUG = False
 
# Constants
MAX_GUESSES = 6
MAX_TIMEOUT = 30
MAX_INVALID_WRONG = 3
WORD_LENGTHS = [4, 5, 6]
ALLOWED_WORDS = []  # List of valid words from the dictionary

player_username = "Guest"  # Default username if they opt out
word_to_guess = ""  # The word to guess
difficulty = 5  # Default difficulty level (5 letters)
invalid_wrong_count = 0

used_letters = []
last_guess = []
clue_history = []  # Stores clues and guesses
hint_used = False  # Tracks if hint is used
hint_words = []

# Game Modes
MODES = ["Normal", "Hard"]
mode = "Normal"  # Default mode

#
# MENU LOGIC
#


def display_menu():
    """Display the menu for selecting difficulty and game mode."""
    global difficulty
    global mode
    print("\n--| Welcome to Wordle Game |--")
    print(f"\nDifficulty: {difficulty} letters - Gamemode: {mode}\n")
    print(" 1. Select Difficulty")
    print(" 2. Select Gamemode")
    print(" 3. Start Game")
    print(" 4. View Rules")
    print(" 5. View Leaderboard")
    print(" 6. Exit")
    
    try:
        choice = int(input("Please select an option (1-6): "))
        if choice == 1:
            select_difficulty()
        elif choice == 2:
            select_mode()
        elif choice == 3:
            start_game()
        elif choice == 4:
            display_rules()
        elif choice == 5:
            display_leaderboard()
        elif choice == 6:
            sys.exit()
        else:
            print("Invalid option. Please select a valid number.")
            display_menu()
    except ValueError:
        print("Please enter a valid number.")
        display_menu()

def select_difficulty():
    """Allow the player to select the difficulty level."""
    global difficulty
    while True:
        print("\n--| Difficulty Menu |--")
        print("1. 4 Letters")
        print("2. 5 Letters")
        print("3. 6 Letters")
        try:
            choice = int(input("Select difficulty (1-3): "))
            if choice == 1:
                difficulty = 4
                print("Difficulty set to 4 letters.")
                break
            elif choice == 2:
                difficulty = 5
                print("Difficulty set to 5 letters.")
                break
            elif choice == 3:
                difficulty = 6
                print("Difficulty set to 6 letters.")
                break
            else:
                print("Invalid choice, please select between 1-3.")
        except ValueError:
            print("Please enter a valid number.")
        
    display_menu()

def select_mode():
    """Allow the player to select the game mode."""
    global mode
    while True:
        print("\n--| Game Mode Menu |--\n")
        print("1. Normal (No time limit)")
        print("2. Hard (include letters marked as * and + in subsequent guesses)")
        try:
            choice = int(input("Select game mode (1-2): "))
            if choice == 1:
                mode = "Normal"
                print("Game mode set to Normal.")
                break
            elif choice == 2:
                mode = "Hard"
                print("Game mode set to Hard.")
                break
            else:
                print("Invalid choice, please select between 1-2.")
        except ValueError:
            print("Please enter a valid number.")
        
    display_menu()

def display_rules():
    """Display the game rules in a clear and engaging way."""
    print("\n--| Wordle Game Rules |--")
    print("=" * 30)
    print("\n1. The Goal:")
    print("   - Guess the word!")
    print("   - The game randomly selects a word from a dictionary.")
    print("   - You have 6 attempts to guess it.")
    print("   - Each guess must be a valid word of the selected difficulty.\n")
    
    print("2. Clues:")
    print("   - After each guess, you'll get a clue.")
    print("   - '*' means the letter is in the correct position.")
    print("   - '+' means the letter is in the word but in the wrong position.")
    print("   - '_' means the letter is NOT in the word at all.\n")
    
    print("3. Example: Guessing 'crate' for a 5-letter word")
    print("   - Word to guess: 'grape'")
    print("   - Guess: 'crate' => Clue: '* _ + * _'")
    print("     - The first and fourth letters are correct.")
    print("     - The letter 'r' is in the word, but not in the second position.")
    print("     - The other letters aren't in the word.\n")
    
    print("4. Hints and Help:")
    print("   - You can ask for a hint once per game. This will reveal a letter in the word.")
    print("   - The help option will provide possible words based on the clues you've gathered so far.")
    print("   - Be strategic about using them – especially the hint, as you only get one!\n")
    
    print("5. Winning and Losing:")
    print("   - If you guess the word within 6 attempts, you win!")
    print("   - If you use all attempts without guessing correctly, you lose.")
    print("   - After the game, your score (time and attempts) will be recorded.\n")
    
    print("6. Leaderboard:")
    print("   - Top players' results are recorded in the leaderboard.")
    print("   - The leaderboard shows your username, the difficulty level, your average time, and tries.")
    print("\nGood luck, and may the best guesser win!\n")
    display_menu()

#
# GAME LOGIC
#

def load_words(filename):
    """Load words from a dictionary file based on selected difficulty."""
    global ALLOWED_WORDS
    try:
        with open(filename, 'r') as f:
            ALLOWED_WORDS = [line.strip().lower() for line in f if len(line.strip()) == difficulty]
    except FileNotFoundError:
        print("Dictionary file not found.")
        
        sys.exit()


def display_leaderboard():
    """Display the leaderboard of past winners."""
    try:
        with open("winners.txt", "r") as f:
            print("\n--| Leaderboard |--")
            print("Rank | User - Difficulty - Avg Time(s) - Tries")
            count = 0
            for line in f:
                print(f"#{count + 1} | {line.strip()}")
                count += 1
    except FileNotFoundError:
        print("No previous winners found.")

def get_username():
    """Get the username of the player."""
    global player_username
    user_opt = input("Would you like to create a username? (yes/no): ").strip().lower()
    if user_opt == "yes" or user_opt == "y":
        player_username = input("Enter your username: ").strip()
    else:
        print(f"Username set to default: {player_username}")

def select_random_word():
    """Select a random word from the allowed words list."""
    global word_to_guess
    word_to_guess = random.choice(ALLOWED_WORDS)

def get_guess(turn):
    """Prompt the user to enter a guess and validate it."""
    global word_to_guess, invalid_wrong_count, MAX_INVALID_WRONG
    start_time = time.time()  # Record time when the guess is initiated
    try:   
        while True:
            time_left = MAX_TIMEOUT - int(time.time() - start_time)  # Calculate remaining time
            if time_left <= 0:
                print("Time's up! Your turn is lost.")
                return None
            
            print(f"You have {MAX_GUESSES - turn} tries left.")
            print(f"Your guess (You have {time_left} seconds): ", end="")
            guess = input().strip().lower()

            # Check if the guess length matches the selected difficulty
            if len(guess) != difficulty:
                print(f"Please enter a {difficulty}-letter word.")
            elif guess not in ALLOWED_WORDS:
                print(f"'{guess}' is not a valid word. Try again.")
                invalid_wrong_count += 1
                print(f"You have {MAX_INVALID_WRONG - invalid_wrong_count} until you lose this turn.")
                if MAX_INVALID_WRONG <= invalid_wrong_count:
                    print(f"You did not use a word inside the Dictionary. You have lost a turn.")
                    invalid_wrong_count = 0
                    return None 
            else:
                # The guess is valid
                last_guess.append(guess)
                for char in guess:
                    used_letters.append(char)
                return guess

    except KeyboardInterrupt:
        quit_prompt = int(input("\nDo you wish to give up? [1: Yes 2: No] \n> "))
        if quit_prompt == 1:
            print("\nThank you for playing!")
            display_leaderboard()
            print(f"\nThe correct word was '{word_to_guess}'")
            display_menu()
        else:
            get_guess(turn)


def provide_clue(guess, correct_word):
    """Generate and return a clue based on the guess."""
    clue = ['_'] * len(guess)  # Start with underscores for all letters.
    word_copy = list(correct_word)
    
    # First pass: check for exact matches ('*')
    for i in range(len(guess)):
        if guess[i] == correct_word[i]:
            clue[i] = '*'  # Correct position
            word_copy[i] = None  # Mark this position as already used
    
    # Second pass: check for wrong position matches ('+')
    for i in range(len(guess)):
        if clue[i] == '_':  # Only check if the letter hasn't been matched already
            if guess[i] in word_copy:
                clue[i] = '+'  # Correct letter, wrong position
                word_copy[word_copy.index(guess[i])] = None  # Remove this letter from further checks
    
    # Remaining clues are '_'
    
    return " ".join(clue)


def print_game_status(guess, clue):
    """Print the game status, including the clue and the letters used so far."""
    global used_letters, last_guess
    print(f"\nUsed Letters: {used_letters}\n")
    
    print(f"Guess: {guess}")
    print(f"Clue: {clue}")

    print(f"{len(last_guess)}")
    if len(last_guess) > 0: 
        print(f"\nYour last guess was {last_guess[len(last_guess) - 1]}")


def hint():
    """Provide a random letter from the word without revealing its position."""
    global hint_used
    if hint_used:
        print("You have already used your hint.")
        return
    hint_used = True
    revealed_letter = random.choice(word_to_guess)
    print(f"Hint: The word contains the letter '{revealed_letter}'")

def help_words():
    """Provide possible words based on known correct letters and positions."""
    global hint_words
    known_correct = [c for i, c in enumerate(last_guess[-1]) if clue_history[-1][1][i] == '*']
    possible_words = [word for word in ALLOWED_WORDS if all(letter in word for letter in known_correct)]
    hint_words = possible_words
    print("Possible words: ", ', '.join(possible_words))


def save_winner(time_taken, tries):
    """Save the winner to the 'winners.txt' file."""
    global player_username, difficulty
    with open("winners.txt", "a") as f:
        f.write(f"{player_username} - {difficulty} - {time_taken:.2f}s - {tries}\n")
    print("Your result has been saved to the leaderboard.")

def start_game():
    """Start the game loop and allow the player to guess the word."""
    global word_to_guess, clue_history, hint_used, help_used, player_username, invalid_wrong_count
    get_username()
    select_random_word()  # Ensure a word is selected at the start
    print(f"Welcome to Wordle, {player_username}!")
    if DEBUG:
        print(f"[*] DEBUG: The word is {word_to_guess}")
    

    game_header()
    print(f"Try to guess the {difficulty}-letter word")
    print(f"    You have {MAX_GUESSES} attempts.\n")

    start_time = time.time()  # Record overall game start time
    for turn in range(MAX_GUESSES):
        guess = get_guess(turn)  # This handles the timed guesses
        if guess is None:
            continue  # If time is up, continue to the next turn
       
        clue = provide_clue(guess, word_to_guess)  # Generate the clue based on the guess
        clue_history.append((guess, clue))
        
        print_game_status(guess, clue)
        
        if guess == word_to_guess:
            end_time = time.time()  # Calculate the time taken
            time_taken = end_time - start_time
            print(f"Congratulations, {player_username}! You've guessed the word in {time_taken:.2f} seconds.")
            save_winner(time_taken, turn + 1)
            break
    else:
        print(f"Sorry, you've used all {MAX_GUESSES} guesses. The word was: {word_to_guess}")
        
        # Reset the other values - Just in case
        player_username = ""
        invalid_wrong_count = 0
    display_menu()


def game_header():
    print("\n    -| Wordle |-    ")

try:
    load_words("dictionary.txt")
    display_menu()
except KeyboardInterrupt as e:
    print("\nExiting the game.. Thank you for playing.")
