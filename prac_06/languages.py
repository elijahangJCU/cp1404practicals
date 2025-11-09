"""
Practical 6 Languages
Estimates time to complete: 20 mins
Actual time taken to complete: 25 mins
"""

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", "True", 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
java = ProgrammingLanguage("Java", "Static", "True", 1995)
c_plusplus = ProgrammingLanguage("C++", "Static", "False", 1983)
print(python)
print(ruby)
print(visual_basic)
print(java)
print(c_plusplus)

languages = [python, ruby, visual_basic, java, c_plusplus]

print("\nThe dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
