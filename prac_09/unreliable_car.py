"""
Practical 9 Unreliable Car
Estimated time to complete: 15 mins
Actual time taken to complete: 12 mins
"""

import random
from car import Car


class UnreliableCar(Car):
    """A car that sometimes does not drive, based on reliability."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if a random number is less than reliability."""
        chance = random.uniform(0, 100)

        if chance < self.reliability:
            return super().drive(distance)
        else:
            return 0
