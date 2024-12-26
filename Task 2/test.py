import random
def provide_clue(guess, word_to_guess):
    """Generate and return a clue based on the guess."""
    clue = ['_'] * len(guess)  # Start with underscores for all letters.
    word_copy = list(word_to_guess) 
    
    # First pass: check for exact matches ('*')
    for i in range(len(guess)):
        if guess[i] == word_to_guess[i]:
            clue[i] = '*'  # Correct position
            word_copy[i] = None  # Mark this position as already used
    
    # Second pass: check for wrong position matches ('+')
    for i in range(len(guess)):
        if clue[i] == '_':  # Only check if the letter hasn't been matched already
            if guess[i] in word_copy:
                clue[i] = '+'  # Correct letter, wrong position
                word_copy[word_copy.index(guess[i])] = None  # Remove this letter from further checks
    
    return " ".join(clue)

def random_test_clue_generation():
    """Test the clue generation function with random guesses from the dictionary."""
    
    # Load all words from the dictionary file
    try:
        with open("dictionary.txt", "r") as f:
            allowed_words = [line.strip().lower() for line in f.readlines() if len(line.strip()) == 5]
    except FileNotFoundError:
        print("The dictionary file was not found.")
        return

    # Randomly test clues for every word in the dictionary
    for word_to_guess in allowed_words:
        guess = random.choice(allowed_words)
        
        print(f"Testing word: {word_to_guess} with random guess: {guess}")
        
        actual_clue = provide_clue(guess, word_to_guess)
        
        print(f"Guess: {guess}")
        print(f"Clue: {actual_clue}")
        print("-" * 30)
        
    print("\nRandom testing completed for all words!")

random_test_clue_generation()
