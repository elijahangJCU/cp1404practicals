"""
Practical 4
Quick Picks
"""

import random
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


picks = int(input("How many number of picks?: "))

for i in range(picks):
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)

    quick_pick.sort()
    print(" ".join(f"{number:2}" for number in quick_pick))