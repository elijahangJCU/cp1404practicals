"""
Shop Calculator
"""

total_price = 0
DISCOUNT_MIN_SPEND = 100
DISCOUNT_RATE = 0.90

number_of_items = int(input("Number of items: "))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item

if total_price > DISCOUNT_MIN_SPEND:
    final_price = total_price * DISCOUNT_RATE
else:
    final_price = total_price

print(f"Total price for {number_of_items} items is ${final_price:.2f}")