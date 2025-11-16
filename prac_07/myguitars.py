"""
Practical 7 My Guitars
Estimated time to complete: 35 mins
Actual time taken to complete: 40 mins
"""

from guitar import Guitar

def load_guitars():
    guitars = []
    with open("guitars.csv", "r") as file:
        for line in file:
            name, year, cost = line.strip().split(",")
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def display_guitars(guitars):
    print("These are my guitars:")
    if not guitars:
        print("No guitars found.")
        return
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:20} ({guitar.year}), worth ${guitar.cost:10,.2f}")

def add_new_guitars(guitars):
    print("Add new guitars:")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}), worth ${cost:,.2f} added.")
        name = input("Name: ")
    return guitars

def save_guitars(guitars):
    with open("guitars.csv", "w") as file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=file)
    print(f"{len(guitars)} guitars saved to guitars.csv")

def main():
    guitars = load_guitars()
    display_guitars(guitars)
    guitars.sort(key=lambda g: g.year)
    print("Sorted by year:")
    display_guitars(guitars)
    add_new_guitars(guitars)
    save_guitars(guitars)

if __name__ == "__main__":
    main()
