"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}

longest_code = max(len(code) for code in CODE_TO_NAME)

for code, name in CODE_TO_NAME.items():
    print(f"{code:<{longest_code}} is {name:<2}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
        state_code = input("Enter short state: ").upper()
    except KeyError:
        print("Invalid short state")
        state_code = input("Enter short state: ").upper()
