"""
Practical 2
password stars
"""

def main():
    password = get_password()
    print_asterisks(password)

def get_password():
    return input("Enter password: ")

def print_asterisks(password):
    length = len(password)
    print("*" * length)

main()
