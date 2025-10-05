"""
Practical 3
Files
"""


# 1
user_name = input("Enter your name: ")

file = open('name.txt', 'w')
file.write(user_name)
file.close()

# 2
file = open('name.txt', 'r')
name = file.read()
print(name)
file.close()

# 3
with open('numbers.txt', 'r') as file:
    num1 = int(file.readline())
    num2 = int(file.readline())
    print(num1 + num2)

# 4
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        number = int(line)
        total += number
    print(total)
