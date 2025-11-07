"""
CP1404 - Practical 07
"""

from guitar import Guitar


def main():
    guitars = load_guitars("guitars.csv")
    print("Guitars loaded:")
    display_guitars(guitars)
    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)


def load_guitars(filename):
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(",")
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


if __name__ == '__main__':
    main()
