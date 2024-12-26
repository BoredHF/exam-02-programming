# Task 1 - Albert Roche (29191815)
# This script performs the following:
# 1. Accepts only positive integers as input.
# 2. Removes duplicates and informs the user.
# 3. Calculates product, range, and variance of the numbers.
# 4. Separates even and odd numbers into separate lists and handles edge cases.

user_input_numbers = []   # List to store all user inputs
even_numbers = [] # List to store all even numbers
odd_numbers = [] # List to store all odd numbers
amount_unique_numbers = 0


def remove_duplicates(numbers):
    """Remove duplicates and return a list of unique numbers."""
    global amount_unique_numbers 
    startTotal = len(numbers)
    unique_numbers = []
    for num in numbers: # Loops thru all numbers, if they aren't in the new list, add them
        if num not in unique_numbers:
            unique_numbers.append(num)
    amount_unique_numbers = len(unique_numbers) # Adds the amount of unique numbers to a var
    removedTotal = startTotal - amount_unique_numbers
    print(f"Removed {removedTotal} numbers from your list.")
    return unique_numbers


def separate_even_odd(numbers):
    """Separate numbers into even and odd lists."""
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)


def calculate_product(numbers):
    """Calculate the product of all numbers in the list."""
    product = 1
    for num in numbers:
        product *= num
    return product


def calculate_mean(numbers):
    """Calculate the mean of the list manually."""
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return total / count


def calculate_variance(numbers):
    """Calculate the variance of the list manually."""
    mean = calculate_mean(numbers)
    squared_differences = 0
    count = 0
    for num in numbers:
        squared_differences += (num - mean) ** 2
        count += 1
    return squared_differences / count


def calculate_range(numbers):
    """Calculate the range of numbers in the list manually."""
    return numbers[-1] - numbers[0] # Grabs the last index, and first from an already sorted list.


def input_numbers():
    """Prompt the user to input positive integers."""
    global user_input_numbers
    while True:
        try:
            print(f"Numbers: {user_input_numbers}" if user_input_numbers else "Nothing..")
            user_input = int(input("Please enter a positive integer: \n> "))
            if user_input <= 0:
                print("Only positive integers are allowed. Please try again.")
                continue
            user_input_numbers.append(user_input)
            print(f"Added {user_input} to the list.")
        except ValueError:
            print("Invalid input. Please enter a whole positive number only.")

        try:
            option = int(input("Would you like to add more numbers? [1 = Yes, 2 = No] \n> "))
            if option == 2:
                break
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")


# Main Execution
print("Task 1 - Albert Roche")
input_numbers()


print("-- Program --")
print(f"Your numbers: \n{user_input_numbers}")
user_input_numbers.sort()
user_input_numbers = remove_duplicates(user_input_numbers)
separate_even_odd(user_input_numbers)

print("\nResults:")
print(f"Sorted Numbers: {user_input_numbers}")
print(f"Unique Numbers: {amount_unique_numbers}")
print(f"Odd Numbers: {odd_numbers}" if odd_numbers else "No Odd Numbers were provided.")
print(f"Even Numbers: {even_numbers}" if even_numbers else "No Even Numbers were provided.")
print(f"Product: {calculate_product(user_input_numbers)}")
print(f"Range: {calculate_range(user_input_numbers)}")
print(f"Variance: {calculate_variance(user_input_numbers)}")