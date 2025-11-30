"""
Practical 9 Taxi Test
Estimated time to complete: 10 mins
Actual time taken to complete:
"""

from taxi import Taxi

my_taxi = Taxi("Prius 1", 100)

# Trip 1
my_taxi.drive(40)
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare()}")

# Restart meter and go again
my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare()}")
