"""
Practical 7 My Guitars
Estimated time to complete: 35 mins
Actual time taken to complete:
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
    for guitar in guitars:
        print(f"{guitar.name:20} ({guitar.year}), worth ${guitar.cost:.2f}")

def main():
    guitars = load_guitars()
    display_guitars(guitars)
    guitars.sort(key=lambda g: g.year)
    print("Sorted by year:")
    display_guitars(guitars)

if __name__ == "__main__":
    main()
