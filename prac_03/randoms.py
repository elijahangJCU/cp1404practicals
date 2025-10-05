"""
Practical 3
Randoms
"""

import random

print(random.randint(5, 20))  # Could be any integer from 5 to 20 inclusive, so smallest is 5 and largest is 20.

print(random.randrange(3, 10, 2))  # Could be 3, 5, 7, or 9. 4 will never appear because step is 2 starting at 3.

print(random.uniform(2.5, 5.5))  # Could be any float between 2.5 and 5.5 inclusive, so smallest is 2.5 and largest is 5.5.

print(random.randint(1, 100))  # Could be any integer from 1 to 100 inclusive.
