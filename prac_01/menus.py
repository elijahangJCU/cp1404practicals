"""
Menus
"""

MENU = (
        "(H)ello"
        "\n(G)oodbye"
        "\n(Q)uit"
        )

username = input("Enter name: ")
print(MENU)
user_choice = input(">>> ").lower()

while user_choice != "q":
    if user_choice == "h":
        print("Hello", username)
    elif user_choice == "g":
        print("Goodbye", username)
    else:
        print("Invalid choice")
    print(MENU)
    user_choice = input(">>> ").lower()
print("Finished")