"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

SALES_TARGET = 1000
LOOP_THRESHOLD = 0

sales = float(input("Enter sales (-1 to quit): $"))

while sales >= LOOP_THRESHOLD:
    if sales <  SALES_TARGET:
        bonus = (10/100) * sales
        print(f"Congratulations, your bonus is ${bonus:.2f}")
    else:
        bonus = (15/100) * sales
        print(f"Congratulations, your bonus is ${bonus:.2f}")

    sales = float(input("Enter sales (-1 to quit): $"))

print("Thank you for using our program.")