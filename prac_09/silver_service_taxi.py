"""
Practical 9 Silver Service Taxi
Estimated time to complete: 15 mins
Actual time taken to complete: 15 mins
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A more expensive taxi that includes fanciness and a flagfall."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness
        self.fanciness = fanciness

    def get_fare(self):
        return super().get_fare() + self.flagfall
