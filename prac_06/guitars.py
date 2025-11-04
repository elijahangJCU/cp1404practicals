"""
Practical 6 Playing the Guitars
Estimated time to complete: 35 mins
Actual time taken to complete: 45 mins
"""

from guitar import Guitar

guitars = []

print("My guitars!")

guitar_name = input("Name: ")

while guitar_name != "":
    year_made = int(input("Year: "))
    guitar_cost = float(input("Cost: "))
    guitars.append(Guitar(guitar_name, year_made, guitar_cost))
    print(f"{guitars[-1]} added. \n")
    guitar_name = input("Name: ")

print("These are my guitars:")

longest_name = max(len(guitar.name) for guitar in guitars)

for i, guitar in enumerate(guitars, 1):
    vintage_tag = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>{longest_name}} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_tag}")
