"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Calculates the monthly cumulative totals for incomes and displays them"""
    incomes = []
    num_of_months = int(input("How many months? "))

    for month in range(1, num_of_months + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)

    print_report(incomes, num_of_months)


def print_report(incomes, num_of_months):
    """Prints out the monthly cumulative totals for incomes"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()