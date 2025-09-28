"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# Fixed Version:

score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:         # 90 or more is excellent
    print("Excellent")
elif score >= 50:       # 50 or more is pass
    print("Pass")
else:                   # Less than 50 is bad
    print("Bad")

