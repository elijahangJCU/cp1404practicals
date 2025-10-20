
"""
Wimbledon Data Processor
Estimate: 40 minutes
Actual:
"""

FILENAME = "wimbledon.csv"


def main():
    """Read Wimbledon data and display champions and countries."""
    records = load_data(FILENAME)
    champion_to_wins = count_champions(records)
    countries = extract_countries(records)
    display_results(champion_to_wins, countries)


def load_data(filename):
    """Read data from CSV file and return a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip header
        records = [line.strip().split(",") for line in in_file]
    return records


def count_champions(records):
    """Count how many times each champion has won Wimbledon."""
    champion_to_wins = {}
    for record in records:
        champion = record[2]  # Column 2 contains the champion's name
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def extract_countries(records):
    """Extract a sorted set of unique countries (column 1: champion's country)."""
    countries = {record[1] for record in records}
    return sorted(countries)


def display_results(champion_to_wins, countries):
    """Display Wimbledon champions and countries neatly."""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion:20} {wins}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


main()

