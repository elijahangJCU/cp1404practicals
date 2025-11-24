"""
Practical 9 Unreliable Car Test
Estimated time to complete: 15 mins
Actual time taken to complete: 10 mins
"""

from unreliable_car import UnreliableCar

# Create an unreliable car
bad_car = UnreliableCar("Old Bomb", 100, 30)

total_distance = 0

# Try driving it 100 times
for attempt in range(100):
    driven = bad_car.drive(10)
    total_distance += driven
    print(f"Attempt {attempt + 1}: Drove {driven}km | Fuel: {bad_car.fuel}")

print("\nTotal distance driven:", total_distance)
