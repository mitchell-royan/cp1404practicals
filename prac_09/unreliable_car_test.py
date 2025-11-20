"""
CP1404 - Practical 09
Test the unreliable car class
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    reliable_car = UnreliableCar("Good", 100, 90)
    unreliable_car = UnreliableCar("Unreliable", 100, 0)

    for i in range(1, 12):
        print(f"Attempting to drive {i}km:")
        print(f"{reliable_car.name:12} drove {reliable_car.drive(i):2}km")
        print(f"{unreliable_car.name:12} drove {unreliable_car.drive(i):2}km")

    print(reliable_car)
    print(unreliable_car)


if __name__ == "__main__":
    main()
