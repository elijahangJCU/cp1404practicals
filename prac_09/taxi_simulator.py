"""
Practical 9 Taxi Simulator
Estimated time to complete: 35 mins
Actual time taken to complete: 35 mins
"""


from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    bill_to_date = 0

    print("Let's drive!")
    menu = "q)uit, c)hoose taxi, d)rive"

    choice = ""
    while choice != "q":
        print(menu)
        choice = input(">>> ").lower()

        if choice == "c":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")

            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid taxi choice")

        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    current_taxi.start_fare()
                    current_taxi.drive(distance)
                    trip_cost = current_taxi.get_fare()
                    bill_to_date += trip_cost
                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                except ValueError:
                    print("Invalid distance")

        elif choice == "q":
            break

        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()
