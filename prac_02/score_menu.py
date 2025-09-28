"""
Practical 2
Score Menu Program
"""


MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    score = get_valid_score()
    print_menu()
    choice = get_choice()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(evaluate_score(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print_menu()
        choice = get_choice()
    print("Farewell.")


def get_valid_score():
    """Prompt the user for a valid score (0-100 inclusive)."""
    while True:
        try:
            score = float(input("Enter score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Must be between 0 and 100.")
        except ValueError:
            print("Invalid input; enter a number.")


def evaluate_score(score):
    """Evaluate the score and return a result string."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Print as many stars as the integer part of the score."""
    print("*" * int(score))


def print_menu():
    print(MENU)


def get_choice():
    return input(">>> ").strip().upper()


if __name__ == "__main__":
    main()