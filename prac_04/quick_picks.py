"""
CP1404 Practical 04 - Quick Picks
"""

import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    """Asks user for number of picks and display random numbers"""
    number_of_picks = int(input("How many quick picks? "))
    while number_of_picks < 0:
        print("Please enter a positive number.")
        number_of_picks = int(input("How many quick picks? "))

    for i in range(number_of_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_PICK):
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            while number in quick_pick:
                number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()

        print(" ".join(f"{number:2}" for number in quick_pick))


main()
