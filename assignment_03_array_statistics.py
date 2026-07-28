# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# Ask user for the number of numbers
# Ask numbers from the user
# Find sum, Average, Max and Min without using the built-in functions

number_of_num = int(input("How many numbers? "))

if number_of_num <= 0:
    print("Error: Number of numbers must be a positive integer.")

else:
    user_numbers = []

    for i in range(1, number_of_num + 1):
        ask_user = int(input(f"Enter number {i}: "))
        user_numbers.append(ask_user)

    # print(user_numbers)

    def sum_numbers(user_numbers):
        total = 0
        for i in range(len(user_numbers)):
            total = total + user_numbers[i]

        return total

    total = sum_numbers(user_numbers)
    print(f"Sum: {total}")

    def average_numbers(user_numbers):
        total = sum_numbers(user_numbers)
        mean = total / number_of_num

        return mean

    mean = average_numbers(user_numbers)
    print(f"Average: {mean}")

    def max_numbers(user_numbers):
        maximum = user_numbers[0]
        for i in range(len(user_numbers)):
            if maximum < user_numbers[i]:
                maximum = user_numbers[i]

        return maximum

    maximum = max_numbers(user_numbers)
    print(f"Maximum: {maximum}")

    def min_numbers(user_numbers):
        minimum = user_numbers[0]
        for i in range(len(user_numbers)):
            if minimum > user_numbers[i]:
                minimum = user_numbers[i]

        return minimum

    minimum = min_numbers(user_numbers)
    print(f"Minimum: {minimum}")
