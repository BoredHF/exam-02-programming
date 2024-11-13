# Programming - Exam (Task 1)
#
# Prompts the user to input only positive integer numbers at the terminal (numbers with decimals, negative numbers, or characters will not be accepted).
# Assigns those numbers to a list, removes any duplicate numbers, and informs the user of the removed duplicates.
# Counts the number of unique numbers in the list.
# Calculates the product, range, and variance of the numbers.
# Identifies the even and odd numbers from the list and stores them in separate lists.
# If the list of even numbers is empty, print a message saying "No even numbers were provided."
# If the list of odd numbers is empty, print a message saying "No odd numbers were provided."
# Prints all the above information to the terminal.
from html.parser import starttagopen

# The script should start and end without issues. There should be no 'crashing' or 'unhandled exceptions' due to erroneous input.
# The use of any built-in method that performs the above operations is not allowed.
# Importing of modules is also not allowed.
# The code must be commented, including header comments and inline comments following the PEP 8 style.
# Consideration must be given to the naming convention of variables and function names.




# Ask the user for input of ONLY positive integers
# Make sure each numbers with decimals, negative numbers, or characters will not be accepted and prompt the user about it
# Remove all duplicated numbers and inform the user about the removal

# Create a new list of the numbers
# Check the size (unique numbers in the list) if there are no duplicates, all numbers would be classed as unique

# Calculate the product (multiplying), range (largest and smallest numbers), Variance(mean - list / amount)
# Create two lists; One even, and one Odd
# Check if the list is not Null, if they are inform the user
# Output all lists, and information to the user



userStillInputting = True  # Tracks if the user is still inputting numbers

userInputNumbers = []   # List to store all user numbers
formattedInputNumbers = []  # List to store all user numbers without duplicates

odd_numbers = []
even_numbers = []


def remove_duplicates(nums):
    """Remove duplicates by manually adding each unique value to a new list."""
    print("-- Removing all Duplicates --")
    formatted_input_numbers = []  # new list for unique numbers

    for num in nums:
        if num not in formatted_input_numbers:
            formatted_input_numbers.append(num)  # Add only if not already in the list
    print(f"You have {len(formatted_input_numbers)} unique numbers.")
    return formatted_input_numbers


def separate_even_odd(numbers):
    """Separate a list of numbers into even and odd lists."""
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

def calculate_product(nums):
    total = 0
    for num in nums:
        total *= num

def input_one_by_one():
    global userStillInputting

    while userStillInputting:
        if userInputNumbers is not None:
            print("Your numbers: " + str(userInputNumbers))

        try:
            userInput = int(input("\nPlease enter a positive integer: \n> "))

            if userInput <= 0:
                print("Only positive integers are allowed. Please try again.")
                continue  # Skip if the value doesn't match the notes.
            userInputNumbers.append(userInput)

            userOption = int(input("Would you like to add more numbers? [1 = Yes, 2 = No] \n> "))
            if userOption == 2:
                userStillInputting = False  # Exit the loop if the user is done, and starts the next stage

        except ValueError:  # Handles with unhandled exceptions
            print("Invalid input. Please enter a whole positive number only.")

def startPrompt():
    print("    TASK 1    ")
    print("   Albert Roche  \n")
    print("How would you like to implement the numbers?")
    print("\n 1. One by One")
    print("\n 2. All Numbers at Once")
    print("\n 3. Exit")
    try:
        userOptionInput = int(input("\n> "))
    except ValueError:
        print("Please enter an option.")
    if userOptionInput == 1:
        # Enter input one by one
        input_one_by_one()
    else:
        print("I have don't that yet lol")




startPrompt()
userInputNumbers.sort()
print("\n   Stage 1")
print("Sorted List: " + str(userInputNumbers))
formattedInputNumbers = remove_duplicates(userInputNumbers) # Replaces old formatted numbers with the non dupe
print("Removed Dupes: " + str(formattedInputNumbers))

separate_even_odd(formattedInputNumbers)    # Fills both odd, even lists with their values.

print("\n   Stage 2")
print("Odd Numbers: " + str(odd_numbers))
print("Even Number: " + str(even_numbers))

print("\n   Stage 3")
print("Product: " + str(calculate_product(formattedInputNumbers)))

