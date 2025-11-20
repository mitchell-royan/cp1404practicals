"""
CP1404 - Practical 09
Silver service taxi class
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Silver Service Taxi Class"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise Class"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        fare = self.flagfall + super().get_fare()
        return f"${fare:.2f}"
