"""
CP1404 Practical 05 - Wimbledon
Estimate: 35 Minutes
Actual: 45 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Read data file and displays details about champion win counts and countries"""
    records = load_file_data(FILENAME)
    champion_to_wins, countries = process_records(records)
    display_results(champion_to_wins, countries)


def process_records(records):
    """Process records to count wins and countries"""
    champion_to_wins = {}
    countries = set()
    for record in records:
        countries.add(record[1])  # Country at index 1 (from CSV file)
        try:
            champion_to_wins[record[2]] += 1  # Champion at index 2 (from CSV file)
        except KeyError:
            champion_to_wins[record[2]] = 1
    return champion_to_wins, countries


def display_results(champion_to_wins, countries):
    """Display champions win counts and sorted list of countries"""
    print("Wimbledon Champions: ")
    for champion, wins in champion_to_wins.items():
        print(champion, wins)
    print(f"\nThese {len(countries)} countries have won Wimbledon")
    print(", ".join(sorted(countries)))


def load_file_data(filename):
    """Loads data from wimbledon CSV file"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
