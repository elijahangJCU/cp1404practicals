"""
Practical 5
Hex Colours Dictionary (https://www.color-hex.com/color-names.html)
"""

# This open file section helps me save time and effort when creating a dict with all the colour
# names and their codes.
HEX_COLOURS = {}
with open("hex_colour_options", "r") as file:
    for line in file:
        clean_line = line.split()
        if len(clean_line) > 1:
            colour_name = " ".join(clean_line[:-1])
        else:
            colour_name = clean_line[0]
        HEX_COLOURS[colour_name] = clean_line[-1]

longest_name = max(len(colour) for colour in HEX_COLOURS.keys())

for colour, code in HEX_COLOURS.items():
    print(f"{colour:<{longest_name}} is {code:>2}")

colour = input("Enter colour: ")
while colour != "":
    for name, code in HEX_COLOURS.items():
        if name.lower() == colour.lower():
            print(f"{name:<2} is {code:>2}")
            break
    else:
        print("Invalid colour")
    colour = input("Enter colour: ")



