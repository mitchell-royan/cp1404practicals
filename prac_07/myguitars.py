"""
CP1404 - Practical 07
"""

from guitar import Guitar


def main():
    guitars = load_guitars("guitars.csv")
    print("Guitars loaded:")
    display_guitars(guitars)
    print("Enter your new guitars:")
    guitars.extend(get_new_guitars())
    guitars.sort()
    save_guitars("guitars.csv", guitars)
    print("\nGuitars saved to guitars.csv")
    print("Here are all guitars (sorted by year):")
    display_guitars(guitars)


def load_guitars(filename):
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(",")
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def get_new_guitars():
    new_guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitars.append(Guitar(name, year, cost))
        print(f"{name} added to list of guitars")
        name = input("Name: ")
    return new_guitars


def save_guitars(filename, guitars):
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


if __name__ == '__main__':
    main()
