"""
Emails
Estimate: 35 minutes
Actual: 40 minutes
"""

email_input = input("Email: ").lower()

emails_and_names = {}

while email_input != "":
    email_characters = email_input.split('@')[0]
    if "." in email_characters:
        name = " ".join(email_characters.split(".")).title()
    else:
        name = email_characters.title()

    name_confirmation = input(f"Is your name {name}? (Y/N): ").lower()

    if name_confirmation in ("y", "yes"):
        emails_and_names[email_input] = name
    elif name_confirmation in ("n", "no"):
        ask_for_name = input("Name: ")
        emails_and_names[email_input] = ask_for_name

    email_input = input("Email: ").lower()

for email, name in emails_and_names.items():
    print(f"{name} ({email})")







