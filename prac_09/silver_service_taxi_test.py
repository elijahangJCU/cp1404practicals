"""
Practical 9 Silver Service Taxi Test
Estimated time to complete: 5 mins
Actual time taken to complete: 5 mins
"""

from silver_service_taxi import SilverServiceTaxi

# Create a fancy taxi
limo = SilverServiceTaxi("Limo", 100, 2)

# Start fresh
limo.start_fare()
limo.drive(18)

fare = limo.get_fare()
print(limo)
print(f"Fare: ${fare:.2f}")
