"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Set is_finished to True after successful conversion
    except ValueError:  # Catch only ValueError for invalid integer input
        print("Please enter a valid integer.")
print("Valid result is:", result)