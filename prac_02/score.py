"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

def main():
    score = get_score()
    result = evaluate_score(score)
    print(f"User score: {score}")
    print(result)
    random_score = random.randint(0, 100)
    random_result = evaluate_score(random_score)
    print(f"Random score: {random_score}")
    print(random_result)


def get_score():
    """Prompt the user for a score and return it as a float."""
    return float(input("Enter score: "))


def evaluate_score(score):
    """Return the evaluation string for the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == "__main__":
    main()