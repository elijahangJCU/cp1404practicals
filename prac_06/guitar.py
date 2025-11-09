"""
Practical 6 Guitar
Estimated time to complete: 20 mins
Actual time taken to complete: 30 mins
"""

class Guitar:
    def __init__(self, name=" ", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        return 2025 - self.year

    def is_vintage(self):
        return self.get_age() >= 50

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

if __name__ == "__main__":
    test_guitar = Guitar(name="hehe", year=2020, cost=100)
    age = test_guitar.get_age()
    print(test_guitar)
    print(f"{age} years old")
    if test_guitar.is_vintage():
        print("Test guitar is vintage")
    else:
        print("Test guitar is not vintage")
