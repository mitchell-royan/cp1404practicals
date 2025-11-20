"""
CP1404 - Practical 09
Unreliable Car Class
"""

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Unreliable version of a car"""

    def __init__(self, name, fuel, reliability):
        """Initialise"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive car only if, random number < reliability"""
        chance = randint(1, 100)
        if chance < self.reliability:
            return super().drive(distance)
        return 0
        