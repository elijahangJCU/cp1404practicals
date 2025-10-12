"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

subject_info = []

with open(FILENAME, 'r') as subject_data:
    for i in subject_data:
        line = i.strip().split(",")
        line[2] = int(line[2])
        subject_info.append(line)

for r in subject_info:
    print(f"{r[0]} is taught by {r[1]} and has {r[2]} students")