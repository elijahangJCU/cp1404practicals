"""
Practical 6 Guitar Test
Estimated time to complete: 20 mins
Actual time taken to complete: 15 mins
"""

from guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another = Guitar("Another Guitar", 2013, 100)

print(
    f"Gibson L-5 CES get_age() - Expected 103. Got {gibson.get_age()}"
    f"\nAnothet Guitar get_age() - Expected 12. Got {another.get_age()}"
    f"\nGibson L-5 CES is_vintage() - Expected True. Got {gibson.is_vintage()}"
    f"\nAnother Guitar is_vintage() - Expected False. Got {another.is_vintage()}"
)