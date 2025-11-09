"""
Practical 6 Programming Language
Estimated time to complete: 15 mins
Actual time taken to complete: 15 mins
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

if __name__ == "__main__":
    test_language = ProgrammingLanguage("Test", "Dynamic", True, 1995)
    print(test_language)